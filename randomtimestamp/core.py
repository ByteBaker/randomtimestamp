from datetime import date, datetime, time, timedelta
from random import randint
from typing import Tuple

DEFAULT_DATE_FORMAT: str = "%d-%m-%Y"
DEFAULT_TIME_FORMAT: str = "%H:%M:%S"
DEFAULT_FORMAT: str = DEFAULT_DATE_FORMAT + " " + DEFAULT_TIME_FORMAT

MIN_DATE: date = date(1950, 1, 1)
MAX_DATE: date = datetime.today().date()


def validate(
    start_year: int, end_year: int, text: bool, start: datetime, end: datetime
) -> Tuple[datetime, datetime]:
    """
    Validate user supplied arguments.
    - Check type validity.
    - Check value ranges.

    Not to be imported.

    Order of resolution:
    - text
    - start/end
    - start_year/end_year
    """
    start_datetime = end_datetime = None

    if text not in {True, False}:
        # 'text' must be boolean
        error = "'text' can only be True/False"
        raise TypeError(error)

    if start is not None:
        if isinstance(start, datetime):
            # 'start' given
            if end is not None:
                if isinstance(end, datetime):
                    # 'end' given
                    if start > end:
                        # 'start' <= 'end' required
                        # raise ValueError
                        error = "'start' <= 'end' required"
                        raise ValueError(error)
                    else:
                        # both 'start' & 'end' are valid
                        start_datetime, end_datetime = start.replace(
                            microsecond=0
                        ), end.replace(microsecond=0)
                else:
                    # 'end' is not a valid datetime object
                    # raise TypeError
                    error = "'end' must be an instance of datetime"
                    raise TypeError(error)
            else:
                # 'end' not given, use now() as default
                start_datetime = start.replace(microsecond=0)
                end_datetime = datetime.combine(MAX_DATE, time(23, 59, 59))
                if start_datetime > end_datetime:
                    # 'start' < now() required
                    # raise ValueError
                    error = "'end' not given, 'start' < now() required"
                    raise ValueError(error)
                else:
                    # 'start_datetime' & 'end_datetime' are assigned
                    # the function can return
                    pass
        else:
            # 'start' is not a valid datetime object
            # raise TypeError
            error = "'start' must be an instance of datetime"
            raise TypeError(error)

    elif start_year is not None:
        if isinstance(start_year, int):
            # 'start_year' given

            if not 1 <= start_year <= 9999:
                # 1 <= 'start_year' <= 9999 required
                # raise ValueError
                error = "1 <= 'start_year' <= 9999 required"
                raise ValueError(error)

            if end_year is not None:
                if isinstance(end_year, int):
                    # 'end_year' given
                    if not 1 <= end_year <= 9999:
                        # 1 <= 'end_year' <= 9999 required
                        # raise ValueError
                        error = "1 <= 'end_year' <= 9999 required"
                        raise ValueError(error)

                    if start_year > end_year:
                        # 'start_year' <= 'end_year' required
                        # raise ValueError
                        error = "'start_year' <= 'end_year' required"
                        raise ValueError(error)
                    else:
                        # 'start_year' & 'end_year' are valid
                        # generate datetime for both and return
                        start_datetime = datetime(start_year, 1, 1, 0, 0, 0)
                        end_datetime = datetime(end_year, 12, 31, 0, 0, 0)
                else:
                    # 'end_year' is not int
                    # raise TypeError
                    error = "'end_year' must be an integer."
                    raise TypeError(error)
            else:
                # 'end_year' not given, use now().year as default
                # thus 'start_year' <= now().year required
                # otherwise raise ValueError
                end_datetime = datetime.now().replace(microsecond=0)
                if start_year > end_datetime.year:
                    # 'start_year' < now().year required
                    # raise ValueError
                    error = "'start_year' < now().year required"
                    raise ValueError(error)
                else:
                    # 'start_year' is valid, using for start_datetime
                    # datetime(start_year, 1, 1, 0, 0, 0) <= range <= now()
                    start_datetime = datetime(start_year, 1, 1, 0, 0, 0)
        else:
            # 'start_year' is not int
            # raise TypeError
            error = "'start_year' must be an integer."
            raise TypeError(error)
    else:
        # Both 'start' & 'start_datetime' are None
        # datetime(1950, 1, 1, 0, 0, 0) <= default range <= datetime.now()

        start_datetime = datetime(1950, 1, 1, 0, 0, 0)
        end_datetime = datetime.now().replace(microsecond=0)

    return start_datetime, end_datetime


def validate_time(start: time, end: time, text: bool) -> None:
    """
    Validate user supplied arguments.
    - Check type validity.
    - Check value ranges.

    Not to be imported.

    Order of resolution:
    - text
    - start/end
    """

    if not isinstance(text, bool):
        error = "'text' can only be True/False"
        raise TypeError(error)

    if not isinstance(start, time):
        error = "'start' must be an instance of time"
        raise TypeError(error)

    if not isinstance(end, time):
        error = "'start' must be an instance of time"
        raise TypeError(error)

    if not start < end:
        error = "'start' < 'end' required"
        raise ValueError(error)


def validate_date(start: date, end: date, text: bool) -> None:
    """
    Validate user supplied arguments.
    - Check type validity.
    - Check value ranges.

    Not to be imported.

    Order of resolution:
    - text
    - start/end
    """

    if not isinstance(text, bool):
        error = "'text' can only be True/False"
        raise TypeError(error)

    if not isinstance(start, date):
        error = "'start' must be an instance of date"
        raise TypeError(error)

    if not isinstance(end, date):
        error = "'start' must be an instance of date"
        raise TypeError(error)

    if not start < end:
        error = "'start' < 'end' required"
        raise ValueError(error)


# Function which generates random datetime object
def get_datetime(start_datetime: datetime, end_datetime: datetime) -> datetime:
    """
    Core function to generate a random timestamp between two datetime objects.
    Should not be imported.
    """
    gap_seconds = int((end_datetime - start_datetime).total_seconds())
    random_gap_seconds = randint(0, gap_seconds)
    random_datetime = start_datetime + timedelta(seconds=random_gap_seconds)
    return random_datetime


# Function which generates random time object
def get_time_between(start_time: time, end_time: time) -> time:
    """
    Core function to generate a random time between two time objects
    Should not be imported.
    """

    # Combined 'start_time' & 'end_time' with MIN_DATE to generate datetime object
    # So that randomtimestamp can be used to generate a random datetime
    # And then take out the time part of it since date is same for both

    start_datetime: datetime = datetime.combine(MIN_DATE, start_time)
    end_datetime: datetime = datetime.combine(MIN_DATE, end_time).replace(microsecond=0)

    r_datetime: datetime = get_datetime(start_datetime, end_datetime)
    r_time: time = r_datetime.time()

    return r_time


# Function which generates random date object
def get_date_between(start_date: date, end_date: date) -> date:
    """
    Core function to generate a random date between two date objects
    Should not be imported.
    """
    min_time: time = time(0, 0, 0)  # Minimum time possible

    # Combined 'start_date' & 'end_date' with 'min_time' to generate datetime object
    # So that randomtimestamp can be used to generate a random datetime
    # And then take out the date part of it since time is same for both

    start_datetime: datetime = datetime.combine(start_date, min_time)
    end_datetime: datetime = datetime.combine(end_date, min_time)

    r_datetime: datetime = get_datetime(start_datetime, end_datetime)
    r_date: date = r_datetime.date()

    return r_date
