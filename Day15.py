#Date and time module:
# import datetime
# we have many more featues like we can calculate indivually date,time,timedelta.

#to get current date and time we use
# 
import datetime
print(datetime.datetime.now())   #2025-03-05 06:51:41.154316

#to print current date
print(datetime.datetime.now().date())  #2025-03-05

#to print current time
print(datetime.datetime.now().time()) 

# to print current month

print(datetime.datetime.now().month)

# to print current year
print(datetime.datetime.now().year)

# to print current day
print(datetime.datetime.now().day)

# #date
# Y-M-D
# date(2025,1,1)

print(datetime.datetime.now().date()) #2025-03-05

#time
# HH:MM:SS
#we can also print houes minutes and seconds separately
print(datetime.datetime.now().time()) 
# to print hours separetely
print(datetime.datetime.now().hour)
# to print minutes separetely
print(datetime.datetime.now().minute)
# to print seconds separetely
print(datetime.datetime.now().second)
# to print datetime at same time
print(datetime.datetime(2025,1,1,10,30,0))  #2025-01-01 10:30:00

# to print timedelta
# suppose we have flight in 5 houres we can calculate using time delta
from datetime import timedelta
print(datetime.datetime.now() + timedelta(hours=5)) #2025-03-05 12:15:44.514399
#to print timedelta
print(timedelta(hours=5))#5:00:00
 
#short dates
# long dates
# timezones
# difference b/w dates,time

