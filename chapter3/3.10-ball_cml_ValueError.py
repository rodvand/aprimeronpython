"""
Excercise 3.10
"""
import sys

g = 9.81

try:
    v0 = eval(sys.argv[1])
except IndexError:
    v0 = eval(raw_input("v0=?\n"))

try:
    t = eval(sys.argv[2])
except IndexError:
    t = eval(raw_input("t=?\n"))

if t > ((2*v0)/g) or t < 0:
    a = (2*v0)/g
    raise ValueError("Value must be between "+str(a)+" and 0")
    print "Value is not between 0 and 2v0/g. Aborting..."

y = v0*t - 0.5*g*t**2
print y
