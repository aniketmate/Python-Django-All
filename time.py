import time
seconds = time.time()
# print("Seconds since epoch =", seconds)	 # the epoch is January 1, 1970, 00:00:00 (UTC).

# seconds = time.time()
# local_time = time.ctime(seconds) #ctime returns a string representing local time.
# print("Local time:", local_time)

# print("This is printed immediately.")
# time.sleep(2.4)                               #sleep delays execution of the current thread for the given number of seconds.
# print("This is printed after 2.4 seconds.")


# result = time.localtime(seconds)    #returns struct_time in local time.
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# result = time.gmtime(seconds)     #returns struct_time in UTC
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# t = (2021, 7, 31, 8, 44, 4, 4, 362, 0)

# result = time.asctime(t)  # returns t in string
# print("Result:", result)

import datetime

# datetime_object = datetime.datetime.now() #current date and time
# print(datetime_object)

# date_object = datetime.date.today() # current date
# print(date_object)

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute, second, microsecond)
c = time(11, 34, 56, 234566)
print("c =", c)

# from datetime import datetime

# #datetime(year, month, day)
# a = datetime(2018, 11, 28)
# print(a)

# # datetime(year, month, day, hour, minute, second, microsecond)
# b = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(b)

# from datetime import datetime

# # current date and time
# now = datetime.now()

# t = now.strftime("%H:%M:%S")
# print("time:", t)

# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("s1:", s1)

# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)

# from datetime import datetime

# date_string = "21 June, 2018"
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")   #The strptime() method creates a datetime object from a given string 
# print("date_object =", date_object)