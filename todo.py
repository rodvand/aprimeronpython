#!/usr/bin/python
"""
Generate a TODO file with the exercise numbers.
"""
import sys

filename = "TODO"
try:
    chapter = sys.argv[1]
    excercises = int(sys.argv[2])
except e:
    print "You need to supply a chapter and a number of excercises."
    exit(1)

try:
    f = open(filename, "w+")
except e:
    print "Unable to open file for writing: "+e[1]
    exit(1)

for i in range(1, excercises+1):
    f.write(str(chapter)+"."+str(i)+"\n")
f.close()
