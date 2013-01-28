"""
Write a Fahrenheit-Celsius conversion table
Create a table showing the Fahrenheit value,
the exact conversion to Celsius,
and the approximation value to Celsius
"""
def f2c_approx(F):
    return (F - 30.)/2.

def f2c_exact(F):
    return (F - 32) * 5. /9.
F = []
C = []
Ca = []
values = [F, C, Ca]
for i in range(0, 101, 10):
    F.append(i)
    C.append(f2c_exact(i))
    Ca.append(f2c_approx(i))

print "F\tC\tCa"                    # The heading

for i in range(len(F)):             # We know how long our lists are
    print "\t"                      
    for j in values:
        print "%d\t" % j[i],        # Print each row. Comma means no newline

print ""                            # To get a clean finish

"""
Running program
Unix>python 2.20-f2c_shortcut_table.py
F	C	Ca
	
0	-17	-15		
10	-12	-10		
20	-6	-5		
30	-1	0		
40	4	5		
50	10	10		
60	15	15		
70	21	20		
80	26	25		
90	32	30		
100	37	35	
"""