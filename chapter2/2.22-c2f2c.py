"""
Write a Fahrenheit-Celsius conversion function
"""

def C(F):
    return (5.0/9.0)*(F-32)

def F(C):
    return (C * 9.) / 5. + 32
f = 100
if C(f) == F(C(f)):
    print "ok"
print C(f), F(C(f))
