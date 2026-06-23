# Updated: Force rebuild
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from src.constants import APP_HOST, APP_PORT
from src.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI(title="Movie Recommendation System")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

predict = PredictionPipeline()

genres = [
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


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "genres": genres,
            "movies": [],
            "selected": None
        }
    )


@app.post("/", response_class=HTMLResponse)
async def recommend(request: Request, genre: str = Form(...)):

    df = predict.recommend_by_genre(genre, n=10)

    movies = []

    for _, row in df.iterrows():

        movies.append({
            "title": row["title"],
            "vote_average": row["vote_average"],
            "poster": predict.fetch_poster(int(row["movie_id"]))
        })

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "genres": genres,
            "movies": movies,
            "selected": genre
        }
    )


if __name__ == "__main__":
    app_run(
        "app:app",          # change app if filename is different
        host=APP_HOST,
        port=APP_PORT,
        reload=True
    )