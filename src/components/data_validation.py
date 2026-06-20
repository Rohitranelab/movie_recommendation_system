import os
import sys
import pandas as pd
from pandas import DataFrame
import yaml

from src.exception import MyException
from src.logger import logging
from src.constants import SCHEMA_FILE_PATH
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.utils.main_utils import read_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(file_path = SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e, sys)
        
    def validate_movie_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            excepted_columns = list(self._schema_config['movies_columns'].keys())
            missing_columns = []

            for column in excepted_columns:
                if column not in dataframe.columns:
                    missing_columns.append(column)
            
            if len(missing_columns) > 0:
                logging.info(f'Missing Movie Columns: {missing_columns}')
                return False
        
            return True
        
        except Exception as e:
            raise MyException(e, sys)
        
    def validate_credit_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            excepted_columns = list(self._schema_config['credits_columns'].keys())
            missing_columns = []

            for column in excepted_columns:
                if column not in dataframe.columns:
                    missing_columns.append(column)
            
            if len(missing_columns) > 0:
                logging.info(f'Missing Credit Columns: {missing_columns}')
                return False
            
            return True
        
        except Exception as e:
            raise MyException(e, sys)
        
    def write_validation_report(self, movie_status, credit_status):
        try:
            report = {
                'Movie Status': movie_status,
                'Credit Status': credit_status
            }

            report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(report_dir, exist_ok = True)

            with open(self.data_validation_config.validation_report_file_path, "w") as file:
                yaml.dump(report, file)
        
        except Exception as e:
            raise MyException(e, sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            logging.info(f'Reading the movie dataset')
            movie_df = pd.read_csv(self.data_ingestion_artifact.movie_file_path)

            logging.info(f'Reading the credit dataset')
            credit_df = pd.read_csv(self.data_ingestion_artifact.credit_file_path)

            movie_status = self.validate_movie_columns(movie_df)
            credit_status = self.validate_credit_columns(credit_df)
            validation_status = (movie_status and credit_status)
            self.write_validation_report(movie_status, credit_status)

            artifact = DataValidationArtifact(validation_status = validation_status,
                                              message = 'Validation Completed',
                                              validation_report_file_path = self.data_validation_config.validation_report_file_path)
            
            logging.info(f'Validation Artifact: {artifact}')
            return artifact
    
        except Exception as e:
            raise MyException(e, sys)