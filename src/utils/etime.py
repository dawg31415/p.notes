from datetime import time, datetime
from constants.consts import TIME_FORMAT, DATE_FORMAT
from typing import Union

def time_to_str(_time: time) -> str:
    return _time.strftime(TIME_FORMAT)

def date_to_str(date: datetime) -> str:
    return date.strftime(DATE_FORMAT)

def str_to_date(date: str) -> datetime:
    return datetime.strptime(date, DATE_FORMAT)

def str_to_time(date: str) -> time:
    return datetime.strptime(date, TIME_FORMAT)
