from datetime import datetime
from typing import Union

from .core import DEFAULT_FORMAT, gettime, validate


# Main function that is invoked by the user
def randomtimestamp(
        start_year: int = 1950,
        text: bool = True,
        end_year: int = None,
        start: datetime = None,
        end: datetime = None,
        pattern: str = DEFAULT_FORMAT
        ) -> Union[datetime, str]:
    """
    Function generates random timestamps between two dates/years.

    With no input, the resulting timestamp lies between
    (January 1, 1950, 00:00:00) and (December 31, current_year, 23:59:59)

    Arguments:
    - start_year (int) [default=1950]
      Generate timestamp after (start_year, 1, 1, 0, 0, 0)
      Has no effect if 'start' or 'end' are given

    - end_year (int) [default=None]
      Generate timestamp before (end_year, 12, 31, 23, 59, 59)
      Has no effect if 'start' or 'end' are given

    - text (bool) [default=True]
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
    stamp = gettime(start_dtime, end_dtime)
    if text:
        return stamp.strftime(pattern)
    else:
        return stamp


__all__ = ['randomtimestamp']
