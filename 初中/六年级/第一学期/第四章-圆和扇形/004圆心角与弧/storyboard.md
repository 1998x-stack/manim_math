# 圆心角与弧 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 7 个
- 难度等级: 小学六年级
- 核心知识点: 圆心角定义、弧的定义、圆心角与弧的关系、弧长计算公式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 主蓝色 - 圆
COLOR_ANGLE = "#e74c3c"         # 红色 - 圆心角
COLOR_ARC = "#f39c12"           # 橙色 - 弧
COLOR_HIGHLIGHT = YELLOW        # 高亮黄色
COLOR_AUXILIARY = GRAY_B        # 辅助灰色
COLOR_FORMULA = "#2ecc71"       # 绿色 - 公式
COLOR_COMPARISON = "#9b59b6"    # 紫色 - 对比元素
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | ORIGIN + UP*1.5 | self.center |
| 半径 | 2.0 单位 | self.radius |
| 圆 | Circle(radius) | self.circle |
| 角度点A | center + radius*(cos(30°), sin(30°)) | self.point_A |
| 角度点B | center + radius*(cos(120°), sin(120°)) | self.point_B |
| 圆心角度数 | 90° | self.angle_degrees |
| 弧起始角 | 30° | self.arc_start |
| 弧结束角 | 120° | self.arc_end |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 引出圆心角概念，抓住注意力

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "什么是圆心角？"
3. 一个圆（带问号）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.0s | 圆形从中心生长 | `GrowFromCenter(circle)` |
| 1.8s | 圆心点闪烁 | `FadeIn(center_dot, scale=1.5)` |
| 2.5s | 问号出现 | `FadeIn(question_mark)` |
| 3.5s | 等待 | `Wait(0.8)` |
| 4.3s | 问号淡出 | `FadeOut(question_mark)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: circle, center_dot, author_info

---

## Scene 2: 定义圆心角 (5-15秒)
**目的**: 清晰展示圆心角的定义

### 元素
1. 标题 "圆心角"
2. 定义文字
3. 两条半径（从圆心到圆周）
4. 圆心角弧形标记
5. 角度标签 "∠AOB"

### 几何计算
```python
# 圆心角顶点
self.O = self.center  # 圆心

# 两条半径的端点（圆周上）
angle_A = 30 * DEGREES  # 30度
angle_B = 120 * DEGREES  # 120度
self.A = self.center + self.radius * np.array([np.cos(angle_A), np.sin(angle_A), 0])
self.B = self.center + self.radius * np.array([np.cos(angle_B), np.sin(angle_B), 0])

# 圆心角大小
self.central_angle = 90  # 度
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` |
| 5.5s | 定义文字淡入 | `FadeIn(definition)` |
| 6.5s | 半径OA绘制 | `Create(radius_OA)` |
| 7.3s | 点A标注 | `FadeIn(label_A)` |
| 8.0s | 半径OB绘制 | `Create(radius_OB)` |
| 8.8s | 点B标注 | `FadeIn(label_B)` |
| 9.5s | 圆心角弧形标记出现 | `Create(angle_arc)` |
| 10.3s | 角度标签出现 | `FadeIn(angle_label)` |
| 11.5s | 说明文字 "顶点在圆心" | `FadeIn(explanation)` |
| 13.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, definition, explanation
- 保留: circle, center_dot, radius_OA, radius_OB, label_A, label_B, angle_arc, angle_label

---

## Scene 3: 定义弧 (15-25秒)
**目的**: 展示圆心角所对的弧

### 元素
1. 标题 "弧"
2. 定义文字 "圆心角所对的弧"
3. 弧高亮显示
4. 弧标记符号 "⌒"
5. 弧标签 "弧AB"

### 几何计算
```python
# 弧：从点A到点B的圆弧
arc_start_angle = 30 * DEGREES
arc_end_angle = 120 * DEGREES
arc_angle = arc_end_angle - arc_start_angle  # 90度

self.arc_AB = Arc(
    radius=self.radius,
    start_angle=arc_start_angle,
    angle=arc_angle,
    arc_center=self.center
)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 15.0s | 标题淡入 | `FadeIn(title_arc)` |
| 15.5s | 定义文字淡入 | `FadeIn(definition_arc)` |
| 16.5s | 弧高亮绘制 | `Create(arc_highlight)` |
| 18.0s | 弧标记符号出现 | `FadeIn(arc_symbol)` |
| 18.8s | 弧标签出现 | `FadeIn(arc_label)` |
| 20.0s | 箭头指示 "这就是弧" | `GrowArrow(arrow), FadeIn(hint)` |
| 22.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title_arc, definition_arc, arc_symbol, arrow, hint
- 保留: circle, center_dot, radius_OA, radius_OB, arc_highlight, arc_label

---

## Scene 4: 关系演示 - 角度与弧长 (25-40秒)
**目的**: 展示圆心角越大，弧越长

### 元素
1. 标题 "圆心角越大，弧越长"
2. 三个不同大小的圆心角（30°, 60°, 90°）
3. 对应的三条弧（颜色渐变）
4. 动态演示：角度增大，弧变长

### 几何计算
```python
# 三个圆心角
angles = [30, 60, 90]  # 度
colors = [BLUE, ORANGE, RED]

# 对应的弧
for i, angle in enumerate(angles):
    arc = Arc(
        radius=radius,
        start_angle=0,
        angle=angle * DEGREES,
        arc_center=center,
        color=colors[i]
    )
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 25.0s | 清理之前元素 | `FadeOut(previous_elements)` |
| 25.5s | 标题淡入 | `FadeIn(title_relationship)` |
| 26.5s | 30°圆心角+弧出现 | `Create(angle_30), Create(arc_30)` |
| 28.0s | 60°圆心角+弧出现 | `Create(angle_60), Create(arc_60)` |
| 29.5s | 90°圆心角+弧出现 | `Create(angle_90), Create(arc_90)` |
| 31.0s | 标注角度 | `FadeIn(labels)` |
| 32.5s | 动态演示：ValueTracker | `tracker.animate.set_value(0->90)` |
| 36.0s | 说明文字 "同圆中成正比" | `FadeIn(proportion_text)` |
| 38.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title_relationship, angle_30, angle_60, angle_90, arc_30, arc_60, arc_90, labels, proportion_text
- 保留: circle, center_dot

---

## Scene 5: 弧长公式推导 (40-55秒)
**目的**: 推导弧长计算公式

### 元素
1. 标题 "弧长公式"
2. 圆周长公式 C = 2πr
3. 360°对应整个圆周
4. n°对应的弧长推导
5. 最终公式

### 公式演变
```python
# Step 1: 圆周长
formula_1 = "C = 2πr"

# Step 2: 比例关系
formula_2 = "弧长 / 圆周长 = n° / 360°"

# Step 3: 代入
formula_3 = "弧长 = (n/360) × 2πr"

# Step 4: 简化（可选）
formula_4 = "l = (nπr) / 180"
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 40.0s | 标题淡入 | `FadeIn(title_formula)` |
| 41.0s | 圆周长公式书写 | `Write(formula_circumference)` |
| 42.5s | 360°标注在圆上 | `FadeIn(angle_360_label)` |
| 44.0s | 说明 "整圆对应360°" | `FadeIn(explanation_1)` |
| 46.0s | n°角度标注 | `Create(angle_n), FadeIn(n_label)` |
| 48.0s | 比例关系公式 | `Write(formula_proportion)` |
| 50.0s | 最终公式推导 | `TransformMatchingTex->Write(formula_final)` |
| 52.0s | 公式高亮 | `formula_final.animate.scale(1.2).set_color(YELLOW)` |
| 54.0s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title_formula, formula_circumference, angle_360_label, explanation_1, angle_n, n_label, formula_proportion
- 保留: formula_final, circle

---

## Scene 6: 实例计算 (55-68秒)
**目的**: 通过具体例子巩固知识

### 元素
1. 标题 "例题"
2. 题目：r=3, n=60°, 求弧长
3. 圆形示意图
4. 计算步骤
5. 答案

### 计算过程
```python
# 示例
r = 3
n = 60
C = 2 * π * r = 6π
l = (n/360) × C = (60/360) × 6π = π
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 55.0s | 公式移至顶部 | `formula_final.animate.move_to(UP*5).scale(0.7)` |
| 56.0s | 例题标题 | `FadeIn(example_title)` |
| 57.0s | 题目条件 | `Write(problem_text)` |
| 58.5s | 示意图绘制 | `Create(example_circle), Create(example_arc)` |
| 60.0s | 标注r=3, 60° | `FadeIn(r_label), FadeIn(angle_label_60)` |
| 61.5s | 计算步骤1 | `Write(step_1)` |
| 63.0s | 计算步骤2 | `Write(step_2)` |
| 64.5s | 答案高亮 | `answer.animate.set_color(YELLOW)` |
| 66.0s | 答案框 | `Create(answer_box)` |
| 67.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: example_title, problem_text, example_circle, example_arc, r_label, angle_label_60, step_1, step_2, answer, answer_box, formula_final
- 保留: author_info

---

## Scene 7: 总结与片尾 (68-85秒)
**目的**: 强化记忆，引导关注

### 元素
1. 核心知识点卡片
2. 公式回顾
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 68.0s | 知识点卡片1 "圆心角：顶点在圆心" | `FadeIn(card_1)` |
| 69.5s | 知识点卡片2 "弧：圆心角对应的圆周部分" | `FadeIn(card_2)` |
| 71.0s | 知识点卡片3 "角度↑ → 弧长↑" | `FadeIn(card_3)` |
| 72.5s | 公式卡片 "l = (n/360)×2πr" | `FadeIn(formula_card)` |
| 75.0s | 作者信息放大 | `Transform(author_info, author_big)` |
| 76.0s | 关注提示 | `FadeIn(follow_text)` |
| 78.0s | 圆形装饰旋转 | `Rotate(decorative_circles)` |
| 81.0s | 等待 | `Wait(2.0)` |
| 83.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- FadeOut: 所有元素

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 作者标识 |
| circle | Scene 1 | Scene 6 | 主圆 |
| center_dot | Scene 1 | Scene 5 | 圆心点 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |
| radius_OA | Scene 2 | Scene 3 | 半径OA |
| radius_OB | Scene 2 | Scene 3 | 半径OB |
| angle_arc | Scene 2 | Scene 3 | 圆心角标记 |
| arc_highlight | Scene 3 | Scene 4 | 弧高亮 |
| formula_final | Scene 5 | Scene 6 | 最终公式 |

---

## 特殊注意事项

### 1. 角度计算精确性
```python
# 使用弧度制进行计算
angle_radians = angle_degrees * DEGREES
# 或
angle_radians = np.radians(angle_degrees)

# 圆周上的点
point = center + radius * np.array([np.cos(angle_radians), np.sin(angle_radians), 0])
```

### 2. Arc 对象使用
```python
# Manim 的 Arc
arc = Arc(
    radius=2.0,
    start_angle=30*DEGREES,  # 起始角（弧度）
    angle=90*DEGREES,        # 角度大小（弧度，不是结束角！）
    arc_center=ORIGIN,
    color=ORANGE,
    stroke_width=4
)
```

### 3. 角度标记
```python
# 使用 Angle 类标记圆心角
angle_marker = Angle(
    line1,  # Line 对象
    line2,  # Line 对象
    radius=0.5,
    color=RED
)
```

### 4. 中文公式处理
```python
# ❌ 错误
MathTex(r"\text{弧长} = ...")

# ✅ 正确
arc_text = Text("弧长", font="Noto Sans CJK SC", font_size=24)
eq = MathTex("=")
formula = MathTex(r"\frac{n}{360} \times 2\pi r")
VGroup(arc_text, eq, formula).arrange(RIGHT, buff=0.2)
```

### 5. 坐标边界
- 主内容区域: y ∈ [-2, +4.5]
- 公式区域: y ∈ [-5, -2]
- 顶部作者: y = +7
- 避免元素超出 y=±8

### 6. 动画节奏
- 角度变化动画: 2-3秒（使用ValueTracker）
- 公式推导: 每步1.5-2秒
- 几何图形创建: 0.8-1.2秒
- 关键停留: 1.5-2秒

---

## 视觉设计要点

### 颜色语义
- **蓝色**: 圆本身
- **红色**: 圆心角
- **橙色**: 弧
- **黄色**: 强调和高亮
- **绿色**: 公式

### 尺寸比例
- 圆半径: 2.0 单位
- 圆心点: 0.08 半径
- 标签字号: 20-24
- 公式字号: 28-32

### 动画流畅性
- 避免突兀的跳跃
- 使用 smooth rate_func
- 适当的过渡时间
- 保持视觉连贯性