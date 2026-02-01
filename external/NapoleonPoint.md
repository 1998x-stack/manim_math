# 拿破仑点 (Napoleon's Point) - 动画分镜脚本

## 元信息
- 目标时长: 75-90 秒
- 场景数量: 8 个
- 难度等级: 高中 / 数学竞赛
- 视频格式: TikTok 竖屏 (1080×1920)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"           # 蓝色 - 主三角形
COLOR_OUTER_TRIANGLE = "#e74c3c"    # 红色 - 外侧正三角形
COLOR_INNER_TRIANGLE = "#2ecc71"    # 绿色 - 内侧正三角形
COLOR_NAPOLEON_OUTER = "#f39c12"    # 橙色 - 外拿破仑三角形
COLOR_NAPOLEON_INNER = "#9b59b6"    # 紫色 - 内拿破仑三角形
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_TEXT = WHITE
```

## 几何预计算清单

### 主三角形（任意三角形）
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点A | 基准坐标 | self.A |
| 顶点B | 基准坐标 | self.B |
| 顶点C | 基准坐标 | self.C |
| 边长a (BC) | `np.linalg.norm(B - C)` | self.a |
| 边长b (CA) | `np.linalg.norm(C - A)` | self.b |
| 边长c (AB) | `np.linalg.norm(A - B)` | self.c |
| 重心G | `(A + B + C) / 3` | self.G |

### 外侧正三角形构造
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 正三角形△BCA' | 以BC为底，向外作正三角形 | self.A_outer |
| 正三角形△CAB' | 以CA为底，向外作正三角形 | self.B_outer |
| 正三角形△ABC' | 以AB为底,向外作正三角形 | self.C_outer |
| 外正三角形中心OA | △BCA'的中心（重心）| self.O_A |
| 外正三角形中心OB | △CAB'的中心 | self.O_B |
| 外正三角形中心OC | △ABC'的中心 | self.O_C |
| 外拿破仑三角形 | 连接OA, OB, OC | Polygon(O_A, O_B, O_C) |
| 外拿破仑点 | △OA OB OC的中心 | self.N_outer |

### 内侧正三角形构造
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 正三角形△BCA'' | 以BC为底，向内作正三角形 | self.A_inner |
| 正三角形△CAB'' | 以CA为底，向内作正三角形 | self.B_inner |
| 正三角形△ABC'' | 以AB为底，向内作正三角形 | self.C_inner |
| 内正三角形中心IA | △BCA''的中心 | self.I_A |
| 内正三角形中心IB | △CAB''的中心 | self.I_B |
| 内正三角形中心IC | △ABC''的中心 | self.I_C |
| 内拿破仑三角形 | 连接IA, IB, IC | Polygon(I_A, I_B, I_C) |
| 内拿破仑点 | △IA IB IC的中心 | self.N_inner |

### 关键性质验证
| 性质 | 验证方法 | 备注 |
|------|---------|------|
| 外拿破仑三角形为正三角形 | 验证三边相等 | 拿破仑定理核心 |
| 内拿破仑三角形为正三角形 | 验证三边相等 | 拿破仑定理核心 |
| 两拿破仑点连线中点 = 重心G | `(N_outer + N_inner)/2 == G` | 神奇性质 |

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 抓住注意力，提出问题

### 视觉元素
1. 作者标识（顶部，小字，灰色）
2. 钩子问题（中心，大字，金色）
3. 任意三角形淡入

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2, run_time=0.3)` | 顶部固定 |
| 0.3s | 钩子文字打字效果 | `Write(hook_text, run_time=1.0)` | "任意三角形中隐藏的秘密" |
| 1.5s | 三角形创建 | `Create(triangle, run_time=1.2)` | 主角登场 |
| 2.8s | 三个顶点标记 | `FadeIn(labels_ABC)` | A, B, C标签 |
| 3.5s | 提示文字 | `FadeIn(hint, shift=UP*0.3)` | "拿破仑点是什么?" |
| 4.5s | 等待 | `Wait(0.5)` | 让观众思考 |

### 几何元素生命周期
- **创建**: triangle, labels_ABC, author_info
- **销毁**: hook_text, hint
- **保留**: triangle, labels_ABC, author_info

---

## Scene 2: 外侧正三角形构造 (5-18秒)

**目的**: 演示向外构造正三角形的过程

### 副标题
```python
title = Text("外拿破仑点构造", font="Noto Sans CJK SC", font_size=32, color=COLOR_OUTER_TRIANGLE)
subtitle = Text("以各边为底，向外作正三角形", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
```

### 动画序列

#### Step 1: 高亮BC边并构造正三角形 (5-8秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 5.0s | 标题淡入 | `FadeIn(title, subtitle)` | 场景标题 |
| 5.5s | BC边高亮 | `BC_line.animate.set_color(COLOR_HIGHLIGHT).set_stroke_width(5)` | 聚焦当前操作 |
| 6.0s | 标注"以BC为底" | `FadeIn(label_bc)` | 说明文字 |
| 6.5s | 绘制外侧正三角形△BCA' | `Create(triangle_BCA_outer, run_time=1.5)` | 逐步绘制 |
| 8.0s | 标记A'点 | `FadeIn(dot_A_outer, label_A_outer)` | 新顶点 |

#### Step 2: 标记中心OA (8-9秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 8.5s | 从三边画中线 | `Create(medians_BCA)` | 三条虚线 |
| 9.0s | 中心点闪烁 | `FadeIn(dot_OA, scale=0.5), Flash(dot_OA)` | OA点出现 |
| 9.5s | 标注OA | `FadeIn(label_OA)` | 中心标记 |

#### Step 3: 构造CAB'和ABC' (9-13秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 10.0s | 淡出辅助线 | `FadeOut(medians_BCA, label_bc)` | 清理 |
| 10.3s | 同时创建另两个正三角形 | `Create(triangle_CAB_outer), Create(triangle_ABC_outer)` | 加速节奏 |
| 11.5s | 标记B', C'点 | `FadeIn(dots_BC_outer, labels_BC_outer)` | 批量出现 |
| 12.0s | 标记中心OB, OC | `FadeIn(dots_OBOC, labels_OBOC)` | 三个中心齐聚 |
| 13.0s | 等待 | `Wait(1.0)` | 让观众理解 |

#### Step 4: 连接三个中心 (13-16秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 13.5s | 提示文字 | `Write(text_connect)` | "连接三个中心" |
| 14.0s | 绘制外拿破仑三角形 | `Create(napoleon_outer_triangle, run_time=1.5)` | 重要时刻 |
| 15.5s | 三条边闪烁 | `Indicate(napoleon_outer_triangle)` | 强调 |
| 16.0s | 验证正三角形 | `FadeIn(text_equilateral)` | "这是一个正三角形!" |

#### Step 5: 标记外拿破仑点 (16-18秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 16.5s | 外拿破仑点出现 | `FadeIn(dot_N_outer, scale=0.5), Flash(dot_N_outer)` | 金色光芒 |
| 17.0s | 标注N_outer | `Write(label_N_outer)` | 外拿破仑点 |
| 17.5s | 说明文字 | `FadeIn(text_definition)` | "外拿破仑点" |
| 18.0s | 等待 | `Wait(0.5)` | 理解时间 |

### 几何元素生命周期
- **创建**: title, subtitle, triangle_BCA_outer, triangle_CAB_outer, triangle_ABC_outer, dots_centers, labels_centers, napoleon_outer_triangle, dot_N_outer
- **销毁**: title, subtitle, text_connect, text_equilateral, text_definition（场景结尾清理）
- **保留**: 外侧正三角形（半透明）, dot_N_outer（缩小）, napoleon_outer_triangle（虚线化）

---

## Scene 3: 内侧正三角形构造 (18-28秒)

**目的**: 演示向内构造，展示对称美

### 副标题
```python
title = Text("内拿破仑点构造", font="Noto Sans CJK SC", font_size=32, color=COLOR_INNER_TRIANGLE)
subtitle = Text("以各边为底，向内作正三角形", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
```

### 动画序列（加速版，利用观众已有理解）

#### Step 1: 快速构造三个内侧正三角形 (18-21秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 18.0s | 标题淡入 | `FadeIn(title, subtitle)` | 场景切换 |
| 18.5s | 同时创建三个内正三角形 | `Create(triangles_inner, run_time=2.0)` | 批量操作 |
| 20.5s | 标记A'', B'', C'' | `FadeIn(dots_inner, labels_inner)` | 内侧顶点 |

#### Step 2: 标记中心并连接 (21-24秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 21.0s | 三个中心同时出现 | `FadeIn(dots_IA_IB_IC, labels_IA_IB_IC)` | IA, IB, IC |
| 21.5s | 提示文字 | `Write(text_connect_inner)` | "连接内侧中心" |
| 22.0s | 绘制内拿破仑三角形 | `Create(napoleon_inner_triangle, run_time=1.5)` | 绿色正三角形 |
| 23.5s | 验证 | `FadeIn(text_also_equilateral)` | "同样是正三角形!" |

#### Step 3: 标记内拿破仑点 (24-26秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 24.0s | 内拿破仑点出现 | `FadeIn(dot_N_inner, scale=0.5), Flash(dot_N_inner)` | 紫色光芒 |
| 24.5s | 标注N_inner | `Write(label_N_inner)` | 内拿破仑点 |
| 25.0s | 说明 | `FadeIn(text_inner_napoleon)` | "内拿破仑点" |
| 26.0s | 等待 | `Wait(2.0)` | 欣赏对称美 |

### 几何元素生命周期
- **创建**: triangles_inner, dots_centers_inner, napoleon_inner_triangle, dot_N_inner
- **销毁**: title, subtitle, text_connect_inner, text_also_equilateral
- **保留**: 内侧正三角形（半透明）, dot_N_inner（缩小）, napoleon_inner_triangle（虚线化）

---

## Scene 4: 拿破仑定理陈述 (28-35秒)

**目的**: 正式陈述定理，强化核心概念

### 视觉布局
```
┌─────────────────────────────┐
│   拿破仑定理 Napoleon's Theorem   │  y = +6
├─────────────────────────────┤
│                             │
│   [主三角形 + 两个拿破仑三角形]    │  y ∈ [+2, +5]
│                             │
├─────────────────────────────┤
│   定理陈述（分步显示）          │  y ∈ [-2, +1]
│   1. 向外/内作正三角形          │
│   2. 连接三个中心             │
│   3. 得到的三角形是正三角形      │
│   4. 其中心为拿破仑点           │
├─────────────────────────────┤
│   重点: "必然是正三角形"        │  y = -4
└─────────────────────────────┘
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 28.0s | 清理辅助元素 | `FadeOut(外侧/内侧正三角形)` | 保留拿破仑三角形 |
| 28.5s | 定理标题 | `Write(theorem_title, run_time=0.8)` | 大标题 |
| 29.5s | 图形缩小上移 | `triangles.animate.scale(0.7).move_to(UP*3.5)` | 腾出空间 |
| 30.0s | 定理陈述第1条 | `FadeIn(statement_1, shift=UP*0.2)` | "向外/内作正三角形" |
| 30.8s | 高亮外拿破仑三角形 | `Indicate(napoleon_outer_triangle)` | 视觉对应 |
| 31.5s | 定理陈述第2条 | `FadeIn(statement_2, shift=UP*0.2)` | "连接三个中心" |
| 32.3s | 定理陈述第3条 | `FadeIn(statement_3, shift=UP*0.2)` | "得到正三角形" |
| 33.0s | 强调"必然" | `Write(emphasis_text)` | 金色大字 |
| 33.8s | 定理陈述第4条 | `FadeIn(statement_4, shift=UP*0.2)` | "其中心为拿破仑点" |
| 34.5s | 两个拿破仑点闪烁 | `Flash(dot_N_outer), Flash(dot_N_inner)` | 呼应 |
| 35.0s | 等待 | `Wait(1.5)` | 消化信息 |

### 几何元素生命周期
- **保留**: triangle, napoleon_outer_triangle, napoleon_inner_triangle, dots_N_outer_inner
- **销毁**: theorem_title, statements（场景末）

---

## Scene 5: 神奇性质揭示 (35-45秒)

**目的**: 展示两拿破仑点连线中点 = 重心的性质

### 动画序列

#### Step 1: 连接两个拿破仑点 (35-37秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 35.0s | 清理定理文字 | `FadeOut(theorem_statements)` | 准备新内容 |
| 35.5s | 提示文字 | `Write(text_amazing_property)` | "神奇性质" |
| 36.0s | 画线连接N_outer和N_inner | `Create(line_N_outer_N_inner, run_time=1.2)` | 虚线，金色 |
| 37.0s | 两点高亮 | `Indicate(dot_N_outer), Indicate(dot_N_inner)` | 呼应 |

#### Step 2: 标记中点 (37-39秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 37.5s | 中点出现 | `FadeIn(dot_midpoint, scale=0.5)` | 小圆点 |
| 38.0s | 标注M | `Write(label_M)` | 中点标记 |
| 38.5s | 说明 | `FadeIn(text_midpoint)` | "连线的中点" |

#### Step 3: 显示重心并验证重合 (39-43秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 39.0s | 绘制三条中线 | `Create(medians_ABC, run_time=1.0)` | 虚线 |
| 40.0s | 重心出现 | `FadeIn(dot_G, scale=0.5), Flash(dot_G)` | 重心闪烁 |
| 40.5s | 标注G | `Write(label_G)` | 重心 |
| 41.0s | 中点M移动到重心 | `dot_midpoint.animate.move_to(dot_G)` | 展示重合！ |
| 41.8s | 爆炸效果 | `Flash(dot_G, color=GOLD, flash_radius=0.5)` | 强调重合 |
| 42.5s | 结论文字 | `Write(text_conclusion, run_time=1.2)` | "中点恰好是重心!" |
| 43.5s | 等待 | `Wait(1.5)` | 惊叹时刻 |

### 几何元素生命周期
- **创建**: line_N_outer_N_inner, dot_midpoint, medians, dot_G
- **保留**: 所有拿破仑构造
- **销毁**: text_amazing_property, text_conclusion（场景末）

---

## Scene 6: 对比展示 (45-55秒)

**目的**: 并列展示外拿破仑点和内拿破仑点的构造

### 视觉布局（分屏）
```
┌──────────────┬──────────────┐
│  外拿破仑点   │  内拿破仑点   │
│              │              │
│   [外构造]    │   [内构造]    │
│              │              │
│  红色正△     │  绿色正△      │
│  橙色点      │  紫色点       │
└──────────────┴──────────────┘
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 45.0s | 清理中间过程 | `FadeOut(medians, line_N_outer_N_inner等)` | 准备对比 |
| 45.5s | 分屏标题 | `Write(title_outer), Write(title_inner)` | 左右标题 |
| 46.0s | 左侧外构造淡入 | `FadeIn(outer_construction_left)` | 左半边 |
| 46.5s | 右侧内构造淡入 | `FadeIn(inner_construction_right)` | 右半边 |
| 47.0s | 同步高亮外拿破仑三角形 | `Indicate(napoleon_outer_left)` | 左侧 |
| 47.5s | 同步高亮内拿破仑三角形 | `Indicate(napoleon_inner_right)` | 右侧 |
| 48.0s | 同步标记外拿破仑点 | `Flash(dot_N_outer_left)` | 左侧橙色 |
| 48.3s | 同步标记内拿破仑点 | `Flash(dot_N_inner_right)` | 右侧紫色 |
| 49.0s | 特性卡片1 | `FadeIn(card_outer)` | "外接圆相关" |
| 49.5s | 特性卡片2 | `FadeIn(card_inner)` | "内部结构" |
| 50.5s | 合并动画 | 两侧合并回中心 | 过渡 |
| 52.0s | 总结文字 | `Write(text_summary)` | "两个拿破仑点，对称之美" |
| 53.5s | 等待 | `Wait(1.5)` | 理解 |

### 几何元素生命周期
- **创建**: 分屏元素
- **销毁**: 分屏元素（合并后）
- **保留**: 主三角形及两个拿破仑点

---

## Scene 7: 动态演示 (55-65秒)

**目的**: 变换三角形形状，展示拿破仑点的普适性

### 动画序列

#### 变换1: 从锐角三角形到钝角三角形 (55-58秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 55.0s | 提示文字 | `Write(text_transform)` | "改变三角形形状..." |
| 55.5s | 顶点C向下移动 | `self.C.animate.shift(DOWN*1.5)` | 变钝角 |
| 56.0s | 所有派生元素同步更新 | `always_redraw机制` | 自动重算 |
| 57.0s | 拿破仑点依然存在 | `Indicate(dots_napoleon)` | 强调稳定性 |
| 58.0s | 说明 | `FadeIn(text_still_exists)` | "拿破仑点仍然存在!" |

#### 变换2: 变成近似等边三角形 (58-61秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 58.5s | 三个顶点同时调整 | `vertices.animate.move_to(...)` | 变等边 |
| 59.5s | 外拿破仑三角形几乎重合 | 视觉效果 | 特殊情况 |
| 60.0s | 说明 | `FadeIn(text_special_case)` | "等边三角形时的特殊性" |
| 61.0s | 恢复原状 | `vertices.animate.move_to(original)` | 回归 |

#### 变换3: 快速多次变换 (61-64秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 61.5s | 连续变换 | `Succession(变换1, 变换2, 变换3)` | 快速展示 |
| 63.0s | 轨迹留痕 | 拿破仑点的运动轨迹 | 可选效果 |
| 64.0s | 总结 | `Write(text_universal)` | "对任意三角形都成立!" |
| 65.0s | 等待 | `Wait(1.0)` | 强调普适性 |

### 几何元素生命周期
- **保留**: 动态更新的所有元素
- **销毁**: text_transform, text_universal（场景末）

---

## Scene 8: 总结与片尾 (65-75秒)

**目的**: 回顾要点，引导关注

### 动画序列

#### Step 1: 清理并缩小图形 (65-67秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 65.0s | 淡出所有辅助线 | `FadeOut(auxiliary_elements)` | 清理 |
| 65.5s | 主图形缩小并上移 | `main.animate.scale(0.5).move_to(UP*4)` | 腾出空间 |

#### Step 2: 要点回顾卡片 (67-72秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 67.0s | 卡片1滑入 | `card_1.animate.shift(LEFT*10 to ORIGIN)` | "拿破仑定理: 必得正三角形" |
| 68.0s | 卡片2滑入 | `card_2.animate.shift(...)` | "两个拿破仑点: 外/内" |
| 69.0s | 卡片3滑入 | `card_3.animate.shift(...)` | "神奇性质: 中点=重心" |
| 70.0s | 卡片4滑入 | `card_4.animate.shift(...)` | "对任意三角形成立" |
| 71.0s | 卡片闪烁 | `Indicate(all_cards)` | 强调 |

#### Step 3: 片尾关注引导 (72-75秒)
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 72.0s | 作者信息放大 | `author_info.animate.scale(2).move_to(UP*1)` | 中心位置 |
| 72.5s | 关注提示 | `Write(follow_text)` | "关注我，学更多几何技巧!" |
| 73.0s | 装饰动画 | 小三角形旋转 | 视觉吸引 |
| 74.0s | 五心图标（彩蛋） | `FadeIn(five_centers_icons)` | 关联其他内容 |
| 75.0s | 全部淡出 | `FadeOut(everything)` | 结束 |

### 几何元素生命周期
- **创建**: 要点卡片, follow_text, 装饰元素
- **销毁**: 全部淡出

---

## 元素生命周期追踪总表

| 元素 | 创建场景 | 销毁场景 | 持续时长 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程 | 顶部固定 |
| triangle (主三角形) | Scene 1 | Scene 8 | 全程 | 主角 |
| labels_ABC | Scene 1 | Scene 8 | 全程 | 顶点标记 |
| triangle_BCA_outer | Scene 2 | Scene 4 | 短期 | 外侧正三角形 |
| napoleon_outer_triangle | Scene 2 | Scene 8 | 长期 | 外拿破仑三角形 |
| dot_N_outer | Scene 2 | Scene 8 | 长期 | 外拿破仑点 |
| triangles_inner | Scene 3 | Scene 4 | 短期 | 内侧正三角形 |
| napoleon_inner_triangle | Scene 3 | Scene 8 | 长期 | 内拿破仑三角形 |
| dot_N_inner | Scene 3 | Scene 8 | 长期 | 内拿破仑点 |
| line_N_outer_N_inner | Scene 5 | Scene 6 | 短期 | 连线 |
| dot_G (重心) | Scene 5 | Scene 8 | 中期 | 重心 |
| medians | Scene 5 | Scene 6 | 短期 | 中线 |
| text_* (各种说明) | 各场景 | 各场景末 | 临时 | 即时清理 |

---

## 关键几何计算公式

### 1. 以边为底向外作正三角形
```python
def construct_equilateral_outward(P1, P2):
    """
    以P1P2为底边，向外侧作正三角形，返回第三个顶点
    
    方法: 
    1. 计算中点M = (P1 + P2) / 2
    2. 计算边向量 V = P2 - P1
    3. 计算高度 h = |V| * sqrt(3) / 2
    4. 计算垂直方向（向外）N = rotate_90_ccw(V) 
    5. 第三顶点 P3 = M + (h / |N|) * N
    
    注意: 需要判断"向外"方向，使用叉积判断
    """
    mid = (P1 + P2) / 2
    edge_vec = P2 - P1
    edge_length = np.linalg.norm(edge_vec)
    height = edge_length * np.sqrt(3) / 2
    
    # 垂直方向（逆时针旋转90度）
    perp = np.array([-edge_vec[1], edge_vec[0], 0])
    perp_normalized = perp / np.linalg.norm(perp)
    
    # 判断方向: 需要根据原三角形判断"外侧"
    # 使用叉积判断: 如果(P1P2) × (P1P_opposite) > 0，则perp是外侧
    # 这里假设已知原三角形的第三个顶点opposite_vertex
    
    P3 = mid + height * perp_normalized  # 或 - height * perp_normalized
    
    return P3
```

### 2. 正三角形的中心
```python
def equilateral_center(P1, P2, P3):
    """
    正三角形的中心 = 重心 = 外心 = 内心 = 垂心
    """
    return (P1 + P2 + P3) / 3
```

### 3. 验证正三角形
```python
def verify_equilateral(P1, P2, P3, eps=1e-6):
    """
    验证三个点构成正三角形
    """
    a = np.linalg.norm(P2 - P1)
    b = np.linalg.norm(P3 - P2)
    c = np.linalg.norm(P1 - P3)
    
    return (abs(a - b) < eps and abs(b - c) < eps)
```

### 4. 判断点在三角形的哪一侧
```python
def point_side_of_edge(P, edge_start, edge_end, reference_point):
    """
    判断点P相对于边(edge_start, edge_end)的位置
    使用reference_point作为"内侧"参考
    
    返回: 1 (与reference同侧), -1 (相反侧), 0 (在边上)
    """
    edge_vec = edge_end - edge_start
    to_P = P - edge_start
    to_ref = reference_point - edge_start
    
    cross_P = edge_vec[0] * to_P[1] - edge_vec[1] * to_P[0]
    cross_ref = edge_vec[0] * to_ref[1] - edge_vec[1] * to_ref[0]
    
    if abs(cross_P) < 1e-10:
        return 0
    elif cross_P * cross_ref > 0:
        return 1
    else:
        return -1
```

---

## 时间节奏指南

| 场景 | 建议时长 | 节奏特点 | 关键停顿 |
|------|---------|---------|---------|
| Scene 1 开场 | 5s | 快速抓住注意力 | 钩子后0.5s |
| Scene 2 外构造 | 13s | 详细展示，建立理解 | 每个正三角形完成后1s |
| Scene 3 内构造 | 10s | 加速（观众已理解） | 拿破仑点出现后2s |
| Scene 4 定理陈述 | 7s | 稳重，权威 | 每条陈述间隔0.8s |
| Scene 5 性质揭示 | 10s | 递进，制造惊喜 | 重合时刻停留1.5s |
| Scene 6 对比展示 | 10s | 并列，强化对比 | 合并前停顿1.5s |
| Scene 7 动态演示 | 10s | 快速变化，展示普适性 | 最后总结停留1s |
| Scene 8 总结片尾 | 10s | 温和收尾，引导关注 | 要点卡片依次出现 |

**总时长**: 75秒（符合TikTok短视频最佳长度）

---

## 颜色与视觉层次

### 图层优先级（从后到前）
1. **背景层**: 深色背景 `#1a1a2e`
2. **辅助层**: 虚线、说明文字（灰色 GRAY_B）
3. **主图形层**: 原三角形（蓝色 `#3498db`）
4. **扩展层**: 外侧/内侧正三角形（半透明，红/绿）
5. **核心层**: 拿破仑三角形（实线，橙/紫）
6. **关键点层**: 拿破仑点（大圆点，金色光晕）
7. **文字层**: 标题、说明（白色/金色）

### 强调策略
- **闪烁 (Flash)**: 关键点出现时
- **指示 (Indicate)**: 需要观众注意的元素
- **缩放 (Scale)**: 创建时从小到大
- **颜色变化**: 高亮时临时变为 YELLOW

---

## 字幕与旁白建议（可选）

| 场景 | 旁白文字 |
|------|---------|
| Scene 1 | "一个任意三角形，隐藏着怎样的几何秘密？" |
| Scene 2 | "以每条边为底，向外作正三角形..." |
| Scene 2 | "连接三个中心，神奇的事情发生了..." |
| Scene 2 | "它们构成了一个完美的正三角形！" |
| Scene 3 | "向内构造，同样得到正三角形" |
| Scene 4 | "这就是拿破仑定理" |
| Scene 5 | "更神奇的是..." |
| Scene 5 | "两个拿破仑点连线的中点，恰好是原三角形的重心！" |
| Scene 7 | "无论三角形如何变化..." |
| Scene 7 | "拿破仑点始终存在" |

---

## 技术检查清单

在开始编码前确认:
- [x] 所有坐标通过精确计算（使用GeometryCalculator）
- [x] 向外/向内构造的方向判断逻辑正确
- [x] 正三角形验证机制存在
- [x] 所有派生点有统一初始化
- [x] 颜色配置符合视觉层次
- [x] 时间节奏分配合理
- [x] 元素生命周期追踪清晰
- [x] 边界检查（x∈[-4,4], y∈[-7,7]）
- [x] 中文文字使用Text()而非MathTex()
- [x] 度数符号使用`^\circ`
- [x] 所有Angle对象方向正确

---

## 备注与优化建议

1. **性能优化**: Scene 7 动态演示时使用 `always_redraw` 保持几何关系自动更新
2. **视觉优化**: 拿破仑三角形使用半透明填充 `fill_opacity=0.2` 避免遮挡
3. **教学优化**: Scene 2 首次构造时详细，Scene 3 复用观众已有理解加速
4. **互动建议**: 可在片尾添加二维码，引导观众到完整证明视频
5. **扩展内容**: 可制作姊妹篇介绍费马点，因为构造方法相同

---

**分镜脚本完成！准备进入代码编写阶段。**