"""数据离散度：本课采用以 n 为分母的描述性方差，而非 n-1 的无偏估计。"""
from fractions import Fraction
from math import sqrt

A = (3, 4, 5, 6, 7)
B = (1, 2, 5, 8, 9)


def mean(values):
    xs = tuple(Fraction(x) for x in values)
    if not xs:
        raise ValueError("至少需要一个数据")
    return sum(xs, Fraction(0)) / len(xs)


def data_range(values):
    xs = tuple(values)
    if not xs:
        raise ValueError("极差要求非空数据")
    return max(xs) - min(xs)


def descriptive_variance(values):
    xs = tuple(Fraction(x) for x in values)
    if not xs:
        raise ValueError("方差要求非空数据")
    avg = mean(xs)
    return sum(((x - avg) ** 2 for x in xs), Fraction(0)) / len(xs)


def unbiased_sample_variance(values):
    """对照公式，不作为本课 A/B 描述性方差的展示结果。"""
    xs = tuple(Fraction(x) for x in values)
    if len(xs) < 2:
        raise ValueError("使用 n-1 分母须至少有两个观察值")
    avg = mean(xs)
    return sum(((x - avg) ** 2 for x in xs), Fraction(0)) / (len(xs) - 1)


def standard_deviation(values):
    return sqrt(float(descriptive_variance(values)))


def coefficient_of_variation(values):
    """非零均值时返回无量纲 CV=标准差/|均值|；并非所有测量尺度都适用。"""
    avg = mean(values)
    if not avg:
        raise ValueError("均值为零时不能计算变异系数")
    return standard_deviation(values) / abs(float(avg))
