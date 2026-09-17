from pathlib import Path

from cv.feature_extractor import FeatureExtractor


class SimilarityEngine:

    @staticmethod
    def cosine_similarity(feature1, feature2):
        """
        Calculate cosine similarity between two image feature vectors.
        """
        similarity = feature1 @ feature2

        return similarity.item()


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[1]
    dataset_path = (
        project_root
        / "data"
        / "Lost-Found-Items.v1i.multiclass"
        / "train"
    )

    # Get two image files
    images = []

    for extension in ["*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"]:
        images.extend(dataset_path.glob(extension))

    if len(images) < 2:
        raise RuntimeError("Not enough images found in dataset.")

    image1 = images[0]
    image2 = images[1]

    print("Image 1:", image1.name)
    print("Image 2:", image2.name)

    extractor = FeatureExtractor()

    feature1 = extractor.extract(image1)
    feature2 = extractor.extract(image2)

    score = SimilarityEngine.cosine_similarity(
        feature1,
        feature2
    )

    print(f"\nCosine similarity: {score:.4f}")