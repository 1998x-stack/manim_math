# 一次函数的图像 - 动画分镜脚本

## 元信息
- **目标时长**: 60-75秒
- **场景数量**: 7个
- **难度等级**: 中等 (八年级)
- **知识点**: 一次函数y=kx+b的图像特征

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主函数线
COLOR_SECONDARY = "#e74c3c"      # 红色 - 对比函数线
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮标注
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_POSITIVE_K = "#2ecc71"     # 绿色 - k>0的线
COLOR_NEGATIVE_K = "#9b59b6"     # 紫色 - k<0的线
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝背景
```

## 几何预计算清单

### 坐标系参数
- **x轴范围**: [-4, 4, 1]
- **y轴范围**: [-3, 5, 1]
- **坐标系位置**: UP * 1.5 (为底部说明留空间)
- **坐标系缩放**: 0.85

### 示例函数
1. **主函数**: y = 2x + 1
   - 斜率 k = 2
   - y截距 b = 1
   - y轴交点: (0, 1)
   - x轴交点: (-0.5, 0)
   
2. **对比函数1**: y = -x + 2 (k<0示例)
   - 斜率 k = -1
   - y截距 b = 2
   - y轴交点: (0, 2)
   - x轴交点: (2, 0)

3. **对比函数2**: y = 0.5x - 1 (小斜率示例)
   - 斜率 k = 0.5
   - y截距 b = -1
   - y轴交点: (0, -1)
   - x轴交点: (2, 0)

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部, font_size=20)
2. 钩子问题 (大字, font_size=40)
3. 一条神秘的直线 (部分显示)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 神秘直线部分绘制 | `Create(mystery_line, run_time=0.8)` |
| 1.9s | 问号闪烁 | `Flash(question_mark, run_time=0.4)` |
| 2.3s | 等待 | `self.wait(1.0)` |

### 文案
- **作者**: "上海初高中数学直通车 @emptyandcalm"
- **钩子**: "这条直线藏着什么秘密?"

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, mystery_line (变淡)

---

## Scene 2: 建立坐标系 (4-6秒)
**目的**: 引入坐标系，建立数学框架

### 元素
1. 标题文字: "一次函数的图像"
2. 坐标系 (Axes)
3. 原点标注 O
4. x轴、y轴标签

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=UP*0.3, run_time=0.5)` |
| 0.5s | 坐标轴创建 | `Create(axes, run_time=1.2)` |
| 1.7s | 原点标注 | `FadeIn(origin_label, run_time=0.3)` |
| 2.0s | 轴标签显示 | `Write(x_label), Write(y_label, run_time=0.4)` |
| 2.4s | 等待 | `self.wait(0.8)` |

### 说明文字 (底部)
- "所有一次函数都在这个坐标系中"

### 清理
- FadeOut: title, 说明文字
- 保留: axes, origin_label, axis_labels

---

## Scene 3: 绘制主函数 y=2x+1 (8-10秒)
**目的**: 展示一次函数的基本形态，标注关键点

### 元素
1. 函数表达式: y = 2x + 1
2. 函数图像 (直线)
3. y轴交点 (0, 1) 及标注
4. x轴交点 (-0.5, 0) 及标注
5. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 函数式淡入顶部 | `Write(formula, run_time=0.8)` |
| 0.8s | 直线从左到右绘制 | `Create(graph, run_time=1.5)` |
| 2.3s | y轴交点标记 | `FadeIn(y_intercept_dot, scale=0.5), Write(y_label, run_time=0.5)` |
| 2.8s | 虚线连接y轴 | `Create(dashed_line_y, run_time=0.4)` |
| 3.2s | 坐标标注 | `FadeIn(coord_y, run_time=0.3)` |
| 3.5s | x轴交点标记 | `FadeIn(x_intercept_dot, scale=0.5), Write(x_label, run_time=0.5)` |
| 4.0s | 虚线连接x轴 | `Create(dashed_line_x, run_time=0.4)` |
| 4.4s | 坐标标注 | `FadeIn(coord_x, run_time=0.3)` |
| 4.7s | 等待 | `self.wait(1.5)` |

### 说明文字 (底部, y=-5位置)
- "图像是一条直线"
- "与y轴交于 (0, b)"
- "与x轴交于 (-b/k, 0)"

### 清理
- FadeOut: 虚线, 部分标注
- 保留: formula, graph, 交点dots, 坐标标注

---

## Scene 4: 斜率k的影响 - k>0 (6-8秒)
**目的**: 展示k>0时直线从左下到右上

### 元素
1. 强调 k=2 (红色高亮)
2. 箭头指示方向 (从左下到右上)
3. 说明文字
4. 对比: k=0.5的直线 (较平缓)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 高亮k值 | `Indicate(k_part, color=RED, run_time=0.6)` |
| 0.6s | 箭头出现 | `GrowArrow(direction_arrow, run_time=0.5)` |
| 1.1s | 说明文字 | `FadeIn(explanation, shift=UP*0.2, run_time=0.5)` |
| 1.6s | 等待 | `self.wait(0.8)` |
| 2.4s | 对比线淡入 | `Create(compare_graph, run_time=1.0)` |
| 3.4s | 对比说明 | `FadeIn(compare_text, run_time=0.4)` |
| 3.8s | 等待 | `self.wait(1.2)` |

### 说明文字
- "k > 0: 直线从左下到右上倾斜"
- "|k|越大, 直线越陡"

### 清理
- FadeOut: direction_arrow, compare_graph, compare_text, explanation
- 保留: main graph, formula

---

## Scene 5: 斜率k的影响 - k<0 (6-8秒)
**目的**: 展示k<0时直线从左上到右下

### 元素
1. 新函数: y = -x + 2
2. 紫色直线 (k<0)
3. 箭头指示方向 (从左上到右下)
4. 对比原函数 (变淡)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原函数变淡 | `graph.animate.set_opacity(0.3), formula.animate.set_opacity(0.3), run_time=0.5` |
| 0.5s | 新函数式 | `Write(new_formula, run_time=0.8)` |
| 1.3s | 新直线绘制 | `Create(negative_graph, run_time=1.2)` |
| 2.5s | 高亮k值 | `Indicate(k_negative, color=PURPLE, run_time=0.6)` |
| 3.1s | 箭头出现 | `GrowArrow(direction_arrow_down, run_time=0.5)` |
| 3.6s | 说明文字 | `FadeIn(explanation_negative, run_time=0.5)` |
| 4.1s | 等待 | `self.wait(1.5)` |

### 说明文字
- "k < 0: 直线从左上到右下倾斜"

### 清理
- FadeOut: negative_graph, new_formula, direction_arrow_down, explanation_negative
- 恢复: main graph opacity

---

## Scene 6: 截距b的影响 (6-8秒)
**目的**: 展示b值决定直线在y轴上的位置

### 元素
1. 三条平行线: y=2x+2, y=2x+1, y=2x-1
2. 强调 b 值
3. y轴交点动画 (上下移动)
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 三条线同时淡入 | `FadeIn(parallel_lines, lag_ratio=0.3, run_time=1.2)` |
| 1.2s | 高亮b值 | `Indicate(b_values, run_time=0.6)` |
| 1.8s | y轴交点标记 | `FadeIn(y_intercepts, run_time=0.5)` |
| 2.3s | 动画演示移动 | `Transform(graph, upper_graph), Transform(graph, lower_graph, run_time=1.5)` |
| 3.8s | 说明文字 | `FadeIn(explanation_b, run_time=0.5)` |
| 4.3s | 等待 | `self.wait(1.5)` |

### 说明文字
- "b 决定直线与y轴的交点"
- "b增大, 直线整体上移"

### 清理
- FadeOut: parallel_lines, y_intercepts, explanation_b
- 恢复: main graph

---

## Scene 7: 总结与结尾 (8-10秒)
**目的**: 总结关键知识点，引导关注

### 元素
1. 关键点卡片 (3个)
2. 主函数图像 (缩小, 背景)
3. 作者信息 (放大)
4. 关注引导

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(VGroup(*mobjects), run_time=0.5)` |
| 0.5s | 卡片1滑入 | `card1.animate.shift(RIGHT*10), run_time=0.5` |
| 1.0s | 卡片2滑入 | `card2.animate.shift(RIGHT*10), run_time=0.5` |
| 1.5s | 卡片3滑入 | `card3.animate.shift(RIGHT*10), run_time=0.5` |
| 2.0s | 等待 | `self.wait(1.0)` |
| 3.0s | 卡片淡出 | `FadeOut(cards, run_time=0.5)` |
| 3.5s | 作者信息放大 | `Transform(author_small, author_large, run_time=0.6)` |
| 4.1s | 关注文字 | `FadeIn(follow_text, scale=1.1, run_time=0.6)` |
| 4.7s | 装饰动画 | `Rotate(decorations, run_time=1.0)` |
| 5.7s | 等待 | `self.wait(1.5)` |

### 卡片内容
1. **直线形态**: "一次函数图像是直线"
2. **斜率影响**: "k决定倾斜方向和陡峭程度"
3. **截距影响**: "b决定与y轴交点位置"

### 关注文字
- "关注我, 学更多函数技巧!"

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持顶部 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| main_graph (y=2x+1) | Scene 3 | Scene 7 | 主函数线 |
| formula | Scene 3 | Scene 7 | 函数表达式 |
| y_intercept_dot | Scene 3 | Scene 6 | y轴交点 |
| x_intercept_dot | Scene 3 | Scene 6 | x轴交点 |
| direction_arrow | Scene 4 | Scene 4 | 临时箭头 |
| compare_graph | Scene 4 | Scene 4 | 临时对比线 |
| negative_graph | Scene 5 | Scene 5 | k<0示例 |
| parallel_lines | Scene 6 | Scene 6 | b影响演示 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 几何精度验证点

### 坐标计算
- y轴交点 (0, b): 直接使用 axes.c2p(0, b)
- x轴交点 (-b/k, 0): 计算 x = -b/k, 使用 axes.c2p(x, 0)
- 图像绘制: 使用 axes.plot(lambda x: k*x + b, x_range=...)

### 边界检查
- 坐标系: x ∈ [-4, 4], y ∈ [-3, 5]
- 主内容区: y ∈ [-3, 5.5] (留给坐标系)
- 顶部区: y ∈ [6, 7.5] (作者、标题)
- 底部区: y ∈ [-6, -4] (说明文字)

### 视觉验证
- 所有直线必须严格经过计算的交点
- 平行线必须完全平行 (相同斜率k)
- 箭头方向必须与斜率符号一致

---

## 动画节奏控制

| 场景 | 时长 | 节奏 | 关键等待 |
|------|------|------|---------|
| Scene 1 | 3-4s | 快速吸引 | 1.0s |
| Scene 2 | 4-6s | 中等建立 | 0.8s |
| Scene 3 | 8-10s | 慢速详解 | 1.5s (关键点) |
| Scene 4 | 6-8s | 中等演示 | 1.2s |
| Scene 5 | 6-8s | 中等对比 | 1.5s |
| Scene 6 | 6-8s | 中等演示 | 1.5s |
| Scene 7 | 8-10s | 慢速总结 | 2.5s (总计) |

**总时长**: 45-62秒 (符合TikTok短视频标准)

---

## 特殊注意事项

### 中文文字处理
- 所有中文使用 `Text(font="Noto Sans CJK SC")`
- 数学符号使用 `MathTex`
- 混合时使用 `VGroup` 组合

### LaTeX公式
- 函数式: `MathTex(r"y = {{ k }}x + {{ b }}")`
- 具体值: `MathTex(r"y = 2x + 1")`
- 坐标: `MathTex(r"(0, 1)")`

### 颜色一致性
- 主函数线: COLOR_PRIMARY (#3498db)
- k>0 示例: COLOR_POSITIVE_K (#2ecc71)
- k<0 示例: COLOR_NEGATIVE_K (#9b59b6)
- 高亮: YELLOW
- 辅助: GRAY_B

### 性能优化
- 使用 `self.remove()` 清理不再需要的元素
- 避免同时播放超过5个复杂动画
- 虚线使用 `DashedLine` 而非 `DashedVMobject`

---

## 验证清单

### 几何验证
- [ ] 所有交点坐标精确计算
- [ ] 直线斜率与公式k值一致
- [ ] 平行线斜率完全相同
- [ ] 所有元素在边界内

### 动画验证
- [ ] 总时长 45-75秒
- [ ] 难点停留 ≥ 1.5秒
- [ ] 无元素溢出
- [ ] 无文字重叠

### 内容验证
- [ ] 知识点准确
- [ ] 说明文字清晰
- [ ] 视觉引导明确
- [ ] 开头有钩子
- [ ] 结尾有引导

---

## 下一步: 编写Python代码

基于此分镜脚本, 将创建:
1. `linear_function_graph.py` - 主动画代码
2. `verify_geometry.py` - 几何验证脚本

确保所有坐标精确计算, 遵循Manim 0.19.2约束。