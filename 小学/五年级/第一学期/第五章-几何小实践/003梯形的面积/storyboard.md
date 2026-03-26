# 梯形的面积 — 动画分镜脚本

## 元信息
- 目标时长: ~42秒
- 场景数量: 6个
- 年级: 五年级

## 几何预计算

```
T1 顶点 (逆时针, 从左下):
  A(-2.0, 0.5)   下底左端
  B( 1.0, 0.5)   下底右端
  C( 0.2, 2.5)   上底右端
  D(-1.2, 2.5)   上底左端

下底 b = |AB| = 3.0
上底 a = |DC| = 1.4
高   h = 2.5 - 0.5 = 2.0

M_BC = midpoint(B, C) = (0.6, 1.5)   ← T2 旋转轴

旋转验证 (T2 绕 M_BC 旋转 180°):
  A(-2.0, 0.5) → A' = 2*(0.6,1.5) - (-2.0,0.5) = (3.2, 2.5)
  B( 1.0, 0.5) → B' = 2*(0.6,1.5) - (1.0,0.5) = (0.2,2.5) = C ✓
  C( 0.2, 2.5) → C' = 2*(0.6,1.5) - (0.2,2.5) = (1.0,0.5) = B ✓
  D(-1.2, 2.5) → D' = 2*(0.6,1.5) - (-1.2,2.5) = (2.4, 0.5)

平行四边形顶点 (逆时针):
  A(-2.0,0.5) → D'(2.4,0.5) → A'(3.2,2.5) → D(-1.2,2.5)
  底边 = 2.4-(-2.0) = 4.4 = a+b = 1.4+3.0 ✓
  x 范围: [-2.0, 3.2] ⊂ [-4.5,4.5] ✓

垂足 H_foot = (D.x, A.y) = (-1.2, 0.5)
面积(平行四边形) = (a+b)*h = 4.4*2.0 = 8.8
面积(梯形)       = 8.8/2 = 4.4
```

## 颜色配置

```python
BG_COLOR    = "#1a1a2e"
COLOR_TRAP1 = "#3b82f6"   # 蓝色 T1
COLOR_TRAP2 = "#ef4444"   # 红色 T2
COLOR_PARA  = "#22c55e"   # 绿色平行四边形
COLOR_LOWER = "#f59e0b"   # 橙色下底
COLOR_UPPER = "#fb923c"   # 浅橙上底
COLOR_HEIGHT= "#a78bfa"   # 紫色高
COLOR_HL    = "#fbbf24"   # 黄色高亮
```

## 元素生命周期

| 元素 | 创建 | 销毁 | 备注 |
|------|------|------|------|
| author_mob | Scene 1 | Scene 6 | 片尾放大 |
| main_trap | Scene 1 | Scene 6 | 贯穿始终 |
| t2 | Scene 2 | Scene 4 end | 旋转后保留 |
| para_outline | Scene 2 | Scene 4 end | |
| brace (a+b) | Scene 3 | Scene 4 end | 保留供推导参考 |
| brace_lbl | Scene 3 | Scene 4 end | |

---

## Scene 1: 开场 (4s)

| 时间 | 动作 |
|------|------|
| 0.0s | FadeIn author |
| 0.4s | Write "为什么梯形面积" |
| 1.0s | Write "要 ÷ 2 ？" |
| 1.7s | Create main_trap |
| 2.9s | FadeIn "?" |
| 3.7s | FadeOut hook texts + "?" |

---

## Scene 2: 拼合法 (13s)

| 时间 | 动作 |
|------|------|
| 0.0s | FadeIn "拼合法" 标题 |
| 0.5s | Write "复制一个完全相同的梯形" |
| 1.1s | GrowFromCenter t2 (红色梯形) |
| 1.8s | 切换说明文字 |
| 2.2s | Rotate t2, PI, about_point=M_BC (2.2s) |
| 4.4s | FadeIn "拼成了一个平行四边形！" |
| 5.2s | Create para_outline |
| 6.2s | Indicate para_outline |
| 6.7s | FadeIn "2个梯形 = 1个平行四边形" |
| 8.2s | FadeOut title/texts (保留 t2, para_outline) |

---

## Scene 3: 标注底和高 (8s)

| 时间 | 动作 |
|------|------|
| 0.0s | Write "标注底和高" 标题 |
| 0.5s | Create Brace (a+b) + 标签 |
| 1.2s | Create 高虚线 + 直角符号 + "高h" |
| 2.0s | FadeIn "平行四边形面积 = (上底+下底)×h" |
| 3.5s | wait 1.5s |
| 5.0s | FadeOut 标题/高线/公式 (保留 brace + brace_lbl) |

---

## Scene 4: 推导公式 (9s)

| 时间 | 动作 |
|------|------|
| 0.0s | Write "推导梯形面积" 标题 |
| 0.5s | FadeIn "2×梯形面积 = 平行四边形面积" |
| 1.1s | arrow + FadeIn "梯形面积 = 平行四边形面积÷2" |
| 1.8s | ReplacementTransform → "梯形面积 = (a+b)×h÷2" |
| 2.6s | wait 2s (★ 关键理解点) |
| 4.6s | FadeOut all (t2, para_outline, brace, brace_lbl) |

---

## Scene 5: 公式总结 (7s)

| 时间 | 动作 |
|------|------|
| 0.0s | Create 上底线 + 下底线 |
| 0.4s | FadeIn 上底brace+a, 下底brace+b |
| 1.0s | Create 高虚线 + 直角 + "高h" |
| 1.6s | FadeIn 公式框 |
| 1.9s | Write "梯形面积公式" |
| 2.3s | Write "S = (a+b)×h÷2" |
| 3.3s | Create 红色矩形框 (highlight ÷2) |
| 3.7s | FadeIn "÷2 = 梯形是平行四边形面积的一半" |
| 5.7s | wait 2s |
| 6.2s | FadeOut all |

---

## Scene 6: 片尾 (3.5s)

| 时间 | 动作 |
|------|------|
| 0.0s | FadeOut main_trap |
| 0.4s | Transform author→放大 |
| 1.0s | FadeIn "@emptyandcalm" |
| 1.5s | FadeIn "关注我，获得更多数学技巧！" |
| 2.1s | FadeIn + Rotate 小梯形装饰 |
| 3.3s | FadeOut all |