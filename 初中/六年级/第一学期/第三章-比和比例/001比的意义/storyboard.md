# 比的意义 - 动画分镜脚本

## 元信息
- 目标时长: 55-70 秒
- 场景数量: 6 个
- 难度等级: 简单
- 目标年级: 六年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 前项
COLOR_SECONDARY = "#e74c3c"    # 红色 - 后项
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 比值
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
COLOR_RELATION = GOLD          # 金色 - 关系强调
COLOR_WARNING = ORANGE         # 橙色 - 警告(后项不能为0)
```

## 几何预计算清单
本题目主要涉及文字、公式和图示,无复杂几何计算

---

## Scene 1: 开场钩子 (4秒)
**目的**: 生活场景引入,激发兴趣

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "一杯果汁:水=2:3是什么意思?"
3. 两个杯子图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 左杯子出现(果汁) | `FadeIn(cup_juice, scale=0.8)` |
| 1.4s | 右杯子出现(水) | `FadeIn(cup_water, scale=0.8)` |
| 2.0s | 比例符号2:3 | `Write(ratio_symbol)` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, cups
- 保留: author_info

---

## Scene 2: 比的定义 (10秒)
**目的**: 明确比的概念和写法

### 元素
1. 标题: "什么是比?"
2. 定义框
3. 两种写法: a:b 和 a/b
4. 示例: 2:3

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 定义框滑入 | `FadeIn(definition_box, scale=0.9)` |
| 1.2s | 定义文字书写 | `Write(definition_text)` |
| 3.0s | 写法1: a:b | `Write(format_1)` |
| 3.8s | 写法2: a/b | `Write(format_2)` |
| 4.5s | 示例出现 | `FadeIn(example)` |
| 5.5s | 箭头标注前项后项 | `GrowArrow(arrows)` |
| 7.0s | 标注说明 | `FadeIn(labels)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, definition_box
- 保留: format_1, format_2 (缩小移到角落)

---

## Scene 3: 比的各部分名称 (8秒)
**目的**: 介绍前项、后项、比值

### 元素
1. 标题: "比的组成"
2. 大号比式: 6 : 3
3. 标注: 前项、后项、比号
4. 比值计算: 6÷3=2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 0.6s | 比式出现 | `Write(ratio_large)` |
| 1.2s | 前项标注 | `FadeIn(label_前项), Indicate(num_6)` |
| 2.0s | 后项标注 | `FadeIn(label_后项), Indicate(num_3)` |
| 2.8s | 比号标注 | `FadeIn(label_比号), Indicate(colon)` |
| 3.6s | 比值说明 | `FadeIn(ratio_value_text)` |
| 4.5s | 计算过程 | `Write(calculation)` |
| 6.0s | 结果高亮 | `result.animate.set_color(GOLD).scale(1.3)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 4: 三者关系 (15秒)
**目的**: 核心内容 - 比、除法、分数的关系

### 元素
1. 标题: "比的三种形式"
2. 三个等式: a:b = a÷b = a/b
3. 变形动画展示关系
4. 具体示例: 4:5 = 4÷5 = 4/5 = 0.8

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 比式出现 | `Write(ratio_form)` |
| 2.0s | 变换为除法 | `TransformMatchingTex(ratio_form, division_form)` |
| 3.5s | 变换为分数 | `TransformMatchingTex(division_form, fraction_form)` |
| 5.0s | 三者并列 | `VGroup(ratio, division, fraction).arrange()` |
| 6.0s | 等号连接 | `Write(equal_signs)` |
| 7.0s | 示例标题 | `FadeIn(example_title)` |
| 7.5s | 示例计算 | `Write(example_calc)` |
| 9.0s | 逐步展开 | `TransformMatchingTex` 连续变换 |
| 11.0s | 最终结果 | `result.animate.set_color(GOLD)` |
| 12.0s | 关系图示 | `Create(relationship_diagram)` |
| 14.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 大部分元素
- 保留: 核心公式(缩小)

---

## Scene 5: 重要提醒 (8秒)
**目的**: 强调后项不能为0

### 元素
1. 警告框
2. 文字: "重要: 比的后项不能为0"
3. 错误示例: 5:0 ✗
4. 解释: 因为除数不能为0

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 警告框弹出 | `FadeIn(warning_box, scale=1.2)` |
| 0.5s | 警告文字 | `Write(warning_text, color=ORANGE)` |
| 1.5s | 错误示例 | `Write(wrong_example)` |
| 2.3s | 叉号 | `Write(cross_mark), Flash(cross_mark)` |
| 3.0s | 解释原因 | `FadeIn(explanation)` |
| 4.0s | 关联图示 | `Create(connection_lines)` |
| 5.5s | 强调闪烁 | `Indicate(warning_box)` |
| 7.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有警告元素
- 保留: 无

---

## Scene 6: 实际应用 + 结尾 (12秒)
**目的**: 展示应用场景,结束

### 元素
1. 标题: "比在生活中"
2. 三个应用场景:
   - 调配饮料 (水:糖浆 = 3:1)
   - 地图比例 (图上:实际 = 1:100000)
   - 配方比例 (面粉:水 = 5:3)
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 场景1出现 | `FadeIn(scene_1, shift=UP*0.3)` |
| 2.5s | 场景2出现 | `FadeIn(scene_2, shift=UP*0.3)` |
| 4.0s | 场景3出现 | `FadeIn(scene_3, shift=UP*0.3)` |
| 5.5s | 全部高亮 | `Indicate(scenes)` |
| 6.5s | 场景淡出 | `FadeOut(scenes)` |
| 7.0s | 作者信息放大 | `author_info.animate.scale(1.5).move_to(UP)` |
| 8.0s | 关注提示 | `FadeIn(follow_text)` |
| 9.0s | 关键词标签 | `FadeIn(keywords)` |
| 11.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 始终在顶部 |
| cups | Scene 1 | Scene 1 | 开场道具 |
| definition_box | Scene 2 | Scene 2 | 定义框 |
| ratio_forms | Scene 2 | Scene 4 | 比的写法 |
| warning_box | Scene 5 | Scene 5 | 警告信息 |
| scenes | Scene 6 | Scene 6 | 应用场景 |

---

## 节奏控制要点
1. **开场要快** (4秒内引入)
2. **定义要清晰** (慢速讲解,10秒)
3. **关系是重点** (核心,15秒详细展示)
4. **警告要醒目** (8秒强调)
5. **结尾轻松** (应用场景放松节奏)

## 字体大小使用
- 标题: 36
- 副标题: 28
- 比式(大): 48
- 比式(正常): 32
- 说明文字: 22
- 标注: 20
- 作者信息: 20

## 特殊效果
1. **变换动画**: TransformMatchingTex 展示等价关系
2. **警告框**: 橙色边框 + 闪烁效果
3. **高亮强调**: Indicate + 颜色变化
4. **渐进展示**: LaggedStart 分步出现