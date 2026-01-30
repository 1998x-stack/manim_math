<manim_video_generation_prompt>

# Manim 数学教学动画生成专业指南

## 📋 任务概述

<task_definition>
**目标**: 基于给定的数学题目/知识点，生成高质量的 Manim 教学动画视频代码

**目标受众**: 小学/初中/高中学生
- 使用简洁易懂的语言
- 避免过于抽象的表述
- 注重视觉化和动画引导

**输出格式**: TikTok 竖屏短视频 (1080×1920)

**执行流程**:
1. **阅读技能文档** - 解压并研读 manim skill（包含 references、examples）
2. **构建分镜脚本** - 创建 `storybook.md`，包含详细场景、几何计算、元素生命周期管理
3. **编写动画代码** - 基于分镜脚本和技能文档生成 Python 代码
</task_definition>

---

## 🎯 题目/知识点

<problem>
{
  "年级": "六年级",
  "学期": "第二学期",
  "章节": "第二章",
  "内容": "比例",
  "知识点": "图形的放大与缩小",
  "知识点内容详细描述": "理解图形按比例放大或缩小,是对应边长的比相等,形状不变。如一个三角形按2:1放大,各边长度都扩大到原来的2倍,但各角度数不变,形状不变。应用于地图、模型、设计图等。这是相似图形的初步认识。",
  "数学公式": [
    "按比例k放大: 边长×k, 面积×k²",
    "按比例k缩小: 边长÷k, 面积÷k²",
    "对应边长比相等,形状不变"
  ],
  "相关知识点": [
    "放大",
    "缩小",
    "比例",
    "相似",
    "对应边"
  ],
  "manim动画涉及元素": [
    "Polygon",
    "Text",
    "VGroup",
    "Transform",
    "Scale",
    "Indicate"
  ]
}
</problem>

---

## ⚙️ 全局配置规范

<global_configuration>

### 1. 视频尺寸设置 (TikTok 竖屏)
```python
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9      # 逻辑宽度
config.frame_height = 16    # 逻辑高度
```

### 2. 背景色
```python
self.camera.background_color = "#1a1a2e"
```

### 3. 坐标系边界参考
```
┌─────────────────────────────┐  y = +8
│     顶部安全区 (标题/作者)    │  y = +7
├─────────────────────────────┤  y = +5.5
│                             │
│     主内容区域               │  y ∈ [-3, +5]
│     (几何图形、公式)          │
│                             │
├─────────────────────────────┤  y = -3
│     底部文字区域             │  y ∈ [-6, -3]
│     (说明、步骤提示)          │
├─────────────────────────────┤  y = -6
│     底部安全区               │  y = -8
└─────────────────────────────┘

横向: x ∈ [-4.5, +4.5] (留边距后建议 x ∈ [-4, +4])
```

### 4. 品牌标识
```python
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "Noto Sans CJK SC"  # 或 "SimHei"

# 开头: 题目钩子（抓住注意力）
# 结尾: 作者信息 + "关注我，获得更多数学技巧!"
```

### 5. 字体大小规范
```python
FONT_SIZES = {
    "title": 36,          # 大标题
    "subtitle": 28,       # 副标题/步骤标题
    "body": 22,           # 正文说明
    "label": 20,          # 几何标签 (A, B, C)
    "small": 18,          # 小字/注释
    "author": 20,         # 作者信息
    "formula": 28,        # 数学公式
}
```

</global_configuration>

---

## 🔧 几何元素管理规范

<geometry_management>

### 核心原则
> **所有几何元素必须通过 NumPy 精确计算，严禁臆想坐标！**

### 1. 全局变量存储架构
```python
class MyScene(Scene):
    def construct(self):
        # ===== 1. 初始化所有几何数据 =====
        self.setup_geometry()
        
        # ===== 2. 执行各场景 =====
        self.scene_1_opening()
        self.scene_2_construction()
        # ...
    
    def setup_geometry(self):
        """
        【关键】所有几何元素的坐标在此统一计算和存储
        后续场景只引用，不重复计算
        """
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 2.0
        
        # 主要顶点
        self.A = np.array([...]) * self.SCALE + self.OFFSET
        self.B = np.array([...]) * self.SCALE + self.OFFSET
        self.C = np.array([...]) * self.SCALE + self.OFFSET
        
        # 派生点（中点、垂足、交点等）
        self.M_AB = (self.A + self.B) / 2
        self.foot_A = self.calculate_foot(self.A, self.B, self.C)
        self.circumcenter = self.calculate_circumcenter()
        
        # 边长缓存
        self.AB = np.linalg.norm(self.B - self.A)
        self.BC = np.linalg.norm(self.C - self.B)
        self.CA = np.linalg.norm(self.A - self.C)
        
        # 验证计算正确性
        self.verify_geometry()
```

### 2. 精确计算函数库
```python
def calculate_midpoint(P1, P2):
    """计算中点"""
    return (P1 + P2) / 2

def calculate_foot(point, line_start, line_end):
    """计算点到直线的垂足"""
    line_vec = line_end - line_start
    point_vec = point - line_start
    t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
    return line_start + t * line_vec

def calculate_line_intersection(P1, D1, P2, D2):
    """
    计算两直线交点
    直线1: P1 + t*D1
    直线2: P2 + s*D2
    """
    A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
    b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
    if np.abs(np.linalg.det(A)) < 1e-10:
        return None  # 平行
    params = np.linalg.solve(A, b)
    return np.array([*(P1[:2] + params[0] * D1[:2]), 0])

def calculate_circumcenter(A, B, C):
    """计算三角形的外心 - 使用解析公式"""
    ax, ay = A[0], A[1]
    bx, by = B[0], B[1]
    cx, cy = C[0], C[1]
    D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
    uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
    return np.array([ux, uy, 0])

def calculate_incenter(A, B, C, a=None, b=None, c=None):
    """计算三角形的内心 - 加权平均
    如果未提供边长，则自动计算
    """
    if a is None or b is None or c is None:
        a = np.linalg.norm(B - C)  # BC
        b = np.linalg.norm(C - A)  # CA
        c = np.linalg.norm(A - B)  # AB
    return (a*A + b*B + c*C) / (a + b + c)

def calculate_centroid(A, B, C):
    """计算三角形的重心"""
    return (A + B + C) / 3

# 新增函数
def calculate_orthocenter(A, B, C):
    """计算三角形的垂心"""
    # 垂心是三条高线的交点
    # 可以通过顶点和外心计算：H = A + B + C - 2*O
    O = GeometryCalculator.calculate_circumcenter(A, B, C)
    return A + B + C - 2*O

def calculate_nine_point_center(A, B, C):
    """计算九点圆的圆心（外心与垂心连线的中点）"""
    O = GeometryCalculator.calculate_circumcenter(A, B, C)
    H = GeometryCalculator.calculate_orthocenter(A, B, C)
    return (O + H) / 2

def calculate_euler_line_points(A, B, C, t_range=(-2, 2)):
    """计算欧拉线上的点（用于可视化）
    返回欧拉线上的两个点（直线两端）
    """
    O = GeometryCalculator.calculate_circumcenter(A, B, C)
    H = GeometryCalculator.calculate_orthocenter(A, B, C)
    
    # 欧拉线方向向量
    direction = H - O
    direction = direction / np.linalg.norm(direction)  # 单位化
    
    # 返回两个点以绘制直线
    return [O + t_range[0] * direction, O + t_range[1] * direction]

def calculate_angle(A, B, C):
    """计算∠ABC的角度（弧度）"""
    BA = A - B
    BC = C - B
    cos_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
    # 处理数值误差
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    return np.arccos(cos_angle)

def calculate_triangle_area(A, B, C):
    """计算三角形面积"""
    return 0.5 * np.abs(
        A[0]*(B[1]-C[1]) + 
        B[0]*(C[1]-A[1]) + 
        C[0]*(A[1]-B[1])
    )

def calculate_distance_point_to_line(point, line_start, line_end):
    """计算点到直线的距离"""
    # 使用叉积公式：|(p - a) × (b - a)| / |b - a|
    line_vec = line_end - line_start
    point_vec = point - line_start
    cross_product = np.cross(point_vec[:2], line_vec[:2])
    return np.abs(cross_product) / np.linalg.norm(line_vec)

def calculate_angle_bisector(A, B, C):
    """计算∠ABC的角平分线与AC的交点"""
    # 角平分线定理：AB/BC = AD/DC
    AB = np.linalg.norm(B - A)
    BC = np.linalg.norm(B - C)
    ratio = AB / BC
    
    # 在AC上找到分割点
    D = (C * ratio + A) / (1 + ratio)
    return np.array([*D[:2], 0])

def calculate_perpendicular_bisector(P1, P2):
    """计算线段P1P2的垂直平分线
    返回：中点、方向向量
    """
    midpoint = GeometryCalculator.calculate_midpoint(P1, P2)
    segment = P2 - P1
    # 垂直向量（旋转90度）
    perpendicular = np.array([-segment[1], segment[0], 0])
    return midpoint, perpendicular

def is_point_in_triangle(P, A, B, C):
    """判断点P是否在三角形ABC内部（含边界）"""
    # 使用重心坐标法
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    d1 = sign(P, A, B)
    d2 = sign(P, B, C)
    d3 = sign(P, C, A)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)  # 点在三角形内或边界上

def calculate_circle_center_from_points(P1, P2, P3):
    """通过三点计算圆的圆心"""
    # 使用垂直平分线的交点
    mid1, dir1 = GeometryCalculator.calculate_perpendicular_bisector(P1, P2)
    mid2, dir2 = GeometryCalculator.calculate_perpendicular_bisector(P2, P3)
    
    return GeometryCalculator.calculate_line_intersection(mid1, dir1, mid2, dir2)

def calculate_reflection_point(point, line_start, line_end):
    """计算点关于直线的对称点"""
    foot = GeometryCalculator.calculate_foot(point, line_start, line_end)
    return 2 * foot - point

def calculate_parallel_line(point, direction):
    """通过点和方向计算平行线
    返回：点、方向向量
    """
    return point, direction

def calculate_median_intersection(A, B, C, vertex_index=0):
    """计算中线上的点（用于绘制中线）
    vertex_index: 0->A, 1->B, 2->C
    """
    vertices = [A, B, C]
    vertex = vertices[vertex_index]
    opposite_midpoint = GeometryCalculator.calculate_midpoint(
        vertices[(vertex_index + 1) % 3],
        vertices[(vertex_index + 2) % 3]
    )
    return vertex, opposite_midpoint
    
def circle_intersection(c1, r1, c2, r2):
    """
    计算两个圆的交点
    c1, c2: 圆心坐标 [x, y, z]
    r1, r2: 半径
    返回: 交点列表 (可能为0,1,2个交点)
    """
    # 转换为2D计算
    x1, y1 = c1[0], c1[1]
    x2, y2 = c2[0], c2[1]
    
    # 计算圆心距离
    d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 检查是否相交
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0 and r1 != r2:
        return []  # 无交点
    
    # 计算交点
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = np.sqrt(r1**2 - a**2)
    
    x0 = x1 + a * (x2 - x1) / d
    y0 = y1 + a * (y2 - y1) / d
    
    if h < 1e-10:  # 相切，一个交点
        return [np.array([x0, y0, 0])]
    
    # 两个交点
    rx = -h * (y2 - y1) / d
    ry = h * (x2 - x1) / d
    
    return [
        np.array([x0 + rx, y0 + ry, 0]),
        np.array([x0 - rx, y0 - ry, 0])
    ]

def line_circle_intersection(line_start, line_end, circle_center, radius):
    """
    计算直线与圆的交点
    直线: 从line_start到line_end
    圆: 圆心circle_center，半径radius
    返回: 交点列表
    """
    # 转换为2D
    A = np.array(line_start[:2])
    B = np.array(line_end[:2])
    C = np.array(circle_center[:2])
    
    # 直线方向向量
    AB = B - A
    AB_norm = AB / np.linalg.norm(AB) if np.linalg.norm(AB) > 0 else AB
    
    # 直线参数方程: A + t*AB
    # 计算t使得距离圆心为radius
    AC = C - A
    
    # 解二次方程: ||A + t*AB - C||^2 = radius^2
    a = np.dot(AB, AB)
    b = 2 * np.dot(AB, AC)
    c = np.dot(AC, AC) - radius**2
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return []  # 无交点
    
    t1 = (-b + np.sqrt(discriminant)) / (2*a)
    t2 = (-b - np.sqrt(discriminant)) / (2*a)
    
    intersections = []
    if 0 <= t1 <= 1:
        intersections.append(np.array([*(A + t1*AB), 0]))
    if 0 <= t2 <= 1 and abs(t1 - t2) > 1e-10:
        intersections.append(np.array([*(A + t2*AB), 0]))
    
    return intersections

def calculate_arc_parameters(center, start_point, end_point, angle=None):
    """
    计算圆弧的参数
    返回: 圆心, 半径, 起始角度(弧度), 终止角度(弧度)
    """
    # 计算半径
    radius = np.linalg.norm(start_point[:2] - center[:2])
    
    # 计算角度
    start_angle = atan2(start_point[1] - center[1], start_point[0] - center[0])
    end_angle = atan2(end_point[1] - center[1], end_point[0] - center[0])
    
    # 如果提供了角度，直接使用
    if angle is not None:
        end_angle = start_angle + angle
    
    # 确保角度在[0, 2π)范围内
    start_angle = start_angle % (2*pi)
    end_angle = end_angle % (2*pi)
    
    return center, radius, start_angle, end_angle

def calculate_arc_points(center, radius, start_angle, end_angle, num_points=100):
    """
    生成圆弧上的点
    用于在manim中绘制精确的圆弧
    """
    # 确保角度方向正确
    if end_angle < start_angle:
        end_angle += 2*pi
    
    angles = np.linspace(start_angle, end_angle, num_points)
    points = []
    for angle in angles:
        x = center[0] + radius * cos(angle)
        y = center[1] + radius * sin(angle)
        z = center[2] if len(center) > 2 else 0
        points.append(np.array([x, y, z]))
    
    return points

def calculate_tangent_points(point, circle_center, radius):
    """
    计算从一点到圆的切线切点
    返回: 切点列表 (0,1,2个)
    """
    # 转换为2D
    P = np.array(point[:2])
    C = np.array(circle_center[:2])
    
    # 计算点到圆心的距离
    d = np.linalg.norm(P - C)
    
    if d < radius:  # 点在圆内，无切线
        return []
    elif abs(d - radius) < 1e-10:  # 点在圆上，一个切点
        return [np.array([*P, 0])]
    
    # 计算切点
    # 使用相似三角形：PT^2 = d^2 - r^2
    PT = np.sqrt(d**2 - radius**2)
    
    # 计算角度
    alpha = acos(radius / d)
    beta = atan2(P[1] - C[1], P[0] - C[0])
    
    # 两个切点
    angle1 = beta + alpha
    angle2 = beta - alpha
    
    return [
        np.array([C[0] + radius * cos(angle1), C[1] + radius * sin(angle1), 0]),
        np.array([C[0] + radius * cos(angle2), C[1] + radius * sin(angle2), 0])
    ]

def calculate_common_tangent_lines(c1, r1, c2, r2):
    """
    计算两个圆的公切线
    返回: 每条切线由两个切点定义 [(切点1在圆1, 切点2在圆2), ...]
    """
    # 转换为2D
    x1, y1 = c1[0], c1[1]
    x2, y2 = c2[0], c2[1]
    
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if d < abs(r1 - r2):  # 内含，无公切线
        return []
    
    results = []
    
    # 处理外切线
    if d > abs(r1 - r2):
        # 外切线条数: 2
        if abs(r1 - r2) < 1e-10:  # 半径相等
            # 平行切线
            angle = atan2(y2-y1, x2-x1)
            perp_angle = angle + pi/2
            
            for sign in [1, -1]:
                dx1 = r1 * cos(perp_angle) * sign
                dy1 = r1 * sin(perp_angle) * sign
                dx2 = r2 * cos(perp_angle) * sign
                dy2 = r2 * sin(perp_angle) * sign
                
                results.append((
                    np.array([x1+dx1, y1+dy1, 0]),
                    np.array([x2+dx2, y2+dy2, 0])
                ))
        else:
            # 一般情况外切线
            # 计算相似中心
            if r1 > r2:
                k = r1 / (r1 - r2)
                center = np.array([x1 + k*(x2-x1), y1 + k*(y2-y1)])
            else:
                k = r2 / (r2 - r1)
                center = np.array([x2 + k*(x1-x2), y2 + k*(y1-y2)])
            
            # 从相似中心向两个圆作切线
            points1 = EnhancedGeometryCalculator.calculate_tangent_points(center, c1, r1)
            points2 = EnhancedGeometryCalculator.calculate_tangent_points(center, c2, r2)
            
            # 配对切线
            for i, p1 in enumerate(points1[:2]):
                for j, p2 in enumerate(points2[:2]):
                    # 检查是否在同一条直线上（通过相似中心）
                    if abs(np.cross(p1[:2]-center, p2[:2]-center)) < 1e-10:
                        results.append((p1, p2))
    
    # 处理内切线
    if d > r1 + r2:
        # 内切线条数: 2
        # 计算内相似中心
        k = r1 / (r1 + r2)
        center = np.array([x1 + k*(x2-x1), y1 + k*(y2-y1)])
        
        # 从内相似中心向两个圆作切线
        points1 = EnhancedGeometryCalculator.calculate_tangent_points(center, c1, r1)
        points2 = EnhancedGeometryCalculator.calculate_tangent_points(center, c2, r2)
        
        # 配对切线
        for i, p1 in enumerate(points1[:2]):
            for j, p2 in enumerate(points2[:2]):
                if abs(np.cross(p1[:2]-center, p2[:2]-center)) < 1e-10:
                    results.append((p1, p2))
    
    return results

def calculate_angle_arc_center(vertex, point1, point2, radius):
    """
    计算角度的圆弧的圆心和参数
    vertex: 角的顶点
    point1, point2: 角的两边上的一点
    radius: 圆弧半径
    返回: 圆心, 起始角度, 终止角度
    """
    # 计算角的两边方向
    v1 = point1[:2] - vertex[:2]
    v2 = point2[:2] - vertex[:2]
    
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    
    # 计算角平分线方向
    bisector = v1_norm + v2_norm
    if np.linalg.norm(bisector) < 1e-10:  # 180度角
        bisector = np.array([-v1_norm[1], v1_norm[0]])  # 垂直方向
    
    bisector_norm = bisector / np.linalg.norm(bisector)
    
    # 计算圆心（沿着角平分线）
    # 需要计算圆心到两边的距离等于radius
    # 使用公式: distance = radius / sin(angle/2)
    angle = EnhancedGeometryCalculator.calculate_angle(point1, vertex, point2)
    d = radius / sin(angle/2)
    
    center_2d = vertex[:2] + d * bisector_norm
    center = np.array([center_2d[0], center_2d[1], vertex[2] if len(vertex)>2 else 0])
    
    # 计算圆弧起始和终止角度
    start_angle = atan2(point1[1] - center[1], point1[0] - center[0])
    end_angle = atan2(point2[1] - center[1], point2[0] - center[0])
    
    return center, start_angle, end_angle

def calculate_sector_area(center, radius, start_angle, end_angle):
    """计算扇形面积"""
    if end_angle < start_angle:
        end_angle += 2*pi
    
    angle = end_angle - start_angle
    return 0.5 * radius**2 * angle

def calculate_segment_area(center, radius, start_angle, end_angle):
    """计算弓形面积"""
    sector_area = EnhancedGeometryCalculator.calculate_sector_area(center, radius, start_angle, end_angle)
    
    if end_angle < start_angle:
        end_angle += 2*pi
    
    angle = end_angle - start_angle
    triangle_area = 0.5 * radius**2 * sin(angle)
    
    return sector_area - triangle_area

def create_parallel_line(point, line_start, line_end):
    """创建通过一点且平行于给定直线的直线
    返回: 新直线上的两个点
    """
    direction = line_end - line_start
    return point, point + direction

def create_perpendicular_line(point, line_start, line_end):
    """创建通过一点且垂直于给定直线的直线
    返回: 垂足, 垂线的另一个点
    """
    foot = EnhancedGeometryCalculator.calculate_foot(point, line_start, line_end)
    # 垂直方向
    direction = line_end - line_start
    perpendicular = np.array([-direction[1], direction[0], 0])
    
    return foot, foot + perpendicular

def create_angle_bisector_line(vertex, point1, point2, length=2):
    """创建角的平分线
    返回: 平分线上的两个点
    """
    v1 = point1 - vertex
    v2 = point2 - vertex
    
    # 角平分线方向
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    bisector_dir = v1_norm + v2_norm
    
    if np.linalg.norm(bisector_dir) < 1e-10:  # 180度角
        bisector_dir = np.array([-v1_norm[1], v1_norm[0], 0])
    
    bisector_dir = bisector_dir / np.linalg.norm(bisector_dir)
    
    return vertex, vertex + length * bisector_dir

def calculate_inscribed_circle(triangle_points):
    """计算三角形的内切圆
    返回: 圆心, 半径
    """
    A, B, C = triangle_points
    
    # 计算边长
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(C - A)
    c = np.linalg.norm(A - B)
    
    # 内心
    incenter = (a*A + b*B + c*C) / (a + b + c)
    
    # 内切圆半径: r = 2S / (a+b+c)
    area = EnhancedGeometryCalculator.calculate_triangle_area(A, B, C)
    radius = 2 * area / (a + b + c)
    
    return incenter, radius

def calculate_circumcircle(triangle_points):
    """计算三角形的外接圆
    返回: 圆心, 半径
    """
    A, B, C = triangle_points
    
    # 外心
    circumcenter = EnhancedGeometryCalculator.calculate_circumcenter(A, B, C)
    
    # 半径
    radius = np.linalg.norm(A - circumcenter)
    
    return circumcenter, radius
```

### 3. 几何验证函数
```python
def verify_geometry(self):
    """验证所有计算的正确性"""
    epsilon = 1e-6
    
    # 示例：验证外心到三顶点距离相等
    dist_A = np.linalg.norm(self.circumcenter - self.A)
    dist_B = np.linalg.norm(self.circumcenter - self.B)
    dist_C = np.linalg.norm(self.circumcenter - self.C)
    assert abs(dist_A - dist_B) < epsilon, "外心计算错误!"
    assert abs(dist_B - dist_C) < epsilon, "外心计算错误!"
    
    print("✓ 几何验证通过")
```

### 4. 缩放时的坐标同步
```python
# ❌ 错误做法：缩放后几何点不同步
triangle.scale(0.5)
dot.move_to(self.circumcenter)  # 位置错误！

# ✅ 正确做法：重新计算或使用相对定位
scale_factor = 0.5
new_center = triangle.get_center()
new_circumcenter = (self.circumcenter - old_center) * scale_factor + new_center
dot.move_to(new_circumcenter)
```

</geometry_management>

---

## 🚫 常见错误及修复

<err_example>
1. Chinese characters cannot be used in MathTex
2. 在LaTeX中，度数符号需要使用 ^\circ 或 ^{\circ} 表示，而不是直接使用 °。让我修复所有相关部分：
3. 错误显示在创建 Sector 对象时出现了参数冲突：outer_radius 参数被重复赋值。这是因为 Sector 类的构造函数可能不接受 outer_radius 参数，而是使用 radius 参数。
4. 问题仍然在LaTeX编译阶段。错误信息显示 you need another { and }，这通常表示LaTeX公式语法有问题。\over 命令在LaTeX中需要正确的分组。
5. 有双花括号 {{...}} 导致Manim解析错误
6. 度数符号问题：在MathTex中，要么直接使用数字（如60），要么使用LaTeX的度数命令 ^\circ（但需要确保Manim支持）
7. ❌ Original (causes error): Tex(r"周角 $= 360^\circ$"); ✅ Fixed: chinese = Text("周角 =", font="Noto Sans CJK SC")    math = MathTex(r"360^\circ")    VGroup(chinese, math).arrange(RIGHT)
</err_example>

<error_prevention>

### 1. LaTeX/Unicode 错误
```python
# ❌ 错误：中文放入 MathTex
MathTex(r"\text{三角形}")  # Unicode Error!

# ✅ 正确：中文用 Text，数学用 MathTex
Text("三角形", font="Noto Sans CJK SC")
MathTex(r"\triangle ABC")
```

### 2. 虚线绘制
```python
# ❌ 错误：set_style 不支持 stroke_dasharray
line.set_style(stroke_dasharray="5 5")  # TypeError!

# ✅ 正确：使用 DashedLine 或 DashedVMobject
DashedLine(start, end, dash_length=0.1, color=GRAY)
DashedVMobject(Line(start, end), num_dashes=20)
```

### 3. 元素溢出边界
```python
# ❌ 错误：硬编码位置
text.move_to(UP * 10)  # 超出 frame_height=16 的一半 (8)

# ✅ 正确：使用安全边界
MAX_Y = 7.5  # 留 0.5 余量
text.move_to(UP * min(desired_y, MAX_Y))
```

### 4. 位置管理混乱
```python
# ❌ 错误：不同场景使用不一致的偏移
# scene_1: triangle.shift(UP * 2)
# scene_2: triangle.shift(UP * 4)

# ✅ 正确：统一在 setup_geometry() 定义
self.MAIN_OFFSET = UP * 2
self.A = base_A + self.MAIN_OFFSET
```

### 5. 元素未清理
```python
# ❌ 错误：场景切换时残留元素
self.play(Create(helper_line))
# ... 忘记 FadeOut

# ✅ 正确：明确管理元素生命周期
self.play(Create(helper_line))
# ... 使用完毕
self.play(FadeOut(helper_line))

# 或使用 VGroup 批量管理
temp_elements = VGroup(line1, line2, dot)
self.play(FadeOut(temp_elements))
```

### 6. 重复计算
```python
# ❌ 错误：每个方法都重新计算
def scene_1(self):
    midpoint = (self.A + self.B) / 2  # 重复
def scene_2(self):
    midpoint = (self.A + self.B) / 2  # 重复

# ✅ 正确：setup_geometry 中统一计算
def setup_geometry(self):
    self.M_AB = (self.A + self.B) / 2
```

</error_prevention>

---

## 📝 分镜脚本模板 (storybook.md)

<storybook_template>
```markdown
# [题目名称] - 动画分镜脚本

## 元信息
- 目标时长: XX 秒
- 场景数量: X 个
- 难度等级: 中等

## 颜色配置
```python
COLOR_PRIMARY = "#..."
COLOR_SECONDARY = "#..."
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 中点M | (A+B)/2 | self.M |
| 外心O | 三边垂直平分线交点 | self.O |
| ... | ... | ... |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 主图形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 图形创建 | `Create(triangle)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: triangle, author_info

---

## Scene 2: [场景名称] (X-X秒)
...

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| triangle | Scene 1 | Scene 8 | 主三角形 |
| aux_line | Scene 3 | Scene 3 | 临时辅助线 |
| ... | ... | ... | ... |
```
</storybook_template>

---

## 🎬 动画节奏指南

<timing_guide>

| 内容类型 | 建议时长 | 说明 |
|---------|---------|------|
| 简单图形创建 | 0.5-1.0s | `Create(simple_shape)` |
| 复杂图形创建 | 1.0-1.5s | 等边三角形、圆等 |
| 文字书写 | 0.4-0.8s | 根据长度调整 |
| 公式书写 | 0.6-1.0s | 复杂公式更长 |
| 变换动画 | 0.8-1.2s | `Transform(a, b)` |
| 简单等待 | 0.3-0.5s | 过渡停顿 |
| 理解停顿 | 1.0-2.0s | 关键步骤后 |
| **难点停留** | **2.0-3.0s** | 核心概念，让学生消化 |
| 场景切换 | 0.4-0.6s | FadeOut 批量元素 |

### 节奏原则
1. **难点慢，简单快** - 关键步骤多停留
2. **动静结合** - 动画后适当等待
3. **呼吸感** - 不要连续高密度动画
4. **总时长控制** - TikTok 建议 45-90 秒

</timing_guide>

---

## 📚 Manim 技能参考

<manim_skill>
---
name: manim
description: >
  Create mathematical animations using Manim (Mathematical Animation Engine).
  Use when Claude needs to create math visualizations, animate equations or
  formulas, plot function graphs, visualize geometric transformations, create
  3D mathematical surfaces, build step-by-step proof animations, or generate
  LaTeX-rendered formula animations.
---

# Manim Mathematical Animation Skill

Create precise, professional mathematical animations using Python code.

## Quick Start

```python
from manim import *

class Example(Scene):
    def construct(self):
        formula = MathTex(r"E = mc^2")
        self.play(Write(formula))
        self.wait()
```

Render: `manim -pql script.py Example`

## Core Workflow

1. **Create objects** → `Circle()`, `MathTex()`, `Axes()`
2. **Position them** → `.move_to()`, `.next_to()`, `.shift()`
3. **Animate** → `self.play(Create(obj))`, `Transform(a, b)`
4. **Wait** → `self.wait(seconds)`

## Essential Classes

### Geometric Shapes

```python
Circle(radius=1, color=BLUE, fill_opacity=0.5)
Square(side_length=2)
Rectangle(width=4, height=2)
Line(start=LEFT, end=RIGHT)
Arrow(start=ORIGIN, end=UP)
Dot(point=ORIGIN, radius=0.1)
Polygon(ORIGIN, RIGHT, UP)  # Triangle
```

### Text & Math

```python
Text("Hello", font_size=48)           # Plain text
Tex(r"This is \LaTeX")                # LaTeX text mode
MathTex(r"\int_0^1 x^2 dx = \frac{1}{3}")  # Math mode (auto)
```

**LaTeX tips:**
- Use raw strings: `r"..."`
- MathTex auto-wraps in math mode
- Isolate parts with `{{ }}`: `MathTex(r"{{ a }}^2 + {{ b }}^2")`

### Coordinate Systems

```python
axes = Axes(
    x_range=[-3, 3, 1],   # [min, max, step]
    y_range=[-2, 2, 0.5],
    axis_config={"include_numbers": True}
)
graph = axes.plot(lambda x: np.sin(x), color=BLUE)
label = axes.get_graph_label(graph, r"\sin(x)")
```

### 3D Objects (use `ThreeDScene`)

```python
class My3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        axes = ThreeDAxes()
        sphere = Sphere(radius=1)
        self.add(axes, sphere)
```

## Essential Animations

| Animation | Effect |
|-----------|--------|
| `Create(obj)` | Draw outline |
| `Write(text)` | Handwriting effect |
| `FadeIn(obj)` / `FadeOut(obj)` | Fade |
| `Transform(a, b)` | Morph a into b |
| `ReplacementTransform(a, b)` | Replace a with b |
| `TransformMatchingTex(t1, t2)` | Smart TeX transform |
| `GrowFromCenter(obj)` | Grow from center |
| `Rotate(obj, angle=PI)` | Rotation |

### Animate Syntax (Recommended)

```python
self.play(obj.animate.shift(RIGHT * 2))
self.play(obj.animate.scale(0.5).set_color(RED))
self.play(obj.animate.rotate(PI/4).move_to(UP))
```

### Animation Parameters

```python
self.play(Create(circle), run_time=2, rate_func=smooth)
# rate_func options: smooth, linear, rush_into, rush_from, there_and_back
```

## Positioning

```python
# Absolute
obj.move_to(ORIGIN)
obj.move_to([1, 2, 0])

# Relative
obj.shift(RIGHT * 2 + UP)
obj.next_to(other, DOWN, buff=0.5)
obj.to_edge(LEFT)
obj.to_corner(UR)

# Alignment
obj.align_to(other, UP)  # Align top edges
```

**Direction constants:** `UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR, ORIGIN, OUT, IN`

## Grouping

```python
group = VGroup(circle, square, triangle)
group.arrange(RIGHT, buff=0.5)       # Horizontal layout
group.arrange(DOWN, aligned_edge=LEFT)  # Vertical, left-aligned
group.set_color(BLUE)                # Apply to all
group[0].set_color(RED)              # Access by index
```

## ValueTracker & Updaters

For dynamic animations:

```python
t = ValueTracker(0)

# Method 1: always_redraw
dot = always_redraw(lambda: Dot([t.get_value(), 0, 0]))

# Method 2: add_updater
label = DecimalNumber(0)
label.add_updater(lambda m: m.set_value(t.get_value()))

self.add(dot, label)
self.play(t.animate.set_value(5), run_time=3)
```

## CLI Quick Reference

```bash
# Quality presets
-ql   # 480p 15fps (preview)
-qm   # 720p 30fps
-qh   # 1080p 60fps
-qk   # 4K 60fps

# Common flags
-p    # Preview after render
-s    # Save last frame only
-t    # Transparent background
-c WHITE  # Background color
--format gif  # Output GIF

# Examples
manim -pql scene.py MyScene     # Quick preview
manim -qh scene.py MyScene      # High quality
manim -pql --format gif scene.py MyScene  # GIF output
```

## Common Patterns

### Equation Derivation

```python
step1 = MathTex(r"(a+b)^2")
step2 = MathTex(r"a^2 + 2ab + b^2")
self.play(Write(step1))
self.wait()
self.play(TransformMatchingTex(step1, step2))
```

### Function Animation

```python
axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
t = ValueTracker(-3)

graph = always_redraw(
    lambda: axes.plot(lambda x: np.sin(x), x_range=[-3, t.get_value()], color=BLUE)
)
dot = always_redraw(
    lambda: Dot(axes.c2p(t.get_value(), np.sin(t.get_value())))
)

self.add(axes, graph, dot)
self.play(t.animate.set_value(3), run_time=4)
```

### Sub-formula Coloring

```python
eq = MathTex(r"{{ a }}^2 + {{ b }}^2 = {{ c }}^2")
eq.set_color_by_tex("a", RED)
eq.set_color_by_tex("b", BLUE)
eq.set_color_by_tex("c", GREEN)
```

### Moving Camera (3D)

```python
class CameraMove(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        # ...
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
```

## Color Constants

`RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD, MAROON, WHITE, BLACK, GRAY`

Variants: `BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E` (light to dark)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| LaTeX error | Check LaTeX installation; use raw strings `r"..."` |
| Chinese text broken | Specify font: `Text("中文", font="SimHei")` |
| Slow rendering | Use `-ql` for preview |
| Memory error | Use `self.remove(obj)` to free objects |

## References

For advanced topics, see:
- `references/advanced-patterns.md` - Complex animation patterns
- `references/3d-guide.md` - 3D scene techniques
- `references/latex-cheatsheet.md` - LaTeX math symbols
</manim_skill>

---

## ✅ 代码质量检查清单

<quality_checklist>

### 运行前检查
- [ ] 所有几何点在 `setup_geometry()` 中统一计算
- [ ] 使用 `verify_geometry()` 验证计算正确性
- [ ] 中文文本使用 `Text()` 而非 `MathTex()`
- [ ] 虚线使用 `DashedLine` 或 `DashedVMobject`
- [ ] 所有元素位置在边界范围内 (x∈[-4,4], y∈[-7,7])
- [ ] 字体大小遵循规范
- [ ] 元素生命周期明确（创建/销毁）

### 渲染后检查
- [ ] 无元素溢出边界
- [ ] 无文字/图形重叠
- [ ] 动画节奏流畅
- [ ] 难点有足够停留时间
- [ ] 开头有钩子，结尾有作者信息
- [ ] 总时长符合预期

</quality_checklist>

---

## 🖼️ 良好示例模板

<good_template>
"""
三角形的五心动画 - Triangle Five Centers Animation
使用 Manim 创建的中学几何教学视频

内容: 外心、内心、重心、垂心、旁心的定义、构造和性质
目标观众: 中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TriangleFiveCenters(Scene):
    """
    三角形五心教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 外心 (Circumcenter)
    3. 内心 (Incenter)
    4. 重心 (Centroid)
    5. 垂心 (Orthocenter)
    6. 旁心 (Excenter)
    7. 五心汇总
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCUMCENTER = "#e74c3c"  # 红色 - 外心
        self.COLOR_INCENTER = "#3498db"      # 蓝色 - 内心
        self.COLOR_CENTROID = "#2ecc71"      # 绿色 - 重心
        self.COLOR_ORTHOCENTER = "#f39c12"   # 橙色 - 垂心
        self.COLOR_EXCENTER = "#9b59b6"      # 紫色 - 旁心
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_circumcenter()
        self.show_incenter()
        self.show_centroid()
        self.show_orthocenter()
        self.show_excenter()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点 (使用斜三角形便于展示所有五心)
        self.A = np.array([-2.5, 1.5, 0])
        self.B = np.array([2.5, -0.5, 0])
        self.C = np.array([-1.0, -2.5, 0])
        
        # 缩放和偏移
        self.SCALE = 0.9
        self.OFFSET = UP * 1.5
        
        # 应用变换
        self.A = self.A * self.SCALE + self.OFFSET
        self.B = self.B * self.SCALE + self.OFFSET
        self.C = self.C * self.SCALE + self.OFFSET
        
        # 计算边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # 预计算所有中点
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2
        
        # 预计算五心
        self.circumcenter = self.calculate_circumcenter()
        self.incenter = self.calculate_incenter()
        self.centroid = self.calculate_centroid()
        self.orthocenter = self.calculate_orthocenter()
        self.excenter_A = self.calculate_excenter_A()
        
        # 验证几何计算
        self.verify_geometry()
        
        # 创建三角形对象 (但不添加到场景)
        self.triangle = Polygon(self.A, self.B, self.C, color=self.COLOR_TRIANGLE, stroke_width=3)
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证外心：到三顶点距离相等
        dist_OA = np.linalg.norm(self.circumcenter - self.A)
        dist_OB = np.linalg.norm(self.circumcenter - self.B)
        dist_OC = np.linalg.norm(self.circumcenter - self.C)
        
        if not (abs(dist_OA - dist_OB) < epsilon and abs(dist_OB - dist_OC) < epsilon):
            print(f"WARNING: 外心计算可能有误! 距离: {dist_OA:.6f}, {dist_OB:.6f}, {dist_OC:.6f}")
        
        # 验证内心：应该是加权平均
        incenter_check = (self.a * self.A + self.b * self.B + self.c * self.C) / (self.a + self.b + self.c)
        if np.linalg.norm(self.incenter - incenter_check) > epsilon:
            print(f"WARNING: 内心计算可能有误!")
        
        # 验证重心：应该是简单平均
        centroid_check = (self.A + self.B + self.C) / 3
        if np.linalg.norm(self.centroid - centroid_check) > epsilon:
            print(f"WARNING: 重心计算可能有误!")
        
        # 验证垂心：验证高线垂直性
        # 从A到BC的高应该垂直于BC
        foot_BC = self.perpendicular_foot(self.orthocenter, self.B, self.C)
        vec_H_to_foot = foot_BC - self.orthocenter
        vec_BC = self.C - self.B
        
        # 点积应该接近0（垂直）
        dot_product = np.dot(vec_H_to_foot[:2], vec_BC[:2])
        if abs(dot_product) > epsilon:
            print(f"WARNING: 垂心计算可能有误! 点积: {dot_product:.6f}")
        
        print("✓ 几何验证完成")
    
    def calculate_circumcenter(self):
        """计算外心 - 使用解析公式精确计算"""
        # 使用公式: O = A + [(|AC|^2(AB) - |AB|^2(AC)) × (AB × AC)] / (2|AB × AC|^2)
        # 更简单的方法: 解线性方程组
        
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]
        
        # 计算D值 (行列式)
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        
        if abs(D) < 1e-10:
            # 三点共线，退化情况
            return (self.A + self.B + self.C) / 3
        
        # 计算外心坐标
        ux = ((ax**2 + ay**2) * (by - cy) + 
              (bx**2 + by**2) * (cy - ay) + 
              (cx**2 + cy**2) * (ay - by)) / D
        
        uy = ((ax**2 + ay**2) * (cx - bx) + 
              (bx**2 + by**2) * (ax - cx) + 
              (cx**2 + cy**2) * (bx - ax)) / D
        
        return np.array([ux, uy, 0])
    
    def calculate_incenter(self):
        """计算内心 - 加权平均"""
        return (self.a * self.A + self.b * self.B + self.c * self.C) / (self.a + self.b + self.c)
    
    def calculate_centroid(self):
        """计算重心 - 简单平均"""
        return (self.A + self.B + self.C) / 3
    
    def calculate_orthocenter(self):
        """计算垂心 - 使用解析公式精确计算"""
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]
        
        # 从A到BC的高线: 方向垂直于BC
        # BC的方向向量: (cx-bx, cy-by)
        # 高线方向: (cy-by, bx-cx)
        
        # 从B到AC的高线: 方向垂直于AC
        # AC的方向向量: (cx-ax, cy-ay)
        # 高线方向: (cy-ay, ax-cx)
        
        # 高线1: A + t1*(cy-by, bx-cx)
        # 高线2: B + t2*(cy-ay, ax-cx)
        
        # 解方程组找交点
        # ax + t1*(cy-by) = bx + t2*(cy-ay)
        # ay + t1*(bx-cx) = by + t2*(ax-cx)
        
        det = (cy - by) * (ax - cx) - (bx - cx) * (cy - ay)
        
        if abs(det) < 1e-10:
            # 退化情况
            return self.centroid
        
        t1 = ((bx - ax) * (ax - cx) + (by - ay) * (ay - cy)) / det
        
        hx = ax + t1 * (cy - by)
        hy = ay + t1 * (bx - cx)
        
        return np.array([hx, hy, 0])
    
    def calculate_excenter_A(self):
        """计算角A对应的旁心 - 使用精确公式"""
        # 旁心公式: J_A = (-a*A + b*B + c*C) / (-a + b + c)
        # 其中 a = |BC|, b = |CA|, c = |AB|
        
        denom = -self.a + self.b + self.c
        
        if abs(denom) < 1e-10:
            # 退化情况 (不太可能发生)
            return self.A + (self.B - self.A) * 2
        
        excenter = (-self.a * self.A + self.b * self.B + self.c * self.C) / denom
        return excenter
    
    def perpendicular_foot(self, point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + projection * line_vec
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 标题
        title = Text(
            "三角形的五心",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "神奇的几何中心",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 三角形淡入
        self.play(Create(self.triangle), run_time=1.0)
        
        # 五个小点闪烁
        centers = [
            self.circumcenter,
            self.incenter,
            self.centroid,
            self.orthocenter,
            self.excenter_A
        ]
        
        dots = VGroup(*[
            Dot(center, radius=0.08, color=YELLOW)
            for center in centers
        ])
        
        for dot in dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)
        
        # 提示文字
        hint = Text(
            "一个三角形竟有五个特殊点?",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hint),
            FadeOut(dots),
            run_time=0.5
        )
    
    def show_circumcenter(self):
        """场景2: 外心 - 垂直平分线交点"""
        # 标题
        title = Text(
            "外心 Circumcenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_CIRCUMCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三边垂直平分线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: AB的垂直平分线
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ab_line), run_time=0.5)
        
        # 中点
        m_ab_dot = Dot(self.M_AB, color=self.COLOR_AUXILIARY, radius=0.06)
        m_ab_label = Text("M", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(m_ab_dot, UP, buff=0.1)
        
        self.play(FadeIn(m_ab_dot), FadeIn(m_ab_label), run_time=0.4)
        
        # 垂直平分线 - 精确计算方向和端点
        dir_AB = self.B - self.A
        perp_AB = np.array([-dir_AB[1], dir_AB[0], 0])  # 垂直方向
        perp_AB_normalized = perp_AB / np.linalg.norm(perp_AB)
        
        # 计算合适的长度，确保能看到交点
        extension_length = 3.0
        perp_line_1 = DashedLine(
            self.M_AB - perp_AB_normalized * extension_length,
            self.M_AB + perp_AB_normalized * extension_length,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        explain_1 = Text(
            "垂直平分线: 过中点且垂直",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(perp_line_1), FadeIn(explain_1), run_time=0.8)
        self.play(ab_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        
        # Step 2: BC的垂直平分线
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.5)
        
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        self.play(FadeIn(m_bc_dot), run_time=0.3)
        
        dir_BC = self.C - self.B
        perp_BC = np.array([-dir_BC[1], dir_BC[0], 0])  # 垂直方向
        perp_BC_normalized = perp_BC / np.linalg.norm(perp_BC)
        
        extension_length = 3.0
        perp_line_2 = DashedLine(
            self.M_BC - perp_BC_normalized * extension_length,
            self.M_BC + perp_BC_normalized * extension_length,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(perp_line_2), run_time=0.8)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), FadeOut(explain_1), run_time=0.3)
        self.play(FadeOut(ab_line), FadeOut(bc_line), run_time=0.2)
        
        # Step 3: 标记外心
        o_dot = Dot(self.circumcenter, color=self.COLOR_CIRCUMCENTER, radius=0.12)
        o_label = Text("O", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CIRCUMCENTER).next_to(o_dot, RIGHT, buff=0.15)
        o_label_2 = Text("外心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CIRCUMCENTER).next_to(o_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(o_dot, scale=0.5), run_time=0.5)
        self.play(Flash(o_dot, color=self.COLOR_CIRCUMCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(o_label), FadeIn(o_label_2), run_time=0.4)
        
        # Step 4: 绘制外接圆
        radius = np.linalg.norm(self.circumcenter - self.A)
        circumcircle = Circle(
            radius=radius,
            color=self.COLOR_CIRCUMCENTER,
            stroke_width=2
        ).move_to(self.circumcenter)
        
        self.play(Create(circumcircle), run_time=1.5)
        
        # 连线到顶点
        radii = VGroup(
            DashedLine(self.circumcenter, self.A, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.circumcenter, self.B, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.circumcenter, self.C, color=self.COLOR_AUXILIARY, dash_length=0.08)
        )
        
        self.play(Create(radii), run_time=0.8)
        
        property_text = Text(
            "到三顶点距离相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(perp_line_1),
            FadeOut(perp_line_2),
            FadeOut(m_ab_dot),
            FadeOut(m_ab_label),
            FadeOut(m_bc_dot),
            FadeOut(circumcircle),
            FadeOut(radii),
            FadeOut(property_text),
            FadeOut(o_label),
            FadeOut(o_label_2),
            run_time=0.6
        )
        
        # 保留外心点但变小
        self.o_small = Dot(self.circumcenter, color=self.COLOR_CIRCUMCENTER, radius=0.05, fill_opacity=0.5)
        self.play(Transform(o_dot, self.o_small), run_time=0.3)
        self.remove(o_dot)
        self.add(self.o_small)
    
    def show_incenter(self):
        """场景3: 内心 - 角平分线交点"""
        # 标题
        title = Text(
            "内心 Incenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_INCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条角平分线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: 角A的角平分线 - 精确计算
        # 单位方向向量
        vec_AB_unit = (self.B - self.A) / np.linalg.norm(self.B - self.A)
        vec_AC_unit = (self.C - self.A) / np.linalg.norm(self.C - self.A)
        bisector_A_dir = vec_AB_unit + vec_AC_unit
        bisector_A_dir_normalized = bisector_A_dir / np.linalg.norm(bisector_A_dir)
        
        # 计算角平分线与BC边的交点（精确）
        # 使用角平分线定理：交点D满足 BD/DC = AB/AC = c/b
        t = self.c / (self.b + self.c)
        D_point = self.B + t * (self.C - self.B)
        
        angle_bisector_1 = DashedLine(
            self.A,
            D_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        explain_1 = Text(
            "角平分线: 平分角度",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(angle_bisector_1), FadeIn(explain_1), run_time=1.0)
        
        # Step 2: 角B的角平分线 - 精确计算
        vec_BA_unit = (self.A - self.B) / np.linalg.norm(self.A - self.B)
        vec_BC_unit = (self.C - self.B) / np.linalg.norm(self.C - self.B)
        bisector_B_dir = vec_BA_unit + vec_BC_unit
        bisector_B_dir_normalized = bisector_B_dir / np.linalg.norm(bisector_B_dir)
        
        # 计算角平分线与CA边的交点（精确）
        # 使用角平分线定理：交点E满足 CE/EA = BC/BA = a/c
        t = self.a / (self.a + self.c)
        E_point = self.C + t * (self.A - self.C)
        
        angle_bisector_2 = DashedLine(
            self.B,
            E_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(angle_bisector_2), FadeOut(explain_1), run_time=0.8)
        
        # Step 3: 标记内心
        i_dot = Dot(self.incenter, color=self.COLOR_INCENTER, radius=0.12)
        i_label = Text("I", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_INCENTER).next_to(i_dot, RIGHT, buff=0.15)
        i_label_2 = Text("内心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_INCENTER).next_to(i_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(i_dot, scale=0.5), run_time=0.5)
        self.play(Flash(i_dot, color=self.COLOR_INCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(i_label), FadeIn(i_label_2), run_time=0.4)
        
        # Step 4: 绘制内切圆
        # 计算内切圆半径 (点到边的距离)
        inradius = np.abs(np.cross((self.B - self.incenter)[:2], (self.C - self.incenter)[:2])) / np.linalg.norm(self.B - self.C)
        
        incircle = Circle(
            radius=inradius,
            color=self.COLOR_INCENTER,
            stroke_width=2
        ).move_to(self.incenter)
        
        self.play(Create(incircle), run_time=1.5)
        
        # 到三边的垂线
        foot_BC = self.perpendicular_foot(self.incenter, self.B, self.C)
        foot_CA = self.perpendicular_foot(self.incenter, self.C, self.A)
        foot_AB = self.perpendicular_foot(self.incenter, self.A, self.B)
        
        perpendiculars = VGroup(
            DashedLine(self.incenter, foot_BC, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.incenter, foot_CA, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.incenter, foot_AB, color=self.COLOR_AUXILIARY, dash_length=0.08)
        )
        
        self.play(Create(perpendiculars), run_time=0.8)
        
        property_text = Text(
            "到三边距离相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(angle_bisector_1),
            FadeOut(angle_bisector_2),
            FadeOut(incircle),
            FadeOut(perpendiculars),
            FadeOut(property_text),
            FadeOut(i_label),
            FadeOut(i_label_2),
            run_time=0.6
        )
        
        # 保留内心点但变小
        self.i_small = Dot(self.incenter, color=self.COLOR_INCENTER, radius=0.05, fill_opacity=0.5)
        self.play(Transform(i_dot, self.i_small), run_time=0.3)
        self.remove(i_dot)
        self.add(self.i_small)
    
    def show_centroid(self):
        """场景4: 重心 - 中线交点"""
        # 标题
        title = Text(
            "重心 Centroid",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_CENTROID
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条中线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: 中线AM
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        m_bc_label = Text("M", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(m_bc_dot, DOWN, buff=0.1)
        
        self.play(FadeIn(m_bc_dot), FadeIn(m_bc_label), run_time=0.4)
        
        median_1 = Line(self.A, self.M_BC, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        explain_1 = Text(
            "中线: 顶点到对边中点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(median_1), FadeIn(explain_1), run_time=1.0)
        
        # Step 2: 中线BN
        m_ca_dot = Dot(self.M_CA, color=self.COLOR_AUXILIARY, radius=0.06)
        self.play(FadeIn(m_ca_dot), run_time=0.3)
        
        median_2 = Line(self.B, self.M_CA, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(median_2), FadeOut(explain_1), run_time=0.8)
        
        # Step 3: 标记重心
        g_dot = Dot(self.centroid, color=self.COLOR_CENTROID, radius=0.12)
        g_label = Text("G", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CENTROID).next_to(g_dot, RIGHT, buff=0.15)
        g_label_2 = Text("重心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CENTROID).next_to(g_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(g_dot, scale=0.5), run_time=0.5)
        self.play(Flash(g_dot, color=self.COLOR_CENTROID, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(g_label), FadeIn(g_label_2), run_time=0.4)
        
        # Step 4: 标注2:1比例
        # 计算分段点
        segment_AG = self.centroid - self.A
        point_2_3 = self.A + segment_AG * (2/3)
        
        brace_1 = Brace(Line(self.A, self.centroid), direction=LEFT, buff=0.1, color=YELLOW)
        brace_label_1 = Text("2", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_1, LEFT, buff=0.05)
        
        brace_2 = Brace(Line(self.centroid, self.M_BC), direction=LEFT, buff=0.1, color=YELLOW)
        brace_label_2 = Text("1", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_2, LEFT, buff=0.05)
        
        property_text = Text(
            "重心分中线为2:1",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        property_text_2 = Text(
            "物理重心 (平衡点)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(
            FadeIn(brace_1),
            FadeIn(brace_label_1),
            FadeIn(brace_2),
            FadeIn(brace_label_2),
            FadeIn(property_text),
            FadeIn(property_text_2),
            run_time=1.0
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(median_1),
            FadeOut(median_2),
            FadeOut(m_bc_dot),
            FadeOut(m_bc_label),
            FadeOut(m_ca_dot),
            FadeOut(brace_1),
            FadeOut(brace_label_1),
            FadeOut(brace_2),
            FadeOut(brace_label_2),
            FadeOut(property_text),
            FadeOut(property_text_2),
            FadeOut(g_label),
            FadeOut(g_label_2),
            run_time=0.6
        )
        
        # 保留重心点但变小
        self.g_small = Dot(self.centroid, color=self.COLOR_CENTROID, radius=0.05, fill_opacity=0.5)
        self.play(Transform(g_dot, self.g_small), run_time=0.3)
        self.remove(g_dot)
        self.add(self.g_small)
    
    def show_orthocenter(self):
        """场景5: 垂心 - 高线交点"""
        # 标题
        title = Text(
            "垂心 Orthocenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ORTHOCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条高线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: 从A到BC的高
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.5)
        
        foot_D = self.perpendicular_foot(self.A, self.B, self.C)
        altitude_1 = DashedLine(self.A, foot_D, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        # 垂直符号
        right_angle_1 = self.create_right_angle_mark(foot_D, self.A, self.B, size=0.15)
        
        explain_1 = Text(
            "高线: 顶点到对边的垂线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(altitude_1), FadeIn(right_angle_1), FadeIn(explain_1), run_time=1.0)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        
        # Step 2: 从B到CA的高
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ca_line), FadeOut(bc_line), run_time=0.5)
        
        foot_E = self.perpendicular_foot(self.B, self.C, self.A)
        altitude_2 = DashedLine(self.B, foot_E, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        right_angle_2 = self.create_right_angle_mark(foot_E, self.B, self.C, size=0.15)
        
        self.play(Create(altitude_2), FadeIn(right_angle_2), FadeOut(explain_1), run_time=0.8)
        self.play(ca_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ca_line), run_time=0.2)
        
        # Step 3: 标记垂心
        h_dot = Dot(self.orthocenter, color=self.COLOR_ORTHOCENTER, radius=0.12)
        h_label = Text("H", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_ORTHOCENTER).next_to(h_dot, RIGHT, buff=0.15)
        h_label_2 = Text("垂心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_ORTHOCENTER).next_to(h_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(h_dot, scale=0.5), run_time=0.5)
        self.play(Flash(h_dot, color=self.COLOR_ORTHOCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(h_label), FadeIn(h_label_2), run_time=0.4)
        
        # Step 4: 验证第三条高
        foot_F = self.perpendicular_foot(self.C, self.A, self.B)
        altitude_3 = DashedLine(self.C, foot_F, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        property_text = Text(
            "三条高线共点!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Create(altitude_3), FadeIn(property_text), run_time=1.0)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(altitude_1),
            FadeOut(altitude_2),
            FadeOut(altitude_3),
            FadeOut(right_angle_1),
            FadeOut(right_angle_2),
            FadeOut(property_text),
            FadeOut(h_label),
            FadeOut(h_label_2),
            run_time=0.6
        )
        
        # 保留垂心点但变小
        self.h_small = Dot(self.orthocenter, color=self.COLOR_ORTHOCENTER, radius=0.05, fill_opacity=0.5)
        self.play(Transform(h_dot, self.h_small), run_time=0.3)
        self.remove(h_dot)
        self.add(self.h_small)
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
        return square
    
    def show_excenter(self):
        """场景6: 旁心 - 外角平分线交点"""
        # 标题
        title = Text(
            "旁心 Excenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_EXCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "一条内角平分线与两条外角平分线的交点",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        note = Text(
            "每个三角形有三个旁心",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.1)
        
        self.play(Write(title), FadeIn(definition), FadeIn(note), run_time=1.0)
        
        # Step 1: 延长边并标注外角 - 精确计算延长线
        # 延长AB：从B沿BA反方向延长
        vec_BA = self.A - self.B
        vec_BA_normalized = vec_BA / np.linalg.norm(vec_BA)
        extend_length = 2.5
        
        extend_AB = DashedLine(
            self.B,
            self.B - vec_BA_normalized * extend_length,  # 沿BA反方向
            color=GRAY_B,
            dash_length=0.08
        )
        
        # 延长AC：从C沿CA反方向延长
        vec_CA = self.A - self.C
        vec_CA_normalized = vec_CA / np.linalg.norm(vec_CA)
        
        extend_AC = DashedLine(
            self.C,
            self.C - vec_CA_normalized * extend_length,  # 沿CA反方向
            color=GRAY_B,
            dash_length=0.08
        )
        
        explain_1 = Text(
            "外角: 延长边形成的角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(extend_AB), Create(extend_AC), FadeIn(explain_1), run_time=1.0)
        
        # Step 2: 外角B的平分线 - 精确计算
        # 外角B的两条边：BC和BA的延长线（即-AB方向）
        vec_BC_unit = (self.C - self.B) / np.linalg.norm(self.C - self.B)
        vec_BA_ext_unit = -(self.A - self.B) / np.linalg.norm(self.A - self.B)  # BA延长线方向
        
        # 外角平分线方向
        ext_bisector_B_dir = vec_BC_unit + vec_BA_ext_unit
        ext_bisector_B_dir_normalized = ext_bisector_B_dir / np.linalg.norm(ext_bisector_B_dir)
        
        # 计算延伸长度，确保能到达旁心
        distance_to_excenter = np.linalg.norm(self.excenter_A - self.B)
        extension = max(distance_to_excenter * 1.2, 3.0)
        
        ext_bisector_1 = DashedLine(
            self.B,
            self.B + ext_bisector_B_dir_normalized * extension,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(ext_bisector_1), FadeOut(explain_1), run_time=0.8)
        
        # Step 3: 外角C的平分线 - 精确计算
        vec_CB_unit = (self.B - self.C) / np.linalg.norm(self.B - self.C)
        vec_CA_ext_unit = -(self.A - self.C) / np.linalg.norm(self.A - self.C)  # CA延长线方向
        
        # 外角平分线方向
        ext_bisector_C_dir = vec_CB_unit + vec_CA_ext_unit
        ext_bisector_C_dir_normalized = ext_bisector_C_dir / np.linalg.norm(ext_bisector_C_dir)
        
        # 计算延伸长度
        distance_to_excenter = np.linalg.norm(self.excenter_A - self.C)
        extension = max(distance_to_excenter * 1.2, 3.0)
        
        ext_bisector_2 = DashedLine(
            self.C,
            self.C + ext_bisector_C_dir_normalized * extension,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(ext_bisector_2), run_time=0.8)
        
        # Step 4: 标记旁心
        j_dot = Dot(self.excenter_A, color=self.COLOR_EXCENTER, radius=0.12)
        j_label = Text("J", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_EXCENTER).next_to(j_dot, RIGHT, buff=0.15)
        j_label_2 = Text("旁心", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_EXCENTER).next_to(j_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(j_dot, scale=0.5), run_time=0.5)
        self.play(Flash(j_dot, color=self.COLOR_EXCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(j_label), FadeIn(j_label_2), run_time=0.4)
        
        # Step 5: 绘制旁切圆
        # 计算旁切圆半径
        exradius = np.abs(np.cross((self.B - self.excenter_A)[:2], (self.C - self.excenter_A)[:2])) / np.linalg.norm(self.B - self.C)
        
        excircle = Circle(
            radius=exradius,
            color=self.COLOR_EXCENTER,
            stroke_width=2
        ).move_to(self.excenter_A)
        
        self.play(Create(excircle), run_time=1.5)
        
        property_text = Text(
            "与一边及另两边延长线相切",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(note),
            FadeOut(extend_AB),
            FadeOut(extend_AC),
            FadeOut(ext_bisector_1),
            FadeOut(ext_bisector_2),
            FadeOut(excircle),
            FadeOut(property_text),
            FadeOut(j_label),
            FadeOut(j_label_2),
            run_time=0.6
        )
        
        # 保留旁心点但变小
        self.j_small = Dot(self.excenter_A, color=self.COLOR_EXCENTER, radius=0.05, fill_opacity=0.5)
        self.play(Transform(j_dot, self.j_small), run_time=0.3)
        self.remove(j_dot)
        self.add(self.j_small)
    
    def show_summary(self):
        """场景7: 五心汇总"""
        # 三角形移动并缩小
        triangle_small = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=2
        ).scale(0.6).move_to(UP * 3)
        
        # 重新计算缩放后的五心位置
        scale_factor = 0.6
        center_offset = UP * 3
        
        o_pos = (self.circumcenter - self.OFFSET) * scale_factor + center_offset
        i_pos = (self.incenter - self.OFFSET) * scale_factor + center_offset
        g_pos = (self.centroid - self.OFFSET) * scale_factor + center_offset
        h_pos = (self.orthocenter - self.OFFSET) * scale_factor + center_offset
        j_pos = (self.excenter_A - self.OFFSET) * scale_factor + center_offset
        
        self.play(
            Transform(self.triangle, triangle_small),
            self.o_small.animate.move_to(o_pos).scale(2).set_opacity(1),
            self.i_small.animate.move_to(i_pos).scale(2).set_opacity(1),
            self.g_small.animate.move_to(g_pos).scale(2).set_opacity(1),
            self.h_small.animate.move_to(h_pos).scale(2).set_opacity(1),
            self.j_small.animate.move_to(j_pos).scale(2).set_opacity(1),
            run_time=1.0
        )
        
        # 标注五心
        o_label = Text("O", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CIRCUMCENTER).next_to(self.o_small, RIGHT, buff=0.08)
        i_label = Text("I", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_INCENTER).next_to(self.i_small, LEFT, buff=0.08)
        g_label = Text("G", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_CENTROID).next_to(self.g_small, DOWN, buff=0.08)
        h_label = Text("H", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_ORTHOCENTER).next_to(self.h_small, UP, buff=0.08)
        j_label = Text("J", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_EXCENTER).next_to(self.j_small, LEFT, buff=0.08)
        
        self.play(
            Flash(self.o_small, color=self.COLOR_CIRCUMCENTER),
            Flash(self.i_small, color=self.COLOR_INCENTER),
            Flash(self.g_small, color=self.COLOR_CENTROID),
            Flash(self.h_small, color=self.COLOR_ORTHOCENTER),
            Flash(self.j_small, color=self.COLOR_EXCENTER),
            run_time=0.8
        )
        
        self.play(
            FadeIn(o_label),
            FadeIn(i_label),
            FadeIn(g_label),
            FadeIn(h_label),
            FadeIn(j_label),
            run_time=0.5
        )
        
        # 五心特性卡片
        cards = VGroup()
        
        # 外心卡片
        card_1 = self.create_center_card(
            "外心",
            "垂直平分线交点, 外接圆圆心",
            self.COLOR_CIRCUMCENTER,
            UP * 1
        )
        cards.add(card_1)
        
        # 内心卡片
        card_2 = self.create_center_card(
            "内心",
            "角平分线交点, 内切圆圆心",
            self.COLOR_INCENTER,
            ORIGIN
        )
        cards.add(card_2)
        
        # 重心卡片
        card_3 = self.create_center_card(
            "重心",
            "中线交点, 物理重心, 2:1比例",
            self.COLOR_CENTROID,
            DOWN * 1
        )
        cards.add(card_3)
        
        # 垂心卡片
        card_4 = self.create_center_card(
            "垂心",
            "高线交点",
            self.COLOR_ORTHOCENTER,
            DOWN * 2
        )
        cards.add(card_4)
        
        # 旁心卡片
        card_5 = self.create_center_card(
            "旁心",
            "外角平分线交点, 旁切圆圆心 (共3个)",
            self.COLOR_EXCENTER,
            DOWN * 3,
            font_size_content=16
        )
        cards.add(card_5)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight = Text(
            "掌握五心, 轻松解题!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.o_small),
            FadeOut(self.i_small),
            FadeOut(self.g_small),
            FadeOut(self.h_small),
            FadeOut(self.j_small),
            FadeOut(o_label),
            FadeOut(i_label),
            FadeOut(g_label),
            FadeOut(h_label),
            FadeOut(j_label),
            FadeOut(cards),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def create_center_card(self, title, content, color, position, font_size_content=18):
        """创建五心特性卡片"""
        # 图标圆
        icon = Circle(radius=0.2, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=font_size_content,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小三角形装饰
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        # 五心图标快闪
        icon_size = 0.3
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_CIRCUMCENTER, fill_opacity=0.8).shift(LEFT * 2),
            Circle(radius=icon_size, color=self.COLOR_INCENTER, fill_opacity=0.8).shift(LEFT * 1),
            Circle(radius=icon_size, color=self.COLOR_CENTROID, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_ORTHOCENTER, fill_opacity=0.8).shift(RIGHT * 1),
            Circle(radius=icon_size, color=self.COLOR_EXCENTER, fill_opacity=0.8).shift(RIGHT * 2)
        ).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql triangle_five_centers.py TriangleFiveCenters  # 快速预览
# manim -qh triangle_five_centers.py TriangleFiveCenters   # 高质量渲染
</good_template>

</manim_video_generation_prompt>