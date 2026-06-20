import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion

from src.entity.config_entity import DataIngestionConfig

from src.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        '''
        This method of TrainPipeline class is responsible for starting data ingestion component
        '''
        try:
            logging.info('Entered the start_data_ingestion method of TrainPipeline class')
            logging.info('Getting the data from MongoDB')
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f'Got the movies and credits data from MongoDB')
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys)
        
    def run_pipeline(self, ) -> None:
        '''
        This method of TrainPipeline class is responsible for running complelte pipeline
        '''
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise MyException(e, sys)