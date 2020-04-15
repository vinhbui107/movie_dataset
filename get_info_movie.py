import pandas as pd
import numpy as np
from tmdbv3api import TMDb, Movie


# get api movie with key
tmdb = TMDb()
movie = Movie()
tmdb.api_key = "1a68f9e403acd4cd793cc445996fb694"
tmdb.language = "en"
tmdb.debug = True


movie_data = pd.read_csv("./movie_data.csv")
movie_data.overview = movie_data.overview.astype(str)
movie_data.poster_path = movie_data.poster_path.astype(str)


def _search_overview(movie_title):
    movie = Movie()
    search = movie.search(movie_title)

    if search is not None:
        for movie in search:
            if movie.title == movie_title:
                return movie.overview
    else:
        return None


def _search_poster_path(movie_title):
    movie = Movie()
    search = movie.search(movie_title)

    if search is not None:
        for movie in search:
            if movie.title == movie_title:
                return movie.poster_path
            else:
                return None
    else:
        return None


def get_info(movie_data):
    for idx, row in movie_data.iterrows():
        overview = _search_overview(movie_data.at[idx, "movie_title"])
        movie_data.at[idx, "overview"] = overview

        poster_path = _search_poster_path(movie_data.at[idx, "movie_title"])
        movie_data.at[idx, "poster_path"] = poster_path


get_info(movie_data)

# now i will write new dataframe movie to a new csv file
movie_data.to_csv("./movie_data_new.csv", encoding="utf-8", index=False)

print("SUCCESSED TO FIND DATA INFO MOVIE")
