"""
几何验证脚本
用于验证含绝对值不等式的计算和边界检查
"""
import numpy as np


def verify_absolute_value_definitions():
    """
    验证绝对值定义和基本性质
    """
    print("开始验证绝对值定义...")
    
    # 测试不同的数值情况
    test_cases = [
        # 正数情况
        {
            'name': '正数测试',
            'value': 5,
            'expected_abs': 5,
            'expected_sign': 1
        },
        # 负数情况
        {
            'name': '负数测试',
            'value': -3,
            'expected_abs': 3,
            'expected_sign': -1
        },
        # 零情况
        {
            'name': '零测试',
            'value': 0,
            'expected_abs': 0,
            'expected_sign': 0
        },
        # 小数情况
        {
            'name': '小数测试',
            'value': -2.5,
            'expected_abs': 2.5,
            'expected_sign': -1
        }
    ]
    
    for test_case in test_cases:
        val = test_case['value']
        expected_abs = test_case['expected_abs']
        expected_sign = test_case['expected_sign']
        
        # 计算绝对值
        calculated_abs = abs(val)
        
        # 计算符号 (signum函数)
        if val > 0:
            calculated_sign = 1
        elif val < 0:
            calculated_sign = -1
        else:
            calculated_sign = 0
        
        print(f"{test_case['name']}: |{val}| = {calculated_abs}, 期望值 {expected_abs}")
        
        # 检查是否在合理范围内
        if abs(calculated_abs - expected_abs) > 1e-10:
            print(f"  ❌ 错误: 绝对值计算错误!")
        else:
            print(f"  ✓ 绝对值验证通过")
        
        if calculated_sign != expected_sign:
            print(f"  ❌ 错误: 符号计算错误!")
        else:
            print(f"  ✓ 符号验证通过")
    
    print("\n绝对值定义验证完成")


def verify_basic_inequalities():
    """
    验证基本绝对值不等式解法
    """
    print("\n开始验证基本绝对值不等式解法...")
    
    # 测试 |x| < a 的情况 (a > 0)
    a = 3
    x_values_for_less_than = [-2.5, 0, 2.9]  # 应该满足 |x| < 3
    x_values_for_not_less_than = [-3.1, 3.2]  # 应该不满足 |x| < 3
    
    print(f"验证 |x| < {a} ⟺ -{a} < x < {a}:")
    for x in x_values_for_less_than:
        abs_x = abs(x)
        satisfies_ineq = -a < x < a
        satisfies_abs_ineq = abs_x < a
        if satisfies_ineq and satisfies_abs_ineq:
            print(f"  ✓ x = {x}: |x| = {abs_x} < {a}, -{a} < {x} < {a}")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    for x in x_values_for_not_less_than:
        abs_x = abs(x)
        satisfies_ineq = -a < x < a
        satisfies_abs_ineq = abs_x < a
        if not satisfies_ineq and not satisfies_abs_ineq:
            print(f"  ✓ x = {x}: |x| = {abs_x} ≮ {a}, {x} ∉ (-{a}, {a})")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    # 验证 |x| > a 的情况 (a > 0)
    x_values_for_greater_than = [-4, 4]  # 应该满足 |x| > 3
    x_values_for_not_greater_than = [-2, 0, 2]  # 应该不满足 |x| > 3
    
    print(f"\n验证 |x| > {a} ⟺ x < -{a} 或 x > {a}:")
    for x in x_values_for_greater_than:
        abs_x = abs(x)
        satisfies_ineq = (x < -a) or (x > a)
        satisfies_abs_ineq = abs_x > a
        if satisfies_ineq and satisfies_abs_ineq:
            print(f"  ✓ x = {x}: |x| = {abs_x} > {a}, {x} ∈ (-∞, -{a}) ∪ ({a}, +∞)")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    for x in x_values_for_not_greater_than:
        abs_x = abs(x)
        satisfies_ineq = (x < -a) or (x > a)
        satisfies_abs_ineq = abs_x > a
        if not satisfies_ineq and not satisfies_abs_ineq:
            print(f"  ✓ x = {x}: |x| = {abs_x} ≯ {a}, {x} ∉ (-∞, -{a}) ∪ ({a}, +∞)")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    print("\n基本绝对值不等式验证完成")


def verify_shifted_inequalities():
    """
    验证平移型绝对值不等式 |x-a| < b
    """
    print("\n开始验证平移型绝对值不等式...")
    
    # 测试 |x-2| < 1 的情况
    center = 2
    radius = 1
    lower_bound = center - radius  # 1
    upper_bound = center + radius  # 3
    
    x_valid = [1.5, 2, 2.9]  # 应该满足 |x-2| < 1
    x_invalid = [0.5, 3.5]    # 应该不满足 |x-2| < 1
    
    print(f"验证 |x-{center}| < {radius} ⟺ {lower_bound} < x < {upper_bound}:")
    for x in x_valid:
        dist_to_center = abs(x - center)
        satisfies_original = dist_to_center < radius
        satisfies_transformed = lower_bound < x < upper_bound
        if satisfies_original and satisfies_transformed:
            print(f"  ✓ x = {x}: |x-{center}| = {dist_to_center} < {radius}, {lower_bound} < {x} < {upper_bound}")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    for x in x_invalid:
        dist_to_center = abs(x - center)
        satisfies_original = dist_to_center < radius
        satisfies_transformed = lower_bound < x < upper_bound
        if not satisfies_original and not satisfies_transformed:
            print(f"  ✓ x = {x}: |x-{center}| = {dist_to_center} ≮ {radius}, {x} ∉ ({lower_bound}, {upper_bound})")
        else:
            print(f"  ❌ x = {x}: 验证失败")
    
    print("\n平移型绝对值不等式验证完成")


def verify_triangle_inequality():
    """
    验证三角不等式 |a + b| ≤ |a| + |b|
    """
    print("\n开始验证三角不等式 |a + b| ≤ |a| + |b|...")
    
    # 测试各种数值组合
    test_combinations = [
        (3, 4),     # 两个正数
        (-3, 4),    # 一正一负
        (3, -4),    # 一正一负
        (-3, -4),   # 两个负数
        (0, 5),     # 其中一个为0
        (2.5, -1.7) # 小数
    ]
    
    all_passed = True
    for a, b in test_combinations:
        left_side = abs(a + b)
        right_side = abs(a) + abs(b)
        
        satisfies = left_side <= right_side
        
        print(f"  a={a}, b={b}: |{a}+{b}| = |{a+b}| = {left_side}, |{a}|+|{b}| = {abs(a)}+{abs(b)} = {right_side}, 满足: {satisfies}")
        
        if not satisfies:
            print(f"    ❌ 三角不等式验证失败!")
            all_passed = False
        else:
            print(f"    ✓ 三角不等式验证通过")
    
    if all_passed:
        print("  ✓ 所有三角不等式验证通过")
    else:
        print("  ❌ 部分三角不等式验证失败")
    
    print("\n三角不等式验证完成")


def check_latex_compatibility():
    """
    检测可能导致LaTeX编译错误的字符
    """
    print("\n开始检测LaTeX编译错误风险...")
    
    # 检查当前目录下的Python文件中的潜在问题
    import os
    
    problematic_files = []
    current_dir = '.'
    
    for file in os.listdir(current_dir):
        if file.endswith('.py'):
            filepath = os.path.join(current_dir, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查可能导致LaTeX错误的中文字符
                problematic_chars = ['乘', '除', '加', '减', '等', '°']  # 度号也需要特殊处理
                
                found_chars = []
                for char in problematic_chars:
                    if char in content:
                        count = content.count(char)
                        found_chars.append((char, count))
                
                if found_chars:
                    problematic_files.append((filepath, found_chars))
                    
            except IOError as e:
                print(f"无法读取文件 {filepath}: {e}")
    
    if problematic_files:
        print("发现潜在的LaTeX错误字符:")
        for filepath, chars in problematic_files:
            print(f"  文件: {filepath}")
            for char, count in chars:
                print(f"    字符 '{char}' 出现 {count} 次")
        
        print("\n修复建议:")
        print("  - 将'°'替换为'^\\circ'，如：MathTex(r'90^\\circ')")
        print("  - 中文字符使用Text()代替MathTex()")
    else:
        print("✓ 未发现明显的LaTeX编译错误风险")
    
    print("\nLaTeX检查完成")


def verify_boundaries():
    """
    验证元素是否在安全边界内
    """
    print("\n开始验证元素边界...")
    
    # 定义TikTok竖屏的安全边界
    x_min, x_max = -4.0, 4.0
    y_min, y_max = -7.0, 7.0  # 给顶部和底部一些安全边距
    
    # 测试一些典型的坐标点
    test_points = [
        # 标题区域 (应该在安全区域内)
        np.array([0, 6.5, 0]),  # 标题位置，应该安全
        np.array([0, 7, 0]),    # 顶部，OK
        # 主内容区域
        np.array([0, 0, 0]),    # 中心，应该安全
        np.array([-3, -2, 0]),  # 应该安全
        np.array([3, 2, 0]),    # 应该安全
        # 边界测试
        np.array([5, 0, 0]),    # x超出边界
        np.array([0, 8, 0]),    # y超出边界
        np.array([-5, -8, 0]),  # xy都超出边界
    ]
    
    boundary_issues = []
    
    for i, point in enumerate(test_points):
        x, y, _ = point
        
        issues = []
        if x < x_min or x > x_max:
            issues.append(f"x坐标超出范围 [{x_min}, {x_max}]: {x}")
        if y < y_min or y > y_max:
            issues.append(f"y坐标超出范围 [{y_min}, {y_max}]: {y}")
        
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
    print("="*60)
    print("含绝对值不等式 - 几何验证脚本")
    print("="*60)
    
    verify_absolute_value_definitions()
    verify_basic_inequalities()
    verify_shifted_inequalities()
    verify_triangle_inequality()
    check_latex_compatibility()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()