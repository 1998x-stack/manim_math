# 数列的极限教学动画 - 分镜脚本

## 元信息
- **目标时长**: 90-110 秒
- **场景数量**: 7 个
- **难度等级**: 高二第一学期
- **知识点**: 数列的极限、收敛与发散、重要极限

## 颜色配置
```python
COLOR_LIMIT = "#e74c3c"         # 红色 - 极限值
COLOR_SEQUENCE = "#3498db"      # 蓝色 - 数列点
COLOR_CONVERGE = "#2ecc71"      # 绿色 - 收敛
COLOR_DIVERGE = "#e67e22"       # 橙色 - 发散
COLOR_EPSILON = "#9b59b6"       # 紫色 - ε邻域
COLOR_E = "#f39c12"             # 金色 - 自然常数e
COLOR_BACKGROUND = "#1a1a2e"    # 深蓝背景
```

## 核心数学元素预计算

### 极限示例数列
```python
# 示例1: aₙ = 1/n → 0
self.seq_1 = lambda n: 1/n
self.limit_1 = 0

# 示例2: aₙ = (n+1)/n → 1
self.seq_2 = lambda n: (n+1)/n
self.limit_2 = 1

# 示例3: aₙ = (1+1/n)^n → e
self.seq_3 = lambda n: (1 + 1/n)**n
self.limit_3 = np.e  # ≈ 2.718

# 发散示例: aₙ = n
self.seq_diverge = lambda n: n
```

### 坐标系配置
```python
# 配置1: 展示1/n趋向0
self.axes_1_config = {
    "x_range": [0, 20, 5],
    "y_range": [0, 1.2, 0.2],
    "x_length": 6,
    "y_length": 5,
    "axis_config": {"include_numbers": True}
}

# 配置2: 展示(1+1/n)^n趋向e
self.axes_2_config = {
    "x_range": [0, 50, 10],
    "y_range": [0, 3.5, 0.5],
    "x_length": 6,
    "y_length": 5,
    "axis_config": {"include_numbers": True}
}
```

### 几何验证清单
| 验证项 | 公式 | 说明 |
|--------|------|------|
| 极限值正确性 | \|aₙ - L\| < ε | 对充分大的n验证 |
| 收敛性 | lim aₙ 存在 | 数值验证 |
| e的计算 | (1+1/n)^n ≈ 2.718 | n→∞时验证 |
| 点在坐标系内 | axes.c2p() | 所有点位置验证 |

---

## Scene 1: 开场钩子 (5-6秒)
**目的**: 快速吸引注意力，引出极限概念

### 元素
1. 作者标识（顶部）
2. 钩子问题："0.9, 0.99, 0.999, ...接近什么？"
3. 数字逐渐增加动画

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 顶部灰色小字 |
| 0.3s | 钩子问题书写 | `Write(hook_question)` | "无限接近的奥秘" |
| 1.0s | 数字序列 | `Write(number_seq)` | "0.9, 0.99, 0.999, 0.9999, ..." |
| 2.5s | 箭头指向 | `GrowArrow(arrow)` | 指向"1" |
| 3.5s | 闪烁强调 | `Flash(target_number)` | "1" 闪烁 |
| 4.0s | 等待 | `self.wait(0.5)` | 悬念 |

### 几何计算
```python
# 数字位置
numbers_positions = [
    UP * 2 + LEFT * 3,
    UP * 2 + LEFT * 1,
    UP * 2 + RIGHT * 1,
    UP * 2 + RIGHT * 3,
]

# 目标数字
target_position = DOWN * 0.5
```

### 清理
- FadeOut: number_seq, arrow
- 保留: author_info

---

## Scene 2: 极限定义 (15-18秒)
**目的**: 清晰定义极限，可视化展示

### 元素
1. 定义文字（中文）
2. 数学表达式：lim(n→∞) aₙ = A
3. 坐标系展示数列点趋近极限
4. ε邻域动画

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题出现 | `Write(title)` | "数列的极限" |
| 0.6s | 定义文字 | `FadeIn(definition)` | "当n无限增大时，aₙ无限接近常数A" |
| 1.5s | 公式 | `Write(formula)` | lim(n→∞) aₙ = A |
| 2.5s | 坐标系创建 | `Create(axes)` | x-n, y-aₙ 坐标系 |
| 3.5s | 极限线 | `Create(limit_line)` | y=A 虚线 |
| 4.0s | 数列点依次 | `LaggedStart(*[FadeIn(dot) for dot in dots])` | n=1,2,3,...,10 |
| 6.0s | ε邻域 | `Create(epsilon_band)` | A±ε 区域 |
| 7.5s | 说明文字 | `FadeIn(note)` | "最终所有点都在ε邻域内" |
| 9.0s | 等待 | `self.wait(2.0)` | 理解概念 |

### 几何计算
```python
# 示例数列: aₙ = 1/n
n_values = range(1, 11)
sequence_points = []

for n in n_values:
    an = 1/n
    point = axes.c2p(n, an)
    sequence_points.append(point)

# 极限线 y=0
limit_y = 0
limit_line_start = axes.c2p(0, limit_y)
limit_line_end = axes.c2p(20, limit_y)

# ε邻域
epsilon = 0.3
upper_bound = limit_y + epsilon
lower_bound = limit_y - epsilon

# 验证收敛
for n in range(50, 101):
    an = 1/n
    assert abs(an - limit_y) < epsilon
```

### 清理
- FadeOut: definition, note
- 保留: title (缩小), axes, limit_line, epsilon_band (淡化)

---

## Scene 3: 收敛与发散 (12-15秒)
**目的**: 对比收敛和发散数列

### 元素
1. 左侧：收敛数列 (1+1/n)
2. 右侧：发散数列 (n)
3. 标签和箭头

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "收敛 vs 发散" |
| 0.6s | 左坐标系 | `Create(axes_left)` | 收敛示例 |
| 1.0s | 右坐标系 | `Create(axes_right)` | 发散示例 |
| 1.8s | 左侧点 | `LaggedStart(dots_converge)` | (n+1)/n → 1 |
| 3.0s | 左极限线 | `Create(limit_line_left)` | y=1 虚线 |
| 3.8s | 收敛标签 | `FadeIn(label_converge)` | "收敛 ✓" 绿色 |
| 4.8s | 右侧点 | `LaggedStart(dots_diverge)` | n → ∞ |
| 6.0s | 上升箭头 | `GrowArrow(arrow_up)` | 指向上方 |
| 6.8s | 发散标签 | `FadeIn(label_diverge)` | "发散 ✗" 橙色 |
| 8.0s | 对比说明 | `FadeIn(comparison)` | "收敛：有极限；发散：无极限" |
| 10.0s | 等待 | `self.wait(1.5)` | 理解对比 |

### 几何计算
```python
# 收敛数列：aₙ = (n+1)/n = 1 + 1/n → 1
converge_seq = lambda n: 1 + 1/n
converge_limit = 1

# 发散数列：aₙ = n → ∞
diverge_seq = lambda n: n

# 左坐标系配置
axes_left_config = {
    "x_range": [0, 10, 2],
    "y_range": [0, 2.5, 0.5],
    "x_length": 3,
    "y_length": 4,
}

# 右坐标系配置（y轴需要很大范围）
axes_right_config = {
    "x_range": [0, 10, 2],
    "y_range": [0, 12, 2],
    "x_length": 3,
    "y_length": 4,
}

# 验证收敛
for n in range(1, 51):
    an = converge_seq(n)
    assert abs(an - converge_limit) < 0.1 or n < 10
```

### 清理
- FadeOut: 所有坐标系、点、标签
- 保留: 无

---

## Scene 4: 重要极限1 - lim(1/n)=0 (15-18秒)
**目的**: 详细展示最基础的重要极限

### 元素
1. 公式：lim(n→∞) 1/n = 0
2. 坐标系展示
3. 数值表格
4. 趋近动画

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "重要极限①" |
| 0.6s | 公式 | `Write(formula)` | lim(n→∞) 1/n = 0 |
| 1.5s | 公式强调 | `formula.animate.scale(1.2).set_color(COLOR_LIMIT)` | 放大高亮 |
| 2.5s | 坐标系 | `Create(axes)` | 创建坐标系 |
| 3.2s | 极限线 | `Create(limit_line)` | y=0 红色虚线 |
| 3.8s | 数列点1-5 | `LaggedStart(dots_1_5)` | n=1,2,3,4,5 |
| 5.0s | 数值表格 | `Create(table)` | n | 1/n 对应值 |
| 6.5s | 表格填充 | `Write(table_entries)` | 1→1, 5→0.2, 10→0.1, 100→0.01 |
| 8.5s | 数列点6-20 | `LaggedStart(dots_6_20)` | 加速显示 |
| 10.0s | 趋近箭头 | `GrowArrow(arrow_to_zero)` | 指向y=0 |
| 11.0s | 说明 | `FadeIn(explanation)` | "n越大，1/n越接近0" |
| 13.0s | 等待 | `self.wait(2.0)` | 理解 |

### 几何计算
```python
# 数列：aₙ = 1/n
seq = lambda n: 1/n
limit = 0

# 坐标系
axes_config = {
    "x_range": [0, 20, 5],
    "y_range": [0, 1.2, 0.2],
    "x_length": 6,
    "y_length": 5,
}

# 数值验证
test_values = [1, 5, 10, 20, 50, 100, 1000]
for n in test_values:
    an = 1/n
    print(f"n={n}: 1/n={an:.6f}")
    # n=1: 1/n=1.000000
    # n=100: 1/n=0.010000
    # n=1000: 1/n=0.001000

# 验证极限
assert abs(1/1000 - 0) < 0.01
```

### 清理
- FadeOut: table, explanation
- 保留: formula (缩小), axes (淡化)

---

## Scene 5: 重要极限2 - lim(1+1/n)^n=e (20-25秒)
**目的**: 展示自然常数e的重要极限

### 元素
1. 公式：lim(n→∞) (1+1/n)^n = e
2. 坐标系展示逐渐趋近e
3. e的值动画
4. 数值计算表

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "重要极限②" |
| 0.6s | 公式 | `Write(formula)` | lim(n→∞) (1+1/n)^n = e |
| 1.8s | e的定义 | `FadeIn(e_definition)` | "e ≈ 2.71828..." |
| 2.8s | 公式强调 | `formula.animate.scale(1.15).set_color(COLOR_E)` | 金色 |
| 3.8s | 坐标系 | `Create(axes)` | 更大范围 |
| 4.5s | e参考线 | `Create(e_line)` | y=e 虚线 |
| 5.2s | 数列点1-10 | `LaggedStart(dots_1_10)` | 从下方逐渐上升 |
| 7.5s | 数值表格 | `Create(table)` | n | (1+1/n)^n |
| 9.0s | 表格填充 | `Write(table_entries)` | n=1→2, 5→2.488, 10→2.594, 50→2.692 |
| 11.5s | 数列点11-50 | `LaggedStart(dots_11_50)` | 加速，接近e |
| 13.5s | 趋近动画 | `Indicate(e_line)` | 闪烁e线 |
| 14.5s | 说明 | `FadeIn(explanation)` | "e是数学中最重要的常数之一" |
| 16.0s | 应用提示 | `FadeIn(applications)` | "复利计算、微积分基础" |
| 18.0s | 等待 | `self.wait(2.5)` | 重要概念 |

### 几何计算
```python
# 数列：aₙ = (1+1/n)^n
seq = lambda n: (1 + 1/n)**n
limit = np.e  # ≈ 2.718281828...

# 坐标系
axes_config = {
    "x_range": [0, 50, 10],
    "y_range": [0, 3.5, 0.5],
    "x_length": 6,
    "y_length": 5,
}

# 数值验证
test_values = [1, 2, 5, 10, 20, 50, 100, 1000]
for n in test_values:
    an = (1 + 1/n)**n
    print(f"n={n}: (1+1/n)^n={an:.6f}, e={np.e:.6f}, diff={abs(an-np.e):.6f}")

# 验证收敛到e
assert abs((1 + 1/1000)**1000 - np.e) < 0.001
```

### 清理
- FadeOut: axes, table, explanation, applications
- 保留: formula (缩小)

---

## Scene 6: 极限运算法则 (12-15秒)
**目的**: 介绍极限的四则运算

### 元素
1. 四个运算法则
2. 示例计算
3. 注意事项

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "极限运算法则" |
| 0.6s | 法则1 | `FadeIn(rule_1)` | lim(aₙ±bₙ) = lim aₙ ± lim bₙ |
| 1.4s | 法则2 | `FadeIn(rule_2)` | lim(aₙ·bₙ) = lim aₙ · lim bₙ |
| 2.2s | 法则3 | `FadeIn(rule_3)` | lim(aₙ/bₙ) = lim aₙ / lim bₙ |
| 3.0s | 条件 | `FadeIn(condition)` | "(lim bₙ ≠ 0)" 红色 |
| 4.0s | 示例标题 | `Write(example_title)` | "示例：" |
| 4.8s | 示例问题 | `Write(example_problem)` | "lim[(2n+1)/n]" |
| 5.8s | 步骤1 | `Write(step_1)` | "= lim(2 + 1/n)" |
| 6.8s | 步骤2 | `Write(step_2)` | "= lim 2 + lim(1/n)" |
| 7.8s | 步骤3 | `Write(step_3)` | "= 2 + 0 = 2" |
| 9.0s | 框选答案 | `Create(answer_box)` | 框选"2" |
| 10.0s | 等待 | `self.wait(1.5)` | 理解运算 |

### 几何计算
```python
# 验证示例计算
seq = lambda n: (2*n + 1) / n
limit_calculated = 2

# 数值验证
for n in [10, 100, 1000]:
    an = (2*n + 1) / n
    print(f"n={n}: (2n+1)/n={an:.6f}, limit={limit_calculated}")
    assert abs(an - limit_calculated) < 0.01 or n < 100
```

### 清理
- FadeOut: 所有法则和示例
- 保留: 无

---

## Scene 7: 总结与关注 (10-12秒)
**目的**: 总结关键点，引导关注

### 元素
1. 关键概念总结
2. 重要极限汇总
3. 作者信息和关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "数列极限要点" |
| 0.6s | 要点1 | `FadeIn(point_1)` | "极限：n→∞时aₙ接近常数A" |
| 1.4s | 要点2 | `FadeIn(point_2)` | "收敛/发散：极限存在/不存在" |
| 2.2s | 要点3 | `FadeIn(point_3)` | "重要极限：1/n→0, (1+1/n)^n→e" |
| 3.2s | 公式卡片1 | `FadeIn(card_1)` | lim(1/n)=0 |
| 4.0s | 公式卡片2 | `FadeIn(card_2)` | lim(1+1/n)^n=e |
| 4.8s | 作者放大 | `author_info.animate.scale(2).move_to(CENTER)` | 居中 |
| 5.8s | 关注提示 | `Write(follow_text)` | "关注我，掌握极限技巧！" |
| 7.0s | 点赞图标 | `FadeIn(like_icon, scale=0.5)` | Star图标 |
| 8.0s | 闪烁 | `Flash(like_icon)` | 强调 |
| 9.5s | 等待 | `self.wait(1.5)` | 结束停留 |

### 几何计算
无特殊几何计算

### 清理
全部保留至结束

---

## 元素生命周期追踪表

| 元素ID | 创建场景 | 销毁场景 | 持续场景 | 备注 |
|--------|---------|---------|---------|------|
| `author_info` | Scene 1 | Scene 7 | 全程 | 顶部作者信息 |
| `limit_formula` | Scene 2 | Scene 7 | 2-7 | 极限定义公式（缩小后保留） |
| `axes_main` | Scene 2 | Scene 3结束 | 2-3 | 主坐标系 |
| `formula_1_n` | Scene 4 | Scene 7 | 4-7 | lim(1/n)=0（缩小后保留） |
| `formula_e` | Scene 5 | Scene 7 | 5-7 | lim(1+1/n)^n=e（缩小后保留） |

---

## 动画节奏控制

### 各场景时长分配
| 场景 | 时长 | 节奏 | 说明 |
|------|------|------|------|
| Scene 1 | 5-6s | 快 | 吸引注意 |
| Scene 2 | 15-18s | 慢 | 核心定义，重点 |
| Scene 3 | 12-15s | 中 | 概念对比 |
| Scene 4 | 15-18s | 慢 | 重要极限1，详细 |
| Scene 5 | 20-25s | 慢 | 重要极限2，最重要 |
| Scene 6 | 12-15s | 中 | 运算法则 |
| Scene 7 | 10-12s | 中 | 总结收尾 |

### 停顿策略
- **核心定义后**: 2-3秒（Scene 2）
- **重要极限后**: 2-2.5秒（Scene 4, 5）
- **示例计算后**: 1.5秒（Scene 6）
- **总计**: 约95秒（符合TikTok合理长度）

---

## 渲染命令

```bash
# 快速预览（开发阶段）
manim -pql sequence_limit.py SequenceLimit

# 高质量渲染（最终输出）
manim -qh sequence_limit.py SequenceLimit

# 4K渲染（如需要）
manim -qk sequence_limit.py SequenceLimit
```

---

## 质量检查清单

### 内容完整性
- [ ] 极限定义清晰
- [ ] 收敛/发散对比明显
- [ ] 两个重要极限详细展示
- [ ] 运算法则有示例
- [ ] 有数值验证

### 技术规范
- [ ] 所有LaTeX无中文
- [ ] 坐标系点位置正确
- [ ] 元素位置在安全边界
- [ ] 极限值精确计算

### 动画质量
- [ ] 趋近过程可视化
- [ ] 数列点动画流畅
- [ ] 颜色对比清晰
- [ ] 无溢出或重叠

### 教学效果
- [ ] 开场有吸引力
- [ ] 概念直观易懂
- [ ] 重点突出
- [ ] 有总结

---

## 备注

1. **可视化重点**: 用坐标系上的点展示"趋近"过程
2. **e的重要性**: 强调这是数学中最重要的常数之一
3. **动画关键**: 
   - 点的依次出现要有节奏感
   - 极限线要清晰醒目
   - ε邻域要直观
4. **时间分配**: Scene 5 (e的极限) 占25%时间，最重要
5. **颜色编码**: 极限值用红色，收敛用绿色，发散用橙色