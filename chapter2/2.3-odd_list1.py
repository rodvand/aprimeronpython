"""
Generate odd numbers

Generate odd numbers from 1 to n
and store them in a list
"""

n = 9                   # The upper limit
start = 1               # Start at 1
odd = []

while start < n:
    odd.append(start)   # Add the number to the list
    start = start + 2   # To get odd number
print odd               # Print the list

"""
Running program
Unix>python odd_list1.py
[1, 3, 5, 7]
"""
