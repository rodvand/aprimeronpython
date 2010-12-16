from numpy import random
import sys
N = int(sys.argv[1])
ndice = 4
M = 0
eyes = random.randint(1, 7, (N, ndice))
six = [6 for i in range(ndice)]
for i in range(N):
    # check experiment no. i:
    compare = eyes[i,:] == six
    if sum(compare) == ndice:
        M += 1
p = float(M)/N
print 'probability:', p


