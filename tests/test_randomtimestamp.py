import unittest
import datetime
import re
from typing import Pattern
from randomtimestamp import randomtimestamp, random_date, random_time


class TestRandomTimestamp(unittest.TestCase):

    def test_default_type_and_range(self) -> None:
        ts: datetime.datetime = randomtimestamp()
        self.assertIsInstance(ts, datetime.datetime)
        earliest: datetime.datetime = datetime.datetime(1950, 1, 1)
        now: datetime.datetime = datetime.datetime.now()
        self.assertTrue(earliest <= ts <= now)

    def test_year_bounds(self) -> None:
        ts: datetime.datetime = randomtimestamp(start_year=2000, end_year=2001)
        self.assertIsInstance(ts, datetime.datetime)
        self.assertTrue(2000 <= ts.year <= 2001)

    def test_datetime_bounds(self) -> None:
        start: datetime.datetime = datetime.datetime(2022, 5, 1, 0, 0, 0)
        end: datetime.datetime = datetime.datetime(2022, 5, 2, 23, 59, 59)
        ts: datetime.datetime = randomtimestamp(start=start, end=end)
        self.assertIsInstance(ts, datetime.datetime)
        self.assertTrue(start <= ts <= end)

    def test_start_after_end_raises(self) -> None:
        start: datetime.datetime = datetime.datetime(2023, 1, 2)
        end: datetime.datetime = datetime.datetime(2023, 1, 1)
        with self.assertRaises(ValueError):
            randomtimestamp(start=start, end=end)

    def test_text_output_patterns(self) -> None:
        patterns: list[str] = ["%d-%m-%Y %H:%M:%S", "%Y/%m/%d %I:%M %p"]
        for pattern in patterns:
            txt: str = randomtimestamp(
                start_year=2021, end_year=2021, text=True, pattern=pattern
            )
            self.assertIsInstance(txt, str)
            regex: Pattern = re.compile(r"[\d\-/ :APMapm]+")
            self.assertRegex(txt, regex)

    def test_microsecond_normalization(self) -> None:
        start: datetime.datetime = datetime.datetime(2024, 1, 1, 12, 0, 0, 123456)
        end: datetime.datetime = datetime.datetime(2024, 1, 1, 12, 0, 1, 654321)
        ts: datetime.datetime = randomtimestamp(start=start, end=end)
        self.assertIsInstance(ts, datetime.datetime)
        self.assertTrue(
            start.replace(microsecond=0) <= ts <= end.replace(microsecond=0)
        )


class TestRandomDate(unittest.TestCase):

    def test_default_type_and_range(self) -> None:
        d: datetime.date = random_date()
        self.assertIsInstance(d, datetime.date)
        self.assertTrue(datetime.date(1950, 1, 1) <= d <= datetime.date.today())

    def test_bounds(self) -> None:
        start: datetime.date = datetime.date(2025, 1, 1)
        end: datetime.date = datetime.date(2025, 1, 10)
        d: datetime.date = random_date(start=start, end=end)
        self.assertTrue(start <= d <= end)

    def test_text_output(self) -> None:
        # random_date supports text and pattern, without year bounds
        pattern: str = "%Y/%m/%d"
        txt: str = random_date(text=True, pattern=pattern)
        self.assertIsInstance(txt, str)
        self.assertRegex(txt, r"\d{4}/\d{2}/\d{2}")


class TestRandomTime(unittest.TestCase):

    def test_default_type_and_range(self) -> None:
        t: datetime.time = random_time()
        self.assertIsInstance(t, datetime.time)
        self.assertTrue(datetime.time(0, 0, 0) <= t <= datetime.time(23, 59, 59))

    def test_bounds(self) -> None:
        start: datetime.time = datetime.time(8, 0, 0)
        end: datetime.time = datetime.time(17, 0, 0)
        t: datetime.time = random_time(start=start, end=end)
        self.assertTrue(start <= t <= end)

    def test_text_output(self) -> None:
        # random_time supports text and pattern
        pattern: str = "%I:%M:%S %p"
        txt: str = random_time(text=True, pattern=pattern)
        self.assertIsInstance(txt, str)
        self.assertRegex(txt, r"\d{2}:\d{2}:\d{2} [AP]M")

    def test_start_after_end_raises(self) -> None:
        start: datetime.time = datetime.time(18, 0, 0)
        end: datetime.time = datetime.time(8, 0, 0)
        with self.assertRaises(ValueError):
            random_time(start=start, end=end)


if __name__ == "__main__":
    unittest.main()
