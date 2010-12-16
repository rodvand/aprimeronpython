import sys
from numpy import zeros, float96
N = int(sys.argv[1])
x = zeros(N+1, float96)  # or long
x[0] = 1
x[1] = 1
for n in range(2, N+1):
    x[n] = x[n-1] + x[n-2]
    print n, x[n]
