"""统计估计：均值点估计、n-1方差、已知sigma正态均值置信区间。"""
from fractions import Fraction
from math import erf, isfinite, sqrt

SAMPLE = (Fraction(-6, 5), Fraction(-2, 5), Fraction(1, 10),
          Fraction(7, 10), Fraction(7, 5))
MU_DEMO = Fraction(0)
SIGMA_DEMO = 1.0
Z_95_APPROX = 1.96


def sample_mean(sample=SAMPLE):
    data = tuple(Fraction(v) for v in sample)
    if not data:
        raise ValueError("均值估计要求至少一个观测值")
    return sum(data, Fraction(0)) / len(data)


def sample_variance_unbiased(sample=SAMPLE):
    data = tuple(Fraction(v) for v in sample)
    if len(data) < 2:
        raise ValueError("n-1 方差要求至少两个观测值")
    avg = sample_mean(data)
    return sum(((x - avg) ** 2 for x in data), Fraction(0)) / (len(data) - 1)


def normal_ci_known_sigma(sample=SAMPLE, sigma=SIGMA_DEMO, z=Z_95_APPROX):
    """仅在i.i.d.正态且sigma已知时为经典双侧均值置信区间。"""
    data = tuple(sample)
    n = len(data)
    if n < 1 or not isfinite(float(sigma)) or sigma <= 0 or not isfinite(float(z)) or z <= 0:
        raise ValueError("需要非空样本、已知正sigma与正临界值")
    center = float(sample_mean(data))
    margin = float(z) * float(sigma) / sqrt(n)
    return center - margin, center + margin


def normal_coverage(z=Z_95_APPROX):
    if not isfinite(float(z)) or z <= 0:
        raise ValueError("双侧z临界值必须正且有限")
    return erf(float(z) / sqrt(2))


def variance_of_sample_mean(n, sigma=SIGMA_DEMO):
    if type(n) is not int or n <= 0 or not isfinite(float(sigma)) or sigma <= 0:
        raise ValueError("要求正整数n及正有限sigma")
    return float(sigma) ** 2 / n
