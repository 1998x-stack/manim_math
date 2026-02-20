# 圆与圆的位置关系 - 动画分镜脚本

## 元信息
- 目标时长: 75-90秒
- 场景数量: 9个
- 难度等级: 初中进阶
- 知识点: 两圆的五种位置关系

## 颜色配置
```python
COLOR_CIRCLE_1 = "#3498db"      # 蓝色 - 大圆
COLOR_CIRCLE_2 = "#e74c3c"      # 红色 - 小圆
COLOR_DISTANCE = "#2ecc71"      # 绿色 - 圆心距
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
COLOR_TANGENT = "#f39c12"       # 橙色 - 切点/交点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 数值 |
|------|---------|---------|------|
| 大圆圆心O₁ | 固定位置 | self.O1 | (-1.2, 1.5, 0) |
| 小圆圆心O₂ | 根据d计算 | self.O2_* | 各场景不同 |
| 大圆半径R | 固定值 | self.R | 1.5 |
| 小圆半径r | 固定值 | self.r | 1.0 |
| 圆心距d(外离) | > R+r | self.d_separate | 3.0 |
| 圆心距d(外切) | = R+r | self.d_external_tangent | 2.5 |
| 圆心距d(相交) | R-r < d < R+r | self.d_intersect | 1.8 |
| 圆心距d(内切) | = R-r | self.d_internal_tangent | 0.5 |
| 圆心距d(内含) | < R-r | self.d_contain | 0.2 |

## 关键验证点
- ✅ 外离: d=3.0 > R+r=2.5 ✓
- ✅ 外切: d=2.5 = R+r=2.5 ✓
- ✅ 相交: 0.5 < d=1.8 < 2.5 ✓
- ✅ 内切: d=0.5 = R-r=0.5 ✓
- ✅ 内含: d=0.2 < R-r=0.5 ✓

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力

### 元素
1. 作者信息
2. 钩子问题："两个圆相遇有几种方式?"
3. 两圆快速闪现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子文字 | `Write(hook_text)` |
| 1.5s | 大圆淡入 | `FadeIn(circle1)` |
| 2.0s | 小圆从右侧进入 | `circle2.animate.shift()` |
| 3.0s | 两圆动态移动 | `AnimationGroup()` |
| 4.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text
- 保留: circles, author_info

---

## Scene 2: 基础概念 (5-12秒)
**目的**: 建立圆心、半径、圆心距概念

### 元素
1. 大圆O₁、半径R
2. 小圆O₂、半径r
3. 圆心距d
4. 连线O₁O₂

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标记O₁ | `FadeIn(O1_dot), Write(O1_label)` |
| 5.5s | 标记R | `Create(radius1), Write(R_label)` |
| 6.5s | 标记O₂ | `FadeIn(O2_dot), Write(O2_label)` |
| 7.0s | 标记r | `Create(radius2), Write(r_label)` |
| 8.0s | 绘制O₁O₂连线 | `Create(distance_line)` |
| 8.8s | 标注d | `FadeIn(d_brace), Write(d_label)` |
| 9.5s | 说明文字 | `FadeIn(explain)` |
| 11.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: radius lines, explain
- 保留: circles, O1/O2 dots and labels

---

## Scene 3: 外离 (12-21秒)
**目的**: d > R+r

### 元素
1. 小圆移动到外离位置
2. 圆心距d标注
3. 公式显示
4. 间隙提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 标题 | `Write(title: "外离")` |
| 12.5s | 小圆移动 | `circle2.animate.move_to()` |
| 13.5s | 绘制连线 | `Create(distance_line)` |
| 14.0s | 标注d | `FadeIn(d_brace), Write(d_label)` |
| 15.0s | 显示R+r | `Write(formula: d > R+r)` |
| 16.0s | 高亮间隙 | `Indicate()` |
| 17.0s | 说明文字 | `FadeIn(explain: "无公共点")` |
| 18.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, distance_line, brace, formula, explain

---

## Scene 4: 外切 (21-30秒)
**目的**: d = R+r

### 元素
1. 小圆移动到外切位置
2. 切点T
3. 公式 d = R+r
4. 公切线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 21.0s | 标题 | `Write(title: "外切")` |
| 21.5s | 小圆移动 | `circle2.animate.move_to()` |
| 22.5s | 标记切点T | `FadeIn(T_dot), Flash()` |
| 23.0s | 标注T | `Write(T_label)` |
| 24.0s | 绘制连线 | `Create(distance_line)` |
| 24.5s | 标注d=R+r | `Write(formula)` |
| 25.5s | 绘制公切线 | `Create(tangent_line)` |
| 26.5s | 说明 | `FadeIn(explain: "一个公共点")` |
| 28.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, T_dot, T_label, distance_line, formula, tangent_line, explain

---

## Scene 5: 相交 (30-40秒)
**目的**: R-r < d < R+r

### 元素
1. 小圆移动到相交位置
2. 两个交点A、B
3. 公式不等式
4. 公共弦

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 30.0s | 标题 | `Write(title: "相交")` |
| 30.5s | 小圆移动 | `circle2.animate.move_to()` |
| 31.5s | 绘制连线 | `Create(distance_line)` |
| 32.0s | 标注d | `Write(d_label)` |
| 33.0s | 标记交点A | `FadeIn(A_dot), Flash()` |
| 33.5s | 标记交点B | `FadeIn(B_dot), Flash()` |
| 34.0s | 标注A、B | `Write(labels)` |
| 35.0s | 显示公式 | `Write(formula: R-r < d < R+r)` |
| 36.0s | 绘制公共弦 | `Create(chord)` |
| 37.0s | 说明 | `FadeIn(explain: "两个交点")` |
| 38.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, distance_line, dots, labels, formula, chord, explain

---

## Scene 6: 内切 (40-49秒)
**目的**: d = R-r

### 元素
1. 小圆移动到内切位置
2. 切点T
3. 公式 d = R-r
4. 内部切线提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 40.0s | 标题 | `Write(title: "内切")` |
| 40.5s | 小圆移动 | `circle2.animate.move_to()` |
| 41.5s | 标记切点T | `FadeIn(T_dot), Flash()` |
| 42.0s | 标注T | `Write(T_label)` |
| 43.0s | 绘制连线 | `Create(distance_line)` |
| 43.5s | 标注d=R-r | `Write(formula)` |
| 44.5s | 绘制切线 | `Create(tangent_line)` |
| 45.5s | 说明 | `FadeIn(explain: "一个公共点")` |
| 47.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, T_dot, T_label, distance_line, formula, tangent_line, explain

---

## Scene 7: 内含 (49-57秒)
**目的**: d < R-r

### 元素
1. 小圆移动到内含位置
2. 公式 d < R-r
3. 完全包含示意

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 49.0s | 标题 | `Write(title: "内含")` |
| 49.5s | 小圆移动 | `circle2.animate.move_to()` |
| 50.5s | 绘制连线 | `Create(distance_line)` |
| 51.0s | 标注d | `Write(d_label)` |
| 52.0s | 显示公式 | `Write(formula: d < R-r)` |
| 53.0s | 说明 | `FadeIn(explain: "无公共点")` |
| 54.0s | 包含提示 | `Indicate(circles)` |
| 55.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, distance_line, d_label, formula, explain, circles, dots

---

## Scene 8: 总结对比 (57-72秒)
**目的**: 五种关系并排对比

### 元素
1. 五组小图(并排/竖排)
2. 五个公式
3. 五个说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 57.0s | 标题 | `Write(title: "位置关系判定")` |
| 58.0s | 五组图淡入 | `FadeIn(all_groups)` |
| 59.5s | 依次闪烁 | `Indicate(group1), Wait()...` |
| 63.0s | 公式高亮 | `formulas.animate.set_color()` |
| 64.5s | 关键规律 | `Write(pattern)` |
| 67.0s | 数轴示意 | `Create(number_line)` |
| 70.0s | 等待记忆 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 9: 片尾 (72-80秒)
**目的**: 作者信息+关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 72.0s | 作者名放大 | `Transform(author)` |
| 73.0s | ID显示 | `FadeIn(author_id)` |
| 74.0s | 关注文字 | `FadeIn(follow_text)` |
| 75.0s | 圆形装饰 | `Create(circles), Rotate()` |
| 78.0s | 等待 | `Wait(1.5)` |
| 79.5s | 淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 全程保留 |
| circle1 (大圆) | Scene 1 | Scene 7 | 主要元素 |
| circle2 (小圆) | Scene 1 | Scene 7 | 移动元素 |
| O1_dot, O1_label | Scene 2 | Scene 7 | 圆心标注 |
| O2_dot, O2_label | Scene 2 | Scene 7 | 圆心标注 |
| distance_line | Scene 3-7 | 各场景末 | 临时连线 |
| tangent_dots | Scene 4, 6 | 各场景末 | 切点 |
| intersection_dots | Scene 5 | Scene 5 | 交点 |

---

## 坐标布局方案

### 主场景布局 (Scene 3-7)
```
┌─────────────────────────┐  y = +7 (作者信息)
│                         │
│      标题区域            │  y = +5.5
├─────────────────────────┤
│                         │
│   ⭕ 大圆    → 小圆⭕    │  y ∈ [0, +4]
│   (O₁)        (O₂)      │
│                         │
├─────────────────────────┤
│   公式区域               │  y ∈ [-3, -1]
│   d > R+r               │
├─────────────────────────┤
│   说明文字               │  y ∈ [-5, -3]
└─────────────────────────┘

大圆中心: (-1.2, 1.5, 0)
小圆中心: 根据d动态计算
```

### 总结场景布局 (Scene 8)
```
竖排五组, 每组包含:
- 示意图 (左侧)
- 公式 (右侧)
- 说明 (下方)

y坐标从上到下:
- 外离: y = +4
- 外切: y = +2
- 相交: y = 0
- 内切: y = -2
- 内含: y = -4
```

---

## 关键几何计算公式

### 小圆圆心位置计算
```python
# O₂在O₁右侧, 距离为d
O2 = O1 + np.array([d, 0, 0])
```

### 交点计算 (相交情况)
```python
# 两圆交点
# 圆1: (x-x1)² + (y-y1)² = R²
# 圆2: (x-x2)² + (y-y2)² = r²
# 解得两个交点A、B
```

### 切点计算
```python
# 外切/内切: 切点在O₁O₂连线上
# 外切: T = O1 + (O2-O1) * R / d
# 内切: T = O1 + (O2-O1) * R / d
```

---

## 边界安全检查
- ✅ 大圆中心: (-1.2, 1.5) ✓
- ✅ 大圆范围: x∈[-2.7, 0.3], y∈[0, 3.0] ✓
- ✅ 外离时小圆: 不超出右边界 ✓
- ✅ 所有文字标注: 预留安全距离 ✓