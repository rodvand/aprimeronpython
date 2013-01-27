"""
What type of objects are i and j?
"""
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

for i in q:
    for j in range(len(i)):
        print i[j]

"""
Answer: i is a list object
        j is a list element
"""

"""
Running program
Unix>python 2.16-nested_list_iter.py
a
b
c
d
e
f
g
h
"""