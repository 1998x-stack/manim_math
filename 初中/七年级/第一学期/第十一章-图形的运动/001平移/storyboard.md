# 平移 (Translation) - 动画分镜脚本

<!-- /root/code/sss/media/videos/translation_animation/1920p60/TranslationAnimation.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初级（七年级）
- 目标受众: 七年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主图形
COLOR_SECONDARY = "#e74c3c"    # 红色 - 变换后图形
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点标注
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_ARROW = "#2ecc71"        # 绿色 - 平移箭头
COLOR_PATH = "#9b59b6"         # 紫色 - 轨迹路径
```

## 几何预计算清单

### 主要图形 - 三角形ABC
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 顶点A | np.array([-2, 0.5, 0]) | self.A | 原始位置 |
| 顶点B | np.array([-0.5, 0.5, 0]) | self.B | 原始位置 |
| 顶点C | np.array([-1.25, 2, 0]) | self.C | 原始位置 |
| 顶点A' | A + translation_vector | self.A_prime | 平移后位置 |
| 顶点B' | B + translation_vector | self.B_prime | 平移后位置 |
| 顶点C' | C + translation_vector | self.C_prime | 平移后位置 |

### 平移向量
| 元素 | 数值 | 存储变量 |
|------|------|---------|
| 水平分量 | 3.0 | self.dx |
| 垂直分量 | 1.5 | self.dy |
| 向量 | np.array([dx, dy, 0]) | self.translation_vector |

### 坐标偏移
| 元素 | 数值 | 说明 |
|------|------|------|
| 全局偏移 | UP * 2.0 | self.OFFSET | 整体上移，避免底部溢出 |
| 缩放比例 | 0.85 | self.SCALE | 确保图形适配屏幕 |

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出平移概念

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字，吸引眼球)
3. 简单图形（正方形）做快速平移演示

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 0.8s |
| 1.1s | 正方形创建 | `Create(square)` | 0.6s |
| 1.7s | 正方形快速平移 | `square.animate.shift(RIGHT*2)` | 1.0s |
| 2.7s | 问题文字出现 | `FadeIn(question)` | 0.5s |
| 3.2s | 等待理解 | `Wait(1.8)` | 1.8s |

### 钩子文字
- 主标题: "图形怎么移动？"
- 副标题: "平移变换的秘密"

### 清理
- FadeOut: hook_text, square, question
- 保留: author_info

---

## Scene 2: 定义介绍 (5-12秒)
**目的**: 清晰说明平移的定义

### 元素
1. 标题："什么是平移？"
2. 定义文字（分步显示）
3. 关键词高亮

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 5.0s | 标题写入 | `Write(title)` | 0.8s |
| 5.8s | 定义第1部分 | `FadeIn(def_part1)` | 0.6s |
| 6.4s | 定义第2部分 | `FadeIn(def_part2)` | 0.6s |
| 7.0s | 关键词高亮 | `Indicate(keywords)` | 0.8s |
| 7.8s | 等待阅读 | `Wait(1.2)` | 1.2s |

### 定义文字
- 第1部分: "平移是把图形沿某个方向"
- 第2部分: "移动一定距离的变换"
- 关键词: "方向" 和 "距离" (黄色高亮)

### 清理
- FadeOut: title, definition
- 保留: author_info

---

## Scene 3: 构建主三角形 (12-18秒)
**目的**: 创建演示用的三角形ABC

### 元素
1. 标题: "三角形ABC"
2. 三角形ABC（蓝色）
3. 顶点标签 A, B, C
4. 坐标轴参考（可选，浅灰色）

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 12.0s | 标题淡入 | `FadeIn(title)` | 0.4s |
| 12.4s | 三角形绘制 | `Create(triangle_ABC)` | 1.2s |
| 13.6s | 顶点A标签 | `FadeIn(label_A)` | 0.3s |
| 13.9s | 顶点B标签 | `FadeIn(label_B)` | 0.3s |
| 14.2s | 顶点C标签 | `FadeIn(label_C)` | 0.3s |
| 14.5s | 说明文字 | `FadeIn(explain)` | 0.5s |
| 15.0s | 等待观察 | `Wait(1.5)` | 1.5s |

### 说明文字
"这是我们的原始三角形"

### 清理
- FadeOut: title, explain
- 保留: triangle_ABC, label_A, label_B, label_C, author_info

---

## Scene 4: 展示平移向量 (18-26秒)
**目的**: 明确平移的方向和距离

### 元素
1. 标题: "平移方向与距离"
2. 平移箭头（绿色，粗箭头）
3. 向量标注（水平和垂直分量）
4. 距离和方向说明

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 18.0s | 标题写入 | `Write(title)` | 0.6s |
| 18.6s | 平移箭头绘制 | `GrowArrow(arrow)` | 1.0s |
| 19.6s | 水平分量虚线 | `Create(h_dash)` | 0.5s |
| 20.1s | 垂直分量虚线 | `Create(v_dash)` | 0.5s |
| 20.6s | 水平标注 | `FadeIn(h_label)` | 0.4s |
| 21.0s | 垂直标注 | `FadeIn(v_label)` | 0.4s |
| 21.4s | 说明文字 | `FadeIn(explain)` | 0.6s |
| 22.0s | 等待理解 | `Wait(2.0)` | 2.0s |

### 标注内容
- 水平分量: "向右3单位"
- 垂直分量: "向上1.5单位"
- 说明: "平移向量决定了移动的方向和距离"

### 清理
- FadeOut: title, h_dash, v_dash, h_label, v_label, explain
- 保留: triangle_ABC, labels, arrow, author_info

---

## Scene 5: 执行平移动画 (26-38秒)
**目的**: 展示平移过程，强调对应点的移动

### 元素
1. 标题: "开始平移！"
2. 三角形A'B'C'（红色，逐渐出现）
3. 对应点连线（AA', BB', CC'）
4. 轨迹路径（虚线，紫色）
5. 平移后的顶点标签 A', B', C'

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 26.0s | 标题闪现 | `FadeIn(title, scale=1.2)` | 0.5s |
| 26.5s | 创建副本三角形 | `triangle_prime = triangle.copy()` | - |
| 26.5s | 轨迹路径启动 | `add_updater(traced_path)` | - |
| 26.5s | 平移动画 | `triangle_prime.animate.shift(vector)` | 2.5s |
| 29.0s | 移除轨迹追踪 | `remove_updater()` | - |
| 29.0s | 对应点连线AA' | `Create(line_AA)` | 0.5s |
| 29.5s | 对应点连线BB' | `Create(line_BB)` | 0.5s |
| 30.0s | 对应点连线CC' | `Create(line_CC)` | 0.5s |
| 30.5s | 标签A'出现 | `FadeIn(label_A_prime)` | 0.3s |
| 30.8s | 标签B'出现 | `FadeIn(label_B_prime)` | 0.3s |
| 31.1s | 标签C'出现 | `FadeIn(label_C_prime)` | 0.3s |
| 31.4s | 说明文字 | `FadeIn(explain)` | 0.6s |
| 32.0s | 等待观察 | `Wait(2.5)` | 2.5s |

### 说明文字
"对应点沿着相同方向移动相同距离"

### 清理
- FadeOut: title, explain
- 保留: triangle_ABC, triangle_A'B'C', all labels, connecting lines, author_info

---

## Scene 6: 平移的性质 (38-52秒)
**目的**: 强调平移的三个关键性质

### 元素
1. 标题: "平移的性质"
2. 性质1: 形状、大小、方向不变
3. 性质2: 对应点连线平行且相等
4. 性质3: 对应线段平行且相等
5. 视觉验证（测量标注）

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 38.0s | 标题写入 | `Write(title)` | 0.8s |
| 38.8s | 性质1卡片 | `FadeIn(prop1_card, shift=UP)` | 0.6s |
| 39.4s | 闪烁强调原图 | `Flash(triangle_ABC)` | 0.4s |
| 39.8s | 闪烁强调新图 | `Flash(triangle_prime)` | 0.4s |
| 40.2s | 等待 | `Wait(1.0)` | 1.0s |
| 41.2s | 性质2卡片 | `FadeIn(prop2_card, shift=UP)` | 0.6s |
| 41.8s | 标注平行符号 | `FadeIn(parallel_marks)` | 0.8s |
| 42.6s | 标注相等符号 | `FadeIn(equal_marks)` | 0.6s |
| 43.2s | 等待 | `Wait(1.5)` | 1.5s |
| 44.7s | 性质3卡片 | `FadeIn(prop3_card, shift=UP)` | 0.6s |
| 45.3s | 高亮边AB | `Indicate(edge_AB)` | 0.5s |
| 45.8s | 高亮边A'B' | `Indicate(edge_AB_prime)` | 0.5s |
| 46.3s | 平行标记 | `FadeIn(parallel_edge_marks)` | 0.6s |
| 46.9s | 等待理解 | `Wait(2.0)` | 2.0s |

### 性质卡片内容
- 性质1: "图形的形状、大小、方向均不变"
- 性质2: "对应点连线平行且相等 (AA' ∥ BB' 且 AA' = BB')"
- 性质3: "对应线段平行且相等，对应角相等"

### 清理
- FadeOut: title, prop_cards, marks
- 保留: triangles, labels, author_info

---

## Scene 7: 总结与片尾 (52-65秒)
**目的**: 巩固知识点，引导关注

### 元素
1. 总结标题: "平移变换 - 关键要点"
2. 要点列表（三个关键公式/性质）
3. 实际应用提示
4. 作者信息放大
5. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 时长 |
|------|------|---------|------|
| 52.0s | 清空所有图形 | `FadeOut(all_geometry)` | 0.8s |
| 52.8s | 总结标题 | `Write(summary_title)` | 0.8s |
| 53.6s | 要点1滑入 | `FadeIn(point1, shift=RIGHT)` | 0.5s |
| 54.1s | 要点2滑入 | `FadeIn(point2, shift=RIGHT)` | 0.5s |
| 54.6s | 要点3滑入 | `FadeIn(point3, shift=RIGHT)` | 0.5s |
| 55.1s | 应用提示 | `FadeIn(application_hint)` | 0.6s |
| 55.7s | 等待阅读 | `Wait(2.0)` | 2.0s |
| 57.7s | 作者信息放大 | `Transform(author_info, large_author)` | 0.8s |
| 58.5s | 关注提示 | `FadeIn(follow_text, scale=1.2)` | 0.6s |
| 59.1s | 装饰动画 | `Create(decorations)` | 1.0s |
| 60.1s | 最终等待 | `Wait(2.0)` | 2.0s |
| 62.1s | 全部淡出 | `FadeOut(everything)` | 1.0s |

### 要点内容
1. "平移 = 方向 + 距离"
2. "对应点连线: AA' ∥ BB' 且相等"
3. "形状、大小、方向都不变"

### 应用提示
"平移在坐标系、向量、全等变换中都很重要！"

### 关注文字
"关注我，获得更多数学技巧！"

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 持续时长 | 备注 |
|------|---------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程 | 顶部小字 |
| hook_square | Scene 1 | Scene 1 | 5s | 开场演示 |
| triangle_ABC | Scene 3 | Scene 7 | 40s | 主要图形 |
| label_A/B/C | Scene 3 | Scene 7 | 40s | 顶点标签 |
| translation_arrow | Scene 4 | Scene 7 | 30s | 平移箭头 |
| triangle_A'B'C' | Scene 5 | Scene 7 | 25s | 平移后图形 |
| label_A'/B'/C' | Scene 5 | Scene 7 | 25s | 新顶点标签 |
| connecting_lines | Scene 5 | Scene 7 | 25s | AA', BB', CC' |
| traced_paths | Scene 5 | Scene 5 | 2.5s | 临时轨迹 |
| property_cards | Scene 6 | Scene 6 | 10s | 性质说明 |
| summary_points | Scene 7 | Scene 7 | 8s | 总结要点 |

---

## 技术要点

### 1. 坐标系统
- 使用全局偏移确保所有元素在安全区域内
- 原始三角形中心位于 y=2 附近
- 平移后三角形中心位于 y=3.5 附近

### 2. 颜色一致性
- 原始图形: 蓝色 (#3498db)
- 平移后图形: 红色 (#e74c3c)
- 箭头和向量: 绿色 (#2ecc71)
- 辅助线和连线: 灰色 (GRAY_B)

### 3. 动画时长控制
- 快速动画 (创建简单元素): 0.3-0.6s
- 中速动画 (平移、变换): 1.0-2.5s
- 慢速等待 (理解停顿): 1.5-2.5s

### 4. 字体大小规范
- 主标题: 36
- 副标题/场景标题: 28
- 正文说明: 22
- 顶点标签: 24
- 小注释: 18
- 作者信息: 20

### 5. 精确计算要求
- 所有顶点坐标在 setup_geometry() 中统一计算
- 平移向量精确定义
- 对应点位置通过向量加法计算，不得臆想
- 使用 NumPy 进行所有几何运算

---

## 总时长规划
- Scene 1 (开场): 5s
- Scene 2 (定义): 7s
- Scene 3 (构建): 6s
- Scene 4 (向量): 8s
- Scene 5 (平移): 12s
- Scene 6 (性质): 14s
- Scene 7 (总结): 13s
- **总计: 65秒**

---

## 验证检查清单
- [ ] 所有坐标在 setup_geometry() 中预计算
- [ ] 无元素超出边界 (x∈[-4,4], y∈[-7,7])
- [ ] 中文文本使用 Text(), 数学公式使用 MathTex()
- [ ] 虚线使用 DashedLine
- [ ] 字体大小符合规范
- [ ] 颜色一致性
- [ ] 元素生命周期清晰
- [ ] 动画节奏合理
- [ ] 难点有足够停留时间
- [ ] 开头有钩子，结尾有关注引导