import sys

try:
    n = int(sys.argv[1]) # n dice
    i = int(sys.argv[2]) # i experiments
except:
    print '''Usage: python %s n i
n - number of dice
i - number of experiments to run''' % sys.argv[0]


def one6(n):
    return 1./6.*n - (n-1)/36. # Exact probability

def throw_die():
    import random
    return random.randint(1,6)

j = 0
match = 0
while j < i:
    hit = False
    for k in range(n):
        die = throw_die()
        if die == 6:
            hit = True
    if hit:
        match +=1
    j += 1

print "Probability for at least one six when throwing %g dice is %.f percent (%g throws)" % (n, float(match)/i*100, i)

'''
Unix>python one6_2dice.py 2 100000
Probability for at least one six when throwing 2 dice is 31 percent (100000 throws)
'''
