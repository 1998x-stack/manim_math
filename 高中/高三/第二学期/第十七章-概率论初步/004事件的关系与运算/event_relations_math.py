"""事件关系、并交、互斥与对立的有限样本空间模型。"""
from fractions import Fraction

OMEGA = frozenset(range(1, 7))
A = frozenset((1, 3, 5))  # 奇数
B = frozenset((2, 3, 5))  # 质数


def event(items, omega=OMEGA):
    """验证输入是给定有限样本空间的子集；整数不是事件。"""
    sample = frozenset(omega)
    result = frozenset(items)
    if not sample or not result <= sample:
        raise ValueError("必须给出非空样本空间内的事件")
    return result


def intersection(a, b, omega=OMEGA):
    return event(a, omega) & event(b, omega)


def union(a, b, omega=OMEGA):
    return event(a, omega) | event(b, omega)


def complement(a, omega=OMEGA):
    return event(omega, omega) - event(a, omega)


def mutually_exclusive(a, b, omega=OMEGA):
    return not intersection(a, b, omega)


def complementary(a, b, omega=OMEGA):
    return mutually_exclusive(a, b, omega) and union(a, b, omega) == event(omega, omega)


def probability(a, omega=OMEGA):
    """仅适用于所有基本事件等可能的有限非空样本空间。"""
    sample = event(omega, omega)
    return Fraction(len(event(a, sample)), len(sample))
