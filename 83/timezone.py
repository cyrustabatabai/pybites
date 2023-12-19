from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')
timezones = [AUSTRALIA,SPAIN]


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    
    return tuple([naive_utc_dt.replace(tzinfo=utc).astimezone(time) for time in timezones])


