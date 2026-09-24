"""纯数学模型：条件概率、独立、二项分布与全概率公式。"""
from fractions import Fraction
from itertools import product
from math import comb

OMEGA = frozenset(range(1, 11))
B = frozenset((1, 2, 3, 4))
A = frozenset((1, 5, 6, 7, 8))


def probability(event, space=OMEGA):
    outcomes = frozenset(space)
    hits = frozenset(event)
    if not outcomes or not hits <= outcomes:
        raise ValueError("事件应属于非空样本空间")
    return Fraction(len(hits), len(outcomes))


def conditional(a, b, space=OMEGA):
    """等可能有限模型：B 非空；一般情形需 P(B)>0。"""
    outcomes = frozenset(space)
    given = frozenset(b)
    probability(given, outcomes)
    if not given:
        raise ValueError("条件事件概率不能为零")
    return Fraction(len(frozenset(a) & given), len(given)) if frozenset(a) <= outcomes else probability(a, outcomes)


def independent(a, b, space=OMEGA):
    return probability(frozenset(a) & frozenset(b), space) == probability(a, space) * probability(b, space)


def fair_coin_pairs():
    return tuple(product(("H", "T"), repeat=2))


def binomial(n, k, p=Fraction(1, 2)):
    if type(n) is not int or type(k) is not int or n < 0 or k < 0 or k > n:
        raise ValueError("要求整数 n>=0、0<=k<=n")
    p = Fraction(p)
    if not 0 <= p <= 1:
        raise ValueError("单次成功概率应在零到一之间")
    return comb(n, k) * p**k * (1 - p)**(n - k)


def total_from_partition(a, parts, space=OMEGA):
    """检查正概率互斥分区，并逐项计算 P(B_i)P(A|B_i)。"""
    universe = frozenset(space)
    probability(a, universe)
    checked = []
    covered = frozenset()
    for part in parts:
        group = frozenset(part)
        probability(group, universe)
        if not group or covered & group:
            raise ValueError("分区不能包含空事件或重叠")
        covered |= group
        checked.append(group)
    if covered != universe:
        raise ValueError("分区应覆盖整个样本空间")
    return sum((probability(part, universe) * conditional(a, part, universe)
                for part in checked), Fraction(0))
