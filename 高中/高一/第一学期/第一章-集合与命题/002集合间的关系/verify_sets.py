"""集合关系动画的纯 Python 数学与几何回归检查。

运行：python verify_sets.py
本脚本不导入 Manim，也不声称验证了 LaTeX 编译、字体或最终画面。
"""

from itertools import combinations
from math import hypot, pi


def require(condition, message):
    """避免使用会被 ``python -O`` 移除的 assert 语句。"""
    if not condition:
        raise AssertionError(message)


def powerset(items):
    """返回有限集合的所有子集，迭代顺序固定，便于复现。"""
    ordered = tuple(sorted(items))
    return [frozenset(group) for size in range(len(ordered) + 1)
            for group in combinations(ordered, size)]


def verify_set_theory():
    """覆盖空集、自反性、真包含、相等与有限集合子集计数。"""
    universe = frozenset(range(4))
    subsets = powerset(universe)
    require(len(subsets) == 2 ** len(universe), "全集子集总数不正确")
    require(len(set(subsets)) == len(subsets), "子集枚举出现重复")

    for a in subsets:
        require(frozenset().issubset(a), "空集应为任意集合的子集")
        require(a.issubset(a), "子集关系应满足自反性")
        require(len(powerset(a)) == 2 ** len(a), "子集计数应为 2^n")
        require(sum(candidate < a for candidate in powerset(a)) == 2 ** len(a) - 1,
                "真子集计数应为 2^n-1")
        for b in subsets:
            require((a < b) == (a <= b and a != b), "真子集定义不成立")
            require((a == b) == (a <= b and b <= a), "集合相等的双向包含条件不成立")
            if a <= b:
                require(all(item in b for item in a), "子集定义不成立")
    require(not (frozenset() < frozenset()), "空集不是自身的真子集")
    print("PASS: 集合关系与 2^n / (2^n-1) 子集计数")


def circle_inside_circle(inner_center, inner_radius, outer_center, outer_radius):
    """按圆心距判断小圆是否完整落在大圆内；仅用于当前圆形布局。"""
    if inner_radius < 0 or outer_radius < 0:
        return False
    return (hypot(inner_center[0] - outer_center[0],
                  inner_center[1] - outer_center[1]) + inner_radius
            <= outer_radius + 1e-12)


def verify_geometry():
    """检查当前子集 Venn 圆的包含关系，而非仅打印圆面积。"""
    a_center, a_radius = (-0.5, 2.0), 1.2
    b_center, b_radius = (0.0, 2.0), 2.0
    require(circle_inside_circle(a_center, a_radius, b_center, b_radius),
            "子集示意图中 A 未完整位于 B 内")
    require(not circle_inside_circle(b_center, b_radius, a_center, a_radius),
            "不应将 B 画成 A 的子集")
    require(pi * a_radius ** 2 < pi * b_radius ** 2, "子集圆面积应小于母集圆")
    print("PASS: Venn 圆包含关系")


def verify_angles():
    """当前集合关系动画无需角度证明，不以无关的直角计算冒充测试。"""
    print("SKIP: 本课无须检验的角度性质")


def verify_boundaries():
    """仅检查当前圆的理论坐标，不代表渲染后文字也位于安全区。"""
    safe_x, safe_y = 4.0, 7.0
    configs = (((-1.5, 2.0), 1.3), ((1.5, 2.0), 1.3),
               ((-0.5, 2.0), 1.2), ((0.0, 2.0), 2.0))
    for (x, y), radius in configs:
        require(radius > 0, "圆半径必须为正")
        require(abs(x) + radius < safe_x and abs(y) + radius < safe_y,
                "集合圆超出预设安全范围")
    print("PASS: 集合圆静态坐标边界；文字和动画仍需目视审核")


def grep_MathTex():
    """保留历史入口，但不能通过检查静态字符串证明 LaTeX 可编译。"""
    print("SKIP: LaTeX 表达式须在安装 Manim/TeX 的环境中实际渲染")


def main():
    verify_set_theory()
    verify_geometry()
    verify_angles()
    verify_boundaries()
    grep_MathTex()
    print("PASS: 已运行的纯 Python 检查全部通过")


if __name__ == "__main__":
    main()
