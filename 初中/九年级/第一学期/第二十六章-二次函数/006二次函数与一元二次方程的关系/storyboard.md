# 二次函数与一元二次方程的关系 - 动画分镜脚本

## 元信息
- 目标时长: 75-90秒
- 场景数量: 8个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
# 主题颜色
COLOR_PARABOLA = "#e74c3c"           # 红色 - 抛物线
COLOR_X_AXIS = "#3498db"             # 蓝色 - x轴
COLOR_INTERSECTION = "#2ecc71"       # 绿色 - 交点
COLOR_DISCRIMINANT = "#f39c12"       # 橙色 - 判别式
COLOR_EQUATION = GOLD                # 金色 - 方程
COLOR_HIGHLIGHT = YELLOW             # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B             # 灰色 - 辅助
BACKGROUND_COLOR = "#1a1a2e"         # 深蓝黑 - 背景
```

## 核心概念
1. **抛物线与x轴交点的横坐标 = 方程的根**
2. **判别式Δ = b² - 4ac 决定交点个数**
   - Δ > 0: 两个交点（两个不等实根）
   - Δ = 0: 一个交点（两个相等实根，顶点在x轴上）
   - Δ < 0: 无交点（无实根）

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 坐标系 | Axes配置 | self.axes | x∈[-5,5], y∈[-3,5] |
| 抛物线1 (Δ>0) | y = (x-1)(x-3) = x²-4x+3 | self.func_two_roots | 两个交点 |
| 抛物线2 (Δ=0) | y = (x-2)² = x²-4x+4 | self.func_one_root | 一个交点 |
| 抛物线3 (Δ<0) | y = x²-2x+3 | self.func_no_root | 无交点 |
| 交点坐标 | 方程求根 | self.roots_* | 精确计算 |
| 判别式 | Δ = b²-4ac | self.delta_* | 验证性质 |

## 关键参数设置

```python
# 示例1: Δ>0, 两个交点
PARAMS_TWO_ROOTS = {
    'a': 1,
    'b': -4,
    'c': 3,
    'delta': 4,  # b²-4ac = 16-12 = 4 > 0
    'roots': [1, 3],
    'description': '两个不等实根'
}

# 示例2: Δ=0, 一个交点
PARAMS_ONE_ROOT = {
    'a': 1,
    'b': -4,
    'c': 4,
    'delta': 0,  # b²-4ac = 16-16 = 0
    'roots': [2],  # 重根
    'description': '两个相等实根'
}

# 示例3: Δ<0, 无交点
PARAMS_NO_ROOT = {
    'a': 1,
    'b': -2,
    'c': 3,
    'delta': -8,  # b²-4ac = 4-12 = -8 < 0
    'roots': [],
    'description': '无实根'
}

# 坐标系配置
AXES_CONFIG = {
    'x_range': [-1, 5, 1],
    'y_range': [-2, 5, 1],
    'x_length': 7,
    'y_length': 10,
    'axis_config': {
        'include_numbers': True,
        'font_size': 18,
        'color': WHITE
    }
}
```

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 吸引注意力，提出核心问题

### 元素生命周期
- author_info (0-90s) - 贯穿全片
- hook_question (0-3.5s)
- parabola_preview (1.5-4.5s)

### 视觉元素
1. 作者标识（顶部，贯穿全片）
   - 文字: "上海初高中数学直通车 @emptyandcalm"
   - 位置: y=7
   - 字体大小: 20
   - 颜色: GRAY_B

2. 钩子问题（大字，中心）
   - 文字: "抛物线与x轴的交点藏着什么秘密?"
   - 位置: y=5
   - 字体大小: 38
   - 颜色: COLOR_HIGHLIGHT

3. 快速预览（三种情况的抛物线闪烁）
   - 三条抛物线快速出现
   - 交点数量不同
   - 引发好奇

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | run_time=0.3 |
| 0.3s | 钩子问题书写 | `Write(hook_question)` | run_time=0.8 |
| 1.5s | 三条抛物线闪现 | `Succession(FadeIn, FadeOut)` | 快速切换 |
| 3.0s | 等待 | `self.wait(0.5)` | 给观众反应时间 |
| 3.5s | 清理问题 | `FadeOut(hook_question)` | run_time=0.4 |

### 场景切换
- 保留: author_info
- 移除: hook_question, parabola_preview

---

## Scene 2: 建立坐标系与概念引入 (5-12秒)

**目的**: 建立数学环境，引入核心概念

### 元素生命周期
- axes (5-90s) - 贯穿全片
- title_relationship (5-10s)
- concept_intro (7-12s)

### 视觉元素
1. 坐标系
   - 配置: x∈[-1,5], y∈[-2,5]
   - 位置: 整体向下偏移 DOWN*1
   - x轴加粗标记: COLOR_X_AXIS
   - 刻度标注: 整数点

2. 标题
   - 文字: "二次函数 ↔ 一元二次方程"
   - 位置: y=6
   - 字体大小: 32

3. 概念说明
   - 文字: "交点横坐标 = 方程的根"
   - 位置: y=-5
   - 字体大小: 24

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 5.0s | 坐标系创建 | `Create(axes)` | run_time=1.2 |
| 6.2s | x轴强调 | x轴变色闪烁 | COLOR_X_AXIS |
| 6.8s | 标题淡入 | `FadeIn(title)` | run_time=0.5 |
| 7.5s | 概念说明出现 | `Write(concept_intro)` | run_time=0.8 |
| 9.0s | 等待理解 | `self.wait(1.5)` | 重要概念 |
| 10.5s | 清理标题 | `FadeOut(title, concept_intro)` | run_time=0.4 |

### 几何计算
```python
# 坐标系设置
self.axes = Axes(
    x_range=[-1, 5, 1],
    y_range=[-2, 5, 1],
    x_length=7,
    y_length=10,
    axis_config={...}
).shift(DOWN * 1)

# x轴高亮
self.x_axis_highlight = self.axes.get_x_axis().copy().set_color(COLOR_X_AXIS).set_stroke(width=6)
```

---

## Scene 3: 情况1 - Δ>0 两个交点 (12-30秒)

**目的**: 展示判别式大于0的情况

### 元素生命周期
- parabola_two (12-30s)
- equation_two (12-30s)
- intersection_dots (15-30s)
- delta_formula (18-28s)

### 视觉元素
1. 方程显示
   - 公式: y = x² - 4x + 3
   - 因式分解: y = (x-1)(x-3)
   - 位置: y=5.5
   - 颜色: COLOR_EQUATION

2. 抛物线
   - 函数: y = x² - 4x + 3
   - 颜色: COLOR_PARABOLA
   - 线宽: 4
   - x范围: [-1, 5]

3. 交点
   - 点1: (1, 0)
   - 点2: (3, 0)
   - 颜色: COLOR_INTERSECTION
   - 半径: 0.12

4. 判别式计算
   - Δ = b² - 4ac = 16 - 12 = 4 > 0
   - 位置: y=-5
   - 分步显示

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 12.0s | 方程出现 | `Write(equation)` | run_time=0.8 |
| 13.0s | 抛物线绘制 | `Create(parabola)` | run_time=1.5 |
| 14.8s | 交点1闪现 | `FadeIn + Flash` | (1, 0) |
| 15.5s | 交点2闪现 | `FadeIn + Flash` | (3, 0) |
| 16.5s | 标注根 | x₁=1, x₂=3 标签 | run_time=0.6 |
| 17.5s | 判别式标题 | "判别式 Δ" 出现 | y=-4.5 |
| 18.0s | 计算步骤1 | Δ = b² - 4ac | run_time=0.5 |
| 18.7s | 计算步骤2 | = (-4)² - 4(1)(3) | run_time=0.5 |
| 19.5s | 计算步骤3 | = 16 - 12 = 4 | run_time=0.5 |
| 20.3s | 结论强调 | "Δ > 0 → 两个交点" | 闪烁 |
| 21.5s | 垂直虚线 | 从交点到x轴 | 强调横坐标 |
| 23.0s | 等待理解 | `self.wait(2.0)` | 关键概念 |
| 25.0s | 清理辅助元素 | FadeOut判别式、虚线 | run_time=0.5 |

### 几何精确计算
```python
# 方程参数
self.a1 = 1
self.b1 = -4
self.c1 = 3

# 抛物线函数
self.func_two = lambda x: self.a1 * x**2 + self.b1 * x + self.c1

# 精确求根（因式分解形式）
self.root1_1 = 1.0
self.root1_2 = 3.0

# 验证: f(root) = 0
assert abs(self.func_two(self.root1_1)) < 1e-10
assert abs(self.func_two(self.root1_2)) < 1e-10

# 交点坐标（Manim坐标）
self.intersection1_1 = self.axes.c2p(self.root1_1, 0)
self.intersection1_2 = self.axes.c2p(self.root1_2, 0)

# 判别式验证
self.delta1 = self.b1**2 - 4*self.a1*self.c1
assert self.delta1 == 4 and self.delta1 > 0
```

---

## Scene 4: 情况2 - Δ=0 一个交点 (30-48秒)

**目的**: 展示判别式等于0的情况

### 元素生命周期
- parabola_one (30-48s)
- equation_one (30-48s)
- intersection_tangent (33-48s)
- vertex_annotation (35-48s)

### 视觉元素
1. 方程显示
   - 公式: y = x² - 4x + 4
   - 完全平方: y = (x-2)²
   - 位置: y=5.5
   - 颜色: COLOR_EQUATION

2. 抛物线
   - 函数: y = (x-2)²
   - 颜色: COLOR_PARABOLA
   - **顶点在x轴上**

3. 交点（切点）
   - 点: (2, 0)
   - 颜色: COLOR_INTERSECTION
   - 半径: 0.12
   - 特殊标记: 双圆圈表示重根

4. 判别式计算
   - Δ = b² - 4ac = 16 - 16 = 0
   - 强调: **顶点式特征**

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 30.0s | 清除上一场景 | `FadeOut(parabola1, dots)` | run_time=0.5 |
| 30.8s | 新方程出现 | `Write(equation2)` | run_time=0.8 |
| 31.8s | 强调完全平方 | 因式分解动画 | TransformMatchingTex |
| 32.8s | 抛物线绘制 | `Create(parabola2)` | run_time=1.5 |
| 34.5s | 切点闪现 | `FadeIn + Flash` | (2, 0) |
| 35.3s | 双圆圈标记 | 重根符号 | run_time=0.4 |
| 36.0s | 标注 | "x₁=x₂=2 (重根)" | run_time=0.6 |
| 37.0s | 判别式计算 | Δ = 16 - 16 = 0 | 分步 |
| 38.5s | 结论 | "Δ = 0 → 一个交点" | 闪烁 |
| 39.5s | 顶点标注 | "顶点在x轴上" | 关键特征 |
| 41.0s | x轴相切动画 | 抛物线与x轴切线 | 视觉强化 |
| 43.0s | 等待理解 | `self.wait(2.0)` | 关键概念 |
| 45.0s | 清理 | FadeOut辅助元素 | run_time=0.5 |

### 几何精确计算
```python
# 方程参数
self.a2 = 1
self.b2 = -4
self.c2 = 4

# 抛物线函数（完全平方形式）
self.func_one = lambda x: (x - 2)**2

# 精确求根（重根）
self.root2 = 2.0

# 验证
assert abs(self.func_one(self.root2)) < 1e-10

# 顶点坐标（就是交点）
self.vertex2 = self.axes.c2p(2, 0)

# 判别式验证
self.delta2 = self.b2**2 - 4*self.a2*self.c2
assert self.delta2 == 0

# 验证顶点在x轴上
assert abs(self.func_one(2) - 0) < 1e-10
```

---

## Scene 5: 情况3 - Δ<0 无交点 (48-63秒)

**目的**: 展示判别式小于0的情况

### 元素生命周期
- parabola_none (48-63s)
- equation_none (48-63s)
- no_intersection_mark (52-63s)

### 视觉元素
1. 方程显示
   - 公式: y = x² - 2x + 3
   - 位置: y=5.5
   - 颜色: COLOR_EQUATION

2. 抛物线
   - 函数: y = x² - 2x + 3
   - 颜色: COLOR_PARABOLA
   - **完全在x轴上方**

3. 无交点标记
   - x轴与抛物线间的距离线
   - 文字: "无交点"
   - 颜色: GRAY_B（淡化）

4. 判别式计算
   - Δ = b² - 4ac = 4 - 12 = -8 < 0
   - 强调: **负数 → 无实根**

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 48.0s | 清除上一场景 | `FadeOut(parabola2, dot)` | run_time=0.5 |
| 48.8s | 新方程出现 | `Write(equation3)` | run_time=0.8 |
| 49.8s | 抛物线绘制 | `Create(parabola3)` | run_time=1.5 |
| 51.5s | 强调分离 | x轴闪烁 | COLOR_X_AXIS |
| 52.3s | 距离线动画 | 从顶点到x轴虚线 | run_time=0.6 |
| 53.2s | 无交点标记 | "✗ 无交点" 出现 | run_time=0.4 |
| 54.0s | 判别式计算 | Δ = 4 - 12 = -8 | 分步 |
| 55.5s | 结论 | "Δ < 0 → 无交点" | 闪烁 |
| 56.5s | 说明 | "无实数根" | y=-5.5 |
| 58.0s | 等待理解 | `self.wait(2.0)` | 关键概念 |
| 60.0s | 清理 | FadeOut辅助元素 | run_time=0.5 |

### 几何精确计算
```python
# 方程参数
self.a3 = 1
self.b3 = -2
self.c3 = 3

# 抛物线函数
self.func_none = lambda x: self.a3 * x**2 + self.b3 * x + self.c3

# 顶点坐标
self.h3 = -self.b3 / (2 * self.a3)  # = 1
self.k3 = self.func_none(self.h3)    # = 2

# 验证顶点在x轴上方
assert self.k3 > 0

# 判别式验证
self.delta3 = self.b3**2 - 4*self.a3*self.c3
assert self.delta3 == -8 and self.delta3 < 0

# 顶点到x轴距离
self.vertex3_pos = self.axes.c2p(self.h3, self.k3)
self.vertex3_proj = self.axes.c2p(self.h3, 0)
self.distance_to_x_axis = self.k3  # 2
```

---

## Scene 6: 三种情况对比总结 (63-75秒)

**目的**: 系统对比三种情况，强化记忆

### 元素生命周期
- comparison_table (63-75s)
- three_parabolas_small (63-75s)

### 视觉元素
1. 三条抛物线并排显示（缩小版）
   - 位置: 上半部分 y∈[2, 5]
   - 左: Δ>0, 中: Δ=0, 右: Δ<0
   - 同步缩放

2. 对比表格
   - 位置: 下半部分 y∈[-5, 1]
   - 三列对比
   - 颜色编码

### 对比表格内容
| Δ > 0 | Δ = 0 | Δ < 0 |
|-------|-------|-------|
| 两个交点 | 一个交点 | 无交点 |
| 两个不等实根 | 两个相等实根 | 无实根 |
| x₁ ≠ x₂ | x₁ = x₂ | - |

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 63.0s | 清空场景 | `FadeOut(all)` | run_time=0.5 |
| 63.8s | 标题 | "三种情况对比" | y=6 |
| 64.5s | 三条抛物线出现 | 并排淡入 | run_time=1.0 |
| 65.8s | 标注Δ值 | Δ>0, Δ=0, Δ<0 | 在各抛物线下方 |
| 67.0s | 表格行1 | 交点个数 | 依次出现 |
| 68.0s | 表格行2 | 根的情况 | 依次出现 |
| 69.0s | 表格行3 | 具体值/说明 | 依次出现 |
| 70.5s | 整体闪烁 | 强调对比 | run_time=0.8 |
| 71.5s | 等待记忆 | `self.wait(2.0)` | 重要总结 |
| 73.5s | 清理 | FadeOut | run_time=0.5 |

---

## Scene 7: 判别式公式强化 (75-82秒)

**目的**: 强化判别式公式的记忆

### 视觉元素
1. 判别式公式大字显示
   - Δ = b² - 4ac
   - 位置: 中心
   - 字体大小: 48
   - 颜色: COLOR_DISCRIMINANT

2. 三种情况图标
   - 符号: >, =, <
   - 对应结果: 2个, 1个, 0个
   - 图形化展示

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 75.0s | 公式放大入场 | `GrowFromCenter` | run_time=0.8 |
| 76.0s | 公式闪烁 | `Flash` 多次 | 强调记忆 |
| 77.0s | 三种情况图标 | 从公式下方展开 | run_time=1.0 |
| 78.5s | 关键提示 | "记住判别式!" | y=-5 |
| 80.0s | 等待 | `self.wait(1.5)` | |
| 81.5s | 清理 | FadeOut | run_time=0.5 |

---

## Scene 8: 片尾关注 (82-90秒)

**目的**: 品牌强化，引导关注

### 元素生命周期
- author_large (82-90s)
- follow_cta (82-90s)
- decorative_elements (84-90s)

### 视觉元素
1. 作者信息放大
   - "上海初高中数学直通车"
   - "@emptyandcalm"
   - 字体大小: 36

2. 关注引导
   - "关注我，轻松学二次函数!"
   - 颜色: YELLOW
   - 字体大小: 28

3. 装饰元素
   - 三条小抛物线（代表三种情况）
   - 旋转动画
   - 颜色: 红/橙/绿

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 82.0s | 作者信息放大 | `author_info.animate.scale(1.8)` | run_time=0.7 |
| 82.8s | ID淡入 | `FadeIn(author_id)` | run_time=0.4 |
| 83.5s | 关注文字 | `Write(follow_text)` | run_time=0.7 |
| 84.5s | 装饰抛物线出现 | 3条小抛物线 | run_time=0.5 |
| 85.2s | 旋转动画 | `Rotate(parabolas, PI)` | run_time=1.5 |
| 86.7s | 闪烁强调 | 关注文字闪烁 | run_time=0.8 |
| 87.8s | 等待 | `self.wait(1.2)` | |
| 89.0s | 全部淡出 | `FadeOut(all)` | run_time=1.0 |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 存活时长 | 备注 |
|------|---------|---------|----------|------|
| author_info | Scene 1 | Scene 8 | 0-90s | 贯穿全片 |
| axes | Scene 2 | Scene 6 | 5-75s | 主坐标系 |
| parabola_two | Scene 3 | Scene 3 | 12-30s | Δ>0情况 |
| parabola_one | Scene 4 | Scene 4 | 30-48s | Δ=0情况 |
| parabola_none | Scene 5 | Scene 5 | 48-63s | Δ<0情况 |
| comparison_table | Scene 6 | Scene 6 | 63-75s | 对比总结 |
| delta_formula | Scene 7 | Scene 7 | 75-82s | 公式强化 |

---

## 时间节奏控制

| 场景 | 时长 | 节奏 | 说明 |
|------|------|------|------|
| Scene 1 | 5s | 快 | 钩子，抓注意 |
| Scene 2 | 7s | 中 | 建立环境 |
| Scene 3 | 18s | 慢 | **核心概念1** |
| Scene 4 | 18s | 慢 | **核心概念2** |
| Scene 5 | 15s | 中 | 核心概念3 |
| Scene 6 | 12s | 中 | 对比总结 |
| Scene 7 | 7s | 快 | 公式强化 |
| Scene 8 | 8s | 慢 | 品牌记忆 |

**总时长**: 90秒

---

## 验证检查清单

### 几何精度
- [ ] 所有交点通过方程求根精确计算
- [ ] 抛物线函数验证: f(root) = 0
- [ ] 判别式计算验证: Δ = b²-4ac
- [ ] 顶点坐标精确: h=-b/2a, k=f(h)

### 视觉边界
- [ ] 所有元素在安全区域内 (x∈[-4,4], y∈[-7,7])
- [ ] 抛物线不超出坐标系范围
- [ ] 文字标签无重叠
- [ ] 公式不溢出屏幕

### 动画质量
- [ ] 关键概念停留≥1.5s
- [ ] 场景切换流畅
- [ ] 颜色对比清晰
- [ ] 三种情况对比明确

### 教学效果
- [ ] 概念顺序符合认知规律
- [ ] 视觉引导明确
- [ ] 重点突出（交点=根，判别式）
- [ ] 语言简洁（九年级水平）

---

## 配音脚本（可选）

### Scene 1 (0-5s)
"抛物线与x轴的交点，藏着什么秘密？今天揭晓答案！"

### Scene 3 (12-30s)
"看这个抛物线，y等于x平方减4x加3。它与x轴有两个交点，横坐标是1和3。注意！这正是方程x²-4x+3=0的两个根！判别式Δ等于b²减4ac，算出来是4，大于0，所以有两个不等实根。"

### Scene 4 (30-48s)
"再看这个，y等于x减2的平方。这是完全平方式，抛物线的顶点刚好在x轴上！只有一个交点，横坐标是2。判别式Δ等于0，两个相等实根，x1等于x2等于2。"

### Scene 5 (48-63s)
"最后这个，y等于x²减2x加3。抛物线完全在x轴上方，没有交点！判别式Δ等于负8，小于0，方程无实数根。"

### Scene 6 (63-75s)
"总结一下：判别式大于0，两个交点；等于0，一个交点；小于0，无交点。记住这个规律，解题快人一步！"

### Scene 8 (82-90s)
"关注我，轻松学二次函数！"

---

## 代码结构框架

```python
class QuadraticFunctionEquationRelation(Scene):
    def construct(self):
        self.setup_config()
        self.setup_geometry()
        self.verify_geometry()
        
        self.scene_1_opening()
        self.scene_2_setup_axes()
        self.scene_3_delta_positive()
        self.scene_4_delta_zero()
        self.scene_5_delta_negative()
        self.scene_6_comparison()
        self.scene_7_formula_emphasis()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """统一计算所有几何数据"""
        # 三种情况的方程参数
        # 交点坐标
        # 判别式值
        pass
    
    def verify_geometry(self):
        """验证计算正确性"""
        # 验证: f(root) = 0
        # 验证: Δ = b²-4ac
        # 验证: 交点个数与Δ符号一致
        pass
```

---

## 备注

1. **重点难点**: Scene 3-5（三种情况）需要清晰对比
2. **视觉连续性**: 坐标系始终保留，抛物线切换流畅
3. **颜色一致性**: 红色=抛物线，蓝色=x轴，绿色=交点，橙色=判别式
4. **教学逻辑**: 从具体示例 → 对比分析 → 公式强化
5. **数学严谨性**: 所有根通过求根公式验证，判别式精确计算