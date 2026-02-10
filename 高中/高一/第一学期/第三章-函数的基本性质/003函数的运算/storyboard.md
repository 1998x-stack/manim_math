# 函数的运算 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - f(x)
COLOR_SECONDARY = "#e74c3c"    # 红色 - g(x)
COLOR_RESULT = "#2ecc71"       # 绿色 - 运算结果
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
BACKGROUND = "#1a1a2e"
```

## 数学元素预定义

### 函数定义
```python
f(x) = x²
g(x) = 2x
定义域：f: ℝ, g: ℝ
```

### 运算结果
```python
(f+g)(x) = x² + 2x
(f-g)(x) = x² - 2x
(f·g)(x) = 2x³
(f/g)(x) = x²/(2x) = x/2, x≠0
(f∘g)(x) = f(g(x)) = (2x)² = 4x²
```

### 坐标系配置
```python
x_range = [-3, 3, 1]
y_range = [-2, 10, 2]
坐标轴位置: 中央偏上 (y=0)
```

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出核心问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 两个简单函数图像浮现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入顶部 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "函数也能做运算?" |
| 1.5s | f(x)图像从左侧滑入 | `Create(f_graph).shift(LEFT*2)` |
| 2.5s | g(x)图像从右侧滑入 | `Create(g_graph).shift(RIGHT*2)` |
| 3.5s | 问号闪烁 | `Flash(question_mark)` |
| 4.5s | 等待 | `Wait(0.5)` |

### 视觉布局
```
y = +7: 作者信息
y = +6: "函数也能做运算?"
y = [0, 5]: f(x)和g(x)的图像（左右分开）
y = -2: 问号
```

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, 坐标轴（待建）

---

## Scene 2: 加法运算 (f+g)(x) (5-15秒)
**目的**: 展示函数加法的图像叠加原理

### 元素
1. 标题: "(f+g)(x) = f(x) + g(x)"
2. 坐标系
3. f(x)蓝色曲线
4. g(x)红色曲线
5. (f+g)(x)绿色曲线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题写入 | `Write(title)` |
| 5.8s | 创建坐标系 | `Create(axes)` |
| 6.5s | f(x)图像生长 | `Create(f_graph)` |
| 7.5s | 标签"f(x)=x²"淡入 | `FadeIn(f_label)` |
| 8.0s | g(x)图像生长 | `Create(g_graph)` |
| 9.0s | 标签"g(x)=2x"淡入 | `FadeIn(g_label)` |
| 9.5s | 等待理解 | `Wait(1.0)` |
| 10.5s | 选取x=2点，标记 | `FadeIn(dot_x2)` |
| 11.0s | 虚线连接f(2)和g(2) | `Create(vertical_lines)` |
| 12.0s | 箭头向上"相加" | `GrowArrow(add_arrow)` |
| 12.5s | 结果点闪烁 | `Flash(result_dot)` |
| 13.0s | (f+g)(x)图像生长 | `Create(sum_graph)` |
| 14.0s | 说明文字 | `FadeIn(explain)` "逐点相加" |
| 15.0s | 等待 | `Wait(1.0)` |

### 视觉布局
```
y = +7: 作者信息
y = +5.5: 标题 "(f+g)(x) = f(x) + g(x)"
y = [0, 5]: 坐标系和图像
y = -5: 说明文字
```

### 清理
- FadeOut: title, dots, arrows, explain
- 保留: axes, graphs (淡化)

---

## Scene 3: 减法运算 (f-g)(x) (15-22秒)
**目的**: 快速展示减法（与加法类似）

### 元素
1. 标题: "(f-g)(x) = f(x) - g(x)"
2. 使用相同坐标系
3. (f-g)(x)紫色曲线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 15.0s | 标题写入 | `Write(title)` |
| 16.0s | 前两个图恢复高亮 | `graphs.animate.set_opacity(1)` |
| 17.0s | 选取x=1点 | `FadeIn(dot_x1)` |
| 17.5s | 向下箭头"相减" | `GrowArrow(subtract_arrow)` |
| 18.5s | (f-g)(x)图像生长 | `Create(diff_graph)` |
| 19.5s | 说明"逐点相减" | `FadeIn(explain)` |
| 21.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, dots, arrows, explain, diff_graph
- 保留: axes, f_graph, g_graph (淡化)

---

## Scene 4: 乘法运算 (f·g)(x) (22-30秒)
**目的**: 展示函数乘法

### 元素
1. 标题: "(f·g)(x) = f(x) · g(x)"
2. (f·g)(x)橙色曲线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 22.0s | 标题写入 | `Write(title)` |
| 23.0s | 选取x=1.5点 | `FadeIn(dot)` |
| 23.5s | f(1.5)×g(1.5)动画 | `Transform(numbers)` |
| 24.5s | 结果闪烁 | `Flash(result)` |
| 25.0s | (f·g)(x)图像生长 | `Create(product_graph)` |
| 26.5s | 说明"逐点相乘" | `FadeIn(explain)` |
| 28.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, dots, explain, product_graph
- 保留: axes

---

## Scene 5: 除法运算 (f/g)(x) (30-40秒)
**目的**: 强调定义域限制（g(x)≠0）

### 元素
1. 标题: "(f/g)(x) = f(x)/g(x), g(x)≠0"
2. (f/g)(x)品红色曲线
3. ⚠️ 警告符号（x=0处）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 30.0s | 标题写入 | `Write(title)` |
| 31.0s | 恢复f, g图像 | `graphs.animate.set_opacity(1)` |
| 32.0s | 标记x=0点 | `FadeIn(warning_dot)` |
| 32.5s | 警告符号⚠️闪烁 | `Flash(warning)` |
| 33.5s | 说明"g(x)=0时无定义" | `FadeIn(explain)` |
| 35.0s | (f/g)(x)图像生长（跳过x=0） | `Create(quotient_graph)` |
| 36.5s | 虚线标记间断点 | `Create(dashed_line)` |
| 38.0s | 定义域说明 | `FadeIn(domain_text)` "定义域: x≠0" |
| 39.5s | 等待强调 | `Wait(1.5)` |

### 清理
- FadeOut: title, warning, explain, quotient_graph, domain_text
- 保留: axes

---

## Scene 6: 复合函数 (f∘g)(x) (40-55秒)
**目的**: 展示复合函数的"先后顺序"

### 元素
1. 标题: "复合函数: f(g(x))"
2. 流程图: x → g(x) → f(结果)
3. (f∘g)(x)金色曲线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 40.0s | 标题写入 | `Write(title)` |
| 41.0s | 清空坐标系 | `FadeOut(all_graphs)` |
| 42.0s | 流程图淡入 | `FadeIn(flowchart)` |
| 43.0s | x=1流动动画 | `MoveAlongPath(dot, arrow1)` |
| 44.0s | "g(1)=2"显示 | `FadeIn(step1)` |
| 45.0s | 继续流动 | `MoveAlongPath(dot, arrow2)` |
| 46.0s | "f(2)=4"显示 | `FadeIn(step2)` |
| 47.0s | 结果高亮 | `Flash(result)` |
| 48.0s | 流程图淡出 | `FadeOut(flowchart)` |
| 49.0s | 重建坐标系 | `Create(axes)` |
| 50.0s | f(x)淡入 | `FadeIn(f_graph)` |
| 51.0s | g(x)淡入 | `FadeIn(g_graph)` |
| 52.0s | f∘g(x)生长 | `Create(composite_graph)` |
| 53.5s | 说明"先g再f" | `FadeIn(explain)` |
| 55.0s | 等待 | `Wait(1.0)` |

### 视觉布局
```
流程图阶段:
y = +3: x → [g] → g(x) → [f] → f(g(x))

图像阶段:
y = [0, 5]: 坐标系
```

### 清理
- FadeOut: title, explain, all graphs, axes

---

## Scene 7: 总结与片尾 (55-75秒)
**目的**: 复习要点，引导关注

### 元素
1. 五种运算公式卡片
2. 定义域提示框
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 55.0s | "函数的五种运算"标题 | `Write(title)` |
| 56.0s | 卡片1滑入 | `card1.animate.shift(RIGHT*4)` |
| 57.0s | 卡片2滑入 | `card2.animate.shift(RIGHT*4)` |
| 58.0s | 卡片3滑入 | `card3.animate.shift(RIGHT*4)` |
| 59.0s | 卡片4滑入 | `card4.animate.shift(RIGHT*4)` |
| 60.0s | 卡片5滑入 | `card5.animate.shift(RIGHT*4)` |
| 61.0s | 定义域提示框 | `FadeIn(domain_box)` "注意定义域!" |
| 62.5s | 作者信息放大 | `Transform(author)` |
| 64.0s | 关注提示 | `FadeIn(follow)` "关注我，学更多函数技巧!" |
| 65.0s | 装饰动画 | `Rotate(icons)` |
| 68.0s | 等待 | `Wait(2.0)` |
| 70.0s | 全部淡出 | `FadeOut(VGroup(*all))` |

### 卡片内容
```
卡片1: (f+g)(x) = f(x) + g(x)
卡片2: (f-g)(x) = f(x) - g(x)
卡片3: (f·g)(x) = f(x) · g(x)
卡片4: (f/g)(x) = f(x)/g(x), g(x)≠0
卡片5: f(g(x)) - 先算g，再算f
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终显示 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| f_graph | Scene 2 | Scene 6 | f(x)=x² |
| g_graph | Scene 2 | Scene 6 | g(x)=2x |
| sum_graph | Scene 2 | Scene 2 | (f+g)(x) |
| diff_graph | Scene 3 | Scene 3 | (f-g)(x) |
| product_graph | Scene 4 | Scene 4 | (f·g)(x) |
| quotient_graph | Scene 5 | Scene 5 | (f/g)(x) |
| composite_graph | Scene 6 | Scene 6 | f∘g(x) |
| flowchart | Scene 6 | Scene 6 | 复合函数流程 |
| summary_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 关键时间节点检查

- [ ] 0-5s: 钩子足够吸引人
- [ ] 每个运算有独立场景（清晰分离）
- [ ] 除法场景强调g(x)≠0（停留1.5秒以上）
- [ ] 复合函数用流程图（最难理解的部分）
- [ ] 总时长控制在60-75秒
- [ ] 片尾关注提示清晰

---

## 技术注意事项

### 坐标系边界
- 主内容区：y ∈ [-1, 6]（给图像留足空间）
- 标题区：y ∈ [5.5, 6.5]
- 说明文字区：y ∈ [-5, -4]
- 作者信息：y = +7（固定）

### 字体大小
- 标题: 32
- 公式: 28
- 说明: 22
- 作者: 20

### 函数图像精度
- 使用 `axes.plot()` 时 `x_range` 需密集采样
- 除法函数在x=0附近跳过 `discontinuities=[0]`

### 颜色一致性
- f(x): 蓝色 `#3498db`
- g(x): 红色 `#e74c3c`
- 结果: 根据运算类型变化（绿/紫/橙/品红/金）