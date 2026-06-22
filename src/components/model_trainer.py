import os
import sys
import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.logger import logging
from src.exception import MyException
from src.entity.artifact_entity import ModelTrainerArtifact, DataTransformationArtifact
from src.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,
                 data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info(f'Loading transformed data')
            df = pd.read_csv(self.data_transformation_artifact.transformed_movie_file_path)
            
            logging.info(f'Creating CountVectorier in data')
            cv = CountVectorizer(max_features = 5000, stop_words = 'english')

            vector = cv.fit_transform(df['tags']).toarray()

            logging.info("Calculating cosine similarity")
            similarity = cosine_similarity(vector)
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok = True)

            logging.info(f'Saving movies.pkl')
            movies_dir = self.model_trainer_config.movies_model_path
            with open(movies_dir, "wb") as f:
                pickle.dump(df, f)

            logging.info(f'Saving similarity.pkl')
            similarity_dir = self.model_trainer_config.similarity_model_path
            with open(similarity_dir, "wb") as f:
                pickle.dump(similarity, f)

            logging.info(f'Saving count_vectorizer.pkl')
            vectorizer_dir = self.model_trainer_config.vectorizer_model_path
            with open(vectorizer_dir, "wb") as f:
                pickle.dump(cv, f)
            
            return ModelTrainerArtifact(
                movies_model_path=movies_dir,
                similarity_model_path=similarity_dir,
                vectorizer_model_path=vectorizer_dir
            )    
               
        except Exception as e:
            raise MyException(e, sys)