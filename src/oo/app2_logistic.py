from ODESolver import *
from scitools.std import *

v0 = 0.05
dtau = 0.05
T = 10
method = RungeKutta4(lambda v, tau: v*(1-v), dtau)
method.set_initial_condition(v0)
v, tau = method.solve(T)
plot(tau, v, title='Scaled logistic equation',
     hardcopy='tmp_logistic.eps')

def ut(alpha, R):
    return alpha*tau, R*v

figure()
for alpha in linspace(0.2, 1, 5):
    t, u = ut(alpha, R=1)
    plot(t, u, legend='alpha=%g' % alpha)
    hold('on')
axis([0, T, 0, 1.1])
hardcopy('tmp_logistic_u.eps')
