t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

def y(t):
    # formula 1.1 - find the vertical position of a ball at a specific (t) time
    v0 = 5 # initial velocity
    g = 9.81 # gravity 
    
    return (v0*t)- (0.5*g*(t**2))

# calculate the y for the different t values
y = [y(T) for T in t]

# save the two lists in one list

t1 = [t, y]

i = 0
print '---------------------'
print '|__t______|y(t)_____|'

# loop through our two lists and print the values
while i < len(t1[0]):
    tvalues = t1[0] # our t values
    yvalues = t1[1] # our y values        
    print '|  %g   |%4.4f    |' % (tvalues[i], yvalues[i])
    i = i + 1
print '---------------------'

# by using list comprehension we can mix the two values into new elements in our new list
t2 = [[T, Y] for T, Y in zip(t, y)]
print '---------]2[---------'
# we print the elements, we know that t is index 0 and y(t) is index 1 in each of our list elements
for T2 in t2:
    print '|  %g   |%4.4f    |' % (T2[0], T2[1])
print '---------------------'


'''
Unix> python ball_table3.py 
---------------------
|__t______|y(t)_____|
|  0.1   |0.4509    |
|  0.2   |0.8038    |
|  0.3   |1.0585    |
|  0.4   |1.2152    |
|  0.5   |1.2737    |
|  0.6   |1.2342    |
---------------------
---------]2[---------
|  0.1   |0.4509    |
|  0.2   |0.8038    |
|  0.3   |1.0585    |
|  0.4   |1.2152    |
|  0.5   |1.2737    |
|  0.6   |1.2342    |
---------------------
'''
