"""Independent exact-rational data model for A-Level P1 §1.3."""
from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


@dataclass(frozen=True)
class Quadratic:
    a: Fraction
    b: Fraction
    c: Fraction

    def __post_init__(self):
        for name in ('a', 'b', 'c'):
            object.__setattr__(self, name, Fraction(getattr(self, name)))
        if self.a == 0:
            raise ValueError('A quadratic equation must have a nonzero leading coefficient')

    @property
    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    @property
    def axis(self):
        return -self.b / (2 * self.a)

    @property
    def vertex_y(self):
        return self.c - self.b ** 2 / (4 * self.a)

    @property
    def real_root_count(self):
        return 2 if self.delta > 0 else 1 if self.delta == 0 else 0

    def value(self, x):
        x = Fraction(x)
        return self.a * x * x + self.b * x + self.c

    def real_roots(self):
        """Sorted numerical real roots; keep exact surd notation in the lesson."""
        if self.delta < 0:
            return ()
        if self.delta == 0:
            return (float(self.axis),)
        a, b = float(self.a), float(self.b)
        d = sqrt(float(self.delta))
        return tuple(sorted(((-b - d) / (2 * a), (-b + d) / (2 * a))))

    def completed_square(self):
        """Return (a,h,k) for a(x-h)^2+k; h,k are exact Fractions."""
        return self.a, self.axis, self.vertex_y


def area_square_model(x=2, d=2):
    """Integer x,d >=0: x*x + two x*d strips + d*d corner."""
    if not all(isinstance(v, int) and v >= 0 for v in (x, d)):
        raise ValueError('Tile model requires nonnegative integer lengths')
    return dict(base=x * x, strips=2 * x * d, corner=d * d,
                whole=(x + d) ** 2, side=x + d)


def discriminant_family(k):
    """(x-1)^2-k = x^2-2x+(1-k): discriminant 4k."""
    q = Quadratic(1, -2, 1 - Fraction(k))
    assert q.delta == 4 * Fraction(k)
    return q


EXAMPLE = Quadratic(2, -2, -1)  # roots (1 +/- sqrt(3))/2
PRACTICE = Quadratic(3, 2, -2)  # roots (-1 +/- sqrt(7))/3
