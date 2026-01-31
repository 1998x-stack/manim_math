# 公倍数与最小公倍数 - 动画分镜脚本

<!-- /root/code/sss/media/videos/lcm_animation/1920p60/CommonMultiplesLCM.mp4 -->
## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 简单
- 目标年级: 六年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 数字4的倍数
COLOR_SECONDARY = "#e74c3c"    # 红色 - 数字6的倍数
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 公倍数高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线/文字
COLOR_LCM = GOLD               # 金色 - 最小公倍数
COLOR_TABLE_HEADER = "#2c3e50" # 深灰 - 表头
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴原点 | ORIGIN + DOWN*1 | self.numberline_center |
| 表格位置 | UP*2 | self.table_position |
| 公式位置 | DOWN*4 | self.formula_position |

---

## Scene 1: 开场钩子 (3秒)
**目的**: 抓住注意力,引出问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字)
3. 两个数字: 4 和 6

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 数字4出现 | `FadeIn(num_4, scale=0.5)` |
| 1.4s | 数字6出现 | `FadeIn(num_6, scale=0.5)` |
| 2.0s | 问号闪烁 | `Flash(question_mark)` |
| 2.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, question_mark
- 保留: num_4, num_6, author_info

---

## Scene 2: 倍数概念 (8秒)
**目的**: 回顾倍数的基本概念

### 元素
1. 标题: "什么是倍数?"
2. 4的倍数列表
3. 6的倍数列表
4. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | "4的倍数"标签 | `FadeIn(label_4)` |
| 1.0s | 倍数依次出现 | `LaggedStart(*[FadeIn(m) for m in multiples_4])` |
| 3.0s | "6的倍数"标签 | `FadeIn(label_6)` |
| 3.4s | 倍数依次出现 | `LaggedStart(*[FadeIn(m) for m in multiples_6])` |
| 5.5s | 说明文字 | `FadeIn(explanation)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, explanation
- 保留: multiples_4, multiples_6, labels

---

## Scene 3: 数轴可视化 (10秒)
**目的**: 在数轴上标记倍数,直观展示

### 元素
1. 数轴 (0-30)
2. 4的倍数标记点 (蓝色)
3. 6的倍数标记点 (红色)
4. 重叠点高亮 (黄色)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建数轴 | `Create(numberline)` |
| 1.0s | 4的倍数跳跃标记 | `LaggedStart(*[GrowFromCenter(dot) for dot in dots_4])` |
| 3.0s | 6的倍数跳跃标记 | `LaggedStart(*[GrowFromCenter(dot) for dot in dots_6])` |
| 5.0s | 公倍数点变色 | `*[dot.animate.set_color(YELLOW).scale(1.5) for dot in common_dots]` |
| 6.5s | 圈出公倍数 | `Create(circles)` |
| 8.0s | 标注文字 | `FadeIn(annotation)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: numberline, all dots, circles, annotation
- 保留: 无

---

## Scene 4: 公倍数定义 (6秒)
**目的**: 明确公倍数的定义

### 元素
1. 定义文字框
2. 公倍数列表: 12, 24, 36, ...
3. 韦恩图(可选)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 定义框滑入 | `definition_box.animate.shift(DOWN*10 to ORIGIN)` |
| 1.0s | 定义文字书写 | `Write(definition_text)` |
| 2.5s | 公倍数依次出现 | `LaggedStart(*[FadeIn(cm) for cm in common_multiples])` |
| 4.5s | 高亮显示 | `Indicate(common_multiples)` |
| 5.5s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: definition_box, common_multiples
- 保留: 无

---

## Scene 5: 最小公倍数 (12秒)
**目的**: 引出LCM概念,强调"最小"

### 元素
1. 标题: "最小公倍数 LCM"
2. 公倍数序列: 12, 24, 36, 48, ...
3. 12被放大并高亮
4. 公式: lcm(4,6) = 12

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 1.0s | 公倍数序列排列 | `Create(sequence)` |
| 2.5s | 箭头指向12 | `GrowArrow(arrow)` |
| 3.0s | 12放大变金色 | `number_12.animate.scale(2).set_color(GOLD)` |
| 4.0s | 闪光效果 | `Flash(number_12, color=GOLD)` |
| 4.5s | "最小"文字强调 | `FadeIn(min_text, scale=1.2)` |
| 6.0s | 公式滑入 | `formula.animate.shift(UP*10 to position)` |
| 7.5s | 公式高亮 | `Indicate(formula)` |
| 9.0s | 说明文字 | `FadeIn(explanation)` |
| 11.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, sequence, arrow, min_text, explanation
- 保留: formula (缩小移到角落)

---

## Scene 6: 求法演示 - 短除法 (15秒)
**目的**: 展示短除法求LCM

### 元素
1. 标题: "如何求最小公倍数?"
2. 短除法表格
3. 步骤说明
4. 计算过程动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 写出4和6 | `Write(numbers)` |
| 1.5s | 短除符号 | `Create(division_symbol)` |
| 2.0s | 除以2 | `FadeIn(divisor_2)` |
| 2.5s | 结果2,3 | `TransformFromCopy(numbers, result_1)` |
| 3.5s | 箭头提示 | `GrowArrow(arrow_1)` |
| 4.0s | 说明"继续除" | `FadeIn(hint_1)` |
| 5.0s | 不能再除 | `FadeIn(final_numbers)` |
| 6.0s | 计算公式 | `Write(calculation)` |
| 7.5s | 2×2×3 = 12 | `TransformMatchingTex(calculation, result)` |
| 9.0s | 答案高亮 | `result.animate.set_color(GOLD).scale(1.3)` |
| 10.0s | 验证说明 | `FadeIn(verification)` |
| 13.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有短除法元素
- 保留: 无

---

## Scene 7: 重要关系式 + 结尾 (8秒)
**目的**: 展示GCD与LCM的关系,结束

### 元素
1. 重要公式: a × b = gcd(a,b) × lcm(a,b)
2. 实例验证: 4 × 6 = 2 × 12
3. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题"重要关系" | `Write(title)` |
| 1.0s | 公式出现 | `FadeIn(formula)` |
| 2.0s | 实例计算 | `Write(example)` |
| 3.5s | 两边结果 | `TransformMatchingTex(example, verification)` |
| 4.5s | 24 = 24 ✓ | `Indicate(check_mark)` |
| 5.5s | 作者信息放大 | `author_info.animate.scale(1.5).move_to(UP)` |
| 6.5s | 关注提示 | `FadeIn(follow_text, shift=UP*0.3)` |
| 7.5s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保持在顶部 |
| num_4, num_6 | Scene 1 | Scene 2 | 开场数字 |
| multiples_4 | Scene 2 | Scene 3 | 4的倍数列表 |
| multiples_6 | Scene 2 | Scene 3 | 6的倍数列表 |
| numberline | Scene 3 | Scene 3 | 数轴 |
| formula | Scene 5 | Scene 7 | LCM公式(缩小保留) |
| division_table | Scene 6 | Scene 6 | 短除法表格 |

---

## 节奏控制要点
1. **开场钩子要快** (3秒内抓住注意力)
2. **倍数概念可以稍快** (学生已学过)
3. **数轴可视化要清晰** (关键理解点,多停留)
4. **短除法演示要慢** (新方法,需要理解)
5. **结尾要有力** (强化记忆点)

## 字体大小使用
- 标题: 36
- 副标题: 28
- 数字(大): 48
- 数字(正常): 28
- 说明文字: 22
- 小字注释: 18
- 作者信息: 20

## 特殊效果
1. **公倍数高亮**: 使用 Flash + scale(1.5)
2. **最小值强调**: GOLD + scale(2) + Flash
3. **数字出现**: LaggedStart 产生节奏感
4. **公式推导**: TransformMatchingTex 平滑过渡