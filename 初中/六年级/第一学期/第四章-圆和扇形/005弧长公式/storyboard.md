# 弧长公式 - 动画分镜脚本
<!-- /root/code/sss/media/videos/arc_length_formula/1920p60/ArcLengthFormula.mp4 -->

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 7 个
- 难度等级: 中等 (六年级)
- 主题: 圆和扇形 - 弧长公式

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"        # 蓝色 - 主圆
COLOR_ARC = "#e74c3c"           # 红色 - 弧
COLOR_RADIUS = "#2ecc71"        # 绿色 - 半径
COLOR_ANGLE = "#f39c12"         # 橙色 - 圆心角
COLOR_FORMULA = "#9b59b6"       # 紫色 - 公式
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | (0, 0, 0) | self.center |
| 半径 | 2.0 | self.radius |
| 起始角 | 30° | self.start_angle |
| 结束角 | 150° | self.end_angle |
| 圆心角 | 120° | self.central_angle |
| 弧长 | (120π×2)/180 | self.arc_length |
| 圆周长 | 2π×2 | self.circumference |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 吸引注意力 + 引出主题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 完整圆 + 弧高亮闪烁

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "如何计算弧长?" |
| 1.2s | 圆形创建 | `Create(circle)` |
| 2.0s | 弧高亮闪烁 | `Flash(arc)` + 变红色 |
| 3.5s | 等待理解 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: circle, author_info

---

## Scene 2: 圆周长复习 (8-10秒)
**目的**: 回顾基础知识 - 圆周长公式

### 元素
1. 完整圆
2. 半径标注
3. 圆周长公式
4. 动画展开圆周

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` - "首先, 回顾圆周长" |
| 0.8s | 半径线创建 | `Create(radius_line)` |
| 1.2s | 半径标注 | `FadeIn(radius_label)` - "r" |
| 2.0s | 公式书写 | `Write(formula)` - "C = 2πr" |
| 3.0s | 圆"展开"成直线 | `Transform(circle, line)` - 创意动画 |
| 4.5s | 标注长度 | `Brace` + "2πr" |
| 6.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, 展开的线, brace
- 保留: circle (恢复原状), radius_line, radius_label

---

## Scene 3: 弧的概念 (8-10秒)
**目的**: 引入弧 - 圆周的一部分

### 元素
1. 完整圆
2. 高亮弧
3. 圆心角
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "弧: 圆周的一部分" |
| 0.8s | 弧高亮 | `Create(arc)` - 红色加粗 |
| 1.5s | 半径1创建 | `Create(radius1)` - 到起点 |
| 2.0s | 半径2创建 | `Create(radius2)` - 到终点 |
| 2.5s | 圆心角标注 | `Create(angle_arc)` + `MathTex("n°")` |
| 3.5s | 说明文字 | `FadeIn(explain)` - "圆心角决定弧的大小" |
| 5.0s | 等待 | `Wait(2.0)` - 重点停留 |

### 清理
- FadeOut: title, explain
- 保留: circle, arc, radius1, radius2, angle_arc, angle_label

---

## Scene 4: 比例关系推导 (12-15秒)
**目的**: 核心推理 - 弧长与圆心角的关系

### 元素
1. 圆心角 n°
2. 完整圆 360°
3. 比例关系式
4. 动画演示比例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "找规律: 比例关系" |
| 1.0s | 问题1 | `FadeIn(question1)` - "圆心角是多少?" |
| 1.5s | 答案1 | `FadeIn(answer1)` - "n°" (指向角) |
| 2.5s | 问题2 | `FadeIn(question2)` - "完整圆是多少?" |
| 3.0s | 答案2 | `FadeIn(answer2)` - "360°" (指向整圆) |
| 4.0s | 比例式1 | `Write(ratio1)` - "弧长/圆周长 = n°/360°" |
| 5.5s | 分数可视化 | 扇形饼图动画 - 展示n/360的含义 |
| 7.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, question1, question2, answer1, answer2, 饼图
- 保留: ratio1 (移到顶部)

---

## Scene 5: 弧长公式推导 (12-15秒)
**目的**: 数学推导 - 得出三个公式形式

### 元素
1. 比例关系式
2. 代入圆周长
3. 化简步骤
4. 三个公式形式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "推导弧长公式" |
| 1.0s | Step 1 | `TransformMatchingTex(ratio1, step1)` |
|      |        | "l/2πr = n/360" |
| 2.5s | Step 2 | `TransformMatchingTex(step1, step2)` |
|      |        | "l = (n/360) × 2πr" - 高亮公式2 |
| 4.0s | Step 3 | `TransformMatchingTex(step2, step3)` |
|      |        | "l = (nπr)/180" - 高亮公式1 |
| 5.5s | 三公式并列 | 排列三个公式, 用框标注 |
|      |           | 公式1: l = (nπr)/180 |
|      |           | 公式2: l = (n/360) × 2πr |
|      |           | 公式3: l = αr (弧度制) |
| 8.0s | 等待 | `Wait(2.5)` - 难点停留 |

### 清理
- FadeOut: title, step推导过程
- 保留: 三公式框 (移到底部)

---

## Scene 6: 实例计算 (15-18秒)
**目的**: 应用公式 - 具体例题

### 元素
1. 题目描述
2. 已知条件标注
3. 公式选择
4. 计算过程
5. 答案

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "实战演练" |
| 0.8s | 题目 | `FadeIn(problem)` |
|      |      | "已知: r=3cm, n=120°, 求弧长l" |
| 2.0s | 图形标注 | 在圆上标注 r=3, 角=120° |
| 3.5s | 公式选择 | 高亮公式1: l = (nπr)/180 |
| 4.5s | Step 1 | `Write(calc1)` - "l = (120π×3)/180" |
| 5.5s | Step 2 | `TransformMatchingTex` - "l = 360π/180" |
| 6.5s | Step 3 | `TransformMatchingTex` - "l = 2π cm" |
| 7.5s | 答案框 | `SurroundingRectangle` - 黄色高亮答案 |
| 8.5s | 数值近似 | `FadeIn` - "≈ 6.28 cm" |
| 10.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有计算元素
- 保留: circle, arc (回到干净状态)

---

## Scene 7: 片尾总结 + 关注 (8-10秒)
**目的**: 总结要点 + 引导关注

### 元素
1. 知识点总结卡片
2. 三个公式回顾
3. 记忆技巧
4. 作者信息放大
5. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "弧长公式总结" |
| 1.0s | 要点1 | `FadeIn(point1)` - "弧长 = 圆周长 × 角度比例" |
| 2.0s | 要点2 | `FadeIn(point2)` - "三种公式形式, 灵活选择" |
| 3.0s | 公式卡片 | 三公式并列展示 |
| 4.5s | 记忆技巧 | `FadeIn(tip)` - "记住: n/360 = 角度比" |
| 6.0s | 作者信息 | 放大 author_info |
| 7.0s | 关注提示 | `FadeIn(follow)` - "关注我, 学更多数学!" |
| 8.0s | 图标动画 | 小圆圈旋转装饰 |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终在顶部 |
| circle | Scene 1 | Scene 7 | 主圆, 贯穿全程 |
| arc | Scene 1 | Scene 7 | 弧, 多次高亮 |
| radius_line | Scene 2 | Scene 6 | 半径标注 |
| angle_arc | Scene 3 | Scene 6 | 圆心角标注 |
| formulas | Scene 5 | Scene 7 | 三个公式 |

---

## 关键技术点

### 1. 圆和弧的创建
```python
circle = Circle(radius=self.radius, color=COLOR_CIRCLE)
arc = Arc(
    radius=self.radius,
    start_angle=self.start_angle * DEGREES,
    angle=self.central_angle * DEGREES,
    color=COLOR_ARC,
    stroke_width=6
)
```

### 2. 圆心角标注
```python
angle_arc = Angle(
    radius_line1, radius_line2,
    radius=0.5,
    color=COLOR_ANGLE
)
angle_label = MathTex("n°").next_to(angle_arc, ...)
```

### 3. 公式变换动画
```python
# 使用 TransformMatchingTex 实现公式的平滑过渡
formula1 = MathTex(r"{{l}} \over {{2\pi r}} = {{n}} \over {{360}}")
formula2 = MathTex(r"{{l}} = {{n}} \over {{360}} \times {{2\pi r}}")
self.play(TransformMatchingTex(formula1, formula2))
```

### 4. 比例可视化 (饼图)
```python
# 使用多个扇形组合
full_circle = Circle(...)
sector = Sector(
    outer_radius=radius,
    angle=self.central_angle * DEGREES,
    start_angle=self.start_angle * DEGREES,
    fill_opacity=0.3
)
```

---

## 字体大小规范应用
- 标题: 36px
- 公式: 28px
- 说明文字: 22px
- 标注 (r, n°): 20px
- 作者信息: 20px

## 时间节奏控制
- 简单动画: 0.5-0.8s
- 公式书写: 0.8-1.2s
- 关键推导: 1.5-2.0s
- 难点停留: 2.0-2.5s
- 场景过渡: 0.4-0.6s

## 预期总时长
Scene 1: 4-5s
Scene 2: 8-10s
Scene 3: 8-10s
Scene 4: 12-15s
Scene 5: 12-15s
Scene 6: 15-18s
Scene 7: 8-10s
**总计: 67-83秒** ✓ 符合TikTok短视频标准