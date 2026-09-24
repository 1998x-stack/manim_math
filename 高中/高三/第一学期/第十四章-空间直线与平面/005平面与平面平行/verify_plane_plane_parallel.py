"""两平面平行：三维模型、判定反例及平行线段端点条件回归。"""

from math import isclose, sqrt


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


def parallel(a, b):
    if isclose(norm(a), 0) or isclose(norm(b), 0):
        raise ValueError("不能使用零方向或零法向量")
    return all(isclose(x, 0, abs_tol=1e-12) for x in cross(a, b))


def line_parallel_plane(point, direction, plane_origin, plane_normal):
    if norm(direction) == 0 or norm(plane_normal) == 0:
        raise ValueError("退化方向/法向量")
    return (isclose(dot(direction, plane_normal), 0, abs_tol=1e-12)
            and not isclose(dot(sub(point, plane_origin), plane_normal),
                            0, abs_tol=1e-12))


def test_definition_and_criterion():
    alpha_n, beta_n = (0, 0, 1), (0, 0, 1)
    a0, a_dir = (0, 0, 0), (1, 0, 0)
    b0, b_dir = (0, 0, 0), (0, 1, 0)
    beta0 = (0, 0, 2)
    assert parallel(alpha_n, beta_n)
    assert not isclose(dot(sub(beta0, a0), alpha_n), 0)
    assert norm(cross(a_dir, b_dir)) > 0
    assert line_parallel_plane(a0, a_dir, beta0, beta_n)
    assert line_parallel_plane(b0, b_dir, beta0, beta_n)
    # 反例：α:y=0 与 β:z=0 相交，α 内两条平行 x 轴的直线可同时平行 β。
    alpha_intersecting_n = (0, 1, 0)
    a1, a2 = (0, 0, 1), (0, 0, 2)
    assert parallel((1, 0, 0), (2, 0, 0))
    assert line_parallel_plane(a1, (1, 0, 0), (0, 0, 0), beta_n)
    assert line_parallel_plane(a2, (1, 0, 0), (0, 0, 0), beta_n)
    assert norm(cross(alpha_intersecting_n, beta_n)) > 0


def test_sections():
    alpha_n, beta_n, gamma_n = (0, 0, 1), (0, 0, 1), (0, 1, 0)
    assert parallel(alpha_n, beta_n)
    section_a = cross(alpha_n, gamma_n)
    section_b = cross(beta_n, gamma_n)
    assert norm(section_a) > 0 and norm(section_b) > 0
    assert parallel(section_a, section_b)
    # γ 与 α 平行时不存在交线，不适用性质定理。
    assert cross(alpha_n, alpha_n) == (0, 0, 0)


def test_segments_and_endpoint_conditions():
    a, b = (-1.5, 0.2, 0), (-1.5, 0.2, 2)
    c, d = (1.5, 0.2, 0), (1.5, 0.2, 2)
    ab, cd = sub(b, a), sub(d, c)
    assert parallel(ab, cd)
    assert isclose(norm(ab), norm(cd)) and isclose(norm(ab), 2.0)
    assert a[2] == c[2] == 0 and b[2] == d[2] == 2
    # 只保留线段平行，端点不同时落在这对平面上就可能不等长。
    shorter = sub((1.5, 0.2, 1.5), (1.5, 0.2, 0))
    assert parallel(ab, shorter) and not isclose(norm(ab), norm(shorter))


if __name__ == "__main__":
    for check in (test_definition_and_criterion, test_sections,
                  test_segments_and_endpoint_conditions):
        check()
        print(f"PASS {check.__name__}")
