#!/usr/bin/python
"""
Note that the final answer is formatted for prettiness
not accurateness. So you could add a %f and get a more accurate
value
"""

print '------------------'      # table heading
F = 0                           # start value for F
dC = 10                         # increment of F in loop
print "F\tC  "                  # print heading
while F <= 100:                 
    C = ((F - 32) * 5.0) / 9.0      
    print "%d\t%d" % (F, C)     # format the string 
    F = F + dC                
print '------------------'     

"""
Running the program
Unix>python c2f_table_while.py
------------------
F	C  
0	-17
10	-12
20	-6
30	-1
40	4
50	10
60	15
70	21
80	26
90	32
100	37
------------------
"""
