import os
import shutil
import sys

from src.exception import MyException
from src.logger import logging

from src.entity.config_entity import ModelPusherConfig
from src.entity.artifact_entity import ModelEvaluationArtifact, ModelPusherArtifact

class ModelPusher:
    def __init__(self, model_evaluation_artifact: ModelEvaluationArtifact, model_pusher_config: ModelPusherConfig):
        self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = model_pusher_config

    def initiate_model_pusher(self):
        try:
            logging.info("Entered Model Pusher")

            os.makedirs(self.model_pusher_config.bucket_name,exist_ok=True)

            shutil.copy2(self.model_evaluation_artifact.movies_model_path, self.model_pusher_config.movies_model_path)
            shutil.copy2(self.model_evaluation_artifact.similarity_model_path, self.model_pusher_config.similarity_model_path)
            shutil.copy2(self.model_evaluation_artifact.vectorizer_model_path, self.model_pusher_config.vectorizer_model_path)

            logging.info("Models copied successfully.")

            return ModelPusherArtifact(
                movies_model_path=self.model_pusher_config.movies_model_path,
                similarity_model_path=self.model_pusher_config.similarity_model_path,
                vectorizer_model_path=self.model_pusher_config.vectorizer_model_path
            )

        except Exception as e:
            raise MyException(e, sys)