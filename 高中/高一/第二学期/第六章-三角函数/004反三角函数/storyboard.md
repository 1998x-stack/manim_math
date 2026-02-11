# 反三角函数教学动画 - 分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高一数学
- 主题: 反三角函数的定义、图像与性质

## 颜色配置
```python
COLOR_ARCSIN = "#e74c3c"      # 红色 - arcsin
COLOR_ARCCOS = "#3498db"      # 蓝色 - arccos  
COLOR_ARCTAN = "#2ecc71"      # 绿色 - arctan
COLOR_ORIGINAL = "#f39c12"    # 橙色 - 原函数
COLOR_REFLECTION = "#9b59b6"  # 紫色 - 对称线
COLOR_AUXILIARY = GRAY_B      # 辅助元素
COLOR_HIGHLIGHT = YELLOW      # 高亮
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标轴 | Axes(x_range=[-1.5,1.5], y_range=[-2,2]) | self.axes |
| y=x线 | Line([-1.5,-1.5], [1.5,1.5]) | self.reflection_line |
| arcsin曲线 | 反正弦函数图像 | self.arcsin_graph |
| arccos曲线 | 反余弦函数图像 | self.arccos_graph |
| arctan曲线 | 反正切函数图像 | self.arctan_graph |
| 定义域标记 | [-1,1]区间 | domain_markers |

---

## Scene 1: 开场钩子 (5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题："sin(30°) = 1/2，那反过来呢？"
3. 问号动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` |
| 0.3s | 问题文字书写 | `Write(hook_question)` |
| 1.5s | 问号缩放强调 | `question_mark.animate.scale(1.5)` |
| 2.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: author_info

---

## Scene 2: 反函数概念 (8秒)
**目的**: 回顾反函数基础

### 元素
1. 标题："反函数 Inverse Function"
2. y=sin(x) 图像（限制在[-π/2, π/2]）
3. y=x 对称线
4. 反射动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.8s | 绘制坐标轴 | `Create(axes)` |
| 1.5s | 绘制sin曲线 | `Create(sin_graph)` |
| 2.5s | y=x线闪现 | `Create(reflection_line)` |
| 3.5s | 反射动画 | `Rotate(sin_graph, about_point)` |
| 5.0s | 标注arcsin | `Write(arcsin_label)` |
| 6.5s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, sin_graph
- 保留: axes, reflection_line, arcsin_label

---

## Scene 3: arcsin 详解 (12秒)
**目的**: arcsin的定义域、值域、图像

### 元素
1. 标题："反正弦函数 y = arcsin x"
2. 定义：定义域[-1,1]，值域[-π/2,π/2]
3. arcsin曲线
4. 定义域区间标记
5. 值域区间标记
6. 关键点标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 定义文字书写 | `Write(definition)` |
| 1.5s | 绘制arcsin曲线 | `Create(arcsin_graph, run_time=2)` |
| 3.5s | 标记定义域 | `Create(domain_bracket)` |
| 4.5s | 标记值域 | `Create(range_bracket)` |
| 5.5s | 标注关键点(-1,-π/2) | `FadeIn(point_1)` |
| 6.5s | 标注关键点(0,0) | `FadeIn(point_2)` |
| 7.5s | 标注关键点(1,π/2) | `FadeIn(point_3)` |
| 8.5s | 公式：sin(arcsin x)=x | `Write(identity_1)` |
| 10.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, definition, domain_bracket, range_bracket, points, identity_1
- 保留: axes, arcsin_graph

---

## Scene 4: arccos 详解 (10秒)
**目的**: arccos的定义域、值域、图像

### 元素
1. 标题："反余弦函数 y = arccos x"
2. 定义：定义域[-1,1]，值域[0,π]
3. arccos曲线
4. 对比arcsin

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 淡出arcsin | `arcsin_graph.animate.set_opacity(0.3)` |
| 0.5s | 标题淡入 | `FadeIn(title)` |
| 1.0s | 定义文字 | `Write(definition)` |
| 2.0s | 绘制arccos曲线 | `Create(arccos_graph, run_time=2)` |
| 4.0s | 标注关键点 | `FadeIn(key_points)` |
| 5.5s | 公式：arcsin x + arccos x = π/2 | `Write(identity_2)` |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, definition, arcsin_graph, key_points, identity_2
- 保留: axes, arccos_graph

---

## Scene 5: arctan 详解 (10秒)
**目的**: arctan的定义域、值域、图像

### 元素
1. 标题："反正切函数 y = arctan x"
2. 定义：定义域R，值域(-π/2,π/2)
3. arctan曲线
4. 渐近线标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 淡出arccos | `FadeOut(arccos_graph)` |
| 0.5s | 调整坐标轴 | `Transform(axes, new_axes)` |
| 1.5s | 标题淡入 | `FadeIn(title)` |
| 2.0s | 定义文字 | `Write(definition)` |
| 3.0s | 绘制arctan曲线 | `Create(arctan_graph, run_time=2.5)` |
| 5.5s | 标记渐近线y=π/2 | `Create(asymptote_up)` |
| 6.5s | 标记渐近线y=-π/2 | `Create(asymptote_down)` |
| 7.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: title, definition, asymptote_up, asymptote_down
- 保留: axes, arctan_graph

---

## Scene 6: 三函数对比 (10秒)
**目的**: 并列显示三个反三角函数

### 元素
1. 标题："三大反三角函数对比"
2. 三个函数图像并列
3. 对比表格

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 图像缩小移位 | `Transform(axes, small_axes)` |
| 1.5s | 重绘三个函数 | `Create(all_three_graphs)` |
| 3.5s | 显示对比表格 | `FadeIn(comparison_table)` |
| 6.0s | 高亮定义域差异 | `Indicate(domain_column)` |
| 7.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: 所有图像和表格
- 保留: author_info

---

## Scene 7: 片尾总结 (10秒)
**目的**: 关键要点 + 关注引导

### 元素
1. 关键要点卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 要点卡片滑入 | `card.animate.shift(LEFT*5)` |
| 2.0s | 作者信息放大 | `author_info.animate.scale(2)` |
| 3.0s | 关注提示 | `FadeIn(follow_text)` |
| 5.0s | 三角函数图标旋转 | `Rotate(icons)` |
| 8.0s | 淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| reflection_line | Scene 2 | Scene 3 | y=x对称线 |
| arcsin_graph | Scene 3 | Scene 4 | arcsin图像 |
| arccos_graph | Scene 4 | Scene 5 | arccos图像 |
| arctan_graph | Scene 5 | Scene 6 | arctan图像 |

---

## 关键参数配置
```python
# 坐标轴配置（Scene 2-4: arcsin/arccos）
AXES_CONFIG_SMALL = {
    "x_range": [-1.5, 1.5, 0.5],
    "y_range": [-2, 2, 0.5],
    "x_length": 6,
    "y_length": 8,
    "axis_config": {"include_numbers": True, "font_size": 20}
}

# 坐标轴配置（Scene 5: arctan）
AXES_CONFIG_WIDE = {
    "x_range": [-5, 5, 1],
    "y_range": [-2, 2, 0.5],
    "x_length": 7,
    "y_length": 6
}

# 函数绘制精度
GRAPH_PRECISION = 0.01
```

---

## 验证清单
- [ ] 所有数学函数使用 numpy 精确计算
- [ ] 中文文字使用 Text() 类
- [ ] 数学公式使用 MathTex() 类
- [ ] 定义域、值域标记准确
- [ ] 所有元素在安全边界内 (x∈[-4,4], y∈[-7,7])
- [ ] 动画节奏流畅，难点停留2秒+
- [ ] 字体大小遵循规范
- [ ] 颜色区分明确