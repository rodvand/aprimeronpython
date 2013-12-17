"""
Original code
from math import sin, cos   # Problem 2
x = pi/4                    # Problem 2
1_val = sin^2(x) + cos^2(x) # Problem 1 and 3
print 1_VAL                 # Problem 1
"""

# Corrected code
from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print(val)

"""
First task: run the program
Problem 1:
When running this program you will receive a syntax error due to the name
1_val. In Python it is not allowed to start a variable with a number.
Solution: change 1_val and 1_VAL to a valid name.
Problem 2:
If we correct the naming error, we will receive a NameError telling us that
pi is not defined. This is correct as we have not imported pi from math.
Solution: add pi to the import statement
Problem 3:
We will get an error on the computation of sun^2(x) because this is not valid 
Python.
Solution: Change from sin^2(x) to sin(x)**2. Do the same with cos.
"""

"""
Running the program
Unix>python sin2_plus_co2.py 
1.0
"""
