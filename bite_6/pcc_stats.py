"""Given a listing of files for our community branch, determine:

- Who opened the most pull requests (excluding PyBites)?

- Which challenge has the most pull requests?

Complete the functions gen_files and diehard_pybites below.

The docstring for each function contains more information to help you solve the problem.
"""

from collections import Counter, namedtuple
import os
import urllib.request
from pprint import pprint

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = ['static', 'templates', 'data', 'pybites', 'bbelderbos', 'hobojoe1848']

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile, "r") as file:

        gen_list = [line.lower().split(",")[0] for line in file if "True" in line]

    return gen_list

def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()
    counter = Counter(files)
    pprint(counter)

    users = Counter()
    popular_challenges = Counter()

    # your code