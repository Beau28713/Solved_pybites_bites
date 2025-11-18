import datetime
def tomorrow(today=None):
    ###Help me out by completing the tomorrow() function to return a date object with tomorrow's date.###
    # Your code goes here
    if today is None:
        today = datetime.date(2020, 7, 9)
    next_day = today + datetime.timedelta(days=1)
    return next_day