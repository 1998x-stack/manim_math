# 实系数一元二次方程 - 动画分镜脚本

## 元信息
- 目标时长: ~75 秒
- 场景数量: 7 个
- 难度等级: 高二 / 中等偏上

## 颜色配置
```python
BG_COLOR      = "#1a1a2e"
GOLD          = "#f39c12"
BLUE_BRIGHT   = "#3498db"
GREEN_BRIGHT  = "#2ecc71"
RED_BRIGHT    = "#e74c3c"
PURPLE_BRIGHT = "#9b59b6"
GRAY_LABEL    = "#95a5a6"
WHITE         = WHITE
YELLOW_HL     = YELLOW
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 抛物线轴位置 | Axes 内部 | axes |
| Δ>0 两实根 | x=(-b±√Δ)/2a | root1, root2 |
| Δ=0 重根 | x=-b/2a | root_double |
| Δ<0 无实根 | 无 | — |

---

## Scene 0: 开场 (3.5s)
**目的**: 钩子 + 引出问题

元素:
1. 作者信息（顶部）
2. 大标题：一元二次方程
3. 核心方程 ax²+bx+c=0
4. 钩子问题：Δ<0 时根在哪？

动画序列:
| 时间 | 动作 |
|------|------|
| 0.0s | 作者信息 FadeIn |
| 0.3s | 标题 Write |
| 1.0s | 方程 Write |
| 1.8s | 问号 / 钩子文字 FadeIn |
| 2.5s | 等待 |
| 3.5s | FadeOut 钩子 |

---

## Scene 1: 判别式 Δ (5s)
**目的**: 引入 Δ = b²-4ac，三种情形

元素:
1. 判别式公式 Δ = b²-4ac
2. 三行条件文字（Δ>0 Δ=0 Δ<0）

---

## Scene 2: Δ>0 两实根 (12s)
**目的**: 可视化 Δ>0 时抛物线与 x 轴两交点

元素:
- Axes 坐标系（主内容区）
- 抛物线（绿色）：f(x) = x²-3x+2（Δ=1>0）
- 两个根的 Dot + DashedLine
- 求根公式代入展示
- 韦达定理短暂提示

---

## Scene 3: Δ=0 重根 (10s)
**目的**: 抛物线与 x 轴切于一点

元素:
- 新抛物线（蓝色）：f(x) = x²-2x+1（Δ=0）
- 单根 Dot，标注 x=-b/2a

---

## Scene 4: Δ<0 无实根 (12s)
**目的**: 抛物线在 x 轴上方，无实数根

元素:
- 新抛物线（红色）：f(x) = x²-2x+5（Δ=-16<0）
- X 叉号：无实数根！
- 引出：复数范围的根

---

## Scene 5: 复数根公式 (15s)
**目的**: 给出共轭虚根公式，逐步推导

元素:
- 公式步骤：
  1. x = (-b ± √Δ)/(2a)
  2. Δ < 0，令 Δ = -|Δ|
  3. √Δ = i√|Δ|
  4. x = (-b ± i√|Δ|)/(2a)
- 颜色高亮 i

---

## Scene 6: 韦达定理（复数范围）(10s)
**目的**: 韦达定理在复数域成立

元素:
- x₁+x₂ = -b/a
- x₁·x₂ = c/a
- 共轭验证示例（代入 x²-2x+5=0 验证）

---

## Scene 7: 片尾 (3s)
**目的**: 关注作者

元素:
- 作者名放大
- "关注我，学更多数学技巧！"

---

## 元素生命周期追踪表
| 元素 | 创建 | 销毁 |
|------|------|------|
| author_info | Scene0 | Scene7 (transform) |
| hook_text | Scene0 | Scene0 末 |
| delta_formula | Scene1 | Scene1 末 |
| axes | Scene2 | Scene4 末 |
| parabola_green | Scene2 | Scene3 初 |
| parabola_blue | Scene3 | Scene4 初 |
| parabola_red | Scene4 | Scene4 末 |
| complex_steps | Scene5 | Scene5 末 |
| vieta_group | Scene6 | Scene6 末 |