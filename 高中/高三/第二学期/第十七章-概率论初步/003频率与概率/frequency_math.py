"""频率与概率：与 Manim 无关的抽样数据及必要数学边界。"""
from fractions import Fraction
import random


def running_frequency(outcomes):
    """返回累计正面数和累计频率；每个结果必须为整数 0 或 1。"""
    result = []
    heads = 0
    for index, value in enumerate(outcomes, 1):
        if type(value) is not int or value not in (0, 1):
            raise ValueError("试验结果必须是整数 0 或 1")
        heads += value
        result.append((index, heads, Fraction(heads, index)))
    if not result:
        raise ValueError("试验次数必须大于零")
    return tuple(result)


def fair_coin_trials(count=200, seed=42):
    """局部 RNG：保证画面与文案可复现，不改变全局 random 状态。"""
    if type(count) is not int or count < 1:
        raise ValueError("试验次数必须是正整数")
    rng = random.Random(seed)
    return tuple(rng.randrange(2) for _ in range(count))


def experiment(count=200, seed=42):
    return running_frequency(fair_coin_trials(count, seed))


def benchmark_probability():
    """公平硬币的理论概率；不得当作一次模拟的确定频率。"""
    return Fraction(1, 2)
