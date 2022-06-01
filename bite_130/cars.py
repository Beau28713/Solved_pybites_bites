from collections import Counter
from enum import auto

import requests

from pprint import pprint

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    year_dic = [dic.get('automaker') for dic in data if dic.get("year") == year]
    
    return Counter(year_dic).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""

    model_dic = [dic.get('model') for dic in data if dic.get("automaker") == automaker and dic.get("year") == year]

    return set(model_dic)