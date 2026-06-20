import os
import sys
from typing import Tuple

from pandas import DataFrame
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.movie_data import MovieRecommendationData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise MyException(e, sys)
    
    def export_data_into_feature_store(self) -> Tuple[DataFrame, DataFrame]:
        try:
            logging.info(r'Exporting data from MongoDB')
            my_data = MovieRecommendationData()
            movie_dataframe = my_data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.movie_collection_name)
            credit_dataframe = my_data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.credit_collection_name)

            # Remove MongoDB _id column
            movie_dataframe.drop(columns = ['_id'], errors = 'ignore', inplace = True)
            credit_dataframe.drop(columns = ['_id'], errors = 'ignore', inplace = True)

            logging.info(f'Shape of movie dataframe: {movie_dataframe.shape}')
            logging.info(f'Shape of credit dataframe: {credit_dataframe.shape}')
            os.makedirs(self.data_ingestion_config.feature_store_dir, exist_ok = True)
            logging.info(f'Saving exported data into feature store file path: {self.data_ingestion_config.feature_store_dir}')
            movie_dataframe.to_csv(self.data_ingestion_config.movie_file_path, index = False, header = True)
            credit_dataframe.to_csv(self.data_ingestion_config.credit_file_path, index = False, header = True)
            return movie_dataframe, credit_dataframe
        except Exception as e:
            raise MyException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            movie_dataframe, credit_dataframe = self.export_data_into_feature_store()
            logging.info('Got the data from MongoDB')
            logging.info('Exited initiate_data_ingestion method of Data_Ingestion class')
            data_ingestion_artifact = DataIngestionArtifact(movie_file_path = self.data_ingestion_config.movie_file_path,
                                                            credit_file_path = self.data_ingestion_config.credit_file_path)
            logging.info(f'Data Ingestion Artifact: {data_ingestion_artifact}')
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys)