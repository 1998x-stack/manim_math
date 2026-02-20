# 命题与证明 - 动画分镜脚本

## 元信息
- **目标时长**: 70-85秒
- **场景数量**: 8个
- **难度等级**: 基础
- **年级**: 八年级
- **知识点**: 命题与证明的基本概念

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要内容
COLOR_CONDITION = "#e74c3c"      # 红色 - 条件
COLOR_CONCLUSION = "#2ecc71"     # 绿色 - 结论
COLOR_TRUE = "#2ecc71"           # 绿色 - 真命题
COLOR_FALSE = "#e74c3c"          # 红色 - 假命题
COLOR_PROOF = "#9b59b6"          # 紫色 - 证明
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
COLOR_BACKGROUND = "#1a1a2e"
```

## 核心元素定义
这是纯理论主题，不涉及几何计算。主要元素：
- 命题示例（Text + MathTex）
- 结构拆解（箭头、括号标注）
- 证明格式展示（规范书写）
- 真假命题对比

---

## Scene 1: 开场钩子 (0-4秒)
**目的**: 引出命题的概念

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题："这句话是真的还是假的？"
3. 示例语句："如果下雨，那么地面会湿"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.9)` |
| 1.2s | 示例语句出现 | `FadeIn(statement, shift=UP)` |
| 2.2s | 问号闪烁 | `Flash(question_mark)` |
| 2.8s | 等待 | `Wait(0.5)` |

### 清理
- FadeOut: hook_text, statement, question_mark
- 保留: author_info

---

## Scene 2: 命题的定义 (4-11秒)
**目的**: 介绍命题的概念和特点

### 元素
1. 标题："什么是命题？"
2. 定义："可以判断真假的语句"
3. 关键特点框：
   - ✓ 能判断真假
   - ✓ 是陈述句
   - ✓ 只有一个答案

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 4.0s | 标题写入 | `Write(title)` |
| 4.8s | 定义出现 | `FadeIn(definition, shift=UP)` |
| 5.8s | 关键特点1 | `FadeIn(feature_1, shift=LEFT)` |
| 6.8s | 关键特点2 | `FadeIn(feature_2, shift=LEFT)` |
| 7.8s | 关键特点3 | `FadeIn(feature_3, shift=LEFT)` |
| 8.8s | 框选整体 | `Create(surrounding_box)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 3: 命题的结构 (11-20秒)
**目的**: 拆解命题的条件和结论

### 元素
1. 副标题："命题的结构"
2. 标准格式："若p，则q"
3. 具体示例："若两角是对顶角，则这两角相等"
4. 结构标注：
   - 条件（p）- 用红色
   - 结论（q）- 用绿色
   - 箭头连接

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 11.0s | 副标题 | `Write(subtitle)` |
| 11.6s | 标准格式 | `Write(standard_format)` |
| 12.6s | 具体示例 | `Write(example)` |
| 13.6s | 标注条件 | `Indicate(condition), Brace(condition)` |
| 14.6s | 标注结论 | `Indicate(conclusion), Brace(conclusion)` |
| 15.6s | 箭头连接 | `GrowArrow(arrow)` |
| 16.6s | 说明文字 | `FadeIn(explanation)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 4: 真命题与假命题 (20-30秒)
**目的**: 区分真假命题

### 元素
1. 副标题："真命题 vs 假命题"
2. 左侧：真命题示例
   - "若a=b，则a+c=b+c" ✓
   - 颜色：绿色
3. 右侧：假命题示例
   - "若a>b，则a²>b²" ✗
   - 颜色：红色
4. 反例：a=-3, b=-2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 20.0s | 副标题 | `Write(subtitle)` |
| 20.6s | 真命题示例 | `FadeIn(true_prop, shift=LEFT)` |
| 21.6s | 绿色勾号 | `FadeIn(check_mark, scale=1.5)` |
| 22.6s | 假命题示例 | `FadeIn(false_prop, shift=RIGHT)` |
| 23.6s | 红色叉号 | `FadeIn(cross_mark, scale=1.5)` |
| 24.6s | 反例说明 | `FadeIn(counter_example)` |
| 25.6s | 计算展示 | `Write(calculation)` |
| 26.8s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 5: 定理的概念 (30-38秒)
**目的**: 介绍定理与真命题的关系

### 元素
1. 副标题："什么是定理？"
2. 定义："经过证明的真命题"
3. 流程图：
   - 真命题 → 证明 → 定理
4. 例子："勾股定理"、"三角形内角和定理"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 30.0s | 副标题 | `Write(subtitle)` |
| 30.6s | 定义 | `FadeIn(definition)` |
| 31.6s | 流程图1 | `FadeIn(box_1)` |
| 32.3s | 箭头1 | `GrowArrow(arrow_1)` |
| 32.8s | 流程图2 | `FadeIn(box_2)` |
| 33.3s | 箭头2 | `GrowArrow(arrow_2)` |
| 33.8s | 流程图3 | `FadeIn(box_3)` |
| 34.8s | 例子列表 | `FadeIn(examples)` |
| 35.8s | 高亮 | `Indicate(examples)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 6: 什么是证明 (38-48秒)
**目的**: 介绍证明的概念和过程

### 元素
1. 副标题："什么是证明？"
2. 定义："从已知到结论的推理过程"
3. 证明三要素：
   - 已知条件（起点）
   - 逻辑推理（过程）
   - 得出结论（终点）
4. 推理依据：
   - 定义
   - 公理
   - 已证定理

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 38.0s | 副标题 | `Write(subtitle)` |
| 38.6s | 定义 | `FadeIn(definition)` |
| 39.6s | 三要素依次出现 | `FadeIn(element_1/2/3)` |
| 42.0s | 箭头连接 | `GrowArrow(arrows)` |
| 43.0s | 推理依据标题 | `Write(basis_title)` |
| 43.8s | 依据列表 | `FadeIn(basis_list)` |
| 45.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 7: 证明的格式 (48-60秒)
**目的**: 展示规范的证明书写格式

### 元素
1. 副标题："证明的规范格式"
2. 完整证明示例：
   ```
   已知：∠1和∠2是对顶角
   求证：∠1 = ∠2
   证明：∵ ∠1和∠2是对顶角（已知）
        ∴ ∠1 + ∠3 = 180°（平角定义）
           ∠2 + ∠3 = 180°（平角定义）
        ∴ ∠1 + ∠3 = ∠2 + ∠3（等量代换）
        ∴ ∠1 = ∠2（等式性质）
   ```
3. 格式标注：
   - "已知"部分（红色框）
   - "求证"部分（绿色框）
   - "证明"部分（紫色框）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 48.0s | 副标题 | `Write(subtitle)` |
| 48.6s | 已知部分 | `Write(given)` |
| 49.6s | 框选已知 | `Create(given_box)` |
| 50.3s | 求证部分 | `Write(prove)` |
| 51.3s | 框选求证 | `Create(prove_box)` |
| 52.0s | 证明部分逐行 | `Write(proof_line_1/2/3...)` |
| 56.0s | 框选证明 | `Create(proof_box)` |
| 57.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 8: 总结与片尾 (60-72秒)
**目的**: 总结要点，引导关注

### 元素
1. 标题："命题与证明 - 要点总结"
2. 四个要点：
   - ① 命题 = 能判断真假的语句
   - ② 命题 = 条件 + 结论（若p则q）
   - ③ 真命题经证明后 → 定理
   - ④ 证明要用规范格式（已知→求证→证明）
3. 关键提示
4. 作者信息与关注引导

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 60.0s | 标题 | `Write(summary_title)` |
| 60.8s | 要点1 | `FadeIn(point_1, shift=UP)` |
| 62.0s | 要点2 | `FadeIn(point_2, shift=UP)` |
| 63.2s | 要点3 | `FadeIn(point_3, shift=UP)` |
| 64.4s | 要点4 | `FadeIn(point_4, shift=UP)` |
| 65.6s | 关键提示 | `FadeIn(key_point, scale=1.1)` |
| 66.8s | 作者放大 | `Transform(author_info, author_large)` |
| 67.5s | 关注提示 | `FadeIn(follow_text)` |
| 68.5s | 装饰符号 | `Rotate(decorations)` |
| 70.0s | 等待 | `Wait(1.5)` |
| 71.5s | 全部淡出 | `FadeOut(VGroup(*))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留，最后放大 |
| various_content | Scene 2-7 | Scene 2-7 | 每个场景独立 |
| summary_content | Scene 8 | Scene 8 | 总结内容 |

---

## 技术要点

### 1. 文字与公式混排
```python
# 使用 VGroup 组合 Text 和 MathTex
statement = VGroup(
    Text("若", font="Noto Sans CJK SC"),
    MathTex(r"a=b"),
    Text("，则", font="Noto Sans CJK SC"),
    MathTex(r"a+c=b+c")
).arrange(RIGHT, buff=0.15)
```

### 2. 条件结论标注
```python
# 使用 Brace 标注
condition = MathTex(r"p")
brace = Brace(condition, DOWN, color=RED)
label = Text("条件", font="Noto Sans CJK SC").next_to(brace, DOWN)
```

### 3. 箭头连接
```python
arrow = Arrow(start, end, color=YELLOW, buff=0.1)
self.play(GrowArrow(arrow))
```

### 4. 框选结构
```python
box = SurroundingRectangle(
    content,
    color=COLOR,
    buff=0.2,
    corner_radius=0.1
)
```

### 5. 对比布局
```python
# 左右对比
true_content.move_to(LEFT * 2.5 + UP * 1)
false_content.move_to(RIGHT * 2.5 + UP * 1)
```

---

## 验证清单

### 内容正确性
- [ ] 命题定义准确
- [ ] 真假命题示例正确
- [ ] 证明格式规范

### LaTeX 正确性
- [ ] 无中文字符在 MathTex 中
- [ ] 符号使用正确（∵ ∴）
- [ ] 不等号、等号正确

### 视觉效果
- [ ] 颜色区分清晰（条件/结论）
- [ ] 文字不溢出边界
- [ ] 对比布局合理

### 节奏控制
- [ ] 每个概念有足够展示时间
- [ ] 关键内容有停留
- [ ] 总时长70-85秒

---

## 边界参考 (TikTok竖屏)
```
┌─────────────────────────────┐  y = +8
│  顶部：作者信息             │  y = +7 ~ +6.3
├─────────────────────────────┤  y = +5.5
│                             │
│  主内容区域：                │  y ∈ [-4.5, +5]
│  - 标题（y ∈ [+4.5, +5.5]） │
│  - 定义/示例（y ∈ [+2, +4]）│
│  - 详细内容（y ∈ [-3, +2]） │
│                             │
├─────────────────────────────┤  y = -4.5
│  底部：说明文字             │  y ∈ [-6, -4.5]
├─────────────────────────────┤  y = -6
│  底部安全区                  │  y = -8
└─────────────────────────────┘

横向: x ∈ [-4, +4] (安全区域)
```

---

## 特殊注意事项

### 1. 中文与数学符号混排
- 命题语句中"若"、"则"用Text()
- 数学表达式用MathTex()
- 组合使用VGroup

### 2. 逻辑符号
- ∵ (因为): `\because`
- ∴ (所以): `\therefore`
- 确保在MathTex中使用

### 3. 证明格式对齐
- 使用aligned_edge=LEFT确保左对齐
- 缩进使用空格或shift

### 4. 真假对比
- 真命题用绿色+勾号✓
- 假命题用红色+叉号✗
- 视觉对比强烈

---

## 动画节奏指南

| 内容类型 | 建议时长 |
|---------|---------|
| 概念定义 | 0.8-1.2s |
| 示例展示 | 1.0-1.5s |
| 结构拆解 | 1.5-2.0s |
| 证明展示 | 8-12s |
| 关键停顿 | 1.0-1.5s |
| 总结要点 | 6-8s |