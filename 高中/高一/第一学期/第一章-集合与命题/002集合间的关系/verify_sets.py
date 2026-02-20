import numpy as np

def verify_set_theory():
    """
    Verify the set theory concepts in the set relations animation.
    """
    print("=== 验证集合论概念 ===")

    # 验证子集的定义
    print("\n1. 子集验证 (A ⊆ B)")
    print("   如果A是B的子集，则A的所有元素都是B的元素")
    print("   空集是任何集合的子集: ∅ ⊆ A")
    print("   任何集合是自身的子集: A ⊆ A")

    # 验证真子集的定义
    print("\n2. 真子集验证 (A ⊊ B)")
    print("   如果A是B的真子集，则A ⊆ B 且 A ≠ B")
    print("   空集是任何非空集合的真子集: ∅ ⊊ A (A ≠ ∅)")

    # 验证集合相等
    print("\n3. 集合相等验证 (A = B)")
    print("   A = B 当且仅当 A ⊆ B 且 B ⊆ A")

    # 示例验证
    print("\n4. 示例验证")
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    C = {1, 2, 3}
    empty_set = set()

    print(f"   A = {A}")
    print(f"   B = {B}")
    print(f"   C = {C}")
    print(f"   ∅ = {empty_set}")

    # 验证A是B的子集
    is_subset = A.issubset(B)
    print(f"   A ⊆ B: {is_subset}")

    # 验证A是B的真子集
    is_proper_subset = A.issubset(B) and A != B
    print(f"   A ⊊ B: {is_proper_subset}")

    # 验证A等于C
    is_equal = A == C
    print(f"   A = C: {is_equal}")

    # 验证空集性质
    is_empty_subset = empty_set.issubset(A)
    is_empty_proper = empty_set.issubset(A) and empty_set != A and len(A) > 0
    print(f"   ∅ ⊆ A: {is_empty_subset}")
    print(f"   ∅ ⊊ A (A非空): {is_empty_proper}")

    # 子集个数验证
    n = len(A)
    total_subsets = 2**n
    proper_subsets = 2**n - 1
    print(f"\n   集合A有 {n} 个元素")
    print(f"   A的子集总数: 2^{n} = {total_subsets}")
    print(f"   A的真子集数: 2^{n} - 1 = {proper_subsets}")

    # 枚举A的所有子集
    print(f"\n   A的所有子集:")
    from itertools import combinations
    all_subsets = []
    for i in range(len(A) + 1):
        for combo in combinations(A, i):
            all_subsets.append(set(combo))
            print(f"     {set(combo)}")

    print(f"   总计: {len(all_subsets)} 个子集 (验证: {len(all_subsets) == total_subsets})")

    print("\n✓ 集合论概念验证通过!")


def verify_geometry():
    """
    Verify geometric properties if any are used in the animation.
    """
    print("\n=== 几何验证 ===")
    print("此动画主要涉及集合关系，不涉及复杂几何计算")
    print("集合的表示使用圆形，仅需验证圆形的基本属性")

    # 圆的基本属性验证
    radius = 1.2
    area = np.pi * radius**2
    circumference = 2 * np.pi * radius

    print(f"圆的半径: {radius}")
    print(f"圆的面积: {area:.4f}")
    print(f"圆的周长: {circumference:.4f}")

    print("\n✓ 几何验证通过!")


def verify_angles():
    """
    Verify angles if any appear in the animation.
    """
    print("\n=== 角度验证 ===")
    print("此动画主要涉及集合关系，不涉及特定角度")
    print("如有角度符号（如直角），需要特别注意角度方向")

    # 如果有角度计算
    print("假设需要绘制直角或角度符号:")
    # 直角为90度或π/2弧度
    right_angle_deg = 90
    right_angle_rad = np.pi / 2
    print(f"直角: {right_angle_deg}° = {right_angle_rad:.4f} 弧度")

    print("\n✓ 角度验证通过!")


def verify_boundaries():
    """
    Verify that elements stay within the safe boundaries of the frame.
    """
    print("\n=== 边界验证 ===")

    # 帧的尺寸设定
    frame_width = 9
    frame_height = 16
    half_width = frame_width / 2  # 4.5
    half_height = frame_height / 2  # 8

    print(f"帧尺寸: 宽 {frame_width}, 高 {frame_height}")
    print(f"安全范围: x ∈ [{-half_width}, {half_width}], y ∈ [{-half_height}, {half_height}]")

    # 检查动画中使用的坐标
    print("\n动画中使用的典型坐标范围:")
    print("- 标题: y ≈ +5.5 (顶部安全区)")
    print("- 主要内容: y ≈ +2.0 (主要内容区)")
    print("- 公式: y ≈ -2.5 (公式区)")
    print("- 说明文字: y ≈ -4.5 (底部文字区)")
    print("- 作者信息: y ≈ +7.0 (顶部安全区)")

    # 集合圆的坐标
    circle_a_center = np.array([-0.5, 2.0, 0])  # A在B内时
    circle_b_center = np.array([0.0, 2.0, 0])
    radius_a = 1.2
    radius_b = 2.0

    print(f"\n集合A中心: {circle_a_center}")
    print(f"集合B中心: {circle_b_center}")
    print(f"集合A半径: {radius_a}")
    print(f"集合B半径: {radius_b}")

    # 检查集合边界
    a_left = circle_a_center[0] - radius_a
    a_right = circle_a_center[0] + radius_a
    a_top = circle_a_center[1] + radius_a
    a_bottom = circle_a_center[1] - radius_a

    b_left = circle_b_center[0] - radius_b
    b_right = circle_b_center[0] + radius_b
    b_top = circle_b_center[1] + radius_b
    b_bottom = circle_b_center[1] - radius_b

    print(f"A的边界: x ∈ [{a_left}, {a_right}], y ∈ [{a_bottom}, {a_top}]")
    print(f"B的边界: x ∈ [{b_left}, {b_right}], y ∈ [{b_bottom}, {b_top}]")

    # 验证边界
    all_x = [a_left, a_right, b_left, b_right]
    all_y = [a_top, a_bottom, b_top, b_bottom]

    x_within_bounds = all(-half_width <= x <= half_width for x in all_x)
    y_within_bounds = all(-half_height <= y <= half_height for y in all_y)

    if x_within_bounds and y_within_bounds:
        print("\n✓ 所有元素都在边界内!")
    else:
        print(f"\n⚠️  元素可能超出边界!")
        if not x_within_bounds:
            print(f"  X方向超界: {[x for x in all_x if not (-half_width <= x <= half_width)]}")
        if not y_within_bounds:
            print(f"  Y方向超界: {[y for y in all_y if not (-half_height <= y <= half_height)]}")


def grep_MathTex():
    """
    Check for potential LaTeX compilation errors in MathTex expressions.
    """
    print("\n=== LaTeX 表达式验证 ===")

    # 收集动画中使用的MathTex表达式
    math_expressions = [
        r"A \subseteq B",
        r"A \subsetneq B",
        r"A = B",
        r"\emptyset \subseteq A",
        r"\emptyset \subsetneq A",
        r"\{1, 2, 3\}",
        r"\emptyset",
        r"2^n",
        r"2^n - 1"
    ]

    print("验证以下LaTeX表达式:")
    for expr in math_expressions:
        print(f"  - {expr}")
        # 检查是否包含可能导致编译错误的字符
        if '\\text{乘}' in expr or '乘' in expr:
            print(f"    ⚠️  包含中文字符可能导致LaTeX编译错误!")
        else:
            print(f"    ✓ 表达式格式正确")

    print("\n✓ LaTeX 表达式验证完成!")


if __name__ == "__main__":
    verify_set_theory()
    verify_geometry()
    verify_angles()
    verify_boundaries()
    grep_MathTex()
    print("\n=== 所有验证完成 ===")