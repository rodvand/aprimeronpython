"""
Exercise 3.11. Look up calendar functionality.
The purpose of this exercise is to make a program which takes a
date, consisting of year (4 digits), month (2 digits), and day (1-31) on the command line and prints the corresponding name of the weekday (Monday, Tuesday, etc.). Python has a module calendar, which you must look up in the Python Library Reference (see Chapter 2.4.3), for calculating the weekday of a date. Name of program file: weekday.py.
"""
import sys
import calendar

year = eval(sys.argv[1])
month = eval(sys.argv[2])
day = eval(sys.argv[3])

print "The date %d %d %d is a %s" % (year, month, day, calendar.day_name[calendar.weekday(year, month, day)])
