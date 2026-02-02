# 蒙日圆（椭圆垂直切线交点轨迹）- 动画分镜脚本

## 元信息
- 目标时长: 90-120 秒
- 场景数量: 8 个
- 难度等级: 高中数学（圆锥曲线）
- 核心概念: 蒙日圆定理

## 颜色配置
```python
COLOR_ELLIPSE = "#3498db"          # 蓝色 - 椭圆
COLOR_MONGE = "#e74c3c"            # 红色 - 蒙日圆
COLOR_TANGENT1 = "#2ecc71"         # 绿色 - 切线1
COLOR_TANGENT2 = "#f39c12"         # 橙色 - 切线2
COLOR_INTERSECTION = "#9b59b6"     # 紫色 - 交点T
COLOR_FORMULA = YELLOW             # 黄色 - 公式
COLOR_AUXILIARY = GRAY_B           # 灰色 - 辅助线
```

## 几何预计算清单

### 基础椭圆参数
| 元素 | 值/公式 | 存储变量 |
|------|---------|---------|
| 长半轴 a | 3.0 | self.a |
| 短半轴 b | 2.0 | self.b |
| 椭圆缩放 | 0.8 | self.ELLIPSE_SCALE |
| 椭圆偏移 | UP * 1.5 | self.ELLIPSE_OFFSET |

### 蒙日圆参数
| 元素 | 公式 | 说明 |
|------|------|------|
| 圆心O | (0, 0) | 椭圆中心 |
| 半径R | √(a²+b²) | R = √(9+4) = √13 ≈ 3.606 |
| 方程 | x²+y² = a²+b² | x²+y² = 13 |

### 关键点坐标（示例点）
| 点 | 数学定义 | 计算方法 |
|---|----------|---------|
| 交点T | 在蒙日圆上 | T在圆 x²+y²=13 上，如 T(3, 2) |
| 切点P | 在椭圆上 | 通过求解切线方程与椭圆联立 |
| 切点Q | 在椭圆上 | 通过求解切线方程与椭圆联立 |

### 切线斜率计算
从点T(x₀, y₀)作椭圆的两条切线，斜率k₁, k₂满足：
- 二次方程: (x₀²-a²)k² - 2x₀y₀k + (y₀²-b²) = 0
- 垂直条件: k₁·k₂ = -1
- 韦达定理: k₁·k₂ = (y₀²-b²)/(x₀²-a²) = -1
- 推导: y₀²-b² = -(x₀²-a²) → x₀²+y₀² = a²+b²

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
吸引注意力，提出神奇的几何问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题（动画文字）
3. 椭圆和蒙日圆同时出现

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 0.3s |
| 0.3s | 钩子主标题 | `Write(hook_main)` | 1.0s |
| 1.3s | 钩子副标题 | `FadeIn(hook_sub)` | 0.5s |
| 1.8s | 椭圆创建 | `Create(ellipse)` | 1.0s |
| 2.8s | 蒙日圆淡入 | `Create(monge_circle)` | 1.0s |
| 3.8s | 等待理解 | `Wait(1.2)` | 1.2s |

### 钩子文字内容
```
主标题: "椭圆的蒙日圆"
副标题: "两条垂直切线的交点在哪里?"
```

### 几何初始化
```python
# 椭圆
ellipse = Ellipse(
    width=2*self.a*self.SCALE,
    height=2*self.b*self.SCALE,
    color=COLOR_ELLIPSE,
    stroke_width=3
).move_to(self.OFFSET)

# 蒙日圆
R = np.sqrt(self.a**2 + self.b**2)
monge_circle = Circle(
    radius=R*self.SCALE,
    color=COLOR_MONGE,
    stroke_width=3
).move_to(self.OFFSET)
```

### 清理
- FadeOut: hook_main, hook_sub
- 保留: ellipse, monge_circle, author_info

---

## Scene 2: 问题演示 (5-15秒)

### 目的
直观展示垂直切线的交点轨迹

### 元素
1. 在蒙日圆上选取一点T
2. 从T作两条垂直切线
3. 动画展示切线垂直
4. 移动T，展示轨迹

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 5.0s | 点T出现 | `FadeIn(dot_T)` | 0.4s |
| 5.4s | 第一条切线 | `Create(tangent1)` | 0.8s |
| 6.2s | 第二条切线 | `Create(tangent2)` | 0.8s |
| 7.0s | 直角标记 | `FadeIn(right_angle)` | 0.5s |
| 7.5s | 强调垂直 | `Indicate(right_angle)` | 0.6s |
| 8.1s | T点移动动画 | `t_tracker.animate.set_value(2*PI)` | 4.0s |
| 12.1s | 等待观察 | `Wait(2.9)` | 2.9s |

### 关键代码
```python
# 使用 ValueTracker 实现T点动画
t_tracker = ValueTracker(0)

# always_redraw 动态更新
dot_T = always_redraw(lambda: Dot(
    self.point_on_monge_circle(t_tracker.get_value()),
    color=COLOR_INTERSECTION
))

tangent1 = always_redraw(lambda: self.create_tangent_line(
    self.point_on_monge_circle(t_tracker.get_value()), 
    slope_index=0
))

tangent2 = always_redraw(lambda: self.create_tangent_line(
    self.point_on_monge_circle(t_tracker.get_value()), 
    slope_index=1
))
```

### 清理
- 停止动画
- 保留: ellipse, monge_circle, 静止的切线和点T

---

## Scene 3: 核心结论展示 (15-25秒)

### 目的
明确蒙日圆的定义和公式

### 元素
1. 核心公式框
2. 圆心和半径标注
3. 几何意义说明

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 15.0s | 清理动画元素 | `FadeOut(tangents, dot_T)` | 0.5s |
| 15.5s | 标题淡入 | `Write(title_conclusion)` | 0.8s |
| 16.3s | 公式1 | `Write(formula_circle)` | 1.2s |
| 17.5s | 公式框 | `Create(formula_box)` | 0.5s |
| 18.0s | 圆心标注 | `FadeIn(center_O)` | 0.4s |
| 18.4s | 半径标注 | `Create(radius_line), Write(radius_label)` | 1.0s |
| 19.4s | 说明文字 | `FadeIn(explanation)` | 0.8s |
| 20.2s | 等待理解 | `Wait(4.8)` | 4.8s |

### 数学内容
```python
# 标题
title_conclusion = Text(
    "蒙日圆定理",
    font="Noto Sans CJK SC",
    font_size=40,
    color=COLOR_FORMULA
).move_to(UP * 6.5)

# 核心公式
formula_circle = MathTex(
    r"x^2 + y^2 = a^2 + b^2",
    font_size=36,
    color=COLOR_FORMULA
).move_to(UP * 5.5)

# 说明
explanation = VGroup(
    Text("圆心: 椭圆中心O", font="Noto Sans CJK SC", font_size=24),
    MathTex(r"R = \sqrt{a^2 + b^2}", font_size=26)
).arrange(DOWN, buff=0.3).move_to(DOWN * 5)
```

### 清理
- FadeOut: explanation
- 保留: ellipse, monge_circle, formula_box (移到左上角)

---

## Scene 4: 代数法证明 - Part 1 (25-40秒)

### 目的
展示代数法证明的前半部分

### 元素
1. 设定切线和交点
2. 写出切线方程
3. 引入垂直条件

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 25.0s | 方法标题 | `Write(method_title)` | 0.6s |
| 25.6s | 步骤1标题 | `FadeIn(step1_title)` | 0.4s |
| 26.0s | 设T点和切点 | 显示点和标签 | 1.0s |
| 27.0s | 切线方程1 | `Write(tangent_eq1)` | 1.2s |
| 28.2s | 切线方程2 | `Write(tangent_eq2)` | 1.2s |
| 29.4s | 步骤2标题 | `FadeIn(step2_title)` | 0.4s |
| 29.8s | 斜率定义 | `Write(slope_def)` | 1.0s |
| 30.8s | 垂直条件 | `Write(perpendicular_cond)` | 1.2s |
| 32.0s | 等待理解 | `Wait(8.0)` | 8.0s |

### 数学内容
```python
# 切线方程（椭圆标准形式）
tangent_eq1 = MathTex(
    r"l_1: \frac{x_1 x}{a^2} + \frac{y_1 y}{b^2} = 1",
    font_size=28,
    color=COLOR_TANGENT1
).move_to(UP * 4)

tangent_eq2 = MathTex(
    r"l_2: \frac{x_2 x}{a^2} + \frac{y_2 y}{b^2} = 1",
    font_size=28,
    color=COLOR_TANGENT2
).move_to(UP * 3)

# 斜率
slope_def = VGroup(
    MathTex(r"k_1 = -\frac{b^2 x_1}{a^2 y_1}", font_size=26),
    MathTex(r"k_2 = -\frac{b^2 x_2}{a^2 y_2}", font_size=26)
).arrange(RIGHT, buff=1.0).move_to(UP * 1.5)

# 垂直条件
perpendicular_cond = MathTex(
    r"k_1 \cdot k_2 = -1",
    font_size=32,
    color=COLOR_FORMULA
).move_to(ORIGIN)
```

### 清理
- FadeOut: 所有公式
- 保留: ellipse, monge_circle, formula_box

---

## Scene 5: 代数法证明 - Part 2 (40-55秒)

### 目的
完成代数推导，得出蒙日圆方程

### 元素
1. 代入斜率公式
2. 整理化简
3. 得到最终结果

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 40.0s | 回顾垂直条件 | `Write(perpendicular_cond)` | 0.6s |
| 40.6s | 代入斜率 | `Write(substitute_slopes)` | 1.5s |
| 42.1s | 化简提示 | `FadeIn(simplify_hint)` | 0.5s |
| 42.6s | 化简步骤1 | `TransformMatchingTex` | 1.2s |
| 43.8s | 化简步骤2 | `TransformMatchingTex` | 1.2s |
| 45.0s | 最终结果 | `Write(final_result)` | 1.5s |
| 46.5s | 结果框 | `Create(result_box)` | 0.5s |
| 47.0s | 闪烁强调 | `Circumscribe(result_box)` | 1.0s |
| 48.0s | 等待理解 | `Wait(7.0)` | 7.0s |

### 数学内容
```python
# 代入斜率
substitute_slopes = MathTex(
    r"\frac{b^4 x_1 x_2}{a^4 y_1 y_2} = -1",
    font_size=30
).move_to(UP * 4)

# 化简步骤
simplify_step1 = MathTex(
    r"x_1 x_2 = -\frac{a^4}{b^4} y_1 y_2",
    font_size=30
).move_to(UP * 2.5)

# 最终结果（推导过程简化）
final_result = MathTex(
    r"x_0^2 + y_0^2 = a^2 + b^2",
    font_size=36,
    color=COLOR_FORMULA
).move_to(DOWN * 4)
```

### 清理
- FadeOut: 推导步骤
- 保留: final_result (移到与开头的formula_box合并)

---

## Scene 6: 判别式法证明（更直接）(55-70秒)

### 目的
展示更简洁的判别式法证明

### 元素
1. 设过T的直线
2. 相切条件（判别式=0）
3. 韦达定理应用

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 55.0s | 方法2标题 | `Write(method2_title)` | 0.6s |
| 55.6s | 设直线方程 | `Write(line_eq)` | 1.0s |
| 56.6s | 联立椭圆 | `Write(combined_eq)` | 1.2s |
| 57.8s | 相切条件 | `Write(tangent_condition)` | 1.0s |
| 58.8s | 判别式=0 | `Write(discriminant_eq)` | 1.2s |
| 60.0s | 化简得m² | `TransformMatchingTex` | 1.0s |
| 61.0s | 代入m关系 | `Write(substitute_m)` | 1.2s |
| 62.2s | 整理为二次方程 | `Write(quadratic_eq)` | 1.2s |
| 63.4s | 韦达定理 | `Write(vieta_formula)` | 1.0s |
| 64.4s | 得出结论 | `Write(conclusion)` | 1.0s |
| 65.4s | 等待理解 | `Wait(4.6)` | 4.6s |

### 数学内容
```python
# 直线方程
line_eq = MathTex(
    r"y = kx + m, \quad m = y_0 - kx_0",
    font_size=28
).move_to(UP * 5)

# 相切条件
tangent_condition = MathTex(
    r"\Delta = 0 \Rightarrow m^2 = a^2 k^2 + b^2",
    font_size=28
).move_to(UP * 3)

# 二次方程
quadratic_eq = MathTex(
    r"(x_0^2 - a^2)k^2 - 2x_0 y_0 k + (y_0^2 - b^2) = 0",
    font_size=26
).move_to(UP * 1)

# 韦达定理
vieta_formula = MathTex(
    r"k_1 k_2 = \frac{y_0^2 - b^2}{x_0^2 - a^2} = -1",
    font_size=28
).move_to(DOWN * 1)

# 结论
conclusion = MathTex(
    r"x_0^2 + y_0^2 = a^2 + b^2",
    font_size=32,
    color=COLOR_FORMULA
).move_to(DOWN * 4)
```

### 清理
- FadeOut: 所有推导
- 保留: ellipse, monge_circle

---

## Scene 7: 几何意义和应用 (70-85秒)

### 目的
展示蒙日圆的几何意义和实际应用

### 元素
1. 圆与椭圆的位置关系
2. 外切矩形性质
3. 应用示例

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 70.0s | 标题 | `Write(geometric_title)` | 0.6s |
| 70.6s | 位置关系说明 | `FadeIn(position_text)` | 0.8s |
| 71.4s | 标注半径 | 高亮R和a的关系 | 1.0s |
| 72.4s | 外切矩形演示 | 创建矩形动画 | 2.0s |
| 74.4s | 矩形顶点标注 | 显示顶点在蒙日圆上 | 1.5s |
| 75.9s | 应用说明 | `FadeIn(application_text)` | 1.0s |
| 76.9s | 示例题目 | 显示判断题 | 2.0s |
| 78.9s | 等待理解 | `Wait(6.1)` | 6.1s |

### 数学内容
```python
# 位置关系
position_text = VGroup(
    Text("蒙日圆完全在椭圆外部", font="Noto Sans CJK SC", font_size=24),
    MathTex(r"R = \sqrt{a^2 + b^2} > a", font_size=26)
).arrange(DOWN, buff=0.3).move_to(UP * 5)

# 外切矩形性质
rectangle_property = Text(
    "外切矩形的顶点都在蒙日圆上",
    font="Noto Sans CJK SC",
    font_size=24,
    color=COLOR_FORMULA
).move_to(DOWN * 4)

# 应用示例
example = VGroup(
    Text("例: 判断点P(2,3)能否作", font="Noto Sans CJK SC", font_size=22),
    Text("椭圆的两条垂直切线", font="Noto Sans CJK SC", font_size=22)
).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 5.5)
```

### 清理
- FadeOut: 所有示例
- 保留: ellipse, monge_circle

---

## Scene 8: 总结和片尾 (85-120秒)

### 目的
总结要点，引导关注

### 元素
1. 核心公式回顾
2. 关键步骤总结
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 85.0s | 总结标题 | `Write(summary_title)` | 0.6s |
| 85.6s | 大号公式 | `Write(big_formula)` | 1.2s |
| 86.8s | 公式框 | `Create(formula_frame)` | 0.5s |
| 87.3s | 关键点1 | `FadeIn(key_point1)` | 0.6s |
| 87.9s | 关键点2 | `FadeIn(key_point2)` | 0.6s |
| 88.5s | 关键点3 | `FadeIn(key_point3)` | 0.6s |
| 89.1s | 装饰动画 | 椭圆和圆旋转 | 2.0s |
| 91.1s | 作者信息放大 | `author_info.animate.scale(2)` | 0.8s |
| 91.9s | ID显示 | `FadeIn(author_id)` | 0.5s |
| 92.4s | 关注提示 | `FadeIn(follow_text)` | 0.6s |
| 93.0s | 装饰旋转 | 小圆圈环绕 | 2.0s |
| 95.0s | 等待结束 | `Wait(25.0)` | 25.0s |

### 数学内容
```python
# 总结标题
summary_title = Text(
    "核心总结",
    font="Noto Sans CJK SC",
    font_size=40,
    color=GOLD
).move_to(UP * 6.5)

# 大号公式
big_formula = MathTex(
    r"x^2 + y^2 = a^2 + b^2",
    font_size=48,
    color=COLOR_FORMULA
).move_to(UP * 4.5)

# 关键点
key_point1 = Text("✓ 两条垂直切线交点轨迹", font="Noto Sans CJK SC", font_size=24).move_to(UP * 2)
key_point2 = Text("✓ 圆心在椭圆中心", font="Noto Sans CJK SC", font_size=24).move_to(UP * 1)
key_point3 = Text("✓ 半径 R = √(a²+b²)", font="Noto Sans CJK SC", font_size=24).move_to(ORIGIN)

# 关注提示
follow_text = Text(
    "关注我, 掌握圆锥曲线技巧!",
    font="Noto Sans CJK SC",
    font_size=30,
    color=COLOR_FORMULA
).move_to(DOWN * 5)
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 贯穿全程 |
| ellipse | Scene 1 | Scene 8 | 主椭圆 |
| monge_circle | Scene 1 | Scene 8 | 蒙日圆 |
| formula_box | Scene 3 | Scene 5 | 公式框 |
| tangent_lines | Scene 2 | Scene 2 | 动态切线 |
| dot_T | Scene 2 | Scene 2 | 交点T |

---

## 几何精确计算方案

### 椭圆参数
```python
a = 3.0  # 长半轴
b = 2.0  # 短半轴
```

### 蒙日圆
```python
R = np.sqrt(a**2 + b**2)  # R = √13 ≈ 3.606
```

### 从点T(x₀, y₀)作切线的斜率
```python
def calculate_tangent_slopes(x0, y0, a, b):
    """
    计算从点(x0, y0)到椭圆的两条切线斜率
    满足: (x0²-a²)k² - 2x0y0·k + (y0²-b²) = 0
    """
    A = x0**2 - a**2
    B = -2 * x0 * y0
    C = y0**2 - b**2
    
    if abs(A) < 1e-10:
        # A=0时，k = -C/B
        return [-C/B, None]  # 一条切线
    
    discriminant = B**2 - 4*A*C
    
    if discriminant < 0:
        return None  # 无切线
    
    k1 = (-B + np.sqrt(discriminant)) / (2*A)
    k2 = (-B - np.sqrt(discriminant)) / (2*A)
    
    return [k1, k2]
```

### 验证垂直性
```python
def verify_perpendicular(k1, k2):
    """验证两斜率的切线是否垂直"""
    product = k1 * k2
    return abs(product + 1) < 1e-6  # k1·k2 = -1
```

### 蒙日圆上的点
```python
def point_on_monge_circle(angle, R, offset):
    """
    参数方程: x = R·cos(θ), y = R·sin(θ)
    """
    x = R * np.cos(angle)
    y = R * np.sin(angle)
    return np.array([x, y, 0]) * SCALE + offset
```

---

## 动画节奏控制

### 时长分配
| 场景 | 时长 | 占比 |
|------|------|------|
| Scene 1: 开场 | 5s | 4% |
| Scene 2: 问题演示 | 10s | 8% |
| Scene 3: 核心结论 | 10s | 8% |
| Scene 4: 证明Part1 | 15s | 13% |
| Scene 5: 证明Part2 | 15s | 13% |
| Scene 6: 判别式法 | 15s | 13% |
| Scene 7: 几何意义 | 15s | 13% |
| Scene 8: 总结 | 35s | 29% |
| **总计** | **120s** | **100%** |

---

## 验证清单

### 几何验证
- [ ] 蒙日圆半径 R = √(a²+b²)
- [ ] 蒙日圆上任一点满足 x²+y² = a²+b²
- [ ] 从蒙日圆上的点作的两切线斜率满足 k₁·k₂ = -1
- [ ] 椭圆完全在蒙日圆内部

### 代码验证
- [ ] 所有坐标精确计算
- [ ] 中文使用 Text()
- [ ] 公式使用 MathTex()
- [ ] 所有元素在边界内
- [ ] 动画节奏合理