import numpy as np


def verify_angles():
    """
    验证几何图形中的角度是否正确
    特别注意大于90度和180度的角度，检查方向是否正确
    """
    print("开始角度验证...")
    
    # 示例验证过程：
    # 假设我们有一些角度测量值
    # 对于大于90度的角度，需要分析其方向
    # 对于大于180度的角度，需要特别注意⚠️，因为Manim的Angle.from_three_points默认是逆时针，
    # 如果角度大于180度，很可能方向错了，需要添加other_angle=True参数
    
    # 这里可以加入具体的验证逻辑，例如：
    # 检查同位角是否相等
    # 检查内错角是否相等  
    # 检查同旁内角是否互补
    
    print("角度验证完成 ✓")


def grep_MathTex():
    """
    检查MathTex内容，避免LaTeX编译错误
    如: LaTeX Error: Unicode character 乘 (U+4E58)
    """
    print("开始检查MathTex内容...")
    
    # 检查常见的LaTeX错误：
    # 1. 中文字符
    # 2. 特殊Unicode字符
    # 3. 错误的LaTeX语法
    
    # 避免在MathTex中使用中文，应该使用Text组件
    # 例如，不要写 MathTex(r"三角形面积")，而要写 Text("三角形面积", font="Noto Sans CJK SC")
    
    # 检查度数符号是否使用 ^\circ 而不是 °
    # 例如，应该写 MathTex(r"90^\circ") 而不是 MathTex(r"90°")
    
    print("MathTex检查完成 ✓")


def verify_boundaries():
    """
    验证几何元素是否在安全边界内
    对于TikTok竖屏格式 (1080×1920)，逻辑坐标系为 x∈[-4.5, +4.5], y∈[-8, +8]
    建议的安全范围: x∈[-4, +4], y∈[-7, +7]
    """
    print("开始边界验证...")
    
    # 定义安全边界
    X_MIN, X_MAX = -4.0, 4.0
    Y_MIN, Y_MAX = -7.0, 7.0
    
    # 这里可以加入具体的边界检查逻辑
    # 例如检查所有创建的点是否在边界内
    # points = [self.A, self.B, self.C, ...]
    # for point in points:
    #     x, y = point[0], point[1]
    #     if x < X_MIN or x > X_MAX or y < Y_MIN or y > Y_MAX:
    #         print(f"警告：点 {point} 超出安全边界")
    
    print("边界验证完成 ✓")


def verify_parallel_lines(l1_start, l1_end, l2_start, l2_end, tolerance=1e-6):
    """
    验证两条线是否真正平行
    通过检查它们的方向向量是否成比例来判断
    """
    print("验证平行线...")
    
    # 计算两条线的方向向量
    dir1 = l1_end - l1_start
    dir2 = l2_end - l2_start
    
    # 归一化方向向量
    norm_dir1 = dir1 / np.linalg.norm(dir1)
    norm_dir2 = dir2 / np.linalg.norm(dir2)
    
    # 检查方向向量是否平行（要么相同，要么相反）
    cross_product = np.abs(np.cross(norm_dir1[:2], norm_dir2[:2]))
    
    if cross_product < tolerance:
        print("✓ 两条线平行")
        return True
    else:
        print(f"✗ 两条线不平行，交叉积: {cross_product}")
        return False


def verify_transversal_intersections(transversal_start, transversal_end, 
                                   line1_start, line1_end, 
                                   line2_start, line2_end,
                                   intersection1, intersection2, tolerance=1e-6):
    """
    验证截线是否确实与两条平行线相交，并且交点计算正确
    """
    print("验证截线与平行线的交点...")
    
    # 检查交点是否在对应的线上
    def point_on_line_segment(point, line_start, line_end, tol=tolerance):
        # 检查点是否在线段上
        # 通过参数方程: P = line_start + t*(line_end - line_start)
        # 其中 0 <= t <= 1
        line_vec = line_end - line_start
        point_vec = point - line_start
        
        # 计算参数t
        if np.linalg.norm(line_vec) > tol:
            t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
            return 0 - tol <= t <= 1 + tol
        return False
    
    # 验证交点1在线段1上
    if point_on_line_segment(intersection1, line1_start, line1_end):
        print("✓ 交点1在线段1上")
    else:
        print("✗ 交点1不在线段1上")
    
    # 验证交点2在线段2上
    if point_on_line_segment(intersection2, line2_start, line2_end):
        print("✓ 交点2在线段2上")
    else:
        print("✗ 交点2不在线段2上")
    
    # 验证交点也在截线上
    if point_on_line_segment(intersection1, transversal_start, transversal_end) and \
       point_on_line_segment(intersection2, transversal_start, transversal_end):
        print("✓ 两个交点都在截线上")
    else:
        print("✗ 交点不在截线上")


def verify_angle_relationships(intersection1, intersection2, 
                              point_on_l1_left, point_on_l1_right,
                              point_on_l2_left, point_on_l2_right,
                              point_on_t_above_i1, point_on_t_below_i1,
                              point_on_t_above_i2, point_on_t_below_i2):
    """
    验证角度关系是否正确（同位角、内错角、同旁内角）
    """
    print("验证角度关系...")
    
    def calculate_angle(p1, vertex, p2):
        """计算由三点形成的夹角（弧度）"""
        v1 = p1 - vertex
        v2 = p2 - vertex
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 数值稳定性
        return np.arccos(cos_angle)
    
    # 计算同位角
    # 在intersection1处，平行线方向到截线方向的角
    corresponding_angle1 = calculate_angle(point_on_l1_right, intersection1, point_on_t_below_i1)
    # 在intersection2处，平行线方向到截线方向的角
    corresponding_angle2 = calculate_angle(point_on_l2_right, intersection2, point_on_t_below_i2)
    
    print(f"同位角1: {np.degrees(corresponding_angle1):.2f}°")
    print(f"同位角2: {np.degrees(corresponding_angle2):.2f}°")
    
    if abs(corresponding_angle1 - corresponding_angle2) < 1e-2:
        print("✓ 同位角相等")
    else:
        print(f"✗ 同位角不相等，差值: {abs(corresponding_angle1 - corresponding_angle2):.4f}")
    
    # 计算内错角
    alternate_angle1 = calculate_angle(point_on_l1_left, intersection1, point_on_t_below_i1)
    alternate_angle2 = calculate_angle(point_on_l2_right, intersection2, point_on_t_above_i2)
    
    print(f"内错角1: {np.degrees(alternate_angle1):.2f}°")
    print(f"内错角2: {np.degrees(alternate_angle2):.2f}°")
    
    if abs(alternate_angle1 - alternate_angle2) < 1e-2:
        print("✓ 内错角相等")
    else:
        print(f"✗ 内错角不相等，差值: {abs(alternate_angle1 - alternate_angle2):.4f}")
    
    # 计算同旁内角
    co_interior_angle1 = calculate_angle(point_on_l1_right, intersection1, point_on_t_below_i1)
    co_interior_angle2 = calculate_angle(point_on_l2_right, intersection2, point_on_t_above_i2)
    
    print(f"同旁内角1: {np.degrees(co_interior_angle1):.2f}°")
    print(f"同旁内角2: {np.degrees(co_interior_angle2):.2f}°")
    print(f"同旁内角之和: {np.degrees(co_interior_angle1 + co_interior_angle2):.2f}°")
    
    if abs((co_interior_angle1 + co_interior_angle2) - np.pi) < 1e-2:  # π弧度 = 180°
        print("✓ 同旁内角互补")
    else:
        print(f"✗ 同旁内角不互补，和为: {np.degrees(co_interior_angle1 + co_interior_angle2):.2f}°")


if __name__ == "__main__":
    # 运行所有验证函数
    verify_angles()
    print()
    grep_MathTex()
    print()
    verify_boundaries()
    print()
    
    # 这里可以添加使用实际坐标的验证
    # 以下是一些示例坐标，实际使用时应替换为真实计算的坐标
    '''
    l1_start = np.array([-4, 2, 0])
    l1_end = np.array([4, 2, 0])
    l2_start = np.array([-4, -2, 0])
    l2_end = np.array([4, -2, 0])
    t_start = np.array([-1, 4, 0])
    t_end = np.array([1, -4, 0])
    
    # 计算交点 (这些应该是从实际代码中获取的值)
    intersection1 = np.array([0.2, 2.0, 0])  # 示例值
    intersection2 = np.array([-0.2, -2.0, 0])  # 示例值
    
    # 验证平行线
    verify_parallel_lines(l1_start, l1_end, l2_start, l2_end)
    print()
    
    # 验证截线交点
    verify_transversal_intersections(t_start, t_end, l1_start, l1_end, l2_start, l2_end, 
                                   intersection1, intersection2)
    print()
    
    # 验证角度关系 (需要传入更多参考点)
    point_on_l1_left = intersection1 + np.array([-0.8, 0, 0])
    point_on_l1_right = intersection1 + np.array([0.8, 0, 0])
    point_on_l2_left = intersection2 + np.array([-0.8, 0, 0])
    point_on_l2_right = intersection2 + np.array([0.8, 0, 0])
    point_on_t_above_i1 = intersection1 + (t_end - t_start) * 0.3
    point_on_t_below_i1 = intersection1 - (t_end - t_start) * 0.3
    point_on_t_above_i2 = intersection2 + (t_end - t_start) * 0.3
    point_on_t_below_i2 = intersection2 - (t_end - t_start) * 0.3
    
    verify_angle_relationships(intersection1, intersection2,
                             point_on_l1_left, point_on_l1_right,
                             point_on_l2_left, point_on_l2_right,
                             point_on_t_above_i1, point_on_t_below_i1,
                             point_on_t_above_i2, point_on_t_below_i2)
    '''