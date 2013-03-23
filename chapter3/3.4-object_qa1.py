"""
Exercise 3.4. Read input from the keyboard.
Make a program that asks the user for an integer, a real number, a
list, a tuple, and a string. Use eval to convert the input string to a list or tuple. Name of program file: objects_qa1.py.
"""

integer = raw_input("Give me an integer, please.\n")
real = raw_input("A real number, please.\n")
alist = raw_input("A list, please.\n")
atuple = raw_input("A tuple, please.\n")
astring = raw_input("And a string, please.\n")
convert = eval('["'+astring+'"]')
print convert
