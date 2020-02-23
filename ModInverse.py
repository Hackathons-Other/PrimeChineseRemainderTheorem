

def multInv(x, m):
    """ Find the multiplicative inverse of X mod M.
        The multiplicative inverse is A such that A * X = 1 mod M. """
    pass


def switched(x, y):
    """Returns Y, X."""
    return (y, x)


def extendedEuclid(x, y):
    """Returns d, a, b such that d is the gcd of X and Y and aX + bY = d. """
    swapped = False
    if x < y:
        swapped = True
        x, y = switched(x, y)
    eqs = {x: (1, 0),
           y: (0, 1)}
    while (x != 0 and x != 1):
        eqs[x - y] = (eqs[x][0] - eqs[y][0], eqs[x][1] - eqs[y][1])
        x -= y
        if (x < y) and (x != 1):
            x, y = switched(x, y)
        elif (x == 1 or y == 0):
            if swapped:
                return (x, eqs[x][1], eqs[x][0])
            return (x, eqs[x][0], eqs[x][1])
    if swapped:
        return (y, eqs[1][1], eqs[1][0])
    return (y, eqs[1][0], eqs[1][1])

