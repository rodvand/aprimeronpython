"""
Implement the factorial function
"""

def fact(n):
    if n == 1 or n == 0:
        return n
    sum = 1
    while n > 1: 
        sum *= n
        n -= 1
    return sum

print fact(4)
