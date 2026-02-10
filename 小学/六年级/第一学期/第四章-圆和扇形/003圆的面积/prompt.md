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
1. **阅读技能文档** - 解压并研读 manim-math.skill（包含 references、examples）
2. **构建分镜脚本** - 创建 `storyboard.md`，包含详细场景、几何计算、元素生命周期管理
3. **编写动画代码** - 基于分镜脚本和技能文档生成 Python 代码
4. **verify_geometry.py本地运行获取反馈** - verify_geometry.py本地运行获取反馈，然后fix&repair python code
    - notice: use only numpy package, do not use manim package; 
    - build def verify_angles() function in verify_geometry.py: 注意涉及的angle，如果大于90度，需要稍微分析一下；如果大于180度，要加强注意⚠️，非常非常可能angle方向错了！（ Manim 的 Angle.from_three_points 默认是逆时针。需要添加 other_angle=True 参数。让我修复：）
    - build def grep_MathTex() function: avoid for LaTeX compilation error(such as LaTeX Error: Unicode character 乘 (U+4E58) )
    - build verify_boundaries() function: 验证元素是否在安全边界内
</task_definition>

---

## 🎯 题目/知识点

<problem>
{
  "年级": "六年级",
  "学期": "第一学期",
  "章节": "第四章",
  "内容": "圆和扇形",
  "知识点": "圆的面积",
  "知识点内容详细描述": "公式推导:通过'剪拼法',将圆等分成若干个小扇形,拼成一个近似的长方形。长方形的长约等于圆周长的一半(πr),宽约等于半径(r),所以圆的面积S=πr×r=πr²。理解公式中r²的意义,以及极限思想(分得越细,越接近长方形)。",
  "数学公式": [
    "S = πr²",
    "圆面积 = π × 半径²",
    "推导: 长方形面积 = πr × r"
  ],
  "相关知识点": [
    "面积",
    "圆",
    "半径",
    "π",
    "转化思想",
    "极限思想"
  ],
  "manim动画涉及元素": [
    "Circle",
    "Polygon",
    "Rectangle",
    "Text",
    "MathTex",
    "VGroup",
    "Transform",
    "FadeIn"
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

## 📝 分镜脚本模板 (storyboard.md)

<storyboard_template>
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
</storyboard_template>

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
# manim -qh triangle_five_centers.py TriangleFiveCenters   # 高质量
# manim -qh triangle_five_centers.py TriangleFiveCenters   # 4K质量
</good_template>

</manim_video_generation_prompt>