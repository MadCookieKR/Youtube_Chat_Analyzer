from datetime import datetime


def to_time(time):
    if len(time) <= 5:
        return datetime.strptime(time, '%M:%S')
    else:
        return datetime.strptime(time, '%H:%M:%S')
