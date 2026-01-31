# 通分 (Finding Common Denominators) - 动画分镜脚本

<!-- /root/code/sss/media/videos/fraction_properties/1920p60/FractionProperties.mp4 -->

## 元信息
- 目标时长: 60-75秒
- 场景数量: 7个
- 难度等级: 六年级基础
- 知识点: 通分 (将异分母分数转化为同分母分数)

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要分数
COLOR_SECONDARY = "#e74c3c"    # 红色 - 第二个分数
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_COMMON = "#2ecc71"       # 绿色 - 公分母/结果
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线/说明
COLOR_STEP = "#f39c12"         # 橙色 - 步骤标记
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 | 说明 |
|------|---------|---------|------|
| 饼图1中心 | np.array([-2.5, 2, 0]) | self.pie1_center | 1/3的饼图 |
| 饼图2中心 | np.array([2.5, 2, 0]) | self.pie2_center | 1/4的饼图 |
| 饼图半径 | 1.2 | self.pie_radius | 统一半径 |
| 公式位置 | UP * 5.5 | - | 顶部公式区域 |
| 说明文字位置 | DOWN * 4.5 | - | 底部说明区域 |

## 关键数学概念
1. **通分目的**: 为了进行分数加减法
2. **最小公倍数**: lcm(3, 4) = 12
3. **分数基本性质**: 分子分母同时乘以相同的数，分数值不变
4. **具体例子**: 1/3 = 4/12, 1/4 = 3/12

---

## Scene 1: 开场钩子 (0-5秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字动画)
3. 两个不同的分数: 1/3 和 1/4

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` | 0.3s |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | 1.0s |
| 1.3s | 显示 1/3 | `FadeIn(frac_1, shift=DOWN*0.3)` | 0.5s |
| 1.8s | 显示 + 号 | `FadeIn(plus_sign)` | 0.3s |
| 2.1s | 显示 1/4 | `FadeIn(frac_2, shift=DOWN*0.3)` | 0.5s |
| 2.6s | 疑问标记闪烁 | `Flash(question_mark)` | 0.4s |
| 3.0s | 等待理解 | `Wait(1.5)` | 1.5s |

### 清理
- FadeOut: hook_text, question_mark
- 保留: author_info, frac_1, plus_sign, frac_2

---

## Scene 2: 问题可视化 - 饼图展示 (5-12秒)
**目的**: 用视觉图形展示为什么不能直接相加

### 元素
1. 1/3 的饼图 (分成3份，填充1份)
2. 1/4 的饼图 (分成4份，填充1份)
3. 说明文字

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 分数移动到饼图上方 | `frac_1.animate.move_to(pie1_top)` | 0.8s |
| 0.8s | 绘制饼图1完整圆 | `Create(pie1_full)` | 0.6s |
| 1.4s | 分割成3份 | `Create(pie1_divisions)` | 0.5s |
| 1.9s | 填充1份 | `FadeIn(pie1_fill)` | 0.4s |
| 2.3s | 绘制饼图2完整圆 | `Create(pie2_full)` | 0.6s |
| 2.9s | 分割成4份 | `Create(pie2_divisions)` | 0.5s |
| 3.4s | 填充1份 | `FadeIn(pie2_fill)` | 0.4s |
| 3.8s | 显示问题说明 | `FadeIn(explain_text)` | 0.5s |
| 4.3s | 等待理解 | `Wait(1.5)` | 1.5s |

### 说明文字
"分母不同，不能直接相加！"

### 清理
- FadeOut: explain_text
- 保留: 饼图、分数

---

## Scene 3: 引入通分概念 (12-20秒)
**目的**: 解释什么是通分，为什么需要通分

### 元素
1. 标题: "通分"
2. 定义文字
3. 箭头指向变换

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 标题书写 | `Write(title)` | 0.8s |
| 0.8s | 定义显示 | `FadeIn(definition, shift=UP*0.2)` | 0.6s |
| 1.4s | 高亮"同分母" | `definition[key_part].animate.set_color(YELLOW)` | 0.4s |
| 1.8s | 显示目标 | `FadeIn(goal_text)` | 0.5s |
| 2.3s | 等待理解 | `Wait(2.0)` | 2.0s |
| 4.3s | 淡出标题和定义 | `FadeOut(title, definition)` | 0.5s |

### 文字内容
- 标题: "通分"
- 定义: "把异分母分数化成同分母分数"
- 目标: "找到公分母: 3和4的最小公倍数"

### 清理
- FadeOut: title, definition
- 保留: goal_text, 饼图

---

## Scene 4: 寻找最小公倍数 (20-30秒)
**目的**: 教学生如何找最小公倍数

### 元素
1. 3的倍数列表
2. 4的倍数列表
3. 公倍数标记
4. 最小公倍数突出显示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 显示"3的倍数:" | `Write(label_3)` | 0.5s |
| 0.5s | 逐个显示: 3,6,9,12,15... | `LaggedStart(*[FadeIn(n) for n in nums_3])` | 1.5s |
| 2.0s | 显示"4的倍数:" | `Write(label_4)` | 0.5s |
| 2.5s | 逐个显示: 4,8,12,16... | `LaggedStart(*[FadeIn(n) for n in nums_4])` | 1.5s |
| 4.0s | 12同时出现在两个列表 | `Flash(twelve_3), Flash(twelve_4)` | 0.6s |
| 4.6s | 圈出两个12 | `Create(circle_3), Create(circle_4)` | 0.5s |
| 5.1s | 显示结论 | `FadeIn(conclusion)` | 0.6s |
| 5.7s | 等待 | `Wait(1.5)` | 1.5s |

### 文字内容
- "3的倍数: 3, 6, 9, 12, 15, 18..."
- "4的倍数: 4, 8, 12, 16, 20..."
- "最小公倍数 = 12"

### 清理
- FadeOut: 倍数列表, goal_text
- 保留: conclusion (最小公倍数=12)

---

## Scene 5: 通分过程 - 1/3 (30-40秒)
**目的**: 详细展示如何将 1/3 转化为 4/12

### 元素
1. 原分数 1/3
2. 转化箭头
3. 新分数 4/12
4. 说明: "分子分母同乘4"

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 1/3高亮 | `frac_1.animate.set_color(YELLOW)` | 0.3s |
| 0.3s | 显示步骤说明 | `FadeIn(step_1_text)` | 0.5s |
| 0.8s | 显示乘法: 1×4 / 3×4 | `Write(multiply_formula)` | 1.0s |
| 1.8s | 饼图1重新分割成12份 | `Transform(pie1_3parts, pie1_12parts)` | 1.2s |
| 3.0s | 填充4份 | `FadeIn(pie1_fill_4)` | 0.6s |
| 3.6s | 显示结果 4/12 | `TransformMatchingTex(multiply_formula, result_4_12)` | 0.8s |
| 4.4s | 验证相等 | `FadeIn(equals_sign)` | 0.3s |
| 4.7s | 等待 | `Wait(1.5)` | 1.5s |

### 文字内容
- "分子分母同乘 4"
- "1/3 = 4/12"
- "分数的值不变！"

### 清理
- FadeOut: step_1_text, multiply_formula
- 保留: 新饼图, result_4_12

---

## Scene 6: 通分过程 - 1/4 (40-50秒)
**目的**: 详细展示如何将 1/4 转化为 3/12

### 元素
1. 原分数 1/4
2. 转化箭头
3. 新分数 3/12
4. 说明: "分子分母同乘3"

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 1/4高亮 | `frac_2.animate.set_color(YELLOW)` | 0.3s |
| 0.3s | 显示步骤说明 | `FadeIn(step_2_text)` | 0.5s |
| 0.8s | 显示乘法: 1×3 / 4×3 | `Write(multiply_formula_2)` | 1.0s |
| 1.8s | 饼图2重新分割成12份 | `Transform(pie2_4parts, pie2_12parts)` | 1.2s |
| 3.0s | 填充3份 | `FadeIn(pie2_fill_3)` | 0.6s |
| 3.6s | 显示结果 3/12 | `TransformMatchingTex(multiply_formula_2, result_3_12)` | 0.8s |
| 4.4s | 验证相等 | `FadeIn(equals_sign_2)` | 0.3s |
| 4.7s | 等待 | `Wait(1.5)` | 1.5s |

### 文字内容
- "分子分母同乘 3"
- "1/4 = 3/12"

### 清理
- FadeOut: step_2_text, multiply_formula_2
- 保留: 新饼图, result_3_12

---

## Scene 7: 总结与加法 (50-65秒)
**目的**: 展示通分后可以进行加法，总结要点

### 元素
1. 完整的加法算式
2. 结果
3. 总结要点
4. 关注提示

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 两个饼图合并动画 | `pie1.animate.move_to(...), pie2.animate.move_to(...)` | 1.0s |
| 1.0s | 显示完整算式 | `Write(final_equation)` | 1.2s |
| 2.2s | 计算结果 | `Write(final_result)` | 0.8s |
| 3.0s | 饼图合并显示7/12 | `FadeIn(combined_pie)` | 1.0s |
| 4.0s | 显示总结标题 | `Write(summary_title)` | 0.6s |
| 4.6s | 要点1 | `FadeIn(point_1, shift=LEFT*0.3)` | 0.5s |
| 5.1s | 要点2 | `FadeIn(point_2, shift=LEFT*0.3)` | 0.5s |
| 5.6s | 要点3 | `FadeIn(point_3, shift=LEFT*0.3)` | 0.5s |
| 6.1s | 等待 | `Wait(2.0)` | 2.0s |

### 文字内容
- 完整算式: "1/3 + 1/4 = 4/12 + 3/12 = 7/12"
- 总结标题: "通分三步骤:"
- 要点1: "① 找最小公倍数"
- 要点2: "② 分子分母同乘"
- 要点3: "③ 分数值不变"

### 清理
- 准备片尾

---

## Scene 8: 片尾关注 (65-75秒)
**目的**: 品牌露出，引导关注

### 元素
1. 作者名称放大
2. 关注提示
3. 装饰动画

### 动画序列
| 时间 | 动作 | 代码参考 | 持续时间 |
|------|------|---------|---------|
| 0.0s | 清空所有内容 | `FadeOut(all_objects)` | 0.6s |
| 0.6s | 作者名称放大 | `Transform(author_info, author_large)` | 0.8s |
| 1.4s | ID显示 | `FadeIn(author_id)` | 0.5s |
| 1.9s | 关注文字 | `FadeIn(follow_text, scale=1.2)` | 0.6s |
| 2.5s | 分数图标旋转 | `Rotate(fraction_icons, PI)` | 1.5s |
| 4.0s | 全部淡出 | `FadeOut(all)` | 1.0s |

### 文字内容
- "上海初高中数学直通车"
- "@emptyandcalm"
- "关注我，学更多数学技巧！"

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留 |
| frac_1 (1/3) | Scene 1 | Scene 7 | 主要分数1 |
| frac_2 (1/4) | Scene 1 | Scene 7 | 主要分数2 |
| pie1 | Scene 2 | Scene 7 | 饼图1 |
| pie2 | Scene 2 | Scene 7 | 饼图2 |
| lcm_conclusion | Scene 4 | Scene 5 | 最小公倍数结论 |
| result_4_12 | Scene 5 | Scene 7 | 通分结果1 |
| result_3_12 | Scene 6 | Scene 7 | 通分结果2 |
| final_equation | Scene 7 | Scene 8 | 最终算式 |

---

## 技术要点

### 饼图绘制精确计算
```python
# 1/3的饼图 (120度扇形)
angle_1_3 = 2 * PI / 3
sector_1_3 = AnnularSector(
    inner_radius=0,
    outer_radius=self.pie_radius,
    angle=angle_1_3,
    start_angle=PI/2,  # 从顶部开始
    color=COLOR_PRIMARY,
    fill_opacity=0.6
)

# 1/4的饼图 (90度扇形)
angle_1_4 = PI / 2
sector_1_4 = AnnularSector(
    inner_radius=0,
    outer_radius=self.pie_radius,
    angle=angle_1_4,
    start_angle=PI/2,
    color=COLOR_SECONDARY,
    fill_opacity=0.6
)
```

### 分数变换动画
使用 `TransformMatchingTex` 进行平滑的分数变换，确保分子分母正确对应。

### 位置管理
- 公式区: y ∈ [4, 6]
- 主内容区: y ∈ [-2, 4]
- 说明区: y ∈ [-4.5, -3]
- 保持 x ∈ [-4, 4] 安全边界

---

## 预期学习效果

学生通过本动画应该掌握:
1. ✓ 理解通分的目的 (为了加减法)
2. ✓ 掌握找最小公倍数的方法
3. ✓ 理解分数基本性质 (同乘不变)
4. ✓ 能够独立进行通分操作

---

## 渲染参数
```bash
# 预览
manim -pql tongfen.py TongFenAnimation

# 高清渲染
manim -qh tongfen.py TongFenAnimation
```