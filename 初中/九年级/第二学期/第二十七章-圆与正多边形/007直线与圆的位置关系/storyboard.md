# 直线与圆的位置关系 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 初中基础
- 知识点: 直线与圆的三种位置关系

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"        # 蓝色 - 圆
COLOR_LINE = "#e74c3c"          # 红色 - 直线
COLOR_PERPENDICULAR = "#2ecc71" # 绿色 - 垂线
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
COLOR_INTERSECT = "#f39c12"     # 橙色 - 交点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定位置 | self.O |
| 半径r | 固定值2.0 | self.r |
| 距离d(相交) | 0.8*r | self.d_intersect |
| 距离d(相切) | r | self.d_tangent |
| 距离d(相离) | 1.5*r | self.d_separate |
| 垂足H | 圆心到直线垂足 | self.foot_* |
| 交点A,B | 直线与圆交点 | self.intersection_* |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力,引出问题

### 元素
1. 作者信息 (顶部小字)
2. 钩子问题 "直线与圆能有几种相遇方式?"
3. 圆和直线快速闪现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.5s | 圆淡入 | `FadeIn(circle, scale=0.8)` |
| 2.0s | 直线从左侧划入 | `Create(line)` |
| 3.5s | 直线动画移动示意 | `line.animate.shift()` |
| 4.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, line
- 保留: circle, author_info

---

## Scene 2: 基础概念介绍 (5-12秒)
**目的**: 建立圆心O、半径r、距离d的概念

### 元素
1. 圆心O标注
2. 半径r标注
3. 水平直线
4. 垂线(从O到直线)
5. 距离d标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标记圆心O | `FadeIn(O_dot), Write(O_label)` |
| 5.8s | 标记半径r | `Create(radius_line), Write(r_label)` |
| 7.0s | 绘制水平直线 | `Create(line)` |
| 7.8s | 标注"直线l" | `Write(line_label)` |
| 8.5s | 绘制垂线OH | `Create(perpendicular, rate_func=linear)` |
| 9.5s | 标注距离d | `FadeIn(d_brace), Write(d_label)` |
| 10.5s | 说明文字 | `FadeIn(explain_text)` |
| 11.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: radius_line, r_label, perpendicular, d_brace, d_label, explain_text
- 保留: circle, O_dot, O_label, line, line_label

---

## Scene 3: 情况1 - 相交 (12-25秒)
**目的**: 演示 d < r 时直线与圆相交

### 元素
1. 直线移动到相交位置 (d = 0.8r)
2. 垂线OH
3. 两个交点A, B
4. 公式 d < r
5. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 12.0s | 标题淡入 | `FadeIn(title_intersect)` |
| 12.5s | 直线移动到相交位置 | `line.animate.shift(UP*distance)` |
| 14.0s | 绘制垂线 | `Create(perpendicular)` |
| 14.8s | 标注垂足H | `FadeIn(H_dot), Write(H_label)` |
| 15.5s | 标注距离d | `FadeIn(d_brace), Write(d_label)` |
| 16.5s | 高亮两个交点 | `FadeIn(A_dot, scale=0.5), Flash(A_dot)` |
| 17.0s | 同上 | `FadeIn(B_dot, scale=0.5), Flash(B_dot)` |
| 17.5s | 标注交点 | `Write(A_label), Write(B_label)` |
| 18.5s | 显示公式 | `Write(formula: d < r)` |
| 19.5s | 说明文字 | `FadeIn(explain: "相交-两个公共点")` |
| 21.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, perpendicular, H_dot, H_label, d_brace, d_label, A_dot, B_dot, A_label, B_label, formula, explain
- 保留: circle, O_dot, O_label, line

---

## Scene 4: 情况2 - 相切 (25-38秒)
**目的**: 演示 d = r 时直线与圆相切

### 元素
1. 直线从相交移动到相切位置 (d = r)
2. 垂线OH
3. 切点T
4. 公式 d = r
5. 垂直符号
6. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 25.0s | 标题淡入 | `FadeIn(title_tangent)` |
| 25.5s | 直线移动到相切位置 | `line.animate.shift(UP*distance)` |
| 27.0s | 绘制垂线 | `Create(perpendicular)` |
| 27.8s | 标注切点T | `FadeIn(T_dot, scale=0.5), Flash(T_dot)` |
| 28.5s | 标注切点标签 | `Write(T_label)` |
| 29.0s | 标注距离d=r | `FadeIn(d_brace), Write(d_equals_r_label)` |
| 30.0s | 添加垂直符号 | `FadeIn(right_angle_mark)` |
| 31.0s | 显示公式 | `Write(formula: d = r)` |
| 32.0s | 说明文字 | `FadeIn(explain: "相切-一个公共点")` |
| 33.0s | 切线性质 | `FadeIn(property: "切线⊥半径")` |
| 35.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, perpendicular, T_dot, T_label, d_brace, d_equals_r_label, right_angle_mark, formula, explain, property
- 保留: circle, O_dot, O_label, line

---

## Scene 5: 情况3 - 相离 (38-50秒)
**目的**: 演示 d > r 时直线与圆相离

### 元素
1. 直线从相切移动到相离位置 (d = 1.5r)
2. 垂线OH
3. 公式 d > r
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 38.0s | 标题淡入 | `FadeIn(title_separate)` |
| 38.5s | 直线移动到相离位置 | `line.animate.shift(UP*distance)` |
| 40.0s | 绘制垂线 | `Create(perpendicular)` |
| 40.8s | 标注垂足H | `FadeIn(H_dot), Write(H_label)` |
| 41.5s | 标注距离d | `FadeIn(d_brace), Write(d_label)` |
| 42.5s | 显示公式 | `Write(formula: d > r)` |
| 43.5s | 说明文字 | `FadeIn(explain: "相离-无公共点")` |
| 45.0s | 闪烁提示无交点 | `Indicate(line), Indicate(circle)` |
| 47.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, line, perpendicular, H_dot, H_label, d_brace, d_label, formula, explain
- 保留: circle, O_dot, O_label

---

## Scene 6: 总结对比 (50-62秒)
**目的**: 三种情况并排对比

### 元素
1. 三个小圆(并排)
2. 三条直线(不同位置)
3. 三个公式
4. 三个说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 50.0s | 标题 | `Write(title: "位置关系判定")` |
| 51.0s | 三组图同时淡入 | `FadeIn(group_all)` |
| 52.5s | 依次闪烁三组 | `Indicate(group_1), Wait(0.3)...` |
| 54.0s | 关键公式高亮 | `formulas.animate.set_color(YELLOW)` |
| 55.5s | 口诀文字 | `Write(mnemonic)` |
| 58.0s | 等待记忆 | `Wait(3.0)` |

### 清理
- FadeOut: 所有元素

---

## Scene 7: 片尾关注 (62-70秒)
**目的**: 作者信息+引导关注

### 元素
1. 作者名称
2. ID
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 62.0s | 作者信息放大 | `Transform(author_info, large)` |
| 63.0s | ID淡入 | `FadeIn(author_id)` |
| 64.0s | 关注文字 | `FadeIn(follow_text, scale=1.1)` |
| 65.0s | 圆形装饰旋转 | `Create(circles), Rotate(circles)` |
| 68.0s | 等待 | `Wait(1.5)` |
| 69.5s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| circle | Scene 1 | Scene 6 | 主圆 |
| O_dot, O_label | Scene 2 | Scene 6 | 圆心标注 |
| line | Scene 2 | Scene 5 | 移动的直线 |
| perpendicular_* | Scene 2-5 | 各场景末 | 临时垂线 |
| intersection_dots | Scene 3 | Scene 3 | 交点 |
| tangent_dot | Scene 4 | Scene 4 | 切点 |

---

## 关键几何验证点
1. ✅ 圆心O位置固定在 (0, 1, 0)
2. ✅ 半径r = 2.0
3. ✅ 相交时: d = 1.6, 满足 d < r
4. ✅ 相切时: d = 2.0, 满足 d = r
5. ✅ 相离时: d = 3.0, 满足 d > r
6. ✅ 垂线必须精确垂直于直线
7. ✅ 交点计算必须精确(使用圆与直线方程)

---

## 坐标安全边界检查
- 圆心: (0, 1, 0) ✓ 在y∈[-3, 5]范围内
- 半径: 2.0, 圆边界y∈[-1, 3] ✓ 安全
- 直线范围: x∈[-4, 4] ✓ 安全
- 标签位置: 需动态检查避免溢出