"""Independent exact arithmetic model for P1 §1.6 (no Manim import)."""
from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


def rational(x):
    return x if isinstance(x, Fraction) else Fraction(x)


@dataclass(frozen=True)
class Quadratic:
    a: Fraction
    b: Fraction
    c: Fraction

    def __post_init__(self):
        for key in ('a', 'b', 'c'):
            object.__setattr__(self, key, rational(getattr(self, key)))
        if self.a == 0:
            raise ValueError('a=0 is not a quadratic')

    @classmethod
    def from_vertex(cls, a, h, k):
        a, h, k = map(rational, (a, h, k))
        return cls(a, -2*a*h, a*h*h+k)

    def value(self, x):
        x = rational(x)
        return self.a*x*x + self.b*x + self.c

    @property
    def h(self):
        return -self.b / (2*self.a)

    @property
    def k(self):
        return self.value(self.h)

    @property
    def discriminant(self):
        return self.b*self.b - 4*self.a*self.c

    @property
    def kind(self):
        return 'minimum' if self.a > 0 else 'maximum'

    def roots(self):
        """Distinct REAL zero locations, sorted (floating coordinates for Manim)."""
        d = self.discriminant
        if d < 0:
            return ()
        if d == 0:
            return (float(self.h),)
        sd = sqrt(float(d))
        return tuple(sorted(((-float(self.b)-sd)/(2*float(self.a)),
                             (-float(self.b)+sd)/(2*float(self.a)))))

    def interval_extrema(self, left, right):
        """Closed interval [left,right], exact min/max values & a realizing x."""
        left, right = rational(left), rational(right)
        if left > right:
            raise ValueError('left must not exceed right')
        xs = [left, right]
        if left <= self.h <= right:
            xs.append(self.h)
        pairs = [(self.value(x), x) for x in xs]
        mn = min(pairs)
        mx = max(pairs)
        return {'min': mn, 'max': mx}

    def verify_vertex_identity(self, x):
        x = rational(x)
        return self.value(x) == self.a*(x-self.h)**2 + self.k


UP = Quadratic(1, -4, 1)         # (x-2)^2-3, vertex (2,-3)
DOWN = Quadratic(-1, 6, -5)      # 4-(x-3)^2, vertex (3,4)
PRACTICE = Quadratic(-1, 4, 1)   # 5-(x-2)^2, vertex (2,5)
