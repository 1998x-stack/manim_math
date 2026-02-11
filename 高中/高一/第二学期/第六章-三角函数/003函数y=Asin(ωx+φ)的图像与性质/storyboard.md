# 函数y=Asin(ωx+φ)的图像与性质 - 动画分镜脚本

## 元信息
- 目标时长: 60-90 秒
- 场景数量: 8 个
- 难度等级: 中等
- 格式: TikTok竖屏 (1080×1920)

## 颜色配置
```python
COLOR_PRIMARY = "#e74c3c"    # 红色 - 强调
COLOR_SECONDARY = "#3498db"  # 蓝色 - 坐标轴/基础函数
COLOR_HIGHLIGHT = YELLOW     # 黄色 - 重要元素
COLOR_AUXILIARY = GRAY_B     # 灰色 - 辅助线
COLOR_FUNCTION = BLUE        # 蓝色 - 函数图像
COLOR_TRANSFORMED = RED      # 红色 - 变换后图像
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 基础正弦波 | y=sin(x) | self.base_wave |
| A变化 | y=A*sin(x) | self.amplitude_wave |
| ω变化 | y=sin(ω*x) | self.frequency_wave |
| φ变化 | y=sin(x+φ) | self.phase_wave |
| 完整函数 | y=A*sin(ω*x+φ)+B | self.full_transformed |

---

## Scene 1: 开场 (3-4秒)
**目的**: 钩子 + 引出问题

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 主函数公式

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 标题书写 | `Write(title)` |
| 1.1s | 主公式出现 | `Create(formula)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- FadeOut: hook_text
- 保留: title, formula

---

## Scene 2: 基础正弦函数回顾 (5-6秒)
**目的**: 复习基础的y=sin(x)图像

### 元素
1. 坐标系
2. y=sin(x)图像
3. 标记周期、振幅

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 创建坐标系 | `Create(axes)` |
| 0.5s | 绘制sin图像 | `Create(sin_graph)` |
| 1.5s | 标记周期 | `Create(period_brace)` |
| 2.5s | 标记振幅 | `Create(amplitude_brace)` |
| 3.5s | 显示数值 | `Write(period_label, amplitude_label)` |

### 清理
- 保留: axes, sin_graph

---

## Scene 3: 振幅A的作用 (8-10秒)
**目的**: 展示A对图像的影响

### 元素
1. 基础sin图像（虚线）
2. A变化后的图像
3. 振幅标记线
4. 参数A的滑块或指示器

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 基础图像变虚线 | `sin_graph.set_stroke(opacity=0.5)` |
| 0.5s | 创建A=2的图像 | `Create(double_amplitude_graph)` |
| 2.0s | 标记新振幅 | `Create(new_amplitude_brace)` |
| 3.0s | 对比显示 | `Transform(amplitude_brace)` |
| 4.0s | 数学公式演示 | `TransformMatchingTex(formula1, formula2)` |

### 清理
- 保留: axes, transformed_graph

---

## Scene 4: 频率ω的作用 (8-10秒)
**目的**: 展示ω对图像的影响

### 元素
1. 基础图像（参考）
2. ω变化后的图像
3. 周期对比线
4. 参数ω的指示器

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 添加ω变化图像 | `Create(omega_graph)` |
| 1.0s | 标记新周期 | `Create(omega_period_brace)` |
| 2.5s | 计算公式 | `Write(omega_formula)` |
| 4.0s | 对比演示 | `TransformMatchingTex(period_formula1, period_formula2)` |

### 清理
- 保留: axes, omega_graph

---

## Scene 5: 相位φ的作用 (8-10秒)
**目的**: 展示φ对图像的影响

### 元素
1. 基础图像（参考）
2. φ变化后的图像
3. 水平位移标记
4. 参数φ的指示器

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 添加φ变化图像 | `Create(phi_graph)` |
| 1.0s | 显示位移 | `Create(shift_arrow)` |
| 2.5s | 标记相位 | `Write(phase_label)` |
| 4.0s | 相位公式 | `Write(phase_formula)` |

### 清理
- 保留: axes, phi_graph

---

## Scene 6: 垂直平移B的作用 (5-6秒)
**目的**: 展示B对图像的影响

### 元素
1. 之前的图像
2. B变化后的图像
3. 垂直位移标记
4. 参数B的指示器

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 添加B变化图像 | `Create(b_shifted_graph)` |
| 1.0s | 显示垂直位移 | `Create(vertical_shift_arrow)` |
| 2.5s | 标记B值 | `Write(b_label)` |
| 3.5s | 完整公式 | `Write(full_formula)` |

### 清理
- 保留: axes, full_graph

---

## Scene 7: 参数联动演示 (8-10秒)
**目的**: 综合展示所有参数的作用

### 元素
1. 坐标系
2. 动态函数图像
3. 参数控制器
4. 实时公式更新

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 参数滑块显示 | `Create(sliders)` |
| 1.0s | 函数动态变化 | `UpdateFromAlphaFunc(graph)` |
| 3.0s | 关键点标记 | `Create(key_points)` |
| 5.0s | 特征标记 | `Create(max_min_lines)` |

### 清理
- 保留: axes, final_graph

---

## Scene 8: 总结回顾 (4-5秒)
**目的**: 总结各个参数的作用

### 元素
1. 最终函数图像
2. 参数作用总结
3. 作者信息

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示总结框 | `Create(summary_box)` |
| 0.5s | A作用说明 | `Write(a_explanation)` |
| 1.5s | ω作用说明 | `Write(omega_explanation)` |
| 2.5s | φ作用说明 | `Write(phi_explanation)` |
| 3.5s | B作用说明 | `Write(b_explanation)` |
| 4.5s | 结尾 | `Write(outro_text)` |

### 清理
- 全部清理

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| axes | Scene 2 | Scene 8 | 坐标系 |
| base_sin | Scene 2 | Scene 3 | 基础正弦函数 |
| amplitude_graph | Scene 3 | Scene 8 | 振幅变换函数 |
| omega_graph | Scene 4 | Scene 8 | 频率变换函数 |
| phi_graph | Scene 5 | Scene 8 | 相位变换函数 |
| full_graph | Scene 6 | Scene 8 | 完整变换函数 |
| formula | Scene 1 | Scene 8 | 主公式 |
| summary_box | Scene 8 | Scene 8 | 总结框 |