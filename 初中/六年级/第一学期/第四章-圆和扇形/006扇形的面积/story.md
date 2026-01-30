# 扇形的面积 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 六年级 (中等)
- 核心概念: 扇形面积 = 圆面积的一部分

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"        # 蓝色 - 圆
COLOR_SECTOR = "#e74c3c"        # 红色 - 扇形
COLOR_RADIUS = "#2ecc71"        # 绿色 - 半径
COLOR_ARC = "#f39c12"           # 橙色 - 弧
COLOR_ANGLE = "#9b59b6"         # 紫色 - 角度
COLOR_FORMULA = YELLOW          # 黄色 - 公式
COLOR_HIGHLIGHT = GOLD          # 金色 - 强调
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 圆心 | 原点偏移 | self.center | UP * 1.5 |
| 半径 | 固定值 | self.radius | 2.0 |
| 圆心角 | 示例角度 | self.angle | 90° = PI/2 |
| 半径1端点 | 极坐标 | self.P1 | center + radius*RIGHT |
| 半径2端点 | 极坐标 | self.P2 | center + radius*(cos θ, sin θ) |
| 弧长 | 公式 | self.arc_length | (n/360) * 2πr |
| 扇形面积 | 公式 | self.sector_area | (n/360) * πr² |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部小字) - "上海初高中数学直通车 @emptyandcalm"
2. 钩子问题 (大字) - "披萨切一块，面积怎么算?"
3. 披萨简图 (扇形示意)

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | 0.8s |
| 1.1s | 披萨扇形创建 | `Create(pizza_sector, run_time=1.0)` | 1.0s |
| 2.1s | 扇形闪烁强调 | `Flash(pizza_sector, color=GOLD)` | 0.5s |
| 2.6s | 等待理解 | `Wait(1.5)` | 1.5s |
| 4.1s | 过渡文字 | "这就是扇形!" | 0.9s |

### 几何设置
```python
# 披萨扇形 (大角度，更直观)
center = UP * 2.0
radius = 1.8
angle = 120 * DEGREES  # 120度扇形

# 披萨装饰 (芝士效果)
pizza_sector = Sector(
    radius=radius,
    angle=angle,
    start_angle=0,
    color=COLOR_SECTOR,
    fill_opacity=0.3
)
```

### 清理
- FadeOut: hook_text, pizza_sector
- 保留: author_info

---

## Scene 2: 认识扇形 (5-12秒)
**目的**: 定义扇形，展示组成部分

### 元素
1. 标题 "什么是扇形?"
2. 完整的圆
3. 两条半径
4. 圆弧
5. 标注文字

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 5.5s | 圆创建 | `Create(circle, run_time=1.2)` | 1.2s |
| 6.7s | 标记圆心O | `FadeIn(dot_O, label_O)` | 0.5s |
| 7.2s | 绘制半径1 (OA) | `Create(radius_1, run_time=0.6)` | 0.6s |
| 7.8s | 标注点A | `FadeIn(label_A)` | 0.3s |
| 8.1s | 绘制半径2 (OB) | `Create(radius_2, run_time=0.6)` | 0.6s |
| 8.7s | 标注点B | `FadeIn(label_B)` | 0.3s |
| 9.0s | 高亮圆弧AB | `Create(arc, run_time=0.8)` | 0.8s |
| 9.8s | 扇形填充 | `FadeIn(sector_fill)` | 0.6s |
| 10.4s | 定义文字 | "两条半径+圆弧=扇形" | 1.0s |
| 11.4s | 等待 | `Wait(0.6)` | 0.6s |

### 几何计算
```python
self.center = UP * 1.5
self.radius = 2.0
self.angle = 90 * DEGREES  # 示例使用90度

# 半径端点 (精确计算)
self.O = self.center
self.A = self.center + self.radius * RIGHT
self.B = self.center + self.radius * np.array([
    np.cos(self.angle), 
    np.sin(self.angle), 
    0
])

# 圆弧中点 (用于标注)
mid_angle = self.angle / 2
self.arc_mid = self.center + (self.radius + 0.3) * np.array([
    np.cos(mid_angle),
    np.sin(mid_angle),
    0
])
```

### 清理
- FadeOut: title, definition_text
- 保留: circle, sector_fill, radius_1, radius_2, labels

---

## Scene 3: 圆心角概念 (12-18秒)
**目的**: 引入圆心角，建立角度与面积的关系

### 元素
1. 标题 "圆心角"
2. 角度标记 (n°)
3. 角度弧线
4. 几个不同角度的扇形对比

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 12.0s | 标题淡入 | `FadeIn(title_angle)` | 0.5s |
| 12.5s | 圆心角弧线 | `Create(angle_arc, run_time=0.6)` | 0.6s |
| 13.1s | 角度标注 n° | `Write(angle_label)` | 0.5s |
| 13.6s | 说明文字 | "圆心角决定扇形大小" | 0.8s |
| 14.4s | 变换: 60° | `Transform(sector, sector_60)` | 0.8s |
| 15.2s | 变换: 120° | `Transform(sector, sector_120)` | 0.8s |
| 16.0s | 变换: 180° | `Transform(sector, sector_180)` | 0.8s |
| 16.8s | 回到90° | `Transform(sector, sector_90)` | 0.6s |
| 17.4s | 等待 | `Wait(0.6)` | 0.6s |

### 几何计算
```python
# 创建角度标记
def create_angle_arc(center, radius, start_angle, end_angle):
    """创建角度标记弧"""
    arc_radius = 0.5  # 角度标记半径
    return Arc(
        radius=arc_radius,
        start_angle=start_angle,
        angle=end_angle - start_angle,
        arc_center=center,
        color=COLOR_ANGLE,
        stroke_width=3
    )

# 不同角度的扇形
angles = [60, 90, 120, 180]
sectors = {
    angle: Sector(
        outer_radius=self.radius,
        angle=angle * DEGREES,
        start_angle=0,
        arc_center=self.center,
        color=COLOR_SECTOR,
        fill_opacity=0.5
    )
    for angle in angles
}
```

### 清理
- FadeOut: title_angle, explanation, angle variations
- 保留: 90° sector (作为主示例)

---

## Scene 4: 面积公式推导 - 第一形式 (18-30秒)
**目的**: 推导 S = (n/360) × πr²

### 元素
1. 标题 "扇形面积公式"
2. 整圆面积公式
3. 分数关系图解
4. 逐步推导过程

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 18.0s | 标题淡入 | `FadeIn(title_formula)` | 0.5s |
| 18.5s | 问题提出 | "扇形是圆的一部分" | 0.8s |
| 19.3s | 整圆公式 | S_圆 = πr² | 1.0s |
| 20.3s | 圆分割动画 | 360等分展示 | 1.5s |
| 21.8s | 扇形占比 | "圆心角n°占360°的几分之几?" | 1.2s |
| 23.0s | 分数表示 | n/360 高亮 | 0.8s |
| 23.8s | 公式组合 | S_扇形 = (n/360) × S_圆 | 1.2s |
| 25.0s | 最终公式 | S = (n/360) × πr² | 1.0s |
| 26.0s | 公式框住强调 | 矩形框 + 闪烁 | 1.0s |
| 27.0s | 等待理解 | `Wait(2.0)` | 2.0s |

### 几何计算
```python
# 圆分割可视化
def create_circle_divisions(center, radius, num_divisions=12):
    """创建圆的等分线"""
    lines = VGroup()
    for i in range(num_divisions):
        angle = i * TAU / num_divisions
        end_point = center + radius * np.array([
            np.cos(angle),
            np.sin(angle),
            0
        ])
        line = DashedLine(
            center, 
            end_point,
            color=COLOR_AUXILIARY,
            dash_length=0.05
        )
        lines.add(line)
    return lines
```

### 公式排版
```python
# 推导步骤
step_1 = MathTex(r"S_{\text{circle}} = \pi r^2", font_size=32)
step_2 = MathTex(r"\text{ratio} = \frac{n}{360}", font_size=32)
step_3 = MathTex(
    r"S_{\text{sector}} = \frac{n}{360} \times \pi r^2",
    font_size=36
)

# 最终公式 (分隔符用于颜色标注)
formula_final = MathTex(
    r"S = ", 
    r"\frac{n \pi r^2}{360}",
    font_size=40
)
formula_final[1].set_color(COLOR_FORMULA)
```

### 清理
- FadeOut: derivation steps
- 保留: final formula (移到顶部小尺寸)

---

## Scene 5: 面积公式推导 - 第二形式 (30-40秒)
**目的**: 推导 S = (1/2)lr (弧长形式)

### 元素
1. 标题 "另一个公式"
2. 弧长公式
3. 替换推导
4. 两个公式对比

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 30.0s | 标题淡入 | `FadeIn(title_arc)` | 0.5s |
| 30.5s | 高亮圆弧 | `Indicate(arc, color=COLOR_ARC)` | 0.8s |
| 31.3s | 弧长公式 | l = (n/360) × 2πr | 1.2s |
| 32.5s | 提示 | "用弧长代替角度" | 0.8s |
| 33.3s | 从第一公式开始 | S = (n/360) × πr² | 0.8s |
| 34.1s | 变形 | S = (n/360 × 2πr) × (r/2) | 1.2s |
| 35.3s | 替换弧长 | S = l × (r/2) | 1.0s |
| 36.3s | 最终形式 | S = (1/2)lr | 1.0s |
| 37.3s | 框住强调 | 矩形框 + 闪烁 | 0.8s |
| 38.1s | 两公式并列 | 上下排列对比 | 1.2s |
| 39.3s | 等待 | `Wait(0.7)` | 0.7s |

### 公式推导
```python
# 弧长公式
arc_length_formula = MathTex(
    r"l = \frac{n}{360} \times 2\pi r",
    font_size=32
)

# 推导链
deriv_1 = MathTex(r"S = \frac{n}{360} \times \pi r^2")
deriv_2 = MathTex(r"S = \frac{n}{360} \times 2\pi r \times \frac{r}{2}")
deriv_3 = MathTex(r"S = l \times \frac{r}{2}")
deriv_4 = MathTex(r"S = \frac{1}{2}lr", font_size=40)
deriv_4.set_color(COLOR_FORMULA)

# 最终对比
comparison = VGroup(
    MathTex(r"S = \frac{n\pi r^2}{360}", font_size=32),
    MathTex(r"S = \frac{1}{2}lr", font_size=32)
).arrange(DOWN, buff=0.8)
```

### 清理
- FadeOut: title, derivation steps
- 保留: comparison (移到角落)

---

## Scene 6: 实例计算 (40-55秒)
**目的**: 用具体数字演示计算过程

### 元素
1. 标题 "例题"
2. 题目: r=6cm, n=60°, 求面积
3. 几何图形 (带尺寸标注)
4. 分步计算过程
5. 最终答案

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 40.0s | 标题淡入 | `Write(title_example)` | 0.5s |
| 40.5s | 题目显示 | "已知: r=6cm, n=60°" | 1.0s |
| 41.5s | 绘制扇形 | 60°扇形，标注尺寸 | 1.5s |
| 43.0s | 公式选择 | S = (n/360) × πr² | 0.8s |
| 43.8s | 代入数值 | S = (60/360) × π × 6² | 1.2s |
| 45.0s | 化简分数 | S = (1/6) × π × 36 | 1.0s |
| 46.0s | 计算 | S = 6π | 0.8s |
| 46.8s | 近似值 | S ≈ 18.84 cm² | 1.0s |
| 47.8s | 答案框 | 矩形框 + 对勾 | 0.8s |
| 48.6s | 验证用公式2 | 快速展示 l = 2π, S = (1/2)×2π×6 = 6π ✓ | 2.0s |
| 50.6s | 等待 | `Wait(1.4)` | 1.4s |

### 几何绘制
```python
# 示例扇形 (缩小，移到侧边)
example_sector = Sector(
    radius=1.5,
    angle=60 * DEGREES,
    start_angle=0,
    arc_center=LEFT * 2.5 + UP * 1,
    color=COLOR_SECTOR,
    fill_opacity=0.4,
    stroke_width=3
)

# 尺寸标注
radius_line = Line(center, center + 1.5*RIGHT, color=COLOR_RADIUS)
radius_label = MathTex("r=6", font_size=24, color=COLOR_RADIUS)
radius_label.next_to(radius_line, DOWN, buff=0.1)

angle_label = MathTex("60°", font_size=24, color=COLOR_ANGLE)
angle_label.move_to(center + 0.5*np.array([np.cos(30*DEGREES), np.sin(30*DEGREES), 0]))
```

### 计算步骤布局
```python
# 计算过程 (右侧排列)
calc_steps = VGroup(
    MathTex(r"S = \frac{60}{360} \times \pi \times 6^2"),
    MathTex(r"= \frac{1}{6} \times \pi \times 36"),
    MathTex(r"= 6\pi \text{ cm}^2"),
    MathTex(r"\approx 18.84 \text{ cm}^2")
).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
calc_steps.move_to(RIGHT * 2)
```

### 清理
- FadeOut: example sector, calculations
- 保留: 无

---

## Scene 7: 总结与片尾 (55-65秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结卡片 (3条要点)
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 停留时间 |
|------|------|---------|---------|
| 55.0s | 总结标题 | "扇形面积 - 核心要点" | 0.8s |
| 55.8s | 要点1 | "扇形 = 两半径 + 圆弧" | 1.0s |
| 56.8s | 要点2 | "公式1: S=(nπr²)/360" | 1.0s |
| 57.8s | 要点3 | "公式2: S=(1/2)lr" | 1.0s |
| 58.8s | 要点闪烁 | Flash all | 0.5s |
| 59.3s | 清空 | FadeOut要点 | 0.5s |
| 59.8s | 作者信息 | 放大显示 | 0.8s |
| 60.6s | 关注文字 | "关注我，学更多数学技巧!" | 1.2s |
| 61.8s | 装饰动画 | 小扇形旋转 | 2.0s |
| 63.8s | 全部淡出 | FadeOut all | 1.2s |

### 总结卡片设计
```python
def create_summary_card(icon, title, content, color):
    """创建总结要点卡片"""
    # 图标
    icon_obj = icon.scale(0.3).set_color(color)
    
    # 文字
    title_text = Text(title, font="Noto Sans CJK SC", font_size=24, color=WHITE)
    content_text = Text(content, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
    
    # 组合
    card = VGroup(icon_obj, title_text, content_text).arrange(RIGHT, buff=0.3)
    return card

# 三个要点
point_1 = create_summary_card(
    Sector(radius=0.3, angle=PI/2),
    "定义",
    "两半径+圆弧围成",
    COLOR_SECTOR
)

point_2 = create_summary_card(
    MathTex(r"\frac{n}{360}").scale(0.5),
    "公式1",
    "S = (nπr²)/360",
    COLOR_FORMULA
)

point_3 = create_summary_card(
    MathTex(r"\frac{1}{2}lr").scale(0.5),
    "公式2",
    "S = (1/2)lr",
    COLOR_FORMULA
)
```

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 持续时间 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程 | 顶部作者标识 |
| hook_text | Scene 1 | Scene 1 | 4s | 开场钩子 |
| pizza_sector | Scene 1 | Scene 1 | 2.5s | 披萨示意图 |
| circle | Scene 2 | Scene 3 | 6s | 主圆 |
| sector_main | Scene 2 | Scene 6 | 38s | 主扇形 (变换) |
| radius_1, radius_2 | Scene 2 | Scene 3 | 6s | 两条半径 |
| angle_arc | Scene 3 | Scene 4 | 6s | 角度标记 |
| formula_1 | Scene 4 | Scene 5 | 12s | 第一公式 |
| formula_2 | Scene 5 | Scene 6 | 10s | 第二公式 |
| example_sector | Scene 6 | Scene 6 | 8s | 例题图形 |
| summary_cards | Scene 7 | Scene 7 | 5s | 总结卡片 |

---

## 关键技术点

### 1. 扇形精确绘制
```python
sector = Sector(
    radius=radius,
    angle=angle_in_radians,
    start_angle=0,  # 从右侧水平开始
    arc_center=center_point,
    color=COLOR_SECTOR,
    fill_opacity=0.5,
    stroke_width=3
)
```

### 2. 角度标记
```python
angle_arc = Arc(
    radius=0.6,  # 小于扇形半径
    start_angle=0,
    angle=angle_in_radians,
    arc_center=center,
    color=COLOR_ANGLE,
    stroke_width=3
)

# 角度文字
angle_label = MathTex(f"{int(angle_degrees)}°", font_size=28)
angle_label.move_to(center + 0.8 * np.array([
    np.cos(angle_in_radians/2),
    np.sin(angle_in_radians/2),
    0
]))
```

### 3. 公式对齐
```python
# 使用 TransformMatchingTex 实现平滑过渡
formula_1 = MathTex(r"S = {{ \frac{n}{360} }} \times {{ \pi r^2 }}")
formula_2 = MathTex(r"S = {{ \frac{n}{360} \times 2\pi r }} \times {{ \frac{r}{2} }}")

self.play(TransformMatchingTex(formula_1, formula_2))
```

### 4. 圆分割动画
```python
# 创建多个扇形展示360等分概念
sectors_360 = VGroup(*[
    Sector(
        radius=radius,
        angle=1*DEGREES,
        start_angle=i*DEGREES,
        arc_center=center,
        color=COLOR_SECTOR if i % 2 == 0 else COLOR_AUXILIARY,
        fill_opacity=0.6,
        stroke_width=0.5
    )
    for i in range(360)
])
```

---

## 验证检查清单

### 渲染前
- [ ] 所有角度使用弧度制 (`DEGREES` 宏)
- [ ] 扇形中心点统一为 `self.center`
- [ ] 半径统一为 `self.radius`
- [ ] 公式使用 `MathTex`，中文使用 `Text`
- [ ] 颜色配置统一引用全局常量
- [ ] 所有元素在安全边界内 (y ∈ [-7, 7])

### 渲染后
- [ ] 扇形绘制准确无误
- [ ] 角度标记清晰可见
- [ ] 公式推导逻辑正确
- [ ] 动画节奏流畅，难点有停留
- [ ] 无元素重叠遮挡
- [ ] 总时长 60-65秒

---

## 备注

### 难点停留时间
- 公式推导: 2-3秒 (Scene 4, Scene 5)
- 例题计算: 1.5秒 (Scene 6)
- 总结要点: 1秒/条 (Scene 7)

### 动画节奏
- 快: 简单几何图形创建 (0.5-0.8s)
- 中: 公式书写、变换 (0.8-1.2s)
- 慢: 推导步骤、关键概念 (1.5-3.0s)

### 颜色语义
- 红色系: 扇形主体 (强调核心对象)
- 蓝色系: 圆/背景 (辅助参照)
- 绿色系: 半径 (结构元素)
- 橙色系: 弧 (长度元素)
- 紫色系: 角度 (度量元素)
- 黄色/金色: 公式/强调 (重点内容)