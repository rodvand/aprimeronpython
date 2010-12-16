from numpy import random, sum
random.seed(11)
import sys
N = int(sys.argv[1])      # no of experiments
ndice = int(sys.argv[2])  # no of dice
nsix = int(sys.argv[3])   # wanted no of dice with six eyes

eyes = random.randint(1, 7, (N, ndice))
compare = eyes == 6
nthrows_with_6 = sum(compare, axis=1)  # sum over columns (index 1)
nsuccesses = nthrows_with_6 >= nsix
M = sum(nsuccesses)
p = float(M)/N
print 'probability:', p

