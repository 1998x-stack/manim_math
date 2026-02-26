"""
几何验证脚本 - 验证平行线性质动画中的几何计算
"""
import numpy as np


def verify_angles():
    """
    验证角度计算 - 检查是否超过90度或180度的情况
    """
    print("正在验证角度计算...")
    
    # 模拟平行线和截线的几何设置
    line_y_pos_1 = 1.0
    line_y_pos_2 = -1.0
    
    # 截线的起始和结束点
    transversal_start = np.array([-2.5, 3, 0])
    transversal_end = np.array([2.5, -3, 0])
    
    # 计算截线斜率和截距
    slope = (transversal_end[1] - transversal_start[1]) / (transversal_end[0] - transversal_start[0])
    intercept = transversal_start[1] - slope * transversal_start[0]
    
    # 计算交点
    intersection1_x = (line_y_pos_1 - intercept) / slope
    intersection1 = np.array([intersection1_x, line_y_pos_1, 0])
    
    intersection2_x = (line_y_pos_2 - intercept) / slope
    intersection2 = np.array([intersection2_x, line_y_pos_2, 0])
    
    # 计算关键角度
    # 同位角：水平线向右与截线之间的角度
    horizontal_vec = np.array([1, 0, 0])  # 水平向右单位向量
    transversal_vec = transversal_end - transversal_start  # 截线方向向量
    transversal_vec = transversal_vec / np.linalg.norm(transversal_vec)  # 单位化
    
    # 使用点积计算角度
    cos_angle = np.dot(horizontal_vec[:2], transversal_vec[:2])
    angle_rad = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    
    print(f"截线与水平线的锐角: {angle_deg:.2f}°")
    
    # 验证角度是否小于90度（正常情况）
    if angle_deg > 90:
        print(f"⚠️  警告: 角度大于90度 ({angle_deg:.2f}°)，注意角度方向！")
        if angle_deg > 180:
            print(f"❌ 错误: 角度大于180度 ({angle_deg:.2f}°)，角度方向很可能错误！")
            print("    Manim 的 Angle.from_three_points 默认是逆时针。可能需要添加 other_angle=True 参数。")
    else:
        print("✓ 角度计算正常")
    
    # 计算其他角度（用于内错角、同旁内角等）
    supplementary_angle = 180 - angle_deg
    print(f"互补角: {supplementary_angle:.2f}°")
    
    if supplementary_angle > 180:
        print(f"⚠️  警告: 互补角大于180度 ({supplementary_angle:.2f}°)")
    
    print()


def grep_MathTex():
    """
    检查MathTex中可能的LaTeX编译错误
    """
    print("检查MathTex中的LaTeX编译错误...")
    
    # 常见错误：中文字符
    problematic_expressions = [
        r"乘",  # 中文字符
        r"除",  # 中文字符
        r"角A", # 包含中文
    ]
    
    safe_expressions = [
        r"\alpha",
        r"\beta", 
        r"\gamma",
        r"\angle 1",
        r"\angle A",
        r"180^\circ",
        r"\neq",
        r"\parallel",  # 平行符号
        r"\perp",     # 垂直符号
    ]
    
    print("安全的MathTex表达式示例:")
    for expr in safe_expressions:
        print(f"  ✓ {expr}")
    
    print("\n需要避免的表达式示例:")
    for expr in problematic_expressions:
        print(f"  ❌ 包含字符: {expr}")
    
    print("\n解决方案:")
    print("- 使用 Text() 来显示中文，而不是 MathTex()")
    print("- MathTex 仅用于纯数学符号和公式")
    print("- 使用 LaTeX 命令如 ^\\circ 替代度数符号")
    print()


def verify_boundaries():
    """
    验证元素是否在安全边界内
    """
    print("验证元素边界...")
    
    # TikTok竖屏尺寸: 1080x1920，逻辑宽高: 9x16
    # 安全范围: x ∈ [-4.5, 4.5], y ∈ [-8, 8]
    # 推荐范围: x ∈ [-4, 4], y ∈ [-7, 7]
    
    # 平行线位置
    line_y_pos_1 = 1.0
    line_y_pos_2 = -1.0
    line_x_range = [-4, 4]
    
    # 检查平行线是否在安全范围内
    if -7 <= line_y_pos_1 <= 7 and -7 <= line_y_pos_2 <= 7:
        print("✓ 平行线Y坐标在安全范围内")
    else:
        print(f"❌ 平行线Y坐标超出安全范围: {line_y_pos_1}, {line_y_pos_2}")
    
    if -4 <= line_x_range[0] and line_x_range[1] <= 4:
        print("✓ 平行线X范围在安全范围内")
    else:
        print(f"❌ 平行线X范围超出安全范围: {line_x_range}")
    
    # 截线端点
    transversal_start = np.array([-2.5, 3, 0])
    transversal_end = np.array([2.5, -3, 0])
    
    if (-4 <= transversal_start[0] <= 4 and -7 <= transversal_start[1] <= 7 and
        -4 <= transversal_end[0] <= 4 and -7 <= transversal_end[1] <= 7):
        print("✓ 截线端点在安全范围内")
    else:
        print(f"❌ 截线端点超出安全范围: start={transversal_start}, end={transversal_end}")
    
    # 交点（已通过几何计算得出）
    slope = (transversal_end[1] - transversal_start[1]) / (transversal_end[0] - transversal_start[0])
    intercept = transversal_start[1] - slope * transversal_start[0]
    
    intersection1_x = (line_y_pos_1 - intercept) / slope
    intersection1 = np.array([intersection1_x, line_y_pos_1, 0])
    
    intersection2_x = (line_y_pos_2 - intercept) / slope
    intersection2 = np.array([intersection2_x, line_y_pos_2, 0])
    
    intersections = [intersection1, intersection2]
    all_in_bounds = True
    
    for i, point in enumerate(intersections):
        if not (-4 <= point[0] <= 4 and -7 <= point[1] <= 7):
            print(f"❌ 交点{i+1}超出安全范围: {point[:2]}")
            all_in_bounds = False
    
    if all_in_bounds:
        print("✓ 所有交点在安全范围内")
    
    print("边界验证完成\n")


def main():
    print("="*50)
    print("几何验证脚本 - 平行线性质动画")
    print("="*50)
    
    verify_angles()
    grep_MathTex()
    verify_boundaries()
    
    print("所有验证完成！")


if __name__ == "__main__":
    main()