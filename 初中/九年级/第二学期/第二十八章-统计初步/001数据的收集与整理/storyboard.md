# 数据的收集与整理 - 动画分镜脚本

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 9 个
- 难度等级: 基础（九年级统计入门）
- 竖屏格式: 1080×1920 (9:16)
- 特色: 数据可视化、表格动画、柱状图

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主色调
COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调色
COLOR_SUCCESS = "#2ecc71"        # 绿色 - 成功/正确
COLOR_WARNING = "#f39c12"        # 橙色 - 警告/注意
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_TABLE = WHITE              # 白色 - 表格
COLOR_BAR_1 = "#3498db"          # 蓝色 - 柱状图1
COLOR_BAR_2 = "#9b59b6"          # 紫色 - 柱状图2
COLOR_BAR_3 = "#1abc9c"          # 青色 - 柱状图3
```

## 数据示例设置

### 示例数据：学生身高（单位：cm）
```python
# 原始数据（20个学生）
raw_data = [
    158, 162, 165, 168, 172, 155, 160, 163, 167, 170,
    159, 161, 164, 169, 173, 156, 162, 166, 171, 157
]

# 分组数据
groups = [
    "155-159",
    "160-164", 
    "165-169",
    "170-174"
]

# 频数
frequencies = [4, 6, 5, 5]

# 频率
rates = [0.20, 0.30, 0.25, 0.25]
```

---

## Scene 1: 开场钩子 (0-4s)

**目的**: 用生活场景引入统计概念

### 元素
1. 作者标识（顶部）
2. 钩子问题
3. 数据示意图

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 0.3s |
| 0.3s | 钩子文字 | `Write(hook_text)` | 0.8s |
| 1.1s | 数据图标 | `FadeIn(data_icons)` | 1.0s |
| 2.1s | 问题文字 | `FadeIn(question)` | 0.5s |
| 2.6s | 等待 | `Wait()` | 1.0s |

### 具体内容
- 钩子: "班级要统计身高"
- 问题: "这么多数据怎么整理？"
- 数据图标: 一堆数字（混乱）

### 清理
- FadeOut: hook_text, question, data_icons
- 保留: author_info

---

## Scene 2: 统计步骤介绍 (4-10s)

**目的**: 介绍统计的四个基本步骤

### 元素
1. 四个步骤卡片
2. 步骤图标

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 步骤1卡片 | `FadeIn(step1, shift=LEFT)` | 0.5s |
| 0.9s | 步骤2卡片 | `FadeIn(step2, shift=LEFT)` | 0.5s |
| 1.4s | 步骤3卡片 | `FadeIn(step3, shift=LEFT)` | 0.5s |
| 1.9s | 步骤4卡片 | `FadeIn(step4, shift=LEFT)` | 0.5s |
| 2.4s | 箭头连接 | `Create(arrows)` | 0.6s |
| 3.0s | 高亮重点 | `Indicate(step1, step2)` | 0.8s |
| 3.8s | 等待 | `Wait()` | 1.5s |

### 步骤内容
1. 收集数据
2. 整理数据 ⭐
3. 描述数据
4. 分析数据

### 清理
- FadeOut: 所有步骤卡片和箭头
- 保留: title（缩小移到顶部）

---

## Scene 3: 数据收集方式 (10-18s)

**目的**: 对比普查和抽样调查

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 普查卡片 | `FadeIn(census_card)` | 0.6s |
| 1.0s | 普查说明 | `Write(census_desc)` | 0.8s |
| 1.8s | 图示（全部） | `Create(census_visual)` | 0.8s |
| 2.6s | 抽样卡片 | `FadeIn(sample_card)` | 0.6s |
| 3.2s | 抽样说明 | `Write(sample_desc)` | 0.8s |
| 4.0s | 图示（部分） | `Create(sample_visual)` | 0.8s |
| 4.8s | 对比表 | `Create(comparison_table)` | 1.0s |
| 5.8s | 等待 | `Wait()` | 1.5s |

### 对比内容
| 项目 | 普查 | 抽样调查 |
|------|------|---------|
| 范围 | 全部 | 部分 |
| 准确性 | 高 | 较高 |
| 成本 | 高 | 低 |
| 适用 | 小范围 | 大范围 |

### 视觉设计
```
普查：   ●●●●●●●●●●  （全部实心圆）
抽样：   ●○○●○○●○○●  （部分实心圆）
```

### 清理
- FadeOut: 所有卡片、图示、对比表

---

## Scene 4: 原始数据展示 (18-24s)

**目的**: 展示未整理的原始数据

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 数据说明 | `FadeIn(data_desc)` | 0.5s |
| 0.9s | 数据逐个出现 | `Write(data_numbers)` | 2.0s |
| 2.9s | 混乱强调 | `Indicate(data_numbers)` | 0.6s |
| 3.5s | 问题文字 | `FadeIn(problem_text)` | 0.5s |
| 4.0s | 等待 | `Wait()` | 1.0s |

### 数据展示
```
学生身高（cm）：
158, 162, 165, 168, 172, 155, 160, 163, 167, 170,
159, 161, 164, 169, 173, 156, 162, 166, 171, 157
```

### 问题
"数据太乱了，怎么办？"

### 清理
- FadeOut: data_numbers, problem_text
- 保留: title, data_desc

---

## Scene 5: 数据分组 (24-32s)

**目的**: 展示如何将数据分组

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 分组说明 | `FadeIn(group_desc)` | 0.5s |
| 0.9s | 创建分组框 | `Create(group_boxes)` | 0.8s |
| 1.7s | 数据归类动画 | `data.animate.move_to(group)` | 2.5s |
| 4.2s | 统计频数 | `Write(frequencies)` | 1.0s |
| 5.2s | 高亮结果 | `Indicate(frequencies)` | 0.6s |
| 5.8s | 等待 | `Wait()` | 1.5s |

### 分组过程
```
原始数据 → 分组
155-159: 155, 156, 157, 158, 159  (频数: 4)
160-164: 160, 161, 162, 162, 163, 164  (频数: 6)
165-169: 165, 166, 167, 168, 169  (频数: 5)
170-174: 170, 171, 172, 173  (频数: 5)
```

### 清理
- FadeOut: group_boxes, data
- 保留: frequencies（缩小）

---

## Scene 6: 频数分布表 (32-42s)

**目的**: 制作频数分布表

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 表格框架 | `Create(table_frame)` | 0.8s |
| 1.2s | 表头 | `Write(table_headers)` | 0.6s |
| 1.8s | 第1行数据 | `Write(row1)` | 0.5s |
| 2.3s | 第2行数据 | `Write(row2)` | 0.5s |
| 2.8s | 第3行数据 | `Write(row3)` | 0.5s |
| 3.3s | 第4行数据 | `Write(row4)` | 0.5s |
| 3.8s | 合计行 | `Write(total_row)` | 0.6s |
| 4.4s | 表格高亮 | `Indicate(table)` | 0.8s |
| 5.2s | 等待 | `Wait()` | 2.0s |

### 频数分布表
| 身高分组(cm) | 频数 |
|-------------|------|
| 155-159 | 4 |
| 160-164 | 6 |
| 165-169 | 5 |
| 170-174 | 5 |
| **合计** | **20** |

### 清理
- 表格缩小移到左侧

---

## Scene 7: 频率概念 (42-52s)

**目的**: 引入频率的概念和计算

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 频率定义 | `FadeIn(definition)` | 0.6s |
| 1.0s | 频率公式 | `Write(formula)` | 0.8s |
| 1.8s | 示例计算1 | `Write(calc1)` | 1.0s |
| 2.8s | 示例计算2 | `Write(calc2)` | 1.0s |
| 3.8s | 添加频率列 | `Create(rate_column)` | 1.0s |
| 4.8s | 频率和性质 | `FadeIn(sum_property)` | 0.8s |
| 5.6s | 验证 | `Indicate(sum_check)` | 0.6s |
| 6.2s | 等待 | `Wait()` | 2.0s |

### 频率公式
```
频率 = 频数 / 总数
```

### 计算示例
```
155-159组: 频率 = 4/20 = 0.20
160-164组: 频率 = 6/20 = 0.30
```

### 频率性质
```
各组频率之和 = 1
验证: 0.20 + 0.30 + 0.25 + 0.25 = 1.00 ✓
```

### 完整表格
| 身高分组(cm) | 频数 | 频率 |
|-------------|------|------|
| 155-159 | 4 | 0.20 |
| 160-164 | 6 | 0.30 |
| 165-169 | 5 | 0.25 |
| 170-174 | 5 | 0.25 |
| **合计** | **20** | **1.00** |

### 清理
- 表格移到右上角

---

## Scene 8: 柱状图展示 (52-65s)

**目的**: 用柱状图可视化频数分布

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title)` | 0.4s |
| 0.4s | 坐标轴 | `Create(axes)` | 0.8s |
| 1.2s | 柱子1 | `GrowFromEdge(bar1, DOWN)` | 0.6s |
| 1.8s | 柱子2 | `GrowFromEdge(bar2, DOWN)` | 0.6s |
| 2.4s | 柱子3 | `GrowFromEdge(bar3, DOWN)` | 0.6s |
| 3.0s | 柱子4 | `GrowFromEdge(bar4, DOWN)` | 0.6s |
| 3.6s | 数值标注 | `Write(bar_labels)` | 0.8s |
| 4.4s | 横坐标标签 | `Write(x_labels)` | 0.6s |
| 5.0s | 纵坐标标签 | `Write(y_label)` | 0.4s |
| 5.4s | 图表标题 | `Write(chart_title)` | 0.5s |
| 5.9s | 最高柱高亮 | `Indicate(bar2)` | 0.6s |
| 6.5s | 等待 | `Wait()` | 2.0s |

### 柱状图设计
```
频数
 6 ┤     ██
 5 ┤ ██  ██  ██  ██
 4 ┤ ██  ██  ██  ██
 3 ┤ ██  ██  ██  ██
 2 ┤ ██  ██  ██  ██
 1 ┤ ██  ██  ██  ██
 0 └─────────────────→
   155 160 165 170
   -159 -164 -169 -174
```

### 清理
- FadeOut: 柱状图
- 保留: 表格

---

## Scene 9: 结尾总结 (65-75s)

**目的**: 总结并引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 总结标题 | `FadeIn(summary_title)` | 0.6s |
| 0.6s | 关键点1 | `FadeIn(point1)` | 0.5s |
| 1.1s | 关键点2 | `FadeIn(point2)` | 0.5s |
| 1.6s | 关键点3 | `FadeIn(point3)` | 0.5s |
| 2.1s | 公式框 | `Create(formula_box)` | 0.8s |
| 2.9s | 作者放大 | `author.animate.scale(2)` | 0.6s |
| 3.5s | 关注提示 | `Write(follow_text)` | 0.8s |
| 4.3s | 装饰动画 | `Create(decorations)` | 0.8s |
| 5.1s | 等待 | `Wait()` | 1.5s |

### 总结要点
1. 数据分组，计算频数
2. 频率 = 频数/总数
3. 频率和 = 1

### 公式汇总
```
频数 = 该组数据出现的次数
频率 = 频数/数据总数
各组频率之和 = 1
```

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 全程保留在顶部 |
| frequency_table | Scene 6 | Scene 9 | 频数分布表 |
| formula_box | Scene 7 | Scene 9 | 公式框 |

---

## 关键注意事项

### 表格设计约束
```python
# Manim Table 使用
table = Table(
    [
        ["155-159", "4", "0.20"],
        ["160-164", "6", "0.30"],
        ["165-169", "5", "0.25"],
        ["170-174", "5", "0.25"],
    ],
    row_labels=[Text("身高分组"), Text("频数"), Text("频率")],
    include_outer_lines=True
)

# 位置约束
table.scale(0.6).move_to(UP * 2)  # 确保在可见范围内
```

### 柱状图约束
```python
# BarChart 使用
chart = BarChart(
    values=[4, 6, 5, 5],
    bar_names=["155-159", "160-164", "165-169", "170-174"],
    y_range=[0, 8, 2],
    y_length=5,
    x_length=8,
    x_axis_config={"font_size": 20}
)

# 位置约束
chart.move_to(ORIGIN)  # 居中显示
```

### LaTeX 安全性
- ❌ 禁止：MathTex(r"\text{频数}")
- ✅ 正确：Text("频数", font="Noto Sans CJK SC")
- ✅ 公式：MathTex(r"\text{Frequency} = \frac{f}{n}")

### 边界安全
- 表格区域：y ∈ [1, 5]
- 柱状图区域：y ∈ [-2, 4]
- 文字说明：y ∈ [-5, -3]

---

## 动画时长预算

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1 | 4s | 4s |
| Scene 2 | 6s | 10s |
| Scene 3 | 8s | 18s |
| Scene 4 | 6s | 24s |
| Scene 5 | 8s | 32s |
| Scene 6 | 10s | 42s |
| Scene 7 | 10s | 52s |
| Scene 8 | 13s | 65s |
| Scene 9 | 10s | 75s |

**总时长**: 约75秒 ✓（符合短视频标准）

---

## 技术实现要点

### 1. 数据归类动画
```python
def animate_data_grouping(data_mobjects, group_boxes):
    """数据归类到各组的动画"""
    animations = []
    for data, group in zip(data_mobjects, group_boxes):
        animations.append(
            data.animate.move_to(group.get_center())
        )
    return AnimationGroup(*animations, lag_ratio=0.1)
```

### 2. 表格逐行创建
```python
def create_table_rows(table, lag_ratio=0.3):
    """逐行创建表格的动画"""
    animations = []
    for row in table.get_rows():
        animations.append(FadeIn(row, shift=UP*0.2))
    return Succession(*animations, lag_ratio=lag_ratio)
```

### 3. 柱状图生长动画
```python
def grow_bar_chart(bars):
    """柱状图从底部生长的动画"""
    return AnimationGroup(
        *[GrowFromEdge(bar, DOWN) for bar in bars],
        lag_ratio=0.2
    )
```

### 4. 频率计算动画
```python
def animate_rate_calculation(frequency, total):
    """频率计算过程的动画"""
    # 显示计算过程
    calc = MathTex(
        r"\text{Rate} = ", 
        f"{frequency}", 
        r"\div", 
        f"{total}", 
        r"=", 
        f"{frequency/total:.2f}"
    )
    return Write(calc)
```

---

## 数据验证要点

### 频数验证
```python
# 验证频数和等于总数
assert sum(frequencies) == total_count

# 验证每组频数 >= 0
assert all(f >= 0 for f in frequencies)
```

### 频率验证
```python
# 验证频率和为1
rates_sum = sum(rates)
assert abs(rates_sum - 1.0) < 1e-6

# 验证每个频率在[0,1]之间
assert all(0 <= r <= 1 for r in rates)
```

### 边界验证
```python
# 表格位置
assert -4 <= table.get_center()[0] <= 4
assert -3 <= table.get_center()[1] <= 5

# 柱状图位置
assert -4 <= chart.get_center()[0] <= 4
assert -5 <= chart.get_center()[1] <= 4
```