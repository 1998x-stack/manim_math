"""Pure-Python models for A-Level P1 §1.5: quadratic in a function of x."""
from __future__ import annotations
from math import isclose, log, sqrt
from typing import Literal

Mode = Literal['square', 'square_root', 'power3']


def quadratic_roots(a: float, b: float, c: float) -> tuple[float, ...]:
    """Distinct real roots of a*t²+b*t+c, ascending. a must not be zero."""
    if isclose(a, 0.0, abs_tol=1e-12):
        raise ValueError('The leading coefficient must be nonzero.')
    delta = b * b - 4 * a * c
    if delta < -1e-12:
        return ()
    if isclose(delta, 0.0, abs_tol=1e-12):
        return (-b / (2 * a),)
    d = sqrt(max(0., delta))
    # Numerically stable for large coefficients / roots of disparate magnitude.
    q = -0.5 * (b + (d if b >= 0 else -d))
    if isclose(q, 0.0, abs_tol=1e-14):
        return tuple(sorted(((-b-d) / (2*a), (-b+d) / (2*a))))
    return tuple(sorted((q/a, c/q)))


def preimages(t: float, mode: Mode) -> tuple[float, ...]:
    """Solve g(x)=t over real x; g is x², sqrt(x), or 3**x."""
    if mode == 'square':
        if t < -1e-12:
            return ()
        if isclose(t, 0., abs_tol=1e-12):
            return (0.,)
        r = sqrt(t)
        return (-r, r)
    if mode == 'square_root':
        if t < -1e-12:
            return ()
        return (max(0., t)**2,)
    if mode == 'power3':
        if t <= 0:
            return ()
        return (log(t)/log(3.),)
    raise ValueError(f'Unknown mode: {mode}')


def solve_transformed(a: float, b: float, c: float, mode: Mode) -> tuple[float, ...]:
    """Solve a*g(x)²+b*g(x)+c=0, filtering forbidden intermediate roots."""
    xs = sorted(x for t in quadratic_roots(a, b, c) for x in preimages(t, mode))
    unique: list[float] = []
    for x in xs:
        if not unique or not isclose(x, unique[-1], abs_tol=1e-10):
            unique.append(x)
    return tuple(unique)


def evaluate_transformed(x: float, a: float, b: float, c: float, mode: Mode) -> float:
    if mode == 'square':
        t = x*x
    elif mode == 'square_root':
        if x < 0:
            raise ValueError('sqrt(x) requires x >= 0')
        t = sqrt(x)
    elif mode == 'power3':
        t = 3.**x
    else:
        raise ValueError(f'Unknown mode: {mode}')
    return a*t*t + b*t + c


MAIN_T = quadratic_roots(1, -5, 4)
MAIN_X = solve_transformed(1, -5, 4, 'square')
SURD_X = solve_transformed(1, -5, 6, 'square_root')
POWER_X = solve_transformed(1, -10, 9, 'power3')
PRACTICE_X = solve_transformed(1, -1, -6, 'square')
CHALLENGE_X = solve_transformed(1, -10, 9, 'square')
