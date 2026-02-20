# 双曲线定义与标准方程 - 动画分镜脚本

## 元信息
- 目标时长: 50-60 秒
- 场景数量: 7 个
- 难度等级: 高二
- 知识点: 双曲线的定义、标准方程、关系式

## 颜色配置
```python
COLOR_HYPERBOLA = "#e74c3c"      # 红色 - 双曲线主体
COLOR_FOCUS = "#f39c12"          # 橙色 - 焦点
COLOR_AXIS_REAL = "#3498db"      # 蓝色 - 实轴
COLOR_AXIS_IMAGINARY = "#2ecc71" # 绿色 - 虚轴
COLOR_ASYMPTOTE = "#9b59b6"      # 紫色 - 渐近线
COLOR_POINT_P = "#e91e63"        # 粉色 - 动点P
COLOR_DISTANCE = "#00bcd4"       # 青色 - 距离线
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 参数a | 固定值2.0 | self.a |
| 参数b | 固定值1.5 | self.b |
| 半焦距c | √(a²+b²) | self.c |
| 焦点F₁ | (-c, 0, 0) | self.F1 |
| 焦点F₂ | (c, 0, 0) | self.F2 |
| 顶点A₁ | (-a, 0, 0) | self.A1 |
| 顶点A₂ | (a, 0, 0) | self.A2 |
| 双曲线右支 | 参数方程 x=a*cosh(t), y=b*sinh(t) | ParametricFunction |
| 双曲线左支 | 参数方程 x=-a*cosh(t), y=b*sinh(t) | ParametricFunction |
| 渐近线1 | y = (b/a)x | Line |
| 渐近线2 | y = -(b/a)x | Line |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出双曲线

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "什么曲线有两个分支？"
3. 双曲线轮廓预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 双曲线淡入（半透明） | `Create(hyperbola_preview, run_time=1.5)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 位置规划
- 作者信息: y = 7
- 钩子文字: y = 6
- 双曲线中心: y = 2

### 清理
- FadeOut: hook_text
- 保留: hyperbola_preview (变半透明), author_info

---

## Scene 2: 双曲线定义 (10-12秒)
**目的**: 展示双曲线的几何定义

### 元素
1. 标题 "双曲线的定义"
2. 两个焦点 F₁(-c, 0), F₂(c, 0)
3. 动点 P
4. 距离线段 PF₁, PF₂
5. 距离标签
6. 定义公式 ||PF₁| - |PF₂|| = 2a

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 焦点F₁, F₂出现 | `FadeIn(F1_dot), FadeIn(F2_dot)` |
| 0.8s | 焦点标签 | `Write(F1_label), Write(F2_label)` |
| 1.2s | 动点P出现 | `FadeIn(P_dot)` |
| 1.6s | 绘制PF₁线段 | `Create(line_PF1)` |
| 2.0s | 绘制PF₂线段 | `Create(line_PF2)` |
| 2.4s | 显示距离标签 | `FadeIn(dist_label_1), FadeIn(dist_label_2)` |
| 3.0s | P点沿双曲线移动 | `MoveAlongPath(P, hyperbola, run_time=4)` + updater |
| 7.0s | 公式淡入 | `Write(definition_formula)` |
| 8.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 动点P的位置（参数方程）
def get_P_position(t):
    x = self.a * np.cosh(t)
    y = self.b * np.sinh(t)
    return np.array([x, y, 0]) * self.SCALE + self.OFFSET

# 距离差验证
dist_diff = abs(np.linalg.norm(P - F1) - np.linalg.norm(P - F2))
# 应该等于 2*a
```

### 位置规划
- 标题: y = 5.5
- 焦点F₁: (-c*SCALE, 2, 0)
- 焦点F₂: (c*SCALE, 2, 0)
- 动点P轨迹: 双曲线右支
- 公式: y = -4

### 清理
- FadeOut: title, P_dot, line_PF1, line_PF2, dist_labels
- 保留: F1_dot, F2_dot, F1_label, F2_label, definition_formula (移到顶部)

---

## Scene 3: 关键参数 a, b, c (8-10秒)
**目的**: 解释实半轴、虚半轴、半焦距

### 元素
1. 标题 "关键参数"
2. 实轴（长度2a）- 蓝色
3. 虚轴（长度2b）- 绿色
4. 焦距（长度2c）- 橙色
5. 参数标注 a, b, c
6. 关系式 c² = a² + b²

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 绘制实轴 | `Create(real_axis)` |
| 1.0s | 标注a | `FadeIn(a_brace), Write(a_label)` |
| 1.6s | 绘制虚轴 | `Create(imaginary_axis)` |
| 2.2s | 标注b | `FadeIn(b_brace), Write(b_label)` |
| 2.8s | 高亮焦距 | `Indicate(line_F1F2)` |
| 3.4s | 标注c | `FadeIn(c_brace), Write(c_label)` |
| 4.0s | 显示关系式 | `Write(relation_formula)` |
| 5.5s | 等待 | `Wait(1.5)` |

### 位置规划
- 实轴: y = 2, x ∈ [-a, a]
- 虚轴: x = 0, y ∈ [-b, b] （虚线）
- 关系式: y = -4

### 清理
- FadeOut: title, braces, some labels
- 保留: real_axis, imaginary_axis, relation_formula (移到角落)

---

## Scene 4: 标准方程（焦点在x轴）(10-12秒)
**目的**: 推导并展示标准方程

### 元素
1. 标题 "标准方程（焦点在x轴）"
2. 坐标系
3. 双曲线图形（完整，两支）
4. 标准方程 x²/a² - y²/b² = 1
5. 焦点坐标 F₁(-c, 0), F₂(c, 0)
6. 顶点坐标 A₁(-a, 0), A₂(a, 0)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 坐标系创建 | `Create(axes)` |
| 1.2s | 绘制双曲线右支 | `Create(hyperbola_right, run_time=1.5)` |
| 2.7s | 绘制双曲线左支 | `Create(hyperbola_left, run_time=1.5)` |
| 4.2s | 显示标准方程 | `Write(standard_eq)` |
| 5.5s | 标注焦点 | `Indicate(F1_dot), Indicate(F2_dot)` |
| 6.2s | 显示焦点坐标 | `FadeIn(focus_coords)` |
| 7.0s | 标注顶点 | `FadeIn(A1_dot), FadeIn(A2_dot)` |
| 7.6s | 显示顶点坐标 | `FadeIn(vertex_coords)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 双曲线右支参数方程
def hyperbola_right(t):
    x = self.a * np.cosh(t)
    y = self.b * np.sinh(t)
    return axes.c2p(x, y)

# 双曲线左支参数方程
def hyperbola_left(t):
    x = -self.a * np.cosh(t)
    y = self.b * np.sinh(t)
    return axes.c2p(x, y)

# t 范围: [0, 2.5] 或根据显示范围调整
```

### 位置规划
- 标题: y = 5.5
- 坐标系中心: y = 1.5
- 方程: y = -3.5
- 坐标标注: y = -5

### 清理
- FadeOut: title
- 保留: axes, hyperbola, standard_eq, focus/vertex dots

---

## Scene 5: 渐近线 (6-8秒)
**目的**: 展示双曲线的渐近线

### 元素
1. 标题 "渐近线"
2. 虚框（2a × 2b矩形）
3. 对角线（渐近线）
4. 渐近线方程 y = ±(b/a)x
5. 说明文字 "双曲线无限接近但不相交"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 绘制虚框 | `Create(rectangle)` |
| 1.2s | 绘制渐近线1 | `Create(asymptote_1)` |
| 1.8s | 绘制渐近线2 | `Create(asymptote_2)` |
| 2.4s | 显示方程 | `Write(asymptote_eq)` |
| 3.5s | 说明文字淡入 | `FadeIn(explanation)` |
| 5.0s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 渐近线斜率
slope = self.b / self.a

# 渐近线1: y = slope * x
# 渐近线2: y = -slope * x

# 确保渐近线延伸到边界
x_range = [-4.5, 4.5]
```

### 位置规划
- 标题: y = 5.5
- 虚框中心: 与坐标系原点重合
- 方程: y = -4
- 说明: y = -5.5

### 清理
- FadeOut: title, rectangle, explanation
- 保留: asymptote lines, asymptote_eq

---

## Scene 6: 焦点在y轴的情况 (5-6秒)
**目的**: 快速展示另一种标准方程

### 元素
1. 标题 "焦点在y轴"
2. 双曲线（旋转90度）
3. 标准方程 y²/a² - x²/b² = 1
4. 焦点 F₁(0, -c), F₂(0, c)
5. 顶点 A₁(0, -a), A₂(0, a)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(previous_elements)` |
| 0.5s | 标题淡入 | `FadeIn(title)` |
| 0.9s | 新双曲线创建 | `Create(hyperbola_y)` |
| 2.0s | 显示方程 | `Write(standard_eq_y)` |
| 3.0s | 标注焦点和顶点 | `FadeIn(dots_and_labels)` |
| 4.0s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 焦点在y轴的双曲线参数方程
def hyperbola_y_upper(t):
    x = self.b * np.sinh(t)
    y = self.a * np.cosh(t)
    return axes.c2p(x, y)

def hyperbola_y_lower(t):
    x = self.b * np.sinh(t)
    y = -self.a * np.cosh(t)
    return axes.c2p(x, y)
```

### 位置规划
- 标题: y = 5.5
- 方程: y = -4
- 标注: 左右两侧

### 清理
- FadeOut: most elements
- 保留: 用于总结的关键公式

---

## Scene 7: 总结与关注 (4-5秒)
**目的**: 回顾关键公式，引导关注

### 元素
1. 关键公式卡片
   - 定义: ||PF₁| - |PF₂|| = 2a
   - 方程: x²/a² - y²/b² = 1
   - 关系: c² = a² + b²
2. 作者信息（放大）
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(all)` |
| 0.4s | 公式卡片滑入 | `card.animate.shift(RIGHT*10)` |
| 1.5s | 作者信息放大 | `Transform(author_info, large)` |
| 2.2s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 3.5s | 等待 | `Wait(1.0)` |

### 位置规划
- 公式卡片: 中央偏上
- 作者信息: y = 1
- 关注提示: y = -1

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hyperbola_preview | Scene 1 | Scene 4 | 开场预览 |
| F1_dot, F2_dot | Scene 2 | Scene 6 | 焦点 |
| definition_formula | Scene 2 | Scene 7 | 定义公式 |
| real_axis | Scene 3 | Scene 6 | 实轴 |
| imaginary_axis | Scene 3 | Scene 6 | 虚轴 |
| relation_formula | Scene 3 | Scene 7 | c²=a²+b² |
| axes | Scene 4 | Scene 6 | 坐标系 |
| hyperbola_main | Scene 4 | Scene 6 | 主双曲线 |
| standard_eq | Scene 4 | Scene 7 | 标准方程 |
| asymptote_lines | Scene 5 | Scene 6 | 渐近线 |
| hyperbola_y | Scene 6 | Scene 6 | y轴双曲线 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 几何验证要点

### 验证1: 焦点位置
```python
assert abs(self.c - np.sqrt(self.a**2 + self.b**2)) < 1e-6
```

### 验证2: 双曲线上点的距离差
```python
# 对于双曲线上任意点P
dist_diff = abs(np.linalg.norm(P - F1) - np.linalg.norm(P - F2))
assert abs(dist_diff - 2*self.a) < 1e-6
```

### 验证3: 渐近线斜率
```python
slope_calculated = self.b / self.a
# 验证渐近线通过原点且斜率正确
```

### 验证4: 边界安全
```python
# 确保所有元素在安全范围内
# x ∈ [-4, 4], y ∈ [-7, 7]
```

---

## 动画节奏控制

| 阶段 | 节奏 | 原因 |
|------|------|------|
| Scene 1 | 快 | 吸引注意 |
| Scene 2 | 中慢 | 核心定义，需理解 |
| Scene 3 | 中 | 参数解释 |
| Scene 4 | 慢 | 标准方程推导 |
| Scene 5 | 快 | 补充知识 |
| Scene 6 | 快 | 变式对比 |
| Scene 7 | 中 | 总结回顾 |

---

## LaTeX 公式列表

```python
# 确保所有公式使用正确的LaTeX语法，避免Unicode字符

formulas = {
    "definition": r"||PF_1| - |PF_2|| = 2a",
    "standard_x": r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1",
    "standard_y": r"\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1",
    "relation": r"c^2 = a^2 + b^2",
    "asymptote": r"y = \pm \frac{b}{a}x",
    "focus_x": r"F_1(-c, 0), \quad F_2(c, 0)",
    "focus_y": r"F_1(0, -c), \quad F_2(0, c)",
    "vertex_x": r"A_1(-a, 0), \quad A_2(a, 0)",
    "vertex_y": r"A_1(0, -a), \quad A_2(0, a)",
}
```

---

## 颜色语义映射

| 颜色 | 用途 | Hex |
|------|------|-----|
| 红色 | 双曲线主体 | #e74c3c |
| 橙色 | 焦点 | #f39c12 |
| 蓝色 | 实轴 | #3498db |
| 绿色 | 虚轴 | #2ecc71 |
| 紫色 | 渐近线 | #9b59b6 |
| 粉色 | 动点P | #e91e63 |
| 青色 | 距离线 | #00bcd4 |
| 黄色 | 高亮提示 | YELLOW |
| 灰色 | 辅助元素 | GRAY_B |

---

## 完成标准

- [x] 所有场景时长控制在目标范围
- [x] 几何元素位置精确计算
- [x] 使用统一的颜色配置
- [x] LaTeX公式无中文字符
- [x] 边界检查通过
- [x] 元素生命周期明确
- [x] 动画节奏合理
- [x] 难点有足够停留时间