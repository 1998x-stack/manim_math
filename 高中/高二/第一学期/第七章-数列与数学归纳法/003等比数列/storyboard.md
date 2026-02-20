# 等比数列动画 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高二水平
- 内容: 等比数列的定义、通项公式、前n项和公式

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数列
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调公比
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键公式
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
COLOR_GEOMETRIC = "#9b59b6"    # 紫色 - 几何表示
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数列项位置 | 等间距分布 | self.term_positions |
| 公比箭头起点/终点 | 基于项位置 | self.arrow_points |
| 图形缩放比例 | q的幂次 | self.scale_factors |
| 坐标轴范围 | 基于数列范围 | self.axes_config |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力 + 引出等比数列概念

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题: "1, 2, 4, 8, 16... 规律是什么?"
3. 动态数字序列

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 数字序列依次出现 | `FadeIn(numbers, lag_ratio=0.3)` |
| 2.5s | 等待思考 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: author_info, number_sequence

---

## Scene 2: 定义与公比 (8-10秒)
**目的**: 展示等比数列定义和公比概念

### 元素
1. 标题: "等比数列 Geometric Sequence"
2. 定义文字
3. 数列项: a₁, a₂, a₃, a₄...
4. 公比箭头和标注

### 几何计算
```python
# 数列项位置 (横向排列, y=2)
term_positions = [
    np.array([-3, 2, 0]),
    np.array([-1, 2, 0]),
    np.array([1, 2, 0]),
    np.array([3, 2, 0])
]

# 公比箭头 (从第n项指向第n+1项)
arrow_1 = Arrow(term_positions[0] + RIGHT*0.3, term_positions[1] + LEFT*0.3)
# 标注位置在箭头上方
ratio_label_pos = (term_positions[0] + term_positions[1]) / 2 + UP*0.5
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.5s | 定义文字淡入 | `FadeIn(definition)` |
| 1.2s | 数列项依次出现 | `FadeIn(terms, lag_ratio=0.2)` |
| 2.5s | 公比箭头创建 | `GrowArrow(ratio_arrows)` |
| 3.2s | 公比标注 (×q) | `Write(ratio_labels)` |
| 4.5s | 高亮公式: aₙ₊₁/aₙ = q | `Indicate(formula)` |

### 清理
- FadeOut: definition
- 保留: title (缩小移到顶部), terms, ratio_arrows

---

## Scene 3: 通项公式推导 (10-12秒)
**目的**: 展示通项公式 aₙ = a₁ · q^(n-1) 的推导

### 元素
1. 推导步骤文字
2. 数学公式变换
3. 指数展示

### 几何计算
```python
# 公式位置 (居中, y=1)
formula_center = np.array([0, 1, 0])

# 推导步骤垂直排列
step_positions = [
    formula_center + UP*1.5,    # a₁
    formula_center + UP*0.5,    # a₂ = a₁·q
    formula_center + DOWN*0.5,  # a₃ = a₁·q²
    formula_center + DOWN*1.5   # aₙ = a₁·q^(n-1)
]
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示 a₁ | `Write(step1)` |
| 0.8s | 显示 a₂ = a₁·q | `TransformMatchingTex(step1, step2)` |
| 1.8s | 显示 a₃ = a₁·q² | `TransformMatchingTex(step2, step3)` |
| 2.8s | 显示 a₄ = a₁·q³ | `Write(step4)` |
| 3.8s | 省略号出现 | `FadeIn(dots)` |
| 4.5s | 通项公式框出 | `Create(box)` |
| 5.5s | 重点停留 | `Wait(2.0)` |

### 清理
- FadeOut: 所有推导步骤
- 保留: 通项公式框

---

## Scene 4: 几何可视化 (10-12秒)
**目的**: 用面积/长度可视化等比关系

### 元素
1. 正方形序列 (q=2时)
2. 面积标注
3. 几何增长动画

### 几何计算
```python
# 正方形序列 (q=2, 边长倍增)
# 基准边长
base_size = 0.5
squares = [
    Square(side_length=base_size * (2**i))
    for i in range(4)
]

# 位置计算 (横向排列, 底部对齐)
positions = []
x_start = -3
y_baseline = -2
for i, sq in enumerate(squares):
    x_pos = x_start + sum([base_size * (2**j) for j in range(i)]) + base_size * (2**i) / 2
    positions.append(np.array([x_pos, y_baseline + squares[i].height/2, 0]))
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 第一个正方形出现 | `FadeIn(square1, scale=0.5)` |
| 0.8s | 第二个正方形生长 | `GrowFromCenter(square2)` |
| 1.6s | 第三个正方形生长 | `GrowFromCenter(square3)` |
| 2.4s | 第四个正方形生长 | `GrowFromCenter(square4)` |
| 3.5s | 面积标注 | `FadeIn(area_labels)` |
| 4.5s | 公比关系箭头 | `Create(ratio_arrows)` |
| 6.0s | 强调几何倍增 | `Indicate(squares)` |

### 清理
- FadeOut: squares, area_labels, arrows
- 保留: 无

---

## Scene 5: 前n项和公式 (q≠1) (12-15秒)
**目的**: 展示前n项和公式推导和应用

### 元素
1. 公式: Sₙ = a₁(1-qⁿ)/(1-q)
2. 推导方法提示 (错位相减法)
3. 数值示例

### 几何计算
```python
# 公式位置
sum_formula_pos = np.array([0, 2, 0])

# 推导步骤
derivation_steps = [
    "Sₙ = a₁ + a₁q + a₁q² + ... + a₁q^(n-1)",
    "qSₙ = a₁q + a₁q² + ... + a₁q^n",
    "Sₙ - qSₙ = a₁ - a₁q^n",
    "Sₙ(1-q) = a₁(1-q^n)"
]

step_positions = [sum_formula_pos + DOWN*i*0.8 for i in range(4)]
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题: 前n项和 | `Write(title)` |
| 0.8s | Sₙ表达式 | `Write(sum_expression)` |
| 1.8s | qSₙ表达式 | `Write(q_times_sum)` |
| 2.8s | 错位相减 | `TransformMatchingTex(...)` |
| 4.0s | 化简步骤 | `Write(simplification)` |
| 5.5s | 最终公式框出 | `Create(box)` |
| 7.0s | 重点停留 | `Wait(2.5)` |

### 清理
- FadeOut: 推导步骤
- 保留: 最终公式

---

## Scene 6: 特殊情况 q=1 (6-8秒)
**目的**: 讲解q=1时的特殊情况

### 元素
1. 条件: q = 1
2. 数列变为常数列
3. 公式: Sₙ = na₁

### 几何计算
```python
# 常数列可视化 (所有项高度相同)
constant_terms = [
    Rectangle(width=0.5, height=1.5, color=BLUE).move_to(np.array([-3+i, 0, 0]))
    for i in range(5)
]
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示 q=1 | `Write(condition)` |
| 0.8s | 常数列出现 | `FadeIn(constant_terms, lag_ratio=0.2)` |
| 2.0s | 公式推导 | `Write(formula)` |
| 3.5s | 强调简化公式 | `Indicate(formula)` |

### 清理
- FadeOut: constant_terms
- 保留: 公式

---

## Scene 7: 无穷等比数列 (可选, 8-10秒)
**目的**: 展示|q|<1时的无穷和

### 元素
1. 条件: |q| < 1
2. 几何级数收敛
3. 公式: S∞ = a₁/(1-q)

### 几何计算
```python
# 衰减可视化
decay_bars = [
    Rectangle(width=0.4, height=2*(0.5**i), color=PURPLE)
    .move_to(np.array([-3+i, -(0.5**i), 0]))
    for i in range(8)
]

# 收敛极限线
limit_line = DashedLine(LEFT*4 + DOWN*2, RIGHT*4 + DOWN*2, color=YELLOW)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示条件 |q|<1 | `Write(condition)` |
| 0.8s | 衰减柱状图 | `FadeIn(decay_bars, lag_ratio=0.15)` |
| 2.5s | 极限线出现 | `Create(limit_line)` |
| 3.5s | 无穷和公式 | `Write(infinity_formula)` |
| 5.0s | 收敛动画 | `Indicate(limit_line)` |

### 清理
- FadeOut: decay_bars, limit_line
- 保留: 公式

---

## Scene 8: 总结与片尾 (6-8秒)
**目的**: 总结核心公式 + 关注提示

### 元素
1. 核心公式汇总卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式卡片滑入 | `card.animate.shift(LEFT)` |
| 1.5s | 作者信息放大 | `Transform(author, large_author)` |
| 2.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 4.0s | 装饰动画 | `Rotate(decorations)` |
| 5.5s | 全部淡出 | `FadeOut(VGroup(...))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| number_sequence | Scene 1 | Scene 2 | 开场数字 |
| title | Scene 2 | Scene 8 | 缩小后保留 |
| terms | Scene 2 | Scene 4 | 数列项 |
| ratio_arrows | Scene 2 | Scene 3 | 公比箭头 |
| formula_box | Scene 3 | Scene 8 | 通项公式 |
| squares | Scene 4 | Scene 4 | 几何可视化 |
| sum_formula | Scene 5 | Scene 8 | 求和公式 |
| special_case | Scene 6 | Scene 7 | q=1情况 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键动画时机
- 难点停留: 通项公式推导 (2.0s), 前n项和公式 (2.5s)
- 过渡等待: 场景切换 (0.4-0.6s)
- 快速动画: 数字序列 (0.3s lag), 箭头生长 (0.5s)

## 边界安全检查
- 所有公式 y ∈ [-3, 5]
- 几何图形 x ∈ [-4, 4]
- 文字标注避免重叠 (buff ≥ 0.15)