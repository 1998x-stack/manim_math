# 中心对称 (Central Symmetry) - 动画分镜脚本

## 元信息
- **目标时长**: 60-75 秒
- **场景数量**: 7 个主场景
- **难度等级**: 七年级（初一）
- **核心概念**: 中心对称 = 绕某点旋转180°
- **教学目标**: 
  1. 理解中心对称的定义
  2. 掌握中心对称的性质（对应点连线过对称中心且被平分）
  3. 能够识别和构造中心对称图形

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"        # 红色 - 原图形
COLOR_SECONDARY = "#3498db"      # 蓝色 - 对称图形
COLOR_CENTER = "#f39c12"         # 橙色 - 对称中心
COLOR_CONNECTION = "#2ecc71"     # 绿色 - 连线
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝黑色背景
```

## 几何预计算清单

### 场景2-4: 三角形中心对称
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 对称中心O | 手动设置 | `self.O` | 坐标系原点附近 |
| 原三角形顶点 | 手动设置 | `self.A, self.B, self.C` | 偏移至合适位置 |
| 对称三角形顶点 | 关于O对称 | `self.A_sym, self.B_sym, self.C_sym` | `2*O - A` |
| 对应点连线 | 直线 | `line_AA, line_BB, line_CC` | 验证过O且被平分 |
| 中点 | `(A + A_sym) / 2` | `mid_A, mid_B, mid_C` | 验证等于O |

### 场景5: 字母中心对称（N, S, Z）
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 字母中心 | 字母边界框中心 | `letter_center` | 用于旋转 |
| 旋转后字母 | `rotate(180°, about=center)` | `letter_rotated` | 验证重合 |

### 场景6: 平行四边形对角线
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 平行四边形顶点 | 手动设置 | `P1, P2, P3, P4` | 确保是平行四边形 |
| 对角线交点 | 线段交点 | `intersection_O` | 对角线AC与BD交点 |
| 验证中点 | `(P1+P3)/2, (P2+P4)/2` | - | 验证两者相等 |

---

## 场景分镜

### Scene 0: 初始化几何数据 (setup_geometry)
**时长**: 0秒（预计算）

#### 几何计算
```python
def setup_geometry(self):
    # 全局缩放和偏移
    self.SCALE = 1.0
    self.MAIN_OFFSET = UP * 1.5
    
    # 对称中心 (多个场景共用)
    self.O = ORIGIN + self.MAIN_OFFSET
    
    # === 场景2-4: 三角形 ===
    # 原三角形顶点 (斜三角形)
    self.A = np.array([-2.0, 1.5, 0]) * self.SCALE + self.MAIN_OFFSET
    self.B = np.array([1.5, 2.0, 0]) * self.SCALE + self.MAIN_OFFSET
    self.C = np.array([0.5, -1.0, 0]) * self.SCALE + self.MAIN_OFFSET
    
    # 对称三角形顶点 (关于O中心对称)
    self.A_sym = 2 * self.O - self.A
    self.B_sym = 2 * self.O - self.B
    self.C_sym = 2 * self.O - self.C
    
    # 验证对应点连线中点
    self.mid_A = (self.A + self.A_sym) / 2
    self.mid_B = (self.B + self.B_sym) / 2
    self.mid_C = (self.C + self.C_sym) / 2
    
    # === 场景6: 平行四边形 ===
    self.P1 = np.array([-2.5, 1.5, 0]) + self.MAIN_OFFSET
    self.P2 = np.array([0.5, 2.5, 0]) + self.MAIN_OFFSET
    self.P3 = np.array([2.5, 0.5, 0]) + self.MAIN_OFFSET
    self.P4 = np.array([-0.5, -0.5, 0]) + self.MAIN_OFFSET
    
    # 对角线交点
    self.diag_center = self.calculate_line_intersection(
        self.P1, self.P3 - self.P1,
        self.P2, self.P4 - self.P2
    )
    
    # 验证几何正确性
    self.verify_geometry()

def verify_geometry(self):
    epsilon = 1e-6
    
    # 验证三角形中点等于O
    assert np.linalg.norm(self.mid_A - self.O) < epsilon, "中点A验证失败"
    assert np.linalg.norm(self.mid_B - self.O) < epsilon, "中点B验证失败"
    assert np.linalg.norm(self.mid_C - self.O) < epsilon, "中点C验证失败"
    
    # 验证平行四边形对角线交点是中点
    mid_AC = (self.P1 + self.P3) / 2
    mid_BD = (self.P2 + self.P4) / 2
    assert np.linalg.norm(mid_AC - mid_BD) < epsilon, "平行四边形对角线中点不重合"
    
    print("✓ 几何验证通过")
```

---

### Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出"中心对称"概念

#### 元素
1. 作者标识（顶部，贯穿全片）
2. 钩子问题（大字）
3. 旋转的图形暗示

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 两个三角形旋转展示 | `Rotate(triangle_pair, PI)` | 1.5s |
| 2.6s | 问题文字淡入 | `FadeIn(question)` | 0.5s |
| 3.1s | 等待思考 | `Wait(0.8)` | 0.8s |

#### 具体内容
```python
# 作者信息 (顶部，全局保留)
author = Text(
    "上海初高中数学直通车 @emptyandcalm",
    font="Noto Sans CJK SC",
    font_size=20,
    color=GRAY_B
).move_to(UP * 7)

# 钩子文字
hook = Text(
    "这两个图形有什么关系?",
    font="Noto Sans CJK SC",
    font_size=42,
    color=COLOR_HIGHLIGHT
).move_to(UP * 6)

# 暗示性图形 (两个三角形)
tri1 = Polygon(
    [-1.5, 0.5, 0], [0, 1.5, 0], [-0.5, -0.5, 0],
    color=COLOR_PRIMARY, fill_opacity=0.3
).move_to(LEFT * 1.5 + UP * 2)

tri2 = Polygon(
    [1.5, -0.5, 0], [0, -1.5, 0], [0.5, 0.5, 0],
    color=COLOR_SECONDARY, fill_opacity=0.3
).move_to(RIGHT * 1.5 + UP * 2)

center_dot = Dot(UP * 2, color=COLOR_CENTER, radius=0.1)

# 问题文字
question = Text(
    "它们是中心对称的!",
    font="Noto Sans CJK SC",
    font_size=36,
    color=WHITE
).move_to(DOWN * 1)
```

#### 清理
- FadeOut: hook, tri1, tri2, center_dot, question
- 保留: author (全局)

---

### Scene 2: 定义引入 (8-10秒)
**目的**: 明确"中心对称"的定义

#### 元素
1. 标题："什么是中心对称?"
2. 定义文字框
3. 三角形+对称中心演示

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 标题淡入 | `Write(title)` | 0.6s |
| 0.6s | 原三角形创建 | `Create(triangle_ABC)` | 1.0s |
| 1.6s | 对称中心O出现 | `FadeIn(dot_O), Flash(dot_O)` | 0.5s |
| 2.1s | 标注"对称中心O" | `FadeIn(label_O)` | 0.4s |
| 2.5s | 定义文字框淡入 | `FadeIn(definition_box)` | 0.8s |
| 3.3s | 等待阅读 | `Wait(1.5)` | 1.5s |
| 4.8s | 高亮关键词"180°" | `definition_box[key].set_color(YELLOW)` | 0.5s |
| 5.3s | 三角形旋转180° | `Rotate(triangle_ABC, PI, about=O)` | 2.0s |
| 7.3s | 对称三角形淡入（重合演示） | `FadeIn(triangle_sym, scale=1.05)` | 0.8s |
| 8.1s | 等待观察 | `Wait(1.0)` | 1.0s |

#### 具体内容
```python
# 标题
title = Text(
    "什么是中心对称?",
    font="Noto Sans CJK SC",
    font_size=36,
    color=WHITE
).move_to(UP * 5.5)

# 定义文字框
definition_texts = [
    Text("定义: 如果把一个图形绕某点", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    Text("旋转180°后能与另一个图形", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    Text("重合, 则这两个图形", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
    Text("关于这点中心对称。", font="Noto Sans CJK SC", font_size=24, color=WHITE),
]
definition_box = VGroup(*definition_texts).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
definition_box.move_to(DOWN * 4.5)

# 背景框
bg_rect = SurroundingRectangle(
    definition_box, 
    color=COLOR_AUXILIARY, 
    buff=0.3, 
    corner_radius=0.1,
    fill_opacity=0.1
)

# 三角形
triangle_ABC = Polygon(
    self.A, self.B, self.C,
    color=COLOR_PRIMARY,
    stroke_width=3,
    fill_opacity=0.2
)

# 对称中心
dot_O = Dot(self.O, color=COLOR_CENTER, radius=0.12)
label_O = VGroup(
    Text("O", font="Noto Sans CJK SC", font_size=24, color=COLOR_CENTER),
    Text("对称中心", font="Noto Sans CJK SC", font_size=18, color=COLOR_CENTER)
).arrange(DOWN, buff=0.05).next_to(dot_O, DOWN, buff=0.2)

# 对称后的三角形 (虚线，用于重合演示)
triangle_sym = Polygon(
    self.A_sym, self.B_sym, self.C_sym,
    color=COLOR_SECONDARY,
    stroke_width=3,
    stroke_opacity=0.5
).set_style(stroke_dasharray=[5, 5])  # 使用虚线
```

#### 清理
- FadeOut: title, definition_box, bg_rect, triangle_ABC (旋转后), triangle_sym
- 保留: dot_O, label_O (缩小并半透明)

---

### Scene 3: 性质1 - 对应点连线过对称中心 (10-12秒)
**目的**: 演示"对应点的连线都经过对称中心"

#### 元素
1. 重新创建原三角形和对称三角形
2. 标注对应顶点 A↔A', B↔B', C↔C'
3. 绘制对应点连线
4. 验证连线过O

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 性质标题淡入 | `Write(property_title)` | 0.6s |
| 0.6s | 原三角形创建 | `Create(triangle_1)` | 0.8s |
| 1.4s | 对称三角形创建 | `Create(triangle_2)` | 0.8s |
| 2.2s | 标注顶点 A,B,C | `FadeIn(labels_ABC)` | 0.5s |
| 2.7s | 标注顶点 A',B',C' | `FadeIn(labels_sym)` | 0.5s |
| 3.2s | 说明文字: "找对应点" | `FadeIn(explain_1)` | 0.5s |
| 3.7s | 连线 AA' | `Create(line_AA)` | 0.8s |
| 4.5s | 闪烁O点（强调过O） | `Flash(dot_O)` | 0.4s |
| 4.9s | 连线 BB' | `Create(line_BB)` | 0.8s |
| 5.7s | 闪烁O点 | `Flash(dot_O)` | 0.4s |
| 6.1s | 连线 CC' | `Create(line_CC)` | 0.8s |
| 6.9s | 闪烁O点 | `Flash(dot_O)` | 0.4s |
| 7.3s | 性质文字淡入 | `FadeIn(property_text_1)` | 0.8s |
| 8.1s | 高亮所有连线 | `lines.animate.set_color(COLOR_HIGHLIGHT)` | 0.6s |
| 8.7s | 等待理解 | `Wait(1.5)` | 1.5s |

#### 具体内容
```python
# 性质标题
property_title = Text(
    "性质1: 对应点连线过对称中心",
    font="Noto Sans CJK SC",
    font_size=30,
    color=COLOR_HIGHLIGHT
).move_to(UP * 5.5)

# 三角形
triangle_1 = Polygon(self.A, self.B, self.C, 
                     color=COLOR_PRIMARY, stroke_width=3)
triangle_2 = Polygon(self.A_sym, self.B_sym, self.C_sym,
                     color=COLOR_SECONDARY, stroke_width=3)

# 顶点标签
label_A = Text("A", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.A, LEFT, buff=0.1)
label_B = Text("B", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.B, UP, buff=0.1)
label_C = Text("C", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.C, DOWN, buff=0.1)

label_A_sym = Text("A'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.A_sym, RIGHT, buff=0.1)
label_B_sym = Text("B'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.B_sym, DOWN, buff=0.1)
label_C_sym = Text("C'", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(self.C_sym, UP, buff=0.1)

labels_ABC = VGroup(label_A, label_B, label_C)
labels_sym = VGroup(label_A_sym, label_B_sym, label_C_sym)

# 对应点连线
line_AA = Line(self.A, self.A_sym, color=COLOR_CONNECTION, stroke_width=2)
line_BB = Line(self.B, self.B_sym, color=COLOR_CONNECTION, stroke_width=2)
line_CC = Line(self.C, self.C_sym, color=COLOR_CONNECTION, stroke_width=2)
lines = VGroup(line_AA, line_BB, line_CC)

# 说明文字
explain_1 = Text(
    "连接对应点...",
    font="Noto Sans CJK SC",
    font_size=24,
    color=GRAY_A
).move_to(DOWN * 4.5)

# 性质文字
property_text_1 = Text(
    "所有连线都经过对称中心O!",
    font="Noto Sans CJK SC",
    font_size=26,
    color=WHITE
).move_to(DOWN * 5.5)
```

#### 清理
- FadeOut: property_title, explain_1, property_text_1
- 保留: triangle_1, triangle_2, labels, lines, dot_O (用于下一场景)

---

### Scene 4: 性质2 - 对应点连线被对称中心平分 (10-12秒)
**目的**: 演示"且被对称中心平分"

#### 元素
1. 继承上一场景的元素
2. 标注线段长度 AO = OA'
3. 标注中点

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 性质标题淡入 | `Write(property_title_2)` | 0.6s |
| 0.6s | 高亮线段AA' | `line_AA.animate.set_stroke(width=4)` | 0.4s |
| 1.0s | 标注线段AO | `Create(brace_AO), FadeIn(label_AO)` | 0.8s |
| 1.8s | 标注线段OA' | `Create(brace_OA), FadeIn(label_OA)` | 0.8s |
| 2.6s | 等式: AO = OA' | `FadeIn(equation_1)` | 0.6s |
| 3.2s | 标记中点重合 | `Flash(dot_O, color=YELLOW)` | 0.5s |
| 3.7s | 切换到BB'线段 | `line_BB.animate.set_stroke(width=4)` | 0.5s |
| 4.2s | 快速标注BO=OB' | `FadeIn(braces_B)` | 0.6s |
| 4.8s | 切换到CC'线段 | `line_CC.animate.set_stroke(width=4)` | 0.5s |
| 5.3s | 快速标注CO=OC' | `FadeIn(braces_C)` | 0.6s |
| 5.9s | 性质总结文字 | `FadeIn(property_text_2)` | 0.8s |
| 6.7s | 公式: OA=OA', 且O在AA'上 | `FadeIn(formula_box)` | 0.8s |
| 7.5s | 等待理解 | `Wait(2.0)` | 2.0s |

#### 具体内容
```python
# 性质标题
property_title_2 = Text(
    "性质2: 对称中心平分连线",
    font="Noto Sans CJK SC",
    font_size=30,
    color=COLOR_HIGHLIGHT
).move_to(UP * 5.5)

# 大括号和标签 (线段AA')
brace_AO = Brace(Line(self.A, self.O), direction=normalize(np.array([-(self.O[1]-self.A[1]), self.O[0]-self.A[0], 0])), color=YELLOW)
label_AO = brace_AO.get_text("AO", font_size=20)

brace_OA = Brace(Line(self.O, self.A_sym), direction=normalize(np.array([-(self.O[1]-self.A[1]), self.O[0]-self.A[0], 0])), color=YELLOW)
label_OA = brace_OA.get_text("OA'", font_size=20)

# 等式
equation_1 = MathTex(r"AO = OA'", font_size=32, color=YELLOW).move_to(DOWN * 4)

# 性质文字
property_text_2 = Text(
    "对称中心是对应点连线的中点!",
    font="Noto Sans CJK SC",
    font_size=26,
    color=WHITE
).move_to(DOWN * 5.5)

# 公式框
formula_box = VGroup(
    Text("通用公式:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
    MathTex(r"OA = OA'", font_size=28),
    Text("且 O 在线段 AA' 上", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
).arrange(DOWN, buff=0.2).move_to(DOWN * 6.5)
```

#### 清理
- FadeOut: 所有元素（准备切换场景风格）
- 保留: author (全局)

---

### Scene 5: 应用1 - 中心对称图形（字母） (8-10秒)
**目的**: 展示实际应用：哪些字母/图形是中心对称的

#### 元素
1. 标题："哪些图形是中心对称图形?"
2. 字母展示: N, S, Z (中心对称), A, B, E (非中心对称)
3. 旋转验证

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 标题淡入 | `Write(title)` | 0.6s |
| 0.6s | 说明文字 | `FadeIn(explain)` | 0.5s |
| 1.1s | 字母N淡入 | `FadeIn(letter_N)` | 0.4s |
| 1.5s | 旋转180°验证 | `Rotate(letter_N_copy, PI)` | 1.2s |
| 2.7s | 打勾标记 | `FadeIn(check_N)` | 0.3s |
| 3.0s | 字母S淡入 | `FadeIn(letter_S)` | 0.4s |
| 3.4s | 旋转验证 | `Rotate(letter_S_copy, PI)` | 1.2s |
| 4.6s | 打勾标记 | `FadeIn(check_S)` | 0.3s |
| 4.9s | 字母Z淡入 | `FadeIn(letter_Z)` | 0.4s |
| 5.3s | 旋转验证 | `Rotate(letter_Z_copy, PI)` | 1.2s |
| 6.5s | 打勾标记 | `FadeIn(check_Z)` | 0.3s |
| 6.8s | 字母A淡入 | `FadeIn(letter_A)` | 0.4s |
| 7.2s | 旋转验证（不重合） | `Rotate(letter_A_copy, PI)` | 1.0s |
| 8.2s | 打叉标记 | `FadeIn(cross_A)` | 0.3s |
| 8.5s | 总结文字 | `FadeIn(summary)` | 0.6s |
| 9.1s | 等待 | `Wait(1.0)` | 1.0s |

#### 具体内容
```python
# 标题
title = Text(
    "应用: 识别中心对称图形",
    font="Noto Sans CJK SC",
    font_size=36,
    color=WHITE
).move_to(UP * 6)

# 说明
explain = Text(
    "旋转180°后能与自己重合的图形",
    font="Noto Sans CJK SC",
    font_size=24,
    color=GRAY_A
).move_to(UP * 5.2)

# 字母 (使用Text对象)
letter_N = Text("N", font="Arial", font_size=80, color=COLOR_PRIMARY).move_to(UP * 2.5 + LEFT * 3)
letter_S = Text("S", font="Arial", font_size=80, color=COLOR_PRIMARY).next_to(letter_N, RIGHT, buff=1.5)
letter_Z = Text("Z", font="Arial", font_size=80, color=COLOR_PRIMARY).next_to(letter_S, RIGHT, buff=1.5)
letter_A = Text("A", font="Arial", font_size=80, color=GRAY).move_to(DOWN * 1 + LEFT * 1.5)

# 勾叉标记
check_N = Text("✓", font_size=40, color=GREEN).next_to(letter_N, DOWN, buff=0.3)
check_S = Text("✓", font_size=40, color=GREEN).next_to(letter_S, DOWN, buff=0.3)
check_Z = Text("✓", font_size=40, color=GREEN).next_to(letter_Z, DOWN, buff=0.3)
cross_A = Text("✗", font_size=40, color=RED).next_to(letter_A, DOWN, buff=0.3)

# 总结
summary = Text(
    "N, S, Z 是中心对称图形!",
    font="Noto Sans CJK SC",
    font_size=28,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 4.5)
```

#### 清理
- FadeOut: 所有元素
- 保留: author

---

### Scene 6: 应用2 - 平行四边形对角线互相平分 (10-12秒)
**目的**: 应用中心对称性质证明平行四边形对角线互相平分

#### 元素
1. 平行四边形ABCD
2. 对角线AC, BD
3. 交点O
4. 证明过程

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 标题淡入 | `Write(title)` | 0.6s |
| 0.6s | 平行四边形创建 | `Create(parallelogram)` | 1.0s |
| 1.6s | 标注顶点A,B,C,D | `FadeIn(labels)` | 0.5s |
| 2.1s | 绘制对角线AC | `Create(diag_AC)` | 0.8s |
| 2.9s | 绘制对角线BD | `Create(diag_BD)` | 0.8s |
| 3.7s | 标记交点O | `FadeIn(dot_O), Flash(dot_O)` | 0.5s |
| 4.2s | 说明: "平行四边形关于O中心对称" | `FadeIn(explain_1)` | 0.8s |
| 5.0s | 高亮A和C（对应点） | `labels[A,C].set_color(YELLOW)` | 0.5s |
| 5.5s | 高亮对角线AC | `diag_AC.animate.set_color(YELLOW)` | 0.4s |
| 5.9s | 标注AO=OC | `FadeIn(brace_AO_OC)` | 0.6s |
| 6.5s | 高亮B和D（对应点） | `labels[B,D].set_color(YELLOW)` | 0.5s |
| 7.0s | 高亮对角线BD | `diag_BD.animate.set_color(YELLOW)` | 0.4s |
| 7.4s | 标注BO=OD | `FadeIn(brace_BO_OD)` | 0.6s |
| 8.0s | 结论文字 | `FadeIn(conclusion)` | 0.8s |
| 8.8s | 等待 | `Wait(1.5)` | 1.5s |

#### 具体内容
```python
# 标题
title = Text(
    "应用: 平行四边形对角线互相平分",
    font="Noto Sans CJK SC",
    font_size=32,
    color=WHITE
).move_to(UP * 6)

# 平行四边形
parallelogram = Polygon(
    self.P1, self.P2, self.P3, self.P4,
    color=COLOR_PRIMARY,
    stroke_width=3
)

# 顶点标签
label_P1 = Text("A", font="Noto Sans CJK SC", font_size=22).next_to(self.P1, LEFT)
label_P2 = Text("B", font="Noto Sans CJK SC", font_size=22).next_to(self.P2, UP)
label_P3 = Text("C", font="Noto Sans CJK SC", font_size=22).next_to(self.P3, RIGHT)
label_P4 = Text("D", font="Noto Sans CJK SC", font_size=22).next_to(self.P4, DOWN)
labels = VGroup(label_P1, label_P2, label_P3, label_P4)

# 对角线
diag_AC = Line(self.P1, self.P3, color=COLOR_CONNECTION, stroke_width=2)
diag_BD = Line(self.P2, self.P4, color=COLOR_CONNECTION, stroke_width=2)

# 交点
dot_O = Dot(self.diag_center, color=COLOR_CENTER, radius=0.1)
label_O = Text("O", font="Noto Sans CJK SC", font_size=20).next_to(dot_O, DOWN*0.5+RIGHT*0.5, buff=0.05)

# 说明
explain_1 = Text(
    "平行四边形关于对角线交点中心对称",
    font="Noto Sans CJK SC",
    font_size=22,
    color=GRAY_A
).move_to(DOWN * 4.5)

# 结论
conclusion = VGroup(
    Text("根据中心对称性质:", font="Noto Sans CJK SC", font_size=24, color=WHITE),
    MathTex(r"AO = OC,\quad BO = OD", font_size=28, color=COLOR_HIGHLIGHT),
    Text("对角线互相平分!", font="Noto Sans CJK SC", font_size=24, color=COLOR_HIGHLIGHT)
).arrange(DOWN, buff=0.2).move_to(DOWN * 5.5)
```

#### 清理
- FadeOut: 所有元素
- 保留: author

---

### Scene 7: 总结与关注 (6-8秒)
**目的**: 总结知识点，引导关注

#### 元素
1. 核心知识点总结卡片
2. 关注提示
3. 装饰动画

#### 动画序列
| 时间轴 | 动作 | 代码参考 | 运行时长 |
|--------|------|---------|---------|
| 0.0s | 总结标题淡入 | `Write(summary_title)` | 0.6s |
| 0.6s | 知识卡片1滑入 | `card_1.animate.shift(RIGHT*10)` | 0.5s |
| 1.1s | 知识卡片2滑入 | `card_2.animate.shift(RIGHT*10)` | 0.5s |
| 1.6s | 知识卡片3滑入 | `card_3.animate.shift(RIGHT*10)` | 0.5s |
| 2.1s | 等待阅读 | `Wait(1.5)` | 1.5s |
| 3.6s | 作者信息放大 | `author.animate.scale(1.5).move_to(UP*2)` | 0.6s |
| 4.2s | 关注文字淡入 | `FadeIn(follow_text)` | 0.6s |
| 4.8s | 图形装饰旋转 | `Rotate(decorations, PI)` | 1.2s |
| 6.0s | 等待 | `Wait(1.0)` | 1.0s |

#### 具体内容
```python
# 总结标题
summary_title = Text(
    "中心对称 - 核心要点",
    font="Noto Sans CJK SC",
    font_size=40,
    color=GOLD
).move_to(UP * 6)

# 知识卡片
card_1 = VGroup(
    Circle(radius=0.2, color=COLOR_PRIMARY, fill_opacity=1),
    Text("定义: 旋转180°重合", font="Noto Sans CJK SC", font_size=24, color=WHITE)
).arrange(RIGHT, buff=0.3).move_to(UP * 3).shift(LEFT * 10)

card_2 = VGroup(
    Circle(radius=0.2, color=COLOR_SECONDARY, fill_opacity=1),
    Text("性质: 对应点连线过对称中心且被平分", 
         font="Noto Sans CJK SC", font_size=22, color=WHITE)
).arrange(RIGHT, buff=0.3).move_to(UP * 1.5).shift(LEFT * 10)

card_3 = VGroup(
    Circle(radius=0.2, color=COLOR_HIGHLIGHT, fill_opacity=1),
    Text("应用: 平行四边形、字母N/S/Z", 
         font="Noto Sans CJK SC", font_size=22, color=WHITE)
).arrange(RIGHT, buff=0.3).move_to(ORIGIN).shift(LEFT * 10)

# 关注文字
follow_text = Text(
    "关注我, 学更多几何技巧!",
    font="Noto Sans CJK SC",
    font_size=32,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 2)

# 装饰图形（小三角形旋转）
decorations = VGroup(*[
    Polygon(ORIGIN, RIGHT*0.3, UP*0.3, 
            color=COLOR_PRIMARY, fill_opacity=0.6)
    .scale(0.4)
    .move_to(follow_text.get_center() + 
             1.5*np.array([np.cos(i*PI/3), np.sin(i*PI/3), 0]))
    for i in range(6)
])
```

#### 清理
- FadeOut: 全部元素
- 黑屏结束

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author | Scene 1 | Scene 7 | 全局保留 |
| triangle_ABC (原) | Scene 2 | Scene 2 | 单场景使用 |
| triangle_sym (对称) | Scene 2 | Scene 2 | 单场景使用 |
| dot_O (对称中心) | Scene 2 | Scene 4 | 多场景保留 |
| triangle_1 | Scene 3 | Scene 4 | 两场景共用 |
| triangle_2 | Scene 3 | Scene 4 | 两场景共用 |
| lines (连线) | Scene 3 | Scene 4 | 两场景共用 |
| letters (字母) | Scene 5 | Scene 5 | 单场景使用 |
| parallelogram | Scene 6 | Scene 6 | 单场景使用 |
| summary_cards | Scene 7 | Scene 7 | 单场景使用 |

---

## 时长分配总结

| 场景 | 预计时长 | 累计时长 |
|------|---------|---------|
| Scene 1: 开场 | 4s | 4s |
| Scene 2: 定义 | 9s | 13s |
| Scene 3: 性质1 | 10s | 23s |
| Scene 4: 性质2 | 10s | 33s |
| Scene 5: 应用1（字母） | 10s | 43s |
| Scene 6: 应用2（平行四边形） | 10s | 53s |
| Scene 7: 总结 | 7s | 60s |

**总时长**: 约 60 秒 ✓ (符合TikTok短视频要求)

---

## 技术注意事项

### 1. 坐标系安全边界
- 主内容区: y ∈ [-3, +5.5]
- 顶部标题: y ∈ [+5.5, +7]
- 底部说明: y ∈ [-6, -3]
- 横向: x ∈ [-4, +4]

### 2. 字体使用
- 中文: `font="Noto Sans CJK SC"` 或 `font="SimHei"`
- 英文/数学: MathTex 或 Text (Arial)
- 避免 MathTex 中使用中文 (会报错)

### 3. 虚线绘制
```python
# ✓ 正确
DashedLine(start, end, dash_length=0.1)
# 或
line.set_style(stroke_dasharray=[5, 5])  # 在新版本中测试
```

### 4. 旋转动画
```python
# 绕点O旋转180°
self.play(
    Rotate(obj, angle=PI, about_point=self.O),
    run_time=2.0
)
```

### 5. 对称点计算
```python
# 关于点O对称
A_sym = 2 * O - A
```

---

## 质量检查清单

运行前:
- [x] 所有几何点在 `setup_geometry()` 中计算
- [x] 使用 `verify_geometry()` 验证
- [x] 中文用 Text(), 数学用 MathTex()
- [x] 所有坐标在安全边界内
- [x] 元素生命周期明确

渲染后检查:
- [ ] 无元素溢出
- [ ] 文字清晰可读
- [ ] 动画流畅
- [ ] 难点有足够停留
- [ ] 开头钩子 + 结尾关注

---

**脚本文件名**: `central_symmetry.py`
**渲染命令**: 
```bash
# 快速预览
manim -pql central_symmetry.py CentralSymmetry

# 高质量渲染
manim -qh central_symmetry.py CentralSymmetry
```