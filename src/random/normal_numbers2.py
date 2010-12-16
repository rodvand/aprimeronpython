from scitools.std import *
N = int(sys.argv[1]); m = float(sys.argv[2]); s = float(sys.argv[3])
random.seed(12)
samples = random.normal(m, s, N)
x, y = compute_histogram(samples, 20, piecewise_constant=True)
print mean(samples), std(samples)
plot(x, y)
title('%d samples of Gaussian/normal numbers on (0,1)' % N)
hardcopy('tmp.eps')


