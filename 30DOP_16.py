#DATE TIME
'''
from MODULE import CLASS
'''
from datetime import datetime, date, time, timedelta
'''
With this 2 commands, we can know the available functions for each module
print(dir(datetime))
print(help(datetime))
'''
date = datetime.now() #now 'date' is a class calling its method 'now'
print('Full date:',date)
day = date.day #we can bring different properties from a class
print('Day:',day)
month = date.month
print('Month:',month)
year = date.year
print('Year:',year)
second = date.second
print('Second:',second)
minute = date.minute
print('Minute:',minute)
hour = date.hour
print('Hour:',hour)
timestamp = date.timestamp()
print('Amount of seconds from 1st of January 1970 UTC:',timestamp)

#to set a date
#datetime( year, month, day, hour, minute, second)
new_year = datetime(2024, 8, 2, 20, 45, 23)
print('Representative year:',new_year)

#strftime cheatsheet: https://strftime.org/
#to give different kinds of format
t = date.strftime("%A, %d/%m/%Y")
print('Formatted date or time, deppends on callings of the method \'strftime\':',t)

#strptime = string to time object
str_time = 'Monday 5, November 2019'
date_obj = datetime.strptime(str_time, "%A %d, %B %Y")
print('Date as an object took from a string:',date_obj)

#time class from datetime module
#time(hour, minute, second, microsecond)
a = time()
print(a)
b = time(10, 5, 23)
print(b)
c = time(hour=21, minute=34, second=59)
print(c)
#we can do atithmetics with dates
t1 = datetime.now()
t2 = datetime(2025, 1, 1, 00, 00, 00)
t3 = t2 - t1
print('Time left for new year:',t3)

#timedelta:
t4 = timedelta(weeks=10, hours=10, seconds=50)
t5 = timedelta(days=5, seconds=10, hours=9)
t6 = t4 - t5
print(t6)