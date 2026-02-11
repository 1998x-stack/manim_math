# 三角函数 y=Asin(ωx+φ)+B 图像与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高一
- 核心内容: 参数意义 + 图像变换

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主函数
COLOR_SECONDARY = "#e74c3c"      # 红色 - 对比/强调
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_AMPLITUDE = "#2ecc71"      # 绿色 - 振幅
COLOR_PERIOD = "#f39c12"         # 橙色 - 周期
COLOR_PHASE = "#9b59b6"          # 紫色 - 相位
```

## 几何/数值预计算清单
| 元素 | 计算公式/值 | 存储变量 |
|------|------------|---------|
| 坐标系范围 | x: [-π, 3π], y: [-3, 3] | axes |
| 基础函数 | y = sin(x) | base_func |
| 振幅示例 | A = 2 | amplitude_value |
| 周期示例 | ω = 2, T = π | omega_value |
| 相位示例 | φ = π/4 | phase_value |
| 平移示例 | B = 1 | shift_value |
| 最终函数 | y = 2sin(2x + π/4) + 1 | final_func |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意 + 引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题："三角函数的秘密武器"
3. 函数公式闪现

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 顶部小字 |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | "掌握这个公式，解题快人一步！" |
| 1.5s | 公式淡入 | `FadeIn(formula)` | y=Asin(ωx+φ)+B |
| 2.5s | 公式闪烁 | `Flash(formula)` | 吸引注意 |
| 3.5s | 等待 | `Wait(1.0)` | - |

### 位置信息
- author_info: UP * 7
- hook_text: UP * 6
- formula: UP * 4.5 (大字号 36)

### 清理
- FadeOut: hook_text
- 保留: author_info, formula (缩小移至 UP*6)

---

## Scene 2: 基础函数 y=sin(x) (5-12秒)
**目的**: 建立基准，展示标准正弦函数

### 元素
1. 坐标系 (x: [-π, 3π], y: [-3, 3])
2. 基础正弦曲线 y=sin(x)
3. 关键点标注 (最大值、最小值、零点)
4. 振幅、周期标注

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 5.0s | 创建坐标系 | `Create(axes)` | 淡入 |
| 6.0s | 绘制 sin(x) | `Create(graph_sin)` | 蓝色曲线 |
| 7.0s | 标注关键点 | `FadeIn(dots_group)` | 最大值(π/2,1)、最小值(3π/2,-1)、零点 |
| 8.0s | 振幅标注 | `Create(amplitude_brace)` | 双向箭头 y=-1到1 |
| 9.0s | 周期标注 | `Create(period_brace)` | 水平括号 0到2π |
| 10.0s | 说明文字 | `FadeIn(explanation)` | "标准正弦函数：振幅1，周期2π" |
| 11.5s | 等待 | `Wait(1.0)` | 理解停顿 |

### 位置信息
- axes 中心: DOWN * 1
- explanation: DOWN * 5.5

### 清理
- FadeOut: amplitude_brace, period_brace, explanation, dots_group
- 保留: axes, graph_sin

---

## Scene 3: 参数 A - 振幅变化 (12-20秒)
**目的**: 展示振幅如何控制"高度"

### 元素
1. 保留的 y=sin(x)
2. 新曲线 y=2sin(x) (红色)
3. 振幅对比线
4. 动态数值显示

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 12.0s | 标题淡入 | `FadeIn(title_A)` | "参数A：振幅" |
| 12.5s | 公式变化 | `TransformMatchingTex` | y=sin(x) → y=2sin(x) |
| 13.0s | 绘制新曲线 | `Create(graph_2sin)` | 红色，A=2 |
| 14.0s | 振幅线对比 | `Create(amp_lines)` | 虚线标注 y=±1 和 y=±2 |
| 15.0s | 说明文字 | `FadeIn(explanation_A)` | "A=2：图像纵向拉伸2倍" |
| 16.0s | 高亮最值 | `Flash(max_dots)` | 最大值从1变为2 |
| 17.5s | 等待 | `Wait(1.0)` | - |

### 位置信息
- title_A: UP * 6
- explanation_A: DOWN * 5.5

### 清理
- FadeOut: title_A, amp_lines, explanation_A
- Transform: graph_sin 保持，graph_2sin 变为新 base

---

## Scene 4: 参数 ω - 周期变化 (20-30秒)
**目的**: 展示 ω 如何控制"密度"

### 元素
1. 当前基准曲线
2. 新曲线 y=2sin(2x) (橙色)
3. 周期对比标注
4. 公式 T=2π/ω

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 20.0s | 标题淡入 | `FadeIn(title_omega)` | "参数ω：周期" |
| 20.5s | 公式变化 | `TransformMatchingTex` | y=2sin(x) → y=2sin(2x) |
| 21.5s | 绘制新曲线 | `Create(graph_omega)` | 橙色，ω=2 |
| 22.5s | 周期公式 | `FadeIn(period_formula)` | T=2π/ω = π |
| 23.5s | 周期标注 | `Create(period_braces)` | 旧周期2π vs 新周期π |
| 25.0s | 说明文字 | `FadeIn(explanation_omega)` | "ω=2：周期缩短一半，图像横向压缩" |
| 27.0s | 动画演示 | `graph.animate.stretch` | 横向压缩动画 |
| 28.5s | 等待 | `Wait(1.0)` | - |

### 位置信息
- title_omega: UP * 6
- period_formula: UP * 5
- explanation_omega: DOWN * 5.5

### 清理
- FadeOut: title_omega, period_braces, explanation_omega, period_formula
- 更新 base: graph_omega

---

## Scene 5: 参数 φ - 相位平移 (30-40秒)
**目的**: 展示相位如何"左右平移"

### 元素
1. 当前基准曲线
2. 新曲线 y=2sin(2x + π/4) (紫色)
3. 水平位移箭头
4. 关键：φ>0 左移，φ<0 右移

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 30.0s | 标题淡入 | `FadeIn(title_phi)` | "参数φ：初相位" |
| 30.5s | 公式变化 | `TransformMatchingTex` | y=2sin(2x) → y=2sin(2x+π/4) |
| 31.5s | 平移公式 | `FadeIn(shift_formula)` | "平移量 = -φ/ω = -π/8" |
| 32.5s | 绘制新曲线 | `Create(graph_phi)` | 紫色 |
| 33.5s | 水平箭头 | `Create(shift_arrow)` | 向左箭头 |
| 34.5s | 说明文字 | `FadeIn(explanation_phi)` | "φ>0：图像向左平移" |
| 36.0s | 动画演示 | `graph.animate.shift(LEFT)` | 左移动画 |
| 38.0s | 等待 | `Wait(1.0)` | - |

### 位置信息
- title_phi: UP * 6
- shift_formula: UP * 5
- explanation_phi: DOWN * 5.5
- shift_arrow: axes 上方

### 清理
- FadeOut: title_phi, shift_arrow, explanation_phi, shift_formula
- 更新 base: graph_phi

---

## Scene 6: 参数 B - 纵向平移 (40-48秒)
**目的**: 展示 B 如何上下平移整体

### 元素
1. 当前基准曲线
2. 最终曲线 y=2sin(2x+π/4)+1 (金色)
3. 垂直平移箭头
4. 中轴线标注

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 40.0s | 标题淡入 | `FadeIn(title_B)` | "参数B：纵向平移" |
| 40.5s | 公式变化 | `TransformMatchingTex` | +B |
| 41.5s | 绘制新曲线 | `Create(graph_final)` | 金色，B=1 |
| 42.5s | 中轴线 | `Create(midline)` | y=1 虚线 |
| 43.5s | 垂直箭头 | `Create(vertical_arrow)` | 向上箭头 |
| 44.5s | 说明文字 | `FadeIn(explanation_B)` | "B=1：图像整体上移1单位" |
| 46.0s | 最值标注 | `FadeIn(max_min_labels)` | 最大值3，最小值-1 |
| 47.5s | 等待 | `Wait(1.0)` | - |

### 位置信息
- title_B: UP * 6
- explanation_B: DOWN * 5.5
- midline: y=1 水平虚线

### 清理
- FadeOut: title_B, vertical_arrow, explanation_B, midline
- 保留: graph_final, max_min_labels

---

## Scene 7: 性质总结 + 片尾 (48-65秒)
**目的**: 总结性质 + 关注引导

### 元素
1. 最终函数图像
2. 性质卡片（振幅、周期、最值）
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 48.0s | 清屏 | `FadeOut(axes, graph_*)` | 只保留公式 |
| 48.5s | 公式居中 | `formula.animate.move_to(UP*3)` | 放大 |
| 49.5s | 性质卡片1 | `FadeIn(card_amplitude)` | "振幅A=2" |
| 50.5s | 性质卡片2 | `FadeIn(card_period)` | "周期T=π" |
| 51.5s | 性质卡片3 | `FadeIn(card_range)` | "值域[-1, 3]" |
| 53.0s | 总结文字 | `FadeIn(summary)` | "四个参数，控制三角函数全貌" |
| 55.0s | 作者信息放大 | `author_info.animate.scale(2)` | - |
| 56.0s | 关注提示 | `FadeIn(follow_text)` | "关注我，学更多数学技巧" |
| 58.0s | 装饰动画 | `Create(decorations)` | 波浪线装饰 |
| 60.0s | 等待 | `Wait(2.0)` | - |
| 62.0s | 全部淡出 | `FadeOut(*)` | 结束 |

### 位置信息
- formula: UP * 3 (放大到 font_size=40)
- card_amplitude: UP * 1
- card_period: ORIGIN
- card_range: DOWN * 1
- summary: DOWN * 3
- follow_text: DOWN * 5

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| formula | Scene 1 | Scene 7 | 变换多次 |
| axes | Scene 2 | Scene 7 | 坐标系 |
| graph_sin | Scene 2 | Scene 3 | 基础正弦 |
| graph_2sin | Scene 3 | Scene 4 | A=2 |
| graph_omega | Scene 4 | Scene 5 | ω=2 |
| graph_phi | Scene 5 | Scene 6 | 加相位 |
| graph_final | Scene 6 | Scene 7 | 最终函数 |
| dots (各种标注点) | Scene 2-6 | 各场景内 | 临时标注 |

---

## 关键技术要点

### 1. 坐标系设置
```python
axes = Axes(
    x_range=[-PI, 3*PI, PI/2],
    y_range=[-3, 3, 1],
    x_length=8,
    y_length=10,
    axis_config={"include_numbers": True, "font_size": 20},
    tips=False
).scale(0.7).shift(DOWN*1)
```

### 2. 函数图像
```python
graph = axes.plot(
    lambda x: 2*np.sin(2*x + PI/4) + 1,
    x_range=[-PI, 3*PI],
    color=COLOR_PRIMARY
)
```

### 3. 公式变换
```python
# 使用 TransformMatchingTex 保持连贯
formula_1 = MathTex(r"y = \sin(x)")
formula_2 = MathTex(r"y = 2\sin(x)")
self.play(TransformMatchingTex(formula_1, formula_2))
```

### 4. 参数标注
```python
# 振幅 - 双向箭头
amplitude_line = DoubleArrow(
    start=axes.c2p(0, -2),
    end=axes.c2p(0, 2),
    color=COLOR_AMPLITUDE,
    buff=0
)

# 周期 - 括号标注
period_brace = Brace(
    Line(axes.c2p(0, 0), axes.c2p(PI, 0)),
    direction=DOWN,
    color=COLOR_PERIOD
)
```

### 5. 动画节奏
- 快速过渡: 0.5s (坐标系、简单元素)
- 标准动画: 1.0s (曲线绘制、公式变换)
- 理解停顿: 1.5-2.0s (关键概念后)

---

## 边界检查
- 坐标系 axes: 缩放0.7后移至 DOWN*1，确保在 y∈[-3, 5] 范围内
- 公式: 最高 UP*6，最低 DOWN*6，安全
- 所有文字: font_size ≤ 36，避免溢出

---

## LaTeX 检查清单
- ✅ 使用 `\sin` 而非 sin
- ✅ 使用 `\pi` 显示 π
- ✅ 中文用 Text()，数学用 MathTex()
- ✅ 度数用 `^\circ`
- ✅ 分数用 `\frac{}{}`

---

## 预期输出
- 时长: 60-65秒
- 文件大小: ~10-15MB (1080p)
- 渲染时间: ~3-5分钟 (取决于机器)