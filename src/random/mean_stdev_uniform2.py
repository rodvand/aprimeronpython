import sys
N = int(sys.argv[1])
from numpy import random, mean, var, std, sqrt
x = random.uniform(-1, 1, size=N)
xm = mean(x)
xv = var(x)
xs = std(x)
print '%10d mean: %12.5e  stdev: %12.5e' % (N, xm, xs)


