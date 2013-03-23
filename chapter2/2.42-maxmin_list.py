"""
Find the max/min elements in a list.
"""

def max(a):
    max_elem = a[0]
    for element in a[1:]:
        if element > max_elem:
            max_elem = element
    return max_elem

def min(a):
    minimum = a[0]
    for elem in a[1:]:
        if elem < minimum:
            minimum = elem
    return minimum
