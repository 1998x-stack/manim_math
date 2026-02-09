# 有理数混合运算 - 动画分镜脚本

## 元信息
- 目标时长: 80-95 秒
- 场景数量: 10 个
- 难度等级: 进阶
- 核心概念: 运算顺序与括号优先级

## 颜色配置
```python
COLOR_POWER = "#9b59b6"         # 紫色 - 乘方
COLOR_MULTIPLY = "#3498db"      # 蓝色 - 乘除
COLOR_ADD = "#2ecc71"           # 绿色 - 加减
COLOR_BRACKET_SMALL = "#e74c3c" # 红色 - 小括号 ()
COLOR_BRACKET_MID = "#f39c12"   # 橙色 - 中括号 []
COLOR_BRACKET_BIG = "#1abc9c"   # 青色 - 大括号 {}
COLOR_RESULT = YELLOW           # 黄色 - 结果
COLOR_ERROR = "#e74c3c"         # 红色 - 错误
COLOR_STEP = GRAY_A             # 灰色 - 步骤说明
```

## 不涉及几何元素
本项目主要是公式动画，不需要复杂的几何计算。
主要使用：
- MathTex 展示公式
- SurroundingRectangle 高亮运算部分
- Arrow 指示运算顺序
- Transform 展示计算过程

---

## Scene 1: 开场引入 (4秒)
**目的**: 引出混合运算的复杂性

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题: "3+2×5² = ?"
3. 多个错误答案闪现
4. 副标题: "运算顺序很重要!"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.5s | 错误答案闪现 | `FadeIn(wrong_answers, scale=0.8)` |
| 2.5s | 副标题淡入 | `FadeIn(subtitle)` |
| 3.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_question, wrong_answers, subtitle
- 保留: author_info

---

## Scene 2: 运算顺序法则 (8秒)
**目的**: 展示核心法则

### 元素
1. 标题: "运算顺序"
2. 法则卡片:
   - 第一级：乘方 (紫色)
   - 第二级：乘除 (蓝色)
   - 第三级：加减 (绿色)
3. 箭头指示优先级
4. 括号优先规则

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 乘方卡片 | `FadeIn(power_card, shift=UP)` |
| 1.5s | 乘除卡片 | `FadeIn(multiply_card, shift=UP)` |
| 2.5s | 加减卡片 | `FadeIn(add_card, shift=UP)` |
| 3.5s | 优先级箭头 | `GrowArrow(priority_arrows)` |
| 4.5s | 括号规则 | `FadeIn(bracket_rule)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素
- 保留: author_info

---

## Scene 3: 示例1 - 只有加减 (7秒)
**目的**: 展示最简单情况：从左到右

### 元素
1. 标题: "只有加减：从左到右"
2. 原式: 5 - 3 + 2
3. 步骤标注
4. 逐步计算

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 + 原式 | `Write(formula)` |
| 1.0s | 高亮第一步 | `SurroundingRectangle(5-3)` |
| 2.0s | 计算第一步 | `Transform(5-3, 2)` |
| 3.0s | 高亮第二步 | `SurroundingRectangle(2+2)` |
| 4.0s | 计算第二步 | `Transform(2+2, 4)` |
| 5.0s | 结果闪烁 | `Flash(result)` |
| 6.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 4: 示例2 - 先乘除后加减 (9秒)
**目的**: 展示运算顺序的核心规则

### 元素
1. 标题: "先乘除，后加减"
2. 原式: 3 + 2 × 4 - 6 ÷ 2
3. 颜色编码：乘除（蓝色），加减（绿色）
4. 步骤说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原式书写 | `Write(formula)` |
| 1.0s | 颜色标注 | `set_color_by_tex` |
| 1.5s | 提示：先算乘除 | `FadeIn(hint)` |
| 2.5s | 高亮 2×4 | `SurroundingRectangle` |
| 3.5s | 计算 2×4=8 | `Transform` |
| 4.5s | 高亮 6÷2 | `SurroundingRectangle` |
| 5.5s | 计算 6÷2=3 | `Transform` |
| 6.5s | 计算 3+8-3 | `Transform` |
| 7.5s | 结果 = 8 | `Flash(result)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 5: 示例3 - 带乘方 (9秒)
**目的**: 展示乘方的最高优先级

### 元素
1. 标题: "先算乘方"
2. 原式: 3 + 2 × 5²
3. 颜色编码：乘方（紫色），乘法（蓝色），加法（绿色）
4. 优先级标注：①②③

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原式书写 | `Write(formula)` |
| 1.0s | 颜色 + 序号标注 | `set_color + add_label` |
| 2.0s | 高亮 5² | `SurroundingRectangle` |
| 3.0s | 计算 5²=25 | `Transform` |
| 4.0s | 高亮 2×25 | `SurroundingRectangle` |
| 5.0s | 计算 2×25=50 | `Transform` |
| 6.0s | 高亮 3+50 | `SurroundingRectangle` |
| 7.0s | 计算 3+50=53 | `Transform` |
| 8.0s | 结果闪烁 | `Flash(result)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 6: 示例4 - 小括号优先 (9秒)
**目的**: 展示括号改变运算顺序

### 元素
1. 标题: "括号优先"
2. 原式: (3 + 2) × 4
3. 对比: 3 + 2 × 4（无括号）
4. 结果对比

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原式书写 | `Write(formula)` |
| 1.0s | 高亮括号 | `SurroundingRectangle(括号, 红色)` |
| 2.0s | 提示：先算括号内 | `FadeIn(hint)` |
| 3.0s | 计算 (3+2)=5 | `Transform` |
| 4.0s | 计算 5×4=20 | `Transform` |
| 5.0s | 对比公式出现 | `FadeIn(compare)` |
| 6.0s | 无括号结果=11 | `Write(11)` |
| 7.0s | 结果对比 | `indicate(20 vs 11)` |
| 8.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 7: 示例5 - 多层括号 (10秒)
**目的**: 展示括号嵌套的处理

### 元素
1. 标题: "多层括号：由内到外"
2. 原式: {2 × [3 + (4 - 1)]}
3. 括号颜色编码
4. 逐层剥离

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 原式书写 | `Write(formula)` |
| 1.0s | 括号颜色编码 | `set_color` |
| 2.0s | 高亮小括号 | `SurroundingRectangle(小括号)` |
| 3.0s | 计算 (4-1)=3 | `Transform` |
| 4.0s | 高亮中括号 | `SurroundingRectangle(中括号)` |
| 5.0s | 计算 [3+3]=6 | `Transform` |
| 6.0s | 高亮大括号 | `SurroundingRectangle(大括号)` |
| 7.0s | 计算 {2×6}=12 | `Transform` |
| 8.0s | 结果闪烁 | `Flash(result)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 8: 常见错误 (8秒)
**目的**: 提醒学生容易犯的错误

### 元素
1. 标题: "常见错误"
2. 错误1: 忽略括号
3. 错误2: 运算顺序错误
4. 错误3: 负号处理错误

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 错误1展示 | `Write(error1)` |
| 2.0s | 错误2展示 | `Write(error2)` |
| 3.5s | 错误3展示 | `Write(error3)` |
| 5.0s | 叉号标记 | `FadeIn(cross_marks)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 9: 总结 - 运算口诀 (10秒)
**目的**: 总结记忆口诀

### 元素
1. 大标题: "运算口诀"
2. 口诀卡片:
   - "括号优先第一位"
   - "乘方紧随其后来"
   - "乘除运算第三级"
   - "加减最后算出来"
3. 顺序图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 大标题 | `Write(title)` |
| 1.0s | 口诀1 | `FadeIn(line1, shift=UP)` |
| 2.5s | 口诀2 | `FadeIn(line2, shift=UP)` |
| 4.0s | 口诀3 | `FadeIn(line3, shift=UP)` |
| 5.5s | 口诀4 | `FadeIn(line4, shift=UP)` |
| 7.0s | 顺序图示 | `Create(arrows)` |
| 8.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素

---

## Scene 10: 片尾关注 (6秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者名放大
2. 作者ID
3. 关注提示
4. 运算符号装饰

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, author_name)` |
| 0.8s | 作者ID淡入 | `FadeIn(author_id)` |
| 1.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 2.0s | 符号装饰 | `FadeIn(decorations)` |
| 3.0s | 符号旋转 | `Rotate(decorations)` |
| 5.0s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 顶部常驻 |
| formula | Scene 3-7 | 各场景末尾 | 运算公式 |
| rectangles | Scene 3-7 | 各场景末尾 | 高亮框 |
| steps | Scene 3-7 | 各场景末尾 | 步骤说明 |
| rule_cards | Scene 9 | Scene 9 | 口诀卡片 |

---

## 关键技术点
1. **颜色编码系统**: 不同运算用不同颜色
2. **SurroundingRectangle**: 高亮当前运算部分
3. **TransformMatchingTex**: 公式逐步变换
4. **序号标注**: 标明运算顺序①②③
5. **括号颜色**: 多层括号用不同颜色区分

---

## 预期难点
1. **公式变换动画**: 需要精确匹配 LaTeX 元素
2. **高亮框定位**: SurroundingRectangle 需要准确定位到子公式
3. **颜色编码**: set_color_by_tex 需要精确匹配
4. **步骤说明**: 文字与公式的布局和时机

---

## 验证要点
- [ ] 所有运算结果数学正确
- [ ] 运算顺序符合法则
- [ ] 颜色编码清晰一致
- [ ] 文字无重叠
- [ ] 动画节奏合理
- [ ] 总时长 80-95 秒