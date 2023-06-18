import random
from pprint import pprint

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    new_list = (SEPARATOR.join(map(str, elements)) for elements in zip(*args))

    return new_list