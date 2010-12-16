import numpy

class ODESolver:
    """
    Superclass for numerical methods solving ODEs

      du/dt = f(u, t)

    Attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f, dt):
        # For ODE systems, f will often return a list, but
        # arithmetic operations with f in numerical methods
        # require that f is an array. Let self.f be a function
        # that first calls f(u,t) and then ensures that the
        # result is an array of floats:
        self.f = lambda u, t: numpy.asarray(f(u, t), float)
        self.dt = dt

    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError

    def set_initial_condition(self, u0, t0=0):
        self.u = []    # u[k] is solution at time t[k]
        self.t = []    # time levels in the solution process
        
        self.u.append(numpy.asarray(u0, float))
        self.t.append(float(t0))
        self.k = 0  # time level counter

    def solve(self, T, terminate=None):
        """
        Advance solution from t = t0 to t <= T, steps of dt
        as long as terminate(u,t,k) is False. 
        terminate(u,t,k) is a user-given function
        returning True or False. By default, a terminate
        function which always returns False is used.
        """
        if terminate is None:
            terminate = lambda u, t, k: False
        self.k = 0
        tnew = 0
        while tnew <= T and \
            not terminate(self.u, self.t, self.k):

            unew = self.advance()

            self.u.append(unew)
            tnew = self.t[-1] + self.dt
            self.t.append(tnew)
            self.k += 1
        return numpy.array(self.u), numpy.array(self.t)
    

class ForwardEuler(ODESolver):
    def advance(self):
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]

        unew = u[k] + dt*f(u[k], t)
        return unew

class RungeKutta4(ODESolver):
    def advance(self):
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t)
        K2 = dt*f(u[k] + 0.5*K1, t + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t + dt2)
        K4 = dt*f(u[k] + K3, t + dt)
        unew = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return unew

import sys, os
# need to import function Newton from ../diffeq/Newton.py:
sys.path.insert(0, os.path.join(os.pardir, 'diffeq'))
from Newton import Newton

class BackwardEuler(ODESolver):
    def __init__(self, f, dt):
        ODESolver.__init__(self, f, dt)
        # make a sample call to check that f is a scalar function:
        value = f(1,1)
        if not isinstance(value, (int, float)):
            raise ValueError\
            ('f(u,t) must return float/int, not %s' % type(value))

    # alternative implementation of F:
    #def F(self, w):
    #    return w - self.dt*self.f(w, self.t[-1]) - self.u[self.k]
    
    def advance(self):
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]

        def F(w):
            return w - dt*f(w, t) - u[k]

        dFdw = Derivative(F)
        w_start = u[k] + dt*f(u[k], t)
        unew, n, F_value = Newton(F, w_start, dFdw, N=30)
        if k == 0:
            self.Newton_iter = []
        self.Newton_iter.append(n)
        if n >= 30:
            print "Newton's failed to converge at t=%g "\
                  "(%d iterations)" % (t, n)
        return unew


class Derivative:
    def __init__(self, f, h=1E-9):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x-h))/(2*h)


# tests and verifications:

def _f1(u, t):
    return 0.2 + (u - _u_solution_f1(t))**5

def _u_solution_f1(t):
    """Exact u(t) corresponding to _f1 above."""
    return 0.2*t + 3

def _verify(f, exact):
    u0 = 3;  dt = 0.4;  T = 2.8
    for Method_class in ForwardEuler, RungeKutta4, BackwardEuler:
        method = Method_class(f, dt)
        method.set_initial_condition(u0)
        u, t = method.solve(T)
        print Method_class.__name__, ':\n', u
    u_exact = exact(t)
    print 'Exact:\n', u_exact
    print 'Backward Euler iterations:', method.Newton_iter

if __name__ == '__main__':
    _verify(_f1, _u_solution_f1)
    _verify(lambda u, t: 3*t*t, lambda t: 3 + t**3)

    
