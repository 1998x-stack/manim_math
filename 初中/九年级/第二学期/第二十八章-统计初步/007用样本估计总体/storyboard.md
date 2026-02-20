# 用样本估计总体 - 动画分镜脚本

## 元信息
- 目标时长: 60-70 秒
- 场景数量: 7 个
- 难度等级: 中等
- 主题: 统计学 - 用样本估计总体

## 颜色配置
```python
COLOR_POPULATION = "#3498db"    # 蓝色 - 总体
COLOR_SAMPLE = "#e74c3c"        # 红色 - 样本
COLOR_ESTIMATE = "#2ecc71"      # 绿色 - 估计值
COLOR_TRUE_VALUE = "#9b59b6"    # 紫色 - 真实值
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
```

## 示例设计
```python
# 总体：假设有100个数据点
POPULATION_SIZE = 100
POPULATION_MEAN = 75  # 总体平均数（真实值）
POPULATION_STD = 10   # 总体标准差

# 样本
SAMPLE_SIZES = [5, 10, 30]  # 不同的样本容量
SAMPLE_MEANS = [72, 74, 75]  # 对应的样本平均数（示例）

# 可视化配置
DOT_RADIUS = 0.08
GRID_SIZE = 10  # 10×10网格展示总体
```

## 坐标系配置
```python
# 总体展示区域
POPULATION_AREA = {
    "center": UP * 2,
    "width": 6,
    "height": 4
}

# 样本展示区域
SAMPLE_AREA = {
    "center": DOWN * 2,
    "width": 4,
    "height": 2
}

# 对比图表区域
COMPARISON_AREA = {
    "center": ORIGIN,
    "x_range": [0, 40, 10],
    "y_range": [60, 90, 10]
}
```

## 元素边界检查
- 总体区域: y ∈ [0, +4]（主内容区上部）
- 样本区域: y ∈ [-4, -1]（主内容区下部）
- 标题: y = +6
- 说明文字: y ∈ [-5.5, -5]
- 作者信息: y = +7

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 抓住注意力，引出问题

### 元素
1. 作者标识（顶部）
2. 钩子问题（大字）
3. 问题情境

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` | 1.1s |
| 1.1s | 问题情境 | `FadeIn(scenario)` | 1.7s |
| 1.7s | 问题文字 | `Write(question, run_time=1.0)` | 2.7s |
| 2.7s | 等待理解 | `Wait(1.5)` | 4.2s |

### 清理
- FadeOut: hook_text, scenario, question
- 保留: author_info

**检查点**: 
- hook_text 位置: y = +6 ✓
- scenario 位置: y = +2 ✓
- question 位置: y = -3 ✓

---

## Scene 2: 总体与样本概念 (5-12秒)
**目的**: 建立总体和样本的概念

### 元素
1. 标题："总体与样本"
2. 总体：100个蓝色点（10×10网格）
3. 标签："总体：所有对象"

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 标题写入 | `Write(title)` | 0.8s |
| 0.8s | 总体点逐渐出现 | `LaggedStart FadeIn` | 2.8s |
| 2.8s | 总体标签 | `FadeIn(population_label)` | 3.3s |
| 3.3s | 说明文字 | `FadeIn(explanation)` | 3.8s |
| 3.8s | 等待 | `Wait(1.5)` | 5.3s |

### 清理
- 保留: title（变换）, population_dots

**检查点**:
- population_dots 位置: y ∈ [0, +4] ✓
- explanation 位置: y = -5 ✓

---

## Scene 3: 抽样过程 (12-20秒)
**目的**: 展示从总体中抽取样本的过程

### 元素
1. 抽样箭头动画
2. 样本点移动到样本区域
3. 样本标签

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 新标题 | `Transform(title)` | 0.5s |
| 0.5s | 说明抽样 | `FadeIn(sampling_text)` | 1.0s |
| 1.0s | 高亮第1个点 | `Indicate(dot_1)` | 1.5s |
| 1.5s | 箭头指向样本区 | `Create(arrow_1)` | 2.0s |
| 2.0s | 点变色移动 | `dot.animate.set_color().move_to()` | 2.8s |
| 2.8s | 重复5次 | `循环抽样` | 5.8s |
| 5.8s | 样本标签 | `FadeIn(sample_label)` | 6.3s |
| 6.3s | 等待 | `Wait(1.0)` | 7.3s |

### 清理
- FadeOut: arrows, sampling_text
- 保留: population_dots, sample_dots

**检查点**:
- sample_dots 位置: y ∈ [-4, -1] ✓
- arrows 路径在边界内 ✓

---

## Scene 4: 样本平均数估计 (20-32秒)
**目的**: 展示用样本平均数估计总体平均数

### 元素
1. 总体平均数（真实值）
2. 样本平均数（估计值）
3. 对比展示

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 新标题 | `Transform(title)` | 0.5s |
| 0.5s | 计算样本平均数 | `Write(sample_mean_calc)` | 2.0s |
| 2.0s | 样本平均数结果 | `Write(sample_mean_result)` | 2.8s |
| 2.8s | 总体平均数（未知）| `FadeIn(population_mean_text)` | 3.3s |
| 3.3s | 估计关系 | `Create(estimate_arrow)` | 4.3s |
| 4.3s | 公式 | `Write(formula)` | 5.8s |
| 5.8s | 对比数值 | `FadeIn(comparison)` | 6.8s |
| 6.8s | 强调接近 | `Indicate(values)` | 7.8s |
| 7.8s | 等待 | `Wait(1.5)` | 9.3s |

### 清理
- FadeOut: calculations, comparison
- 保留: 部分标注

**检查点**:
- formula 位置: y = +5 ✓
- comparison 位置: y = 0 ✓

---

## Scene 5: 样本容量的影响 (32-45秒)
**目的**: 展示样本容量对估计准确性的影响

### 元素
1. 三种不同容量的样本
2. 对应的估计值
3. 对比图表

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 新标题 | `Transform(title)` | 0.5s |
| 0.5s | 清空旧样本 | `FadeOut(old_sample)` | 1.0s |
| 1.0s | 小样本(n=5) | `Create sample_5` | 2.0s |
| 2.0s | 估计值1 | `Write(estimate_5)` | 2.8s |
| 2.8s | 中样本(n=10) | `Transform to sample_10` | 3.8s |
| 3.8s | 估计值2 | `Write(estimate_10)` | 4.6s |
| 4.6s | 大样本(n=30) | `Transform to sample_30` | 5.6s |
| 5.6s | 估计值3 | `Write(estimate_30)` | 6.4s |
| 6.4s | 对比图表 | `Create(comparison_chart)` | 8.4s |
| 8.4s | 结论 | `FadeIn(conclusion)` | 9.4s |
| 9.4s | 等待 | `Wait(2.0)` | 11.4s |

### 清理
- FadeOut: samples, chart
- 保留: conclusion（变换）

**检查点**:
- samples 位置: y ∈ [-4, -1] ✓
- chart 位置: y ∈ [-2, +2] ✓

---

## Scene 6: 代表性的重要性 (45-55秒)
**目的**: 强调样本的代表性

### 元素
1. 有偏样本示例
2. 代表性样本示例
3. 对比效果

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 新标题 | `Transform(title)` | 0.5s |
| 0.5s | 有偏样本 | `Create(biased_sample)` | 1.5s |
| 1.5s | 偏差大 | `Write(biased_result)` | 2.5s |
| 2.5s | 代表性样本 | `Transform to representative` | 3.5s |
| 3.5s | 估计准确 | `Write(accurate_result)` | 4.5s |
| 4.5s | 对比 | `Create(comparison)` | 5.5s |
| 5.5s | 关键要点 | `FadeIn(key_point)` | 6.5s |
| 6.5s | 等待 | `Wait(2.0)` | 8.5s |

### 清理
- FadeOut: samples, comparison

**检查点**:
- samples 位置: y ∈ [-3, +3] ✓

---

## Scene 7: 总结和片尾 (55-70秒)
**目的**: 总结要点，引导关注

### 元素
1. 三大要点总结
2. 关键公式
3. 片尾信息

### 动画序列
| 时间 | 动作 | 代码参考 | 累计时长 |
|------|------|---------|---------|
| 0.0s | 清空画面 | `FadeOut(all)` | 0.5s |
| 0.5s | 总结标题 | `Write(summary_title)` | 1.5s |
| 1.5s | 要点1：样本估计总体 | `FadeIn(point_1)` | 2.5s |
| 2.5s | 要点2：容量越大越准 | `FadeIn(point_2)` | 3.5s |
| 3.5s | 要点3：代表性重要 | `FadeIn(point_3)` | 4.5s |
| 4.5s | 关键公式 | `Write(formulas)` | 6.5s |
| 6.5s | 片尾动画 | `Outro animation` | 10.5s |
| 10.5s | 淡出 | `FadeOut(all)` | 12.0s |

**检查点**:
- summary 位置: y ∈ [0, +5] ✓
- points 位置: y ∈ [-2, +2] ✓

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 始终保留顶部 |
| population_dots | Scene 2 | Scene 6 | 总体点集 |
| sample_dots | Scene 3 | Scene 6 | 样本点集 |
| title | Scene 2 | Scene 7 | 不断变换 |
| arrows | Scene 3 | Scene 3 | 临时抽样箭头 |
| comparison_chart | Scene 5 | Scene 5 | 对比图表 |
| summary | Scene 7 | Scene 7 | 总结 |

---

## 关键技术点

### 1. 总体点阵生成
```python
# 10×10网格生成100个点
population_dots = VGroup()
for i in range(10):
    for j in range(10):
        dot = Dot(
            radius=DOT_RADIUS,
            color=COLOR_POPULATION,
            fill_opacity=0.8
        )
        # 定位到网格位置
        x = (j - 4.5) * 0.5
        y = (i - 4.5) * 0.5 + 2  # 偏移到上方
        dot.move_to([x, y, 0])
        population_dots.add(dot)
```

### 2. 随机抽样动画
```python
# 随机选择若干个点作为样本
import random
sample_indices = random.sample(range(100), sample_size)

for idx in sample_indices:
    dot = population_dots[idx]
    
    # 创建箭头
    arrow = Arrow(
        dot.get_center(),
        sample_area_center,
        color=COLOR_SAMPLE
    )
    
    # 动画：高亮→箭头→移动→变色
    self.play(
        Indicate(dot, color=COLOR_HIGHLIGHT),
        run_time=0.3
    )
    self.play(Create(arrow), run_time=0.4)
    self.play(
        dot.animate.move_to(sample_position).set_color(COLOR_SAMPLE),
        FadeOut(arrow),
        run_time=0.6
    )
```

### 3. 样本容量对比
```python
# 创建对比图表
sizes = [5, 10, 30]
estimates = [72, 74, 75]
true_value = 75

# 使用 BarChart 或手动创建柱状图
bars = VGroup()
for i, (size, est) in enumerate(zip(sizes, estimates)):
    bar = Rectangle(
        width=0.5,
        height=(est - 60) / 30 * 4,  # 缩放到合适高度
        fill_color=COLOR_SAMPLE,
        fill_opacity=0.7
    )
    bar.move_to([i * 1.5 - 1.5, 0, 0])
    bars.add(bar)

# 真实值参考线
true_line = DashedLine(
    LEFT * 3,
    RIGHT * 3,
    color=COLOR_TRUE_VALUE
).move_to(UP * ((true_value - 60) / 30 * 4 - 2))
```

### 4. 代表性对比
```python
# 有偏样本：只从一侧抽取
biased_indices = list(range(0, 10))  # 前10个

# 代表性样本：随机分布抽取
representative_indices = random.sample(range(100), 10)

# 视觉对比
biased_group = VGroup(*[population_dots[i] for i in biased_indices])
representative_group = VGroup(*[population_dots[i] for i in representative_indices])

# 用矩形框标注
biased_box = SurroundingRectangle(biased_group, color=RED)
representative_scatter = VGroup(*[
    Circle(radius=0.15, color=GREEN).move_to(population_dots[i])
    for i in representative_indices
])
```

---

## 验证清单

### 统计验证
- [x] 样本从总体中抽取
- [x] 样本容量设置合理（5, 10, 30）
- [x] 估计值接近真实值

### 视觉验证
- [x] 所有元素在边界内
- [x] 总体和样本区分清晰
- [x] 动画流畅自然
- [x] 颜色对比明显

### 公式验证
- [x] 无中文字符混入LaTeX
- [x] 公式格式正确

### 角度验证
- [ ] 本动画不涉及几何角度

### 节奏验证
- [x] 开场 < 5秒
- [x] 每个概念停留 2-3秒
- [x] 总时长 60-70秒
- [x] 抽样动画流畅

---

## 预期效果

1. **教学目标**：学生理解用样本估计总体的原理和方法
2. **视觉记忆**：蓝色总体、红色样本、抽样动画
3. **关键洞察**：样本容量越大，估计越准确；代表性很重要
4. **应用场景**：问卷调查、质量检测、民意调查

---

## 备注

- 使用点阵可视化总体和样本
- 抽样动画是核心，需要流畅自然
- 对比不同样本容量的效果是重点
- 强调代表性的重要性（避免有偏样本）
- 不涉及复杂几何计算，主要是统计可视化