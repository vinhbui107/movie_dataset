import pandas as pd
import numpy as np
from tmdbv3api import TMDb, Movie, Person

# get api movie with key
tmdb = TMDb()
tmdb.api_key = "1a68f9e403acd4cd793cc445996fb694"
tmdb.language = "en"
tmdb.debug = True


actor_data = pd.read_csv("./actor_data.csv")
actor_data.image_path = actor_data.image_path.astype(str)


def _search_actor_image(actor_name):
    actor = Person()
    search = actor.search(actor_name)

    if search is not None:
        for actor in search:
            if actor.name == actor_name:
                return actor.profile_path
            else:
                return None
    else:
        return None


def get_actor_image(actor_name):
    for idx, row in actor_data.iterrows():
        image_path = _search_actor_image(actor_data.at[idx, "actor_name"])
        actor_data.at[idx, "image_path"] = image_path


get_actor_image(actor_data)

# now i will write new dataframe to a new csv file
actor_data.to_csv("./actor_data_new.csv", encoding="utf-8", index=False)

print("SUCCESSED TO FIND IMAGE OF ACTOR")

# hello
def print_hello(str):
    print("Hello World")
