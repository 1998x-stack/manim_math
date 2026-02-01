# 三角形外角定理证明 - 动画分镜脚本

## 元信息
- 目标时长: 60-70 秒
- 场景数量: 7 个
- 难度等级: 初中
- 核心知识点: 外角定理、平行线性质(内错角、同位角)

## 颜色配置
```python
COLOR_TRIANGLE = WHITE
COLOR_EXTERIOR_ANGLE = "#e74c3c"  # 红色 - 外角
COLOR_INTERIOR_ANGLE_1 = "#3498db"  # 蓝色 - 内角∠A
COLOR_INTERIOR_ANGLE_2 = "#2ecc71"  # 绿色 - 内角∠B
COLOR_AUXILIARY = YELLOW  # 辅助线
COLOR_HIGHLIGHT = GOLD  # 高亮
COLOR_GRAY = GRAY_B  # 说明文字
```

## 几何预计算清单

### 主要顶点
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 顶点A | [-2, 1, 0] * SCALE + OFFSET | self.A | 左上角 |
| 顶点B | [2, 0.5, 0] * SCALE + OFFSET | self.B | 右侧 |
| 顶点C | [0, -2, 0] * SCALE + OFFSET | self.C | 底部 |
| 延长点D | C + (C-B)*延长系数 | self.D | BC延长线上的点 |

### 辅助线相关
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 平行线点E | C + (A-B) | self.E | 过C平行于AB的线上的点 |

### 角度相关(使用Angle类)
| 角 | 顶点 | 起始边终点 | 终止边终点 | 存储变量 | 备注 |
|---|------|-----------|-----------|---------|------|
| ∠ACD (外角) | C | A | D | self.angle_ACD | 红色,外角 |
| ∠A (内角) | A | C | B | self.angle_A | 蓝色,内角1 |
| ∠B (内角) | B | C | A | self.angle_B | 绿色,内角2 |
| ∠ACE (内错角) | C | A | E | self.angle_ACE | 等于∠A |
| ∠ECD (同位角) | C | E | D | self.angle_ECD | 等于∠B |

### 角度方向性说明
**关键**: Angle类的参数顺序为 `Angle(line1, line2, quadrant=...)`
- line1: 起始边 (从顶点指向的第一个点)
- line2: 终止边 (从顶点指向的第二个点)
- 角度从line1逆时针转向line2

**示例**:
```python
# ∠ACD: 顶点C, 从CA边逆时针转到CD边
angle_ACD = Angle(
    Line(C, A),  # 起始边CA
    Line(C, D),  # 终止边CD
    radius=0.6,
    color=COLOR_EXTERIOR_ANGLE
)
```

## 全局常数
```python
SCALE = 1.0
OFFSET = UP * 1.5
EXTENSION_FACTOR = 1.5  # BC延长的系数
```

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
吸引注意力，提出问题

### 元素
1. 作者信息 (顶部)
2. 钩子问题文字
3. 三角形 + 外角闪烁

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` | 0.3s |
| 0.3s | 问题文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 三角形创建 | `Create(triangle)` | 1.0s |
| 2.1s | 外角闪烁 | `Flash(angle_arc)` | 0.5s |
| 2.6s | 问题强化 | `Indicate(hook_text)` | 0.5s |
| 3.1s | 等待 | `Wait(1.0)` | 1.0s |

### 文案
- 钩子: "外角 = 两个内角之和?"
- 位置: UP * 6

### 清理
- FadeOut: hook_text
- 保留: triangle, author_info

---

## Scene 2: 标注角度 (5-12秒)

### 目的
明确标注外角和两个内角，建立认知

### 元素
1. 延长BC至D
2. 外角∠ACD标注 (红色圆弧 + α标签)
3. 内角∠A标注 (蓝色圆弧 + ∠A标签)
4. 内角∠B标注 (绿色圆弧 + ∠B标签)

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 延长BC | `Create(extend_line)` | 0.6s |
| 0.6s | 标注外角 | `Create(angle_ACD), Write(label_exterior)` | 1.0s |
| 1.6s | 说明文字 | `FadeIn(explain_exterior)` | 0.4s |
| 2.0s | 等待 | `Wait(0.8)` | 0.8s |
| 2.8s | 标注∠A | `Create(angle_A), Write(label_A)` | 0.8s |
| 3.6s | 标注∠B | `Create(angle_B), Write(label_B)` | 0.8s |
| 4.4s | 问题提示 | `FadeIn(question)` | 0.5s |
| 4.9s | 等待 | `Wait(1.5)` | 1.5s |

### 文案
- 外角说明: "外角 α"
- 问题: "α = ∠A + ∠B ?"
- 位置: DOWN * 5

### 角度绘制要点
```python
# 使用Angle类确保方向正确
# 外角∠ACD
angle_ACD = Angle(
    Line(C, A),  # 起始边
    Line(C, D),  # 终止边
    radius=0.6,
    color=COLOR_EXTERIOR_ANGLE
)

# 内角∠A (在顶点A处)
angle_A = Angle(
    Line(A, C),  # 起始边AC
    Line(A, B),  # 终止边AB
    radius=0.5,
    color=COLOR_INTERIOR_ANGLE_1
)

# 内角∠B (在顶点B处)
angle_B = Angle(
    Line(B, C),  # 起始边BC
    Line(B, A),  # 终止边BA
    radius=0.5,
    color=COLOR_INTERIOR_ANGLE_2
)
```

### 清理
- FadeOut: explain_exterior, question
- 保留: triangle, extend_line, angle_ACD, angle_A, angle_B, labels

---

## Scene 3: 引入辅助线 (12-18秒)

### 目的
引入关键辅助线：过C作AB的平行线

### 元素
1. 辅助线CE (虚线，黄色)
2. 平行符号标记
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 辅助线提示 | `FadeIn(hint)` | 0.5s |
| 0.5s | 绘制CE | `Create(auxiliary_line)` | 1.2s |
| 1.7s | 平行标记 | `FadeIn(parallel_marks)` | 0.6s |
| 2.3s | 说明 | `FadeIn(explain)` | 0.5s |
| 2.8s | 强调 | `Indicate(auxiliary_line)` | 0.6s |
| 3.4s | 等待 | `Wait(1.5)` | 1.5s |

### 文案
- 提示: "关键: 过C作AB的平行线"
- 说明: "CE // AB"
- 位置: DOWN * 5

### 几何计算
```python
# 计算E点: C点 + AB的方向向量
vec_AB = B - A
E = C + vec_AB * 1.5  # 延长以显示

# 辅助线CE (虚线)
auxiliary_line = DashedLine(
    C - vec_AB * 0.3,  # 稍微延伸
    E,
    color=COLOR_AUXILIARY,
    dash_length=0.1
)
```

### 清理
- FadeOut: hint, explain
- 保留: auxiliary_line, parallel_marks

---

## Scene 4: 证明步骤1 - 内错角 (18-28秒)

### 目的
证明∠ACE = ∠A (内错角相等)

### 元素
1. 高亮∠ACE (新角度，蓝色虚线)
2. 内错角标记
3. 等式显示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title_step1)` | 0.4s |
| 0.4s | 绘制∠ACE | `Create(angle_ACE)` | 0.8s |
| 1.2s | 同时闪烁∠A和∠ACE | `Flash(angle_A), Flash(angle_ACE)` | 0.6s |
| 1.8s | 内错角标记 | `FadeIn(alternate_marks)` | 0.6s |
| 2.4s | 等式1显示 | `Write(equation_1)` | 1.0s |
| 3.4s | 解释 | `FadeIn(explain_1)` | 0.5s |
| 3.9s | 等待理解 | `Wait(2.0)` | 2.0s |
| 5.9s | 高亮等式 | `Indicate(equation_1)` | 0.5s |

### 文案
- 标题: "步骤1: 利用内错角"
- 等式1: "∠ACE = ∠A" (蓝色)
- 解释: "CE // AB, 内错角相等"
- 位置: 
  - 标题: UP * 5.5
  - 等式: DOWN * 4.5
  - 解释: DOWN * 5.5

### 角度绘制
```python
# ∠ACE: 顶点C, 从CA到CE
angle_ACE = Angle(
    Line(C, A),  # 起始边CA
    Line(C, E),  # 终止边CE
    radius=0.5,
    color=COLOR_INTERIOR_ANGLE_1,
    stroke_width=2,
    stroke_opacity=0.6  # 虚化以区分
)
```

### 清理
- FadeOut: title_step1, explain_1, alternate_marks
- 保留: angle_ACE, equation_1

---

## Scene 5: 证明步骤2 - 同位角 (28-38秒)

### 目的
证明∠ECD = ∠B (同位角相等)

### 元素
1. 高亮∠ECD (新角度，绿色虚线)
2. 同位角标记
3. 等式显示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题出现 | `FadeIn(title_step2)` | 0.4s |
| 0.4s | 绘制∠ECD | `Create(angle_ECD)` | 0.8s |
| 1.2s | 同时闪烁∠B和∠ECD | `Flash(angle_B), Flash(angle_ECD)` | 0.6s |
| 1.8s | 同位角标记 | `FadeIn(corresponding_marks)` | 0.6s |
| 2.4s | 等式2显示 | `Write(equation_2)` | 1.0s |
| 3.4s | 解释 | `FadeIn(explain_2)` | 0.5s |
| 3.9s | 等待理解 | `Wait(2.0)` | 2.0s |
| 5.9s | 高亮等式 | `Indicate(equation_2)` | 0.5s |

### 文案
- 标题: "步骤2: 利用同位角"
- 等式2: "∠ECD = ∠B" (绿色)
- 解释: "CE // AB, 同位角相等"
- 位置:
  - 标题: UP * 5.5
  - 等式: DOWN * 5.5
  - 解释: DOWN * 6.5

### 角度绘制
```python
# ∠ECD: 顶点C, 从CE到CD
angle_ECD = Angle(
    Line(C, E),  # 起始边CE
    Line(C, D),  # 终止边CD
    radius=0.5,
    color=COLOR_INTERIOR_ANGLE_2,
    stroke_width=2,
    stroke_opacity=0.6
)
```

### 清理
- FadeOut: title_step2, explain_2, corresponding_marks
- 保留: angle_ECD, equation_2

---

## Scene 6: 综合推导 (38-50秒)

### 目的
组合两个等式，得出最终结论

### 元素
1. 角度拆分示意
2. 等式推导动画
3. 最终结论

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题 | `FadeIn(title_final)` | 0.4s |
| 0.4s | 提示拆分 | `FadeIn(hint_split)` | 0.5s |
| 0.9s | 高亮外角 | `Indicate(angle_ACD)` | 0.6s |
| 1.5s | 显示拆分 | `Write(split_equation)` | 1.0s |
| 2.5s | 等式1移动 | `equation_1.animate.move_to(...)` | 0.8s |
| 3.3s | 等式2移动 | `equation_2.animate.move_to(...)` | 0.8s |
| 4.1s | 替换符号 | `Transform(...)` | 1.0s |
| 5.1s | 最终等式 | `Write(final_equation)` | 1.2s |
| 6.3s | 庆祝特效 | `Flash(final_equation), Circumscribe(...)` | 1.0s |
| 7.3s | 等待欣赏 | `Wait(2.0)` | 2.0s |

### 文案
- 标题: "综合推导"
- 提示: "外角 = ∠ACE + ∠ECD"
- 拆分: "α = ∠ACE + ∠ECD"
- 最终: "α = ∠A + ∠B ✓" (大字，金色)
- 位置:
  - 标题: UP * 5.5
  - 拆分: DOWN * 3.5
  - 最终: DOWN * 5, 字体大小40

### 推导动画
```python
# 等式组合
equations_group = VGroup(
    equation_1,  # ∠ACE = ∠A
    equation_2,  # ∠ECD = ∠B
    split_equation  # α = ∠ACE + ∠ECD
).arrange(DOWN, buff=0.3).move_to(DOWN * 4)

# 替换动画
final = MathTex(
    r"\alpha = \angle A + \angle B",
    font_size=40,
    color=GOLD
).move_to(DOWN * 5)
```

### 清理
- FadeOut: all previous equations, angles, auxiliary elements except triangle
- 保留: final_equation

---

## Scene 7: 结尾总结 (50-60秒)

### 目的
强化记忆，引导关注

### 元素
1. 定理总结卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 三角形缩小移动 | `triangle.animate.scale(0.6).move_to(UP*3)` | 0.8s |
| 0.8s | 定理卡片 | `FadeIn(theorem_card)` | 0.8s |
| 1.6s | 要点列表 | `Write(key_points)` | 1.2s |
| 2.8s | 作者信息放大 | `Transform(author_info, ...)` | 0.6s |
| 3.4s | 关注提示 | `FadeIn(follow_text), Flash(...)` | 0.8s |
| 4.2s | 装饰动画 | `FadeIn(decorations)` | 0.6s |
| 4.8s | 最终等待 | `Wait(2.0)` | 2.0s |

### 文案
- 定理: "三角形外角定理"
- 要点:
  - "外角 = 两个不相邻内角之和"
  - "关键: 作平行线"
  - "利用内错角和同位角"
- 关注: "关注我, 学更多几何技巧!"
- 位置:
  - 定理卡片: UP * 1
  - 要点: ORIGIN 到 DOWN * 2
  - 关注: DOWN * 5

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | - | 全程保留 |
| triangle | Scene 1 | - | 全程保留 |
| extend_line | Scene 2 | Scene 7 | BC延长线 |
| angle_ACD | Scene 2 | Scene 6 | 外角 |
| angle_A | Scene 2 | Scene 6 | 内角A |
| angle_B | Scene 2 | Scene 6 | 内角B |
| auxiliary_line | Scene 3 | Scene 6 | 辅助线CE |
| parallel_marks | Scene 3 | Scene 6 | 平行标记 |
| angle_ACE | Scene 4 | Scene 6 | 内错角 |
| angle_ECD | Scene 5 | Scene 6 | 同位角 |
| equation_1 | Scene 4 | Scene 6 | 等式1 |
| equation_2 | Scene 5 | Scene 6 | 等式2 |
| final_equation | Scene 6 | Scene 7 | 最终结论 |

---

## 关键技术要点

### 1. 角度方向性
- **必须明确**: 每个角有起始边和终止边
- **Angle类用法**: `Angle(line1, line2, ...)` 从line1逆时针转到line2
- **验证方法**: 视觉检查角度弧是否在正确位置

### 2. 几何精确性
- 所有点坐标在 `setup_geometry()` 中预计算
- 使用向量运算确保平行关系
- 验证函数检查几何关系正确性

### 3. 颜色一致性
- 同一角度始终使用同一颜色
- 相等的角用相同或相近颜色标注
- 辅助线用黄色，主图形用白色

### 4. 动画节奏
- 难点(步骤4-6)每步停留2秒以上
- 简单动作(标注角度)0.8秒即可
- 最终结论停留2秒让学生消化

### 5. 文字位置
- 标题: UP * 5.5 到 UP * 6
- 主要说明: DOWN * 4 到 DOWN * 5
- 次要说明: DOWN * 5.5 到 DOWN * 6.5
- 避免与图形重叠

---

## 预计时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场 | 5s | 5s |
| Scene 2: 标注角度 | 7s | 12s |
| Scene 3: 辅助线 | 6s | 18s |
| Scene 4: 内错角 | 10s | 28s |
| Scene 5: 同位角 | 10s | 38s |
| Scene 6: 推导 | 12s | 50s |
| Scene 7: 结尾 | 10s | 60s |

**总时长**: 约60秒 (TikTok最佳时长)