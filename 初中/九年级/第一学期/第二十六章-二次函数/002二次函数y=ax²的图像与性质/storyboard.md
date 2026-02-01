# 二次函数 y=ax² 的图像与性质 - 动画分镜脚本

<!-- /root/code/sss/media/videos/quadratic_function2/1920p60/QuadraticFunction.mp4 -->

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 目标观众: 九年级学生

## 颜色配置
```python
COLOR_PARABOLA_POSITIVE = "#e74c3c"  # 红色 - a>0的抛物线
COLOR_PARABOLA_NEGATIVE = "#3498db"  # 蓝色 - a<0的抛物线
COLOR_VERTEX = "#2ecc71"             # 绿色 - 顶点
COLOR_AXIS = "#f39c12"               # 橙色 - 对称轴
COLOR_HIGHLIGHT = YELLOW             # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B             # 灰色 - 辅助元素
COLOR_BACKGROUND = "#1a1a2e"         # 深蓝黑色背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 顶点 | (0, 0) | self.vertex |
| 对称轴 | x = 0 (y轴) | self.symmetry_axis |
| 坐标轴 | x∈[-4,4], y∈[-3,5] | self.axes |
| 抛物线1 (a=1) | y = x² | self.parabola_1 |
| 抛物线2 (a=-1) | y = -x² | self.parabola_2 |
| 抛物线3 (a=0.5) | y = 0.5x² | self.parabola_3 |
| 抛物线4 (a=2) | y = 2x² | self.parabola_4 |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 抓住注意力，引出二次函数

### 元素
1. 作者标识 (顶部)
2. 钩子问题 (大字): "抛物线的秘密在哪里?"
3. 快速闪现的抛物线轮廓

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 抛物线闪现 | `Create(outline, run_time=0.6)` |
| 1.7s | 等待 | `Wait(0.5)` |
| 2.2s | 清理钩子 | `FadeOut(hook_text, outline, run_time=0.4)` |

### 清理
- FadeOut: hook_text, outline
- 保留: author_info

---

## Scene 2: 建立坐标系 (4-5秒)
**目的**: 创建坐标系，标注顶点和对称轴

### 元素
1. 坐标轴 (x∈[-4,4], y∈[-3,5])
2. 原点标记
3. 顶点标注: "顶点 (0, 0)"
4. 对称轴标注: "对称轴: x = 0"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 坐标轴创建 | `Create(axes, run_time=1.2)` |
| 1.2s | 原点标记 | `FadeIn(origin_dot, scale=0.5)` |
| 1.5s | 顶点标注 | `FadeIn(vertex_label, shift=UP*0.2)` |
| 2.0s | 对称轴绘制 | `Create(symmetry_axis, run_time=0.8)` |
| 2.8s | 对称轴标注 | `FadeIn(axis_label, run_time=0.5)` |
| 3.3s | 等待 | `Wait(0.8)` |

### 清理
- 保留: axes, origin_dot, vertex_label (缩小), symmetry_axis (淡化)
- 移除标签准备下一场景

---

## Scene 3: a>0 的情况 (10-12秒)
**目的**: 展示 a>0 时抛物线向上开口，有最小值

### 元素
1. 标题: "当 a > 0 时"
2. 公式: y = x²
3. 抛物线图像 (红色)
4. 开口方向箭头
5. 最小值标注
6. 增减性标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `Write(title, run_time=0.6)` |
| 0.6s | 公式显示 | `Write(formula, run_time=0.8)` |
| 1.4s | 抛物线绘制 | `Create(parabola, run_time=2.0)` |
| 3.4s | 开口箭头 | `GrowArrow(arrow_up, run_time=0.5)` |
| 3.9s | 最小值标注 | `FadeIn(min_label, run_time=0.5)` |
| 4.4s | Flash顶点 | `Flash(origin_dot, color=YELLOW)` |
| 4.8s | 左侧递减标注 | `FadeIn(decreasing_label)` |
| 5.3s | 右侧递增标注 | `FadeIn(increasing_label)` |
| 5.8s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, arrow_up, min_label, decreasing_label, increasing_label
- 保留: parabola (淡化为辅助)

---

## Scene 4: a<0 的情况 (10-12秒)
**目的**: 展示 a<0 时抛物线向下开口，有最大值

### 元素
1. 标题: "当 a < 0 时"
2. 公式: y = -x²
3. 抛物线图像 (蓝色)
4. 开口方向箭头
5. 最大值标注
6. 增减性标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `Write(title, run_time=0.6)` |
| 0.6s | 公式显示 | `Write(formula, run_time=0.8)` |
| 1.4s | 抛物线绘制 | `Create(parabola_neg, run_time=2.0)` |
| 3.4s | 开口箭头 | `GrowArrow(arrow_down, run_time=0.5)` |
| 3.9s | 最大值标注 | `FadeIn(max_label, run_time=0.5)` |
| 4.4s | Flash顶点 | `Flash(origin_dot, color=YELLOW)` |
| 4.8s | 左侧递增标注 | `FadeIn(increasing_label)` |
| 5.3s | 右侧递减标注 | `FadeIn(decreasing_label)` |
| 5.8s | 等待理解 | `Wait(1.5)` |

### 清理
- FadeOut: title, formula, arrow_down, max_label, increasing_label, decreasing_label
- 保留: parabola_neg (淡化为辅助)

---

## Scene 5: |a|对开口大小的影响 (12-15秒)
**目的**: 展示|a|越大，开口越小；|a|越小，开口越大

### 元素
1. 标题: "|a| 的大小影响开口"
2. 四条抛物线对比:
   - y = 2x² (深红色，最窄)
   - y = x² (红色，标准)
   - y = 0.5x² (浅红色，最宽)
3. 标注: "|a| 越大，开口越小"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `Write(title, run_time=0.7)` |
| 0.7s | 清空旧抛物线 | `FadeOut(old_parabolas, run_time=0.5)` |
| 1.2s | 绘制 y=0.5x² | `Create(para_05, run_time=1.0)` |
| 2.2s | 标注 a=0.5 | `FadeIn(label_05)` |
| 2.7s | 绘制 y=x² | `Create(para_1, run_time=1.0)` |
| 3.7s | 标注 a=1 | `FadeIn(label_1)` |
| 4.2s | 绘制 y=2x² | `Create(para_2, run_time=1.0)` |
| 5.2s | 标注 a=2 | `FadeIn(label_2)` |
| 5.7s | 对比动画 | `Indicate(para_2), Indicate(para_05)` |
| 6.5s | 结论文字 | `FadeIn(conclusion, run_time=0.8)` |
| 7.3s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, para_05, para_1, para_2, labels, conclusion
- 保留: axes

---

## Scene 6: 性质总结 (10-12秒)
**目的**: 归纳总结 y=ax² 的关键性质

### 元素
1. 标题: "性质总结"
2. 性质卡片 (4个):
   - 顶点: (0, 0)
   - 对称轴: x = 0 (y轴)
   - a > 0: 开口向上，最小值 0
   - a < 0: 开口向下，最大值 0
3. 背景抛物线 (淡化)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题显示 | `Write(title, run_time=0.6)` |
| 0.6s | 背景抛物线 | `FadeIn(bg_parabola, run_time=0.5)` |
| 1.1s | 卡片1滑入 | `card1.animate.shift(RIGHT*0), run_time=0.5` |
| 1.6s | 卡片2滑入 | `card2.animate.shift(RIGHT*0), run_time=0.5` |
| 2.1s | 卡片3滑入 | `card3.animate.shift(RIGHT*0), run_time=0.5` |
| 2.6s | 卡片4滑入 | `card4.animate.shift(RIGHT*0), run_time=0.5` |
| 3.1s | 整体强调 | `Flash(cards, color=YELLOW)` |
| 3.6s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, cards, bg_parabola

---

## Scene 7: 片尾关注 (8-10秒)
**目的**: 品牌展示，引导关注

### 元素
1. 作者信息放大
2. 关注提示: "关注我，学更多数学技巧!"
3. 抛物线装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息放大 | `Transform(author_info, author_large)` |
| 0.8s | 关注提示 | `FadeIn(follow_text, scale=1.1)` |
| 1.4s | 装饰抛物线 | `Create(deco_parabolas, run_time=1.0)` |
| 2.4s | 旋转动画 | `Rotate(deco_parabolas, angle=PI)` |
| 3.9s | 等待 | `Wait(1.5)` |
| 5.4s | 全部淡出 | `FadeOut(all, run_time=1.0)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 贯穿全片 |
| axes | Scene 2 | Scene 6 | 主坐标系 |
| origin_dot | Scene 2 | Scene 6 | 原点标记 |
| symmetry_axis | Scene 2 | Scene 6 | 对称轴 |
| parabola_positive | Scene 3 | Scene 5 | a>0抛物线 |
| parabola_negative | Scene 4 | Scene 5 | a<0抛物线 |
| comparison_parabolas | Scene 5 | Scene 5 | 对比抛物线组 |
| summary_cards | Scene 6 | Scene 6 | 性质卡片 |

---

## 时长分配
- Scene 1: 3-4秒 (开场)
- Scene 2: 4-5秒 (坐标系)
- Scene 3: 10-12秒 (a>0)
- Scene 4: 10-12秒 (a<0)
- Scene 5: 12-15秒 (|a|影响)
- Scene 6: 10-12秒 (总结)
- Scene 7: 8-10秒 (片尾)
- **总计: 60-75秒**

---

## 关键技术要点
1. **坐标系设置**: x∈[-4,4], y∈[-3,5]，适配竖屏
2. **抛物线绘制**: 使用 `axes.plot(lambda x: a*x**2)`
3. **对称性展示**: 对称轴用虚线，强调y轴对称
4. **增减性标注**: 用箭头+文字清晰标注
5. **颜色对比**: a>0用暖色，a<0用冷色
6. **动画节奏**: 关键步骤停留1.5-2秒