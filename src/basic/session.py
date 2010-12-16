def F(C):
    return (9./5)*C + 32

a = 10
F1 = F(a)
F2 = F(15.5)
print F1, F2

Cdegrees = [10, 30, 60]
Fdegrees = [F(C) for C in Cdegrees]
Fdegrees


def F2(C):
    F_value = (9.0/5)*C + 32
    return '%.1f degrees Celsius corresponds to '\
           '%.1f degrees Fahrenheit' % (C, F_value)

s1 = F2(21)
s1
c1 = 37.5
s2 = F2(c1)
F_value
C


def F3(C):
    F_value = (9.0/5)*C + 32
    print 'Inside F3: C=%s F_value=%s r=%s' % (C, F_value, r)
    return '%.1f degrees Celsius corresponds to '\
           '%.1f degrees Fahrenheit' % (C, F_value)

C = 60    # make a global variable C
r = 21    # another global variable
s3 = F3(r)
s3
C

def F4(C):
    F_value = (9.0/5)*C + 32
    print locals()   # all local variables
    return F_value

F4(21)
import pprint
pprint.pprint(globals())  # all global variables





C = [-10, -5, 0, 5, 10, 15, 20, 25, 30]   # create a list
C.append(35)              # add new element 45 at the end
C                         # view list C
C = C + [40, 45]          # add another list to the end
C.insert(0, -15)          # insert new element -15 as index 0
C
del C[2]                  # delete 3rd element
C
del C[2]                  # delete what is now 3rd element
C
C.index(10)               # find index for an element (10)
10 in C                   # is 10 an element in C?
len(C)                    # length of list
C[-1]                     # view the last list element
C[-2]                     # view the next last list element

somelist = ['book.tex', 'book.log', 'book.pdf']
texfile, logfile, pdf = somelist
texfile
logfile
pdf

degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print 'list element:', C

print 'The degrees list has', len(degrees), 'elements'

degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print 'list element:', C
    print 'The degrees list has', len(degrees), 'elements'

for C in degrees:
    F = (9.0/5)*C + 32
    print '%5d %5.1f' % (C, F)

def F(C):
    return (9.0/5)*C + 32

Fdegrees = [F(C) for C in degrees]

import pprint, scitools.pprint2
somelist = [15.8, [0.2, 1.7]]
pprint. pprint(somelist)
scitools.pprint2.pprint(somelist)
scitools.pprint2.float_format = '%.2e'
scitools.pprint2.pprint(somelist)
[1.58e+01, [2.00e-01, 1.70e+00]]

from numpy import zeros
somelist = zeros((3,2,3,2)).tolist()
print 'Iterating over indices:'
for i1 in range(len(somelist)):
    for i2 in range(len(somelist[i1])):
        for i3 in range(len(somelist[i1][i2])):
            for i4 in range(len(somelist[i1][i2][i3])):
                value = somelist[i1][i2][i3][i4]
                print 'somelist[%d][%d][%d][%d]=%g' % (i1,i2,i3,i4,value)

print 'Iterating over sublists:'
for sublist1 in somelist:
    for sublist2 in sublist1:
        for sublist3 in sublist2:
            for sublist4 in sublist3:
                value = sublist4
                print 'value =', value


def yfunc(t):
    g = 9.81
    return v0*t - 0.5*g*t**2

yfunc(0.6)
# initialize global v0 variable:
v0 = 5
yfunc(0.6)


def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

t_values = [0.05*i for i in range(10)]
for t in t_values:
    pos, vel = yfunc(t, v0=5)
    print 't=%-10g position=%-10g velocity=%-10g' % (t, pos, vel)

def ytable(tmin, tmax, no_of_time_levels, v0):
    g = 9.81
    dt = (tmax - tmin)/(no_of_time_levels - 1)
    t = tmin
    ylist = []
    while t <= tmax:
        y = v0*t - 0.5*g*t**2
        ylist.append(y)
        t += dt
    return ylist

y = ytable(tmin=0, tmax=0.5, no_of_time_levels=3, v0=5)
import pprint
pprint.pprint(y)

def ytable(tmin, tmax, no_of_time_levels, v0):
    g = 9.81
    dt = (tmax - tmin)/(no_of_time_levels - 1)
    tlist = [dt*i for i in range(0, no_of_time_levels)]
    ylist = [v0*t - 0.5*g*t**2 for t in tlist]
    return tlist, ylist

t, y = ytable(tmin=0, tmax=0.5, no_of_time_levels=6, v0=5)
pprint.pprint(t)
pprint.pprint(y)
'%s' % t

print 'S:'

def S(x, epsilon=1.0E-6):
    term = 1
    sum = term
    while abs(term) > epsilon:
        term = -term*x
        sum += term
    return sum

x = 0.5
sum_approx = S(x, epsilon=1E-4)
sum_exact = 1.0/(1+x)
print sum_exact - sum_approx
   


t = 0; dt = 0.5; T = 3
while t <= T:
     print t, t <= T
     t += dt

print 'Final t:', t, '; t <= T is', t <= T

for elem in [10, 20, 25, 27, 28.5]:
    print elem

for elem in range(1, 4, 2):
    print elem

numbers = [0.25, 0.5, 1, 2, 4, 10]
numbers.append([20,30,40])
numbers
numbers[1]
del numbers[1]
numbers[1]      # a new element with index 1
numbers.insert(0, 'a text')
numbers
numbers[-1]     # last element is a new list
numbers[-1][1]  # indexing a nested list
import pprint
pprint.pprint(numbers)


numbers = range(10)
print numbers
for n in numbers:
    i = len(numbers)/2
    del numbers[i]
    print 'n=%d, del %d' % (n,i), numbers

# round-off
def float_eq(a, b):
    tolerance = 1.0E-15
    equal = abs(a-b) < tolerance
    return equal

a1=1/49.*49
b1=1/51.*51
print 'a1=%.16f, b1=%.16f' % (a1, b1)
float_eq(a1, b1)
a1-b1              # expect zero

a2=1000000/49.*49
b2=1000000/51.*51
print 'a2=%.16f, b2=%.16f' % (a2, b2)
float_eq(a2, b2)
a2-b2              # expect zero

def printlist(list_object, list_name='', line_length=70):
    output = ''
    for i in range(len(list_object)):
        output += '%s[%d]=%g ' % (list_name, i, list_object[i])
    import textwrap
    output = textwrap.wrap(output, width=line_length, 
                           break_long_words=False)
    # output is now a list of lines (strings)
    for line in output:
        print line


printlist([i*100 for i in range(50)], line_length=60)


# tuples:
t = (2, 4, 6, 'temp.pdf')
t = 2, 4, 6, 'temp.pdf'
for element in 'myfile.txt', 'yourfile.txt', 'herfile.txt':
    print element,

type(t)
isinstance(t, tuple)

def f(x):
    return x, x**2, x**4

s = f(2)
s
type(s)

t = t + (-1.0, -2.0)
t
t[1]
t[2:]
6 in t

t[1] = -1       # illegal - cannot change a tuple
t.append(0)     # illegal - cannot change a tuple
del t[1]        # illegal - cannot change a tuple
t.index         # illegal - no index method

def C2F(C):
    """Conversion of C degrees Celsius to Fahrenheit degrees."""
    return (9.0/5)*C + 32

def line(x0, y0, x1, y1):
    """
    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through two points (x0,y0) and (x1,y1).

    x0, y0: a point on the line (float).
    x1, y1: another point on the line (float).
    return: coefficients a, b (floats) for the line (y=a*x+b).
    """
    a = (y1 - y0)/float(x1 - x0)
    b = y0 - a*x0
    return a, b

print line.__doc__
a, b = line(1, -1, 4, 3)
a
b

# new line function with interactive session:
def line(x0, y0, x1, y1):
    """
    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through two points (x0,y0) and (x1,y1).

    x0, y0: a point on the line (float).
    x1, y1: another point on the line (float).
    return: coefficients a, b (floats) for the line (y=a*x+b).

    Example:
    >>> a, b = line(1, -1, 4, 3)
    >>> a
    1.3333333333333333
    >>> b
    -2.333333333333333
    """
    a = (y1 - y0)/float(x1 - x0)
    b = y0 - a*x0
    return a, b

print line.__doc__


def print_date():
    import time
    print time.strftime("%b %d, %Y")

# call:
print_date()

# keyword arguments:
from math import exp, sin, pi
def f(x, A=1, a=1, w=pi):
    return A*exp(-a*x)*sin(w*x)

f1 = f(0)
x2 = 0.1
f2 = f(x2, w=2*pi)
f3 = f(x2, w=4*pi, A=10, a=0.1)
f4 = f(w=4*pi, A=10, a=0.1, x=x2)



def diff2(f, x, h=1E-9):
    r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
    return r

def g(t):
    return t**(-6)

for k in range(1,15):
    h = 10**(-k)
    print 'h=%.0e: %.5f' % (h, diff2(g, 1, h))

