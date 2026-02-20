# 比例线段 - 动画分镜脚本

## 元信息
- 目标时长: 50-65 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标受众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要线段
COLOR_SECONDARY = "#e74c3c"      # 红色 - 对比线段
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
COLOR_SEGMENT_A = "#e74c3c"      # 线段a
COLOR_SEGMENT_B = "#3498db"      # 线段b
COLOR_SEGMENT_C = "#2ecc71"      # 线段c
COLOR_SEGMENT_D = "#f39c12"      # 线段d
```

## 几何预计算清单

### 场景2: 比例定义（四条线段）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 线段a | 长度 = 2 单位 | self.len_a = 2.0 |
| 线段b | 长度 = 3 单位 | self.len_b = 3.0 |
| 线段c | 长度 = 4 单位 | self.len_c = 4.0 |
| 线段d | 长度 = 6 单位 | self.len_d = 6.0 |
| 比例验证 | a/b = 2/3, c/d = 4/6 = 2/3 | ratio_ab = ratio_cd |

### 场景3: 内项外项
| 元素 | 说明 | 存储变量 |
|------|------|---------|
| 外项 | a 和 d | outer_items |
| 内项 | b 和 c | inner_items |
| 内项积 | b × c = 3 × 4 = 12 | product_inner |
| 外项积 | a × d = 2 × 6 = 12 | product_outer |

### 场景4: 比例中项
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 线段a | 2 单位 | self.len_a_mid = 2.0 |
| 比例中项b | √(a×c) = √(2×8) = 4 | self.len_b_mid = 4.0 |
| 线段c | 8 单位 | self.len_c_mid = 8.0 |
| 验证 | b² = a×c → 16 = 16 | verification |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出比例概念

### 元素
1. 作者标识（顶部小字）
2. 钩子问题
3. 四条不同长度的线段动画
4. 问号闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write("这四条线段有什么关系?")` |
| 1.0s | 四条线段依次出现 | `Create(lines)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.8s | 等待 | `Wait(0.6)` |

### 清理
- FadeOut: 钩子文字、问号
- 保留: 作者信息、四条线段轮廓

---

## Scene 2: 比例定义 (10-12秒)
**目的**: 展示比例的定义和判断方法

### 元素
1. 标题："比例线段 - Proportional Segments"
2. 四条线段（带标签 a, b, c, d）
3. 长度标注
4. 比例公式
5. 验证过程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 线段a出现 | `Create(seg_a)` + `Write("a")` |
| 0.9s | 线段b出现 | `Create(seg_b)` + `Write("b")` |
| 1.3s | 线段c出现 | `Create(seg_c)` + `Write("c")` |
| 1.7s | 线段d出现 | `Create(seg_d)` + `Write("d")` |
| 2.3s | 标注长度 | `Write("2, 3, 4, 6")` |
| 3.0s | 显示比例 | `Write("a/b = 2/3")` |
| 3.6s | 显示比例 | `Write("c/d = 4/6 = 2/3")` |
| 4.2s | 比例相等 | `Write("a/b = c/d")` + 高亮 |
| 5.0s | 定义 | `Write("这四条线段成比例")` |
| 6.0s | 等待理解 | `Wait(1.5)` |

### 几何精确计算
```python
# 线段长度（使用精确比例）
self.len_a = 2.0
self.len_b = 3.0
self.len_c = 4.0
self.len_d = 6.0

# 验证比例
ratio_ab = self.len_a / self.len_b  # 2/3 ≈ 0.6667
ratio_cd = self.len_c / self.len_d  # 4/6 ≈ 0.6667
assert abs(ratio_ab - ratio_cd) < 1e-6

# 线段位置（竖直排列）
self.seg_a_start = np.array([-3.0, 2.5, 0])
self.seg_a_end = self.seg_a_start + RIGHT * self.len_a

self.seg_b_start = np.array([-3.0, 1.2, 0])
self.seg_b_end = self.seg_b_start + RIGHT * self.len_b

self.seg_c_start = np.array([-3.0, -0.3, 0])
self.seg_c_end = self.seg_c_start + RIGHT * self.len_c

self.seg_d_start = np.array([-3.0, -1.8, 0])
self.seg_d_end = self.seg_d_start + RIGHT * self.len_d
```

### 清理
- FadeOut: 标题、长度标注
- Transform: 线段移动到新位置
- 保留: 四条线段

---

## Scene 3: 内项与外项 (10-12秒)
**目的**: 介绍内项外项概念及基本性质

### 元素
1. 标题："内项与外项"
2. 比例式：a : b = c : d
3. 内项标注（b, c）
4. 外项标注（a, d）
5. 基本性质：ad = bc
6. 计算验证

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 显示比例式 | `Write("a : b = c : d")` |
| 1.2s | 标注外项 | 高亮 a, d + `Write("外项")` |
| 2.0s | 标注内项 | 高亮 b, c + `Write("内项")` |
| 2.8s | 基本性质 | `Write("ad = bc")` |
| 3.5s | 计算左侧 | `Write("a × d = 2 × 6 = 12")` |
| 4.3s | 计算右侧 | `Write("b × c = 3 × 4 = 12")` |
| 5.1s | 验证相等 | 高亮 "12 = 12" |
| 6.0s | 等待理解 | `Wait(1.5)` |

### 计算验证
```python
# 外项积
product_outer = self.len_a * self.len_d  # 2 × 6 = 12

# 内项积
product_inner = self.len_b * self.len_c  # 3 × 4 = 12

# 验证
assert abs(product_outer - product_inner) < 1e-6
```

### 清理
- FadeOut: 所有元素
- 保留: 作者信息

---

## Scene 4: 比例中项 (10-12秒)
**目的**: 展示比例中项的特殊情况

### 元素
1. 标题："比例中项"
2. 三条线段（a, b, c）
3. 比例关系：a/b = b/c
4. 特殊性质：b² = ac
5. 数值示例：2, 4, 8
6. 验证：4² = 2×8

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 三条线段出现 | `Create(segs)` |
| 1.2s | 标注长度 | `Write("a=2, b=4, c=8")` |
| 1.9s | 比例关系 | `Write("a/b = b/c")` |
| 2.6s | 特殊性质 | `Write("b² = ac")` |
| 3.3s | b是比例中项 | `Write("b 是 a 和 c 的比例中项")` |
| 4.0s | 验证左侧 | `Write("b² = 4² = 16")` |
| 4.7s | 验证右侧 | `Write("ac = 2×8 = 16")` |
| 5.4s | 高亮相等 | 高亮 "16 = 16" |
| 6.2s | 等待理解 | `Wait(1.5)` |

### 几何精确计算
```python
# 比例中项示例
self.len_a_mid = 2.0
self.len_b_mid = 4.0  # √(a×c) = √(2×8) = 4
self.len_c_mid = 8.0

# 验证比例
ratio_1 = self.len_a_mid / self.len_b_mid  # 2/4 = 0.5
ratio_2 = self.len_b_mid / self.len_c_mid  # 4/8 = 0.5
assert abs(ratio_1 - ratio_2) < 1e-6

# 验证平方关系
b_squared = self.len_b_mid ** 2  # 16
a_times_c = self.len_a_mid * self.len_c_mid  # 16
assert abs(b_squared - a_times_c) < 1e-6
```

### 清理
- FadeOut: 所有元素
- 保留: 作者信息

---

## Scene 5: 比例性质 (8-10秒)
**目的**: 快速展示合比性质和等比性质

### 元素
1. 标题："比例的性质"
2. 性质1：合比性质
3. 性质2：等比性质
4. 公式展示
5. 示例说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 性质1卡片滑入 | `FadeIn(card1, shift=LEFT)` |
| 1.5s | 合比公式 | `Write("(a+b)/b = (c+d)/d")` |
| 2.5s | 性质2卡片滑入 | `FadeIn(card2, shift=LEFT)` |
| 3.5s | 等比公式 | `Write("a/b = c/d = (a+c)/(b+d)")` |
| 4.5s | 高亮提示 | `Write("前提：a/b = c/d")` |
| 5.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: 所有性质卡片
- 保留: 作者信息

---

## Scene 6: 总结与片尾 (8-10秒)
**目的**: 总结要点，引导关注

### 元素
1. 三个核心概念卡片
2. 关注提示
3. 作者信息放大

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"核心要点" | `Write(title)` |
| 0.6s | 卡片1: 比例定义 | `FadeIn(card1, shift=UP)` |
| 1.2s | 卡片2: 内项×外项 | `FadeIn(card2, shift=UP)` |
| 1.8s | 卡片3: 比例中项 | `FadeIn(card3, shift=UP)` |
| 2.6s | 作者信息放大 | `author.animate.scale(1.5)` |
| 3.4s | 关注提示 | `Write("关注我，学更多相似三角形!")` |
| 4.2s | 装饰动画 | `Flash(decorations)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- 所有元素淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 钩子文字 |
| segments_group | Scene 2 | Scene 2 | 四条线段 |
| proportion_formula | Scene 2 | Scene 3 | 比例式 |
| inner_outer_labels | Scene 3 | Scene 3 | 内外项标注 |
| mid_segments | Scene 4 | Scene 4 | 比例中项线段 |
| property_cards | Scene 5 | Scene 5 | 性质卡片 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 关键技术要点

### 1. 线段长度精确性
- 所有线段使用精确比例（2:3:4:6）
- 比例中项满足 b² = ac
- 内项积 = 外项积

### 2. 视觉层次
- 线段粗细: stroke_width=6（主要线段）
- 标签字体: font_size=24
- 公式字体: font_size=28
- 标注清晰，避免重叠

### 3. 动画节奏
- 线段创建: 0.6s
- 公式书写: 0.7-0.9s
- 理解停顿: 1.5s（关键步骤）
- 场景切换: 0.5s

### 4. 边界安全
- 线段主要在 y∈[-3, 3] 区域
- 公式在 y∈[-5, -3] 区域
- 标题在 y∈[5.5, 6.5] 区域

### 5. 颜色编码
- 线段a: 红色 #e74c3c
- 线段b: 蓝色 #3498db
- 线段c: 绿色 #2ecc71
- 线段d: 橙色 #f39c12
- 高亮: 黄色 YELLOW

---

## 验证检查项

- [ ] 所有比例关系精确验证
- [ ] 内项积 = 外项积（12 = 12）
- [ ] 比例中项 b² = ac（16 = 16）
- [ ] MathTex 中无中文字符
- [ ] 所有标注清晰可读
- [ ] 没有元素溢出边界
- [ ] 动画总时长在目标范围内
- [ ] 线段长度视觉上成比例