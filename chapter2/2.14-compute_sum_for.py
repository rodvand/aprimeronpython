"""
Rewrite Exc 2.12 to use a for loop
instead of the while. See 2.12
for original code
"""
s = 0; k = 1; M = 100

for i in range(k, M + 1):
    s += 1./i
print s

"""
Running program
Unix>python 2.14-compute_sum_for.py
5.18737751764
"""