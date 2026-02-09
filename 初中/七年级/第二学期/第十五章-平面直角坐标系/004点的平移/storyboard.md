# 点的平移 - Point Translation Animation Storyboard

## 元信息 (Metadata)
- **目标时长**: 60-75秒
- **场景数量**: 7个场景
- **难度等级**: 七年级 (初一)
- **主题**: 平面直角坐标系中点的平移规律

## 颜色配置 (Color Scheme)
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要点
COLOR_SECONDARY = "#e74c3c"      # 红色 - 平移后的点
COLOR_ARROW = "#f39c12"          # 橙色 - 平移箭头
COLOR_AXIS = "#95a5a6"           # 灰色 - 坐标轴
COLOR_GRID = "#34495e"           # 深灰 - 网格
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
COLOR_TEXT = WHITE               # 白色 - 文字
COLOR_FORMULA_BG = "#2c3e50"     # 深蓝 - 公式背景
```

## 几何预计算清单 (Geometry Precalculations)

| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 坐标原点 | [0, 0, 0] | `self.ORIGIN_POINT` | NumberPlane中心 |
| 初始点P | [2, 3, 0] * scale | `self.P` | 示例点 |
| 右平移点P1 | P + [3, 0, 0] * scale | `self.P1_right` | 向右平移3个单位 |
| 左平移点P2 | P + [-2, 0, 0] * scale | `self.P2_left` | 向左平移2个单位 |
| 上平移点P3 | P + [0, 2, 0] * scale | `self.P3_up` | 向上平移2个单位 |
| 下平移点P4 | P + [0, -1, 0] * scale | `self.P4_down` | 向下平移1个单位 |
| 综合平移点P5 | P + [2, -3, 0] * scale | `self.P5_combined` | 右2下3 |
| 缩放系数 | 0.4 | `self.SCALE` | 坐标系缩放 |
| 坐标系偏移 | UP * 1.5 | `self.OFFSET` | 垂直居中偏移 |

### 坐标系参数
```python
x_range = [-6, 6, 1]  # x轴: -6到6, 步长1
y_range = [-5, 5, 1]  # y轴: -5到5, 步长1
x_length = 8          # x轴逻辑长度
y_length = 7          # y轴逻辑长度
axis_config = {
    "include_numbers": True,
    "font_size": 16,
    "include_tip": True,
    "tip_width": 0.15,
    "tip_height": 0.15
}
```

---

## Scene 0: 开场钩子 (Opening Hook) - 3秒

**目的**: 吸引注意力，提出问题

### 元素清单
1. 作者标识 (顶部, y=7)
2. 钩子问题 (大字, y=6)
3. 点在坐标系中闪烁

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | 0.8s |
| 1.1s | 简单坐标系淡入 | `FadeIn(plane)` | 0.5s |
| 1.6s | 点P出现并闪烁 | `FadeIn(dot_P), Flash(dot_P)` | 0.5s |
| 2.1s | 等待 | `self.wait(0.9)` | 0.9s |

### 文案内容
```python
hook_text = "点在坐标系里怎么\"移动\"?"
# 或者: "坐标会怎么变化?"
```

### 清理操作
- FadeOut: `hook_text`
- 保留: `author_info`, `plane`, `dot_P`

---

## Scene 1: 建立坐标系 (Setup Coordinate System) - 5秒

**目的**: 清晰展示坐标平面和初始点

### 元素清单
1. NumberPlane (带网格和数字)
2. x轴、y轴标签
3. 初始点P(2, 3)
4. 点P的坐标标注

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 0.5s | 坐标系创建 | `Create(plane)` | 1.2s |
| 1.7s | 轴标签出现 | `FadeIn(x_label, y_label)` | 0.4s |
| 2.1s | 点P出现 | `FadeIn(dot_P, scale=0.5)` | 0.5s |
| 2.6s | 坐标标注 | `Write(coord_label)` | 0.6s |
| 3.2s | 从点到坐标的虚线 | `Create(dashed_lines)` | 0.8s |
| 4.0s | 等待 | `self.wait(1.0)` | 1.0s |

### 文案内容
```python
title = Text("点的平移", font="Noto Sans CJK SC", font_size=36)
coord_label = MathTex("P(2, 3)", font_size=24)
```

### 清理操作
- FadeOut: `title`, `dashed_lines`
- 保留: `plane`, `dot_P`, `coord_label`, `x_label`, `y_label`

---

## Scene 2: 向右平移 (Translate Right) - 8秒

**目的**: 演示向右平移规律 - 横坐标加

### 元素清单
1. 原点P(2, 3)
2. 平移箭头 (向右3个单位)
3. 新点P'(5, 3)
4. 公式: (x, y) → (x+3, y)

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 说明文字淡入 | `FadeIn(explanation)` | 0.5s |
| 0.5s | 公式淡入 | `FadeIn(formula_bg), Write(formula)` | 0.8s |
| 1.3s | 平移箭头生长 | `GrowArrow(arrow_right)` | 1.0s |
| 2.3s | 点沿箭头移动 | `dot_P.animate.move_to(P1_right)` | 1.2s |
| 3.5s | 新坐标标注 | `Write(new_coord)` | 0.6s |
| 4.1s | 高亮横坐标变化 | `Indicate(x_change)` | 0.8s |
| 4.9s | 等待理解 | `self.wait(2.0)` | 2.0s |
| 6.9s | 点恢复原位 | `dot_P.animate.move_to(P)` | 0.8s |
| 7.7s | 清理 | FadeOut箭头和新坐标 | 0.3s |

### 文案内容
```python
explanation = Text("向右平移3个单位", font="Noto Sans CJK SC", font_size=22)
formula = MathTex(r"(x, y) \rightarrow (x+3, y)", font_size=28)
# 分解: MathTex(r"({{2}}, {{3}}) \rightarrow ({{2+3}}, {{3}})")
```

### 几何约束验证
- 箭头起点 = P
- 箭头终点 = P1_right
- 箭头方向 = 纯水平 (y坐标不变)
- 验证: `np.linalg.norm(arrow_end - arrow_start - [3*scale, 0, 0]) < 1e-6`

### 清理操作
- FadeOut: `explanation`, `formula`, `formula_bg`, `arrow_right`, `new_coord`
- 保留: `plane`, `dot_P`, `coord_label`

---

## Scene 3: 向左平移 (Translate Left) - 7秒

**目的**: 演示向左平移规律 - 横坐标减

### 元素清单
1. 原点P(2, 3)
2. 平移箭头 (向左2个单位)
3. 新点P'(0, 3)
4. 公式: (x, y) → (x-2, y)

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 说明文字淡入 | `FadeIn(explanation)` | 0.5s |
| 0.5s | 公式淡入 | `Write(formula)` | 0.8s |
| 1.3s | 平移箭头生长 | `GrowArrow(arrow_left)` | 1.0s |
| 2.3s | 点沿箭头移动 | `dot_P.animate.move_to(P2_left)` | 1.2s |
| 3.5s | 新坐标标注 | `Write(new_coord)` | 0.6s |
| 4.1s | 等待理解 | `self.wait(1.5)` | 1.5s |
| 5.6s | 点恢复原位 | `dot_P.animate.move_to(P)` | 0.8s |
| 6.4s | 清理 | FadeOut | 0.3s |

### 文案内容
```python
explanation = Text("向左平移2个单位", font="Noto Sans CJK SC", font_size=22)
formula = MathTex(r"(x, y) \rightarrow (x-2, y)", font_size=28)
```

### 清理操作
- FadeOut: 所有临时元素
- 保留: `plane`, `dot_P`, `coord_label`

---

## Scene 4: 向上平移 (Translate Up) - 7秒

**目的**: 演示向上平移规律 - 纵坐标加

### 元素清单
1. 原点P(2, 3)
2. 平移箭头 (向上2个单位)
3. 新点P'(2, 5)
4. 公式: (x, y) → (x, y+2)

### 动画序列
(与Scene 2类似结构)

### 文案内容
```python
explanation = Text("向上平移2个单位", font="Noto Sans CJK SC", font_size=22)
formula = MathTex(r"(x, y) \rightarrow (x, y+2)", font_size=28)
```

---

## Scene 5: 向下平移 (Translate Down) - 7秒

**目的**: 演示向下平移规律 - 纵坐标减

### 元素清单
1. 原点P(2, 3)
2. 平移箭头 (向下1个单位)
3. 新点P'(2, 2)
4. 公式: (x, y) → (x, y-1)

### 动画序列
(与Scene 3类似结构)

### 文案内容
```python
explanation = Text("向下平移1个单位", font="Noto Sans CJK SC", font_size=22)
formula = MathTex(r"(x, y) \rightarrow (x, y-1)", font_size=28)
```

---

## Scene 6: 综合平移 (Combined Translation) - 10秒

**目的**: 演示斜向平移 - 横纵坐标同时变化

### 元素清单
1. 原点P(2, 3)
2. 分步箭头:
   - 先右移2个单位 (绿色虚线箭头)
   - 再下移3个单位 (蓝色虚线箭头)
3. 直接箭头 (橙色实线箭头)
4. 新点P'(4, 0)
5. 公式: (x, y) → (x+2, y-3)

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 说明淡入 | `FadeIn(explanation)` | 0.5s |
| 0.5s | 公式淡入 | `Write(formula)` | 0.8s |
| 1.3s | 分步提示 | `FadeIn(step_hint)` | 0.4s |
| 1.7s | 第一步箭头(右) | `GrowArrow(arrow_h)` | 0.8s |
| 2.5s | 点移动到中间 | `dot_P.animate.move_to(mid_point)` | 1.0s |
| 3.5s | 中间点标注 | `Write(mid_coord)` | 0.5s |
| 4.0s | 第二步箭头(下) | `GrowArrow(arrow_v)` | 0.8s |
| 4.8s | 点移动到终点 | `dot_P.animate.move_to(P5)` | 1.0s |
| 5.8s | 终点坐标 | `Write(final_coord)` | 0.5s |
| 6.3s | 等待 | `self.wait(1.0)` | 1.0s |
| 7.3s | 直接路径淡入 | `FadeIn(direct_arrow)` | 0.6s |
| 7.9s | 提示文字 | `FadeIn(direct_hint)` | 0.4s |
| 8.3s | 等待理解 | `self.wait(1.5)` | 1.5s |

### 文案内容
```python
explanation = Text("向右2个单位，再向下3个单位", font="Noto Sans CJK SC", font_size=20)
formula = MathTex(r"(x, y) \rightarrow (x+2, y-3)", font_size=28)
step_hint = Text("分两步:", font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
direct_hint = Text("也可以一步到位!", font="Noto Sans CJK SC", font_size=18, color=YELLOW)
```

### 几何约束验证
```python
# 中间点
mid_point = P + [2*scale, 0, 0]
assert np.allclose(mid_point, [4*scale, 3*scale, 0])

# 终点
P5 = mid_point + [0, -3*scale, 0]
assert np.allclose(P5, [4*scale, 0*scale, 0])

# 直接箭头
direct_vec = P5 - P
assert np.allclose(direct_vec, [2*scale, -3*scale, 0])
```

### 清理操作
- FadeOut: 所有临时元素
- 保留: `plane`

---

## Scene 7: 口诀总结 (Summary & Mnemonic) - 12秒

**目的**: 总结规律，强化记忆

### 元素清单
1. 四个方向的示例 (小坐标系)
2. 口诀卡片
3. 公式总结

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 坐标系缩小移上 | `plane.animate.scale(0.5).move_to(UP*3)` | 0.8s |
| 0.8s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 1.3s | 四个公式卡片依次滑入 | Loop FadeIn | 1.6s |
| 2.9s | 口诀卡片放大进入 | `FadeIn(mnemonic, scale=1.2)` | 0.8s |
| 3.7s | 口诀高亮动画 | `Circumscribe(mnemonic)` | 1.0s |
| 4.7s | 等待记忆 | `self.wait(2.5)` | 2.5s |
| 7.2s | 练习提示 | `FadeIn(practice_hint)` | 0.5s |
| 7.7s | 等待 | `self.wait(1.5)` | 1.5s |

### 文案内容
```python
title = Text("平移规律总结", font="Noto Sans CJK SC", font_size=32, color=GOLD)

# 四个公式卡片
cards = [
    ("向右a", r"(x, y) \to (x+a, y)", COLOR_PRIMARY),
    ("向左a", r"(x, y) \to (x-a, y)", COLOR_SECONDARY),
    ("向上b", r"(x, y) \to (x, y+b)", GREEN),
    ("向下b", r"(x, y) \to (x, y-b)", PURPLE)
]

# 口诀
mnemonic = Text(
    "左减右加，下减上加",
    font="Noto Sans CJK SC",
    font_size=40,
    color=YELLOW,
    weight=BOLD
)

practice_hint = Text(
    "多做练习，熟能生巧!",
    font="Noto Sans CJK SC",
    font_size=24,
    color=GRAY_A
)
```

### 卡片布局
```python
# 2x2网格布局
positions = [
    UP*1.5 + LEFT*2,    # 右
    UP*1.5 + RIGHT*2,   # 左
    DOWN*0.5 + LEFT*2,  # 上
    DOWN*0.5 + RIGHT*2  # 下
]
```

---

## Scene 8: 片尾 (Outro) - 5秒

**目的**: 强化品牌，引导关注

### 元素清单
1. 作者信息放大
2. 关注提示
3. 装饰元素 (坐标点动画)

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 清空所有内容 | `FadeOut(Group(*self.mobjects))` | 0.6s |
| 0.6s | 作者名放大淡入 | `FadeIn(author_name, scale=1.2)` | 0.8s |
| 1.4s | 账号ID淡入 | `FadeIn(author_id, shift=UP*0.3)` | 0.5s |
| 1.9s | 关注提示 | `FadeIn(follow_text, scale=1.1)` | 0.6s |
| 2.5s | 装饰点阵旋转 | `Rotate(decorations, PI)` | 1.5s |
| 4.0s | 等待 | `self.wait(1.0)` | 1.0s |

### 文案内容
```python
author_name = Text(
    "上海初高中数学直通车",
    font="Noto Sans CJK SC",
    font_size=40,
    color=WHITE
)

author_id = Text(
    "@emptyandcalm",
    font="Noto Sans CJK SC",
    font_size=32,
    color=GRAY_B
)

follow_text = Text(
    "关注我，轻松学坐标!",
    font="Noto Sans CJK SC",
    font_size=30,
    color=YELLOW
)
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 持续时间 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 0 | Scene 8 | 全程 | 始终在顶部 |
| plane | Scene 0 | Scene 7 | 大部分时间 | 主要坐标系 |
| dot_P | Scene 0 | Scene 6 | 演示用 | 主角点 |
| coord_label | Scene 1 | Scene 6 | 长期 | 当前坐标 |
| arrow_right | Scene 2 | Scene 2 | 临时 | 右平移箭头 |
| arrow_left | Scene 3 | Scene 3 | 临时 | 左平移箭头 |
| arrow_up | Scene 4 | Scene 4 | 临时 | 上平移箭头 |
| arrow_down | Scene 5 | Scene 5 | 临时 | 下平移箭头 |
| arrow_h, arrow_v | Scene 6 | Scene 6 | 临时 | 综合平移辅助箭头 |
| direct_arrow | Scene 6 | Scene 6 | 临时 | 直接路径箭头 |
| formula_cards | Scene 7 | Scene 7 | 临时 | 总结卡片 |
| mnemonic | Scene 7 | Scene 7 | 临时 | 口诀 |

---

## 总时长分配

| 场景 | 时长 | 累计时长 |
|------|------|---------|
| Scene 0: 开场 | 3s | 3s |
| Scene 1: 建立坐标系 | 5s | 8s |
| Scene 2: 向右平移 | 8s | 16s |
| Scene 3: 向左平移 | 7s | 23s |
| Scene 4: 向上平移 | 7s | 30s |
| Scene 5: 向下平移 | 7s | 37s |
| Scene 6: 综合平移 | 10s | 47s |
| Scene 7: 口诀总结 | 12s | 59s |
| Scene 8: 片尾 | 5s | 64s |
| **总计** | **64秒** | - |

目标: 60-75秒 ✓

---

## 特殊技术要点

### 1. 箭头创建
```python
arrow = Arrow(
    start=point_A,
    end=point_B,
    buff=0.1,
    color=COLOR_ARROW,
    stroke_width=4,
    tip_length=0.2,
    max_tip_length_to_length_ratio=0.25
)
```

### 2. 追踪路径
```python
# 方法1: 使用TracedPath
path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=2)
self.add(path)
self.play(dot.animate.move_to(target))

# 方法2: 手动创建Line
trail = Line(start, end, color=GRAY_A, stroke_width=1)
```

### 3. 坐标标注动态更新
```python
coord_label = always_redraw(
    lambda: MathTex(
        f"({self.current_x:.0f}, {self.current_y:.0f})",
        font_size=20
    ).next_to(dot, UR, buff=0.1)
)
```

### 4. 虚线样式
```python
dashed_line = DashedLine(
    start, end,
    dash_length=0.1,
    dashed_ratio=0.5,
    color=GRAY_B
)
```

---

## 验证检查清单

### 几何验证
- [ ] 所有箭头终点 = 目标点位置
- [ ] 水平箭头 y坐标不变
- [ ] 垂直箭头 x坐标不变
- [ ] 综合平移: 中间点坐标正确
- [ ] 直接箭头向量 = 总平移向量

### 视觉验证
- [ ] 所有元素在边界内 (x∈[-4,4], y∈[-7,7])
- [ ] 文字无重叠
- [ ] 箭头清晰可见
- [ ] 颜色对比度足够

### 动画验证
- [ ] 难点停留时间 ≥ 2秒
- [ ] 过渡流畅
- [ ] 总时长在60-75秒内

---

## 备用方案

### 如果时间紧张
- 合并Scene 3和Scene 5 (左、下平移快速演示)
- 缩短Scene 7的等待时间

### 如果需要延长
- 在Scene 6添加更多中间步骤讲解
- Scene 7增加互动练习题

---

## 渲染参数

```bash
# 预览
manim -pql point_translation.py PointTranslation

# 高质量 (推荐)
manim -qh point_translation.py PointTranslation

# 4K (最终版)
manim -qk point_translation.py PointTranslation
```

---

**分镜脚本完成日期**: 2026-02-09
**预计制作时间**: 2-3小时
**目标平台**: TikTok, 抖音