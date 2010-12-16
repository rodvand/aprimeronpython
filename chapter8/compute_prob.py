# Exercise 8.2
# Probability of getting a number (0.5, 0.6)

from random import random

def prob(start, stop, N):
    i = 0 # N must be positive
    match = 0
    while i <= N:
        ran = random()
        if ran > start and ran < stop: # Not including the start and stop point
            match += 1
        i += 1
    print "Probability that the values lies between %g and %g is %g percent." % (start, stop, float(match)/N*100)

i = [1, 2, 3, 6]

for j in i:
    prob(0.5, 0.6, 10**j)


'''
Unix>python compute_prob.py
Probability that the values lies between 0.5 and 0.6 is 0 percent.
Probability that the values lies between 0.5 and 0.6 is 9 percent.
Probability that the values lies between 0.5 and 0.6 is 11.2 percent.
Probability that the values lies between 0.5 and 0.6 is 10.0365 percent.
'''
