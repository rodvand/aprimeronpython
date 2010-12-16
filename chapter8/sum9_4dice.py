def throw_die():
    import random
    return random.randint(1,6)

money = 100
startMoney = money
n = 4 # Number of times to throw the die
win = 0.0
j = 0.0
while money > 0:
    j += 1
    money -= 1 # Pay 1 to play
    sum = 0    
    for i in range(n):
        sum += throw_die()
    if sum < 9:
        win += 1
        money += 10
    if j == 1000: # We break to get out of the loop
        break

print 'Starting with %g money and %g dice, after %g throws we\'re left with %g money. Number of times we had a sum less than 9: %g. Probability for getting a sum less than 9 after %g throws: %g' % (startMoney, n, j, money, win, j, (win/j)*100)

'''
Unix>python sum9_4dice.py
Starting with 100 money and 4 dice, after 360 throws we're left with 0 money. Number of times we had a sum less than 9: 26. Probability for getting a sum less than 9 after 360 throws: 7.22222
'''
