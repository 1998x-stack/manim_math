# 平面与平面的位置关系 - 动画分镜脚本

## 元信息
- 目标时长: 30-45 秒
- 场景数量: 5 个
- 难度等级: 简单
- 目标观众: 初中生

## 颜色配置
```python
PLANE_COLOR = BLUE
HIGHLIGHT_COLOR = YELLOW
TEXT_COLOR = WHITE
BACKGROUND_COLOR = "#1a1a2e"
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 平行平面1 | Rectangle | plane1 |
| 平行平面2 | Rectangle | plane2 |
| 相交平面1 | Rectangle, rotated | intersecting_plane1 |
| 相交平面2 | Rectangle, rotated | intersecting_plane2 |
| 相交线 | Line | intersection_line |

---

## Scene 1: 开场 (2-3秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 主标题 (平面与平面的位置关系)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |

### 清理
- 保留: title, author_info

---

## Scene 2: 平行平面 (4-6秒)
**目的**: 展示两平面平行关系

### 元素
1. 两个平行平面 (淡蓝色半透明矩形)
2. 平行关系标签 (α ∥ β)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建两个平行平面 | `Create(plane1), Create(plane2)` |
| 1.0s | 显示平行关系标签 | `Write(parallel_label)` |
| 3.0s | 等待观察 | `Wait(2.0)` |

### 清理
- 保留: none (will be faded out)

---

## Scene 3: 相交平面 (4-6秒)
**目的**: 展示两平面相交关系

### 元素
1. 两个相交平面 (不同颜色)
2. 相交线 (黄色粗线)
3. 相交关系标签 (α ∩ β = l)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景 | `FadeOut(...)` |
| 0.2s | 创建相交平面1 | `Create(intersecting_plane1)` |
| 0.8s | 创建相交平面2 | `Create(intersecting_plane2)` |
| 1.4s | 创建相交线并显示标签 | `Create(intersection_line), Write(intersect_label)` |
| 3.4s | 等待观察 | `Wait(2.0)` |

### 清理
- 保留: none (will be faded out)

---

## Scene 4: 垂直平面 (4-6秒)
**目的**: 展示两平面垂直关系

### 元素
1. 两个垂直平面 (不同颜色)
2. 垂直关系标签 (α ⊥ β)

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景 | `FadeOut(...)` |
| 0.2s | 创建垂直平面1 | `Create(vertical_plane1)` |
| 0.8s | 创建垂直平面2 | `Create(vertical_plane2)` |
| 1.4s | 显示垂直关系标签 | `Write(perpendicular_label)` |
| 3.4s | 等待观察 | `Wait(2.0)` |

### 清理
- 保留: none (will be faded out)

---

## Scene 5: 总结 (4-5秒)
**目的**: 总结三种位置关系

### 元素
1. 结论文本 (三种关系总结)
2. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 清除前一场景 | `FadeOut(...)` |
| 0.2s | 显示结论 | `Write(conclusion)` |
| 2.0s | 显示作者信息 | `FadeIn(author_info)` |
| 3.0s | 结束等待 | `Wait(1.0)` |

### 清理
- 保留: conclusion, author_info

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| title | Scene 1 | Scene 4 | 主标题 |
| plane1,plane2 | Scene 2 | Scene 2 end | 平行平面 |
| intersecting_plane1,2 | Scene 3 | Scene 3 end | 相交平面 |
| intersection_line | Scene 3 | Scene 3 end | 相交线 |
| vertical_plane1,2 | Scene 4 | Scene 4 end | 垂直平面 |
| conclusion | Scene 5 | End | 结论文本 |
| author_info | Scene 1 | End | 作者信息 |

---

## 数学公式
- 平面平行：α ∥ β
- 平面相交：α ∩ β = l
- 平面垂直：α ⊥ β

## 相关知识点
- 线面关系
- 线线关系
- 二面角
