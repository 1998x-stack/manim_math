# 函数的奇偶性 - 动画分镜脚本

## 元信息
- 目标时长: 70-85秒
- 场景数量: 8个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_EVEN = "#e74c3c"       # 红色 - 偶函数
COLOR_ODD = "#3498db"        # 蓝色 - 奇函数
COLOR_Y_AXIS = "#2ecc71"     # 绿色 - y轴对称线
COLOR_ORIGIN = "#f39c12"     # 橙色 - 原点对称
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
BACKGROUND = "#1a1a2e"
```

## 数学元素预定义

### 函数定义
```python
# 偶函数示例
f_even(x) = x²
f_even_2(x) = cos(x)

# 奇函数示例
f_odd(x) = x³
f_odd_2(x) = sin(x)

# 定义域：均为 [-3, 3]
```

### 对称性验证点
```python
# 验证点对
对于 x = 2:
  偶函数: f(-2) = f(2) = 4
  奇函数: f(-2) = -f(2) = -8

对于 x = 0:
  奇函数必须: f(0) = 0
```

### 坐标系配置
```python
x_range = [-3, 3, 1]
y_range = [-9, 9, 3]
坐标轴位置: 中央 (y=0.5)
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出对称性问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 两个神秘的函数图像

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "函数也有对称美?" |
| 1.5s | 偶函数图像从左侧淡入 | `FadeIn(even_graph, shift=RIGHT)` |
| 2.5s | 奇函数图像从右侧淡入 | `FadeIn(odd_graph, shift=LEFT)` |
| 3.5s | 对称符号闪烁 | `Flash(symmetry_icons)` |
| 4.5s | 等待 | `Wait(0.5)` |

### 视觉布局
```
y = +7: 作者信息
y = +6: "函数也有对称美?"
y = [0, 5]: 两个函数图像（左右分开）
y = -2: 对称符号提示
```

### 清理
- FadeOut: hook_text, symmetry_icons
- 保留: author_info

---

## Scene 2: 偶函数定义 (5-15秒)
**目的**: 介绍偶函数的定义和y轴对称性

### 元素
1. 标题: "偶函数 Even Function"
2. 定义公式: f(-x) = f(x)
3. 坐标系 + f(x) = x²
4. y轴对称线
5. 对称点对

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题写入 | `Write(title)` |
| 5.8s | 定义公式淡入 | `FadeIn(definition)` |
| 6.5s | 创建坐标系 | `Create(axes)` |
| 7.5s | f(x)=x²图像生长 | `Create(even_graph)` |
| 8.5s | y轴高亮 | `y_axis.animate.set_color(COLOR_Y_AXIS).set_stroke_width(6)` |
| 9.0s | 说明"关于y轴对称" | `FadeIn(explain)` |
| 9.5s | 选取x=2点 | `FadeIn(dot_pos)` |
| 10.0s | 镜像到x=-2 | `Create(mirror_line)` + `FadeIn(dot_neg)` |
| 10.5s | 标注f(-2)=f(2) | `FadeIn(values)` |
| 11.5s | 虚线连接对称点 | `Create(dashed_horizontal)` |
| 13.0s | 等待理解 | `Wait(1.5)` |

### 几何计算
- 对称点对: (2, 4) ↔ (-2, 4)
- 镜像线: 垂直y轴的虚线
- y轴位置: x = 0

### 清理
- FadeOut: title, definition, dots, lines, values
- 保留: axes, even_graph (淡化)

---

## Scene 3: 奇函数定义 (15-25秒)
**目的**: 介绍奇函数的定义和原点对称性

### 元素
1. 标题: "奇函数 Odd Function"
2. 定义公式: f(-x) = -f(x)
3. f(x) = x³图像
4. 原点标记
5. 对称点对

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 15.0s | 清除前一场景 | `FadeOut(even_graph)` |
| 15.5s | 标题写入 | `Write(title)` |
| 16.3s | 定义公式淡入 | `FadeIn(definition)` |
| 17.0s | f(x)=x³图像生长 | `Create(odd_graph)` |
| 18.0s | 原点高亮 | `Indicate(origin_dot)` |
| 18.5s | 说明"关于原点对称" | `FadeIn(explain)` |
| 19.0s | 选取x=2点 | `FadeIn(dot_pos)` (2, 8) |
| 19.5s | 旋转到x=-2 | `Rotate(dot_pos, PI, about_point=ORIGIN)` |
| 20.0s | 显示对称点 | `FadeIn(dot_neg)` (-2, -8) |
| 20.5s | 标注f(-2)=-f(2) | `FadeIn(values)` |
| 21.5s | 通过原点的线 | `Create(line_through_origin)` |
| 23.0s | 等待理解 | `Wait(1.5)` |

### 几何计算
- 对称点对: (2, 8) ↔ (-2, -8)
- 旋转中心: 原点 (0, 0)
- 旋转角度: 180° (π)

### 清理
- FadeOut: title, definition, dots, lines, values
- 保留: axes, odd_graph (淡化)

---

## Scene 4: 对称性可视化对比 (25-35秒)
**目的**: 直观展示两种对称性的区别

### 元素
1. 分屏：左侧偶函数，右侧奇函数
2. 对称动画演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 25.0s | 重置坐标系 | `FadeOut(all)` |
| 26.0s | 左侧标题"偶函数" | `FadeIn(left_title)` |
| 26.5s | 右侧标题"奇函数" | `FadeIn(right_title)` |
| 27.0s | 左侧坐标系+图像 | `Create(left_axes, even_graph)` |
| 28.0s | 右侧坐标系+图像 | `Create(right_axes, odd_graph)` |
| 29.0s | 左侧y轴闪烁 | `Flash(y_axis_left, color=COLOR_Y_AXIS)` |
| 29.5s | 右侧原点闪烁 | `Flash(origin_right, color=COLOR_ORIGIN)` |
| 30.0s | 同步选点动画 | 两侧同时显示对称点对 |
| 32.0s | 镜像/旋转动画 | 左侧镜像，右侧旋转 |
| 34.0s | 等待对比 | `Wait(1.0)` |

### 视觉布局
```
左半屏 (x ∈ [-4, -0.5]):
  - 偶函数图像
  - y轴对称线

右半屏 (x ∈ [0.5, 4]):
  - 奇函数图像
  - 原点标记
```

### 清理
- FadeOut: 所有分屏元素

---

## Scene 5: 判断方法 (35-50秒)
**目的**: 教授判断奇偶性的两步法

### 元素
1. 标题: "如何判断奇偶性?"
2. 步骤卡片
3. 示例函数

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 35.0s | 标题淡入 | `FadeIn(title)` |
| 36.0s | 步骤1卡片滑入 | `step1.animate.shift(RIGHT*10)` |
| 37.5s | 示例：检查定义域 | 显示 f(x)=1/x，定义域 x≠0 |
| 39.0s | ✓ 关于原点对称 | `FadeIn(check_mark)` |
| 40.0s | 步骤2卡片滑入 | `step2.animate.shift(RIGHT*10)` |
| 41.5s | 计算f(-x) | 显示 f(-x) = 1/(-x) = -1/x |
| 43.0s | 对比f(x)和-f(x) | f(-x) = -f(x) ✓ |
| 44.5s | 结论闪烁 | `Flash(conclusion)` "奇函数!" |
| 46.0s | 图像验证 | `Create(graph)` 显示 1/x 图像 |
| 48.0s | 等待 | `Wait(1.5)` |

### 卡片内容
```
步骤1: 检查定义域是否关于原点对称
步骤2: 计算 f(-x)，比较与 f(x) 的关系
  - f(-x) = f(x) → 偶函数
  - f(-x) = -f(x) → 奇函数
```

### 清理
- FadeOut: title, cards, example

---

## Scene 6: 特殊性质 - f(0)=0 (50-58秒)
**目的**: 强调奇函数的关键性质

### 元素
1. 标题: "奇函数的特殊性质"
2. 重要公式框
3. 证明演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 50.0s | 标题淡入 | `FadeIn(title)` |
| 51.0s | 重要提示框 | `FadeIn(important_box)` |
| 52.0s | 公式书写 | `Write(formula)` "奇函数若在x=0有定义，则f(0)=0" |
| 53.5s | 证明步骤1 | `FadeIn(proof1)` f(-0) = -f(0) |
| 54.5s | 证明步骤2 | `FadeIn(proof2)` f(0) = -f(0) |
| 55.5s | 证明步骤3 | `FadeIn(proof3)` 2f(0) = 0 |
| 56.5s | 结论 | `FadeIn(conclusion)` f(0) = 0 |
| 57.5s | 图像验证 | 多个奇函数图像都过原点 |

### 证明框架
```
已知: f(-x) = -f(x)
令 x = 0:
  f(-0) = -f(0)
  f(0) = -f(0)
  2f(0) = 0
  ∴ f(0) = 0
```

### 清理
- FadeOut: title, box, proof

---

## Scene 7: 综合示例 (58-68秒)
**目的**: 展示常见函数的奇偶性

### 元素
1. 四个示例函数
2. 快速闪卡展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 58.0s | 标题"常见函数的奇偶性" | `Write(title)` |
| 59.0s | 示例1: x² | 图像+标注"偶" |
| 60.5s | 示例2: x³ | 图像+标注"奇" |
| 62.0s | 示例3: |x| | 图像+标注"偶" |
| 63.5s | 示例4: 1/x | 图像+标注"奇" |
| 65.0s | 四个图像同时显示 | `VGroup(all).arrange(2x2)` |
| 67.0s | 等待 | `Wait(1.0)` |

### 布局
```
┌────────┬────────┐
│  x²   │  x³   │
│ (偶)   │ (奇)   │
├────────┼────────┤
│ |x|   │  1/x  │
│ (偶)   │ (奇)   │
└────────┴────────┘
```

### 清理
- FadeOut: 所有示例

---

## Scene 8: 总结与片尾 (68-85秒)
**目的**: 复习要点，引导关注

### 元素
1. 要点卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 68.0s | 标题"函数奇偶性总结" | `Write(title)` |
| 69.0s | 要点1滑入 | "偶函数: f(-x)=f(x), y轴对称" |
| 70.0s | 要点2滑入 | "奇函数: f(-x)=-f(x), 原点对称" |
| 71.0s | 要点3滑入 | "判断: ①定义域对称 ②计算f(-x)" |
| 72.0s | 要点4滑入 | "特殊: 奇函数f(0)=0" |
| 73.5s | 重要提示框 | `FadeIn(tip_box)` "定义域必须关于原点对称!" |
| 75.0s | 作者信息放大 | `Transform(author)` |
| 76.5s | 关注提示 | `FadeIn(follow)` "关注我，学更多函数技巧!" |
| 78.0s | 装饰动画 | 对称图标旋转 |
| 81.0s | 等待 | `Wait(2.0)` |
| 83.0s | 全部淡出 | `FadeOut(VGroup(*all))` |

### 卡片内容
```
卡片1: 偶函数 - f(-x) = f(x) - y轴对称
卡片2: 奇函数 - f(-x) = -f(x) - 原点对称
卡片3: 判断方法 - 两步走
卡片4: 特殊性质 - f(0) = 0
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终显示 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| even_graph | Scene 2 | Scene 4 | f(x)=x² |
| odd_graph | Scene 3 | Scene 4 | f(x)=x³ |
| y_axis_highlight | Scene 2 | Scene 2 | y轴高亮 |
| origin_highlight | Scene 3 | Scene 3 | 原点高亮 |
| split_screen | Scene 4 | Scene 4 | 分屏对比 |
| step_cards | Scene 5 | Scene 5 | 判断步骤 |
| proof_box | Scene 6 | Scene 6 | 证明框 |
| examples_grid | Scene 7 | Scene 7 | 示例网格 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键时间节点检查

- [ ] 0-5s: 钩子足够吸引人（对称美）
- [ ] 每种对称性有独立展示（清晰分离）
- [ ] Scene 4: 对比动画（停留足够长）
- [ ] Scene 6: f(0)=0 证明（重点强调）
- [ ] 总时长控制在 70-85秒
- [ ] 片尾关注提示清晰

---

## 技术注意事项

### 坐标系边界
- 主内容区：y ∈ [-2, 6]（给图像留足空间）
- 标题区：y ∈ [5.5, 6.5]
- 说明文字区：y ∈ [-5.5, -4.5]
- 作者信息：y = +7（固定）

### 字体大小
- 标题: 36
- 副标题: 28
- 公式: 28
- 说明: 22
- 作者: 20

### 对称性验证
- y轴对称: 使用 `Reflect` 或手动计算镜像点
- 原点对称: 使用 `Rotate(angle=PI, about_point=ORIGIN)`
- 验证点对的y坐标关系

### 函数图像精度
- 使用 `axes.plot()` 时 `x_range` 需密集采样
- 奇函数确保过原点（x=0时y=0）
- 偶函数确保y轴两侧对称

### 颜色一致性
- 偶函数: 红色 `#e74c3c`
- 奇函数: 蓝色 `#3498db`
- y轴: 绿色 `#2ecc71`
- 原点: 橙色 `#f39c12`