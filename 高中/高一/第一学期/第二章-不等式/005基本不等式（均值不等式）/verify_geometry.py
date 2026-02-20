"""
几何验证脚本
用于验证基本不等式（均值不等式）的计算和边界检查
"""
import numpy as np


def verify_basic_inequality():
    """
    验证基本不等式 (a+b)/2 ≥ √(ab) (a,b > 0)
    """
    print("开始验证基本不等式...")
    
    # 测试不同的数值情况
    test_cases = [
        # 相等时的情况
        {
            'name': '相等测试 a=b=1',
            'a': 1,
            'b': 1,
            'expected_arithmetic': 1,
            'expected_geometric': 1
        },
        {
            'name': '相等测试 a=b=4',
            'a': 4,
            'b': 4,
            'expected_arithmetic': 4,
            'expected_geometric': 4
        },
        # 不相等时的情况
        {
            'name': '不等测试 a=1, b=4',
            'a': 1,
            'b': 4,
            'expected_arithmetic': 2.5,
            'expected_geometric': 2
        },
        {
            'name': '不等测试 a=2, b=8',
            'a': 2,
            'b': 8,
            'expected_arithmetic': 5,
            'expected_geometric': 4
        },
        # 小数测试
        {
            'name': '小数测试 a=0.5, b=2',
            'a': 0.5,
            'b': 2,
            'expected_arithmetic': 1.25,
            'expected_geometric': 1
        }
    ]
    
    for test_case in test_cases:
        a = test_case['a']
        b = test_case['b']
        expected_arithmetic = test_case['expected_arithmetic']
        expected_geometric = test_case['expected_geometric']
        
        # 计算算术平均数
        arithmetic_mean = (a + b) / 2
        # 计算几何平均数
        geometric_mean = np.sqrt(a * b)
        
        print(f"{test_case['name']}:")
        print(f"  算术平均数: (a+b)/2 = ({a}+{b})/2 = {arithmetic_mean}, 期望值 {expected_arithmetic}")
        print(f"  几何平均数: √(ab) = √({a}*{b}) = √{a*b} = {geometric_mean}, 期望值 {expected_geometric}")
        
        # 检查是否在合理范围内
        if abs(arithmetic_mean - expected_arithmetic) > 1e-10:
            print(f"  ❌ 算术平均数计算错误!")
        else:
            print(f"  ✓ 算术平均数验证通过")
        
        if abs(geometric_mean - expected_geometric) > 1e-10:
            print(f"  ❌ 几何平均数计算错误!")
        else:
            print(f"  ✓ 几何平均数验证通过")
        
        # 检查基本不等式是否成立
        if arithmetic_mean >= geometric_mean:
            print(f"  ✓ 基本不等式成立: {arithmetic_mean} ≥ {geometric_mean}")
        else:
            print(f"  ❌ 基本不等式不成立: {arithmetic_mean} < {geometric_mean}")
        
        # 当a=b时，算术平均数应该等于几何平均数
        if a == b:
            if abs(arithmetic_mean - geometric_mean) < 1e-10:
                print(f"  ✓ 等号成立条件验证通过: a=b 时算术平均数=几何平均数")
            else:
                print(f"  ❌ 等号成立条件验证失败: a=b 时算术平均数≠几何平均数")
        
        print()


def verify_extended_formulas():
    """
    验证扩展的不等式变体
    """
    print("开始验证扩展不等式变体...")
    
    # 测试 a + b ≥ 2√(ab)
    a, b = 3, 12
    left_side = a + b
    right_side = 2 * np.sqrt(a * b)
    
    print(f"验证 a + b ≥ 2√(ab) (a={a}, b={b}):")
    print(f"  左边: a + b = {a} + {b} = {left_side}")
    print(f"  右边: 2√(ab) = 2√({a*b}) = 2*{np.sqrt(a*b):.6f} = {right_side:.6f}")
    
    if left_side >= right_side:
        print(f"  ✓ 不等式成立: {left_side} ≥ {right_side:.6f}")
    else:
        print(f"  ❌ 不等式不成立: {left_side} < {right_side:.6f}")
    
    print()
    
    # 测试 ab ≤ (a+b)²/4
    a, b = 2, 8
    left_side = a * b
    right_side = (a + b)**2 / 4
    
    print(f"验证 ab ≤ (a+b)²/4 (a={a}, b={b}):")
    print(f"  左边: ab = {a} * {b} = {left_side}")
    print(f"  右边: (a+b)²/4 = ({a}+{b})²/4 = {(a+b)**2}/4 = {right_side}")
    
    if left_side <= right_side:
        print(f"  ✓ 不等式成立: {left_side} ≤ {right_side}")
    else:
        print(f"  ❌ 不等式不成立: {left_side} > {right_side}")
    
    print()
    
    # 测试 a² + b² ≥ 2ab
    a, b = 5, 3
    left_side = a**2 + b**2
    right_side = 2 * a * b
    
    print(f"验证 a² + b² ≥ 2ab (a={a}, b={b}):")
    print(f"  左边: a² + b² = {a}² + {b}² = {a**2} + {b**2} = {left_side}")
    print(f"  右边: 2ab = 2*{a}*{b} = {right_side}")
    
    if left_side >= right_side:
        print(f"  ✓ 不等式成立: {left_side} ≥ {right_side}")
    else:
        print(f"  ❌ 不等式不成立: {left_side} < {right_side}")
    
    print()


def verify_means_chain():
    """
    验证各种平均数的链式关系
    H ≤ G ≤ A ≤ Q
    调和平均数 ≤ 几何平均数 ≤ 算术平均数 ≤ 平方平均数
    """
    print("开始验证平均数链式关系 H ≤ G ≤ A ≤ Q...")
    
    # 测试值
    a, b = 2, 8
    
    # 计算各种平均数
    harmonic_mean = 2 / (1/a + 1/b)  # 调和平均数
    geometric_mean = np.sqrt(a * b)    # 几何平均数
    arithmetic_mean = (a + b) / 2      # 算术平均数
    quadratic_mean = np.sqrt((a**2 + b**2) / 2)  # 平方平均数
    
    print(f"对于 a={a}, b={b}:")
    print(f"  调和平均数 H = 2/(1/a + 1/b) = {harmonic_mean:.6f}")
    print(f"  几何平均数 G = √(ab) = {geometric_mean:.6f}")
    print(f"  算术平均数 A = (a+b)/2 = {arithmetic_mean:.6f}")
    print(f"  平方平均数 Q = √((a²+b²)/2) = {quadratic_mean:.6f}")
    
    # 验证链式关系
    chain_valid = (
        harmonic_mean <= geometric_mean and
        geometric_mean <= arithmetic_mean and
        arithmetic_mean <= quadratic_mean
    )
    
    if chain_valid:
        print(f"  ✓ 链式关系成立: H ≤ G ≤ A ≤ Q")
        print(f"     {harmonic_mean:.6f} ≤ {geometric_mean:.6f} ≤ {arithmetic_mean:.6f} ≤ {quadratic_mean:.6f}")
    else:
        print(f"  ❌ 链式关系不成立")
        print(f"     H={harmonic_mean:.6f}, G={geometric_mean:.6f}, A={arithmetic_mean:.6f}, Q={quadratic_mean:.6f}")
    
    print()


def check_latex_compatibility():
    """
    检测可能导致LaTeX编译错误的字符
    """
    print("开始检测LaTeX编译错误风险...")
    
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
    print("开始验证元素边界...")
    
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
    print("基本不等式（均值不等式） - 几何验证脚本")
    print("="*60)
    
    verify_basic_inequality()
    verify_extended_formulas()
    verify_means_chain()
    check_latex_compatibility()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()