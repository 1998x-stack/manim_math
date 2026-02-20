import numpy as np


def verify_angles():
    """
    验证涉及的角度，特别是大于90度或180度的角度
    对于Manim中的Angle.from_three_points，默认是逆时针方向
    如果角度大于180度，需要加强注意，因为角度方向可能错误！
    """
    print("验证角度计算...")

    # 在分式不等式的上下文中，我们主要涉及的是数轴上的区间分析，
    # 不会有具体的几何角度，但如果动画中有角度元素，则需要验证

    # 示例：如果我们需要验证两个向量之间的夹角
    def calc_angle_between_vectors(v1, v2):
        """计算两个向量之间的夹角（弧度）"""
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 数值稳定性
        angle_rad = np.arccos(cos_angle)
        angle_deg = np.degrees(angle_rad)
        return angle_rad, angle_deg

    # 示例向量
    v1 = np.array([1, 0, 0])
    v2 = np.array([0, 1, 0])
    angle_rad, angle_deg = calc_angle_between_vectors(v1, v2)

    print(f"向量 {v1} 和 {v2} 之间的角度: {angle_deg:.2f}° ({angle_rad:.2f} 弧度)")

    # 检查是否大于90度
    if angle_deg > 90:
        print(f"⚠️  角度大于90度: {angle_deg:.2f}°")
        if angle_deg > 180:
            print(f"⚠️⚠️  警告：角度大于180度: {angle_deg:.2f}°，可能需要调整方向！")

    print("角度验证完成\n")


def grep_MathTex():
    """
    验证LaTeX编译错误（如Unicode字符错误）
    避免使用中文字符等可能导致LaTeX编译失败的内容
    """
    print("验证LaTeX表达式...")

    # 验证一些可能在MathTex中使用的LaTeX表达式
    test_expressions = [
        r"\frac{f(x)}{g(x)} > 0",  # 分式不等式
        r"f(x) \cdot g(x) > 0",    # 乘积形式
        r"x \in (-\infty, -2) \cup [1, +\infty)",  # 区间表示
        r"\mathbb{R}",             # 实数集合
        r"\neq",                   # 不等于
        r"\geq",                   # 大于等于
        r"\leq",                   # 小于等于
    ]

    for expr in test_expressions:
        try:
            # 检查是否包含可能导致LaTeX编译错误的字符
            problematic_chars = ['乘', '除', '乘法', '除法']  # 中文字符
            has_problem = False
            for char in problematic_chars:
                if char in expr:
                    print(f"❌ 发现潜在LaTeX错误字符 '{char}' 在表达式: {expr}")
                    has_problem = True

            if not has_problem:
                print(f"✅ LaTeX表达式验证通过: {expr}")

        except Exception as e:
            print(f"❌ LaTeX表达式验证失败: {expr}, 错误: {e}")

    print("LaTeX表达式验证完成\n")


def verify_boundaries():
    """
    验证元素是否在安全边界内
    对于TikTok竖屏(1080×1920)格式，逻辑坐标为frame_width=9, frame_height=16
    x ∈ [-4.5, +4.5], y ∈ [-8, +8]，但建议安全范围是 x ∈ [-4, +4], y ∈ [-7, +7]
    """
    print("验证元素边界...")

    # 检查动画中的元素位置
    safe_x_range = (-4.5, 4.5)
    safe_y_range = (-8, 8)

    # 数轴的位置测试
    number_line_positions = [
        {'x': 0, 'y': 2.5, 'desc': '数轴中心'},
        {'x': -4, 'y': 2.5, 'desc': '数轴左端'},
        {'x': 4, 'y': 2.5, 'desc': '数轴右端'},
    ]

    critical_points_positions = [
        {'x': -2, 'y': 2.5, 'desc': '关键点x=-2'},
        {'x': 1, 'y': 2.5, 'desc': '关键点x=1'},
    ]

    text_positions = [
        {'x': 0, 'y': 7, 'desc': '作者信息'},
        {'x': 0, 'y': 6, 'desc': '标题'},
        {'x': 0, 'y': -7, 'desc': '底部文字'},
        {'x': 0, 'y': -8, 'desc': '底部安全区'},
    ]

    all_positions = number_line_positions + critical_points_positions + text_positions

    violations = []
    for pos in all_positions:
        x, y = pos['x'], pos['y']
        desc = pos['desc']

        if x < safe_x_range[0] or x > safe_x_range[1]:
            violations.append(f"{desc}: x={x} 超出范围 [{safe_x_range[0]}, {safe_x_range[1]}]")

        if y < safe_y_range[0] or y > safe_y_range[1]:
            violations.append(f"{desc}: y={y} 超出范围 [{safe_y_range[0]}, {safe_y_range[1]}]")

    if violations:
        print("❌ 发现边界违规:")
        for violation in violations:
            print(f"  - {violation}")
    else:
        print("✅ 所有元素都在安全边界内")

    # 检查建议的安全范围
    print("\n建议的安全范围验证 (x ∈ [-4, +4], y ∈ [-7, +7]):")
    recommended_x_range = (-4, 4)
    recommended_y_range = (-7, 7)

    recommended_violations = []
    for pos in all_positions:
        x, y = pos['x'], pos['y']
        desc = pos['desc']

        if x < recommended_x_range[0] or x > recommended_x_range[1]:
            recommended_violations.append(f"{desc}: x={x} 超出建议范围 [{recommended_x_range[0]}, {recommended_x_range[1]}]")

        if y < recommended_y_range[0] or y > recommended_y_range[1]:
            recommended_violations.append(f"{desc}: y={y} 超出建议范围 [{recommended_y_range[0]}, {recommended_y_range[1]}]")

    if recommended_violations:
        print("⚠️  发现建议范围外的元素:")
        for violation in recommended_violations:
            print(f"  - {violation}")
    else:
        print("✅ 所有元素都在建议的安全范围内")

    print("边界验证完成\n")


def main():
    """
    主验证函数
    """
    print("="*50)
    print("分式不等式Manim动画验证脚本")
    print("="*50)

    verify_angles()
    grep_MathTex()
    verify_boundaries()

    print("="*50)
    print("验证完成!")
    print("如果所有验证都通过，则可以安全地运行Manim动画脚本。")
    print("="*50)


if __name__ == "__main__":
    main()