Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Fdegrees = []              # start with empty list
for C in Cdegrees:
    F = (9.0/5)*C + 32
    Fdegrees.append(F)

# list comprehension:
Fdegrees = [(9.0/5)*C + 32 for C in Cdegrees]

print Fdegrees  # check

# print table:
print '    C    F'         # table headline
for i in range(len(Cdegrees)):
    print '%5.0f %5.1f' % (Cdegrees[i], Fdegrees[i])

# more Pythonic print:
print '    C    F'         # table headline
for C, F in zip(Cdegrees, Fdegrees):
    print '%5.0f %5.1f' % (C, F)

# table data as nested lists:
Cdegrees = range(-20, 41, 5)   # -20, -15, ..., 35, 40
Fdegrees = [(9.0/5)*C + 32 for C in Cdegrees]
table = [Cdegrees, Fdegrees]
print 'column 1 (C):', table[0]
print 'column 2 (F):', table[1]
print '5th row, 2nd column: table[1][4] =', table[1][4]

# table data with rows as first index (the standard way):
table = []
for C, F in zip(Cdegrees, Fdegrees):
    table.append([C, F])
print 'table:', table

# alternative construction of table using list comprehension:
table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]

import pprint
pprint.pprint(table)

for C, F in table:
    print '%5.0f %5.1f' % (C, F)

# build the formatted table as a list strings:
lines = ['%5.0f %5.1f' % (C, F) for C, F in table]
lines.insert(0, '    C    F')  # headline
pprint.pprint(lines)

for line in lines:
    print line

# slices:
table[4:]    # extract positive C degrees pairs [C,F]

for C, F in table[Cdegrees.index(10):Cdegrees.index(35)]:
    print '%5.0f %5.1f' % (C, F)

