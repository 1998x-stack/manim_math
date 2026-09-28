"""可独立于 Manim 验证的古典概型模型；等可能性是模型前提。"""
from fractions import Fraction
from itertools import product


def probability(outcomes, favorable):
    """在非空、有限且等可能的基本事件空间中计算概率。"""
    omega = tuple(outcomes)
    if not omega or len(set(omega)) != len(omega):
        raise ValueError("基本事件须非空、可区分且互异")
    hits = set(favorable)
    if not hits.issubset(set(omega)):
        raise ValueError("事件必须是样本空间的子集")
    return Fraction(len(hits), len(omega))


def die_outcomes():
    return tuple(range(1, 7))


def double_die_outcomes():
    """有序二元组，区分第一次与第二次掷骰。"""
    return tuple(product(die_outcomes(), repeat=2))


def sum_seven_outcomes():
    return tuple(pair for pair in double_die_outcomes() if sum(pair) == 7)


def ball_outcomes(red=3, blue=5):
    """每个球有独立编号；仅在每个球被摸出的机会相等时适用。"""
    if not isinstance(red, int) or not isinstance(blue, int) or isinstance(red, bool) or isinstance(blue, bool) or red < 0 or blue < 0 or red + blue == 0:
        raise ValueError("红球、蓝球数量须为非负整数且总量大于零")
    return tuple(("红", index) for index in range(1, red + 1)) + tuple(("蓝", index) for index in range(1, blue + 1))


def two_coin_outcomes():
    """两次独立投掷公平硬币；HT 与 TH 是不同的基本事件。"""
    return tuple(product(("H", "T"), repeat=2))


def example_probabilities():
    die = die_outcomes()
    pair = double_die_outcomes()
    balls = ball_outcomes()
    coins = two_coin_outcomes()
    return {
        "die_one": probability(die, (1,)),
        "die_even": probability(die, (2, 4, 6)),
        "double_sum_seven": probability(pair, sum_seven_outcomes()),
        "red_ball": probability(balls, (ball for ball in balls if ball[0] == "红")),
        "at_least_one_head": probability(coins, (pair for pair in coins if "H" in pair)),
    }
