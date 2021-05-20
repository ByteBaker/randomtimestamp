from datetime import datetime, timedelta
from random import randint
from typing import Tuple

DEFAULT_FORMAT = "%d-%m-%Y %H:%M:%S"


def validate(
        start_year: int,
        end_year: int,
        text: bool,
        start: datetime,
        end: datetime
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
                        start_datetime, end_datetime = start, end
                else:
                    # 'end' is not a valid datetime object
                    # raise TypeError
                    error = "'end' must be an instance of datetime"
                    raise TypeError(error)
            else:
                # 'end' not given, use now() as default
                start_datetime = start
                end_datetime = datetime.now().replace(microsecond=0)
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


# Function which generates random datetime object
def gettime(start_datetime: datetime, end_datetime: datetime) -> datetime:
    """
    Core function to generate a random timestamp between two datetime objects.
    Should not be imported.
    """
    gap_seconds = (end_datetime - start_datetime).total_seconds()
    random_gap_seconds = randint(0, gap_seconds)
    random_datetime = start_datetime + timedelta(seconds=random_gap_seconds)
    return random_datetime
