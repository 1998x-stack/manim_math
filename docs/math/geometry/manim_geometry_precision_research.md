# Manim 几何精度与约束法则完全指南

> **核心原则：所有几何元素必须通过 NumPy 精确计算，严禁臆想坐标！**

---

## 📋 目录

1. [常见低级错误分类与根因](#1-常见低级错误分类与根因)
2. [精确几何计算框架](#2-精确几何计算框架)
3. [角度系统深度解析](#3-角度系统深度解析)
4. [长度与比例约束](#4-长度与比例约束)
5. [位置关系验证机制](#5-位置关系验证机制)
6. [数值精度与浮点误差处理](#6-数值精度与浮点误差处理)
7. [Manim 0.19.2 API 约束表](#7-manim-0192-api-约束表)
8. [工业级场景结构模板](#8-工业级场景结构模板)
9. [调试与验证清单](#9-调试与验证清单)

---

## 1. 常见低级错误分类与根因

### 1.1 角度方向错误

**症状**: 角度弧画在了错误的一侧，或角度看起来不正确

**根因分析**:
- Manim 的 `Angle` 类默认从 `line1` 逆时针画弧到 `line2`
- `quadrant` 参数控制锚点选择，但经常被误用
- `other_angle=True/False` 切换互补角

**解决方案**:

```python
def create_correct_angle_arc(vertex, point_a, point_b, radius=0.5):
    """
    创建正确方向的角度弧
    角度从 vertex→point_a 到 vertex→point_b
    """
    line1 = Line(vertex, point_a)
    line2 = Line(vertex, point_b)
    
    # 计算叉积确定方向
    v1 = np.array(point_a) - np.array(vertex)
    v2 = np.array(point_b) - np.array(vertex)
    cross_z = v1[0] * v2[1] - v1[1] * v2[0]
    
    # cross_z > 0: 逆时针 (默认)
    # cross_z < 0: 顺时针 (需要 other_angle=True)
    return Angle(line1, line2, radius=radius, other_angle=(cross_z < 0))

# 推荐方法：使用 from_three_points
angle = Angle.from_three_points(A, B, C, radius=0.5)  # 顶点在 B
```

### 1.2 长度不一致

**症状**: 声称等长的线段视觉上明显不等

**根因分析**:
- 直接使用臆想的坐标值
- 缩放操作后未重新计算派生点
- 混用不同坐标系

**解决方案**:

```python
# ❌ 错误：臆想坐标
A = np.array([0, 0, 0])
B = np.array([3, 0, 0])  # 假设长度为 3
C = np.array([1.5, 2.6, 0])  # 臆想的等腰三角形顶点

# ✅ 正确：数学计算
def create_isosceles_triangle(base_length, leg_length, offset=ORIGIN):
    """创建等腰三角形，确保边长精确"""
    A = np.array([-base_length/2, 0, 0])
    B = np.array([base_length/2, 0, 0])
    # 使用勾股定理计算高度
    height = np.sqrt(leg_length**2 - (base_length/2)**2)
    C = np.array([0, height, 0])
    return A + offset, B + offset, C + offset

# 验证
A, B, C = create_isosceles_triangle(4, 3)
assert np.isclose(np.linalg.norm(A - C), np.linalg.norm(B - C)), "边长不等!"
```

### 1.3 点位置偏移

**症状**: 点不在预期位置（如中点、垂足、交点）

**根因分析**:
- 中点计算使用了错误的公式
- 垂足计算时参数方程理解错误
- 缩放/旋转后未同步更新

**解决方案**:

```python
class GeometryPrecision:
    """精确几何计算工具类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """线段中点"""
        return (np.array(P1) + np.array(P2)) / 2
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        """
        点到直线的垂足
        原理：P' = A + t*(B-A), 其中 t = (P-A)·(B-A) / |B-A|²
        """
        P = np.array(point)
        A = np.array(line_start)
        B = np.array(line_end)
        AB = B - A
        t = np.dot(P - A, AB) / np.dot(AB, AB)
        return A + t * AB
    
    @staticmethod
    def line_intersection(P1, D1, P2, D2):
        """
        两直线交点
        直线1: P1 + t*D1
        直线2: P2 + s*D2
        """
        # 构建方程组: [D1 | -D2] * [t, s]^T = P2 - P1
        A = np.array([[D1[0], -D2[0]], 
                      [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        
        det = np.linalg.det(A)
        if np.abs(det) < 1e-10:
            return None  # 平行线
        
        params = np.linalg.solve(A, b)
        t = params[0]
        return np.array([P1[0] + t*D1[0], P1[1] + t*D1[1], 0])
```

### 1.4 直线关系错误

**症状**: 应该平行的线不平行，应该垂直的线不垂直

**根因分析**:
- 方向向量计算错误
- 未考虑 3D 向量的 z 分量
- 数值精度问题导致验证失败

**解决方案**:

```python
class RelationshipVerifier:
    """几何关系验证器"""
    
    EPSILON = 1e-8  # 数值精度阈值
    
    @classmethod
    def are_parallel(cls, v1, v2):
        """
        检查两向量是否平行
        原理：平行向量叉积为零
        """
        cross = np.cross(v1[:2], v2[:2])
        return np.abs(cross) < cls.EPSILON
    
    @classmethod
    def are_perpendicular(cls, v1, v2):
        """
        检查两向量是否垂直
        原理：垂直向量点积为零
        """
        dot = np.dot(v1[:2], v2[:2])
        return np.abs(dot) < cls.EPSILON
    
    @classmethod
    def are_collinear(cls, P1, P2, P3):
        """
        检查三点是否共线
        原理：三角形面积为零
        """
        area = 0.5 * np.abs(
            P1[0]*(P2[1]-P3[1]) + 
            P2[0]*(P3[1]-P1[1]) + 
            P3[0]*(P1[1]-P2[1])
        )
        return area < cls.EPSILON
    
    @classmethod
    def is_on_line(cls, point, line_start, line_end):
        """检查点是否在直线上"""
        return cls.are_collinear(point, line_start, line_end)
    
    @classmethod
    def is_on_segment(cls, point, seg_start, seg_end):
        """检查点是否在线段上（含端点）"""
        if not cls.is_on_line(point, seg_start, seg_end):
            return False
        # 检查是否在线段范围内
        t = np.dot(point - seg_start, seg_end - seg_start) / \
            np.dot(seg_end - seg_start, seg_end - seg_start)
        return -cls.EPSILON <= t <= 1 + cls.EPSILON
```

---

## 2. 精确几何计算框架

### 2.1 全局几何数据管理

```python
class GeometryManagedScene(Scene):
    """几何数据全局管理的场景基类"""
    
    def construct(self):
        # 1. 初始化几何数据（执行一次）
        self._setup_geometry()
        
        # 2. 验证几何正确性
        self._verify_geometry()
        
        # 3. 创建 Mobject
        self._create_mobjects()
        
        # 4. 执行动画
        self._animate()
    
    def _setup_geometry(self):
        """
        【核心】所有几何数据在此初始化
        后续只引用，不重复计算
        """
        # === 基准参数 ===
        self.SCALE = 1.0
        self.OFFSET = np.array([0, 0, 0])
        
        # === 主顶点（手动定义或计算） ===
        self.A = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2, -1, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0, 2, 0]) * self.SCALE + self.OFFSET
        
        # === 派生点（必须计算，不可臆想）===
        self.M_AB = GeometryPrecision.midpoint(self.A, self.B)
        self.M_BC = GeometryPrecision.midpoint(self.B, self.C)
        self.M_CA = GeometryPrecision.midpoint(self.C, self.A)
        
        # === 特殊点 ===
        self.circumcenter = self._calc_circumcenter()
        self.incenter = self._calc_incenter()
        self.centroid = self._calc_centroid()
        self.orthocenter = self._calc_orthocenter()
        
        # === 边长缓存（避免重复计算）===
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # === 角度缓存（弧度）===
        self.angle_A = self._calc_angle_at(self.A, self.B, self.C)
        self.angle_B = self._calc_angle_at(self.B, self.C, self.A)
        self.angle_C = self._calc_angle_at(self.C, self.A, self.B)
    
    def _calc_circumcenter(self):
        """外心：到三顶点距离相等"""
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]
        D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        return np.array([ux, uy, 0])
    
    def _calc_incenter(self):
        """内心：到三边距离相等"""
        return (self.a*self.A + self.b*self.B + self.c*self.C) / (self.a + self.b + self.c)
    
    def _calc_centroid(self):
        """重心：三中线交点"""
        return (self.A + self.B + self.C) / 3
    
    def _calc_orthocenter(self):
        """垂心：三高交点"""
        return self.A + self.B + self.C - 2 * self.circumcenter
    
    def _calc_angle_at(self, vertex, p1, p2):
        """计算顶点处的角度（弧度）"""
        v1 = p1 - vertex
        v2 = p2 - vertex
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(cos_angle, -1.0, 1.0))
```

### 2.2 高级几何计算函数

```python
class AdvancedGeometry:
    """高级几何计算"""
    
    @staticmethod
    def circle_intersection(c1, r1, c2, r2):
        """
        两圆交点
        返回交点列表（0、1或2个点）
        """
        d = np.linalg.norm(np.array(c2[:2]) - np.array(c1[:2]))
        
        # 无交点情况
        if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
            return []
        
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h_sq = r1**2 - a**2
        
        if h_sq < 0:
            return []
        
        h = np.sqrt(h_sq)
        
        # 中点和方向
        direction = (np.array(c2[:2]) - np.array(c1[:2])) / d
        perpendicular = np.array([-direction[1], direction[0]])
        base = np.array(c1[:2]) + a * direction
        
        if h < 1e-10:  # 相切
            return [np.array([*base, 0])]
        
        return [
            np.array([*(base + h * perpendicular), 0]),
            np.array([*(base - h * perpendicular), 0])
        ]
    
    @staticmethod
    def line_circle_intersection(line_start, line_end, center, radius):
        """
        直线与圆的交点
        注意：这是无限直线，不是线段
        """
        A = np.array(line_start[:2])
        B = np.array(line_end[:2])
        C = np.array(center[:2])
        
        d = B - A  # 方向向量
        f = A - C  # 从圆心到直线起点
        
        a = np.dot(d, d)
        b = 2 * np.dot(f, d)
        c = np.dot(f, f) - radius**2
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return []
        
        discriminant = np.sqrt(discriminant)
        t1 = (-b - discriminant) / (2*a)
        t2 = (-b + discriminant) / (2*a)
        
        points = []
        for t in [t1, t2]:
            point = A + t * d
            points.append(np.array([*point, 0]))
        
        if abs(t1 - t2) < 1e-10:
            return [points[0]]  # 相切
        
        return points
    
    @staticmethod
    def tangent_from_external_point(external_point, center, radius):
        """
        从外部点到圆的切点
        """
        P = np.array(external_point[:2])
        C = np.array(center[:2])
        
        d = np.linalg.norm(P - C)
        
        if d < radius:
            return []  # 点在圆内
        
        if abs(d - radius) < 1e-10:
            return [np.array([*P, 0])]  # 点在圆上
        
        # 切线长度
        tangent_length = np.sqrt(d**2 - radius**2)
        
        # 切点角度
        alpha = np.arccos(radius / d)
        beta = np.arctan2(P[1] - C[1], P[0] - C[0])
        
        angles = [beta + alpha, beta - alpha]
        return [
            np.array([C[0] + radius * np.cos(a), C[1] + radius * np.sin(a), 0])
            for a in angles
        ]
    
    @staticmethod
    def angle_bisector_intersection(vertex, p1, p2):
        """
        角平分线与对边的交点
        vertex: 角的顶点
        p1, p2: 角的两条边上的点
        返回角平分线的方向向量和与对边的交点
        """
        v1 = np.array(p1) - np.array(vertex)
        v2 = np.array(p2) - np.array(vertex)
        
        # 单位化
        v1_unit = v1 / np.linalg.norm(v1)
        v2_unit = v2 / np.linalg.norm(v2)
        
        # 角平分线方向
        bisector_dir = v1_unit + v2_unit
        if np.linalg.norm(bisector_dir) < 1e-10:  # 180度角
            bisector_dir = np.array([-v1_unit[1], v1_unit[0], 0])
        else:
            bisector_dir = bisector_dir / np.linalg.norm(bisector_dir)
        
        return bisector_dir
```

---

## 3. 角度系统深度解析

### 3.1 Manim Angle 类参数详解

```python
Angle(
    line1,              # 第一条线 (Line 对象)
    line2,              # 第二条线 (Line 对象)
    radius=0.5,         # 角度弧的半径
    quadrant=(1, 1),    # 锚点选择 (见下文)
    other_angle=False,  # 是否使用补角
    dot=False,          # 是否在弧上显示点
    dot_radius=0.04,    # 点的半径
    dot_distance=0.55,  # 点到顶点的距离
    dot_color=WHITE,    # 点的颜色
    elbow=False         # 是否使用直角符号
)
```

### 3.2 quadrant 参数详解

`quadrant = (a, b)` 控制角度弧的锚定方式：

| quadrant | line1 锚点 | line2 锚点 | 使用场景 |
|----------|-----------|-----------|---------|
| (1, 1)   | 终点 (end) | 终点 (end) | 两线都从顶点出发 |
| (-1, 1)  | 起点 (start) | 终点 (end) | line1 指向顶点 |
| (1, -1)  | 终点 (end) | 起点 (start) | line2 指向顶点 |
| (-1, -1) | 起点 (start) | 起点 (start) | 两线都指向顶点 |

**关键理解**:
- `1` 表示使用线的 **终点** (end)
- `-1` 表示使用线的 **起点** (start)
- 两条线的锚点应该重合（即角的顶点）

### 3.3 正确创建角度的模式

```python
# 模式1：两线从顶点出发（最常用）
# 场景：标注三角形的内角
def angle_at_vertex_outward(vertex, point_a, point_b, radius=0.5):
    """顶点在 vertex，两条边分别指向 point_a 和 point_b"""
    line1 = Line(vertex, point_a)
    line2 = Line(vertex, point_b)
    # 两线都从顶点(start)出发，所以锚点都是 end
    return Angle(line1, line2, radius=radius, quadrant=(1, 1))

# 模式2：两线指向顶点
def angle_at_vertex_inward(vertex, point_a, point_b, radius=0.5):
    """两条边都指向 vertex"""
    line1 = Line(point_a, vertex)  # 从 A 指向顶点
    line2 = Line(point_b, vertex)  # 从 B 指向顶点
    # 两线都指向顶点(end)，锚点都是 end
    return Angle(line1, line2, radius=radius, quadrant=(1, 1))

# 模式3：使用 from_three_points（推荐！）
def angle_from_points(A, B, C, radius=0.5, other_angle=False):
    """
    三点定角：角在 B 点
    A---B---C
    """
    return Angle.from_three_points(A, B, C, radius=radius, other_angle=other_angle)

# 模式4：直角标记
def right_angle_mark(vertex, point_a, point_b, length=0.3):
    """直角符号"""
    line1 = Line(vertex, point_a)
    line2 = Line(vertex, point_b)
    return RightAngle(line1, line2, length=length)
    # 或者
    # return Angle(line1, line2, radius=length, elbow=True)
```

### 3.4 角度方向控制

```python
def determine_angle_direction(vertex, point_a, point_b):
    """
    确定从 point_a 到 point_b 的旋转方向
    返回：'CCW' (逆时针) 或 'CW' (顺时针)
    """
    v1 = np.array(point_a) - np.array(vertex)
    v2 = np.array(point_b) - np.array(vertex)
    
    # 二维叉积（z分量）
    cross_z = v1[0] * v2[1] - v1[1] * v2[0]
    
    return 'CCW' if cross_z > 0 else 'CW'

def create_angle_with_direction(vertex, point_a, point_b, radius=0.5, direction='CCW'):
    """
    创建指定方向的角度弧
    direction: 'CCW' 逆时针, 'CW' 顺时针
    """
    actual_direction = determine_angle_direction(vertex, point_a, point_b)
    other_angle = (actual_direction != direction)
    
    line1 = Line(vertex, point_a)
    line2 = Line(vertex, point_b)
    return Angle(line1, line2, radius=radius, other_angle=other_angle)
```

### 3.5 Arc 方向控制

```python
# Arc 类的角度方向
# angle > 0: 逆时针
# angle < 0: 顺时针

# 从 0° 逆时针画 90°
arc_ccw = Arc(radius=1, start_angle=0, angle=PI/2)

# 从 90° 顺时针画 90°（回到 0°）
arc_cw = Arc(radius=1, start_angle=PI/2, angle=-PI/2)

# ArcBetweenPoints 的方向由 radius 符号控制
# radius > 0: 弧在连线的左侧（逆时针方向）
# radius < 0: 弧在连线的右侧（顺时针方向）
arc_left = ArcBetweenPoints(start=LEFT, end=RIGHT, radius=1)   # 上弧
arc_right = ArcBetweenPoints(start=LEFT, end=RIGHT, radius=-1)  # 下弧
```

---

## 4. 长度与比例约束

### 4.1 边长验证模式

```python
class LengthConstraintVerifier:
    """长度约束验证器"""
    
    def __init__(self, epsilon=1e-6):
        self.epsilon = epsilon
        self.constraints = []
    
    def add_equal_length(self, name, segment1, segment2):
        """添加等长约束"""
        self.constraints.append({
            'type': 'equal_length',
            'name': name,
            'seg1': segment1,
            'seg2': segment2
        })
    
    def add_ratio(self, name, segment1, segment2, ratio):
        """添加比例约束: len(seg1) / len(seg2) = ratio"""
        self.constraints.append({
            'type': 'ratio',
            'name': name,
            'seg1': segment1,
            'seg2': segment2,
            'ratio': ratio
        })
    
    def add_fixed_length(self, name, segment, length):
        """添加固定长度约束"""
        self.constraints.append({
            'type': 'fixed_length',
            'name': name,
            'segment': segment,
            'length': length
        })
    
    def verify_all(self):
        """验证所有约束"""
        results = []
        for c in self.constraints:
            if c['type'] == 'equal_length':
                len1 = np.linalg.norm(c['seg1'][1] - c['seg1'][0])
                len2 = np.linalg.norm(c['seg2'][1] - c['seg2'][0])
                passed = abs(len1 - len2) < self.epsilon
                results.append((c['name'], passed, f"差值: {abs(len1-len2):.2e}"))
            
            elif c['type'] == 'ratio':
                len1 = np.linalg.norm(c['seg1'][1] - c['seg1'][0])
                len2 = np.linalg.norm(c['seg2'][1] - c['seg2'][0])
                actual_ratio = len1 / len2 if len2 > 0 else float('inf')
                passed = abs(actual_ratio - c['ratio']) < self.epsilon
                results.append((c['name'], passed, f"实际比例: {actual_ratio:.6f}"))
            
            elif c['type'] == 'fixed_length':
                actual = np.linalg.norm(c['segment'][1] - c['segment'][0])
                passed = abs(actual - c['length']) < self.epsilon
                results.append((c['name'], passed, f"实际长度: {actual:.6f}"))
        
        # 打印结果
        all_passed = True
        for name, passed, detail in results:
            status = "✓" if passed else "✗"
            print(f"{status} {name}: {detail}")
            if not passed:
                all_passed = False
        
        return all_passed

# 使用示例
verifier = LengthConstraintVerifier()
verifier.add_equal_length("AB = CD", (A, B), (C, D))
verifier.add_ratio("AB / BC = 2:1", (A, B), (B, C), 2.0)
verifier.add_fixed_length("AB = 4", (A, B), 4.0)
assert verifier.verify_all(), "长度约束验证失败!"
```

### 4.2 比例计算工具

```python
class ProportionCalculator:
    """比例计算工具"""
    
    @staticmethod
    def divide_segment(start, end, ratio):
        """
        按比例分割线段
        ratio: m:n 的 m/(m+n)
        返回分割点
        """
        t = ratio
        return (1 - t) * np.array(start) + t * np.array(end)
    
    @staticmethod
    def divide_segment_mn(start, end, m, n):
        """
        按 m:n 分割线段
        返回分割点 P，使 SP:PE = m:n
        """
        return ProportionCalculator.divide_segment(start, end, m / (m + n))
    
    @staticmethod
    def golden_ratio_point(start, end, longer_first=True):
        """
        黄金分割点
        longer_first=True: 返回靠近 start 的点（长段在前）
        """
        phi = (1 + np.sqrt(5)) / 2  # ≈ 1.618
        if longer_first:
            t = 1 / phi
        else:
            t = 1 - 1 / phi
        return ProportionCalculator.divide_segment(start, end, t)
    
    @staticmethod
    def harmonic_conjugate(A, B, P):
        """
        调和共轭点
        给定 A, B, P 在一条直线上，找 Q 使 (A,B;P,Q) = -1
        """
        # 使用交比公式
        t = np.dot(P - A, B - A) / np.dot(B - A, B - A)
        t_q = t / (2*t - 1) if abs(2*t - 1) > 1e-10 else None
        if t_q is None:
            return None
        return A + t_q * (B - A)
```

---

## 5. 位置关系验证机制

### 5.1 综合关系验证器

```python
class GeometryRelationshipValidator:
    """几何关系综合验证器"""
    
    EPSILON = 1e-8
    
    def __init__(self):
        self.validations = []
        self.errors = []
    
    # ===== 添加约束 =====
    
    def add_perpendicular(self, name, line1, line2):
        """添加垂直约束"""
        self.validations.append({
            'type': 'perpendicular',
            'name': name,
            'line1': line1,  # (start, end) tuple
            'line2': line2
        })
    
    def add_parallel(self, name, line1, line2):
        """添加平行约束"""
        self.validations.append({
            'type': 'parallel',
            'name': name,
            'line1': line1,
            'line2': line2
        })
    
    def add_collinear(self, name, points):
        """添加共线约束"""
        self.validations.append({
            'type': 'collinear',
            'name': name,
            'points': points
        })
    
    def add_concurrent(self, name, lines):
        """添加共点约束（多条直线过同一点）"""
        self.validations.append({
            'type': 'concurrent',
            'name': name,
            'lines': lines  # list of (start, end) tuples
        })
    
    def add_on_circle(self, name, center, radius, points):
        """添加共圆约束"""
        self.validations.append({
            'type': 'on_circle',
            'name': name,
            'center': center,
            'radius': radius,
            'points': points
        })
    
    def add_angle_sum(self, name, angles, expected_sum):
        """添加角度和约束（弧度）"""
        self.validations.append({
            'type': 'angle_sum',
            'name': name,
            'angles': angles,
            'expected': expected_sum
        })
    
    # ===== 验证逻辑 =====
    
    def _check_perpendicular(self, line1, line2):
        v1 = np.array(line1[1]) - np.array(line1[0])
        v2 = np.array(line2[1]) - np.array(line2[0])
        dot = np.dot(v1[:2], v2[:2])
        return abs(dot) < self.EPSILON
    
    def _check_parallel(self, line1, line2):
        v1 = np.array(line1[1]) - np.array(line1[0])
        v2 = np.array(line2[1]) - np.array(line2[0])
        cross = np.cross(v1[:2], v2[:2])
        return abs(cross) < self.EPSILON
    
    def _check_collinear(self, points):
        if len(points) < 3:
            return True
        for i in range(len(points) - 2):
            p1, p2, p3 = points[i], points[i+1], points[i+2]
            area = 0.5 * abs(
                p1[0]*(p2[1]-p3[1]) + 
                p2[0]*(p3[1]-p1[1]) + 
                p3[0]*(p1[1]-p2[1])
            )
            if area > self.EPSILON:
                return False
        return True
    
    def _check_concurrent(self, lines):
        if len(lines) < 2:
            return True
        
        # 找第一个交点
        l1, l2 = lines[0], lines[1]
        d1 = np.array(l1[1]) - np.array(l1[0])
        d2 = np.array(l2[1]) - np.array(l2[0])
        
        intersection = GeometryPrecision.line_intersection(
            np.array(l1[0]), d1, np.array(l2[0]), d2
        )
        if intersection is None:
            return False
        
        # 检查其他线是否过此点
        for line in lines[2:]:
            if not self._point_on_line(intersection, line[0], line[1]):
                return False
        return True
    
    def _point_on_line(self, point, line_start, line_end):
        """检查点是否在直线上"""
        v1 = np.array(point) - np.array(line_start)
        v2 = np.array(line_end) - np.array(line_start)
        cross = np.cross(v1[:2], v2[:2])
        return abs(cross) < self.EPSILON
    
    def _check_on_circle(self, center, radius, points):
        for p in points:
            dist = np.linalg.norm(np.array(p[:2]) - np.array(center[:2]))
            if abs(dist - radius) > self.EPSILON:
                return False
        return True
    
    def _check_angle_sum(self, angles, expected):
        actual_sum = sum(angles)
        return abs(actual_sum - expected) < self.EPSILON
    
    # ===== 主验证方法 =====
    
    def validate_all(self, raise_on_error=True):
        """验证所有约束"""
        self.errors = []
        
        for v in self.validations:
            passed = False
            detail = ""
            
            if v['type'] == 'perpendicular':
                passed = self._check_perpendicular(v['line1'], v['line2'])
                if not passed:
                    v1 = np.array(v['line1'][1]) - np.array(v['line1'][0])
                    v2 = np.array(v['line2'][1]) - np.array(v['line2'][0])
                    dot = np.dot(v1[:2], v2[:2])
                    detail = f"点积 = {dot:.2e} (应为0)"
            
            elif v['type'] == 'parallel':
                passed = self._check_parallel(v['line1'], v['line2'])
                if not passed:
                    v1 = np.array(v['line1'][1]) - np.array(v['line1'][0])
                    v2 = np.array(v['line2'][1]) - np.array(v['line2'][0])
                    cross = np.cross(v1[:2], v2[:2])
                    detail = f"叉积 = {cross:.2e} (应为0)"
            
            elif v['type'] == 'collinear':
                passed = self._check_collinear(v['points'])
                detail = f"{len(v['points'])} 个点"
            
            elif v['type'] == 'concurrent':
                passed = self._check_concurrent(v['lines'])
                detail = f"{len(v['lines'])} 条线"
            
            elif v['type'] == 'on_circle':
                passed = self._check_on_circle(v['center'], v['radius'], v['points'])
                detail = f"{len(v['points'])} 个点, r={v['radius']:.4f}"
            
            elif v['type'] == 'angle_sum':
                passed = self._check_angle_sum(v['angles'], v['expected'])
                actual = sum(v['angles'])
                detail = f"实际: {np.degrees(actual):.4f}°, 期望: {np.degrees(v['expected']):.4f}°"
            
            status = "✓" if passed else "✗"
            print(f"{status} [{v['type']}] {v['name']}: {detail}")
            
            if not passed:
                self.errors.append(v['name'])
        
        if self.errors and raise_on_error:
            raise AssertionError(f"几何验证失败: {', '.join(self.errors)}")
        
        return len(self.errors) == 0
```

---

## 6. 数值精度与浮点误差处理

### 6.1 浮点数比较原则

```python
# ❌ 错误：直接比较浮点数
if a == b:  # 危险！

# ✅ 正确：使用容差比较
EPSILON = 1e-10

def float_equal(a, b, eps=EPSILON):
    """安全的浮点数比较"""
    return abs(a - b) < eps

def float_zero(a, eps=EPSILON):
    """检查是否为零"""
    return abs(a) < eps

# ✅ 使用 numpy 的 isclose
np.isclose(a, b, rtol=1e-9, atol=1e-12)
np.allclose(array1, array2, rtol=1e-9, atol=1e-12)
```

### 6.2 数值稳定性问题

```python
class NumericalStability:
    """数值稳定性工具"""
    
    @staticmethod
    def safe_arccos(x):
        """安全的 arccos，处理边界情况"""
        return np.arccos(np.clip(x, -1.0, 1.0))
    
    @staticmethod
    def safe_sqrt(x):
        """安全的 sqrt，处理微小负数"""
        return np.sqrt(max(0, x))
    
    @staticmethod
    def safe_divide(a, b, default=0):
        """安全的除法"""
        if abs(b) < 1e-15:
            return default
        return a / b
    
    @staticmethod
    def normalize_vector(v):
        """安全的向量单位化"""
        norm = np.linalg.norm(v)
        if norm < 1e-15:
            return v  # 返回原向量（零向量）
        return v / norm
    
    @staticmethod
    def condition_number_check(matrix, threshold=1e10):
        """
        检查矩阵条件数
        条件数过大意味着数值不稳定
        """
        cond = np.linalg.cond(matrix)
        if cond > threshold:
            print(f"警告：矩阵条件数过大 ({cond:.2e})，结果可能不稳定")
        return cond < threshold
```

### 6.3 累积误差控制

```python
# 累积误差示例：迭代计算
# ❌ 错误：每次迭代都累积误差
angle = 0
for i in range(360):
    angle += 1 * DEGREES  # 每次加1度
# 最终 angle 可能不精确等于 2*PI

# ✅ 正确：使用索引计算
for i in range(360):
    angle = i * DEGREES  # 无累积误差

# Kahan 求和算法（减少浮点累积误差）
def kahan_sum(values):
    """Kahan 求和算法"""
    total = 0.0
    compensation = 0.0
    for v in values:
        y = v - compensation
        t = total + y
        compensation = (t - total) - y
        total = t
    return total
```

---

## 7. Manim 0.19.2 API 约束表

### 7.1 类参数约束

| 类名 | ✅ 允许的参数 | ❌ 禁止的参数 | 备注 |
|------|-------------|-------------|------|
| `Sector` | `radius`, `angle`, `start_angle` | `inner_radius`, `outer_radius` | 使用 `radius` 而非 `outer_radius` |
| `AnnularSector` | `inner_radius`, `outer_radius`, `angle` | - | 环形扇区专用 |
| `Rectangle` | `width`, `height` | `corner_radius` | 圆角矩形用 RoundedRectangle |
| `RoundedRectangle` | `corner_radius`, `width`, `height` | - | - |
| `MathTex` | ASCII, LaTeX | 中文/Unicode | 中文用 Text |
| `Arrow.scale()` | `scale_tips=True/False` | - | 控制箭头尖端是否缩放 |

### 7.2 LaTeX 常见错误

```python
# 1. 中文不能用于 MathTex
# ❌ 错误
MathTex(r"\text{三角形}")  # Unicode Error!

# ✅ 正确
Text("三角形", font="Noto Sans CJK SC")

# 2. 度数符号
# ❌ 错误
MathTex(r"90°")  # 特殊字符错误

# ✅ 正确
MathTex(r"90^\circ")

# 3. 分数格式
# ❌ 错误
MathTex(r"{{a} \over {b}}")  # 双花括号解析错误

# ✅ 正确
MathTex(r"\frac{a}{b}")

# 4. 混合中英文
# ❌ 错误
Tex(r"周角 = 360^\circ")  # 混合失败

# ✅ 正确
chinese = Text("周角 =", font="Noto Sans CJK SC")
math = MathTex(r"360^\circ")
VGroup(chinese, math).arrange(RIGHT)

# 或使用 ctex 模板
from manim import TexTemplateLibrary
Tex(r"周角 $= 360^\circ$", tex_template=TexTemplateLibrary.ctex)
```

### 7.3 虚线绘制

```python
# ❌ 错误：set_style 不支持 stroke_dasharray
line.set_style(stroke_dasharray="5 5")  # TypeError!

# ✅ 正确方法1：DashedLine
DashedLine(start, end, dash_length=0.1, color=GRAY)

# ✅ 正确方法2：DashedVMobject
from manim import DashedVMobject
dashed = DashedVMobject(Line(start, end), num_dashes=20)
```

---

## 8. 工业级场景结构模板

```python
from manim import *
import numpy as np


class GeometryPrecision:
    """几何精度计算工具类"""
    
    EPSILON = 1e-10
    
    @staticmethod
    def midpoint(P1, P2):
        return (np.array(P1) + np.array(P2)) / 2
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        P, A, B = np.array(point), np.array(line_start), np.array(line_end)
        AB = B - A
        t = np.dot(P - A, AB) / np.dot(AB, AB)
        return A + t * AB
    
    @staticmethod
    def circumcenter(A, B, C):
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        D = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        return np.array([ux, uy, 0])
    
    @staticmethod
    def incenter(A, B, C):
        a = np.linalg.norm(B - C)
        b = np.linalg.norm(C - A)
        c = np.linalg.norm(A - B)
        return (a*A + b*B + c*C) / (a + b + c)
    
    @staticmethod
    def are_perpendicular(v1, v2, eps=1e-10):
        return abs(np.dot(v1[:2], v2[:2])) < eps
    
    @staticmethod
    def are_parallel(v1, v2, eps=1e-10):
        return abs(np.cross(v1[:2], v2[:2])) < eps


class IndustrialGeometryScene(Scene):
    """工业级几何场景模板"""
    
    def construct(self):
        # 阶段1：几何数据初始化
        self._setup_geometry()
        
        # 阶段2：几何验证
        self._verify_geometry()
        
        # 阶段3：创建 Mobject
        self._create_mobjects()
        
        # 阶段4：执行动画
        self._animate()
    
    # ========== 阶段1：几何数据初始化 ==========
    
    def _setup_geometry(self):
        """
        【核心】初始化所有几何数据
        原则：计算一次，到处引用
        """
        # --- 基准参数 ---
        self.SCALE = 1.0
        self.OFFSET = ORIGIN
        
        # --- 主顶点 ---
        self.A = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2, -1, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0, 2, 0]) * self.SCALE + self.OFFSET
        
        # --- 派生点（必须计算！）---
        self.M_AB = GeometryPrecision.midpoint(self.A, self.B)
        self.M_BC = GeometryPrecision.midpoint(self.B, self.C)
        self.M_CA = GeometryPrecision.midpoint(self.C, self.A)
        
        # --- 特殊点 ---
        self.circumcenter = GeometryPrecision.circumcenter(self.A, self.B, self.C)
        self.incenter = GeometryPrecision.incenter(self.A, self.B, self.C)
        self.centroid = (self.A + self.B + self.C) / 3
        
        # --- 边长缓存 ---
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA  
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # --- 外接圆半径 ---
        self.circumradius = np.linalg.norm(self.A - self.circumcenter)
        
        # --- 内切圆半径 ---
        s = (self.a + self.b + self.c) / 2  # 半周长
        area = np.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
        self.inradius = area / s
    
    # ========== 阶段2：几何验证 ==========
    
    def _verify_geometry(self):
        """验证几何计算正确性"""
        eps = 1e-6
        
        # 验证外心到三顶点距离相等
        r_A = np.linalg.norm(self.A - self.circumcenter)
        r_B = np.linalg.norm(self.B - self.circumcenter)
        r_C = np.linalg.norm(self.C - self.circumcenter)
        
        assert abs(r_A - r_B) < eps, f"外心验证失败: r_A={r_A}, r_B={r_B}"
        assert abs(r_B - r_C) < eps, f"外心验证失败: r_B={r_B}, r_C={r_C}"
        
        # 验证内心到三边距离相等
        d_A = GeometryPrecision.foot_of_perpendicular(self.incenter, self.B, self.C)
        d_B = GeometryPrecision.foot_of_perpendicular(self.incenter, self.C, self.A)
        d_C = GeometryPrecision.foot_of_perpendicular(self.incenter, self.A, self.B)
        
        dist_A = np.linalg.norm(self.incenter - d_A)
        dist_B = np.linalg.norm(self.incenter - d_B)
        dist_C = np.linalg.norm(self.incenter - d_C)
        
        assert abs(dist_A - dist_B) < eps, f"内心验证失败"
        assert abs(dist_B - dist_C) < eps, f"内心验证失败"
        
        print("✓ 几何验证通过")
    
    # ========== 阶段3：创建 Mobject ==========
    
    def _create_mobjects(self):
        """创建所有 Mobject"""
        # 三角形
        self.triangle = Polygon(self.A, self.B, self.C, color=WHITE)
        
        # 顶点标签
        self.label_A = MathTex("A").next_to(self.A, DL)
        self.label_B = MathTex("B").next_to(self.B, DR)
        self.label_C = MathTex("C").next_to(self.C, UP)
        
        # 外接圆
        self.circumcircle = Circle(
            radius=self.circumradius,
            color=BLUE
        ).move_to(self.circumcenter)
        
        # 内切圆
        self.incircle = Circle(
            radius=self.inradius,
            color=GREEN
        ).move_to(self.incenter)
        
        # 特殊点
        self.dot_circumcenter = Dot(self.circumcenter, color=BLUE)
        self.dot_incenter = Dot(self.incenter, color=GREEN)
        self.dot_centroid = Dot(self.centroid, color=RED)
    
    # ========== 阶段4：执行动画 ==========
    
    def _animate(self):
        """执行动画序列"""
        # 显示三角形
        self.play(Create(self.triangle))
        self.play(
            Write(self.label_A),
            Write(self.label_B),
            Write(self.label_C)
        )
        
        # 显示外接圆
        self.play(Create(self.circumcircle))
        self.play(FadeIn(self.dot_circumcenter))
        
        # 显示内切圆
        self.play(Create(self.incircle))
        self.play(FadeIn(self.dot_incenter))
        
        # 显示重心
        self.play(FadeIn(self.dot_centroid))
        
        self.wait(2)
```

---

## 9. 调试与验证清单

### 9.1 创建前检查清单

- [ ] 所有坐标是通过数学计算得出的，不是臆想的
- [ ] 派生点（中点、垂足、交点等）是从主点计算的
- [ ] 缓存了常用的边长、角度值
- [ ] 使用了一致的坐标系和缩放因子

### 9.2 几何关系检查清单

- [ ] 垂直关系：点积 ≈ 0
- [ ] 平行关系：叉积 ≈ 0
- [ ] 共线关系：三角形面积 ≈ 0
- [ ] 等长关系：长度差 ≈ 0
- [ ] 角度和：三角形内角和 ≈ π

### 9.3 数值精度检查清单

- [ ] 浮点比较使用容差 (ε ≈ 1e-10)
- [ ] arccos 参数 clip 到 [-1, 1]
- [ ] 除法检查分母非零
- [ ] 向量单位化检查模长非零

### 9.4 Manim API 检查清单

- [ ] Sector 使用 `radius`，不是 `inner_radius`
- [ ] Rectangle 不使用 `corner_radius`
- [ ] MathTex 不包含中文
- [ ] 度数使用 `^\circ` 不是 `°`
- [ ] 分数使用 `\frac{}{}` 不是 `\over`

### 9.5 动画前检查清单

- [ ] 所有元素在画布范围内 (x: ±7, y: ±4)
- [ ] 元素不会在动画中超出边界
- [ ] 缩放操作后更新了派生点
- [ ] 场景结束时清理了临时元素

---

## 总结

**核心记忆点**:

1. **永不臆想坐标** - 所有点必须通过数学公式计算
2. **一次计算，多次引用** - 在 setup 阶段计算所有几何数据
3. **验证几何关系** - 在动画前验证所有约束
4. **注意数值精度** - 使用容差比较，处理边界情况
5. **遵守 API 约束** - 注意 0.19.2 版本的参数限制
6. **角度方向判断** - 使用叉积确定方向，正确设置 `other_angle`

遵循这些原则，可以大幅减少几何动画中的低级错误，创建精确、专业的数学动画。
