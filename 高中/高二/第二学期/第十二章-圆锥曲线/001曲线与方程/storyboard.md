# 曲线与方程 - 动画分镜脚本

## 元信息
- 目标时长: 60-75秒
- 场景数量: 6个
- 难度等级: 中等
- 知识点: 曲线与方程的关系、充要条件

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 曲线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 点
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
COLOR_GRID = "#34495e"         # 深灰 - 网格
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | ORIGIN | self.circle_center |
| 圆半径 | 2.0 | self.circle_radius |
| 示例点1 | 圆上点(√2, √2) | self.point_on_circle |
| 示例点2 | 圆外点(3, 0) | self.point_outside |
| 坐标系范围 | x∈[-4,4], y∈[-3,3] | self.axes_config |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，引出核心问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题："如何用方程表示一个图形？"
3. 一个圆形逐渐形成

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question, run_time=0.8)` |
| 1.2s | 圆形创建 | `Create(circle, run_time=1.5)` |
| 2.8s | 等待 | `self.wait(1.2)` |

### 清理
- FadeOut: hook_question
- 保留: circle, author_info

---

## Scene 2: 建立坐标系 (6秒)
**目的**: 引入坐标系，准备讨论方程

### 元素
1. 坐标轴 Axes
2. 坐标轴标签
3. 圆在坐标系中

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标轴创建 | `Create(axes, run_time=1.2)` |
| 1.2s | 圆移动到坐标系 | `circle.animate.move_to(ORIGIN)` |
| 2.2s | 说明文字 | `FadeIn(explanation)` |
| 3.2s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: explanation
- 保留: axes, circle

---

## Scene 3: 引入方程概念 (10秒)
**目的**: 展示"圆的方程"

### 元素
1. 圆的方程 x² + y² = 4
2. 方程高亮动画
3. 连接圆与方程的视觉元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 方程淡入 | `FadeIn(equation, shift=UP*0.3)` |
| 1.0s | 方程与圆同时高亮 | `circle.animate.set_color(HIGHLIGHT)` |
| 2.0s | 标题"曲线的方程" | `Write(title)` |
| 3.5s | 等待理解 | `self.wait(2.5)` |

### 清理
- Transform: equation移到顶部
- 保留: axes, circle, equation

---

## Scene 4: 充要条件 - 正向 (12秒)
**目的**: 点在曲线上 → 坐标满足方程

### 元素
1. 圆上取点 P(√2, √2)
2. 验证：代入方程
3. 计算过程动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 点P出现在圆上 | `FadeIn(point_P, scale=0.5)` |
| 0.5s | 标注坐标 | `Write(coordinates)` |
| 1.5s | "代入方程"文字 | `FadeIn(substitute_text)` |
| 2.5s | 计算步骤1 | `Write(calc_step1)` |
| 4.0s | 计算步骤2 | `TransformMatchingTex(step1, step2)` |
| 5.5s | 结论"满足!" | `FadeIn(check_mark, scale=1.5)` |
| 6.5s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: 所有计算步骤
- 保留: axes, circle, point_P

---

## Scene 5: 充要条件 - 反向 (12秒)
**目的**: 坐标满足方程 → 点在曲线上

### 元素
1. 先给出满足方程的坐标 (√2, √2)
2. 在坐标系中定位该点
3. 验证在圆上

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 给出坐标 | `Write(given_coords)` |
| 1.0s | 验证满足方程 | `Write(verify_equation)` |
| 2.5s | 在坐标系中描点 | `FadeIn(new_point)` |
| 3.5s | 点移动到圆上 | `new_point.animate.move_to(circle_point)` |
| 4.5s | 高亮重合 | `Flash(new_point)` |
| 5.5s | 结论文字 | `FadeIn(conclusion)` |
| 7.0s | 等待 | `self.wait(2.0)` |

### 清理
- FadeOut: 所有验证步骤
- 保留: axes, circle

---

## Scene 6: 反例演示 (8秒)
**目的**: 展示不在曲线上的点不满足方程

### 元素
1. 圆外点 Q(3, 0)
2. 代入方程，不满足
3. 用红叉表示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 点Q出现在圆外 | `FadeIn(point_Q)` |
| 1.0s | 代入验证 | `Write(verify_Q)` |
| 2.0s | 9 ≠ 4 | `Write(inequality, color=RED)` |
| 3.0s | 红叉出现 | `FadeIn(cross_mark, scale=1.5)` |
| 4.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: point_Q, 验证步骤
- 保留: axes, circle

---

## Scene 7: 总结定义 (10秒)
**目的**: 完整呈现曲线方程的定义

### 元素
1. 完整定义框
2. 充要条件符号 ⟺
3. 关键词高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 定义框淡入 | `FadeIn(definition_box)` |
| 1.0s | 关键词依次高亮 | `AnimatedText` |
| 3.0s | 双向箭头动画 | `Create(double_arrow)` |
| 5.0s | 等待理解 | `self.wait(2.5)` |

### 清理
- FadeOut: definition_box
- 保留: axes, circle

---

## Scene 8: 片尾 (6秒)
**目的**: 关注引导

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清空场景 | `FadeOut(axes, circle)` |
| 0.6s | 作者名放大 | `author_info.animate.scale(2)` |
| 1.6s | 关注文字 | `FadeIn(follow_text)` |
| 2.6s | 装饰动画 | `点阵闪烁` |
| 4.0s | 等待 | `self.wait(2.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 始终保留 |
| circle | Scene 1 | Scene 7 | 主要图形 |
| axes | Scene 2 | Scene 7 | 坐标系 |
| equation | Scene 3 | Scene 7 | 方程式 |
| point_P | Scene 4 | Scene 4 | 示例点 |
| point_Q | Scene 6 | Scene 6 | 反例点 |
| definition_box | Scene 7 | Scene 7 | 定义框 |

---

## 注意事项
1. **数学准确性**: 圆的方程 x² + y² = 4，半径 r = 2
2. **点坐标精确**: (√2, √2) ≈ (1.414, 1.414)，需要精确到小数
3. **边界安全**: 圆半径2，坐标系范围应为 [-4, 4] × [-3, 3]
4. **动画节奏**: 关键概念（充要条件）多停留 2-2.5秒
5. **颜色一致性**: 满足用绿色✓，不满足用红色✗