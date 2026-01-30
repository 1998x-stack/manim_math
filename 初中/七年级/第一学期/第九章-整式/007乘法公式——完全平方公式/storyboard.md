# 完全平方公式 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中基础
- 目标受众: 七年级学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主公式
COLOR_SECONDARY = "#e74c3c"    # 红色 - a项
COLOR_TERTIARY = "#2ecc71"     # 绿色 - b项
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 正方形边长a | 固定值 2.0 | self.side_a |
| 正方形边长b | 固定值 1.0 | self.side_b |
| 大正方形顶点 | (a+b)为边长的正方形 | self.square_vertices |
| 分割点 | 边上距离a和b的点 | self.split_points |
| 小矩形区域 | 4个区域坐标 | self.regions |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字动画)
3. 公式预览 (神秘感)

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | 顶部固定 |
| 0.3s | 钩子文字打字效果 | `Write(hook_text)` | "你知道(a+b)²等于什么吗?" |
| 1.3s | 公式神秘显现 | `FadeIn(formula_preview, scale=1.2)` | (a+b)² = ? |
| 2.3s | 等待思考 | `Wait(1.0)` | 给学生思考时间 |

### 清理
- FadeOut: hook_text, formula_preview
- 保留: author_info

### 位置规划
- author_info: y = 7
- hook_text: y = 5
- formula_preview: y = 2

---

## Scene 2: 公式展开 (6-8秒)
**目的**: 展示完整公式，建立视觉记忆

### 元素
1. 完全平方公式 (两个版本)
2. 步骤标题
3. 强调标注

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 标题写入 | `Write(title)` | "完全平方公式" |
| 0.8s | 第一个公式展开 | `Write(formula_1)` | (a+b)² = a² + 2ab + b² |
| 2.0s | 标注关键项 | `Indicate(middle_term)` | 强调2ab |
| 2.8s | 第二个公式展开 | `Write(formula_2)` | (a-b)² = a² - 2ab + b² |
| 4.0s | 标注符号差异 | `Flash(minus_sign)` | 强调负号 |
| 5.0s | 记忆口诀出现 | `FadeIn(mnemonic)` | "首平方，尾平方，首尾二倍放中央" |
| 6.5s | 等待记忆 | `Wait(1.5)` | 重点停留 |

### 清理
- FadeOut: title, mnemonic
- 保留: formula_1 (缩小移到顶部)
- FadeOut: formula_2

### 位置规划
- title: y = 6
- formula_1: y = 3
- formula_2: y = 0
- mnemonic: y = -3

---

## Scene 3: 几何直观 - 构造大正方形 (8-10秒)
**目的**: 用几何图形直观理解公式

### 几何计算
```python
# 基准参数
self.side_a = 2.0
self.side_b = 1.0
self.total_side = self.side_a + self.side_b  # 3.0

# 中心位置
self.center = np.array([0, 1.5, 0])

# 大正方形顶点（边长 a+b）
half = self.total_side / 2
self.vertices = [
    self.center + np.array([-half, -half, 0]),  # 左下
    self.center + np.array([half, -half, 0]),   # 右下
    self.center + np.array([half, half, 0]),    # 右上
    self.center + np.array([-half, half, 0])    # 左上
]

# 分割点（边上的切分点）
self.split_horizontal = self.center[1] + (self.side_a - self.side_b) / 2
self.split_vertical = self.center[0] + (self.side_a - self.side_b) / 2
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 说明文字 | `Write(explanation)` | "用正方形来理解" |
| 0.8s | 创建大正方形 | `Create(big_square)` | 边长(a+b) |
| 2.0s | 标注边长 | `FadeIn(label_side)` | 标注"a+b" |
| 3.0s | 面积公式 | `Write(area_formula)` | 面积 = (a+b)² |
| 4.5s | 等待理解 | `Wait(1.0)` |  |
| 5.5s | 提示分割 | `Write(hint)` | "让我们分割这个正方形" |

### 清理
- FadeOut: explanation, hint
- 保留: big_square, label_side, area_formula (移到角落)

### 位置规划
- big_square: center at (0, 1.5)
- explanation: y = 5
- area_formula: y = -4 (底部)

---

## Scene 4: 几何分割 - 四个区域 (10-12秒)
**目的**: 展示如何分割成4个矩形

### 几何计算
```python
# 四个区域的顶点
# 区域1: a×a (左上红色)
self.region_aa = [
    self.vertices[3],  # 左上角
    np.array([self.split_vertical, self.vertices[3][1], 0]),
    np.array([self.split_vertical, self.split_horizontal, 0]),
    np.array([self.vertices[3][0], self.split_horizontal, 0])
]

# 区域2: a×b (右上绿色)
self.region_ab_1 = [
    np.array([self.split_vertical, self.vertices[2][1], 0]),
    self.vertices[2],
    np.array([self.vertices[2][0], self.split_horizontal, 0]),
    np.array([self.split_vertical, self.split_horizontal, 0])
]

# 区域3: b×a (左下绿色)
self.region_ab_2 = [
    np.array([self.vertices[0][0], self.split_horizontal, 0]),
    np.array([self.split_vertical, self.split_horizontal, 0]),
    np.array([self.split_vertical, self.vertices[0][1], 0]),
    self.vertices[0]
]

# 区域4: b×b (右下蓝色)
self.region_bb = [
    np.array([self.split_vertical, self.split_horizontal, 0]),
    np.array([self.vertices[1][0], self.split_horizontal, 0]),
    self.vertices[1],
    np.array([self.split_vertical, self.vertices[1][1], 0])
]
```

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 绘制横线 | `Create(h_line)` | 水平分割线 |
| 0.6s | 标注上方长度 | `FadeIn(label_a_top)` | 标"a" |
| 1.2s | 标注下方长度 | `FadeIn(label_b_bottom)` | 标"b" |
| 2.0s | 绘制竖线 | `Create(v_line)` | 垂直分割线 |
| 2.6s | 标注左侧长度 | `FadeIn(label_a_left)` | 标"a" |
| 3.2s | 标注右侧长度 | `FadeIn(label_b_right)` | 标"b" |
| 4.0s | 等待观察 | `Wait(0.8)` |  |

### 清理
- 保留: 所有元素进入下一场景

---

## Scene 5: 区域着色与标注 (10-12秒)
**目的**: 给四个区域着色并标注面积

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 区域1着色 | `FillFromCenter(region_aa)` | 红色，透明度0.6 |
| 0.4s | 标注a² | `Write(label_aa)` | 中心显示"a²" |
| 1.0s | 区域2着色 | `FillFromCenter(region_ab_1)` | 绿色，透明度0.6 |
| 1.4s | 标注ab | `Write(label_ab_1)` | 中心显示"ab" |
| 2.0s | 区域3着色 | `FillFromCenter(region_ab_2)` | 绿色，透明度0.6 |
| 2.4s | 标注ab | `Write(label_ab_2)` | 中心显示"ab" |
| 3.0s | 区域4着色 | `FillFromCenter(region_bb)` | 蓝色，透明度0.6 |
| 3.4s | 标注b² | `Write(label_bb)` | 中心显示"b²" |
| 4.2s | 强调两个ab | `Indicate(label_ab_1, label_ab_2)` | 同时闪烁 |
| 5.2s | 等待理解 | `Wait(1.5)` | 重点停留 |

### 清理
- 保留所有元素进入下一场景

---

## Scene 6: 公式推导 (8-10秒)
**目的**: 从几何图形推导出代数公式

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 说明文字 | `Write(explanation)` | "总面积 = 四个小区域之和" |
| 1.0s | 公式开始 | `Write(equation_start)` | "(a+b)² =" |
| 1.8s | 加入a² | `Transform(label_aa, term_aa)` | 从图形飞到公式 |
| 2.6s | 加入第一个ab | `Transform(label_ab_1, term_ab_1)` | + ab |
| 3.4s | 加入第二个ab | `Transform(label_ab_2, term_ab_2)` | + ab |
| 4.2s | 合并2ab | `TransformMatchingTex(ab+ab, 2ab)` | ab + ab → 2ab |
| 5.0s | 加入b² | `Transform(label_bb, term_bb)` | + b² |
| 6.0s | 完整公式闪烁 | `Flash(complete_formula)` | 强调结果 |
| 7.0s | 等待记忆 | `Wait(1.5)` | 重点停留 |

### 清理
- FadeOut: 图形部分
- 保留: 公式移到顶部

### 位置规划
- equation: 从 y=0 移到 y=5

---

## Scene 7: 具体例题与结尾 (8-10秒)
**目的**: 应用公式，巩固理解，引导关注

### 动画序列
| 时间 | 动作 | 代码参考 | 备注 |
|------|------|---------|------|
| 0.0s | 例题出现 | `Write(example_title)` | "例题：计算(x+3)²" |
| 1.0s | 写出公式 | `Write(example_formula)` | (x+3)² = |
| 2.0s | 应用公式 | `Write(step_1)` | x² + 2·x·3 + 3² |
| 3.0s | 简化 | `TransformMatchingTex(step_1, step_2)` | x² + 6x + 9 |
| 4.0s | 标注答案 | `Indicate(step_2)` | 框选答案 |
| 5.0s | 总结文字 | `Write(summary)` | "掌握公式，展开轻松！" |
| 6.0s | 关注提示 | `Write(follow_text)` | "关注我，获得更多数学技巧!" |
| 7.0s | 作者信息放大 | `Transform(author_small, author_large)` |  |
| 8.5s | 装饰动画 | `FadeIn(decorations)` | 小方块装饰 |

### 清理
- 全部淡出

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留 |
| hook_text | Scene 1 | Scene 1 | 钩子文字 |
| formula_1 | Scene 2 | Scene 2→顶部 | 主公式 |
| formula_2 | Scene 2 | Scene 2 | 副公式 |
| big_square | Scene 3 | Scene 6 | 大正方形 |
| h_line, v_line | Scene 4 | Scene 6 | 分割线 |
| region_aa | Scene 5 | Scene 6 | 左上区域 |
| region_ab_1 | Scene 5 | Scene 6 | 右上区域 |
| region_ab_2 | Scene 5 | Scene 6 | 左下区域 |
| region_bb | Scene 5 | Scene 6 | 右下区域 |
| complete_formula | Scene 6 | Scene 7 | 推导结果 |
| example_formula | Scene 7 | Scene 7 | 例题 |

---

## 时间节奏规划
| 场景 | 时长 | 累计时长 |
|------|------|---------|
| Scene 1: 开场钩子 | 3-4s | 4s |
| Scene 2: 公式展开 | 6-8s | 12s |
| Scene 3: 构造大正方形 | 8-10s | 22s |
| Scene 4: 几何分割 | 10-12s | 34s |
| Scene 5: 区域着色 | 10-12s | 46s |
| Scene 6: 公式推导 | 8-10s | 56s |
| Scene 7: 例题结尾 | 8-10s | 66s |
| **总计** | **60-75s** | **66s** |

---

## 关键注意事项

### 1. 几何精度
- ✅ 所有顶点在 setup_geometry() 中统一计算
- ✅ 使用 NumPy 精确计算，禁止臆想坐标
- ✅ 边界检查：x ∈ [-4, 4], y ∈ [-7, 7]

### 2. 文字处理
- ✅ 中文使用 Text(font="Noto Sans CJK SC")
- ✅ 数学符号使用 MathTex(r"...")
- ✅ 分开处理中英文：VGroup(中文, 数学).arrange(RIGHT)

### 3. 颜色一致性
- 红色系: a相关项
- 绿色系: ab相关项  
- 蓝色系: b相关项
- 黄色: 强调高亮

### 4. 动画节奏
- 难点（Scene 5-6）：停留时间 1.5-2.0s
- 简单过渡：0.3-0.5s
- 公式书写：0.6-1.0s

### 5. 验证清单
- [ ] verify_geometry() 通过
- [ ] 无 LaTeX 编译错误
- [ ] 无元素溢出边界
- [ ] 所有中文正确显示
- [ ] 动画流畅无卡顿