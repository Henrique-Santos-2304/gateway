from datetime import datetime
from time import time


def get_date_now() -> str:
    date_now = datetime.now()
    date = date_now.strftime('%d/%m/%Y %H:%M')
    return date


def get_timestamp():
    return int(time())
