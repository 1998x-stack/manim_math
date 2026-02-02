# 一次函数与方程、不等式的关系 - 动画分镜脚本

## 元信息
- 目标时长: 70-85秒
- 场景数量: 8个
- 难度等级: 中等
- 目标年级: 八年级第二学期

## 颜色配置
```python
COLOR_FUNCTION = "#3498db"      # 蓝色 - 函数图像
COLOR_X_AXIS = WHITE            # x轴
COLOR_ABOVE = "#2ecc71"         # 绿色 - x轴上方区域
COLOR_BELOW = "#e74c3c"         # 红色 - x轴下方区域
COLOR_INTERSECTION = YELLOW     # 黄色 - 交点
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BG = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系中心 | UP * 2.0 | self.axes_center |
| 函数y=2x-3 | lambda x: 2*x - 3 | self.func |
| x轴交点 | 求解2x-3=0, x=1.5 | self.x_intercept |
| 交点坐标 | axes.c2p(1.5, 0) | self.intersection_point |
| 上方区域 | x > 1.5 | - |
| 下方区域 | x < 1.5 | - |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力 + 引出三者关系

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "函数、方程、不等式，它们有什么关系?"
3. 三个关键词闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 三个关键词依次闪现 | `FadeIn(keywords, lag_ratio=0.3)` |
| 2.5s | 等待 | `self.wait(0.8)` |
| 3.3s | 清理 | `FadeOut(hook_text, keywords)` |

### 清理
- FadeOut: hook_text, keywords
- 保留: author_info

---

## Scene 2: 建立坐标系和函数图像 (6秒)
**目的**: 展示一次函数y=2x-3

### 元素
1. 平面直角坐标系 (x: -2到4, y: -5到5)
2. 坐标轴标签
3. 函数y=2x-3的图像（蓝色）
4. 函数公式标签

### 几何计算
```python
# 函数定义
def func(x):
    return 2*x - 3

# x轴交点: 2x - 3 = 0 => x = 1.5
x_intercept = 1.5
intersection_point = axes.c2p(1.5, 0)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系创建 | `Create(axes, run_time=1.0)` |
| 1.0s | 坐标轴标签淡入 | `FadeIn(x_label, y_label)` |
| 1.5s | 函数公式显示 | `Write(formula)` |
| 2.3s | 函数图像绘制 | `Create(graph, run_time=1.5)` |
| 3.8s | 等待 | `self.wait(1.0)` |

### 清理
- 保留: axes, graph, 标签

---

## Scene 3: 方程kx+b=0的解 (12秒)
**目的**: 展示方程的解就是图像与x轴交点的横坐标

### 元素
1. 方程 2x-3=0 显示
2. x轴高亮
3. 交点标记（黄色大点）
4. 交点坐标标注
5. 解的答案 x=1.5
6. 连接线和说明文字

### 几何计算
```python
# 交点位置
x_intercept = 1.5  # 精确计算：2x - 3 = 0
intersection_point = axes.c2p(x_intercept, 0)

# 垂直虚线从交点到x轴刻度
vertical_line_start = intersection_point
vertical_line_end = intersection_point + DOWN * 0.3
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 方程2x-3=0淡入 | `FadeIn(equation)` |
| 0.8s | x轴高亮闪烁 | `Flash(x_axis)` |
| 1.5s | 交点标记放大出现 | `GrowFromCenter(intersection_dot)` |
| 2.5s | 坐标标注淡入 | `FadeIn(coord_label)` |
| 3.5s | 垂直虚线绘制 | `Create(vertical_line)` |
| 4.5s | 解x=1.5显示 | `Write(solution_text)` |
| 5.5s | 说明文字"交点横坐标" | `FadeIn(explanation)` |
| 8.0s | 等待理解 | `self.wait(2.0)` |

### 清理
- 保留: graph, intersection_dot (变小)
- FadeOut: equation, solution_text, explanation, vertical_line

---

## Scene 4: 不等式kx+b>0的解集 (15秒)
**目的**: 展示kx+b>0对应图像在x轴上方

### 元素
1. 不等式 2x-3>0 显示
2. x轴上方区域高亮（绿色半透明）
3. 图像在x轴上方部分加粗高亮
4. x>1.5 数轴标注
5. 区间箭头
6. 说明文字

### 几何计算
```python
# 上方区域定义
# x ∈ (1.5, 4]（坐标系右边界）
region_above = Polygon(
    axes.c2p(1.5, 0),
    axes.c2p(4, 0),
    axes.c2p(4, 5),
    axes.c2p(1.5, func(1.5)),
    fill_color=COLOR_ABOVE,
    fill_opacity=0.2
)

# 图像高亮部分: x从1.5到4
graph_above = axes.plot(
    func,
    x_range=[1.5, 4],
    color=COLOR_ABOVE,
    stroke_width=6
)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 不等式2x-3>0淡入 | `FadeIn(inequality_pos)` |
| 0.8s | 上方区域淡入 | `FadeIn(region_above)` |
| 1.8s | 图像上方部分高亮 | `Create(graph_above)` |
| 3.0s | x>1.5标注显示 | `Write(solution_inequality)` |
| 4.0s | 数轴箭头绘制 | `GrowArrow(arrow_right)` |
| 5.0s | 说明"图像在x轴上方" | `FadeIn(explanation)` |
| 7.0s | 强调闪烁 | `Indicate(region_above)` |
| 9.0s | 等待 | `self.wait(3.0)` |

### 清理
- FadeOut: inequality_pos, region_above, graph_above, explanation

---

## Scene 5: 不等式kx+b<0的解集 (15秒)
**目的**: 展示kx+b<0对应图像在x轴下方

### 元素
1. 不等式 2x-3<0 显示
2. x轴下方区域高亮（红色半透明）
3. 图像在x轴下方部分加粗高亮
4. x<1.5 数轴标注
5. 区间箭头
6. 说明文字

### 几何计算
```python
# 下方区域定义
# x ∈ [-2, 1.5)（坐标系左边界到交点）
region_below = Polygon(
    axes.c2p(-2, 0),
    axes.c2p(1.5, 0),
    axes.c2p(1.5, func(1.5)),
    axes.c2p(-2, func(-2)),
    fill_color=COLOR_BELOW,
    fill_opacity=0.2
)

# 图像高亮部分: x从-2到1.5
graph_below = axes.plot(
    func,
    x_range=[-2, 1.5],
    color=COLOR_BELOW,
    stroke_width=6
)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 不等式2x-3<0淡入 | `FadeIn(inequality_neg)` |
| 0.8s | 下方区域淡入 | `FadeIn(region_below)` |
| 1.8s | 图像下方部分高亮 | `Create(graph_below)` |
| 3.0s | x<1.5标注显示 | `Write(solution_inequality)` |
| 4.0s | 数轴箭头绘制 | `GrowArrow(arrow_left)` |
| 5.0s | 说明"图像在x轴下方" | `FadeIn(explanation)` |
| 7.0s | 强调闪烁 | `Indicate(region_below)` |
| 9.0s | 等待 | `self.wait(3.0)` |

### 清理
- FadeOut: inequality_neg, region_below, graph_below, explanation

---

## Scene 6: 三者关系总结 (12秒)
**目的**: 数形结合，总结三者关系

### 元素
1. 三栏对比表格
2. 左栏：方程 kx+b=0
3. 中栏：不等式 kx+b>0
4. 右栏：不等式 kx+b<0
5. 对应的几何意义
6. 核心提示"数形结合"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 表格框架淡入 | `FadeIn(table_frame)` |
| 1.0s | 方程列填充 | `Write(equation_column)` |
| 2.5s | 不等式>0列填充 | `Write(inequality_pos_column)` |
| 4.0s | 不等式<0列填充 | `Write(inequality_neg_column)` |
| 5.5s | 几何意义标注 | `FadeIn(geometry_meanings)` |
| 7.0s | "数形结合"高亮 | `FadeIn(core_concept, scale=1.2)` |
| 9.0s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: 全部表格内容

---

## Scene 7: 实例演示 (10秒)
**目的**: 动态演示如何用图像解题

### 元素
1. 问题：求2x-3≥0的解集
2. 图像重新显示
3. 交点和上方区域高亮
4. 解的区间动画标注
5. 答案：x≥1.5

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 问题显示 | `Write(problem)` |
| 1.0s | 图像和坐标系回放 | `FadeIn(graph)` |
| 2.0s | 交点闪烁 | `Flash(intersection)` |
| 3.0s | 上方区域高亮 | `FadeIn(region_above)` |
| 4.5s | 区间标注动画 | `Create(interval_notation)` |
| 6.0s | 答案显示 | `Write(answer)` |
| 8.0s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: 全部

---

## Scene 8: 片尾 (5秒)
**目的**: 作者信息 + 关注提示

### 元素
1. 作者名放大
2. 关注提示 "用图像解方程和不等式!"
3. 装饰图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大居中 | `Transform(author, author_large)` |
| 0.8s | 关注提示淡入 | `FadeIn(follow_text, scale=1.1)` |
| 1.5s | 装饰图标动画 | `FadeIn(icons)` |
| 3.5s | 等待 | `self.wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保留在顶部 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| graph | Scene 2 | Scene 7 | 函数图像 |
| intersection_dot | Scene 3 | Scene 7 | 交点标记 |
| region_above | Scene 4 | Scene 4 | 上方区域 |
| region_below | Scene 5 | Scene 5 | 下方区域 |
| summary_table | Scene 6 | Scene 6 | 对比表格 |

---

## 动画节奏设计

### 总体节奏
- 开场: 快速 (4秒)
- 建立图像: 中速 (6秒)
- 方程关系: 慢速详细 (12秒)
- 不等式>0: 慢速详细 (15秒)
- 不等式<0: 慢速详细 (15秒)
- 总结表格: 中速 (12秒)
- 实例演示: 中速 (10秒)
- 片尾: 快速 (5秒)

### 关键停顿点
1. Scene 3结束: 2秒 (让学生理解交点=方程的解)
2. Scene 4结束: 3秒 (理解上方区域=不等式>0的解)
3. Scene 5结束: 3秒 (理解下方区域=不等式<0的解)
4. Scene 6表格显示后: 2秒 (消化三者关系)

---

## 技术要点备忘

### 坐标系配置
```python
axes = Axes(
    x_range=[-2, 4, 1],
    y_range=[-5, 5, 1],
    x_length=7,
    y_length=8,
    axis_config={
        "include_numbers": True,
        "font_size": 20,
    }
).move_to(UP * 2.0)
```

### 函数定义
```python
def func(x):
    return 2 * x - 3

# x轴交点精确计算
x_intercept = 1.5  # 2x - 3 = 0 => x = 1.5
```

### 区域填充
```python
# 上方区域
region_above = axes.get_area(
    graph,
    x_range=[x_intercept, 4],
    color=COLOR_ABOVE,
    opacity=0.3
)

# 下方区域（需要自定义Polygon）
region_below = Polygon(
    axes.c2p(-2, 0),
    axes.c2p(x_intercept, 0),
    axes.c2p(x_intercept, func(x_intercept)),
    axes.c2p(-2, func(-2)),
    fill_color=COLOR_BELOW,
    fill_opacity=0.2,
    stroke_width=0
)
```

### 字体使用
- 中文: `Text("...", font="Noto Sans CJK SC")`
- 数学公式: `MathTex(r"2x - 3 = 0")`
- 不混用!

### 验证要点
- 交点横坐标 x=1.5 必须精确
- 区域边界必须在交点处
- 所有元素在安全区域内