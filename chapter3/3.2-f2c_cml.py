"""
As 3.1 just
Read from the command line
"""
def f2c(f):
    return (f-32)*5./9.

import sys
print "Fahrenheit: %s in Celsius: %d" % (sys.argv[1], f2c(int(sys.argv[1])))
