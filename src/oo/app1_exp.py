from ODESolver import *
from scitools.std import *

def f(u, t):
    return u

T = 3
dt = 0.1
method = ForwardEuler(f, dt)
method.set_initial_condition(1.0)
u, t = method.solve(N)
plot(t, u)

# test more dt values and plot:
figure()
for dt in 0.1, 0.5, 1:
    m = ForwardEuler(f, dt)
    m.set_initial_condition(1)
    u, t = m.solve(T)
    plot(t, u)
    legend('dt=%g' % dt)
    hold('on')

t = linspace(0, T, 41)   # finer resolution
u_exact = exp(t)
plot(t, u_exact)
legend('exact')
title("u'=u solved by the Forward Euler method")
hardcopy('tmp_uexp1.eps')

# test ForwardEuler vs RungeKutta4:
dt = 1
figure()
for Method_class in ForwardEuler, RungeKutta4:
    method = Method_class(f, dt)
    method.set_initial_condition(1)
    u, t = method.solve(T)
    plot(t, u)
    legend('%s' % method.__name__)
    hold('on')

t = linspace(0, T, 41)  # finer resolution
plot(t, u_exact)
legend('exact')
title("u'=u solved numerically")
hardcopy('tmp_uexp2.eps')
