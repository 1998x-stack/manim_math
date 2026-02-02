# 一次函数的性质 - 动画分镜脚本

<!-- /root/code/sss/media/videos/linear_function_properties/1920p60/LinearFunctionProperties.mp4 -->

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 目标年级: 八年级第二学期

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - k>0的线
COLOR_SECONDARY = "#e74c3c"    # 红色 - k<0的线
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BG = "#1a1a2e"
COLOR_POSITIVE_ZONE = "#2ecc71"  # 绿色 - 增函数标记
COLOR_NEGATIVE_ZONE = "#f39c12"  # 橙色 - 减函数标记
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系中心 | UP * 1.5 | self.axes_center |
| k>0直线点1 | axes.c2p(-2, -1) | self.point_k_pos_1 |
| k>0直线点2 | axes.c2p(2, 3) | self.point_k_pos_2 |
| k<0直线点1 | axes.c2p(-2, 2) | self.point_k_neg_1 |
| k<0直线点2 | axes.c2p(2, -2) | self.point_k_neg_2 |
| 单调性箭头起点 | 根据函数值动态计算 | - |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 吸引注意力 + 引出主题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "一次函数的性质你真的掌握了吗?"
3. 简单的y=kx+b公式闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 公式y=kx+b淡入并缩放 | `FadeIn(formula, scale=1.2)` |
| 1.8s | 公式闪烁 | `Flash(formula, color=YELLOW)` |
| 2.5s | 等待 | `self.wait(0.8)` |
| 3.3s | 清理 | `FadeOut(hook_text, formula)` |

### 清理
- FadeOut: hook_text, formula
- 保留: author_info

---

## Scene 2: 建立坐标系 (5秒)
**目的**: 创建可视化环境

### 元素
1. 平面直角坐标系 (x: -3到3, y: -3到3)
2. 坐标轴标签
3. 网格线(可选，淡化)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系创建 | `Create(axes, run_time=1.2)` |
| 1.2s | 坐标轴标签淡入 | `FadeIn(x_label, y_label)` |
| 2.0s | 标题"一次函数 y=kx+b" | `Write(title)` |
| 3.0s | 等待 | `self.wait(1.0)` |

### 清理
- 保留: axes, 标签
- FadeOut: title (移到顶部缩小)

---

## Scene 3: k>0的性质 (12秒)
**目的**: 展示k>0时y随x增大而增大

### 元素
1. 蓝色直线 y = 2x + 1 (k=2, b=1)
2. 动态点在直线上移动
3. x, y值实时显示
4. 箭头标注"增大"方向
5. 文字说明"k>0: y随x增大而增大"

### 几何计算
```python
# k=2, b=1的直线
def func_k_positive(x):
    return 2*x + 1

# 移动点的x坐标范围: -2 到 2
x_start = -2
x_end = 2
point_start = axes.c2p(x_start, func_k_positive(x_start))
point_end = axes.c2p(x_end, func_k_positive(x_end))
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式 y=2x+1 显示 | `Write(formula_k_pos)` |
| 0.8s | 直线绘制 | `Create(line_k_pos, run_time=1.5)` |
| 2.3s | 动点从左到右移动 | `MoveAlongPath(dot, line, run_time=3)` |
| 2.3s | x,y数值实时更新 | `ValueTracker + updater` |
| 5.3s | 上升箭头淡入 | `GrowArrow(arrow_up)` |
| 6.0s | 说明文字"y随x增大而增大" | `FadeIn(explanation, shift=UP*0.3)` |
| 8.0s | 等待强化记忆 | `self.wait(2.0)` |

### 清理
- 保留: line_k_pos (变淡)
- FadeOut: dot, arrow, explanation, formula

---

## Scene 4: k<0的性质 (12秒)
**目的**: 展示k<0时y随x增大而减小

### 元素
1. 红色直线 y = -1.5x + 2 (k=-1.5, b=2)
2. 动态点在直线上移动
3. x, y值实时显示
4. 箭头标注"减小"方向
5. 文字说明"k<0: y随x增大而减小"

### 几何计算
```python
# k=-1.5, b=2的直线
def func_k_negative(x):
    return -1.5*x + 2

# 移动点的x坐标范围: -2 到 2
point_start = axes.c2p(-2, func_k_negative(-2))
point_end = axes.c2p(2, func_k_negative(2))
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 公式 y=-1.5x+2 显示 | `Write(formula_k_neg)` |
| 0.8s | 直线绘制 | `Create(line_k_neg, run_time=1.5)` |
| 2.3s | 动点从左到右移动 | `MoveAlongPath(dot, line, run_time=3)` |
| 2.3s | x,y数值实时更新 | `ValueTracker + updater` |
| 5.3s | 下降箭头淡入 | `GrowArrow(arrow_down)` |
| 6.0s | 说明文字"y随x增大而减小" | `FadeIn(explanation, shift=UP*0.3)` |
| 8.0s | 等待强化记忆 | `self.wait(2.0)` |

### 清理
- 保留: line_k_neg (变淡)
- FadeOut: dot, arrow, explanation, formula

---

## Scene 5: k和b的符号与象限 (15秒)
**目的**: 展示四种组合经过的象限

### 元素
1. 四条直线同时展示
2. 每条线不同颜色 + 标签
3. 象限标注
4. 表格总结

### 直线定义
```python
# Case 1: k>0, b>0 → 过一、二、三象限
line_1 = axes.plot(lambda x: x + 1.5, color="#3498db")  # y=x+1.5
# Case 2: k>0, b<0 → 过一、三、四象限
line_2 = axes.plot(lambda x: x - 1, color="#9b59b6")    # y=x-1
# Case 3: k<0, b>0 → 过一、二、四象限
line_3 = axes.plot(lambda x: -x + 1.5, color="#e74c3c") # y=-x+1.5
# Case 4: k<0, b<0 → 过二、三、四象限
line_4 = axes.plot(lambda x: -x - 1, color="#f39c12")   # y=-x-1
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"k和b的符号与象限" | `Write(title)` |
| 1.0s | 四条线依次绘制 | `Create(lines, lag_ratio=0.3)` |
| 4.0s | 标注每条线的k、b符号 | `FadeIn(labels)` |
| 5.5s | 高亮第一条线+象限闪烁 | `Indicate(line_1), Flash(quadrants)` |
| 7.0s | 高亮第二条线+象限闪烁 | 同上 |
| 8.5s | 高亮第三条线+象限闪烁 | 同上 |
| 10.0s | 高亮第四条线+象限闪烁 | 同上 |
| 11.5s | 汇总表格淡入 | `FadeIn(summary_table)` |
| 13.0s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: 全部 (准备总结)

---

## Scene 6: 性质对比总结 (10秒)
**目的**: 强化核心概念

### 元素
1. 左右分屏对比
2. 左侧: k>0 (蓝色背景)
3. 右侧: k<0 (红色背景)
4. 核心公式和箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 分屏背景淡入 | `FadeIn(left_bg, right_bg)` |
| 0.5s | k>0标题和公式 | `Write(left_title, left_formula)` |
| 1.2s | k<0标题和公式 | `Write(right_title, right_formula)` |
| 2.0s | 向上箭头(左) | `GrowArrow(arrow_up_left)` |
| 2.5s | 向下箭头(右) | `GrowArrow(arrow_down_right)` |
| 3.0s | 性质文字 | `FadeIn(property_texts)` |
| 5.0s | 等待 | `self.wait(3.0)` |

### 清理
- FadeOut: 全部

---

## Scene 7: 片尾 (5秒)
**目的**: 作者信息 + 关注提示

### 元素
1. 作者名放大
2. 关注提示
3. 小装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大居中 | `Transform(author, author_large)` |
| 0.8s | 关注提示淡入 | `FadeIn(follow_text, scale=1.1)` |
| 1.5s | 装饰图标旋转 | `Rotate(decorations, angle=PI)` |
| 3.5s | 等待 | `self.wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留在顶部 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| line_k_pos | Scene 3 | Scene 6 | k>0的线，变淡保留 |
| line_k_neg | Scene 4 | Scene 6 | k<0的线，变淡保留 |
| moving_dot | Scene 3/4 | Scene 3/4 | 临时动点 |
| summary_table | Scene 5 | Scene 5 | 象限表格 |

---

## 动画节奏设计

### 总体节奏
- 开场: 快速 (3秒)
- 核心概念1 (k>0): 慢速详细 (12秒)
- 核心概念2 (k<0): 慢速详细 (12秒)
- 象限关系: 中速 (15秒)
- 对比总结: 慢速强化 (10秒)
- 片尾: 快速 (5秒)

### 关键停顿点
1. Scene 3结束: 2秒 (让学生理解k>0性质)
2. Scene 4结束: 2秒 (让学生理解k<0性质)
3. Scene 5表格显示后: 2秒 (消化象限关系)
4. Scene 6对比图: 3秒 (强化对比记忆)

---

## 技术要点备忘

### 坐标系配置
```python
axes = Axes(
    x_range=[-3, 3, 1],
    y_range=[-3, 3, 1],
    x_length=6,
    y_length=6,
    axis_config={
        "include_numbers": True,
        "font_size": 20,
    }
).move_to(UP * 1.5)
```

### 动点更新器
```python
x_tracker = ValueTracker(-2)
dot = always_redraw(
    lambda: Dot(
        axes.c2p(x_tracker.get_value(), 
                 func(x_tracker.get_value())),
        color=YELLOW,
        radius=0.1
    )
)
```

### 数值标签
```python
x_label = always_redraw(
    lambda: MathTex(
        f"x = {x_tracker.get_value():.1f}"
    ).next_to(dot, UP, buff=0.3)
)
```

### 字体使用
- 中文: `Text("...", font="Noto Sans CJK SC")`
- 数学公式: `MathTex(r"y = kx + b")`
- 不混用!