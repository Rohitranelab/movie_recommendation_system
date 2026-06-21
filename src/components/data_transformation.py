import os
import sys
import ast
import pandas as pd

from nltk.stem.porter import PorterStemmer

from src.logger import logging
from src.exception import MyException
from src.entity.artifact_entity import  DataTransformationArtifact, DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataTransformationConfig
from src.constants import SCHEMA_FILE_PATH
from src.utils.main_utils import read_yaml_file

class DataTransformation:
    def __init__(self, 
                 data_transformation_config: DataTransformationConfig, 
                 data_ingestion_artifact: DataIngestionArtifact, 
                 data_validation_artifact: DataValidationArtifact):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
            self._schema_config = read_yaml_file(file_path = SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e, sys)

    @staticmethod    
    def read_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e, sys)
        
    def merge_data(self, movie_df, credit_df):
        try:
            merge_df = movie_df.merge(credit_df, on = 'title')

            # keep only required columns
            schema = read_yaml_file(file_path = SCHEMA_FILE_PATH)
            required_columns = schema["required_columns"]
            merge_df = merge_df[required_columns]

            # removes missing values
            merge_df.dropna(inplace = True)
            return merge_df
        except Exception as e:
            raise MyException(e, sys)
    
    def convert(self, text):
        x = []
        for i in ast.literal_eval(text):
            x.append(i['name'])
        return x
    
    def cast_convert(self, text):
        s = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter < 3:
                s.append(i['name'])
            counter += 1
        return s
    
    def crew_convert(self, text):
        a = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                a.append(i['name'])
                break
        return a
    
    def remove_space(self, text):
        l = []
        for i in text:
            l.append(i.replace(' ', ''))
        return l
    
    def overview_split(self, text):
        return text.split()
    
    def join_text(self, text):
        return " ".join(text)
    
    def remove_column(self, df):
        drop_col = self._schema_config['drop_columns']
        existing_cols = [col for col in drop_col if col in df.columns]

        if existing_cols:
            df = df.drop(columns=existing_cols)

        return df
    
    def stem(self, text):
        ps = PorterStemmer()
        return " ".join(ps.stem(word) 
                        for word in text.split())

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info(f'Data Transformation started!!')
            if not self.data_validation_artifact.validation_status:
                raise MyException(self.data_validation_artifact.message)

            # Load the movie and credit dataset
            movie_df = self.read_data(file_path = self.data_ingestion_artifact.movie_file_path)
            credit_df = self.read_data(file_path = self.data_ingestion_artifact.credit_file_path)
            logging.info(f'Movie and Credit data loaded')

            df = self.merge_data(movie_df = movie_df, credit_df = credit_df)
            logging.info(f'Apply transformation in data')
            # Apply custom transformation in specified sequence
            df['genres'] = df['genres'].apply(self.convert)
            df['keywords'] = df['keywords'].apply(self.convert)
            df['cast'] = df['cast'].apply(self.cast_convert)
            df['crew'] = df['crew'].apply(self.crew_convert)

            df['genres'] = df['genres'].apply(self.remove_space)
            df['keywords'] = df['keywords'].apply(self.remove_space)
            df['cast'] = df['cast'].apply(self.remove_space)
            df['crew'] = df['crew'].apply(self.remove_space)

            df['overview'] = df['overview'].apply(self.overview_split)

            df['tags'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['crew']
            df = self.remove_column(df)
            df['tags'] = df['tags'].apply(self.join_text)
            df['tags'] = df['tags'].str.lower()
            df['tags'] = df['tags'].apply(self.stem)
            logging.info(f'Transformation complete')

            # Save the the transformed data
            logging.info(f'Saving the data')
            output_file = self.data_transformation_config.transformed_movie_file_path
            os.makedirs(os.path.dirname(output_file), exist_ok = True)
            df.to_csv(output_file, index = False)
            logging.info(f'Save the data in {output_file}')

            return DataTransformationArtifact(
                transformed_movie_file_path = output_file
            )

        except Exception as e:
            raise MyException(e, sys)