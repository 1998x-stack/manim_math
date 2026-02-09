# 有理数的加法 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 8 个
- 难度等级: 基础
- 核心概念: 使用数轴可视化有理数加法

## 颜色配置
```python
COLOR_POSITIVE = "#2ecc71"      # 绿色 - 正数
COLOR_NEGATIVE = "#e74c3c"      # 红色 - 负数
COLOR_ZERO = "#95a5a6"          # 灰色 - 零
COLOR_RESULT = "#f39c12"        # 橙色 - 结果
COLOR_NUMBERLINE = WHITE        # 数轴
COLOR_HIGHLIGHT = YELLOW        # 高亮
COLOR_AUXILIARY = GRAY_B        # 辅助元素
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 数轴 | NumberLine(-5, 5, 单位长度=0.8) | self.number_line |
| 单位长度 | 0.8 (坐标单位) | self.UNIT_LENGTH |
| 数轴位置 | UP * 2 | self.NUMBERLINE_POS |

---

## Scene 1: 开场引入 (4秒)
**目的**: 钩子 + 引出有理数加法问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字): "正数+负数=?"
3. 数轴淡入

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

## Scene 2: 同号加法 - 正数+正数 (8秒)
**目的**: 展示 (+3) + (+2) = +5

### 元素
1. 标题: "同号加法: 正数+正数"
2. 公式: (+3) + (+2)
3. 起点: 0
4. 第一步箭头: 0 → +3 (绿色)
5. 第二步箭头: +3 → +5 (绿色)
6. 结果点: +5 (橙色)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 公式书写 | `Write(formula)` |
| 1.0s | 起点闪烁 | `Flash(start_dot)` |
| 1.5s | 第一步箭头生长 | `GrowArrow(arrow1)` |
| 2.5s | 第一步说明 | `FadeIn(step1_text)` |
| 3.5s | 第二步箭头生长 | `GrowArrow(arrow2)` |
| 4.5s | 第二步说明 | `FadeIn(step2_text)` |
| 5.5s | 结果闪烁 | `Flash(result_dot)` |
| 6.0s | 结论展示 | `Write(conclusion)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, formula, arrows, dots, texts, conclusion
- 保留: number_line

---

## Scene 3: 同号加法 - 负数+负数 (8秒)
**目的**: 展示 (-2) + (-3) = -5

### 元素
1. 标题: "同号加法: 负数+负数"
2. 公式: (-2) + (-3)
3. 起点: 0
4. 第一步箭头: 0 → -2 (红色)
5. 第二步箭头: -2 → -5 (红色)
6. 结果点: -5 (橙色)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 公式书写 | `Write(formula)` |
| 1.0s | 起点闪烁 | `Flash(start_dot)` |
| 1.5s | 第一步箭头生长 (向左) | `GrowArrow(arrow1)` |
| 2.5s | 第一步说明 | `FadeIn(step1_text)` |
| 3.5s | 第二步箭头生长 (向左) | `GrowArrow(arrow2)` |
| 4.5s | 第二步说明 | `FadeIn(step2_text)` |
| 5.5s | 结果闪烁 | `Flash(result_dot)` |
| 6.0s | 结论展示 | `Write(conclusion)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 4: 异号加法 - 正+负 (正数绝对值大) (9秒)
**目的**: 展示 (+5) + (-2) = +3

### 元素
1. 标题: "异号加法: 正数+负数"
2. 公式: (+5) + (-2)
3. 起点: 0
4. 第一步箭头: 0 → +5 (绿色)
5. 第二步箭头: +5 → +3 (红色，反向)
6. 结果点: +3 (橙色)
7. 说明: "正数绝对值较大, 结果为正"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 公式书写 | `Write(formula)` |
| 1.0s | 起点闪烁 | `Flash(start_dot)` |
| 1.5s | 第一步箭头 (向右) | `GrowArrow(arrow1)` |
| 2.5s | 第一步说明 | `FadeIn(step1_text)` |
| 3.5s | 第二步箭头 (向左) | `GrowArrow(arrow2)` |
| 4.5s | 第二步说明 | `FadeIn(step2_text)` |
| 5.5s | 结果闪烁 | `Flash(result_dot)` |
| 6.0s | 结论展示 | `Write(conclusion)` |
| 7.5s | 规则说明 | `FadeIn(rule_text)` |
| 8.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 5: 异号加法 - 负+正 (负数绝对值大) (9秒)
**目的**: 展示 (-5) + (+2) = -3

### 元素
1. 标题: "异号加法: 负数+正数"
2. 公式: (-5) + (+2)
3. 起点: 0
4. 第一步箭头: 0 → -5 (红色)
5. 第二步箭头: -5 → -3 (绿色，向右)
6. 结果点: -3 (橙色)
7. 说明: "负数绝对值较大, 结果为负"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 公式书写 | `Write(formula)` |
| 1.0s | 起点闪烁 | `Flash(start_dot)` |
| 1.5s | 第一步箭头 (向左) | `GrowArrow(arrow1)` |
| 2.5s | 第一步说明 | `FadeIn(step1_text)` |
| 3.5s | 第二步箭头 (向右) | `GrowArrow(arrow2)` |
| 4.5s | 第二步说明 | `FadeIn(step2_text)` |
| 5.5s | 结果闪烁 | `Flash(result_dot)` |
| 6.0s | 结论展示 | `Write(conclusion)` |
| 7.5s | 规则说明 | `FadeIn(rule_text)` |
| 8.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 6: 与零相加 (7秒)
**目的**: 展示 a + 0 = a

### 元素
1. 标题: "与零相加"
2. 公式: (+3) + 0 = +3
3. 起点: 0
4. 第一步箭头: 0 → +3 (绿色)
5. 静止说明: "加0不移动"
6. 结果: 仍在 +3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.4s | 公式书写 | `Write(formula)` |
| 1.0s | 起点闪烁 | `Flash(start_dot)` |
| 1.5s | 箭头移动到+3 | `GrowArrow(arrow)` |
| 2.5s | 到达+3 | `Flash(dot_at_3)` |
| 3.0s | 加0说明 | `Write(add_zero_text)` |
| 4.0s | 停留说明 | `FadeIn(stay_text)` |
| 5.0s | 结论 | `Write(conclusion)` |
| 6.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有场景元素
- 保留: number_line

---

## Scene 7: 总结 - 加法法则 (10秒)
**目的**: 汇总三条加法法则

### 元素
1. 大标题: "有理数加法法则"
2. 法则卡片组 (3张):
   - 法则1: 同号两数相加
   - 法则2: 异号两数相加
   - 法则3: 与零相加

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 数轴淡出 | `FadeOut(number_line)` |
| 0.5s | 大标题书写 | `Write(title)` |
| 1.5s | 法则1卡片滑入 | `card1.animate.shift(RIGHT*0)` |
| 2.5s | 法则2卡片滑入 | `card2.animate.shift(RIGHT*0)` |
| 3.5s | 法则3卡片滑入 | `card3.animate.shift(RIGHT*0)` |
| 4.5s | 重点提示 | `FadeIn(highlight)` |
| 6.0s | 等待 | `Wait(4.0)` |

### 清理
- FadeOut: 全部元素

---

## Scene 8: 片尾关注 (6秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者名放大
2. 作者ID
3. 关注提示
4. 数轴图标装饰

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, author_name)` |
| 0.8s | 作者ID淡入 | `FadeIn(author_id)` |
| 1.3s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 2.0s | 装饰图标 | `FadeIn(decorations)` |
| 3.0s | 图标旋转 | `Rotate(decorations)` |
| 5.0s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 顶部常驻 |
| number_line | Scene 1 | Scene 7 | 主数轴 |
| scene_title | Scene 2-6 | 各场景末尾 | 场景标题 |
| formula | Scene 2-6 | 各场景末尾 | 运算公式 |
| arrows | Scene 2-6 | 各场景末尾 | 移动箭头 |
| dots | Scene 2-6 | 各场景末尾 | 位置标记 |
| rule_cards | Scene 7 | Scene 7 | 法则卡片 |

---

## 关键技术点
1. **数轴精确定位**: 使用 `number_line.n2p(value)` 获取数值对应的坐标
2. **箭头方向**: 正数向右 (RIGHT)，负数向左 (LEFT)
3. **TracedPath**: 可选，用于展示移动轨迹
4. **颜色编码**: 正数绿色，负数红色，结果橙色
5. **动画节奏**: 每个加法示例 7-9 秒，便于理解

---

## 预期难点
1. **箭头起止点计算**: 必须使用 `number_line.n2p()` 精确计算
2. **箭头方向控制**: 负数加法需要反向箭头
3. **文字位置**: 避免与数轴和箭头重叠
4. **节奏控制**: 不能太快导致看不清

---

## 验证要点
- [ ] 所有箭头起止点精确对应数值
- [ ] 颜色编码一致 (正绿负红)
- [ ] 文字无重叠
- [ ] 动画节奏合理
- [ ] 总时长 60-75 秒