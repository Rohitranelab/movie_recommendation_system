import os
from dataclasses import dataclass
from datetime import datetime

from src.constants import *

TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# =====================================================
# Training Pipeline
# =====================================================

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP

training_pipeline_config = TrainingPipelineConfig()


# =====================================================
# Data Ingestion
# =====================================================

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_dir = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    movie_file_path = os.path.join(feature_store_dir, MOVIE_FILE_NAME)
    credit_file_path = os.path.join(feature_store_dir, CREDIT_FILE_NAME)
    movie_collection_name = DATA_INGESTION_MOVIE_COLLECTION
    credit_collection_name = DATA_INGESTION_CREDIT_COLLECTION


# =====================================================
# Data Validation
# =====================================================

@dataclass
class DataValidationConfig:
    data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    validation_report_file_path = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILE_NAME)


# =====================================================
# Data Transformation
# =====================================================

@dataclass
class DataTransformationConfig:
    data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_data_dir = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR)
    transformed_object_dir = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR)
    movies_file_path = os.path.join(transformed_data_dir, MOVIES_PKL_FILE_NAME)
    transformed_movie_file_path = os.path.join(transformed_data_dir, "movies_transformed.csv")


# =====================================================
# Model Trainer
# =====================================================

@dataclass
class ModelTrainerConfig:
    model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
    trained_model_dir = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR)
    similarity_model_path = os.path.join(trained_model_dir, SIMILARITY_PKL_FILE_NAME)
    movies_model_path = os.path.join(trained_model_dir, MOVIES_PKL_FILE_NAME)
    vectorizer_model_path = os.path.join(trained_model_dir, VECTORIZER_PKL_FILE_NAME)


# =====================================================
# Model Evaluation
# =====================================================

@dataclass
class ModelEvaluationConfig:
    changed_threshold_score = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE


# =====================================================
# Model Pusher
# =====================================================

@dataclass
class ModelPusherConfig:
    bucket_name = MODEL_BUCKET_NAME
    movies_model_path = os.path.join(bucket_name, MODEL_BUCKET_MOVIE_NAME)
    similarity_model_path = os.path.join(bucket_name, MODEL_BUCKET_SIMILARITY_NAME)
    vectorizer_model_path = os.path.join(bucket_name, MODEL_BUCKET_VECTORIZER_NAME)


# =====================================================
# Prediction Pipeline
# =====================================================

@dataclass
class PredictionPipelineConfig:
    similarity_model_path = SIMILARITY_PKL_FILE_NAME
    movies_model_path = MOVIES_PKL_FILE_NAME