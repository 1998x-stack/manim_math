# 百分比的三类基本问题 - 动画分镜脚本

<!-- /root/code/sss/media/videos/percentage_problems/1920p60/PercentageProblems.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 6 个
- 难度等级: 小学/初中基础
- 目标观众: 六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要问题类型
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调重点
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键答案
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 核心概念
- 三类问题都围绕"单位1"展开
- 使用视觉化的矩形/条形图表示数量关系
- 每类问题用具体例子演示

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 主矩形 | Rectangle(width=6, height=1) | self.main_rect |
| 部分矩形 | 基于百分比缩放 | self.part_rect |
| 位置偏移 | UP * 1.5 | self.MAIN_OFFSET |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出三类问题

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "百分比的三类问题，你都会吗？"
3. 三个问号图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=1.0)` |
| 1.3s | 三个问号弹出 | `FadeIn(question_marks, scale=0.5)` |
| 2.0s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text, question_marks
- 保留: author_info

---

## Scene 2: 问题类型概览 (5-10秒)
**目的**: 展示三类问题的标题

### 元素
1. 标题: "三类基本问题"
2. 三个类型标签卡片
   - 类型一: 求部分
   - 类型二: 求百分比
   - 类型三: 求整体

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题写入 | `Write(title)` |
| 0.8s | 卡片1滑入 | `card1.animate.shift(LEFT*0)` |
| 1.2s | 卡片2滑入 | `card2.animate.shift(LEFT*0)` |
| 1.6s | 卡片3滑入 | `card3.animate.shift(LEFT*0)` |
| 2.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, cards
- 保留: author_info

---

## Scene 3: 类型一 - 求部分 (10-25秒)
**目的**: 演示 a×p% 的计算

### 核心例子
"一件衣服200元，打8折，是多少钱？"

### 元素
1. 问题文字
2. 整体矩形 (代表200元)
3. 部分矩形 (代表80%)
4. 公式: 200 × 80%
5. 答案: 160元

### 几何计算
```python
# 整体矩形
self.whole_rect = Rectangle(width=6, height=0.8, color=BLUE)
self.whole_rect.move_to(UP * 2)

# 部分矩形 (80% = 0.8)
self.part_rect = Rectangle(width=6*0.8, height=0.8, color=GREEN, fill_opacity=0.5)
self.part_rect.align_to(self.whole_rect, LEFT)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 类型标题 | `Write(type1_title)` |
| 0.8s | 问题出现 | `FadeIn(question)` |
| 1.5s | 整体矩形创建 | `Create(whole_rect)` |
| 2.5s | 标注"200元" | `FadeIn(label_200)` |
| 3.2s | 80%部分高亮 | `Create(part_rect)` |
| 4.5s | 公式写入 | `Write(formula)` |
| 5.5s | 箭头指向答案 | `GrowArrow(arrow)` |
| 6.0s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 7.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 4: 类型二 - 求百分比 (25-40秒)
**目的**: 演示 a÷b×100% 的计算

### 核心例子
"班级50人，女生30人，女生占百分之几？"

### 元素
1. 问题文字
2. 整体矩形 (50人)
3. 部分矩形 (30人)
4. 公式: 30 ÷ 50 × 100%
5. 答案: 60%

### 几何计算
```python
# 整体矩形 (50人)
self.whole_rect = Rectangle(width=6, height=0.8, color=BLUE)

# 部分矩形 (30人 = 60%)
self.part_rect = Rectangle(width=6*0.6, height=0.8, color=YELLOW, fill_opacity=0.5)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 类型标题 | `Write(type2_title)` |
| 0.8s | 问题出现 | `FadeIn(question)` |
| 1.5s | 整体矩形 | `Create(whole_rect), FadeIn(label_50)` |
| 2.5s | 部分矩形 | `Create(part_rect), FadeIn(label_30)` |
| 3.5s | 公式写入 | `Write(formula)` |
| 5.0s | 计算步骤 | `TransformMatchingTex(step1, step2)` |
| 6.0s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 7.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 5: 类型三 - 求整体 (40-55秒)
**目的**: 演示 b÷p% 的计算

### 核心例子
"一本书，已读40页，占全书的25%，全书多少页？"

### 元素
1. 问题文字
2. 部分矩形 (40页, 25%)
3. 整体矩形 (100%, 扩展显示)
4. 公式: 40 ÷ 25%
5. 答案: 160页

### 几何计算
```python
# 部分矩形 (25%)
self.part_rect = Rectangle(width=6*0.25, height=0.8, color=RED, fill_opacity=0.5)

# 整体矩形 (通过扩展动画显示)
self.whole_rect = Rectangle(width=6, height=0.8, color=BLUE)
```

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 类型标题 | `Write(type3_title)` |
| 0.8s | 问题出现 | `FadeIn(question)` |
| 1.5s | 部分矩形 | `Create(part_rect), FadeIn(label_40)` |
| 2.5s | 标注25% | `FadeIn(label_25percent)` |
| 3.5s | 公式写入 | `Write(formula)` |
| 4.5s | 扩展到整体 | `Transform(part_rect, whole_rect)` |
| 5.5s | 答案闪现 | `FadeIn(answer), Flash(answer)` |
| 6.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素
- 保留: author_info

---

## Scene 6: 总结与关注 (55-65秒)
**目的**: 总结三类问题，引导关注

### 元素
1. 总结标题: "掌握三类问题"
2. 三个公式卡片
3. 关键提示: "找准'单位1'"
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 0.8s | 公式卡片出现 | `FadeIn(cards)` |
| 2.0s | 关键提示闪烁 | `Flash(key_point)` |
| 3.0s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 4.0s | 关注提示 | `FadeIn(follow_text)` |
| 5.0s | 装饰动画 | `Rotate(decorations)` |
| 7.0s | 全部淡出 | `FadeOut(VGroup(*all))` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 开场钩子 |
| type_cards | Scene 2 | Scene 2 | 类型概览 |
| whole_rect_1 | Scene 3 | Scene 3 | 类型一整体 |
| part_rect_1 | Scene 3 | Scene 3 | 类型一部分 |
| whole_rect_2 | Scene 4 | Scene 4 | 类型二整体 |
| part_rect_2 | Scene 4 | Scene 4 | 类型二部分 |
| part_rect_3 | Scene 5 | Scene 5 | 类型三部分 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 动画节奏控制
- 每个类型问题: 13-15秒
- 理解停顿: 2秒（每个答案后）
- 场景切换: 0.5秒
- 总时长: 约65秒

## 字体大小规范
- 标题: 36-40
- 问题文字: 28-32
- 公式: 32-36
- 标签: 22-24
- 作者信息: 20

## 关键设计原则
1. 使用矩形条形图直观展示数量关系
2. 颜色编码不同类型的问题
3. 动画强调"单位1"的概念
4. 每个例子都有明确的视觉化过程
5. 公式与图形同步展示