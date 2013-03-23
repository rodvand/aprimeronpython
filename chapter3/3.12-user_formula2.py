"""
Exercise 3.12. Use the StringFunction tool.
Make the program user_formula.py from Chapter 3.1.3 shorter by
using the convenient StringFunction tool from Chapter 3.1.4. Name of program file: user_formula2.py.
"""
from scitools.StringFunction import StringFunction

formula = raw_input('Write a formula involving x: ')
f = StringFunction(formula)

x = 0
while x is not None: 
    x = eval(raw_input('Give x (None to quit): '))
    if x is not None:
        print 'f(%g)=%g' % (x, f(x))
   
