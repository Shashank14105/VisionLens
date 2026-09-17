import pandas as pd
from pathlib import Path


class DatasetLoader:
    def __init__(self, dataset_root):
        self.dataset_root = Path(dataset_root)

    def load_split(self, split):
        split_path = self.dataset_root / split
        csv_path = split_path / "_classes.csv"

        if not split_path.exists():
            raise FileNotFoundError(f"Split folder not found: {split_path}")

        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")

        df = pd.read_csv(csv_path)

        # First column contains image filenames
        filename_column = df.columns[0]

        # Remaining columns are multi-label classes
        label_columns = list(df.columns[1:])

        records = []

        for _, row in df.iterrows():
            filename = str(row[filename_column])

            # A label is active when its value is 1
            labels = [
                label
                for label in label_columns
                if row[label] == 1
            ]

            image_path = split_path / filename

            records.append({
                "filename": filename,
                "image_path": image_path,
                "labels": labels
            })

        return records


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    dataset_root = project_root / "data" / "Lost-Found-Items.v1i.multiclass"

    loader = DatasetLoader(dataset_root)

    for split in ["train", "valid", "test"]:
        records = loader.load_split(split)

        print(f"\n{split.upper()}")
        print("-" * 40)
        print("Images:", len(records))

        if records:
            print("Example:")
            print("Filename:", records[0]["filename"])
            print("Labels:", records[0]["labels"])