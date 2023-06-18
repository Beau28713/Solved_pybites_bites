from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
pybites = namedtuple('pybites', blog.keys())

def dict2nt(dict_):
    f = pybites._make(dict_.values())

    return f


def nt2json(nt):
    f = nt._asdict()
    g = json.dumps(f, indent=4, sort_keys=True, default=str)

    return g