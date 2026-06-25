# 🎬 Movie Recommendation System - End-to-End MLOps Project

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)
[![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge&logo=github)](https://github.com/features/actions)
[![Render](https://img.shields.io/badge/Render-Deployed-purple?style=for-the-badge&logo=render)](https://render.com/)
[![MLOps](https://img.shields.io/badge/MLOps-End%20to%20End-red?style=for-the-badge)](https://en.wikipedia.org/wiki/MLOps)

</p>

---

## 🚀 Project Overview

This project is a **Production-Grade End-to-End MLOps Movie Recommendation System** built using modern Machine Learning Engineering practices.

The system recommends top-rated movies based on user-selected genres using TMDB movie metadata and is designed following a complete MLOps architecture.

The project demonstrates:

✅ Data Pipeline Development

✅ Data Validation & Quality Checks

✅ Feature Engineering

✅ Genre-Based Recommendation Engine

✅ Model Training & Evaluation

✅ Model Versioning

✅ CI/CD Automation

✅ API Development

✅ Cloud Deployment

---

# 🎯 Business Problem

Users often struggle to discover quality movies within their favorite genres.

This system solves the problem by:

* Understanding movie metadata
* Extracting genre information
* Ranking movies based on ratings
* Recommending highly rated movies within the selected genre

---

# 🏗️ MLOps Architecture

```text
MongoDB
   │
   ▼
Data Ingestion
   │
   ▼
Data Validation
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Model Pusher
   │
   ▼
Prediction Pipeline
   │
   ▼
Genre Recommendation Engine
   │
   ▼
FastAPI Application
   │
   ▼
Cloud Deployment
```

---

# 📂 Project Structure

```bash
movie_recommendation_system/

├── artifact/
├── config/
│   └── schema.yaml
│
├── src/
│
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│
│   ├── entity/
│   ├── configuration/
│   ├── exception/
│   ├── logger/
│   └── utils/
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 📊 Dataset

### TMDB 5000 Movie Dataset

The dataset contains:

* Movie Titles
* Genres
* Cast
* Crew
* Overview
* Keywords
* Ratings

Files:

```text
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

---

# 🔄 Data Ingestion

### Source

MongoDB Collections

```python
Movie-Data
Credit-Data
```

### Responsibilities

* Connect MongoDB
* Extract Movie Data
* Extract Credit Data
* Store into Feature Store

---

# ✅ Data Validation

Data Validation ensures:

* Required columns exist
* Missing columns detection
* Schema validation
* Data consistency checks

### Example

```yaml
required_columns:
  - movie_id
  - title
  - genres
  - cast
  - crew
  - overview
```

---

# ⚙️ Data Transformation

The raw data is transformed into a machine-learning-ready format.

### Feature Engineering Steps

### Genres Extraction

```python
[
 {"id":28,"name":"Action"}
]
```

↓

```python
Action
```

### Cast Extraction

Top 3 actors retained.

### Crew Extraction

Only Director retained.

### Text Processing

* Lowercase conversion
* Tokenization
* Stopword removal
* Stemming

### Final Tags Feature

```python
overview
+
genres
+
keywords
+
cast
+
crew
```

↓

```python
tags
```

---

# 🤖 Model Training

### Feature Processing

CountVectorizer

```python
CountVectorizer(
    max_features=5000,
    stop_words="english"
)
```

### Generated Artifacts

```text
movies.pkl
similarity.pkl
count_vectorizer.pkl
```

---

# 📈 Model Evaluation

Validation checks:

* Artifact existence
* Movie dataset integrity
* Genre availability checks
* Recommendation engine readiness

---

# 📦 Model Pusher

Production-ready artifacts are pushed into:

```text
movie-recommendation/
│
├── movies.pkl
├── similarity.pkl
└── count_vectorizer.pkl
```

---

# 🎥 Recommendation Engine

### Genre-Based Recommendation

Input:

```text
Action
```

Output:

```text
The Dark Knight
The Avengers
Gladiator
Mad Max: Fury Road
Inception
```

The system filters movies belonging to the selected genre and recommends the highest-rated titles.

---

# 🌐 API Development

Built using FastAPI.

Example Endpoint:

```python
POST /recommend
```

Request:

```json
{
  "genre":"Action"
}
```

Response:

```json
{
  "recommendations":[
      "The Dark Knight",
      "The Avengers",
      "Inception"
  ]
}
```

---

# ⚡ CI/CD Pipeline

GitHub Actions automates:

* Code Checkout
* Dependency Installation
* Application Validation
* Deployment Trigger

Workflow:

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
Build
      │
      ▼
Test
      │
      ▼
Deploy
```

---

# ☁️ Deployment

Deployment-ready for:

* Render
* Vercel
* AWS EC2

---

# 🛠️ Tech Stack

| Category             | Tools                 |
| -------------------- | --------------------- |
| Language             | Python                |
| Database             | MongoDB               |
| ML Library           | Scikit-Learn          |
| Recommendation Logic | Genre-Based Filtering |
| Data Processing      | Pandas, NumPy         |
| API                  | FastAPI               |
| CI/CD                | GitHub Actions        |
| Deployment           | Render                |
| Version Control      | Git                   |

---

# 📌 Key MLOps Features

✔ Modular Pipeline Architecture

✔ Custom Exception Handling

✔ Centralized Logging

✔ Configuration Management

✔ Artifact Tracking

✔ Schema Validation

✔ Model Evaluation Stage

✔ Model Pusher Stage

✔ CI/CD Automation

✔ Cloud Deployment Ready

---

# 🔮 Future Enhancements

* Personalized User Recommendations
* Trending Movies Recommendation
* Genre Combination Recommendations
* Movie Poster Integration
* Hybrid Recommendation System
* Collaborative Filtering

---
# 🌐 Live Demo

```bash
https://movie-recommendation-system-1-jxlr.onrender.com
```

---

# 👨‍💻 Author

### Rohit Rane

Aspiring Machine Learning Engineer | MLOps Enthusiast

* Machine Learning
* Deep Learning
* NLP
* MLOps
* FastAPI
* CI/CD
* Cloud Deployment

---

## ⭐ If you found this project useful, don't forget to star the repository.
