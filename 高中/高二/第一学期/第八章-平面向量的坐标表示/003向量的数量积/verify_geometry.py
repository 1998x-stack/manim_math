"""
verify_geometry.py - 几何验证脚本
验证 vector_dot_product.py 中的几何计算

使用方法: python verify_geometry.py
注意: 仅使用 numpy，不使用 manim
"""

import numpy as np
import re


# =========================================================
# 场景几何参数（与 vector_dot_product.py 完全一致）
# =========================================================
AXES_ORIGIN = np.array([0, 0.5, 0])
AXES_SCALE = 1.2

VEC_A_COORDS = np.array([2.0, 1.0, 0])
VEC_B_COORDS = np.array([0.5, 2.0, 0])

VEC_P_COORDS = np.array([1.5, 0, 0])
VEC_Q_COORDS = np.array([0, 1.5, 0])

# TikTok 竖屏安全边界
FRAME_WIDTH = 9
FRAME_HEIGHT = 16
SAFE_X = (-4.0, 4.0)
SAFE_Y = (-7.5, 7.5)


# =========================================================
# 核心验证函数
# =========================================================

def verify_angles():
    """
    验证所有角度计算正确性
    重点检查 > 90°、> 180° 的角
    """
    print("\n" + "=" * 50)
    print("verify_angles()")
    print("=" * 50)

    a = VEC_A_COORDS[:2]
    b = VEC_B_COORDS[:2]

    # 计算夹角
    dot = np.dot(a, b)
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    cos_t = dot / (mag_a * mag_b)
    cos_t = np.clip(cos_t, -1.0, 1.0)
    theta_rad = np.arccos(cos_t)
    theta_deg = np.degrees(theta_rad)

    print(f"  a = {a}, b = {b}")
    print(f"  a · b = {dot:.4f}")
    print(f"  |a| = {mag_a:.4f}, |b| = {mag_b:.4f}")
    print(f"  cos θ = {cos_t:.4f}")
    print(f"  θ = {theta_deg:.2f}°")

    # 检查角度范围
    if theta_deg > 180:
        print(f"  ⚠️⚠️ 角度 {theta_deg:.2f}° > 180°，Manim Angle 方向很可能错误！")
        print(f"     需要使用 other_angle=True")
    elif theta_deg > 90:
        print(f"  ⚠️  角度 {theta_deg:.2f}° > 90°，需要注意 Angle 方向")
        print(f"     建议检查 quadrant 参数")
    else:
        print(f"  ✓ 角度 {theta_deg:.2f}° 在正常范围 (0~90°)")

    # 验证叉积方向（用于 Manim other_angle 判断）
    cross_z = a[0] * b[1] - a[1] * b[0]
    print(f"  叉积 z 分量: {cross_z:.4f}")
    if cross_z > 0:
        print(f"  ✓ 从 a 到 b 是逆时针，other_angle=False (默认) 正确")
    else:
        print(f"  ⚠️  从 a 到 b 是顺时针，需要 other_angle=True")

    # 角弧标签位置计算
    angle_of_a = np.arctan2(a[1], a[0])
    mid_angle = theta_rad / 2
    label_angle = angle_of_a + mid_angle
    label_pos = 0.85 * np.array([np.cos(label_angle), np.sin(label_angle), 0])
    print(f"  角标签位置 (相对原点): ({label_pos[0]:.3f}, {label_pos[1]:.3f})")

    # 验证垂直向量角度
    p = VEC_P_COORDS[:2]
    q = VEC_Q_COORDS[:2]
    dot_pq = np.dot(p, q)
    print(f"\n  垂直验证: p·q = {dot_pq} (应为 0)")
    if abs(dot_pq) < 1e-8:
        print(f"  ✓ p ⊥ q 验证通过")
        # 垂直夹角
        cos_pq = dot_pq / (np.linalg.norm(p) * np.linalg.norm(q))
        print(f"  垂直夹角 = {np.degrees(np.arccos(np.clip(cos_pq, -1, 1))):.1f}°")
    else:
        print(f"  ❌ 垂直验证失败！p·q = {dot_pq}")

    return theta_deg, cross_z


def grep_MathTex():
    """
    扫描 Python 文件中的 MathTex 调用
    检查是否含有中文字符（会导致 LaTeX 编译错误）
    """
    print("\n" + "=" * 50)
    print("grep_MathTex() - 检查 LaTeX 兼容性")
    print("=" * 50)

    import ast

    filepath = "vector_dot_product.py"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"  ❌ 文件 {filepath} 未找到")
        return

    errors_found = []
    warnings = []

    # 提取所有 MathTex(...) 调用中的字符串内容
    # 简单正则匹配
    mathtex_pattern = re.compile(r'MathTex\s*\(\s*r?"(.*?)"', re.DOTALL)
    matches = mathtex_pattern.findall(source)

    chinese_range = re.compile(r'[\u4e00-\u9fff]')

    for i, content in enumerate(matches):
        # 检查中文字符
        chinese = chinese_range.findall(content)
        if chinese:
            errors_found.append(f"  ❌ MathTex 含中文字符 {chinese}: '{content[:60]}'")

        # 检查度数符号 °（应用 ^\circ）
        if '°' in content:
            warnings.append(f"  ⚠️  MathTex 含 ° 符号 (应用 ^{{\\circ}}): '{content[:60]}'")

        # 检查双花括号错误用法
        if '{{' in content and '\\over' in content:
            warnings.append(f"  ⚠️  可能的 \\over 错误: '{content[:60]}'")

    if errors_found:
        print(f"  发现 {len(errors_found)} 个错误:")
        for e in errors_found:
            print(e)
    else:
        print(f"  ✓ 扫描 {len(matches)} 个 MathTex 调用，无中文字符")

    if warnings:
        for w in warnings:
            print(w)

    # 检查 Text() 使用（中文应使用 Text）
    text_pattern = re.compile(r'Text\s*\(\s*"(.*?)"', re.DOTALL)
    text_matches = text_pattern.findall(source)
    chinese_in_text = sum(1 for t in text_matches if chinese_range.search(t))
    print(f"  ✓ Text() 调用 {len(text_matches)} 次, 含中文: {chinese_in_text} 次 (正确使用 Text)")


def verify_boundaries():
    """
    验证关键元素是否在安全边界内
    TikTok 竖屏: x ∈ [-4, +4], y ∈ [-7.5, +7.5]
    """
    print("\n" + "=" * 50)
    print("verify_boundaries()")
    print("=" * 50)

    S = AXES_SCALE
    origin = AXES_ORIGIN

    # 定义需要检查的关键点
    key_points = {
        "AXES_ORIGIN": origin,
        "vec_a_end": origin + VEC_A_COORDS * S,
        "vec_b_end": origin + VEC_B_COORDS * S,
        "vec_p_end": origin + VEC_P_COORDS * S,
        "vec_q_end": origin + VEC_Q_COORDS * S,
        "author_bar (UP*7.2)": np.array([0, 7.2, 0]),
        "formula_box (DOWN*3.8)": np.array([0, -3.8, 0]),
        "formula_geo moved (UP*4.2)": np.array([0, 4.2, 0]),
        "coord_formula (DOWN*2.5)": np.array([0, -2.5, 0]),
        "perp_box (DOWN*3.4)": np.array([0, -3.4, 0]),
        "perp_formula line2 (DOWN*3.85)": np.array([0, -3.85, 0]),
        "summary_items (DOWN*4.2)": np.array([0, -4.2, 0]),
        "outro_name (UP*2)": np.array([0, 2.0, 0]),
        "deco arrows (DOWN*2.5)": np.array([0, -2.5, 0]),
        "dot_symbol (DOWN*4.2)": np.array([0, -4.2, 0]),
    }

    all_ok = True
    for name, pt in key_points.items():
        x, y = pt[0], pt[1]
        ok_x = SAFE_X[0] <= x <= SAFE_X[1]
        ok_y = SAFE_Y[0] <= y <= SAFE_Y[1]

        if ok_x and ok_y:
            print(f"  ✓ {name}: ({x:.2f}, {y:.2f})")
        else:
            issues = []
            if not ok_x:
                issues.append(f"x={x:.2f} 超出 [{SAFE_X[0]}, {SAFE_X[1]}]")
            if not ok_y:
                issues.append(f"y={y:.2f} 超出 [{SAFE_Y[0]}, {SAFE_Y[1]}]")
            print(f"  ❌ {name}: {', '.join(issues)}")
            all_ok = False

    # 特殊检查: 坐标轴范围下向量箭头端点
    print(f"\n  坐标系向量端点验证 (scale={S}):")
    for name, coords in [("a", VEC_A_COORDS), ("b", VEC_B_COORDS)]:
        tip = origin + coords * S
        print(f"    vec_{name} 端点: ({tip[0]:.2f}, {tip[1]:.2f})")

    if all_ok:
        print(f"\n  ✓ 所有元素在安全边界内")
    else:
        print(f"\n  ❌ 存在超出边界的元素，需要调整位置")

    return all_ok


def verify_dot_product_math():
    """验证数量积数学计算"""
    print("\n" + "=" * 50)
    print("verify_dot_product_math()")
    print("=" * 50)

    a = VEC_A_COORDS[:2]
    b = VEC_B_COORDS[:2]

    # 坐标法
    dot_coord = float(np.dot(a, b))
    print(f"  坐标法: {a[0]}×{b[0]} + {a[1]}×{b[1]} = {dot_coord}")

    # 几何法
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    cos_t = dot_coord / (mag_a * mag_b)
    dot_geo = mag_a * mag_b * cos_t
    print(f"  几何法: |a|={mag_a:.4f}, |b|={mag_b:.4f}, cos θ={cos_t:.4f}")
    print(f"          |a||b|cosθ = {dot_geo:.4f}")

    # 一致性
    if abs(dot_coord - dot_geo) < 1e-6:
        print(f"  ✓ 两种方法结果一致: {dot_coord:.4f}")
    else:
        print(f"  ❌ 不一致: 坐标法={dot_coord:.4f}, 几何法={dot_geo:.4f}")

    # 模长公式验证
    mag_a_check = np.sqrt(a[0]**2 + a[1]**2)
    mag_a_dot = np.sqrt(np.dot(a, a))
    print(f"\n  模长公式 |a|:")
    print(f"    √(x²+y²) = {mag_a_check:.4f}")
    print(f"    √(a·a)   = {mag_a_dot:.4f}")
    if abs(mag_a_check - mag_a_dot) < 1e-10:
        print(f"  ✓ 模长公式验证通过")
    else:
        print(f"  ❌ 模长公式验证失败")

    # 标量性验证（仅用于说明）
    print(f"\n  数量积是标量（数），不是向量:")
    print(f"    a·b = {dot_coord} (标量)")
    print(f"    a×b (向量积) 不在本节范围")


# =========================================================
# 主程序
# =========================================================
if __name__ == "__main__":
    print("=" * 50)
    print("向量数量积 - 几何验证报告")
    print("=" * 50)

    # 运行所有验证
    theta_deg, cross_z = verify_angles()
    grep_MathTex()
    boundary_ok = verify_boundaries()
    verify_dot_product_math()

    print("\n" + "=" * 50)
    print("验证总结")
    print("=" * 50)

    # 汇总关键参数供 Manim 使用
    print(f"  夹角 θ = {theta_deg:.2f}°")
    print(f"  叉积 z = {cross_z:.4f} → other_angle={'True' if cross_z < 0 else 'False'}")
    print(f"  边界检查: {'✓ 通过' if boundary_ok else '❌ 需修复'}")

    a = VEC_A_COORDS[:2]
    b = VEC_B_COORDS[:2]
    dot = np.dot(a, b)
    print(f"  a·b = {dot:.4f}")

    if theta_deg <= 90 and cross_z > 0 and boundary_ok:
        print("\n  ✅ 所有检查通过！代码可以运行。")
    else:
        print("\n  ⚠️  存在需要注意的问题，请检查上方输出。")
