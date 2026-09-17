from pathlib import Path

from cv.dataset_loader import DatasetLoader
from cv.feature_extractor import FeatureExtractor
from cv.similarity import SimilarityEngine


DATASET_ROOT = Path(
    "data/Lost-Found-Items.v1i.multiclass"
)


def test_dataset_loader():
    loader = DatasetLoader(DATASET_ROOT)

    records = loader.load_split("test")

    assert len(records) > 0
    assert "filename" in records[0]
    assert "labels" in records[0]
    assert records[0]["image_path"].exists()


def test_feature_extraction():
    loader = DatasetLoader(DATASET_ROOT)
    records = loader.load_split("test")

    extractor = FeatureExtractor()

    features = extractor.extract(
        records[0]["image_path"]
    )

    assert features.shape == (512,)


def test_cosine_similarity():
    extractor = FeatureExtractor()
    loader = DatasetLoader(DATASET_ROOT)

    records = loader.load_split("test")

    feature1 = extractor.extract(
        records[0]["image_path"]
    )

    feature2 = extractor.extract(
        records[0]["image_path"]
    )

    similarity = SimilarityEngine.cosine_similarity(
        feature1,
        feature2
    )

    # An image compared with itself should be almost 1.
    assert similarity > 0.99


def test_different_images_produce_similarity_score():
    loader = DatasetLoader(DATASET_ROOT)
    extractor = FeatureExtractor()

    records = loader.load_split("test")

    feature1 = extractor.extract(
        records[0]["image_path"]
    )

    feature2 = extractor.extract(
        records[1]["image_path"]
    )

    similarity = SimilarityEngine.cosine_similarity(
        feature1,
        feature2
    )

    assert -1.0 <= similarity <= 1.0