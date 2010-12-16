from scitools.std import *
N = int(sys.argv[1])
# random is now numpy.random
random.seed(12)
# vectorized generation of random numbers:
samples = random.random(size=N)
x, y = compute_histogram(samples, nbins=20)
plot(x, y, title='%d samples of uniform numbers on [0,1)' % N)
hardcopy('tmp.eps')


