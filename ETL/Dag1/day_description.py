from datetime import date

def day_description():
    """ Returns the description of what day it is today"""

    # This is the call we want to mock
    today = date.today()

    if today.month == 12 and today.day == 24:
        return "Merry Christmas!"
    # today.weekday is an int from 0->6 (Monday->Sunday)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_as_int = today.weekday()
    return "Today it is " + days[day_as_int]