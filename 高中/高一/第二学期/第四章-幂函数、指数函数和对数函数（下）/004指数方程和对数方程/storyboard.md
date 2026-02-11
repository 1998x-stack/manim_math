# 指数方程和对数方程 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 高一
- 知识点: 指数方程和对数方程

## 颜色配置
```python
COLOR_EXPONENTIAL = "#e74c3c"     # 红色 - 指数函数
COLOR_LOGARITHM = "#3498db"       # 蓝色 - 对数函数
COLOR_SOLUTION = "#2ecc71"        # 绿色 - 解
COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
COLOR_WARNING = "#f39c12"         # 橙色 - 警告/验证
```

## 几何/函数预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 坐标系中心 | ORIGIN + DOWN*1 | self.axes_center |
| 指数函数 2^x | lambda x: 2**x | - |
| 对数函数 log_2(x) | lambda x: np.log2(x) | - |
| 交点 (2^x = 4) | x = 2 | self.solution_exp |
| 交点 (log_2(x) = 3) | x = 8 | self.solution_log |
| 坐标轴范围 | x: [-1, 5], y: [-1, 10] | self.x_range, self.y_range |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住注意力，引出主题

### 元素
1. 作者信息 (顶部)
2. 钩子问题 "2^x = 8，x = ?"
3. 快速闪烁的问号

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.5s | 问号闪烁 | `Flash(question_mark, color=YELLOW)` |
| 2.5s | 暂停思考 | `Wait(1.0)` |
| 3.5s | 淡出钩子 | `FadeOut(hook_question)` |

### 清理
- FadeOut: hook_question, question_mark
- 保留: author_info

---

## Scene 2: 指数方程定义 (8秒)
**目的**: 介绍指数方程的概念

### 元素
1. 标题 "指数方程"
2. 定义文字
3. 示例方程 2^x = 8
4. 高亮指数位置

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 定义文字淡入 | `FadeIn(definition)` |
| 2.0s | 方程书写 | `Write(equation)` |
| 3.0s | 指数高亮 | `Indicate(exponent, color=YELLOW)` |
| 5.0s | 等待理解 | `Wait(2.0)` |
| 7.0s | 清理 | `FadeOut(title, definition)` |

### 清理
- FadeOut: title, definition
- 保留: equation (移到顶部)

---

## Scene 3: 图像法求解指数方程 (12秒)
**目的**: 通过函数图像可视化求解过程

### 元素
1. 坐标系 Axes
2. 指数函数曲线 y = 2^x (红色)
3. 水平线 y = 8 (蓝色虚线)
4. 交点 Dot
5. 解的标注 x = 3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标系 | `Create(axes)` |
| 1.0s | 绘制 y=2^x | `Create(exp_graph)` |
| 2.5s | 标注函数名 | `Write(exp_label)` |
| 3.5s | 绘制 y=8 线 | `Create(horizontal_line)` |
| 5.0s | 标注 y=8 | `Write(y8_label)` |
| 6.0s | 标记交点 | `FadeIn(intersection_dot, scale=0.5)` |
| 7.0s | 交点闪光 | `Flash(intersection_dot)` |
| 8.0s | 垂线到x轴 | `Create(vertical_line)` |
| 9.0s | 标注 x=3 | `Write(solution_label)` |
| 11.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: horizontal_line, vertical_line, y8_label
- 保留: axes, exp_graph, exp_label, intersection_dot, solution_label

---

## Scene 4: 同底数法 (10秒)
**目的**: 展示同底数比较指数的方法

### 元素
1. 方程 2^x = 8
2. 变换箭头
3. 方程 2^x = 2^3
4. 结论 x = 3
5. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原方程显示 | `Write(eq1)` |
| 1.5s | 提示文字 | `FadeIn(hint_text)` |
| 2.5s | 变换箭头 | `GrowArrow(arrow)` |
| 3.5s | 新方程 | `TransformMatchingTex(eq1, eq2)` |
| 5.0s | 框选底数 | `Create(box_base)` |
| 6.5s | 结论 | `Write(conclusion)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: eq1, eq2, arrow, hint_text, box_base
- 保留: conclusion

---

## Scene 5: 对数方程定义 (8秒)
**目的**: 介绍对数方程的概念

### 元素
1. 标题 "对数方程"
2. 定义文字
3. 示例方程 log₂(x) = 3
4. 高亮真数位置

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理前面内容 | `FadeOut(all_previous)` |
| 0.8s | 标题写入 | `Write(title)` |
| 1.6s | 定义文字淡入 | `FadeIn(definition)` |
| 3.0s | 方程书写 | `Write(log_equation)` |
| 4.0s | 真数高亮 | `Indicate(true_value, color=YELLOW)` |
| 6.0s | 等待理解 | `Wait(1.5)` |
| 7.5s | 清理 | `FadeOut(title, definition)` |

### 清理
- FadeOut: title, definition
- 保留: log_equation (移到顶部)

---

## Scene 6: 图像法求解对数方程 (12秒)
**目的**: 通过函数图像可视化对数方程求解

### 元素
1. 坐标系 Axes
2. 对数函数曲线 y = log₂(x) (蓝色)
3. 水平线 y = 3 (红色虚线)
4. 交点 Dot
5. 解的标注 x = 8

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标系 | `Create(axes)` |
| 1.0s | 绘制 y=log₂(x) | `Create(log_graph)` |
| 2.5s | 标注函数名 | `Write(log_label)` |
| 3.5s | 绘制 y=3 线 | `Create(horizontal_line)` |
| 5.0s | 标注 y=3 | `Write(y3_label)` |
| 6.0s | 标记交点 | `FadeIn(intersection_dot, scale=0.5)` |
| 7.0s | 交点闪光 | `Flash(intersection_dot)` |
| 8.0s | 垂线到x轴 | `Create(vertical_line)` |
| 9.0s | 标注 x=8 | `Write(solution_label)` |
| 11.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: horizontal_line, vertical_line, y3_label
- 保留: axes, log_graph, log_label, intersection_dot, solution_label

---

## Scene 7: 验根提醒 + 片尾 (8秒)
**目的**: 强调验根的重要性，引导关注

### 元素
1. 警告框
2. 验根条件列表
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理图像 | `FadeOut(axes, graphs, dots)` |
| 0.6s | 警告框出现 | `FadeIn(warning_box, scale=1.1)` |
| 1.2s | 条件列表 | `Write(conditions)` |
| 3.5s | 等待 | `Wait(1.5)` |
| 5.0s | 淡出警告 | `FadeOut(warning_box, conditions)` |
| 5.6s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 6.4s | 关注提示 | `FadeIn(follow_text)` |
| 7.4s | 等待结束 | `Wait(1.0)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持在顶部 |
| hook_question | Scene 1 | Scene 1 | 开场钩子 |
| exp_equation | Scene 2 | Scene 4 | 指数方程 |
| axes_exp | Scene 3 | Scene 4 | 指数图坐标系 |
| exp_graph | Scene 3 | Scene 4 | 指数函数曲线 |
| log_equation | Scene 5 | Scene 6 | 对数方程 |
| axes_log | Scene 6 | Scene 7 | 对数图坐标系 |
| log_graph | Scene 6 | Scene 7 | 对数函数曲线 |
| warning_box | Scene 7 | Scene 7 | 验根提醒 |

---

## 坐标系配置

### 指数方程坐标系
```python
axes_exp = Axes(
    x_range=[-1, 5, 1],
    y_range=[-1, 10, 2],
    x_length=6,
    y_length=7,
    axis_config={
        "include_numbers": True,
        "font_size": 20,
    }
).move_to(DOWN * 0.5)
```

### 对数方程坐标系
```python
axes_log = Axes(
    x_range=[-1, 10, 2],
    y_range=[-1, 5, 1],
    x_length=7,
    y_length=6,
    axis_config={
        "include_numbers": True,
        "font_size": 20,
    }
).move_to(DOWN * 0.5)
```

---

## 边界检查清单
- [ ] 作者信息在 y = 7
- [ ] 标题在 y ∈ [5, 6]
- [ ] 主内容在 y ∈ [-3, 5]
- [ ] 说明文字在 y ∈ [-5, -3]
- [ ] 所有元素 x ∈ [-4, 4]
- [ ] 坐标系不超出安全边界

---

## 字体大小规范
| 元素类型 | 字体大小 |
|---------|---------|
| 作者信息 | 20 |
| 场景标题 | 36 |
| 副标题/定义 | 24 |
| 方程公式 | 28 |
| 坐标轴标签 | 20 |
| 说明文字 | 22 |
| 警告文字 | 26 |

---

## 时间轴总览
```
0-4s:   开场钩子
4-12s:  指数方程定义
12-24s: 指数方程图像求解
24-34s: 同底数法
34-42s: 对数方程定义
42-54s: 对数方程图像求解
54-62s: 验根提醒 + 片尾
总计: ~62秒
```