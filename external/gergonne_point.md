# 热尔岗点 (Gergonne Point) - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 7 个
- 难度等级: 中等偏高（初中-高中）
- 输出格式: TikTok 竖屏 1080×1920

## 颜色配置
```python
COLOR_TRIANGLE = WHITE
COLOR_INCIRCLE = "#3498db"  # 蓝色 - 内切圆
COLOR_INCENTER = "#e74c3c"  # 红色 - 内心
COLOR_GERGONNE = "#f39c12" # 橙色 - 热尔岗点
COLOR_TANGENT = "#9b59b6"  # 紫色 - 切点
COLOR_CEVIAN = "#2ecc71"   # 绿色 - 连线
COLOR_AUXILIARY = GRAY_B
COLOR_HIGHLIGHT = YELLOW
```

## 几何预计算清单

### 主要元素
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 三角形顶点 | 精确坐标 | self.A, self.B, self.C |
| 边长 | np.linalg.norm | self.a, self.b, self.c |
| 内心 | 加权平均公式 | self.I |
| 内切圆半径 | 点到边距离 | self.r |
| 切点D (BC边) | 切线长定理 | self.D |
| 切点E (CA边) | 切线长定理 | self.E |
| 切点F (AB边) | 切线长定理 | self.F |
| 热尔岗点 | AD, BE, CF交点 | self.Ge |

### 切点计算公式（关键）
使用切线长公式：
- 设 BD = BF = x, CE = CD = y, AE = AF = z
- 则 a = x + y, b = y + z, c = z + x
- 解得：x = (a+c-b)/2, y = (a+b-c)/2, z = (b+c-a)/2
- 切点坐标：
  - D = B + (x/a) * (C - B)
  - E = C + (y/b) * (A - C)
  - F = A + (z/c) * (B - A)

### 验证项
- [ ] 内心到三边距离相等（验证内切圆）
- [ ] 切点位置正确（切线长相等）
- [ ] AD, BE, CF三线共点（塞瓦定理）
- [ ] 所有元素在边界内

---

## Scene 1: 开场钩子 (0-5秒)

### 目的
引起注意，提出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题
3. 三角形+内切圆快速展示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 三角形创建 | `Create(triangle)` | 1.0s |
| 2.1s | 内切圆快速出现 | `GrowFromCenter(incircle)` | 0.8s |
| 2.9s | 三个点闪烁 | `Flash(D), Flash(E), Flash(F)` | 0.6s |
| 3.5s | 神秘点出现 | `FadeIn(Ge_dot, scale=0.5)` | 0.5s |
| 4.0s | 等待理解 | `self.wait()` | 1.0s |

### 钩子文字
```
"连接顶点与内切圆切点，
这三条线会交于一点？"
```

### 清理
- FadeOut: hook_text
- 保留: triangle, author_info

---

## Scene 2: 定义介绍 (5-12秒)

### 目的
正式介绍热尔岗点的定义

### 元素
1. 标题："热尔岗点 Gergonne Point"
2. 定义文字
3. 三角形保持
4. 内切圆及内心

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 5.0s | 清除旧元素 | `FadeOut(incircle, Ge_dot)` | 0.4s |
| 5.4s | 标题出现 | `Write(title)` | 0.8s |
| 6.2s | 定义文字淡入 | `FadeIn(definition)` | 0.5s |
| 6.7s | 重新创建内切圆 | `Create(incircle)` | 1.2s |
| 7.9s | 内心标记 | `FadeIn(I_dot), Write(I_label)` | 0.5s |
| 8.4s | 等待阅读 | `self.wait()` | 1.5s |
| 9.9s | 清理文字 | `FadeOut(definition)` | 0.4s |

### 定义文字
```
"连接三角形顶点与
内切圆在对边上切点的
三条线段的交点"
```

### 清理
- FadeOut: title, definition
- 保留: triangle, incircle, I_dot, I_label

---

## Scene 3: 构造过程 - 找切点 (12-22秒)

### 目的
展示如何找到三个切点

### 元素
1. 步骤标题
2. 三个切点依次出现
3. 切点标签 D, E, F
4. 虚线表示垂直

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 步骤标题 | `FadeIn(step_text)` | 0.5s |
| 12.5s | 说明文字 | `FadeIn(explain_tangent)` | 0.5s |
| 13.0s | BC边高亮 | `bc_line.set_color(HIGHLIGHT)` | 0.3s |
| 13.3s | 切点D出现 | `FadeIn(D_dot, scale=0.5)` | 0.5s |
| 13.8s | 垂线ID | `Create(perp_ID)` | 0.6s |
| 14.4s | 标签D | `FadeIn(D_label)` | 0.3s |
| 14.7s | BC恢复 | `bc_line.set_color(TRIANGLE)` | 0.2s |
| 14.9s | CA边高亮 | `ca_line.set_color(HIGHLIGHT)` | 0.3s |
| 15.2s | 切点E出现 | `FadeIn(E_dot, scale=0.5)` | 0.5s |
| 15.7s | 垂线IE | `Create(perp_IE)` | 0.6s |
| 16.3s | 标签E | `FadeIn(E_label)` | 0.3s |
| 16.6s | CA恢复 | `ca_line.set_color(TRIANGLE)` | 0.2s |
| 16.8s | AB边高亮 | `ab_line.set_color(HIGHLIGHT)` | 0.3s |
| 17.1s | 切点F出现 | `FadeIn(F_dot, scale=0.5)` | 0.5s |
| 17.6s | 垂线IF | `Create(perp_IF)` | 0.6s |
| 18.2s | 标签F | `FadeIn(F_label)` | 0.3s |
| 18.5s | AB恢复 | `ab_line.set_color(TRIANGLE)` | 0.2s |
| 18.7s | 等待观察 | `self.wait()` | 1.5s |
| 20.2s | 清理说明 | `FadeOut(step_text, explain)` | 0.4s |

### 说明文字
```
"步骤1: 找到内切圆与三边的切点"
"内心到切点垂直于边"
```

### 清理
- FadeOut: step_text, explain_text, perp lines, bc/ca/ab highlights
- 保留: triangle, incircle, I_dot, D/E/F dots and labels

---

## Scene 4: 连接线段 (22-32秒)

### 目的
连接顶点到对边切点

### 元素
1. 步骤标题
2. 三条连线 AD, BE, CF
3. 强调"对边"的概念

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 22.0s | 步骤标题 | `FadeIn(step2_text)` | 0.5s |
| 22.5s | 说明"对边" | `FadeIn(explain_opposite)` | 0.5s |
| 23.0s | A点闪烁 | `Flash(A, color=HIGHLIGHT)` | 0.3s |
| 23.3s | 箭头A→D | `GrowArrow(arrow_AD)` | 0.4s |
| 23.7s | 线段AD | `Create(line_AD)` | 0.8s |
| 24.5s | 箭头消失 | `FadeOut(arrow_AD)` | 0.2s |
| 24.7s | B点闪烁 | `Flash(B, color=HIGHLIGHT)` | 0.3s |
| 25.0s | 箭头B→E | `GrowArrow(arrow_BE)` | 0.4s |
| 25.4s | 线段BE | `Create(line_BE)` | 0.8s |
| 26.2s | 箭头消失 | `FadeOut(arrow_BE)` | 0.2s |
| 26.4s | C点闪烁 | `Flash(C, color=HIGHLIGHT)` | 0.3s |
| 26.7s | 箭头C→F | `GrowArrow(arrow_CF)` | 0.4s |
| 27.1s | 线段CF | `Create(line_CF)` | 0.8s |
| 27.9s | 箭头消失 | `FadeOut(arrow_CF)` | 0.2s |
| 28.1s | 等待观察 | `self.wait()` | 1.5s |
| 29.6s | 清理说明 | `FadeOut(step2_text, explain)` | 0.4s |

### 说明文字
```
"步骤2: 连接顶点到对边切点"
"A的对边是BC，切点是D"
```

### 清理
- FadeOut: step2_text, explain_opposite
- 保留: triangle, incircle, tangent points, lines AD/BE/CF

---

## Scene 5: 热尔岗点出现 (32-42秒)

### 目的
展示三线共点，标记热尔岗点

### 元素
1. 热尔岗点Ge
2. 共点动画
3. 性质说明

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 32.0s | 内切圆淡化 | `incircle.set_opacity(0.3)` | 0.4s |
| 32.4s | 三线高亮 | `lines.set_color(CEVIAN)` | 0.5s |
| 32.9s | 热尔岗点出现 | `FadeIn(Ge_dot, scale=0.5)` | 0.6s |
| 33.5s | 闪光效果 | `Flash(Ge_dot, color=GERGONNE)` | 0.5s |
| 34.0s | 标签Ge | `Write(Ge_label)` | 0.5s |
| 34.5s | 中文标签 | `FadeIn(Ge_label_cn)` | 0.4s |
| 34.9s | 惊叹文字 | `FadeIn(amazing_text)` | 0.6s |
| 35.5s | 等待惊叹 | `self.wait()` | 1.5s |
| 37.0s | 性质文字 | `FadeIn(property_text)` | 0.8s |
| 37.8s | 等待阅读 | `self.wait()` | 2.0s |
| 39.8s | 清理文字 | `FadeOut(amazing, property)` | 0.4s |

### 文字内容
```
惊叹："三线共点！"
性质："这就是热尔岗点
三角形的一个特殊中心"
```

### 清理
- FadeOut: amazing_text, property_text
- 保留: triangle, Ge_dot, Ge_label, lines

---

## Scene 6: 塞瓦定理验证 (42-55秒)

### 目的
展示塞瓦定理验证共点性

### 元素
1. 塞瓦定理公式
2. 比值标注
3. 计算过程

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 42.0s | 标题出现 | `Write(ceva_title)` | 0.8s |
| 42.8s | 塞瓦公式 | `Write(ceva_formula)` | 1.2s |
| 44.0s | 标注BD | `FadeIn(brace_BD, label_x)` | 0.5s |
| 44.5s | 标注DC | `FadeIn(brace_DC, label_y)` | 0.5s |
| 45.0s | 标注CE | `FadeIn(brace_CE, label_y2)` | 0.5s |
| 45.5s | 标注EA | `FadeIn(brace_EA, label_z)` | 0.5s |
| 46.0s | 标注AF | `FadeIn(brace_AF, label_z2)` | 0.5s |
| 46.5s | 标注FB | `FadeIn(brace_FB, label_x2)` | 0.5s |
| 47.0s | 等待观察 | `self.wait()` | 1.0s |
| 48.0s | 计算步骤1 | `FadeIn(calc_step1)` | 0.8s |
| 48.8s | 等待 | `self.wait()` | 0.8s |
| 49.6s | 计算步骤2 | `TransformMatchingTex(step1, step2)` | 1.0s |
| 50.6s | 等待 | `self.wait()` | 0.8s |
| 51.4s | 结果 | `FadeIn(result, scale=1.2)` | 0.8s |
| 52.2s | 结果高亮 | `result.set_color(HIGHLIGHT)` | 0.3s |
| 52.5s | 等待庆祝 | `self.wait()` | 1.5s |
| 54.0s | 清理 | `FadeOut(all_ceva_elements)` | 0.6s |

### 公式内容
```
塞瓦定理：
\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1

计算：
\frac{x}{y} \cdot \frac{y}{z} \cdot \frac{z}{x} = 1

证明成立！
```

### 清理
- FadeOut: all Ceva elements
- 保留: triangle, Ge_dot, Ge_label

---

## Scene 7: 特性总结与片尾 (55-75秒)

### 目的
总结特性，引导关注

### 元素
1. 特性卡片
2. 关注引导
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 55.0s | 三角形缩小移上 | `triangle.scale(0.6).to_edge(UP)` | 1.0s |
| 56.0s | 特性标题 | `Write(properties_title)` | 0.6s |
| 56.6s | 特性1滑入 | `property1.shift(RIGHT*0)` | 0.4s |
| 57.0s | 特性2滑入 | `property2.shift(RIGHT*0)` | 0.4s |
| 57.4s | 特性3滑入 | `property3.shift(RIGHT*0)` | 0.4s |
| 57.8s | 特性4滑入 | `property4.shift(RIGHT*0)` | 0.4s |
| 58.2s | 等待阅读 | `self.wait()` | 2.5s |
| 60.7s | 清理图形 | `FadeOut(triangle, Ge, properties)` | 0.8s |
| 61.5s | 作者名放大 | `Transform(author, large_author)` | 0.8s |
| 62.3s | ID出现 | `FadeIn(author_id)` | 0.5s |
| 62.8s | 关注文字 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 63.4s | 装饰动画 | `Rotate(decorations)` | 1.5s |
| 64.9s | 等待 | `self.wait()` | 1.0s |
| 65.9s | 全部淡出 | `FadeOut(all)` | 1.0s |

### 特性卡片内容
```
✓ 三线共点（塞瓦定理）
✓ 内心的等角共轭点
✓ 切点三角形的类似重心
✓ Kimberling中心 X₇
```

### 关注文字
```
"关注我，学更多几何奇点！"
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 持续场景 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程 | 顶部标识 |
| triangle | Scene 1 | Scene 7 | 全程 | 主三角形 |
| incircle | Scene 1 | Scene 5 | 1,2,3,4,5 | 内切圆 |
| I_dot | Scene 2 | Scene 5 | 2,3,4,5 | 内心 |
| D_dot | Scene 3 | Scene 7 | 3,4,5,6,7 | 切点D |
| E_dot | Scene 3 | Scene 7 | 3,4,5,6,7 | 切点E |
| F_dot | Scene 3 | Scene 7 | 3,4,5,6,7 | 切点F |
| line_AD | Scene 4 | Scene 7 | 4,5,6,7 | 连线AD |
| line_BE | Scene 4 | Scene 7 | 4,5,6,7 | 连线BE |
| line_CF | Scene 4 | Scene 7 | 4,5,6,7 | 连线CF |
| Ge_dot | Scene 5 | Scene 7 | 5,6,7 | 热尔岗点 |
| perp_ID | Scene 3 | Scene 3 | 3 | 临时垂线 |
| perp_IE | Scene 3 | Scene 3 | 3 | 临时垂线 |
| perp_IF | Scene 3 | Scene 3 | 3 | 临时垂线 |
| ceva_elements | Scene 6 | Scene 6 | 6 | 塞瓦定理标注 |

---

## 时间节奏分配

| 场景 | 时长 | 比例 | 节奏 |
|------|------|------|------|
| Scene 1: 开场 | 5s | 6.7% | 快 - 抓注意力 |
| Scene 2: 定义 | 7s | 9.3% | 中 - 建立概念 |
| Scene 3: 切点 | 10s | 13.3% | 慢 - 关键步骤 |
| Scene 4: 连线 | 10s | 13.3% | 中 - 构造过程 |
| Scene 5: 共点 | 10s | 13.3% | 慢 - 核心发现 |
| Scene 6: 验证 | 13s | 17.3% | 慢 - 数学证明 |
| Scene 7: 总结 | 20s | 26.7% | 中慢 - 巩固+关注 |
| **总计** | **75s** | **100%** | - |

---

## 几何验证代码片段

```python
def verify_all_geometry(self):
    """完整的几何验证"""
    eps = 1e-6
    
    # 1. 验证内心性质
    dist_AB = GeometryCalculator.distance_point_to_line(self.I, self.A, self.B)
    dist_BC = GeometryCalculator.distance_point_to_line(self.I, self.B, self.C)
    dist_CA = GeometryCalculator.distance_point_to_line(self.I, self.C, self.A)
    assert abs(dist_AB - dist_BC) < eps, "内心到边距离不等"
    assert abs(dist_BC - dist_CA) < eps, "内心到边距离不等"
    
    # 2. 验证切点位置（切线长相等）
    BD = np.linalg.norm(self.D - self.B)
    BF = np.linalg.norm(self.F - self.B)
    assert abs(BD - BF) < eps, "切线长不等: BD ≠ BF"
    
    CD = np.linalg.norm(self.D - self.C)
    CE = np.linalg.norm(self.E - self.C)
    assert abs(CD - CE) < eps, "切线长不等: CD ≠ CE"
    
    AE = np.linalg.norm(self.E - self.A)
    AF = np.linalg.norm(self.F - self.A)
    assert abs(AE - AF) < eps, "切线长不等: AE ≠ AF"
    
    # 3. 验证热尔岗点在三条线上
    dist_Ge_to_AD = GeometryCalculator.distance_point_to_line(self.Ge, self.A, self.D)
    dist_Ge_to_BE = GeometryCalculator.distance_point_to_line(self.Ge, self.B, self.E)
    dist_Ge_to_CF = GeometryCalculator.distance_point_to_line(self.Ge, self.C, self.F)
    assert dist_Ge_to_AD < eps, "Ge不在AD上"
    assert dist_Ge_to_BE < eps, "Ge不在BE上"
    assert dist_Ge_to_CF < eps, "Ge不在CF上"
    
    # 4. 验证塞瓦定理
    BD_DC = BD / np.linalg.norm(self.C - self.D)
    CE_EA = CE / np.linalg.norm(self.A - self.E)
    AF_FB = AF / np.linalg.norm(self.B - self.F)
    product = BD_DC * CE_EA * AF_FB
    assert abs(product - 1.0) < eps, f"塞瓦定理失败: {product} ≠ 1"
    
    print("✓ 所有几何验证通过")
```

---

## 注意事项

### 精度要求
- 所有坐标计算精确到小数点后10位
- 使用 NumPy 进行所有几何计算
- 避免任何臆想坐标

### 视觉优化
- 切点用较大的点表示（radius=0.08）
- 热尔岗点最大（radius=0.12）
- 连线使用不同颜色区分
- 适当使用闪光效果突出重点

### 文字处理
- 所有中文使用 Text() + font="Noto Sans CJK SC"
- 所有数学公式使用 MathTex()
- 度数符号使用 ^\circ

### 动画流畅度
- 关键步骤后停留1.5-2秒
- 过渡动画0.4-0.6秒
- 避免过快的切换