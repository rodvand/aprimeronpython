"""
Implement the sum function
"""

def sum(list):
    s = 0
    for element in list:
        s += element
    return s
print sum([1,3,5,-5])

"""
Running program
Unix>python 2.41-sum.py
4
"""