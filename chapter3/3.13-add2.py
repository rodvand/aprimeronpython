"""
TODO
Exercise 3.13. Extend a program from Ch. 3.2.1.
How can you modify the add_cml.py program from the end of Chap-
ter 3.1.2 such that it accepts input like sqrt(2) and sin(1.2)?
"""
import math
import sys
from scitools.StringFunction import StringFunction

i1 = StringFunction(sys.argv[1])
i2 = StringFunction(sys.argv[2])
print i1, i2
#print '%s + %s becomes %s\nwith value %s' % \
#        (type(i1), type(i2), type(r), r)
