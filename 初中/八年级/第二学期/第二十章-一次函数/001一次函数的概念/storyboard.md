# 一次函数概念 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等 (八年级)
- 核心概念: 从正比例函数到一次函数的扩展

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 一次函数主色
COLOR_SECONDARY = "#e74c3c"     # 红色 - 正比例函数
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_INTERCEPT = "#2ecc71"     # 绿色 - 截距
COLOR_SLOPE = "#f39c12"         # 橙色 - 斜率
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系 | Axes(x_range=[-4,4,1], y_range=[-3,3,1]) | self.axes |
| 正比例函数 y=2x | lambda x: 2*x | self.proportional_func |
| 一次函数 y=2x+1 | lambda x: 2*x+1 | self.linear_func |
| y=2x+1 的截距点 | (0, 1) | self.intercept_point |
| y=2x+1 在x=1处的点 | (1, 3) | self.point_on_line |
| 斜率三角形顶点 | (0,1), (1,1), (1,3) | self.slope_triangle_points |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出从正比例函数到一次函数的自然过渡

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 坐标系 + 正比例函数图像

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "正比例函数的图像一定过原点吗?" |
| 1.5s | 坐标系创建 | `Create(axes)` |
| 2.3s | 正比例函数y=2x图像绘制 | `Create(proportional_graph)` |
| 3.5s | 等待 | `Wait(0.8)` |

### 几何细节
- 坐标系: x∈[-4,4], y∈[-3,3], 位置 y∈[-2, 3]
- 正比例函数: 红色, stroke_width=3
- 原点标记: 红色小圆点

### 清理
- FadeOut: hook_text
- 保留: axes, proportional_graph, author_info

---

## Scene 2: 一次函数的引入 (5-7秒)
**目的**: 展示一次函数是正比例函数的推广

### 元素
1. 标题: "一次函数 y = kx + b"
2. 正比例函数图像 (红色)
3. 一次函数图像 (蓝色)
4. 平移箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` - 位置 UP*5.5 |
| 0.8s | 公式显示 | `FadeIn(formula)` - "y = kx + b (k ≠ 0)" |
| 1.5s | 正比例函数图像复制 | `proportional_copy = proportional_graph.copy()` |
| 2.0s | 平移动画 | `proportional_copy.animate.shift(UP*1)` |
| 3.2s | 变色为蓝色 | `proportional_copy.animate.set_color(COLOR_PRIMARY)` |
| 3.8s | 标注"向上平移1个单位" | `FadeIn(shift_label)` |
| 5.0s | 等待 | `Wait(1.2)` |

### 几何细节
- 平移距离: 精确计算为 axes.c2p(0, 1) - axes.c2p(0, 0)
- 平移箭头: 虚线箭头，从原点到(0,1)

### 清理
- FadeOut: shift_label, formula
- 保留: title, axes, proportional_graph, linear_graph (即平移后的图像)

---

## Scene 3: 截距的概念 (6-8秒)
**目的**: 讲解截距 b 的几何意义

### 元素
1. 小标题: "截距 b"
2. y轴截距点 (0, 1)
3. 截距标注
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题淡入 | `FadeIn(subtitle)` - "截距: 与y轴交点的纵坐标" |
| 0.5s | 正比例函数淡化 | `proportional_graph.animate.set_opacity(0.3)` |
| 1.0s | 截距点闪烁 | `Flash(intercept_dot)` + `FadeIn(intercept_dot)` |
| 1.6s | 虚线从截距点到y轴 | `Create(dashed_line_to_y)` |
| 2.2s | 截距值标注 | `FadeIn(intercept_label)` - "b = 1" |
| 2.8s | 说明文字 | `FadeIn(explanation)` - "当 x=0 时, y=b" |
| 4.0s | 高亮公式中的 b | `formula_b.animate.set_color(COLOR_INTERCEPT)` |
| 5.5s | 等待 | `Wait(1.5)` |

### 几何细节
- 截距点: axes.c2p(0, 1), 绿色圆点, radius=0.08
- 虚线: 从截距点水平延伸到y轴, DashedLine
- 标注位置: 截距点右侧, buff=0.3

### 清理
- FadeOut: subtitle, dashed_line_to_y, explanation
- 保留: intercept_dot, intercept_label, linear_graph

---

## Scene 4: 斜率的概念 (7-9秒)
**目的**: 讲解斜率 k 的几何意义

### 元素
1. 小标题: "斜率 k"
2. 斜率三角形
3. Δx, Δy 标注
4. 斜率计算过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题淡入 | `FadeIn(subtitle)` - "斜率: 直线的倾斜程度" |
| 0.6s | 在图像上取两点 | `FadeIn(point1, point2)` - (0,1) 和 (1,3) |
| 1.2s | 绘制斜率三角形 | `Create(slope_triangle)` |
| 2.0s | Δx 标注 | `FadeIn(delta_x_label)` - "Δx = 1" |
| 2.5s | Δy 标注 | `FadeIn(delta_y_label)` - "Δy = 2" |
| 3.2s | 斜率公式 | `Write(slope_formula)` - "k = Δy/Δx = 2/1 = 2" |
| 4.5s | 高亮公式中的 k | `formula_k.animate.set_color(COLOR_SLOPE)` |
| 5.8s | 说明文字 | `FadeIn(explanation)` - "k > 0, 从左到右上升" |
| 7.5s | 等待 | `Wait(1.2)` |

### 几何细节
- 点1: axes.c2p(0, 1), 蓝色
- 点2: axes.c2p(1, 3), 蓝色
- 斜率三角形: Polygon((0,1), (1,1), (1,3)), 橙色边框, fill_opacity=0.2
- Δx: 水平虚线, 底边中点下方
- Δy: 竖直虚线, 右边中点右侧

### 清理
- FadeOut: subtitle, slope_triangle, delta_x_label, delta_y_label, slope_formula, explanation, point1, point2
- 保留: linear_graph, axes

---

## Scene 5: 完整公式展示 (5-6秒)
**目的**: 汇总知识点，展示完整的一次函数公式

### 元素
1. 完整公式: y = kx + b
2. k 和 b 的分解说明
3. 特殊情况: b=0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 完整公式放大居中 | `formula_complete.animate.scale(1.5).move_to(UP*5)` |
| 0.8s | k 的说明框 | `FadeIn(k_box)` - "k: 斜率 (k ≠ 0)" |
| 1.4s | b 的说明框 | `FadeIn(b_box)` - "b: 截距" |
| 2.2s | 特殊情况提示 | `FadeIn(special_case)` - "当 b=0 时, y=kx (正比例函数)" |
| 3.5s | 正比例函数图像闪烁 | `Flash(proportional_graph)` + `proportional_graph.animate.set_opacity(0.8)` |
| 4.8s | 等待 | `Wait(1.0)` |

### 几何细节
- 说明框: SurroundingRectangle, color=对应颜色, buff=0.1
- 布局: k_box 和 b_box 水平排列在公式下方

### 清理
- FadeOut: k_box, b_box, special_case
- 保留: formula_complete, axes, linear_graph, proportional_graph

---

## Scene 6: 多个一次函数对比 (8-10秒)
**目的**: 通过不同的 k 和 b 值，展示一次函数的多样性

### 元素
1. 多条一次函数图像
2. 对应的公式标注
3. 动态变化效果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除之前的图像 | `FadeOut(proportional_graph, linear_graph)` |
| 0.5s | 绘制 y=x+1 | `Create(graph1)` - 绿色 |
| 1.2s | 绘制 y=-x+2 | `Create(graph2)` - 红色 |
| 1.9s | 绘制 y=0.5x-1 | `Create(graph3)` - 紫色 |
| 2.6s | 绘制 y=-2x | `Create(graph4)` - 橙色 |
| 3.5s | 公式组显示 | `FadeIn(formulas_group)` |
| 4.5s | 观察文字 | `FadeIn(observation)` - "k 决定倾斜, b 决定位置" |
| 6.0s | 高亮 k>0 的线 | `graph1.animate.set_stroke(width=5)` |
| 7.0s | 高亮 k<0 的线 | `graph2.animate.set_stroke(width=5), graph4.animate.set_stroke(width=5)` |
| 8.5s | 等待 | `Wait(1.2)` |

### 几何细节
- 所有图像: x_range=[-3, 3]
- 公式位置: 右侧垂直排列, font_size=20
- 线条宽度: 初始3, 高亮5

### 清理
- FadeOut: graph1, graph2, graph3, graph4, formulas_group, observation
- 保留: axes, formula_complete

---

## Scene 7: 片尾总结 (6-8秒)
**目的**: 总结关键点，引导关注

### 元素
1. 总结文字
2. 关键公式
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系淡出 | `FadeOut(axes, formula_complete)` |
| 0.5s | 总结标题 | `Write(summary_title)` - "一次函数" |
| 1.2s | 关键点1 | `FadeIn(key1)` - "形式: y = kx + b (k ≠ 0)" |
| 1.8s | 关键点2 | `FadeIn(key2)` - "k: 斜率 (倾斜程度)" |
| 2.4s | 关键点3 | `FadeIn(key3)` - "b: 截距 (与y轴交点)" |
| 3.2s | 特殊说明 | `FadeIn(special)` - "b=0 时为正比例函数" |
| 4.5s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP*1.5)` |
| 5.2s | 关注提示 | `FadeIn(follow_text)` - "关注我, 学更多函数知识!" |
| 6.5s | 装饰动画 | `Create(decoration)` - 小图标旋转 |
| 7.5s | 等待 | `Wait(1.0)` |

### 几何细节
- 总结文字: 居中排列, 逐个淡入
- 装饰: 简单的函数曲线图标，围绕关注文字

### 清理
- 全部淡出结束

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终显示 |
| axes | Scene 1 | Scene 7 | 主坐标系 |
| proportional_graph | Scene 1 | Scene 6 | 正比例函数 y=2x |
| linear_graph | Scene 2 | Scene 6 | 一次函数 y=2x+1 |
| intercept_dot | Scene 3 | Scene 6 | 截距点 |
| slope_triangle | Scene 4 | Scene 4 | 临时辅助 |
| formula_complete | Scene 5 | Scene 7 | 完整公式 |
| multiple_graphs | Scene 6 | Scene 6 | 多函数对比 |

---

## 动画节奏总结
- 快节奏: Scene 1 (钩子), Scene 2 (引入)
- 中等节奏: Scene 3 (截距), Scene 4 (斜率)
- 慢节奏: Scene 5 (完整公式), Scene 6 (对比展示)
- 总结: Scene 7 (片尾)

总时长估计: 63-72秒

---

## 特殊注意事项
1. 所有坐标转换使用 axes.c2p()
2. 中文文字使用 Text(..., font="Noto Sans CJK SC")
3. 数学公式使用 MathTex(r"...")
4. 颜色一致性: 正比例函数红色, 一次函数蓝色
5. 截距和斜率分别用绿色和橙色高亮