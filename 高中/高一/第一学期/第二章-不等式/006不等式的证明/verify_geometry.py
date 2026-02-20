"""
几何验证脚本
用于验证不等式证明的计算和边界检查
"""
import numpy as np


def verify_comparison_method():
    """
    验证比较法 (a-b ≥ 0 ⟺ a ≥ b)
    """
    print("开始验证比较法...")
    
    # 测试不同的数值情况
    test_cases = [
        # a > b 情况
        {
            'name': 'a > b 测试',
            'a': 5,
            'b': 3,
            'expected_comparison': True
        },
        # a = b 情况
        {
            'name': 'a = b 测试',
            'a': 4,
            'b': 4,
            'expected_comparison': True
        },
        # a < b 情况
        {
            'name': 'a < b 测试',
            'a': 2,
            'b': 6,
            'expected_comparison': False
        },
        # 负数情况
        {
            'name': '负数测试',
            'a': -1,
            'b': -3,
            'expected_comparison': True  # -1 > -3
        }
    ]
    
    for test_case in test_cases:
        a = test_case['a']
        b = test_case['b']
        expected = test_case['expected_comparison']
        
        # 计算 a - b
        diff = a - b
        # 验证 a ≥ b ⟺ a - b ≥ 0
        actual_comparison = a >= b
        actual_diff = diff >= 0
        
        print(f"{test_case['name']}: a={a}, b={b}")
        print(f"  a - b = {diff}, a - b ≥ 0: {actual_diff}")
        print(f"  a ≥ b: {actual_comparison}, 期望值: {expected}")
        
        if actual_comparison == actual_diff:
            print(f"  ✓ 比较法验证通过: a ≥ b ⟺ a - b ≥ 0")
        else:
            print(f"  ❌ 比较法验证失败!")
    
    print("\n比较法验证完成")


def verify_basic_inequalities():
    """
    验证基本不等式 a² + b² ≥ 2ab
    """
    print("\n开始验证基本不等式 a² + b² ≥ 2ab...")
    
    # 测试不同的数值情况
    test_cases = [
        # 正数情况
        {
            'name': '正数测试',
            'a': 3,
            'b': 2,
            'expected': True
        },
        # 相等时的情况
        {
            'name': '相等测试',
            'a': 4,
            'b': 4,
            'expected': True
        },
        # 负数情况
        {
            'name': '负数测试',
            'a': -2,
            'b': -3,
            'expected': True
        },
        # 混合正负
        {
            'name': '混合测试',
            'a': 3,
            'b': -2,
            'expected': True
        }
    ]
    
    for test_case in test_cases:
        a = test_case['a']
        b = test_case['b']
        
        left_side = a**2 + b**2
        right_side = 2*a*b
        satisfies = left_side >= right_side
        
        print(f"{test_case['name']}: a={a}, b={b}")
        print(f"  a² + b² = {a}² + {b}² = {left_side}")
        print(f"  2ab = 2·{a}·{b} = {right_side}")
        print(f"  {left_side} ≥ {right_side}: {satisfies}")
        
        # 验证 (a-b)² ≥ 0
        diff_squared = (a - b)**2
        print(f"  (a-b)² = ({a}-{b})² = {diff_squared} ≥ 0: {diff_squared >= 0}")
        
        if satisfies and diff_squared >= 0:
            print(f"  ✓ 基本不等式验证通过")
        else:
            print(f"  ❌ 基本不等式验证失败")
    
    print("\n基本不等式验证完成")


def verify_cauchy_inequality():
    """
    验证柯西不等式 (a² + b²)(c² + d²) ≥ (ac + bd)²
    """
    print("\n开始验证柯西不等式 (a² + b²)(c² + d²) ≥ (ac + bd)²...")
    
    # 测试不同的数值情况
    test_cases = [
        # 简单情况
        {
            'name': '简单测试',
            'a': 1, 'b': 2, 'c': 3, 'd': 4
        },
        # 相等时的情况 (当 ad = bc 时等号成立)
        {
            'name': '等号成立测试',
            'a': 2, 'b': 1, 'c': 4, 'd': 2  # ad = 4, bc = 4, 满足 ad = bc
        },
        # 负数情况
        {
            'name': '负数测试',
            'a': -1, 'b': 2, 'c': -3, 'd': 4
        }
    ]
    
    for test_case in test_cases:
        a, b, c, d = test_case['a'], test_case['b'], test_case['c'], test_case['d']
        
        left_side = (a**2 + b**2) * (c**2 + d**2)
        right_side = (a*c + b*d)**2
        satisfies = left_side >= right_side
        
        print(f"{test_case['name']}: a={a}, b={b}, c={c}, d={d}")
        print(f"  (a² + b²)(c² + d²) = ({a}² + {b}²)({c}² + {d}²) = {left_side}")
        print(f"  (ac + bd)² = ({a*c} + {b*d})² = {right_side}")
        print(f"  {left_side} ≥ {right_side}: {satisfies}")
        
        # 验证等号成立条件
        ad_bc_equal = a*d == b*c
        equal_case = left_side == right_side
        if ad_bc_equal and equal_case:
            print(f"  ✓ 等号成立条件验证通过: ad = bc ({a*d} = {b*c})")
        elif not ad_bc_equal and satisfies:
            print(f"  ✓ 不等号成立，且满足柯西不等式")
        elif ad_bc_equal and not equal_case:
            print(f"  ❌ 等号应成立但未成立")
        else:
            print(f"  ❌ 柯西不等式验证失败")
    
    print("\n柯西不等式验证完成")


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
    print("不等式的证明 - 几何验证脚本")
    print("="*60)
    
    verify_comparison_method()
    verify_basic_inequalities()
    verify_cauchy_inequality()
    check_latex_compatibility()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()