"""
Equation:

       m*u'' + beta*u' + k*u = m*w''(t) + m*g

written as a 2x2 first-order ODE system and solved
by classes in the ODESolver hierarchy of methods.
"""

from ODESolver import *
from scitools.std import *

class OscSystem:
    def __init__(self, m, beta, k, g, w):
        self.m, self.beta, self.k, self.g, self.w = \
                float(m), float(beta), float(k), float(g), w

    def __call__(self, u, t):
        u0, u1 = u
        m, beta, k, g, w = \
           self.m, self.beta, self.k, self.g, self.w
        # use a finite difference for w''(t):
        h = 1E-5
        ddw = (w(t+h) - 2*w(t) + w(t-h))/(2*h)
        f = [u1, ddw  + g - beta/m*u1 - k/m*u0]
        return f

# test case: u = cos(t)
f = OscSystem(1.0, 0.0, 1.0, 0.0, lambda t: 0)
u_init = [1, 0]    # initial condition
T = 7*pi
for Method_class in ForwardEuler, RungeKutta4:
    # let ForwardEuler dt be 1/10 of the RungeKutta dt:
    if Method_class == ForwardEuler:
        dt = 2*pi/200
    elif Method_class == RungeKutta4:
        dt = 2*pi/20
    method = Method_class(f, dt)
    method.set_initial_condition(u_init)
    u, t = method.solve(T)

    # u is an array of [u0,u1] pairs for each time level,
    # get the u0 values from u for plotting:
    u0_values = u[:, 0]
    u1_values = u[:, 1]
    u0_exact = cos(t)
    u1_exact = -sin(t)
    figure()
    alg = Method_class.__name__  # (class) name of algorithm
    plot(t, u0_values, 'r-',
         t, u0_exact, 'b-',
         legend=('numerical', 'exact'),
         title='Oscillating system; position - %s' % alg,
         hardcopy='tmp_oscsystem_pos_%s.eps' % alg)
    figure()
    plot(t, u1_values, 'r-',
         t, u1_exact, 'b-',
         legend=('numerical', 'exact'),
         title='Oscillating system; velocity - %s' % alg,
         hardcopy='tmp_oscsystem_vel_%s.eps' % alg)
