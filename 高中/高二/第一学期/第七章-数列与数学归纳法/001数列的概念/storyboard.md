# 数列的概念 - 动画分镜脚本

## 元信息
- **目标时长**: 75-85秒
- **场景数量**: 7个
- **难度等级**: 高二 (基础概念)
- **核心目标**: 让学生理解数列的本质、表示方法和基本性质

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#2ecc71"    # 绿色 - 次要元素
COLOR_HIGHLIGHT = "#e74c3c"    # 红色 - 高亮强调
COLOR_FORMULA = "#f39c12"      # 橙色 - 公式
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
COLOR_SEQUENCE = "#9b59b6"     # 紫色 - 数列点
```

## 几何预计算清单
由于本主题主要涉及数列（非几何图形），主要计算内容为：

| 元素 | 计算说明 | 存储变量 |
|------|---------|---------|
| 数轴刻度位置 | 等间距分布 | `self.tick_positions` |
| 数列项位置 | 基于索引的坐标 | `self.term_positions` |
| 坐标系网格 | x=[1,8], y=[0,18] | `self.axes` |
| 数列点坐标 | (n, aₙ) 映射 | `self.sequence_points` |

## 坐标系统说明
- **TikTok竖屏**: x ∈ [-4.5, 4.5], y ∈ [-8, 8]
- **安全区域**: x ∈ [-4, 4], y ∈ [-7, 7]
- **顶部标题区**: y ∈ [6, 7.5]
- **主内容区**: y ∈ [-3, 5.5]
- **底部文字区**: y ∈ [-6, -3]

---

## Scene 0: 初始化 (`setup_geometry`)
**目的**: 预计算所有数值和坐标

### 计算内容
```python
# 示例数列: aₙ = 2n (2, 4, 6, 8, 10, 12, 14, 16)
self.example_sequence = [2, 4, 6, 8, 10, 12, 14, 16]
self.sequence_indices = list(range(1, 9))  # n = 1, 2, ..., 8

# 数轴配置
self.numberline_range = [0, 18, 2]  # [min, max, step]
self.numberline_length = 7

# 坐标系配置
self.axes_x_range = [0, 9, 1]
self.axes_y_range = [0, 18, 2]
self.axes_width = 7
self.axes_height = 4.5

# 位置偏移
self.axes_offset = UP * 1.5

# 验证边界
assert all(-4 <= x <= 4 for x in [各种x坐标])
assert all(-7 <= y <= 7 for y in [各种y坐标])
```

---

## Scene 1: 开场钩子 (0-6秒)
**目的**: 吸引注意力，引出数列概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字标题)
3. 生活场景示例 (动画数字序列)

### 动画序列
| 时间 | 动作 | 代码参考 | 停留 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | - |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | - |
| 1.1s | 示例数字序列出现 | `LaggedStart(*[FadeIn(num) for num in numbers])` | - |
| 2.5s | 数字高亮闪烁 | `Succession(*[Flash(num) for num in numbers])` | 0.8s |
| 3.3s | 引出"数列"概念 | `FadeIn(concept_text, shift=UP*0.3)` | 1.2s |

### 内容文案
- **钩子**: "1, 2, 3, 5, 8, 13, 21... 发现规律了吗?"
- **示例**: 楼层号: 1F, 2F, 3F, 4F, 5F...
- **引出**: "这就是数学中的——数列!"

### 清理
- FadeOut: hook_text, numbers
- 保留: author_info (全程保留)

---

## Scene 2: 数列的定义 (6-16秒)
**目的**: 讲解数列的严格定义和记号

### 元素
1. 标题: "数列的概念"
2. 定义文字
3. 数列记号展示
4. 项的命名

### 动画序列
| 时间 | 动作 | 代码参考 | 停留 |
|------|------|---------|------|
| 6.0s | 标题出现 | `Write(title)` | - |
| 6.6s | 定义文字书写 | `Write(definition)` | 1.2s |
| 7.8s | 数列记号展示 | `Write(notation)` | - |
| 8.6s | 逐项高亮说明 | `Indicate(a1), Indicate(a2), ...` | - |
| 10.2s | 通项公式出现 | `FadeIn(general_term)` | 1.5s |

### 内容文案
- **定义**: "按照一定顺序排列的一列数"
- **记号**: {aₙ} = a₁, a₂, a₃, ..., aₙ, ...
- **说明**: 
  - a₁: 第1项
  - a₂: 第2项
  - aₙ: 第n项 (通项)

### 清理
- FadeOut: title, definition (保留notation作为参考)

---

## Scene 3: 数列与函数 (16-26秒)
**目的**: 揭示数列的函数本质

### 元素
1. 标题: "数列 = 特殊的函数"
2. 坐标系 (横轴n, 纵轴aₙ)
3. 离散点 (n, aₙ)
4. 函数对应关系

### 动画序列
| 时间 | 动作 | 代码参考 | 停留 |
|------|------|---------|------|
| 16.0s | 标题出现 | `FadeIn(title)` | - |
| 16.5s | 坐标系创建 | `Create(axes)` | - |
| 17.5s | 说明文字 | `FadeIn(explanation)` | 1.0s |
| 18.5s | 逐个绘制点 | `LaggedStart(*[GrowFromCenter(dot) for dot in dots])` | - |
| 20.5s | 箭头指示对应 | `Create(arrows)` | 1.2s |

### 坐标系配置
```python
axes = Axes(
    x_range=[0, 9, 1],     # n: 1→8
    y_range=[0, 18, 2],    # aₙ: 0→16
    x_length=7,
    y_length=4.5,
    axis_config={"include_numbers": True, "font_size": 20},
    tips=False
).move_to(UP * 1.5)
```

### 点的坐标
```python
# 示例: aₙ = 2n
points = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16)]
```

### 内容文案
- **标题**: "数列的函数本质"
- **说明**: "定义在正整数集上的函数: n → aₙ"

### 清理
- FadeOut: title, explanation, arrows
- 保留: axes, dots (用于下一场景)

---

## Scene 4: 数列的表示方法 (26-45秒)
**目的**: 介绍四种表示方法

### 4.1 通项公式法 (26-31秒)
| 时间 | 动作 | 内容 |
|------|------|------|
| 26.0s | 标题出现 | "① 通项公式法" |
| 26.5s | 公式书写 | aₙ = 2n |
| 27.5s | 逐项验证 | a₁=2×1=2, a₂=2×2=4, ... |
| 29.0s | 高亮优点 | "直接计算任意项" |

### 4.2 递推公式法 (31-36秒)
| 时间 | 动作 | 内容 |
|------|------|------|
| 31.0s | 标题切换 | "② 递推公式法" |
| 31.5s | 公式书写 | a₁=2, aₙ=aₙ₋₁+2 |
| 32.5s | 递推动画 | 2 → 4 → 6 → 8 (箭头动画) |
| 34.0s | 高亮特点 | "根据前项求后项" |

### 4.3 列表法 (36-40秒)
| 时间 | 动作 | 内容 |
|------|------|------|
| 36.0s | 标题切换 | "③ 列表法" |
| 36.5s | 表格出现 | n: 1 2 3 4 5 ... <br> aₙ: 2 4 6 8 10 ... |
| 38.0s | 高亮特点 | "直观明了" |

### 4.4 图像法 (40-45秒)
| 时间 | 动作 | 内容 |
|------|------|------|
| 40.0s | 标题切换 | "④ 图像法" |
| 40.5s | 点闪烁 | 之前的坐标系点高亮 |
| 41.5s | 连线动画 | 用虚线连接各点 |
| 43.0s | 高亮特点 | "看出变化趋势" |

### 清理
- FadeOut: 所有表示方法的文字和公式
- 保留: axes, dots

---

## Scene 5: 数列的分类 (45-58秒)
**目的**: 展示数列的不同类型

### 5.1 递增数列 (45-49秒)
```python
# 示例: 2, 4, 6, 8, 10, 12, 14, 16
点从左到右依次上升
```

### 5.2 递减数列 (49-52秒)
```python
# 示例: 16, 14, 12, 10, 8, 6, 4, 2
点从左到右依次下降
```

### 5.3 常数列 (52-55秒)
```python
# 示例: 5, 5, 5, 5, 5, 5, 5, 5
所有点在同一水平线
```

### 5.4 周期数列 (55-58秒)
```python
# 示例: 1, 2, 3, 1, 2, 3, 1, 2
点呈周期性波动
```

### 动画序列
| 时间 | 动作 | 代码 | 停留 |
|------|------|------|------|
| 45.0s | 标题 | "数列的分类" | - |
| 45.5s | 递增数列演示 | `Transform(dots, increasing_dots)` | 0.8s |
| 47.3s | 递减数列演示 | `Transform(dots, decreasing_dots)` | 0.8s |
| 49.1s | 常数列演示 | `Transform(dots, constant_dots)` | 0.8s |
| 50.9s | 周期数列演示 | `Transform(dots, periodic_dots)` | 1.0s |

### 清理
- FadeOut: axes, dots, 分类标题

---

## Scene 6: 前n项和 (58-70秒)
**目的**: 讲解前n项和的概念和公式

### 元素
1. 标题: "前n项和"
2. Sₙ 定义
3. 求和动画
4. aₙ 与 Sₙ 的关系

### 动画序列
| 时间 | 动作 | 代码参考 | 停留 |
|------|------|---------|------|
| 58.0s | 标题出现 | `Write(title)` | - |
| 58.6s | Sₙ定义 | `Write(sum_formula)` | 1.0s |
| 59.6s | 数列展示 | `Write(sequence)` | - |
| 60.4s | 求和动画 | `数字逐个飞入求和` | 1.5s |
| 61.9s | 结果显示 | `S₅ = 2+4+6+8+10 = 30` | 1.0s |
| 62.9s | 递推关系出现 | `aₙ = Sₙ - Sₙ₋₁` | 1.5s |
| 64.4s | 特殊情况 | `a₁ = S₁` | 1.2s |

### 内容文案
- **定义**: Sₙ = a₁ + a₂ + ... + aₙ
- **示例**: S₅ = 2 + 4 + 6 + 8 + 10 = 30
- **递推**: aₙ = Sₙ - Sₙ₋₁ (n ≥ 2)
- **特例**: a₁ = S₁

### 清理
- FadeOut: 所有公式和文字

---

## Scene 7: 总结 & 关注 (70-85秒)
**目的**: 总结要点，引导关注

### 元素
1. 知识点卡片
2. 作者信息放大
3. 关注提示
4. 装饰动画

### 动画序列
| 时间 | 动作 | 内容 | 停留 |
|------|------|------|------|
| 70.0s | 总结标题 | "数列核心要点" | - |
| 70.6s | 卡片1滑入 | "定义: 有序排列的数" | 0.3s |
| 71.4s | 卡片2滑入 | "本质: 离散函数 n→aₙ" | 0.3s |
| 72.2s | 卡片3滑入 | "表示: 通项/递推/列表/图像" | 0.3s |
| 73.0s | 卡片4滑入 | "分类: 递增/递减/常/周期" | 0.3s |
| 73.8s | 卡片5滑入 | "求和: Sₙ, aₙ=Sₙ-Sₙ₋₁" | 1.0s |
| 74.8s | 作者信息放大 | "@emptyandcalm" | - |
| 75.5s | 关注提示 | "关注我, 学更多数学!" | - |
| 76.5s | 装饰动画 | 数字旋转、闪烁 | 2.0s |

### 清理
- FadeOut: 全部元素

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 用途 | 备注 |
|------|---------|---------|------|------|
| author_info | Scene 1 | Scene 7 | 作者标识 | 全程保留 |
| axes | Scene 3 | Scene 5 | 坐标系 | 多场景复用 |
| sequence_dots | Scene 3 | Scene 5 | 数列点 | 变换展示不同类型 |
| notation | Scene 2 | Scene 2 | 数列记号 | 定义展示 |
| formulas | Scene 4/6 | Scene 4/6 | 公式展示 | 临时元素 |

---

## 关键技术点

### 1. 数轴动画
```python
numberline = NumberLine(
    x_range=[0, 18, 2],
    length=7,
    include_numbers=True,
    font_size=20
)
```

### 2. 坐标系配置
```python
axes = Axes(
    x_range=[0, 9, 1],
    y_range=[0, 18, 2],
    x_length=7,
    y_length=4.5,
    axis_config={"include_numbers": True}
).move_to(UP * 1.5)
```

### 3. 离散点绘制
```python
dots = VGroup(*[
    Dot(axes.c2p(n, 2*n), color=COLOR_SEQUENCE, radius=0.08)
    for n in range(1, 9)
])
```

### 4. 数字飞入动画
```python
numbers = VGroup(*[MathTex(str(a)) for a in [2,4,6,8,10]])
self.play(
    LaggedStart(*[
        number.animate.move_to(target_pos)
        for number, target_pos in zip(numbers, positions)
    ], lag_ratio=0.2)
)
```

### 5. 防止中文LaTeX错误
```python
# ❌ 错误
MathTex(r"数列")

# ✅ 正确
Text("数列", font="Noto Sans CJK SC")
```

---

## 边界安全检查

### 坐标范围验证
```python
def verify_boundaries():
    """验证所有元素在安全边界内"""
    SAFE_X = [-4, 4]
    SAFE_Y = [-7, 7]
    
    # 检查坐标系
    assert axes.get_left()[0] >= SAFE_X[0]
    assert axes.get_right()[0] <= SAFE_X[1]
    assert axes.get_bottom()[1] >= SAFE_Y[0]
    assert axes.get_top()[1] <= SAFE_Y[1]
    
    # 检查所有点
    for dot in dots:
        pos = dot.get_center()
        assert SAFE_X[0] <= pos[0] <= SAFE_X[1]
        assert SAFE_Y[0] <= pos[1] <= SAFE_Y[1]
```

---

## 时间分配总结

| 场景 | 时长 | 累计 | 重要度 |
|------|------|------|--------|
| Scene 1: 开场钩子 | 6s | 6s | ⭐⭐⭐ |
| Scene 2: 定义 | 10s | 16s | ⭐⭐⭐⭐⭐ |
| Scene 3: 函数本质 | 10s | 26s | ⭐⭐⭐⭐ |
| Scene 4: 表示方法 | 19s | 45s | ⭐⭐⭐⭐⭐ |
| Scene 5: 分类 | 13s | 58s | ⭐⭐⭐ |
| Scene 6: 前n项和 | 12s | 70s | ⭐⭐⭐⭐ |
| Scene 7: 总结关注 | 15s | 85s | ⭐⭐ |

**总时长**: 约 85 秒 (符合 TikTok 推荐长度)

---

## 待验证项

- [ ] 所有文字是否使用 `Text()` 而非 `MathTex()`
- [ ] 所有坐标是否在安全边界内
- [ ] LaTeX 公式是否避免中文字符
- [ ] 动画节奏是否流畅（不过快/过慢）
- [ ] 字体大小是否符合规范
- [ ] 作者信息是否全程显示