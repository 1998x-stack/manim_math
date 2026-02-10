# 函数的定义域与值域 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主函数
COLOR_SECONDARY = "#e74c3c"      # 红色 - 定义域
COLOR_HIGHLIGHT = "#f39c12"      # 橙色 - 值域
COLOR_AUXILIARY = "#95a5a6"      # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"     # 深蓝背景
COLOR_DOMAIN_FILL = "#3498db"    # 定义域填充（半透明）
COLOR_RANGE_FILL = "#f39c12"     # 值域填充（半透明）
```

## 几何/数学元素预计算清单

### 坐标系配置
| 元素 | 参数 | 存储变量 |
|------|------|---------|
| 主坐标系 | x∈[-3,3], y∈[-2,4] | self.axes |
| x轴范围 | [-3, 3, 1] | - |
| y轴范围 | [-2, 4, 1] | - |
| 坐标系位置 | UP * 1.5 | self.AXES_OFFSET |
| 坐标系缩放 | 0.8 | self.AXES_SCALE |

### 函数定义
| 函数 | 公式 | 定义域 | 值域 | 颜色 |
|------|------|--------|------|------|
| 示例1 | f(x)=√(x+1) | x≥-1 | y≥0 | BLUE |
| 示例2 | g(x)=1/(x-1) | x≠1 | y≠0 | RED |
| 示例3 | h(x)=x²-1 | x∈[-2,2] | y∈[-1,3] | GREEN |

### 关键点坐标（示例1: f(x)=√(x+1)）
| 点 | 数学意义 | 坐标计算 | 存储变量 |
|---|---------|---------|---------|
| 定义域起点 | x=-1 | axes.c2p(-1, 0) | self.domain_start |
| 函数起点 | f(-1)=0 | axes.c2p(-1, 0) | self.func_start |
| 定义域终点 | x→+∞ | axes.c2p(3, 0) | self.domain_end |
| 值域起点 | y=0 | axes.c2p(0, 0) | self.range_start |

### 边界安全检查
- 坐标系中心：y = 1.5（在安全区 y∈[-3, 5.5]）
- 标题位置：y = 6.5（在安全区）
- 说明文字：y ∈ [-5, -3]（底部安全区）
- x轴范围：x ∈ [-4, 4]（留边距）

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意 + 引出问题

### 元素
1. 作者标识（顶部，y=7）
2. 钩子问题（大字，y=6）
3. 神秘函数图像（模糊/虚线）

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | 1.0s |
| 1.3s | 神秘函数图像浮现 | `Create(mystery_graph, rate_func=smooth)` | 1.2s |
| 2.5s | 问号闪烁 | `Flash(question_mark)` | 0.5s |
| 3.0s | 等待思考 | `Wait(1.5)` | 1.5s |

### 文案
- 作者信息: "上海初高中数学直通车 @emptyandcalm"
- 钩子: "这个函数能取所有x值吗？"
- 神秘图像: 一条函数曲线（半透明）

### 清理
- FadeOut: hook_text, mystery_graph, question_mark
- 保留: author_info

### 几何验证
- 无复杂几何，仅需验证边界

---

## Scene 2: 定义域概念引入 (5-15秒)
**目的**: 解释定义域的含义

### 元素
1. 标题 "定义域 Domain"（y=5.5）
2. 定义文字（y=4.5）
3. 坐标系（y=1.5）
4. 示例函数: f(x) = √(x+1)

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 5.0s | 标题滑入 | `title.animate.shift(RIGHT*0)` | 0.5s |
| 5.5s | 定义文字淡入 | `FadeIn(definition)` | 0.6s |
| 6.1s | 坐标系绘制 | `Create(axes)` | 1.0s |
| 7.1s | x轴高亮 | `axes.x_axis.animate.set_color(YELLOW)` | 0.4s |
| 7.5s | 说明文字 | `FadeIn(explain_x)` | 0.5s |
| 8.0s | 函数公式写入 | `Write(formula)` | 0.8s |
| 8.8s | 限制条件标注 | `Write(constraint)` | 0.6s |
| 9.4s | x≥-1 区域高亮 | `Create(domain_highlight)` | 0.8s |
| 10.2s | 等待理解 | `Wait(1.5)` | 1.5s |

### 文案
- 标题: "定义域 Domain"
- 定义: "函数有意义的x的取值范围"
- 公式: "f(x) = √(x+1)"
- 约束: "被开方数 ≥ 0"
- 说明: "x+1 ≥ 0 → x ≥ -1"

### 关键计算
```python
# 定义域起点
domain_start_x = -1
domain_start_point = axes.c2p(domain_start_x, 0)

# 定义域高亮区域（x轴上）
domain_line = Line(
    axes.c2p(-1, 0),
    axes.c2p(3, 0),  # 延伸到x=3
    color=COLOR_SECONDARY,
    stroke_width=8
)

# 起点标记
start_dot = Dot(axes.c2p(-1, 0), color=COLOR_SECONDARY, radius=0.08)
```

### 清理
- FadeOut: explain_x, constraint (保留 formula, domain_highlight)
- 保留: title, definition, axes, domain_line, start_dot

### 几何验证
- 验证 domain_start_x = -1 在 x轴范围内
- 验证 domain_line 端点在边界内

---

## Scene 3: 定义域可视化 (15-25秒)
**目的**: 绘制函数图像，展示定义域

### 元素
1. 函数图像 f(x) = √(x+1)
2. 定义域区间标注
3. 端点标记
4. 区间表示法

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 15.0s | 函数图像绘制 | `Create(func_graph)` | 1.5s |
| 16.5s | 端点闪烁 | `Flash(start_dot)` | 0.4s |
| 16.9s | x轴投影虚线 | `Create(projection_lines)` | 0.6s |
| 17.5s | 定义域括号 | `Create(domain_brace)` | 0.5s |
| 18.0s | 区间标注 | `Write(domain_text)` | 0.6s |
| 18.6s | 重点提示 | `FadeIn(highlight_text)` | 0.5s |
| 19.1s | 等待 | `Wait(2.0)` | 2.0s |

### 文案
- 区间标注: "定义域: [-1, +∞)"
- 重点提示: "x只能从-1开始取值"

### 关键计算
```python
# 函数图像
func_graph = axes.plot(
    lambda x: np.sqrt(x + 1),
    x_range=[-1, 3],
    color=COLOR_PRIMARY
)

# 投影虚线（从图像多个点到x轴）
projection_points = [-1, 0, 1, 2, 3]
projection_lines = VGroup(*[
    DashedLine(
        axes.c2p(x, 0),
        axes.c2p(x, np.sqrt(x+1)),
        color=COLOR_AUXILIARY,
        dash_length=0.08
    )
    for x in projection_points
])

# 定义域括号
domain_brace = Brace(
    Line(axes.c2p(-1, 0), axes.c2p(3, 0)),
    direction=DOWN,
    color=COLOR_SECONDARY
)
```

### 清理
- FadeOut: projection_lines, highlight_text
- 保留: func_graph, domain_brace, domain_text

### 几何验证
- 验证函数在 x=-1 处值为0: sqrt(-1+1) = 0
- 验证所有投影点在图像上

---

## Scene 4: 值域概念引入 (25-35秒)
**目的**: 解释值域的含义

### 元素
1. 标题切换到 "值域 Range"
2. y轴高亮
3. 值域区域标注

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 25.0s | 标题变换 | `TransformMatchingTex(old_title, new_title)` | 0.6s |
| 25.6s | 定义文字变换 | `Transform(old_def, new_def)` | 0.5s |
| 26.1s | y轴高亮 | `axes.y_axis.animate.set_color(YELLOW)` | 0.4s |
| 26.5s | x轴恢复 | `axes.x_axis.animate.set_color(WHITE)` | 0.3s |
| 26.8s | 说明文字 | `FadeIn(explain_y)` | 0.5s |
| 27.3s | y≥0 区域高亮 | `Create(range_highlight)` | 0.8s |
| 28.1s | y轴投影虚线 | `Create(y_projection_lines)` | 0.6s |
| 28.7s | 值域括号 | `Create(range_brace)` | 0.5s |
| 29.2s | 区间标注 | `Write(range_text)` | 0.6s |
| 29.8s | 等待 | `Wait(1.5)` | 1.5s |

### 文案
- 标题: "值域 Range"
- 定义: "函数所有可能的y值的集合"
- 说明: "f(x) = √(x+1) ≥ 0"
- 区间标注: "值域: [0, +∞)"

### 关键计算
```python
# 值域起点
range_start_y = 0
range_start_point = axes.c2p(0, range_start_y)

# 值域高亮区域（y轴上）
range_line = Line(
    axes.c2p(0, 0),
    axes.c2p(0, 3.5),  # 延伸到y=3.5
    color=COLOR_HIGHLIGHT,
    stroke_width=8
)

# y轴投影虚线（从图像到y轴）
y_values = [0, 1, 1.414, 1.732, 2]
y_projection_lines = VGroup(*[
    DashedLine(
        axes.c2p(y**2 - 1, y),  # x = y² - 1 (反函数)
        axes.c2p(0, y),
        color=COLOR_AUXILIARY,
        dash_length=0.08
    )
    for y in y_values
])
```

### 清理
- FadeOut: explain_y, y_projection_lines
- 保留: range_highlight, range_brace, range_text, func_graph

### 几何验证
- 验证 y=0 时 x=-1 (起点)
- 验证所有 y_projection_lines 端点在函数图像上

---

## Scene 5: 常见限制条件总结 (35-50秒)
**目的**: 快速展示常见的定义域限制

### 元素
1. 限制条件卡片（5个）
2. 示例公式

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 35.0s | 清屏 | `FadeOut(func_graph, axes, ...)` | 0.5s |
| 35.5s | 总结标题 | `Write(summary_title)` | 0.6s |
| 36.1s | 卡片1: 分式 | `card_1.animate.shift(RIGHT*0)` | 0.5s |
| 36.6s | 卡片2: 偶次根 | `card_2.animate.shift(RIGHT*0)` | 0.5s |
| 37.1s | 卡片3: 对数 | `card_3.animate.shift(RIGHT*0)` | 0.5s |
| 37.6s | 卡片4: 零次幂 | `card_4.animate.shift(RIGHT*0)` | 0.5s |
| 38.1s | 卡片5: 实际意义 | `card_5.animate.shift(RIGHT*0)` | 0.5s |
| 38.6s | 全部卡片高亮 | `cards.animate.set_color(YELLOW)` | 0.4s |
| 39.0s | 恢复颜色 | `cards.animate.set_color(WHITE)` | 0.3s |
| 39.3s | 等待记忆 | `Wait(2.5)` | 2.5s |

### 文案
- 总结标题: "常见定义域限制"
- 卡片1: "① 分式: 分母 ≠ 0"
- 卡片2: "② 偶次根: 被开方数 ≥ 0"
- 卡片3: "③ 对数: 真数 > 0, 底数 > 0 且 ≠ 1"
- 卡片4: "④ 零次幂: 底数 ≠ 0"
- 卡片5: "⑤ 实际问题: 考虑实际意义"

### 卡片布局
```python
cards = VGroup()
y_positions = [2.5, 1.5, 0.5, -0.5, -1.5]

for i, (content, y_pos) in enumerate(zip(contents, y_positions)):
    card = create_constraint_card(content, y_pos)
    cards.add(card)

# 初始位置在左侧外
cards.shift(LEFT * 10)
```

### 清理
- FadeOut: summary_title, cards
- 保留: author_info

### 几何验证
- 验证卡片位置在边界内（y ∈ [-2, 3]）

---

## Scene 6: 值域求法提示 (50-60秒)
**目的**: 简要介绍求值域的方法

### 元素
1. 方法列表
2. 快速示例

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 50.0s | 方法标题 | `Write(methods_title)` | 0.6s |
| 50.6s | 方法1-6依次 | `FadeIn(methods, lag_ratio=0.2)` | 2.0s |
| 52.6s | 重点高亮 | `Indicate(method_2, method_5)` | 0.8s |
| 53.4s | 提示文字 | `FadeIn(tip_text)` | 0.5s |
| 53.9s | 等待 | `Wait(1.5)` | 1.5s |

### 文案
- 方法标题: "求值域常用方法"
- 方法1: "① 观察法（简单函数）"
- 方法2: "② 配方法（二次函数）"
- 方法3: "③ 换元法"
- 方法4: "④ 判别式法"
- 方法5: "⑤ 单调性法"
- 方法6: "⑥ 数形结合法"
- 提示: "掌握方法，灵活运用！"

### 清理
- FadeOut: methods_title, methods, tip_text
- 保留: author_info

---

## Scene 7: 片尾关注 (60-70秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 运行时间 |
|------|------|---------|---------|
| 60.0s | 作者名放大 | `author_info.animate.scale(1.5)` | 0.6s |
| 60.6s | ID显示 | `FadeIn(author_id)` | 0.4s |
| 61.0s | 关注文字 | `FadeIn(follow_text, scale=1.2)` | 0.6s |
| 61.6s | 图标闪烁 | `Flash(icons)` | 0.8s |
| 62.4s | 图标旋转 | `Rotate(icons, PI)` | 1.0s |
| 63.4s | 最终等待 | `Wait(1.5)` | 1.5s |
| 64.9s | 全部淡出 | `FadeOut(everything)` | 1.0s |

### 文案
- 作者名: "上海初高中数学直通车"
- ID: "@emptyandcalm"
- 关注文字: "关注我，学更多函数知识！"

### 清理
- FadeOut: 所有元素

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| mystery_graph | Scene 1 | Scene 1 | 神秘函数 |
| axes | Scene 2 | Scene 5 | 主坐标系 |
| formula | Scene 2 | Scene 5 | f(x)公式 |
| func_graph | Scene 3 | Scene 5 | 函数图像 |
| domain_highlight | Scene 2 | Scene 5 | 定义域标注 |
| range_highlight | Scene 4 | Scene 5 | 值域标注 |
| constraint_cards | Scene 5 | Scene 5 | 限制条件卡片 |
| methods_list | Scene 6 | Scene 6 | 方法列表 |

---

## 关键验证点

### 1. 边界验证
- 坐标系中心 y=1.5 在安全区 ✓
- 所有文字在 y ∈ [-6, 7] ✓
- x轴范围 [-3, 3] 留有边距 ✓

### 2. 数学正确性
- f(-1) = √0 = 0 ✓
- 定义域 x ≥ -1 正确 ✓
- 值域 y ≥ 0 正确 ✓

### 3. LaTeX 安全性
- 避免中文字符在 MathTex 中 ✓
- 使用 Text() 显示中文 ✓
- 公式使用原始字符串 r"..." ✓

### 4. 颜色一致性
- 定义域使用 COLOR_SECONDARY (红色) ✓
- 值域使用 COLOR_HIGHLIGHT (橙色) ✓
- 函数使用 COLOR_PRIMARY (蓝色) ✓

---

## 总时长分配

| 场景 | 时长 | 占比 |
|------|------|------|
| Scene 1: 开场 | 5s | 7% |
| Scene 2: 定义域概念 | 10s | 15% |
| Scene 3: 定义域可视化 | 10s | 15% |
| Scene 4: 值域概念 | 10s | 15% |
| Scene 5: 限制条件总结 | 15s | 23% |
| Scene 6: 值域方法 | 10s | 15% |
| Scene 7: 片尾 | 10s | 15% |
| **总计** | **70s** | **100%** |

---

## 制作注意事项

1. **避免过度动画** - 定义域/值域是基础概念，动画要清晰明了
2. **文字可读性** - 公式和说明要有足够停留时间
3. **颜色区分** - 定义域(红)和值域(橙)要明显区分
4. **LaTeX安全** - 所有数学公式用 MathTex，中文用 Text
5. **边界检查** - 所有元素位置在运行前验证

---

## 备用素材

### 其他示例函数（可替换）
```python
# 示例2: 反比例函数
g(x) = 1 / (x - 1)
# 定义域: x ≠ 1 (分式限制)
# 值域: y ≠ 0

# 示例3: 对数函数
h(x) = log(x)
# 定义域: x > 0 (对数限制)
# 值域: y ∈ R

# 示例4: 二次函数
k(x) = x² - 1, x ∈ [-2, 2]
# 定义域: [-2, 2] (给定区间)
# 值域: [-1, 3] (配方法求得)
```