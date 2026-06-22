import os
import sys
import pickle

from src.logger import logging
from src.exception import MyException

from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import ModelTrainerArtifact, ModelEvaluationArtifact

class ModelEvaluation:
    def __init__(self, model_trainer_artifact: ModelTrainerArtifact, model_evaluation_config: ModelEvaluationConfig):
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config

    def initiate_model_evaluation(self):
        try:
            movies_path = self.model_trainer_artifact.movies_model_path
            similarity_path = self.model_trainer_artifact.similarity_model_path
            vectorizer_path = self.model_trainer_artifact.vectorizer_model_path

            if not os.path.exists(movies_path):
                raise MyException("movies.pkl not found")

            if not os.path.exists(similarity_path):
                raise MyException("similarity.pkl not found")

            if not os.path.exists(vectorizer_path):
                raise MyException("vectorizer.pkl not found")

            with open(movies_path, "rb") as f:
                movies = pickle.load(f)

            with open(similarity_path, "rb") as f:
                similarity = pickle.load(f)

            if len(movies) != similarity.shape[0]:
                raise MyException("Movies and similarity matrix size mismatch.")

            logging.info("Model Evaluation completed.")

            return ModelEvaluationArtifact(
                is_model_accepted=True,
                movies_model_path=movies_path,
                similarity_model_path=similarity_path,
                vectorizer_model_path=vectorizer_path
            )

        except Exception as e:
            raise MyException(e, sys)