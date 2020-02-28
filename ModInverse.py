

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
    while (x != 0):
        if (x < y) and (x != 1):
            x, y = switched(x, y)
        if (x == 1 or y == 0):
            if swapped:
                return (x, eqs[x][1], eqs[x][0])
            return (x, eqs[x][0], eqs[x][1])
        scaleBy = (x // y)
        eqs[x % y] = (eqs[x][0] - scaleBy * eqs[y][0], eqs[x][1] - scaleBy * eqs[y][1])
        x = x % y
    if swapped:
        return (y, eqs[y][1], eqs[y][0])
    return (y, eqs[y][0], eqs[y][1])

