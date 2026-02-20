# 抛物线的定义与标准方程 - 动画分镜脚本

## 元信息
- 目标时长: 50-60 秒
- 场景数量: 8 个
- 难度等级: 高二
- 知识点: 抛物线的定义、焦点、准线、标准方程、四种开口

## 颜色配置
```python
COLOR_PARABOLA = "#e74c3c"       # 红色 - 抛物线主体
COLOR_FOCUS = "#f39c12"          # 橙色 - 焦点
COLOR_DIRECTRIX = "#3498db"      # 蓝色 - 准线
COLOR_DISTANCE = "#2ecc71"       # 绿色 - 距离线
COLOR_POINT_P = "#e91e63"        # 粉色 - 动点P
COLOR_AXIS = "#9b59b6"           # 紫色 - 对称轴
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 焦准距p | 固定值2.0 | self.p |
| 焦点F | (p/2, 0) | self.F |
| 准线位置 | x = -p/2 | self.directrix_x |
| 抛物线方程 | y² = 2px | y = ±√(2px) |
| 动点P | (x, √(2px)) | 参数方程 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，展示抛物线的普遍性

### 元素
1. 作者标识（全程保留）
2. 钩子文字："这个曲线随处可见!"
3. 快速闪现实例
   - 喷泉水柱
   - 投篮轨迹
   - 桥拱形状（简化图标）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author)` |
| 0.3s | 钩子文字书写 | `Write(hook)` |
| 1.0s | 小图标依次闪现 | `FadeIn(icons, lag_ratio=0.2)` |
| 2.5s | 图标集合变换为抛物线 | `Transform(icons, parabola)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 位置规划
- 作者信息: y = 7
- 钩子文字: y = 6
- 图标: y = 4, 间距1.5
- 抛物线: 中央 y = 1

### 清理
- FadeOut: hook, icons
- 保留: author, parabola

---

## Scene 2: 抛物线定义 (10-12秒)
**目的**: 展示抛物线的几何定义

### 元素
1. 标题 "抛物线的定义"
2. 焦点 F
3. 准线 l
4. 动点 P
5. 距离线段 PF 和 P到准线
6. 距离标签（相等）
7. 定义公式 |PF| = d

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 焦点F出现 | `FadeIn(F_dot), Write(F_label)` |
| 1.0s | 准线绘制 | `Create(directrix)` |
| 1.6s | 动点P出现 | `FadeIn(P_dot)` |
| 2.2s | 绘制PF线段 | `Create(line_PF)` |
| 2.8s | 绘制P到准线垂线 | `Create(perpendicular)` |
| 3.4s | 显示距离标签 | `FadeIn(dist_labels)` |
| 4.0s | P点开始沿抛物线移动 | `MoveAlongPath(P, parabola, run_time=4)` |
| 8.0s | 显示定义公式 | `Write(definition)` |
| 9.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 抛物线上的点
def parabola_point(x):
    # y² = 2px => y = √(2px)
    if x >= 0:
        y = np.sqrt(2 * self.p * x)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    return None

# 验证定义
dist_PF = np.linalg.norm(P - F)
dist_to_directrix = abs(P[0] - self.directrix_x * self.SCALE)
# 应该相等
```

### 位置规划
- 标题: y = 5.5
- 焦点F: (p/2 * SCALE, 0) + OFFSET
- 准线: x = -p/2 * SCALE + OFFSET[0]
- 定义公式: y = -4.5

### 清理
- FadeOut: title, P_dot, lines, dist_labels
- 保留: F_dot, directrix, definition (移到角落), parabola

---

## Scene 3: 焦点和准线 (6-7秒)
**目的**: 强调焦点和准线的位置关系

### 元素
1. 副标题 "焦点与准线"
2. 焦点F（高亮）
3. 准线l（高亮）
4. 焦准距p标注
5. 坐标标注
6. 说明：F不在l上

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 焦点F放大高亮 | `Indicate(F_dot, scale_factor=1.5)` |
| 1.0s | 显示焦点坐标 | `Write(F_coords)` |
| 1.8s | 准线高亮 | `Indicate(directrix)` |
| 2.4s | 显示准线方程 | `Write(directrix_eq)` |
| 3.2s | 标注焦准距p | `Create(p_line), Write(p_label)` |
| 4.5s | 说明文字 | `FadeIn(explanation)` |
| 5.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 焦点
F = np.array([self.p/2, 0, 0]) * self.SCALE + self.OFFSET

# 准线
directrix_x = -self.p/2

# 焦准距（F到准线的距离）
focal_distance = abs(self.p/2 - (-self.p/2)) = self.p
```

### 位置规划
- 副标题: y = 5.5
- 焦点坐标: F旁边
- 准线方程: 准线旁边
- p标注: F和准线之间
- 说明: y = -5

### 清理
- FadeOut: subtitle, coords, p_line, explanation
- 保留: F_dot, directrix, parabola

---

## Scene 4: 标准方程（y²=2px）(8-9秒)
**目的**: 推导并展示开口向右的标准方程

### 元素
1. 副标题 "标准方程（开口向右）"
2. 坐标系
3. 抛物线（完整，清晰）
4. 标准方程 y² = 2px
5. 参数说明：p > 0
6. 焦点和准线位置公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 创建坐标系 | `Create(axes)` |
| 1.2s | 绘制抛物线（上下对称） | `Create(parabola_upper), Create(parabola_lower)` |
| 2.5s | 显示标准方程 | `Write(standard_eq)` |
| 3.5s | 显示p>0条件 | `Write(p_condition)` |
| 4.5s | 标注焦点公式 | `Write(focus_formula)` |
| 5.5s | 标注准线公式 | `Write(directrix_formula)` |
| 7.0s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 抛物线参数方程
def parabola_upper(x):
    return np.sqrt(2 * self.p * x)

def parabola_lower(x):
    return -np.sqrt(2 * self.p * x)

# x范围：[0, x_max]
x_range = [0, 5]
```

### 位置规划
- 副标题: y = 5.5
- 坐标系中心: y = 1
- 标准方程: y = -3.5
- 参数说明: y = -4.5
- 焦点/准线公式: y = -5.5

### 清理
- FadeOut: subtitle
- 保留: axes, parabola, standard_eq, formulas

---

## Scene 5: 四种开口方向 (8-10秒)
**目的**: 展示抛物线的四种标准方程对比

### 元素
1. 副标题 "四种开口方向"
2. 四个小抛物线（2×2网格）
   - 开口向右：y² = 2px
   - 开口向左：y² = -2px
   - 开口向上：x² = 2py
   - 开口向下：x² = -2py
3. 每个标注方程和焦点/准线位置

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(previous)` |
| 0.5s | 副标题淡入 | `FadeIn(subtitle)` |
| 1.0s | 右抛物线出现 | `Create(parabola_right)` |
| 1.8s | 标注方程 | `Write(eq_right)` |
| 2.4s | 左抛物线出现 | `Create(parabola_left)` |
| 3.0s | 标注方程 | `Write(eq_left)` |
| 3.6s | 上抛物线出现 | `Create(parabola_up)` |
| 4.2s | 标注方程 | `Write(eq_up)` |
| 4.8s | 下抛物线出现 | `Create(parabola_down)` |
| 5.4s | 标注方程 | `Write(eq_down)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 关键计算
```python
# 四个方向的抛物线
# 右: y² = 2px, x ∈ [0, max]
# 左: y² = -2px, x ∈ [min, 0]
# 上: x² = 2py, y ∈ [0, max]
# 下: x² = -2py, y ∈ [min, 0]

# 缩放因子（使四个能放入屏幕）
small_scale = 0.35
positions = {
    "right": UP * 2.5 + LEFT * 2,
    "left": UP * 2.5 + RIGHT * 2,
    "up": DOWN * 2.5 + LEFT * 2,
    "down": DOWN * 2.5 + RIGHT * 2,
}
```

### 位置规划
- 副标题: y = 5.5
- 右上: (−2, 2.5)
- 左上: (2, 2.5)
- 右下: (−2, −2.5)
- 左下: (2, −2.5)

### 清理
- FadeOut: subtitle, four_parabolas
- 准备总结

---

## Scene 6: 参数p的意义 (6-7秒)
**目的**: 解释p对抛物线形状的影响

### 元素
1. 副标题 "参数p的意义"
2. 三个不同p值的抛物线对比
   - p = 1: 较窄
   - p = 2: 中等
   - p = 4: 较宽
3. 说明：p越大，开口越大
4. p是焦准距

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.4s | 创建p=1抛物线 | `Create(parabola_p1)` |
| 1.0s | 标注p=1 | `Write(label_p1)` |
| 1.6s | 创建p=2抛物线 | `Create(parabola_p2)` |
| 2.2s | 标注p=2 | `Write(label_p2)` |
| 2.8s | 创建p=4抛物线 | `Create(parabola_p4)` |
| 3.4s | 标注p=4 | `Write(label_p4)` |
| 4.5s | 说明文字 | `FadeIn(explanation)` |
| 5.5s | 等待 | `Wait(1.0)` |

### 关键计算
```python
# 不同p值的抛物线
def create_parabola(p_value, color, opacity=1.0):
    return FunctionGraph(
        lambda x: np.sqrt(2 * p_value * x),
        x_range=[0, 5],
        color=color
    ).set_opacity(opacity)
```

### 位置规划
- 副标题: y = 5.5
- 三条抛物线重叠显示，颜色不同
- 标签: 各曲线右侧
- 说明: y = -5

### 清理
- FadeOut: subtitle, all_parabolas, labels, explanation

---

## Scene 7: 实际应用 (5-6秒)
**目的**: 展示抛物线的实际应用

### 元素
1. 副标题 "生活中的抛物线"
2. 应用示例（简化图示）
   - 抛物面天线
   - 桥拱
   - 喷泉
3. 说明文字：焦点性质应用

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 副标题淡入 | `FadeIn(subtitle)` |
| 0.5s | 示例1淡入 | `FadeIn(example1)` |
| 1.2s | 示例2淡入 | `FadeIn(example2)` |
| 1.9s | 示例3淡入 | `FadeIn(example3)` |
| 2.8s | 说明文字 | `FadeIn(explanation)` |
| 4.5s | 等待 | `Wait(1.0)` |

### 位置规划
- 副标题: y = 5.5
- 三个示例: 横向排列 y = 1
- 说明: y = -4

### 清理
- FadeOut: all

---

## Scene 8: 总结与关注 (5-6秒)
**目的**: 回顾核心内容，引导关注

### 元素
1. 总结标题
2. 关键公式卡片
   - 定义：|PF| = d
   - y² = 2px: F(p/2, 0), x = -p/2
   - 四种开口
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(summary_title)` |
| 0.4s | 卡片依次滑入 | `card.animate.shift(RIGHT*10)` |
| 2.5s | 作者信息放大 | `Transform(author)` |
| 3.0s | 关注提示 | `FadeIn(follow_text)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 位置规划
- 标题: y = 5
- 卡片: y = 3, 2, 1
- 作者: y = 0
- 关注: y = -2

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| parabola | Scene 1 | Scene 4 | 基本抛物线 |
| F_dot | Scene 2 | Scene 7 | 焦点 |
| directrix | Scene 2 | Scene 7 | 准线 |
| definition | Scene 2 | Scene 8 | 定义公式 |
| axes | Scene 4 | Scene 6 | 坐标系 |
| standard_eq | Scene 4 | Scene 8 | 标准方程 |
| four_parabolas | Scene 5 | Scene 5 | 四种开口 |
| p_comparison | Scene 6 | Scene 6 | p值对比 |
| applications | Scene 7 | Scene 7 | 应用示例 |
| summary_cards | Scene 8 | Scene 8 | 总结卡片 |

---

## 几何验证要点

### 验证1: 抛物线定义
```python
# 对于抛物线上任意点P
dist_PF = np.linalg.norm(P - F)
dist_to_directrix = abs(P[0] - directrix_x)
# 应该相等
assert abs(dist_PF - dist_to_directrix) < epsilon
```

### 验证2: 焦点位置
```python
# y² = 2px
F = (p/2, 0)
directrix_x = -p/2

# 焦准距
focal_distance = F[0] - directrix_x = p/2 - (-p/2) = p
```

### 验证3: 抛物线方程
```python
# 对于点(x, y)在抛物线上
y_squared = y**2
two_px = 2 * p * x
assert abs(y_squared - two_px) < epsilon
```

### 验证4: 四种开口
```python
# 右: y² = 2px, F(p/2, 0), x = -p/2
# 左: y² = -2px, F(-p/2, 0), x = p/2
# 上: x² = 2py, F(0, p/2), y = -p/2
# 下: x² = -2py, F(0, -p/2), y = p/2
```

### 验证5: 边界安全
```python
# 所有元素在安全范围内
# x ∈ [-4, 4], y ∈ [-7, 7]
```

---

## 动画节奏控制

| 阶段 | 节奏 | 原因 |
|------|------|------|
| Scene 1 | 快 | 吸引注意 |
| Scene 2 | 慢 | 核心定义，需理解 |
| Scene 3 | 中 | 焦点准线讲解 |
| Scene 4 | 中慢 | 标准方程推导 |
| Scene 5 | 中 | 四种开口对比 |
| Scene 6 | 快 | p值影响 |
| Scene 7 | 快 | 应用举例 |
| Scene 8 | 中 | 总结回顾 |

---

## LaTeX 公式列表

```python
formulas = {
    # 定义
    "definition": r"|PF| = d",
    
    # 标准方程
    "standard_right": r"y^2 = 2px",
    "standard_left": r"y^2 = -2px",
    "standard_up": r"x^2 = 2py",
    "standard_down": r"x^2 = -2py",
    
    # 焦点
    "focus_right": r"F(\frac{p}{2}, 0)",
    "focus_left": r"F(-\frac{p}{2}, 0)",
    "focus_up": r"F(0, \frac{p}{2})",
    "focus_down": r"F(0, -\frac{p}{2})",
    
    # 准线
    "directrix_right": r"x = -\frac{p}{2}",
    "directrix_left": r"x = \frac{p}{2}",
    "directrix_up": r"y = -\frac{p}{2}",
    "directrix_down": r"y = \frac{p}{2}",
    
    # 条件
    "p_condition": r"p > 0",
}
```

**注意**: 所有中文使用 `Text()` 单独创建！

---

## 颜色语义映射

| 颜色 | 用途 | Hex |
|------|------|-----|
| 红色 | 抛物线主体 | #e74c3c |
| 橙色 | 焦点 | #f39c12 |
| 蓝色 | 准线 | #3498db |
| 绿色 | 距离线 | #2ecc71 |
| 粉色 | 动点P | #e91e63 |
| 紫色 | 对称轴 | #9b59b6 |
| 黄色 | 高亮提示 | YELLOW |
| 灰色 | 辅助元素 | GRAY_B |

---

## 完成标准

- [x] 场景覆盖所有核心知识点
- [x] 几何元素位置精确计算
- [x] 动画节奏合理分配
- [x] LaTeX公式无中文字符
- [x] 颜色配置语义化
- [x] 元素生命周期明确
- [x] 边界检查通过
- [x] 验证机制完善
- [x] 实际应用展示