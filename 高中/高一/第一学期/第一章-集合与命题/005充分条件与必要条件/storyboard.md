# 充分条件与必要条件 - 动画分镜脚本

## 元信息
- 目标时长: 60-90 秒
- 场景数量: 5 个
- 难度等级: 中等
- 针对年级: 高一
- 章节: 第一章 集合与命题

## 颜色配置
```python
COLOR_LOGIC = "#3498db"        # 蓝色 - 逻辑关系
COLOR_SUFFICIENT = "#e74c3c"   # 红色 - 充分条件
COLOR_NECESSARY = "#2ecc71"    # 绿色 - 必要条件
COLOR_EQUIVALENT = "#f39c12"   # 橙色 - 充要条件
COLOR_SET = "#9b59b6"          # 紫色 - 集合关系
COLOR_AUXILIARY = GRAY_B       # 辅助元素颜色
COLOR_HIGHLIGHT = YELLOW       # 高亮颜色
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 命题P集合中心 | 由逻辑决定 | self.set_P |
| 命题Q集合中心 | 由逻辑决定 | self.set_Q |
| 集合半径 | 设定固定值 | self.radius |

---

## Scene 1: 开场介绍 (4-5秒)
**目的**: 引出充分条件与必要条件的概念

### 元素
1. 作者标识 (顶部小字)
2. 主题标题
3. 核心概念介绍

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 主题标题书写 | `Write(title)` |
| 1.1s | 副标题出现 | `FadeIn(subtitle)` |
| 2.1s | 核心概念出现 | `Write(concept)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 元素
- 作者: `Text("上海初高中数学直通车 @emptyandcalm", ...)`
- 标题: `Text("充分条件与必要条件", ...)`
- 副标题: `Text("逻辑推理的重要概念", ...)`
- 概念: `MathTex(r"p \Rightarrow q")`

### 清理
- 保留: 标题、副标题

---

## Scene 2: 充分条件解释 (15-20秒)
**目的**: 解释什么是充分条件，p是q的充分条件

### 元素
1. 命题P的集合表示
2. 命题Q的集合表示
3. 集合关系可视化 (P⊆Q)
4. 文字解释

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理前一幕 | `FadeOut(...)` |
| 0.2s | 显示P集合 | `Create(set_P)` |
| 1.0s | 显示Q集合 | `Create(set_Q)` |
| 2.0s | 调整位置展示P⊆Q关系 | `set_P.animate.move_to(...)` |
| 3.0s | 添加箭头表示蕴含关系 | `Create(arrow)` |
| 4.0s | 添加充分条件标签 | `Write(sufficient_label)` |
| 5.0s | 添加定义文字 | `Write(def_sufficient)` |
| 6.0s | 高亮展示 | `Indicate(...) or Flash(...)` |

### 元素
- P集合: `Circle(color=COLOR_SUFFICIENT, ...)`
- Q集合: `Circle(color=COLOR_LOGIC, ...)`
- 箭头: `Arrow(...)`
- 标签: `Text("充分条件", ...)`
- 定义: `Text("p是q的充分条件", ...)`

### 清理
- 保留: 集合图示、箭头、部分标签

---

## Scene 3: 必要条件解释 (15-20秒)
**目的**: 解释什么是必要条件，q是p的必要条件

### 元素
1. 之前的集合关系
2. 必要条件的文字说明
3. 集合关系的另一种解读

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 保留之前元素 | - |
| 0.2s | 强调P→Q关系 | `Indicate(arrow)` |
| 1.0s | 添加q是必要条件标签 | `Write(necessary_label)` |
| 2.0s | 添加定义文字 | `Write(def_necessary)` |
| 3.0s | 添加"有它一定行，没它一定不行"说明 | `Write(explanation)` |
| 4.0s | 举例说明 | `Transform(...) or Write(example)` |
| 5.0s | 高亮关键部分 | `Flash(...) or ApplyWave(...)` |

### 元素
- 必要条件标签: `Text("必要条件", ...)`
- 定义: `Text("q是p的必要条件", ...)`
- 解释: `Text("有它一定行，没它一定不行", ...)`
- 例子: `MathTex(r"若x > 2, 则x > 0")`

### 清理
- 保留: 集合图示、部分关键标签

---

## Scene 4: 充要条件讲解 (15-20秒)
**目的**: 解释充要条件，p⟺q的情况

### 元素
1. 两个相等的集合 (P=Q)
2. 双向箭头表示等价关系
3. 充要条件的定义

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 调整现有集合 | `set_P.animate..., set_Q.animate...` |
| 1.0s | 展示P=Q的情况 | `Transform(set_Q, equal_set)` |
| 2.0s | 添加双向箭头 | `Create(double_arrow)` |
| 3.0s | 添加充要条件标签 | `Write(equivalent_label)` |
| 4.0s | 添加等价符号 | `Write(symbol_equivalent)` |
| 5.0s | 添加充要条件定义 | `Write(def_equivalent)` |
| 6.0s | 高亮等价关系 | `Flash(...) or ApplyWave(...)` |

### 元素
- 相等集合: `Circle(...) 位置重合`
- 双向箭头: `DoubleArrow(...)`
- 标签: `Text("充要条件", ...)`
- 符号: `MathTex(r"p \iff q")`
- 定义: `Text("充分必要条件", ...)`

### 清理
- 保留: 关键视觉元素

---

## Scene 5: 总结与应用 (10-15秒)
**目的**: 总结三种条件，并给出实际应用

### 元素
1. 三种条件对比表
2. 实际应用场景
3. 片尾关注信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理之前元素 | `FadeOut(...)` |
| 0.2s | 显示条件对比表 | `Write(conditions_table)` |
| 2.0s | 展示实际例子 | `Write(real_example)` |
| 3.5s | 添加学习建议 | `Write(advice)` |
| 5.0s | 作者信息出现 | `FadeIn(final_author)` |
| 6.0s | 关注提示 | `Write(follow_up)` |
| 7.0s | 最终效果 | `Indicate(...) or Flash(...)` |
| 8.0s | 结束 | `Wait(1.0)` |

### 元素
- 对比表: `Table(...)`
- 例子: `MathTex(r"x > 2 \Rightarrow x > 0")`
- 建议: `Text("理解集合关系是关键", ...)`
- 作者信息: `Text("@emptyandcalm", ...)`
- 关注提示: `Text("关注我，获得更多数学技巧!", ...)`

### 清理
- 全部元素淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| 标题 | Scene 1 | Scene 5 | 主标题 |
| 集合P | Scene 2 | Scene 5 | 命题P的集合表示 |
| 集合Q | Scene 2 | Scene 5 | 命题Q的集合表示 |
| 箭头 | Scene 2 | Scene 5 | 逻辑关系箭头 |
| 条件标签 | Scene 2-4 | Scene 5 | 充分/必要/充要标签 |
| 作者信息 | Scene 1 | Scene 5 | 作者标识 |
