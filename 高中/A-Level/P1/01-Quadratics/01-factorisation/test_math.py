"""Independent lesson-specific assertions. Run: python test_math.py"""
from fractions import Fraction
from math_model import (expand_linear_factors, solve_monic_by_integer_factors,
                        square_partition, check_solutions, f)


def test():
    assert expand_linear_factors(1,-2,1,-3) == (1,-5,6)
    for x in [-10,-3,0,1,2,2.5,3,4,5,10]:
        assert abs((x*x-5*x+6)-f(x)) < 1e-10
    assert solve_monic_by_integer_factors(-5,6) == (2,3)
    assert solve_monic_by_integer_factors(6,9) == (-3,-3)  # repeated root
    assert solve_monic_by_integer_factors(0,-4) == (-2,2)
    for params in [(-4,2),(0,1)]:
        try:
            solve_monic_by_integer_factors(*params)
        except ValueError:
            pass
        else:
            raise AssertionError('Non-integral/nonreal-root case must be rejected')
    assert check_solutions()
    for x in (3,4,5,7.5):
        area=square_partition(x)
        assert abs(area['square']-area['right_strip']-
                   area['upper_strip']+area['overlap']-area['remaining']) < 1e-10
    for x in (0,2,2.999):
        try:
            square_partition(x)
        except ValueError:
            pass
        else:
            raise AssertionError('Area model restricted to x >= 3')
    assert f(2.5) == Fraction(-1,4)
    assert f(1)>0 and f(4)>0 and f(2.5)<0
    # A cancelled factor can discard a solution:
    assert (1-2)*(1-3) != 0 and f(2) == 0
    print('PASS: algebra expansion, integer-root cases, identity, area domain, roots, parabola signs, cancellation caveat')


if __name__=='__main__':
    test()
