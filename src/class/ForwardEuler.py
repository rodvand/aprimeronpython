import numpy

class ForwardEuler:
    """
    Class for solving an ODE,

      du/dt = f(u, t)

    by the ForwardEuler method.
    
    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f, dt):
        self.f, self.dt = f, dt

    def set_initial_condition(self, u0, t0=0):
        self.u = []    # u[k] is solution at time t[k]
        self.t = []    # time levels in the solution process
        
        self.u.append(float(u0))
        self.t.append(float(t0))
        self.k = 0  # time level counter

    def solve(self, T):
        """Advance solution in time until t <= T."""
        tnew = 0
        while tnew <= T:
            unew = self.advance()
            self.u.append(unew)
            tnew = self.t[-1] + self.dt
            self.t.append(tnew)
            self.k += 1
        return numpy.array(self.u), numpy.array(self.t)

    def advance(self):
        """Advance the solution one time step."""
        # load attributes into local variables to
        # obtain a formula that is as close as possible
        # to the mathematical notation:
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]

        unew = u[k] + dt*f(u[k], t)
        return unew


def _f1(u, t):
    return 0.2 + (u - _u_solution_f1(t))**4

def _u_solution_f1(t):
    return 0.2*t + 3

def _verify_f1():
    u0 = 3;  dt = 0.4;  T = 3
    method = ForwardEuler(_f1, dt)
    method.set_initial_condition(u0, 0)
    u, t = method.solve(T)
    u_exact = _u_solution_f1(t)
    print 'Numerical:\n', u
    print 'Exact:\n', u_exact

class Logistic:
    """Problem class for a logistic ODE."""
    def __init__(self, alpha, R, u0):
        self.alpha, self.R, self.u0 = alpha, float(R), u0

    def __call__(self, u, t):
        """Return f(u,t) for the logistic ODE."""
        return self.alpha*u*(1 - u/self.R)

    def __str__(self):
        """Return ODE and initial condition."""
        return "u'(t) = %g*u*(1 - u/%g)\nu(0)=%g" % \
               (self.alpha, self.R, self.u0)
    
def logistic():
    problem = Logistic(0.2, 1, 0.1)
    T = 40
    dt = 0.1
    method = ForwardEuler(problem, dt)
    method.set_initial_condition(problem.u0, 0)
    u, t = method.solve(T)
    # note that import * is not legal inside functions so we
    # have to import each specific function:
    from scitools.std import plot, hardcopy, xlabel, ylabel, title
    plot(t, u)
    xlabel('t'); ylabel('u')
    title('Logistic growth: alpha=0.2, dt=%g, %d steps' \
          % (dt, len(u)-1))
    # compare with exponential growth:
    #from scitools.std import hold, linspace, exp
    #te = linspace(0, dt*N, N+1)
    #ue = 0.1*exp(0.2*te)
    #hold('on')
    #plot(te, ue)
    hardcopy('tmp.eps')
    
if __name__ == '__main__':
    import sys
    try:
        command = sys.argv[1]
    except IndexError:
        print 'provide a command (verify, logistic, ...)'
        sys.exit(1)
        
    if command == 'verify':
        _verify_f1()
    elif command == 'logistic':
        logistic()
    
