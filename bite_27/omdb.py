import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_list = []
    for file in files:
        with open(file, "r") as f:
            data = json.loads(f.read())
            movie_list.append(data)
    return movie_list

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    _ = "".join([movie.get("Title") for movie in movies if "Comedy" in movie.get("Genre").split(",")])
    
    return _


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    prev_nominations = 0
    for movie in movies:
        movie_nominations = int(movie.get("Awards").split("&")[1].split(" ")[1])
        if(movie_nominations > prev_nominations):
            prev_nominations = movie_nominations
            nom_movie = movie.get("Title")
    return nom_movie


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    
    prev_runtimes = 0
    for movie in movies:
        movie_runtime = int(movie.get("Runtime").split(" ")[0])
        if(movie_runtime > prev_runtimes):
            prev_runtimes = movie_runtime
            runtime_movie = movie.get("Title")
    return runtime_movie