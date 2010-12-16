from scitools.std import *
xr = random.uniform(0, 2, 500)
yr = random.uniform(0, 2.4, 500)
x = linspace(0, 2, 51)
y = 2 + x**2*exp(-0.5*x)*sin(pi*x)
plot(x, y, 'r', xr, yr, 'o', hardcopy='tmp.eps')
