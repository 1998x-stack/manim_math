# 两直线垂直与夹角 - Storyboard

## Metadata
- **Target Duration:** ~41 seconds
- **Total Scenes:** 5
- **Difficulty Level:** 高二（第二学期·第十一章）
- **Key Concepts:** 两直线垂直条件 k₁k₂=-1, 夹角公式 tan θ=|k₁-k₂|/(1+k₁k₂)
- **Format:** TikTok 竖屏 1080×1920, frame_width=9, frame_height=16

---

## Color Scheme
```python
BG_COLOR      = "#0f0c29"    # 深蓝紫背景
LINE1_COLOR   = "#00d4ff"    # 青色 — 线 l₁ (k₁=2)
LINE2_COLOR   = "#ff6b6b"    # 红色 — 线 l₂ (k₂=-0.5, 垂直场景)
LINE3_COLOR   = "#ffd93d"    # 黄色 — 线 l₃ (k₃=1/3, 夹角场景)
ANGLE_COLOR   = "#a8ff78"    # 绿色 — 角度弧线
FORMULA_BG    = "#16213e"    # 公式框背景
HIGHLIGHT     = YELLOW
```

---

## Layout (Frame logical coordinates, 9 wide × 16 tall)
```
y=+8.0  ┌──────────────────────┐
y=+7.0  │  Author branding     │ ← 全程可见
y=+5.5  ├──────────────────────┤
y=+5.0  │  Scene section label │ ← 每幕标题
y=+4.5  ├──────────────────────┤ ← axes top
        │                      │
y=+1.0  │  [Coordinate Axes]   │ ← axes center (y=1 in frame)
        │   Lines & Angles     │
y=-1.5  ├──────────────────────┤ ← axes bottom
y=-2.5  │  Step explanation    │
y=-3.5  ├──────────────────────┤
y=-5.5  │  Formula boxes       │
y=-8.0  └──────────────────────┘
```

---

## Geometry Pre-calculations

### Axes Configuration
```
Axes(x_range=[-3,3,1], y_range=[-2.5,2.5,1], x_length=6, y_length=5)
axes.move_to(UP * 1.0)
# Frame conversion: frame_x = axes_x, frame_y = axes_y + 1.0
```

### Scene 2 — 垂直线
```
k₁ = 2,    l₁: y = 2x
k₂ = -0.5, l₂: y = -0.5x
k₁ · k₂ = -1  ✓

Intersection P = axes(0,0) → frame(0, 1)
l₁ endpoints: axes(-1.25, -2.5) to axes(1.25, 2.5)
l₂ endpoints: axes(-3,  1.5)   to axes(3,  -1.5)

RightAngle arm vectors (from P):
  arm1 direction: (1, 2)  → arm1 end at axes(0.5, 1.0)
  arm2 direction: (2,-1)  → arm2 end at axes(2.0, -1.0)
  Dot product: 1×2 + 2×(-1) = 0  ✓ perpendicular
```

### Scene 3 — 夹角
```
k₁ = 2,   l₁: y = 2x   (复用)
k₃ = 1/3, l₃: y = x/3
k₁ · k₃ = 2/3 ≠ -1  → 不垂直

tan θ = |2 - 1/3| / (1 + 2×1/3)
      = |5/3| / (5/3) = 1
⟹ θ = 45°   (整数结果，教学友好)

l₃ endpoints: axes(-3, -1) to axes(3, 1)

Angle arc (Angle.from_three_points, CCW from l₃ to l₁):
  P_on_l3 = axes(1.5, 0.5)  [方向角≈18.4°]
  P_on_l1 = axes(0.5, 1.0)  [方向角≈63.4°]
  vertex   = axes(0, 0)
  cross_z = (1.5)(1.0) - (0.5)(0.5) = 1.25 > 0  → CCW ✓
  from_three_points(P_on_l3, vertex, P_on_l1) 得到 45° 弧 ✓
```

### Verification Summary
| Check | Expression | Expected |
|-------|-----------|---------|
| 垂直条件 | k₁·k₂ | -1.0 |
| 直角向量 | arm1·arm2 dot | 0.0 |
| 夹角正切 | tan(θ) | 1.0 |
| 夹角度数 | θ in degrees | 45.0° |
| P_on_l3 in axes range | x∈[-3,3], y∈[-2.5,2.5] | True |
| All frame pts | x∈[-4,4], y∈[-7,7] | True |

---

## Scene 1: Title Hook (3s)

| t | Action | Element |
|---|--------|---------|
| 0.0s | FadeIn | author_text y=7.0 |
| 0.4s | Write | title "两直线的垂直与夹角" y=5.5 |
| 1.2s | FadeIn | subtitle "高中数学 · 坐标几何" y=4.8 |
| 1.8s | FadeIn(shift UP) | axes (坐标系) |
| 2.5s | Wait | |

---

## Scene 2: 垂直条件 (14s, t=3~17s)

| t | Action | Element |
|---|--------|---------|
| 3.0s | Write | section "① 两直线垂直" |
| 3.8s | Create | line_l1 (cyan, k₁=2) |
| 4.8s | Create | line_l2 (red, k₂=-½) |
| 5.5s | FadeIn | slope labels k₁=2, k₂=-½ |
| 6.0s | Create | RightAngle mark at intersection |
| 6.5s | FadeIn | intersection dot (yellow) |
| 7.0s | Write | formula: k₁=2, k₂=-½ at y=-2.5 |
| 8.0s | Write | k₁·k₂ = 2×(-½) = -1 |
| 9.5s | Indicate | the "-1" (yellow flash) |
| 10.0s | Write | "∴ l₁ ⊥ l₂" |
| 10.8s | FadeIn | general form A₁A₂+B₁B₂=0 at y=-4.5 |
| 12.5s | Wait | 理解停顿 |

---

## Scene 3: 夹角公式 (13s, t=17~30s)

| t | Action | Element |
|---|--------|---------|
| 17.0s | FadeOut | scene2 unique elements |
| 17.5s | Write | section "② 两直线夹角" |
| 18.0s | Create | line_l3 (yellow, k₃=1/3) |
| 18.8s | FadeIn | labels k₁=2, k₃=1/3 |
| 19.5s | Create | angle_arc (green, 45°) |
| 20.0s | FadeIn | θ label near arc |
| 20.8s | Write | formula tan θ = |k₁-k₃|/(1+k₁k₃) |
| 22.0s | Write | substitution = |2-1/3|/(1+2/3) |
| 23.2s | Write | = 1  ⟹  θ = 45° |
| 24.0s | Indicate | result (YELLOW flash) |
| 25.0s | FadeIn | note "θ∈[0°, 90°]，夹角取锐角" |
| 27.0s | Wait | |

---

## Scene 4: 公式总结 (8s, t=30~38s)

| t | Action | Element |
|---|--------|---------|
| 30.0s | FadeOut | axes region |
| 30.5s | Write | "公式总结" title |
| 31.0s | FadeIn | box1: k₁k₂=-1 |
| 31.8s | FadeIn | box2: A₁A₂+B₁B₂=0 |
| 32.6s | FadeIn | box3: tan θ 公式 |
| 33.4s | FadeIn | box4: θ∈[0,π/2] |
| 34.5s | Flash | all boxes |
| 36.0s | Wait | |

---

## Scene 5: Outro (3s, t=38~41s)

| t | Action | Element |
|---|--------|---------|
| 38s | Transform | author → larger centered |
| 39s | FadeIn | CTA "关注我，学更多数学！" |
| 41s | End | |

---

## Element Lifecycle

| Element | Created | Removed | Notes |
|---------|---------|---------|-------|
| author_text | S1 | end | 全程显示 |
| axes | S1 | S4 | 主图形 |
| line_l1 (cyan) | S2 | S4 | k₁=2 |
| line_l2 (red) | S2 | S3 | k₂=-½ |
| right_angle_mark | S2 | S3 | 白色直角 |
| perp_formula | S2 | S3 | |
| line_l3 (yellow) | S3 | S4 | k₃=1/3 |
| angle_arc (green) | S3 | S4 | 45°弧 |
| angle_formula | S3 | S4 | |
| summary_boxes | S4 | end | |