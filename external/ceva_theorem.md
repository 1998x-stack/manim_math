# 塞瓦定理与塞瓦三角形 - 动画分镜脚本

## 元信息
- 目标时长: 75-85 秒
- 场景数量: 6 个
- 难度等级: 中高
- 核心概念: 塞瓦定理 - 三线共点的充要条件

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 主三角形
COLOR_CEVIAN = "#e74c3c"        # 红色 - 塞瓦线
COLOR_CEVA_POINT = "#f39c12"    # 橙色 - 塞瓦点P
COLOR_CEVIAN_TRIANGLE = "#2ecc71"  # 绿色 - 塞瓦三角形DEF
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
COLOR_RATIO = "#9b59b6"         # 紫色 - 比例标记
```

## 几何预计算清单

### 基准参数
```python
SCALE = 1.0
OFFSET = UP * 1.0
```

### 主要点位
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 点A | 手动定义 | self.A | 三角形顶点A |
| 点B | 手动定义 | self.B | 三角形顶点B |
| 点C | 手动定义 | self.C | 三角形顶点C |
| 塞瓦点P | 手动定义（三角形内部） | self.P | 三条塞瓦线的交点 |
| 点D | 直线AP与BC的交点 | self.D | BC边上的分点 |
| 点E | 直线BP与CA的交点 | self.E | CA边上的分点 |
| 点F | 直线CP与AB的交点 | self.F | AB边上的分点 |

### 关键计算

#### 1. 直线交点计算（线段与边的交点）
```python
# D点：直线AP与BC的交点
# 参数方程：P + t*(A-P) 与 B + s*(C-B)
def line_intersection(P1, D1, P2, D2):
    """计算两直线交点"""
    # 详见 GeometryCalculator.line_intersection
```

#### 2. 塞瓦比例计算
```python
# 计算有向线段比
AD_over_DB = signed_ratio(A, D, B)  # AD/DB
BE_over_EC = signed_ratio(B, E, C)  # BE/EC
CF_over_FA = signed_ratio(C, F, A)  # CF/FA

# 塞瓦定理验证
product = AD_over_DB * BE_over_EC * CF_over_FA
assert abs(product - 1.0) < 1e-6  # 应该等于1
```

### 验证计算
```python
# 1. 验证D、E、F在对应边上
assert point_on_segment(D, B, C)
assert point_on_segment(E, C, A)
assert point_on_segment(F, A, B)

# 2. 验证三线共点于P
assert lines_concurrent(A, D, B, E, C, F)

# 3. 验证塞瓦定理
product = (AD/DB) * (BE/EC) * (CF/FA)
assert abs(product - 1.0) < epsilon
```

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 吸引注意力，引出三线共点问题

### 元素
1. 作者标识（顶部）
2. 钩子问题："三条线什么时候会交于一点?"
3. 三角形ABC出现
4. 三条看似随机的线段

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 三角形创建 | `Create(triangle)` | 1.0s |
| 2.1s | 顶点标签出现 | `FadeIn(labels)` | 0.4s |
| 2.5s | 三条线段依次绘制 | `Create(cevian1, 2, 3)` | 1.2s |
| 3.7s | 问号闪烁 | `Write(question_mark)` | 0.4s |
| 4.1s | 等待 | `Wait()` | 0.9s |

### 坐标布局
```
A: (-2.5, 1.5, 0) * SCALE + OFFSET
B: (2.5, -1.0, 0) * SCALE + OFFSET
C: (-1.0, -1.5, 0) * SCALE + OFFSET
P: (0.2, 0.3, 0) * SCALE + OFFSET  # 三角形内部
hook_text: UP * 6
question_mark: DOWN * 4
```

### 清理
- FadeOut: hook_text, question_mark
- 保留: triangle, labels, author

---

## Scene 2: 揭示塞瓦定理 (5-15秒)

**目的**: 介绍塞瓦定理及其公式

### 元素
1. 标题："塞瓦定理 Ceva's Theorem"
2. 塞瓦点P高亮
3. 三条塞瓦线AD、BE、CF
4. 塞瓦定理公式

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 5.0s | 标题淡入 | `Write(title)` | 0.8s |
| 5.8s | 清除旧线，塞瓦点P闪烁 | `FadeOut(old), Flash(P)` | 0.6s |
| 6.4s | P点放大高亮 | `dot_P.animate.scale(2)` | 0.5s |
| 6.9s | 标签P出现 | `FadeIn(label_P)` | 0.3s |
| 7.2s | 塞瓦线AD绘制 | `Create(cevian_AD)` | 0.8s |
| 8.0s | 点D标记 | `FadeIn(dot_D, label_D)` | 0.4s |
| 8.4s | 塞瓦线BE绘制 | `Create(cevian_BE)` | 0.8s |
| 9.2s | 点E标记 | `FadeIn(dot_E, label_E)` | 0.4s |
| 9.6s | 塞瓦线CF绘制 | `Create(cevian_CF)` | 0.8s |
| 10.4s | 点F标记 | `FadeIn(dot_F, label_F)` | 0.4s |
| 10.8s | 说明文字："三线共点于P" | `FadeIn(concurrent_text)` | 0.6s |
| 11.4s | 塞瓦定理公式出现 | `Write(ceva_formula)` | 1.2s |
| 12.6s | 公式高亮 | `Indicate(ceva_formula)` | 0.6s |
| 13.2s | 等待 | `Wait()` | 1.8s |

### 关键计算
```python
# 计算D、E、F点（直线交点）
# D: 直线AP与BC的交点
dir_AP = self.A - self.P
D = line_intersection(self.P, dir_AP, self.B, self.C - self.B)

# E: 直线BP与CA的交点
dir_BP = self.B - self.P
E = line_intersection(self.P, dir_BP, self.C, self.A - self.C)

# F: 直线CP与AB的交点
dir_CP = self.C - self.P
F = line_intersection(self.P, dir_CP, self.A, self.B - self.A)
```

### 公式显示
```python
ceva_formula = MathTex(
    r"\frac{AD}{DB} \times \frac{BE}{EC} \times \frac{CF}{FA} = 1",
    font_size=32,
    color=COLOR_HIGHLIGHT
).move_to(DOWN * 5)
```

### 清理
- FadeOut: title, concurrent_text
- 保留: triangle, cevians, P, D, E, F, ceva_formula

---

## Scene 3: 验证比例关系 (15-30秒)

**目的**: 详细展示如何验证塞瓦定理

### 子步骤

#### 3.1 标注第一个比例 AD/DB (15-19秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 15.0s | 说明："计算各线段比例" | `FadeIn(explain_text)` | 0.6s |
| 15.6s | BC边高亮 | `bc_line.animate.set_stroke(YELLOW, 4)` | 0.4s |
| 16.0s | AD段标注 | `Create(brace_AD)`, `FadeIn(label_AD)` | 0.6s |
| 16.6s | DB段标注 | `Create(brace_DB)`, `FadeIn(label_DB)` | 0.6s |
| 17.2s | 比值显示 | `Write(ratio_1)`: "AD/DB ≈ 1.5" | 0.7s |
| 17.9s | 等待 | `Wait()` | 1.1s |

#### 3.2 标注第二个比例 BE/EC (19-23秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 19.0s | CA边高亮 | `ca_line.animate.set_stroke(YELLOW, 4)` | 0.4s |
| 19.4s | BE段标注 | `Create(brace_BE)`, `FadeIn(label_BE)` | 0.6s |
| 20.0s | EC段标注 | `Create(brace_EC)`, `FadeIn(label_EC)` | 0.6s |
| 20.6s | 比值显示 | `Write(ratio_2)`: "BE/EC ≈ 2.0" | 0.7s |
| 21.3s | 等待 | `Wait()` | 1.7s |

#### 3.3 标注第三个比例 CF/FA (23-27秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 23.0s | AB边高亮 | `ab_line.animate.set_stroke(YELLOW, 4)` | 0.4s |
| 23.4s | CF段标注 | `Create(brace_CF)`, `FadeIn(label_CF)` | 0.6s |
| 24.0s | FA段标注 | `Create(brace_FA)`, `FadeIn(label_FA)` | 0.6s |
| 24.6s | 比值显示 | `Write(ratio_3)`: "CF/FA ≈ 0.33" | 0.7s |
| 25.3s | 等待 | `Wait()` | 1.7s |

#### 3.4 计算乘积 (27-30秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 27.0s | 三个比值移动到一起 | `ratio_group.animate.arrange(RIGHT)` | 0.8s |
| 27.8s | 乘积计算显示 | `Write(product_calc)`: "1.5 × 2.0 × 0.33 ≈ 1.0" | 1.0s |
| 28.8s | 验证勾标记 | `FadeIn(checkmark)`, `Flash(product)` | 0.6s |
| 29.4s | 等待 | `Wait()` | 0.6s |

### 清理
- FadeOut: all braces, labels, ratios, product
- 保留: triangle, cevians, P, D, E, F

---

## Scene 4: 塞瓦三角形DEF (30-45秒)

**目的**: 引入塞瓦三角形（切点三角形）的概念

### 元素
1. 塞瓦三角形DEF
2. 说明文字
3. 对比原三角形

### 动画序列
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 30.0s | 标题："塞瓦三角形" | `Write(cevian_triangle_title)` | 0.7s |
| 30.7s | 说明："由三个分点D、E、F构成" | `FadeIn(explanation)` | 0.7s |
| 31.4s | D、E、F点放大高亮 | `dots.animate.scale(1.5)` | 0.5s |
| 31.9s | 连接DE | `Create(edge_DE)` | 0.6s |
| 32.5s | 连接EF | `Create(edge_EF)` | 0.6s |
| 33.1s | 连接FD | `Create(edge_FD)` | 0.6s |
| 33.7s | 塞瓦三角形填充 | `FadeIn(cevian_tri_fill)` | 0.8s |
| 34.5s | 原三角形变淡 | `triangle.animate.set_opacity(0.3)` | 0.5s |
| 35.0s | 塞瓦三角形高亮旋转 | `Rotate(cevian_tri, PI/12)` | 1.0s |
| 36.0s | 性质说明 | `FadeIn(property_text)` | 0.8s |
| 36.8s | 等待 | `Wait()` | 2.2s |

### 关键代码
```python
# 塞瓦三角形
cevian_triangle = Polygon(
    self.D, self.E, self.F,
    color=COLOR_CEVIAN_TRIANGLE,
    stroke_width=4,
    fill_opacity=0.2,
    fill_color=COLOR_CEVIAN_TRIANGLE
)
```

### 坐标布局
```
cevian_triangle_title: UP * 5.5
explanation: UP * 4.8
property_text: DOWN * 5 ("P点的切点三角形")
```

### 清理
- 原三角形恢复不透明度
- FadeOut: title, explanation, property_text
- 保留: cevian_triangle, P

---

## Scene 5: 特殊情况 - 重心 (45-60秒)

**目的**: 展示塞瓦定理的应用 - 证明重心存在

### 子步骤

#### 5.1 引入特殊情况 (45-48秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 45.0s | 清除塞瓦三角形 | `FadeOut(cevian_triangle, cevians)` | 0.6s |
| 45.6s | 标题："应用：证明重心" | `Write(centroid_title)` | 0.8s |
| 46.4s | 说明："取三边中点" | `FadeIn(midpoint_text)` | 0.6s |
| 47.0s | 等待 | `Wait()` | 1.0s |

#### 5.2 绘制中线 (48-53秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 48.0s | BC中点M₁出现 | `FadeIn(dot_M1, label_M1)` | 0.4s |
| 48.4s | 中线AM₁绘制 | `Create(median_1)` | 0.8s |
| 49.2s | CA中点M₂出现 | `FadeIn(dot_M2, label_M2)` | 0.4s |
| 49.6s | 中线BM₂绘制 | `Create(median_2)` | 0.8s |
| 50.4s | AB中点M₃出现 | `FadeIn(dot_M3, label_M3)` | 0.4s |
| 50.8s | 中线CM₃绘制 | `Create(median_3)` | 0.8s |
| 51.6s | 等待 | `Wait()` | 1.4s |

#### 5.3 应用塞瓦定理 (53-58秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 53.0s | 说明："每个比值都是1" | `FadeIn(ratio_text)` | 0.7s |
| 53.7s | 公式显示 | `Write(centroid_formula)`: "1×1×1=1" | 1.0s |
| 54.7s | 验证勾 | `FadeIn(checkmark)` | 0.4s |
| 55.1s | 重心G闪烁 | `Flash(centroid_G)` | 0.5s |
| 55.6s | 标签G | `FadeIn(label_G)`: "重心G" | 0.5s |
| 56.1s | 说明："三条中线共点!" | `Write(conclusion)` | 0.8s |
| 56.9s | 等待 | `Wait()` | 1.1s |

### 几何计算
```python
# 三边中点
M1_BC = (self.B + self.C) / 2
M2_CA = (self.C + self.A) / 2
M3_AB = (self.A + self.B) / 2

# 重心（三条中线交点）
G = (self.A + self.B + self.C) / 3

# 验证：AM1/M1B = BM2/M2C = CM3/M3A = 1
```

### 清理
- FadeOut: medians, midpoints, formulas, texts
- 保留: triangle, centroid_G

---

## Scene 6: 总结与应用 (60-80秒)

**目的**: 总结塞瓦定理的重要性和应用

### 子步骤

#### 6.1 性质总结 (60-68秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 60.0s | 清屏 | `FadeOut(all)` | 0.6s |
| 60.6s | 标题："塞瓦定理的威力" | `Write(summary_title)` | 0.8s |
| 61.4s | 卡片1："证明三线共点" | `FadeIn(card_1)` | 0.7s |
| 62.1s | 卡片2："比例→共点" | `FadeIn(card_2)` | 0.7s |
| 62.8s | 卡片3："重心、内心..." | `FadeIn(card_3)` | 0.7s |
| 63.5s | 卡片4："竞赛必备工具" | `FadeIn(card_4)` | 0.7s |
| 64.2s | 等待 | `Wait()` | 3.8s |

#### 6.2 实例展示 (68-75秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 68.0s | 小三角形+重心闪烁 | `FadeIn(example_tri)` | 0.6s |
| 68.6s | 标注："重心" | `FadeIn(centroid_label)` | 0.4s |
| 69.0s | 小三角形+内心闪烁 | `Transform(to incenter)` | 0.8s |
| 69.8s | 标注："内心" | `Transform(label)` | 0.4s |
| 70.2s | 强调文字 | `Write(emphasis)`: "掌握塞瓦，轻松解题!" | 1.0s |
| 71.2s | 等待 | `Wait()` | 3.8s |

#### 6.3 片尾 (75-80秒)
| 时间 | 动作 | 代码参考 | run_time |
|------|------|---------|----------|
| 75.0s | 全部淡出 | `FadeOut(VGroup(*all))` | 0.8s |
| 75.8s | 作者信息放大 | `author.animate.scale(2)` | 0.7s |
| 76.5s | 关注提示 | `FadeIn(follow_text)` | 0.6s |
| 77.1s | 塞瓦图标装饰 | `FadeIn(ceva_icons)` | 0.6s |
| 77.7s | 等待 | `Wait()` | 2.3s |

### 坐标布局
```
summary_title: UP * 6
card_1: UP * 2.5
card_2: UP * 1.0
card_3: DOWN * 0.5
card_4: DOWN * 2.0
emphasis: DOWN * 4.5
follow_text: DOWN * 1
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 类型 | 备注 |
|------|---------|---------|------|------|
| author | Scene 1 | Scene 6结尾 | Text | 作者信息，全程显示 |
| triangle | Scene 1 | Scene 6 | Polygon | 主三角形ABC |
| label_A, B, C | Scene 1 | Scene 6 | Text | 顶点标签 |
| dot_P | Scene 2 | Scene 4 | Dot | 塞瓦点P |
| cevian_AD | Scene 2 | Scene 4 | Line | 塞瓦线AD |
| cevian_BE | Scene 2 | Scene 4 | Line | 塞瓦线BE |
| cevian_CF | Scene 2 | Scene 4 | Line | 塞瓦线CF |
| dot_D, E, F | Scene 2 | Scene 4 | Dot | 分点D、E、F |
| ceva_formula | Scene 2 | Scene 3 | MathTex | 塞瓦定理公式 |
| braces | Scene 3 | Scene 3 | Brace | 线段标注，临时 |
| cevian_triangle | Scene 4 | Scene 4 | Polygon | 塞瓦三角形DEF |
| medians | Scene 5 | Scene 5 | Line | 中线，临时 |
| centroid_G | Scene 5 | Scene 5 | Dot | 重心 |
| summary_cards | Scene 6 | Scene 6 | VGroup | 总结卡片 |

---

## 特殊注意事项

### 直线交点计算
```python
# 关键：确保D、E、F在三角形边上而非延长线上
# 使用参数方程求交点时要验证参数t在[0,1]范围内
def line_segment_intersection(P1, D1, P2, D2):
    """计算直线P1+t*D1与线段P2到P2+D2的交点"""
    # 返回交点和参数t
    # 验证：0 <= t <= 1 确保在线段上
```

### 有向线段比
```python
# 注意：塞瓦定理使用有向线段比
# AD/DB中，如果D在AB之间，比值为正
# 如果D在AB延长线上，需要考虑符号
def signed_ratio(A, D, B):
    """计算有向线段比 AD/DB"""
    AD = np.linalg.norm(D - A)
    DB = np.linalg.norm(B - D)
    # 检查D是否在AB之间
    if dot((D-A), (B-A)) < 0 or dot((D-B), (A-B)) < 0:
        return -AD / DB  # D在AB外
    return AD / DB
```

### 边界检查
- 塞瓦点P必须在三角形内部
- 所有元素保持在 x∈[-4,4], y∈[-7,7]
- 标签避免重叠

### 文字渲染
- 所有中文使用 `Text(..., font="Noto Sans CJK SC")`
- 公式使用 `MathTex(r"...")`
- 特殊符号：乘号用 `\times`，分数用 `\frac{}{}`

### 动画节奏
- 塞瓦定理公式出现时放慢速度
- 比例验证环节要清晰
- 重心证明要有足够停留时间

---

## 总时长分配

| 场景 | 时长 | 占比 |
|------|------|------|
| Scene 1: 开场 | 5s | 6.3% |
| Scene 2: 塞瓦定理 | 10s | 12.5% |
| Scene 3: 验证比例 | 15s | 18.8% |
| Scene 4: 塞瓦三角形 | 15s | 18.8% |
| Scene 5: 重心应用 | 15s | 18.8% |
| Scene 6: 总结 | 20s | 25.0% |
| **总计** | **80s** | **100%** |

---

## 渲染命令

```bash
# 快速预览
manim -pql ceva_theorem.py CevaTheorem

# 高质量渲染
manim -qh ceva_theorem.py CevaTheorem

# 4K质量
manim -qk ceva_theorem.py CevaTheorem
```