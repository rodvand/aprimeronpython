"""
Original code
a = 3,3 b = 5,3         # Problem 1 and 4
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2ab + b2 # Problem 2 and 5
eq2_sum = a2 - 2ab + b2 # Problem 2 and 5

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print 'First equation: %g = %g', % (eq1_sum, eq1_pow)   # Problem 3
print 'Second equation: %g = %g', % (eq2_sum, eq2_pow)  # Problem 3
"""
"""
Modified code
"""
a = 3.3; b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print 'First equation: %g = %g' % (eq1_sum, eq1_pow)
print 'Second equation: %g = %g' % (eq2_sum, eq2_pow)

"""
First task: run the program
Problem 1:
We get an invalid syntax error on the first line. We are not allowed to 
declare two variables on one line. Python reads line by line, but we can force
Python to evaluate values on one line twice with a simple ; between the 
statements. So we insert a semicolon between the a and b declaration. There
are more problems on the first line, but we will return to that later.
Solution: Insert semicolo (;) between a and b statement.
Problem 2:
We get an invalid syntax error on the first sum statement. 2ab is not a valid
multiplication statement.
Solution: insert a * between 2 and ab. This will also have to be done
for the line beneath.
Problem 3:
We get an invalid syntax error when trying to print the sums of the equations.
The comma between the print string and the variables to be included in the 
string is the culprit. Remove the variable and the print will work.
Solution: Remove the comma between the string and the variables on the line of
the print.
Problem 4:
We get an error saying the operand is not supported with the type we wish to
use. Well we do not wish to use a tuple. We wish to have a and b as decimal
number or floats as Python call them. Our error in this problem is that 
we created two tuples instead of floats. We should have used a dot instead
of comma.
Solution: Use dot instead of comma.
Problem 5:
ab does not exist. We wish to multiply a and b. 
Solution: Add a multiplication sign between a and b.
"""

"""
Running the program 
Unix>python a_pm_b_sqr.py 
First equation: 73.96 = 73.96
Second equation: 4 = 4
"""
