"""Exact algebraic data source for A-Level P1 §1.4, independent of Manim."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, sqrt


@dataclass(frozen=True)
class Parabola:
    a: F
    b: F
    c: F

    def __post_init__(self):
        if self.a == 0:
            raise ValueError('quadratic leading coefficient must be nonzero')

    def at(self, x):
        return self.a*x*x + self.b*x + self.c


@dataclass(frozen=True)
class Line:
    m: F
    k: F

    def at(self, x):
        return self.m*x + self.k


def eliminated_coefficients(curve, line):
    """Substitution y=m*x+k into y=a*x²+b*x+c."""
    return curve.a, curve.b-line.m, curve.c-line.k


def discriminant(curve, line):
    a, b, c = eliminated_coefficients(curve, line)
    return b*b-4*a*c


def exact_sqrt_fraction(q):
    q = F(q)
    if q < 0:
        raise ValueError('negative radicand')
    p, r = isqrt(q.numerator), isqrt(q.denominator)
    return F(p, r) if p*p == q.numerator and r*r == q.denominator else None


def intersections(curve, line):
    """Real intersections, exact Fraction when discriminant is a square, else float."""
    a, b, _ = eliminated_coefficients(curve, line)
    d = discriminant(curve, line)
    if d < 0:
        return ()
    q = exact_sqrt_fraction(d)
    root = q if q is not None else sqrt(float(d))
    xs = sorted({(-b-root)/(2*a), (-b+root)/(2*a)})
    points = tuple((x, line.at(x)) for x in xs)
    for x, y in points:
        if abs(float(curve.at(x)-y)) > 1e-9:
            raise AssertionError('substitution did not yield a common solution')
    return points


def circle_line_points(radius_squared, line):
    """For x²+y²=r² and y=m*x+k; returns real common points."""
    if radius_squared <= 0:
        raise ValueError('radius squared must be positive')
    m, k = line.m, line.k
    coeff = Parabola(1+m*m, 2*m*k, k*k-F(radius_squared))
    result = intersections(coeff, Line(F(0), F(0)))
    return tuple((x, line.at(x)) for x, _ in result)


MAIN_CURVE = Parabola(F(1), F(-2), F(1))
MAIN_LINE = Line(F(1), F(1))
TANGENT = Line(F(1), F(-5, 4))
MISSED = Line(F(1), F(-2))
PRACTICE_CURVE = Parabola(F(1), F(-2), F(2))
PRACTICE_LINE = Line(F(2), F(-1))
