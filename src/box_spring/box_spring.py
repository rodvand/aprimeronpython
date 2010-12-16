def init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N):
    import getopt, sys
    try:
        options, args = getopt.getopt(
            sys.argv[1:], '', 
            ['m=', 'mass=',
             'b=', 'boxheight=',
             'L=', 'spring-length=',
             'k=', 'spring-stiffness=',
             'beta=', 'spring-damping=',
             'S0=', 'initial-position=',
             'dt=','timestep=',
             'g=', 'gravity=',
             'w=', 
	     'N='])
    except getopt.GetoptError, e:
        print 'Error in command-line option:\n', e
        sys.exit(1)

    for option, value in options:
        if option in ('--m', '--mass'):
            m = float(value)
        elif option in ('--b', '--boxheight'):
            b = float(value)
        elif option in ('--L', '--spring-length'):
            L = float(value)
        elif option in ('--k', '--spring-stiffness'):
            k = float(value)
        elif option in ('--beta', '--spring-damping'):
            beta = float(value)
        elif option in ('--S0', '--initial-position'):
            S0 = float(value)
        elif option in ('--dt', '--timestep'):
            dt = float(value)
        elif option in ('--g', '--gravity'):
            g = float(value)
        elif option in ('--w',):
            w_formula = value  # string
        elif option == '--N':
            N = int(value)

    from scitools.StringFunction import StringFunction
    w = StringFunction(w_formula, independent_variables='t')
    return m, b, L, k, beta, S0, dt, g, w, N


def solve(m, k, beta, S0, dt, g, w, N,
          user_action=lambda S, time, time_step_no: None):
    """Calculate N steps forward. Return list S."""
    S = [0.0]*(N+1)      # output list
    gamma = beta*dt/2.0  # short form
    t = 0
    S[0] = S0
    user_action(S, t, 0)
    # special formula for first time step:
    i = 0
    S[i+1] = (1/(2.0*m))*(2*m*S[i] - dt**2*k*S[i] + 
             m*(w(t+dt) - 2*w(t) + w(t-dt)) + dt**2*m*g)
    t = dt
    user_action(S, t, i+1)

    # time loop:
    for i in range(1,N):
        S[i+1] = (1/(m + gamma))*(2*m*S[i] - m*S[i-1] +
                                  gamma*dt*S[i-1] - dt**2*k*S[i] +
                                  m*(w(t+dt) - 2*w(t) + w(t-dt))
                                  + dt**2*m*g)
        t += dt
        user_action(S, t, i+1)
        
    return S

def _test():
    def print_S(S, t, step):
        print 't=%.2f  S[%d]=%+g' % (t, step, S[step])

    # default values:
    from math import pi
    m = 1; b = 2; L = 10; k = 1; beta = 0; S0 = 1;
    dt = 2*pi/40; g = 9.81; w_formula = '0'; N = 80; 

    m, b, L, k, beta, S0, dt, g, w, N = \
       init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N)
    S = solve(m, k, beta, S0, dt, g, w, N,
              user_action=print_S)

if __name__ == '__main__':
    _test()

