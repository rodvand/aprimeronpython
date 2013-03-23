"""
Exercise 3.6. Prompt the user for input to the formula (1.1). Consider the simplest program for evaluting (1.1):
"""

g = 9.81
t = eval(raw_input("T=?\n"))
v0 = eval(raw_input("v0=?\n"))

y = v0*t - 0.5*g*t**2
print y
