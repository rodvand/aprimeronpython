p = 5       # Interest rate %
A = 1000    # Initial amount
years = 3   # Number of years to grow

# Formula for calculating sum: A(1 + p/100)^n
# To avoid integer division we convert p to float
sum = A * (1 + (float(p)/100))**years

print "After %g years with %g%% interest rate and an initial amount of %g we have %g." % (years, p, A, sum)

"""
Unix>python interest_rate.py 
After 3 years with 5% interest rate and an initial amount of 1000 we have 1157.63.
"""
