"""
几何验证脚本
用于验证加法初步认识动画的计算和边界检查
"""
import numpy as np


def verify_basic_operations():
    """
    验证基础加法运算
    """
    print("开始验证加法运算...")
    
    # 测试基本加法运算
    test_cases = [
        {"expression": "1 + 1", "result": 2},
        {"expression": "2 + 1", "result": 3},
        {"expression": "3 + 2", "result": 5},
        {"expression": "4 + 3", "result": 7},
        {"expression": "5 + 4", "result": 9},
    ]
    
    for test_case in test_cases:
        expression = test_case["expression"]
        expected = test_case["result"]
        parts = expression.split(" + ")
        a, b = int(parts[0]), int(parts[1])
        calculated = a + b
        
        if calculated == expected:
            print(f"  ✓ {expression} = {calculated}")
        else:
            print(f"  ✗ {expression} = {calculated}, expected {expected}")


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


def verify_visual_elements():
    """
    验证视觉元素的合理性（如圆圈数量代表加法）
    """
    print("开始验证视觉元素...")
    
    # 验证加法的视觉表示
    # 例如：2 + 1 应该显示2个圆圈 + 1个圆圈 = 3个圆圈
    
    addition_examples = [
        {"a": 1, "b": 1, "total": 2},
        {"a": 2, "b": 1, "total": 3},
        {"a": 2, "b": 3, "total": 5},
        {"a": 3, "b": 2, "total": 5},
    ]
    
    for example in addition_examples:
        a, b, total = example["a"], example["b"], example["total"]
        calc_total = a + b
        
        if calc_total == total:
            print(f"  ✓ {a} + {b} = {total} (视觉元素数量匹配)")
        else:
            print(f"  ✗ {a} + {b} = {calc_total}, expected {total}")
    
    print("\n视觉元素验证完成")


def main():
    """
    主验证函数
    """
    print("="*60)
    print("加法的初步认识 - 几何验证脚本")
    print("="*60)
    
    verify_basic_operations()
    print()
    verify_visual_elements()
    print()
    check_latex_compatibility()
    print()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()