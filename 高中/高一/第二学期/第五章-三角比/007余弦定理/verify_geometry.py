"""
几何验证脚本
专门用于验证余弦定理动画中的几何计算
"""

import numpy as np
import sys
import os

# 添加当前路径以导入动画文件
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def verify_angles():
    """
    验证角度相关的计算
    注意：如果角度大于90度需要分析，如果大于180度要加强注意，可能angle方向错了
    Manim的Angle.from_three_points默认是逆时针，需要添加other_angle=True参数来修正
    """
    print("开始验证角度计算...")

    # 使用余弦定理动画中的三角形顶点
    A = np.array([-2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])  # 应用SCALE和OFFSET
    B = np.array([2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])
    C = np.array([0.5, 2.0, 0]) * 0.9 + np.array([0, 1, 0])

    # 计算各个角
    def calculate_angle_at_vertex(point1, vertex, point2):
        """计算顶点处的角度 (弧度)"""
        v1 = point1 - vertex
        v2 = point2 - vertex

        # 使用向量计算夹角
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 防止浮点误差导致超出范围
        return np.arccos(cos_angle)

    angle_A = calculate_angle_at_vertex(B, A, C)  # ∠BAC
    angle_B = calculate_angle_at_vertex(A, B, C)  # ∠ABC
    angle_C = calculate_angle_at_vertex(A, C, B)  # ∠ACB

    print(f"角A (∠BAC): {np.degrees(angle_A):.2f}° ({angle_A:.3f} 弧度)")
    print(f"角B (∠ABC): {np.degrees(angle_B):.2f}° ({angle_B:.3f} 弧度)")
    print(f"角C (∠ACB): {np.degrees(angle_C):.2f}° ({angle_C:.3f} 弧度)")

    # 验证角度和为180度
    total_angle_deg = np.degrees(angle_A + angle_B + angle_C)
    print(f"角度和: {total_angle_deg:.2f}° (应为180°)")

    if abs(total_angle_deg - 180) < 0.1:
        print("✓ 角度和验证通过")
    else:
        print(f"⚠️  角度和不等于180°: {total_angle_deg:.2f}")

    # 检查是否有大于180度的角（需要使用other_angle参数）
    angles = [("A", angle_A), ("B", angle_B), ("C", angle_C)]
    for name, angle in angles:
        if angle > np.pi:
            print(f"⚠️  角{name}大于180度 ({np.degrees(angle):.2f}°)，注意Manim中的Angle方向!")
            print("  提示: 检查Manim中的Angle.from_three_points是否需要添加other_angle=True参数")
        elif angle > np.pi/2:  # 大于90度的钝角
            print(f"⚠️  角{name}为钝角 ({np.degrees(angle):.2f}°)，可能需要注意角度方向")


def verify_cosine_theorem():
    """
    验证余弦定理的正确性
    """
    print("\n开始验证余弦定理...")

    # 使用余弦定理动画中的三角形顶点
    A = np.array([-2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])  # 应用SCALE和OFFSET
    B = np.array([2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])
    C = np.array([0.5, 2.0, 0]) * 0.9 + np.array([0, 1, 0])

    # 计算边长
    a = np.linalg.norm(B - C)  # BC 边，对应角A
    b = np.linalg.norm(C - A)  # CA 边，对应角B
    c = np.linalg.norm(A - B)  # AB 边，对应角C

    print(f"边长: a(BC)={a:.3f}, b(CA)={b:.3f}, c(AB)={c:.3f}")

    # 计算角度
    def calculate_angle_at_vertex(point1, vertex, point2):
        v1 = point1 - vertex
        v2 = point2 - vertex
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)

    angle_A = calculate_angle_at_vertex(B, A, C)  # ∠BAC
    angle_B = calculate_angle_at_vertex(A, B, C)  # ∠ABC
    angle_C = calculate_angle_at_vertex(A, C, B)  # ∠ACB

    print(f"角度: A={np.degrees(angle_A):.2f}°, B={np.degrees(angle_B):.2f}°, C={np.degrees(angle_C):.2f}°")

    epsilon = 1e-5

    # 验证 a² = b² + c² - 2bc cos(A)
    lhs_a = a ** 2
    rhs_a = b ** 2 + c ** 2 - 2 * b * c * np.cos(angle_A)
    print(f"\n验证 a² = b² + c² - 2bc cos(A):")
    print(f"  左边: a² = {lhs_a:.6f}")
    print(f"  右边: b² + c² - 2bc cos(A) = {rhs_a:.6f}")
    if abs(lhs_a - rhs_a) < epsilon:
        print("  ✓ 余弦定理 a²=b²+c²-2bc*cos(A) 验证通过")
    else:
        print(f"  ⚠️  余弦定理 a²=b²+c²-2bc*cos(A) 验证失败: {abs(lhs_a - rhs_a):.8f}")

    # 验证 b² = a² + c² - 2ac cos(B)
    lhs_b = b ** 2
    rhs_b = a ** 2 + c ** 2 - 2 * a * c * np.cos(angle_B)
    print(f"\n验证 b² = a² + c² - 2ac cos(B):")
    print(f"  左边: b² = {lhs_b:.6f}")
    print(f"  右边: a² + c² - 2ac cos(B) = {rhs_b:.6f}")
    if abs(lhs_b - rhs_b) < epsilon:
        print("  ✓ 余弦定理 b²=a²+c²-2ac*cos(B) 验证通过")
    else:
        print(f"  ⚠️  余弦定理 b²=a²+c²-2ac*cos(B) 验证失败: {abs(lhs_b - rhs_b):.8f}")

    # 验证 c² = a² + b² - 2ab cos(C)
    lhs_c = c ** 2
    rhs_c = a ** 2 + b ** 2 - 2 * a * b * np.cos(angle_C)
    print(f"\n验证 c² = a² + b² - 2ab cos(C):")
    print(f"  左边: c² = {lhs_c:.6f}")
    print(f"  右边: a² + b² - 2ab cos(C) = {rhs_c:.6f}")
    if abs(lhs_c - rhs_c) < epsilon:
        print("  ✓ 余弦定理 c²=a²+b²-2ab*cos(C) 验证通过")
    else:
        print(f"  ⚠️  余弦定理 c²=a²+b²-2ab*cos(C) 验证失败: {abs(lhs_c - rhs_c):.8f}")


def check_latex_compatibility():
    """
    检测可能导致LaTeX编译错误的字符
    如: LaTeX Error: Unicode character 乘 (U+4E58)
    """
    print("\n开始检测LaTeX编译错误风险...")

    # 检查当前Python文件中的潜在问题
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "007_余弦定理.py")

    if not os.path.exists(filepath):
        print(f"⚠️  未找到动画文件: {filepath}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 常见的会导致LaTeX错误的Unicode字符
        problematic_chars = {
            '乘': 'U+4E58',  # 乘号
            '除': 'U+9664',
            '加': 'U+52A0',
            '减': 'U+51CF',
            '等': 'U+7B49',
        }

        found_chars = []
        for char, code in problematic_chars.items():
            if char in content:
                found_chars.append((char, code))

        if found_chars:
            print("发现潜在的LaTeX错误字符:")
            for char, code in found_chars:
                print(f"  字符 '{char}' ({code})")
            print("\n修复建议:")
            print("  - 将中文字符替换为LaTeX命令，如：乘 → \\times, 除 → \\div")
            print("  - 或使用Text()代替MathTex()来显示中文")
        else:
            print("✓ 未发现明显的LaTeX编译错误风险")

        # 特别检查MathTex中是否使用了度数符号
        import re
        degree_pattern = r'[0-9]+°'
        degree_matches = re.findall(degree_pattern, content)
        if degree_matches:
            print(f"\n⚠️  发现度数符号(°)的使用: {degree_matches}")
            print("  提示: 在MathTex中应使用 ^\\circ 替代 °")

    except IOError as e:
        print(f"无法读取文件 {filepath}: {e}")


def verify_boundaries():
    """
    验证元素是否在安全边界内
    """
    print("\n开始验证元素边界...")

    # 定义TikTok竖屏的安全边界 (基于prompt.md中的说明)
    # x ∈ [-4.5, +4.5] (建议 x ∈ [-4, +4])
    # y ∈ [-8, +8] (主内容区域 y ∈ [-3, +5])
    x_min, x_max = -4.0, 4.0
    y_min_main, y_max_main = -3.0, 5.0  # 主内容区域
    y_min_total, y_max_total = -8.0, 8.0  # 总区域

    # 使用动画中的三角形顶点进行测试
    A = np.array([-2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])  # 应用SCALE和OFFSET
    B = np.array([2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0])
    C = np.array([0.5, 2.0, 0]) * 0.9 + np.array([0, 1, 0])

    triangle_points = [A, B, C]

    boundary_issues = []

    for i, point in enumerate(triangle_points):
        x, y, _ = point

        issues = []
        if x < x_min or x > x_max:
            issues.append(f"x坐标超出安全范围 [{x_min}, {x_max}]: {x:.2f}")
        if y < y_min_total or y > y_max_total:
            issues.append(f"y坐标超出总范围 [{y_min_total}, {y_max_total}]: {y:.2f}")
        elif y_min_main <= y <= y_max_main:
            # 在主内容区域，这是最好的
            pass
        else:
            # 在边界区域，但仍在安全范围内
            issues.append(f"y坐标在边界区域，不在主内容区域 [{y_min_main}, {y_max_main}]: {y:.2f}")

        if issues:
            boundary_issues.append((i, point, issues))

    # 检查其他可能的位置
    test_positions = [
        np.array([0, 7.5, 0]),  # 作者信息位置
        np.array([0, 6, 0]),    # 标题位置
        np.array([0, -5, 0]),   # 底部关注提示位置
    ]

    for pos in test_positions:
        x, y, _ = pos
        issues = []
        if x < x_min or x > x_max:
            issues.append(f"x坐标超出安全范围 [{x_min}, {x_max}]: {x:.2f}")
        if y < y_min_total or y > y_max_total:
            issues.append(f"y坐标超出总范围 [{y_min_total}, {y_max_total}]: {y:.2f}")

        if issues:
            boundary_issues.append(('position', pos, issues))

    if boundary_issues:
        print("发现边界问题:")
        for idx, point, issues in boundary_issues:
            print(f"  位置 {idx}: {point}")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("✓ 所有测试点都在安全边界内")


def main():
    """
    主验证函数
    """
    print("="*60)
    print("余弦定理动画几何验证脚本")
    print("="*60)

    verify_angles()
    verify_cosine_theorem()
    check_latex_compatibility()
    verify_boundaries()

    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()