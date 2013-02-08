"""
Express a step function as a python function
"""

def H(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

print H(-0.5)
print H(0)
print H(10)

"""
Running program
Unix>python 2.36-Heaviside.py
0
1
1
"""