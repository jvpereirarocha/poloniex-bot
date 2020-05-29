import datetime
import time


def datetime_to_string(date):
    try:
        converted_date = date.strftime('%d/%m/%Y %H:%M:%S')
        return converted_date
    except TypeError:
        raise TypeError('Invalid datetime format')


def string_to_datetime(text):
    try:
        format = '%Y-%m-%d %H:%M:%S'
        text_converted_to_datetime = datetime.datetime.strptime(text, format)
        return text_converted_to_datetime
    except TypeError:
        raise TypeError('Invalid text format')


def datetime_to_timestamp(date):
    try:
        converted = date.timetuple()
        aux = str(time.mktime(converted))
        timestamp = aux.split('.')[0]
        return timestamp
    except TypeError:
        raise TypeError('Invalid datetime format')


def timestamp_to_datetime(timestamp):
    try:
        date_time = datetime.datetime.fromtimestamp(timestamp)
        return date_time
    except TypeError:
        raise TypeError('Invalid timestamp format')
