import datetime


def str2datetime(date_str: str) -> datetime:
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')