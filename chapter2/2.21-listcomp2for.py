"""
Convert nested list comprehensions
to nested standard loops
"""
# q = [r**2 for r in [10**i for i in range(5)]]

r = []
s = []
for i in range(5):
    r.append(10**i)

for j in range(len(r)):
    s.append(r[j] ** 2)

print s
