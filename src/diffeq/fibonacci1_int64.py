import sys
from numpy import zeros, int64
N = int(sys.argv[1])
x = zeros(N+1, int64)  # (long is equivalent to int64)
x[0] = 1
x[1] = 1
for n in range(2, N+1):
    x[n] = x[n-1] + x[n-2]
    print n, x[n]
