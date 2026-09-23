"""等比数列数学数据；只使用 Python 标准库，图形层不可自行伪造面积值。"""
from math import sqrt
from numbers import Real


def _real(name, value, nonzero=False):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} 必须是实数")
    if nonzero and value == 0:
        raise ValueError(f"{name} 必须非零")
    return value


def _positive_index(name, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError(f"{name} 必须是正整数")
    return n


def term(a1, q, n):
    _real("a1", a1, nonzero=True)
    _real("q", q, nonzero=True)
    _positive_index("n", n)
    return a1 * q ** (n - 1)


def sample(a1=2, q=2, count=5):
    _positive_index("count", count)
    return tuple(term(a1, q, n) for n in range(1, count + 1))


def finite_sum(a1, q, n):
    _real("a1", a1, nonzero=True)
    _real("q", q, nonzero=True)
    _positive_index("n", n)
    if q == 1:
        return n * a1
    return a1 * (1 - q ** n) / (1 - q)


def infinite_sum(a1, q):
    _real("a1", a1, nonzero=True)
    _real("q", q, nonzero=True)
    if abs(q) >= 1:
        raise ValueError("无穷等比级数收敛要求 |q|<1")
    return a1 / (1 - q)


def area_tiles(first_area=2, ratio=2, count=4, screen_scale=0.55):
    """返回 (数学面积, 屏幕边长)；边长按 sqrt(面积) 而非面积成倍。"""
    _real("first_area", first_area)
    _real("ratio", ratio)
    _real("screen_scale", screen_scale)
    _positive_index("count", count)
    if first_area <= 0 or ratio <= 0 or screen_scale <= 0:
        raise ValueError("面积、公比及屏幕比例须均为正")
    return tuple((first_area * ratio ** k,
                  screen_scale * sqrt(first_area * ratio ** k))
                 for k in range(count))


def equal_index_product(a1, q, m, n, p, r):
    for name, index in (("m", m), ("n", n), ("p", p), ("r", r)):
        _positive_index(name, index)
    if m + n != p + r:
        raise ValueError("必须满足 m+n=p+r")
    return term(a1, q, m) * term(a1, q, n) == term(a1, q, p) * term(a1, q, r)
