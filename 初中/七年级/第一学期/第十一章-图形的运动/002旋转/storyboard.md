# 图形的旋转 - 动画分镜脚本

<!-- /root/code/sss/media/videos/rotation_animation/1920p60/RotationAnimation.mp4 -->
## 元信息
- 目标时长: 60-75 秒
- 场景数量: 7 个
- 难度等级: 初中七年级
- 知识点: 旋转的定义、性质和应用

## 颜色配置
```python
COLOR_ORIGINAL = "#3498db"      # 蓝色 - 原图形
COLOR_ROTATED = "#e74c3c"       # 红色 - 旋转后图形
COLOR_CENTER = "#f39c12"        # 橙色 - 旋转中心
COLOR_ANGLE = "#2ecc71"         # 绿色 - 旋转角
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮强调
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_TRIANGLE = WHITE          # 白色 - 三角形边框
```

## 几何预计算清单

### 场景1-2: 开场和定义 (不需要复杂几何)
- 旋转中心 O: ORIGIN
- 简单点 A: 2*RIGHT + UP

### 场景3: 旋转性质演示
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 旋转中心 O | ORIGIN | self.O |
| 原点 A | [2, 1, 0] | self.A |
| 原点 B | [2, -0.5, 0] | self.B |
| 旋转后点 A' | A 绕 O 旋转 60° | self.A_prime |
| 旋转后点 B' | B 绕 O 旋转 60° | self.B_prime |
| 距离 OA | \|\|A - O\|\| | self.dist_OA |
| 距离 OA' | \|\|A' - O\|\| | self.dist_OA_prime |

### 场景4: 三角形旋转
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 旋转中心 O | [-1, -1, 0] | self.O_tri |
| 三角形顶点 A | [1, 1, 0] | self.tri_A |
| 三角形顶点 B | [2.5, 0.5, 0] | self.tri_B |
| 三角形顶点 C | [1.5, -0.8, 0] | self.tri_C |
| 旋转角度 | 90° (PI/2) | self.rotation_angle |
| A' | A 绕 O 旋转 90° | self.tri_A_prime |
| B' | B 绕 O 旋转 90° | self.tri_B_prime |
| C' | C 绕 O 旋转 90° | self.tri_C_prime |

### 旋转计算函数
```python
def rotate_point(point, center, angle):
    """
    将点 point 绕 center 旋转 angle 弧度
    angle > 0: 逆时针
    angle < 0: 顺时针
    """
    # 平移到原点
    translated = point - center
    
    # 旋转矩阵
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    
    # 2D 旋转
    x_new = translated[0] * cos_a - translated[1] * sin_a
    y_new = translated[0] * sin_a + translated[1] * cos_a
    
    # 平移回原位置
    rotated = np.array([x_new, y_new, 0]) + center
    
    return rotated
```

---

## 场景分镜

### Scene 1: 开场钩子 (3-4秒)
**目的**: 吸引注意力，引出旋转主题

#### 元素
1. 作者标识 (顶部)
2. 钩子问题: "如何让图形优雅地转动？"
3. 旋转的风车/齿轮动画示例

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` | author: 创建 |
| 0.3s | 钩子文字书写 | `Write(hook_text)` | hook_text: 创建 |
| 1.0s | 简单图形旋转演示 | `Rotate(shape, angle=2*PI)` | shape: 创建 |
| 3.0s | 等待 | `Wait(0.5)` | - |
| 3.5s | 清理钩子 | `FadeOut(hook_text, shape)` | hook_text, shape: 销毁 |

#### 清理
- FadeOut: hook_text, shape
- 保留: author

---

### Scene 2: 旋转定义 (5-6秒)
**目的**: 明确旋转的三要素

#### 元素
1. 标题: "旋转的定义"
2. 旋转中心 O (橙色点)
3. 原图形点 A (蓝色)
4. 旋转方向箭头
5. 旋转角度标注
6. 定义文字

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题淡入 | `Write(title)` | title: 创建 |
| 0.5s | 旋转中心出现 | `FadeIn(O_dot, scale=0.5)` | O_dot: 创建 |
| 1.0s | 原点 A 出现 | `FadeIn(A_dot)` | A_dot: 创建 |
| 1.5s | 定义文字逐条出现 | `FadeIn(def_text_1)` | def_text_1/2/3: 创建 |
| 2.0s | 旋转方向箭头 | `Create(arc_arrow)` | arc_arrow: 创建 |
| 2.5s | 角度标注 | `Write(angle_label)` | angle_label: 创建 |
| 3.5s | A 旋转到 A' | `MoveAlongPath(A_dot, arc_path)` | A_prime_dot: 创建 |
| 5.0s | 等待理解 | `Wait(1.0)` | - |
| 6.0s | 清理 | `FadeOut(title, def_text)` | title, def_text: 销毁 |

#### 保留元素
- O_dot, A_dot, A_prime_dot (变小透明)
- arc_arrow, angle_label (准备下一场景)

---

### Scene 3: 性质1 - 距离不变 (8-10秒)
**目的**: 演示 OA = OA'

#### 元素
1. 标题: "性质1: 距离相等"
2. 原点 A, B (蓝色)
3. 旋转后点 A', B' (红色)
4. 距离线段 OA, OA' (虚线)
5. 距离标注

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题淡入 | `Write(title)` | title: 创建 |
| 0.5s | 添加点 B | `FadeIn(B_dot)` | B_dot: 创建 |
| 1.0s | 旋转 A, B 到 A', B' | `Rotate(VGroup(A, B))` | A_prime, B_prime: 创建 |
| 2.5s | 绘制距离线 OA | `Create(line_OA)` | line_OA: 创建 |
| 3.0s | 绘制距离线 OA' | `Create(line_OA_prime)` | line_OA_prime: 创建 |
| 3.5s | 距离标注 | `Write(dist_label_OA)` | dist_labels: 创建 |
| 4.5s | 高亮相等 | `Flash(line_OA), Flash(line_OA_prime)` | - |
| 5.5s | 公式出现 | `Write(formula)` | formula: 创建 |
| 7.0s | 等待理解 | `Wait(2.0)` | - |
| 9.0s | 清理 | `FadeOut(title, lines, labels, formula)` | 部分元素: 销毁 |

#### 保留元素
- O_dot, A_dot, B_dot, A_prime_dot, B_prime_dot (变小)

---

### Scene 4: 性质2 - 旋转角相等 (8-10秒)
**目的**: 演示 ∠AOA' = ∠BOB' = 旋转角

#### 元素
1. 标题: "性质2: 旋转角相等"
2. 角 ∠AOA' (绿色扇形)
3. 角 ∠BOB' (绿色扇形)
4. 角度标注
5. 公式

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题淡入 | `Write(title)` | title: 创建 |
| 0.5s | 绘制角 ∠AOA' | `Create(angle_AOA)` | angle_AOA: 创建 |
| 1.5s | 角度标注 60° | `Write(angle_label_1)` | angle_label_1: 创建 |
| 2.5s | 绘制角 ∠BOB' | `Create(angle_BOB)` | angle_BOB: 创建 |
| 3.5s | 角度标注 60° | `Write(angle_label_2)` | angle_label_2: 创建 |
| 4.5s | 高亮两个角 | `Flash(angle_AOA), Flash(angle_BOB)` | - |
| 5.5s | 公式出现 | `Write(formula)` | formula: 创建 |
| 7.0s | 等待理解 | `Wait(2.0)` | - |
| 9.0s | 清理 | `FadeOut(all_elements)` | 所有: 销毁 |

---

### Scene 5: 性质3 - 形状大小不变 (8-10秒)
**目的**: 演示全等变换

#### 元素
1. 标题: "性质3: 形状大小不变"
2. 原三角形 ABC (蓝色)
3. 旋转后三角形 A'B'C' (红色)
4. 全等符号
5. 边长/角度标注

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题淡入 | `Write(title)` | title: 创建 |
| 0.5s | 创建原三角形 | `Create(triangle_ABC)` | triangle_ABC: 创建 |
| 1.5s | 标注边长 | `Write(side_labels)` | side_labels: 创建 |
| 2.5s | 旋转三角形 | `Rotate(triangle_ABC.copy(), 90°)` | triangle_prime: 创建 |
| 4.5s | 标注旋转后边长 | `Write(side_labels_prime)` | side_labels_prime: 创建 |
| 5.5s | 高亮对应边 | `Flash(对应边)` | - |
| 6.5s | 全等符号 | `Write(congruence_symbol)` | congruence: 创建 |
| 8.0s | 等待理解 | `Wait(1.5)` | - |
| 9.5s | 清理 | `FadeOut(all)` | 所有: 销毁 |

---

### Scene 6: 综合应用 (10-12秒)
**目的**: 综合展示所有性质

#### 元素
1. 标题: "旋转的性质总结"
2. 复杂图形 (五边形)
3. 旋转中心
4. 旋转动画
5. 性质标注卡片

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 标题淡入 | `Write(title)` | title: 创建 |
| 0.5s | 五边形出现 | `Create(pentagon)` | pentagon: 创建 |
| 1.5s | 旋转中心标记 | `FadeIn(center_dot)` | center_dot: 创建 |
| 2.0s | 旋转动画 (慢速) | `Rotate(pentagon, angle=PI/3, run_time=3)` | pentagon_rotated: 创建 |
| 5.5s | 性质卡片1滑入 | `card_1.animate.shift(RIGHT*5)` | card_1: 创建 |
| 6.5s | 性质卡片2滑入 | `card_2.animate.shift(RIGHT*5)` | card_2: 创建 |
| 7.5s | 性质卡片3滑入 | `card_3.animate.shift(RIGHT*5)` | card_3: 创建 |
| 9.0s | 等待理解 | `Wait(2.0)` | - |
| 11.0s | 清理 | `FadeOut(all)` | 所有: 销毁 |

---

### Scene 7: 片尾关注 (4-5秒)
**目的**: 引导关注

#### 元素
1. 作者信息放大
2. 关注提示
3. 旋转图标装饰

#### 动画序列
| 时间 | 动作 | 代码参考 | 元素生命周期 |
|------|------|---------|-------------|
| 0.0s | 作者信息放大 | `Transform(author, author_large)` | - |
| 0.8s | 关注提示 | `FadeIn(follow_text)` | follow_text: 创建 |
| 1.5s | 旋转图标环绕 | `Rotate(icons, angle=2*PI)` | icons: 创建 |
| 3.5s | 等待 | `Wait(1.0)` | - |
| 4.5s | 全部淡出 | `FadeOut(all)` | 所有: 销毁 |

---

## 元素生命周期追踪表

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author | Scene 1 | Scene 7 | 作者标识 |
| O_dot | Scene 2 | Scene 5 | 旋转中心 |
| A_dot | Scene 2 | Scene 5 | 原点 A |
| A_prime_dot | Scene 2 | Scene 5 | 旋转后点 A' |
| B_dot | Scene 3 | Scene 5 | 原点 B |
| B_prime_dot | Scene 3 | Scene 5 | 旋转后点 B' |
| triangle_ABC | Scene 5 | Scene 5 | 原三角形 |
| triangle_prime | Scene 5 | Scene 5 | 旋转后三角形 |
| pentagon | Scene 6 | Scene 6 | 综合应用图形 |

---

## 关键验证点

### 几何验证
1. ✓ 旋转后距离相等: `||A' - O|| == ||A - O||`
2. ✓ 旋转角度一致: `angle(A, O, A') == rotation_angle`
3. ✓ 形状全等: `side_lengths_equal(ABC, A'B'C')`

### 动画节奏
1. 开场钩子: 3-4秒 ✓
2. 定义讲解: 5-6秒 ✓
3. 性质演示: 每个 8-10秒 ✓
4. 综合应用: 10-12秒 ✓
5. 片尾: 4-5秒 ✓
6. **总时长: 60-75秒** ✓

### 教学重点
1. 旋转三要素明确标注 ✓
2. 性质逐个演示，有充分停留 ✓
3. 使用对比色区分原图和旋转后图形 ✓
4. 关键公式出现并保持足够时间 ✓