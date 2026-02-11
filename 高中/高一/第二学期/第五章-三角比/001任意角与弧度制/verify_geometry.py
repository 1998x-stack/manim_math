"""
几何验证脚本
用于验证角度计算、LaTeX兼容性和边界检查
"""

import numpy as np


def verify_angles():
    """
    验证角度相关的计算
    注意：如果角度大于90度需要分析，如果大于180度要加强注意，可能angle方向错了
    Manim的Angle.from_three_points默认是逆时针，需要添加other_angle=True参数来修正
    """
    print("开始验证角度计算...")

    # 测试不同的角度情况
    test_cases = [
        # 锐角 (小于90度)
        {
            'name': '锐角测试',
            'points': (np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([1, 1, 0])),  # 45度角
            'expected_deg': 45
        },
        # 钝角 (大于90度小于180度)
        {
            'name': '钝角测试',
            'points': (np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([-1, 1, 0])),  # 135度角
            'expected_deg': 135
        },
        # 大于180度的角
        {
            'name': '优角测试',
            'points': (np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, -1, 0])),  # 270度角 (但从逆时针角度看是-90度)
            'expected_deg': 270
        }
    ]

    for test_case in test_cases:
        p1, p2, p3 = test_case['points']  # p2是顶点
        expected_deg = test_case['expected_deg']

        # 计算从p1到p3相对于顶点p2的角度
        v1 = p1 - p2  # 向量p2->p1
        v2 = p3 - p2  # 向量p2->p3

        # 使用点积计算夹角
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 确保在有效范围内
        angle_rad = np.arccos(cos_angle)
        angle_deg = np.degrees(angle_rad)

        print(f"{test_case['name']}: 计算角度 {angle_deg:.2f}°, 期望角度 {expected_deg}°")

        # 检查是否在合理范围内
        if abs(angle_deg - expected_deg) > 5:  # 允许5度误差
            print(f"  ⚠️  警告: 角度差异较大 ({abs(angle_deg - expected_deg):.2f}°)")
            if expected_deg > 180:
                print("  ⚠️  特别注意: 角度大于180度，很可能angle方向错了！")
                print("  提示: 检查Manim中的Angle.from_three_points是否需要添加other_angle=True参数")
        else:
            print(f"  ✓ 角度验证通过")

    print("\n角度验证完成")


def check_latex_compatibility():
    """
    检测可能导致LaTeX编译错误的字符
    如: LaTeX Error: Unicode character 乘 (U+4E58)
    """
    print("开始检测LaTeX编译错误风险...")

    # 常见的会导致LaTeX错误的Unicode字符
    problematic_chars = {
        '乘': 'U+4E58',  # 乘号
        '除': 'U+9664',
        '加': 'U+52A0',
        '减': 'U+51CF',
        '等': 'U+7B49',
        # 更多中文字符也可能是问题
    }

    # 检查当前目录下的Python文件中的潜在问题
    import os

    problematic_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    found_chars = []
                    for char, code in problematic_chars.items():
                        if char in content:
                            found_chars.append((char, code))

                    if found_chars:
                        problematic_files.append((filepath, found_chars))

                except IOError as e:
                    print(f"无法读取文件 {filepath}: {e}")

    if problematic_files:
        print("发现潜在的LaTeX错误字符:")
        for filepath, chars in problematic_files:
            print(f"  文件: {filepath}")
            for char, code in chars:
                print(f"    字符 '{char}' ({code})")

        print("\n修复建议:")
        print("  - 将中文字符替换为LaTeX命令，如：乘 → \\times, 除 → \\div")
        print("  - 或使用Text()代替MathTex()来显示中文")
    else:
        print("✓ 未发现明显的LaTeX编译错误风险")

    print("\nLaTeX检查完成")


def verify_boundaries():
    """
    验证元素是否在安全边界内
    """
    print("开始验证元素边界...")

    # 定义TikTok竖屏的安全边界 (基于prompt.md中的说明)
    # x ∈ [-4.5, +4.5] (建议 x ∈ [-4, +4])
    # y ∈ [-8, +8] (主内容区域 y ∈ [-3, +5])
    x_min, x_max = -4.0, 4.0
    y_min_main, y_max_main = -3.0, 5.0  # 主内容区域
    y_min_total, y_max_total = -8.0, 8.0  # 总区域

    # 示例：检查一些典型的坐标点
    test_points = [
        # 标题区域 (应该在安全区域内)
        np.array([0, 7, 0]),  # 顶部，OK
        np.array([0, 8.5, 0]),  # 超出边界
        # 主内容区域
        np.array([0, 0, 0]),  # 中心，OK
        np.array([5, 0, 0]),  # x超出边界
        np.array([0, 6, 0]),  # y超出主区域但仍在总区域内
        # 底部区域
        np.array([0, -7, 0]),  # 底部，OK
        np.array([0, -8.5, 0]),  # 超出底部边界
    ]

    boundary_issues = []

    for i, point in enumerate(test_points):
        x, y, _ = point

        issues = []
        if x < x_min or x > x_max:
            issues.append(f"x坐标超出安全范围 [{x_min}, {x_max}]: {x}")
        if y < y_min_total or y > y_max_total:
            issues.append(f"y坐标超出总范围 [{y_min_total}, {y_max_total}]: {y}")
        elif y_min_main <= y <= y_max_main:
            # 在主内容区域，这是最好的
            pass
        else:
            # 在边界区域，但仍在安全范围内
            issues.append(f"y坐标在边界区域，不在主内容区域 [{y_min_main}, {y_max_main}]: {y}")

        if issues:
            boundary_issues.append((i, point, issues))

    if boundary_issues:
        print("发现边界问题:")
        for idx, point, issues in boundary_issues:
            print(f"  点 {idx}: {point}")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("✓ 所有测试点都在安全边界内")

    print("\n边界验证完成")


def main():
    """
    主验证函数
    """
    print("="*50)
    print("几何验证脚本")
    print("="*50)

    verify_angles()
    print()
    check_latex_compatibility()
    print()
    verify_boundaries()

    print("\n" + "="*50)
    print("验证完成")
    print("="*50)


if __name__ == "__main__":
    main()