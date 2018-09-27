from random import randint
from datetime import timedelta as td, datetime as dt,date,time

start_dt = date(1950, 1, 1)
end_dt = dt.now().date()

myFormat = "%d-%m-%Y %H:%M:%S"
def accesstime(date1, date2):
	n = randint(0, int((date2 - date1).days)+1)
	date1 = date1 + td(n)
	hour = randint(0,23)
	min = randint(0,59)
	sec = randint(0,59)
	tm = time(hour,min,sec)
	return dt.combine(date1,tm)

def gettime():
	return accesstime(start_dt,end_dt)
	
def timestamp(year=1900,month=1,day=1,full="part",type="tuple"):
	