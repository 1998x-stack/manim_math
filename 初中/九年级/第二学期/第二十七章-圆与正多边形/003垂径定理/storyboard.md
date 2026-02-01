# 垂径定理 - 动画分镜脚本

<!-- /root/code/sss/media/videos/perpendicular_chord_theorem/1920p60/PerpendicularChordTheorem.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"          # 蓝色 - 圆
COLOR_DIAMETER = "#e74c3c"        # 红色 - 直径
COLOR_CHORD = "#f39c12"           # 橙色 - 弦
COLOR_HIGHLIGHT = YELLOW          # 高亮黄色
COLOR_AUXILIARY = GRAY_B          # 辅助灰色
COLOR_ARC_MAJOR = "#9b59b6"       # 紫色 - 大弧
COLOR_ARC_MINOR = "#2ecc71"       # 绿色 - 小弧
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 验证条件 |
|------|---------|---------|---------|
| 圆心O | 预定义 | self.O | - |
| 半径r | 预定义 | self.radius | r > 0 |
| 弦AB的点A | 圆周上任意点 | self.A | \|OA\| = r |
| 弦AB的点B | 圆周上另一点 | self.B | \|OB\| = r |
| 弦AB中点M | (A+B)/2 | self.M | AM = MB |
| 垂足D | foot_of_perpendicular(O, A, B) | self.D | OD ⊥ AB |
| 直径CD的点C | O + (D-O)单位向量 * r | self.C | \|OC\| = r, O-D-C共线 |
| 直径CD的点D' | O - (D-O)单位向量 * r | self.D_ext | \|OD'\| = r, 与C对径 |
| 弧AC终点 | - | - | - |
| 弧BC终点 | - | - | - |

## 几何关系验证清单

| 关系 | 验证方法 | 数学表达式 |
|------|---------|-----------|
| OD ⊥ AB | dot(OD, AB) = 0 | OD · AB = 0 |
| M是AB中点 | \|AM\| = \|MB\| | AM = MB |
| D = M | \|D - M\| < ε | D ≡ M |
| 弧AC = 弧BC | 圆心角相等 | ∠AOC = ∠BOC |
| A, B在圆上 | 距离检查 | \|OA\| = \|OB\| = r |

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识 (顶部，y=7)
2. 问题文字 "如何快速平分一条弦?" (大字，y=6)
3. 圆和弦AB (主要图形，中心y=1)

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 问题文字打字效果 | `Write(hook_question)` | 0.8s |
| 1.1s | 圆形创建 | `Create(circle)` | 1.0s |
| 2.1s | 弦AB绘制（高亮橙色） | `Create(chord_AB)` | 0.6s |
| 2.7s | 点A, B标记闪烁 | `Flash(dot_A), Flash(dot_B)` | 0.4s |
| 3.1s | 等待思考 | `Wait(1.0)` | 1.0s |
| 4.1s | 提示"用垂径定理!" | `FadeIn(hint_text, shift=UP*0.3)` | 0.5s |
| 4.6s | 清理钩子文字 | `FadeOut(hook_question, hint_text)` | 0.4s |

### 几何参数
- 圆心: O = (0, 1, 0)
- 半径: r = 2.5
- 点A: O + 2.5 * (cos(150°), sin(150°), 0)
- 点B: O + 2.5 * (cos(30°), sin(30°), 0)

### 清理
- FadeOut: hook_question, hint_text
- 保留: author_info, circle, chord_AB, dot_A, dot_B

### 备注
- 弦AB应该明显不是水平的，角度约120°，便于展示垂直关系

---

## Scene 2: 绘制直径 (5-12秒)

**目的**: 引入关键元素——垂直于弦的直径

### 元素
1. 场景标题 "垂径定理" (y=5.5)
2. 直径CD (红色，虚线)
3. 垂直符号 (直角标记)
4. 标签 O, C, D

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `Write(title)` | 0.6s |
| 5.6s | 说明文字"作垂直于AB的直径" | `FadeIn(instruction)` | 0.5s |
| 6.1s | 从O到弦AB画虚线 | `Create(dash_line_OD)` | 0.8s |
| 6.9s | 标记垂足D | `FadeIn(dot_D, scale=0.5)` | 0.3s |
| 7.2s | 垂直符号出现 | `Create(right_angle_mark)` | 0.4s |
| 7.6s | 延长OD到圆周C和D' | `Create(diameter_line)` | 1.0s |
| 8.6s | 标记圆心O | `FadeIn(dot_O), Write(label_O)` | 0.5s |
| 9.1s | 标记C, D'点 | `FadeIn(dot_C), FadeIn(dot_D_ext)` | 0.4s |
| 9.5s | 高亮直径CD | `diameter.animate.set_color(COLOR_HIGHLIGHT)` | 0.3s |
| 9.8s | 等待理解 | `Wait(1.2)` | 1.2s |
| 11.0s | 清理说明文字 | `FadeOut(instruction)` | 0.3s |

### 几何计算（关键！）
```python
# 垂足D的精确计算
vec_AB = B - A
foot_D = A + np.dot(O - A, vec_AB) / np.dot(vec_AB, vec_AB) * vec_AB

# 验证：D应该等于M (中点)
M = (A + B) / 2
assert np.linalg.norm(foot_D - M) < 1e-6, "垂足应该是中点"

# 直径方向
OD_vec = foot_D - O
OD_unit = OD_vec / np.linalg.norm(OD_vec)

# 圆周交点
C = O + OD_unit * radius
D_ext = O - OD_unit * radius
```

### 清理
- FadeOut: instruction, dash_line_OD
- 保留: title, circle, chord_AB, diameter_line, right_angle_mark, dots, labels

---

## Scene 3: 证明平分弦 (12-25秒)

**目的**: 展示定理第一部分——直径平分弦

### 元素
1. 中点M的标记
2. 距离标注 AM, MB
3. 公式 AM = MB
4. 动画验证

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 说明"首先，证明平分弦" | `FadeIn(step1_text)` | 0.5s |
| 12.5s | 中点M淡入（与D重合） | `FadeIn(dot_M, scale=0.5)` | 0.3s |
| 12.8s | M标签出现 | `Write(label_M)` | 0.3s |
| 13.1s | 创建Brace标注AM | `Create(brace_AM)` | 0.5s |
| 13.6s | AM长度标签 | `Write(label_AM)` | 0.3s |
| 13.9s | 创建Brace标注MB | `Create(brace_MB)` | 0.5s |
| 14.4s | MB长度标签 | `Write(label_MB)` | 0.3s |
| 14.7s | 高亮AM和MB（颜色变化） | `brace_AM.animate.set_color(YELLOW)` | 0.4s |
| 15.1s | 等式AM = MB出现 | `Write(equation_AM_MB)` | 0.8s |
| 15.9s | 闪烁强调等式 | `Flash(equation, color=YELLOW)` | 0.4s |
| 16.3s | 等待理解 | `Wait(1.5)` | 1.5s |
| 17.8s | 清理 | `FadeOut(braces, labels, equation, step1_text)` | 0.5s |

### 关键代码片段
```python
# 确保M = D（数值验证）
M = (A + B) / 2
assert np.linalg.norm(M - D) < 1e-6

# Brace方向（垂直于AB向外）
perpendicular_direction = np.array([-vec_AB[1], vec_AB[0], 0])
brace_direction = perpendicular_direction / np.linalg.norm(perpendicular_direction)

# 距离计算
AM_length = np.linalg.norm(M - A)
MB_length = np.linalg.norm(B - M)
assert abs(AM_length - MB_length) < 1e-6, "中点距离应相等"
```

### 清理
- FadeOut: step1_text, braces, distance_labels, equation
- 保留: 所有几何元素

---

## Scene 4: 证明平分优弧 (25-38秒)

**目的**: 展示定理第二部分——平分弦所对的优弧

### 元素
1. 优弧ACB（大弧，紫色）
2. 分段：弧AC和弧CB（不同颜色）
3. 圆心角标记
4. 弧度标注

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 25.0s | 说明"其次，平分优弧" | `FadeIn(step2_text)` | 0.5s |
| 25.5s | 绘制优弧ACB（整体） | `Create(arc_major_ACB)` | 1.2s |
| 26.7s | 优弧分成两段，变色 | `Transform(arc_ACB, arc_AC + arc_CB)` | 0.8s |
| 27.5s | 弧AC高亮（紫色） | `arc_AC.animate.set_color(COLOR_ARC_MAJOR)` | 0.3s |
| 27.8s | 弧CB高亮（紫色） | `arc_CB.animate.set_color(COLOR_ARC_MAJOR)` | 0.3s |
| 28.1s | 画圆心角∠AOC | `Create(angle_AOC)` | 0.5s |
| 28.6s | 画圆心角∠BOC | `Create(angle_BOC)` | 0.5s |
| 29.1s | 标注"∠AOC" | `Write(label_angle_AOC)` | 0.4s |
| 29.5s | 标注"∠BOC" | `Write(label_angle_BOC)` | 0.4s |
| 29.9s | 等式"∠AOC = ∠BOC"出现 | `Write(equation_angles)` | 0.8s |
| 30.7s | 闪烁强调 | `Flash(equation_angles)` | 0.4s |
| 31.1s | 结论"∴ 弧AC = 弧BC" | `FadeIn(conclusion_arcs, shift=UP*0.3)` | 0.6s |
| 31.7s | 等待理解 | `Wait(1.5)` | 1.5s |
| 33.2s | 清理 | `FadeOut(angles, labels, equations)` | 0.5s |

### 几何计算（圆心角和弧）
```python
# 计算圆心角（用于验证）
angle_AOC = GeometryCalculator.angle_at_vertex(A, O, C)
angle_BOC = GeometryCalculator.angle_at_vertex(B, O, C)

# 验证相等
assert abs(angle_AOC - angle_BOC) < 1e-6, "圆心角应相等"

# 弧的起止角度
import math
start_angle_AC = math.atan2(A[1] - O[1], A[0] - O[0])
end_angle_AC = math.atan2(C[1] - O[1], C[0] - O[0])

# 使用Arc创建弧
arc_AC = Arc(
    radius=radius,
    start_angle=start_angle_AC,
    angle=end_angle_AC - start_angle_AC,  # 注意方向
    arc_center=O,
    color=COLOR_ARC_MAJOR,
    stroke_width=4
)
```

### 清理
- FadeOut: step2_text, arcs (保留淡化版), angles, labels
- 保留: 基本几何元素

---

## Scene 5: 证明平分劣弧 (38-48秒)

**目的**: 展示定理第二部分——平分弦所对的劣弧

### 元素
1. 劣弧AB（小弧，绿色）
2. 分段：弧AD和弧DB
3. 对称性展示

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 38.0s | 说明"同时，平分劣弧" | `FadeIn(step3_text)` | 0.5s |
| 38.5s | 绘制劣弧AB（整体绿色） | `Create(arc_minor_AB)` | 1.0s |
| 39.5s | 劣弧分成两段 | `Transform(arc_AB, arc_AD + arc_DB)` | 0.6s |
| 40.1s | 弧AD高亮 | `arc_AD.animate.set_color(COLOR_ARC_MINOR)` | 0.3s |
| 40.4s | 弧DB高亮 | `arc_DB.animate.set_color(COLOR_ARC_MINOR)` | 0.3s |
| 40.7s | 对称性动画：镜像闪烁 | `Flash at D, symmetry indication` | 0.6s |
| 41.3s | 结论"弧AD = 弧DB"出现 | `FadeIn(conclusion_minor_arcs)` | 0.5s |
| 41.8s | 等待 | `Wait(1.2)` | 1.2s |
| 43.0s | 清理 | `FadeOut(arcs, step3_text)` | 0.5s |

### 几何计算
```python
# 劣弧的计算（通过直径另一侧）
# 劣弧从A经过D到B（不经过C）

start_angle_AD = math.atan2(A[1] - O[1], A[0] - O[0])
mid_angle_D = math.atan2(D_ext[1] - O[1], D_ext[0] - O[0])
end_angle_DB = math.atan2(B[1] - O[1], B[0] - O[0])

# 确保方向正确（可能需要调整符号）
```

### 清理
- FadeOut: step3_text, minor_arcs
- 保留: 基本几何元素

---

## Scene 6: 定理总结 (48-58秒)

**目的**: 总结垂径定理的完整内容

### 元素
1. 定理陈述（文字和公式）
2. 关键词高亮
3. 图示回顾

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 48.0s | 标题变为"垂径定理总结" | `Transform(title, summary_title)` | 0.5s |
| 48.5s | 定理陈述1："垂直于弦的直径..." | `Write(theorem_part1)` | 1.2s |
| 49.7s | 关键词"垂直"高亮黄色 | `theorem_part1[key].set_color(YELLOW)` | 0.3s |
| 50.0s | 定理陈述2："平分这条弦" | `Write(theorem_part2)` | 0.8s |
| 50.8s | 关键词"平分"高亮 | `theorem_part2[key].set_color(YELLOW)` | 0.3s |
| 51.1s | 定理陈述3："并且平分弦所对的两条弧" | `Write(theorem_part3)` | 1.0s |
| 52.1s | 关键词"两条弧"高亮 | `theorem_part3[key].set_color(YELLOW)` | 0.3s |
| 52.4s | 公式出现 | `Write(formula)` | 0.8s |
| 53.2s | 公式: CD ⊥ AB ⟹ AM=MB, 弧AC=弧BC | | |
| 54.0s | 图示快闪回顾（各部分） | `Succession of Indicate()` | 1.5s |
| 55.5s | 等待记忆 | `Wait(1.5)` | 1.5s |
| 57.0s | 清理 | `FadeOut(theorem_texts, formula)` | 0.5s |

### 公式布局
```python
formula = MathTex(
    r"CD \perp AB",
    r"\Rightarrow",
    r"AM = MB",
    r"\text{  且  }",
    r"\text{弧}AC = \text{弧}BC"
)
# 注意：中文用Text单独处理
```

### 清理
- FadeOut: summary_title, theorem_texts, formula
- 保留: 基本图形（淡化）

---

## Scene 7: 片尾关注 (58-65秒)

**目的**: 品牌标识和引导关注

### 元素
1. 作者名放大居中
2. 账号ID
3. 关注引导语
4. 装饰图形

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 58.0s | 几何图形淡出 | `FadeOut(all_geometry)` | 0.6s |
| 58.6s | 作者名放大移动到中心 | `author_info.animate.scale(2).move_to(UP)` | 0.8s |
| 59.4s | 账号ID淡入 | `FadeIn(author_id, shift=UP*0.3)` | 0.5s |
| 59.9s | 关注引导语 | `FadeIn(follow_text, scale=1.1)` | 0.5s |
| 60.4s | 圆形装饰旋转进入 | `Rotate(decoration_circles)` | 1.0s |
| 61.4s | 定理关键词闪烁 | `Flash("垂径定理")` | 0.5s |
| 61.9s | 等待 | `Wait(1.5)` | 1.5s |
| 63.4s | 全部淡出 | `FadeOut(everything)` | 1.0s |

### 装饰元素
```python
decoration = VGroup(*[
    Circle(radius=0.3, color=COLOR_CIRCLE, fill_opacity=0.5)
    .shift(2 * np.array([np.cos(i*PI/3), np.sin(i*PI/3), 0]))
    for i in range(6)
])
```

### 清理
- FadeOut: 所有元素

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留，最后放大 |
| circle | Scene 1 | Scene 6 | 主圆，全程可见 |
| chord_AB | Scene 1 | Scene 6 | 弦AB，主要元素 |
| dot_A, dot_B | Scene 1 | Scene 6 | 端点标记 |
| diameter_CD | Scene 2 | Scene 6 | 直径，关键元素 |
| right_angle_mark | Scene 2 | Scene 6 | 垂直符号 |
| dot_O, label_O | Scene 2 | Scene 6 | 圆心 |
| dot_M | Scene 3 | Scene 3 | 中点标记，短暂 |
| braces (AM, MB) | Scene 3 | Scene 3 | 距离标注 |
| arc_major_ACB | Scene 4 | Scene 4 | 优弧 |
| angles (AOC, BOC) | Scene 4 | Scene 4 | 圆心角 |
| arc_minor_AB | Scene 5 | Scene 5 | 劣弧 |
| theorem_texts | Scene 6 | Scene 6 | 定理陈述 |
| follow_text | Scene 7 | Scene 7 | 关注引导 |

---

## 时间轴总览

```
0s        5s        12s       25s       38s       48s       58s       65s
|---------|---------|---------|---------|---------|---------|---------|
  钩子      绘直径     平分弦     平分优弧   平分劣弧   定理总结   片尾关注
  开场      Scene2    Scene3    Scene4    Scene5    Scene6    Scene7
```

---

## 验证检查清单

### 几何正确性
- [ ] 垂足D = 中点M（误差 < 1e-6）
- [ ] OD ⊥ AB（点积 < 1e-8）
- [ ] 圆心角∠AOC = ∠BOC（误差 < 1e-6）
- [ ] AM = MB（误差 < 1e-6）
- [ ] 所有点在圆上（距离 = radius，误差 < 1e-6）

### 动画流畅性
- [ ] 场景过渡自然（FadeOut/FadeIn衔接）
- [ ] 关键步骤有足够停留时间（≥1.2s）
- [ ] 无元素重叠
- [ ] 文字大小适中（主标题≥36, 正文≥22）

### 边界检查
- [ ] 所有元素在安全区域（x ∈ [-4, 4], y ∈ [-7, 7]）
- [ ] 圆半径合适（不超出边界）
- [ ] 文字不与图形重叠

### 品牌一致性
- [ ] 开头有作者信息
- [ ] 结尾有关注引导
- [ ] 配色符合品牌调性