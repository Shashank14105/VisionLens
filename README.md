# VisionLens

## Computer Vision Based Campus Lost-and-Found Visual Matching System

> **VITyarthi** | Computer Vision Project

---

## Student Information

| Field | Details |
|---|---|
| **Name** | Shashank Kumar |
| **Registration Number** | 24BAI10032 |
| **Slot** | B22 |
| **Project** | VisionLens |
| **Course** | Computer Vision |
| **Platform** | VITyarthi |
| **Date of Submission** | 2026 |

---

## Project Overview

**VisionLens** is a computer vision based visual matching system designed to assist in finding lost items on a campus.

Instead of manually searching through photographs of found objects, a user can upload an image of a lost item. VisionLens extracts visual features from the uploaded image and compares them with a gallery of found-item images.

The system then ranks the images according to visual similarity and displays the **Top-5 most visually similar matches**.

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

# VisionLens

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

## Project Structure

```text
VisionLens/
│
├── README.md
├── statement.md
├── requirements.txt
│
├── app/
│   └── ...
│
├── cv/
│   ├── dataset_loader.py
│   ├── feature_extractor.py
│   ├── similarity.py
│   └── search_engine.py
│
├── data/
│   └── diagrams/
│       ├── 01_architecture.png
│       ├── 02_workflow.png
│       ├── 03_use_case.png
│       ├── 04_class_component.png
│       └── 05_sequence.png
│
├── features/
│   └── gallery.pt
│
├── tests/
│   └── test_visionlens.py
│
└── ...
```
```
                 ┌──────────────────┐
                 │      User        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Flask Web UI   │
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

1. Handling a multi-label dataset stored through CSV files.

2. Understanding how pretrained CNN models can be used for feature extraction.

3. Selecting an appropriate similarity metric.

4. Managing feature extraction for a relatively large image gallery.

5. Designing a modular architecture within a limited project timeline.

6. Handling dataset files without unnecessarily modifying the original dataset structure.

---

## License

This project was submitted as part of the **Open Source Software Course at VIT Bhopal University**.
All scripts and documentation are original work by **SHASHANK KUMAR**.

---



