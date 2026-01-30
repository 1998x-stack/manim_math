# 线段的和差倍分 - 动画分镜脚本

<!-- /root/code/sss/media/videos/line_segment_operations/1920p60/LineSegmentOperations.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 初级（六年级）
- 目标受众: 小学高年级/初中学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要线段
COLOR_SECONDARY = "#e74c3c"    # 红色 - 辅助线段
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_SUCCESS = "#2ecc71"      # 绿色 - 结果
COLOR_POINT = "#f39c12"        # 橙色 - 关键点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 点A | [-3, 0, 0] * SCALE + OFFSET | self.A | 线段AB起点 |
| 点B | [0, 0, 0] * SCALE + OFFSET | self.B | 线段AB终点/线段BC起点 |
| 点C | [2, 0, 0] * SCALE + OFFSET | self.C | 线段BC终点 |
| 点M | (A + B) / 2 | self.M | 线段AB中点 |
| 点D | [-2, 0, 0] * SCALE + OFFSET | self.D | 长线段起点 |
| 点E | [3, 0, 0] * SCALE + OFFSET | self.E | 长线段终点 |
| 线段AB长度 | ||B - A|| | self.len_AB | 基准长度 |
| 线段BC长度 | ||C - B|| | self.len_BC | 基准长度 |

### 坐标系配置
- 主内容区域: y ∈ [0, 3] (线段绘制区)
- 公式区域: y ∈ [-2, -0.5] (数学公式展示)
- 说明文字区域: y ∈ [-4, -2] (步骤说明)
- SCALE = 0.9
- OFFSET = UP * 2

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 吸引注意力，引出主题

### 元素
1. 作者标识 (顶部，y=7)
2. 钩子问题 (大字，y=5.5)
3. 三个点快速连成线段

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 创建并保留 |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 创建 |
| 1.2s | 三个点闪现 | `FadeIn(dots, scale=0.5)` | 创建 |
| 1.8s | 点连成线段 | `Create(demo_line)` | 创建 |
| 2.8s | 等待 | `Wait(0.8)` | - |
| 3.6s | 淡出钩子和演示 | `FadeOut(hook_text, dots, demo_line)` | 销毁 |

### 钩子文字内容
```
"两条线段能相加吗?"
"它们的一半在哪里?"
```

### 清理
- FadeOut: hook_text, demo_line, dots
- 保留: author_info

---

## Scene 2: 线段的和 (12-14秒)
**目的**: 演示AB + BC = AC (B在AC上的情况)

### 几何设置
```python
# 两条首尾相连的线段
self.A = np.array([-3, 0, 0]) * self.SCALE + self.OFFSET
self.B = np.array([0, 0, 0]) * self.SCALE + self.OFFSET  # 共同点
self.C = np.array([2, 0, 0]) * self.SCALE + self.OFFSET

self.len_AB = np.linalg.norm(self.B - self.A)
self.len_BC = np.linalg.norm(self.C - self.B)
self.len_AC = np.linalg.norm(self.C - self.A)
```

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 场景标题淡入 | `FadeIn(title_sum)` | "线段的和" |
| 0.5s | 绘制线段AB | `Create(line_AB)` | 蓝色线段 |
| 1.0s | 标注点A, B | `FadeIn(dot_A, label_A, dot_B, label_B)` | 橙色点+标签 |
| 1.5s | 测量AB长度 | `Create(brace_AB), FadeIn(length_AB)` | 大括号+长度标注 |
| 2.5s | 绘制线段BC | `Create(line_BC)` | 红色线段 |
| 3.0s | 标注点C | `FadeIn(dot_C, label_C)` | 橙色点+标签 |
| 3.5s | 测量BC长度 | `Create(brace_BC), FadeIn(length_BC)` | 大括号+长度标注 |
| 4.5s | 公式出现 | `Write(formula_sum)` | AB + BC = AC |
| 5.5s | 高亮整体线段AC | `line_AB.animate.set_color(GREEN), line_BC.animate.set_color(GREEN)` | 变绿 |
| 6.5s | 测量AC总长 | `Create(brace_AC), FadeIn(length_AC)` | 大括号+总长 |
| 7.5s | 闪烁强调 | `Flash(formula_sum)` | 公式闪烁 |
| 8.5s | 说明文字 | `FadeIn(explanation)` | "首尾相连，长度相加" |
| 10.0s | 等待理解 | `Wait(1.5)` | - |

### 公式内容
```latex
AB + BC = AC
```

### 清理
- FadeOut: title_sum, line_AB, line_BC, dots, labels, braces, length_texts, formula_sum, explanation
- 保留: 无

---

## Scene 3: 线段的差 (12-14秒)
**目的**: 演示线段相减 (长 - 短)

### 几何设置
```python
# 同一直线上的两个线段，一长一短
self.D = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
self.E = np.array([2.5, 0, 0]) * self.SCALE + self.OFFSET
self.F = np.array([1, 0, 0]) * self.SCALE + self.OFFSET  # DF较短

self.len_DE = np.linalg.norm(self.E - self.D)  # 长线段
self.len_DF = np.linalg.norm(self.F - self.D)  # 短线段
self.len_FE = self.len_DE - self.len_DF       # 差
```

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 场景标题 | `FadeIn(title_diff)` | "线段的差" |
| 0.5s | 绘制长线段DE | `Create(line_DE)` | 蓝色线段 |
| 1.0s | 标注D, E点 | `FadeIn(dots, labels)` | 橙色点 |
| 1.5s | 测量DE长度 | `Create(brace_DE), FadeIn(length_DE)` | 大括号 |
| 2.5s | 绘制短线段DF | `Create(line_DF)` | 红色覆盖部分 |
| 3.0s | 标注F点 | `FadeIn(dot_F, label_F)` | 橙色点 |
| 3.5s | 测量DF长度 | `Create(brace_DF), FadeIn(length_DF)` | 大括号 |
| 4.5s | 公式出现 | `Write(formula_diff)` | DE - DF = FE |
| 5.5s | 高亮剩余部分FE | `line_FE.animate.set_color(GREEN).set_stroke_width(5)` | 加粗变绿 |
| 6.5s | 测量FE长度 | `Create(brace_FE), FadeIn(length_FE)` | 大括号+差值 |
| 7.5s | 闪烁强调 | `Flash(formula_diff)` | 公式闪烁 |
| 8.5s | 说明文字 | `FadeIn(explanation)` | "较长减较短" |
| 10.0s | 等待理解 | `Wait(1.5)` | - |

### 公式内容
```latex
DE - DF = FE
```

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 4: 线段的倍 (12-14秒)
**目的**: 演示一条线段是另一条的N倍

### 几何设置
```python
# 短线段和其2倍线段
self.P = np.array([-3, 0, 0]) * self.SCALE + self.OFFSET
self.Q = np.array([-1, 0, 0]) * self.SCALE + self.OFFSET
self.R = np.array([3, 0, 0]) * self.SCALE + self.OFFSET

self.len_PQ = np.linalg.norm(self.Q - self.P)  # 基准长度
self.len_PR = 2 * self.len_PQ                  # 2倍长度

# 验证: PR确实是PQ的2倍
assert abs(np.linalg.norm(self.R - self.P) - self.len_PR) < 1e-6
```

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 场景标题 | `FadeIn(title_multiple)` | "线段的倍" |
| 0.5s | 绘制短线段PQ | `Create(line_PQ)` | 红色线段 |
| 1.0s | 标注P, Q点 | `FadeIn(dots, labels)` | 橙色点 |
| 1.5s | 测量PQ长度 | `Create(brace_PQ), FadeIn(length_PQ)` | 标注"1倍" |
| 2.5s | 复制线段PQ | `line_PQ_copy.animate.move_to(...)` | 虚线平移 |
| 3.5s | 拼接成PR | `Transform(line_PQ_copy, line_QR)` | 实线化 |
| 4.5s | 标注R点 | `FadeIn(dot_R, label_R)` | 橙色点 |
| 5.0s | 公式出现 | `Write(formula_multiple)` | PR = 2 × PQ |
| 6.0s | 高亮整体PR | `line_PR_full.animate.set_color(GREEN)` | 变绿 |
| 7.0s | 测量PR长度 | `Create(brace_PR), FadeIn(length_PR)` | 标注"2倍" |
| 8.0s | 闪烁强调 | `Flash(formula_multiple)` | 公式闪烁 |
| 9.0s | 说明文字 | `FadeIn(explanation)` | "首尾相连得倍数" |
| 10.5s | 等待理解 | `Wait(1.5)` | - |

### 公式内容
```latex
PR = 2 \times PQ
```

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 5: 线段的分 (中点) (14-16秒)
**目的**: 演示中点的概念和计算

### 几何设置
```python
# 线段AB及其中点M
self.A = np.array([-3, 0, 0]) * self.SCALE + self.OFFSET
self.B = np.array([3, 0, 0]) * self.SCALE + self.OFFSET
self.M = (self.A + self.B) / 2  # 精确中点

self.len_AB = np.linalg.norm(self.B - self.A)
self.len_AM = np.linalg.norm(self.M - self.A)
self.len_MB = np.linalg.norm(self.B - self.M)

# 验证: AM = MB = AB/2
assert abs(self.len_AM - self.len_MB) < 1e-6
assert abs(self.len_AM - self.len_AB / 2) < 1e-6
```

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 场景标题 | `FadeIn(title_division)` | "线段的分 - 中点" |
| 0.5s | 绘制线段AB | `Create(line_AB)` | 蓝色线段 |
| 1.0s | 标注A, B点 | `FadeIn(dots, labels)` | 橙色点 |
| 1.5s | 测量AB长度 | `Create(brace_AB), FadeIn(length_AB)` | 大括号 |
| 2.5s | 问题出现 | `FadeIn(question)` | "如何找到中点?" |
| 3.5s | 中点M闪现 | `FadeIn(dot_M, scale=1.5)` | 黄色点放大 |
| 4.0s | 标注M点 | `FadeIn(label_M)` | "M (中点)" |
| 4.5s | 公式出现 | `Write(formula_midpoint)` | AM = MB = AB/2 |
| 5.5s | 测量AM段 | `Create(brace_AM), FadeIn(length_AM)` | 左半段 |
| 6.5s | 测量MB段 | `Create(brace_MB), FadeIn(length_MB)` | 右半段 |
| 7.5s | 等号闪烁 | `Flash(formula_midpoint)` | 强调相等 |
| 8.5s | 虚线分割 | `Create(dashed_line_M)` | 中点处虚线 |
| 9.5s | 说明文字 | `FadeIn(explanation)` | "中点二等分线段" |
| 11.0s | 等待理解 | `Wait(2.0)` | 重点内容多停留 |

### 公式内容
```latex
AM = MB = \frac{AB}{2}
```

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 6: 综合总结 (12-14秒)
**目的**: 回顾四个知识点，强化记忆

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title_summary)` | "知识点回顾" |
| 0.5s | 四个卡片依次滑入 | `card.animate.shift(DOWN*0)` | 从左侧滑入 |
| 1.5s | 卡片1: 和 | `FadeIn(card_sum)` | 图标+文字 |
| 2.5s | 卡片2: 差 | `FadeIn(card_diff)` | 图标+文字 |
| 3.5s | 卡片3: 倍 | `FadeIn(card_multiple)` | 图标+文字 |
| 4.5s | 卡片4: 分 | `FadeIn(card_division)` | 图标+文字 |
| 5.5s | 关键提示 | `FadeIn(key_point)` | "牢记中点性质!" |
| 7.0s | 所有卡片闪烁 | `Flash(cards)` | 同时闪烁 |
| 8.0s | 等待 | `Wait(2.0)` | - |

### 卡片内容
```python
cards = [
    {"title": "和", "content": "AB + BC = AC (首尾相连)", "icon_color": BLUE},
    {"title": "差", "content": "长减短得差", "icon_color": RED},
    {"title": "倍", "content": "重复拼接", "icon_color": PURPLE},
    {"title": "分", "content": "中点二等分", "icon_color": GREEN}
]
```

### 清理
- 所有元素淡出（除author_info外）

---

## Scene 7: 片尾关注 (6-8秒)
**目的**: 品牌强化，引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 视觉效果 |
|------|------|---------|---------|
| 0.0s | 作者信息放大 | `Transform(author_info, author_large)` | 放大居中 |
| 0.8s | ID出现 | `FadeIn(author_id)` | @emptyandcalm |
| 1.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` | "关注获得更多技巧!" |
| 2.5s | 线段装饰动画 | `Create(decoration_lines)` | 小线段环绕 |
| 3.5s | 装饰旋转 | `Rotate(decoration)` | 360度旋转 |
| 5.0s | 等待 | `Wait(1.5)` | - |
| 6.5s | 全部淡出 | `FadeOut(*)` | - |

### 装饰元素
- 6条小线段环绕文字，颜色渐变

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终显示 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| demo_line | Scene 1 | Scene 1 | 演示线段 |
| line_AB | Scene 2 | Scene 2 | 线段和的AB |
| line_BC | Scene 2 | Scene 2 | 线段和的BC |
| line_DE | Scene 3 | Scene 3 | 线段差的长线段 |
| line_DF | Scene 3 | Scene 3 | 线段差的短线段 |
| line_PQ | Scene 4 | Scene 4 | 线段倍的基准 |
| line_PR | Scene 4 | Scene 4 | 线段倍的2倍 |
| line_AB | Scene 5 | Scene 5 | 中点的完整线段 |
| dot_M | Scene 5 | Scene 5 | 中点 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |
| decoration | Scene 7 | Scene 7 | 装饰元素 |

---

## 几何验证清单
- [ ] 所有点坐标在setup_geometry()中计算
- [ ] 验证中点计算: AM = MB
- [ ] 验证倍数关系: PR = 2 × PQ
- [ ] 验证和: AC = AB + BC
- [ ] 验证差: FE = DE - DF
- [ ] 所有元素在边界内 (x∈[-4,4], y∈[-7,7])

---

## 动画节奏控制
- 简单创建: 0.5-0.8s
- 复杂动画: 1.0-1.5s
- 理解停顿: 1.5-2.0s (中点等重点)
- 场景切换: 0.4-0.6s
- 总时长: 60-75秒

---

## 特殊注意事项
1. **中文文字**: 全部使用 `Text(..., font="Noto Sans CJK SC")`
2. **公式**: 使用 `MathTex(r"...")`，不含中文
3. **虚线**: 使用 `DashedLine` 而非 `set_style`
4. **颜色一致性**: 主线段蓝色，辅助红色，结果绿色
5. **标注清晰**: 大括号、点标签、长度数值都要清晰可见
6. **动画流畅**: 避免突兀切换，多用淡入淡出
7. **重点强调**: 中点场景多停留2秒