# 二次函数的应用 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 九年级
- 主题: 二次函数的实际应用 - 最值问题

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主抛物线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 顶点/最值点
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点标注
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_PROFIT = "#2ecc71"       # 绿色 - 利润线
COLOR_AXES = WHITE             # 白色 - 坐标轴
```

## 几何预计算清单

### 场景1-3：基础抛物线
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 抛物线 | y = -x² + 4x + 5 | self.parabola_basic |
| 顶点 | (-b/2a, f(-b/2a)) | self.vertex_basic |
| 对称轴 | x = -b/2a = 2 | self.axis_x |
| 最大值 | y_max = 9 | self.max_value |

### 场景4-6：实际应用（利润问题）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 利润函数 | P = -2x² + 20x - 30 | self.profit_func |
| 最优价格 | x = -20/(2×(-2)) = 5 | self.optimal_price |
| 最大利润 | P_max = 20 | self.max_profit |
| x轴交点 | 解P=0的根 | self.breakeven_points |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题："如何定价才能赚最多钱？"
3. 简单的价格-利润示意图

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 简单曲线出现 | `Create(curve_sketch)` | 1.0s |
| 2.1s | 标注"最高点" | `FadeIn(peak_label, scale=0.8)` | 0.5s |
| 2.6s | 等待理解 | `self.wait(1.4)` | 1.4s |

### 清理
- FadeOut: hook_text, curve_sketch, peak_label
- 保留: author_info

---

## Scene 2: 二次函数基础 (5-15秒)
**目的**: 复习二次函数的基本性质

### 元素
1. 坐标系 (x: -1 to 5, y: 0 to 10)
2. 抛物线: y = -x² + 4x + 5
3. 顶点标注
4. 对称轴虚线
5. 最值标注

### 几何计算
```python
# 抛物线顶点
a, b, c = -1, 4, 5
vertex_x = -b / (2*a)  # = 2
vertex_y = a * vertex_x**2 + b * vertex_x + c  # = 9
self.vertex_basic = np.array([vertex_x, vertex_y, 0])

# 对称轴
self.axis_line_start = np.array([vertex_x, 0, 0])
self.axis_line_end = np.array([vertex_x, 10, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 5.5s | 创建坐标系 | `Create(axes)` | 1.0s |
| 6.5s | 绘制抛物线 | `Create(parabola)` | 1.5s |
| 8.0s | 标注顶点 | `FadeIn(vertex_dot), Write(vertex_label)` | 0.8s |
| 8.8s | 对称轴出现 | `Create(axis_line)` | 0.8s |
| 9.6s | 公式显示 | `Write(formula)` | 1.0s |
| 10.6s | 最值说明 | `FadeIn(max_text)` | 0.6s |
| 11.2s | 等待理解 | `self.wait(1.8)` | 1.8s |

### 文字内容
- 标题: "二次函数 y = ax² + bx + c"
- 顶点标签: "顶点(2, 9)"
- 公式: "当 a < 0 时，在 x = -b/2a 处取最大值"
- 最值文本: "最大值 = 9"

### 清理
- FadeOut: title, formula, max_text
- 保留: axes, parabola (缩小), vertex_dot, axis_line

---

## Scene 3: 顶点公式推导 (15-25秒)
**目的**: 强化顶点坐标计算方法

### 元素
1. 通用公式展示
2. 示例计算动画
3. 步骤高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 15.0s | 通用公式 | `Write(general_formula)` | 1.0s |
| 16.0s | 标注a,b,c | `Indicate(a_part), Indicate(b_part), Indicate(c_part)` | 1.2s |
| 17.2s | 顶点x坐标公式 | `TransformMatchingTex(formula1, formula2)` | 1.0s |
| 18.2s | 代入数值 | `Write(calculation_step1)` | 0.8s |
| 19.0s | 计算结果 | `TransformMatchingTex(step1, step2)` | 0.8s |
| 19.8s | 顶点y坐标 | `Write(y_calc)` | 1.0s |
| 20.8s | 最终顶点 | `FadeIn(final_vertex, scale=1.2)` | 0.6s |
| 21.4s | 等待 | `self.wait(1.6)` | 1.6s |

### 公式内容
```
y = -x² + 4x + 5
a = -1, b = 4, c = 5
x顶点 = -b/2a = -4/(2×(-1)) = 2
y顶点 = -(2)² + 4(2) + 5 = 9
顶点: (2, 9)
```

### 清理
- FadeOut: 所有公式文本
- 保留: axes (保持在背景)

---

## Scene 4: 实际问题引入 (25-35秒)
**目的**: 引入利润最大化实例

### 元素
1. 问题文字
2. 数据表格
3. 散点图
4. 拟合曲线

### 问题描述
```
某商店销售商品：
- 进价：30元/件
- 定价：x元/件
- 每天销量：100 - 2x 件
求：如何定价使利润最大？
```

### 几何计算
```python
# 利润函数: P = (x-30)(100-2x) = -2x² + 160x - 3000
# 简化为: P = -2x² + 20x - 30 (缩放后便于显示)
a_profit = -2
b_profit = 20
c_profit = -30

# 最优价格
optimal_x = -b_profit / (2 * a_profit)  # = 5
optimal_y = a_profit * optimal_x**2 + b_profit * optimal_x + c_profit  # = 20

self.optimal_point = np.array([optimal_x, optimal_y, 0])

# 盈亏平衡点 (P = 0)
# -2x² + 20x - 30 = 0
# x = (5 ± √10)
discriminant = b_profit**2 - 4*a_profit*c_profit
x1 = (-b_profit + np.sqrt(discriminant)) / (2*a_profit)
x2 = (-b_profit - np.sqrt(discriminant)) / (2*a_profit)

self.breakeven_1 = np.array([x1, 0, 0])
self.breakeven_2 = np.array([x2, 0, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 25.0s | 问题标题 | `Write(problem_title)` | 0.8s |
| 25.8s | 问题详情 | `FadeIn(problem_details, shift=UP*0.3)` | 1.0s |
| 26.8s | 数据表格 | `Create(data_table)` | 1.2s |
| 28.0s | 等待阅读 | `self.wait(1.5)` | 1.5s |
| 29.5s | 表格淡出 | `FadeOut(problem_details, data_table)` | 0.5s |
| 30.0s | 建立坐标系 | `Create(profit_axes)` | 1.0s |
| 31.0s | 散点数据 | `FadeIn(scatter_dots, lag_ratio=0.1)` | 1.2s |
| 32.2s | 提示"用二次函数拟合" | `Write(hint_text)` | 0.8s |
| 33.0s | 等待 | `self.wait(1.0)` | 1.0s |

### 清理
- FadeOut: problem_title, hint_text, scatter_dots
- 保留: profit_axes

---

## Scene 5: 建立函数模型 (35-48秒)
**目的**: 展示如何建立二次函数模型

### 元素
1. 利润公式推导
2. 函数图像
3. 顶点计算
4. 最值标注

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 35.0s | 利润公式 | `Write(profit_formula_derivation)` | 1.5s |
| 36.5s | 简化公式 | `TransformMatchingTex(raw, simplified)` | 1.0s |
| 37.5s | 绘制曲线 | `Create(profit_parabola)` | 1.8s |
| 39.3s | 标注系数 | `FadeIn(coefficients_label)` | 0.7s |
| 40.0s | 计算顶点x | `Write(vertex_x_calc)` | 1.2s |
| 41.2s | 计算顶点y | `Write(vertex_y_calc)` | 1.2s |
| 42.4s | 顶点点标注 | `FadeIn(optimal_dot, scale=0.5), Flash(optimal_dot)` | 0.8s |
| 43.2s | 垂直线到轴 | `Create(vertical_line)` | 0.6s |
| 43.8s | 最值标签 | `Write(max_profit_label)` | 0.8s |
| 44.6s | 等待强化 | `self.wait(2.0)` | 2.0s |

### 公式内容
```
P = (售价 - 成本) × 销量
P = (x - 30)(100 - 2x)
P = -2x² + 160x - 3000

顶点: x = -160/(2×(-2)) = 40
      P_max = 200元
```

### 清理
- FadeOut: 所有公式，保留关键标注
- 保留: profit_axes, profit_parabola, optimal_dot

---

## Scene 6: 答案解读 (48-58秒)
**目的**: 解释实际意义

### 元素
1. 最优价格突出
2. 最大利润突出
3. 区间分析

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 48.0s | 答案框 | `Create(answer_box)` | 0.8s |
| 48.8s | 最优价格 | `Write(answer_price)` | 0.8s |
| 49.6s | 最大利润 | `Write(answer_profit)` | 0.8s |
| 50.4s | 价格区间 | `Create(range_arrow)` | 1.0s |
| 51.4s | 区间说明 | `Write(range_text)` | 1.2s |
| 52.6s | 盈亏点标注 | `FadeIn(breakeven_dots)` | 0.6s |
| 53.2s | 盈利区间高亮 | `Create(profit_zone_highlight)` | 0.8s |
| 54.0s | 总结 | `FadeIn(conclusion, scale=1.1)` | 1.0s |
| 55.0s | 等待 | `self.wait(2.0)` | 2.0s |

### 文字内容
- 答案价格: "最优定价: 40元"
- 答案利润: "最大利润: 200元/天"
- 区间说明: "定价在32-48元之间盈利"
- 结论: "二次函数帮你找到最优解！"

### 清理
- FadeOut: answer_box, range_arrow, range_text, profit_zone_highlight
- 保留: profit_parabola, optimal_dot (缩小)

---

## Scene 7: 片尾总结 (58-65秒)
**目的**: 总结要点，引导关注

### 元素
1. 三步法总结
2. 关键公式
3. 作者信息+关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 58.0s | 清空场景 | `FadeOut(VGroup(*self.mobjects))` | 0.8s |
| 58.8s | 总结标题 | `Write(summary_title)` | 0.6s |
| 59.4s | 步骤1 | `FadeIn(step1, shift=RIGHT)` | 0.5s |
| 59.9s | 步骤2 | `FadeIn(step2, shift=RIGHT)` | 0.5s |
| 60.4s | 步骤3 | `FadeIn(step3, shift=RIGHT)` | 0.5s |
| 60.9s | 关键公式 | `Write(key_formula)` | 0.8s |
| 61.7s | 作者信息放大 | `Transform(author_info, author_large)` | 0.6s |
| 62.3s | 关注提示 | `FadeIn(follow_text, scale=1.2)` | 0.6s |
| 62.9s | 图标动画 | `Rotate(icon_group)` | 1.0s |
| 63.9s | 最后等待 | `self.wait(1.1)` | 1.1s |

### 文字内容
```
总结标题: "二次函数应用三步法"
步骤1: "1. 建立函数模型"
步骤2: "2. 求顶点坐标 x=-b/2a"
步骤3: "3. 解释实际意义"
关键公式: "a<0→最大值  a>0→最小值"
关注: "关注我，掌握更多数学技巧！"
```

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 持续显示 |
| hook_text | Scene 1 | Scene 1 | 钩子 |
| axes (basic) | Scene 2 | Scene 3 | 基础坐标系 |
| parabola_basic | Scene 2 | Scene 3 | 基础抛物线 |
| profit_axes | Scene 4 | Scene 6 | 利润坐标系 |
| profit_parabola | Scene 5 | Scene 6 | 利润曲线 |
| optimal_dot | Scene 5 | Scene 6 | 最优点 |
| formulas_* | 各场景 | 当前场景 | 临时公式 |

---

## 验证检查清单

### 几何计算验证
- [ ] 顶点坐标计算正确: x = -b/2a
- [ ] 顶点y值计算正确: 代入函数
- [ ] 盈亏平衡点计算正确: 判别式、求根公式
- [ ] 所有点在坐标系范围内

### 坐标系配置
```python
# Scene 2-3: 基础抛物线
axes_basic = Axes(
    x_range=[-1, 5, 1],
    y_range=[0, 10, 2],
    x_length=6,
    y_length=8,
    axis_config={"include_numbers": True}
).shift(DOWN * 0.5)

# Scene 4-6: 利润函数
profit_axes = Axes(
    x_range=[0, 10, 2],
    y_range=[-40, 30, 10],
    x_length=7,
    y_length=8,
    axis_config={"include_numbers": True, "font_size": 20}
).shift(DOWN * 1)
```

### 动画节奏
- 简单动画: 0.5-0.8s
- 复杂动画: 1.0-1.5s
- 理解停留: 1.5-2.0s
- 总时长: ~65秒 ✓

### LaTeX安全性
- [ ] 使用 `r"..."` 原始字符串
- [ ] 中文用 Text()，数学用 MathTex()
- [ ] 度数用 `^\circ`
- [ ] 分数用 `\frac{}{}`

---

## 特殊注意事项

### 函数绘制
```python
# 使用 axes.plot() 而非直接 FunctionGraph
parabola = axes.plot(
    lambda x: -x**2 + 4*x + 5,
    x_range=[-0.5, 4.5],
    color=COLOR_PRIMARY
)
```

### 顶点标注定位
```python
# 确保标签不重叠
vertex_label = MathTex(r"(2, 9)", font_size=28, color=COLOR_SECONDARY)
vertex_label.next_to(vertex_dot, UR, buff=0.2)

# 如果重叠，调整为 DR 或其他方向
```

### 颜色一致性
- 主曲线: 蓝色 (#3498db)
- 顶点/最值: 红色 (#e74c3c)
- 重点强调: 黄色 (YELLOW)
- 辅助元素: 灰色 (GRAY_B)
- 利润相关: 绿色 (#2ecc71)

---

## 预期效果

1. **教学清晰度**: 从抽象到具体，步步深入
2. **视觉吸引力**: 色彩对比，动画流畅
3. **实用价值**: 真实问题，实际意义
4. **记忆点**: "三步法"、顶点公式
5. **互动性**: 钩子问题引起思考

---

## 备选方案

如果时间过长 (>70秒):
- 简化 Scene 3 (公式推导)
- 合并 Scene 5-6 (建模+解读)

如果需要更多内容:
- 添加第二个应用实例 (抛物线运动、面积问题等)
- 增加互动练习提示