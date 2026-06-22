# below code is to check the logging config
# rom src.logger import logging
# 
# ogging.debug('This is a debug message.')
# ogging.info('This is a info message.')
# ogging.warning('This is a warning message.')
# ogging.error('This is a error message.')
# ogging.critical('This is a critical message.')


# below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys
# 
# try:
#     a = 1 + 'z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# import pickle
# 
# with open("movie-recommendation/movies.pkl", "rb") as f:
#     movies = pickle.load(f)
# 
# print(type(movies))
# print(movies.head())

from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()