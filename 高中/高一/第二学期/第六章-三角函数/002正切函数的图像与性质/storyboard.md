# 正切函数的图像与性质 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 8 个
- 难度等级: 高一
- 知识点: 正切函数

## 颜色配置
```python
COLOR_TANGENT = "#e74c3c"        # 红色 - 正切函数
COLOR_SINE = "#3498db"           # 蓝色 - 正弦（对比用）
COLOR_COSINE = "#2ecc71"         # 绿色 - 余弦（对比用）
COLOR_ASYMPTOTE = "#f39c12"      # 橙色 - 渐近线
COLOR_HIGHLIGHT = YELLOW         # 高亮
COLOR_AUXILIARY = GRAY_B         # 辅助
COLOR_AXES = WHITE               # 坐标轴
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标轴 | Axes(x_range=[-3π/2, 3π/2], y_range=[-4, 4]) | self.axes |
| 正切曲线(主周期) | axes.plot(np.tan, x_range=(-π/2+ε, π/2-ε)) | self.tan_graph_main |
| 渐近线位置 | x = -π/2, π/2, 3π/2 等 | self.asymptote_x_values |
| 零点 | x = 0, ±π, ±2π | self.zero_points |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 吸引注意力 + 引入主题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 神秘的垂直线条预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "为什么这个函数有这么多垂直线？" |
| 1.5s | 神秘渐近线闪烁 | `Create(asymptote_lines)` |
| 3.5s | 淡出钩子 | `FadeOut(hook_text, asymptote_preview)` |

### 清理
- FadeOut: hook_text, asymptote_preview
- 保留: author_info

---

## Scene 2: 函数定义 (8-10秒)
**目的**: 引入 tan x = sin x / cos x

### 元素
1. 标题: "正切函数 Tangent Function"
2. 定义公式: tan x = sin x / cos x
3. 单位圆演示（可选）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 1.0s | 定义公式书写 | `Write(formula)` |
| 2.5s | 强调分母不能为0 | `Indicate(cos_part)` |
| 4.0s | 引出定义域限制 | `FadeIn(domain_text)` |
| 6.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: domain_text (临时说明)
- 保留: title, formula (移到顶部)

---

## Scene 3: 绘制主周期图像 (12-15秒)
**目的**: 绘制 (-π/2, π/2) 区间的正切曲线

### 元素
1. 坐标轴
2. 垂直渐近线 x = ±π/2
3. 正切曲线（主周期）
4. 关键点标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标轴 | `Create(axes)` |
| 1.5s | 标记 x 轴刻度 | `Write(x_labels)` |
| 2.5s | 渐近线出现 | `Create(asymptote_left, asymptote_right)` |
| 3.5s | 说明文字 | `Write(asymptote_explanation)` |
| 5.0s | 从原点开始绘制 | `Create(tan_graph_main)` |
| 8.0s | 标注关键点 | `FadeIn(zero_dot)` - (0, 0) |
| 9.0s | 标注 (π/4, 1) | `FadeIn(key_point_1)` |
| 10.0s | 标注 (-π/4, -1) | `FadeIn(key_point_2)` |

### 清理
- FadeOut: asymptote_explanation, key_point_labels
- 保留: axes, tan_graph_main, asymptote_lines

---

## Scene 4: 展示周期性 (10-12秒)
**目的**: 展示周期 T = π

### 元素
1. 左侧周期添加
2. 右侧周期添加
3. 周期标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 左侧渐近线出现 | `Create(asymptote_left_2)` |
| 1.0s | 左侧曲线绘制 | `Create(tan_graph_left)` |
| 2.5s | 右侧渐近线出现 | `Create(asymptote_right_2)` |
| 3.5s | 右侧曲线绘制 | `Create(tan_graph_right)` |
| 5.0s | 周期标注 | `Create(period_brace)` |
| 6.0s | 周期公式 | `Write(period_formula)` - "T = π" |
| 8.0s | 强调周期性 | `Indicate(period_brace)` |

### 清理
- FadeOut: period_brace, period_formula
- 保留: 所有曲线和渐近线

---

## Scene 5: 性质标注 - 定义域和值域 (8-10秒)
**目的**: 标注定义域、值域

### 元素
1. 定义域标注
2. 值域标注（强调无界）
3. 动画展示趋向无穷

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 定义域文字 | `FadeIn(domain_text)` |
| 1.5s | 高亮渐近线 | `asymptote_lines.animate.set_color(YELLOW)` |
| 3.0s | 值域文字 | `FadeIn(range_text)` - "值域: R" |
| 4.5s | 箭头指向无穷 | `Create(arrow_up, arrow_down)` |
| 6.0s | 强调无最大最小值 | `Write(no_bound_text)` |

### 清理
- FadeOut: property_texts, arrows
- 保留: axes, graphs, asymptotes

---

## Scene 6: 性质标注 - 奇偶性和单调性 (10-12秒)
**目的**: 展示奇函数性质和单调性

### 元素
1. 奇函数对称演示
2. 单调递增标注
3. 公式: tan(-x) = -tan x

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 奇函数公式 | `Write(odd_formula)` |
| 1.5s | 对称性演示 | `Create(symmetric_indicator)` |
| 3.5s | 高亮原点对称 | `Flash(origin)` |
| 5.0s | 单调性文字 | `FadeIn(monotone_text)` |
| 6.5s | 高亮一个周期 | `Indicate(tan_graph_main)` |
| 8.0s | 箭头表示递增 | `Create(increase_arrows)` |

### 清理
- FadeOut: property_texts, indicators
- 保留: axes, graphs

---

## Scene 7: 与正弦余弦对比 (12-15秒)
**目的**: 对比三个函数的异同

### 元素
1. 正弦、余弦曲线淡入（半透明）
2. 对比表格
3. 关键差异强调

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 图像缩小移到上方 | `graphs.animate.scale(0.6).to_edge(UP)` |
| 1.5s | 对比表格滑入 | `card.animate.shift(RIGHT)` |
| 3.0s | 正弦曲线叠加 | `Create(sin_graph_overlay)` |
| 4.5s | 余弦曲线叠加 | `Create(cos_graph_overlay)` |
| 6.0s | 差异1: 周期 | `Indicate(period_row)` |
| 7.5s | 差异2: 值域 | `Indicate(range_row)` |
| 9.0s | 差异3: 渐近线 | `Indicate(asymptote_row)` |

### 清理
- FadeOut: comparison_table, sin_graph, cos_graph
- 保留: tan_graph

---

## Scene 8: 总结与片尾 (10-12秒)
**目的**: 总结要点 + 关注提示

### 元素
1. 核心性质卡片
2. 应用提示
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(all_objects)` |
| 1.0s | 总结标题 | `Write(summary_title)` |
| 2.0s | 性质卡片滑入 | 依次显示5个要点 |
| 6.0s | 应用场景 | `FadeIn(application_text)` - "斜率、倾斜角" |
| 8.0s | 关注提示放大 | `Write(follow_text)` |
| 10.0s | 装饰动画 | 渐近线装饰效果 |
| 12.0s | 全部淡出 | `FadeOut(VGroup(*))` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| axes | Scene 3 | Scene 7 | 坐标轴 |
| tan_graph_main | Scene 3 | Scene 7 | 主周期曲线 |
| tan_graph_left | Scene 4 | Scene 7 | 左侧周期 |
| tan_graph_right | Scene 4 | Scene 7 | 右侧周期 |
| asymptote_lines | Scene 3 | Scene 7 | 渐近线 |
| property_texts | Scene 5/6 | Scene 5/6 | 临时性质标注 |
| comparison_table | Scene 7 | Scene 7 | 对比表格 |

---

## 技术要点

### 1. 渐近线处理
正切函数在 x = π/2 + kπ 处有垂直渐近线，需要：
- 分段绘制曲线，避开奇点
- 使用 DashedLine 绘制渐近线
- 使用 epsilon (ε = 0.01) 避开渐近线

```python
epsilon = 0.01
tan_graph = axes.plot(
    np.tan,
    x_range=(-PI/2 + epsilon, PI/2 - epsilon),
    discontinuities=[],  # 不自动处理不连续点
    use_smoothing=False
)
```

### 2. 分段绘制
每个周期单独绘制：
```python
periods = [
    (-3*PI/2 + epsilon, -PI/2 - epsilon),
    (-PI/2 + epsilon, PI/2 - epsilon),
    (PI/2 + epsilon, 3*PI/2 - epsilon)
]
```

### 3. 关键角度标注
- x = 0: tan(0) = 0
- x = π/4: tan(π/4) = 1
- x = -π/4: tan(-π/4) = -1
- x = π/3: tan(π/3) = √3

### 4. 颜色使用
- 正切函数: 红色 (#e74c3c)
- 渐近线: 橙色 (#f39c12)
- 正弦对比: 蓝色 (#3498db)
- 余弦对比: 绿色 (#2ecc71)

### 5. 动画节奏
- 渐近线出现: 0.8s
- 曲线绘制: 2.0s (强调从0开始)
- 性质标注: 1.0-1.5s
- 理解停顿: 2.0s (关键概念后)

---

## 特别注意事项

### ⚠️ 渐近线的精确定位
```python
# 渐近线 x 坐标（精确计算）
asymptote_x = [
    -3*PI/2,  # -270°
    -PI/2,    # -90°
    PI/2,     # 90°
    3*PI/2    # 270°
]
```

### ⚠️ 避免数值溢出
```python
# 限制 y 轴范围，避免数值过大
y_range = [-5, 5]  # 足够展示特性，但不会溢出
```

### ⚠️ 平滑度控制
```python
# 正切函数在渐近线附近变化剧烈
# 需要增加采样点
num_samples = 200  # 而不是默认的 100
```

---

## 预期效果

学生通过这个动画应该理解：
1. ✅ 正切函数的定义（sin/cos）
2. ✅ 为什么有垂直渐近线（cos = 0）
3. ✅ 周期为 π 而不是 2π
4. ✅ 值域是全体实数（无界）
5. ✅ 奇函数性质
6. ✅ 单调递增特性
7. ✅ 与正弦、余弦的区别