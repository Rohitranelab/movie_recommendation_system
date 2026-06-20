import sys
import pandas as pd
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException
from src.logger import logging


class MovieRecommendationData:

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            logging.info(f"Fetching data from MongoDB Collection: {collection_name}")
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"Data fetched successfully. Total Records: {len(df)}")
            # Remove MongoDB ObjectId
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)