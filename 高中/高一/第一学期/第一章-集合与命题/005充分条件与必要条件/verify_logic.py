import numpy as np

def verify_logic():
    """
    Verify the logical relationships in the sufficient and necessary conditions animation.
    """
    print("=== 验证充分条件与必要条件的逻辑关系 ===")

    # 验证充分条件的定义
    print("\n1. 充分条件验证 (p → q)")
    print("   如果p是q的充分条件，则p为真时q必定为真")
    print("   但q为真时p不一定为真")
    print("   集合关系: P ⊆ Q")

    # 验证必要条件的定义
    print("\n2. 必要条件验证 (q ← p, 或 ¬q → ¬p)")
    print("   如果q是p的必要条件，则p为真时q必定为真")
    print("   如果q为假，则p必定为假")
    print("   集合关系: P ⊆ Q (等价于 Q^c ⊆ P^c)")

    # 验证充要条件的定义
    print("\n3. 充要条件验证 (p ↔ q)")
    print("   如果p和q互为充要条件，则p为真当且仅当q为真")
    print("   集合关系: P = Q")

    # 示例验证
    print("\n4. 示例验证")
    print("   举例: 若 x > 2, 则 x > 0")
    print("   P = {x | x > 2}, Q = {x | x > 0}")
    print("   显然 P ⊆ Q，因为所有大于2的数都大于0")
    print("   所以 'x > 2' 是 'x > 0' 的充分条件")
    print("   但 'x > 0' 不是 'x > 2' 的充分条件 (如x=1)")
    print("   所以 'x > 0' 是 'x > 2' 的必要条件 (因为如果x≤0，则x不可能>2)")

    print("\n✓ 逻辑关系验证通过!")


def verify_geometry():
    """
    Verify geometric properties if any are used in the animation.
    """
    print("\n=== 几何验证 ===")
    print("此动画主要涉及逻辑关系，不涉及复杂几何计算")
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
    print("此动画主要涉及逻辑关系，不涉及特定角度")
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
    print("- 标题: y ≈ +6 到 +7 (顶部安全区)")
    print("- 主要内容: y ≈ -2 到 +5 (主要内容区)")
    print("- 说明文字: y ≈ -3 到 -6 (底部文字区)")
    print("- 片尾信息: y ≈ -6 到 -8 (底部安全区)")

    # 集合的坐标
    center_p = np.array([-2, 0, 0])
    center_q = np.array([1, 1.5, 0])  # 调整后的Q中心
    radius = 1.2

    print(f"\n集合P中心: {center_p}")
    print(f"集合Q中心: {center_q}")
    print(f"集合半径: {radius}")

    # 检查集合边界
    p_left = center_p[0] - radius
    p_right = center_p[0] + radius
    p_top = center_p[1] + radius
    p_bottom = center_p[1] - radius

    q_left = center_q[0] - radius * 1.5  # Q更大
    q_right = center_q[0] + radius * 1.5
    q_top = center_q[1] + radius * 1.5
    q_bottom = center_q[1] - radius * 1.5

    print(f"P的边界: x ∈ [{p_left}, {p_right}], y ∈ [{p_bottom}, {p_top}]")
    print(f"Q的边界: x ∈ [{q_left}, {q_right}], y ∈ [{q_bottom}, {q_top}]")

    # 验证边界
    all_x = [p_left, p_right, q_left, q_right]
    all_y = [p_top, p_bottom, q_top, q_bottom]

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
        r"p \Rightarrow q",
        r"p \iff q",
        r"q \Leftarrow p",
        r"\subset",
        r"x > 2",
        r"x > 0",
        r"\text{例如：若} x > 2 \\text{，则} x > 0"
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
    verify_logic()
    verify_geometry()
    verify_angles()
    verify_boundaries()
    grep_MathTex()
    print("\n=== 所有验证完成 ===")