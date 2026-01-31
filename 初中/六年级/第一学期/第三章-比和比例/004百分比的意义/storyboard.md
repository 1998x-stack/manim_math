# 百分比的意义 - 动画分镜脚本

<!-- /root/code/sss/media/videos/percentage_meaning/1920p60/PercentageMeaning.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 简单
- 目标年级: 六年级

## 颜色配置
```python
COLOR_PERCENT = "#e74c3c"       # 红色 - 百分比
COLOR_FRACTION = "#3498db"      # 蓝色 - 分数
COLOR_DECIMAL = "#2ecc71"       # 绿色 - 小数
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
COLOR_FILLED = "#f39c12"        # 橙色 - 填充区域
COLOR_EMPTY = "#34495e"         # 深灰 - 空白区域
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 圆心 | ORIGIN | self.circle_center |
| 百分比扇形角度 | percent/100 * 2π | self.sector_angle |
| 100格子位置 | 网格计算 | self.grid_positions |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 生活场景引入,激发兴趣

### 元素
1. 作者标识 (顶部)
2. 钩子问题: "考试成绩85%是什么意思?"
3. 百分号图标

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 百分号85%放大 | `Write(percent_symbol).scale(2)` |
| 2.5s | 闪烁强调 | `Flash(percent_symbol)` |
| 3.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text, percent_symbol
- 保留: author_info

---

## Scene 2: 百分比定义 (10秒)
**目的**: 明确百分比的概念

### 元素
1. 标题: "什么是百分比?"
2. 定义框
3. 百分号%的含义
4. 后项固定为100

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 定义框滑入 | `FadeIn(definition_box, scale=0.9)` |
| 1.2s | 定义文字 | `Write(definition_text)` |
| 3.0s | %符号分解 | `Create(percent_parts)` |
| 4.5s | 标注100 | `Indicate(hundred_part)` |
| 6.0s | 示例25% | `Write(example)` |
| 7.5s | 说明:25/100 | `TransformMatchingShapes` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 大部分元素
- 保留: 核心公式

---

## Scene 3: 视觉化理解 - 100格子 (12秒)
**目的**: 用100格子直观展示百分比

### 元素
1. 10×10网格 (共100格)
2. 逐步填充25格
3. 标注: 25格/100格 = 25%

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 网格出现 | `Create(grid)` |
| 1.0s | 标注总数100 | `FadeIn(total_label)` |
| 2.0s | 开始填充 | `LaggedStart(FadeIn格子)` |
| 5.0s | 填充完25格 | 完成 |
| 6.0s | 标注25格 | `Indicate(filled_squares)` |
| 7.0s | 等式出现 | `Write(equation)` |
| 9.0s | 变换为25% | `Transform` |
| 11.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: grid, labels
- 保留: 无

---

## Scene 4: 圆形图示 (10秒)
**目的**: 用扇形图展示百分比

### 元素
1. 完整圆形
2. 25%扇形
3. 75%扇形
4. 标注百分比

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 圆形出现 | `Create(circle)` |
| 1.0s | 分割扇形 | `Create(sector_25)` |
| 2.5s | 填充25% | `sector_25.animate.set_fill(opacity=0.6)` |
| 3.5s | 标注25% | `Write(label_25)` |
| 4.5s | 标注75% | `Write(label_75)` |
| 6.0s | 旋转展示 | `Rotate(circle_group)` |
| 8.0s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 5: 三者关系 (15秒)
**目的**: 核心内容 - 百分比、分数、小数的互化

### 元素
1. 标题: "百分比的三种形式"
2. 核心公式: a% = a/100 = 0.01a
3. 具体示例: 25% = 1/4 = 0.25
4. 变换动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 百分比形式 | `Write(percent_form)` |
| 2.5s | 变换为分数 | `TransformMatchingShapes(to_fraction)` |
| 4.0s | 变换为小数 | `TransformMatchingShapes(to_decimal)` |
| 5.5s | 三者并列 | `VGroup.arrange()` |
| 6.5s | 等号连接 | `Write(equal_signs)` |
| 7.5s | 框选强调 | `Create(box)` |
| 8.5s | 示例标题 | `FadeIn(example_title)` |
| 9.0s | 25% = 25/100 | `Write` 逐步展开 |
| 11.0s | 化简为1/4 | `Transform` |
| 12.5s | =0.25 | `Write` |
| 14.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 大部分元素
- 保留: 核心公式(缩小)

---

## Scene 6: 常用百分比 (10秒)
**目的**: 展示常见百分比及其对应

### 元素
1. 标题: "常用百分比"
2. 四个示例:
   - 50% = 1/2 = 0.5
   - 25% = 1/4 = 0.25
   - 75% = 3/4 = 0.75
   - 10% = 1/10 = 0.1
3. 表格展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 表格出现 | `Create(table)` |
| 1.5s | 50%行 | `FadeIn(row_1)` |
| 2.5s | 25%行 | `FadeIn(row_2)` |
| 3.5s | 75%行 | `FadeIn(row_3)` |
| 4.5s | 10%行 | `FadeIn(row_4)` |
| 5.5s | 全部高亮 | `Indicate(table)` |
| 7.0s | 提示记忆 | `FadeIn(hint)` |
| 9.0s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: 所有元素
- 保留: 无

---

## Scene 7: 应用场景 + 结尾 (12秒)
**目的**: 展示实际应用,结束

### 元素
1. 标题: "百分比在生活中"
2. 三个应用:
   - 📊 考试成绩 (85%)
   - 💰 打折优惠 (20% off)
   - 📈 增长率 (+15%)
3. 作者信息
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` |
| 1.0s | 场景1 | `FadeIn(scene_1)` |
| 2.5s | 场景2 | `FadeIn(scene_2)` |
| 4.0s | 场景3 | `FadeIn(scene_3)` |
| 5.5s | 全部高亮 | `Indicate(scenes)` |
| 6.5s | 淡出场景 | `FadeOut(scenes)` |
| 7.0s | 作者放大 | `author.animate.scale(1.5)` |
| 8.0s | 关注提示 | `FadeIn(follow_text)` |
| 9.0s | 关键词 | `FadeIn(keywords)` |
| 11.0s | 全部淡出 | `FadeOut(everything)` |

### 清理
- 全部清空

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终在顶部 |
| definition_box | Scene 2 | Scene 2 | 定义框 |
| grid | Scene 3 | Scene 3 | 100格子 |
| circle | Scene 4 | Scene 4 | 圆形图 |
| formula | Scene 5 | Scene 7 | 核心公式 |
| table | Scene 6 | Scene 6 | 常用百分比表 |

---

## 节奏控制要点
1. **开场要快** (4秒内引入)
2. **定义要清晰** (10秒详细讲解)
3. **视觉化是亮点** (网格+圆形,22秒)
4. **关系是核心** (三者互化,15秒重点)
5. **结尾轻松** (应用场景,12秒)

## 字体大小使用
- 标题: 36
- 副标题: 28
- 百分比(大): 60
- 百分比(正常): 36
- 说明文字: 22
- 标注: 20
- 小字: 18

## 特殊效果
1. **网格填充**: LaggedStart 逐格填充
2. **扇形旋转**: Rotate 展示角度
3. **变换动画**: TransformMatchingShapes 展示等价
4. **表格渐显**: 逐行出现
5. **百分号分解**: %拆分为/100