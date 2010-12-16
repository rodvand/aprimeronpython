from numpy import random, sum
import sys
N = int(sys.argv[1])
eyes = random.randint(1, 7, N)
success = eyes == 6  # True/False array
M = sum(success)     # treats True as 1, False as 0
print 'Got six %d times out of %d' % (M, N)
