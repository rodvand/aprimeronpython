N = int(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])

import random as random_number
random_number.seed(12)   # for debugging/testing
from scitools.std import *

samples = [random_number.normalvariate(m, s) for i in range(N)]
x, y = compute_histogram(samples, 20, piecewise_constant=True)

print mean(samples), std(samples)
plot(x, y)
title('%d samples of Gaussian random numbers on (0,1)' % N)
hardcopy('tmp.eps')


