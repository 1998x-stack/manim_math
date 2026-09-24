"""无需 Manim 的平面公理回归：python verify_plane_axioms.py。"""

from itertools import combinations
from math import isclose


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def on_plane(point, normal, origin=(0, 0, 0)):
    return isclose(dot(sub(point, origin), normal), 0.0, abs_tol=1e-10)


def collinear(a, b, c):
    return all(isclose(v, 0.0, abs_tol=1e-10)
               for v in cross(sub(b, a), sub(c, a)))


def test_axiom_1():
    # alpha: z=0；两点在直线且在平面中，则其所有线性组合仍在平面中。
    a, b = (-1, 0, 0), (2, 0, 0)
    assert a != b
    for t in (-10, -1, 0, 0.25, 1, 5, 10):
        p = tuple(a[i] + t * (b[i] - a[i]) for i in range(3))
        assert on_plane(p, (0, 0, 1)), (t, p)


def test_axiom_2():
    a, b, c = (-1, 0, 0), (1, 0, 0), (0, 2, 0)
    assert not collinear(a, b, c)
    normal = cross(sub(b, a), sub(c, a))
    assert normal != (0, 0, 0)
    assert all(on_plane(p, normal, a) for p in (a, b, c))
    assert collinear((0, 0, 0), (1, 0, 0), (2, 0, 0))
    # 共线三点同时属于 z=0 和 y=0 两个不重合平面，不能定唯一平面。
    for normal in ((0, 0, 1), (0, 1, 0)):
        assert all(on_plane(p, normal) for p in
                   ((0, 0, 0), (1, 0, 0), (2, 0, 0)))


def test_axiom_3():
    # 两个不同的平面 alpha:z=0, beta:y=0，交集为 x 轴。
    n_alpha, n_beta = (0, 0, 1), (0, 1, 0)
    direction = cross(n_alpha, n_beta)
    assert direction != (0, 0, 0)
    for t in (-10, -1, 0, 0.5, 1, 10):
        p = (t, 0, 0)
        assert on_plane(p, n_alpha) and on_plane(p, n_beta)
    # 任意同时位于两个平面的点均满足 y=z=0，不可能只有单点 P。
    for p in ((0, 0, 0), (1, 0, 0), (-1, 0, 0)):
        assert on_plane(p, n_alpha) and on_plane(p, n_beta)
    assert not on_plane((0, 1, 0), n_beta)
    assert not on_plane((0, 0, 1), n_alpha)


def test_four_plane_conditions():
    # 三个不共线点；直线和线外点；两相交直线；两条不同的平行直线。
    a, b, c = (0, 0, 0), (1, 0, 0), (0, 1, 0)
    assert not collinear(a, b, c)
    assert not collinear(a, b, (0, 1, 0))
    line1 = ((0, 0, 0), (1, 0, 0))
    intersecting_line = ((0, 0, 0), (0, 1, 0))
    assert line1[0] == intersecting_line[0]
    assert cross(sub(*line1[::-1]), sub(*intersecting_line[::-1])) != (0, 0, 0)
    parallel_line = ((0, 1, 0), (1, 1, 0))
    assert sub(*line1[::-1]) == sub(*parallel_line[::-1])
    assert line1[0] not in parallel_line
    assert all(on_plane(p, (0, 0, 1)) for p in
               (*line1, *intersecting_line, *parallel_line))


if __name__ == "__main__":
    for test in (test_axiom_1, test_axiom_2, test_axiom_3,
                 test_four_plane_conditions):
        test()
        print(f"PASS {test.__name__}")
