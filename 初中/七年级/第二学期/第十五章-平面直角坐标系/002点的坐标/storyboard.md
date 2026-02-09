# 平面直角坐标系 - 点的坐标 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 基础（七年级）
- 目标：理解点的坐标表示法，掌握由点确定坐标和由坐标确定点的方法

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调点
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_AXES = WHITE             # 白色 - 坐标轴
COLOR_GRID = "#2c3e50"         # 深灰 - 网格
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 坐标原点 | (0, 0) | self.origin | 坐标系中心 |
| 示例点P | (3, 2) | self.point_P | 第一象限点 |
| 示例点Q | (-2, 1) | self.point_Q | 第二象限点 |
| 示例点R | (2, -1.5) | self.point_R | 第四象限点 |
| x轴点A | (2, 0) | self.point_A | x轴上的点 |
| y轴点B | (0, -1) | self.point_B | y轴上的点 |
| P到x轴垂足 | (3, 0) | self.foot_Px | 垂线交点 |
| P到y轴垂足 | (0, 2) | self.foot_Py | 垂线交点 |

**注意**: 所有点的坐标都需要乘以坐标系的单位长度scale来转换为Manim坐标

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出主题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 神秘的点闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` "如何用数字描述平面上的位置?" |
| 1.0s | 三个神秘点闪烁 | `Flash(dot)` 循环3次 |
| 2.5s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, mystery_dots
- 保留: author_info

---

## Scene 2: 建立坐标系 (6-8秒)
**目的**: 介绍坐标系的组成部分

### 元素
1. 标题 "平面直角坐标系"
2. 坐标轴（x轴、y轴）
3. 原点标记O
4. 坐标轴标签
5. 四个象限标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=UP*0.3)` |
| 0.5s | x轴生长 | `Create(x_axis)` |
| 1.2s | y轴生长 | `Create(y_axis)` |
| 1.9s | 原点标记 | `FadeIn(origin_dot), Write(origin_label "O")` |
| 2.5s | 坐标轴标签 | `FadeIn(x_label "x"), FadeIn(y_label "y")` |
| 3.2s | 象限标注闪现 | `FadeIn(quadrant_labels)` I, II, III, IV |
| 4.5s | 网格淡入 | `FadeIn(grid, opacity=0.2)` |
| 5.5s | 说明文字 | `FadeIn(explain)` "两条数轴互相垂直" |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, explain
- 保留: axes, grid, origin_dot, origin_label

---

## Scene 3: 由点确定坐标（第一部分）(10-12秒)
**目的**: 教会学生如何从点读出坐标

### 元素
1. 标题 "由点确定坐标"
2. 点P(3, 2)及标签
3. 从P到x轴的垂线（虚线）
4. 从P到y轴的垂线（虚线）
5. x轴上读数标记：3
6. y轴上读数标记：2
7. 坐标表示 P(3, 2)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 点P出现 | `FadeIn(dot_P, scale=0.5), Flash(dot_P)` |
| 0.8s | 点P标签 | `Write(label_P "P")` |
| 1.3s | 步骤提示 | `FadeIn(step1)` "步骤1: 作垂线到x轴" |
| 1.8s | 垂线到x轴 | `Create(perpendicular_to_x)` 虚线 |
| 2.5s | x轴读数高亮 | `Indicate(x_value)`, 标记3 |
| 3.2s | x坐标标注 | `FadeIn(x_coord "x=3")` |
| 4.0s | 步骤提示2 | `Transform(step1, step2)` "步骤2: 作垂线到y轴" |
| 4.5s | 垂线到y轴 | `Create(perpendicular_to_y)` 虚线 |
| 5.2s | y轴读数高亮 | `Indicate(y_value)`, 标记2 |
| 5.9s | y坐标标注 | `FadeIn(y_coord "y=2")` |
| 6.7s | 合并坐标 | `Transform(coords, final "P(3, 2)")` |
| 7.5s | 直角标记 | `FadeIn(right_angle_marks)` 两个直角符号 |
| 8.5s | 重点提示 | `FadeIn(highlight)` "横坐标x, 纵坐标y" |
| 10.5s | 等待 | `Wait(1.5)` 让学生理解 |

### 清理
- FadeOut: subtitle, step_texts, highlight, perpendiculars, right_angle_marks
- 保留: dot_P, label_P, coordinate_label

---

## Scene 4: 由点确定坐标（更多示例）(8-10秒)
**目的**: 巩固理解，展示不同象限的点

### 元素
1. 点Q(-2, 1) 第二象限
2. 点R(2, -1.5) 第四象限
3. 快速动画流程

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 说明 | `FadeIn(text)` "再看两个例子" |
| 0.5s | 点Q出现 | `FadeIn(dot_Q, scale=0.5)` |
| 1.0s | Q的垂线（快速）| `Create(perp_Q_group)` 同时两条 |
| 1.8s | Q坐标标注 | `FadeIn(label_Q "Q(-2, 1)")` |
| 2.5s | 点R出现 | `FadeIn(dot_R, scale=0.5)` |
| 3.0s | R的垂线（快速）| `Create(perp_R_group)` |
| 3.8s | R坐标标注 | `FadeIn(label_R "R(2, -1.5)")` |
| 4.5s | 提示 | `FadeIn(hint)` "注意: 负数表示方向相反" |
| 6.5s | 三点闪烁 | `Indicate(all_dots)` |
| 8.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: text, hint, perp_Q_group, perp_R_group
- 保留: dots, labels

---

## Scene 5: 由坐标确定点 (10-12秒)
**目的**: 反向操作 - 根据坐标找点

### 元素
1. 标题 "由坐标确定点"
2. 坐标 S(2.5, -2)
3. 在x轴上标记2.5
4. 在y轴上标记-2
5. 从轴上作垂线
6. 垂线交点即为点S

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空旧点 | `FadeOut(dot_P, dot_Q, dot_R, labels)` |
| 0.5s | 标题淡入 | `FadeIn(subtitle2)` |
| 1.0s | 显示坐标 | `Write(given_coord "S(2.5, -2)")` |
| 1.8s | 步骤1提示 | `FadeIn(step1)` "在x轴找到2.5" |
| 2.3s | x轴标记 | `FadeIn(x_mark), Indicate(x_mark)` |
| 3.0s | x轴垂线 | `Create(vertical_line)` 虚线向上/向下 |
| 3.7s | 步骤2提示 | `Transform(step1, step2)` "在y轴找到-2" |
| 4.2s | y轴标记 | `FadeIn(y_mark), Indicate(y_mark)` |
| 4.9s | y轴垂线 | `Create(horizontal_line)` 虚线左/右 |
| 5.6s | 交点闪烁 | `Flash(intersection)` |
| 6.3s | 点S出现 | `FadeIn(dot_S, scale=0.5)` |
| 6.8s | 标签 | `Write(label_S "S")` |
| 7.5s | 直角标记 | `FadeIn(right_angles)` |
| 8.5s | 重点 | `FadeIn(highlight)` "两条垂线的交点" |
| 10.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: subtitle2, step_texts, highlight, vertical_line, horizontal_line, right_angles
- 保留: dot_S, label_S, given_coord

---

## Scene 6: 坐标轴上的点（特殊情况）(8-10秒)
**目的**: 强调坐标轴上点的特殊性

### 元素
1. 标题 "特殊位置: 坐标轴上的点"
2. x轴上的点A(2, 0)
3. y轴上的点B(0, -1)
4. 原点O(0, 0)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空 | `FadeOut(dot_S, label_S, given_coord)` |
| 0.5s | 标题 | `FadeIn(subtitle3)` |
| 1.0s | x轴高亮 | `x_axis.animate.set_color(YELLOW)` |
| 1.5s | 点A出现 | `FadeIn(dot_A), Write(label_A "A(2, 0)")` |
| 2.3s | 说明1 | `FadeIn(explain1)` "x轴上: y = 0" |
| 3.5s | x轴恢复 | `x_axis.animate.set_color(WHITE)` |
| 3.8s | y轴高亮 | `y_axis.animate.set_color(YELLOW)` |
| 4.3s | 点B出现 | `FadeIn(dot_B), Write(label_B "B(0, -1)")` |
| 5.1s | 说明2 | `FadeIn(explain2)` "y轴上: x = 0" |
| 6.3s | y轴恢复 | `y_axis.animate.set_color(WHITE)` |
| 6.6s | 原点闪烁 | `Indicate(origin_dot)` |
| 7.1s | 原点说明 | `FadeIn(explain3)` "原点: (0, 0)" |
| 8.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: subtitle3, explain1, explain2, explain3, dot_A, dot_B
- 保留: axes, grid, origin

---

## Scene 7: 总结与关注 (8-10秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结要点（3条）
2. 作者信息放大
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标系缩小淡出 | `axes.animate.scale(0.5).fade(0.7)` |
| 0.8s | 总结标题 | `Write(summary_title)` "要点总结" |
| 1.3s | 要点1 | `FadeIn(point1, shift=RIGHT)` "点用有序数对(x,y)表示" |
| 2.0s | 要点2 | `FadeIn(point2, shift=RIGHT)` "由点确定坐标: 作垂线读数" |
| 2.7s | 要点3 | `FadeIn(point3, shift=RIGHT)` "由坐标确定点: 作垂线找交点" |
| 3.4s | 要点4 | `FadeIn(point4, shift=RIGHT)` "坐标轴上: 一个坐标为0" |
| 4.5s | 装饰 | `Create(decorative_box)` 框住要点 |
| 5.5s | 作者放大 | `author_info.animate.scale(1.5).move_to(UP)` |
| 6.2s | 关注文字 | `Write(follow_text)` "关注我, 学更多数学!" |
| 7.2s | 装饰动画 | `Rotate(decorations)` 小点围绕旋转 |
| 9.0s | 淡出 | `FadeOut(VGroup(*all_objects))` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留 |
| axes | Scene 2 | Scene 7 | 主坐标系 |
| grid | Scene 2 | Scene 7 | 背景网格 |
| origin_dot | Scene 2 | Scene 6 | 原点标记 |
| dot_P | Scene 3 | Scene 4 | 第一个示例点 |
| dot_Q | Scene 4 | Scene 5 | 第二象限点 |
| dot_R | Scene 4 | Scene 5 | 第四象限点 |
| dot_S | Scene 5 | Scene 6 | 由坐标确定的点 |
| dot_A | Scene 6 | Scene 6 | x轴上的点 |
| dot_B | Scene 6 | Scene 6 | y轴上的点 |
| perpendiculars | Scene 3-5 | 各场景内 | 临时辅助线 |

---

## 技术要点

### 1. 坐标系配置
```python
# NumberPlane 参数
axes = NumberPlane(
    x_range=[-4, 4, 1],
    y_range=[-3, 3, 1],
    x_length=8,
    y_length=6,
    background_line_style={
        "stroke_color": COLOR_GRID,
        "stroke_width": 1,
        "stroke_opacity": 0.3
    }
).scale(0.85).shift(UP * 1.5)
```

### 2. 垂线创建（精确）
```python
# 从点到x轴的垂线
def perpendicular_to_x_axis(point):
    x, y, _ = point
    foot = np.array([x, 0, 0])
    return DashedLine(point, foot, color=COLOR_AUXILIARY, dash_length=0.1)

# 从点到y轴的垂线
def perpendicular_to_y_axis(point):
    x, y, _ = point
    foot = np.array([0, y, 0])
    return DashedLine(point, foot, color=COLOR_AUXILIARY, dash_length=0.1)
```

### 3. 直角标记
```python
# 在垂足处创建直角符号
def create_right_angle(foot, direction1, direction2, size=0.15):
    # direction1: 指向点的方向
    # direction2: 沿轴的方向
    square = Square(side_length=size, color=YELLOW, stroke_width=2, fill_opacity=0)
    # ... 旋转和定位
    return square
```

### 4. 坐标标签定位
```python
# 点的坐标标签（避免遮挡）
def place_coordinate_label(dot, coord_text, prefer_direction=UR):
    label = MathTex(coord_text, color=WHITE, font_size=24)
    
    # 智能定位：避开坐标轴和其他标签
    directions = [prefer_direction, UP, DOWN, LEFT, RIGHT]
    for direction in directions:
        label.next_to(dot, direction, buff=0.2)
        if is_clear_position(label):  # 自定义碰撞检测
            return label
    
    return label
```

---

## 动画节奏控制

### 关键停顿时机
1. **Scene 3 末尾**: 2.0s - 理解"由点确定坐标"的完整流程
2. **Scene 5 末尾**: 1.5s - 理解"由坐标确定点"的逆向过程
3. **Scene 6 末尾**: 1.0s - 记住坐标轴上点的特殊性

### 速度建议
- 坐标系建立: 慢速 (让学生看清结构)
- 第一个示例: 慢速 (详细步骤)
- 后续示例: 中速 (巩固理解)
- 总结: 慢速 (强化记忆)

---

## 预期问题与解决方案

### 问题1: 网格可能太密集
**解决**: 使用 `x_range` 和 `y_range` 的 step 参数控制，建议 step=1

### 问题2: 标签重叠
**解决**: 实现智能定位函数，检测碰撞并调整位置

### 问题3: 垂线可能延伸到边界外
**解决**: 计算垂线长度时限制在可见范围内

### 问题4: 负坐标可能不易理解
**解决**: 在 Scene 4 中特别强调负数的方向含义

---

## 验证清单

### 几何精确性
- [ ] 所有垂线确实垂直于坐标轴（使用向量垂直验证）
- [ ] 点的 Manim 坐标与逻辑坐标一致
- [ ] 直角标记方向正确

### 视觉清晰度
- [ ] 文字大小符合规范（标题36, 正文22, 标签20）
- [ ] 所有元素在安全区域内（x∈[-4,4], y∈[-7,7]）
- [ ] 颜色对比度足够（白色背景深色字体，或反之）

### 教学有效性
- [ ] 步骤顺序合理（先由点到坐标，再由坐标到点）
- [ ] 重点内容有足够停留时间
- [ ] 特殊情况（坐标轴上）有说明

---

## 总预估时长
- Scene 1: 3-4s
- Scene 2: 6-8s
- Scene 3: 10-12s
- Scene 4: 8-10s
- Scene 5: 10-12s
- Scene 6: 8-10s
- Scene 7: 8-10s
- **总计**: 约 60-75 秒 ✓

---

## 下一步
1. ✅ 分镜脚本完成
2. ⏳ 编写 Python 代码
3. ⏳ 创建 verify_geometry.py
4. ⏳ 渲染测试