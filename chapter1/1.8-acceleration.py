""" 
Original code
v0 = 3 m/s              # Problem 1
t = 1 s                 # Problem 1
a = 2 m/s**2            # Problem 1
s = v0*t + 1/2 a*t**2   # Problem 2 and 3
print s
"""
"""
Modified code
"""
v0 = 3  # m/s           
t = 1   # s            
a = 2**2 # m/s          
s = v0*t + 0.5 * a*t**2
print s

"""
First task: run the program
Problem 1: 
Syntax error with v0 = 3 m/s. If we wish to calculate on v0 we
should only include number in the variable. If we wish to print we could
make it a string. As we in the program wish to calculate we omit the m/s
and add this as a comment. We have this problem with t and a as well.
Solution: Move m/s (v0), s (t) and m/s (a) into a comment.
Problem 2:
Syntax error with the 1/2 a*t on the s becomes equal to statement. When 
doing calculations by hand we quickly realise that this means 1/2a times t 
two times. We have to include the multiplication symbol in each operation in 
Python.
Solution: Add a * sign between 1/2 and a
Problem 3:
The answer is not correct. If we write the equation in numbers and do the 
math by hand we quickly see that the answer is incorrect in our program.
s = 3 * 1 + 1/2 * 4 * 1^2
s = 3 + 2
s = 5
5 != 3
Why this? See the 1/2 in the middle? That is our culprit. Dividing 1/2 is 
not very hard for us to do, but Python suffers from the sickness that is
Integer Division. Dividing two integers with each other will return an integer
. In this case Python will return 0. 
Solution: Change 1/2 into 0.5 or .5 (they're the same).
"""

"""
Running the program
Unix>python acceleration.py 
5.0
"""
