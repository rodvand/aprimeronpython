import random
random.seed(42)
N = 500  # no of samples
x = range(N)
y = [random.uniform(-1,1) for i in x]
from scitools.easyviz import *
plot(x, y, '+', axis=[0,N-1,-1.2,1.2])
hardcopy('tmp.eps')
