# 平行线的性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-90 秒
- 场景数量: 8 个
- 难度等级: 中等
- 目标观众: 七年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 平行线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 截线
COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 角度标记
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
COLOR_TEXT = WHITE
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 平行线1 | y = const | self.line1_start, self.line1_end |
| 平行线2 | y = const + offset | self.line2_start, self.line2_end |
| 截线 | 任意斜率 | self.transversal_start, self.transversal_end |
| 交点 | 线线交点公式 | self.intersection1, self.intersection2 |

---

## Scene 1: 开场 (4-5秒)
**目的**: 钩子 + 引出平行线性质问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 动态平行线演示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text)` |
| 1.0s | 创建平行线 | `Create(parallel_lines)` |
| 2.0s | 添加截线 | `Create(transversal_line)` |
| 3.0s | 显示问题 | `FadeIn(question_text)` |

### 清理
- 保留: 平行线、截线
- 淡出: 钩子问题、问题文字

---

## Scene 2: 同位角相等 (8-10秒)
**目的**: 演示两直线平行时同位角相等

### 元素
1. 平行线和截线
2. 同位角标记
3. 角度数值显示
4. 结论文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 强调平行线和截线 | `Indicate(parallel_lines)` |
| 1.0s | 创建第一个同位角 | `Create(angle1)` |
| 1.5s | 创建第二个同位角 | `Create(angle2)` |
| 2.5s | 闪烁两个角度 | `Flash(angle1, angle2)` |
| 3.0s | 显示角度数值 | `Write(angle_values)` |
| 4.0s | 显示结论 | `Write(conclusion_text)` |
| 6.0s | 强调相等关系 | `Indicate(conclusion_text)` |

### 清理
- 保留: 平行线、截线、角度标记
- 淡出: 角度数值、结论文字

---

## Scene 3: 内错角相等 (8-10秒)
**目的**: 演示两直线平行时内错角相等

### 元素
1. 平行线和截线
2. 内错角标记
3. 角度数值显示
4. 结论文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 隐藏前一组角度 | `FadeOut(prev_angles)` |
| 1.0s | 创建第一组内错角 | `Create(alternate_angle1)` |
| 1.5s | 创建第二组内错角 | `Create(alternate_angle2)` |
| 2.5s | 闪烁两个角度 | `Flash(alternate_angles)` |
| 3.0s | 显示角度数值 | `Write(alternate_angle_values)` |
| 4.0s | 显示结论 | `Write(alternate_conclusion)` |
| 6.0s | 强调相等关系 | `Indicate(alternate_conclusion)` |

### 清理
- 保留: 平行线、截线、角度标记
- 淡出: 角度数值、结论文字

---

## Scene 4: 同旁内角互补 (8-10秒)
**目的**: 演示两直线平行时同旁内角互补

### 元素
1. 平行线和截线
2. 同旁内角标记
3. 角度数值显示
4. 结论文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 隐藏前一组角度 | `FadeOut(prev_alternate_angles)` |
| 1.0s | 创建第一组同旁内角 | `Create(co_interior_angle1)` |
| 1.5s | 创建第二组同旁内角 | `Create(co_interior_angle2)` |
| 2.5s | 闪烁两个角度 | `Flash(co_interior_angles)` |
| 3.0s | 显示角度数值 | `Write(co_interior_angle_values)` |
| 4.0s | 显示求和动画 | `Transform(sum_animation)` |
| 5.0s | 显示结论 | `Write(complement_conclusion)` |
| 7.0s | 强调互补关系 | `Indicate(complement_conclusion)` |

### 清理
- 保留: 平行线、截线、角度标记
- 淡出: 角度数值、结论文字

---

## Scene 5: 动态验证 (10-12秒)
**目的**: 通过改变截线角度，展示性质仍然成立

### 元素
1. 平行线
2. 可移动截线
3. 动态角度测量
4. 等式显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 恢复初始角度 | `Restore(initial_config)` |
| 1.0s | 创建可动截线 | `Create(movable_transversal)` |
| 2.0s | 演示角度变化 | `Rotate(transversal, angle=PI/4)` |
| 4.0s | 实时更新角度值 | `Update(angle_displays)` |
| 6.0s | 验证同位角相等 | `Verify(corresponding_angles)` |
| 8.0s | 验证内错角相等 | `Verify(alternate_angles)` |
| 10.0s | 验证同旁内角互补 | `Verify(co_interior_angles)` |

### 清理
- 保留: 平行线、截线
- 恢复: 固定截线状态

---

## Scene 6: 对比非平行线 (8-10秒)
**目的**: 展示非平行线时，上述性质不成立

### 元素
1. 非平行线组
2. 截线
3. 角度比较
4. 反例文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 变换为非平行线 | `Transform(lines, non_parallel_config)` |
| 2.0s | 显示同位角 | `Create(non_parallel_corresponding_angles)` |
| 3.0s | 显示不等关系 | `Write(unequal_sign)` |
| 4.0s | 显示内错角 | `Create(non_parallel_alternate_angles)` |
| 5.0s | 显示不等关系 | `Write(unequal_sign2)` |
| 6.0s | 显示同旁内角 | `Create(non_parallel_co_interior_angles)` |
| 7.0s | 显示非互补关系 | `Write(not_complement_sign)` |
| 9.0s | 强调条件 | `Write(condition_text)` |

### 清理
- 保留: 平行线基础图形
- 恢复: 平行线状态

---

## Scene 7: 总结回顾 (6-8秒)
**目的**: 总结三个平行线性质

### 元素
1. 平行线和截线
2. 性质卡片
3. 公式显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 恢复平行线标准图 | `Restore(standard_config)` |
| 0.5s | 显示性质1 | `FadeIn(property1_card)` |
| 2.0s | 显示性质2 | `FadeIn(property2_card)` |
| 3.5s | 显示性质3 | `FadeIn(property3_card)` |
| 5.0s | 组合显示 | `VGroup(properties).arrange(DOWN)` |

### 清理
- 保留: 平行线基础图形
- 保留: 性质卡片

---

## Scene 8: 片尾关注 (4-5秒)
**目的**: 作者信息和关注提示

### 元素
1. 作者信息
2. 关注提示
3. 联系方式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 淡出性质卡片 | `FadeOut(properties)` |
| 0.5s | 放大作者信息 | `Transform(author_info, large_author)` |
| 1.5s | 显示关注提示 | `FadeIn(follow_text)` |
| 3.0s | 循环播放 | `Wait(1.0)` |

### 清理
- 无

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| parallel_lines | Scene 1 | Scene 8 | 平行线主体 |
| transversal_line | Scene 1 | Scene 8 | 截线 |
| angle_markings | Scene 2-7 | Scene 8 | 角度标记 |
| property_cards | Scene 7 | Scene 8 | 性质卡片 |
| author_info | Scene 1 | Scene 8 | 作者信息 |
| hook_texts | Scene 1 | Scene 1 | 钩子文字，立即销毁 |
