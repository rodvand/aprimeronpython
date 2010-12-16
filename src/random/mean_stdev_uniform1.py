import sys
N = int(sys.argv[1])
import random as random_number
from math import sqrt
sm = 0; sv = 0
for q in range(1, N+1):
    x = random_number.uniform(-1, 1)
    sm += x
    sv += x**2

    # write out mean and st.dev. 10 times in this loop:
    if q % (N/10) == 0:
        xm = sm/q
        xs = sqrt(sv/q - xm**2)
        print '%10d mean: %12.5e  stdev: %12.5e' % (q, xm, xs)


