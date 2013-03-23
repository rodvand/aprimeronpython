"""
Exercise 3.5. Read input from the command line.
Let a program store the result of applying the eval function to the
first command-line argument. Print out the resulting object and its type (use type from Chapter 1.5.2). Run the program with different input: an integer, a real number, a list, and a tuple. Then try the string "this is a string" as a command-line argument. Why does this string cause problems and what is the remedy? Name of program file: objects_cml.py.
"""

import sys
cml = eval(sys.argv[1])
print "The resulting object: "+str(cml)
print "The type: "+str(type(cml))

"""
The string causes trouble because the eval function will remove the quotes from
"this is a string" and evaluate the keywords this is a string. To get around this
you can just use extra quotation marks, like this: "'this is a string'"
"""
