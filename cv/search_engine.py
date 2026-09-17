from pathlib import Path

import torch

from cv.dataset_loader import DatasetLoader
from cv.feature_extractor import FeatureExtractor
from cv.similarity import SimilarityEngine


class SearchEngine:

    def __init__(self, dataset_root):
        self.dataset_root = Path(dataset_root)

        self.loader = DatasetLoader(self.dataset_root)
        self.extractor = FeatureExtractor()
        self.similarity = SimilarityEngine()

        self.gallery = []

        self.feature_file = Path("features/gallery.pt")

    def build_gallery(self):
        """
        Extract features from all training images
        and save them to disk.
        """

        records = self.loader.load_split("train")

        print(f"Processing {len(records)} training images...")

        self.gallery = []

        for index, record in enumerate(records, start=1):

            try:
                features = self.extractor.extract(
                    record["image_path"]
                )

                self.gallery.append({
                    "filename": record["filename"],
                    "image_path": str(record["image_path"]),
                    "labels": record["labels"],
                    "features": features
                })

                if index % 100 == 0:
                    print(
                        f"Processed {index}/{len(records)} images"
                    )

            except Exception as error:
                print(
                    f"Skipping {record['filename']}: {error}"
                )

        self.feature_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        torch.save(
            self.gallery,
            self.feature_file
        )

        print(
            f"\nGallery ready: {len(self.gallery)} images"
        )

        print(
            f"Features saved to: {self.feature_file}"
        )

    def load_gallery(self):
        """
        Load previously extracted features.
        """

        if not self.feature_file.exists():
            print("No saved gallery found.")
            return False

        self.gallery = torch.load(
            self.feature_file,
            weights_only=False
        )

        print(
            f"Loaded gallery: {len(self.gallery)} images"
        )

        return True

    def search(self, query_image, top_k=5):
        """
        Find the most visually similar training images.
        """

        if not self.gallery:
            raise RuntimeError(
                "Gallery is empty. Build or load the gallery first."
            )

        query_features = self.extractor.extract(
            query_image
        )

        results = []

        for item in self.gallery:

            score = self.similarity.cosine_similarity(
                query_features,
                item["features"]
            )

            results.append({
                "filename": item["filename"],
                "image_path": item["image_path"],
                "labels": item["labels"],
                "score": score
            })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:top_k]


if __name__ == "__main__":

    dataset_root = Path(
        "data/Lost-Found-Items.v1i.multiclass"
    )

    engine = SearchEngine(dataset_root)

    # Build gallery if it does not already exist.
    if not engine.load_gallery():
        engine.build_gallery()

    test_images = list(
        (dataset_root / "test").glob("*.jpg")
    )

    if not test_images:
        raise RuntimeError(
            "No test images found."
        )

    query_image = test_images[0]

    print("\nQuery image:")
    print(query_image.name)

    results = engine.search(
        query_image,
        top_k=5
    )

    print("\nTop 5 matches:")
    print("-" * 60)

    for rank, result in enumerate(results, start=1):

        print(
            f"{rank}. "
            f"{result['filename']} | "
            f"Score: {result['score']:.4f} | "
            f"Labels: {result['labels']}"
        )