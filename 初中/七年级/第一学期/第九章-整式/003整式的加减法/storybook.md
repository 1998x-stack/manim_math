# 整式的加减法 - 动画分镜脚本

<!-- /root/code/sss/media/videos/polynomial_addition_subtraction/1920p60/PolynomialAdditionSubtraction.mp4 -->
## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 目标年级: 七年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要项
COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要项  
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正号
COLOR_NEGATIVE = "#e67e22"     # 橙色 - 负号
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝灰 - 背景
```

## 核心概念
1. 去括号法则：括号前是正号，括号内各项符号不变；括号前是负号，括号内各项变号
2. 合并同类项：系数相加，字母和指数不变

## 几何/数学元素清单
| 元素 | 类型 | 用途 |
|------|------|------|
| 主公式 | MathTex | 展示完整表达式 |
| 括号箱 | Rectangle | 视觉化括号 |
| 符号箭头 | Arrow | 指示变号过程 |
| 项分组 | VGroup | 同类项管理 |
| 下划线 | Line | 标记同类项 |

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题
3. 示例题目闪现

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 问题公式出现 | `FadeIn(problem, shift=UP*0.3)` |
| 2.5s | 等待思考 | `Wait(1.5)` |

### 清理
- FadeOut: hook_text
- 保留: author_info, problem (会变换)

---

## Scene 2: 去括号法则 - 正号情况 (4-12秒)
**目的**: 演示括号前是正号的去括号规则

### 元素
1. 标题 "去括号法则 (一)"
2. 公式: +(a+b) = a+b
3. 括号高亮框
4. 符号对比箭头

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 左侧公式出现 | `Write(formula_left)` |
| 1.5s | 括号框高亮 | `Create(bracket_box, color=YELLOW)` |
| 2.3s | 正号闪烁 | `Indicate(plus_sign)` |
| 3.0s | 箭头指向右侧 | `GrowArrow(arrow)` |
| 3.5s | 右侧结果出现 | `TransformMatchingTex(left, right)` |
| 4.8s | 说明文字 | `FadeIn(explanation)` |
| 6.5s | 停留理解 | `Wait(1.5)` |

### 关键点
- 用不同颜色标记 a 和 b
- 箭头清晰指示变换方向
- 说明文字: "括号前是正号，符号不变"

### 清理
- FadeOut: title, formula, bracket_box, arrow, explanation
- 准备下一场景

---

## Scene 3: 去括号法则 - 负号情况 (12-22秒)
**目的**: 演示括号前是负号的去括号规则（重点）

### 元素
1. 标题 "去括号法则 (二)"
2. 公式: -(a+b) = -a-b
3. 符号变化动画
4. 叉号和对勾标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 左侧公式 | `Write(formula_left)` |
| 1.5s | 负号闪烁3次 | `Indicate(minus_sign, scale=1.3)` |
| 2.5s | 括号内符号标记 | `Circle around signs` |
| 3.5s | 变号箭头动画 | `Transform with curved arrows` |
| 4.5s | 右侧结果逐项出现 | `Write(-a), Write(-b)` |
| 6.0s | 对比标注 | `Cross(old), Checkmark(new)` |
| 7.5s | 说明文字 | `FadeIn(explanation)` |
| 9.0s | 停留理解 | `Wait(1.5)` |

### 关键点
- 负号用醒目颜色（橙色）
- 变号过程要清晰：+ → -, - → +
- 说明文字: "括号前是负号，括号内各项变号"
- 这是难点，停留时间长

### 清理
- FadeOut 所有元素

---

## Scene 4: 综合例题 - 问题呈现 (22-28秒)
**目的**: 引入实际计算题目

### 元素
1. 例题标题
2. 原始题目: (2x+3) - (x-1)
3. 步骤提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 例题标题 | `Write(title)` |
| 0.6s | 原式出现 | `Write(original_eq)` |
| 1.5s | 步骤提示框 | `FadeIn(step_box)` |
| 2.5s | 步骤1文字 | `Write("第一步: 去括号")` |
| 4.0s | 等待 | `Wait(1.0)` |

### 清理
- 保留: original_eq (会变换)
- FadeOut: step_box

---

## Scene 5: 去括号过程 (28-40秒)
**目的**: 演示具体去括号步骤

### 元素
1. 原式: (2x+3) - (x-1)
2. 中间式: 2x+3-x+1
3. 括号消失动画
4. 符号变化标记

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 第一个括号高亮 | `Indicate(first_bracket)` |
| 0.8s | 正号标记 | `Circle(plus_before)` |
| 1.5s | 括号消失，保持符号 | `FadeOut(brackets), remain same` |
| 2.5s | 结果: 2x+3 | `Show result` |
| 3.5s | 第二个括号高亮 | `Indicate(second_bracket)` |
| 4.3s | 负号标记（红色） | `Circle(minus_before, RED)` |
| 5.5s | 符号变化动画 | `Transform: -1 → +1` |
| 7.0s | 括号消失，符号已变 | `FadeOut(brackets)` |
| 8.5s | 完整结果 | `Show: 2x+3-x+1` |
| 10.0s | 等待 | `Wait(1.5)` |

### 关键点
- 分两步展示，先正括号，后负括号
- 负号括号的变号要用动画清晰展示
- 用颜色区分不同项

### 清理
- 保留结果公式

---

## Scene 6: 合并同类项 (40-52秒)
**目的**: 演示同类项合并过程

### 元素
1. 中间式: 2x+3-x+1
2. 同类项下划线
3. 合并动画
4. 最终结果: x+4

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 说明文字 | `Write("第二步: 合并同类项")` |
| 1.0s | x项下划线（蓝色） | `Create(underline1)` |
| 1.8s | x项移动聚集 | `2x, -x move together` |
| 3.0s | 合并计算 | `Transform to: x` |
| 4.0s | 常数项下划线（绿色） | `Create(underline2)` |
| 4.8s | 常数项聚集 | `3, 1 move together` |
| 6.0s | 合并计算 | `Transform to: 4` |
| 7.5s | 最终结果 | `Write(final: x+4)` |
| 9.0s | 结果框强调 | `Rectangle around result` |
| 10.5s | 等待 | `Wait(1.5)` |

### 关键点
- 同类项用相同颜色下划线
- 移动动画要流畅
- 计算过程可见: 2x-x=x, 3+1=4

### 清理
- 保留最终结果

---

## Scene 7: 总结与片尾 (52-65秒)
**目的**: 总结规则，引导关注

### 元素
1. 完整步骤回顾
2. 核心规则卡片
3. 作者信息放大
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write("整式加减两步走")` |
| 1.0s | 步骤1卡片 | `FadeIn(card1: 去括号)` |
| 2.0s | 步骤2卡片 | `FadeIn(card2: 合并同类项)` |
| 3.5s | 要点闪烁 | `Indicate(key_points)` |
| 5.0s | 卡片淡出 | `FadeOut(cards)` |
| 6.0s | 作者信息放大 | `Transform(author)` |
| 7.5s | 关注提示 | `Write("关注我，学更多数学技巧!")` |
| 9.5s | 装饰动画 | `Stars/Icons animation` |
| 11.0s | 等待 | `Wait(2.0)` |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| formula_positive | Scene 2 | Scene 2 | 正号去括号 |
| formula_negative | Scene 3 | Scene 3 | 负号去括号 |
| original_eq | Scene 4 | Scene 5 | 原始题目 |
| intermediate_eq | Scene 5 | Scene 6 | 去括号后 |
| final_result | Scene 6 | Scene 7 | 最终答案 |
| step_cards | Scene 7 | Scene 7 | 总结卡片 |

---

## 时间分配总结
- 开场: 4秒
- 去括号规则（正）: 8秒
- 去括号规则（负）: 10秒（重点）
- 例题呈现: 6秒
- 去括号演示: 12秒
- 合并同类项: 12秒
- 总结片尾: 13秒
- **总计: 约65秒**

## 技术要点
1. 使用 MathTex 而非 Text 显示数学公式
2. 符号变化用 Transform 动画
3. 同类项用 VGroup 管理
4. 颜色编码帮助理解
5. 适当停顿让学生消化

## 验证清单
- [ ] 所有文字使用 Text()，数学用 MathTex()
- [ ] 坐标在安全范围内 (x∈[-4,4], y∈[-7,7])
- [ ] 字体大小符合规范
- [ ] 难点（负号去括号）有足够停留
- [ ] 动画节奏流畅
- [ ] 元素生命周期管理清晰