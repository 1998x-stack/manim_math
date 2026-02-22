# 圆的切线性质与判定 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等 (九年级)
- 核心知识点: 切线性质、切线判定、切线长定理

## 颜色配置
```python
COLOR_CIRCLE = "#3498db"           # 蓝色 - 圆
COLOR_TANGENT = "#e74c3c"          # 红色 - 切线
COLOR_RADIUS = "#2ecc71"           # 绿色 - 半径
COLOR_HIGHLIGHT = YELLOW           # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B           # 灰色 - 辅助线
COLOR_POINT = "#f39c12"            # 橙色 - 切点
COLOR_FORMULA = WHITE              # 白色 - 公式
```

## 几何预计算清单

### 场景1-3: 切线性质 (切线⊥半径)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心O | 固定点 | self.O |
| 半径 | 设定值2.0 | self.radius |
| 切点P | 圆上任意点 | self.P |
| 切线方向 | 半径OP的垂直方向 | tangent_dir |
| 切线端点 | P ± tangent_dir * length | tangent_start, tangent_end |
| 直角标记顶点 | P点 | self.P |

**关键几何关系验证**:
- 验证: OP · tangent_direction = 0 (点积为0，垂直)
- 验证: |OP| = radius

### 场景4-5: 切线判定 (过半径外端且垂直→切线)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 半径外端点Q | 圆上某点 | self.Q |
| 垂直于OQ的直线方向 | (-OQ_y, OQ_x, 0) | perp_dir |
| 候选切线 | Q + t*perp_dir | test_line |

**关键几何关系验证**:
- 验证: OQ · perp_dir = 0 (垂直)
- 验证: Q在圆上: |OQ| = radius
- 验证: 直线与圆只有一个交点Q

### 场景6-7: 切线长定理 (PA = PB)
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆外点P | 选取在圆外 | self.P_external |
| 切点A | 通过几何求解 | self.A |
| 切点B | 通过几何求解 | self.B |
| 切线长PA | |P - A| | self.PA |
| 切线长PB | |P - B| | self.PB |

**切点A, B的精确计算方法**:
```
设 P = (px, py), O = (ox, oy), r = radius
d = |PO| = sqrt((px-ox)^2 + (py-oy)^2)

切线长: l = sqrt(d^2 - r^2)

切点到PO的距离 = r
使用参数方程求解两个切点

向量PO方向: u = (O - P) / |O - P|
垂直方向: v = (-u_y, u_x, 0)

从O到切点A的向量: OA
|OA| = r
PA ⊥ OA

使用三角关系:
sin(θ) = r / d
cos(θ) = l / d

切点A = O + r * (cos(α), sin(α))
其中 α 满足 (A - P) · (A - O) = 0
```

**关键几何关系验证**:
- 验证: |PO| > radius (P在圆外)
- 验证: PA ⊥ OA (切线垂直半径)
- 验证: PB ⊥ OB (切线垂直半径)
- 验证: |PA| = |PB| (切线长相等)
- 验证: |PA|² + r² = |PO|² (勾股定理)

---

## Scene 1: 开场钩子 (3秒)
**目的**: 抓住注意力，提出问题

### 视觉元素
1. 作者标识 (顶部y=7)
2. 钩子问题 (y=6)
3. 圆与切线的神秘图形 (y=2)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 创建，保留全程 |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | 创建 |
| 1.1s | 圆淡入 | `Create(circle)` | 创建 |
| 1.6s | 切线快速划过 | `Create(tangent, run_time=0.5)` | 创建 |
| 2.2s | 问号闪烁 | `Flash(question_mark)` | 创建 |
| 2.8s | 等待 | `Wait(0.5)` | - |

### 清理
- FadeOut: hook_text, question_mark
- 保留: circle, tangent, author_info

---

## Scene 2: 切线性质 - 引入 (4秒)
**目的**: 展示切线与半径的垂直关系

### 视觉元素
1. 标题 "切线性质" (y=5.5)
2. 副标题 "切线垂直于过切点的半径" (y=4.8)
3. 圆O (中心y=1)
4. 切点P (圆上)
5. 半径OP (绿色)
6. 切线l (红色)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题写入 | `Write(title)` | 创建 |
| 0.5s | 副标题淡入 | `FadeIn(subtitle)` | 创建 |
| 1.0s | 标记圆心O | `FadeIn(o_dot), Write(o_label)` | 创建 |
| 1.5s | 标记切点P | `FadeIn(p_dot), Write(p_label)` | 创建 |
| 2.0s | 绘制半径OP | `Create(radius_line)` | 创建 |
| 2.5s | 绘制切线l | `Create(tangent_line)` | 创建 |
| 3.5s | 等待观察 | `Wait(1.0)` | - |

### 清理
- 保留: 所有元素用于下一场景

---

## Scene 3: 切线性质 - 证明垂直 (6秒)
**目的**: 用动画展示和强调垂直关系

### 视觉元素
1. 直角符号 (在P点)
2. 公式 "l ⊥ OP" (y=-4)
3. 旋转的半径演示
4. 跟随的切线

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 添加直角标记 | `FadeIn(right_angle)` | 创建 |
| 0.5s | 直角符号闪烁强调 | `Flash(right_angle, color=YELLOW)` | - |
| 1.0s | 公式写入 | `Write(formula)` | 创建 |
| 1.5s | 说明文字 | `FadeIn(explanation)` | 创建 |
| 2.0s | 半径旋转动画开始 | `Rotate(radius, angle=PI/3)` | - |
| 2.0s | 切线同步旋转 | `Rotate(tangent, angle=PI/3)` | - |
| 3.5s | 直角标记跟随 | `always_redraw(lambda: RightAngle(...))` | - |
| 5.0s | 停止旋转 | - | - |
| 5.5s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: title, subtitle, formula, explanation
- 保留: circle, radius, tangent, right_angle

---

## Scene 4: 切线判定 - 引入 (5秒)
**目的**: 介绍切线的判定方法

### 视觉元素
1. 标题 "切线判定" (y=5.5)
2. 副标题 "如何判断一条直线是否为切线?" (y=4.8)
3. 三个判定条件卡片 (y=-2 到 y=-5)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 清除旧场景 | `FadeOut(...)` | 销毁上一场景 |
| 0.5s | 标题写入 | `Write(title)` | 创建 |
| 1.0s | 副标题淡入 | `FadeIn(subtitle)` | 创建 |
| 1.5s | 条件1卡片滑入 | `card1.animate.shift(RIGHT*0)` | 创建 |
| 2.3s | 条件2卡片滑入 | `card2.animate.shift(RIGHT*0)` | 创建 |
| 3.1s | 条件3卡片滑入 | `card3.animate.shift(RIGHT*0)` | 创建 |
| 4.0s | 等待阅读 | `Wait(1.5)` | - |

**判定条件卡片内容**:
1. "① 过半径外端" (绿色图标)
2. "② 垂直于半径" (黄色图标)
3. "③ 与圆只有一个交点" (蓝色图标)

### 清理
- FadeOut: cards, subtitle
- 保留: title

---

## Scene 5: 切线判定 - 动画验证 (7秒)
**目的**: 动画演示判定条件的必要性

### 视觉元素
1. 圆O (重新绘制)
2. 半径OQ
3. 三条测试直线 (不同情况)
4. 检验标记 (✓ 或 ✗)

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 绘制圆和半径 | `Create(circle), Create(radius)` | 创建 |
| 1.0s | 测试1: 不过外端 | `Create(test_line_1)` | 创建 |
| 2.0s | 显示✗标记 | `FadeIn(cross_mark)` | 创建，销毁 |
| 2.5s | 测试2: 不垂直 | `Transform(test_line_1, test_line_2)` | 变换 |
| 3.5s | 显示✗标记 | `FadeIn(cross_mark)` | 创建，销毁 |
| 4.0s | 测试3: 满足条件 | `Transform(test_line_2, test_line_3)` | 变换 |
| 5.0s | 添加直角标记 | `FadeIn(right_angle)` | 创建 |
| 5.5s | 显示✓标记 | `FadeIn(check_mark)` | 创建 |
| 6.0s | 强调闪烁 | `Flash(check_mark, color=GREEN)` | - |
| 6.5s | 等待 | `Wait(1.0)` | - |

### 清理
- FadeOut: 所有测试元素
- 保留: circle

---

## Scene 6: 切线长定理 - 引入 (6秒)
**目的**: 介绍切线长的概念和定理

### 视觉元素
1. 标题 "切线长定理" (y=5.5)
2. 圆O (中心y=1)
3. 圆外点P (y=3, x=-2)
4. 两条切线PA, PB
5. 切点A, B
6. 切线长标注

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题写入 | `Write(title)` | 创建 |
| 0.5s | 定义文字 | `FadeIn(definition)` | 创建 |
| 1.0s | 标记圆外点P | `FadeIn(p_dot), Write(p_label)` | 创建 |
| 1.5s | 绘制切线PA | `Create(tangent_PA)` | 创建 |
| 2.5s | 标记切点A | `FadeIn(a_dot), Write(a_label)` | 创建 |
| 3.0s | 绘制切线PB | `Create(tangent_PB)` | 创建 |
| 4.0s | 标记切点B | `FadeIn(b_dot), Write(b_label)` | 创建 |
| 4.5s | 标注PA长度 | `FadeIn(brace_PA, label_PA)` | 创建 |
| 5.0s | 标注PB长度 | `FadeIn(brace_PB, label_PB)` | 创建 |
| 5.5s | 等待 | `Wait(1.0)` | - |

### 清理
- 保留: 所有元素用于下一场景

---

## Scene 7: 切线长定理 - 证明相等 (8秒)
**目的**: 证明PA = PB

### 视觉元素
1. 连接半径OA, OB
2. 连接OP
3. 直角标记 (∠OAP, ∠OBP)
4. 全等三角形标记
5. 公式 PA = PB

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 绘制半径OA, OB | `Create(radius_OA), Create(radius_OB)` | 创建 |
| 1.0s | 绘制OP | `Create(line_OP)` | 创建 |
| 1.5s | 添加直角标记 | `FadeIn(right_angle_A, right_angle_B)` | 创建 |
| 2.5s | 说明文字1 | `FadeIn(explanation1)` | 创建，销毁 |
| 3.5s | 高亮△OAP | `triangle_OAP.animate.set_color(YELLOW)` | 创建 |
| 4.0s | 高亮△OBP | `triangle_OBP.animate.set_color(YELLOW)` | 创建 |
| 4.5s | 全等标记 | `Write(congruent_symbol)` | 创建 |
| 5.5s | 说明文字2 | `FadeIn(explanation2)` | 创建，销毁 |
| 6.5s | 公式淡入 | `FadeIn(formula_equality)` | 创建 |
| 7.0s | 公式闪烁强调 | `Flash(formula_equality)` | - |
| 7.5s | 等待 | `Wait(1.5)` | - |

### 清理
- FadeOut: 所有说明元素
- 保留: 主图形和公式用于总结

---

## Scene 8: 总结与片尾 (6秒)
**目的**: 总结三个核心定理，引导关注

### 视觉元素
1. 三个知识卡片
2. 关键公式汇总
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 清除主场景 | `FadeOut(...)` | 销毁 |
| 0.5s | 卡片1滑入 | `card1.animate.shift(RIGHT*0)` | 创建 |
| 1.0s | 卡片2滑入 | `card2.animate.shift(RIGHT*0)` | 创建 |
| 1.5s | 卡片3滑入 | `card3.animate.shift(RIGHT*0)` | 创建 |
| 2.5s | 作者信息放大 | `Transform(author_info, author_large)` | 变换 |
| 3.5s | 关注提示 | `FadeIn(follow_text, shift=UP*0.3)` | 创建 |
| 4.5s | 装饰动画 | `Rotate(decorations)` | 创建 |
| 5.5s | 全部淡出 | `self.play(*[FadeOut(m) for m in self.mobjects])` | 销毁全部 |

---

## 元素生命周期追踪总表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| circle | Scene 1 | Scene 7 | 主圆 |
| hook_text | Scene 1 | Scene 1 | 临时钩子 |
| tangent_line | Scene 2 | Scene 3 | 切线示例 |
| radius_line | Scene 2 | Scene 3 | 半径示例 |
| right_angle | Scene 3 | Scene 4 | 直角标记 |
| test_lines | Scene 5 | Scene 5 | 临时测试 |
| tangent_PA | Scene 6 | Scene 7 | 切线PA |
| tangent_PB | Scene 6 | Scene 7 | 切线PB |
| triangles | Scene 7 | Scene 8 | 全等三角形 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 技术注意事项

### 1. 切点计算 (Scene 6-7)
```python
def calculate_tangent_points(P, O, radius):
    """
    从圆外点P到圆O(半径radius)的两个切点
    
    Returns: (A, B) 两个切点坐标
    """
    # 距离
    d = np.linalg.norm(P - O)
    
    # 切线长
    tangent_length = np.sqrt(d**2 - radius**2)
    
    # PO方向
    u = (O - P) / d
    
    # 垂直方向
    v = np.array([-u[1], u[0], 0])
    
    # 切点到O的距离向量
    # 使用三角关系
    cos_alpha = radius / d
    sin_alpha = tangent_length / d
    
    # 两个切点 (旋转两个方向)
    # OA = radius * (cos(θ) * u + sin(θ) * v)
    # 其中 θ 满足 PA ⊥ OA
    
    # 使用几何关系精确计算
    h = radius * tangent_length / d  # 从O到PA的垂直距离在PO上的投影
    
    # PO上的垂足点M
    M = P + h * u
    
    # 从M到两个切点的距离
    m_to_tangent = np.sqrt(radius**2 - h**2)
    
    # 两个切点
    A = M + m_to_tangent * v
    B = M - m_to_tangent * v
    
    return A, B
```

### 2. 直角标记方向 (所有场景)
- 使用 `RightAngle(line1, line2, quadrant=(1,1), length=0.3)`
- 根据实际角度位置调整 quadrant 参数
- 可能需要 other_angle=True

### 3. 动画节奏控制
- 关键概念停留: 2.0秒
- 普通说明: 1.0秒
- 过渡动画: 0.5秒

### 4. 文字与公式组合
```python
# 中文 + 公式
chinese = Text("切线长:", font="Noto Sans CJK SC", font_size=24)
formula = MathTex(r"PA = PB", font_size=24)
combined = VGroup(chinese, formula).arrange(RIGHT, buff=0.2)
```

### 5. 边界检查
- 所有元素 x ∈ [-4, 4]
- 主内容 y ∈ [-3, 5]
- 标题 y = 5.5
- 底部说明 y ∈ [-5, -4]

---

## 预期总时长分布

| 场景 | 时长 | 累计 |
|------|-----|------|
| Scene 1: 开场 | 3s | 3s |
| Scene 2: 切线性质引入 | 4s | 7s |
| Scene 3: 垂直关系 | 6s | 13s |
| Scene 4: 判定引入 | 5s | 18s |
| Scene 5: 判定验证 | 7s | 25s |
| Scene 6: 切线长引入 | 6s | 31s |
| Scene 7: 切线长证明 | 8s | 39s |
| Scene 8: 总结片尾 | 6s | 45s |

**总计**: 约45秒 (符合TikTok短视频规范)