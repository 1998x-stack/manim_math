# 对数函数教学动画 - 分镜脚本

## 元信息
- **标题**: 对数函数的图像与性质
- **目标时长**: 60-75 秒
- **场景数量**: 7 个
- **难度等级**: 高一
- **知识点**: 对数函数 y = log_a x

## 颜色配置
```python
COLOR_AXES = WHITE
COLOR_GRAPH_INCREASE = "#3498db"  # 蓝色 - a>1 时的图像
COLOR_GRAPH_DECREASE = "#e74c3c"  # 红色 - 0<a<1 时的图像
COLOR_HIGHLIGHT = YELLOW
COLOR_POINT = "#2ecc71"  # 绿色 - 定点
COLOR_ASYMPTOTE = "#f39c12"  # 橙色 - 渐近线
COLOR_GRID = GRAY_B
```

## 关键坐标预计算

### 坐标系设置
```python
# 坐标轴范围
x_range = [0, 6, 1]     # [min, max, step]
y_range = [-3, 3, 1]
axis_length_x = 7
axis_length_y = 10

# 坐标轴位置（向上偏移以留出底部空间）
axes_center = UP * 1.5
```

### 关键点位置
```python
# 定点 (1, 0)
FIXED_POINT = axes.c2p(1, 0)

# 渐近线 x = 0 (y轴)
ASYMPTOTE_X = 0

# 示例点
SAMPLE_POINTS_A_GT_1 = [
    (0.5, -0.693),  # log_2(0.5)
    (1, 0),          # log_2(1)
    (2, 1),          # log_2(2)
    (4, 2)           # log_2(4)
]

SAMPLE_POINTS_A_LT_1 = [
    (0.5, 1),        # log_0.5(0.5)
    (1, 0),          # log_0.5(1)
    (2, -1),         # log_0.5(2)
    (4, -2)          # log_0.5(4)
]
```

## 边界检查
- 坐标轴在安全区域：y ∈ [-3, +5]
- 底部文字区域：y ∈ [-6, -3]
- 顶部标题区域：y ∈ [+6, +7]

---

## Scene 1: 开场引入 (0-5秒)

### 目的
抓住学生注意力，引出对数函数概念

### 元素
1. 作者信息（顶部）
2. 钩子问题
3. 神秘符号闪现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "指数的逆运算是什么?" |
| 1.5s | 神秘符号 log 闪现 | `Flash(log_symbol)` |
| 2.5s | 问题文字淡入 | `FadeIn(question)` - "今天揭秘：对数函数!" |
| 4.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, log_symbol, question
- 保留: author_info

---

## Scene 2: 定义展示 (5-12秒)

### 目的
展示对数函数的定义和基本形式

### 元素
1. 定义标题
2. 函数表达式
3. 条件说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题淡入 | `Write(title)` - "对数函数" |
| 5.5s | 主公式书写 | `Write(main_formula)` - y = log_a x |
| 6.5s | 条件说明淡入 | `FadeIn(conditions)` - a>0 且 a≠1 |
| 7.5s | 定义域/值域标注 | `FadeIn(domain_range)` |
| 9.0s | 等待理解 | `Wait(2.0)` |
| 11.0s | 公式移动到顶部 | `formula.animate.scale(0.7).to_edge(UP)` |

### 清理
- 保留: 缩小的公式在顶部
- FadeOut: 其他说明文字

---

## Scene 3: 坐标系建立 (12-18秒)

### 目的
建立坐标系，准备绘制函数图像

### 元素
1. 坐标轴
2. 坐标轴标签
3. 网格线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 坐标轴创建 | `Create(axes)` |
| 13.0s | 标签淡入 | `FadeIn(x_label, y_label)` |
| 14.0s | 网格线淡入 | `FadeIn(grid, shift=ORIGIN)` |
| 15.0s | 标注定点 (1,0) | `FadeIn(fixed_point_dot)` + `Flash` |
| 16.0s | 定点说明 | `Write(fixed_point_label)` - "恒过点(1,0)" |
| 17.0s | 等待 | `Wait(1.0)` |

### 清理
- 保留: axes, labels, grid, fixed_point_dot
- FadeOut: fixed_point_label（暂时）

---

## Scene 4: a>1 情况 - 单调递增 (18-30秒)

### 目的
展示当 a>1 时对数函数的图像和性质

### 元素
1. 函数图像 y = log_2 x
2. 垂直渐近线
3. 箭头指示增长
4. 关键点标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 18.0s | 说明文字 | `Write(case_1_title)` - "当 a > 1 时" |
| 18.5s | 示例 a=2 | `Write(example)` - "例如：y = log_2 x" |
| 19.5s | 绘制渐近线 | `Create(asymptote)` - 虚线 x=0 |
| 20.5s | 渐近线说明 | `FadeIn(asymptote_label)` - "x=0 是垂直渐近线" |
| 22.0s | 绘制图像 | `Create(graph_increase)` - 从左向右 |
| 24.0s | 高亮定点 | `Flash(fixed_point)` + `Indicate` |
| 25.0s | 标注关键点 | `FadeIn(sample_dots)` - (2,1), (4,2) |
| 26.0s | 箭头指示增长 | `GrowArrow(arrow_up)` + `Write("单调递增")` |
| 28.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: case_1_title, example, sample_dots, arrow_up
- 保留: graph_increase（变淡）, asymptote

---

## Scene 5: 0<a<1 情况 - 单调递减 (30-42秒)

### 目的
展示当 0<a<1 时对数函数的图像和性质

### 元素
1. 函数图像 y = log_0.5 x
2. 箭头指示递减
3. 关键点标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 30.0s | 说明文字 | `Write(case_2_title)` - "当 0 < a < 1 时" |
| 30.5s | 示例 a=0.5 | `Write(example_2)` - "例如：y = log_0.5 x" |
| 31.5s | 绘制图像 | `Create(graph_decrease)` - 红色 |
| 33.5s | 高亮定点 | `Flash(fixed_point)` - 两条曲线都过这点 |
| 34.5s | 标注关键点 | `FadeIn(sample_dots_2)` - (2,-1), (4,-2) |
| 35.5s | 箭头指示递减 | `GrowArrow(arrow_down)` + `Write("单调递减")` |
| 37.0s | 对比说明 | `FadeIn(comparison)` - "a 不同，单调性相反!" |
| 39.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: case_2_title, example_2, sample_dots_2, arrow_down, comparison
- 保留: 两条图像都保留用于总结

---

## Scene 6: 关键性质总结 (42-52秒)

### 目的
系统总结对数函数的关键性质

### 元素
1. 性质卡片列表
2. 图像闪烁配合

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 42.0s | 标题 | `Write("对数函数关键性质")` |
| 43.0s | 性质1 | `FadeIn(prop_1)` - "定义域: (0, +∞)" + 图像闪烁 |
| 44.5s | 性质2 | `FadeIn(prop_2)` - "值域: R" |
| 46.0s | 性质3 | `FadeIn(prop_3)` - "恒过点 (1, 0)" + 定点闪烁 |
| 47.5s | 性质4 | `FadeIn(prop_4)` - "x=0 是垂直渐近线" + 渐近线闪烁 |
| 49.0s | 性质5 | `FadeIn(prop_5)` - "单调性取决于底数 a" |
| 50.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有性质卡片
- 保留: 图像

---

## Scene 7: 片尾关注 (52-60秒)

### 目的
引导关注，强化记忆

### 元素
1. 作者信息放大
2. 关注提示
3. 关键公式回顾

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 52.0s | 图像缩小移到角落 | `graphs.animate.scale(0.5).to_corner(UR)` |
| 53.0s | 作者信息放大 | `author_name.animate.scale(2)` |
| 54.0s | 关注文字 | `Write(follow_text)` - "关注我，学更多函数知识!" |
| 55.0s | 公式回顾 | `Write(formula_recap)` - y = log_a x |
| 56.5s | 装饰动画 | 小图标旋转 |
| 59.0s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| axes | Scene 3 | Scene 7 | 坐标系 |
| graph_increase | Scene 4 | Scene 7 | a>1 图像 |
| graph_decrease | Scene 5 | Scene 7 | 0<a<1 图像 |
| asymptote | Scene 4 | Scene 7 | 渐近线 |
| fixed_point_dot | Scene 3 | Scene 7 | 定点标记 |
| main_formula | Scene 2 | Scene 7 | 移到顶部缩小 |

---

## 技术注意事项

### LaTeX 使用
- ✅ 使用 `MathTex(r"y = \log_a x")`
- ✅ 下标: `\log_2 x`
- ❌ 避免中文在 MathTex 中

### 函数绘制
```python
# a > 1 情况 (例如 a=2)
graph_inc = axes.plot(
    lambda x: np.log2(x),
    x_range=[0.1, 6],
    color=COLOR_GRAPH_INCREASE
)

# 0 < a < 1 情况 (例如 a=0.5)
graph_dec = axes.plot(
    lambda x: np.log(x) / np.log(0.5),
    x_range=[0.1, 6],
    color=COLOR_GRAPH_DECREASE
)
```

### 渐近线
```python
# x = 0 (y轴) 作为垂直渐近线
asymptote = DashedLine(
    axes.c2p(0, -3),
    axes.c2p(0, 3),
    color=COLOR_ASYMPTOTE,
    dash_length=0.1
)
```

### 边界验证
- 坐标轴中心: UP * 1.5 (y ≈ 1.5)
- 坐标轴高度: 10 单位
- 范围: y ∈ [1.5 - 5, 1.5 + 5] = [-3.5, 6.5] ✓ 在安全区域内

---

## 动画节奏参考

| 内容类型 | 时长 |
|---------|------|
| 坐标轴创建 | 1.0s |
| 函数图像绘制 | 2.0s |
| 文字书写 | 0.6-0.8s |
| 公式书写 | 0.8-1.0s |
| 关键点闪烁 | 0.4s |
| 理解停顿 | 1.5-2.0s |
| 场景切换 | 0.5s |

---

## 验证检查点

### 几何验证
- [ ] 定点 (1, 0) 位置正确
- [ ] 渐近线 x=0 位置正确
- [ ] 函数值计算准确（log_2(2)=1, log_2(4)=2）

### 边界验证
- [ ] 所有元素在 x ∈ [-4, 4] 范围内
- [ ] 所有元素在 y ∈ [-7, 7] 范围内
- [ ] 文字不重叠

### LaTeX 验证
- [ ] 无中文字符在 MathTex 中
- [ ] 使用 r"..." 原始字符串
- [ ] 下标和上标语法正确