# 椭圆的几何性质 - 动画分镜脚本

## 元信息
- 目标时长: 80-95 秒
- 场景数量: 9 个
- 难度等级: 中等偏难
- 目标观众: 高二学生

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"      # 红色 - 椭圆
COLOR_FOCUS = "#f39c12"        # 橙色 - 焦点
COLOR_DIRECTRIX = "#9b59b6"    # 紫色 - 准线
COLOR_LATUS = "#16a085"        # 青绿 - 通径
COLOR_HIGHLIGHT = YELLOW        # 高亮色
COLOR_AUXILIARY = GRAY_B        # 辅助线
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 数值示例 |
|------|---------|---------|---------|
| 长半轴 | a | self.a | 3.0 |
| 短半轴 | b | self.b | 2.0 |
| 半焦距 | c = √(a²-b²) | self.c | 2.236 |
| 离心率 | e = c/a | self.e | 0.745 |
| 准线距离 | a²/c | self.directrix_x | 4.025 |
| 通径长度 | 2b²/a | self.latus_length | 2.667 |
| 焦点 | (±c, 0) | self.F1, self.F2 | (±2.236, 0) |
| 准线 | x = ±a²/c | self.L1, self.L2 | x = ±4.025 |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 引出椭圆的性质

### 元素
1. 作者标识
2. 钩子："椭圆有哪些神奇的性质？"
3. 椭圆预览

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子问题 | `Write(hook_text)` |
| 1.1s | 坐标系+椭圆 | `Create(axes, ellipse)` |
| 2.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: hook_text
- 保留: axes, ellipse, author_info

---

## Scene 2: 范围与对称性 (7秒)
**目的**: 展示椭圆的范围和对称性

### 元素
1. 标题："范围与对称性"
2. 矩形边界框显示范围
3. 对称轴标注
4. 文字说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 边界框 | `Create(boundary_rect)` |
| 1.2s | 范围标注 | 显示 -a≤x≤a, -b≤y≤b |
| 2.5s | x轴对称 | 镜像动画 |
| 3.5s | y轴对称 | 镜像动画 |
| 4.5s | 原点对称 | 旋转180° |
| 6.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, boundary_rect, labels
- 保留: ellipse

---

## Scene 3: 离心率概念 (10秒)
**目的**: 解释离心率的定义和意义

### 元素
1. 标题："离心率 e = c/a"
2. 公式：e = c/a (0 < e < 1)
3. c和a的标注
4. 离心率数值显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 公式书写 | `Write(formula)` |
| 1.2s | 焦点标注 | 显示F₁, F₂ |
| 1.8s | c标注 | 焦距标注 |
| 2.5s | a标注 | 长半轴标注 |
| 3.5s | e值计算 | 显示 e ≈ 0.745 |
| 4.5s | 范围说明 | 0 < e < 1 |
| 6.5s | 意义说明 | "e越大越扁" |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, labels
- 保留: ellipse, foci

---

## Scene 4: 离心率的影响 (12秒)
**目的**: 可视化不同离心率的椭圆形状

### 元素
1. 标题："离心率的影响"
2. 三个椭圆对比
3. e值动态变化
4. 形状说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | e→1动画 | 椭圆变扁 |
| 1.5s | 说明文字 | "e接近1，椭圆越扁" |
| 3.0s | 恢复原状 | 回到e=0.745 |
| 4.0s | e→0动画 | 椭圆变圆 |
| 5.0s | 说明文字 | "e接近0，椭圆越圆" |
| 7.0s | 恢复原状 | 回到e=0.745 |
| 8.5s | 极限说明 | "e=0时为圆，e=1时退化为线段" |
| 10.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, extra_ellipses, labels
- 保留: original ellipse

---

## Scene 5: 准线的定义 (10秒)
**目的**: 介绍准线的位置和计算

### 元素
1. 标题："准线"
2. 准线方程：x = ±a²/c
3. 两条准线（虚线）
4. 距离标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 公式书写 | `Write(formula)` |
| 1.5s | 右准线出现 | `Create(directrix_right)` |
| 2.2s | 左准线出现 | `Create(directrix_left)` |
| 3.0s | 距离标注 | 标注 a²/c |
| 4.0s | 数值计算 | 显示 9/2.236 ≈ 4.03 |
| 5.5s | 焦点到准线 | 标注距离 |
| 7.5s | 等待 | `Wait(2.5)` |

### 清理
- FadeOut: title, formula, labels
- 保留: ellipse, directrices

---

## Scene 6: 焦半径公式 (9秒)
**目的**: 展示焦半径公式

### 元素
1. 标题："焦半径"
2. 椭圆上一点P
3. 连线PF₁, PF₂
4. 公式：|PF₁| = a + ex₀, |PF₂| = a - ex₀

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 点P出现 | `FadeIn(point_P)` |
| 1.2s | 连线PF₁ | `Create(line_PF1)` |
| 1.8s | 连线PF₂ | `Create(line_PF2)` |
| 2.5s | 公式1 | |PF₁| = a + ex₀ |
| 3.5s | 公式2 | |PF₂| = a - ex₀ |
| 4.5s | x₀标注 | 点P的横坐标 |
| 6.0s | 数值验证 | 显示具体数值 |
| 7.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, point_P, lines, formulas
- 保留: ellipse

---

## Scene 7: 通径 (10秒)
**目的**: 定义和展示通径

### 元素
1. 标题："通径"
2. 过焦点垂直于长轴的弦
3. 长度公式：2b²/a
4. 长度标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 定义文字 | "过焦点垂直于长轴的弦" |
| 1.5s | 通径绘制 | `Create(latus_rectum)` |
| 2.5s | 端点标注 | 标记P₁, P₂ |
| 3.5s | 公式书写 | 长度 = 2b²/a |
| 5.0s | 数值计算 | 2×4/3 ≈ 2.67 |
| 6.5s | 长度标注 | Brace标注 |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, latus_rectum, labels
- 保留: ellipse

---

## Scene 8: 性质总结 (10秒)
**目的**: 汇总所有性质

### 元素
1. 总结标题
2. 5个性质卡片
3. 关键公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(all)` |
| 0.5s | 总结标题 | `Write("椭圆的性质")` |
| 1.0s | 卡片1 | 范围与对称性 |
| 1.8s | 卡片2 | 离心率 e=c/a |
| 2.6s | 卡片3 | 准线 x=±a²/c |
| 3.4s | 卡片4 | 焦半径公式 |
| 4.2s | 卡片5 | 通径 2b²/a |
| 6.0s | 等待 | `Wait(4.0)` |

### 清理
- FadeOut: all

---

## Scene 9: 片尾 (8秒)
**目的**: 引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author)` |
| 0.8s | ID出现 | `FadeIn(author_id)` |
| 1.5s | 关注提示 | `FadeIn(follow_text)` |
| 2.5s | 装饰椭圆 | 多个小椭圆旋转 |
| 4.0s | 旋转动画 | `Rotate` |
| 6.5s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 作者标识 |
| axes | Scene 1 | Scene 7 | 坐标系 |
| ellipse | Scene 1 | Scene 7 | 主椭圆 |
| foci | Scene 3 | Scene 7 | 焦点 |
| directrices | Scene 5 | Scene 7 | 准线 |

---

## 关键技术点

### 1. 离心率变化动画
使用 ValueTracker 控制 b 的大小，从而改变离心率：
```python
b_tracker = ValueTracker(b_initial)
ellipse = always_redraw(lambda: Ellipse(
    width=2*a, 
    height=2*b_tracker.get_value()
))
```

### 2. 准线位置计算
```python
directrix_x = a**2 / c
directrix_right = Line(
    axes.c2p(directrix_x, -5),
    axes.c2p(directrix_x, 5),
    color=COLOR_DIRECTRIX
)
```

### 3. 通径端点计算
过焦点垂直于x轴，代入椭圆方程：
```python
# x = c, 求 y
y_latus = b**2 / a  # 从方程 c²/a² + y²/b² = 1 解出
P1 = (c, y_latus)
P2 = (c, -y_latus)
```

### 4. 焦半径计算
```python
x0 = point_P_x  # P点横坐标
r1 = a + e * x0  # |PF₁|
r2 = a - e * x0  # |PF₂|
```

## 几何验证重点
- ✓ 验证准线位置：x = a²/c
- ✓ 验证通径长度：2b²/a
- ✓ 验证焦半径：r₁ + r₂ = 2a
- ✓ 验证离心率范围：0 < e < 1
- ✓ 验证对称性
- ✓ 边界检查

## 数值示例（a=3, b=2）
```
c = √5 ≈ 2.236
e = c/a ≈ 0.745
准线: x = ±4.025
通径: 2.667
焦点到准线: 4.025 - 2.236 = 1.789
```