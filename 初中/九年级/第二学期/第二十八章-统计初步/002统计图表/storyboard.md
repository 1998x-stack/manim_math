# 统计图表教学动画 - 分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中
- 知识点: 条形图、折线图、扇形图、频数分布直方图

## 颜色配置
```python
COLOR_BAR_CHART = "#3498db"       # 蓝色 - 条形图
COLOR_LINE_CHART = "#2ecc71"      # 绿色 - 折线图
COLOR_PIE_CHART = "#e74c3c"       # 红色 - 扇形图
COLOR_HISTOGRAM = "#f39c12"       # 橙色 - 直方图
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 数据定义清单
| 元素 | 数据源 | 存储变量 |
|------|--------|---------|
| 条形图数据 | [4, 7, 5, 8, 6] (周一到周五销量) | self.bar_data |
| 折线图数据 | [20, 25, 22, 28, 26, 30, 35] (温度趋势) | self.line_data |
| 扇形图数据 | [30%, 25%, 20%, 15%, 10%] (爱好分布) | self.pie_data |
| 直方图数据 | [5, 8, 12, 10, 6, 3] (成绩分布) | self.hist_data |

## 公式验证清单
| 公式 | 用途 | 验证方法 |
|------|------|---------|
| 扇形圆心角 = 比例 × 360° | 计算扇形角度 | 验证角度总和 = 360° |
| 条形高度比例 | 数据可视化 | 验证最大值映射正确 |
| 直方图面积 | 频数表示 | 验证矩形高度正确 |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "数据如何可视化?"
3. 四种图表缩略图

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字放大 | `Write(hook_text)` | 0.8s |
| 1.1s | 四个图表图标闪现 | `FadeIn(icons, lag_ratio=0.2)` | 1.0s |
| 2.1s | 图标排列 | `icons.arrange(RIGHT)` | 0.5s |
| 2.6s | 等待 | `Wait(0.8)` | 0.8s |

### 清理
- FadeOut: hook_text, icons
- 保留: author_info

---

## Scene 2: 条形图 (5-15秒)
**目的**: 展示条形图特点 - 直观比较数据大小

### 元素
1. 标题 "条形图 Bar Chart"
2. 坐标轴 (x轴: 周一~周五, y轴: 销量 0-10)
3. 5个条形 (动态生长)
4. 说明文字 "直观比较各类数据的大小"

### 数据计算
```python
bar_labels = ["周一", "周二", "周三", "周四", "周五"]
bar_values = [4, 7, 5, 8, 6]
bar_max = 10
bar_positions = [-2, -1, 0, 1, 2]  # x轴位置
bar_heights = [v/bar_max * 3 for v in bar_values]  # 归一化到3个单位高度
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 5.0s | 标题写入 | `Write(title)` | 0.8s |
| 5.8s | 坐标轴绘制 | `Create(axes)` | 1.0s |
| 6.8s | 条形依次生长 | `GrowFromEdge(bars, DOWN, lag_ratio=0.3)` | 1.5s |
| 8.3s | 高亮最高条形 | `bars[3].animate.set_color(YELLOW)` | 0.5s |
| 8.8s | 说明文字淡入 | `FadeIn(explanation)` | 0.5s |
| 9.3s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, axes, bars, explanation
- 保留: author_info

---

## Scene 3: 折线图 (15-25秒)
**目的**: 展示折线图特点 - 反映数据变化趋势

### 元素
1. 标题 "折线图 Line Chart"
2. 坐标轴 (x轴: 周一~周日, y轴: 温度 0-40°C)
3. 折线 (带点标记)
4. 说明文字 "反映数据变化趋势"
5. 上升趋势箭头

### 数据计算
```python
line_labels = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
line_values = [20, 25, 22, 28, 26, 30, 35]  # 温度数据
line_points = [(i-3, (v-20)/20*3, 0) for i, v in enumerate(line_values)]
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 15.0s | 标题写入 | `Write(title)` | 0.8s |
| 15.8s | 坐标轴绘制 | `Create(axes)` | 1.0s |
| 16.8s | 点依次出现 | `FadeIn(dots, lag_ratio=0.2)` | 1.0s |
| 17.8s | 折线绘制 | `Create(line)` | 1.5s |
| 19.3s | 上升箭头 | `GrowArrow(trend_arrow)` | 0.5s |
| 19.8s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 20.3s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, axes, line, dots, trend_arrow, explanation
- 保留: author_info

---

## Scene 4: 扇形图 (25-40秒)
**目的**: 展示扇形图特点 - 表示各部分在总体中的比例

### 元素
1. 标题 "扇形图 Pie Chart"
2. 完整圆形 (半径 2)
3. 5个扇形区域 (不同颜色)
4. 百分比标签
5. 图例
6. 公式 "扇形圆心角 = 比例 × 360°"

### 数据计算
```python
pie_labels = ["运动", "阅读", "游戏", "音乐", "其他"]
pie_percentages = [30, 25, 20, 15, 10]  # 百分比
pie_angles = [p/100 * 360 for p in pie_percentages]  # 转换为角度
pie_colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]

# 累积角度计算（用于定位）
cumulative_angles = [0]
for angle in pie_angles:
    cumulative_angles.append(cumulative_angles[-1] + angle)
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 25.0s | 标题写入 | `Write(title)` | 0.8s |
| 25.8s | 完整圆形 | `Create(circle)` | 1.0s |
| 26.8s | 扇形依次出现 | `FadeIn(sectors, lag_ratio=0.3)` | 2.0s |
| 28.8s | 百分比标签 | `FadeIn(percentages, lag_ratio=0.2)` | 1.0s |
| 29.8s | 高亮最大扇形 | `sectors[0].animate.scale(1.1)` | 0.5s |
| 30.3s | 公式展示 | `Write(formula)` | 1.0s |
| 31.3s | 示例计算 | `Write(example)` | 0.8s |
| 32.1s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 32.6s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, circle, sectors, percentages, formula, example, explanation
- 保留: author_info

---

## Scene 5: 频数分布直方图 (40-52秒)
**目的**: 展示直方图特点 - 表示数据的分布情况

### 元素
1. 标题 "频数分布直方图 Histogram"
2. 坐标轴 (x轴: 分数段, y轴: 频数)
3. 连续矩形条 (无间隙)
4. 说明文字 "表示数据的分布情况"

### 数据计算
```python
hist_ranges = ["0-59", "60-69", "70-79", "80-89", "90-99", "100"]
hist_frequencies = [5, 8, 12, 10, 6, 3]  # 频数
hist_width = 0.8  # 每个矩形宽度
hist_max_freq = 15
hist_heights = [f/hist_max_freq * 3 for f in hist_frequencies]
```

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 40.0s | 标题写入 | `Write(title)` | 0.8s |
| 40.8s | 坐标轴绘制 | `Create(axes)` | 1.0s |
| 41.8s | 矩形依次生长 | `GrowFromEdge(rects, DOWN, lag_ratio=0.2)` | 1.5s |
| 43.3s | 高亮众数区间 | `rects[2].animate.set_color(YELLOW)` | 0.5s |
| 43.8s | 标注 "众数区间" | `Write(mode_label)` | 0.5s |
| 44.3s | 说明文字 | `FadeIn(explanation)` | 0.5s |
| 44.8s | 等待 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: title, axes, rects, mode_label, explanation
- 保留: author_info

---

## Scene 6: 对比总结 (52-65秒)
**目的**: 四种图表对比，总结特点

### 元素
1. 标题 "选择合适的统计图表"
2. 四个小型图表并排
3. 特点标签

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 52.0s | 标题写入 | `Write(title)` | 0.8s |
| 52.8s | 四图依次出现 | `FadeIn(charts, lag_ratio=0.3)` | 1.5s |
| 54.3s | 特点标签 | `FadeIn(labels, lag_ratio=0.2)` | 1.2s |
| 55.5s | 场景应用示例 | `Write(examples)` | 1.0s |
| 56.5s | 等待 | `Wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, charts, labels, examples
- 保留: author_info

---

## Scene 7: 片尾 (65-75秒)
**目的**: 品牌强化，引导关注

### 元素
1. 作者信息放大
2. "关注我，学更多数学技巧!"
3. 图表图标装饰

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 65.0s | 作者信息放大 | `author.animate.scale(1.5)` | 0.8s |
| 65.8s | 关注文字 | `Write(follow_text)` | 0.8s |
| 66.6s | 图标装饰旋转 | `Rotate(icons)` | 1.5s |
| 68.1s | 等待 | `Wait(2.0)` | 2.0s |
| 70.1s | 全部淡出 | `FadeOut(VGroup(*all))` | 1.0s |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| bar_chart | Scene 2 | Scene 2 | 条形图 |
| line_chart | Scene 3 | Scene 3 | 折线图 |
| pie_chart | Scene 4 | Scene 4 | 扇形图 |
| histogram | Scene 5 | Scene 5 | 直方图 |
| comparison | Scene 6 | Scene 6 | 对比总结 |

---

## 数据验证检查项
- [ ] 扇形图角度总和 = 360°
- [ ] 条形图高度比例正确
- [ ] 折线图点坐标准确
- [ ] 直方图矩形连续无间隙
- [ ] 所有文字在安全区域内 (x∈[-4,4], y∈[-7,7])
- [ ] 颜色对比度足够
- [ ] 动画节奏流畅

---

## 特殊注意事项
1. **中文文字**: 使用 `Text(..., font="Noto Sans CJK SC")` 而非 `MathTex`
2. **扇形绘制**: 使用 `Sector(angle=..., start_angle=...)`，注意累积角度计算
3. **直方图**: 矩形之间无间隙，使用 `Rectangle` 紧密排列
4. **颜色一致性**: 每种图表使用固定主题色
5. **动画节奏**: 关键步骤留足理解时间 (1.5-2秒)