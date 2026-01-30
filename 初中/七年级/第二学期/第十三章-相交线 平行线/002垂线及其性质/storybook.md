# 垂线及其性质 - 动画分镜脚本

<!-- /root/code/sss/media/videos/perpendicular_lines/1920p60/PerpendicularLines.mp4 -->

## 元信息
- 题目: 垂线及其性质 (七年级下学期 第十三章)
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 基础
- 视频格式: TikTok 竖屏 (1080×1920, 9:16)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主直线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 垂线
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调元素
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_RIGHT_ANGLE = "#2ecc71"   # 绿色 - 直角标记
COLOR_DISTANCE = "#f39c12"      # 橙色 - 距离相关
```

## 几何预计算清单

### 基础元素
| 元素 | 计算方法 | 存储变量 | 说明 |
|------|---------|---------|------|
| 主直线l | 水平线段 | `self.line_l` | 从(-3, 0, 0)到(3, 0, 0) |
| 点P | 固定点 | `self.P` | (-1.5, 2, 0) |
| 垂足H | 垂足计算 | `self.H` | (-1.5, 0, 0) |
| 垂线PH | 线段 | `self.perpendicular` | 从P到H |
| 点Q | 另一个外部点 | `self.Q` | (1.5, 2.5, 0) |
| 垂足K | 垂足计算 | `self.K` | (1.5, 0, 0) |

### 派生元素
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 距离PH长度 | `np.linalg.norm(P - H)` | `self.dist_PH` |
| 其他点A | 直线上任意点 | `self.A` |
| 距离PA长度 | `np.linalg.norm(P - A)` | `self.dist_PA` |

### 验证清单
- [ ] 垂线PH确实垂直于直线l (点积为0)
- [ ] 垂足H在直线l上
- [ ] 所有距离计算准确
- [ ] 所有元素在画布边界内

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，提出核心问题

### 元素列表
1. 作者标识 (顶部, y=7)
2. 钩子问题文字 (y=5.5)
3. 简单动画图示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子问题书写 | `Write(hook_text)` | 1.0s |
| 1.3s | 两条直线快速闪现 | `Create(line1), Create(line2)` | 0.6s |
| 1.9s | 直角符号强调 | `FadeIn(right_angle, scale=0.5)` | 0.4s |
| 2.3s | 等待理解 | `Wait(1.5)` | 1.5s |

### 文字内容
- 钩子: "什么是垂线? 它有什么神奇性质?"
- 作者: "上海初高中数学直通车 @emptyandcalm"

### 清理计划
- FadeOut: hook_text, initial_lines
- 保留: author_info (整个视频)

---

## Scene 2: 垂线定义 (5-15秒)
**目的**: 清晰展示垂线的定义和符号表示

### 元素列表
1. 标题: "垂线的定义" (y=5.5)
2. 主直线l (y=0, 蓝色)
3. 点P (y=2, 红色点)
4. 垂线PH (红色)
5. 直角标记 (绿色)
6. 标签: l, P, H
7. 定义文字 (y=-4)
8. 数学符号 (y=-5)

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` | 0.4s |
| 5.4s | 绘制主直线l | `Create(line_l)` | 0.8s |
| 6.2s | 点P出现 | `FadeIn(dot_P, scale=0.5)` | 0.3s |
| 6.5s | 标签P | `FadeIn(label_P)` | 0.2s |
| 6.7s | 垂线PH绘制 | `Create(perpendicular)` | 1.0s |
| 7.7s | 垂足H标记 | `FadeIn(dot_H), FadeIn(label_H)` | 0.3s |
| 8.0s | 直角符号出现 | `FadeIn(right_angle_mark)` | 0.4s |
| 8.4s | 强调直角 | `Flash(right_angle_mark)` | 0.3s |
| 8.7s | 定义文字显示 | `Write(definition_text)` | 1.5s |
| 10.2s | 符号显示 | `Write(symbol)` | 0.8s |
| 11.0s | 理解停顿 | `Wait(2.5)` | 2.5s |

### 文字内容
- 标题: "垂线的定义"
- 定义: "两条直线相交成直角时, 称这两条直线互相垂直"
- 符号: "记作: l ⊥ PH"
- 说明: "H叫做垂足"

### 几何计算
```python
# 主直线l: 水平线
self.line_l_start = np.array([-3, 0, 0])
self.line_l_end = np.array([3, 0, 0])

# 点P
self.P = np.array([-1.5, 2, 0])

# 垂足H (P在l上的投影)
self.H = np.array([self.P[0], 0, 0])  # 水平线上投影就是(x, 0, 0)

# 验证垂直性
vec_l = self.line_l_end - self.line_l_start
vec_PH = self.H - self.P
assert abs(np.dot(vec_l, vec_PH)) < 1e-6, "不垂直!"
```

### 清理计划
- FadeOut: title, definition_text
- 保留: line_l, dot_P, perpendicular, right_angle_mark, labels

---

## Scene 3: 性质1 - 唯一性 (15-30秒)
**目的**: 展示"过一点有且只有一条直线与已知直线垂直"

### 元素列表
1. 副标题: "性质1: 唯一性" (y=5.5)
2. 原有元素: line_l, dot_P
3. 多条尝试线 (虚线, 不垂直)
4. 唯一垂线 (实线, 红色)
5. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 15.0s | 副标题出现 | `FadeIn(subtitle)` | 0.4s |
| 15.4s | 尝试线1出现 | `Create(attempt_1)` | 0.5s |
| 15.9s | 交叉标记 | `FadeIn(cross_mark_1)` | 0.2s |
| 16.1s | 尝试线1淡出 | `FadeOut(attempt_1, cross_mark_1)` | 0.3s |
| 16.4s | 尝试线2出现 | `Create(attempt_2)` | 0.5s |
| 16.9s | 交叉标记 | `FadeIn(cross_mark_2)` | 0.2s |
| 17.1s | 尝试线2淡出 | `FadeOut(attempt_2, cross_mark_2)` | 0.3s |
| 17.4s | 唯一垂线高亮 | `perpendicular.animate.set_color(YELLOW)` | 0.5s |
| 17.9s | 对勾标记 | `FadeIn(check_mark)` | 0.3s |
| 18.2s | 恢复颜色 | `perpendicular.animate.set_color(RED)` | 0.3s |
| 18.5s | 性质文字 | `Write(property_text)` | 1.5s |
| 20.0s | 理解停顿 | `Wait(2.5)` | 2.5s |

### 文字内容
- 副标题: "性质1: 唯一性"
- 性质: "过一点有且只有一条直线与已知直线垂直"
- 强调: "有且只有 = 存在且唯一"

### 清理计划
- FadeOut: subtitle, property_text, check_mark
- 保留: line_l, dot_P, perpendicular, right_angle_mark

---

## Scene 4: 性质2 - 最短距离 (30-50秒)
**目的**: 展示"垂线段最短"的核心性质

### 元素列表
1. 副标题: "性质2: 最短距离" (y=5.5)
2. 原有: line_l, dot_P, perpendicular (垂线段)
3. 其他连接线 PA, PB, PC (不同角度)
4. 距离标注 (Brace + 数值)
5. 对比动画
6. 定义文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 30.0s | 副标题 | `FadeIn(subtitle)` | 0.4s |
| 30.4s | 点A出现 | `FadeIn(dot_A)` | 0.3s |
| 30.7s | 线段PA绘制 | `Create(line_PA)` | 0.6s |
| 31.3s | 距离标注 | `FadeIn(brace_PA, label_PA)` | 0.5s |
| 31.8s | 点B出现 | `FadeIn(dot_B)` | 0.3s |
| 32.1s | 线段PB绘制 | `Create(line_PB)` | 0.6s |
| 32.7s | 距离标注 | `FadeIn(brace_PB, label_PB)` | 0.5s |
| 33.2s | 垂线段高亮 | `perpendicular.animate.set_color(YELLOW).set_stroke_width(6)` | 0.5s |
| 33.7s | 距离标注 | `FadeIn(brace_PH, label_PH)` | 0.5s |
| 34.2s | 对比闪烁 | `Indicate(label_PH)` | 0.6s |
| 34.8s | 恢复样式 | `perpendicular.animate.set_color(RED).set_stroke_width(3)` | 0.3s |
| 35.1s | 定义文字 | `Write(distance_def)` | 1.8s |
| 36.9s | 公式 | `Write(formula)` | 1.0s |
| 37.9s | 理解停顿 | `Wait(2.5)` | 2.5s |

### 文字内容
- 副标题: "性质2: 最短距离"
- 对比: "PH < PA", "PH < PB"
- 定义: "点到直线的距离 = 垂线段的长度"
- 强调: "这是最短距离!"

### 几何计算
```python
# 点A, B在直线l上的不同位置
self.A = np.array([0.5, 0, 0])
self.B = np.array([-3.0, 0, 0])

# 计算距离
self.dist_PH = np.linalg.norm(self.P - self.H)  # 垂线段
self.dist_PA = np.linalg.norm(self.P - self.A)  # 斜线段
self.dist_PB = np.linalg.norm(self.P - self.B)  # 斜线段

# 验证: PH < PA 且 PH < PB
assert self.dist_PH < self.dist_PA, "距离关系错误!"
assert self.dist_PH < self.dist_PB, "距离关系错误!"
```

### 清理计划
- FadeOut: subtitle, distance_def, formula, line_PA, line_PB, dots A/B, braces, labels
- 保留: line_l, dot_P, perpendicular, right_angle_mark

---

## Scene 5: 实际应用示例 (50-60秒)
**目的**: 展示垂线性质的实际应用

### 元素列表
1. 标题: "实际应用" (y=5.5)
2. 新点Q (y=2.5)
3. 点Q到直线l的垂线
4. 距离测量
5. 步骤说明

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 50.0s | 标题 | `FadeIn(title)` | 0.4s |
| 50.4s | 问题文字 | `Write(question)` | 1.0s |
| 51.4s | 点Q出现 | `FadeIn(dot_Q, scale=0.5)` | 0.3s |
| 51.7s | 步骤1文字 | `FadeIn(step1)` | 0.5s |
| 52.2s | 虚线引导 | `Create(guide_line)` | 0.6s |
| 52.8s | 垂足K | `FadeIn(dot_K)` | 0.3s |
| 53.1s | 步骤2文字 | `Transform(step1, step2)` | 0.4s |
| 53.5s | 垂线绘制 | `Create(perp_QK)` | 0.8s |
| 54.3s | 直角标记 | `FadeIn(right_angle_K)` | 0.3s |
| 54.6s | 步骤3文字 | `Transform(step2, step3)` | 0.4s |
| 55.0s | 距离标注 | `FadeIn(brace_QK, distance_value)` | 0.6s |
| 55.6s | 结论 | `Write(conclusion)` | 1.0s |
| 56.6s | 理解停顿 | `Wait(2.0)` | 2.0s |

### 文字内容
- 标题: "实际应用"
- 问题: "求点Q到直线l的距离"
- 步骤1: "① 过Q作l的垂线"
- 步骤2: "② 标记垂足K"
- 步骤3: "③ 测量QK长度"
- 结论: "距离 = QK长度"

### 几何计算
```python
# 新点Q
self.Q = np.array([1.5, 2.5, 0])

# 垂足K
self.K = np.array([self.Q[0], 0, 0])

# 距离
self.dist_QK = np.linalg.norm(self.Q - self.K)
```

### 清理计划
- FadeOut: 所有应用示例元素
- 保留: line_l (用于总结场景)

---

## Scene 6: 知识总结 (60-70秒)
**目的**: 回顾核心知识点

### 元素列表
1. 标题: "知识总结" (y=6)
2. 三个要点卡片
3. 强调图标

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 60.0s | 标题 | `Write(title)` | 0.5s |
| 60.5s | 卡片1滑入 | `card1.animate.shift(RIGHT*0)` | 0.5s |
| 61.0s | 卡片2滑入 | `card2.animate.shift(RIGHT*0)` | 0.5s |
| 61.5s | 卡片3滑入 | `card3.animate.shift(RIGHT*0)` | 0.5s |
| 62.0s | 图标闪烁 | `Flash(icons)` | 0.6s |
| 62.6s | 强调语 | `FadeIn(emphasis)` | 0.5s |
| 63.1s | 理解停顿 | `Wait(2.0)` | 2.0s |

### 文字内容
- 要点1: "定义: 两直线成直角 → 互相垂直"
- 要点2: "唯一性: 过一点有且只有一条垂线"
- 要点3: "最短: 垂线段是最短距离"
- 强调: "掌握垂线, 轻松解题!"

### 清理计划
- FadeOut: 所有总结元素

---

## Scene 7: 片尾关注 (70-75秒)
**目的**: 引导关注

### 元素列表
1. 作者信息放大版
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 70.0s | 作者名放大 | `Transform(author_info, large_author)` | 0.6s |
| 70.6s | ID显示 | `FadeIn(author_id)` | 0.3s |
| 70.9s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.5s |
| 71.4s | 装饰图标 | `FadeIn(decorations)` | 0.5s |
| 71.9s | 图标旋转 | `Rotate(decorations)` | 1.0s |
| 72.9s | 最终停顿 | `Wait(1.0)` | 1.0s |
| 73.9s | 全部淡出 | `FadeOut(VGroup(*all))` | 0.8s |

### 文字内容
- 作者: "上海初高中数学直通车"
- ID: "@emptyandcalm"
- 关注: "关注我, 学更多几何技巧!"

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| line_l | Scene 2 | Scene 7 | 主直线 |
| dot_P | Scene 2 | Scene 5 | 点P |
| perpendicular | Scene 2 | Scene 5 | 垂线PH |
| right_angle_mark | Scene 2 | Scene 5 | 直角标记 |
| attempt_lines | Scene 3 | Scene 3 | 临时尝试线 |
| line_PA, line_PB | Scene 4 | Scene 4 | 距离对比线 |
| dot_Q, perp_QK | Scene 5 | Scene 5 | 应用示例 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |
| outro_elements | Scene 7 | Scene 7 | 片尾元素 |

---

## 技术要点备忘

### 坐标边界检查
```python
# 安全边界
SAFE_X_MIN, SAFE_X_MAX = -4.0, 4.0
SAFE_Y_MIN, SAFE_Y_MAX = -7.0, 7.0

# 检查函数
def check_bounds(point):
    assert SAFE_X_MIN <= point[0] <= SAFE_X_MAX
    assert SAFE_Y_MIN <= point[1] <= SAFE_Y_MAX
```

### 直角标记创建
```python
def create_right_angle_mark(corner, p1, p2, size=0.2):
    v1 = (p1 - corner) / np.linalg.norm(p1 - corner) * size
    v2 = (p2 - corner) / np.linalg.norm(p2 - corner) * size
    return Polygon(corner, corner+v1, corner+v1+v2, corner+v2,
                   color=COLOR_RIGHT_ANGLE, stroke_width=2, fill_opacity=0)
```

### 距离标注模板
```python
brace = Brace(line, direction=LEFT, buff=0.1, color=COLOR_DISTANCE)
label = DecimalNumber(distance, num_decimal_places=2, 
                     color=COLOR_DISTANCE, font_size=20)
label.next_to(brace, LEFT, buff=0.05)
```

---

## 总时长分配

| 场景 | 起止时间 | 时长 | 占比 |
|------|---------|------|------|
| Scene 1: 开场 | 0-5s | 5s | 6.7% |
| Scene 2: 定义 | 5-15s | 10s | 13.3% |
| Scene 3: 唯一性 | 15-30s | 15s | 20.0% |
| Scene 4: 最短距离 | 30-50s | 20s | 26.7% |
| Scene 5: 应用 | 50-60s | 10s | 13.3% |
| Scene 6: 总结 | 60-70s | 10s | 13.3% |
| Scene 7: 片尾 | 70-75s | 5s | 6.7% |
| **总计** | **0-75s** | **75s** | **100%** |

---

## 验证清单

### 渲染前
- [ ] 所有几何计算在 `setup_geometry()` 完成
- [ ] 使用 `verify_geometry()` 验证正确性
- [ ] 中文使用 `Text(font="Noto Sans CJK SC")`
- [ ] 数学符号使用 `MathTex()`
- [ ] 虚线使用 `DashedLine`
- [ ] 所有坐标在安全边界内
- [ ] 字体大小符合规范
- [ ] 元素生命周期明确

### 渲染后
- [ ] 无元素溢出
- [ ] 无文字重叠
- [ ] 节奏流畅
- [ ] 总时长75秒左右
- [ ] 关键点有足够停顿
- [ ] 开头有钩子
- [ ] 结尾有作者信息

---

**脚本完成日期**: 2026-01-30
**预计渲染时间**: ~3分钟 (快速预览模式)