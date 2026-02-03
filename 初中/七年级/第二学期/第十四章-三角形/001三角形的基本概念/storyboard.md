# 三角形基本概念 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 基础
- 目标年级: 七年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主三角形
COLOR_VERTEX = "#e74c3c"         # 红色 - 顶点
COLOR_EDGE = "#2ecc71"           # 绿色 - 边
COLOR_ANGLE = "#f39c12"          # 橙色 - 角
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_LABEL = WHITE              # 白色 - 标签
COLOR_EQUAL_SIDE = "#9b59b6"     # 紫色 - 等腰三角形相等的边
COLOR_RIGHT_ANGLE = "#e74c3c"    # 红色 - 直角标记
```

## 几何预计算清单

### 主三角形 (一般三角形)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 定义基准点 | `self.A = np.array([-2.5, 0, 0])` |
| 顶点B | 定义基准点 | `self.B = np.array([2.5, -1, 0])` |
| 顶点C | 定义基准点 | `self.C = np.array([0, 2.5, 0])` |
| 边长a (BC) | `np.linalg.norm(B - C)` | `self.a` |
| 边长b (CA) | `np.linalg.norm(C - A)` | `self.b` |
| 边长c (AB) | `np.linalg.norm(A - B)` | `self.c` |
| 角A | `angle_at_vertex(C, A, B)` | `self.angle_A` |
| 角B | `angle_at_vertex(A, B, C)` | `self.angle_B` |
| 角C | `angle_at_vertex(B, C, A)` | `self.angle_C` |

### 等腰三角形 (用于分类演示)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A' | `np.array([0, 2, 0])` | `self.A_iso` |
| 顶点B' | `np.array([-1.5, -1, 0])` | `self.B_iso` |
| 顶点C' | `np.array([1.5, -1, 0])` | `self.C_iso` |
| 验证相等 | `abs(AB - AC) < 1e-6` | 验证函数 |

### 等边三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 边长 | `side_length = 3` | `self.eq_side` |
| 顶点A'' | `np.array([0, side_length * np.sqrt(3)/2, 0])` | `self.A_eq` |
| 顶点B'' | `np.array([-side_length/2, 0, 0])` | `self.B_eq` |
| 顶点C'' | `np.array([side_length/2, 0, 0])` | `self.C_eq` |

### 直角三角形
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A''' | `np.array([-2, -1, 0])` | `self.A_rt` |
| 顶点B''' | `np.array([2, -1, 0])` | `self.B_rt` |
| 顶点C''' | `np.array([2, 2, 0])` | `self.C_rt` |
| 验证直角 | `abs(dot(BA, BC)) < 1e-6` | 验证函数 |

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 抓住注意力，引出主题

### 视觉元素
1. 作者信息 (顶部，y=7)
2. 钩子问题大字 (y=6)
3. 神秘三角形轮廓闪现 (y=1)

### 动画序列
| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2, run_time=0.3)` | N/A |
| 0.3s | 钩子问题书写 | `Write(hook_text, run_time=0.8)` | N/A |
| 1.1s | 三角形轮廓闪现 | `Create(triangle_outline, run_time=0.6)` | 使用 `self.A, B, C` |
| 1.7s | 三角形闪烁3次 | `Flash(triangle, flash_radius=0.5) * 3` | N/A |
| 2.3s | 等待 | `Wait(0.5)` | N/A |

### 文案
```python
author_info = "上海初高中数学直通车 @emptyandcalm"
hook_text = "三角形，你真的了解吗？"  # font_size=48
```

### 清理
- `FadeOut(hook_text, run_time=0.4)`
- 保留: `triangle_outline` (转为虚线), `author_info`

---

## Scene 2: 三角形定义 (5-12秒)

**目的**: 明确三角形的定义和组成

### 视觉元素
1. 标题 "什么是三角形" (y=5.5)
2. 定义文字 (y=4.5)
3. 动态构造演示 (y=0-2)
4. 标注三要素 (顶点、边、角)

### 动画序列
| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title, shift=DOWN*0.2, run_time=0.4)` | N/A |
| 5.4s | 定义文字打字 | `Write(definition, run_time=1.0)` | N/A |
| 6.4s | 清空画布，准备构造 | `FadeOut(triangle_outline, run_time=0.3)` | N/A |
| 6.7s | **顶点A出现** | `FadeIn(dot_A, scale=0.5, run_time=0.3)` | `self.A` |
| 7.0s | **顶点B出现** | `FadeIn(dot_B, scale=0.5, run_time=0.3)` | `self.B` |
| 7.3s | **顶点C出现** | `FadeIn(dot_C, scale=0.5, run_time=0.3)` | `self.C` |
| 7.6s | **连线AB** | `Create(edge_AB, run_time=0.5)` | `Line(A, B)` |
| 8.1s | **连线BC** | `Create(edge_BC, run_time=0.5)` | `Line(B, C)` |
| 8.6s | **连线CA** | `Create(edge_CA, run_time=0.5)` | `Line(C, A)` |
| 9.1s | 形成封闭图形高亮 | `Indicate(triangle, color=YELLOW)` | N/A |
| 9.6s | 标注顶点A, B, C | `Write(label_A, B, C)` | `next_to(dot, direction)` |
| 10.1s | 说明文字 | `FadeIn(explain_text)` | N/A |
| 10.6s | 等待理解 | `Wait(1.2)` | N/A |

### 文案
```python
title = "什么是三角形？"  # font_size=36
definition = "由三条线段首尾顺次相接围成的封闭图形"  # font_size=24
explain_text = "记作 △ABC"  # font_size=22, y=-4
```

### 清理
- `FadeOut(title, definition, explain_text, run_time=0.4)`
- 保留: `triangle` (含顶点标签)

---

## Scene 3: 三角形的基本元素 (12-22秒)

**目的**: 介绍顶点、边、角三大要素

### 子场景3.1: 三个顶点 (12-15秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 12.0s | 标题 "三个顶点" | `Write(title_vertex)` | N/A |
| 12.5s | 顶点A放大高亮 | `dot_A.animate.scale(1.5).set_color(COLOR_VERTEX)` | N/A |
| 13.0s | 顶点B放大高亮 | `dot_B.animate.scale(1.5).set_color(COLOR_VERTEX)` | N/A |
| 13.5s | 顶点C放大高亮 | `dot_C.animate.scale(1.5).set_color(COLOR_VERTEX)` | N/A |
| 14.0s | 全部顶点闪烁 | `Flash(dot_A, B, C)` | N/A |
| 14.5s | 恢复原大小 | `dot_A, B, C.animate.scale(1/1.5)` | N/A |

### 子场景3.2: 三条边 (15-18秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 15.0s | 标题 "三条边" | `Transform(title_vertex, title_edge)` | N/A |
| 15.5s | 边AB高亮 + 标注 | `edge_AB.animate.set_color(COLOR_EDGE).set_stroke(width=5)` | N/A |
|  | 边标签 "c" | `MathTex("c").next_to(edge_AB, DOWN)` | midpoint(A, B) |
| 16.2s | 边BC高亮 + 标注 | `edge_BC.animate.set_color(COLOR_EDGE)` | N/A |
|  | 边标签 "a" | `MathTex("a").next_to(edge_BC, RIGHT)` | midpoint(B, C) |
| 16.9s | 边CA高亮 + 标注 | `edge_CA.animate.set_color(COLOR_EDGE)` | N/A |
|  | 边标签 "b" | `MathTex("b").next_to(edge_CA, LEFT)` | midpoint(C, A) |
| 17.6s | 说明对边关系 | `FadeIn(edge_note)` | N/A |

**文案**: `edge_note = "小写字母表示边，a对应顶点A的对边"`

### 子场景3.3: 三个内角 (18-22秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 18.0s | 边恢复原色 | `edge_AB, BC, CA.animate.set_color(COLOR_PRIMARY)` | N/A |
| 18.3s | 标题 "三个内角" | `Transform(title_edge, title_angle)` | N/A |
| 18.8s | **角A绘制** | `Create(angle_A, run_time=0.6)` | ⚠️ 使用 `Angle.from_three_points(C, A, B)` |
|  | 角标签 | `MathTex(r"\angle A").next_to(angle_A)` | 注意quadrant参数 |
| 19.4s | **角B绘制** | `Create(angle_B, run_time=0.6)` | `Angle.from_three_points(A, B, C)` |
|  | 角标签 | `MathTex(r"\angle B").next_to(angle_B)` | 检查other_angle |
| 20.0s | **角C绘制** | `Create(angle_C, run_time=0.6)` | `Angle.from_three_points(B, C, A)` |
|  | 角标签 | `MathTex(r"\angle C").next_to(angle_C)` | 检查other_angle |
| 20.6s | 说明三角形记号 | `FadeIn(notation_text)` | N/A |
| 21.1s | 等待理解 | `Wait(0.8)` | N/A |

**文案**: `notation_text = "△ABC 表示这个三角形"`

**⚠️ 几何验证点**:
```python
# 必须验证角度和 = 180°
angle_sum = self.angle_A + self.angle_B + self.angle_C
assert abs(angle_sum - np.pi) < 1e-6, f"角度和错误: {np.degrees(angle_sum)}"
```

### 清理
- `FadeOut(title_angle, edge_labels, angle_labels, notation_text, run_time=0.4)`
- 保留: `triangle, angles`

---

## Scene 4: 按边分类 (22-35秒)

**目的**: 展示不等边、等腰、等边三角形

### 子场景4.1: 标题引入 (22-23秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 22.0s | 主三角形缩小移到左上 | `triangle.animate.scale(0.4).to_corner(UL)` | N/A |
| 22.6s | 分类标题 | `Write(classification_title)` | N/A |

**文案**: `classification_title = "三角形的分类 - 按边"`

### 子场景4.2: 不等边三角形 (23-26秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 23.0s | 不等边三角形出现 | `Create(tri_scalene, run_time=0.8)` | 使用 `self.A, B, C` |
| 23.8s | 标注三条边长度不同 | `Write(edge_lengths)` | 显示实际边长 |
| 24.3s | 标签 | `FadeIn(label_scalene)` | N/A |
| 24.8s | 说明 | `FadeIn(explain_scalene)` | N/A |

**文案**:
```python
label_scalene = "不等边三角形"
explain_scalene = "三条边长度都不相等"
edge_lengths = f"a={self.a:.1f}, b={self.b:.1f}, c={self.c:.1f}"  # 显示在三角形旁
```

### 子场景4.3: 等腰三角形 (26-30秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 26.0s | 不等边淡出 | `FadeOut(tri_scalene, labels, run_time=0.3)` | N/A |
| 26.3s | **等腰三角形出现** | `Create(tri_isosceles, run_time=0.8)` | ⚠️ 使用 `self.A_iso, B_iso, C_iso` |
| 27.1s | **标注相等的边** | 两条边高亮为紫色 | `edge_AB_iso.set_color(COLOR_EQUAL_SIDE)` |
|  | 相等标记 | 在两边上画相等记号 (短横线) | midpoint + 垂直短线 |
| 27.8s | 标签 | `FadeIn(label_isosceles)` | N/A |
| 28.3s | 说明 | `FadeIn(explain_isosceles)` | N/A |
| 28.8s | 等待 | `Wait(1.0)` | N/A |

**文案**:
```python
label_isosceles = "等腰三角形"
explain_isosceles = "有两条边相等"
```

**⚠️ 几何验证点**:
```python
# 验证AB = AC
side_AB = np.linalg.norm(self.B_iso - self.A_iso)
side_AC = np.linalg.norm(self.C_iso - self.A_iso)
assert abs(side_AB - side_AC) < 1e-6, "等腰三角形边长不相等"
```

### 子场景4.4: 等边三角形 (30-35秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 30.0s | 等腰淡出 | `FadeOut(tri_isosceles, labels, run_time=0.3)` | N/A |
| 30.3s | **等边三角形出现** | `Create(tri_equilateral, run_time=0.8)` | ⚠️ 使用精确60°计算 |
| 31.1s | **三边全部高亮** | 三边同时变色 | `set_color(COLOR_EQUAL_SIDE)` |
|  | 三边相等标记 | 每条边上两道短横线 | 精确计算中点和垂直方向 |
| 31.8s | 标签 | `FadeIn(label_equilateral)` | N/A |
| 32.3s | 说明 + 特性 | `FadeIn(explain_equilateral)` | N/A |
| 32.8s | **角度标注** | 三个角全部60° | `MathTex("60^{\circ}")` |
| 33.5s | 等待理解 | `Wait(1.2)` | N/A |

**文案**:
```python
label_equilateral = "等边三角形"
explain_equilateral = "三条边都相等，三个角都是60°"
```

**⚠️ 几何验证点**:
```python
# 验证三边相等
side_AB = np.linalg.norm(self.B_eq - self.A_eq)
side_BC = np.linalg.norm(self.C_eq - self.B_eq)
side_CA = np.linalg.norm(self.A_eq - self.C_eq)
assert abs(side_AB - side_BC) < 1e-6 and abs(side_BC - side_CA) < 1e-6

# 验证三个角都是60°
for angle in [angle_A_eq, angle_B_eq, angle_C_eq]:
    assert abs(angle - np.pi/3) < 1e-6, "角度不是60°"
```

### 清理
- `FadeOut(tri_equilateral, all_labels, classification_title, run_time=0.5)`

---

## Scene 5: 按角分类 (35-48秒)

**目的**: 展示锐角、直角、钝角三角形

### 子场景5.1: 标题引入 (35-36秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 35.0s | 分类标题 | `Write(classification_title2)` | N/A |

**文案**: `classification_title2 = "三角形的分类 - 按角"`

### 子场景5.2: 锐角三角形 (36-40秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 36.0s | 锐角三角形出现 | `Create(tri_acute, run_time=0.8)` | 使用精确计算的锐角三角形 |
| 36.8s | **三个角依次高亮** | 角A → 角B → 角C | 每个角闪烁 |
| 37.5s | 角度标注 | 显示三个角度值 | 使用 `np.degrees(angle)` |
| 38.2s | 标签 + 说明 | `FadeIn(label_acute, explain_acute)` | N/A |
| 39.0s | 等待 | `Wait(0.8)` | N/A |

**文案**:
```python
label_acute = "锐角三角形"
explain_acute = "三个角都小于90°"
```

### 子场景5.3: 直角三角形 (40-44秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 40.0s | 锐角淡出 | `FadeOut(tri_acute, labels, run_time=0.3)` | N/A |
| 40.3s | **直角三角形出现** | `Create(tri_right, run_time=0.8)` | ⚠️ 使用 `self.A_rt, B_rt, C_rt` |
| 41.1s | **直角标记** | 使用 `RightAngle` 或 `elbow=True` | ⚠️ 注意quadrant参数 |
|  | 直角高亮 | 直角符号变红色 | `set_color(COLOR_RIGHT_ANGLE)` |
| 41.8s | 标注90° | `MathTex("90^{\circ}")` | next_to直角标记 |
| 42.3s | 标签 + 说明 | `FadeIn(label_right, explain_right)` | N/A |
| 43.0s | 等待 | `Wait(0.8)` | N/A |

**文案**:
```python
label_right = "直角三角形"
explain_right = "有一个角等于90°"
```

**⚠️ 几何验证点**:
```python
# 验证直角 (B是直角顶点)
vec_BA = self.A_rt - self.B_rt
vec_BC = self.C_rt - self.B_rt
dot_product = np.dot(vec_BA[:2], vec_BC[:2])
assert abs(dot_product) < 1e-6, f"不是直角！点积={dot_product}"
```

### 子场景5.4: 钝角三角形 (44-48秒)

| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 44.0s | 直角淡出 | `FadeOut(tri_right, labels, run_time=0.3)` | N/A |
| 44.3s | 钝角三角形出现 | `Create(tri_obtuse, run_time=0.8)` | 使用钝角三角形坐标 |
| 45.1s | **钝角高亮** | 钝角闪烁并放大 | 使用 `Indicate` |
| 45.8s | 角度标注 | 显示钝角度数 (>90°) | 例如 "120°" |
| 46.3s | 标签 + 说明 | `FadeIn(label_obtuse, explain_obtuse)` | N/A |
| 47.0s | 等待 | `Wait(0.8)` | N/A |

**文案**:
```python
label_obtuse = "钝角三角形"
explain_obtuse = "有一个角大于90°"
```

### 清理
- `FadeOut(tri_obtuse, all_labels, classification_title2, run_time=0.5)`

---

## Scene 6: 知识总结 (48-58秒)

**目的**: 用知识卡片汇总所有分类

### 视觉元素
1. 标题 "三角形分类总结" (y=6)
2. 左侧卡片组: 按边分类 (x=-2)
3. 右侧卡片组: 按角分类 (x=+2)

### 动画序列
| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 48.0s | 总结标题 | `Write(summary_title)` | N/A |
| 48.6s | 左标题 "按边分" | `FadeIn(left_title)` | N/A |
| 49.0s | 卡片1: 不等边 | `card1.animate.shift(RIGHT*0)` | 从左侧滑入 |
| 49.5s | 卡片2: 等腰 | `card2.animate.shift(RIGHT*0)` | 从左侧滑入 |
| 50.0s | 卡片3: 等边 | `card3.animate.shift(RIGHT*0)` | 从左侧滑入 |
| 50.5s | 右标题 "按角分" | `FadeIn(right_title)` | N/A |
| 51.0s | 卡片4: 锐角 | `card4.animate.shift(LEFT*0)` | 从右侧滑入 |
| 51.5s | 卡片5: 直角 | `card5.animate.shift(LEFT*0)` | 从右侧滑入 |
| 52.0s | 卡片6: 钝角 | `card6.animate.shift(LEFT*0)` | 从右侧滑入 |
| 52.5s | 全部卡片闪烁 | `Indicate(all_cards)` | N/A |
| 53.2s | 重点提示 | `FadeIn(key_point, scale=1.1)` | N/A |
| 54.0s | 等待理解 | `Wait(3.5)` | N/A |

**文案**:
```python
summary_title = "三角形分类总结"
left_title = "按边分类"
right_title = "按角分类"
key_point = "掌握这6种三角形，轻松解题！"  # font_size=32, y=-5
```

### 卡片内容
```python
# 每个卡片包含: 小图标 + 名称 + 特征
cards = [
    ("不等边", "三边都不等", 小三角形图标),
    ("等腰", "两边相等", 等腰图标),
    ("等边", "三边相等", 等边图标),
    ("锐角", "三角都<90°", 锐角图标),
    ("直角", "一角=90°", 直角图标),
    ("钝角", "一角>90°", 钝角图标),
]
```

### 清理
- `FadeOut(summary_title, all_cards, titles, key_point, run_time=0.6)`

---

## Scene 7: 片尾关注 (58-65秒)

**目的**: 引导关注，结束动画

### 动画序列
| 时间 | 动作 | 代码参考 | 几何计算 |
|------|------|---------|---------|
| 58.0s | 作者信息放大 | `Transform(author_info, author_name_large)` | N/A |
| 58.8s | ID显示 | `FadeIn(author_id, shift=UP*0.3)` | N/A |
| 59.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)` | N/A |
| 60.0s | 六个小三角形装饰 | 围绕关注文字旋转 | 六边形排列 |
| 61.0s | 三角形图案旋转 | `Rotate(triangles, angle=PI)` | N/A |
| 62.5s | 等待 | `Wait(2.0)` | N/A |
| 64.5s | 全部淡出 | `FadeOut(VGroup(*all_elements))` | N/A |

**文案**:
```python
author_name_large = "上海初高中数学直通车"  # font_size=40
author_id = "@emptyandcalm"  # font_size=32
follow_text = "关注我，学更多几何知识！"  # font_size=30
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| `author_info` | Scene 1 | Scene 7 | 贯穿全片 |
| `hook_text` | Scene 1 | Scene 1 | 开场钩子 |
| `triangle` (主) | Scene 2 | Scene 4 | 主三角形 |
| `dot_A, B, C` | Scene 2 | Scene 4 | 顶点 |
| `edge_AB, BC, CA` | Scene 2 | Scene 4 | 边 |
| `angle_A, B, C` | Scene 3 | Scene 4 | 角 |
| `tri_scalene` | Scene 4.2 | Scene 4.2 | 不等边 |
| `tri_isosceles` | Scene 4.3 | Scene 4.3 | 等腰 |
| `tri_equilateral` | Scene 4.4 | Scene 4.4 | 等边 |
| `tri_acute` | Scene 5.2 | Scene 5.2 | 锐角 |
| `tri_right` | Scene 5.3 | Scene 5.3 | 直角 |
| `tri_obtuse` | Scene 5.4 | Scene 5.4 | 钝角 |
| `summary_cards` | Scene 6 | Scene 6 | 总结卡片 |

---

## 关键几何验证检查点

### 验证清单
- [ ] 主三角形角度和 = 180°
- [ ] 等腰三角形两边相等 (误差 < 1e-6)
- [ ] 等边三角形三边相等且三角都是60°
- [ ] 直角三角形垂直验证 (点积 ≈ 0)
- [ ] 所有角度标记方向正确 (quadrant, other_angle)
- [ ] 所有中点计算精确
- [ ] 边界检查: 所有元素在安全区域内

---

## 渲染配置

```bash
# 快速预览
manim -pql triangle_basics.py TriangleBasics

# 高质量输出
manim -qh triangle_basics.py TriangleBasics

# 生产环境 (TikTok上传)
manim -qh --format mp4 triangle_basics.py TriangleBasics
```

---

## 预期总时长: 60-65秒

- Scene 1: 5秒
- Scene 2: 7秒
- Scene 3: 10秒
- Scene 4: 13秒
- Scene 5: 13秒
- Scene 6: 10秒
- Scene 7: 7秒

**总计**: 65秒 ✓ 符合TikTok建议时长 (45-90秒)