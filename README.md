![PyPI - Python Version](https://img.shields.io/pypi/pyversions/randomtimestamp?label=Python) ![PyPI - License](https://img.shields.io/pypi/l/randomtimestamp?label=License&color=red) ![Maintenance](https://img.shields.io/maintenance/yes/2022?label=Maintained) ![PyPI](https://img.shields.io/pypi/v/randomtimestamp?label=PyPi) ![PyPI - Format](https://img.shields.io/pypi/format/randomtimestamp?label=Format) ![PyPI - Downloads](https://img.shields.io/pypi/dm/randomtimestamp?label=Downloads&color=yellow)

# randomtimestamp <sup> (v2.0.0)</sup>
Random timestamp generator
## Installation
You know it:
```
pip install randomtimestamp
```
## Usage
randomtimestamp can be used from the command line or imported as a python module.

#### Command line usage
To use the script from command line
```
  $randomtimestamp
  30-08-1995 17:58:14
```

#### Python Module Usage

In v2.0.0, the function **randomtimestamp** takes six optional arguments:
```
randomtimestamp(
    start_year: int = 1950,
    text: bool = True,
    end_year: int = None,
    start: datetime.datetime = None,
    end: datetime.datetime = None,
    pattern: str = "%d-%m-%Y %H:%M:%S"
    )
```
Order of **start_year** & **text** hasn't been changed in v2.0.0 for backward compatibility. Future versions may not support the same order of arguments.

*Order of resolution:*
1. start/end
2. start_year/end_year

This means providing *start_year/end_year* to function call has no effect if *start/end* are also provided.

The default values of **start_year** and **text** are *1950* and *True* respectively.
The timestamp is generated between *January 1st, 1950, 00:00:00* and *datetime.now()*.


## Features:
1. Call without arguments returns a random timestamp as string (**DD-MM-YYYY HH:MM:SS**), where **HH** follows 24-hour format. Setting **text=False** returns a *datetime* object.
2. Lower limit of **start_year = 1950** has been removed. Now 1 <= start_year <= 9999 is allowed. **end_year** has been added to provide upper limit of timestamp beyond current year (within 1-9999). If **end_year** is not given, current year is used as **end_year**. 

	**NOTE**: Both are integers and *start_year <= end_year* is required. If *end_year* is provided, *start_year* is required too.

3. **start** and **end** arguments are datetime objects and can be used for more precise control over timestamp range. **start_year** & **end_year** have no effect if **start** and **end** are given. If **end** is not given, **datetime.now()** is used as **end**.

    **NOTE**: Both are datetime objects and *start < end* is required. If *end* is provided, *start* is required too.

4. **pattern** can be used to generate timestamps in desired format, using valid formats described in [datetime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes). The default pattern is **"%d-%m-%Y %H:%M:%S"**.

	**NOTE**: *pattern* has no effect if **text=False**.



## Examples:
Here are some examples of the possible syntaxes:
```
  >>> from randomtimestamp import randomtimestamp

  >>> randomtimestamp()
  '02-06-1970 23:34:10'

  >>> randomtimestamp(start_year=2020, end_year=2021)
  '05-09-2021 17:24:28'

  >>> randomtimestamp(start_year=2020, end_year=2021, text=False)
  datetime.datetime(2021, 1, 10, 5, 6, 19)

  >>> from datetime import datetime
  >>> start = datetime(2020, 5, 10, 0, 0, 0)
  >>> end = datetime(2020, 10, 10, 0, 0, 0)
  >>> randomtimestamp(start=start, end=end)
  '27-09-2020 20:42:55'
  
  >>> randomtimestamp(start=start, end=end, pattern='%d-%h-%Y %I:%M:%S %p')
  '03-Aug-2020 08:06:27 PM'
```
In any case, if you ever feel stuck, use **help(randomtimestamp)** inside Python's REPL. 

---

#### Footnote:
Type validation has been done, but it won't be required for most developers. If you're someone who likes to break the code with deliberately crafted inputs, you'd most likely receive a **TypeError** or a **ValueError**.

However, if you do find a bug, please report to make the experience better for other developers.


## License
This project is released under [GNU GENERAL PUBLIC LICENSE V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
