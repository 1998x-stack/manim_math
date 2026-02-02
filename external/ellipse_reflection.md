# 椭圆焦点反射性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 中等（高中物理/数学）

## 颜色配置
```python
COLOR_ELLIPSE = "#3498db"        # 蓝色 - 椭圆主体
COLOR_FOCUS = "#e74c3c"          # 红色 - 焦点
COLOR_LIGHT_PATH = "#f39c12"     # 橙色 - 光线路径
COLOR_TANGENT = "#2ecc71"        # 绿色 - 切线
COLOR_NORMAL = "#9b59b6"         # 紫色 - 法线
COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
```

## 几何预计算清单

| 元素 | 计算公式 | 存储变量 | 备注 |
|------|---------|---------|------|
| 椭圆中心 | ORIGIN | self.center | 坐标原点 |
| 半长轴 | 3.0 | self.a | 长轴半径 |
| 半短轴 | 2.0 | self.b | 短轴半径 |
| 焦距 | c = √(a²-b²) | self.c | 焦点到中心距离 |
| 左焦点 | (-c, 0, 0) | self.F1 | 左侧焦点 |
| 右焦点 | (c, 0, 0) | self.F2 | 右侧焦点 |
| 反射点P | 椭圆参数方程 | self.P | t=60° |
| 切线方向 | dP/dt | self.tangent_dir | 椭圆在P点切线 |
| 法线方向 | 垂直于切线 | self.normal_dir | 椭圆在P点法线 |
| 入射角 | ∠(F1P, 法线) | self.angle_in | 入射角 |
| 反射角 | ∠(F2P, 法线) | self.angle_out | 反射角 |

## 椭圆参数方程
```python
x(t) = a * cos(t)
y(t) = b * sin(t)

切线方向: (-a*sin(t), b*cos(t))
法线方向: (b*cos(t), a*sin(t))
```

---

## Scene 1: 开场钩子 (0-5秒)

**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题
3. 椭圆 + 两个焦点
4. 多条光线动画

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 椭圆创建 | `Create(ellipse)` | 1.0s |
| 2.1s | 焦点闪烁 | `Flash(F1), Flash(F2)` | 0.5s |
| 2.6s | 多条光线演示 | `Create(light_paths)` | 1.5s |
| 4.1s | 等待观察 | `Wait(0.9)` | 0.9s |

### 钩子文字
"为什么椭圆镜面能汇聚光线?"

### 清理
- FadeOut: hook_text
- 保留: ellipse, F1, F2, author_info
- 移除: 多条光线

---

## Scene 2: 椭圆定义 (5-12秒)

**目的**: 介绍椭圆基本性质

### 元素
1. 标题："椭圆的定义"
2. 椭圆上一点P
3. 到两焦点的连线
4. 距离标注
5. 公式: |PF1| + |PF2| = 2a

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 5.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 5.5s | 点P出现 | `FadeIn(P_dot)` | 0.3s |
| 5.8s | 绘制PF1 | `Create(line_PF1)` | 0.5s |
| 6.3s | 绘制PF2 | `Create(line_PF2)` | 0.5s |
| 6.8s | 标注距离 | `Write(dist_labels)` | 0.6s |
| 7.4s | 公式出现 | `Write(formula)` | 0.8s |
| 8.2s | 点P沿椭圆移动 | `MoveAlongPath(P, ellipse)` | 2.5s |
| 10.7s | 强调"距离和不变" | `Indicate(formula)` | 0.6s |
| 11.3s | 等待 | `Wait(0.7)` | 0.7s |

### 公式内容
```latex
|PF_1| + |PF_2| = 2a = \text{常数}
```

### 清理
- FadeOut: title, line_PF1, line_PF2, dist_labels, formula
- 保留: ellipse, F1, F2, P_dot

---

## Scene 3: 反射定律介绍 (12-20秒)

**目的**: 引入反射定律基础知识

### 元素
1. 标题："反射定律"
2. 椭圆在P点的切线
3. 法线（垂直于切线）
4. 入射光线（从F1到P）
5. 反射光线（从P到F2）
6. 入射角和反射角标注

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 12.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 12.5s | 绘制切线 | `Create(tangent_line)` | 0.6s |
| 13.1s | 绘制法线 | `Create(normal_line)` | 0.6s |
| 13.7s | 光从F1到P | `Create(incident_ray)` | 0.7s |
| 14.4s | 光从P反射到F2 | `Create(reflected_ray)` | 0.7s |
| 15.1s | 标注入射角θ₁ | `Write(angle_in_label)` | 0.5s |
| 15.6s | 标注反射角θ₂ | `Write(angle_out_label)` | 0.5s |
| 16.1s | 公式: θ₁ = θ₂ | `Write(law_formula)` | 0.8s |
| 16.9s | 角度动画验证 | `Flash(angles)` | 0.6s |
| 17.5s | 等待 | `Wait(0.5)` | 0.5s |

### 公式内容
```latex
\theta_{\text{入}} = \theta_{\text{反}}
```

### 清理
- FadeOut: title, law_formula
- 保留: ellipse, F1, F2, P, tangent_line, normal_line, rays, angles

---

## Scene 4: 几何证明 (20-35秒)

**目的**: 证明椭圆反射性质

### 元素
1. 标题："为什么反射必过另一焦点?"
2. 切线性质标注
3. 等腰三角形构造
4. 角度相等标注

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 20.0s | 标题淡入 | `FadeIn(title)` | 0.6s |
| 20.6s | 说明文字1 | `FadeIn(explain_1)` | 0.8s |
| 21.4s | 高亮PF1和切线夹角α | `Indicate(angle_alpha)` | 0.6s |
| 22.0s | 说明文字2 | `FadeIn(explain_2)` | 0.8s |
| 22.8s | 高亮PF2和切线夹角β | `Indicate(angle_beta)` | 0.6s |
| 23.4s | 椭圆切线性质 | `Write(property_text)` | 1.0s |
| 24.4s | 高亮α = β | `Flash(equal_angles)` | 0.8s |
| 25.2s | 推导入射角=反射角 | `Write(derivation)` | 1.5s |
| 26.7s | 箭头指向结论 | `GrowArrow(conclusion_arrow)` | 0.5s |
| 27.2s | 结论高亮 | `Write(conclusion)` | 1.2s |
| 28.4s | 等待理解 | `Wait(1.6)` | 1.6s |

### 关键说明文字
```
椭圆切线性质:
∠(PF₁, 切线) = ∠(PF₂, 切线)
```

### 清理
- FadeOut: title, explain texts, property_text, derivation
- 保留: ellipse, F1, F2, P, tangent, rays

---

## Scene 5: 费马原理 (35-50秒)

**目的**: 从物理角度理解

### 元素
1. 标题："费马原理"
2. 多条可能路径
3. 路径长度标注
4. 高亮最短/稳定路径

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 35.0s | 标题淡入 | `FadeIn(title)` | 0.6s |
| 35.6s | 费马原理说明 | `FadeIn(fermat_text)` | 1.0s |
| 36.6s | 绘制多条路径 | `Create(path_group)` | 1.5s |
| 38.1s | 标注路径长度 | `Write(length_labels)` | 0.8s |
| 38.9s | 所有路径长度相同! | `Indicate(equal_lengths)` | 0.8s |
| 39.7s | 高亮反射定律路径 | `path.set_color(YELLOW)` | 0.5s |
| 40.2s | 说明：唯一稳定路径 | `FadeIn(stable_text)` | 1.0s |
| 41.2s | 其他路径淡化 | `FadeOut(other_paths)` | 0.6s |
| 41.8s | 结论 | `Write(conclusion)` | 1.2s |
| 43.0s | 等待 | `Wait(2.0)` | 2.0s |

### 说明文字
```
费马原理: 光沿所有可能路径中的稳定路径传播
椭圆上: |PF₁| + |PF₂| = 2a (所有点相同!)
```

### 清理
- FadeOut: title, fermat_text, paths, labels, conclusion
- 保留: ellipse, F1, F2

---

## Scene 6: 应用与片尾 (50-65秒)

**目的**: 展示应用，引导关注

### 元素
1. 标题："实际应用"
2. 多束光线汇聚动画
3. 应用场景文字
4. 作者信息放大
5. 关注提示

### 动画序列

| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 50.0s | 标题淡入 | `FadeIn(title)` | 0.5s |
| 50.5s | 多束光线演示 | `Create(light_beams)` | 2.0s |
| 52.5s | 应用文字1 | `FadeIn(app_1)` | 0.6s |
| 53.1s | 应用文字2 | `FadeIn(app_2)` | 0.6s |
| 53.7s | 应用文字3 | `FadeIn(app_3)` | 0.6s |
| 54.3s | 清理图形 | `FadeOut(all_geometry)` | 0.8s |
| 55.1s | 作者信息放大 | `Transform(author)` | 0.8s |
| 55.9s | 关注提示 | `FadeIn(follow_text)` | 0.6s |
| 56.5s | 装饰动画 | `Create(decorations)` | 0.8s |
| 57.3s | 等待 | `Wait(2.7)` | 2.7s |

### 应用场景
```
1. 椭圆形反射镜 - 医疗碎石
2. 耳语廊 - 建筑声学
3. 天文望远镜 - 光学系统
```

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终保留在顶部 |
| ellipse | Scene 1 | Scene 6 | 主体图形 |
| F1, F2 | Scene 1 | Scene 6 | 焦点 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| P_dot | Scene 2 | Scene 5 | 反射点 |
| tangent_line | Scene 3 | Scene 5 | 切线 |
| normal_line | Scene 3 | Scene 5 | 法线 |
| incident_ray | Scene 3 | Scene 5 | 入射光线 |
| reflected_ray | Scene 3 | Scene 5 | 反射光线 |
| multi_paths | Scene 5 | Scene 5 | 多条路径 |
| light_beams | Scene 6 | Scene 6 | 应用演示 |

---

## 几何验证要点

### 验证1: 椭圆焦点位置
```python
c = sqrt(a^2 - b^2)
assert abs(c - sqrt(self.a**2 - self.b**2)) < 1e-6
```

### 验证2: 点P在椭圆上
```python
assert abs(P[0]**2/a**2 + P[1]**2/b**2 - 1) < 1e-6
```

### 验证3: 切线垂直于法线
```python
dot_product = tangent · normal
assert abs(dot_product) < 1e-6
```

### 验证4: 入射角等于反射角
```python
angle_in = angle(F1P, normal)
angle_out = angle(PF2, normal)
assert abs(angle_in - angle_out) < 1e-6
```

### 验证5: 距离和恒定
```python
dist_sum = |PF1| + |PF2|
assert abs(dist_sum - 2*a) < 1e-6
```

---

## 动画节奏总结

- **快节奏**: Scene 1 (钩子), Scene 6 (应用)
- **中速**: Scene 2 (定义), Scene 3 (反射定律)
- **慢节奏**: Scene 4 (证明), Scene 5 (费马原理)

总时长约 60-65 秒，适合 TikTok 短视频。