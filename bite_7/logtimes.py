"""In this Bite we will look at this short server log, finding the first and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
You'll need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects. Then use datetime.timedelta to calculate the time difference between them.

You can assume the log is sorted in ascending order. Check out each function's docstring and the TESTS for more details on how to solve this Bite.

Good luck, keep calm, and code in Python!
"""

from datetime import datetime, timedelta
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
    t = re.sub("T", " ", line)

    match_str = (re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', t))

    res = datetime.strptime(match_str.group(), '%Y-%m-%d %H:%M:%S')

    return res

def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown = []

    for line in loglines:
        if re.search(r"Shutdown initiated", line):
            shutdown.append(datetime.strptime(re.search(r"\d{2}:\d{2}:\d{2}",line).group(), "%H:%M:%S"))

    delta_1 = timedelta(hours=shutdown[0].hour, minutes=shutdown[0].minute, seconds=shutdown[0].second)
    delta_2 = timedelta(hours=shutdown[1].hour, minutes=shutdown[1].minute, seconds=shutdown[1].second)

    delta_change = delta_2 - delta_1

    return delta_change