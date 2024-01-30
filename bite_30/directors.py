import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

import statistics

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movie_dict = defaultdict(list)

    with open(MOVIE_DATA,"r", encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        for row in file_reader:
            dir_name = row["director_name"]
            title = row["movie_title"]
            
            if not row["title_year"]:
                continue
            year = int(row["title_year"])
            
            if year <= 1960:
                continue
            
            score = float(row["imdb_score"])
            movie_dict[dir_name].append(Movie(title=title, year=year, score=score))

    return movie_dict
    
def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    mean_score = round(statistics.mean([movie.score for movie in movies]), 1)
    return mean_score


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    g = []
    for dir in directors:
        if len(directors[dir]) < MIN_MOVIES:
            continue
        g.append((dir, (round(statistics.mean(list(x.score for x in directors[dir])), 1))))
        
    return sorted(g, key= lambda x: x[1], reverse= True)