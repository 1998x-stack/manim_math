# 线段的概念 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 简单 (六年级)
- 目标受众: 小学六年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主线段
COLOR_SECONDARY = "#e74c3c"    # 红色 - 辅助线段
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_POINT = "#2ecc71"        # 绿色 - 端点
COLOR_MIDPOINT = "#f39c12"     # 橙色 - 中点
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 线段AB起点 | 固定坐标 | self.A |
| 线段AB终点 | 固定坐标 | self.B |
| 线段长度 | ‖B-A‖ | self.AB_length |
| 中点M | (A+B)/2 | self.M |
| 线段CD起点 | 固定坐标 | self.C |
| 线段CD终点 | 固定坐标 | self.D |
| 线段CD长度 | ‖D-C‖ | self.CD_length |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出线段概念

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字): "从A点到B点，最短的路径是什么?"
3. 三条不同路径动画 (曲线、折线、直线)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子问题书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 点A和点B出现 | `FadeIn(VGroup(dot_A, dot_B), scale=0.5)` |
| 1.5s | 曲线路径绘制 | `Create(curved_path, run_time=0.6)` |
| 2.1s | 曲线变灰，折线路径绘制 | `Create(zigzag_path, run_time=0.6)` |
| 2.7s | 折线变灰，直线路径绘制 | `Create(straight_path, run_time=0.6)` |
| 3.3s | 直线高亮闪烁 | `Flash(straight_path, color=YELLOW)` |

### 清理
- FadeOut: hook_text, curved_path, zigzag_path
- 保留: author_info, dot_A, dot_B, straight_path

---

## Scene 2: 线段定义 (8-10秒)
**目的**: 介绍线段的基本定义

### 元素
1. 标题: "什么是线段?"
2. 定义文字: "直线上两点之间的部分"
3. 主线段AB (从Scene 1的直线变换)
4. 端点标签 A、B
5. 长度标注

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=DOWN*0.3)` |
| 0.5s | 定义文字逐行书写 | `Write(definition, run_time=1.2)` |
| 1.7s | 端点A、B高亮放大 | `Indicate(VGroup(dot_A, dot_B), scale_factor=1.5)` |
| 2.3s | 添加端点标签 | `FadeIn(VGroup(label_A, label_B))` |
| 2.8s | 强调"包括两个端点" | 端点颜色变为绿色 |
| 3.5s | 添加长度标注和大括号 | `Create(brace), Write(length_label)` |
| 4.5s | 介绍记号: AB或|AB| | `Write(notation)` |
| 6.0s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, definition, notation
- 保留: straight_path (变为segment_AB), dot_A, dot_B, label_A, label_B

---

## Scene 3: 线段的基本性质 (10-12秒)
**目的**: 两点之间线段最短

### 元素
1. 标题: "两点之间，线段最短"
2. 对比图形 (重新显示曲线和折线)
3. 长度数值标注
4. 强调文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title, run_time=0.8)` |
| 0.8s | 重新绘制曲线路径 | `Create(curved_path_2)` |
| 1.5s | 标注曲线长度 (约8.5) | `FadeIn(length_curved)` |
| 2.2s | 重新绘制折线路径 | `Create(zigzag_path_2)` |
| 2.9s | 标注折线长度 (约7.2) | `FadeIn(length_zigzag)` |
| 3.6s | 强调直线长度 (6.0) | `Indicate(segment_AB), Write(length_straight)` |
| 4.5s | 三条路径对比闪烁 | 依次Flash |
| 5.5s | 结论文字出现 | `FadeIn(conclusion, shift=UP*0.3)` |
| 7.0s | 等待理解 | `Wait(3.0)` |

### 清理
- FadeOut: title, curved_path_2, zigzag_path_2, all length labels, conclusion
- 保留: segment_AB, dot_A, dot_B, label_A, label_B

---

## Scene 4: 线段的中点 (10-12秒)
**目的**: 介绍中点概念和性质

### 元素
1. 标题: "线段的中点"
2. 定义: "将线段分成两条相等线段的点"
3. 中点M及标签
4. 两段长度标注
5. 公式: AM = MB = AB/2

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 定义文字书写 | `Write(definition, run_time=1.0)` |
| 1.5s | 中点M出现 | `FadeIn(dot_M, scale=0.5), Flash(dot_M)` |
| 2.1s | 中点标签M | `FadeIn(label_M)` |
| 2.6s | 线段AB分为两段 (颜色变化) | `segment_AB变为两段不同颜色` |
| 3.3s | 标注AM长度 | `Create(brace_AM), Write(length_AM)` |
| 4.0s | 标注MB长度 | `Create(brace_MB), Write(length_MB)` |
| 4.7s | 强调AM = MB | 两个长度数值同时闪烁 |
| 5.5s | 公式出现 | `Write(formula, run_time=1.2)` |
| 7.0s | 等待理解 | `Wait(2.5)` |

### 清理
- FadeOut: title, definition, formula, braces
- 保留: segment_AB, dot_A, dot_B, dot_M, all labels

---

## Scene 5: 线段的度量 (8-10秒)
**目的**: 展示如何测量线段长度

### 元素
1. 标题: "线段可以度量"
2. 刻度尺动画
3. 测量过程演示
4. 长度数值动态显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title)` |
| 0.5s | 刻度尺从底部滑入 | `ruler.animate.shift(UP*2)` |
| 1.2s | 线段移动到刻度尺上方 | `segment_AB.animate.move_to(ruler_position)` |
| 2.0s | 起点A对齐到刻度0 | `Indicate(dot_A), Show scale mark 0` |
| 2.7s | 终点B对齐到刻度6 | `Indicate(dot_B), Show scale mark 6` |
| 3.4s | 动态数字计数器 (0→6) | `ValueTracker动画` |
| 4.5s | 单位标注: 6厘米 | `Write(unit_label)` |
| 5.5s | 说明文字 | `FadeIn(explanation)` |
| 7.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, ruler, unit_label, explanation
- 线段AB移回中心位置
- 保留: segment_AB, all dots and labels

---

## Scene 6: 线段的和与差 (10-12秒)
**目的**: 介绍线段的加法和减法运算

### 元素
1. 标题: "线段的和与差"
2. 新线段CD
3. 计算演示: AB + CD, AB - CD (假设AB>CD)
4. 可视化结果

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题书写 | `Write(title)` |
| 0.6s | 新线段CD出现在下方 | `Create(segment_CD), FadeIn(dot_C, dot_D)` |
| 1.3s | 标注: AB=6, CD=4 | `Write(length_labels)` |
| 2.0s | 副标题: "线段的和" | `FadeIn(subtitle_add)` |
| 2.5s | CD复制并移动到B点后 | `Transform copy of CD` |
| 3.5s | 显示结果: AB+CD=10 | `Write(result_add)` |
| 4.5s | 清理加法元素 | `FadeOut(subtitle_add, copied_segment, result_add)` |
| 5.0s | 副标题: "线段的差" | `FadeIn(subtitle_sub)` |
| 5.5s | 从AB中减去CD (标记4个单位) | 动画演示 |
| 6.5s | 显示结果: AB-CD=2 | `Write(result_sub)` |
| 7.5s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: title, segment_CD, all computation elements
- 保留: segment_AB, basic labels

---

## Scene 7: 总结与片尾 (8-10秒)
**目的**: 总结要点，引导关注

### 元素
1. 总结卡片 (4-5个要点)
2. 作者信息放大
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除所有线段元素 | `FadeOut(all geometry)` |
| 0.5s | 标题: "线段知识总结" | `Write(summary_title)` |
| 1.2s | 要点1: 定义 | `FadeIn(point_1, shift=LEFT*0.5)` |
| 1.8s | 要点2: 两点间最短 | `FadeIn(point_2, shift=LEFT*0.5)` |
| 2.4s | 要点3: 中点性质 | `FadeIn(point_3, shift=LEFT*0.5)` |
| 3.0s | 要点4: 可度量 | `FadeIn(point_4, shift=LEFT*0.5)` |
| 3.6s | 要点5: 可加减 | `FadeIn(point_5, shift=LEFT*0.5)` |
| 4.5s | 所有要点高亮闪烁 | `Flash all points` |
| 5.5s | 作者信息放大 | `Transform(author_info, author_large)` |
| 6.5s | 关注提示 | `FadeIn(follow_text, scale=1.2)` |
| 7.5s | 装饰线段旋转 | `Rotating decorative segments` |
| 9.0s | 全部淡出 | `FadeOut(all, run_time=1.0)` |

### 清理
- 全部清除

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留在顶部 |
| dot_A | Scene 1 | Scene 6 | 端点A |
| dot_B | Scene 1 | Scene 6 | 端点B |
| label_A | Scene 2 | Scene 6 | 标签A |
| label_B | Scene 2 | Scene 6 | 标签B |
| segment_AB | Scene 1 | Scene 6 | 主线段 |
| dot_M | Scene 4 | Scene 6 | 中点 |
| label_M | Scene 4 | Scene 6 | 中点标签 |
| curved_path | Scene 1 | Scene 1 | 临时曲线 |
| zigzag_path | Scene 1 | Scene 1 | 临时折线 |
| segment_CD | Scene 6 | Scene 6 | 第二线段 |
| ruler | Scene 5 | Scene 5 | 刻度尺 |

---

## 关键技术要点

### 1. 坐标精确计算
```python
# 主线段AB (水平，便于理解)
self.A = np.array([-3.0, 0, 0]) + UP * 2
self.B = np.array([3.0, 0, 0]) + UP * 2
self.AB_length = np.linalg.norm(self.B - self.A)  # 应该是6.0

# 中点M
self.M = (self.A + self.B) / 2

# 线段CD (较短)
self.C = np.array([-2.0, -2.0, 0]) + UP * 0.5
self.D = np.array([2.0, -2.0, 0]) + UP * 0.5
self.CD_length = np.linalg.norm(self.D - self.C)  # 应该是4.0
```

### 2. 曲线路径生成
```python
# 曲线 (使用贝塞尔曲线)
curved_path = CubicBezier(
    self.A, 
    self.A + UP*1.5 + RIGHT*0.5,
    self.B + UP*1.5 + LEFT*0.5,
    self.B,
    color=GRAY_B
)

# 折线 (使用Polygon)
zigzag_points = [
    self.A,
    self.A + RIGHT*1.5 + UP*0.8,
    self.A + RIGHT*3.0 + DOWN*0.5,
    self.A + RIGHT*4.5 + UP*0.8,
    self.B
]
zigzag_path = Polygon(*zigzag_points, color=GRAY_B, fill_opacity=0)
```

### 3. 刻度尺实现
```python
# 使用NumberLine创建刻度尺
ruler = NumberLine(
    x_range=[0, 10, 1],
    length=8,
    include_numbers=True,
    numbers_to_include=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    font_size=20,
    color=GRAY_A
).move_to(DOWN * 3)
```

### 4. 动态数字计数器
```python
counter = DecimalNumber(0, num_decimal_places=1, font_size=36)
counter.add_updater(lambda m: m.set_value(tracker.get_value()))
self.play(tracker.animate.set_value(6.0), run_time=2)
```

---

## 配音文案参考

### Scene 1
"从A点到B点，你觉得哪条路最短？弯弯曲曲的？还是折来折去的？其实，最短的就是这条直的！"

### Scene 2
"这条连接两个点的直线段，我们叫它'线段'。它包括A和B两个端点，长度可以测量。我们用AB或|AB|来表示它的长度。"

### Scene 3
"为什么线段最短？因为两点之间，线段就是最短的距离！看，曲线长8.5，折线长7.2，而直线段只有6！"

### Scene 4
"线段上还有一个特殊的点，叫做中点。中点M把线段AB分成了两段完全相等的部分，AM等于MB，都等于AB的一半！"

### Scene 5
"线段的长度怎么测量呢？用尺子！把A点对准刻度0，B点正好在刻度6，所以AB的长度就是6厘米！"

### Scene 6
"线段还可以做加法和减法！AB加上CD，就是把两条线段接起来，等于10。AB减去CD，就是去掉4个单位，等于2！"

### Scene 7
"今天我们学习了线段的定义、最短性质、中点、度量和运算。掌握这些基础，几何学习更轻松！关注我，学更多数学技巧！"