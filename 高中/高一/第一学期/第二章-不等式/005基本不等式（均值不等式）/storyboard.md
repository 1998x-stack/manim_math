# 基本不等式（均值不等式） - 动画分镜脚本

## 元信息
- 目标时长: 45-60 秒
- 场景数量: 6 个
- 难度等级: 中等
- 目标观众: 高一学生

## 颜色配置
```python
COLOR_ARITHMETIC_MEAN = BLUE
COLOR_GEOMETRIC_MEAN = GREEN
COLOR_HARMONIC_MEAN = PURPLE
COLOR_QUADRATIC_MEAN = ORANGE
COLOR_AUXILIARY = GRAY_B
BACKGROUND_COLOR = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 点A | (0, 0) | self.point_A |
| 点B | (a, 0) | self.point_B |
| 点C | (a, b) | self.point_C |
| 点D | (0, b) | self.point_D |
| 算术平均数 | (a+b)/2 | self.arithmetic_mean |
| 几何平均数 | √(ab) | self.geometric_mean |
| 调和平均数 | 2ab/(a+b) | self.harmonic_mean |
| 平方平均数 | √((a²+b²)/2) | self.quadratic_mean |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出基本不等式

### 元素
1. 作者标识 (顶部小字)
2. 主标题 (基本不等式（均值不等式）)
3. 钩子问题 ("为什么算术平均数总是大于等于几何平均数？")

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.1s | 钩子问题出现 | `Write(hook_question)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_question
- 保留: title, author_info

---

## Scene 2: 算术平均数与几何平均数 (6-8秒)
**目的**: 直观展示算术平均数与几何平均数

### 元素
1. 数轴
2. 两个正数a和b的表示
3. 算术平均数位置标记
4. 几何平均数位置标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 绘制数轴 | `Create(number_line)` |
| 0.5s | 标记点a和b | `Dot(point_a), Dot(point_b), Write(labels)` |
| 1.5s | 计算并标记算术平均数 | `Dot(arithmetic_pos), Write(arithmetic_label)` |
| 2.5s | 计算并标记几何平均数 | `Dot(geometric_pos), Write(geometric_label)` |
| 3.5s | 用线段比较两者大小 | `Line(arithmetic_pos, geometric_pos)` |
| 4.5s | 显示不等式 | `Write(inequality: (a+b)/2 ≥ √(ab))` |

### 清理
- 保留: number_line, arithmetic_dot, geometric_dot

---

## Scene 3: 几何解释 - 矩形与正方形 (8-10秒)
**目的**: 用矩形与正方形面积解释不等式

### 元素
1. 矩形 (边长a和b)
2. 靣应的正方形 (边长√(ab))
3. 靣应的正方形 (边长(a+b)/2)
4. 靣积比较

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 保持数轴显示 | `Keep(number_line)` |
| 0.5s | 创建矩形 | `Rectangle(width=a, height=b)` |
| 1.5s | 创建面积相等的正方形 | `Square(side_length=sqrt(a*b))` |
| 2.5s | 创建边长相等的正方形 | `Square(side_length=(a+b)/2)` |
| 3.5s | 比较面积 | `SurroundingRectangle` for areas |
| 4.5s | 解释几何意义 | `Write(geometric_explanation)` |

### 清理
- 保留: rectangles_comparison

---

## Scene 4: 代数证明 (6-8秒)
**目的**: 简单展示代数证明过程

### 元素
1. 代数推导步骤
2. 关键变形过程
3. 结论确认

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清理前一场景 | `FadeOut(previous_elements)` |
| 0.5s | 显示起始公式 | `Write(starting_formula: (a-b)² ≥ 0)` |
| 1.5s | 展开平方 | `Transform(starting, expanded)` |
| 2.5s | 变形得到不等式 | `Transform(expanded, inequality)` |
| 3.5s | 显示等号成立条件 | `Write(condition: a=b)` |
| 4.5s | 等待确认 | `Wait(1.0)` |

### 清理
- 保留: final_inequality, condition

---

## Scene 5: 应用条件 (6-8秒)
**目的**: 解释"一正二定三相等"的应用条件

### 元素
1. 条件说明文字
2. 有效应用示例
3. 无效应用示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示三个条件 | `Write(three_conditions)` |
| 1.0s | 展示"一正" | `Write(positive_condition)` |
| 2.0s | 展示"二定" | `Write(constant_condition)` |
| 3.0s | 展示"三相等" | `Write(equal_condition)` |
| 4.0s | 举例说明 | `Write(example_application)` |

### 清理
- 保留: three_conditions

---

## Scene 6: 平均数链式不等式 (6-8秒)
**目的**: 展示各种平均数的大小关系

### 元素
1. 调和平均数
2. 几何平均数
3. 算术平均数
4. 平方平均数
5. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示链式不等式 | `Write(chain_inequality)` |
| 1.0s | 逐个标记各种平均数 | `Write(various_means_labels)` |
| 3.0s | 显示作者信息 | `FadeIn(final_author_info)` |
| 4.0s | 结束等待 | `Wait(2.0)` |

### 清理
- 保留: chain_inequality, author_info

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| number_line | Scene 2 | End | 主数轴 |
| arithmetic_dot | Scene 2 | End | 算术平均数点 |
| geometric_dot | Scene 2 | End | 几何平均数点 |
| rectangles_comparison | Scene 3 | End | 靣积比较图形 |
| final_inequality | Scene 4 | End | 最终不等式 |
| three_conditions | Scene 5 | End | 三个条件 |
| chain_inequality | Scene 6 | End | 链式不等式 |
| title | Scene 1 | Scene 2 | 标题 |
| hook_question | Scene 1 | Scene 1 | 钩子问题 |

---

## 数学公式
- (a + b)/2 ≥ √(ab) (a,b > 0)
- a + b ≥ 2√(ab)
- ab ≤ (a + b)²/4
- a²+ b² ≥ 2ab
- a/b + b/a ≥ 2 (a,b同号)
- √((a² + b²)/2) ≥ (a + b)/2 ≥ √(ab) ≥ 2/(1/a + 1/b)

## 相关知识点
- 算术平均数
- 几何平均数
- 调和平均数
- 最值问题
