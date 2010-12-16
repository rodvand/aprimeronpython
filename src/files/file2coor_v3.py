infile = open('xyz.dat', 'r')
coor = []  # list of (x,y,z) tuples
for line in infile:
    words = line.split('=')
    x = float(words[1][:-1])
    y = float(words[2][:-1])
    z = float(words[3])
    coor.append((x, y, z))
infile.close()

from numpy import *
coor = array(coor)
print coor.shape, coor

