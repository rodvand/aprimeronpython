import sys
from math import pi, exp, sqrt

m = 0
s = 2
x = 1

if s <= 0:
    print 's must be greater than zero!'
    sys.exit(1)

f = (1./(sqrt(2 * pi) * s)) * exp(-0.5 * ((x -m)/float(s))**2)

print(f)

"""
Running the program
Unix>python Gaussian_function1.py 
0.176032663382
"""
