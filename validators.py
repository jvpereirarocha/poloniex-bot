import datetime


def validate_period(period):
    if type(period) != '<class int>':
        raise TypeError('InvalidType')
    return True


def validate_date(start):
    pass
