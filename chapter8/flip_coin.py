import random

def flip(n):
    heads = 0
    while n > 0:
        flip = random.randint(1,2)
        n -= 1
        if flip == 1:
            print 'Head!'
            heads += 1
        else:
            print 'Tail!'
    print 'Number of heads: %g' % heads 

flip(20)

"""
Running the program
Unix>python flip_coin.py 
Head!
Head!
Head!
Head!
Tail!
Head!
Tail!
Head!
Tail!
Tail!
Head!
Tail!
Head!
Tail!
Head!
Tail!
Head!
Head!
Head!
Tail!
Number of heads: 12
"""
