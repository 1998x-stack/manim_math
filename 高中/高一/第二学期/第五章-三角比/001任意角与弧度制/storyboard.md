# 任意角与弧度制 - 动画分镜脚本

## 概述
任意角：将角的概念从锐角推广到任意大小的正角、负角和零角。正角为逆时针旋转，负角为顺时针旋转。弧度制：以弧长等于半径的弧所对的圆心角为1弧度。弧度与角度的换算：π rad=180°，1 rad≈57.3°，1°=π/180 rad。弧长公式：l=|α|r；扇形面积：S=½lr=½|α|r²。弧度制使三角函数的导数公式更加简洁。

## 目标时长
约60-90秒

## 场景数量
8个主要场景

## 颜色配置
```python
COLOR_MAIN = BLUE          # 主要颜色
COLOR_HIGHLIGHT = YELLOW   # 高亮颜色
COLOR_AUXILIARY = GRAY_B   # 辅助颜色
COLOR_FORMULA = WHITE      # 公式颜色
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 单位圆 | 半径为R | self.RADIUS |
| 起始点 | R*(cos(0), sin(0), 0) | self.START_POINT |
| 终点 | R*(cos(α), sin(α), 0) | self.END_POINT |
| 中点 | R*(cos(α/2), sin(α/2), 0) | self.MID_POINT |

---

## Scene 1: 开场介绍 (2-3秒)
**目的**: 钩子 + 引出主题

### 元素
1. 作者标识 (顶部小字)
2. 标题 "任意角与弧度制"
3. 副标题 "三角比的基础概念"

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.1s | 副标题淡入 | `FadeIn(subtitle)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: title, subtitle

---

## Scene 2: 任意角的概念 (8-10秒)
**目的**: 介绍任意角的定义和方向

### 元素
1. 坐标轴 (x轴、y轴)
2. 单位圆
3. 起始边 (x轴正方向)
4. 终边 (旋转后的射线)
5. 角度弧线
6. 角度标注
7. 定义文字
8. 方向说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 绘制坐标轴 | `Create(x_axis, y_axis)` |
| 1.3s | 绘制单位圆 | `Create(circle)` |
| 1.8s | 绘制起始边 | `Create(initial_line)` |
| 2.3s | 绘制终边 | `Create(terminal_line)` |
| 3.1s | 绘制角度弧 | `Create(angle_arc)` |
| 3.9s | 角度标注 | `Write(angle_label)` |
| 4.4s | 定义说明淡入 | `FadeIn(definition)` |
| 4.9s | 方向说明淡入 | `FadeIn(direction_text)` |
| 5.4s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有几何元素

---

## Scene 3: 弧度制的概念 (8-10秒)
**目的**: 介绍弧度制的基本定义

### 元素
1. 单位圆
2. π/2弧度的弧线
3. 1弧度的弧线
4. 等长半径
5. 弧长标注
6. 定义文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 绘制圆 | `Create(circle)` |
| 1.8s | 绘制π/2弧 | `Create(quarter_arc)` |
| 2.8s | 绘制1弧度弧和半径线 | `Create(unit_arc, radius_line)` |
| 3.8s | 弧长标注 | `Write(arc_label)` |
| 4.3s | 定义文字 | `FadeIn(rad_def)` |
| 4.8s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有几何元素

---

## Scene 4: 弧度与角度转换 (10-12秒)
**目的**: 展示弧度与角度的转换公式

### 元素
1. π rad = 180° 公式
2. 1 rad 转换公式
3. 1° 转换公式
4. 常用角度转换示例
5. 提示文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | π转换公式 | `Write(pi_formula)` |
| 1.6s | 1rad转换公式 | `Write(rad_to_deg)` |
| 2.4s | 1°转换公式 | `Write(deg_to_rad)` |
| 3.2s | 示例标题 | `Write(example_title)` |
| 3.5s | 示例1 | `Write(example_1)` |
| 3.8s | 示例2 | `Write(example_2)` |
| 4.1s | 示例3 | `Write(example_3)` |
| 4.6s | 提示文字 | `FadeIn(tip)` |
| 5.1s | 等待理解 | `Wait(2.5)` |

### 清理
- FadeOut: 所有公式元素

---

## Scene 5: 弧长公式 (8-10秒)
**目的**: 介绍弧长公式及其几何意义

### 元素
1. 弧长公式 l = |α|·r
2. 几何图解 (圆、弧、半径、角度)
3. 各元素标注
4. 公式说明
5. 示例计算

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 公式出现 | `Write(formula)` |
| 1.6s | 几何图解同时出现 | `Create(circle, center_dot, radius_line, ...)` |
| 3.1s | 说明文字 | `FadeIn(explanation)` |
| 3.6s | 示例文字 | `FadeIn(example)` |
| 4.1s | 等待理解 | `Wait(2.5)` |

### 清理
- FadeOut: 所有几何元素

---

## Scene 6: 扇形面积公式 (8-10秒)
**目的**: 介绍扇形面积公式及其优势

### 元素
1. 两个面积公式
2. 扇形图解
3. 各元素标注
4. 优势说明

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 两个公式出现 | `Write(formula_1, formula_2)` |
| 1.8s | 几何图解出现 | `Create(circle, sector, ...)` |
| 3.3s | 说明文字 | `FadeIn(explanation)` |
| 3.8s | 等待理解 | `Wait(2.0)` |

### 清理
- FadeOut: 所有几何元素

---

## Scene 7: 终边相同的角 (10-12秒)
**目的**: 介绍终边相同角的概念

### 元素
1. 公式 α + 2kπ
2. 几何图解 (原角和其他同终边角)
3. 各角度标注
4. 概念说明
5. 弧度制优势

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 标题出现 | `Write(title)` |
| 0.8s | 公式出现 | `Write(formula)` |
| 1.6s | 基础几何 | `Create(circle, original_line, angle_arc, ...)` |
| 2.4s | 同终边角1 | `Create(line_2pi)` |
| 3.2s | 同终边角2 | `Create(line_neg2pi)` |
| 4.0s | 角度标注 | `Write(label_2pi, label_neg2pi)` |
| 4.5s | 说明文字 | `FadeIn(explanation)` |
| 5.0s | 优势说明 | `FadeIn(advantage)` |
| 5.5s | 等待理解 | `Wait(2.5)` |

### 清理
- FadeOut: 所有几何元素

---

## Scene 8: 总结与关注 (8-10秒)
**目的**: 知识点总结和引流

### 元素
1. 知识点总结列表
2. 作者信息
3. 关注提示
4. 装饰元素

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 总结标题 | `Write(summary_title)` |
| 0.6s | 逐项显示知识点 | `FadeIn(item, shift=RIGHT*0.3)` |
| 3.0s | 作者名淡入 | `FadeIn(author_name, shift=DOWN*0.5)` |
| 3.8s | 作者ID淡入 | `FadeIn(author_id, shift=UP*0.3)` |
| 4.4s | 关注提示淡入 | `FadeIn(follow_text, shift=UP*0.3, scale=1.1)` |
| 5.0s | 装饰弧线 | `Create(decorative_arcs)` |
| 6.0s | 淡出所有 | `FadeOut(...)` |

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| 作者信息 | Scene 1 | Scene 8 | 一直保留到底 |
| 标题元素 | 各场景 | 下一场景开始前 | 每场景结束后清理 |
| 几何图形 | 各场景 | 各场景结束前 | 仅当前场景内存在 |
| 公式 | 各场景 | 各场景结束前 | 仅当前场景内存在 |

## 验证要点
1. 几何验证: 角度计算准确性，点位置精确性
2. LaTeX验证: 避免中文字符在MathTex中使用
3. 边界验证: 所有元素在安全边界内 (x∈[-4,4], y∈[-8,8])
