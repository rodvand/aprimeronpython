"""
As uniform_numbers1.py but the histogram is plotted both as a piecewise
constant curve and a piecewise linear curve. The number of bins is
read from the command line.
"""
from scitools.std import *
N = int(sys.argv[1])
nbins = int(sys.argv[2])
random.seed(12)
# vectorized generation of random numbers:
samples = random.random(size=N)
x1, y1 = compute_histogram(samples, nbins, piecewise_constant=True)
x2, y2 = compute_histogram(samples, nbins, piecewise_constant=False)
plot(x1, y1, 'r', x2, y2, 'b')
title('%d samples of uniform numbers on (0,1)' % N)
hardcopy('tmp.eps')


