# 逆命题与逆定理 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标受众: 八年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 原命题
COLOR_SECONDARY = "#e74c3c"     # 红色 - 逆命题
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
COLOR_TRUE = "#2ecc71"          # 绿色 - 真命题
COLOR_FALSE = "#e67e22"         # 橙色 - 假命题
COLOR_AUXILIARY = GRAY_B        # 辅助线
COLOR_ARROW = "#9b59b6"         # 紫色 - 箭头
```

## 几何/文本预计算清单
| 元素 | 类型 | 存储变量 | 位置 |
|------|------|---------|------|
| 原命题框 | Rectangle | self.prop_box | y=2 |
| 逆命题框 | Rectangle | self.inverse_box | y=-2 |
| 双向箭头 | DoubleArrow | self.swap_arrow | x=0 |
| 示例三角形A | Polygon | self.triangle_a | LEFT*2.5 |
| 示例三角形B | Polygon | self.triangle_b | RIGHT*2.5 |

## 核心概念架构
```
原命题: 若p则q
    ↕️ (互换条件和结论)
逆命题: 若q则p

关系: 原命题真 ≠> 逆命题真
特例: 逆命题也真 → 逆定理
```

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部，y=7)
2. 钩子问题 (大字，y=5)
3. 两个问号动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.2)` |
| 1.5s | 问号闪烁 | `Flash(question_marks)` |
| 2.5s | 等待 | `Wait(0.8)` |

### 文本内容
- 钩子: "如果命题是真的，反过来说还是真的吗?"
- 字体: Noto Sans CJK SC, 36px

### 清理
- FadeOut: hook_text, question_marks
- 保留: author_info

---

## Scene 2: 定义原命题与逆命题 (8-10秒)
**目的**: 清晰展示定义

### 元素
1. 标题 "逆命题的定义" (y=6)
2. 原命题框 (y=2)
3. 逆命题框 (y=-2)
4. 双向箭头 (连接两框)
5. 说明文字 (y=-5)

### 几何计算
```python
# 命题框尺寸
box_width = 6.0
box_height = 1.5

# 原命题框
prop_box_center = UP * 2
self.prop_box = Rectangle(
    width=box_width,
    height=box_height,
    color=COLOR_PRIMARY
).move_to(prop_box_center)

# 逆命题框
inverse_box_center = DOWN * 2
self.inverse_box = Rectangle(
    width=box_width,
    height=box_height,
    color=COLOR_SECONDARY
).move_to(inverse_box_center)

# 箭头
arrow_start = prop_box_center + DOWN * (box_height/2 + 0.3)
arrow_end = inverse_box_center + UP * (box_height/2 + 0.3)
self.swap_arrow = DoubleArrow(
    arrow_start,
    arrow_end,
    color=COLOR_ARROW,
    buff=0
)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 原命题框创建 | `Create(prop_box)` |
| 1.0s | 原命题文字书写 | `Write(prop_text)` |
| 2.0s | 双向箭头生长 | `GrowArrow(swap_arrow)` |
| 2.5s | "互换条件和结论"文字 | `FadeIn(swap_label)` |
| 3.5s | 逆命题框创建 | `Create(inverse_box)` |
| 4.0s | 逆命题文字书写 | `Write(inverse_text)` |
| 5.5s | 底部说明淡入 | `FadeIn(definition_text)` |
| 6.5s | 等待理解 | `Wait(2.0)` |

### 文本内容
- 原命题框内: "原命题: 若p则q"
- 逆命题框内: "逆命题: 若q则p"
- 箭头旁: "互换"
- 底部: "把命题的条件和结论互换，得到逆命题"

### 清理
- FadeOut: title, definition_text
- 保留: prop_box, prop_text, inverse_box, inverse_text, swap_arrow

---

## Scene 3: 具体示例 - 等腰三角形 (10-12秒)
**目的**: 用具体例子说明原命题和逆命题

### 元素
1. 示例标题 (y=6)
2. 左侧: 原命题+三角形A (x=-2.5)
3. 右侧: 逆命题+三角形B (x=2.5)
4. 真值标记 (✓符号)

### 几何计算
```python
# 等腰三角形 (原命题侧)
# 顶点A在上，AB=AC
self.A = np.array([-2.5, 1.5, 0])
self.B = np.array([-3.5, -0.5, 0])
self.C = np.array([-1.5, -0.5, 0])

# 验证等腰: |AB| = |AC|
self.AB = np.linalg.norm(self.B - self.A)
self.AC = np.linalg.norm(self.C - self.A)
assert abs(self.AB - self.AC) < 1e-6, "等腰三角形边长不相等"

# 底边中点
self.M = (self.B + self.C) / 2

# 等边角标记位置
# 角B和角C应该相等
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除上一场景 | `FadeOut(previous_elements)` |
| 0.5s | 示例标题淡入 | `FadeIn(example_title)` |
| 1.0s | 原命题文字淡入 | `FadeIn(prop_statement)` |
| 1.5s | 绘制三角形A | `Create(triangle_a)` |
| 2.0s | 标注AB=AC | `Write(equal_sides_label)` |
| 3.0s | 标注底角相等 | `Write(equal_angles_label)` |
| 4.0s | ✓标记闪烁 | `Flash(check_mark_left)` |
| 5.0s | 逆命题文字淡入 | `FadeIn(inverse_statement)` |
| 5.5s | 绘制三角形B | `Create(triangle_b)` |
| 6.0s | 标注角B=角C | `Write(equal_angles_label_b)` |
| 7.0s | 标注AB=AC | `Write(equal_sides_label_b)` |
| 8.0s | ✓标记闪烁 | `Flash(check_mark_right)` |
| 9.0s | 等待 | `Wait(1.5)` |

### 文本内容
- 原命题: "若AB=AC, 则∠B=∠C"
- 逆命题: "若∠B=∠C, 则AB=AC"
- 底部提示: "两个都是真命题!"

### 清理
- FadeOut: example_title, triangles, labels
- 保留: 无

---

## Scene 4: 关键关系 - 原命题真 ≠> 逆命题真 (10-12秒)
**目的**: 强调核心概念

### 元素
1. 大标题 (y=5)
2. 公式展示 (y=1)
3. X符号动画 (强调"不一定")
4. 警告图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 大标题书写 | `Write(key_title)` |
| 1.0s | "原命题真"淡入 | `FadeIn(prop_true)` |
| 1.5s | 箭头生长 | `GrowArrow(implies_arrow)` |
| 2.0s | "逆命题真"淡入 | `FadeIn(inverse_true)` |
| 2.5s | X符号划过箭头 | `Create(cross_mark)` |
| 3.0s | "不一定"文字强调 | `Flash + Write(not_certain)` |
| 4.0s | 警告图标闪烁 | `Flash(warning_icon)` |
| 5.0s | 说明文字 | `FadeIn(explanation)` |
| 6.0s | 等待理解 | `Wait(2.5)` |

### 文本内容
- 标题: "重要! 原命题与逆命题的关系"
- 公式: "原命题真 ≠> 逆命题真"
- 强调: "不一定成立!"
- 说明: "原命题为真，逆命题可能真，也可能假"

### 清理
- FadeOut: all elements
- 保留: 无

---

## Scene 5: 反例展示 (10-12秒)
**目的**: 用反例说明逆命题可能为假

### 元素
1. 反例标题 (y=6)
2. 原命题 (真) - 左侧
3. 逆命题 (假) - 右侧
4. ✓和✗符号对比

### 几何计算
```python
# 示例: "同位角相等"
# 原命题 (真): 若两直线平行, 则同位角相等
# 绘制两条平行线和截线

# 平行线1
line1_start = np.array([-3, 1, 0])
line1_end = np.array([-1, 1, 0])

# 平行线2
line2_start = np.array([-3, -0.5, 0])
line2_end = np.array([-1, -0.5, 0])

# 截线
transversal_start = np.array([-2.5, 1.5, 0])
transversal_end = np.array([-1.5, -1, 0])

# 标注角度相等
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 反例标题淡入 | `FadeIn(counter_example_title)` |
| 0.5s | 原命题文字 | `Write(prop_text)` |
| 1.0s | 绘制平行线图形 | `Create(parallel_diagram)` |
| 2.0s | 标注角度 | `Write(angle_labels)` |
| 3.0s | ✓符号 | `FadeIn(check_mark)` |
| 4.0s | 逆命题文字 | `Write(inverse_text)` |
| 4.5s | 绘制非平行线图形 | `Create(non_parallel_diagram)` |
| 5.5s | 标注角度相等但不平行 | `Write(angle_labels_2)` |
| 6.5s | ✗符号闪烁 | `Flash(cross_mark)` |
| 7.5s | 说明文字 | `FadeIn(explanation)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 文本内容
- 原命题: "若两直线平行, 则同位角相等" (✓)
- 逆命题: "若同位角相等, 则两直线平行" (✗)
- 说明: "同位角相等时，直线可能相交"

### 清理
- FadeOut: all elements
- 保留: 无

---

## Scene 6: 逆定理的定义 (8-10秒)
**目的**: 介绍逆定理的概念

### 元素
1. 标题 "什么是逆定理?" (y=6)
2. 定义框 (y=2)
3. 条件强调 (两个✓符号)
4. 示例列举

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.8s | 定义框创建 | `Create(definition_box)` |
| 1.3s | 定义文字淡入 | `FadeIn(definition_text)` |
| 2.5s | 条件1: 原命题真 (✓) | `FadeIn(condition_1)` |
| 3.0s | 条件2: 逆命题真 (✓) | `FadeIn(condition_2)` |
| 3.5s | "逆定理"高亮 | `Flash(theorem_word)` |
| 4.5s | 示例标题 | `FadeIn(example_title)` |
| 5.0s | 示例1淡入 | `FadeIn(example_1)` |
| 5.5s | 示例2淡入 | `FadeIn(example_2)` |
| 6.5s | 等待 | `Wait(2.0)` |

### 文本内容
- 定义: "如果一个定理的逆命题也是真命题，则称它为逆定理"
- 示例1: "勾股定理 ⟺ 勾股定理的逆定理"
- 示例2: "等腰三角形性质 ⟺ 等腰三角形判定"

### 清理
- FadeOut: all elements
- 保留: 无

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结框 (3个要点)
2. 作者信息放大
3. 关注提示
4. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 0.8s | 要点1淡入 | `FadeIn(point_1, shift=LEFT)` |
| 1.5s | 要点2淡入 | `FadeIn(point_2, shift=LEFT)` |
| 2.2s | 要点3淡入 | `FadeIn(point_3, shift=LEFT)` |
| 3.5s | 作者信息放大 | `Transform(author)` |
| 4.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 5.5s | 装饰动画 | `Flash(decoration_circles)` |
| 7.0s | 等待 | `Wait(1.5)` |
| 8.5s | 全部淡出 | `FadeOut(everything)` |

### 文本内容
- 要点1: "逆命题 = 条件和结论互换"
- 要点2: "原命题真 ≠> 逆命题真"
- 要点3: "逆命题也真 → 逆定理"
- 关注: "关注我，学更多数学技巧!"

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终在顶部 |
| prop_box | Scene 2 | Scene 2 | 原命题框 |
| inverse_box | Scene 2 | Scene 2 | 逆命题框 |
| triangle_a | Scene 3 | Scene 3 | 示例三角形 |
| warning_icon | Scene 4 | Scene 4 | 警告图标 |
| parallel_lines | Scene 5 | Scene 5 | 反例图形 |
| definition_box | Scene 6 | Scene 6 | 定义框 |
| summary_points | Scene 7 | Scene 7 | 总结要点 |

---

## 时间轴总览
```
0s ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75s
   ↑        ↑           ↑           ↑           ↑           ↑        ↑
   开场      定义         示例         关系         反例         逆定理    总结
   (3s)     (10s)       (12s)       (12s)       (12s)       (10s)    (10s)
```

## 验证清单
- [ ] 所有文字使用 Text() 而非 MathTex() (中文)
- [ ] 数学符号使用 MathTex()
- [ ] 所有元素在边界内 (x∈[-4,4], y∈[-7,7])
- [ ] 关键概念停留时间≥2秒
- [ ] 颜色对比清晰
- [ ] 字体大小符合规范
- [ ] 作者信息始终可见