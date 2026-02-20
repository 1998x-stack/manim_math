# 圆周角定理 - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 8 个
- 难度等级: 中高级（九年级）
- 核心概念: 圆周角、圆心角、圆周角定理、直径与90°的关系

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"          # 蓝色 - 圆
COLOR_INSCRIBED_ANGLE = "#e74c3c" # 红色 - 圆周角
COLOR_CENTRAL_ANGLE = "#f39c12"   # 橙色 - 圆心角
COLOR_ARC = "#9b59b6"             # 紫色 - 弧
COLOR_DIAMETER = "#2ecc71"        # 绿色 - 直径
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O = ORIGIN + UP * 1.5 |
| 半径 | 固定值 | self.radius = 2.0 |
| 点A（圆上） | O + r*(cos(α), sin(α), 0) | self.A = point_on_circle(30°) |
| 点B（圆上） | O + r*(cos(β), sin(β), 0) | self.B = point_on_circle(150°) |
| 点P（圆上） | O + r*(cos(γ), sin(γ), 0) | self.P = point_on_circle(240°) |
| 圆心角∠AOB | 从OA到OB的角度 | self.central_angle = ∠AOB |
| 圆周角∠APB | 从PA到PB的角度 | self.inscribed_angle = ∠APB |
| 角度关系验证 | inscribed = central / 2 | assert abs(inscribed - central/2) < ε |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 引发好奇 - 角度之间的神奇关系

### 元素
1. 作者标识（顶部）
2. 钩子问题："圆上的角，藏着什么秘密？"
3. 圆和几个点的轮廓

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 圆出现 | `Create(circle, run_time=0.8)` |
| 1.9s | 几个点闪现 | `FadeIn(dots)` |
| 2.9s | 问号闪烁 | `Indicate(question_mark)` |
| 3.4s | 等待 | `Wait(0.3)` |

### 清理
- FadeOut: hook_text, question_mark
- 保留: circle, author_info

---

## Scene 2: 圆周角定义 (6-8秒)
**目的**: 明确圆周角的定义

### 元素
1. 小标题："什么是圆周角？"
2. 圆上的点P（顶点）
3. 圆上的点A和B
4. 圆周角∠APB（高亮）
5. 定义文字："顶点在圆上，两边都与圆相交的角"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 点P出现在圆上 | `FadeIn(dot_P, scale=0.5)` |
| 1.0s | 点A和B出现 | `FadeIn(dot_A), FadeIn(dot_B)` |
| 1.6s | 连线PA和PB | `Create(line_PA), Create(line_PB)` |
| 2.2s | 圆周角弧出现 | `Create(inscribed_angle_arc)` |
| 3.0s | 标注"圆周角" | `FadeIn(label_inscribed)` |
| 3.8s | 定义文字 | `FadeIn(definition_text)` |
| 5.0s | 等待理解 | `Wait(1.5)` |

### 几何验证
```python
# 验证P、A、B都在圆上
assert abs(np.linalg.norm(P - O) - radius) < 1e-6
assert abs(np.linalg.norm(A - O) - radius) < 1e-6
assert abs(np.linalg.norm(B - O) - radius) < 1e-6
```

### 清理
- FadeOut: subtitle, definition_text
- 保留: circle, dots, angle

---

## Scene 3: 圆心角引入 (5-6秒)
**目的**: 引入圆心角概念，为定理做铺垫

### 元素
1. 圆心O
2. 圆心角∠AOB（橙色）
3. 弧AB（紫色粗线）
4. 标注："圆心角"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 圆心O出现 | `FadeIn(dot_O, scale=0.5)` |
| 0.5s | 标注"O" | `FadeIn(label_O)` |
| 1.0s | 连线OA和OB | `Create(line_OA), Create(line_OB)` |
| 1.8s | 圆心角弧出现 | `Create(central_angle_arc)` |
| 2.5s | 标注"圆心角" | `FadeIn(label_central)` |
| 3.2s | 弧AB高亮 | `Create(arc_AB, color=COLOR_ARC)` |
| 4.2s | 等待 | `Wait(1.0)` |

### 几何验证
```python
# 验证圆心角计算正确
angle_A = arctan2(A[1]-O[1], A[0]-O[0])
angle_B = arctan2(B[1]-O[1], B[0]-O[0])
central_angle = abs(angle_B - angle_A)
if central_angle > PI:
    central_angle = 2*PI - central_angle
```

### 清理
- FadeOut: 无（保留用于对比）
- 保留: 所有元素

---

## Scene 4: 圆周角定理主体 (10-12秒)
**目的**: 展示并证明核心定理

### 元素
1. 大标题："圆周角定理"
2. 圆周角∠APB（红色）
3. 圆心角∠AOB（橙色）
4. 公式："∠APB = (1/2)∠AOB"
5. 动画：显示角度数值

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 大标题淡入 | `FadeIn(main_title, shift=UP*0.3)` |
| 0.8s | 圆周角高亮 | `Indicate(inscribed_angle, color=RED)` |
| 1.5s | 圆心角高亮 | `Indicate(central_angle, color=ORANGE)` |
| 2.5s | 公式出现 | `Write(formula, run_time=1.0)` |
| 3.5s | 测量圆心角 | `FadeIn(central_measure)` |
| 4.5s | 测量圆周角 | `FadeIn(inscribed_measure)` |
| 5.5s | 对比动画（闪烁） | `Indicate(both_angles)` |
| 7.0s | 强调"一半" | `Indicate(formula[half_part])` |
| 8.5s | 等待理解 | `Wait(2.0)` |

### 几何验证（CRITICAL）
```python
# 这是最关键的验证
central_angle_rad = calculate_central_angle(O, A, B)
inscribed_angle_rad = calculate_inscribed_angle(P, A, B)

# 验证定理
ratio = inscribed_angle_rad / central_angle_rad
assert abs(ratio - 0.5) < 1e-4, f"定理验证失败！圆周角/圆心角 = {ratio}"
```

### 清理
- FadeOut: main_title, measures
- 保留: formula, angles

---

## Scene 5: 推论1 - 同弧圆周角相等 (7-9秒)
**目的**: 展示第一个推论

### 元素
1. 小标题："推论1：同弧所对的圆周角相等"
2. 另一个点Q在圆上（不同位置）
3. 圆周角∠AQB
4. 显示∠APB = ∠AQB

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.8s | 点Q出现 | `FadeIn(dot_Q, scale=0.5)` |
| 1.4s | 连线QA和QB | `Create(line_QA), Create(line_QB)` |
| 2.2s | 圆周角∠AQB出现 | `Create(angle_AQB)` |
| 3.2s | 两个圆周角同时高亮 | `Indicate(angle_APB), Indicate(angle_AQB)` |
| 4.5s | 角度数值显示 | `FadeIn(angle_values)` |
| 5.5s | 等号出现 | `Write(equals_sign)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证两个圆周角相等
angle_APB = calculate_inscribed_angle(P, A, B)
angle_AQB = calculate_inscribed_angle(Q, A, B)
assert abs(angle_APB - angle_AQB) < 1e-4
```

### 清理
- FadeOut: subtitle, Q相关元素, angle_values
- 保留: circle, 原有角度

---

## Scene 6: 推论2 - 直径对应90° (8-10秒)
**目的**: 展示直径所对的圆周角是直角

### 元素
1. 小标题："推论2：直径所对的圆周角 = 90°"
2. 直径AB（绿色粗线）
3. 圆上的点C
4. 圆周角∠ACB = 90°
5. 直角符号

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空并重置 | `FadeOut(previous_elements)` |
| 0.5s | 小标题写入 | `Write(subtitle)` |
| 1.2s | 直径AB出现（通过圆心） | `Create(diameter_AB)` |
| 2.0s | 标注"直径" | `FadeIn(diameter_label)` |
| 2.8s | 点C出现在圆上（任意位置） | `FadeIn(dot_C, scale=0.5)` |
| 3.6s | 连线CA和CB | `Create(line_CA), Create(line_CB)` |
| 4.4s | 圆周角出现 | `Create(angle_ACB)` |
| 5.4s | 直角符号 | `FadeIn(right_angle_mark)` |
| 6.4s | 90°标注 | `FadeIn(angle_90_label)` |
| 7.4s | 等待 | `Wait(1.5)` |

### 几何验证（CRITICAL）
```python
# 验证AB是直径
assert abs(np.linalg.norm(A - O) - radius) < 1e-6
assert abs(np.linalg.norm(B - O) - radius) < 1e-6
# A和B在O的两侧
midpoint_AB = (A + B) / 2
assert np.linalg.norm(midpoint_AB - O) < 1e-6

# 验证圆周角是90°
angle_ACB = calculate_inscribed_angle(C, A, B)
assert abs(angle_ACB - PI/2) < 1e-4
```

### 清理
- FadeOut: subtitle, diameter_label, angle_90_label
- 保留: diameter, angle with right angle mark

---

## Scene 7: 推论3 - 90°对应直径 (7-9秒)
**目的**: 展示逆命题

### 元素
1. 小标题："推论3：90°圆周角所对的弦是直径"
2. 先有圆周角90°
3. 验证对应的弦是直径

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.8s | 强调90°角 | `Indicate(right_angle_mark)` |
| 1.6s | 弦AB高亮 | `Indicate(chord_AB)` |
| 2.6s | 圆心O闪烁 | `Flash(dot_O)` |
| 3.4s | 验证线通过圆心 | `Create(extended_line)` |
| 4.4s | 标注"直径" | `FadeIn(diameter_confirmation)` |
| 5.4s | 对号出现 | `FadeIn(check_mark)` |
| 6.4s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证：给定90°圆周角，对应的弦是直径
# AB的中点应该是圆心
midpoint = (A + B) / 2
assert np.linalg.norm(midpoint - O) < 1e-4
```

### 清理
- FadeOut: subtitle, check_mark, extended_line
- 保留: 主要元素

---

## Scene 8: 总结与片尾 (10-12秒)
**目的**: 知识总结，强化记忆

### 元素
1. 图形缩小移到上方
2. 知识卡片（4个要点）
3. 总结文字
4. 作者关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 整体缩小上移 | `VGroup(...).animate.scale(0.5).move_to(UP*4.5)` |
| 1.0s | 卡片1："圆周角 = 圆心角 ÷ 2" | `FadeIn(card_1, shift=RIGHT)` |
| 1.8s | 卡片2："同弧圆周角相等" | `FadeIn(card_2, shift=RIGHT)` |
| 2.6s | 卡片3："直径 → 90°" | `FadeIn(card_3, shift=RIGHT)` |
| 3.4s | 卡片4："90° → 直径" | `FadeIn(card_4, shift=RIGHT)` |
| 4.5s | 总结文字 | `FadeIn(summary_text, shift=UP*0.3)` |
| 5.5s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 6.5s | 关注提示 | `FadeIn(follow_text)` |
| 7.5s | 装饰动画 | `Rotate(decorations, PI)` |
| 9.0s | 等待 | `Wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 顶部作者信息 |
| circle | Scene 1 | Scene 8 | 主圆 |
| dot_A, dot_B | Scene 2 | Scene 8 | 弧的端点 |
| dot_P | Scene 2 | Scene 5 | 圆周角顶点1 |
| inscribed_angle | Scene 2 | Scene 5 | 圆周角∠APB |
| dot_O | Scene 3 | Scene 8 | 圆心 |
| central_angle | Scene 3 | Scene 5 | 圆心角∠AOB |
| dot_Q | Scene 5 | Scene 5 | 圆周角顶点2 |
| diameter | Scene 6 | Scene 8 | 直径AB |
| dot_C | Scene 6 | Scene 7 | 直径对应的圆周角顶点 |
| right_angle_mark | Scene 6 | Scene 7 | 90°标记 |
| knowledge_cards | Scene 8 | Scene 8 | 知识卡片 |

---

## 关键技术点

### 1. 圆上点的精确计算
```python
def point_on_circle(center, radius, angle_deg):
    """在圆上生成精确的点"""
    angle_rad = angle_deg * DEGREES
    return center + radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
```

### 2. 圆周角的精确计算（CRITICAL）
```python
def calculate_inscribed_angle(vertex, point1, point2):
    """
    计算圆周角（从vertex看point1到point2的角度）
    注意：需要考虑角度方向
    """
    v1 = point1 - vertex
    v2 = point2 - vertex
    
    # 计算夹角
    cos_angle = np.dot(v1[:2], v2[:2]) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angle = np.arccos(cos_angle)
    
    return angle
```

### 3. 圆心角的精确计算
```python
def calculate_central_angle(center, point1, point2):
    """计算圆心角"""
    angle1 = np.arctan2(point1[1] - center[1], point1[0] - center[0])
    angle2 = np.arctan2(point2[1] - center[1], point2[0] - center[0])
    
    angle = abs(angle2 - angle1)
    if angle > np.pi:
        angle = 2 * np.pi - angle
    
    return angle
```

### 4. Angle对象的正确创建
```python
# 对于圆周角，需要特别注意方向
# 如果计算出的角度 > 180°，可能需要 other_angle=True

inscribed_angle = Angle.from_three_points(
    point_A,
    vertex_P,
    point_B,
    radius=0.5,
    other_angle=False  # 根据实际情况调整
)
```

### 5. 直径验证
```python
def is_diameter(point1, point2, center):
    """验证线段是否为直径"""
    midpoint = (point1 + point2) / 2
    return np.linalg.norm(midpoint - center) < 1e-6
```

---

## 预期时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场钩子 | 3-4s | 4s |
| Scene 2: 圆周角定义 | 6-8s | 12s |
| Scene 3: 圆心角引入 | 5-6s | 18s |
| Scene 4: 主定理 | 10-12s | 30s |
| Scene 5: 推论1 | 7-9s | 39s |
| Scene 6: 推论2 | 8-10s | 49s |
| Scene 7: 推论3 | 7-9s | 58s |
| Scene 8: 总结 | 10-12s | 70s |
| **总计** | **75-90s** | |

---

## 风格统一要点

1. **角度精确性**：这是本动画的核心，必须确保所有角度计算精确
2. **角度方向**：特别注意Manim的角度方向，必要时使用other_angle
3. **颜色区分**：圆周角（红）、圆心角（橙）、弧（紫）、直径（绿）
4. **动画节奏**：定理部分停留时间长（2-3秒），推论部分适中（1.5秒）
5. **视觉对比**：定理展示时，圆周角和圆心角要同时可见，便于对比

---

## 验证清单（CRITICAL）

### 几何验证
- [ ] 所有点都在圆上（距圆心距离 = 半径）
- [ ] 圆周角 = 圆心角 / 2（误差 < 0.01°）
- [ ] 同弧的两个圆周角相等
- [ ] 直径的中点是圆心
- [ ] 直径对应的圆周角 = 90°
- [ ] 90°圆周角对应的弦是直径

### 角度验证（CRITICAL）
- [ ] 所有角度 < 180°（如果>180°检查other_angle）
- [ ] 圆周角测量正确（使用正确的顶点和两边）
- [ ] 圆心角测量正确（从圆心出发）
- [ ] 90°直角标记正确

### LaTeX检查
- [ ] 无中文字符在 MathTex 中
- [ ] 使用 `^\circ` 表示度数
- [ ] 分数使用 `\frac{1}{2}` 而非 1/2

### 边界检查
- [ ] 所有元素在边界内
- [ ] 文字不重叠
- [ ] 角度标记清晰可见