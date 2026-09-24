"""纯数学数据层：不依赖 Manim，可由普通 Python 单独测试。"""


def union_probability(p_a, p_b, p_both):
    """返回 P(A∪B)，拒绝不可能的概率三元组。"""
    values = (p_a, p_b, p_both)
    if not all(0 <= p <= 1 for p in values):
        raise ValueError("概率必须在 [0, 1] 内")
    if not max(0, p_a + p_b - 1) <= p_both <= min(p_a, p_b):
        raise ValueError("交集概率与两事件的概率不相容")
    return p_a + p_b - p_both


def complement_probability(p_a):
    if not 0 <= p_a <= 1:
        raise ValueError("概率必须在 [0, 1] 内")
    return 1 - p_a
