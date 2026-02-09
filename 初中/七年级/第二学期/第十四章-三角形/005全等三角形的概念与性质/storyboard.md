# 全等三角形的概念与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 8 个
- 难度等级: 中等
- 年级: 七年级
- 知识点: 全等三角形的概念与性质

## 颜色配置
```python
COLOR_TRIANGLE_1 = "#3498db"      # 蓝色 - 第一个三角形
COLOR_TRIANGLE_2 = "#e74c3c"      # 红色 - 第二个三角形
COLOR_CONGRUENT = "#2ecc71"       # 绿色 - 重合后的颜色
COLOR_HIGHLIGHT = YELLOW          # 高亮
COLOR_AUXILIARY = GRAY_B          # 辅助线/文字
COLOR_CORRESPONDENCE = "#f39c12"  # 橙色 - 对应关系标注
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 三角形ABC顶点 | 基准定义 | self.A, self.B, self.C |
| 三角形DEF顶点 | 初始位置（右侧偏移） | self.D, self.E, self.F |
| 三角形DEF目标位置 | 与ABC完全重合 | self.D_target, self.E_target, self.F_target |
| 边长 | np.linalg.norm() | self.AB, self.BC, self.CA |
| 角度 | 向量夹角公式 | self.angle_A, self.angle_B, self.angle_C |

---

## Scene 1: 开场钩子 (4秒)
**目的**: 抓住学生注意力，引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题："这两个三角形有什么关系?"
3. 两个三角形（不同颜色，不同位置）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text, run_time=0.8)` |
| 1.1s | 第一个三角形创建 | `Create(triangle_ABC, run_time=1.0)` |
| 2.1s | 第二个三角形创建 | `Create(triangle_DEF, run_time=1.0)` |
| 3.1s | 等待思考 | `Wait(0.8)` |

### 清理
- FadeOut: hook_text
- 保留: triangle_ABC, triangle_DEF, author_info

---

## Scene 2: 定义全等三角形 (6秒)
**目的**: 给出全等三角形的定义

### 元素
1. 标题："全等三角形"
2. 定义文字："能够完全重合的两个三角形"
3. 两个三角形（保持）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题淡入 | `FadeIn(title, shift=DOWN*0.3)` |
| 0.5s | 定义文字书写 | `Write(definition, run_time=1.2)` |
| 1.7s | 强调"完全重合" | `Indicate(key_words, color=YELLOW)` |
| 2.7s | 等待理解 | `Wait(1.5)` |

### 清理
- 保留: title（缩小移至顶部）
- FadeOut: definition
- 保留: triangle_ABC, triangle_DEF

---

## Scene 3: 演示重合过程 (8秒)
**目的**: 通过动画演示"完全重合"的过程

### 元素
1. 三角形DEF进行平移、旋转变换
2. 重合过程的说明文字
3. 重合后改变颜色

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 提示文字 | `FadeIn(hint_text)` "让我们试试重合" |
| 0.8s | DEF平移到ABC附近 | `triangle_DEF.animate.move_to(ABC位置)` |
| 2.3s | DEF旋转对齐 | `triangle_DEF.animate.rotate(angle)` |
| 4.0s | 完全重合闪光 | `Flash(重合位置, color=GREEN)` |
| 4.5s | 改变颜色表示重合 | `triangle_DEF.animate.set_color(GREEN)` |
| 5.5s | 提示"完全重合!" | `FadeIn(success_text)` |
| 6.5s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hint_text, success_text
- 保留: triangle_ABC, triangle_DEF（重合状态）

---

## Scene 4: 介绍全等符号 (5秒)
**目的**: 教授全等符号的写法

### 元素
1. 全等符号公式：△ABC ≌ △DEF
2. 说明文字："读作：三角形ABC全等于三角形DEF"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 将两三角形分开 | `triangle_DEF.animate.shift(RIGHT*3)` |
| 1.2s | 全等符号书写 | `Write(congruence_formula, run_time=1.5)` |
| 2.7s | 读法说明淡入 | `FadeIn(reading_text)` |
| 3.5s | 等待 | `Wait(1.2)` |

### 清理
- FadeOut: reading_text
- 保留: congruence_formula（移至顶部）
- 保留: triangle_ABC, triangle_DEF

---

## Scene 5: 标注对应关系 (8秒)
**目的**: 强调对应顶点、对应边、对应角

### 元素
1. 顶点标签：A, B, C, D, E, F
2. 对应关系箭头
3. 说明："确定对应关系很重要!"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 顶点标签淡入 | `FadeIn(labels, lag_ratio=0.2)` |
| 1.0s | 说明文字 | `FadeIn(correspondence_text)` |
| 1.8s | A↔D 箭头 | `GrowArrow(arrow_AD)` |
| 2.5s | B↔E 箭头 | `GrowArrow(arrow_BE)` |
| 3.2s | C↔F 箭头 | `GrowArrow(arrow_CF)` |
| 4.0s | 高亮对应 | `Indicate(对应组, scale=1.2)` |
| 5.5s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: arrows, correspondence_text
- 保留: labels, triangles

---

## Scene 6: 性质1 - 对应边相等 (10秒)
**目的**: 展示对应边相等的性质

### 元素
1. 标题："性质1：对应边相等"
2. 三组边的等式
3. 边长标注和高亮

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 性质标题淡入 | `FadeIn(property_title)` |
| 0.8s | AB边高亮 | `triangle_ABC边[AB].animate.set_color(YELLOW)` |
| 1.3s | DE边高亮 | `triangle_DEF边[DE].animate.set_color(YELLOW)` |
| 1.8s | 等式AB=DE书写 | `Write(equation_1)` |
| 3.0s | 恢复颜色，BC边高亮 | 同上流程 |
| 4.5s | 等式BC=EF书写 | `Write(equation_2)` |
| 5.7s | CA边高亮 | 同上 |
| 7.0s | 等式CA=FD书写 | `Write(equation_3)` |
| 8.2s | 三个等式组合展示 | `VGroup(equations).arrange(DOWN)` |
| 9.0s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: property_title, equations
- 边恢复原色
- 保留: labels, triangles

---

## Scene 7: 性质2 - 对应角相等 (10秒)
**目的**: 展示对应角相等的性质

### 元素
1. 标题："性质2：对应角相等"
2. 三组角的等式
3. 角度标注和弧线

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 性质标题淡入 | `FadeIn(property_title)` |
| 0.8s | 角A的弧线 | `Create(angle_arc_A)` |
| 1.3s | 角D的弧线 | `Create(angle_arc_D)` |
| 1.8s | 等式∠A=∠D书写 | `Write(equation_1)` |
| 3.0s | 角B、角E弧线 | 同上流程 |
| 4.5s | 等式∠B=∠E书写 | `Write(equation_2)` |
| 5.7s | 角C、角F弧线 | 同上 |
| 7.0s | 等式∠C=∠F书写 | `Write(equation_3)` |
| 8.2s | 三个等式组合展示 | `VGroup(equations).arrange(DOWN)` |
| 9.0s | 等待 | `Wait(0.8)` |

### 清理
- FadeOut: property_title, equations, angle_arcs
- 保留: labels, triangles

---

## Scene 8: 总结与片尾 (8秒)
**目的**: 强调书写顺序的重要性，引导关注

### 元素
1. 重点提示："注意：对应顶点的书写顺序要对应!"
2. 示例对比：正确 vs 错误
3. 作者信息和关注提示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 重点提示淡入 | `FadeIn(warning_text, scale=1.1)` |
| 1.0s | 正确示例 | `FadeIn(correct_example, color=GREEN)` |
| 2.0s | 错误示例 | `FadeIn(wrong_example, color=RED)` |
| 3.0s | 对比闪烁 | `Flash(), Indicate()` |
| 4.5s | 清理三角形 | `FadeOut(triangles, labels)` |
| 5.0s | 作者信息放大 | `author_info.animate.scale(1.5)` |
| 5.8s | 关注提示 | `FadeIn(follow_text)` |
| 6.8s | 装饰动画 | 小三角形旋转 |
| 7.8s | 全部淡出 | `FadeOut(all)` |

### 清理
- 全部元素淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 8 | 全程保留，最后放大 |
| triangle_ABC | Scene 1 | Scene 8 | 主三角形 |
| triangle_DEF | Scene 1 | Scene 8 | 第二个三角形 |
| title | Scene 2 | Scene 4 | 移至顶部后保留 |
| congruence_formula | Scene 4 | Scene 8 | 移至顶部 |
| labels (A-F) | Scene 5 | Scene 8 | 顶点标签 |
| property_title_1 | Scene 6 | Scene 6 | 临时标题 |
| property_title_2 | Scene 7 | Scene 7 | 临时标题 |
| equations | Scene 6, 7 | Scene 6, 7 | 临时公式 |

---

## 关键几何计算验证点

### 三角形ABC（基准）
```python
self.A = np.array([-2.5, 0.5, 0]) * SCALE + OFFSET
self.B = np.array([1.0, -1.5, 0]) * SCALE + OFFSET
self.C = np.array([-0.5, 2.0, 0]) * SCALE + OFFSET
```

### 三角形DEF（初始位置 - 右侧）
```python
# 初始位置：右侧偏移
self.D_init = self.A + RIGHT * 5
self.E_init = self.B + RIGHT * 5
self.F_init = self.C + RIGHT * 5

# 目标位置：完全重合（与ABC相同）
self.D_target = self.A
self.E_target = self.B
self.F_target = self.C
```

### 验证
- 边长验证：AB = DE, BC = EF, CA = FD
- 角度验证：∠A = ∠D, ∠B = ∠E, ∠C = ∠F
- 重合验证：目标位置与ABC完全一致

---

## 节奏控制要点

1. **开场要快** (4秒内抓住注意力)
2. **定义要清晰** (慢速书写，强调关键词)
3. **重合演示要流畅** (平滑动画，避免卡顿)
4. **性质展示要有节奏** (分步高亮，逐个呈现)
5. **总结要简洁有力** (强调书写顺序)

## 字体大小使用规范
- 标题: 36
- 定义/性质: 28
- 公式: 28
- 说明文字: 22
- 顶点标签: 24
- 小提示: 20