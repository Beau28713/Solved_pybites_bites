import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as f:
        lines = f.readlines()
    my_dict = defaultdict(str)
    for count, line in enumerate(lines):
        if 'sending to slack channel' in line:
            if "Python" in lines[count-1]:
                my_dict[lines[count-1][:5]] += PY_BOOK
            
            else:
                my_dict[lines[count-1][:5]] += OTHER_BOOK
                
    for key in my_dict:
        print(f"{key} {my_dict[key]}")