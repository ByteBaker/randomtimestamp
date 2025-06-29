![PyPI - Python Version](https://img.shields.io/pypi/pyversions/randomtimestamp?label=Python) ![PyPI - License](https://img.shields.io/pypi/l/randomtimestamp?label=License&color=red) ![PyPI](https://img.shields.io/pypi/v/randomtimestamp?label=PyPi) ![PyPI - Status](https://img.shields.io/pypi/status/randomtimestamp?label=Status) ![PyPI - Format](https://img.shields.io/pypi/format/randomtimestamp?label=Format) ![PyPI - Downloads](https://img.shields.io/pypi/dm/randomtimestamp?label=Downloads&color=yellow) 

# randomtimestamp <sup> (v2.3)</sup>
Random timestamp generator
## Installation
You know it:
```bash
pip install randomtimestamp
```
## Usage
randomtimestamp can be used from the command line or imported as a python module.

#### Command line usage
To use the script from command line
```bash
  $ randomtimestamp
  30-08-1995 17:58:14
```

#### Python Module Usage

The module exposes the APIs **randomtimestamp**, **random_time**, and **random_date**.

1.  **randomtimestamp()** takes six optional arguments. A call without arguments returns a datetime between **January 1st, 1950, 00:00:00** and **({today}, 23:59:59)**.

 **NOTE**: **start/end** are resolved before **start_year/end_year**, therefore **start_year/end_year** have no effect if **start/end** have been provided.
```py
randomtimestamp(
    start_year: int = 1950,
    end_year: int = None,
    text: bool = False,
    start: datetime.datetime = None,
    end: datetime.datetime = None,
    pattern: str = "%d-%m-%Y %H:%M:%S"
    ) -> Union[datetime, str]:
```
2.  **random_time()** takes four optional arguments. A call without arguments returns a time between **between (00:00:00)** and **(23:59:59)**.
 
```py
random_time(
    start: datetime.time = time.min,
    end: datetime.time = time.max,
    text: bool = False,
    pattern: str = "%H:%M:%S"
    ) -> Union[time, str]:
```
3.  **random_date()** takes four optional arguments. A call without arguments returns a date between **(January 1, 1950)** and **today**.
 
```py
random_date(
    start: datetime.date = date(1950, 1, 1),
    end: datetime.date = datetime.today().date(),
    text: bool = False,
    pattern: str = "%d-%m-%Y"
    ) -> Union[date, str]:
```
In any of these function calls, **start < end** & **start_year < end_year** is mandatory. **pattern** has no effect if **text = False**.

#### Running tests
```bash
python -m unittest discover
```
---


## Examples:
Here are some examples of the possible syntaxes:
```py
  >>> from randomtimestamp import randomtimestamp, random_date, random_time

  >>> randomtimestamp()
  datetime.datetime(1970, 6, 2, 23, 34, 10)

  >>> randomtimestamp(start_year=2020, end_year=2021)
  datetime.datetime(2021, 1, 10, 5, 6, 19)

  >>> randomtimestamp(start_year=2020, end_year=2021, text=True)
  '05-09-2021 17:24:28'

  >>> random_time()
  datetime.time(13, 18, 14)

  >>> random_date()
  datetime.date(1990, 6, 13)
  
  >>> random_time(text=True, pattern='%I:%M:%S %p')
  '08:06:27 PM'
```
In any case, if you ever feel stuck, use **help(randomtimestamp)** inside Python's REPL. 

---

#### Footnote:
Type validation has been done, but it won't be required for most developers. If you're someone who likes to break the code with deliberately crafted inputs, you'd most likely receive a **TypeError** or a **ValueError**.

However, if you do find a bug, please report to make the experience better for other developers.


## License
This project is released under [GNU GENERAL PUBLIC LICENSE V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
