"""
Index the nested list to get
1) The letter a
2) The list ['d', 'e', 'f']
3) The last element
4) The d element

Explain why q[-1][-2] is the value g
    With - we just move left instead of the conventional
    right. So we move to the last element with [-1], 
    and in that element we move to the left twice.
    And with a list containing only two elements,
    the result will be that [-2] is the same as
    [0]
"""
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

# 1)
print q[0][0]

# 2)
print q[1]

# 3)
print q[-1][-1]

# 4)
print q[1][0]

"""
Running program
Unix>python 2.15-index_nested_list.py
a
['d', 'e', 'f']
h
d
"""