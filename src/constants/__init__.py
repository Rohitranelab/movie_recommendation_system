import os
from datetime import date

# ===========================
# MongoDB
# ===========================

DATABASE_NAME = "movie_recommendation_system"
COLLECTION_MOVIES_NAME = "Movie-Data"
COLLECTION_CREDITS_NAME = "Credit-Data"
MONGODB_URL_KEY = "MONGODB_URL"

# ===========================
# Pipeline
# ===========================

PIPELINE_NAME = "movie_recommendation"
ARTIFACT_DIR = "artifact"
CURRENT_YEAR = date.today().year

# ===========================
# Dataset
# ===========================

MOVIE_FILE_NAME = "tmdb_5000_movies.csv"
CREDIT_FILE_NAME = "tmdb_5000_credits.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# ===========================
# Data Ingestion
# ===========================

DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_MOVIE_COLLECTION = COLLECTION_MOVIES_NAME
DATA_INGESTION_CREDIT_COLLECTION = COLLECTION_CREDITS_NAME

# ===========================
# Data Validation
# ===========================

DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME = "report.yaml"

# ===========================
# Data Transformation
# ===========================

DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"

# ===========================
# Model Trainer
# ===========================

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MOVIES_PKL_FILE_NAME = "movies.pkl"
SIMILARITY_PKL_FILE_NAME = "similarity.pkl"
VECTORIZER_PKL_FILE_NAME = "count_vectorizer.pkl"

# ===========================
# Model Evaluation
# ===========================

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02

# ===========================
# MinIO / S3
# ===========================

MODEL_BUCKET_NAME = "movie-recommendation"

# ===========================
# API
# ===========================

APP_HOST = "0.0.0.0"
APP_PORT = 5000