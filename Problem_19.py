"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

import time
import datetime
import sys

ti = time.time()

def countSundays():
    count = 0
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    weekday = 1
    for year in range(1900,2001):
        month_index = 0
        for m in months:
            for d in range(1, m + 1):
                if int(m) == 29 and int(d) == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                    break
                current_date = datetime.datetime(year, month_index + 1, d)
                print "%s %s %d %d %s" % (weekday_names[weekday - 1], month_names[month_index], d, year, current_date.strftime("%a %B %d %Y"))

                if current_date.strftime("%a") != weekday_names[weekday - 1]:
                    sys.exit()
                if current_date.strftime("%B") != month_names[month_index]:
                    sys.exit()
                if int(current_date.strftime("%d")) != d:
                    sys.exit()
                if int(current_date.strftime("%Y")) != year:
                    sys.exit()

                if int(m) == 29 and int(d) == 29:
                    print "LEAP YEAR"
                if d == 1 and weekday == 7 and year >= 1901:
                    print "MATCH"
                    count += 1
                if weekday == 7:
                    weekday = 0
                weekday += 1
            month_index += 1
    return count
    
print countSundays()          

print "Time taken(secs):", time.time() - ti
