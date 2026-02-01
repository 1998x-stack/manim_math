# 圆心角、弧、弦、弦心距关系 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标受众: 九年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主圆
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_ARC_1 = "#2ecc71"        # 绿色 - 弧1
COLOR_ARC_2 = "#9b59b6"        # 紫色 - 弧2
COLOR_CHORD_1 = "#f39c12"      # 橙色 - 弦1
COLOR_CHORD_2 = "#1abc9c"      # 青色 - 弦2
```

## 几何预计算清单

### 主要参数
| 元素 | 计算公式 | 存储变量 | 数值 |
|------|---------|---------|------|
| 圆心 | 固定点 | self.O | (0, 1, 0) |
| 圆半径 | 固定值 | self.R | 2.5 |
| 圆心角1 | 固定角度 | self.angle_1 | 60° (π/3) |
| 圆心角2 | 固定角度 | self.angle_2 | 60° (π/3) |

### 派生点位
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 点A | O + R*(cos(90°), sin(90°)) | self.A |
| 点B | O + R*(cos(30°), sin(30°)) | self.B |
| 点C | O + R*(cos(-30°), sin(-30°)) | self.C |
| 点D | O + R*(cos(-90°), sin(-90°)) | self.D |
| 弦AB中点M1 | (A + B) / 2 | self.M1 |
| 弦CD中点M2 | (C + D) / 2 | self.M2 |

### 几何量计算
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 弦AB长度 | \|\|B - A\|\| | self.chord_1_length |
| 弦CD长度 | \|\|D - C\|\| | self.chord_2_length |
| 弦AB弦心距 | \|\|M1 - O\|\| | self.sagitta_1 |
| 弦CD弦心距 | \|\|M2 - O\|\| | self.sagitta_2 |
| 弧AB长度 | R × angle_1 | self.arc_1_length |
| 弧CD长度 | R × angle_2 | self.arc_2_length |

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
吸引注意力，提出核心问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 圆的简单预览

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 1.0s |
| 1.3s | 圆形创建 | `Create(circle)` | 0.8s |
| 2.1s | 几个点闪烁暗示 | `FadeIn(dots, lag_ratio=0.2)` | 0.6s |
| 2.7s | 等待理解 | `Wait()` | 1.0s |
| 3.7s | 淡出钩子文字 | `FadeOut(hook_text)` | 0.4s |

### 文案
- 钩子: "圆中的四个量，有一个相等，其余全等？"
- 副标题: "让我们一探究竟..."

### 清理
- FadeOut: hook_text
- 保留: circle, author_info

---

## Scene 2: 概念介绍 (5-12秒)

### 目的
介绍四个核心概念：圆心角、弧、弦、弦心距

### 元素
1. 圆心O
2. 两条半径OA, OB
3. 圆心角∠AOB
4. 弧AB
5. 弦AB
6. 弦心距（垂足M）

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 5.5s | 圆心O高亮 | `Flash(O_dot)` | 0.4s |
| 5.9s | 绘制半径OA, OB | `Create(radius_OA), Create(radius_OB)` | 0.8s |
| 6.7s | 标记圆心角 | `Create(angle_arc), Write(angle_label)` | 0.8s |
| 7.5s | 高亮弧AB | `Create(arc_AB, color=highlight)` | 0.7s |
| 8.2s | 绘制弦AB | `Create(chord_AB)` | 0.6s |
| 8.8s | 绘制弦心距OM | `Create(sagitta_line), Create(M_dot)` | 0.8s |
| 9.6s | 说明文字淡入 | `FadeIn(explanation)` | 0.5s |
| 10.1s | 等待理解 | `Wait()` | 1.5s |

### 文案
- 标题: "四个关键元素"
- 说明: "圆心角 → 弧 → 弦 → 弦心距"

### 清理
- 保留所有元素用于下一场景

---

## Scene 3: 第二组元素构建 (12-18秒)

### 目的
构建第二组相等的元素（∠COD = ∠AOB）

### 元素
1. 点C, D
2. 半径OC, OD
3. 圆心角∠COD
4. 弧CD
5. 弦CD
6. 弦心距ON

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 说明文字 | `Write(instruction)` | 0.6s |
| 12.6s | 绘制半径OC, OD | `Create(radius_OC), Create(radius_OD)` | 0.8s |
| 13.4s | 标记圆心角∠COD | `Create(angle_2_arc)` | 0.6s |
| 14.0s | 弧CD高亮 | `Create(arc_CD)` | 0.7s |
| 14.7s | 绘制弦CD | `Create(chord_CD)` | 0.6s |
| 15.3s | 绘制弦心距ON | `Create(sagitta_2_line), Create(N_dot)` | 0.8s |
| 16.1s | 等待 | `Wait()` | 1.0s |

### 文案
- 说明: "再取相等的圆心角∠COD"

### 清理
- 保留所有元素

---

## Scene 4: 圆心角相等 → 弧相等 (18-25秒)

### 目的
演示第一个推导：圆心角相等 ⇒ 弧相等

### 元素
1. 角度标注
2. 弧的长度标注
3. 动画对比

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 18.0s | 淡化其他元素 | `FadeOut(chords, sagitta_lines)` | 0.4s |
| 18.4s | 标题淡入 | `Write(title_1)` | 0.5s |
| 18.9s | 角度标注 | `Write(angle_1_label), Write(angle_2_label)` | 0.8s |
| 19.7s | 角度闪烁强调 | `Flash(angle_1), Flash(angle_2)` | 0.5s |
| 20.2s | 箭头动画 | `GrowArrow(arrow)` | 0.6s |
| 20.8s | 弧AB高亮 | `arc_AB.animate.set_color(YELLOW)` | 0.4s |
| 21.2s | 弧CD高亮 | `arc_CD.animate.set_color(YELLOW)` | 0.4s |
| 21.6s | 弧长标注 | `Write(arc_length_labels)` | 0.8s |
| 22.4s | 等于符号 | `Write(equals_sign)` | 0.4s |
| 22.8s | 等待理解 | `Wait()` | 1.5s |

### 文案
- 标题: "① 圆心角相等 → 弧相等"
- 标注: "∠AOB = ∠COD = 60°"
- 结论: "⌒AB = ⌒CD"

### 清理
- FadeOut: 标注和箭头
- 保留: 圆、半径、弧

---

## Scene 5: 弧相等 → 弦相等 (25-32秒)

### 目的
演示第二个推导：弧相等 ⇒ 弦相等

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 25.0s | 标题更新 | `Transform(title_1, title_2)` | 0.4s |
| 25.4s | 弧闪烁 | `Indicate(arc_AB), Indicate(arc_CD)` | 0.6s |
| 26.0s | 箭头动画 | `GrowArrow(arrow)` | 0.5s |
| 26.5s | 弦AB淡入 | `Create(chord_AB)` | 0.6s |
| 27.1s | 弦CD淡入 | `Create(chord_CD)` | 0.6s |
| 27.7s | 弦长标注 | `Write(chord_length_labels)` | 0.8s |
| 28.5s | 等于符号 | `Write(equals_sign)` | 0.4s |
| 28.9s | 等待理解 | `Wait()` | 1.5s |

### 文案
- 标题: "② 弧相等 → 弦相等"
- 结论: "AB = CD"

### 清理
- FadeOut: 标注和箭头

---

## Scene 6: 弦相等 → 弦心距相等 (32-40秒)

### 目的
演示第三个推导：弦相等 ⇒ 弦心距相等

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 标题更新 | `Transform(title_2, title_3)` | 0.4s |
| 32.4s | 弦闪烁 | `Indicate(chord_AB), Indicate(chord_CD)` | 0.6s |
| 33.0s | 箭头动画 | `GrowArrow(arrow)` | 0.5s |
| 33.5s | 弦心距OM淡入 | `Create(sagitta_1)` | 0.7s |
| 34.2s | 弦心距ON淡入 | `Create(sagitta_2)` | 0.7s |
| 34.9s | 垂直符号标记 | `Create(right_angle_1), Create(right_angle_2)` | 0.5s |
| 35.4s | 距离标注 | `Write(distance_labels)` | 0.8s |
| 36.2s | 等于符号 | `Write(equals_sign)` | 0.4s |
| 36.6s | 等待理解 | `Wait()` | 1.5s |

### 文案
- 标题: "③ 弦相等 → 弦心距相等"
- 结论: "OM = ON"

### 清理
- 保留所有元素用于总结

---

## Scene 7: 总结与反向推导 (40-50秒)

### 目的
总结四个量的等价关系，强调双向性

### 元素
1. 四个量的图标
2. 双向箭头
3. 总结公式

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 40.0s | 场景缩小移至上方 | `VGroup(...).animate.scale(0.5).to_edge(UP)` | 0.8s |
| 40.8s | 总结标题 | `Write(summary_title)` | 0.6s |
| 41.4s | 四个量图标淡入 | `FadeIn(icons, lag_ratio=0.2)` | 1.0s |
| 42.4s | 双向箭头 | `GrowArrow(arrows, lag_ratio=0.1)` | 1.2s |
| 43.6s | 公式淡入 | `Write(formula)` | 1.0s |
| 44.6s | 强调"反之亦然" | `Indicate(reverse_text)` | 0.5s |
| 45.1s | 等待 | `Wait()` | 2.0s |

### 文案
- 标题: "四个量的等价关系"
- 公式: "圆心角相等 ⟺ 弧相等 ⟺ 弦相等 ⟺ 弦心距相等"
- 强调: "任一个相等 → 其余全等"

### 清理
- 全部淡出准备片尾

---

## Scene 8: 片尾 (50-60秒)

### 目的
品牌宣传，引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 50.0s | 全部淡出 | `FadeOut(VGroup(*))` | 0.6s |
| 50.6s | 作者名放大 | `Transform(author_info, author_large)` | 0.7s |
| 51.3s | ID显示 | `FadeIn(author_id)` | 0.4s |
| 51.7s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 52.3s | 圆形装饰旋转 | `Rotate(decorations)` | 1.5s |
| 53.8s | 全部保持 | `Wait()` | 2.0s |

### 文案
- "上海初高中数学直通车"
- "@emptyandcalm"
- "关注我，获得更多数学技巧！"

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留，最后放大 |
| circle | Scene 1 | Scene 7 | 主圆 |
| O_dot | Scene 2 | Scene 7 | 圆心 |
| radius_OA, radius_OB | Scene 2 | Scene 7 | 第一组半径 |
| angle_1_arc | Scene 2 | Scene 7 | 圆心角1 |
| arc_AB | Scene 2 | Scene 7 | 弧1 |
| chord_AB | Scene 2 | Scene 7 | 弦1 |
| sagitta_1 | Scene 2 | Scene 7 | 弦心距1 |
| radius_OC, radius_OD | Scene 3 | Scene 7 | 第二组半径 |
| angle_2_arc | Scene 3 | Scene 7 | 圆心角2 |
| arc_CD | Scene 3 | Scene 7 | 弧2 |
| chord_CD | Scene 3 | Scene 7 | 弦2 |
| sagitta_2 | Scene 3 | Scene 7 | 弦心距2 |
| temp_labels | Scene 4-6 | Scene 4-6 | 临时标注 |
| summary_elements | Scene 7 | Scene 7 | 总结元素 |

---

## 验证要点

### 几何验证
- [ ] ∠AOB = ∠COD = 60° (精确)
- [ ] 弧AB长度 = 弧CD长度 = R × π/3
- [ ] 弦AB长度 = 弦CD长度 = R × √3
- [ ] 弦心距OM = 弦心距ON = R/2

### 视觉验证
- [ ] 所有元素在边界内 (x∈[-4,4], y∈[-7,7])
- [ ] 文字无重叠
- [ ] 颜色对比度足够
- [ ] 标注清晰可读

### 动画验证
- [ ] 节奏流畅，无突兀
- [ ] 难点有足够停留
- [ ] 总时长60-75秒
- [ ] 开头有钩子，结尾有CTA

---

## 数学公式汇总

```python
# 圆心角到弧长
arc_length = radius * angle_in_radians

# 圆心角到弦长
chord_length = 2 * radius * sin(angle / 2)

# 弦心距（圆心到弦的距离）
sagitta = radius * cos(angle / 2)

# 验证关系
assert abs(chord_1_length - chord_2_length) < 1e-6
assert abs(sagitta_1 - sagitta_2) < 1e-6
assert abs(arc_1_length - arc_2_length) < 1e-6
```