import random

def ballsfromhat():
    # The colours and their respective number of balls
    balls = {"red":10,
            "blue":10,
            "purple":10,
            "green":10,
            "black":10,
            "green":10,
            "white":10}
    # Create a new empty one to keep the drawn values
    drawn = dict.fromkeys(balls.keys(), 0) 

    todraw = 10 # We wish to draw ten balls from the hat
    for i in range(todraw):
        rball = random.choice(balls.keys())
        # Decrease and increase our dictionaries
        balls[rball] -= 1
        drawn[rball] += 1

    return drawn

tests = 10000
match = 0
for i in range(tests):
   r = ballsfromhat()

   if r["blue"] == 2 and r["purple"] == 2:
       match += 1

print 'From %g runs, we get two blue and purple balls %g times. Probability: %g%%' % (tests, match, (match/float(tests))*100)

"""
Running the program
Unix>python 4balls_from10.py 
From 10000 runs, we get two blue and purple balls 844 times. Probability: 8.44%
"""
