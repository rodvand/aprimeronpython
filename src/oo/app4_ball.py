"""Solve an ODE system for the trajectory of a ball."""

from ODESolver import *
from scitools.std import *

def f(u, t):
    x, vx, y, vy = u
    g = 9.81
    return [vx, 0, vy, -g]

v0 = 5
theta = 80*pi/180
u0 = [0, v0*cos(theta), 0, v0*sin(theta)]
T = 1.2; dt = 0.01
method = ForwardEuler(f, dt)
method.set_initial_condition(u0)
u, t = method.solve(T)
x_values = u[:,0]  # or array([x for x, vx, y, vy in u])
y_values = u[:,2]  # or array([y for x, vx, y, vy in u])

# plot only the points on the curve above the x axis:
y_gt_0 = y_values >= 0
y_values = y_values[y_gt_0]
x_values = x_values[y_gt_0]
t = t[y_gt_0]

def exact(x):
    g = 9.81
    y0 = u0[2]  # get y0 from the initial values
    return x*tan(theta) - g*x**2/(2*v0**2)*1/(cos(theta))**2 + y0

plot(x_values, y_values, 'r',
     x_values, exact(x_values), 'b',
     legend=('numerical', 'exact'),
     title='dt=%g' % dt,
     hardcopy='tmp_ball.eps')
