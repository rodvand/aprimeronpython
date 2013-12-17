#x = 1; print 'sin(%g)=%g' % (x, sin(x))

"""
This program will produce an error because sin has not been imported.
To make this program functional do a from math import sin
Example under
"""

from math import sin
x = 1; print('sin(%g)=%g' % (x, sin(x)))

"""
Running the program
Unix>python 1.6.py 
sin(1)=0.841471
"""
