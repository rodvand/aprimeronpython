"""
Write the program in Exec 2.12 as a function
"""

def s(M):
    s = 0;
    k = 1;
    while k <= M:
        s += 1./k
        k += 1
    return s

print s(3)

"""
Running program
Unix>python 2.24-compute_sum_func.py
1.83333333333
"""