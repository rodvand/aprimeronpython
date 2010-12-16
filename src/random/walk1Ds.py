"""As walk1Dp.py but with computing statistics."""
from scitools.std import *
import random as random_number
import time
random_number.seed(11)

try:
    np = int(sys.argv[1])
    ns = int(sys.argv[2])
except IndexError:
    np = 100   # no of particles
    ns = 100   # no of steps

positions = zeros(np)            # all particles start at x=0
HEAD = 1;  TAIL = 2              # constants

xmax = sqrt(ns); xmin = -xmax    # initial extent of plot axis
y = positions.copy()             # y position is always 0
nbins = int(3*xmax)              # no of intervals in histogram
ymax_prev = 1                    # for axis in plot, prev. step
ymin = -0.1                      # min limit for y axis

for step in range(ns):
    for p in range(np):
        coin = random_number.randint(1,2)  # flip coin
        if coin == HEAD:
            positions[p] += 1   # one unit length to the right
        elif coin == TAIL:
            positions[p] -= 1   # one unit length to the left

    # statistics:
    mean_pos = mean(positions)
    stdev_pos = std(positions)

    pos, freq = compute_histogram(positions, nbins,
                                  piecewise_constant=True)


    # extend x axis limits?
    if min(positions) < xmin:  xmin -= 2*sqrt(ns)
    if max(positions) > xmax:  xmax += 2*sqrt(ns)

    # "intelligent" choice of y axis limits:
    # estimate ymax on the y axis from 1.1*max(freq)
    # (1.1 to get some space), do not change ymax
    # unless it deviates more than 0.1 from the previous
    # value, and let ymin = -0.1*ymax
    
    ymax = 1.1*max(freq)  # axis for freq
    if math.abs(ymax - ymax_prev) < 0.1:
        # do not change axis:
        ymax = ymax_prev
    else:
        # keep new value
        ymax_prev = ymax
        ymin = -0.1*ymax

    # graphical vertical lines for mean and +/- stdev:
    yminv, ymaxv = 0, ymax/1.1  # axis for vert. lines
    xmean, ymean   = [mean_pos, mean_pos],     [yminv, ymaxv]
    xstdv1, ystdv1 = [stdev_pos, stdev_pos],   [yminv, ymaxv]
    xstdv2, ystdv2 = [-stdev_pos, -stdev_pos], [yminv, ymaxv]

    plot(positions, y, 'ko3',     # particles as circles
         pos, freq, 'r',          # histogram
         xmean, ymean, 'r2',      # mean position as thick line
         xstdv1, ystdv1, 'b2',    # +1 standard dev.
         xstdv2, ystdv2, 'b2',    # -1 standard dev.
         axis=[xmin, xmax, ymin, ymax],
         title='random walk of %d particles after %d steps' % \
               (np, step+1))
    time.sleep(0.2)             # pause before next move
hardcopy('tmp.eps')
