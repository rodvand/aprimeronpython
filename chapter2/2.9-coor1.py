"""
Generate equally spaced coordinates
between 1 and 2. Space should be 0.01
"""
x = 1
h = 0.01
xcoor = []

for i in range(0, 101):     # 101 to get to 2.00
    xi = i*h
    xcoor.append(x + xi)

"""
Running program
Unix>python 2.9-coor1.py
"""