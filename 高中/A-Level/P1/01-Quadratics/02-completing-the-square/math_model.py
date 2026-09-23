"""Exact, rendering-independent mathematics for Cambridge P1 section 1.2.

Coefficients and solutions use fractions where possible. Geometry depicts x=2
and is an illustration of the identity, not a proof for all real x.
"""
from fractions import Fraction


def completed_square(a, b, c):
    """a*x^2+b*x+c = a*(x+shift)^2 + offset, a != 0."""
    a, b, c = map(Fraction, (a, b, c))
    if a == 0:
        raise ValueError('A quadratic requires a nonzero leading coefficient')
    return a, b / (2 * a), c - b * b / (4 * a)


def polynomial(a, b, c, x):
    return a * x * x + b * x + c


def square_form(a, shift, offset, x):
    return a * (x + shift) ** 2 + offset


def square_completion_tiles(x=2, half_coefficient=3, constant=5):
    """The 5x5 area diagram for x^2+6x+5 with x=2.

    `missing` denotes the unfilled part of a 3x3 corner of the big square.
    A literal nonnegative-area diagram requires x>=0, half_coefficient>=0,
    constant in [0, half_coefficient**2] and integer lengths for unit tiles.
    """
    if not isinstance(x, int) or not isinstance(half_coefficient, int):
        raise ValueError('The tile drawing needs integral x and strip width')
    if x < 0 or half_coefficient < 0 or not (0 <= constant <= half_coefficient**2):
        raise ValueError('Invalid positive-area tiling parameters')
    missing = half_coefficient**2 - constant
    return dict(base=x*x, bottom=x*half_coefficient,
                right=x*half_coefficient, corner_filled=constant,
                corner_missing=missing, whole=(x+half_coefficient)**2,
                expression=x*x+2*x*half_coefficient+constant)


def parabola_vertex_and_roots():
    """For x^2+6x+5, y=(x+3)^2-4; real roots are -5 and -1."""
    a, shift, offset = completed_square(1, 6, 5)
    return (-shift, offset), (-5, -1)


def solve_example_via_square():
    """Exact rational roots of (x+3)^2=4."""
    return tuple(sorted((Fraction(-3-2), Fraction(-3+2))))
