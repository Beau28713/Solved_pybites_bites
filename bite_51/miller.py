from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    hours_left = (PY2_DEATH_DT - start_date).total_seconds() / 3600
    rounded_hours_left = round(hours_left, 2)
    return rounded_hours_left


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    minutes_left = (PY2_DEATH_DT - start_date).total_seconds() / 3679200
    print(minutes_left)
    rounded_minutes_left = round(minutes_left, 2)
    return rounded_minutes_left