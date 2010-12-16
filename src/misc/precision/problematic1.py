from scitools.std import *

def f(x):
    return (x-1)**6

def g(x):
    return 15*x**2 - 6*x - 20*x**3 + 15*x**4 - 6*x**5 + x**6 + 1

x = linspace(0.999, 1.001, 101)  # coordintes

f1 = f(x)
g1 = g(x)
f2 = f1.astype(float32)   # round-off only a problem with 32 bit floats...
g2 = g1.astype(float32)
plot(x, f2, x, g2, 'b', legends=('simple', 'expanded'))



