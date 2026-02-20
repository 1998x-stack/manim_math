# 方差与标准差 - 动画分镜脚本

## 元信息
- 目标时长: 60-70 秒
- 场景数量: 7 个
- 难度等级: 中等
- 主题: 统计学 - 方差与标准差

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数据点
COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比数据点
COLOR_MEAN = "#2ecc71"         # 绿色 - 平均数线
COLOR_DEVIATION = "#f39c12"    # 橙色 - 偏差线
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
```

## 数据设置
```python
# 两组数据用于对比
DATA_SET_A = [5, 5, 5, 5, 5]  # 稳定数据（方差=0）
DATA_SET_B = [1, 3, 5, 7, 9]  # 波动数据（方差较大）

MEAN_A = 5.0
MEAN_B = 5.0

# 计算方差
VARIANCE_A = 0.0
VARIANCE_B = 8.0
STD_DEV_A = 0.0
STD_DEV_B = 2.828
```

## 坐标系配置
```python
AXES_CONFIG = {
    "x_range": [0, 6, 1],     # [min, max, step]
    "y_range": [0, 10, 2],
    "x_length": 7,
    "y_length": 5,
    "axis_config": {
        "include_numbers": True,
        "font_size": 20
    }
}

# 位置: 主内容区域中心
AXES_POSITION = UP * 1.5
```

## 元素边界检查
- 坐标系: y ∈ [-1, +4]（主内容区）
- 标题: y = +6
- 公式: y ∈ [+4.5, +5.5]
- 说明文字: y ∈ [-5, -3]
- 作者信息: y = +7

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 两组数据点预览

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | 1.1s |
| 1.1s | 两组数据点快速显示 | `FadeIn(dots_a), FadeIn(dots_b)` | 1.7s |
| 1.7s | 问题文字 | `Write(question, run_time=1.0)` | 2.7s |
| 2.7s | 等待理解 | `Wait(1.5)` | 4.2s |

### 清理
- FadeOut: hook_text, question, initial_dots
- 保留: author_info

**检查点**: 
- hook_text 位置: y = +6 ✓
- question 位置: y = -5 ✓

---

## Scene 2: 建立坐标系 (5-10秒)
**目的**: 展示数据可视化基础

### 元素
1. 标题："方差 - 衡量数据的波动程度"
2. 坐标系（x轴：索引，y轴：数值）
3. 数据集A的点（稳定）

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 标题写入 | `Write(title)` | 0.8s |
| 0.8s | 坐标系创建 | `Create(axes)` | 1.8s |
| 1.8s | 数据集A点逐个出现 | `FadeIn(dot, scale=0.5) for each` | 3.3s |
| 3.3s | 标注"稳定数据" | `FadeIn(label_a)` | 3.8s |
| 3.8s | 等待 | `Wait(1.0)` | 4.8s |

### 清理
- 保留: axes, dots_a, label_a, title

**检查点**:
- axes 中心: UP * 1.5 ✓
- dots 在坐标系内 ✓

---

## Scene 3: 平均数线 (10-15秒)
**目的**: 引入平均数概念

### 元素
1. 平均数虚线（y = 5）
2. 平均数标签 x̄
3. 公式：x̄ = (x₁+x₂+...+xₙ)/n

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 平均数线绘制 | `Create(mean_line)` | 1.0s |
| 1.0s | 标签出现 | `FadeIn(mean_label)` | 1.4s |
| 1.4s | 公式写入 | `Write(formula_mean)` | 2.4s |
| 2.4s | 强调"数据中心" | `Indicate(mean_line)` | 3.0s |
| 3.0s | 等待 | `Wait(1.0)` | 4.0s |

### 清理
- FadeOut: formula_mean
- 保留: mean_line, mean_label

**检查点**:
- formula_mean 位置: y = +5 ✓

---

## Scene 4: 偏差可视化 (15-25秒)
**目的**: 展示每个数据点与平均数的距离

### 元素
1. 从每个点到平均数线的垂直线（偏差）
2. 偏差标注：(xᵢ - x̄)
3. 说明文字："偏差 = 数据点 - 平均数"

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 第1条偏差线 | `Create(dev_line_1)` | 0.5s |
| 0.5s | 偏差标签 | `FadeIn(dev_label_1)` | 0.8s |
| 0.8s | 第2-5条偏差线 | `Create(line) for lines 2-5` | 2.3s |
| 2.3s | 说明文字 | `FadeIn(explanation)` | 2.8s |
| 2.8s | 对于数据集A：所有偏差=0 | `Indicate(dots_a)` | 3.8s |
| 3.8s | 引入数据集B | `Transform to data_set_b` | 5.8s |
| 5.8s | 数据集B的偏差线 | `Create(dev_lines_b)` | 7.3s |
| 7.3s | 对比："波动更大！" | `FadeIn(comparison)` | 8.3s |
| 8.3s | 等待理解 | `Wait(1.5)` | 9.8s |

### 清理
- 保留: axes, dots_b, mean_line, dev_lines_b

**检查点**:
- dev_lines 在坐标系内 ✓
- explanation 位置: y = -4 ✓

---

## Scene 5: 方差公式推导 (25-40秒)
**目的**: 展示方差计算过程

### 元素
1. 方差公式：s² = [(x₁-x̄)² + ... + (xₙ-x̄)²]/n
2. 分步计算
3. 平方的几何意义（小正方形）

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 公式出现 | `Write(formula_variance)` | 1.5s |
| 1.5s | 强调"平方" | `Indicate(square_part)` | 2.0s |
| 2.0s | 为什么要平方？ | `FadeIn(why_square)` | 2.5s |
| 2.5s | 消除正负抵消 | `Show positive example` | 4.0s |
| 4.0s | 数据集B计算 | `Write step-by-step` | 7.0s |
| 7.0s | (1-5)²=16 | - | 7.5s |
| 7.5s | (3-5)²=4 | - | 8.0s |
| 8.0s | (5-5)²=0 | - | 8.5s |
| 8.5s | (7-5)²=4 | - | 9.0s |
| 9.0s | (9-5)²=16 | - | 9.5s |
| 9.5s | 求和：40 | - | 10.5s |
| 10.5s | 除以5：40/5=8 | - | 11.5s |
| 11.5s | 结果：s²=8 | `Indicate(result)` | 13.0s |
| 13.0s | 等待 | `Wait(1.5)` | 14.5s |

### 清理
- FadeOut: calculation steps
- 保留: formula_variance, result

**检查点**:
- formula_variance 位置: y = +5 ✓
- 计算步骤位置: y ∈ [0, +3] ✓

---

## Scene 6: 标准差 (40-50秒)
**目的**: 引入标准差，恢复原单位

### 元素
1. 标准差公式：s = √s²
2. 计算结果
3. 单位说明

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 标准差公式 | `Write(formula_std)` | 1.0s |
| 1.0s | 计算 | `Write(s = √8 ≈ 2.83)` | 2.0s |
| 2.0s | 单位说明 | `FadeIn(unit_explanation)` | 2.5s |
| 2.5s | 在图上标注±s | `Show std_dev bands` | 4.0s |
| 4.0s | 数据落在 [2.17, 7.83] | `Highlight range` | 5.5s |
| 5.5s | 等待 | `Wait(1.5)` | 7.0s |

### 清理
- FadeOut: formulas, bands
- 保留: axes, dots_b

**检查点**:
- std_dev bands 在坐标系内 ✓

---

## Scene 7: 对比总结 + 片尾 (50-70秒)
**目的**: 总结方差意义，引导关注

### 元素
1. 两组数据对比表
2. 核心要点
3. 片尾关注信息

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 清空画面 | `FadeOut(all)` | 0.5s |
| 0.5s | 对比表 | `FadeIn(comparison_table)` | 2.0s |
| 2.0s | 数据集A: s²=0 | - | 2.5s |
| 2.5s | 数据集B: s²=8 | - | 3.0s |
| 3.0s | 核心要点 | `Write(key_points)` | 5.0s |
| 5.0s | 方差越大→波动越大 | - | 6.0s |
| 6.0s | 方差越小→数据越稳定 | - | 7.0s |
| 7.0s | 简化公式 | `Write(simplified)` | 9.0s |
| 9.0s | s²=x̄²-x̄² | - | 10.0s |
| 10.0s | 片尾动画 | `Outro animation` | 14.0s |
| 14.0s | 关注提示 | - | 16.0s |
| 16.0s | 淡出 | `FadeOut(all)` | 18.0s |

**检查点**:
- comparison_table 位置: y ∈ [0, +4] ✓
- key_points 位置: y ∈ [-3, 0] ✓

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留顶部 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| dots_a | Scene 2 | Scene 4 | 稳定数据 |
| dots_b | Scene 4 | Scene 7 | 波动数据 |
| mean_line | Scene 3 | Scene 6 | 平均数线 |
| dev_lines | Scene 4 | Scene 5 | 偏差线 |
| formula_variance | Scene 5 | Scene 6 | 方差公式 |
| formula_std | Scene 6 | Scene 7 | 标准差公式 |
| comparison_table | Scene 7 | Scene 7 | 对比表 |

---

## 关键技术点

### 1. 坐标转换
```python
# 将数据坐标转换为Manim坐标
point = axes.c2p(x_index, y_value)  # coords_to_point
```

### 2. 偏差线绘制
```python
# 从数据点到平均数线的垂直线
dev_line = Line(
    axes.c2p(i, data[i]),
    axes.c2p(i, mean),
    color=COLOR_DEVIATION,
    stroke_width=3
)
```

### 3. 动态标签
```python
# 使用 DecimalNumber 显示动态数值
variance_value = DecimalNumber(
    0,
    num_decimal_places=2,
    color=COLOR_HIGHLIGHT
)
variance_value.add_updater(lambda m: m.set_value(current_variance))
```

### 4. 分步动画
```python
# 逐步展示计算过程
steps = VGroup(step1, step2, step3, ...)
self.play(
    LaggedStart(*[FadeIn(step) for step in steps], lag_ratio=0.3)
)
```

---

## 验证清单

### 几何验证（不适用 - 统计主题）
- ❌ 无需几何计算

### 数据验证
- [x] 数据集A方差 = 0
- [x] 数据集B方差 = 8
- [x] 平均数 = 5（两组相同）
- [x] 标准差B ≈ 2.83

### 视觉验证
- [x] 所有元素在边界内
- [x] 文字无重叠
- [x] 颜色对比清晰
- [x] 字体大小合适

### 节奏验证
- [x] 开场 < 5秒
- [x] 每个概念停留 2-3秒
- [x] 总时长 60-70秒
- [x] 难点（公式）停留更长

---

## 预期效果

1. **教学目标**：学生理解方差衡量数据波动，标准差恢复原单位
2. **视觉记忆**：偏差线长度 → 方差大小
3. **关键洞察**：相同平均数，不同方差 → 稳定性差异
4. **应用场景**：成绩分析、质量控制、风险评估

---

## 备注

- 本动画不涉及复杂几何，重点是数据可视化
- 使用 Axes 而非几何图形
- 颜色编码：蓝色（稳定）vs 红色（波动）
- 简化公式作为彩蛋，适合进阶学生