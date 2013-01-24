from math import pi

g = 9.81                    # ms^-2
Vk = 120                    # velocity in km/h
V = Vk/3.6                  # velocity, we divided by 3.6 to get m/s
a = 0.11                    # radius of the football in m
A = pi*(a**2)               # cross-sectional area
Cd = 0.2                    # drag coeffisient
m = 0.43                    # mass (in kg)
q = 1.2                     # density of air (in kg m)
Fd = (0.5*Cd)*q*A*(V**2)    # drag force
Fg = m*g                    # gravity force
ratio = Fd/Fg               # drag force/gravity force

print '''
Velocity: %g km/h
Drag force: Fd = 1/2*Cd*q*AV^2 \tequals %.1f N
Gravity force: Fg = m*g \tequals %g * %g = %.1f N
Ratio drag force/gravity force: %.2f
''' % (Vk, Fd, m, g, Fg, ratio)

'''
Unix>python kick.py 

Velocity: 10 km/h
Drag force: Fd = 1/2*Cd*q*AV^2  equals 0.0 N
Gravity force: Fg = m*g         equals 0.43 * 9.81 = 4.2 N
Ratio drag force/gravity force: 0.01

Unix>python kick.py 

Velocity: 120 km/h
Drag force: Fd = 1/2*Cd*q*AV^2  equals 5.1 N
Gravity force: Fg = m*g         equals 0.43 * 9.81 = 4.2 N
Ratio drag force/gravity force: 1.20
'''

