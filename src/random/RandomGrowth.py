class RandomGrowth:
    def __init__(self):
        self.simulations = None
        self.gamma_method = 1

    def compute_next_gamma(self):
        pass
    
    def simulate_one_path(N, x0, p0, M, m):
        x = zeros(N+1)
        p = zeros(N+1)
        index_set = range(0, N+1)

        x[0] = x0
        p[0] = p0

        for n in index_set[1:]:
            x[n] = x[n-1] + p[n-1]/(100.0*12)*x[n-1]

            # update interest rate p:
            r = random_number.randint(1, M)
            if r == 1:
                # adjust gamma:
                r = random_number.randint(1, 2)
                gamma = m if r == 1 else -m
            else:
                gamma = 0
            pn = p[n-1] + gamma
            p[n] = pn if 1 <= pn <= 15 else p[n-1]
        return x, p

    def simulate_one_path2(N, x0, p0, M, m):
        x = zeros(N+1)
        p = zeros(N+1)
        index_set = range(0, N+1)

        x[0] = x0
        p[0] = p0
        gamma_prev = 0

        for n in index_set[1:]:
            x[n] = x[n-1] + p[n-1]/(100.0*12)*x[n-1]

            # update interest rate p:
            r = random_number.randint(1, M)
            if r == 1:
                # adjust gamma:
                if gamma_prev == 0:
                    # first time, equally probable with
                    # +m and -m adjustment:
                    r = random_number.randint(1, 2)
                    gamma = m if r == 1 else -m
                else:
                    r = random.random()
                    if gamma_prev < 0:
                        # 80% chance for -m:
                        gamma = -m if r <= 0.8 else m
                    elif gamma_prev > 0:
                        # 80% chance for +m:
                        gamma = +m if r <= 0.8 else -m
                gamma_prev = gamma
            else:
                gamma = 0
            pn = p[n-1] + gamma
            p[n] = pn if 1 <= pn <= 15 else p[n-1]
        return x, p


    def plot_path(self, data, title, fig_no):
        figure(fig_no)
        plot(data, title=title)
        hold('on')

    
    def simulate_n_paths_minstorage(n, N, x0, p0, M, m):
        xm = zeros(N+1)  # mean of x
        pm = zeros(N+1)  # mean of p
        xs = zeros(N+1)  # standard deviation of x
        ps = zeros(N+1)  # standard deviation of p
        for i in range(n):
            x, p = simulate_one_path(N, x0, p0, M, m)
            # accumulate paths:
            xm += x
            pm += p
            xs += x**2
            ps += p**2

            # show 5 random sample paths:
            if i % (n/5) == 0:
                self.plot_path(x, 'sample paths of investment', 1)
                self.plot_path(p, 'sample paths of interest rate', 2)
        figure(1); hardcopy('tmp_sample_paths_investment.eps')
        figure(2); hardcopy('tmp_sample_paths_interestrate.eps')

        # compute average:
        xm /= float(n)
        pm /= float(n)
        # compute standard deviation:
        xs = xs/float(n) - xm*xm  # variance
        ps = ps/float(n) - pm*pm  # variance
        # remove small negative numbers (round off errors):
        print 'min variance:', xs.min(), ps.min()
        xs[xs < 0] = 0
        ps[ps < 0] = 0
        xs = sqrt(xs)
        ps = sqrt(ps)
        return xm, xs, pm, ps

    def simulate_n_paths_maxstorage(n, N, x0, p0, M, m):
        self.simulations = zeros((n, N+1, 2))
        for i in range(n):
            x, p = simulate_one_path(N, x0, p0, M, m)
            self.simulations[i,:,0] = x
            self.simulations[i,:,1] = p

        # show 5 random sample paths:
        for i in range(0, n, n/5):
            self.plot_path(x, 'sample paths of investment', 1)
            self.plot_path(p, 'sample paths of interest rate', 2)
        figure(1); hardcopy('tmp_sample_paths_investment.eps')
        figure(2); hardcopy('tmp_sample_paths_interestrate.eps')

        # compute average:
        xm = mean(self.simulations[:,:,0], axis=1)
        pm = mean(self.simulations[:,:,1], axis=1)
        # compute standard deviation:
        xs = std(self.simulations[:,:,0], axis=1)
        ps = std(self.simulations[:,:,1], axis=1)

        return xm, xs, pm, ps

from scitools.std import *
import random as random_number
import sys
random_number.seed(1)

x0 = 1                   # initial investment
p0 = 5                   # initial interest rate
N = 10*12                # number of months
M = 3                    # p changes (on average) every M months
n = 1000                 # number of simulations
m = 0.5                  # adjustment of p

# verify:
x, p = simulate_one_path(3, 1, 10, M, 0)
print '3 months with p=10:', x

xm, xs, pm, ps = simulate_n_paths(n, N, x0, p0, M, m)
figure(3)
months = range(len(xm))  # indices along x axis
plot(months, xm, 'r',
     months, xm-xs, 'y',
     months, xm+xs, 'y',
     title='Mean +/- 1 st.dev. of investment',
     hardcopy='tmp_mean_investment.eps')
figure(4)
plot(months, pm, 'r',
     months, pm-ps, 'y',
     months, pm+ps, 'y',
     title='Mean +/- 1 st.dev. of annual interest rate',
     hardcopy='tmp_mean_interestrate.eps')

