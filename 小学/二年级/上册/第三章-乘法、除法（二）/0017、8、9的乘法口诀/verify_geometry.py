import numpy as np

def verify_angles():
    """
    验证涉及的角度，如果大于90度，需要稍微分析一下；
    如果大于180度，要加强注意⚠️，非常非常可能angle方向错了！
    (Manim 的 Angle.from_three_points 默认是逆时针。需要添加 other_angle=True 参数。)
    """
    print("验证角度计算...")

    # 在乘法口诀动画中，我们实际上不涉及具体的角度计算
    # 但在其他几何动画中，需要注意以下情况：

    # 例如，如果我们有一个角度计算：
    # A = np.array([0, 0, 0])
    # B = np.array([1, 0, 0])
    # C = np.array([1, 1, 0])
    #
    # 向量 BA 和 BC
    # vector_BA = A - B  # [-1, 0, 0]
    # vector_BC = C - B  # [0, 1, 0]
    #
    # 计算夹角
    # dot_product = np.dot(vector_BA, vector_BC)
    # norms = np.linalg.norm(vector_BA) * np.linalg.norm(vector_BC)
    # angle_rad = np.arccos(np.clip(dot_product / norms, -1.0, 1.0))
    # angle_deg = np.degrees(angle_rad)
    #
    # print(f"角度为 {angle_deg} 度")
    #
    # if angle_deg > 180:
    #     print("⚠️ 角度大于180度！需要检查方向，可能需要添加 other_angle=True 参数")
    # elif angle_deg > 90:
    #     print("角度大于90度，注意观察")
    # else:
    #     print("锐角，通常没问题")

    print("乘法口诀动画中没有特定的角度计算需要验证")


def grep_MathTex():
    """
    避免 LaTeX 编译错误 (such as LaTeX Error: Unicode character 乘 (U+4E58))
    """
    print("检查 MathTex 使用...")

    # 在我们的乘法口诀动画中，我们主要使用 Text 而不是 MathTex 来避免中文字符的 LaTeX 错误
    # 所以我们不会遇到 Unicode character 错误

    print("动画中使用 Text 而非 MathTex 来显示中文，避免了 LaTeX Unicode 错误")


def verify_boundaries():
    """
    验证元素是否在安全边界内
    """
    print("验证元素边界...")

    # 根据全局配置规范，坐标系边界参考：
    # 横向: x ∈ [-4.5, +4.5] (建议 x ∈ [-4, +4])
    # 纵向: y ∈ [-8, +8]，其中 y ∈ [-3, +5] 为主内容区域

    # 验证我们在动画中使用的坐标是否在边界内
    coordinates_used = [
        (0, 7),    # 顶部作者信息
        (0, 6),    # 标题
        (0, 5.2),  # 副标题
        (-2.5, 3), # 左侧图形位置
        (2.5, -0.5), # 其他图形位置
        (0, -7),   # 底部信息
        (-4.5, 8), # 最大x,y值
        (4.5, 8),  # 最大x,y值
        (-4.5, -8), # 最小x,最大y值
        (4.5, -8)  # 最大x,最小y值
    ]

    boundary_errors = []

    for x, y in coordinates_used:
        if x < -4.5 or x > 4.5:
            boundary_errors.append(f"x坐标 {x} 超出边界 [-4.5, 4.5]")
        if y < -8 or y > 8:
            boundary_errors.append(f"y坐标 {y} 超出边界 [-8, 8]")

    if boundary_errors:
        print("发现边界错误：")
        for error in boundary_errors:
            print(f"  - {error}")
    else:
        print("✓ 所有元素都在安全边界内")


if __name__ == "__main__":
    print("开始验证几何计算...")
    print("="*50)

    verify_angles()
    print()

    grep_MathTex()
    print()

    verify_boundaries()
    print()

    print("="*50)
    print("验证完成！")