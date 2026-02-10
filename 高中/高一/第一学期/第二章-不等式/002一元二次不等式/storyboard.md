# 一元二次不等式 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高一
- 知识点: 一元二次不等式的解法与二次函数图像的关系

## 颜色配置
```python
COLOR_PARABOLA = "#3498db"        # 蓝色 - 抛物线
COLOR_X_AXIS = WHITE              # 白色 - x轴
COLOR_Y_AXIS = WHITE              # 白色 - y轴
COLOR_ROOT = "#e74c3c"            # 红色 - 根/交点
COLOR_POSITIVE = "#2ecc71"        # 绿色 - 正值区域
COLOR_NEGATIVE = "#e67e22"        # 橙色 - 负值区域
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助元素
BACKGROUND_COLOR = "#1a1a2e"      # 深蓝灰 - 背景
```

## 几何/数学预计算清单

### 示例方程: x² - 3x + 2 > 0

| 元素 | 计算公式 | 存储变量 | 数值 |
|------|---------|---------|------|
| 系数a | 给定 | self.a | 1 |
| 系数b | 给定 | self.b | -3 |
| 系数c | 给定 | self.c | 2 |
| 判别式 | Δ = b² - 4ac | self.delta | 9 - 8 = 1 |
| 根x₁ | (-b - √Δ) / 2a | self.x1 | 1 |
| 根x₂ | (-b + √Δ) / 2a | self.x2 | 2 |
| 顶点x坐标 | -b / 2a | self.vertex_x | 1.5 |
| 顶点y坐标 | f(vertex_x) | self.vertex_y | -0.25 |
| 坐标系范围 | x: [-1, 4], y: [-1, 4] | axes配置 | - |

### 三种判别式情况
- **Δ > 0**: 两个不等实根 (本例)
- **Δ = 0**: 一个重根 (补充说明)
- **Δ < 0**: 无实根 (补充说明)

---

## Scene 1: 开场钩子 (3秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题文字
3. 不等式符号闪烁

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 顶部y=7位置 |
| 0.2s | 钩子文字书写 | `Write(hook_text)` | "一元二次不等式怎么解?" |
| 1.0s | 不等式显示 | `Write(inequality)` | x² - 3x + 2 > 0 |
| 1.8s | 符号闪烁 | `Flash(symbol)` | 高亮">"符号 |
| 2.5s | 等待 | `Wait(0.5)` | 停顿让观众思考 |

### 清理
- 保留: author_info
- 淡出: hook_text, inequality (移动到新位置)

---

## Scene 2: 问题转化 (5秒)
**目的**: 说明不等式与二次函数的关系

### 元素
1. 标题: "核心思路"
2. 不等式 → 函数转化
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题淡入 | `FadeIn(title)` | y=5.5位置 |
| 0.5s | 显示函数 | `Write(function)` | y = x² - 3x + 2 |
| 1.2s | 转化箭头 | `Create(arrow)` | 不等式→函数 |
| 1.8s | 说明文字 | `FadeIn(explain)` | "求y>0对应的x范围" |
| 3.5s | 高亮y>0 | `Indicate(text)` | 强调关键 |
| 4.5s | 等待 | `Wait(0.5)` | 理解停顿 |

### 清理
- 移动function到坐标系上方
- 淡出: title, arrow, explain

---

## Scene 3: 建立坐标系 (4秒)
**目的**: 绘制坐标轴，准备画图

### 元素
1. x轴, y轴
2. 刻度标记
3. 原点标注

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 创建坐标系 | `Create(axes)` | 绘制轴线 |
| 1.5s | 添加刻度 | `FadeIn(labels)` | x, y刻度值 |
| 2.5s | 标注原点 | `FadeIn(origin_label)` | "O" |
| 3.5s | 等待 | `Wait(0.5)` | - |

### 几何约束
- 坐标系中心: y=1 (留出上下空间)
- x范围: [-1, 4] (包含根和对称性)
- y范围: [-1, 4] (显示顶点和正值)
- 缩放: 0.85 (适配竖屏)

### 清理
- 保留: axes, labels

---

## Scene 4: 绘制抛物线 (6秒)
**目的**: 画出y = x² - 3x + 2的图像

### 元素
1. 抛物线曲线
2. 函数表达式标注
3. 抛物线开口方向说明

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 绘制抛物线 | `Create(parabola)` | 从左到右 |
| 2.5s | 函数标注 | `FadeIn(func_label)` | 靠近抛物线 |
| 3.5s | 说明文字 | `FadeIn(explain)` | "a>0, 开口向上" |
| 5.0s | 等待 | `Wait(1.0)` | 观察图像 |

### 精确计算
```python
# 抛物线函数
def parabola_func(x):
    return x**2 - 3*x + 2

# 使用axes.plot绘制
parabola = axes.plot(parabola_func, x_range=[-0.5, 3.5], color=COLOR_PARABOLA)
```

### 清理
- 保留: parabola, func_label
- 淡出: explain

---

## Scene 5: 求解方程找根 (8秒)
**目的**: 解x² - 3x + 2 = 0，找交点

### 元素
1. 方程 x² - 3x + 2 = 0
2. 求根公式
3. 计算过程
4. 根的位置标记

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 显示方程 | `Write(equation)` | x² - 3x + 2 = 0 |
| 1.0s | 因式分解 | `TransformMatchingTex` | (x-1)(x-2) = 0 |
| 2.5s | 显示根 | `Write(roots)` | x₁=1, x₂=2 |
| 3.5s | 标记x₁ | `FadeIn(dot1)` + `Flash` | 红点在(1,0) |
| 4.3s | 标记x₂ | `FadeIn(dot2)` + `Flash` | 红点在(2,0) |
| 5.0s | 虚线连接 | `Create(dashed_lines)` | 从根到x轴 |
| 6.5s | 等待 | `Wait(1.5)` | 强调根的位置 |

### 精确坐标计算
```python
# 根的坐标
root1_point = axes.c2p(1, 0)  # (x=1, y=0)
root2_point = axes.c2p(2, 0)  # (x=2, y=2)

# 根在抛物线上的点
root1_on_curve = axes.c2p(1, parabola_func(1))  # 应该≈0
root2_on_curve = axes.c2p(2, parabola_func(2))  # 应该≈0
```

### 清理
- 保留: dot1, dot2, root标签
- 淡出: equation, calculation steps

---

## Scene 6: 分析正负区域 (10秒)
**目的**: 标记y>0和y<0的x范围

### 元素
1. 区域着色
2. 区域标注
3. 不等式解集

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 标题 | `Write(title)` | "观察函数值正负" |
| 0.8s | 说明y>0 | `FadeIn(explain1)` | "抛物线在x轴上方" |
| 1.5s | 高亮左区间 | `FadeIn(left_region)` | x < 1, 绿色 |
| 2.5s | 高亮右区间 | `FadeIn(right_region)` | x > 2, 绿色 |
| 3.5s | 说明y<0 | `FadeIn(explain2)` | "抛物线在x轴下方" |
| 4.5s | 高亮中间区间 | `FadeIn(mid_region)` | 1 < x < 2, 橙色 |
| 6.0s | 显示解集 | `Write(solution)` | x<1 或 x>2 |
| 8.0s | 高亮解集 | `SurroundingRectangle` | 黄色框 |
| 9.0s | 等待 | `Wait(1.0)` | 理解 |

### 区域绘制
```python
# y>0区域 (绿色阴影)
left_area = axes.get_area(
    parabola, 
    x_range=[-0.5, 1], 
    color=COLOR_POSITIVE, 
    opacity=0.3
)
right_area = axes.get_area(
    parabola, 
    x_range=[2, 3.5], 
    color=COLOR_POSITIVE, 
    opacity=0.3
)

# y<0区域 (橙色阴影，需要特殊处理因为在x轴下方)
mid_area = axes.get_riemann_rectangles(
    parabola, 
    x_range=[1, 2],
    dx=0.1,
    color=COLOR_NEGATIVE,
    fill_opacity=0.3
)
```

### 清理
- 保留: regions, solution
- 淡出: title, explains

---

## Scene 7: 三种情况总结 (12秒)
**目的**: 展示Δ>0, Δ=0, Δ<0三种情况

### 元素
1. 三个小坐标系
2. 三条抛物线
3. 判别式说明
4. 解集结论

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 清屏 | `FadeOut(previous)` | 移除之前元素 |
| 0.8s | 标题 | `Write(title)` | "判别式决定根的情况" |
| 1.5s | 显示Δ>0情况 | `Create(case1)` | 左侧小图 |
| 3.0s | 显示Δ=0情况 | `Create(case2)` | 中间小图 |
| 4.5s | 显示Δ<0情况 | `Create(case3)` | 右侧小图 |
| 6.0s | 标注解集 | `Write(solutions)` | 每种情况下方 |
| 9.0s | 强调公式 | `Indicate(formulas)` | Δ = b² - 4ac |
| 10.5s | 等待 | `Wait(1.5)` | 理解总结 |

### 三种情况配置
```python
# Case 1: Δ > 0
case1_func = lambda x: x**2 - 3*x + 2
case1_solution = "x < x₁ 或 x > x₂"

# Case 2: Δ = 0
case2_func = lambda x: (x - 1.5)**2
case2_solution = "x ≠ -b/2a"

# Case 3: Δ < 0
case3_func = lambda x: x**2 + 1
case3_solution = "x ∈ R"
```

### 清理
- 保留: 三个case的图
- 准备片尾

---

## Scene 8: 片尾关注 (4秒)
**目的**: 品牌露出，引导关注

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 | 说明 |
|------|------|---------|------|
| 0.0s | 清屏 | `FadeOut(all)` | 保留author_info |
| 0.5s | 作者名放大 | `Transform(author)` | 移到中心 |
| 1.2s | ID显示 | `FadeIn(author_id)` | @emptyandcalm |
| 2.0s | 关注文字 | `FadeIn(follow)` | "关注我获得更多..." |
| 3.0s | 抛物线装饰 | `Create(deco)` | 小抛物线图案 |
| 4.0s | 结束 | - | - |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| axes | Scene 3 | Scene 7 | 主坐标系 |
| parabola | Scene 4 | Scene 7 | 主抛物线 |
| root_dots | Scene 5 | Scene 7 | 根的标记 |
| regions | Scene 6 | Scene 7 | 正负区域 |
| solution_text | Scene 6 | Scene 7 | 解集 |
| case_groups | Scene 7 | Scene 8 | 三种情况 |

---

## 数学验证检查点

### 验证1: 根的正确性
```python
assert abs(parabola_func(1)) < 1e-6, "x=1应该是根"
assert abs(parabola_func(2)) < 1e-6, "x=2应该是根"
```

### 验证2: 顶点位置
```python
vertex_x_calc = -self.b / (2 * self.a)
assert abs(vertex_x_calc - 1.5) < 1e-6, "顶点x坐标错误"
```

### 验证3: 判别式
```python
delta_calc = self.b**2 - 4*self.a*self.c
assert delta_calc == 1, "判别式应该等于1"
```

### 验证4: 边界检查
```python
# 确保所有元素在安全边界内
assert axes.get_center()[1] > -7 and axes.get_center()[1] < 7
```

---

## 动画节奏说明

- **快节奏**: Scene 1 (钩子), Scene 8 (结尾)
- **中速节奏**: Scene 2, 3, 4 (建立概念)
- **慢节奏**: Scene 5, 6 (核心步骤，多停顿)
- **总结节奏**: Scene 7 (清晰展示三种情况)

**总时长预计**: 60-65秒