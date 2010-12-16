
def ForwardEuler(f, dt, u0, T):
    """Integrate u'=f(u,t), u(0)=u0, in steps of dt until t=T."""
    u = []; t = []   # u[k] is the solution at time t[k]
    u.append(u0)
    t.append(0)
    n = int(round(T/dt))
    for k in range(n):
        unew = u[k] + dt*f(u[k], t[k])

        u.append(unew)
        tnew = t[-1] + dt
        t.append(tnew)
    return numpy.array(u), numpy.array(t)

import numpy
# Problem: u'=u
def f(u, t):
    return u

u0 = 1
T = 3
dt = 0.1
u, t = ForwardEuler(f, dt, u0, T)

# compare numerical solution and exact solution in a plot:
from scitools.std import plot, exp
u_exact = exp(t)
plot(t, u, 'r-', t, u_exact, 'b-',
     xlabel='t', ylabel='u', legend=('numerical', 'exact'),
     title="Solution of the ODE u'=u, u(0)=1")

# Accuracy check for decreasing dt:
for dt in 0.5, 0.05, 0.005:
    u, t = ForwardEuler(f, dt, u0, T)
    print 'dt=%.5f, u(%g)=%.6f, error=%g' % \
          (dt, t[-1], u[-1], exp(t[-1]-u[-1]))
    
