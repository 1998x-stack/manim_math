# 三角比关系 - 动画分镜脚本

## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 中等
- 年级: 九年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
COLOR_SIN = "#2ecc71"          # 绿色 - sin
COLOR_COS = "#9b59b6"          # 紫色 - cos
COLOR_TAN = "#f39c12"          # 橙色 - tan
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 直角三角形顶点A | 直角顶点 | self.A |
| 直角三角形顶点B | 底边端点 | self.B |
| 直角三角形顶点C | 斜边端点 | self.C |
| 角A的度数 | ∠BAC | self.angle_A |
| 对边长度 | BC (opposite) | self.a |
| 邻边长度 | AB (adjacent) | self.b |
| 斜边长度 | AC (hypotenuse) | self.c |
| sin A | a/c | self.sin_A |
| cos A | b/c | self.cos_A |
| tan A | a/b | self.tan_A |

---

## Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出问题

### 元素
1. 作者标识 (顶部小字, y=+7)
2. 钩子问题 (大字, y=+5)
3. 三个公式快闪 (y=+3到+1)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` - "同一个角的三角比有什么关系?" |
| 1.1s | 三个公式快闪 | `Flash` 依次闪现三个公式 |
| 2.5s | 公式消失 | `FadeOut(formulas)` |
| 3.0s | 等待 | `Wait(0.5)` |

### 几何计算
无 (纯文字场景)

### 清理
- FadeOut: hook_text, formulas
- 保留: author_info

---

## Scene 2: 建立直角三角形 (5-6秒)
**目的**: 构建基础几何图形，标注元素

### 元素
1. 直角三角形ABC (y ∈ [-1, +3])
2. 直角标记 (∠A)
3. 顶点标签 (A, B, C)
4. 边长标签 (a, b, c)
5. 角度标记 (∠A)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 绘制三角形 | `Create(triangle)` |
| 0.8s | 标记直角 | `Create(right_angle_mark)` |
| 1.3s | 标注顶点 | `Write(labels_A, B, C)` |
| 2.0s | 标注边长 | `Write(side_labels)` |
| 2.8s | 标记角A | `Create(angle_arc)` |
| 3.5s | 等待 | `Wait(1.0)` |

### 几何计算 (在setup_geometry中)
```python
# 直角在A点
self.A = np.array([0, 0, 0]) * self.SCALE + self.OFFSET
self.B = np.array([3, 0, 0]) * self.SCALE + self.OFFSET  # 水平向右
self.C = np.array([0, 2, 0]) * self.SCALE + self.OFFSET  # 垂直向上

# 边长
self.a = np.linalg.norm(self.C - self.B)  # BC (对边)
self.b = np.linalg.norm(self.B - self.A)  # AB (邻边)
self.c = np.linalg.norm(self.C - self.A)  # AC (斜边)

# 角度
self.angle_A = np.arctan2(self.C[1] - self.A[1], self.C[0] - self.A[0])

# 三角比
self.sin_A = self.a / self.c
self.cos_A = self.b / self.c
self.tan_A = self.a / self.b
```

### 验证
- 直角验证: `dot(AB, AC) ≈ 0`
- 勾股定理: `a² + b² ≈ c²`

### 清理
- 保留: triangle, labels, right_angle_mark, angle_arc

---

## Scene 3: 关系1 - sin²A + cos²A = 1 (10-12秒)
**目的**: 展示勾股定理推导平方和关系

### 元素
1. 勾股定理公式 (y=+5)
2. 除以c²的过程 (y=+4到+2)
3. 高亮sin²A和cos²A (三角形上标注)
4. 最终关系式 (y=0)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write("关系一: 平方和关系")` |
| 0.6s | 写勾股定理 | `Write(pythagorean)` - a² + b² = c² |
| 1.5s | 高亮三角形边 | `Indicate(side_a, side_b, side_c)` |
| 2.5s | 除以c² | `TransformMatchingTex` - 两边同除c² |
| 3.5s | 展开 | `TransformMatchingTex` - (a/c)² + (b/c)² = 1 |
| 4.5s | 替换为sin和cos | `TransformMatchingTex` - sin²A + cos²A = 1 |
| 5.5s | 矩形框高亮 | `SurroundingRectangle` 包围最终公式 |
| 6.5s | 等待理解 | `Wait(2.0)` |

### 几何计算
```python
# 验证: sin²A + cos²A = 1
verification = self.sin_A**2 + self.cos_A**2
assert abs(verification - 1.0) < 1e-6, "sin²+cos²≠1"
```

### 清理
- FadeOut: title, pythagorean, intermediate_steps, rectangle
- 保留: triangle, labels

---

## Scene 4: 关系2 - tanA = sinA/cosA (8-10秒)
**目的**: 从定义直接推导tan关系

### 元素
1. sin和cos定义展示
2. tan定义展示
3. 代数化简过程
4. 最终关系式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write("关系二: 商的关系")` |
| 0.6s | 写sin定义 | `Write(sin_def)` - sinA = a/c |
| 1.2s | 写cos定义 | `Write(cos_def)` - cosA = b/c |
| 1.8s | 写tan定义 | `Write(tan_def)` - tanA = a/b |
| 2.5s | 标注分子分母 | `Brace` 标注 a/c ÷ b/c |
| 3.5s | 化简 | `TransformMatchingTex` - = (a/c)/(b/c) = a/b |
| 4.5s | 得出结论 | `TransformMatchingTex` - tanA = sinA/cosA |
| 5.5s | 矩形框高亮 | `SurroundingRectangle` |
| 6.5s | 等待 | `Wait(1.5)` |

### 几何计算
```python
# 验证: tanA = sinA/cosA
verification = self.sin_A / self.cos_A
assert abs(verification - self.tan_A) < 1e-6, "tan≠sin/cos"
```

### 清理
- FadeOut: title, definitions, steps, rectangle
- 保留: triangle, labels

---

## Scene 5: 关系3 - 互余关系 (10-12秒)
**目的**: 展示互余角的三角比关系

### 元素
1. 90°-A的角标记 (在顶点C)
2. 互余关系说明
3. 三组等式
4. 几何直观解释

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write("关系三: 互余角关系")` |
| 0.6s | 标记角C | `Create(angle_C_arc)` |
| 1.2s | 标注90°-A | `Write(angle_C_label)` - ∠C = 90° - A |
| 2.0s | 互余说明 | `Write("互余: ∠A + ∠C = 90°")` |
| 3.0s | 写第一组 | `Write(eq1)` - sinA = cosC = cos(90°-A) |
| 4.0s | 高亮对应边 | `Indicate(opposite_for_A, adjacent_for_C)` |
| 5.0s | 写第二组 | `Write(eq2)` - cosA = sinC = sin(90°-A) |
| 6.0s | 写第三组 | `Write(eq3)` - tanA·tanC = 1 |
| 7.0s | 框选三组 | `SurroundingRectangle` |
| 8.0s | 等待 | `Wait(2.0)` |

### 几何计算
```python
# 角C的三角比
self.angle_C = np.pi/2 - self.angle_A
self.sin_C = self.b / self.c  # 对于C，邻边变成对边
self.cos_C = self.a / self.c  # 对于C，对边变成邻边
self.tan_C = self.b / self.a

# 验证互余关系
assert abs(self.sin_A - self.cos_C) < 1e-6, "sinA≠cosC"
assert abs(self.cos_A - self.sin_C) < 1e-6, "cosA≠sinC"
assert abs(self.tan_A * self.tan_C - 1.0) < 1e-6, "tanA·tanC≠1"
```

### 清理
- FadeOut: title, angle_C_arc, angle_C_label, equations, rectangle
- 保留: triangle, original_labels

---

## Scene 6: 总结回顾 (8-10秒)
**目的**: 汇总三个关系，强化记忆

### 元素
1. 三个关系并列展示
2. 每个关系的关键词
3. 几何图形缩小到角落

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 三角形移到右上角 | `triangle.animate.scale(0.4).to_corner(UR)` |
| 0.8s | 标题出现 | `Write("三角比的三大关系")` |
| 1.5s | 关系1卡片滑入 | `FadeIn(card1, shift=RIGHT)` |
| 2.5s | 关系2卡片滑入 | `FadeIn(card2, shift=RIGHT)` |
| 3.5s | 关系3卡片滑入 | `FadeIn(card3, shift=RIGHT)` |
| 4.5s | 三卡片高亮 | `Flash` 依次闪烁 |
| 6.0s | 强调文字 | `Write("记住这三个, 解题无忧!")` |
| 7.0s | 等待 | `Wait(1.5)` |

### 卡片内容
**卡片1**: sin²A + cos²A = 1 (平方和关系)
**卡片2**: tanA = sinA/cosA (商的关系)
**卡片3**: sinA = cos(90°-A) (互余关系)

### 清理
- FadeOut: title, cards, triangle

---

## Scene 7: 片尾关注 (5-6秒)
**目的**: 品牌曝光，引导关注

### 元素
1. 作者名放大
2. 账号ID
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, large_author)` |
| 0.6s | 账号ID淡入 | `FadeIn(account_id)` |
| 1.2s | 关注提示 | `FadeIn(follow_text)` - "关注我, 数学更简单!" |
| 2.0s | 装饰三角形 | `FadeIn(triangles)` 围绕旋转 |
| 3.0s | 公式图标闪烁 | `Flash(formula_icons)` |
| 4.0s | 等待 | `Wait(1.0)` |
| 5.0s | 全部淡出 | `FadeOut(VGroup(*))` |

### 清理
- FadeOut: 所有元素

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 全程保留顶部 |
| triangle | Scene 2 | Scene 6 | 主要几何图形 |
| labels (A,B,C) | Scene 2 | Scene 6 | 顶点标签 |
| right_angle_mark | Scene 2 | Scene 6 | 直角符号 |
| angle_A_arc | Scene 2 | Scene 6 | 角A标记 |
| side_labels (a,b,c) | Scene 2 | Scene 3 | 边长标签 |
| relation_1_formula | Scene 3 | Scene 3 | 临时公式 |
| relation_2_formula | Scene 4 | Scene 4 | 临时公式 |
| angle_C_arc | Scene 5 | Scene 5 | 临时角标记 |
| summary_cards | Scene 6 | Scene 6 | 总结卡片 |

---

## 全局配置补充

### 字体大小
```python
FONT_SIZES = {
    "title": 36,          # 场景标题
    "subtitle": 28,       # 副标题
    "formula": 32,        # 数学公式
    "label": 24,          # 几何标签
    "body": 22,           # 正文说明
    "small": 18,          # 小字注释
    "author": 20,         # 作者信息
}
```

### 坐标区域规划
```
y = +8  ┌─────────────────────────────┐
y = +7  │  作者信息 (全程保留)          │
y = +6  ├─────────────────────────────┤
y = +5  │  场景标题区                  │
y = +4  ├─────────────────────────────┤
        │                             │
y = +3  │  几何图形主区域               │
y = +2  │  (直角三角形)                │
y = +1  │                             │
y = 0   │                             │
y = -1  │                             │
        ├─────────────────────────────┤
y = -2  │  公式推导区                  │
y = -3  │  (步骤展示)                  │
y = -4  │                             │
        ├─────────────────────────────┤
y = -5  │  说明文字区                  │
y = -6  │  (提示、注释)                │
        ├─────────────────────────────┤
y = -7  │  底部安全区                  │
y = -8  └─────────────────────────────┘

x ∈ [-4, +4] (主内容区)
```

---

## 时间节奏检查

| 场景 | 预计时长 | 累计时长 | 备注 |
|-----|---------|---------|------|
| Scene 1 | 3.5s | 3.5s | 快速开场 |
| Scene 2 | 5.0s | 8.5s | 建立基础 |
| Scene 3 | 11s | 19.5s | 重点1, 多停留 |
| Scene 4 | 9s | 28.5s | 重点2 |
| Scene 5 | 11s | 39.5s | 重点3, 多停留 |
| Scene 6 | 9s | 48.5s | 总结强化 |
| Scene 7 | 5.5s | 54s | 片尾 |

**总时长**: 约54秒 (符合TikTok 45-90秒建议)

---

## 验证清单

### 几何验证
- [ ] 直角验证: AB ⊥ AC
- [ ] 勾股定理: a² + b² = c²
- [ ] sin²A + cos²A = 1
- [ ] tanA = sinA/cosA
- [ ] sinA = cos(90°-A)
- [ ] cosA = sin(90°-A)
- [ ] tanA·tan(90°-A) = 1

### 坐标边界
- [ ] 三角形顶点在 x∈[-4,4], y∈[-2,4]
- [ ] 所有文字在 x∈[-4,4], y∈[-7,7]
- [ ] 无元素溢出屏幕

### 动画节奏
- [ ] 重点公式停留2秒以上
- [ ] 过渡动画0.5-1秒
- [ ] 无连续高密度动画
- [ ] 总时长45-75秒

---

## 特殊注意事项

1. **LaTeX约束**:
   - 度数符号使用 `^\circ` 而非 `°`
   - 分数使用 `\frac{a}{b}` 而非 `\over`
   - 中文使用 `Text()` 而非 `MathTex()`

2. **角度方向**:
   - 使用叉积判断角度方向
   - 使用 `Angle.from_three_points` 简化创建

3. **颜色一致性**:
   - sin始终用绿色
   - cos始终用紫色
   - tan始终用橙色
   - 保持视觉统一

4. **字体**:
   - 中文: "Noto Sans CJK SC"
   - 数学: MathTex默认
   - 确保可读性