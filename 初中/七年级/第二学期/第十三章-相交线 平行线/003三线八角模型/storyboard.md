# 三线八角模型 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中七年级
- 核心概念: 两条直线被第三条直线所截形成的8个角及其分类

## 颜色配置
```python
COLOR_LINE_1 = "#3498db"      # 蓝色 - 被截线1
COLOR_LINE_2 = "#e74c3c"      # 红色 - 被截线2
COLOR_LINE_3 = "#2ecc71"      # 绿色 - 截线
COLOR_SAME_SIDE = "#f39c12"   # 橙色 - 同位角
COLOR_ALTERNATE = "#9b59b6"   # 紫色 - 内错角
COLOR_CONSECUTIVE = "#e67e22" # 深橙 - 同旁内角
COLOR_HIGHLIGHT = YELLOW
COLOR_AUXILIARY = GRAY_B
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 被截线1起点 | 固定坐标 | self.L1_start | 左上到右下倾斜 |
| 被截线1终点 | 固定坐标 | self.L1_end | 左上到右下倾斜 |
| 被截线2起点 | 固定坐标 | self.L2_start | 平行于L1 |
| 被截线2终点 | 固定坐标 | self.L2_end | 平行于L1 |
| 截线起点 | 固定坐标 | self.L3_start | 左下到右上穿过两线 |
| 截线终点 | 固定坐标 | self.L3_end | 左下到右上穿过两线 |
| 交点P | 截线与L1交点 | self.P | 精确计算 |
| 交点Q | 截线与L2交点 | self.Q | 精确计算 |
| 8个角的顶点 | P和Q | - | 每个交点4个角 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (醒目大字)
3. 三条线的简单草图

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "两条线被一条线截，会产生几个角?" |
| 1.2s | 三条线快速创建 | `Create(line1, line2, line3)` |
| 2.5s | 问号闪烁 | `Flash(question_mark)` |
| 3.0s | 等待 | `self.wait(0.5)` |

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, line1, line2, line3

---

## Scene 2: 构建三线八角 (8-10秒)
**目的**: 清晰展示三线八角的形成过程

### 元素
1. 两条平行的被截线（蓝色和红色）
2. 一条截线（绿色）
3. 两个交点P和Q
4. 8个角的标记（∠1-∠8）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` - "三线八角模型" |
| 0.5s | 被截线1创建 | `Create(line1)` - 蓝色，左上到右下 |
| 1.0s | 被截线2创建 | `Create(line2)` - 红色，平行于line1 |
| 1.5s | 说明文字 | `FadeIn(explain1)` - "两条被截线" |
| 2.5s | 截线创建 | `Create(line3)` - 绿色，穿过两线 |
| 3.0s | 交点P标记 | `FadeIn(dot_P, label_P)` |
| 3.5s | 交点Q标记 | `FadeIn(dot_Q, label_Q)` |
| 4.0s | 说明文字更新 | `Transform(explain1, explain2)` - "截线与两条线形成两个交点" |
| 5.0s | 8个角依次标记 | 循环 `FadeIn(angle_1 to angle_8)` |
| 7.5s | 总结文字 | `FadeIn(summary)` - "共形成8个角" |
| 8.5s | 等待 | `self.wait(1.0)` |

### 清理
- FadeOut: explain1, explain2, summary
- 保留: line1, line2, line3, 8个角标记, 交点

---

## Scene 3: 同位角 (10-12秒)
**目的**: 定义并高亮同位角

### 元素
1. 定义文字
2. 4对同位角的高亮
3. 位置说明图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "同位角 Corresponding Angles" |
| 0.6s | 定义 | `FadeIn(definition)` - "在截线同侧，被截两线的同侧" |
| 1.5s | 位置说明 | `FadeIn(position_hint)` - "位置相同的角" |
| 2.5s | 第1对同位角高亮 | `Indicate(angle_1, angle_5)` - ∠1和∠5 |
| 3.5s | 标注 | `FadeIn(label)` - "∠1 = ∠5 (同位角)" |
| 4.5s | 第2对同位角高亮 | `Indicate(angle_2, angle_6)` |
| 5.5s | 第3对同位角高亮 | `Indicate(angle_3, angle_7)` |
| 6.5s | 第4对同位角高亮 | `Indicate(angle_4, angle_8)` |
| 7.5s | 总结框 | `Create(summary_box)` - "4对同位角" |
| 8.5s | 关键提示 | `FadeIn(key_point)` - "记忆口诀: 位置相同" |
| 10.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有高亮、标签、说明文字
- 保留: line1, line2, line3, 8个角（恢复原色）

---

## Scene 4: 内错角 (10-12秒)
**目的**: 定义并高亮内错角

### 元素
1. 定义文字
2. 2对内错角的高亮
3. 位置说明图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "内错角 Alternate Interior Angles" |
| 0.6s | 定义 | `FadeIn(definition)` - "在截线两侧，被截两线之间" |
| 1.5s | 位置说明 | `FadeIn(position_hint)` - "内部交错的角" |
| 2.5s | 区域高亮 | `FadeIn(interior_region)` - 标记"内部"区域 |
| 3.5s | 第1对内错角高亮 | `Indicate(angle_3, angle_5)` - ∠3和∠5 |
| 4.5s | 标注 | `FadeIn(label)` - "∠3 = ∠5 (内错角)" |
| 5.5s | 交错线示意 | `Create(cross_lines)` - Z字形 |
| 6.5s | 第2对内错角高亮 | `Indicate(angle_4, angle_6)` - ∠4和∠6 |
| 7.5s | 总结框 | `Create(summary_box)` - "2对内错角" |
| 8.5s | 关键提示 | `FadeIn(key_point)` - "记忆口诀: 内部交错" |
| 10.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有高亮、标签、说明文字、区域标记
- 保留: line1, line2, line3, 8个角（恢复原色）

---

## Scene 5: 同旁内角 (10-12秒)
**目的**: 定义并高亮同旁内角

### 元素
1. 定义文字
2. 2对同旁内角的高亮
3. 位置说明图示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "同旁内角 Consecutive Interior Angles" |
| 0.6s | 定义 | `FadeIn(definition)` - "在截线同侧，被截两线之间" |
| 1.5s | 位置说明 | `FadeIn(position_hint)` - "同侧内部的角" |
| 2.5s | 区域高亮 | `FadeIn(interior_region)` - 标记"内部"区域 |
| 3.5s | 第1对同旁内角高亮 | `Indicate(angle_3, angle_6)` - ∠3和∠6 |
| 4.5s | 标注 | `FadeIn(label)` - "∠3 + ∠6 = 180° (同旁内角)" |
| 5.5s | U字形示意 | `Create(u_shape)` - U字形 |
| 6.5s | 第2对同旁内角高亮 | `Indicate(angle_4, angle_5)` - ∠4和∠5 |
| 7.5s | 总结框 | `Create(summary_box)` - "2对同旁内角" |
| 8.5s | 关键提示 | `FadeIn(key_point)` - "记忆口诀: 同侧内部" |
| 10.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有高亮、标签、说明文字、区域标记
- 保留: line1, line2, line3, 8个角（恢复原色）

---

## Scene 6: 知识总结 (10-12秒)
**目的**: 综合展示三类角的对比

### 元素
1. 三列对比卡片
2. 记忆口诀
3. 应用提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题 | `Write(title)` - "三线八角 - 知识总结" |
| 0.5s | 三条线缩小移至上方 | `Transform(lines_group)` |
| 1.5s | 卡片1滑入 | `card1.animate.shift(RIGHT)` - 同位角 |
| 2.0s | 卡片2滑入 | `card2.animate.shift(RIGHT)` - 内错角 |
| 2.5s | 卡片3滑入 | `card3.animate.shift(RIGHT)` - 同旁内角 |
| 3.5s | 对比表格 | `Create(comparison_table)` |
| 5.0s | 记忆口诀 | `FadeIn(mnemonics)` - "位置相同、内部交错、同侧内部" |
| 7.0s | 应用提示 | `FadeIn(application)` - "平行线判定与性质的基础" |
| 9.0s | 全部闪烁 | `Flash(all_elements)` |
| 10.0s | 等待 | `self.wait(1.5)` |

### 清理
- FadeOut: 所有元素除了作者信息
- 保留: author_info

---

## Scene 7: 片尾关注 (5-6秒)
**目的**: 引导关注，结束视频

### 元素
1. 作者信息放大
2. 关注提示
3. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, author_large)` |
| 0.8s | ID显示 | `FadeIn(author_id)` - "@emptyandcalm" |
| 1.5s | 关注文字 | `FadeIn(follow_text)` - "关注我，获得更多数学技巧!" |
| 2.5s | 几何图标 | `FadeIn(icons)` - 角度、平行线图标 |
| 3.5s | 旋转动画 | `Rotate(icons)` |
| 5.0s | 全部淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全程 |
| line1 (被截线1) | Scene 1 | Scene 6 | 蓝色主线 |
| line2 (被截线2) | Scene 2 | Scene 6 | 红色主线 |
| line3 (截线) | Scene 2 | Scene 6 | 绿色主线 |
| angle_1 to angle_8 | Scene 2 | Scene 6 | 8个角标记 |
| dot_P, dot_Q | Scene 2 | Scene 6 | 交点 |
| 各类角高亮 | Scene 3-5 | Scene 3-5 | 临时高亮 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

## 技术要点
1. **精确计算交点**: 使用 `calculate_line_intersection()` 计算P和Q
2. **角度标记**: 使用 `Angle()` 或 `Arc()` 标记角
3. **颜色编码**: 不同类型的角使用不同颜色便于区分
4. **动画节奏**: 关键概念停留时间2-3秒
5. **字体管理**: 中文使用 Text()，数学符号使用 MathTex()

## 难点预判
1. 8个角的精确标记位置
2. 同位角/内错角/同旁内角的视觉区分
3. 动画流畅性：避免元素闪烁或重叠
4. 文字量控制：简洁易懂

## 验证检查项
- [ ] 所有交点坐标使用精确计算
- [ ] 8个角位置无重叠
- [ ] 颜色区分清晰
- [ ] 文字大小符合规范
- [ ] 总时长60-75秒
- [ ] 无元素溢出边界