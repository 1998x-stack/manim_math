# 全等三角形的概念与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 初级
- 目标受众: 七年级学生

## 颜色配置
```python
COLOR_TRIANGLE_1 = "#3498db"      # 蓝色 - 第一个三角形
COLOR_TRIANGLE_2 = "#e74c3c"      # 红色 - 第二个三角形
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
COLOR_EQUAL_MARK = "#2ecc71"      # 绿色 - 相等标记
```

## 几何预计算清单

### 三角形 1 (ABC)
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 顶点A | 基准点 | self.A1 | 左下角 |
| 顶点B | 基准点 | self.B1 | 右下角 |
| 顶点C | 基准点 | self.C1 | 顶部 |
| 边长AB | ‖B1-A1‖ | self.AB1_length | 底边 |
| 边长BC | ‖C1-B1‖ | self.BC1_length | 右边 |
| 边长CA | ‖A1-C1‖ | self.CA1_length | 左边 |
| 角A | 向量夹角 | self.angle_A1 | 顶点A处角度 |
| 角B | 向量夹角 | self.angle_B1 | 顶点B处角度 |
| 角C | 向量夹角 | self.angle_C1 | 顶点C处角度 |

### 三角形 2 (DEF) - 全等但位置不同
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 顶点D | 对应A的位置 | self.D2 | 初始在右侧 |
| 顶点E | 对应B的位置 | self.E2 | 初始在右侧 |
| 顶点F | 对应C的位置 | self.F2 | 初始在右侧 |

### 验证清单
- [ ] AB = DE (对应边相等)
- [ ] BC = EF (对应边相等)
- [ ] CA = FD (对应边相等)
- [ ] ∠A = ∠D (对应角相等)
- [ ] ∠B = ∠E (对应角相等)
- [ ] ∠C = ∠F (对应角相等)

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
吸引注意力，引出全等三角形的概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 两个三角形轮廓（模糊/闪烁）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 两个三角形闪现 | `FadeIn(tri1, tri2, lag_ratio=0.3)` | 0.6s |
| 1.7s | 问号闪烁 | `Flash(question_mark)` | 0.3s |
| 2.0s | 等待 | `self.wait(1.0)` | 1.0s |

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, triangle_1, triangle_2

---

## Scene 2: 定义介绍 (5-12秒)

### 目的
清晰展示全等三角形的定义

### 元素
1. 定义文字
2. 三角形1 (ABC)
3. 三角形2 (DEF)
4. "完全重合"演示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 定义文字淡入 | `FadeIn(definition)` | 0.5s |
| 0.5s | 三角形1创建 | `Create(triangle_1)` | 1.0s |
| 1.5s | 顶点标签A,B,C | `Write(labels_1)` | 0.6s |
| 2.1s | 三角形2创建 | `Create(triangle_2)` | 1.0s |
| 3.1s | 顶点标签D,E,F | `Write(labels_2)` | 0.6s |
| 3.7s | 等待 | `self.wait(0.5)` | 0.5s |

### 几何计算细节
```python
# 三角形1的顶点 (左侧，标准位置)
self.A1 = np.array([-3.5, -1.0, 0]) * self.SCALE + self.OFFSET
self.B1 = np.array([-1.5, -1.0, 0]) * self.SCALE + self.OFFSET
self.C1 = np.array([-2.5, 1.0, 0]) * self.SCALE + self.OFFSET

# 三角形2的顶点 (右侧，相同形状但不同位置)
# 使用旋转 + 平移来确保全等
offset_right = np.array([4.0, 0.5, 0])
rotation_angle = 30 * DEGREES

# 计算D, E, F (保持全等)
center_1 = (self.A1 + self.B1 + self.C1) / 3
```

### 清理
- 保留: triangle_1, triangle_2, labels_1, labels_2
- FadeOut: definition

---

## Scene 3: 重合演示 (12-22秒)

### 目的
通过动画演示"完全重合"的概念

### 元素
1. 三角形2的副本
2. 移动+旋转动画
3. 高亮效果

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 说明文字 | `FadeIn(overlap_text)` | 0.4s |
| 0.4s | 三角形2高亮 | `triangle_2.animate.set_stroke(YELLOW, 5)` | 0.3s |
| 0.7s | 创建副本 | `tri2_copy = triangle_2.copy()` | 0.1s |
| 0.8s | 移动到三角形1 | `tri2_copy.animate.move_to(triangle_1)` | 1.5s |
| 2.3s | 旋转对齐 | `tri2_copy.animate.rotate(align_angle)` | 1.0s |
| 3.3s | 完全重合闪光 | `Flash(tri2_copy)` | 0.4s |
| 3.7s | 等待理解 | `self.wait(1.5)` | 1.5s |

### 关键计算
```python
# 计算从三角形2到三角形1的变换
# 1. 平移向量
translation = center_1 - center_2

# 2. 旋转角度（使对应边对齐）
vec_AB = self.B1 - self.A1
vec_DE = self.E2 - self.D2
align_angle = angle_between_vectors(vec_DE, vec_AB)

# ⚠️ 注意：这里的角度可能大于90度，需要检查方向
# 使用叉积判断旋转方向
cross_z = vec_DE[0] * vec_AB[1] - vec_DE[1] * vec_AB[0]
if cross_z < 0:
    align_angle = -align_angle  # 顺时针
```

### 清理
- FadeOut: tri2_copy, overlap_text
- 保留: triangle_1, triangle_2, labels

---

## Scene 4: 全等符号 (22-30秒)

### 目的
介绍全等符号的书写规范

### 元素
1. 全等符号 ≌
2. 完整表达式 △ABC≌△DEF
3. 对应顺序强调

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.4s |
| 0.4s | 书写△ABC | `Write(triangle_abc_tex)` | 0.8s |
| 1.2s | 书写≌符号 | `Write(congruent_symbol)` | 0.5s |
| 1.7s | 书写△DEF | `Write(triangle_def_tex)` | 0.8s |
| 2.5s | 箭头连接对应点 | `Create(arrows)` | 1.2s |
| 3.7s | 强调提示 | `FadeIn(warning_text)` | 0.5s |
| 4.2s | 等待 | `self.wait(1.5)` | 1.5s |

### LaTeX表达式
```python
congruent_expr = MathTex(
    r"\triangle", "ABC", r"\cong", r"\triangle", "DEF"
)
# 分组以便于独立控制每部分的颜色和动画

# 对应关系箭头
arrows = VGroup(
    Arrow(A_label, D_label, buff=0.1, color=GREEN),
    Arrow(B_label, E_label, buff=0.1, color=GREEN),
    Arrow(C_label, F_label, buff=0.1, color=GREEN)
)
```

### 清理
- FadeOut: title, arrows, warning_text
- 保留: congruent_expr (移到顶部)

---

## Scene 5: 对应边相等 (30-45秒)

### 目的
展示并证明对应边相等的性质

### 元素
1. 三条边的长度标记
2. 相等标记（刻度线）
3. 等式 AB=DE, BC=EF, CA=FD

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(property_title)` | 0.4s |
| 0.4s | 高亮边AB和DE | `Indicate(AB, DE)` | 0.8s |
| 1.2s | 添加相等标记 | `Create(tick_marks_AB_DE)` | 0.5s |
| 1.7s | 显示等式AB=DE | `Write(equation_1)` | 0.6s |
| 2.3s | 高亮边BC和EF | `Indicate(BC, EF)` | 0.8s |
| 3.1s | 添加相等标记 | `Create(tick_marks_BC_EF)` | 0.5s |
| 3.6s | 显示等式BC=EF | `Write(equation_2)` | 0.6s |
| 4.2s | 高亮边CA和FD | `Indicate(CA, FD)` | 0.8s |
| 5.0s | 添加相等标记 | `Create(tick_marks_CA_FD)` | 0.5s |
| 5.5s | 显示等式CA=FD | `Write(equation_3)` | 0.6s |
| 6.1s | 等待 | `self.wait(1.5)` | 1.5s |

### 相等标记绘制
```python
def create_tick_marks(line_start, line_end, num_ticks=1, color=GREEN):
    """
    在线段上创建垂直刻度标记
    """
    direction = line_end - line_start
    direction_normalized = direction / np.linalg.norm(direction)
    perpendicular = np.array([-direction_normalized[1], direction_normalized[0], 0])
    
    tick_length = 0.15
    midpoint = (line_start + line_end) / 2
    
    ticks = VGroup()
    spacing = 0.12
    
    for i in range(num_ticks):
        offset = (i - (num_ticks - 1) / 2) * spacing * direction_normalized
        tick = Line(
            midpoint + offset - perpendicular * tick_length / 2,
            midpoint + offset + perpendicular * tick_length / 2,
            color=color,
            stroke_width=3
        )
        ticks.add(tick)
    
    return ticks
```

### 清理
- FadeOut: property_title, equations
- 保留: tick_marks (保持在图上)

---

## Scene 6: 对应角相等 (45-60秒)

### 目的
展示并证明对应角相等的性质

### 元素
1. 角度弧标记
2. 相等的角度标记（双弧、三弧等）
3. 等式 ∠A=∠D, ∠B=∠E, ∠C=∠F

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(angle_title)` | 0.4s |
| 0.4s | 创建角A和角D的弧 | `Create(angle_A_arc, angle_D_arc)` | 0.8s |
| 1.2s | 添加单弧标记 | `angle_A_arc.set_stroke(YELLOW, 4)` | 0.3s |
| 1.5s | 显示等式∠A=∠D | `Write(angle_equation_1)` | 0.6s |
| 2.1s | 创建角B和角E的弧 | `Create(angle_B_arc, angle_E_arc)` | 0.8s |
| 2.9s | 添加双弧标记 | 双弧效果 | 0.3s |
| 3.2s | 显示等式∠B=∠E | `Write(angle_equation_2)` | 0.6s |
| 3.8s | 创建角C和角F的弧 | `Create(angle_C_arc, angle_F_arc)` | 0.8s |
| 4.6s | 添加三弧标记 | 三弧效果 | 0.3s |
| 4.9s | 显示等式∠C=∠F | `Write(angle_equation_3)` | 0.6s |
| 5.5s | 等待 | `self.wait(1.5)` | 1.5s |

### 角度弧绘制（关键）
```python
def create_angle_arc_safe(vertex, point1, point2, radius=0.4, color=YELLOW):
    """
    安全创建角度弧，自动处理方向问题
    
    ⚠️ 重点：处理大于90度和大于180度的角
    """
    # 计算两个向量
    v1 = point1 - vertex
    v2 = point2 - vertex
    
    # 计算夹角（弧度）
    dot_product = np.dot(v1[:2], v2[:2])
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]  # z分量
    
    angle_rad = np.arctan2(cross_product, dot_product)
    
    # 检查角度范围
    if angle_rad < 0:
        angle_rad += 2 * PI
    
    # ⚠️ 关键判断
    if angle_rad > PI:
        # 角度大于180度，使用补角
        print(f"WARNING: 角度 {np.degrees(angle_rad):.1f}° > 180°，使用补角")
        use_other_angle = True
    elif angle_rad > PI / 2:
        # 角度在90-180度之间，需要注意
        print(f"INFO: 角度 {np.degrees(angle_rad):.1f}° 在90-180度之间")
        use_other_angle = False
    else:
        use_other_angle = False
    
    # 创建角度弧
    line1 = Line(vertex, point1)
    line2 = Line(vertex, point2)
    
    arc = Angle(
        line1, line2,
        radius=radius,
        quadrant=(1, 1),  # 根据实际情况可能需要调整
        other_angle=use_other_angle,
        color=color,
        stroke_width=3
    )
    
    return arc, angle_rad

# 对于每个角都要验证
angle_A_arc, angle_A_rad = create_angle_arc_safe(self.A1, self.C1, self.B1)
angle_D_arc, angle_D_rad = create_angle_arc_safe(self.D2, self.F2, self.E2)

# 验证对应角相等
assert abs(angle_A_rad - angle_D_rad) < 1e-6, "对应角不相等！"
```

### 多重弧标记
```python
def create_multi_arc_mark(arc, num_arcs=1, spacing=0.08):
    """
    创建多重弧标记（用于表示不同的角）
    num_arcs: 1=单弧, 2=双弧, 3=三弧
    """
    arcs = VGroup()
    for i in range(num_arcs):
        arc_copy = arc.copy()
        arc_copy.scale(1 + i * spacing / arc.radius)
        arcs.add(arc_copy)
    return arcs
```

### 清理
- FadeOut: angle_title, angle_equations
- 保留: angle_arcs (保持在图上)

---

## Scene 7: 总结和片尾 (60-75秒)

### 目的
总结知识点，引导关注

### 元素
1. 核心知识点卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 三角形缩小到角落 | `triangles.animate.scale(0.4).to_corner(UL)` | 0.8s |
| 0.8s | 知识点卡片滑入 | `summary_cards.animate.shift(RIGHT*5)` | 1.0s |
| 1.8s | 每张卡片依次高亮 | `Indicate(card)` for card | 1.5s |
| 3.3s | 作者信息放大 | `author.animate.scale(1.5).move_to(UP)` | 0.8s |
| 4.1s | 关注提示淡入 | `FadeIn(follow_text, shift=UP*0.3)` | 0.5s |
| 4.6s | 装饰动画 | `Rotate(decorations)` | 1.5s |
| 6.1s | 全部淡出 | `FadeOut(*)` | 1.0s |

### 知识点卡片内容
1. 定义：能完全重合的两个三角形
2. 符号：△ABC≌△DEF
3. 性质1：对应边相等
4. 性质2：对应角相等
5. 关键：对应顺序很重要！

---

## 元素生命周期追踪表

| 元素ID | 创建场景 | 销毁场景 | 持久性 | 备注 |
|--------|---------|---------|-------|------|
| author_info | Scene 1 | Scene 7 | 全局 | 始终在顶部 |
| triangle_1 | Scene 2 | Scene 7 | 长期 | 主三角形1 |
| triangle_2 | Scene 2 | Scene 7 | 长期 | 主三角形2 |
| labels_1 (A,B,C) | Scene 2 | Scene 7 | 长期 | 顶点标签 |
| labels_2 (D,E,F) | Scene 2 | Scene 7 | 长期 | 顶点标签 |
| hook_text | Scene 1 | Scene 1 | 临时 | 开场钩子 |
| tri2_copy | Scene 3 | Scene 3 | 临时 | 重合演示 |
| congruent_expr | Scene 4 | Scene 7 | 中期 | 全等符号 |
| tick_marks | Scene 5 | Scene 7 | 中期 | 边相等标记 |
| angle_arcs | Scene 6 | Scene 7 | 中期 | 角相等标记 |
| summary_cards | Scene 7 | Scene 7 | 临时 | 总结卡片 |

---

## 关键技术难点

### 1. 全等三角形的构造
**难点**：确保三角形2与三角形1完全全等（所有边长和角度相等）

**解决方案**：
```python
# 使用旋转矩阵 + 平移
def create_congruent_triangle(original_vertices, rotation_angle, translation):
    """
    创建全等三角形
    rotation_angle: 旋转角度（弧度）
    translation: 平移向量
    """
    # 计算原三角形中心
    center = np.mean(original_vertices, axis=0)
    
    # 构造旋转矩阵（2D）
    cos_a = np.cos(rotation_angle)
    sin_a = np.sin(rotation_angle)
    rotation_matrix = np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ])
    
    # 对每个顶点：先移到原点，旋转，再移回并平移
    new_vertices = []
    for vertex in original_vertices:
        centered = vertex - center
        rotated = rotation_matrix @ centered
        translated = rotated + center + translation
        new_vertices.append(translated)
    
    return new_vertices

# 验证全等性
def verify_congruence(tri1_vertices, tri2_vertices):
    """验证两个三角形全等"""
    eps = 1e-6
    
    # 计算边长
    def get_side_lengths(vertices):
        A, B, C = vertices
        return [
            np.linalg.norm(B - A),
            np.linalg.norm(C - B),
            np.linalg.norm(A - C)
        ]
    
    sides1 = sorted(get_side_lengths(tri1_vertices))
    sides2 = sorted(get_side_lengths(tri2_vertices))
    
    for s1, s2 in zip(sides1, sides2):
        assert abs(s1 - s2) < eps, f"边长不相等: {s1:.6f} vs {s2:.6f}"
    
    print("✓ 全等性验证通过")
```

### 2. 角度弧的方向控制
**难点**：确保角度弧在正确的一侧，特别是大于90度的角

**解决方案**：见 Scene 6 的详细代码

### 3. 重合动画的精确对齐
**难点**：让三角形2精确移动到三角形1的位置并完全重合

**解决方案**：
```python
# 分步骤对齐
# Step 1: 计算质心对齐
center1 = (A1 + B1 + C1) / 3
center2 = (D2 + E2 + F2) / 3
translation = center1 - center2

# Step 2: 移动质心
tri2_copy.shift(translation)

# Step 3: 计算旋转角度（使用对应边）
vec_AB = B1 - A1
vec_DE_current = E2 + translation - (D2 + translation)
angle = angle_between_vectors(vec_DE_current, vec_AB)

# Step 4: 绕质心旋转
tri2_copy.rotate(angle, about_point=center1)
```

---

## 验证检查清单

### 几何精度
- [ ] AB = DE (误差 < 1e-6)
- [ ] BC = EF (误差 < 1e-6)
- [ ] CA = FD (误差 < 1e-6)
- [ ] ∠A = ∠D (误差 < 1e-6 弧度)
- [ ] ∠B = ∠E (误差 < 1e-6 弧度)
- [ ] ∠C = ∠F (误差 < 1e-6 弧度)

### 角度方向
- [ ] 所有角度弧在正确的一侧
- [ ] 没有角度弧超出三角形外部
- [ ] 多重弧标记清晰可见

### 动画流畅性
- [ ] 没有元素溢出边界
- [ ] 文字和图形不重叠
- [ ] 难点有足够停留时间 (1.5-2.0s)
- [ ] 总时长在目标范围内

### 教学效果
- [ ] 概念解释清晰
- [ ] 视觉引导明确
- [ ] 重点突出
- [ ] 符号规范准确

---

## 字体大小规范

```python
FONT_SIZES = {
    "title": 36,              # 场景标题
    "subtitle": 28,           # 副标题
    "body": 22,               # 正文说明
    "label": 24,              # 顶点标签 (A, B, C)
    "small": 18,              # 小字/注释
    "author": 20,             # 作者信息
    "formula": 32,            # 数学公式
    "property": 24,           # 性质说明
}
```

---

## 品牌标识

```python
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "Noto Sans CJK SC"

# 位置：顶部 y=+7
author_info = Text(
    f"{AUTHOR_NAME} {AUTHOR_ID}",
    font=AUTHOR_FONT,
    font_size=FONT_SIZES["author"],
    color=GRAY_B
).move_to(UP * 7)
```

---

## 总时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场钩子 | 5s | 5s |
| Scene 2: 定义介绍 | 7s | 12s |
| Scene 3: 重合演示 | 10s | 22s |
| Scene 4: 全等符号 | 8s | 30s |
| Scene 5: 对应边相等 | 15s | 45s |
| Scene 6: 对应角相等 | 15s | 60s |
| Scene 7: 总结片尾 | 15s | 75s |
| **总计** | **75s** | - |

---

## 备注

1. **色彩对比**：蓝色和红色形成强烈对比，便于区分两个三角形
2. **标记一致性**：边用刻度线，角用弧线，保持视觉语言统一
3. **节奏控制**：关键概念（全等定义、对应关系）停留时间加长
4. **验证优先**：每个几何元素创建后立即验证，确保精度