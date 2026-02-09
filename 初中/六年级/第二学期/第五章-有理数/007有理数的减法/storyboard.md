# 有理数的减法 - 动画分镜脚本

## 元信息
- 目标时长: 70-85 秒
- 场景数量: 9 个
- 难度等级: 基础
- 核心概念: 减法转化为加法（相反数）

## 颜色配置
```python
COLOR_POSITIVE = "#2ecc71"      # 绿色 - 正数
COLOR_NEGATIVE = "#e74c3c"      # 红色 - 负数
COLOR_ZERO = "#95a5a6"          # 灰色 - 零
COLOR_RESULT = "#f39c12"        # 橙色 - 结果
COLOR_TRANSFORM = "#9b59b6"     # 紫色 - 转化过程
COLOR_NUMBERLINE = WHITE        # 数轴
COLOR_HIGHLIGHT = YELLOW        # 高亮
COLOR_AUXILIARY = GRAY_B        # 辅助元素
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴 | NumberLine(-6, 6, 单位长度=0.7) | self.number_line |
| 单位长度 | 0.7 (坐标单位) | self.UNIT_LENGTH |
| 数轴位置 | UP * 2 | self.NUMBERLINE_POS |

---

## Scene 1: 开场引入 (4秒)
**目的**: 钩子 + 引出减法与加法的关系

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字): "减法=加法?"
3. 副标题: "揭秘减法的秘密"
4. 数轴淡入

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.5s | 副标题淡入 | `FadeIn(subtitle)` |
| 2.0s | 数轴创建 | `Create(number_line)` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, subtitle
- 保留: number_line, author_info

---

## Scene 2: 核心概念 - 减法转加法 (8秒)
**目的**: 展示 a - b = a + (-b) 的核心思想

### 元素
1. 标题: "减法的秘密"
2. 原式: 3 - 2
3. 转化箭头 (紫色动画)
4. 转化后: 3 + (-2)
5. 相反数说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式书写 | `Write(original)` |
| 1.0s | 等待 | `Wait(0.5)` |
| 1.5s | 相反数概念 | `FadeIn(opposite_concept)` |
| 2.5s | 转化箭头 | `GrowArrow(transform_arrow)` |
| 3.5s | 转化后公式 | `Write(transformed)` |
| 4.5s | 高亮变化部分 | `Indicate(changed_part)` |
| 6.0s | 法则说明 | `FadeIn(rule_text)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 3: 正数减正数 (情况1: 3-2) (8秒)
**目的**: 展示 3 - 2 = 3 + (-2) = 1

### 元素
1. 标题: "正数 - 正数"
2. 公式: 3 - 2 → 3 + (-2)
3. 数轴动画: 从3向左移动2个单位
4. 结果: 1

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式 | `Write(formula_original)` |
| 1.0s | 转化 | `Transform(to_addition)` |
| 2.0s | 起点闪烁(3) | `Flash(start_dot)` |
| 2.5s | 箭头向左(-2) | `GrowArrow(arrow)` |
| 3.5s | 到达结果(1) | `Flash(result_dot)` |
| 4.0s | 结论 | `Write(conclusion)` |
| 6.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 4: 正数减正数 (情况2: 2-5) (8秒)
**目的**: 展示 2 - 5 = 2 + (-5) = -3

### 元素
1. 标题: "正数 - 正数 (被减数较小)"
2. 公式: 2 - 5 → 2 + (-5)
3. 数轴动画: 从2向左移动5个单位
4. 结果: -3 (进入负数区域)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式 | `Write(formula_original)` |
| 1.0s | 转化 | `Transform(to_addition)` |
| 2.0s | 起点闪烁(2) | `Flash(start_dot)` |
| 2.5s | 箭头向左(-5) | `GrowArrow(arrow)` |
| 3.5s | 到达结果(-3) | `Flash(result_dot)` |
| 4.0s | 说明 | `FadeIn(note_text)` |
| 4.5s | 结论 | `Write(conclusion)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 5: 正数减负数 (8秒)
**目的**: 展示 3 - (-2) = 3 + 2 = 5

### 元素
1. 标题: "正数 - 负数"
2. 公式: 3 - (-2) → 3 + 2
3. 重点: 负负得正
4. 数轴动画: 从3向右移动2个单位
5. 结果: 5

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式 | `Write(formula_original)` |
| 1.0s | 负负得正提示 | `FadeIn(hint)` |
| 1.5s | 转化 | `Transform(to_addition)` |
| 2.5s | 起点闪烁(3) | `Flash(start_dot)` |
| 3.0s | 箭头向右(+2) | `GrowArrow(arrow)` |
| 4.0s | 到达结果(5) | `Flash(result_dot)` |
| 4.5s | 结论 | `Write(conclusion)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 6: 负数减正数 (8秒)
**目的**: 展示 (-3) - 2 = (-3) + (-2) = -5

### 元素
1. 标题: "负数 - 正数"
2. 公式: (-3) - 2 → (-3) + (-2)
3. 数轴动画: 从-3向左移动2个单位
4. 结果: -5

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式 | `Write(formula_original)` |
| 1.0s | 转化 | `Transform(to_addition)` |
| 2.0s | 起点闪烁(-3) | `Flash(start_dot)` |
| 2.5s | 箭头向左(-2) | `GrowArrow(arrow)` |
| 3.5s | 到达结果(-5) | `Flash(result_dot)` |
| 4.0s | 结论 | `Write(conclusion)` |
| 6.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 7: 负数减负数 (8秒)
**目的**: 展示 (-2) - (-3) = (-2) + 3 = 1

### 元素
1. 标题: "负数 - 负数"
2. 公式: (-2) - (-3) → (-2) + 3
3. 重点: 负负得正
4. 数轴动画: 从-2向右移动3个单位
5. 结果: 1

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 原式 | `Write(formula_original)` |
| 1.0s | 负负得正提示 | `FadeIn(hint)` |
| 1.5s | 转化 | `Transform(to_addition)` |
| 2.5s | 起点闪烁(-2) | `Flash(start_dot)` |
| 3.0s | 箭头向右(+3) | `GrowArrow(arrow)` |
| 4.0s | 到达结果(1) | `Flash(result_dot)` |
| 4.5s | 结论 | `Write(conclusion)` |
| 6.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 8: 特殊情况 (7秒)
**目的**: 展示 a - 0 = a 和 0 - a = -a

### 元素
1. 标题: "特殊情况"
2. 公式组:
   - a - 0 = a
   - 0 - a = -a
3. 简短说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 公式1书写 | `Write(formula1)` |
| 1.5s | 说明1 | `FadeIn(explain1)` |
| 2.5s | 公式2书写 | `Write(formula2)` |
| 3.5s | 说明2 | `FadeIn(explain2)` |
| 5.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 9: 总结 - 减法法则 (10秒)
**目的**: 汇总减法法则

### 元素
1. 大标题: "有理数减法法则"
2. 法则卡片:
   - 核心法则: a - b = a + (-b)
   - 关键步骤: 1) 找相反数 2) 转化为加法
3. 重点提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 数轴淡出 | `FadeOut(number_line)` |
| 0.5s | 大标题书写 | `Write(title)` |
| 1.5s | 核心法则卡片 | `FadeIn(card_main)` |
| 2.5s | 步骤卡片 | `FadeIn(card_steps)` |
| 3.5s | 示例卡片 | `FadeIn(card_examples)` |
| 4.5s | 重点提示 | `FadeIn(highlight)` |
| 6.0s | 等待 | `Wait(4.0)` |

### 清理
- FadeOut: 全部元素

---

## Scene 10: 片尾关注 (6秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者名放大
2. 作者ID
3. 关注提示
4. 减号变加号动画装饰

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, author_name)` |
| 0.8s | 作者ID淡入 | `FadeIn(author_id)` |
| 1.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 2.0s | 符号装饰 | `FadeIn(decorations)` |
| 3.0s | 符号变换 | `Transform(minus_to_plus)` |
| 5.0s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 9 | 顶部常驻 |
| number_line | Scene 1 | Scene 9 | 主数轴 |
| scene_title | Scene 2-8 | 各场景末尾 | 场景标题 |
| formula | Scene 2-8 | 各场景末尾 | 运算公式 |
| arrows | Scene 3-7 | 各场景末尾 | 移动箭头 |
| dots | Scene 3-7 | 各场景末尾 | 位置标记 |
| rule_cards | Scene 9 | Scene 9 | 法则卡片 |

---

## 关键技术点
1. **公式转化动画**: 使用 `TransformMatchingTex` 展示减法到加法的转化
2. **相反数高亮**: 用颜色变化强调相反数
3. **数轴精确定位**: 使用 `number_line.n2p(value)` 获取数值对应的坐标
4. **箭头方向**: 正数向右 (RIGHT)，负数向左 (LEFT)
5. **颜色编码**: 正数绿色，负数红色，转化过程紫色，结果橙色

---

## 预期难点
1. **公式转化动画**: 需要精确匹配 LaTeX 元素
2. **相反数概念**: 需要清晰的视觉展示
3. **符号变化**: 减号变加号，同时数字符号也变
4. **节奏控制**: 转化过程要慢，运算过程要清晰

---

## 验证要点
- [ ] 所有箭头起止点精确对应数值
- [ ] 公式转化动画流畅
- [ ] 颜色编码一致
- [ ] 文字无重叠
- [ ] 动画节奏合理
- [ ] 总时长 70-85 秒