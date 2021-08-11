from datetime import date, datetime, time
from typing import Union

from .core import (DEFAULT_DATE_FORMAT, DEFAULT_FORMAT, DEFAULT_TIME_FORMAT,
                   MAX_DATE, MIN_DATE, get_date_between, get_datetime,
                   get_time_between, validate, validate_date, validate_time)


# Main function that is invoked by the user
def randomtimestamp(
        start_year: int = 1950,
        end_year: int = None,
        text: bool = False,
        start: datetime = None,
        end: datetime = None,
        pattern: str = DEFAULT_FORMAT
        ) -> Union[datetime, str]:
    """
    Function generates random timestamps between two dates/years.

    With no input, the resulting timestamp lies between
    (January 1, 1950, 00:00:00) and ({today}, 23:59:59)

    Arguments:
    - start_year (int) [default=1950]
      Generate timestamp after (start_year, 1, 1, 0, 0, 0)
      Has no effect if 'start' or 'end' are given

    - end_year (int) [default=None]
      Generate timestamp before (end_year, 12, 31, 23, 59, 59)
      Has no effect if 'start' or 'end' are given

    - text (bool) [default=False]
      If True, return timestamp string, else return datetime object

    - start (datetime) [default=None]
      Generate timestamp after 'start' (datetime)
      Overrides 'start_year' and 'end_year'

    - end (datetime) [default=None]
      Generate timestamp before 'end' (datetime)
      Overrides 'start_year' and 'end_year'

    - pattern (str) [default='%d-%m-%Y %H:%M:%S']
      Use custom output format for timestamp string
      Has no effect if 'text' == False
    """
    start_dtime, end_dtime = validate(start_year, end_year, text, start, end)
    stamp = get_datetime(start_dtime, end_dtime)
    if text:
        return stamp.strftime(pattern)
    else:
        return stamp


def random_time(
        start: time = time.min,
        end: time = time.max,
        text: bool = False,
        pattern: str = DEFAULT_TIME_FORMAT
        ) -> Union[time, str]:
    """
    Function generates random time between two time objects.
    With no input, the resulting time lies between (00:00:00) and (23:59:59)

    Arguments:
    - start (time) [default=(00:00:00)]
      Generate timestamp after 'start'
    
    - end (time) [default=(23:59:59)]
      Generate timestamp before 'end'

    - text (bool) [default=False]
      If True, return time as string, else return time object

    - pattern (str) [default='%H:%M:%S']
      Use custom output format for time string
      Has no effect if 'text' == False
    """

    # If the values aren't valid, this raises an exception
    validate_time(start, end, text)
    
    if text:
        return get_time_between(start, end).strftime(pattern)
    else:
        return get_time_between(start, end)


def random_date(
        start: date = MIN_DATE,
        end: date = MAX_DATE,
        text: bool = False, 
        pattern: str = DEFAULT_DATE_FORMAT
        ) -> Union[date, str]:
    """
    Function generates random date between two date objects.
    With no input, the resulting date lies between
    (January 1, 1950) and 'today'

    Arguments:
    - start (date) [default=(01-01-1950)]
      Generate timestamp after 'start'
    
    - end (date) [default={today})]
      Generate timestamp before 'end'

    - text (bool) [default=False]
      If True, return date as string, else return date object

    - pattern (str) [default='%d-%m-%Y']
      Use custom output format for date string
      Has no effect if 'text' == False
    """

    # If the values aren't valid, this raises an exception
    validate_date(start, end, text)

    if text:
        return get_date_between(start, end).strftime(pattern)
    else:
        return get_date_between(start, end)


__all__ = ['random_date', 'random_time', 'randomtimestamp']
