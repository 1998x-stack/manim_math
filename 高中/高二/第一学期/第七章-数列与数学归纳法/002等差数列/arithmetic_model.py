"""纯数学等差数列模型；不导入 Manim，可独立回归验证。"""
from numbers import Real


def _real(name, value):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} 必须是实数")
    return value


def _index(name, value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} 必须是正整数")
    return value


def term(a1, d, n):
    """等差数列第 n 项，n 从 1 开始。"""
    _real("a1", a1)
    _real("d", d)
    _index("n", n)
    return a1 + (n - 1) * d


def first_n_sum(a1, d, n):
    """前 n 项和，两种常用公式在数学上恒等。"""
    _real("a1", a1)
    _real("d", d)
    _index("n", n)
    return n * (2 * a1 + (n - 1) * d) / 2


def arithmetic_mean(a, b):
    """a、A、b 成等差数列时的中项 A。"""
    _real("a", a)
    _real("b", b)
    return (a + b) / 2


def equal_index_sum(a1, d, m, n, p, q):
    """仅在四个下标均合法且 m+n=p+q 时验证等差数列的和性质。"""
    for name, value in (("m", m), ("n", n), ("p", p), ("q", q)):
        _index(name, value)
    if m + n != p + q:
        raise ValueError("需要 m+n=p+q")
    return term(a1, d, m) + term(a1, d, n) == term(a1, d, p) + term(a1, d, q)


def sample(a1=2, d=3, count=7):
    _index("count", count)
    return tuple(term(a1, d, n) for n in range(1, count + 1))
