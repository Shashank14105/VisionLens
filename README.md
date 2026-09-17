# VisionLens — 24BAI10032

## Computer Vision Based Campus Lost-and-Found Visual Matching System

VITyarthi | Computer Vision Project

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
