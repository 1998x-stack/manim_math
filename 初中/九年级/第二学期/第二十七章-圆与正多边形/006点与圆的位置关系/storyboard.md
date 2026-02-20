# 点与圆的位置关系 - 动画分镜脚本

## 元信息
- 目标时长: 65-75 秒
- 场景数量: 7 个
- 难度等级: 基础（九年级）
- 核心概念: 点到圆心的距离、三种位置关系（圆内、圆上、圆外）

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"       # 蓝色 - 圆
COLOR_POINT_INSIDE = "#e74c3c" # 红色 - 圆内的点
COLOR_POINT_ON = "#f39c12"     # 橙色 - 圆上的点
COLOR_POINT_OUTSIDE = "#2ecc71"# 绿色 - 圆外的点
COLOR_RADIUS = "#9b59b6"       # 紫色 - 半径
COLOR_DISTANCE = "#e67e22"     # 橙红 - 距离线
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O = ORIGIN + UP * 1.5 |
| 半径r | 固定值 | self.radius = 2.0 |
| 点P1（圆内） | \|OP1\| < r | self.P1, d1 = 1.0 < r |
| 点P2（圆上） | \|OP2\| = r | self.P2, d2 = r |
| 点P3（圆外） | \|OP3\| > r | self.P3, d3 = 2.8 > r |
| 距离验证 | d = \|OP\| | np.linalg.norm(P - O) |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 引发思考 - 点和圆的关系

### 元素
1. 作者标识（顶部）
2. 钩子问题："这个点，在圆里还是圆外？"
3. 圆和一个点（位置模糊）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 圆出现 | `Create(circle, run_time=0.8)` |
| 1.9s | 点出现（略模糊的位置） | `FadeIn(mystery_dot, scale=0.5)` |
| 2.7s | 问号闪烁 | `Indicate(question_mark)` |
| 3.2s | 等待 | `Wait(0.3)` |

### 清理
- FadeOut: hook_text, question_mark, mystery_dot
- 保留: circle, author_info

---

## Scene 2: 距离概念引入 (6-8秒)
**目的**: 建立"距离"的概念

### 元素
1. 小标题："关键是距离"
2. 圆心O（橙色点）
3. 圆上的一个点A
4. 距离线OA（虚线）
5. 标注：半径r

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 圆心O出现 | `FadeIn(dot_O, scale=0.5)` |
| 1.0s | 标注"O" | `FadeIn(label_O)` |
| 1.5s | 点A出现在圆上 | `FadeIn(dot_A, scale=0.5)` |
| 2.1s | 距离线OA出现 | `Create(line_OA)` |
| 2.8s | 标注"r"（半径） | `FadeIn(radius_label)` |
| 3.5s | 说明文字："点到圆心的距离" | `FadeIn(explanation)` |
| 5.0s | 等待理解 | `Wait(1.5)` |

### 几何验证
```python
# 验证点A在圆上
assert abs(np.linalg.norm(A - O) - radius) < 1e-6
```

### 清理
- FadeOut: subtitle, dot_A, line_OA, radius_label, explanation
- 保留: circle, dot_O, label_O

---

## Scene 3: 情况1 - 点在圆内 (8-10秒)
**目的**: 展示 d < r 的情况

### 元素
1. 小标题："情况1：点在圆内"
2. 点P1（圆内，红色）
3. 距离线OP1（红色）
4. 距离标注d1
5. 半径标注r
6. 不等式：d < r
7. 强调：点在圆内

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle, color=COLOR_POINT_INSIDE)` |
| 0.6s | 点P1出现在圆内 | `FadeIn(dot_P1, scale=0.5, color=RED)` |
| 1.2s | 标注"P1" | `FadeIn(label_P1)` |
| 1.8s | 距离线OP1 | `Create(line_OP1)` |
| 2.5s | 距离标注"d" | `FadeIn(distance_label_d)` |
| 3.2s | 半径参考线（虚线到圆上） | `Create(radius_reference)` |
| 4.0s | 半径标注"r" | `FadeIn(radius_label)` |
| 4.8s | 不等式出现 | `FadeIn(formula: d < r)` |
| 5.8s | 高亮整个区域（圆内） | `Indicate(interior_region)` |
| 7.0s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证点P1在圆内
d1 = np.linalg.norm(P1 - O)
assert d1 < radius - 1e-6, f"P1应该在圆内，但d={d1}, r={radius}"
```

### 清理
- FadeOut: subtitle, dot_P1, line_OP1, labels, formula, radius_reference
- 保留: circle, dot_O

---

## Scene 4: 情况2 - 点在圆上 (7-9秒)
**目的**: 展示 d = r 的情况

### 元素
1. 小标题："情况2：点在圆上"
2. 点P2（圆上，橙色）
3. 距离线OP2（橙色）
4. 等式：d = r
5. 说明："距离等于半径"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle, color=COLOR_POINT_ON)` |
| 0.6s | 点P2出现在圆上 | `FadeIn(dot_P2, scale=0.5, color=ORANGE)` |
| 1.2s | 标注"P2" | `FadeIn(label_P2)` |
| 1.8s | 距离线OP2 | `Create(line_OP2)` |
| 2.5s | 距离和半径标注（重叠） | `FadeIn(dr_label)` |
| 3.2s | 等式出现 | `FadeIn(formula: d = r)` |
| 4.2s | 说明文字 | `FadeIn(explanation)` |
| 5.2s | 圆周闪烁 | `Indicate(circle)` |
| 6.2s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证点P2在圆上
d2 = np.linalg.norm(P2 - O)
assert abs(d2 - radius) < 1e-6, f"P2应该在圆上，但d={d2}, r={radius}"
```

### 清理
- FadeOut: subtitle, dot_P2, line_OP2, labels, formula, explanation
- 保留: circle, dot_O

---

## Scene 5: 情况3 - 点在圆外 (8-10秒)
**目的**: 展示 d > r 的情况

### 元素
1. 小标题："情况3：点在圆外"
2. 点P3（圆外，绿色）
3. 距离线OP3（绿色）
4. 距离标注d
5. 半径参考线（虚线到圆上）
6. 半径标注r
7. 不等式：d > r
8. 强调：点在圆外

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle, color=COLOR_POINT_OUTSIDE)` |
| 0.6s | 点P3出现在圆外 | `FadeIn(dot_P3, scale=0.5, color=GREEN)` |
| 1.2s | 标注"P3" | `FadeIn(label_P3)` |
| 1.8s | 距离线OP3 | `Create(line_OP3)` |
| 2.5s | 距离标注"d" | `FadeIn(distance_label_d)` |
| 3.2s | 半径参考线（虚线到圆上） | `Create(radius_reference)` |
| 4.0s | 半径标注"r" | `FadeIn(radius_label)` |
| 4.8s | 不等式出现 | `FadeIn(formula: d > r)` |
| 5.8s | 对比：d 更长 | `Indicate(distance_line), Indicate(radius_line)` |
| 7.0s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证点P3在圆外
d3 = np.linalg.norm(P3 - O)
assert d3 > radius + 1e-6, f"P3应该在圆外，但d={d3}, r={radius}"
```

### 清理
- FadeOut: subtitle, dot_P3, line_OP3, labels, formula, radius_reference
- 保留: circle, dot_O

---

## Scene 6: 动态演示 (10-12秒)
**目的**: 通过动画强化理解

### 元素
1. 小标题："动态演示"
2. 移动的点P（从圆外→圆上→圆内）
3. 实时距离标注
4. 实时位置判断文字
5. 颜色变化（绿→橙→红）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 小标题写入 | `Write(subtitle)` |
| 0.6s | 点P出现在圆外 | `FadeIn(dot_P, color=GREEN)` |
| 1.2s | 距离线和标注 | `Create(line_OP), FadeIn(distance_value)` |
| 2.0s | 状态标注："圆外" | `FadeIn(status_text: "圆外")` |
| 3.0s | P移动到圆上 | `dot_P.animate.move_to(...), 颜色→橙` |
| 4.5s | 状态更新："圆上" | `Transform(status_text: "圆上")` |
| 6.0s | P移动到圆内 | `dot_P.animate.move_to(...), 颜色→红` |
| 7.5s | 状态更新："圆内" | `Transform(status_text: "圆内")` |
| 9.0s | 等待 | `Wait(1.5)` |

### 几何验证
```python
# 验证每个位置的距离关系
for position, expected_relation in positions:
    d = np.linalg.norm(position - O)
    if expected_relation == "outside":
        assert d > radius
    elif expected_relation == "on":
        assert abs(d - radius) < 1e-4
    elif expected_relation == "inside":
        assert d < radius
```

### 清理
- FadeOut: subtitle, dot_P, line_OP, distance_value, status_text
- 保留: circle, dot_O

---

## Scene 7: 总结与片尾 (10-12秒)
**目的**: 知识总结，强化记忆

### 元素
1. 圆缩小移到上方
2. 知识卡片（3个判断规则）
3. 总结文字
4. 作者关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 整体缩小上移 | `VGroup(...).animate.scale(0.5).move_to(UP*4.5)` |
| 1.0s | 卡片1："d < r → 圆内" | `FadeIn(card_1, shift=RIGHT)` |
| 1.8s | 卡片2："d = r → 圆上" | `FadeIn(card_2, shift=RIGHT)` |
| 2.6s | 卡片3："d > r → 圆外" | `FadeIn(card_3, shift=RIGHT)` |
| 3.6s | 总结文字 | `FadeIn(summary_text, shift=UP*0.3)` |
| 4.6s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 5.6s | 关注提示 | `FadeIn(follow_text)` |
| 6.6s | 装饰动画 | `Rotate(decorations, PI)` |
| 8.0s | 等待 | `Wait(1.5)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部作者信息 |
| circle | Scene 1 | Scene 7 | 主圆 |
| dot_O | Scene 2 | Scene 7 | 圆心 |
| dot_P1 | Scene 3 | Scene 3 | 圆内的点 |
| dot_P2 | Scene 4 | Scene 4 | 圆上的点 |
| dot_P3 | Scene 5 | Scene 5 | 圆外的点 |
| dot_P_moving | Scene 6 | Scene 6 | 移动的点 |
| knowledge_cards | Scene 7 | Scene 7 | 知识卡片 |

---

## 关键技术点

### 1. 点到圆心的距离计算
```python
def distance_to_center(point, center):
    """计算点到圆心的距离"""
    return np.linalg.norm(point - center)
```

### 2. 判断点的位置
```python
def point_position(point, center, radius):
    """判断点与圆的位置关系"""
    d = np.linalg.norm(point - center)
    epsilon = 1e-6
    
    if d < radius - epsilon:
        return "inside"
    elif abs(d - radius) < epsilon:
        return "on"
    else:
        return "outside"
```

### 3. 动态更新距离值
```python
# 使用 always_redraw 实现实时更新
distance_label = always_redraw(
    lambda: MathTex(
        f"d = {np.linalg.norm(dot_P.get_center() - O):.2f}"
    ).move_to(...)
)
```

### 4. 颜色渐变动画
```python
# 根据距离改变颜色
def get_color_by_distance(d, r):
    if d < r:
        return COLOR_POINT_INSIDE
    elif abs(d - r) < 0.01:
        return COLOR_POINT_ON
    else:
        return COLOR_POINT_OUTSIDE
```

### 5. Brace 标注
```python
# 使用 Brace 标注距离
brace = Brace(line_segment, direction=DOWN, buff=0.1)
brace_label = brace.get_text("d")
```

---

## 预期时长分配

| 场景 | 时长 | 累计 |
|------|------|------|
| Scene 1: 开场钩子 | 3-4s | 4s |
| Scene 2: 距离概念 | 6-8s | 12s |
| Scene 3: 圆内 | 8-10s | 22s |
| Scene 4: 圆上 | 7-9s | 31s |
| Scene 5: 圆外 | 8-10s | 41s |
| Scene 6: 动态演示 | 10-12s | 53s |
| Scene 7: 总结 | 10-12s | 65s |
| **总计** | **65-75s** | |

---

## 风格统一要点

1. **距离可视化**：所有距离用线段表示，清晰标注
2. **颜色编码**：红色（圆内）、橙色（圆上）、绿色（圆外）
3. **动画流畅**：动态演示时颜色和文字平滑过渡
4. **对比强调**：三种情况分别展示，便于对比
5. **公式突出**：d < r, d = r, d > r 清晰呈现

---

## 验证清单

### 几何验证
- [ ] 所有测试点的距离计算正确
- [ ] 圆内点：d < r
- [ ] 圆上点：d = r（误差 < 1e-6）
- [ ] 圆外点：d > r
- [ ] 动态演示的每个位置都符合预期

### 数值精度
- [ ] 距离值显示准确（2位小数）
- [ ] 半径标注与实际一致
- [ ] 等式/不等式符号正确

### LaTeX检查
- [ ] 无中文字符在 MathTex 中
- [ ] 不等号正确：<, =, >
- [ ] 距离和半径符号：d, r

### 边界检查
- [ ] 所有元素在边界内
- [ ] 圆外的点不要太远
- [ ] 文字标注不重叠