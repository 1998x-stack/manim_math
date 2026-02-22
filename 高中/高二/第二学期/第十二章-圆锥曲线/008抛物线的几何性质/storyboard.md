# 抛物线的几何性质 - 动画分镜脚本

## 元信息
- 目标时长: 75-85 秒
- 场景数量: 8 个
- 难度等级: 高中（高二）
- 知识点: 抛物线 y²=2px (p>0) 的几何性质

## 颜色配置
```python
COLOR_PARABOLA = "#3498db"      # 蓝色 - 抛物线主体
COLOR_FOCUS = "#e74c3c"         # 红色 - 焦点
COLOR_DIRECTRIX = "#2ecc71"     # 绿色 - 准线
COLOR_CHORD = "#f39c12"         # 橙色 - 弦（通径）
COLOR_LIGHT = "#f1c40f"         # 黄色 - 光线
COLOR_HIGHLIGHT = YELLOW        # 高亮
COLOR_AUXILIARY = GRAY_B        # 辅助线
COLOR_AXIS = WHITE              # 坐标轴
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 参数p | 给定值 | self.p = 1.5 | 焦参数 |
| 焦点F | (p/2, 0, 0) | self.F | 在x轴正半轴 |
| 准线 | x = -p/2 | self.directrix_x | 垂直于x轴 |
| 顶点O | (0, 0, 0) | self.O | 原点 |
| 抛物线点P | (x, ±√(2px), 0) | 动态计算 | 参数方程 |
| 通径端点 | (p/2, ±p, 0) | self.A, self.B | 过焦点垂直于轴 |
| 焦半径 | x + p/2 | 动态 | 点到焦点距离 |

## 边界安全检查
- 坐标轴范围: x ∈ [-2, 6], y ∈ [-4, 4]
- 主内容区: y ∈ [-3, 5]
- 文字区域: y ∈ [-6, -3] 和 y ∈ [5.5, 7]

---

## Scene 1: 开场钩子 (0-4秒)

**目的**: 抓住注意力 + 引出主题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 "为什么卫星天线是抛物面?"
3. 旋转的抛物面示意图

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 卫星天线图标出现 | `FadeIn(satellite_icon, scale=0.5)` | 0.5s |
| 1.6s | 提示文字 | `FadeIn(hint)` | 0.5s |
| 2.6s | 等待理解 | `self.wait(1.0)` | 1.0s |

### 清理
- FadeOut: hook_text, satellite_icon, hint
- 保留: author_info (移至顶部小字)

---

## Scene 2: 抛物线定义 (4-11秒)

**目的**: 建立抛物线的定义和标准方程

### 元素
1. 坐标轴 (x, y)
2. 焦点F标记
3. 准线 (虚线)
4. 动点P的轨迹
5. 定义文字: |PF| = d(P, 准线)

### 几何计算
```python
# 焦点
self.F = np.array([self.p/2, 0, 0])

# 准线 x = -p/2
self.directrix_x = -self.p/2
directrix_start = np.array([self.directrix_x, -4, 0])
directrix_end = np.array([self.directrix_x, 4, 0])

# 动点P在抛物线上: y² = 2px
def parabola_point(x_val):
    if x_val < 0:
        return None
    y_val = np.sqrt(2 * self.p * x_val)
    return np.array([x_val, y_val, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 4.0s | 坐标轴创建 | `Create(axes)` | 1.0s |
| 5.0s | 焦点F出现 | `FadeIn(focus_dot), Flash(focus_dot)` | 0.6s |
| 5.6s | 准线绘制 | `Create(directrix)` | 0.8s |
| 6.4s | 定义文字 | `Write(definition_text)` | 1.0s |
| 7.4s | 动点P轨迹 | `MoveAlongPath` 或 `ValueTracker动画` | 2.5s |
| 9.9s | 方程出现 | `Write(equation: y²=2px)` | 0.8s |
| 10.7s | 等待 | `self.wait(0.3)` | 0.3s |

### 清理
- FadeOut: definition_text (定义文字)
- 保留: axes, focus, directrix, equation (方程移至顶部), parabola

---

## Scene 3: 几何性质 - 范围与对称性 (11-18秒)

**目的**: 展示范围 x≥0, y∈R 和关于x轴对称

### 元素
1. 范围标注 (x≥0 区域高亮)
2. 对称点对 (P₁ 和 P₂)
3. 对称轴标记

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 11.0s | 范围说明文字 | `FadeIn(range_text: "x≥0, y∈R")` | 0.6s |
| 11.6s | x≥0 区域淡入 | `FadeIn(region, fill_opacity=0.2)` | 0.8s |
| 12.4s | 对称性标题 | `Write(symmetry_title)` | 0.5s |
| 12.9s | 选取点P₁ | `FadeIn(P1_dot)` | 0.3s |
| 13.2s | 镜像得P₂ | `Transform(P1.copy(), P2)` | 0.8s |
| 14.0s | 连线展示 | `Create(symmetric_line)` | 0.5s |
| 14.5s | x轴高亮 | `axes.x_axis.animate.set_color(YELLOW)` | 0.4s |
| 14.9s | 说明文字 | `FadeIn(explanation)` | 0.6s |
| 15.5s | 等待理解 | `self.wait(2.0)` | 2.0s |

### 清理
- FadeOut: range_text, region, symmetry_title, P1, P2, symmetric_line, explanation
- 恢复: axes.x_axis 颜色

---

## Scene 4: 离心率 e=1 (18-24秒)

**目的**: 强调抛物线离心率是定值1

### 元素
1. 离心率公式: e = |PF| / d(P, 准线)
2. 选取抛物线上任意点P
3. 测量|PF|和d
4. 验证比值恒为1

### 几何计算
```python
# 选取点P
P_x = 2.0
P_y = np.sqrt(2 * self.p * P_x)
P = np.array([P_x, P_y, 0])

# 焦半径
PF = np.linalg.norm(P - self.F)

# 到准线距离
d = P_x - self.directrix_x

# 验证 e = PF / d = 1
e = PF / d
```

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 18.0s | 标题: 离心率 | `Write(title: "离心率")` | 0.5s |
| 18.5s | 公式出现 | `Write(formula: e = |PF|/d)` | 0.8s |
| 19.3s | 点P出现 | `FadeIn(P_dot)` | 0.3s |
| 19.6s | 画|PF| | `Create(line_PF)` | 0.6s |
| 20.2s | 画d (垂线) | `Create(perpendicular)` | 0.6s |
| 20.8s | 标注长度 | `FadeIn(PF_label, d_label)` | 0.5s |
| 21.3s | 计算过程 | `Write(calculation: e=1)` | 1.0s |
| 22.3s | 高亮结果 | `Indicate(result)` | 0.5s |
| 22.8s | 等待 | `self.wait(1.0)` | 1.0s |

### 清理
- FadeOut: title, formula, P_dot, line_PF, perpendicular, labels, calculation

---

## Scene 5: 通径 (24-32秒)

**目的**: 展示通径的定义和长度2p

### 元素
1. 通径 AB (过焦点垂直于轴的弦)
2. 端点A, B坐标
3. 长度标注 |AB| = 2p

### 几何计算
```python
# 通径端点 (过焦点F，垂直于x轴)
# F = (p/2, 0, 0)
# 代入y² = 2px: y² = 2p(p/2) = p²
# y = ±p

A = np.array([self.p/2, self.p, 0])
B = np.array([self.p/2, -self.p, 0])

# 验证长度
AB_length = np.linalg.norm(B - A)  # 应该 = 2p
```

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 24.0s | 标题: 通径 | `Write(title)` | 0.5s |
| 24.5s | 定义文字 | `FadeIn(definition)` | 0.6s |
| 25.1s | 焦点闪烁 | `Flash(focus)` | 0.4s |
| 25.5s | 画通径AB | `Create(chord_AB)` | 1.0s |
| 26.5s | 端点A, B | `FadeIn(A_dot, B_dot)` | 0.4s |
| 26.9s | 标注坐标 | `FadeIn(coord_labels)` | 0.6s |
| 27.5s | Brace标注 | `Create(brace), Write(length_label: 2p)` | 1.0s |
| 28.5s | 公式框 | `FadeIn(formula_box: 通径=2p)` | 0.8s |
| 29.3s | 等待理解 | `self.wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, definition, chord_AB, A_dot, B_dot, coord_labels, brace, length_label, formula_box

---

## Scene 6: 焦半径公式 (32-41秒)

**目的**: 推导并验证焦半径公式 |PF| = x₀ + p/2

### 元素
1. 抛物线上任意点P(x₀, y₀)
2. 焦点F(p/2, 0)
3. 焦半径|PF|
4. 到准线距离d = x₀ + p/2
5. 由e=1推导公式

### 几何计算
```python
# 选取点P
x0 = 3.0
y0 = np.sqrt(2 * self.p * x0)
P = np.array([x0, y0, 0])

# 焦半径 |PF|
PF = np.linalg.norm(P - self.F)

# 到准线距离 d
d = x0 - self.directrix_x  # = x0 + p/2

# 验证: |PF| = d (因为e=1)
# 因此: |PF| = x0 + p/2
```

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 标题: 焦半径 | `Write(title)` | 0.5s |
| 32.5s | 点P(x₀,y₀) | `FadeIn(P_dot, label)` | 0.5s |
| 33.0s | 画|PF| | `Create(line_PF)` | 0.6s |
| 33.6s | 回顾e=1 | `FadeIn(recall: "因为e=1")` | 0.7s |
| 34.3s | 所以|PF|=d | `Write(step1)` | 0.8s |
| 35.1s | 画到准线 | `Create(perpendicular)` | 0.6s |
| 35.7s | d = x₀+p/2 | `Write(step2)` | 0.8s |
| 36.5s | 推导框 | `SurroundingRectangle(formula)` | 0.5s |
| 37.0s | 结论出现 | `Write(conclusion: |PF|=x₀+p/2)` | 1.0s |
| 38.0s | 高亮公式 | `Indicate(conclusion)` | 0.5s |
| 38.5s | 等待 | `self.wait(2.0)` | 2.0s |

### 清理
- FadeOut: title, P_dot, label, line_PF, recall, step1, step2, perpendicular, conclusion

---

## Scene 7: 光学性质 (41-54秒)

**目的**: 展示抛物线的反射性质 - 平行光线汇聚于焦点

### 元素
1. 3-4条平行于轴的入射光线
2. 反射光线都通过焦点
3. 法线 (切线的垂线)
4. 应用说明: 卫星天线、汽车前灯

### 几何计算
```python
# 选取抛物线上的点P
P = np.array([x, np.sqrt(2*self.p*x), 0])

# 切线方向: dy/dx = p/y
slope = self.p / P[1]
tangent_vec = np.array([1, slope, 0])
tangent_vec_normalized = tangent_vec / np.linalg.norm(tangent_vec)

# 法线方向 (垂直于切线)
normal_vec = np.array([-slope, 1, 0])
normal_vec_normalized = normal_vec / np.linalg.norm(normal_vec)

# 入射光线: 平行于x轴，从左侧射向P
incident_ray = Arrow(P + LEFT*2, P, color=YELLOW)

# 反射光线: 从P指向焦点F
reflected_ray = Arrow(P, self.F, color=YELLOW)
```

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 41.0s | 标题: 光学性质 | `Write(title)` | 0.6s |
| 41.6s | 说明文字 | `FadeIn(explanation)` | 0.7s |
| 42.3s | 选点P₁ | `FadeIn(P1)` | 0.3s |
| 42.6s | 入射光线₁ | `GrowArrow(ray1_in)` | 0.8s |
| 43.4s | 画法线 | `Create(normal1)` | 0.5s |
| 43.9s | 反射光线₁ | `GrowArrow(ray1_out)` | 0.8s |
| 44.7s | 第2条光 (P₂) | 重复上述, 同时进行 | 1.5s |
| 46.2s | 第3条光 (P₃) | 重复 | 1.5s |
| 47.7s | 焦点闪烁 | `Flash(focus), Indicate(focus)` | 0.6s |
| 48.3s | 结论文字 | `Write(conclusion: "都通过焦点F")` | 0.8s |
| 49.1s | 应用场景 | `FadeIn(application_icons)` | 1.0s |
| 50.1s | 等待理解 | `self.wait(3.0)` | 3.0s |

### 清理
- FadeOut: title, explanation, rays, normals, P_dots, conclusion, application_icons

---

## Scene 8: 总结 + 片尾 (54-75秒)

**目的**: 回顾要点 + 作者关注引导

### 元素
1. 知识点卡片 (5个要点)
2. 作者信息放大
3. 关注提示
4. 抛物线装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 54.0s | 抛物线缩小 | `parabola.animate.scale(0.5).to_edge(UP)` | 0.8s |
| 54.8s | 卡片1滑入 | `card1.animate.shift(RIGHT*0)` | 0.4s |
| 55.2s | 卡片2 | 同上 | 0.4s |
| 55.6s | 卡片3 | 同上 | 0.4s |
| 56.0s | 卡片4 | 同上 | 0.4s |
| 56.4s | 卡片5 | 同上 | 0.4s |
| 56.8s | 等待阅读 | `self.wait(2.5)` | 2.5s |
| 59.3s | 卡片淡出 | `FadeOut(cards)` | 0.5s |
| 59.8s | 作者名放大 | `Transform(author_info, large_author)` | 0.8s |
| 60.6s | 关注文字 | `Write(follow_text)` | 1.0s |
| 61.6s | 抛物线装饰 | `旋转动画` | 2.0s |
| 63.6s | 小图标 | `FadeIn(icons)` | 0.8s |
| 64.4s | 等待 | `self.wait(2.0)` | 2.0s |
| 66.4s | 全部淡出 | `self.play(*[FadeOut(m) for m in self.mobjects])` | 1.5s |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保留 |
| axes | Scene 2 | Scene 8 | 坐标轴 |
| parabola | Scene 2 | Scene 8 | 主曲线 |
| focus | Scene 2 | Scene 8 | 焦点F |
| directrix | Scene 2 | Scene 8 | 准线 |
| equation | Scene 2 | Scene 8 | y²=2px (移至顶部) |
| range_region | Scene 3 | Scene 3 | 临时 |
| P_dots | 各场景 | 各场景 | 临时演示点 |
| chord_AB | Scene 5 | Scene 5 | 通径 |
| light_rays | Scene 7 | Scene 7 | 光线 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键验证点

### 1. 焦点和准线位置验证
```python
# 焦点应在 (p/2, 0)
assert np.allclose(self.F, [self.p/2, 0, 0])

# 准线 x = -p/2
assert np.isclose(self.directrix_x, -self.p/2)
```

### 2. 抛物线方程验证
```python
# 任意点P(x, y)应满足 y² = 2px
x, y = P[0], P[1]
assert np.isclose(y**2, 2 * self.p * x, atol=1e-6)
```

### 3. 通径长度验证
```python
AB_length = np.linalg.norm(self.B - self.A)
assert np.isclose(AB_length, 2 * self.p)
```

### 4. 焦半径公式验证
```python
PF = np.linalg.norm(P - self.F)
expected = P[0] + self.p/2
assert np.isclose(PF, expected, atol=1e-6)
```

### 5. 边界检查
```python
# 确保所有元素在安全区域
for obj in [parabola, focus, labels]:
    bbox = obj.get_bounding_box()
    assert bbox[0][0] >= -4.0 and bbox[1][0] <= 4.0
    assert bbox[0][1] >= -7.0 and bbox[1][1] <= 7.0
```

---

## 注意事项

1. **参数p的选择**: 使用 p=1.5，既能清晰展示焦点，又不会导致抛物线过于狭窄
2. **坐标轴范围**: x ∈ [-2, 6]，y ∈ [-4, 4]，确保所有关键点可见
3. **光线动画**: 使用 `GrowArrow` 而非 `Create`，更符合光线传播
4. **文字大小**: 主标题36px，说明文字22-24px，标签20px
5. **等待时间**: 关键概念（离心率、焦半径）需要2秒理解时间
6. **颜色一致性**: 焦点始终红色，准线始终绿色，抛物线蓝色