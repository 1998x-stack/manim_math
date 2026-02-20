# 圆的定义与基本概念 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级（九年级）
- 核心概念: 圆的定义、基本元素（圆心、半径、直径、弦、弧）

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"       # 蓝色 - 主圆
COLOR_RADIUS = "#e74c3c"       # 红色 - 半径
COLOR_DIAMETER = "#f39c12"     # 橙色 - 直径
COLOR_CHORD = "#2ecc71"        # 绿色 - 弦
COLOR_ARC = "#9b59b6"          # 紫色 - 弧
COLOR_CENTER = "#e74c3c"       # 红色 - 圆心
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O = ORIGIN + UP * 1.0 |
| 半径 | 固定值 | self.radius = 2.0 |
| 点A（圆上） | O + radius * (cos, sin, 0) | self.A = self.O + self.radius * RIGHT |
| 点B（圆上） | O + radius * (cos(θ), sin(θ), 0) | self.B = self.O + self.radius * rotate(UP, angle) |
| 点C（圆上） | O + radius * (cos(φ), sin(φ), 0) | self.C = self.O + self.radius * rotate(LEFT, angle) |
| 直径端点 | O ± radius * direction | self.D = self.O - self.radius * RIGHT |
| 弦端点 | 圆上两点 | 使用 A 和 B |
| 弧的圆心角 | angle_B - angle_A | self.arc_angle |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力 + 引出圆的普遍性

### 元素
1. 作者标识（顶部）
2. 钩子问题："为什么车轮是圆的？"
3. 简单的圆形轮廓动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 圆形轮廓创建 | `Create(circle_outline, run_time=1.0)` |
| 2.1s | 旋转动画（暗示车轮） | `Rotate(circle_outline, PI, run_time=1.0)` |
| 3.1s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text
- 保留: circle_outline (将转换为主圆), author_info

---

## Scene 2: 圆的定义 (8-10秒)
**目的**: 建立圆的数学定义

### 元素
1. 标题："圆的定义"
2. 圆心O（红色点）
3. 半径标注
4. 多个从圆心出发的半径（展示等距性）
5. 定义文字："{P | |PO| = r}"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=DOWN*0.3)` |
| 0.5s | 圆心点出现 | `FadeIn(center_dot, scale=0.5)` |
| 0.8s | 第一条半径生长 | `GrowFromCenter(radius_1)` |
| 1.3s | 半径标注"r" | `FadeIn(radius_label)` |
| 1.8s | 多条半径依次出现（6-8条） | `AnimationGroup([Create(r) for r in radii])` |
| 2.8s | 圆周轨迹描绘 | `Create(circle, run_time=1.5)` |
| 4.3s | 定义公式淡入 | `FadeIn(definition_formula, shift=UP*0.3)` |
| 5.3s | 强调"等距" | `Indicate(radii), Flash(center_dot)` |
| 6.3s | 等待理解 | `Wait(1.5)` |

### 几何验证
```python
# 验证所有半径长度相等
for radius_line in self.radii:
    length = np.linalg.norm(radius_line.get_end() - self.O)
    assert abs(length - self.radius) < 1e-6
```

### 清理
- FadeOut: radii (除了一条), definition_formula, title
- 保留: circle, center_dot, radius_1

---

## Scene 3: 半径 (6-8秒)
**目的**: 明确半径的定义和特性

### 元素
1. 小标题："半径 Radius"
2. 多条半径高亮
3. 半径公式：r = |PO|
4. 说明文字："连接圆心与圆上任意一点的线段"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 创建3-4条不同角度的半径 | `AnimationGroup([Create(r) for r in radius_group])` |
| 1.6s | 半径闪烁高亮 | `Indicate(radius_group, color=COLOR_HIGHLIGHT)` |
| 2.3s | 显示公式 | `FadeIn(radius_formula)` |
| 3.0s | 说明文字 | `FadeIn(explanation_text)` |
| 4.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: subtitle, radius_group (除了水平方向的两条), formula, explanation
- 保留: circle, center_dot

---

## Scene 4: 直径 (7-9秒)
**目的**: 引入直径概念，建立与半径的关系

### 元素
1. 小标题："直径 Diameter"
2. 直径线（橙色粗线）
3. 直径端点A和D
4. 公式：d = 2r
5. 说明："通过圆心的弦，圆中最长的弦"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 两条半径变色为橙色 | `radius_AD.animate.set_color(COLOR_DIAMETER)` |
| 1.2s | 两条半径合并为直径 | `Transform(radius_group, diameter_line)` |
| 1.8s | 端点标注A和D | `FadeIn(point_A_label), FadeIn(point_D_label)` |
| 2.5s | 直径标注"d" | `FadeIn(diameter_label)` |
| 3.2s | 公式d=2r出现 | `FadeIn(formula)` |
| 4.2s | 测量动画（展示长度） | `MeasureLine(A, D)` |
| 5.2s | 说明文字 | `FadeIn(explanation)` |
| 6.2s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证直径长度 = 2 * 半径
diameter_length = np.linalg.norm(self.A - self.D)
assert abs(diameter_length - 2 * self.radius) < 1e-6

# 验证直径通过圆心
midpoint = (self.A + self.D) / 2
assert np.linalg.norm(midpoint - self.O) < 1e-6
```

### 清理
- FadeOut: subtitle, diameter_line, labels, formula, explanation
- 保留: circle, center_dot

---

## Scene 5: 弦 (7-9秒)
**目的**: 介绍弦的概念，区分弦和直径

### 元素
1. 小标题："弦 Chord"
2. 弦线（绿色）连接B和C
3. 点B和C标注
4. 对比：弦 vs 直径
5. 说明："连接圆上任意两点的线段"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 点B和C出现在圆上 | `FadeIn(dot_B), FadeIn(dot_C)` |
| 1.2s | 弦BC生长 | `GrowFromCenter(chord_BC)` |
| 1.8s | 点标注 | `FadeIn(label_B), FadeIn(label_C)` |
| 2.5s | 弦高亮 | `Indicate(chord_BC, color=COLOR_HIGHLIGHT)` |
| 3.2s | 创建另一条弦（对比） | `Create(chord_2)` |
| 4.2s | 直径重新出现（虚线）用于对比 | `Create(diameter_dashed)` |
| 5.2s | 对比文字："直径是特殊的弦（最长）" | `FadeIn(comparison_text)` |
| 6.2s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证B和C在圆上
assert abs(np.linalg.norm(self.B - self.O) - self.radius) < 1e-6
assert abs(np.linalg.norm(self.C - self.O) - self.radius) < 1e-6

# 验证弦长度小于直径
chord_length = np.linalg.norm(self.C - self.B)
assert chord_length <= 2 * self.radius + 1e-6
```

### 清理
- FadeOut: subtitle, chord_BC, chord_2, diameter_dashed, labels, comparison_text
- 保留: circle, center_dot, dot_B, dot_C

---

## Scene 6: 弧 (8-10秒)
**目的**: 介绍弧的概念，区分优弧和劣弧

### 元素
1. 小标题："弧 Arc"
2. 劣弧BC（紫色粗弧）
3. 优弧BC（紫色虚线弧）
4. 弧的符号表示：⌢BC
5. 说明："圆上两点间的部分"
6. 优弧/劣弧标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 点B和C闪烁 | `Indicate(dot_B), Indicate(dot_C)` |
| 1.2s | 劣弧BC描绘（较短的弧） | `Create(minor_arc, run_time=1.0)` |
| 2.2s | 劣弧标注"⌢BC" | `FadeIn(minor_arc_label)` |
| 3.2s | 说明："劣弧（小于半圆）" | `FadeIn(minor_arc_explanation)` |
| 4.2s | 优弧BC描绘（较长的弧，虚线） | `Create(major_arc, run_time=1.5)` |
| 5.7s | 优弧标注 | `FadeIn(major_arc_label)` |
| 6.5s | 说明："优弧（大于半圆）" | `FadeIn(major_arc_explanation)` |
| 7.5s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证劣弧角度小于π
angle_B = np.arctan2(self.B[1] - self.O[1], self.B[0] - self.O[0])
angle_C = np.arctan2(self.C[1] - self.O[1], self.C[0] - self.O[0])
minor_angle = abs(angle_C - angle_B)
if minor_angle > PI:
    minor_angle = 2 * PI - minor_angle
assert minor_angle < PI + 1e-6

# 优弧角度 = 2π - 劣弧角度
major_angle = 2 * PI - minor_angle
assert major_angle > PI - 1e-6
```

### 清理
- FadeOut: subtitle, minor_arc, major_arc, all labels, explanations
- 保留: circle, center_dot

---

## Scene 7: 总结与片尾 (10-12秒)
**目的**: 回顾所有概念，强化记忆

### 元素
1. 完整的圆及所有标注
2. 知识卡片（5个概念）
3. 总结文字："掌握圆的基本元素，开启几何新篇章！"
4. 作者关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 圆缩小并移到上方 | `circle.animate.scale(0.5).move_to(UP*3)` |
| 1.0s | 依次显示5个知识卡片 | 依次FadeIn每张卡片 |
| | - 圆心：定点O | |
| | - 半径：r = \|PO\| | |
| | - 直径：d = 2r，通过圆心 | |
| | - 弦：连接圆上两点 | |
| | - 弧：圆上两点间的部分 | |
| 5.0s | 总结文字淡入 | `FadeIn(summary_text, shift=UP*0.3)` |
| 6.0s | 作者信息放大 | `author_info.animate.scale(1.5).move_to(UP*1)` |
| 7.0s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 8.0s | 小圆形装饰环绕 | `Rotate(decorations, PI, run_time=1.5)` |
| 9.5s | 等待 | `Wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 一直保留在顶部 |
| circle | Scene 2 | Scene 7 | 主圆，贯穿全程 |
| center_dot | Scene 2 | Scene 7 | 圆心点 |
| radius_1 | Scene 2 | Scene 4 | 演示半径 |
| diameter_line | Scene 4 | Scene 4 | 直径 |
| chord_BC | Scene 5 | Scene 5 | 弦 |
| dot_B, dot_C | Scene 5 | Scene 7 | 圆上的点 |
| minor_arc | Scene 6 | Scene 6 | 劣弧 |
| major_arc | Scene 6 | Scene 6 | 优弧 |
| knowledge_cards | Scene 7 | Scene 7 | 知识总结卡片 |

---

## 关键技术点

### 1. 圆上点的精确计算
```python
def point_on_circle(center, radius, angle_deg):
    """在圆上生成精确的点"""
    angle_rad = angle_deg * DEGREES
    return center + radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
```

### 2. 弧的精确绘制
```python
# 使用 Arc 类，确保角度方向正确
# start_angle: 起始角度（弧度）
# angle: 扫过的角度（正为逆时针，负为顺时针）
minor_arc = Arc(
    radius=self.radius,
    start_angle=angle_B,
    angle=angle_C - angle_B,  # 确保为劣弧角度
    color=COLOR_ARC,
    stroke_width=6
).move_to(self.O)
```

### 3. 边界检查
```python
# 确保所有元素在安全区域内
# 圆的最大半径不超过 min(frame_width/2, frame_height/2) - margin
max_radius = min(config.frame_width / 2, config.frame_height / 2) - 1.0
assert self.radius < max_radius
```

### 4. 字体大小遵循
- 标题：36
- 小标题：28
- 正文：22
- 标注：20
- 公式：28

---

## 预期时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 3-4s | 4s |
| Scene 2: 圆的定义 | 8-10s | 14s |
| Scene 3: 半径 | 6-8s | 22s |
| Scene 4: 直径 | 7-9s | 31s |
| Scene 5: 弦 | 7-9s | 40s |
| Scene 6: 弧 | 8-10s | 50s |
| Scene 7: 总结 | 10-12s | 62s |
| **总计** | **60-75s** | |

---

## 风格统一要点

1. **配色一致性**：每个元素有专属颜色，不混用
2. **动画节奏**：难点（定义）慢，简单概念（标注）快
3. **文字规范**：中文使用Text，数学公式使用MathTex
4. **几何精确性**：所有坐标通过计算获得，不臆想
5. **边界意识**：主内容区域 y ∈ [-3, +5]，底部文字 y ∈ [-6, -3]