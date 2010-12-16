def random_walk_2D(np, ns, plot_step):
    xpositions = zeros(np)
    ypositions = zeros(np)
    moves = random.random_integers(1, 4, size=ns*np)
    moves.shape = (ns, np)

    # estimate max and min positions:
    xymax = 3*sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += where(this_move == NORTH, 1, 0)
        ypositions -= where(this_move == SOUTH, 1, 0)
        xpositions += where(this_move == EAST,  1, 0)
        xpositions -= where(this_move == WEST,  1, 0)

        # just plot every plot_step steps:
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[xymin, xymax, xymin, xymax],
                 title='%d particles after %d steps' % \
                       (np, step+1),
                 hardcopy='tmp_%03d.eps' % (step+1))
    return xpositions, ypositions

# main program:
from scitools.std import *
random.seed(11)

np = int(sys.argv[1])  # number of particles
ns = int(sys.argv[2])  # number of steps
plot_step = int(sys.argv[3])  # plot each plot_step step
x, y = random_walk_2D(np, ns, plot_step)
