"""
Program to generate the running example at
the end of the script file.

Example:
Running program
Unix>name of program
Output of the program
"""

import sys
import subprocess

filename = sys.argv[1]
print filename

startline = "\"\"\"\nRunning program\nUnix>python "+filename+"\n"
output = subprocess.check_output("python "+filename, shell=True)
endline = "\"\"\""

arg = startline+output+endline
print arg

f = open(filename, 'a')
f.write("\n")
f.write(arg)
f.close()
