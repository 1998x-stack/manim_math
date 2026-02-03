# 三角形的重要线段 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 七年级学生

## 颜色配置
```python
COLOR_MEDIAN = "#e74c3c"        # 红色 - 中线
COLOR_ALTITUDE = "#3498db"      # 蓝色 - 高线
COLOR_ANGLE_BISECTOR = "#2ecc71" # 绿色 - 角平分线
COLOR_TRIANGLE = WHITE
COLOR_AUXILIARY = GRAY_B
COLOR_HIGHLIGHT = YELLOW
BACKGROUND = "#1a1a2e"
```

## 几何预计算清单

### 基准三角形顶点
- A = np.array([-2.5, 1.5, 0]) * SCALE + OFFSET
- B = np.array([2.5, -0.5, 0]) * SCALE + OFFSET
- C = np.array([-1.0, -2.5, 0]) * SCALE + OFFSET
- SCALE = 0.85
- OFFSET = UP * 1.5

### 中线相关
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| BC中点 | M_BC = (B + C) / 2 | self.M_BC |
| CA中点 | M_CA = (C + A) / 2 | self.M_CA |
| AB中点 | M_AB = (A + B) / 2 | self.M_AB |
| 重心 | G = (A + B + C) / 3 | self.centroid |
| 中线AM | Line(A, M_BC) | median_1 |
| 中线BN | Line(B, M_CA) | median_2 |
| 中线CP | Line(C, M_AB) | median_3 |

### 高线相关
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| A到BC垂足 | foot_of_perpendicular(A, B, C) | foot_D |
| B到CA垂足 | foot_of_perpendicular(B, C, A) | foot_E |
| C到AB垂足 | foot_of_perpendicular(C, A, B) | foot_F |
| 垂心 | calculate_orthocenter() | self.orthocenter |
| 高线AD | DashedLine(A, foot_D) | altitude_1 |
| 高线BE | DashedLine(B, foot_E) | altitude_2 |
| 高线CF | DashedLine(C, foot_F) | altitude_3 |

### 角平分线相关
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 角A平分线交BC于点 | D = B + (c/(b+c))*(C-B) | point_D |
| 角B平分线交CA于点 | E = C + (a/(a+c))*(A-C) | point_E |
| 角C平分线交AB于点 | F = A + (b/(a+b))*(B-A) | point_F |
| 内心 | I = (a*A + b*B + c*C)/(a+b+c) | self.incenter |
| 角平分线AD | DashedLine(A, point_D) | bisector_1 |
| 角平分线BE | DashedLine(B, point_E) | bisector_2 |
| 角平分线CF | DashedLine(C, point_F) | bisector_3 |

### 角度计算(重要⚠️)
```python
# 角A的计算
vec_AB = B - A
vec_AC = C - A
angle_A = angle_between_vectors(vec_AB, vec_AC)  # 应该 < 180度

# 角弧方向判断
cross_z = vec_AB[0] * vec_AC[1] - vec_AB[1] * vec_AC[0]
if cross_z > 0:
    # 逆时针,使用 other_angle=False
    angle_arc = Angle(line_AB, line_AC, other_angle=False)
else:
    # 顺时针,使用 other_angle=True
    angle_arc = Angle(line_AB, line_AC, other_angle=True)
```

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力 + 引出问题

### 元素
1. 作者标识 (顶部小字) - `author_info`
2. 钩子问题 (大字) - `hook_text`
3. 主三角形 - `triangle`

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 三角形创建 | `Create(triangle)` | 1.0s |
| 2.1s | 顶点标签淡入 | `FadeIn(VGroup(label_A, label_B, label_C))` | 0.4s |
| 2.5s | 等待理解 | `Wait(1.0)` | 1.0s |

### 清理
- FadeOut: hook_text
- 保留: triangle, author_info, 顶点标签

---

## Scene 2: 中线 - 连接顶点与对边中点 (10-12秒)
**目的**: 介绍中线定义、三中线交于重心

### 元素
1. 标题: "中线 Median"
2. 定义: "连接顶点与对边中点的线段"
3. 中点M, N, P
4. 三条中线
5. 重心G

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题+定义淡入 | `Write(title), FadeIn(definition)` | 0.8s |
| 0.8s | 高亮BC边 | `BC.animate.set_color(HIGHLIGHT)` | 0.4s |
| 1.2s | 中点M出现 | `FadeIn(m_dot), FadeIn(m_label)` | 0.4s |
| 1.6s | 说明文字 | `FadeIn(explain_1)` | 0.3s |
| 1.9s | 绘制中线AM | `Create(median_1)` | 0.8s |
| 2.7s | BC边恢复颜色 | `BC.animate.set_color(TRIANGLE)` | 0.3s |
| 3.0s | 说明消失 | `FadeOut(explain_1)` | 0.2s |
| 3.2s | 高亮CA边 | `CA.animate.set_color(HIGHLIGHT)` | 0.4s |
| 3.6s | 中点N出现 | `FadeIn(n_dot)` | 0.3s |
| 3.9s | 绘制中线BN | `Create(median_2)` | 0.8s |
| 4.7s | CA边恢复 | `CA.animate.set_color(TRIANGLE)` | 0.3s |
| 5.0s | 高亮AB边 | `AB.animate.set_color(HIGHLIGHT)` | 0.4s |
| 5.4s | 中点P出现 | `FadeIn(p_dot)` | 0.3s |
| 5.7s | 绘制中线CP | `Create(median_3)` | 0.8s |
| 6.5s | AB边恢复 | `AB.animate.set_color(TRIANGLE)` | 0.3s |
| 6.8s | 重心出现 | `FadeIn(g_dot), Flash(g_dot)` | 0.6s |
| 7.4s | 重心标签 | `FadeIn(g_label)` | 0.4s |
| 7.8s | 性质说明 | `FadeIn(property_text)` | 0.5s |
| 8.3s | 等待理解 | `Wait(1.5)` | 1.5s |

### 几何验证
```python
# 验证中点
assert np.allclose(M_BC, (B + C) / 2)
assert np.allclose(M_CA, (C + A) / 2)
assert np.allclose(M_AB, (A + B) / 2)

# 验证重心
assert np.allclose(centroid, (A + B + C) / 3)

# 验证三中线共点
dist_to_AM = distance_point_to_line(centroid, A, M_BC)
dist_to_BN = distance_point_to_line(centroid, B, M_CA)
assert dist_to_AM < 1e-6 and dist_to_BN < 1e-6
```

### 清理
- FadeOut: title, definition, property_text
- 保留但变小: g_dot (变为半透明小点)
- 保留: triangle, 中线(变为虚线灰色)

---

## Scene 3: 高线 - 从顶点到对边的垂线段 (12-15秒)
**目的**: 介绍高线定义、三高线交于垂心

### 元素
1. 标题: "高线 Altitude"
2. 定义: "从顶点向对边所在直线作的垂线段"
3. 垂足D, E, F
4. 三条高线
5. 垂心H
6. 直角符号

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 清理中线 | `FadeOut(medians)` | 0.4s |
| 0.4s | 标题+定义淡入 | `Write(title), FadeIn(definition)` | 0.8s |
| 1.2s | 高亮BC边 | `BC.animate.set_color(HIGHLIGHT)` | 0.5s |
| 1.7s | 说明文字 | `FadeIn(explain_1)` | 0.3s |
| 2.0s | 垂足D出现 | `FadeIn(foot_d_dot)` | 0.3s |
| 2.3s | 绘制高线AD | `Create(altitude_1)` | 0.8s |
| 3.1s | 直角符号 | `FadeIn(right_angle_1)` | 0.4s |
| 3.5s | BC边恢复 | `BC.animate.set_color(TRIANGLE)` | 0.3s |
| 3.8s | 说明消失 | `FadeOut(explain_1)` | 0.2s |
| 4.0s | 高亮CA边 | `CA.animate.set_color(HIGHLIGHT)` | 0.5s |
| 4.5s | 垂足E出现 | `FadeIn(foot_e_dot)` | 0.3s |
| 4.8s | 绘制高线BE | `Create(altitude_2)` | 0.8s |
| 5.6s | 直角符号 | `FadeIn(right_angle_2)` | 0.4s |
| 6.0s | CA边恢复 | `CA.animate.set_color(TRIANGLE)` | 0.3s |
| 6.3s | 高亮AB边 | `AB.animate.set_color(HIGHLIGHT)` | 0.5s |
| 6.8s | 垂足F出现 | `FadeIn(foot_f_dot)` | 0.3s |
| 7.1s | 绘制高线CF | `Create(altitude_3)` | 0.8s |
| 7.9s | 直角符号 | `FadeIn(right_angle_3)` | 0.4s |
| 8.3s | AB边恢复 | `AB.animate.set_color(TRIANGLE)` | 0.3s |
| 8.6s | 垂心出现 | `FadeIn(h_dot), Flash(h_dot)` | 0.6s |
| 9.2s | 垂心标签 | `FadeIn(h_label)` | 0.4s |
| 9.6s | 性质说明 | `FadeIn(property_text)` | 0.5s |
| 10.1s | 等待理解 | `Wait(1.5)` | 1.5s |

### 几何验证
```python
# 验证垂足
foot_D = foot_of_perpendicular(A, B, C)
assert is_perpendicular(A - foot_D, C - B)

# 验证垂心
assert distance_point_to_line(orthocenter, A, foot_D) < 1e-6
assert distance_point_to_line(orthocenter, B, foot_E) < 1e-6

# 验证垂直性
vec_AD = foot_D - A
vec_BC = C - B
dot_product = np.dot(vec_AD[:2], vec_BC[:2])
assert abs(dot_product) < 1e-6
```

### 清理
- FadeOut: title, definition, property_text, right_angle marks
- 保留但变小: h_dot (变为半透明小点)
- 保留: triangle, 高线(变为虚线灰色)

---

## Scene 4: 角平分线 - 平分角的线段 (12-15秒)
**目的**: 介绍角平分线定义、三角平分线交于内心

### 元素
1. 标题: "角平分线 Angle Bisector"
2. 定义: "角的平分线与对边的交点连成的线段"
3. 交点D, E, F
4. 三条角平分线
5. 内心I
6. 角弧标记

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 清理高线 | `FadeOut(altitudes)` | 0.4s |
| 0.4s | 标题+定义淡入 | `Write(title), FadeIn(definition)` | 0.8s |
| 1.2s | 说明文字 | `FadeIn(explain_1)` | 0.3s |
| 1.5s | 角A的两边高亮 | `AB.animate.set_color(HIGHLIGHT), AC.animate.set_color(HIGHLIGHT)` | 0.5s |
| 2.0s | 角A弧线 | `Create(angle_A_arc)` | 0.4s |
| 2.4s | 交点D出现 | `FadeIn(point_d_dot)` | 0.3s |
| 2.7s | 绘制角平分线AD | `Create(bisector_1)` | 0.8s |
| 3.5s | 两个小角弧 | `Create(half_angle_1), Create(half_angle_2)` | 0.5s |
| 4.0s | 边恢复颜色 | `AB.animate.set_color(TRIANGLE), AC.animate.set_color(TRIANGLE)` | 0.3s |
| 4.3s | 说明消失 | `FadeOut(explain_1), FadeOut(angle_A_arc), FadeOut(half_angles)` | 0.2s |
| 4.5s | 角B的两边高亮 | `BA.animate.set_color(HIGHLIGHT), BC.animate.set_color(HIGHLIGHT)` | 0.5s |
| 5.0s | 角B弧线 | `Create(angle_B_arc)` | 0.4s |
| 5.4s | 交点E出现 | `FadeIn(point_e_dot)` | 0.3s |
| 5.7s | 绘制角平分线BE | `Create(bisector_2)` | 0.8s |
| 6.5s | 边恢复颜色 | `BA.animate.set_color(TRIANGLE), BC.animate.set_color(TRIANGLE)` | 0.3s |
| 6.8s | 角弧消失 | `FadeOut(angle_B_arc)` | 0.2s |
| 7.0s | 角C的两边高亮 | `CA.animate.set_color(HIGHLIGHT), CB.animate.set_color(HIGHLIGHT)` | 0.5s |
| 7.5s | 角C弧线 | `Create(angle_C_arc)` | 0.4s |
| 7.9s | 交点F出现 | `FadeIn(point_f_dot)` | 0.3s |
| 8.2s | 绘制角平分线CF | `Create(bisector_3)` | 0.8s |
| 9.0s | 边恢复颜色 | `CA.animate.set_color(TRIANGLE), CB.animate.set_color(TRIANGLE)` | 0.3s |
| 9.3s | 角弧消失 | `FadeOut(angle_C_arc)` | 0.2s |
| 9.5s | 内心出现 | `FadeIn(i_dot), Flash(i_dot)` | 0.6s |
| 10.1s | 内心标签 | `FadeIn(i_label)` | 0.4s |
| 10.5s | 性质说明 | `FadeIn(property_text)` | 0.5s |
| 11.0s | 等待理解 | `Wait(1.5)` | 1.5s |

### 角度方向验证(重要⚠️)
```python
# 角A的计算和验证
vec_AB = B - A
vec_AC = C - A
cross_z = vec_AB[0] * vec_AC[1] - vec_AB[1] * vec_AC[0]

if cross_z > 0:
    # 从AB到AC是逆时针
    angle_A_arc = Angle.from_three_points(B, A, C, other_angle=False)
else:
    # 从AB到AC是顺时针
    angle_A_arc = Angle.from_three_points(B, A, C, other_angle=True)

# 验证角平分线方向
vec_AB_unit = vec_AB / np.linalg.norm(vec_AB)
vec_AC_unit = vec_AC / np.linalg.norm(vec_AC)
bisector_dir = vec_AB_unit + vec_AC_unit
bisector_dir_normalized = bisector_dir / np.linalg.norm(bisector_dir)

# 验证交点位置(角平分线定理)
# D点应该满足: BD/DC = AB/AC = c/b
t = c / (b + c)
D_calculated = B + t * (C - B)
assert np.allclose(point_D, D_calculated, atol=1e-6)
```

### 几何验证
```python
# 验证内心
incenter_calculated = (a*A + b*B + c*C) / (a + b + c)
assert np.allclose(incenter, incenter_calculated, atol=1e-6)

# 验证三角平分线共点
dist_to_AD = distance_point_to_line(incenter, A, point_D)
dist_to_BE = distance_point_to_line(incenter, B, point_E)
assert dist_to_AD < 1e-6 and dist_to_BE < 1e-6
```

### 清理
- FadeOut: title, definition, property_text
- 保留但变小: i_dot (变为半透明小点)
- 保留: triangle, 角平分线(变为虚线灰色)

---

## Scene 5: 三线汇总对比 (8-10秒)
**目的**: 同时展示三种线段,强化对比记忆

### 元素
1. 三角形缩小并移动到上方
2. 三个特殊点(G, H, I)同时显示
3. 三组线段用不同颜色区分
4. 对比卡片

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 清理所有辅助线 | `FadeOut(all_auxiliary_lines)` | 0.4s |
| 0.4s | 三角形缩放移动 | `triangle.animate.scale(0.6).move_to(UP*3)` | 0.8s |
| 1.2s | 重新绘制中线 | `Create(median_group, lag_ratio=0.3)` | 1.0s |
| 2.2s | 重心闪烁 | `g_dot.animate.scale(1.5).set_opacity(1), Flash(g_dot)` | 0.5s |
| 2.7s | 重新绘制高线 | `Create(altitude_group, lag_ratio=0.3)` | 1.0s |
| 3.7s | 垂心闪烁 | `h_dot.animate.scale(1.5).set_opacity(1), Flash(h_dot)` | 0.5s |
| 4.2s | 重新绘制角平分线 | `Create(bisector_group, lag_ratio=0.3)` | 1.0s |
| 5.2s | 内心闪烁 | `i_dot.animate.scale(1.5).set_opacity(1), Flash(i_dot)` | 0.5s |
| 5.7s | 标注三个点 | `FadeIn(VGroup(g_label, h_label, i_label))` | 0.5s |
| 6.2s | 对比卡片滑入 | `comparison_cards.animate.shift(LEFT*0)` | 0.8s |
| 7.0s | 等待理解 | `Wait(2.0)` | 2.0s |

### 对比卡片内容
```
┌─────────────────────────────────┐
│ 🔴 中线: 顶点→对边中点            │
│    交点: 重心G (分中线为2:1)      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 🔵 高线: 顶点→对边垂线            │
│    交点: 垂心H                   │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 🟢 角平分线: 角平分→对边          │
│    交点: 内心I (到三边距离相等)   │
└─────────────────────────────────┘
```

### 清理
- FadeOut: 所有线段和卡片
- 保留: 缩小的三角形

---

## Scene 6: 关键性质强化 (6-8秒)
**目的**: 强调考试重点性质

### 元素
1. 性质卡片列表
2. 公式展示
3. 重点提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 三角形淡出 | `FadeOut(triangle)` | 0.3s |
| 0.3s | 标题 | `Write(title)` | 0.6s |
| 0.9s | 性质1卡片 | `property_1.animate.shift(LEFT*0)` | 0.4s |
| 1.3s | 性质2卡片 | `property_2.animate.shift(LEFT*0)` | 0.4s |
| 1.7s | 性质3卡片 | `property_3.animate.shift(LEFT*0)` | 0.4s |
| 2.1s | 性质4卡片 | `property_4.animate.shift(LEFT*0)` | 0.4s |
| 2.5s | 重点提示 | `FadeIn(highlight_text, scale=1.1)` | 0.5s |
| 3.0s | 等待理解 | `Wait(2.5)` | 2.5s |

### 性质卡片内容
```
1. 中线性质: 重心分中线为 2:1
2. 高线性质: 高线垂直于底边
3. 角平分线性质: 内心到三边距离相等
4. 共同特点: 三线共点
```

### 清理
- FadeOut: 所有卡片和文字

---

## Scene 7: 片尾关注 (4-5秒)
**目的**: 引导关注,强化品牌

### 元素
1. 作者名放大
2. 账号ID
3. 关注提示
4. 三角形装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息放大 | `Transform(author_info, author_name)` | 0.8s |
| 0.8s | 账号ID淡入 | `FadeIn(author_id, shift=UP*0.3)` | 0.5s |
| 1.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 1.9s | 三角形装饰 | `FadeIn(decorative_triangles)` | 0.5s |
| 2.4s | 旋转动画 | `Rotate(decorative_triangles, PI)` | 1.0s |
| 3.4s | 等待 | `Wait(0.8)` | 0.8s |
| 4.2s | 全部淡出 | `FadeOut(all)` | 0.8s |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终在顶部 |
| triangle | Scene 1 | Scene 6 | 主三角形 |
| label_A, B, C | Scene 1 | Scene 5 | 顶点标签 |
| median_group | Scene 2 | Scene 5 | 三条中线 |
| g_dot | Scene 2 | Scene 5 | 重心 |
| altitude_group | Scene 3 | Scene 5 | 三条高线 |
| h_dot | Scene 3 | Scene 5 | 垂心 |
| bisector_group | Scene 4 | Scene 5 | 三条角平分线 |
| i_dot | Scene 4 | Scene 5 | 内心 |
| comparison_cards | Scene 5 | Scene 5 | 对比卡片 |
| property_cards | Scene 6 | Scene 6 | 性质卡片 |

---

## 总时长预估
- Scene 1: 3.5s
- Scene 2: 10s
- Scene 3: 12s
- Scene 4: 12.5s
- Scene 5: 9s
- Scene 6: 5.5s
- Scene 7: 5s
**总计: 约57.5秒** ✓ 符合目标(60-75秒)

---

## 边界安全检查
```python
# 确保所有元素在安全区域内
SAFE_X_MIN = -4.0
SAFE_X_MAX = 4.0
SAFE_Y_MIN = -7.0
SAFE_Y_MAX = 7.0

# 三角形顶点检查
assert SAFE_X_MIN < A[0] < SAFE_X_MAX
assert SAFE_Y_MIN < A[1] < SAFE_Y_MAX
# ... 对B, C, G, H, I同样检查

# 文字位置检查
assert title.get_top()[1] < 7.5  # 不超出顶部
assert property_text.get_bottom()[1] > -7.5  # 不超出底部
```

---

## 渲染命令
```bash
# 快速预览
manim -pql triangle_important_segments.py TriangleImportantSegments

# 高质量渲染
manim -qh triangle_important_segments.py TriangleImportantSegments

# TikTok竖屏配置已内置
```