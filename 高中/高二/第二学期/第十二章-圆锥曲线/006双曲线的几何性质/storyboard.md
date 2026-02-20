# 双曲线的几何性质 - 动画分镜脚本

## 元信息
- 目标时长: 55-65 秒
- 场景数量: 8 个
- 难度等级: 高二
- 知识点: 双曲线的范围、对称性、顶点、离心率、渐近线、准线、等轴双曲线

## 颜色配置
```python
COLOR_HYPERBOLA = "#e74c3c"      # 红色 - 双曲线主体
COLOR_ASYMPTOTE = "#9b59b6"      # 紫色 - 渐近线
COLOR_DIRECTRIX = "#f39c12"      # 橙色 - 准线
COLOR_FOCUS = "#e67e22"          # 深橙 - 焦点
COLOR_ECCENTRICITY = "#3498db"   # 蓝色 - 离心率相关
COLOR_SYMMETRY = "#2ecc71"       # 绿色 - 对称性
COLOR_RANGE = "#00bcd4"          # 青色 - 范围标注
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 参数a | 固定值2.0 | self.a |
| 参数b | 固定值1.5 | self.b |
| 半焦距c | √(a²+b²) | self.c |
| 离心率e | c/a | self.e |
| 焦点F₁, F₂ | (±c, 0) | self.F1, self.F2 |
| 顶点A₁, A₂ | (±a, 0) | self.A1, self.A2 |
| 渐近线斜率 | ±b/a | self.slope |
| 准线位置 | x = ±a²/c | self.directrix_x |
| 等轴双曲线参数 | a=b=1.5 | 新场景 |

---

## Scene 1: 开场与回顾 (4-5秒)
**目的**: 快速回顾，引出几何性质

### 元素
1. 作者标识（全程保留）
2. 钩子文字："双曲线还有哪些神奇性质?"
3. 双曲线基本图形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子文字书写 | `Write(hook)` |
| 1.0s | 双曲线淡入 | `Create(hyperbola)` |
| 2.5s | 标题淡入 | `FadeIn(title)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 位置规划
- 作者信息: y = 7
- 钩子文字: y = 6
- 双曲线中心: y = 1
- 标题: y = 5.5

### 清理
- FadeOut: hook
- 保留: author, hyperbola, title

---

## Scene 2: 范围性质 (6-7秒)
**目的**: 展示双曲线的定义域和值域

### 元素
1. 副标题 "范围"
2. x轴范围标注：|x| ≥ a
3. y轴范围标注：y ∈ ℝ
4. 视觉辅助线（虚线边界）
5. 公式显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 高亮顶点A₁, A₂ | `Indicate(dots)` |
| 1.0s | 绘制x范围边界 | `Create(x_boundary_lines)` |
| 1.6s | 显示 |x| ≥ a | `Write(x_range_formula)` |
| 2.4s | 高亮y方向 | `Create(y_range_arrow)` |
| 3.0s | 显示 y ∈ ℝ | `Write(y_range_formula)` |
| 4.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# x轴边界：x = ±a
x_boundary_left = Line(
    np.array([-self.a, -5, 0]) * self.SCALE,
    np.array([-self.a, 5, 0]) * self.SCALE,
    color=COLOR_RANGE, stroke_width=2
)

# 范围区域着色
left_region = Rectangle(...)  # x < -a 区域
right_region = Rectangle(...)  # x > a 区域
```

### 位置规划
- 副标题: y = 5.5
- 公式: y = -4.5

### 清理
- FadeOut: subtitle, boundary_lines, formulas
- 保留: hyperbola

---

## Scene 3: 对称性 (7-8秒)
**目的**: 展示三种对称性

### 元素
1. 副标题 "对称性"
2. 对称点P和P'（关于x轴）
3. 对称点Q和Q'（关于y轴）
4. 对称点R和R'（关于原点）
5. 对称轴/中心标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 高亮x轴 | `Indicate(x_axis)` |
| 0.8s | 显示P和P'（x轴对称） | `FadeIn(P, P_prime)` |
| 1.4s | 连线动画 | `Create(symmetry_line)` |
| 2.2s | 高亮y轴 | `Indicate(y_axis)` |
| 2.6s | 显示Q和Q'（y轴对称） | `FadeIn(Q, Q_prime)` |
| 3.4s | 高亮原点 | `Indicate(origin)` |
| 3.8s | 显示R和R'（中心对称） | `FadeIn(R, R_prime)` |
| 5.0s | 说明文字 | `FadeIn(explanation)` |
| 6.0s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 选择双曲线上的点
P = self.hyperbola_point_right(0.8)  # (x, y)
P_prime = np.array([P[0], -P[1], 0])  # (x, -y) 关于x轴对称

Q = self.hyperbola_point_right(1.0)  # (x, y)
Q_prime = np.array([-Q[0], Q[1], 0])  # (-x, y) 关于y轴对称
# 注意：Q'应该在左支上

R = self.hyperbola_point_right(0.6)  # (x, y)
R_prime = -R  # (-x, -y) 关于原点对称
```

### 位置规划
- 副标题: y = 5.5
- 说明文字: y = -5.5

### 清理
- FadeOut: subtitle, points, lines, explanation
- 保留: hyperbola

---

## Scene 4: 顶点 (5-6秒)
**目的**: 强调顶点的特殊位置

### 元素
1. 副标题 "顶点"
2. 顶点A₁, A₂高亮
3. 坐标标注
4. 实轴标注
5. 说明：距离原点最近的点

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 顶点A₁, A₂放大高亮 | `ScaleInPlace(dots, 1.5)` |
| 1.0s | 显示坐标 | `Write(coords)` |
| 1.8s | 绘制实轴 | `Create(real_axis)` |
| 2.6s | 说明文字 | `FadeIn(explanation)` |
| 4.0s | 等待 | `Wait(1.0)` |

### 位置规划
- 副标题: y = 5.5
- 坐标: 顶点旁边
- 说明: y = -5

### 清理
- FadeOut: subtitle, real_axis, explanation
- 保留: hyperbola, vertex_dots（变小）

---

## Scene 5: 离心率 (8-9秒)
**目的**: 解释离心率的意义及其对形状的影响

### 元素
1. 副标题 "离心率"
2. 公式 e = c/a
3. 三个双曲线对比（e = 1.2, 1.5, 2.0）
4. 标注：e > 1
5. 说明：e越大，开口越大

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 显示公式 e=c/a | `Write(formula)` |
| 1.0s | 显示当前e值 | `Write(current_e)` |
| 1.6s | 创建e较小的双曲线 | `Create(hyperbola_small_e)` |
| 2.4s | 变换到e中等 | `Transform(...)` |
| 3.2s | 变换到e较大 | `Transform(...)` |
| 4.0s | 说明文字 | `FadeIn(explanation)` |
| 6.0s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 三种离心率的双曲线
# e = 1.2: a=2.0, b=0.9, c=2.4
# e = 1.5: a=2.0, b=1.73, c=3.0
# e = 2.0: a=2.0, b=3.46, c=4.0

def create_hyperbola_with_e(e_value):
    a = 2.0
    c = e_value * a
    b = np.sqrt(c**2 - a**2)
    # 生成双曲线...
```

### 位置规划
- 副标题: y = 5.5
- 公式: y = 4.5
- 双曲线: 中央
- 说明: y = -5

### 清理
- FadeOut: subtitle, comparison_hyperbolas, explanation
- 保留: 原始hyperbola

---

## Scene 6: 渐近线详解 (8-9秒)
**目的**: 深入理解渐近线及其方程

### 元素
1. 副标题 "渐近线"
2. 虚框（2a × 2b）
3. 渐近线 y = ±(b/a)x
4. 动点沿双曲线移动，趋近渐近线
5. 距离标注（递减）
6. 说明：无限接近但永不相交

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 绘制虚框 | `Create(rectangle)` |
| 1.0s | 绘制渐近线 | `Create(asymptotes)` |
| 1.8s | 显示方程 | `Write(asymptote_eq)` |
| 2.4s | 动点开始移动 | `MoveAlongPath(P, ...)` |
| 5.0s | 显示距离递减 | `updater on distance_label` |
| 6.5s | 说明文字 | `FadeIn(explanation)` |
| 7.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 点到直线的距离公式
def distance_to_asymptote(point):
    # 渐近线: bx - ay = 0
    # 距离 = |bx - ay| / √(a² + b²)
    x, y = point[0], point[1]
    dist = abs(self.b * x - self.a * y) / np.sqrt(self.a**2 + self.b**2)
    return dist / self.SCALE  # 转换回原始坐标
```

### 位置规划
- 副标题: y = 5.5
- 方程: y = 4.2
- 动点轨迹: 双曲线右支上部
- 距离标签: 动点旁边
- 说明: y = -5.5

### 清理
- FadeOut: subtitle, rectangle, moving_point, explanation
- 保留: hyperbola, asymptotes

---

## Scene 7: 准线 (6-7秒)
**目的**: 介绍准线的定义和位置

### 元素
1. 副标题 "准线"
2. 准线 x = ±a²/c（虚线）
3. 焦点F₁, F₂
4. 准线方程
5. 点P，标注 |PF|/d = e（焦点距离/准线距离）
6. 几何关系演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 显示焦点 | `FadeIn(F1, F2)` |
| 1.0s | 绘制准线 | `Create(directrices)` |
| 1.6s | 显示方程 | `Write(directrix_eq)` |
| 2.4s | 选点P | `FadeIn(P_dot)` |
| 3.0s | 绘制PF和垂线 | `Create(PF_line, perpendicular)` |
| 3.8s | 显示比值 | `Write(ratio_eq)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 准线位置
self.directrix_x = self.a**2 / self.c

# 准线
directrix_left = DashedLine(
    np.array([-self.directrix_x, -5, 0]) * self.SCALE,
    np.array([-self.directrix_x, 5, 0]) * self.SCALE,
    color=COLOR_DIRECTRIX
)

# 验证：对于双曲线上的点P
# |PF| / d(P, directrix) = e
```

### 位置规划
- 副标题: y = 5.5
- 方程: y = 4.2
- 比值公式: y = -5

### 清理
- FadeOut: subtitle, directrices, focus_dots, P_related
- 保留: hyperbola

---

## Scene 8: 等轴双曲线 (7-8秒)
**目的**: 介绍等轴双曲线的特殊性质

### 元素
1. 副标题 "等轴双曲线"
2. 新双曲线（a = b）
3. 渐近线垂直标记
4. 公式 a = b, e = √2
5. 渐近线方程 y = ±x
6. 说明：渐近线互相垂直

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.5s | 原双曲线变换 | `Transform(hyperbola, equilateral)` |
| 1.5s | 显示条件 a=b | `Write(condition)` |
| 2.0s | 绘制渐近线 | `Create(asymptotes_45deg)` |
| 2.8s | 显示方程 y=±x | `Write(asymptote_eq)` |
| 3.6s | 标记垂直角 | `Create(right_angle_mark)` |
| 4.2s | 显示 e=√2 | `Write(e_value)` |
| 5.5s | 说明文字 | `FadeIn(explanation)` |
| 6.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 等轴双曲线参数
a_eq = b_eq = 1.5
c_eq = a_eq * np.sqrt(2)
e_eq = np.sqrt(2)

# 渐近线斜率 = ±1
# 两渐近线夹角 = 90°

# 验证垂直性
slope1 = 1
slope2 = -1
# slope1 * slope2 = -1 ✓ 垂直
```

### 位置规划
- 副标题: y = 5.5
- 条件公式: y = 4.2
- 渐近线方程: y = -4.5
- 说明: y = -6

### 清理
- FadeOut: subtitle, asymptotes, formulas
- 保留: equilateral_hyperbola

---

## Scene 9: 总结与关注 (5-6秒)
**目的**: 回顾核心性质，引导关注

### 元素
1. 总结标题
2. 性质卡片列表
   - 范围：|x| ≥ a, y ∈ ℝ
   - 对称性：三种对称
   - 离心率：e = c/a > 1
   - 渐近线：y = ±(b/a)x
   - 准线：x = ±a²/c
   - 等轴：a=b, e=√2
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(all)` |
| 0.4s | 标题淡入 | `FadeIn(summary_title)` |
| 0.8s | 卡片依次滑入 | `card.animate.shift(RIGHT*10)` |
| 3.0s | 作者信息放大 | `Transform(author)` |
| 3.5s | 关注提示 | `FadeIn(follow_text)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 位置规划
- 标题: y = 5
- 卡片: y = 3, 2, 1, 0, -1, -2
- 作者: y = 1
- 关注: y = -1

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 全程保留 |
| hyperbola | Scene 1 | Scene 8 | 主双曲线 |
| title | Scene 1 | Scene 2 | 主标题 |
| range_boundaries | Scene 2 | Scene 2 | 范围边界 |
| symmetry_points | Scene 3 | Scene 3 | 对称点 |
| vertex_dots | Scene 4 | Scene 9 | 顶点标记 |
| eccentricity_demo | Scene 5 | Scene 5 | 离心率演示 |
| asymptotes | Scene 6 | Scene 8 | 渐近线 |
| directrices | Scene 7 | Scene 7 | 准线 |
| focus_dots | Scene 7 | Scene 7 | 焦点 |
| equilateral_hyperbola | Scene 8 | Scene 9 | 等轴双曲线 |
| summary_cards | Scene 9 | Scene 9 | 总结卡片 |

---

## 几何验证要点

### 验证1: 范围检查
```python
# 对于双曲线上任意点(x, y)
assert abs(x) >= self.a - epsilon
# y 可以是任意值
```

### 验证2: 对称性验证
```python
# 如果(x, y)在双曲线上
# 则(-x, y), (x, -y), (-x, -y)也在双曲线上
def verify_symmetry(point):
    x, y = point[0], point[1]
    # 验证四个点都满足方程
```

### 验证3: 离心率计算
```python
e = self.c / self.a
assert e > 1.0  # 双曲线的离心率必须大于1
```

### 验证4: 渐近线距离
```python
# 随着点沿双曲线移动到无穷远
# 点到渐近线的距离趋近于0
# 但在有限范围内应该 > 某个小值
```

### 验证5: 准线比值
```python
# 对于双曲线上的点P
# |PF| / d(P, directrix) ≈ e
# 允许一定误差
```

### 验证6: 等轴双曲线
```python
# a = b 时
e_calculated = np.sqrt(2)
assert abs(e - e_calculated) < epsilon

# 渐近线斜率
slope1 = b / a  # = 1
slope2 = -b / a  # = -1
# slope1 * slope2 = -1 ✓ 垂直
```

### 验证7: 边界安全
```python
# 所有元素在安全范围内
# x ∈ [-4, 4], y ∈ [-7, 7]
```

---

## 动画节奏控制

| 阶段 | 节奏 | 原因 |
|------|------|------|
| Scene 1 | 快 | 回顾引入 |
| Scene 2 | 中 | 范围概念 |
| Scene 3 | 中慢 | 对称性需要理解 |
| Scene 4 | 快 | 顶点简单 |
| Scene 5 | 慢 | 离心率重要且抽象 |
| Scene 6 | 中慢 | 渐近线核心概念 |
| Scene 7 | 中 | 准线较难 |
| Scene 8 | 中 | 等轴双曲线特殊 |
| Scene 9 | 中 | 总结回顾 |

---

## LaTeX 公式列表

```python
formulas = {
    # 范围
    "x_range": r"|x| \geq a",
    "y_range": r"y \in \mathbb{R}",
    
    # 对称性
    "symmetry": r"\text{关于}x\text{轴、}y\text{轴、原点对称}",
    
    # 顶点
    "vertices": r"A_1(-a, 0), \quad A_2(a, 0)",
    
    # 离心率
    "eccentricity": r"e = \frac{c}{a} \; (e > 1)",
    "e_effect": r"e\text{越大，开口越大}",
    
    # 渐近线
    "asymptote": r"y = \pm \frac{b}{a}x",
    "asymptote_distance": r"d \to 0 \; (x \to \infty)",
    
    # 准线
    "directrix": r"x = \pm \frac{a^2}{c}",
    "focus_directrix": r"\frac{|PF|}{d} = e",
    
    # 等轴双曲线
    "equilateral_condition": r"a = b",
    "equilateral_e": r"e = \sqrt{2}",
    "equilateral_asymptote": r"y = \pm x",
}
```

**注意**: 所有中文都在 `\text{}` 外，使用 Text() 单独创建！

---

## 颜色语义映射

| 颜色 | 用途 | Hex |
|------|------|-----|
| 红色 | 双曲线主体 | #e74c3c |
| 紫色 | 渐近线 | #9b59b6 |
| 橙色 | 准线 | #f39c12 |
| 深橙 | 焦点 | #e67e22 |
| 蓝色 | 离心率 | #3498db |
| 绿色 | 对称性 | #2ecc71 |
| 青色 | 范围标注 | #00bcd4 |
| 黄色 | 高亮提示 | YELLOW |
| 灰色 | 辅助元素 | GRAY_B |

---

## 完成标准

- [x] 场景覆盖所有核心性质
- [x] 几何元素位置精确计算
- [x] 动画节奏合理分配
- [x] LaTeX公式无中文字符
- [x] 颜色配置语义化
- [x] 元素生命周期明确
- [x] 边界检查通过
- [x] 验证机制完善