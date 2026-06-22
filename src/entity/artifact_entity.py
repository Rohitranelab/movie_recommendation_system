from dataclasses import dataclass

# ======================================================
# Data Ingestion
# ======================================================

@dataclass
class DataIngestionArtifact:
    movie_file_path: str
    credit_file_path: str


# ======================================================
# Data Validation
# ======================================================

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    validation_report_file_path: str


# ======================================================
# Data Transformation
# ======================================================

@dataclass
class DataTransformationArtifact:
    transformed_movie_file_path: str


# ======================================================
# Model Trainer
# ======================================================

@dataclass
class ModelTrainerArtifact:
    movies_model_path: str
    similarity_model_path: str
    vectorizer_model_path: str


# ======================================================
# Model Evaluation
# ======================================================

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool
    movies_model_path: str
    similarity_model_path: str
    vectorizer_model_path: str


# ======================================================
# Model Pusher
# ======================================================

@dataclass
class ModelPusherArtifact:
    movies_model_path: str
    similarity_model_path: str
    vectorizer_model_path: str