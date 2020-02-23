from ModInverse import *


def testExtendedEuclid(x, y):
    dab = extendedEuclid(x, y)
    d = dab[0]
    a = dab[1]
    b = dab[2]
    assert(d == a * x + b * y)
    print(dab)


testExtendedEuclid(54, 17)
testExtendedEuclid(2, 3)
testExtendedEuclid(3, 2)
testExtendedEuclid(3, 3)
testExtendedEuclid(54, 2)
testExtendedEuclid(234, 32)