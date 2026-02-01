# 解直角三角形 - 动画分镜脚本

## 元信息
- 目标时长: 70-80 秒
- 场景数量: 6 个
- 难度等级: 中等
- 年级: 九年级

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
COLOR_BACKGROUND = "#1a1a2e"   # 深蓝背景
COLOR_KNOWN = "#2ecc71"        # 绿色 - 已知量
COLOR_UNKNOWN = "#f39c12"      # 橙色 - 未知量
COLOR_SOLVING = "#9b59b6"      # 紫色 - 求解过程
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 直角顶点C | 直角位置 | self.C |
| 顶点A | 左下角 | self.A |
| 顶点B | 右上角 | self.B |
| 对边a | BC长度 | self.a |
| 邻边b | AC长度 | self.b |
| 斜边c | AB长度 | self.c |
| 角A | ∠BAC | self.angle_A |
| 角B | ∠ABC | self.angle_B |
| sin A, cos A, tan A | 三角比 | self.sin_A, self.cos_A, self.tan_A |

---

## Scene 1: 开场钩子 (4-5秒)
**目的**: 吸引注意力，提出问题

### 元素
1. 作者标识 (顶部, y=+7)
2. 钩子问题 (y=+5.5)
3. 直角三角形快速显示 (y=+2)
4. 问号标记未知元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author_info)` |
| 0.3s | 钩子文字 | `Write("已知两个条件，如何求其他?")` |
| 1.0s | 三角形创建 | `Create(triangle)` |
| 1.8s | 问号闪烁 | `Flash` 在未知元素上 |
| 2.5s | 等待 | `Wait(1.0)` |

### 几何计算
```python
# 使用3-4-5直角三角形
self.C = np.array([0, 0, 0]) * SCALE + OFFSET  # 直角
self.A = np.array([-4, 0, 0]) * SCALE + OFFSET  # 左
self.B = np.array([0, 3, 0]) * SCALE + OFFSET   # 上
```

### 清理
- FadeOut: hook_text, question_marks
- 保留: triangle, author_info

---

## Scene 2: 解题三大工具 (8-10秒)
**目的**: 介绍三个核心关系

### 元素
1. 标题 "三大工具" (y=+5.5)
2. 三个工具卡片 (y=+3到-1)
   - 勾股定理
   - 两锐角互余
   - 三角比定义
3. 三角形保持显示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 工具1滑入 | `FadeIn(card1, shift=LEFT)` - 勾股定理 |
| 1.5s | 工具2滑入 | `FadeIn(card2, shift=LEFT)` - 互余 |
| 2.4s | 工具3滑入 | `FadeIn(card3, shift=LEFT)` - 三角比 |
| 3.3s | 三卡片闪烁 | `Flash` 依次 |
| 4.5s | 等待理解 | `Wait(2.0)` |

### 卡片内容
**卡片1**: a² + b² = c² (勾股定理)
**卡片2**: ∠A + ∠B = 90° (两锐角互余)
**卡片3**: sin A = a/c, cos A = b/c, tan A = a/b

### 清理
- FadeOut: title, cards
- 保留: triangle

---

## Scene 3: 情况一 - 已知两边求第三边和角 (12-14秒)
**目的**: 展示已知两直角边，求斜边和角

### 元素
1. 标题 "情况一: 已知两直角边" (y=+5.5)
2. 三角形标注已知量 (绿色)
3. 步骤展示区 (y=-2到-5)
4. 求解过程动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 标记已知 | `Indicate(side_a, side_b)` 变绿色 |
| 1.2s | 已知条件 | `Write("已知: a=3, b=4")` |
| 2.0s | 求c步骤1 | `Write("c² = a² + b²")` |
| 3.0s | 求c步骤2 | `TransformMatchingTex` - c² = 9 + 16 = 25 |
| 4.0s | 求c步骤3 | `TransformMatchingTex` - c = 5 |
| 5.0s | 高亮结果 | `Indicate(side_c)` 变橙色标注c=5 |
| 6.0s | 求角A | `Write("tan A = a/b = 3/4")` |
| 7.5s | 角度结果 | `Write("∠A ≈ 36.87°")` |
| 8.5s | 求角B | `Write("∠B = 90° - ∠A ≈ 53.13°")` |
| 10.0s | 等待 | `Wait(1.5)` |

### 几何计算
```python
# 验证勾股定理
assert abs(self.a**2 + self.b**2 - self.c**2) < 1e-6
# 验证角度和
assert abs(self.angle_A + self.angle_B - np.pi/2) < 1e-6
```

### 清理
- FadeOut: title, steps, labels
- 保留: triangle (重置颜色)

---

## Scene 4: 情况二 - 已知一边一角求其他 (12-14秒)
**目的**: 展示已知斜边和一角，求其他元素

### 元素
1. 标题 "情况二: 已知斜边和一角" (y=+5.5)
2. 三角形标注已知 (c=5, ∠A=36.87°)
3. 步骤展示
4. 动态求解动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.6s | 标记已知 | 斜边c和角A变绿色 |
| 1.2s | 已知条件 | `Write("已知: c=5, ∠A≈36.87°")` |
| 2.0s | 求角B | `Write("∠B = 90° - ∠A")` |
| 3.0s | 角B结果 | `Write("∠B ≈ 53.13°")` |
| 4.0s | 求a步骤 | `Write("sin A = a/c")` |
| 5.0s | 求a计算 | `TransformMatchingTex` - a = c·sin A |
| 6.0s | a结果 | `Write("a = 5 × 0.6 = 3")` |
| 7.0s | 高亮a | `Indicate(side_a)` |
| 8.0s | 求b步骤 | `Write("cos A = b/c")` |
| 9.0s | b结果 | `Write("b = 5 × 0.8 = 4")` |
| 10.0s | 高亮b | `Indicate(side_b)` |
| 11.0s | 等待 | `Wait(1.5)` |

### 清理
- FadeOut: title, steps, labels
- 保留: triangle (重置)

---

## Scene 5: 解题流程图 (10-12秒)
**目的**: 总结系统的解题方法

### 元素
1. 标题 "解题流程" (y=+6)
2. 流程图 (y=+3到-3)
   - 判断已知条件
   - 选择合适工具
   - 求解步骤
   - 验证答案
3. 三角形缩小到角落

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 三角形缩小 | `triangle.animate.scale(0.4).to_corner(UR)` |
| 0.8s | 标题出现 | `Write(title)` |
| 1.5s | 步骤1 | `FadeIn(step1)` - "识别已知量" |
| 2.5s | 步骤2 | `FadeIn(step2)` - "选择合适关系" |
| 3.5s | 步骤3 | `FadeIn(step3)` - "列方程求解" |
| 4.5s | 步骤4 | `FadeIn(step4)` - "验证结果" |
| 5.5s | 箭头连接 | `Create(arrows)` |
| 7.0s | 强调 | `Flash` 整个流程 |
| 8.5s | 等待 | `Wait(2.0)` |

### 清理
- FadeOut: title, flowchart, triangle

---

## Scene 6: 片尾关注 (6-7秒)
**目的**: 品牌曝光，引导关注

### 元素
1. 作者名放大
2. 账号ID
3. 关注提示
4. 装饰元素（直角三角形图标）

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者名放大 | `Transform(author_info, large_author)` |
| 0.6s | 账号ID | `FadeIn(account_id)` |
| 1.2s | 关注提示 | `FadeIn("关注我，解题更轻松!")` |
| 2.0s | 三角形装饰 | `FadeIn(triangles)` 围绕旋转 |
| 3.5s | 工具图标 | `Flash` 三大工具图标 |
| 5.0s | 等待 | `Wait(1.0)` |
| 6.0s | 淡出 | `FadeOut(all)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 6 | 全程顶部 |
| triangle | Scene 1 | Scene 5 | 主三角形 |
| vertex_labels | Scene 1 | Scene 5 | A,B,C标签 |
| tool_cards | Scene 2 | Scene 2 | 临时卡片 |
| case1_steps | Scene 3 | Scene 3 | 临时步骤 |
| case2_steps | Scene 4 | Scene 4 | 临时步骤 |
| flowchart | Scene 5 | Scene 5 | 流程图 |

---

## 全局配置补充

### 字体大小
```python
FONT_SIZES = {
    "title": 36,          # 场景标题
    "subtitle": 28,       # 副标题
    "formula": 30,        # 数学公式
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
        ├─────────────────────────────┤
y = +3  │  三角形主区域                │
y = +2  │  (或工具卡片区)              │
y = +1  │                             │
y = 0   │                             │
y = -1  │                             │
        ├─────────────────────────────┤
y = -2  │  步骤展示区                  │
y = -3  │  (公式推导)                  │
y = -4  │                             │
y = -5  │                             │
        ├─────────────────────────────┤
y = -6  │  说明文字区                  │
        ├─────────────────────────────┤
y = -7  │  底部安全区                  │
y = -8  └─────────────────────────────┘

x ∈ [-4, +4] (主内容区)
```

---

## 时间节奏检查

| 场景 | 预计时长 | 累计时长 | 备注 |
|-----|---------|---------|------|
| Scene 1 | 4s | 4s | 快速开场 |
| Scene 2 | 9s | 13s | 介绍工具 |
| Scene 3 | 13s | 26s | 情况一，重点 |
| Scene 4 | 13s | 39s | 情况二，重点 |
| Scene 5 | 11s | 50s | 总结流程 |
| Scene 6 | 6.5s | 56.5s | 片尾 |

**总时长**: 约57秒 (符合TikTok 45-90秒建议)

---

## 验证清单

### 几何验证
- [ ] 直角验证: CA ⊥ CB
- [ ] 勾股定理: a² + b² = c²
- [ ] 角度和: ∠A + ∠B = 90°
- [ ] 三角比: sin A = a/c, cos A = b/c, tan A = a/b
- [ ] sin²A + cos²A = 1

### 坐标边界
- [ ] 三角形在 x∈[-4,4], y∈[-2,4]
- [ ] 文字在 x∈[-4,4], y∈[-7,7]
- [ ] 无元素溢出

### 动画节奏
- [ ] 重点步骤停留2秒以上
- [ ] 过渡动画0.5-1秒
- [ ] 总时长45-75秒

---

## 特殊注意事项

1. **精确计算**: 使用3-4-5直角三角形确保数值简单
2. **颜色编码**: 已知量绿色，未知量橙色，保持一致
3. **步骤清晰**: 每个求解步骤独立显示，不要堆叠
4. **验证强调**: 在求解后验证答案的正确性