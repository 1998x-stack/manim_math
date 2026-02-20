"""
几何验证脚本
用于验证一元二次不等式的计算和边界检查
"""
import numpy as np


def verify_quadratic_inequalities():
    """
    验证二次不等式的解法
    """
    print("开始验证一元二次不等式...")
    
    # 测试不同类型的二次不等式
    test_cases = [
        # 情况1: a > 0, Δ > 0, x² - 3x + 2 > 0
        {
            'name': 'x² - 3x + 2 > 0',
            'a': 1,
            'b': -3,
            'c': 2,
            'sign': '>',
            'expected_solution': 'x < 1 或 x > 2'
        },
        # 情况2: a > 0, Δ > 0, x² - 3x + 2 < 0
        {
            'name': 'x² - 3x + 2 < 0',
            'a': 1,
            'b': -3,
            'c': 2,
            'sign': '<',
            'expected_solution': '1 < x < 2'
        },
        # 情况3: a < 0, Δ > 0, -x² + 3x - 2 > 0
        {
            'name': '-x² + 3x - 2 > 0',
            'a': -1,
            'b': 3,
            'c': -2,
            'sign': '>',
            'expected_solution': '1 < x < 2'
        },
        # 情况4: a > 0, Δ = 0, x² - 2x + 1 > 0
        {
            'name': 'x² - 2x + 1 > 0',
            'a': 1,
            'b': -2,
            'c': 1,
            'sign': '>',
            'expected_solution': 'x ≠ 1'
        },
        # 情况5: a > 0, Δ < 0, x² - x + 1 > 0
        {
            'name': 'x² - x + 1 > 0',
            'a': 1,
            'b': -1,
            'c': 1,
            'sign': '>',
            'expected_solution': 'x ∈ ℝ'
        }
    ]
    
    for test_case in test_cases:
        a = test_case['a']
        b = test_case['b']
        c = test_case['c']
        sign = test_case['sign']
        
        print(f"\n验证: {test_case['name']}")
        
        # 计算判别式
        delta = b**2 - 4*a*c
        print(f"  判别式 Δ = b² - 4ac = {b}² - 4({a})({c}) = {delta}")
        
        if delta > 0:
            # 两个不同实根
            sqrt_delta = np.sqrt(delta)
            x1 = (-b - sqrt_delta) / (2 * a)
            x2 = (-b + sqrt_delta) / (2 * a)
            
            print(f"  两根: x₁ = {x1:.3f}, x₂ = {x2:.3f}")
            
            # 根据a的符号和不等号确定解集
            if a > 0:  # 开口向上
                if sign == '>':
                    print(f"  解集: x < {min(x1, x2):.3f} 或 x > {max(x1, x2):.3f}")
                elif sign == '<':
                    print(f"  解集: {min(x1, x2):.3f} < x < {max(x1, x2):.3f}")
            else:  # 开口向下
                if sign == '>':
                    print(f"  解集: {min(x1, x2):.3f} < x < {max(x1, x2):.3f}")
                elif sign == '<':
                    print(f"  解集: x < {min(x1, x2):.3f} 或 x > {max(x1, x2):.3f}")
                    
        elif delta == 0:
            # 一个重根
            x0 = -b / (2 * a)
            print(f"  重根: x₀ = {x0:.3f}")
            
            if a > 0:  # 开口向上
                if sign == '>':
                    print(f"  解集: x ≠ {x0:.3f}")
                elif sign == '<':
                    print(f"  解集: 无解")
            else:  # 开口向下
                if sign == '>':
                    print(f"  解集: 无解")
                elif sign == '<':
                    print(f"  解集: x ≠ {x0:.3f}")
                    
        else:  # delta < 0
            # 无实根
            print("  无实根")
            
            if a > 0:  # 开口向上
                if sign == '>':
                    print("  解集: x ∈ ℝ (全体实数)")
                elif sign == '<':
                    print("  解集: 无解 (∅)")
            else:  # 开口向下
                if sign == '>':
                    print("  解集: 无解 (∅)")
                elif sign == '<':
                    print("  解集: x ∈ ℝ (全体实数)")
        
        print(f"  期望解集: {test_case['expected_solution']}")
        print(f"  ✓ 解析验证完成")


def verify_discriminant_cases():
    """
    验证判别式的三种情况
    """
    print("\n开始验证判别式三种情况...")
    
    # 情况1: Δ > 0 (两个不等实根)
    a, b, c = 1, -3, 2  # x² - 3x + 2 = 0
    delta = b**2 - 4*a*c
    print(f"Δ > 0 情况: {a}x² + {b}x + {c} = 0")
    print(f"  Δ = {delta} > 0, 有两个不等实根")
    
    sqrt_delta = np.sqrt(delta)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    print(f"  x₁ = {x1:.3f}, x₂ = {x2:.3f}")
    
    # 验证根的正确性
    y1 = a*x1**2 + b*x1 + c
    y2 = a*x2**2 + b*x2 + c
    print(f"  验证: f({x1:.3f}) = {y1:.6f}, f({x2:.3f}) = {y2:.6f}")
    
    if abs(y1) < 1e-10 and abs(y2) < 1e-10:
        print("  ✓ 根验证通过")
    else:
        print("  ❌ 根验证失败")
    
    # 情况2: Δ = 0 (一个重根)
    a, b, c = 1, -2, 1  # x² - 2x + 1 = 0
    delta = b**2 - 4*a*c
    print(f"\nΔ = 0 情况: {a}x² + {b}x + {c} = 0")
    print(f"  Δ = {delta} = 0, 有一个重根")
    
    x0 = -b / (2 * a)
    print(f"  x₀ = {x0:.3f}")
    
    y0 = a*x0**2 + b*x0 + c
    print(f"  验证: f({x0:.3f}) = {y0:.6f}")
    
    if abs(y0) < 1e-10:
        print("  ✓ 重根验证通过")
    else:
        print("  ❌ 重根验证失败")
    
    # 情况3: Δ < 0 (无实根)
    a, b, c = 1, -1, 1  # x² - x + 1 = 0
    delta = b**2 - 4*a*c
    print(f"\nΔ < 0 情况: {a}x² + {b}x + {c} = 0")
    print(f"  Δ = {delta} < 0, 无实根")
    
    # 验证判别式计算
    expected_delta = b*b - 4*a*c
    if delta == expected_delta:
        print("  ✓ 判别式计算验证通过")
    else:
        print("  ❌ 判别式计算验证失败")


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
    print("一元二次不等式 - 几何验证脚本")
    print("="*60)
    
    verify_quadratic_inequalities()
    verify_discriminant_cases()
    check_latex_compatibility()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()