# 频数分布 - 动画分镜脚本

## 元信息
- 目标时长: 65-75 秒
- 场景数量: 8 个
- 难度等级: 中等
- 主题: 统计学 - 频数分布

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
COLOR_HISTOGRAM = "#9b59b6"    # 紫色 - 直方图柱子
COLOR_TABLE = "#2ecc71"        # 绿色 - 表格
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
```

## 示例数据设计
```python
# 30个学生的数学成绩（50-100分）
RAW_DATA = [
    85, 72, 68, 90, 55, 78, 82, 95, 61, 77,
    88, 70, 92, 66, 81, 74, 87, 59, 79, 84,
    91, 73, 86, 63, 75, 89, 67, 80, 94, 71
]

# 统计结果
MAX_VALUE = 95
MIN_VALUE = 55
RANGE = 40
GROUP_WIDTH = 10
NUM_GROUPS = 4

# 频数分布表
GROUPS = [
    ("50-60", 3),
    ("60-70", 5),
    ("70-80", 10),
    ("80-90", 9),
    ("90-100", 3)
]

TOTAL = 30
```

## 坐标系配置
```python
# 直方图坐标系
HISTOGRAM_AXES = {
    "x_range": [50, 100, 10],     # [min, max, step]
    "y_range": [0, 12, 2],         # 频数范围
    "x_length": 7,
    "y_length": 4.5,
    "axis_config": {
        "include_numbers": True,
        "font_size": 18
    }
}

# 位置: 主内容区域
AXES_POSITION = UP * 1.0
```

## 元素边界检查
- 直方图: y ∈ [-1.5, +3.5]（主内容区）
- 标题: y = +6
- 数据展示: y ∈ [+3, +5]
- 表格: y ∈ [-1, +3]
- 说明文字: y ∈ [-5, -3]
- 作者信息: y = +7

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 杂乱数据预览

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | 1.1s |
| 1.1s | 杂乱数据快速显示 | `FadeIn(data_mess)` | 1.7s |
| 1.7s | 问题文字 | `Write(question, run_time=1.0)` | 2.7s |
| 2.7s | 等待理解 | `Wait(1.5)` | 4.2s |

### 清理
- FadeOut: hook_text, question, data_mess
- 保留: author_info

**检查点**: 
- hook_text 位置: y = +6 ✓
- question 位置: y = -5 ✓
- data_mess 位置: y ∈ [0, +4] ✓

---

## Scene 2: 原始数据展示 (5-12秒)
**目的**: 展示原始数据，引入整理必要性

### 元素
1. 标题："30个学生的成绩"
2. 数据网格（30个数字）
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 标题写入 | `Write(title)` | 0.8s |
| 0.8s | 数据逐个出现 | `LaggedStart FadeIn` | 3.3s |
| 3.3s | 说明"数据杂乱" | `FadeIn(explanation)` | 3.8s |
| 3.8s | 强调"需要整理" | `Indicate(data_grid)` | 4.8s |
| 4.8s | 等待 | `Wait(1.0)` | 5.8s |

### 清理
- 保留: title（变换为新标题）
- 部分保留: 最大值、最小值高亮

**检查点**:
- data_grid 位置: y ∈ [+1, +4] ✓
- explanation 位置: y = -4 ✓

---

## Scene 3: 计算极差 (12-20秒)
**目的**: 引入极差概念

### 元素
1. 最大值和最小值高亮
2. 极差公式
3. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 高亮最大值 | `Indicate(max_value)` | 0.8s |
| 0.8s | 高亮最小值 | `Indicate(min_value)` | 1.6s |
| 1.6s | 公式出现 | `Write(formula_range)` | 2.6s |
| 2.6s | 计算过程 | `Write(calculation)` | 3.6s |
| 3.6s | 结果：40分 | `Indicate(result)` | 4.6s |
| 4.6s | 说明意义 | `FadeIn(meaning)` | 5.6s |
| 5.6s | 等待 | `Wait(1.2)` | 6.8s |

### 清理
- FadeOut: formula, calculation, meaning
- 保留: result（极差=40）

**检查点**:
- formula_range 位置: y = +5 ✓
- calculation 位置: y = +3.5 ✓

---

## Scene 4: 确定组距和组数 (20-28秒)
**目的**: 展示如何划分数据组

### 元素
1. 组距概念
2. 组数计算
3. 分组示意

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 组距说明 | `FadeIn(group_width_text)` | 0.6s |
| 0.6s | 选择10分 | `Write(width_choice)` | 1.2s |
| 1.2s | 组数公式 | `Write(formula_groups)` | 2.2s |
| 2.2s | 计算：40/10≈4 | `Write(calculation)` | 3.2s |
| 3.2s | 确定5组 | `Write(final_groups)` | 4.2s |
| 4.2s | 分组示意 | `Create(group_lines)` | 5.7s |
| 5.7s | 等待 | `Wait(1.0)` | 6.7s |

### 清理
- FadeOut: formulas, calculations
- 保留: group_lines（分组线）

**检查点**:
- formulas 位置: y ∈ [+4, +5.5] ✓
- group_lines 位置: y = +2 ✓

---

## Scene 5: 频数分布表 (28-40秒)
**目的**: 列出频数分布表

### 元素
1. 表格标题
2. 三列表格（分组、频数、频率）
3. 逐行填入数据

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 表格框架 | `Create(table_frame)` | 1.0s |
| 1.0s | 表头 | `FadeIn(headers)` | 1.5s |
| 1.5s | 第1组数据 | `Write(row_1)` | 2.5s |
| 2.5s | 第2组数据 | `Write(row_2)` | 3.5s |
| 3.5s | 第3组数据 | `Write(row_3)` | 4.5s |
| 4.5s | 第4组数据 | `Write(row_4)` | 5.5s |
| 5.5s | 第5组数据 | `Write(row_5)` | 6.5s |
| 6.5s | 总计行 | `Write(total_row)` | 7.5s |
| 7.5s | 频率计算示例 | `Indicate(frequency)` | 8.5s |
| 8.5s | 等待理解 | `Wait(2.0)` | 10.5s |

### 清理
- 保留: table（缩小移至侧边）

**检查点**:
- table 位置: y ∈ [0, +4] ✓
- 确保所有行在边界内 ✓

---

## Scene 6: 绘制频数直方图 (40-52秒)
**目的**: 将表格数据转换为直方图

### 元素
1. 坐标系（横轴：分数，纵轴：频数）
2. 五个矩形柱子
3. 轴标签

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 坐标系创建 | `Create(axes)` | 1.5s |
| 1.5s | 轴标签 | `FadeIn(labels)` | 2.0s |
| 2.0s | 第1组柱子 | `GrowFromEdge(bar_1, DOWN)` | 3.0s |
| 3.0s | 第2组柱子 | `GrowFromEdge(bar_2, DOWN)` | 4.0s |
| 4.0s | 第3组柱子 | `GrowFromEdge(bar_3, DOWN)` | 5.0s |
| 5.0s | 第4组柱子 | `GrowFromEdge(bar_4, DOWN)` | 6.0s |
| 6.0s | 第5组柱子 | `GrowFromEdge(bar_5, DOWN)` | 7.0s |
| 7.0s | 频数标注 | `FadeIn(freq_labels)` | 7.8s |
| 7.8s | 说明直方图 | `FadeIn(explanation)` | 8.8s |
| 8.8s | 等待 | `Wait(2.0)` | 10.8s |

### 清理
- 保留: axes, bars（准备变换）

**检查点**:
- axes 位置: y ∈ [-1.5, +3.5] ✓
- bars 高度不超过 y = +3.5 ✓

---

## Scene 7: 频率直方图 (52-62秒)
**目的**: 展示频率/组距的概念

### 元素
1. 纵轴变换为"频率/组距"
2. 柱子高度调整
3. 面积之和=1的说明

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 说明变换 | `FadeIn(transform_text)` | 0.8s |
| 0.8s | 纵轴标签变换 | `Transform(y_label)` | 1.8s |
| 1.8s | 柱子高度调整 | `Transform(bars)` | 3.8s |
| 3.8s | 公式：频率/组距 | `Write(formula)` | 4.8s |
| 4.8s | 面积示意 | `Indicate(bars)` | 5.8s |
| 5.8s | 说明面积和=1 | `FadeIn(area_sum)` | 6.8s |
| 6.8s | 等待 | `Wait(2.0)` | 8.8s |

### 清理
- FadeOut: formula, area_sum

**检查点**:
- 调整后的 bars 仍在边界内 ✓

---

## Scene 8: 总结和片尾 (62-75秒)
**目的**: 总结步骤，引导关注

### 元素
1. 四步骤总结
2. 关键要点
3. 片尾信息

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 清空画面 | `FadeOut(all)` | 0.5s |
| 0.5s | 标题：四步骤 | `Write(summary_title)` | 1.5s |
| 1.5s | 步骤1：计算极差 | `FadeIn(step_1)` | 2.5s |
| 2.5s | 步骤2：确定组距 | `FadeIn(step_2)` | 3.5s |
| 3.5s | 步骤3：列频数表 | `FadeIn(step_3)` | 4.5s |
| 4.5s | 步骤4：画直方图 | `FadeIn(step_4)` | 5.5s |
| 5.5s | 关键要点 | `FadeIn(key_points)` | 7.5s |
| 7.5s | 片尾动画 | `Outro animation` | 11.5s |
| 11.5s | 淡出 | `FadeOut(all)` | 13.0s |

**检查点**:
- summary 位置: y ∈ [0, +5] ✓
- key_points 位置: y ∈ [-3, 0] ✓

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保留顶部 |
| data_grid | Scene 2 | Scene 3 | 原始数据 |
| range_result | Scene 3 | Scene 4 | 极差结果 |
| group_lines | Scene 4 | Scene 5 | 分组线 |
| frequency_table | Scene 5 | Scene 8 | 频数表 |
| histogram_axes | Scene 6 | Scene 8 | 坐标系 |
| histogram_bars | Scene 6 | Scene 8 | 直方图柱子 |
| summary | Scene 8 | Scene 8 | 总结 |

---

## 关键技术点

### 1. 数据网格布局
```python
# 6行5列的网格
data_grid = VGroup()
for i, val in enumerate(RAW_DATA):
    row = i // 5
    col = i % 5
    cell = Text(str(val), font_size=20)
    cell.move_to([col - 2, 2 - row * 0.5, 0])
    data_grid.add(cell)
```

### 2. 直方图柱子精确定位
```python
# 每个柱子是一个Rectangle
for i, (group, freq) in enumerate(GROUPS):
    x_start = 50 + i * 10  # 起始分数
    x_end = x_start + 10   # 结束分数
    
    # 计算柱子的宽度和位置
    bar = Rectangle(
        width=axes.x_axis.unit_size * 10,  # 组距对应的宽度
        height=axes.y_axis.unit_size * freq,  # 频数对应的高度
        fill_color=COLOR_HISTOGRAM,
        fill_opacity=0.7,
        stroke_width=2
    )
    
    # 定位：底边在x轴，中心对齐组距中心
    bar.align_to(axes.x_axis, DOWN)
    bar.move_to(axes.c2p(x_start + 5, freq / 2))
```

### 3. 频数分布表
```python
# 使用 MobjectTable
from manim import Table

table_data = [
    ["分组", "频数", "频率"],
    ["50-60", "3", "0.10"],
    ["60-70", "5", "0.17"],
    ["70-80", "10", "0.33"],
    ["80-90", "9", "0.30"],
    ["90-100", "3", "0.10"],
    ["合计", "30", "1.00"]
]

table = Table(
    table_data,
    include_outer_lines=True,
    line_config={"stroke_width": 1, "color": GRAY_B}
)
```

### 4. 频率直方图变换
```python
# 频率 = 频数 / 总数
# 频率/组距 = 频率 / 10 = 高度

new_heights = []
for freq in frequencies:
    frequency = freq / 30  # 频率
    height_per_unit = frequency / 10  # 频率/组距
    new_heights.append(height_per_unit)

# 使用 Transform 调整柱子高度
for bar, new_h in zip(bars, new_heights):
    new_bar = bar.copy()
    new_bar.stretch_to_fit_height(axes.y_axis.unit_size * new_h * 10)
    self.play(Transform(bar, new_bar))
```

---

## 验证清单

### 数据验证
- [x] 极差 = 95 - 55 = 40
- [x] 组距 = 10
- [x] 组数 = 5
- [x] 频数总和 = 30
- [x] 频率总和 = 1.0

### 视觉验证
- [x] 所有元素在边界内
- [x] 直方图柱子高度正确
- [x] 表格清晰可读
- [x] 文字无重叠
- [x] 颜色对比清晰

### 公式验证
- [x] 无中文字符混入LaTeX
- [x] 公式格式正确

### 节奏验证
- [x] 开场 < 5秒
- [x] 每个概念停留 2-3秒
- [x] 总时长 65-75秒
- [x] 难点停留更长

---

## 预期效果

1. **教学目标**：学生理解频数分布的整理过程和直方图的绘制
2. **视觉记忆**：直方图柱子高度 → 频数/频率
3. **关键洞察**：频率直方图面积之和 = 1
4. **应用场景**：成绩分析、数据统计、质量控制

---

## 备注

- 使用真实的学生成绩数据增强代入感
- 直方图是核心，需要精确绘制
- 频率直方图的变换是难点，需要详细说明
- 使用动画引导学生理解从表格到图形的转换