# 两角和与差的三角函数 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 高一
- 知识点: 两角和差公式、三角恒等变换

## 颜色配置
```python
COLOR_ALPHA = "#e74c3c"           # 红色 - 角α
COLOR_BETA = "#3498db"            # 蓝色 - 角β
COLOR_SUM = "#2ecc71"             # 绿色 - 和角α+β
COLOR_DIFF = "#9b59b6"            # 紫色 - 差角α-β
COLOR_UNIT_CIRCLE = WHITE         # 白色 - 单位圆
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
COLOR_FORMULA = "#f39c12"         # 橙色 - 公式
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 单位圆中心 | ORIGIN + DOWN*1 | self.circle_center |
| 单位圆半径 | 1.8 | self.radius |
| 角α示例 | 45° = π/4 | self.alpha |
| 角β示例 | 30° = π/6 | self.beta |
| 点A (角α) | (cos α, sin α) | self.point_A |
| 点B (角β) | (cos β, sin β) | self.point_B |
| 点C (角α+β) | (cos(α+β), sin(α+β)) | self.point_C |
| 点D (角α-β) | (cos(α-β), sin(α-β)) | self.point_D |
| 坐标轴范围 | x: [-2.5, 2.5], y: [-2.5, 2.5] | - |

## 角度方向验证
| 角度 | 度数 | 弧度 | 是否>90° | 是否>180° | other_angle |
|------|------|------|----------|-----------|-------------|
| α | 45° | π/4 | ❌ | ❌ | False |
| β | 30° | π/6 | ❌ | ❌ | False |
| α+β | 75° | 5π/12 | ❌ | ❌ | False |
| α-β | 15° | π/12 | ❌ | ❌ | False |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 引出两角和的问题

### 元素
1. 作者信息 (顶部)
2. 钩子问题 "cos(45° + 30°) = ?"
3. 思考动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 问题书写 | `Write(hook_question)` |
| 1.5s | 问号闪烁 | `Flash(question_mark, color=YELLOW)` |
| 2.5s | 提示文字 | `FadeIn(hint_text)` |
| 3.5s | 清理 | `FadeOut(hook_question, hint_text)` |

### 清理
- FadeOut: hook_question, hint_text
- 保留: author_info

---

## Scene 2: 单位圆介绍 (8秒)
**目的**: 建立单位圆坐标系统

### 元素
1. 坐标轴
2. 单位圆
3. 关键角度标注 (0°, 90°, 180°, 270°)
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.6s | 创建坐标轴 | `Create(axes)` |
| 1.6s | 绘制单位圆 | `Create(unit_circle)` |
| 2.6s | 标注0° | `FadeIn(label_0)` |
| 3.0s | 标注90° | `FadeIn(label_90)` |
| 3.4s | 标注180° | `FadeIn(label_180)` |
| 3.8s | 标注270° | `FadeIn(label_270)` |
| 5.0s | 说明文字 | `Write(explanation)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, explanation
- 保留: axes, unit_circle, angle_labels

---

## Scene 3: 角α和角β的可视化 (10秒)
**目的**: 在单位圆上标注两个角

### 元素
1. 角α = 45° (红色扇形)
2. 角β = 30° (蓝色扇形)
3. 点A、点B
4. 标签

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.8s | 绘制角α | `Create(angle_alpha)` |
| 1.8s | 半径OA | `Create(radius_OA)` |
| 2.4s | 点A | `FadeIn(point_A_dot, scale=0.5)` |
| 3.0s | 标签α | `Write(label_alpha)` |
| 4.0s | 绘制角β | `Create(angle_beta)` |
| 5.0s | 半径OB | `Create(radius_OB)` |
| 5.6s | 点B | `FadeIn(point_B_dot, scale=0.5)` |
| 6.2s | 标签β | `Write(label_beta)` |
| 7.5s | 坐标标注 | `FadeIn(coords_A, coords_B)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, coords_A, coords_B
- 保留: angle_alpha, angle_beta, point_A_dot, point_B_dot, radius_OA, radius_OB, labels

---

## Scene 4: cos(α-β) 几何证明 (12秒)
**目的**: 使用距离公式推导余弦差角公式

### 元素
1. 距离 AB
2. 两点距离公式
3. 推导步骤
4. 最终公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.8s | 连线AB | `Create(line_AB)` |
| 1.6s | 距离公式 | `Write(distance_formula)` |
| 3.0s | 展开计算 | `TransformMatchingTex(step1, step2)` |
| 4.5s | 化简 | `TransformMatchingTex(step2, step3)` |
| 6.0s | 余弦定理 | `Write(cosine_law)` |
| 7.5s | 对比 | `Indicate(comparison)` |
| 9.0s | 结论公式 | `Write(conclusion)` |
| 10.5s | 框选公式 | `Create(box)` |
| 11.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, distance_formula, steps, cosine_law, line_AB
- 保留: conclusion (移到顶部)

---

## Scene 5: 余弦和角公式 (8秒)
**目的**: 展示 cos(α+β) 公式

### 元素
1. cos(α+β) 公式
2. 与 cos(α-β) 的关系
3. 公式框

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.8s | 说明 | `FadeIn(explanation)` |
| 2.0s | 公式推导 | `Write(formula_derivation)` |
| 3.5s | 变换 | `TransformMatchingTex(step1, step2)` |
| 5.0s | 最终公式 | `Write(final_formula)` |
| 6.5s | 框选 | `Create(box)` |
| 7.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, explanation, derivation
- 保留: final_formula (移到列表)

---

## Scene 6: 正弦和差公式 (10秒)
**目的**: 展示 sin(α±β) 公式

### 元素
1. sin(α+β) 公式
2. sin(α-β) 公式
3. 图示（可选）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.8s | 说明 | `FadeIn(explanation)` |
| 2.0s | sin(α+β) | `Write(sin_sum)` |
| 3.5s | 框选 | `Create(box1)` |
| 4.5s | sin(α-β) | `Write(sin_diff)` |
| 6.0s | 框选 | `Create(box2)` |
| 7.0s | 对比符号 | `Indicate(plus_sign, minus_sign)` |
| 8.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, explanation
- 保留: formulas (移到列表)

---

## Scene 7: 正切和差公式 (8秒)
**目的**: 展示 tan(α±β) 公式

### 元素
1. tan(α+β) 公式
2. tan(α-β) 公式
3. 条件说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.8s | tan(α+β) | `Write(tan_sum)` |
| 2.5s | 框选 | `Create(box1)` |
| 3.5s | tan(α-β) | `Write(tan_diff)` |
| 5.0s | 框选 | `Create(box2)` |
| 6.0s | 条件说明 | `FadeIn(condition)` |
| 7.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, condition
- 保留: formulas

---

## Scene 8: 公式总结 + 片尾 (10秒)
**目的**: 汇总所有公式，引导关注

### 元素
1. 六个公式卡片
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理圆形 | `FadeOut(circle, axes, angles)` |
| 0.6s | 标题 | `Write(title)` |
| 1.2s | 公式列表淡入 | `FadeIn(formula_list)` |
| 3.0s | 逐个高亮 | `Indicate(formula1, formula2, ...)` |
| 5.5s | 等待 | `Wait(1.0)` |
| 6.5s | 淡出公式 | `FadeOut(title, formula_list)` |
| 7.2s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 8.0s | 关注提示 | `FadeIn(follow_text)` |
| 9.5s | 等待结束 | `Wait(1.0)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保持顶部 |
| unit_circle | Scene 2 | Scene 8 | 主要参考 |
| axes | Scene 2 | Scene 8 | 坐标系 |
| angle_alpha | Scene 3 | Scene 8 | 角α |
| angle_beta | Scene 3 | Scene 8 | 角β |
| point_A_dot | Scene 3 | Scene 8 | 点A |
| point_B_dot | Scene 3 | Scene 8 | 点B |
| cos_diff_formula | Scene 4 | Scene 8 | 余弦差公式 |
| cos_sum_formula | Scene 5 | Scene 8 | 余弦和公式 |
| sin_formulas | Scene 6 | Scene 8 | 正弦公式 |
| tan_formulas | Scene 7 | Scene 8 | 正切公式 |

---

## 单位圆配置

### 圆心和半径
```python
circle_center = DOWN * 1.0
radius = 1.8  # 缩放后适配竖屏
```

### 关键点计算（以半径1.8为基准）
```python
# 角α = 45° = π/4
point_A = circle_center + radius * np.array([np.cos(π/4), np.sin(π/4), 0])
# ≈ (0, -1) + 1.8 * (0.707, 0.707, 0) = (1.273, -0.273, 0)

# 角β = 30° = π/6
point_B = circle_center + radius * np.array([np.cos(π/6), np.sin(π/6), 0])
# ≈ (0, -1) + 1.8 * (0.866, 0.5, 0) = (1.559, -0.1, 0)

# 角α+β = 75° = 5π/12
point_C = circle_center + radius * np.array([np.cos(5π/12), np.sin(5π/12), 0])
# ≈ (0, -1) + 1.8 * (0.259, 0.966, 0) = (0.466, 0.739, 0)

# 角α-β = 15° = π/12
point_D = circle_center + radius * np.array([np.cos(π/12), np.sin(π/12), 0])
# ≈ (0, -1) + 1.8 * (0.966, 0.259, 0) = (1.739, -0.534, 0)
```

---

## 边界检查清单
- [ ] 作者信息在 y = 7
- [ ] 标题在 y ∈ [5.5, 6.5]
- [ ] 单位圆中心在 y = -1
- [ ] 单位圆半径 1.8，范围 y ∈ [-2.8, 0.8]
- [ ] 单位圆 x ∈ [-1.8, 1.8]（圆心在x=0）
- [ ] 公式显示区域 y ∈ [2, 5]
- [ ] 所有元素 x ∈ [-4, 4]

---

## 字体大小规范
| 元素类型 | 字体大小 |
|---------|---------|
| 作者信息 | 20 |
| 场景标题 | 36 |
| 副标题/说明 | 24 |
| 公式主体 | 32 |
| 公式小字 | 24 |
| 角度标签 | 22 |
| 坐标标注 | 18 |
| 警告/提示 | 26 |

---

## Angle 方向配置

### 角α (45°，从x轴正方向逆时针)
```python
angle_alpha = Angle.from_three_points(
    circle_center + radius * RIGHT,  # x轴正方向
    circle_center,                   # 圆心
    point_A,                         # 角α终边
    radius=0.5,
    other_angle=False,  # 逆时针，< 180°
    color=COLOR_ALPHA
)
```

### 角β (30°，从x轴正方向逆时针)
```python
angle_beta = Angle.from_three_points(
    circle_center + radius * RIGHT,
    circle_center,
    point_B,
    radius=0.4,
    other_angle=False,  # 逆时针，< 180°
    color=COLOR_BETA
)
```

---

## 时间轴总览
```
0-4s:    开场钩子
4-12s:   单位圆介绍
12-22s:  角α和角β可视化
22-34s:  cos(α-β) 几何证明
34-42s:  cos(α+β) 公式
42-52s:  sin(α±β) 公式
52-60s:  tan(α±β) 公式
60-70s:  公式总结 + 片尾
总计: ~70秒
```

---

## 注意事项

### 角度计算精度
- 所有角度使用弧度制
- π/4 = 0.7853981633974483
- π/6 = 0.5235987755982988
- 5π/12 = 1.3089969389957472
- π/12 = 0.2617993877991494

### 点位置验证
```python
# 验证所有点在单位圆上
def verify_on_circle(point, center, radius):
    distance = np.linalg.norm(point - center)
    return abs(distance - radius) < 1e-6
```

### LaTeX 注意
- 不在 MathTex 中使用中文
- 使用 `\alpha`, `\beta` 等希腊字母
- 使用 `\pm`, `\mp` 表示正负号
- 度数用 `^\circ`