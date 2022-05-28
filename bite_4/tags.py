"""In this Bite you will find the top ten tags found in the PyBites blog XML feed (e.g. Python, Flask, Django, learning).

The tests for this Bite expect you to use collections.Counter and we loaded a static copy of our XML feed so we can predictably test your code. The PyBites tags will need to be parsed from the XML tags within each (Hint: you don't need an XML parser for this task).

What are PyBites people most passionate about? Look at the tests and you'll know the answer. Then write your solution to make the tests pass.

Keep calm and code in Python!
"""

import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

import re

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    find_tags = re.findall("<category>(.+?)</category>", content)

    return Counter(find_tags).most_common(n)