"""频率分布/直方图/折线/累积曲线与茎叶图的同源教学数据。"""
from fractions import Fraction
from collections import Counter

SCORES = (
    52, 55, 58,
    61, 63, 64, 65, 66, 67, 68, 69,
    70, 70, 71, 72, 73, 74, 74, 75, 76, 77, 78, 78, 79, 79,
    80, 81, 82, 82, 83, 84, 85, 86, 87, 89,
    90, 91, 93, 95, 99,
)
EDGES = (50, 60, 70, 80, 90, 100)
STEM_SUBSET = (52, 55, 58, 61, 63, 66, 69, 70, 74, 77, 82, 86)


def grouped_counts(scores=SCORES, edges=EDGES):
    """统一左闭右开分组，最后一组也为[90,100)。"""
    xs = tuple(scores)
    bounds = tuple(edges)
    if len(bounds) < 2 or any(b >= c for b, c in zip(bounds, bounds[1:])):
        raise ValueError("分组边界应严格递增")
    if not xs or any(not bounds[0] <= x < bounds[-1] for x in xs):
        raise ValueError("样本必须非空且全部落在分组范围内")
    return tuple(sum(left <= x < right for x in xs)
                 for left, right in zip(bounds, bounds[1:]))


def distribution(scores=SCORES, edges=EDGES):
    counts = grouped_counts(scores, edges)
    n = len(scores)
    frequencies = tuple(Fraction(count, n) for count in counts)
    widths = tuple(right - left for left, right in zip(edges, edges[1:]))
    density = tuple(fr / width for fr, width in zip(frequencies, widths))
    cumulative = tuple(sum(frequencies[:i + 1], Fraction(0)) for i in range(len(counts)))
    return counts, frequencies, density, cumulative


def histogram_area(scores=SCORES, edges=EDGES):
    _, _, heights, _ = distribution(scores, edges)
    return sum((height * (right - left) for height, left, right
                in zip(heights, edges, edges[1:])), Fraction(0))


def stem_leaf(scores=STEM_SUBSET):
    table = {}
    for value in sorted(scores):
        if type(value) is not int or value < 0 or value > 99:
            raise ValueError("两位非负整数成绩才能生成本课茎叶示意")
        table.setdefault(value // 10, []).append(value % 10)
    if not table:
        raise ValueError("茎叶数据不能为空")
    return {stem: tuple(leaves) for stem, leaves in table.items()}


def frequency_polygon_area(scores=SCORES, edges=EDGES):
    """连组中点后两端接地面时的梯形面积；不应误说它恒等于直方图面积1。"""
    _, _, density, _ = distribution(scores, edges)
    mids = tuple(Fraction(a + b, 2) for a, b in zip(edges, edges[1:]))
    points = ((Fraction(edges[0]), Fraction(0)),) + tuple(zip(mids, density)) + ((Fraction(edges[-1]), Fraction(0)),)
    return sum(((points[i + 1][0] - points[i][0]) * (points[i][1] + points[i + 1][1]) / 2
                for i in range(len(points) - 1)), Fraction(0))
