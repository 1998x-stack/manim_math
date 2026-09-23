"""Pure-Python mathematical model for A-Level P1 / 1.1.
No Manim dependency. Polynomial coefficients are (a,b,c) in ax^2+bx+c.
"""
from fractions import Fraction


def expand_linear_factors(p: int, q: int, r: int, s: int):
    """Return coefficients of (p*x+q)(r*x+s)."""
    return p*r, p*s + q*r, q*s


def solve_monic_by_integer_factors(b: int, c: int):
    """Return ordered integer roots of x*x+b*x+c, if both are integers.

    Does not claim to factor all quadratics; nonintegral-root cases raise ValueError.
    """
    from math import isqrt
    delta = b*b-4*c
    if delta < 0 or isqrt(delta)**2 != delta:
        raise ValueError('This lesson method requires integer roots')
    d = isqrt(delta)
    roots = [Fraction(-b-d, 2), Fraction(-b+d, 2)]
    if any(root.denominator != 1 for root in roots):
        raise ValueError('This lesson method requires integer roots')
    return tuple(int(root) for root in roots)


def f(x):
    """The example polynomial in this video."""
    return (x-2)*(x-3)


def square_partition(x):
    """Area model for a square of side x with strips of widths 2 and 3.

    Only a *literal planar area model* when x >= 3. Algebraic identity
    x^2-5x+6=(x-2)(x-3) holds for every real x.
    """
    if x < 3:
        raise ValueError('Geometric strip widths must be nonnegative: x >= 3')
    return dict(square=x*x, right_strip=2*x, upper_strip=3*x,
                overlap=6, remaining=(x-2)*(x-3))


def check_solutions(roots=(2, 3)):
    assert tuple(roots) == (2,3)
    assert all(f(root) == 0 for root in roots)
    return True
