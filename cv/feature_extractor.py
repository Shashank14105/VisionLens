import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image


class FeatureExtractor:
    def __init__(self):
        # Use CPU for maximum compatibility on a coursework laptop
        self.device = torch.device("cpu")

        # Load pretrained ResNet-18
        weights = models.ResNet18_Weights.DEFAULT
        model = models.resnet18(weights=weights)

        # Remove the final classification layer
        self.model = nn.Sequential(*list(model.children())[:-1])

        self.model = self.model.to(self.device)
        self.model.eval()

        # Use the preprocessing expected by the pretrained model
        self.transform = weights.transforms()

    def extract(self, image_path):
        image = Image.open(image_path).convert("RGB")

        image_tensor = self.transform(image)
        image_tensor = image_tensor.unsqueeze(0)
        image_tensor = image_tensor.to(self.device)

        with torch.no_grad():
            features = self.model(image_tensor)

        # Convert from [1, 512, 1, 1] to [512]
        features = features.squeeze()

        # Normalize the feature vector
        features = features / features.norm()

        return features


if __name__ == "__main__":
    print("Feature extractor initialized successfully.")
    