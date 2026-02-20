# 平面向量基本定理 - 动画分镜脚本

## 元信息
- 目标时长: 55 秒
- 场景数量: 6 个
- 难度等级: 高二第一学期

## 颜色配置
```python
BG_COLOR = "#1a1a2e"
C_E1 = "#e74c3c"    # 红色 - 基底向量 e1
C_E2 = "#3498db"    # 蓝色 - 基底向量 e2
C_A  = "#2ecc71"    # 绿色 - 任意向量 a
C_HL = YELLOW       # 黄色 - 高亮/公式
C_AUX = GRAY_B      # 灰色 - 辅助元素
```

## 几何预计算清单

| 元素 | 计算公式 | 坐标值 |
|------|---------|--------|
| 原点 O | 手动定义 | (-0.8, 0.0) |
| e1 向量 | 手动定义 | (2.8, 0.5) |
| e2 向量 | 手动定义 | (0.3, 2.3) |
| λ1, λ2 | 手动设定 | 1.0, 1.0 |
| a 向量 | λ1·e1 + λ2·e2 | (3.1, 2.8) |
| E1 顶点 | O + e1 | (2.0, 0.5) |
| E2 顶点 | O + e2 | (-0.5, 2.3) |
| A 顶点 | O + a | (2.3, 2.8) |
| 平行四边形 | O, E1, A, E2 | 验证: E1+e2=A ✓ |

---

## Scene 1: 开场钩子 (0-5s)
**目的**: 引出"任意向量都能被唯一表示"这一核心命题

### 元素
- 作者标识 (顶部小字, 固定)
- 钩子问题文字 (三行)
- 神秘向量 Arrow + 问号

### 动画序列
| 时间 | 动作 | 代码 |
|------|------|------|
| 0.0s | 作者信息淡入 | FadeIn(author, shift=DOWN*0.2) |
| 0.3s | 三行钩子文字淡入 | FadeIn(lines, shift=DOWN*0.3) |
| 1.0s | 神秘向量创建 | Create(mystery_arrow) |
| 1.8s | 问号闪入 | FadeIn(qmark, scale=0.5) |
| 2.6s | 等待 | wait(0.8) |
| 3.4s | 清理 | FadeOut(lines, mystery, qmark) |

### 清理
- FadeOut: lines, mystery_arrow, qmark
- 保留: author_mob (全程)

---

## Scene 2: 什么是基底 (5-14s)
**目的**: 用两个具体向量展示"不共线"概念和"基底"定义

### 几何关键点
- e1 从 O=(-0.8, 0) 出发，方向接近水平 (2.8, 0.5)
- e2 从 O=(-0.8, 0) 出发，方向接近竖直 (0.3, 2.3)
- 叉积 = 2.8×2.3 - 0.5×0.3 = 6.44 - 0.15 = 6.29 ≠ 0 → 不共线 ✓

### 动画序列
| 时间 | 动作 |
|------|------|
| 5.0s | Write(title) |
| 5.6s | FadeIn(O_dot, O_label) |
| 5.9s | Create(e1_arrow), Write(e1_label) |
| 7.0s | Create(e2_arrow), Write(e2_label) |
| 8.1s | FadeIn(explain_nc, explain_basis) |
| 9.5s | wait(1.2) |
| 10.7s | FadeOut(title, explanations) |

### 保留到 Scene 3
- e1_arrow, e2_arrow, e1_label, e2_label, O_dot, O_label

---

## Scene 3: 向量分解定理 (14-27s)
**目的**: 核心！展示 a = λ1·e1 + λ2·e2 的构造过程

### 几何关键点
- 平行四边形: O(-0.8,0) → E1(2.0,0.5) → A(2.3,2.8) → E2(-0.5,2.3)
- 从 E1 到 A 的虚线 = λ2·e2 方向（平行于 e2）
- 从 E2 到 A 的虚线 = λ1·e1 方向（平行于 e1）
- comp1_arrow: O → E1（沿 e1 方向）
- comp2_arrow: E1 → A（沿 e2 方向）

### 动画序列
| 时间 | 动作 |
|------|------|
| 14s | Write(title) |
| 14.6s | Create(a_arrow), Write(a_label) |
| 15.5s | FadeIn(hint_text) |
| 15.9s | Create(dash_lines) |
| 16.7s | Create(comp1_arrow), Write(comp1_label) |
| 17.7s | Create(comp2_arrow), Write(comp2_label) |
| 18.5s | Write(formula) - 核心公式 |
| 19.3s | FadeIn(unique_text) |
| 20.8s | wait(1.5) - 关键停留 |
| 22.3s | FadeOut(all) |

### 清理所有Scene 2保留物
- FadeOut: e1_arrow, e2_arrow, e1_label, e2_label, O_dot, O_label

---

## Scene 4: 标准基底 (27-40s)
**目的**: 展示直角坐标系中的 i, j 单位向量和坐标表示

### 元素
- Axes(x_range=[-0.5,4], y_range=[-0.5,4], x_length=5, y_length=5) 居中
- i=(1,0) 红色箭头, j=(0,1) 蓝色箭头
- 任意向量 a=(2.5, 2.0) 绿色箭头
- 坐标分量虚线 (竖线 + 横线)
- 公式: a = x·i + y·j ↔ a = (x, y)

### 动画序列
| 时间 | 动作 |
|------|------|
| 27s | Write(title), Create(axes) |
| 28s | Create(i_arrow), Write(i_label) |
| 28.6s | Create(j_arrow), Write(j_label) |
| 29.5s | Create(a_arrow), Write(a_label) |
| 30.2s | Create(dashed_components), Write(coord_labels) |
| 31.2s | Write(formula) |
| 32.0s | Write(coord_form) |
| 33.5s | wait(1.5) |
| 35s | FadeOut(all) |

---

## Scene 5: 知识总结 (40-51s)
**目的**: 用卡片式布局汇总三个核心知识点

### 布局
- 顶部: 定理框 (RoundedRectangle) + 公式
- 中部: ①②③ 三个要点
- 底部: 标准基底专栏

### 动画序列
| 时间 | 动作 |
|------|------|
| 40s | Write(title) |
| 40.5s | FadeIn(box), Write(theorem_title, formula) |
| 41.5s | 逐条 FadeIn 三个要点 |
| 43s | Create(separator) |
| 43.3s | FadeIn 标准基底内容 |
| 45.5s | wait(1.5) |
| 47s | FadeOut(all) |

---

## Scene 6: 片尾 (51-55s)
**目的**: 作者信息放大 + 关注提示

### 元素
- Transform author_mob → big_name
- FadeIn @emptyandcalm
- FadeIn 关注文字
- 装饰性小向量分解图

---

## 元素生命周期追踪表

| 元素 | 创建 | 销毁 | 说明 |
|------|------|------|------|
| author_mob | Scene1开始 | Scene6 Transform | 全程保留 |
| O_dot/label | Scene2 | Scene3结束 | 跨场景 |
| e1_arrow/label | Scene2 | Scene3结束 | 跨场景 |
| e2_arrow/label | Scene2 | Scene3结束 | 跨场景 |
| a_arrow | Scene3 | Scene3结束 | 单场景 |
| parallelogram dashes | Scene3 | Scene3结束 | 单场景 |
| axes | Scene4 | Scene4结束 | 单场景 |
| theorem_box | Scene5 | Scene5结束 | 单场景 |