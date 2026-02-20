# 数学归纳法动画 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 8 个
- 难度等级: 高二水平
- 内容: 数学归纳法的原理、步骤、应用

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调递推
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键步骤
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_DOMINO = "#8e44ad"       # 紫色 - 多米诺骨牌
COLOR_SUCCESS = "#2ecc71"      # 绿色 - 成功/成立
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 多米诺位置 | 等间距分布 | self.domino_positions |
| 步骤框位置 | 垂直堆叠 | self.step_boxes |
| 公式位置 | 居中对齐 | self.formula_positions |
| 箭头起点/终点 | 基于步骤框 | self.arrow_points |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 用多米诺骨牌吸引注意力，引出数学归纳法

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题: "如何证明无限个命题?"
3. 多米诺骨牌动画

### 几何计算
```python
# 多米诺骨牌位置 (横向排列，y=1)
domino_spacing = 0.8
domino_y = 1.0
domino_positions = [
    np.array([-3.5 + i * domino_spacing, domino_y, 0])
    for i in range(8)
]

# 多米诺尺寸
domino_width = 0.4
domino_height = 1.2
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.0s | 多米诺骨牌竖立 | `FadeIn(dominoes, lag_ratio=0.1)` |
| 2.0s | 第一块倒下 | `Rotate(domino[0], -PI/6)` |
| 2.3s | 连锁反应 | `Rotate(dominoes[1:], lag_ratio=0.15)` |

### 清理
- FadeOut: hook_text
- 保留: author_info, dominoes (缩小)

---

## Scene 2: 数学归纳法介绍 (6-8秒)
**目的**: 介绍数学归纳法的定义和核心思想

### 元素
1. 标题: "数学归纳法"
2. 定义文字
3. 多米诺类比

### 几何计算
```python
# 标题位置
title_pos = np.array([0, 6.5, 0])

# 定义框位置
definition_box_center = np.array([0, 4, 0])

# 类比文字位置
analogy_pos = np.array([0, 1.5, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.6s | 定义文字淡入 | `FadeIn(definition)` |
| 1.5s | 多米诺类比 | `Indicate(dominoes)` |
| 2.5s | 箭头指向 | `GrowArrow(arrow)` |
| 3.5s | 类比文字 | `Write(analogy)` |

### 清理
- FadeOut: definition, analogy
- 保留: title (缩小移到顶部)

---

## Scene 3: 两个步骤概览 (8-10秒)
**目的**: 展示数学归纳法的两个核心步骤

### 元素
1. 步骤1框: "归纳奠基 (Base Case)"
2. 步骤2框: "归纳递推 (Inductive Step)"
3. 连接箭头
4. 结论框

### 几何计算
```python
# 步骤框位置 (左右分布)
step1_pos = np.array([-2, 2, 0])
step2_pos = np.array([2, 2, 0])

# 步骤框尺寸
step_box_width = 3.5
step_box_height = 2.0

# 结论框位置
conclusion_pos = np.array([0, -2, 0])

# 箭头
arrow_step1_to_step2 = Arrow(
    step1_pos + RIGHT * (step_box_width/2),
    step2_pos + LEFT * (step_box_width/2)
)
arrow_to_conclusion = Arrow(
    np.array([0, 0, 0]),
    conclusion_pos + UP * 0.5
)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 步骤1框出现 | `FadeIn(step1_box, shift=RIGHT)` |
| 0.8s | 步骤1内容 | `Write(step1_content)` |
| 2.0s | 步骤2框出现 | `FadeIn(step2_box, shift=LEFT)` |
| 2.8s | 步骤2内容 | `Write(step2_content)` |
| 4.0s | 连接箭头 | `GrowArrow(arrows)` |
| 5.0s | 结论框 | `FadeIn(conclusion)` |

### 清理
- FadeOut: step boxes (保留作为小图标)
- 保留: 简化版步骤图示

---

## Scene 4: 步骤1详解 - 归纳奠基 (8-10秒)
**目的**: 详细解释归纳奠基步骤

### 元素
1. 场景标题: "步骤1: 归纳奠基"
2. 公式: n=1 或 n=n₀
3. 多米诺第一块高亮
4. 说明文字

### 几何计算
```python
# 场景标题位置
scene_title_pos = np.array([0, 6, 0])

# 公式位置
formula_pos = np.array([0, 3.5, 0])

# 多米诺第一块位置（已有）
first_domino_pos = domino_positions[0]

# 说明框位置
explanation_pos = np.array([0, 0.5, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 场景标题写入 | `Write(scene_title)` |
| 0.6s | 公式出现 | `Write(formula)` |
| 1.5s | 多米诺第一块放大高亮 | `Indicate(first_domino, scale=1.3)` |
| 2.5s | 说明文字淡入 | `FadeIn(explanation)` |
| 4.0s | 检查标记 (✓) | `FadeIn(check_mark, scale=0.5)` |

### 清理
- FadeOut: scene_title, explanation
- 保留: formula (缩小), check_mark

---

## Scene 5: 步骤2详解 - 归纳递推 (10-12秒)
**目的**: 详细解释归纳递推步骤

### 元素
1. 场景标题: "步骤2: 归纳递推"
2. 假设公式: n=k 成立
3. 证明公式: n=k+1 成立
4. 多米诺连锁动画

### 几何计算
```python
# 场景标题位置
scene_title_pos = np.array([0, 6, 0])

# 假设框位置
assumption_pos = np.array([0, 4, 0])

# 证明框位置  
proof_pos = np.array([0, 2, 0])

# 连接箭头
arrow_assumption_to_proof = Arrow(
    assumption_pos + DOWN * 0.5,
    proof_pos + UP * 0.5
)

# 多米诺k和k+1的位置
domino_k_pos = np.array([-1, -1, 0])
domino_k1_pos = np.array([1, -1, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 场景标题写入 | `Write(scene_title)` |
| 0.6s | 假设框出现 | `FadeIn(assumption_box)` |
| 1.5s | 假设公式 | `Write(assumption_formula)` |
| 2.5s | 箭头生长 | `GrowArrow(arrow)` |
| 3.0s | 证明框出现 | `FadeIn(proof_box)` |
| 3.8s | 证明公式 | `Write(proof_formula)` |
| 5.0s | 多米诺k倒下 | `Rotate(domino_k)` |
| 5.5s | 多米诺k+1倒下 | `Rotate(domino_k1)` |
| 6.5s | 重点停留 | `Wait(2.0)` |

### 清理
- FadeOut: scene_title, boxes
- 保留: 关键公式

---

## Scene 6: 完整证明示例 (12-15秒)
**目的**: 用具体例子演示数学归纳法

### 元素
1. 例题: 证明 1+2+3+...+n = n(n+1)/2
2. 步骤1验证: n=1
3. 步骤2推导: k → k+1
4. 结论

### 几何计算
```python
# 例题位置
problem_pos = np.array([0, 5.5, 0])

# 步骤1区域
step1_region_y = 3.0
step1_left = np.array([-3, step1_region_y, 0])

# 步骤2区域
step2_region_y = 0.5
step2_left = np.array([-3, step2_region_y, 0])

# 公式推导位置（垂直排列）
derivation_y_start = 1.5
derivation_spacing = 0.8
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题出现 | `Write(problem)` |
| 1.0s | 步骤1标签 | `FadeIn(step1_label)` |
| 1.5s | n=1验证 | `Write(verification)` |
| 2.5s | 检查标记 | `FadeIn(check1)` |
| 3.5s | 步骤2标签 | `FadeIn(step2_label)` |
| 4.0s | 假设k成立 | `Write(assumption)` |
| 5.0s | 推导k+1 | `TransformMatchingTex(...)` |
| 7.0s | 代数化简 | `Write(simplification)` |
| 9.0s | 结论成立 | `FadeIn(conclusion, scale=1.2)` |

### 清理
- FadeOut: 所有推导步骤
- 保留: 例题和结论框

---

## Scene 7: 应用场景 (6-8秒)
**目的**: 展示数学归纳法的应用领域

### 元素
1. 应用标题
2. 应用卡片: 恒等式、不等式、整除性
3. 图标装饰

### 几何计算
```python
# 标题位置
app_title_pos = np.array([0, 6, 0])

# 卡片位置（垂直排列）
card_positions = [
    np.array([0, 3, 0]),    # 恒等式
    np.array([0, 1, 0]),    # 不等式
    np.array([0, -1, 0])    # 整除性
]

# 卡片尺寸
card_width = 6.0
card_height = 1.2
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(app_title)` |
| 0.8s | 卡片1滑入 | `card1.animate.shift(RIGHT)` |
| 1.5s | 卡片2滑入 | `card2.animate.shift(RIGHT)` |
| 2.2s | 卡片3滑入 | `card3.animate.shift(RIGHT)` |
| 3.5s | 全部高亮 | `Indicate(cards)` |

### 清理
- FadeOut: 应用卡片
- 保留: 标题

---

## Scene 8: 总结与片尾 (8-10秒)
**目的**: 总结核心要点 + 关注提示

### 元素
1. 核心要点卡片
2. 多米诺最终效果
3. 作者信息放大
4. 关注提示

### 几何计算
```python
# 要点卡片位置
summary_cards_y_start = 3.5
summary_cards_spacing = 1.5

# 多米诺最终位置
final_dominoes_y = 0

# 作者信息位置
author_final_pos = np.array([0, 1.5, 0])
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 要点卡片出现 | `FadeIn(summary_cards, lag_ratio=0.2)` |
| 2.0s | 多米诺完整连锁 | `Rotate(all_dominoes, lag_ratio=0.1)` |
| 4.0s | 作者信息放大 | `Transform(author, large_author)` |
| 5.0s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 6.5s | 装饰动画 | `Rotate(decorations)` |

### 清理
- FadeOut: 全部

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| dominoes | Scene 1 | Scene 8 | 贯穿始终 |
| title | Scene 2 | Scene 8 | 缩小后保留 |
| step_boxes | Scene 3 | Scene 5 | 步骤框 |
| formula_base | Scene 4 | Scene 8 | 归纳奠基公式 |
| formula_inductive | Scene 5 | Scene 8 | 归纳递推公式 |
| example | Scene 6 | Scene 7 | 完整示例 |
| summary | Scene 8 | Scene 8 | 总结卡片 |

---

## 关键动画时机
- 难点停留: 归纳递推推导 (2.0s), 完整证明 (2.5s)
- 过渡等待: 场景切换 (0.4-0.6s)
- 快速动画: 多米诺连锁 (0.15s lag), 卡片滑入 (0.5s)
- 高亮强调: 关键步骤 (Indicate, 1.0s)

## 边界安全检查
- 所有公式 y ∈ [-3, 6]
- 多米诺骨牌 x ∈ [-3.5, 3.5]
- 文字标注避免重叠 (buff ≥ 0.2)
- 步骤框不超出边界