import datetime
import time


def string_to_tick(value):
    return time.mktime(time.strptime(value, "%Y-%m-%d %H:%M:%S"))


def tick_to_string(value):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))


def get_time(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def format_time(value):
    return datetime.datetime.strftime(value, "%Y-%m-%d %H:%M:%S")


def exif_to_tick(value):
    return time.mktime(time.strptime(value, "%Y:%m:%d %H:%M:%S"))
