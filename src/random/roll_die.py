import random as random_number
import sys
N = int(sys.argv[1])   # perform N experiments
M = 0                  # no of times we get 6 eyes
for i in xrange(N):
    outcome = random_number.randint(1, 6)
    if outcome == 6:
        M += 1
print 'Got six %d times out of %d' % (M, N)


