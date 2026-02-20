# 加法的初步认识 - 动画分镜脚本

## 元信息
- 目标时长: 30-45 秒
- 场景数量: 6 个
- 难度等级: 简单
- 目标观众: 小学生

## 颜色配置
```python
CIRCLE_COLOR = BLUE
ADDITION_COLOR = YELLOW
TEXT_COLOR = WHITE
BACKGROUND_COLOR = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 左侧圆圈1 | Circle + shift | left_circles[0] |
| 左侧圆圈2 | Circle + shift | left_circles[1] |
| 右侧圆圈 | Circle + shift | right_circle |
| 目标位置1 | LEFT * 0.5 + UP * 0.4 | target_positions[0] |
| 目标位置2 | LEFT * 0.5 + DOWN * 0.4 | target_positions[1] |
| 目标位置3 | RIGHT * 0.5 | target_positions[2] |

---

## Scene 1: 开场 (2-3秒)
**目的**: 钩子 + 引出加法概念

### 元素
1. 作者标识 (顶部小字)
2. 主标题 (加法的初步认识)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |

### 清理
- 保留: title, author_info

---

## Scene 2: 加法含义展示 (4-6秒)
**目的**: 展示加法的含义 - 合并两部分

### 元素
1. 左侧2个圆圈 (代表第一部分)
2. 右侧1个圆圈 (代表第二部分)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建左侧圆圈和右侧圆圈 | `Create(left_circles[0]), Create(right_circle)` |
| 0.5s | 创建左侧第二个圆圈 | `Create(left_circles[1])` |
| 1.0s | 等待观察 | `Wait(1.0)` |

### 清理
- 保留: left_circles, right_circle

---

## Scene 3: 加号和等号 (3-4秒)
**目的**: 介绍加号和等号

### 元素
1. 加号 (+) 
2. 等号 (=)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示加号 | `Write(plus_sign)` |
| 1.0s | 显示等号 | `Write(equals_sign)` |
| 2.0s | 等待观察 | `Wait(1.0)` |

### 清理
- 保留: plus_sign, equals_sign, circles

---

## Scene 4: 合并过程 (3-4秒)
**目的**: 演示合并过程，得出结果

### 元素
1. 所有圆圈 (移动到中间)
2. 结果数字 (3)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 圆圈移动到中间位置 | `MoveToTarget` |
| 1.0s | 显示结果数字 | `Write(result_number)` |
| 2.0s | 显示完整公式 | `Write(full_formula)` |

### 清理
- 保留: all_circles, result_number, full_formula

---

## Scene 5: 第二个例子 (5-6秒)
**目的**: 演示另一个加法例子

### 元素
1. 新的圆圈组合 (1 + 3)
2. 更新后的公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景元素 | `FadeOut(...)` |
| 0.2s | 创建新的圆圈组合 | `Create(new_circles)` |
| 1.2s | 移动新圆圈到中间 | `MoveToTarget` |
| 2.2s | 显示答案 | `Write(new_result)` |

### 清理
- 保留: new_circles, result, formula

---

## Scene 6: 总结 (3-4秒)
**目的**: 总结加法含义

### 元素
1. 结论文字 (加法是合并求和)
2. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示结论 | `Write(conclusion)` |
| 2.0s | 显示作者信息 | `FadeIn(author_info)` |
| 3.0s | 结束等待 | `Wait(1.0)` |

### 清理
- 保留: conclusion, author_info

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| title | Scene 1 | End | 主标题 |
| left_circles | Scene 2 | Scene 4 end | 左侧圆圈 |
| right_circle | Scene 2 | Scene 4 end | 右侧圆圈 |
| plus_sign | Scene 3 | End | 加号 |
| equals_sign | Scene 3 | End | 等号 |
| all_circles | Scene 4 | Scene 5 start | 合并后圆圈 |
| result_number | Scene 4 | Scene 5 start | 结果数字 |
| full_formula | Scene 4 | Scene 5 | 完整公式 |
| conclusion | Scene 6 | End | 结论文字 |
| author_info | Scene 1 | End | 作者信息 |

---

## 数学公式
- a + b = c
- 2 + 1 = 3
- 加数 + 加数 = 和

## 相关知识点
- 合并
- 求和
- 加号的认识
