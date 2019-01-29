# randomtimestamp
Random timestamp generator

## Usage
randomtimestamp can be used from the command line or imported as a python package.

### Command line usage
To use the script from command line
```
<<<<<<< HEAD
  $randomtimestamp
=======
  $ python -m randomtimestamp
>>>>>>> fb9056350a885ba1c05ce2032afe37468b2cc09d
  30-08-1995 17:58:14
```

### Python Package Usage

The function **randomtimestamp** takes two optional arguments:
```
randomtimestamp(start_year=1950,text=True)
```
The default values of **start_year** and **text** are *1950* and *True* respectively.
The timestamp is generated between *1950* and current year (*datetime.now().year*). Although a year before 1950 could have been used, but it didn't seem to be necessary.

By default, the function returns the output as string in format (**DD-MM-YYYY HH:MM:SS**), where **HH** is in 24-hour format. Setting **text=False** returns a *datetime* object.

Here are examples of all the possible syntaxes:
```
  >>>from randomtimestamp import randomtimestamp
  
  >>>randomtimestamp()
  '02-06-1970 23:34:10'
  
  >>>randomtimestamp(2010)
  '02-06-2013 23:34:10'  
  
  >>>randomtimestamp(start_year=2005)
  '10-04-2015 10:55:02'  
  
  >>>randomtimestamp(2010,False)
  datetime.datetime(2010, 5, 16, 3, 32, 18)
  
  >>>randomtimestamp(text=False)
  datetime.datetime(1951, 2, 13, 18, 19, 1)
```

## License
This project is released under [GNU GENERAL PUBLIC LICENSE V3](https://www.gnu.org/licenses/gpl-3.0.en.html).
