import os
import sys
import pickle
import requests
import pandas as pd

from src.exception import MyException
from src.logger import logging
from src.constants import MODEL_BUCKET_NAME, MODEL_BUCKET_MOVIE_NAME, MODEL_BUCKET_SIMILARITY_NAME

class PredictionPipeline:
    def __init__(self):
        try:
            movie_path = os.path.join(MODEL_BUCKET_NAME, MODEL_BUCKET_MOVIE_NAME)
            similarity_path = os.path.join(MODEL_BUCKET_NAME, MODEL_BUCKET_SIMILARITY_NAME)
            logging.info("Loading movies.pkl")
            with open(movie_path, "rb") as f:
                self.movies = pickle.load(f)
            logging.info("Loading similarity.pkl")
            with open(similarity_path, "rb") as f:
                self.similarity = pickle.load(f)

        except Exception as e:
            raise MyException(e, sys)

    # Recommend using Movie Name
    def recommend_movie(self, movie_name, n=10):
        try:
            movie_index = self.movies[self.movies["title"] == movie_name].index[0]
            distances = list(enumerate(self.similarity[movie_index]))
            distances = sorted(distances, reverse=True, key=lambda x: x[1])
            recommendations = []
            for i in distances[1:n+1]:
                recommendations.append(
                    self.movies.iloc[i[0]].title
                )
            return recommendations

        except Exception as e:
            raise MyException(e, sys)

    # Recommend using Genre
    def recommend_by_genre(self, genre, n=10):
        try:
            df = self.movies.copy()
            genre_movies = df[df["genres"].apply(lambda x: genre in x)]
            genre_movies = genre_movies.sort_values("vote_average", ascending=False)
            return genre_movies[["movie_id", "title", "vote_average"]].head(n)

        except Exception as e:
            raise MyException(e, sys)
    
    def fetch_poster(self, movie_id):
        try:
            api_key = os.getenv("TMDB_API_KEY")   
            url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
            response = requests.get(url)
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
            else:
                return "https://via.placeholder.com/500x750?text=No+Poster"

        except Exception as e:
            raise MyException(e, sys)