"""
Program to generate the running example at
the end of the script file.

Usage: python generate.py <file>

Example:
Running program
Unix>name of program
Output of the program
"""

def usage():
    import sys
    print "Usage: python "+sys.argv[0]+" <file>"
    exit(1);

import sys
import subprocess

try:
    filename = sys.argv[1]
except IndexError:
    usage()

startline = "\"\"\"\nRunning program\nUnix>python "+filename+"\n"
output = subprocess.check_output("python "+filename, shell=True)
endline = "\"\"\""

arg = startline+output+endline

f = open(filename, 'a')
f.write("\n")
f.write(arg)
f.close()
