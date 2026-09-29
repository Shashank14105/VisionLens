# VisionLens

## Computer Vision Based Campus Lost-and-Found Visual Matching System

> **VITyarthi** | Computer Vision Project

---

## Student Information

| Field | Details |
|---|---|
| **Name** | Shashank Kumar |
| **Registration Number** | 24BAI10032 |
| **Slot** | F11+F12 |
| **Project** | VisionLens |
| **Course** | Computer Vision |
| **Platform** | VITyarthi |
| **Date of Submission** | 17 September 2026 |

---

## Project Overview

**VisionLens** is a lost-and-found image search project developed for the Computer Vision course. 
The user provides a photograph of a lost item, and the application compares it with 
images available in our found-item dataset.
Instead of manually searching through photographs of found objects, a user can upload an image of a lost item. VisionLens extracts visual features from the uploaded image and compares them with a gallery of found-item images.

### Core Workflow

```text
User Image
    ↓
Image Validation
    ↓
Image Preprocessing
    ↓
ResNet-18 Feature Extraction
    ↓
Cosine Similarity
    ↓
Similarity Ranking
    ↓
Top-5 Matching Results
```
## Objectives

### The main objectives of VisionLens are:

#### Allow users to upload an image of a lost item.
#### Validate and preprocess the uploaded image.
#### Extract meaningful visual features using a pretrained CNN.
#### Compare the query image with a gallery of found-item images.
---

## Module 1 Dataset Loader
File: cv/dataset_loader.py

Description
Loads the dataset's train, valid, and test splits and reads the corresponding _classes.csv files.

## Module 2 — Feature Extractor
File: cv/feature_extractor.py

Description
Uses a pretrained ResNet-18 convolutional neural network to extract visual features from images.

I removed the last classification layer because I do not need ResNet-18 to predict ImageNet classes. 
For this project, I need the intermediate representation of an image so that it can be compared 
with the images stored in the gallery.

## Module 3 — Similarity Engine
File: cv/similarity.py

Description
Calculates the similarity between two image feature vectors.

VisionLens uses cosine similarity to measure how close two visual representations are.

Because the feature vectors are normalized, their dot product is equivalent to cosine similarity.

## Module 4 — Search Engine
File: cv/search_engine.py

Description
Coordinates the complete visual retrieval process.

The Search Engine:

Loads or builds the feature gallery.
Extracts features from the query image.
Compares the query against gallery images.
Calculates similarity scores.
Sorts the results.
Returns the Top-K matches.

## Module 5 — Web Application
Description
Provides the user-facing interface for VisionLens.

The application accepts an image from the user and passes it through the computer vision pipeline.

The resulting visually similar found items are then displayed to the use

## Module 6 — Testing
Directory: tests/

Description
Contains automated tests used to verify important parts of the VisionLens system.

The testing process checks that the major project components behave as expected.

---
## Features

### 1. Image Upload

Allows the user to provide an image of the lost item.

### 2. Image Validation

Checks whether the supplied input can be processed as a valid image.

### 3. Image Preprocessing

The uploaded image is converted into the format expected by the pretrained computer vision model.

### 4. Feature Extraction

VisionLens uses a pretrained **ResNet-18** model to convert an image into a numerical feature representation.

### 5. Visual Similarity Search

The extracted query feature is compared against stored gallery features using **cosine similarity**.

### 6. Top-5 Matching

The system sorts the gallery according to similarity score and returns the five most visually similar images.

### 7. Cached Feature Gallery

Features extracted from the training gallery are saved locally so that the complete gallery does not need to be processed every time the application starts.

### 8. Modular Architecture

The project separates dataset loading, feature extraction, similarity calculation, search, application logic, and testing into different modules.

---
### Step 1 — Clone the Repository
    git clone https://github.com/Shashank14105/VisionLens
    cd VisionLens
    
### Step 2 — Install Dependencies
    pip install torch torchvision numpy pandas pillow pytest
    
### Step 3 — Add the Dataset
    Place the dataset inside the expected dataset directory with the required _classes.csv files.
    
### Step 4 — Generate the Feature Gallery
    Run the feature extraction process to generate the cached gallery:
    python cv/feature_extractor.py
    The extracted gallery features are stored locally in:
    gallery.pt
    This prevents ResNet-18 features from being recalculated every time the search process is executed.

### Step 5 — Perform Image Search
    Provide a query image to the search pipeline and compare it against the cached gallery.
    The search engine extracts the query image features, calculates cosine similarity against the gallery, sorts the results, and returns the Top-K matches.

### Step 6 — Run Tests
    Run the automated tests using:
    pytest
---

## Project Structure


```
                 ┌──────────────────┐
                 │      User        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Image Validation │
                 │ & Preprocessing  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ ResNet-18 Feature│
                 │    Extractor     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Similarity Engine│
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       ┌──────────────┐       ┌──────────────┐
       │   Feature    │       │ Image Gallery│
       │   Gallery    │       │              │
       └──────────────┘       └──────────────┘
              │                       │
              └───────────┬───────────┘
                          ▼
                 ┌──────────────────┐
                 │ Similarity Ranking│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Top-5 Results  │
                 └──────────────────┘
```
## Challenges

1. The dataset labels were provided through `_classes.csv`, so I had to identify the filename column and convert the remaining columns into a list of active labels.

2. Initially, I had to understand how ResNet-18 could be used for retrieval instead of normal image classification.

3. I selected cosine similarity because the extracted feature vectors can be normalized and compared using their direction.

4. Extracting ResNet features for every gallery image whenever the application starts would be slow, so I saved the extracted features in `gallery.pt`.

5. I separated dataset loading, feature extraction, similarity calculation, and searching into different Python modules to make debugging easier.

---

## License

This project was submitted as part of the **Computer Vision at VIT Bhopal University**.
All scripts and documentation are original work by **SHASHANK KUMAR**.

---



