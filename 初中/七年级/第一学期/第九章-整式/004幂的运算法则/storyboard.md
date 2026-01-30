# 幂的运算法则 - 动画分镜脚本

<!-- /root/code/sss/media/videos/power_operation_laws/1920p60/PowerOperationLaws.mp4 -->
## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 中等
- 目标年级: 七年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要公式
COLOR_SECONDARY = "#e74c3c"    # 红色 - 底数
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调
COLOR_EXPONENT = "#2ecc71"     # 绿色 - 指数
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 核心教学要点
1. 同底数幂相乘：底数不变，指数相加
2. 幂的乘方：底数不变，指数相乘
3. 积的乘方：每个因数分别乘方
4. 同底数幂相除：底数不变，指数相减

## 几何预计算清单
| 元素 | 计算说明 | 存储变量 |
|------|---------|---------|
| 无复杂几何 | 主要使用MathTex和Text | N/A |
| 公式位置 | y ∈ [-1, 3] 主内容区 | self.FORMULA_Y |
| 说明位置 | y ∈ [-4, -2] 底部说明 | self.EXPLAIN_Y |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识（顶部小字）
2. 钩子问题："2³ × 2⁵ = ?"
3. 思考提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_question)` |
| 1.5s | 提示文字浮现 | `FadeIn(hint)` |
| 3.0s | 问号闪烁 | `Flash(question_mark)` |
| 4.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_question, hint
- 保留: author_info

---

## Scene 2: 法则一 - 同底数幂相乘 (5-18秒)
**目的**: 教授第一个运算法则

### 元素
1. 标题："法则一：同底数幂相乘"
2. 公式展示：aᵐ × aⁿ = aᵐ⁺ⁿ
3. 具体例子：2³ × 2⁵ = 2⁸
4. 可视化解释：2³ = 2×2×2, 2⁵ = 2×2×2×2×2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 5.0s | 标题滑入 | `FadeIn(title, shift=DOWN)` |
| 5.8s | 通用公式书写 | `Write(formula_general)` |
| 7.5s | 关键提示出现 | `FadeIn(key_point)` |
| 9.0s | 具体例子书写 | `Write(example)` |
| 10.5s | 展开2³ | `TransformMatchingTex()` |
| 12.0s | 展开2⁵ | `TransformMatchingTex()` |
| 13.5s | 合并计数 | `Transform()` |
| 15.0s | 显示答案2⁸ | `Write(answer)` |
| 16.5s | 停留理解 | `Wait(1.5)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 3: 法则二 - 幂的乘方 (18-28秒)
**目的**: 教授第二个运算法则

### 元素
1. 标题："法则二：幂的乘方"
2. 公式展示：(aᵐ)ⁿ = aᵐⁿ
3. 具体例子：(2³)² = 2⁶
4. 可视化解释

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 18.0s | 标题滑入 | `FadeIn(title, shift=DOWN)` |
| 18.8s | 通用公式书写 | `Write(formula_general)` |
| 20.5s | 关键提示出现 | `FadeIn(key_point)` |
| 21.5s | 具体例子书写 | `Write(example)` |
| 23.0s | 展开含义 | `TransformMatchingTex()` |
| 24.5s | 显示答案 | `Write(answer)` |
| 26.0s | 停留理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 4: 法则三 - 积的乘方 (28-38秒)
**目的**: 教授第三个运算法则

### 元素
1. 标题："法则三：积的乘方"
2. 公式展示：(ab)ⁿ = aⁿbⁿ
3. 具体例子：(2×3)² = 2²×3²
4. 计算验证

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 28.0s | 标题滑入 | `FadeIn(title, shift=DOWN)` |
| 28.8s | 通用公式书写 | `Write(formula_general)` |
| 30.5s | 关键提示出现 | `FadeIn(key_point)` |
| 31.5s | 具体例子书写 | `Write(example)` |
| 33.0s | 分别计算 | `TransformMatchingTex()` |
| 34.5s | 显示答案 | `Write(answer)` |
| 36.0s | 停留理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 5: 法则四 - 同底数幂相除 (38-48秒)
**目的**: 教授第四个运算法则

### 元素
1. 标题："法则四：同底数幂相除"
2. 公式展示：aᵐ ÷ aⁿ = aᵐ⁻ⁿ (a≠0)
3. 具体例子：2⁵ ÷ 2³ = 2²
4. 可视化解释

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 38.0s | 标题滑入 | `FadeIn(title, shift=DOWN)` |
| 38.8s | 通用公式书写 | `Write(formula_general)` |
| 40.5s | 关键提示和条件 | `FadeIn(key_point, condition)` |
| 42.0s | 具体例子书写 | `Write(example)` |
| 43.5s | 展开解释 | `TransformMatchingTex()` |
| 45.0s | 显示答案 | `Write(answer)` |
| 46.5s | 停留理解 | `Wait(1.5)` |

### 清理
- FadeOut: 所有当前元素
- 保留: author_info

---

## Scene 6: 四法则总结 (48-58秒)
**目的**: 汇总四个法则，加深记忆

### 元素
1. 标题："幂的运算四大法则"
2. 四个公式卡片并列展示
3. 记忆口诀

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 48.0s | 标题书写 | `Write(title)` |
| 49.0s | 法则1卡片滑入 | `card_1.animate.shift(RIGHT)` |
| 50.0s | 法则2卡片滑入 | `card_2.animate.shift(RIGHT)` |
| 51.0s | 法则3卡片滑入 | `card_3.animate.shift(RIGHT)` |
| 52.0s | 法则4卡片滑入 | `card_4.animate.shift(RIGHT)` |
| 53.5s | 口诀显示 | `FadeIn(mnemonic)` |
| 55.0s | 所有卡片闪烁 | `Flash()` for all cards |
| 56.5s | 停留理解 | `Wait(1.5)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 7: 片尾关注 (58-65秒)
**目的**: 引导关注，增强互动

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 58.0s | 作者名放大 | `Transform(author_info)` |
| 58.8s | ID显示 | `FadeIn(author_id)` |
| 59.5s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 60.5s | 装饰动画 | `Rotate(decorations)` |
| 62.5s | 停留 | `Wait(1.5)` |
| 64.0s | 全部淡出 | `FadeOut()` all |

### 清理
- 全部元素淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留在顶部 |
| hook_question | Scene 1 | Scene 1 | 开场钩子 |
| formula_general | Scene 2-5 | 各场景结束 | 通用公式 |
| example | Scene 2-5 | 各场景结束 | 具体例子 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 技术要点
1. **字体使用**: 中文用Text("...", font="Noto Sans CJK SC")，数学用MathTex(r"...")
2. **上标处理**: 使用LaTeX语法 `^` 而非 Unicode 上标字符
3. **颜色高亮**: 使用set_color_by_tex()对关键部分着色
4. **动画节奏**: 难点（法则理解）停留2秒，简单转场0.5秒
5. **边界控制**: 公式区域y∈[-1,3]，说明区域y∈[-4,-2]

## 预期学习效果
- 学生能记住四个幂运算法则
- 理解"底数不变"的核心思想
- 能够区分相加、相乘、相减的应用场景