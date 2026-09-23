"""第十四章 003：纯 Python 三维线面平行判定与性质的回归测试。"""

from math import isclose


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def sub(u, v):
    return tuple(x - y for x, y in zip(u, v))


def is_zero(value):
    return isclose(value, 0.0, abs_tol=1e-12)


def parallel(u, v):
    if is_zero(dot(u, u)) or is_zero(dot(v, v)):
        raise ValueError("直线方向向量不能为零")
    return all(is_zero(component) for component in cross(u, v))


def line_plane_relation(line_point, direction, plane_point, normal):
    """返回 contained / parallel / intersect；线方向与平面法向量不得退化。"""
    if is_zero(dot(direction, direction)) or is_zero(dot(normal, normal)):
        raise ValueError("不能用零向量定义直线或平面")
    if not is_zero(dot(direction, normal)):
        return "intersect"
    offset = dot(sub(line_point, plane_point), normal)
    return "contained" if is_zero(offset) else "parallel"


def test_definition_and_counterexample():
    alpha_origin, alpha_normal = (0, 0, 0), (0, 0, 1)
    direction = (1, 0, 0)
    assert line_plane_relation((0, 0, 1.2), direction,
                               alpha_origin, alpha_normal) == "parallel"
    # 两条不同直线即使在同一平面内平行，其中一条仍然不与该平面平行。
    assert parallel(direction, (2, 0, 0))
    assert line_plane_relation((0, 1, 0), direction,
                               alpha_origin, alpha_normal) == "contained"
    assert line_plane_relation((0, 0, 0), (0, 0, 1),
                               alpha_origin, alpha_normal) == "intersect"
    for direction_bad, normal_bad in (((0, 0, 0), alpha_normal),
                                      (direction, (0, 0, 0))):
        try:
            line_plane_relation((0, 0, 1), direction_bad,
                                alpha_origin, normal_bad)
        except ValueError:
            pass
        else:
            raise AssertionError("零向量不应定义有效直线或平面")


def test_criterion():
    origin, normal = (0, 0, 0), (0, 0, 1)
    m_point, m_dir = (0, 0, 0), (1, 0, 0)
    l_point, l_dir = (0, 0, 1.2), (1, 0, 0)
    assert line_plane_relation(m_point, m_dir, origin, normal) == "contained"
    assert parallel(l_dir, m_dir)
    assert line_plane_relation(l_point, l_dir, origin, normal) == "parallel"
    # 反例：省略 l 在面外，结论为假。
    counter_l = (0, 2, 0)
    assert parallel(l_dir, m_dir)
    assert line_plane_relation(counter_l, l_dir, origin, normal) == "contained"


def test_property():
    # alpha:z=0，beta:y=0，alpha∩beta=m={(t,0,0)}；l={(t,0,1.2)}。
    alpha_n, beta_n = (0, 0, 1), (0, 1, 0)
    origin, l_origin, direction = (0, 0, 0), (0, 0, 1.2), (1, 0, 0)
    assert line_plane_relation(l_origin, direction, origin, alpha_n) == "parallel"
    assert line_plane_relation(l_origin, direction, origin, beta_n) == "contained"
    m_direction = cross(alpha_n, beta_n)
    assert parallel(m_direction, direction)
    assert line_plane_relation(origin, m_direction, origin, alpha_n) == "contained"
    assert line_plane_relation(origin, m_direction, origin, beta_n) == "contained"
    # β 若与 α 平行，则没有所需交线，不能套用性质定理。
    parallel_beta_origin = (0, 0, 1.2)
    assert line_plane_relation(origin, direction, parallel_beta_origin,
                               alpha_n) == "parallel"
    assert cross(alpha_n, alpha_n) == (0, 0, 0)


if __name__ == "__main__":
    for check in (test_definition_and_counterexample, test_criterion, test_property):
        check()
        print(f"PASS {check.__name__}")
