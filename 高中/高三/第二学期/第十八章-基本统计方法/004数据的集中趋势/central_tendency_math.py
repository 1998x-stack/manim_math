"""集中趋势的纯数学数据与运算；所有可见数值由同一模型计算。"""
from collections import Counter
from fractions import Fraction

ODD = (52, 63, 71, 74, 78, 82, 85, 85, 90)
EVEN = (62, 68, 74, 78, 85, 91)
MODE_DATA = (71, 74, 78, 78, 78, 82, 85, 90)
BEFORE = (60, 62, 65, 68, 70, 72, 75, 78)
AFTER = BEFORE[:-1] + (200,)
SCORES = (85, 70)
WEIGHTS = (Fraction(3, 5), Fraction(2, 5))


def mean(values):
    items = tuple(values)
    if not items:
        raise ValueError("均值要求非空数据")
    return sum((Fraction(value) for value in items), Fraction(0)) / len(items)


def weighted_mean(values, weights):
    xs, ws = tuple(values), tuple(weights)
    if not xs or len(xs) != len(ws):
        raise ValueError("权重和数据应一一对应且非空")
    ws = tuple(Fraction(w) for w in ws)
    if any(w < 0 for w in ws) or not sum(ws):
        raise ValueError("权重不能为负且总和必须大于0")
    return sum((Fraction(x) * w for x, w in zip(xs, ws)), Fraction(0)) / sum(ws)


def median(values):
    xs = sorted(Fraction(x) for x in values)
    if not xs:
        raise ValueError("中位数要求非空数据")
    mid = len(xs) // 2
    return xs[mid] if len(xs) % 2 else (xs[mid - 1] + xs[mid]) / 2


def modes(values):
    xs = tuple(values)
    if not xs:
        raise ValueError("众数要求非空数据")
    counts = Counter(xs)
    most = max(counts.values())
    # 本课约定：每个取值只出现一次时报告“无重复众数”。
    return tuple(sorted(x for x, count in counts.items() if count == most)) if most > 1 else ()


def outlier_comparison(before=BEFORE, after=AFTER):
    old, new = tuple(before), tuple(after)
    if not old or len(old) != len(new):
        raise ValueError("必须比较相同数量的非空观察值")
    return (mean(old), median(old)), (mean(new), median(new))
