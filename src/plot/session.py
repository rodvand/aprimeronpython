from scitools.std import *
import time

n = 5                 # no of points along the x axis
def f(x):
    return x**3       # sample function

dx = 1./(n-1)         # spacing between x points
pairs = []            # list of all [x,y] pairs
xlist = []            # list of all x coordinates
ylist = []            # list of all y coordinates
for i in range(n):
    x = i*dx;  y = f(x)
    pairs.append([x, y])
    xlist.append(x)
    ylist.append(y)

pairs
xlist
ylist

# alternative, more compact programming with list comprehension:
xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]
pairs = [[x, y] for x, y in zip(xlist, ylist)]

from numpy import *
a = zeros(n)           # array of n zeros
x2 = array(xlist)      # turn list x into array x2
y2 = array(ylist)
x2
y2

# alternatively, compute arrays directly:
n = len(x2)
x2 = linspace(0, 1, n)   # n numbers from 0 to 1
y2 = zeros(n)
for i in range(n):
    y2[i] = f(x2[i])

# direct calculation on complete arrays (all elements):
y2 = f(x2)
y2

Cdegrees = [-30 + i*10 for i in range(3)]
Fdegrees = [9./5*C + 32 for C in Cdegrees]
table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print table
table2 = array(table)    # turn list into array
print table2
table2
table2.shape
table[1][0]     # table[1] is [-20,4], whose index 0 holds -20
table2[1,0]     # common indexing
table2[1][0]    # this works too

for i in range(table2.shape[0]):
    for j in range(table2.shape[1]):
        print 'table2[%d,%d] = %g' % (i, j, table2[i,j])

table2[0:table2.shape[0], 1]  # 2nd column (index 1)
table2[0:, 1]                 # same
table2[:, 1]                  # same


# sin(x):
points = 9, 17, 65   # tuple with points
for n in points:
    x = linspace(0, 4*pi, n)
    y = sin(xi)
    plot(x, y, title='sin(x) with %d points' % n,
         hardcopy='tmp_%dp.eps' % n)
    time.sleep(0.2)  # pause

# Heaviside function:
def H(x):
    if x < 0:
        return 0
    else:
        return 1

# demonstrate that this function is not vectorized:
x = linspace(-4, 4, 4)
y = H(x)
plot(x, y)

# we must either use an explicit loop over x[i] points
# or we may turn H into a vectorized function using numpy.vectorize:
Hv = vectorize(H)

points = 3, 9, 101, 501
for n in points:
    x = linspace(-4, 4, n)
    y = Hv(x)
    plot(x, y, title='Heaviside function with %d points' % n,
         axis=[x[0], x[-1], -0.1, 1.1],
         hardcopy='tmp_H%d.eps' % n)

x = [-4, 0, 0, 4]
y = [0, 0, 1, 1]
lines = plot(x, y, axis=[x[0], x[-1], -0.1, 1.1], hardcopy='tmp_Hsmart.eps')
#import pprint
#pprint.pprint(lines[0].get())


