def throw_die():
    import random
    return random.randint(1,6)

def get_prob(s, n):
    # Calculate probability for a win with n dice where sum is less than s
    i = 5000
    start = i
    win = 0.0
    while i > 0:
        i -= 1
        sum = 0.0
        for k in range(n):
            sum += throw_die()
        if sum < s:
            win += 1
    return (win/start)

def fair_game(s, n): # s = sum, n = number of dice
    r = int(1/get_prob(s, n))
    j = 0.0 # Number of times to run the experiment
    money = 1000
    win = 0.0
    while money > 0:
        money -= 1
        j += 1       
        sum = 0.0
        for i in range(n):
            sum += throw_die()
        if sum < s:
            money += r
            win += 1
        if j == 5000: # After 5000 throws we break no matter what
            break
    return r, money

print 'We start with 1000 units of money.' 
for i in range(10):
    result = fair_game(9, 4)
    print 'After 5000 throws we are left with %g money. The reward is %g units of money per win.' % (result[1], result[0])

'''
Unix>python sum_s_ndice_fair.py
We start with 1000 units of money.
After 5000 throws we are left with 680 money. The reward is 18 units of money per win.
After 5000 throws we are left with 986 money. The reward is 18 units of money per win.
After 5000 throws we are left with 240 money. The reward is 16 units of money per win.
After 5000 throws we are left with 403 money. The reward is 17 units of money per win.
After 5000 throws we are left with 1120 money. The reward is 20 units of money per win.
After 5000 throws we are left with 482 money. The reward is 18 units of money per win.
After 5000 throws we are left with 267 money. The reward is 17 units of money per win.
After 5000 throws we are left with 522 money. The reward is 17 units of money per win.
After 5000 throws we are left with 878 money. The reward is 18 units of money per win.
After 5000 throws we are left with 692 money. The reward is 17 units of money per win.
'''
