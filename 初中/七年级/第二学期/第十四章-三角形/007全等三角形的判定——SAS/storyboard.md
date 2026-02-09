# SAS全等判定教学动画 - 分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 知识点: SAS（边角边）全等判定
- 目标观众: 七年级学生

## 颜色配置
```python
COLOR_TRIANGLE_1 = "#3498db"      # 蓝色 - 第一个三角形
COLOR_TRIANGLE_2 = "#e74c3c"      # 红色 - 第二个三角形
COLOR_HIGHLIGHT = YELLOW          # 高亮颜色
COLOR_EQUAL_MARK = "#2ecc71"      # 绿色 - 相等标记
COLOR_ANGLE_MARK = "#f39c12"      # 橙色 - 角度标记
COLOR_AUXILIARY = GRAY_B          # 辅助线
COLOR_WRONG = "#c0392b"           # 错误示例红色
```

## 几何预计算清单

### 三角形ABC（蓝色）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 基准点 [-2.5, 0, 0] * SCALE + OFFSET | self.A1 |
| 顶点B | [2.5, 0, 0] * SCALE + OFFSET | self.B1 |
| 顶点C | [0, 2.5, 0] * SCALE + OFFSET | self.C1 |
| 边AB长度 | np.linalg.norm(B1 - A1) | self.AB1 |
| 边AC长度 | np.linalg.norm(C1 - A1) | self.AC1 |
| 角A度数 | 使用 angle_between_vectors | self.angle_A1 |

### 三角形DEF（红色）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点D | [0.5, -2.5, 0] * SCALE + OFFSET | self.D |
| 顶点E | 基于DE=AB计算 | self.E |
| 顶点F | 基于DF=AC且∠D=∠A计算 | self.F |

### 验证约束
- AB1 == DE (边1相等)
- AC1 == DF (边2相等)
- angle_A1 == angle_D (夹角相等)

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题："两个三角形什么时候全等？"
3. 两个看起来相似的三角形淡入

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字打字效果 | `Write(hook_text, run_time=1.0)` |
| 1.5s | 两个三角形创建 | `Create(triangle1), Create(triangle2)` |
| 3.0s | 三角形移动到左右位置 | `triangle1.animate.shift(LEFT*2.5)` |
| 4.0s | 等待 | `Wait(1.0)` |

### 坐标计算
```python
# 三角形1（蓝色）- 左侧
self.A1 = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET + LEFT * 2.5
self.B1 = np.array([2.5, 0, 0]) * self.SCALE + self.OFFSET + LEFT * 2.5
self.C1 = np.array([0, 2.5, 0]) * self.SCALE + self.OFFSET + LEFT * 2.5

# 三角形2（红色）- 右侧
# 初始位置相同，后移动
```

### 清理
- FadeOut: hook_text
- 保留: triangles, author_info

---

## Scene 2: 引入SAS概念 (5-12秒)
**目的**: 介绍SAS判定法则

### 元素
1. 标题："SAS判定法则"
2. 定义文字："两边及其夹角对应相等"
3. 高亮显示"夹角"二字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题写入 | `Write(title)` |
| 5.8s | 定义淡入 | `FadeIn(definition)` |
| 6.5s | "夹角"高亮 | `Indicate(key_word, color=YELLOW)` |
| 8.0s | 公式显示 | `Write(formula)` |
| 10.0s | 等待理解 | `Wait(2.0)` |

### 公式
```python
formula = MathTex(
    r"AB", r"=", r"DE", r",\,",
    r"\angle A", r"=", r"\angle D", r",\,",
    r"AC", r"=", r"DF"
)
# AB, DE 用蓝色
# ∠A, ∠D 用橙色
# AC, DF 用绿色
```

### 清理
- FadeOut: title, definition, formula
- 保留: triangles

---

## Scene 3: 标记第一条边AB=DE (12-20秒)
**目的**: 展示第一对相等的边

### 元素
1. 高亮AB和DE边
2. 相等标记（双短线）
3. 长度标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | AB边高亮 | `triangle1[0].animate.set_color(YELLOW)` |
| 12.5s | DE边高亮 | `triangle2[0].animate.set_color(YELLOW)` |
| 13.0s | 显示相等标记 | `Create(equal_mark_AB)` |
| 13.5s | 显示长度值 | `Write(length_label)` |
| 15.0s | 说明文字 | `FadeIn(explain_text)` |
| 17.0s | 等待 | `Wait(2.0)` |

### 相等标记计算
```python
# AB边的中点
M_AB = (self.A1 + self.B1) / 2

# 垂直于AB的方向
vec_AB = self.B1 - self.A1
perp_AB = np.array([-vec_AB[1], vec_AB[0], 0])
perp_AB_unit = perp_AB / np.linalg.norm(perp_AB)

# 双短线位置
mark_offset = 0.2
line1_start = M_AB + perp_AB_unit * mark_offset
line1_end = M_AB - perp_AB_unit * mark_offset
```

### 清理
- FadeOut: equal_marks, length_labels, explain_text
- 边恢复原色: set_color(COLOR_TRIANGLE_1)

---

## Scene 4: 标记夹角∠A=∠D (20-30秒)
**目的**: 强调"夹角"概念的重要性

### 元素
1. 角度弧线
2. 角度标记（相同弧数）
3. 重点提示："必须是夹角！"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 20.0s | 创建角度弧∠A | `Create(angle_A_arc)` |
| 20.5s | 创建角度弧∠D | `Create(angle_D_arc)` |
| 21.0s | 角度标记 | `Create(angle_marks)` |
| 22.0s | 角度值标注 | `Write(angle_label)` |
| 23.0s | 闪烁"夹角"提示 | `Flash(key_point)` |
| 25.0s | 说明文字 | `FadeIn(explain)` |
| 28.0s | 等待 | `Wait(2.0)` |

### 角度弧计算（关键！）
```python
# 使用 Angle.from_three_points 确保方向正确
angle_A = Angle.from_three_points(
    self.B1,  # 第一条边上的点
    self.A1,  # 顶点
    self.C1,  # 第二条边上的点
    radius=0.5,
    color=COLOR_ANGLE_MARK
)

# 验证角度方向
v1 = self.B1 - self.A1
v2 = self.C1 - self.A1
cross_z = v1[0] * v2[1] - v1[1] * v2[0]

# 如果 cross_z < 0，需要使用 other_angle=True
if cross_z < 0:
    angle_A = Angle.from_three_points(
        self.B1, self.A1, self.C1,
        radius=0.5,
        other_angle=True,
        color=COLOR_ANGLE_MARK
    )
```

### 清理
- FadeOut: angle_arcs, angle_labels, explain
- 保留: triangles（角度标记可保留）

---

## Scene 5: 标记第二条边AC=DF (30-38秒)
**目的**: 完成SAS三要素

### 元素
1. 高亮AC和DF边
2. 相等标记（三短线，区别于AB）
3. 汇总说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 30.0s | AC边高亮 | `triangle1[2].animate.set_color(YELLOW)` |
| 30.5s | DF边高亮 | `triangle2[2].animate.set_color(YELLOW)` |
| 31.0s | 显示相等标记 | `Create(equal_mark_AC)` |
| 31.5s | 显示长度值 | `Write(length_label)` |
| 33.0s | 汇总文字 | `FadeIn(summary_text)` |
| 36.0s | 等待 | `Wait(2.0)` |

### 汇总文字
```
两边: AB=DE, AC=DF ✓
夹角: ∠A=∠D ✓
结论: △ABC ≌ △DEF (SAS)
```

### 清理
- FadeOut: equal_marks, labels
- 保留: triangles

---

## Scene 6: 重合验证 (38-50秒)
**目的**: 视觉化全等概念

### 元素
1. 三角形DEF移动并旋转
2. 完美重合动画
3. 全等符号 ≌

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 38.0s | 复制triangle2 | `triangle2_copy = triangle2.copy()` |
| 38.5s | 移动到triangle1位置 | `Rotate + shift组合` |
| 41.0s | 完美重合 | 调整透明度展示重合 |
| 43.0s | 全等符号出现 | `Write(congruence_symbol)` |
| 45.0s | 闪烁效果 | `Flash(symbol)` |
| 48.0s | 等待 | `Wait(2.0)` |

### 重合计算
```python
# 计算旋转角度
angle_diff = self.angle_D - self.angle_A

# 计算平移向量
translation = self.A1 - self.D

# 组合变换
triangle2_copy.rotate(angle_diff, about_point=self.D)
triangle2_copy.shift(translation)
```

### 清理
- FadeOut: triangle2_copy
- 保留: triangle1, congruence_symbol

---

## Scene 7: 错误示例SSA (50-60秒)
**目的**: 强调"夹角"的重要性

### 元素
1. 标题："注意！SSA不能判定全等"
2. 反例三角形
3. 警告符号

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 50.0s | 警告标题 | `Write(warning_title, color=RED)` |
| 51.0s | 创建SSA示例 | `Create(wrong_triangle)` |
| 53.0s | 标记"非夹角" | 用红色虚线标注 |
| 55.0s | 说明文字 | `FadeIn(explanation)` |
| 58.0s | 等待 | `Wait(2.0)` |

### SSA反例构造
```python
# 两边相等但角不是夹角
# 可构造出两个不同的三角形
```

### 清理
- FadeOut: all wrong examples
- 保留: 空场景准备片尾

---

## Scene 8: 片尾 (60-75秒)
**目的**: 总结 + 关注引导

### 元素
1. 核心要点回顾
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 60.0s | 要点总结 | `Write(key_points)` |
| 63.0s | 作者信息放大 | `Transform(author_info)` |
| 65.0s | 关注提示 | `FadeIn(follow_text)` |
| 68.0s | 装饰动画 | 三角形图标旋转 |
| 72.0s | 淡出 | `FadeOut(all)` |

### 要点总结
```
SAS判定要点:
✓ 两边对应相等
✓ 夹角对应相等
✓ 顺序: 边-角-边
✗ SSA不能判定全等
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留，最后放大 |
| triangle1 (ABC) | Scene 1 | Scene 7 | 蓝色主三角形 |
| triangle2 (DEF) | Scene 1 | Scene 7 | 红色对比三角形 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| title_SAS | Scene 2 | Scene 2 | SAS标题 |
| formula | Scene 2 | Scene 2 | 数学公式 |
| equal_marks_AB | Scene 3 | Scene 3 | 边AB相等标记 |
| angle_marks | Scene 4 | Scene 6 | 角度标记 |
| equal_marks_AC | Scene 5 | Scene 5 | 边AC相等标记 |
| triangle2_copy | Scene 6 | Scene 6 | 重合验证用 |
| wrong_example | Scene 7 | Scene 7 | SSA错误示例 |
| summary | Scene 8 | Scene 8 | 最后总结 |

---

## 几何验证检查点

### 验证项1: 边长相等性
```python
assert abs(self.AB1 - self.DE) < 1e-6, "AB ≠ DE"
assert abs(self.AC1 - self.DF) < 1e-6, "AC ≠ DF"
```

### 验证项2: 角度相等性
```python
assert abs(self.angle_A1 - self.angle_D) < 1e-6, "∠A ≠ ∠D"
```

### 验证项3: 重合验证
```python
# 变换后三角形2的顶点应与三角形1重合
assert np.linalg.norm(transformed_D - self.A1) < 1e-6
assert np.linalg.norm(transformed_E - self.B1) < 1e-6
assert np.linalg.norm(transformed_F - self.C1) < 1e-6
```

---

## 动画节奏参考

| 场景 | 时长 | 节奏 |
|------|------|------|
| Scene 1 | 5s | 快速吸引 |
| Scene 2 | 7s | 中速讲解 |
| Scene 3 | 8s | 慢速标注 |
| Scene 4 | 10s | 慢速强调（重点）|
| Scene 5 | 8s | 中速补充 |
| Scene 6 | 12s | 慢速验证（高潮）|
| Scene 7 | 10s | 中速警告 |
| Scene 8 | 15s | 慢速总结 |

**总时长**: 75秒

---

## 配色方案最终确认

```python
# 全局背景
BACKGROUND = "#1a1a2e"

# 主要元素
COLOR_TRIANGLE_1 = "#3498db"      # 蓝色
COLOR_TRIANGLE_2 = "#e74c3c"      # 红色
COLOR_HIGHLIGHT = YELLOW          # 黄色高亮
COLOR_EQUAL_MARK = "#2ecc71"      # 绿色相等标记
COLOR_ANGLE_MARK = "#f39c12"      # 橙色角度
COLOR_AUXILIARY = GRAY_B          # 灰色辅助
COLOR_WRONG = "#c0392b"           # 深红色警告

# 文字
COLOR_TITLE = GOLD                # 金色标题
COLOR_TEXT = WHITE                # 白色正文
COLOR_CAPTION = GRAY_A            # 浅灰说明
```
