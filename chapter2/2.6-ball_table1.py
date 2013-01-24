"""
Make a table from formula (1.1)
"""

v = 5.0         # Initial velocity of the ball
g = 9.81        # Acceleration of gravity
t = 0.0         # Time

end = 2.0*(v / g)
i = 0
step = end/11

print "t\t\ty(t)"
while t < end:    
    y = (v * t) - (0.5 * g * t**2)
    print "%f\t%f" % (t, y)
    t += step    
