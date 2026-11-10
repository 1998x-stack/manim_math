"""Finite 2D triangle facts, without Manim/NumPy dependencies.

Use the same model for lesson tests, screen vertices and labels. This is a
numerical fixture, NOT a general mathematical proof or an every-frame inspector.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


Point = tuple[float, float]


def point2(value) -> Point:
    try:
        if len(value) != 2:
            raise ValueError("expected exactly two coordinates")
        result = (float(value[0]), float(value[1]))
    except (TypeError, ValueError, IndexError) as exc:
        raise ValueError(f"invalid 2D point: {value!r}") from exc
    if not all(map(math.isfinite, result)):
        raise ValueError("point coordinates must be finite")
    return result


def midpoint(a: Point, b: Point) -> Point:
    a, b = point2(a), point2(b)
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


@dataclass(frozen=True)
class Triangle2D:
    a: Point
    b: Point
    c: Point
    relative_tolerance: float = 1e-10

    def __post_init__(self):
        for name in ("a", "b", "c"):
            object.__setattr__(self, name, point2(getattr(self, name)))
        tol = self.relative_tolerance
        if not math.isfinite(tol) or not 0 <= tol < 1:
            raise ValueError("relative_tolerance must be finite in [0,1)")
        ab, ac = self._vectors()
        length_scale = max(math.dist(self.a, self.b), math.dist(self.a, self.c),
                           math.dist(self.b, self.c))
        if length_scale == 0 or abs(self._cross(ab, ac)) <= tol * length_scale**2:
            raise ValueError("degenerate or numerically near-collinear triangle")

    @staticmethod
    def _cross(u: Point, v: Point) -> float:
        return u[0] * v[1] - u[1] * v[0]

    def _vectors(self):
        return ((self.b[0] - self.a[0], self.b[1] - self.a[1]),
                (self.c[0] - self.a[0], self.c[1] - self.a[1]))

    @property
    def signed_double_area(self) -> float:
        return self._cross(*self._vectors())

    @property
    def area(self) -> float:
        return abs(self.signed_double_area) / 2

    @property
    def centroid(self) -> Point:
        return ((self.a[0] + self.b[0] + self.c[0]) / 3,
                (self.a[1] + self.b[1] + self.c[1]) / 3)

    @property
    def circumcenter(self) -> Point:
        u, v = self._vectors()
        determinant = self._cross(u, v)
        squared_u, squared_v = u[0]**2 + u[1]**2, v[0]**2 + v[1]**2
        dx = (squared_u * v[1] - squared_v * u[1]) / (2 * determinant)
        dy = (squared_v * u[0] - squared_u * v[0]) / (2 * determinant)
        return (self.a[0] + dx, self.a[1] + dy)

    @property
    def orthocenter(self) -> Point:
        ox, oy = self.circumcenter
        return (self.a[0] + self.b[0] + self.c[0] - 2 * ox,
                self.a[1] + self.b[1] + self.c[1] - 2 * oy)

    @property
    def incenter(self) -> Point:
        sa = math.dist(self.b, self.c)
        sb = math.dist(self.a, self.c)
        sc = math.dist(self.a, self.b)
        perimeter = sa + sb + sc
        return ((sa * self.a[0] + sb * self.b[0] + sc * self.c[0]) / perimeter,
                (sa * self.a[1] + sb * self.b[1] + sc * self.c[1]) / perimeter)

    def as_scene_points(self) -> dict[str, tuple[float, float, float]]:
        """Data coordinates only; apply Axes.c2p if the Scene has moved/scaled axes."""
        return {name: (*getattr(self, name), 0.0) for name in ("a", "b", "c")}
