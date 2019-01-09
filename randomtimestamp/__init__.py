from random import randint
from datetime import timedelta as td, datetime as dt,date,time

__title__ = 'randomtimestamp'
__version__ = '0.1.0'
__author__ = "Shraddha Kishan Tripathi"
__license__ = 'GPL v3.0'

START_DT = date(2000, 1, 1)
END_DT = dt.now().date()
MY_FORMAT = "%d-%m-%Y %H:%M:%S"

def validate(start_year,text):		# Function to validate and correct the user-supplied arguments
	try:
		start_year = int(start_year)
		start_year = (1950,start_year) [start_year>=1950]
	except:
		start_year = 1950
	global START_DT
	START_DT = date(start_year, 1, 1)
	if text not in [True,False]:
		text = True

	return start_year,text

		

def accesstime(date1, date2):		# Function which generates random datetime object
	n = randint(0, int((date2 - date1).days)+1)
	date1 = date1 + td(n)
	hour = randint(0,23)
	minute = randint(0,59)
	second = randint(0,59)
	tm = time(hour,minute,second)
	return dt.combine(date1,tm).strftime(MY_FORMAT)

def gettime():
	return accesstime(START_DT,END_DT)
	

def randomtimestamp(start_year = 1950,text = True):  			# Main function that is invoked by the user
	start_year,text = validate(start_year,text)
	tst = gettime()
	if text == True:
		return str(tst)
	else:
		return tst