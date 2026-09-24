"""纯数学线面垂直测试：使用三维向量，而非二维透视夹角。"""

from math import isclose


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def zero(value):
    return isclose(value, 0.0, abs_tol=1e-12)


def parallel(a, b):
    if zero(dot(a, a)) or zero(dot(b, b)):
        raise ValueError("直线方向不能是零向量")
    return all(zero(x) for x in cross(a, b))


def plane_normal(a, b):
    if parallel(a, b):
        raise ValueError("两平行方向不足以确定平面")
    return cross(a, b)


def test_criterion_requires_intersection():
    m, n, l = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    normal = plane_normal(m, n)
    assert zero(dot(l, m)) and zero(dot(l, n))
    assert parallel(l, normal)
    # 两条平行面内直线只有一个方向；仅与该方向垂直时未必垂直平面。
    bad_l = (0, 1, 1)
    assert zero(dot(bad_l, m)) and zero(dot(bad_l, (2, 0, 0)))
    assert not parallel(bad_l, normal)
    try:
        plane_normal(m, (2, 0, 0))
    except ValueError:
        pass
    else:
        raise AssertionError("面内两条相交直线必须具有不同方向")


def test_plane_properties():
    normal = (0, 0, 1)
    l1, l2 = (0, 0, 1), (0, 0, -2)
    assert parallel(l1, normal) and parallel(l2, normal)
    assert parallel(l1, l2)
    for m in ((1, 0, 0), (0, 1, 0), (3, -5, 0)):
        assert zero(dot(l1, m))
    for invalid in ((0, 0, 0),):
        try:
            parallel(l1, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("退化向量不得被当作直线方向")


def test_skew_perpendicular_does_not_intersect():
    # l={(0,0,t)}，m={(s,0.8,0)}：方向正交，但两直线不相交。
    l0, ldir = (0, 0, 0), (0, 0, 1)
    m0, mdir = (0, 0.8, 0), (1, 0, 0)
    assert zero(dot(ldir, mdir))
    # (m0-l0) 与 ldir×mdir 的三重积非零，说明是异面直线。
    assert not zero(dot(sub(m0, l0), cross(ldir, mdir)))
    # 辅助线经过垂足且平行于 m，其与 l 有交点，从而定义空间直角。
    auxiliary0, auxiliary_direction = l0, mdir
    assert auxiliary0 == l0 and parallel(auxiliary_direction, mdir)
    assert zero(dot(auxiliary_direction, ldir))


if __name__ == "__main__":
    for check in (test_criterion_requires_intersection, test_plane_properties,
                  test_skew_perpendicular_does_not_intersect):
        check()
        print(f"PASS {check.__name__}")
