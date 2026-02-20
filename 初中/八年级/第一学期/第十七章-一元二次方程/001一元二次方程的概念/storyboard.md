# 一元二次方程的概念 - 动画分镜脚本

## 元信息
- 目标时长: 60 秒
- 场景数量: 6 个
- 难度等级: 初等
- 目标观众: 初中学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#2ecc71"    # 绿色 - 次要元素  
COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 强调元素
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助元素
COLOR_AUTHOR = "#e74c3c"       # 红色 - 作者信息
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 方程框 | 位置固定 | self.formula_box |
| 系数a位置 | 从方程分离 | self.coeff_a_pos |
| 系数b位置 | 从方程分离 | self.coeff_b_pos |
| 系数c位置 | 从方程分离 | self.coeff_c_pos |

---

## Scene 1: 开场 (3-4秒)
**目的**: 吸引注意 + 引出主题

### 元素
1. 作者标识 (顶部小字)
2. 主题标题 (大字)
3. 背景装饰图形

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 主题标题书写 | `Write(title)` |
| 1.1s | 背景装饰动画 | `Create(decoration)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- 保留: title, author_info
- 准备下一场景

---

## Scene 2: 一元二次方程定义 (8-10秒)
**目的**: 正式介绍一元二次方程的定义

### 元素
1. 定义文字
2. 关键词强调

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示定义文字 | `Write(definition_text)` |
| 1.0s | 强调"一个未知数" | `Indicate(word1)` |
| 2.0s | 强调"最高次数是2" | `Indicate(word2)` |
| 3.0s | 强调"整式方程" | `Indicate(word3)` |
| 4.0s | 等待理解 | `Wait(2.0)` |

### 清理
- 保留: definition_text
- 进入下一环节

---

## Scene 3: 一般形式展示 (8-10秒)
**目的**: 展示一元二次方程的标准形式

### 元素
1. 标准形式公式
2. 各部分标识

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 书写标准形式 | `Write(general_form)` |
| 1.0s | 添加括号说明 | `Write(condition)` |
| 2.0s | 标识二次项 | `SurroundingRectangle(quad_term)` |
| 3.0s | 标识一次项 | `SurroundingRectangle(lin_term)` |
| 4.0s | 标识常数项 | `SurroundingRectangle(const_term)` |
| 5.0s | 等待 | `Wait(1.0)` |

### 清理
- 保留: general_form 和标注
- 进入下一部分

---

## Scene 4: 系数解释 (10-12秒)
**目的**: 详细介绍各项系数的意义

### 元素
1. 分解后的公式
2. 各系数说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 分解公式布局 | `Transform(general_form, decomposed)` |
| 1.0s | 解释a的作用 | `Write(a_explanation)` |
| 2.0s | 解释b的作用 | `Write(b_explanation)` |
| 3.0s | 解释c的作用 | `Write(c_explanation)` |
| 4.0s | 强调a≠0的重要性 | `Flash(a_notequal_zero)` |
| 5.0s | 等待消化 | `Wait(2.0)` |

---

## Scene 5: 对比其他方程 (8-10秒)
**目的**: 通过对比加深理解

### 元素
1. 一元二次方程
2. 一元一次方程
3. 三次方程示例

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 一元二次方程 | `Write(quadratic_eq)` |
| 1.0s | 一元一次方程 | `Write(linear_eq)` |
| 2.0s | 三次方程 | `Write(cubic_eq)` |
| 3.0s | 对比分析 | `Create(comparison_lines)` |
| 4.0s | 强调区别 | `Indicate(differences)` |
| 5.0s | 等待 | `Wait(1.0)` |

---

## Scene 6: 总结与回顾 (6-8秒)
**目的**: 总结要点，强化记忆

### 元素
1. 关键信息汇总
2. 作者信息及关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 关键点回顾 | `Write(key_points)` |
| 2.0s | 作者信息 | `Write(final_author)` |
| 3.0s | 关注提示 | `Write(follow_prompt)` |
| 4.0s | 最终强调 | `Flash(main_formula)` |

### 清理
- 结束场景

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| title | Scene 1 | End | 主标题 |
| general_form | Scene 3 | Scene 6 | 标准形式 |
| decomposition | Scene 4 | Scene 6 | 公式分解 |
| author_info | Scene 1 | Scene 6 | 作者信息 |
| ... | ... | ... | ... |

---

## TikTok竖屏规格
- 尺寸: 1080×1920 (9×16比例)
- 背景色: "#1a1a2e" (深蓝灰)
- 安全区域: x∈[-4,4], y∈[-7,7]
- 顶部区域: y∈[6,8] - 标题/作者
- 主内容区: y∈[-3,5] - 公式/图形
- 底部区域: y∈[-6,-3] - 说明/提示
