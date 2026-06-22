import streamlit as st
from src.pipeline.prediction_pipeline import PredictionPipeline

predict = PredictionPipeline()

st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")

genre = st.selectbox(
    "Select which type movie you want!",
    [
        "Action",
        "Adventure",
        "Comedy",
        "Drama",
        "Fantasy",
        "Horror",
        "Romance",
        "ScienceFiction",
        "Thriller"
    ]
)

if st.button("Show Movies"):
    # Get recommended movies
    df = predict.recommend_by_genre(genre, n=10)
    # First Row
    cols = st.columns(5)
    for i in range(5):
        movie = df.iloc[i]
        poster = predict.fetch_poster(movie["movie_id"])
        with cols[i]:
            st.image(poster, width = 200)
            st.markdown(f"**{movie['title']}**")
            st.write(f"⭐ {movie['vote_average']}")

    # Second Row
    cols = st.columns(5)
    for i in range(5, 10):
        movie = df.iloc[i]
        poster = predict.fetch_poster(movie["movie_id"])
        with cols[i - 5]:
            st.image(poster, use_container_width=True)
            st.markdown(f"**{movie['title']}**")
            st.write(f"⭐ {movie['vote_average']}")