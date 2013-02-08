"""
Find the max/min elements in a list.
"""

def max(a):
    maximum = a[0]
    for element in a[1:]:
        if element > maximum:
            maximum = element
    return maximum

def min(a):
    minimum = a[0]
    for elem in a[1:]:
        if elem < minimum:
            minimum = elem
    return minimum
