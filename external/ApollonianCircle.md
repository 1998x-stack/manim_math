# 阿波罗尼斯圆 - 动画分镜脚本

## 元信息
- 目标时长: 80-90 秒
- 场景数量: 7 个
- 难度等级: 中高
- 核心概念: 到两定点距离之比为定值的点的轨迹是圆

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 主圆
COLOR_SECONDARY = "#e74c3c"     # 红色 - 辅助线
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_POINT_A = "#2ecc71"       # 绿色 - 点A
COLOR_POINT_B = "#9b59b6"       # 紫色 - 点B
COLOR_POINT_P = "#f39c12"       # 橙色 - 动点P
COLOR_INTERNAL = "#1abc9c"      # 青色 - 内分点C
COLOR_EXTERNAL = "#e67e22"      # 深橙 - 外分点D
```

## 几何预计算清单

### 基准参数
```python
SCALE = 1.2
OFFSET = UP * 1.0
k_ratio = 2  # PA/PB = 2
```

### 主要点位
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 点A | 手动定义 | self.A | 左侧定点 |
| 点B | 手动定义 | self.B | 右侧定点 |
| 内分点C | C = A + (k/(k+1))*(B-A) | self.C | AC:CB = 2:1 |
| 外分点D | D = A + (k/(k-1))*(B-A) | self.D | AD:DB = 2:1 |
| 圆心O | O = (C+D)/2 | self.O | CD的中点 |
| 半径R | R = \|OC\| = \|OD\| | self.R | 阿波罗尼斯圆半径 |

### 辅助点（用于演示）
| 元素 | 计算公式 | 说明 |
|------|---------|------|
| 点M | 辅助射线上的点 | 用于作平行线找内分点 |
| 点N | 辅助射线上的点 | 用于作平行线找外分点 |
| 点P1-P8 | 圆上8个均匀分布的点 | 验证PA/PB = 2 |

### 验证计算
```python
# 验证内分点
AC = np.linalg.norm(self.C - self.A)
CB = np.linalg.norm(self.B - self.C)
assert abs(AC/CB - k_ratio) < 1e-6

# 验证外分点
AD = np.linalg.norm(self.D - self.A)
DB = np.linalg.norm(self.B - self.D)
assert abs(AD/DB - k_ratio) < 1e-6

# 验证圆心
assert abs(np.linalg.norm(self.O - self.C) - self.R) < 1e-6
assert abs(np.linalg.norm(self.O - self.D) - self.R) < 1e-6

# 验证圆上点满足比例
for P in points_on_circle:
    PA = np.linalg.norm(P - self.A)
    PB = np.linalg.norm(P - self.B)
    assert abs(PA/PB - k_ratio) < 1e-3
```

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题："如果你到两个点的距离之比永远是2:1，你会画出什么轨迹?"
3. 两个点A和B闪烁

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写（分两行） | `Write(hook_line1)`, `Write(hook_line2)` | 1.2s |
| 1.5s | 点A淡入+闪光 | `FadeIn(dot_A)`, `Flash(dot_A)` | 0.6s |
| 2.1s | 点B淡入+闪光 | `FadeIn(dot_B)`, `Flash(dot_B)` | 0.6s |
| 2.7s | 标签AB出现 | `FadeIn(label_A)`, `FadeIn(label_B)` | 0.4s |
| 3.1s | 问号出现 | `Write(question_mark)` | 0.5s |
| 3.6s | 等待思考 | `Wait()` | 1.4s |

### 坐标布局
```
A: (-2.5, 0, 0) * SCALE + OFFSET
B: (2.5, 0, 0) * SCALE + OFFSET
hook_line1: UP * 6
hook_line2: UP * 5.3
question_mark: DOWN * 4
```

### 清理
- FadeOut: hook_line1, hook_line2, question_mark
- 保留: dot_A, dot_B, label_A, label_B, author

---

## Scene 2: 揭示答案 - 圆! (5-10秒)

**目的**: 揭示轨迹是圆，引发惊叹

### 元素
1. 神秘的圆逐渐绘制
2. "答案: 这是一个圆!" 文字
3. 圆上一个动点P，显示PA和PB的长度

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 5.0s | 标题淡入："阿波罗尼斯圆" | `Write(title)` | 0.8s |
| 5.8s | 圆逐渐绘制 | `Create(apollonian_circle)` | 2.0s |
| 7.8s | 答案文字闪现 | `FadeIn(answer_text, scale=1.2)` | 0.5s |
| 8.3s | 动点P出现在圆上 | `FadeIn(dot_P)` | 0.3s |
| 8.6s | PA和PB线段绘制 | `Create(line_PA)`, `Create(line_PB)` | 0.6s |
| 9.2s | 长度标签显示 | `FadeIn(length_PA)`, `FadeIn(length_PB)` | 0.4s |
| 9.6s | 比值公式显示 | `Write(ratio_formula)` | 0.5s |
| 10.1s | 等待 | `Wait()` | 0.9s |

### 关键计算
```python
# 圆心和半径（精确计算）
self.O = (self.C + self.D) / 2
self.R = np.linalg.norm(self.O - self.C)

# 圆上一个示例点（30度位置）
angle_sample = 30 * DEGREES
P_sample = self.O + self.R * np.array([np.cos(angle_sample), np.sin(angle_sample), 0])

# 验证比例
PA_length = np.linalg.norm(P_sample - self.A)
PB_length = np.linalg.norm(P_sample - self.B)
# assert abs(PA_length / PB_length - 2.0) < 0.05
```

### 坐标布局
```
title: UP * 5.5
answer_text: UP * 4.5
ratio_formula: DOWN * 4.5 (显示 PA/PB = 2)
```

### 清理
- FadeOut: title, answer_text, dot_P, line_PA, line_PB, length_PA, length_PB, ratio_formula
- 保留: apollonian_circle, dot_A, dot_B, label_A, label_B

---

## Scene 3: 尺规作图 - 引言 (10-15秒)

**目的**: 引入构造方法

### 元素
1. 问题文字："如何用尺规画出这个圆?"
2. 提示："关键: 找到圆与直线AB的两个交点"

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 10.0s | 问题文字书写 | `Write(question_text)` | 0.8s |
| 10.8s | 直线AB绘制并高亮 | `Create(line_AB_full)`, 设置为YELLOW | 1.0s |
| 11.8s | 圆与AB交点闪烁 | `Flash(self.C)`, `Flash(self.D)` | 0.6s |
| 12.4s | 提示文字淡入 | `FadeIn(hint_text)` | 0.6s |
| 13.0s | C和D点放大高亮 | `dot_C.animate.scale(1.5)`, 类似D | 0.5s |
| 13.5s | 说明文字 | `Write(explanation)`: "CD是直径!" | 0.8s |
| 14.3s | 等待 | `Wait()` | 0.7s |

### 坐标布局
```
question_text: UP * 5.5
hint_text: UP * 4.5
explanation: DOWN * 4
```

### 清理
- FadeOut: question_text, hint_text, explanation
- 保留: apollonian_circle, line_AB_full, dot_A, dot_B
- 圆变为虚线，变淡（作为参考）

---

## Scene 4: 寻找内分点C (15-35秒)

**目的**: 详细演示如何用尺规找内分点（AC:CB = 2:1）

### 子步骤

#### 4.1 过A作辅助射线 (15-18秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 15.0s | 标题："步骤1: 寻找内分点C" | `Write(step_title_1)` | 0.6s |
| 15.6s | 说明："在AB内，AC:CB = 2:1" | `FadeIn(explanation_1)` | 0.5s |
| 16.1s | 过A作向上射线 | `Create(ray_from_A)` | 0.8s |
| 16.9s | 说明文字："作辅助射线" | `FadeIn(aux_text)` | 0.4s |
| 17.3s | 等待 | `Wait()` | 0.7s |

#### 4.2 在射线上截取AM=MN (18-22秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 18.0s | 点M出现 | `FadeIn(dot_M)` | 0.3s |
| 18.3s | 标签M | `FadeIn(label_M)` | 0.2s |
| 18.5s | AM线段高亮 | `Create(segment_AM, color=YELLOW)` | 0.5s |
| 19.0s | 点N出现（距离相同） | `FadeIn(dot_N)` | 0.3s |
| 19.3s | 标签N | `FadeIn(label_N)` | 0.2s |
| 19.5s | MN线段高亮 | `Create(segment_MN, color=YELLOW)` | 0.5s |
| 20.0s | 说明："AM = MN" | `Write(equal_text)` | 0.5s |
| 20.5s | 等待 | `Wait()` | 1.5s |

**几何计算**:
```python
# 辅助射线方向（向上偏45度）
ray_direction = np.array([0.5, 1, 0])
ray_direction = ray_direction / np.linalg.norm(ray_direction)

# 单位长度（基于AB长度）
unit_length = np.linalg.norm(self.B - self.A) / 4

# M点: 沿射线距离unit_length
M = self.A + ray_direction * unit_length

# N点: 沿射线距离2*unit_length
N = self.A + ray_direction * (2 * unit_length)
```

#### 4.3 连接NB (22-24秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 22.0s | 连接NB | `Create(line_NB)` | 0.8s |
| 22.8s | 等待 | `Wait()` | 1.2s |

#### 4.4 过M作NB的平行线 (24-28秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 24.0s | 说明："过M作NB的平行线" | `Write(parallel_text)` | 0.7s |
| 24.7s | 虚线平行线绘制 | `Create(parallel_line, dashed)` | 1.0s |
| 25.7s | 平行符号标记 | `FadeIn(parallel_marks)` | 0.4s |
| 26.1s | 等待 | `Wait()` | 1.9s |

**几何计算**:
```python
# NB方向向量
vec_NB = self.B - N
vec_NB_normalized = vec_NB / np.linalg.norm(vec_NB)

# 平行线: M点 + t * vec_NB
# 与AB的交点C
# 使用参数方程求解
```

#### 4.5 交点即为C (28-32秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 28.0s | 交点C闪烁 | `Flash(dot_C, color=COLOR_INTERNAL)` | 0.5s |
| 28.5s | C点放大高亮 | `dot_C.animate.scale(2).set_color(COLOR_INTERNAL)` | 0.6s |
| 29.1s | 标签C | `FadeIn(label_C)` | 0.3s |
| 29.4s | 标注AC和CB | `FadeIn(brace_AC)`, `FadeIn(brace_CB)` | 0.6s |
| 30.0s | 比例文字："AC:CB = 2:1" | `Write(ratio_AC_CB)` | 0.7s |
| 30.7s | 验证勾 | `FadeIn(checkmark)` | 0.3s |
| 31.0s | 等待 | `Wait()` | 1.0s |

**精确计算内分点C**:
```python
# 使用内分点公式
k = 2
self.C = self.A + (k / (k + 1)) * (self.B - self.A)
# C = A + (2/3)*(B-A)

# 验证
AC = np.linalg.norm(self.C - self.A)
CB = np.linalg.norm(self.B - self.C)
assert abs(AC / CB - 2.0) < 1e-6
```

#### 4.6 清理辅助线 (32-35秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 32.0s | 辅助线淡出 | `FadeOut(ray, M, N, line_NB, parallel_line, ...)` | 1.0s |
| 33.0s | C点保持高亮 | - | - |
| 33.0s | 等待 | `Wait()` | 2.0s |

### 清理
- FadeOut: 所有辅助元素
- 保留: dot_A, dot_B, dot_C, line_AB, label_A, label_B, label_C

---

## Scene 5: 寻找外分点D (35-55秒)

**目的**: 演示如何用尺规找外分点（AD:DB = 2:1, D在AB外侧）

### 子步骤

#### 5.1 引入外分点概念 (35-38秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 35.0s | 标题："步骤2: 寻找外分点D" | `Write(step_title_2)` | 0.6s |
| 35.6s | 说明："在AB外，AD:DB = 2:1" | `FadeIn(explanation_2)` | 0.6s |
| 36.2s | AB向右延长 | `Create(extended_AB)` | 0.8s |
| 37.0s | 等待 | `Wait()` | 1.0s |

#### 5.2 在射线上截取AN=NQ (38-42秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 38.0s | 说明："在之前射线上继续截取" | `FadeIn(continue_text)` | 0.5s |
| 38.5s | 点M、N重新显示 | `FadeIn(dot_M)`, `FadeIn(dot_N)` | 0.3s |
| 38.8s | 点Q出现（第三段） | `FadeIn(dot_Q)` | 0.3s |
| 39.1s | 标签Q | `FadeIn(label_Q)` | 0.2s |
| 39.3s | NQ线段高亮 | `Create(segment_NQ, color=YELLOW)` | 0.5s |
| 39.8s | 说明："NQ = AM = MN" | `Write(equal_text_2)` | 0.6s |
| 40.4s | 等待 | `Wait()` | 1.6s |

**几何计算**:
```python
# Q点: 沿射线距离3*unit_length
Q = self.A + ray_direction * (3 * unit_length)
```

#### 5.3 连接QB (42-44秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 42.0s | 连接QB | `Create(line_QB)` | 0.8s |
| 42.8s | 等待 | `Wait()` | 1.2s |

#### 5.4 过N作QB的平行线 (44-48秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 44.0s | 说明："过N作QB的平行线" | `Write(parallel_text_2)` | 0.7s |
| 44.7s | 虚线平行线绘制 | `Create(parallel_line_2, dashed)` | 1.0s |
| 45.7s | 平行符号标记 | `FadeIn(parallel_marks_2)` | 0.4s |
| 46.1s | 等待 | `Wait()` | 1.9s |

**几何计算**:
```python
# QB方向向量
vec_QB = self.B - Q
vec_QB_normalized = vec_QB / np.linalg.norm(vec_QB)

# 平行线: N点 + s * vec_QB
# 与AB延长线的交点D
```

#### 5.5 交点即为D (48-52秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 48.0s | 交点D闪烁 | `Flash(dot_D, color=COLOR_EXTERNAL)` | 0.5s |
| 48.5s | D点放大高亮 | `dot_D.animate.scale(2).set_color(COLOR_EXTERNAL)` | 0.6s |
| 49.1s | 标签D | `FadeIn(label_D)` | 0.3s |
| 49.4s | 标注AD和DB | `FadeIn(brace_AD)`, `FadeIn(brace_DB)` | 0.6s |
| 50.0s | 比例文字："AD:DB = 2:1" | `Write(ratio_AD_DB)` | 0.7s |
| 50.7s | 验证勾 | `FadeIn(checkmark_2)` | 0.3s |
| 51.0s | 等待 | `Wait()` | 1.0s |

**精确计算外分点D**:
```python
# 使用外分点公式
k = 2
self.D = self.A + (k / (k - 1)) * (self.B - self.A)
# D = A + 2*(B-A) = 2*B - A

# 验证
AD = np.linalg.norm(self.D - self.A)
DB = np.linalg.norm(self.B - self.D)
assert abs(AD / DB - 2.0) < 1e-6
```

#### 5.6 清理辅助线 (52-55秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 52.0s | 辅助线淡出 | `FadeOut(ray, M, N, Q, line_QB, parallel_line_2, ...)` | 1.0s |
| 53.0s | C和D点保持高亮 | - | - |
| 53.0s | 等待 | `Wait()` | 2.0s |

### 清理
- FadeOut: 所有辅助元素
- 保留: dot_A, dot_B, dot_C, dot_D, line_AB, extended_AB

---

## Scene 6: 确定圆 (55-70秒)

**目的**: 用C和D确定圆心和半径，完成构造

### 子步骤

#### 6.1 CD是直径 (55-58秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 55.0s | 标题："步骤3: 确定圆" | `Write(step_title_3)` | 0.6s |
| 55.6s | CD线段高亮 | `Create(line_CD, color=COLOR_HIGHLIGHT)` | 0.8s |
| 56.4s | 说明："CD是直径!" | `Write(diameter_text)` | 0.6s |
| 57.0s | 等待 | `Wait()` | 1.0s |

#### 6.2 取CD中点为圆心O (58-62秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 58.0s | 说明："取CD的中点" | `FadeIn(midpoint_text)` | 0.5s |
| 58.5s | 中点O闪烁出现 | `Flash(dot_O)`, `FadeIn(dot_O)` | 0.6s |
| 59.1s | 标签O | `FadeIn(label_O)` | 0.3s |
| 59.4s | 说明："这就是圆心!" | `Write(center_text)` | 0.6s |
| 60.0s | 等待 | `Wait()` | 2.0s |

**精确计算圆心**:
```python
self.O = (self.C + self.D) / 2

# 验证: O应该在AB上
# 因为C和D都在AB上，所以O也在AB上
```

#### 6.3 以OC或OD为半径画圆 (62-67秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 62.0s | 半径OC绘制 | `Create(radius_OC, color=COLOR_PRIMARY)` | 0.6s |
| 62.6s | 半径OD绘制 | `Create(radius_OD, color=COLOR_PRIMARY)` | 0.6s |
| 63.2s | 说明："半径 R = OC = OD" | `Write(radius_text)` | 0.7s |
| 63.9s | 圆逐渐绘制（实线） | `Create(apollonian_circle_final)` | 2.5s |
| 66.4s | 闪光效果 | `Flash(dot_O, line_length=1.5)` | 0.6s |
| 67.0s | 等待 | `Wait()` | 3.0s |

**精确计算半径**:
```python
self.R = np.linalg.norm(self.O - self.C)

# 验证
R_check = np.linalg.norm(self.O - self.D)
assert abs(self.R - R_check) < 1e-6
```

### 清理
- FadeOut: step_title_3, diameter_text, midpoint_text, center_text, radius_text
- 保留: apollonian_circle_final, dot_A, dot_B, dot_C, dot_D, dot_O

---

## Scene 7: 验证与总结 (70-85秒)

**目的**: 验证圆上任意点满足PA/PB=2，总结性质

### 子步骤

#### 7.1 圆上多个点的验证 (70-76秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 70.0s | 标题："验证: 圆上所有点都满足 PA/PB = 2" | `Write(verify_title)` | 0.8s |
| 70.8s | 8个点依次出现在圆上 | `FadeIn(dots_on_circle, lag_ratio=0.1)` | 1.2s |
| 72.0s | 选一个点P高亮 | `dot_P.animate.scale(2).set_color(COLOR_POINT_P)` | 0.4s |
| 72.4s | PA和PB线段绘制 | `Create(line_PA)`, `Create(line_PB)` | 0.6s |
| 73.0s | 长度数值显示 | `FadeIn(length_PA_val)`, `FadeIn(length_PB_val)` | 0.5s |
| 73.5s | 比值显示 | `Write(ratio_val)`: "PA/PB = 2.00 ✓" | 0.7s |
| 74.2s | P点沿圆移动，数值实时更新 | `UpdateFromFunc` + `ValueTracker` | 1.5s |
| 75.7s | 等待 | `Wait()` | 0.3s |

**圆上8个点的计算**:
```python
angles = [i * 45 * DEGREES for i in range(8)]
points_on_circle = [
    self.O + self.R * np.array([np.cos(angle), np.sin(angle), 0])
    for angle in angles
]

# 验证每个点
for P in points_on_circle:
    PA = np.linalg.norm(P - self.A)
    PB = np.linalg.norm(P - self.B)
    ratio = PA / PB
    assert abs(ratio - 2.0) < 0.05  # 允许小误差
```

#### 7.2 性质总结 (76-82秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 76.0s | 清理验证元素 | `FadeOut(dots, lines, values)` | 0.5s |
| 76.5s | 总结卡片1："定义: PA/PB = k (常数)" | `FadeIn(summary_1)` | 0.7s |
| 77.2s | 总结卡片2："轨迹是圆" | `FadeIn(summary_2)` | 0.7s |
| 77.9s | 总结卡片3："内外分点法构造" | `FadeIn(summary_3)` | 0.7s |
| 78.6s | 总结卡片4："CD是直径" | `FadeIn(summary_4)` | 0.7s |
| 79.3s | 标题："阿波罗尼斯圆的美!" | `Write(beauty_title, color=GOLD)` | 0.8s |
| 80.1s | 等待 | `Wait()` | 1.9s |

### 坐标布局
```
verify_title: UP * 5.5
summary_1: UP * 2
summary_2: UP * 0.5
summary_3: DOWN * 1
summary_4: DOWN * 2.5
beauty_title: DOWN * 4.5
```

#### 7.3 片尾 (82-85秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 82.0s | 所有元素淡出 | `FadeOut(VGroup(*all_objects))` | 1.0s |
| 83.0s | 作者信息放大居中 | `author.animate.scale(2).move_to(ORIGIN)` | 0.8s |
| 83.8s | 关注提示 | `FadeIn(follow_text)`: "关注我，学更多几何!" | 0.5s |
| 84.3s | 等待 | `Wait()` | 0.7s |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 类型 | 备注 |
|------|---------|---------|------|------|
| author | Scene 1 | Scene 7结尾 | Text | 作者信息，全程显示 |
| dot_A | Scene 1 | Scene 7 | Dot | 点A，全程显示 |
| dot_B | Scene 1 | Scene 7 | Dot | 点B，全程显示 |
| label_A | Scene 1 | Scene 7 | Text | 标签A |
| label_B | Scene 1 | Scene 7 | Text | 标签B |
| apollonian_circle | Scene 2 | Scene 6 | Circle | 初始圆（虚线） |
| apollonian_circle_final | Scene 6 | Scene 7 | Circle | 最终圆（实线） |
| dot_C | Scene 4 | Scene 7 | Dot | 内分点C |
| dot_D | Scene 5 | Scene 7 | Dot | 外分点D |
| dot_O | Scene 6 | Scene 7 | Dot | 圆心O |
| ray_from_A | Scene 4 | Scene 4 | Line | 辅助射线，临时 |
| dot_M | Scene 4 | Scene 4 | Dot | 辅助点M，临时 |
| dot_N | Scene 4, 5 | Scene 5 | Dot | 辅助点N，临时 |
| dot_Q | Scene 5 | Scene 5 | Dot | 辅助点Q，临时 |
| line_NB | Scene 4 | Scene 4 | Line | 辅助线NB，临时 |
| line_QB | Scene 5 | Scene 5 | Line | 辅助线QB，临时 |
| parallel_line | Scene 4 | Scene 4 | DashedLine | 平行线1，临时 |
| parallel_line_2 | Scene 5 | Scene 5 | DashedLine | 平行线2，临时 |
| line_CD | Scene 6 | Scene 6 | Line | CD直径线段 |
| radius_OC | Scene 6 | Scene 6 | Line | 半径OC |
| radius_OD | Scene 6 | Scene 6 | Line | 半径OD |
| dots_on_circle | Scene 7 | Scene 7 | VGroup | 验证用的8个点 |

---

## 特殊注意事项

### 角度处理
- 所有角度标记都需要精确计算quadrant参数
- 直角符号使用RightAngle或elbow=True

### 长度一致性
- AC:CB = 2:1 必须精确验证
- AD:DB = 2:1 必须精确验证
- 圆上所有点PA/PB的比值误差 < 0.05

### 边界检查
- 所有元素保持在 x∈[-4,4], y∈[-7,7]
- 外分点D可能超出边界，需要调整SCALE和OFFSET

### 文字渲染
- 所有中文使用 Text(..., font="Noto Sans CJK SC")
- 所有公式使用 MathTex(r"...")
- 度数符号使用 ^\circ

### 动画节奏
- 关键步骤（内外分点构造）放慢速度
- 辅助线的创建和消失要清晰
- 验证环节要有足够停留时间

---

## 总时长分配

| 场景 | 时长 | 占比 |
|------|------|------|
| Scene 1: 开场 | 5s | 5.9% |
| Scene 2: 揭示 | 5s | 5.9% |
| Scene 3: 引言 | 5s | 5.9% |
| Scene 4: 内分点 | 20s | 23.5% |
| Scene 5: 外分点 | 20s | 23.5% |
| Scene 6: 确定圆 | 15s | 17.6% |
| Scene 7: 验证总结 | 15s | 17.6% |
| **总计** | **85s** | **100%** |

---

## 渲染命令

```bash
# 快速预览
manim -pql apollonian_circle.py ApollonianCircle

# 高质量渲染
manim -qh apollonian_circle.py ApollonianCircle

# 4K质量
manim -qk apollonian_circle.py ApollonianCircle
```