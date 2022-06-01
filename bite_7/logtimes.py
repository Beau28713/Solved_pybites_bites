"""In this Bite we will look at this short server log, finding the first and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
You'll need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects. Then use datetime.timedelta to calculate the time difference between them.

You can assume the log is sorted in ascending order. Check out each function's docstring and the TESTS for more details on how to solve this Bite.

Good luck, keep calm, and code in Python!
"""

from datetime import datetime
import os
import urllib.request
from pprint import pprint
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    match_str = []
    for date_line in loglines:
        match_str.append(re.search(r'\d{4}-\d{2}-\d{2}', date_line))
    #res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()

    pprint(match_str)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass