# Manim 几何绘图精确性约束指南

## 深度研究报告：如何避免几何动画中的低级错误

---

## 一、问题分析

### 1.1 常见低级错误类型

在 Manim 几何动画制作中，最常见的错误包括：

| 错误类型 | 具体表现 | 根本原因 |
|---------|---------|---------|
| **角度方向错误** | 角弧画在错误的一侧 | 未理解 `quadrant`、`other_angle` 参数 |
| **长度不一致** | 相等的边长度不同 | 使用臆想坐标而非精确计算 |
| **直线关系错误** | 垂直线不垂直、平行线不平行 | 未使用向量计算保证关系 |
| **点位置偏移** | 中点、交点、垂足位置不准 | 硬编码坐标而非动态计算 |
| **缩放后失真** | 缩放后几何关系被破坏 | 未同步更新派生坐标 |
| **元素重叠/溢出** | 标签重叠、图形超出边界 | 缺乏边界检查机制 |

### 1.2 错误产生的深层原因

```
臆想坐标 → 坐标不精确 → 几何关系破坏 → 动画效果错误
    ↓
缺乏验证 → 问题累积 → 调试困难 → 低效返工
```

---

## 二、核心约束法则

### 2.1 约束法则总览

#### 🔴 绝对禁止

1. **禁止臆想坐标** - 所有坐标必须通过 NumPy 精确计算
2. **禁止重复计算** - 几何数据统一初始化，场景间共享
3. **禁止硬编码派生点** - 中点、垂足、交点等必须用公式计算

#### 🟢 必须遵守

1. **所有几何元素必须有数学依据**
2. **必须建立几何验证机制**
3. **必须使用统一的坐标管理系统**

### 2.2 精确计算原则

```python
import numpy as np

# ❌ 错误：臆想坐标
midpoint = np.array([1.5, 2.3, 0])  # 凭感觉写的

# ✅ 正确：精确计算
midpoint = (point_A + point_B) / 2  # 数学公式
```

---

## 三、几何元素管理架构

### 3.1 统一初始化模式

```python
class GeometryScene(Scene):
    def construct(self):
        # ===== 阶段1：统一初始化所有几何数据 =====
        self.setup_geometry()
        
        # ===== 阶段2：执行各场景 =====
        self.scene_1_opening()
        self.scene_2_construction()
        # ...
    
    def setup_geometry(self):
        """
        【核心】所有几何元素的坐标在此统一计算和存储
        后续场景只引用，不重复计算
        """
        # ========== 基准参数 ==========
        self.SCALE = 0.85
        self.OFFSET = UP * 2.0
        
        # ========== 主要顶点（原始定义）==========
        self.A = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2, -1, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0, 2, 0]) * self.SCALE + self.OFFSET
        
        # ========== 派生点（精确计算）==========
        self.M_AB = (self.A + self.B) / 2  # AB中点
        self.M_BC = (self.B + self.C) / 2  # BC中点
        self.M_CA = (self.C + self.A) / 2  # CA中点
        
        # 垂心、外心、内心等
        self.centroid = (self.A + self.B + self.C) / 3
        self.circumcenter = self._calc_circumcenter(self.A, self.B, self.C)
        self.incenter = self._calc_incenter(self.A, self.B, self.C)
        
        # ========== 边长缓存 ==========
        self.AB = np.linalg.norm(self.B - self.A)
        self.BC = np.linalg.norm(self.C - self.B)
        self.CA = np.linalg.norm(self.A - self.C)
        
        # ========== 角度缓存 ==========
        self.angle_A = self._calc_angle(self.C, self.A, self.B)
        self.angle_B = self._calc_angle(self.A, self.B, self.C)
        self.angle_C = self._calc_angle(self.B, self.C, self.A)
        
        # ========== 验证 ==========
        self._verify_geometry()
```

### 3.2 精确计算函数库

```python
class GeometryCalculator:
    """几何计算工具类 - 所有计算必须使用此类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """计算中点"""
        return (P1 + P2) / 2
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        """
        计算点到直线的垂足
        参数:
            point: 要投影的点
            line_start, line_end: 定义直线的两点
        返回:
            垂足坐标
        """
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
    @staticmethod
    def line_intersection(P1, D1, P2, D2):
        """
        计算两直线交点
        直线1: P1 + t*D1
        直线2: P2 + s*D2
        """
        A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        
        if np.abs(np.linalg.det(A)) < 1e-10:
            return None  # 平行线，无交点
        
        params = np.linalg.solve(A, b)
        return np.array([*(P1[:2] + params[0] * D1[:2]), 0])
    
    @staticmethod
    def circumcenter(A, B, C):
        """
        计算三角形外心
        外心到三顶点距离相等
        """
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        
        D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
        
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        
        return np.array([ux, uy, 0])
    
    @staticmethod
    def incenter(A, B, C):
        """
        计算三角形内心
        使用加权平均公式
        """
        a = np.linalg.norm(B - C)  # BC边长
        b = np.linalg.norm(C - A)  # CA边长
        c = np.linalg.norm(A - B)  # AB边长
        return (a*A + b*B + c*C) / (a + b + c)
    
    @staticmethod
    def orthocenter(A, B, C):
        """
        计算三角形垂心
        H = A + B + C - 2*O (O为外心)
        """
        O = GeometryCalculator.circumcenter(A, B, C)
        return A + B + C - 2*O
    
    @staticmethod
    def angle_between_vectors(V1, V2):
        """
        计算两向量夹角（弧度）
        """
        cos_angle = np.dot(V1, V2) / (np.linalg.norm(V1) * np.linalg.norm(V2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 数值稳定性
        return np.arccos(cos_angle)
    
    @staticmethod
    def angle_at_vertex(A, B, C):
        """
        计算∠ABC的角度（弧度）
        B是顶点
        """
        BA = A - B
        BC = C - B
        return GeometryCalculator.angle_between_vectors(BA, BC)
    
    @staticmethod
    def distance_point_to_line(point, line_start, line_end):
        """计算点到直线的距离"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        cross_product = np.cross(point_vec[:2], line_vec[:2])
        return np.abs(cross_product) / np.linalg.norm(line_vec)
    
    @staticmethod
    def perpendicular_bisector(P1, P2):
        """
        计算线段P1P2的垂直平分线
        返回: (中点, 垂直方向向量)
        """
        midpoint = (P1 + P2) / 2
        segment = P2 - P1
        perpendicular = np.array([-segment[1], segment[0], 0])
        return midpoint, perpendicular
    
    @staticmethod
    def reflection_point(point, line_start, line_end):
        """计算点关于直线的对称点"""
        foot = GeometryCalculator.foot_of_perpendicular(point, line_start, line_end)
        return 2 * foot - point
```

---

## 四、Manim 0.19.2 角度与方向约束

### 4.1 Angle 类详解

Manim 的 `Angle` 类是几何动画中最容易出错的部分。

```python
Angle(
    line1,              # 第一条线
    line2,              # 第二条线
    radius=None,        # 角弧半径
    quadrant=(1, 1),    # 象限选择
    other_angle=False,  # 是否使用另一个角
    dot=False,          # 是否显示点（常用于直角）
    elbow=False         # 是否使用直角符号
)
```

#### quadrant 参数详解

`quadrant` 是一个二元组 `(a, b)`，控制角弧的锚点位置：
- `a = 1`: 锚定在 line1 的 **终点** 侧
- `a = -1`: 锚定在 line1 的 **起点** 侧
- `b = 1`: 锚定在 line2 的 **终点** 侧
- `b = -1`: 锚定在 line2 的 **起点** 侧

```python
# 可能的组合
quadrant=(1, 1)    # 默认，两线的终点侧
quadrant=(-1, 1)   # line1起点侧，line2终点侧
quadrant=(1, -1)   # line1终点侧，line2起点侧
quadrant=(-1, -1)  # 两线的起点侧
```

#### other_angle 参数详解

- `other_angle=False`（默认）: 从 line1 到 line2 **逆时针**方向的角
- `other_angle=True`: 另一个角（补角方向）

```python
# 示例：确保角弧在正确位置
def create_angle_correctly(self, vertex, point1, point2, radius=0.5):
    """
    创建从 point1 到 point2 的角弧（以 vertex 为顶点）
    """
    # 创建从顶点出发的线段
    line1 = Line(vertex, point1)
    line2 = Line(vertex, point2)
    
    # 计算向量夹角判断方向
    v1 = point1 - vertex
    v2 = point2 - vertex
    cross_z = v1[0] * v2[1] - v1[1] * v2[0]  # 叉积的z分量
    
    # cross_z > 0 表示从v1到v2是逆时针
    # cross_z < 0 表示从v1到v2是顺时针
    
    if cross_z > 0:
        # 逆时针，使用默认
        angle = Angle(line1, line2, radius=radius, other_angle=False)
    else:
        # 顺时针，需要使用 other_angle
        angle = Angle(line1, line2, radius=radius, other_angle=True)
    
    return angle
```

### 4.2 使用 Angle.from_three_points（推荐）

```python
# ✅ 推荐方法：直接使用三点
angle = Angle.from_three_points(
    point_on_first_ray,   # 第一条射线上的点
    vertex,                # 顶点
    point_on_second_ray,  # 第二条射线上的点
    radius=0.5,
    quadrant=(1, 1),      # 仍需根据情况调整
    other_angle=False
)
```

### 4.3 直角标记

```python
# 方法1：使用 RightAngle
right_angle = RightAngle(
    line1, line2,
    length=0.3,           # 直角符号边长
    quadrant=(1, 1)       # 同样需要正确设置
)

# 方法2：使用 Angle 的 elbow 参数
angle = Angle(line1, line2, radius=0.3, elbow=True)

# 方法3：手动创建 Elbow
elbow = Elbow(width=0.3, angle=0).move_to(vertex)
```

### 4.4 弧的方向控制

```python
# Arc 类：正角度逆时针，负角度顺时针
arc_ccw = Arc(radius=1, start_angle=0, angle=PI/2)        # 逆时针90°
arc_cw = Arc(radius=1, start_angle=PI/2, angle=-PI/2)     # 顺时针90°

# ArcBetweenPoints：控制弧的方向
# 正radius：逆时针（弧在从start到end方向的左侧）
# 负radius：顺时针（弧在从start到end方向的右侧）
arc = ArcBetweenPoints(start, end, radius=1)    # 逆时针
arc = ArcBetweenPoints(start, end, radius=-1)   # 顺时针
```

---

## 五、长度与比例约束

### 5.1 确保长度一致性

```python
class LengthConsistencyScene(Scene):
    def setup_geometry(self):
        # 定义基准长度
        self.UNIT = 1.0
        
        # 使用基准长度定义所有相关元素
        self.side_length = 2 * self.UNIT
        
        # ❌ 错误：不同位置使用不同值
        # line1 = Line(ORIGIN, 2*RIGHT)
        # line2 = Line(UP, UP + 2.1*RIGHT)  # 不一致！
        
        # ✅ 正确：使用统一变量
        self.A = ORIGIN
        self.B = self.A + self.side_length * RIGHT
        self.C = self.B + self.side_length * UP
        self.D = self.A + self.side_length * UP
    
    def verify_lengths(self):
        """验证长度约束"""
        AB = np.linalg.norm(self.B - self.A)
        BC = np.linalg.norm(self.C - self.B)
        CD = np.linalg.norm(self.D - self.C)
        DA = np.linalg.norm(self.A - self.D)
        
        epsilon = 1e-10
        assert abs(AB - self.side_length) < epsilon, f"AB长度错误: {AB}"
        assert abs(BC - self.side_length) < epsilon, f"BC长度错误: {BC}"
        assert abs(CD - self.side_length) < epsilon, f"CD长度错误: {CD}"
        assert abs(DA - self.side_length) < epsilon, f"DA长度错误: {DA}"
        print("✓ 长度验证通过")
```

### 5.2 比例关系保持

```python
def maintain_ratio(self, point_A, point_B, ratio):
    """
    在AB上找到点P，使得 AP:PB = ratio:(1-ratio)
    """
    return point_A + ratio * (point_B - point_A)

# 示例：三等分点
P1 = maintain_ratio(A, B, 1/3)  # AP1:P1B = 1:2
P2 = maintain_ratio(A, B, 2/3)  # AP2:P2B = 2:1
```

---

## 六、位置关系约束

### 6.1 垂直关系

```python
def ensure_perpendicular(self, line1_start, line1_end, line2_start, line2_end):
    """
    验证两线段垂直
    """
    v1 = line1_end - line1_start
    v2 = line2_end - line2_start
    
    dot_product = np.dot(v1[:2], v2[:2])
    
    if abs(dot_product) > 1e-10:
        raise ValueError(f"线段不垂直！点积 = {dot_product}")
    
    return True

def create_perpendicular_line(self, point, line_start, line_end, length=2):
    """
    过一点创建与给定直线垂直的线段
    """
    # 计算垂足
    foot = GeometryCalculator.foot_of_perpendicular(point, line_start, line_end)
    
    # 垂直方向
    line_vec = line_end - line_start
    perp_vec = np.array([-line_vec[1], line_vec[0], 0])
    perp_vec = perp_vec / np.linalg.norm(perp_vec)  # 单位化
    
    # 创建垂直线
    return Line(foot - length/2 * perp_vec, foot + length/2 * perp_vec)
```

### 6.2 平行关系

```python
def create_parallel_line(self, point, line_start, line_end, length=2):
    """
    过一点创建与给定直线平行的线段
    """
    direction = line_end - line_start
    direction = direction / np.linalg.norm(direction)  # 单位化
    
    return Line(point - length/2 * direction, point + length/2 * direction)

def verify_parallel(self, line1_vec, line2_vec):
    """验证两向量平行"""
    cross = np.cross(line1_vec[:2], line2_vec[:2])
    return abs(cross) < 1e-10
```

### 6.3 共线/共点验证

```python
def are_collinear(self, P1, P2, P3):
    """
    验证三点共线
    使用面积法：共线时三角形面积为0
    """
    area = 0.5 * abs(
        P1[0]*(P2[1]-P3[1]) + 
        P2[0]*(P3[1]-P1[1]) + 
        P3[0]*(P1[1]-P2[1])
    )
    return area < 1e-10

def are_concurrent(self, line1, line2, line3):
    """
    验证三线共点
    line格式: (point_on_line, direction_vector)
    """
    # 计算line1和line2的交点
    intersection = GeometryCalculator.line_intersection(
        line1[0], line1[1],
        line2[0], line2[1]
    )
    
    if intersection is None:
        return False  # line1和line2平行
    
    # 检查line3是否过此点
    # 点到直线距离
    dist = GeometryCalculator.distance_point_to_line(
        intersection,
        line3[0],
        line3[0] + line3[1]
    )
    
    return dist < 1e-10
```

---

## 七、几何验证机制

### 7.1 完整验证函数

```python
def verify_geometry(self):
    """
    统一几何验证函数
    在setup_geometry()末尾调用
    """
    epsilon = 1e-6
    errors = []
    
    # ===== 1. 验证外心性质 =====
    dist_A = np.linalg.norm(self.circumcenter - self.A)
    dist_B = np.linalg.norm(self.circumcenter - self.B)
    dist_C = np.linalg.norm(self.circumcenter - self.C)
    
    if abs(dist_A - dist_B) > epsilon:
        errors.append(f"外心错误: OA={dist_A:.6f}, OB={dist_B:.6f}")
    if abs(dist_B - dist_C) > epsilon:
        errors.append(f"外心错误: OB={dist_B:.6f}, OC={dist_C:.6f}")
    
    # ===== 2. 验证内心性质 =====
    dist_to_AB = GeometryCalculator.distance_point_to_line(self.incenter, self.A, self.B)
    dist_to_BC = GeometryCalculator.distance_point_to_line(self.incenter, self.B, self.C)
    dist_to_CA = GeometryCalculator.distance_point_to_line(self.incenter, self.C, self.A)
    
    if abs(dist_to_AB - dist_to_BC) > epsilon:
        errors.append(f"内心错误: 到AB={dist_to_AB:.6f}, 到BC={dist_to_BC:.6f}")
    
    # ===== 3. 验证角度和 =====
    angle_sum = self.angle_A + self.angle_B + self.angle_C
    if abs(angle_sum - np.pi) > epsilon:
        errors.append(f"角度和错误: {np.degrees(angle_sum):.2f}° ≠ 180°")
    
    # ===== 4. 验证中点性质 =====
    AM_AB = np.linalg.norm(self.M_AB - self.A)
    M_AB_B = np.linalg.norm(self.B - self.M_AB)
    if abs(AM_AB - M_AB_B) > epsilon:
        errors.append(f"中点错误: AM={AM_AB:.6f}, MB={M_AB_B:.6f}")
    
    # ===== 输出结果 =====
    if errors:
        print("❌ 几何验证失败:")
        for e in errors:
            print(f"  - {e}")
        raise ValueError("几何验证失败！")
    else:
        print("✓ 几何验证通过")
```

### 7.2 实时验证装饰器

```python
def verify_geometry_constraint(constraint_type):
    """
    装饰器：在方法执行后自动验证几何约束
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            
            if constraint_type == "perpendicular":
                # 验证垂直关系
                self._verify_perpendicular_constraints()
            elif constraint_type == "parallel":
                # 验证平行关系
                self._verify_parallel_constraints()
            elif constraint_type == "length":
                # 验证长度关系
                self._verify_length_constraints()
            
            return result
        return wrapper
    return decorator
```

---

## 八、缩放与变换时的坐标同步

### 8.1 问题描述

```python
# ❌ 错误：缩放后派生点不同步
triangle = Polygon(self.A, self.B, self.C)
triangle.scale(0.5)
dot.move_to(self.circumcenter)  # 位置错误！circumcenter 未随之缩放
```

### 8.2 正确做法

```python
# ✅ 方法1：重新计算派生点
def scale_with_sync(self, factor, about_point=None):
    """缩放并同步所有几何数据"""
    if about_point is None:
        about_point = self.centroid
    
    # 缩放所有主顶点
    self.A = about_point + (self.A - about_point) * factor
    self.B = about_point + (self.B - about_point) * factor
    self.C = about_point + (self.C - about_point) * factor
    
    # 重新计算所有派生点
    self._recalculate_derived_points()

# ✅ 方法2：使用 always_redraw
circumcenter_dot = always_redraw(
    lambda: Dot(GeometryCalculator.circumcenter(
        self.triangle.get_vertices()[0],
        self.triangle.get_vertices()[1],
        self.triangle.get_vertices()[2]
    ))
)
```

---

## 九、Manim 0.19.2 特定约束与已知问题

### 9.1 参数约束表

| 类 | 参数 | 约束说明 |
|---|------|---------|
| `Sector` | `radius` | ✅ 允许 |
| `Sector` | `inner_radius`, `outer_radius` | ❌ 禁止（0.19已移除） |
| `AnnularSector` | `inner_radius`, `outer_radius` | ✅ 允许 |
| `Rectangle` | `corner_radius` | ❌ 禁止 |
| `RoundedRectangle` | `corner_radius` | ✅ 允许 |
| `Arrow.scale()` | `scale_tips` | ⚠️ 保留箭头尖端大小不变时直接用 |
| `MathTex` | 中文字符 | ❌ 禁止 |
| `Tex` + ctex模板 | 中文字符 | ✅ 允许 |

### 9.2 LaTeX 约束

```python
# ❌ 错误：MathTex 中使用中文
MathTex(r"\text{三角形}")  # Unicode Error!

# ✅ 正确：中文用 Text，数学用 MathTex 分离
chinese = Text("三角形", font="Noto Sans CJK SC")
formula = MathTex(r"\triangle ABC")
VGroup(chinese, formula).arrange(RIGHT)

# ✅ 正确：使用 ctex 模板
from manim import TexTemplateLibrary
tex = Tex(r"三角形 $\triangle ABC$", tex_template=TexTemplateLibrary.ctex)
```

### 9.3 度数符号约束

```python
# ❌ 错误：直接使用 ° 符号
MathTex(r"90°")  # Error!

# ✅ 正确：使用 LaTeX 命令
MathTex(r"90^\circ")
MathTex(r"90^{\circ}")
```

### 9.4 LaTeX 分组约束

```python
# ❌ 错误：双花括号导致解析错误
MathTex(r"{{a} \over {b}}")  # Error!

# ✅ 正确：使用 \frac
MathTex(r"\frac{a}{b}")

# ✅ 正确：如果需要隔离子公式
MathTex(r"{{ a }} + {{ b }}")  # 每组内容独立
```

---

## 十、边界检查与防溢出

### 10.1 场景边界

```python
class BoundaryAwareScene(Scene):
    # Manim 默认场景：8 (高) × 14 (宽)
    SAFE_MARGIN = 0.5
    MAX_X = 7.0 - SAFE_MARGIN
    MAX_Y = 4.0 - SAFE_MARGIN
    MIN_X = -MAX_X
    MIN_Y = -MAX_Y
    
    def clamp_position(self, position):
        """将位置限制在安全边界内"""
        x = np.clip(position[0], self.MIN_X, self.MAX_X)
        y = np.clip(position[1], self.MIN_Y, self.MAX_Y)
        return np.array([x, y, 0])
    
    def is_within_bounds(self, mobject):
        """检查物体是否在边界内"""
        bbox = mobject.get_bounding_box()
        return (
            bbox[0][0] > self.MIN_X and
            bbox[1][0] < self.MAX_X and
            bbox[0][1] > self.MIN_Y and
            bbox[1][1] < self.MAX_Y
        )
```

### 10.2 标签防重叠

```python
def place_label_safely(self, mobject, label, preferred_direction=UR, buff=0.2):
    """
    智能放置标签，避免重叠和溢出
    """
    directions = [preferred_direction, UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR]
    
    for direction in directions:
        label.next_to(mobject, direction, buff=buff)
        
        # 检查是否在边界内
        if self.is_within_bounds(label):
            # 检查是否与其他标签重叠
            if not self._check_overlap_with_existing_labels(label):
                return label
    
    # 所有方向都不行，使用缩小版本
    label.scale(0.7)
    return label.next_to(mobject, preferred_direction, buff=buff)
```

---

## 十一、完整示例：精确几何动画

```python
from manim import *
import numpy as np

class PreciseGeometryDemo(Scene):
    """
    展示如何使用约束法则创建精确的几何动画
    """
    
    def construct(self):
        self.setup_geometry()
        self.create_objects()
        self.animate_construction()
    
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # 基准参数
        self.SCALE = 1.5
        self.OFFSET = DOWN * 0.5
        
        # 定义三角形顶点
        self.A = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2, -1, 0]) * self.SCALE + self.OFFSET  
        self.C = np.array([0, 1.5, 0]) * self.SCALE + self.OFFSET
        
        # 精确计算派生点
        self.calc = GeometryCalculator
        self.circumcenter = self.calc.circumcenter(self.A, self.B, self.C)
        self.circumradius = np.linalg.norm(self.A - self.circumcenter)
        
        # 验证
        self._verify()
    
    def _verify(self):
        """验证几何关系"""
        eps = 1e-10
        r_A = np.linalg.norm(self.A - self.circumcenter)
        r_B = np.linalg.norm(self.B - self.circumcenter)
        r_C = np.linalg.norm(self.C - self.circumcenter)
        
        assert abs(r_A - r_B) < eps and abs(r_B - r_C) < eps, "外心计算错误"
        print("✓ 几何验证通过")
    
    def create_objects(self):
        """创建所有几何对象"""
        # 三角形
        self.triangle = Polygon(self.A, self.B, self.C, color=BLUE)
        
        # 外接圆
        self.circumcircle = Circle(
            radius=self.circumradius, 
            color=YELLOW
        ).move_to(self.circumcenter)
        
        # 外心
        self.O_dot = Dot(self.circumcenter, color=RED)
        self.O_label = MathTex("O").next_to(self.O_dot, UP, buff=0.1)
        
        # 顶点标签
        self.A_label = MathTex("A").next_to(self.A, DL, buff=0.1)
        self.B_label = MathTex("B").next_to(self.B, DR, buff=0.1)
        self.C_label = MathTex("C").next_to(self.C, UP, buff=0.1)
    
    def animate_construction(self):
        """执行动画"""
        # 1. 绘制三角形
        self.play(Create(self.triangle), run_time=2)
        self.play(
            Write(self.A_label),
            Write(self.B_label),
            Write(self.C_label)
        )
        self.wait()
        
        # 2. 添加外心和外接圆
        self.play(
            FadeIn(self.O_dot),
            Write(self.O_label)
        )
        self.play(Create(self.circumcircle), run_time=2)
        self.wait(2)


# 几何计算工具类（简化版）
class GeometryCalculator:
    @staticmethod
    def circumcenter(A, B, C):
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        return np.array([ux, uy, 0])
```

---

## 十二、总结检查清单

### 在开始编写几何动画前

- [ ] 是否定义了 `setup_geometry()` 方法？
- [ ] 所有坐标是否通过精确计算获得？
- [ ] 是否有验证函数检查几何关系？

### 在创建角度时

- [ ] 是否正确设置了 `quadrant` 参数？
- [ ] 是否根据需要使用了 `other_angle`？
- [ ] 直角是否使用了 `RightAngle` 或 `elbow=True`？

### 在处理长度时

- [ ] 相等的边是否使用同一变量？
- [ ] 是否有长度验证？

### 在处理位置关系时

- [ ] 垂直关系是否通过点积验证？
- [ ] 平行关系是否通过叉积验证？
- [ ] 共线/共点是否有验证？

### 在使用 LaTeX 时

- [ ] 中文是否使用 `Text()` 或 ctex 模板？
- [ ] 度数是否使用 `^\circ`？
- [ ] 是否使用原始字符串 `r"..."`？

### 在缩放/变换后

- [ ] 派生点是否同步更新？
- [ ] 是否使用了 `always_redraw` 保持同步？

---

*本文档基于 Manim Community v0.19.2 编写*
*最后更新: 2026-01-31*