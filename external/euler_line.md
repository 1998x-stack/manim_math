# 欧拉线 (Euler Line) - 动画分镜脚本

## 元信息
- 目标时长: 90-110 秒
- 场景数量: 10 个
- 难度等级: 高中/竞赛
- 目标受众: 高中生、数学竞赛学生、数学爱好者

## 颜色配置
```python
COLOR_TRIANGLE = WHITE              # 三角形主体
COLOR_CIRCUMCENTER = "#e74c3c"      # 外心O (红色)
COLOR_CENTROID = "#2ecc71"          # 重心G (绿色)
COLOR_ORTHOCENTER = "#f39c12"       # 垂心H (橙色)
COLOR_NINE_POINT_CENTER = "#9b59b6" # 九点圆圆心N (紫色)
COLOR_EULER_LINE = "#3498db"        # 欧拉线 (蓝色)
COLOR_CIRCUMCIRCLE = "#e74c3c"      # 外接圆 (浅红色)
COLOR_NINE_POINT_CIRCLE = "#9b59b6" # 九点圆 (浅紫色)
COLOR_HIGHLIGHT = YELLOW            # 高亮提示
COLOR_AUXILIARY = GRAY_B            # 辅助线
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 验证条件 |
|------|---------|---------|---------|
| 三角形顶点 | 基准定义 | A, B, C | 不共线 |
| 外心 | 三边垂直平分线交点 | O | \|OA\|=\|OB\|=\|OC\| |
| 重心 | 三条中线交点 | G | G = (A+B+C)/3 |
| 垂心 | 三条高线交点 | H | H = A+B+C-2O |
| 九点圆圆心 | OH中点 | N | N = (O+H)/2 |
| 外接圆半径 | \|OA\| | R | R > 0 |
| 九点圆半径 | R/2 | R_nine | R_nine = R/2 |
| 欧拉线 | 过O, G, H的直线 | - | O, G, H共线 |
| 比例关系 | OG:GH | - | OG:GH = 1:2 |

## 关键几何验证
```python
# 1. 外心验证
assert |OA - R| < eps and |OB - R| < eps and |OC - R| < eps

# 2. 重心验证
assert |G - (A+B+C)/3| < eps

# 3. 垂心验证 (使用欧拉公式)
assert |H - (A+B+C-2*O)| < eps

# 4. 共线性验证 (核心定理)
assert triangle_area(O, G, H) < eps

# 5. 比例验证
assert |OG - |OH|/3| < eps  # OG = OH/3
assert |GH - 2*|OH|/3| < eps  # GH = 2*OH/3

# 6. 九点圆圆心验证
assert |N - (O+H)/2| < eps
```

---

## Scene 1: 开场钩子 (0-6秒)

**目的**: 吸引注意力，展示欧拉线的神奇性质

### 元素
1. 作者标识 (顶部)
2. 钩子问题大字
3. 三角形 + 四个特殊点闪烁

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 顶部小字 |
| 0.3s | 钩子文字快速书写 | `Write(hook_text, run_time=0.9)` | "四个中心竟然共线?" |
| 1.3s | 三角形淡入 | `Create(triangle, run_time=0.9)` | 主图形 |
| 2.3s | 外心O闪烁 | `FadeIn(O_dot) + Flash` | 红色点 |
| 2.8s | 重心G闪烁 | `FadeIn(G_dot) + Flash` | 绿色点 |
| 3.3s | 垂心H闪烁 | `FadeIn(H_dot) + Flash` | 橙色点 |
| 3.8s | 九点圆圆心N闪烁 | `FadeIn(N_dot) + Flash` | 紫色点 |
| 4.3s | **欧拉线戏剧性出现** | `Create(euler_line) + Flash` | 蓝色线 |
| 5.3s | 惊叹文字 | `Write(surprise)` | "这就是欧拉线!" |

### 文案
```
顶部: 上海初高中数学直通车 @emptyandcalm
钩子: "四个中心竟然共线?"
惊叹: "这就是欧拉线!"
```

### 清理
- FadeOut: hook_text, surprise, 四个点
- 保留: triangle, author_info
- 移除: euler_line (为后续构造做准备)

---

## Scene 2: 定理陈述 (6-15秒)

**目的**: 清晰说明欧拉线定理的内容

### 元素
1. 定理标题
2. 四个中心的定义
3. 欧拉线定理陈述
4. 比例关系

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 6.0s | 定理标题出现 | `Write(title, run_time=0.7)` | "欧拉线定理" |
| 6.8s | 副标题 | `FadeIn(subtitle)` | "Euler Line Theorem" |
| 7.5s | 中心1说明 | `FadeIn(center1, shift=UP*0.2)` | "外心O - 外接圆圆心" |
| 8.2s | 中心2说明 | `FadeIn(center2, shift=UP*0.2)` | "重心G - 中线交点" |
| 8.9s | 中心3说明 | `FadeIn(center3, shift=UP*0.2)` | "垂心H - 高线交点" |
| 9.6s | 中心4说明 | `FadeIn(center4, shift=UP*0.2)` | "九点圆圆心N" |
| 10.5s | **核心结论** | `Write(conclusion, color=YELLOW)` | "O, G, H, N 四点共线!" |
| 11.5s | 比例关系 | `FadeIn(ratio)` | "OG:GH = 1:2" |
| 12.5s | 中点关系 | `FadeIn(midpoint)` | "N是OH的中点" |
| 13.8s | 停留理解 | `Wait(1.2)` | 重要概念 |

### 文案
```
标题: 欧拉线定理 (Euler Line Theorem, 1765)

四个中心:
• 外心O: 三边垂直平分线交点，外接圆圆心
• 重心G: 三条中线交点，质量中心
• 垂心H: 三条高线交点
• 九点圆圆心N: 九点圆圆心，欧拉点

定理: O, G, H, N 四点共线！
      OG : GH = 1 : 2
      N 是 OH 的中点
```

### 清理
- FadeOut: title, subtitle, center1-4, conclusion, ratio, midpoint
- 保留: triangle, author_info

---

## Scene 3: 构造外心O (15-22秒)

**目的**: 详细展示外心的构造方法

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 15.0s | 步骤标题 | `FadeIn(step_title)` | "步骤1: 作外心O" |
| 15.6s | 说明 | `FadeIn(explanation)` | "三边垂直平分线的交点" |
| 16.3s | 边AB高亮 | `Indicate(AB_line, color=YELLOW)` | - |
| 16.9s | AB中点M1标记 | `FadeIn(M1_dot)` | 小点 |
| 17.4s | 垂直平分线1 | `Create(perp_bisector_1)` | 虚线 |
| 18.2s | 边BC高亮 | `Indicate(BC_line, color=YELLOW)` | - |
| 18.7s | BC中点M2标记 | `FadeIn(M2_dot)` | 小点 |
| 19.2s | 垂直平分线2 | `Create(perp_bisector_2)` | 虚线 |
| 20.0s | **外心O出现** | `FadeIn(O_dot, scale=0.5) + Flash` | 红色大点 |
| 20.6s | O标签 | `Write(O_label)` | "O 外心" |
| 21.2s | 外接圆 | `Create(circumcircle, run_time=1.2)` | 浅红色圆 |

### 几何计算关键
```python
# 外心O计算
O = GeometryCalculator.circumcenter(A, B, C)

# 验证
R = np.linalg.norm(A - O)
assert abs(np.linalg.norm(B - O) - R) < eps
assert abs(np.linalg.norm(C - O) - R) < eps

# 垂直平分线
M_AB = (A + B) / 2
perp_AB_direction = np.array([-(B-A)[1], (B-A)[0], 0])
```

### 清理
- FadeOut: step_title, explanation, perp_bisector_1, perp_bisector_2, M1_dot, M2_dot
- 保留: O_dot, O_label, circumcircle (淡化为背景)

---

## Scene 4: 构造重心G (22-28秒)

**目的**: 展示重心的构造和性质

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 22.0s | 步骤标题 | `FadeIn(step_title)` | "步骤2: 作重心G" |
| 22.5s | 说明 | `FadeIn(explanation)` | "三条中线的交点" |
| 23.1s | BC中点D标记 | `FadeIn(D_dot)` | - |
| 23.5s | 中线AD | `Create(median_AD)` | 从A到D |
| 24.2s | CA中点E标记 | `FadeIn(E_dot)` | - |
| 24.6s | 中线BE | `Create(median_BE)` | 从B到E |
| 25.3s | **重心G出现** | `FadeIn(G_dot, scale=0.5) + Flash` | 绿色大点 |
| 25.9s | G标签 | `Write(G_label)` | "G 重心" |
| 26.5s | 2:1比例标注 | `FadeIn(ratio_annotation)` | AG:GD = 2:1 |
| 27.5s | 停留 | `Wait(1.0)` | - |

### 几何计算
```python
# 重心G计算
G = (A + B + C) / 3

# 验证
midpoint_BC = (B + C) / 2
AG = G - A
AD = midpoint_BC - A
assert abs(np.linalg.norm(AG) - 2/3 * np.linalg.norm(AD)) < eps
```

### 清理
- FadeOut: step_title, explanation, median_AD, median_BE, D_dot, E_dot, ratio_annotation
- 保留: G_dot, G_label

---

## Scene 5: 构造垂心H (28-35秒)

**目的**: 展示垂心的构造

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 28.0s | 步骤标题 | `FadeIn(step_title)` | "步骤3: 作垂心H" |
| 28.5s | 说明 | `FadeIn(explanation)` | "三条高线的交点" |
| 29.1s | 边BC高亮 | `Indicate(BC_line)` | - |
| 29.6s | 高线AD' | `Create(altitude_A)` | 从A垂直于BC |
| 30.3s | 垂足D'标记 | `FadeIn(D_prime_dot)` | - |
| 30.7s | 直角符号 | `FadeIn(right_angle_1)` | - |
| 31.3s | 边CA高亮 | `Indicate(CA_line)` | - |
| 31.8s | 高线BE' | `Create(altitude_B)` | 从B垂直于CA |
| 32.5s | 垂足E'标记 | `FadeIn(E_prime_dot)` | - |
| 32.9s | 直角符号 | `FadeIn(right_angle_2)` | - |
| 33.5s | **垂心H出现** | `FadeIn(H_dot, scale=0.5) + Flash` | 橙色大点 |
| 34.1s | H标签 | `Write(H_label)` | "H 垂心" |

### 几何计算
```python
# 垂心H计算 (使用欧拉公式)
H = A + B + C - 2 * O

# 验证: AH垂直于BC
foot_BC = GeometryCalculator.foot_of_perpendicular(A, B, C)
AH_vec = H - A
BC_vec = C - B
assert abs(np.dot(AH_vec[:2], BC_vec[:2])) < eps
```

### 清理
- FadeOut: step_title, explanation, altitude_A, altitude_B, 垂足, 直角符号
- 保留: H_dot, H_label

---

## Scene 6: 欧拉线的显现 (35-45秒)

**目的**: 戏剧性地展示O, G, H三点共线

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 35.0s | 提问文字 | `FadeIn(question)` | "这三个点有什么关系?" |
| 35.8s | O, G, H同时高亮 | `AnimationGroup(Indicate...)` | - |
| 36.6s | 连接O-G虚线 | `Create(OG_dashed)` | 灰色虚线 |
| 37.3s | 连接G-H虚线 | `Create(GH_dashed)` | 灰色虚线 |
| 38.0s | 惊叹文字 | `Write(surprise)` | "它们共线!" |
| 38.7s | **欧拉线戏剧性出现** | `Transform(虚线, euler_line)` | 虚线变实线 |
| 39.5s | 欧拉线发光 | `Flash(euler_line, ...)` | 强烈视觉效果 |
| 40.2s | 标签"欧拉线" | `Write(euler_label)` | 蓝色标签 |
| 41.0s | 比例标注 | `FadeIn(ratio_marks)` | OG:GH = 1:2 |
| 41.8s | 测量线段 | `Create(measurement_lines)` | 显示比例 |
| 43.0s | 说明 | `FadeIn(explanation)` | "OG = OH/3, GH = 2OH/3" |
| 44.0s | 停留理解 | `Wait(1.0)` | 核心定理 |

### 几何验证
```python
# 验证共线性
area_OGH = GeometryCalculator.triangle_area(O, G, H)
assert area_OGH < 1e-8

# 验证比例
OG = np.linalg.norm(G - O)
GH = np.linalg.norm(H - G)
assert abs(OG / GH - 1/2) < eps  # OG:GH = 1:2

OH = np.linalg.norm(H - O)
assert abs(OG - OH/3) < eps
```

### 清理
- FadeOut: question, surprise, OG_dashed, GH_dashed, ratio_marks, measurement_lines, explanation
- 保留: euler_line, euler_label

---

## Scene 7: 九点圆圆心N (45-54秒)

**目的**: 介绍九点圆圆心，展示N在欧拉线上

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 45.0s | 步骤标题 | `FadeIn(step_title)` | "步骤4: 九点圆圆心N" |
| 45.6s | 说明 | `FadeIn(explanation)` | "通过9个特殊点的圆" |
| 46.3s | 三边中点闪烁 | `AnimationGroup(Flash...)` | 3个绿点 |
| 47.0s | 三条高垂足闪烁 | `AnimationGroup(Flash...)` | 3个黄点 |
| 47.7s | H到顶点中点闪烁 | `AnimationGroup(Flash...)` | 3个紫点 |
| 48.5s | 九点圆 | `Create(nine_point_circle)` | 浅紫色圆 |
| 49.5s | **九点圆圆心N** | `FadeIn(N_dot, scale=0.5) + Flash` | 紫色大点 |
| 50.1s | N标签 | `Write(N_label)` | "N 九点圆圆心" |
| 50.8s | 惊叹 | `Write(surprise2)` | "N也在欧拉线上!" |
| 51.5s | N在欧拉线上闪烁 | `Indicate(N_dot + euler_line)` | - |
| 52.2s | 中点性质 | `FadeIn(midpoint_text)` | "N是OH的中点" |
| 53.0s | 标注ON = NH | `Create(measurement_ON_NH)` | 等长标记 |

### 几何计算
```python
# 九点圆圆心N (OH中点)
N = (O + H) / 2

# 验证
ON = np.linalg.norm(N - O)
NH = np.linalg.norm(H - N)
assert abs(ON - NH) < eps

# 九点圆半径
R_nine = R / 2  # 是外接圆半径的一半
```

### 清理
- FadeOut: step_title, explanation, 九个点, surprise2, midpoint_text, measurement_ON_NH
- 保留: nine_point_circle (淡化), N_dot, N_label

---

## Scene 8: 动态演示 - 三角形变形 (54-68秒)

**目的**: 展示当三角形形状变化时，欧拉线如何保持性质

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 54.0s | 提示文字 | `FadeIn(hint)` | "三角形变形时..." |
| 54.8s | 使用ValueTracker | 设置动态更新 | - |
| 55.0s | **顶点C开始移动** | `C.animate.move_to(...)` | 慢速移动 |
| 55.0s | O, G, H, N实时跟踪 | `always_redraw(...)` | 同步更新 |
| 55.0s | 欧拉线实时变化 | `always_redraw(...)` | 始终过4点 |
| 55.0s | 圆实时调整 | `always_redraw(...)` | 外接圆和九点圆 |
| 68.0s | C点停止 | 回到初始位置 | - |
| 68.5s | 说明文字 | `FadeIn(property)` | "欧拉线性质始终成立" |

### 技术实现
```python
# ValueTracker控制
vertex_tracker = ValueTracker(0)

def get_C_position(t):
    # C在某条路径上移动
    angle = t * PI
    offset = np.array([np.cos(angle), np.sin(angle) * 0.5, 0])
    return C_initial + offset

# 动态更新
O_dynamic = always_redraw(lambda: Dot(
    GeometryCalculator.circumcenter(A, B, get_C_position(vertex_tracker.get_value())),
    color=COLOR_CIRCUMCENTER
))

# 移动动画
self.play(
    vertex_tracker.animate.set_value(2 * PI),
    run_time=13,
    rate_func=linear
)
```

### 清理
- remove_updater: 所有动态更新
- FadeOut: hint, property
- 保留: 静止的所有元素

---

## Scene 9: 特殊三角形的欧拉线 (68-80秒)

**目的**: 展示特殊三角形中欧拉线的特性

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 68.0s | 场景标题 | `Write(title)` | "特殊三角形" |
| 68.8s | **情况1: 等边三角形** | - | - |
| 69.0s | 等边三角形出现 | `Create(equilateral)` | 左侧 |
| 69.8s | 四个中心重合 | `FadeIn(single_dot)` | 同一点 |
| 70.5s | 说明 | `FadeIn(text1)` | "四心重合，欧拉线退化" |
| 71.5s | **情况2: 直角三角形** | - | - |
| 71.7s | 直角三角形出现 | `Create(right_triangle)` | 中间 |
| 72.5s | 垂心H在直角顶点 | `Indicate(H_at_vertex)` | - |
| 73.2s | 外心O在斜边中点 | `Indicate(O_at_midpoint)` | - |
| 74.0s | 欧拉线 | `Create(euler_right)` | 通过斜边中点 |
| 74.7s | 说明 | `FadeIn(text2)` | "欧拉线过斜边中点" |
| 75.7s | **情况3: 等腰三角形** | - | - |
| 75.9s | 等腰三角形出现 | `Create(isosceles)` | 右侧 |
| 76.7s | 欧拉线 | `Create(euler_isosceles)` | 垂直底边 |
| 77.4s | 说明 | `FadeIn(text3)` | "欧拉线垂直底边" |
| 78.5s | 停留 | `Wait(1.5)` | - |

### 清理
- FadeOut: 所有特殊三角形和说明
- 恢复: 原三角形

---

## Scene 10: 片尾总结与关注 (80-110秒)

**目的**: 总结要点，引导关注

### 动画序列

| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 80.0s | 清空场景 | `FadeOut(所有元素)` | - |
| 81.0s | 总结标题 | `Write(summary_title)` | "欧拉线 - 要点总结" |
| 82.0s | 要点1 | `FadeIn(point1, shift=UP*0.2)` | "四个中心: O, G, H, N" |
| 83.2s | 要点2 | `FadeIn(point2, shift=UP*0.2)` | "四点共线!" |
| 84.4s | 要点3 | `FadeIn(point3, shift=UP*0.2)` | "OG:GH = 1:2" |
| 85.6s | 要点4 | `FadeIn(point4, shift=UP*0.2)` | "N是OH的中点" |
| 86.8s | 小图示意 | `FadeIn(mini_diagram)` | 缩小版 |
| 88.5s | 历史卡片 | `FadeIn(history)` | "Euler, 1765" |
| 90.0s | 作者信息放大 | `Transform(author_info, author_large)` | - |
| 91.0s | 关注提示 | `Write(follow_text)` | "关注我，学更多几何!" |
| 92.0s | 装饰动画 | `FadeIn(decorations)` | 旋转图标 |
| 94.0s | 停留 | `Wait(3.0)` | - |
| 97.0s | 全部淡出 | `*[FadeOut(mob)...]` | - |

### 文案
```
总结:
欧拉线 (Euler Line)

核心要点:
✓ 四个中心: 外心O、重心G、垂心H、九点圆圆心N
✓ 四点共线，构成欧拉线
✓ 比例关系: OG:GH = 1:2
✓ 中点性质: N是OH的中点

历史: 
瑞士数学家莱昂哈德·欧拉
1765年首次发现并证明

掌握几何，从关注开始!
上海初高中数学直通车
@emptyandcalm
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 持续场景 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 1 | Scene 10 | 全程 | 顶部常驻 |
| triangle | Scene 1 | Scene 10 | 全程 | 主图形 |
| O_dot, O_label | Scene 3 | Scene 10 | 3-10 | 外心 |
| G_dot, G_label | Scene 4 | Scene 10 | 4-10 | 重心 |
| H_dot, H_label | Scene 5 | Scene 10 | 5-10 | 垂心 |
| euler_line | Scene 6 | Scene 10 | 6-10 | 欧拉线 |
| N_dot, N_label | Scene 7 | Scene 10 | 7-10 | 九点圆圆心 |
| circumcircle | Scene 3 | Scene 8 | 3-8 | 外接圆(淡化) |
| nine_point_circle | Scene 7 | Scene 8 | 7-8 | 九点圆(淡化) |

---

## 时间节奏控制

| 场景 | 时长 | 节奏 | 理由 |
|------|------|------|------|
| Scene 1 | 6s | 快 | 钩子需快速抓住注意 |
| Scene 2 | 9s | 中 | 定理陈述需清晰 |
| Scene 3 | 7s | 中 | 外心构造 |
| Scene 4 | 6s | 中 | 重心构造 |
| Scene 5 | 7s | 中 | 垂心构造 |
| Scene 6 | 10s | 慢 | 核心定理，戏剧性 |
| Scene 7 | 9s | 中 | 九点圆圆心 |
| Scene 8 | 14s | 慢 | 动态演示需流畅 |
| Scene 9 | 12s | 中 | 特殊情况 |
| Scene 10 | 30s | 慢 | 总结和关注引导 |

**总时长**: 110秒

---

## 技术难点与解决方案

### 难点1: 动态更新四个中心的位置
**问题**: 三角形变形时，O, G, H, N都需实时重新计算
**解决**: 
```python
def get_all_centers(A, B, C):
    O = GeometryCalculator.circumcenter(A, B, C)
    G = (A + B + C) / 3
    H = A + B + C - 2 * O
    N = (O + H) / 2
    return O, G, H, N

# 使用always_redraw
O_dynamic = always_redraw(lambda: Dot(
    get_all_centers(A, B, get_C(t))[0],
    color=COLOR_CIRCUMCENTER
))
```

### 难点2: 比例关系的可视化
**问题**: 如何清晰展示OG:GH = 1:2
**解决**:
```python
# 使用Brace标注
brace_OG = Brace(Line(O, G), direction=LEFT)
label_OG = brace_OG.get_text("1")

brace_GH = Brace(Line(G, H), direction=LEFT)
label_GH = brace_GH.get_text("2")
```

### 难点3: 九点的精确标记
**问题**: 九个点位置需精确计算
**解决**:
```python
# 三边中点
mid_BC = (B + C) / 2
mid_CA = (C + A) / 2
mid_AB = (A + B) / 2

# 三条高垂足
foot_BC = GeometryCalculator.foot_of_perpendicular(A, B, C)
foot_CA = GeometryCalculator.foot_of_perpendicular(B, C, A)
foot_AB = GeometryCalculator.foot_of_perpendicular(C, A, B)

# 垂心到顶点中点
mid_HA = (H + A) / 2
mid_HB = (H + B) / 2
mid_HC = (H + C) / 2
```

### 难点4: 欧拉线在不同三角形中的表现
**问题**: 锐角、直角、钝角三角形的垂心位置不同
**解决**:
- 使用向量法统一计算: H = A + B + C - 2O
- 自动处理垂心在内部/外部的情况
- 欧拉线延长确保覆盖所有中心

---

## 验证清单 (运行前必查)

### 几何正确性
- [ ] 外心O计算正确 (|OA|=|OB|=|OC|)
- [ ] 重心G计算正确 (G = (A+B+C)/3)
- [ ] 垂心H计算正确 (H = A+B+C-2O)
- [ ] 九点圆圆心N计算正确 (N = (O+H)/2)
- [ ] O, G, H, N共线 (area < eps)
- [ ] 比例关系 (OG:GH = 1:2)
- [ ] 所有坐标在边界内

### 动画流畅性
- [ ] 场景切换自然
- [ ] 重点停留足够
- [ ] 动态更新不卡顿
- [ ] 无元素重叠或溢出

### 文字可读性
- [ ] 字体大小符合规范
- [ ] 中文使用Text()
- [ ] LaTeX公式正确
- [ ] 标签不重叠

---

## 备选方案

### 方案A: 简化版 (60秒)
- 省略Scene 8动态演示
- 省略Scene 9特殊三角形
- 直接从Scene 7跳到Scene 10

### 方案B: 深度版 (150秒)
- 增加向量证明推导
- 增加德朗香点介绍
- 增加欧拉线长度公式

---

**脚本状态**: ✅ 分镜完成，准备编码
**预计完成时间**: 3-4小时 (包括调试)
**信心指数**: ⭐⭐⭐⭐⭐