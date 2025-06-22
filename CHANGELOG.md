## Changelog:

##### v2.3
- Fixed [#2](https://github.com/ByteBaker/randomtimestamp/issues/2), supporting newer Python versions.
- Added test cases for various APIs.
- Updated README and moved changelog to separate file.
##### v2.2
- Fixed microsecond handling bug in datetime range. Closes [#1](https://github.com/ByteBaker/randomtimestamp/issues/1).
##### v2.1 
- Dropped a minor version identifier to account for the small size of module. Only 2 digits to be used hereafter.
- [Breaking change] Order of arguments to randomtimestamp() changed. Code using older versions without keyword arguments breaks.
- [Breaking change] By default **randomtimestamp()** now generates datetime objects. **text = False** by default.
- Introduced **random_time() & random_date()** to generate only time or date if needed.
##### v2.0.0
- Ability to provide **start/end** as datetime objects to randomtimestamp() for more precise control.
- Lower limit of **start_year = 1950** removed.
- Ability to use custom datetime pattern as described in [datetime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).
##### v1.0.0
- Randomtimestamp released. Timestamps can be generated between 1950 and current_year.
- The timestamp can be generated as a string (by default) or a datetime object.
