"""第十四章 002：以三维向量校验空间直线关系，不导入 Manim。"""

from math import acos, degrees, isclose, sqrt


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def norm(a):
    return sqrt(dot(a, a))


def line_kind(a0, u, b0, v):
    """两条非退化、不同的空间直线：相交/平行/异面。"""
    if norm(u) == 0 or norm(v) == 0:
        raise ValueError("直线的方向向量不得为零")
    delta = sub(b0, a0)
    n = cross(u, v)
    if isclose(norm(n), 0.0, abs_tol=1e-12):
        if isclose(norm(cross(delta, u)), 0.0, abs_tol=1e-12):
            raise ValueError("两条直线重合，不属于不同直线的三种关系")
        return "parallel"
    return "skew" if not isclose(dot(delta, n), 0.0, abs_tol=1e-12) else "intersect"


def acute_angle(u, v):
    if norm(u) == 0 or norm(v) == 0:
        raise ValueError("方向向量不得为零")
    value = abs(dot(u, v)) / (norm(u) * norm(v))
    return degrees(acos(min(1.0, max(0.0, value))))


def skew_distance(a0, u, b0, v):
    if line_kind(a0, u, b0, v) != "skew":
        raise ValueError("本函数只计算异面直线间的距离")
    n = cross(u, v)
    return abs(dot(sub(b0, a0), n)) / norm(n)


def test_three_relationships():
    a0, u = (0, 0, 0), (1, 0, 0)
    assert line_kind(a0, u, (0, 0, 0), (0, 1, 0)) == "intersect"
    assert line_kind(a0, u, (0, 1, 0), (1, 0, 0)) == "parallel"
    assert line_kind(a0, u, (0, 0, 1.5), (0, 1, 0)) == "skew"
    for args in ((a0, (0, 0, 0), (0, 1, 0), (1, 0, 0)),
                 (a0, u, (0, 0, 0), (2, 0, 0))):
        try:
            line_kind(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("退化或重合直线应报错")


def test_angle_and_parallel_construction():
    u, v = (1, 0, 0), (0, 1, 0)
    original_b = ((0, -2, 1.5), (0, 2, 1.5))
    b_prime = ((0, -1.8, 0), (0, 1.8, 0))
    o = (0, 0, 0)
    assert b_prime[0][2] == b_prime[1][2] == o[2] == 0
    assert cross(sub(*original_b[::-1]), sub(*b_prime[::-1])) == (0, 0, 0)
    assert isclose(acute_angle(u, v), 90.0)
    # 反向同一条直线，不改变无向直线所成的锐角。
    assert isclose(acute_angle((1, 0, 0), (-sqrt(3), -1, 0)), 30.0)


def test_common_perpendicular():
    a0, b0 = (0, 0, 0), (0, 0, 1.5)
    u, v = (1, 0, 0), (0, 1, 0)
    segment = sub(b0, a0)
    assert isclose(dot(segment, u), 0.0)
    assert isclose(dot(segment, v), 0.0)
    assert isclose(skew_distance(a0, u, b0, v), norm(segment))
    assert isclose(skew_distance(a0, u, b0, v), 1.5)


if __name__ == "__main__":
    for check in (test_three_relationships, test_angle_and_parallel_construction,
                  test_common_perpendicular):
        check()
        print(f"PASS {check.__name__}")
