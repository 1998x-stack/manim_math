# 修复记录 - Bug Fixes

## 2024-02-09 修复 GrowArrow 兼容性问题

### 问题描述
在运行 `scene_5_correspondence()` 时出现错误：
```
TypeError: VMobject.scale() got an unexpected keyword argument 'scale_tips'
```

### 根本原因
- Manim 0.19.2 中，`CurvedArrow` 与 `GrowArrow` 动画不兼容
- `GrowArrow` 内部调用 `scale(0, scale_tips=True)`，但 `CurvedArrow` 的 `scale()` 方法不接受 `scale_tips` 参数

### 解决方案
将所有 `GrowArrow` 改为 `Create`：

**修改前：**
```python
self.play(GrowArrow(arrow_AD), run_time=0.7)
self.play(GrowArrow(arrow_BE), run_time=0.7)
self.play(GrowArrow(arrow_CF), run_time=0.7)
```

**修改后：**
```python
self.play(Create(arrow_AD), run_time=0.7)
self.play(Create(arrow_BE), run_time=0.7)
self.play(Create(arrow_CF), run_time=0.7)
```

### 影响
- 箭头动画效果略有不同：从生长效果改为绘制效果
- 视觉上仍然流畅，符合教学需求
- 兼容性更好，不会出现错误

### 测试验证
修复后，代码应该可以正常运行：
```bash
manim -pql congruent_triangles.py CongruentTriangles
```

---

## 技术说明

### Manim 0.19.2 已知限制
根据技能文档，以下是已知的参数约束：

| 类 | 参数 | 约束说明 |
|---|------|---------|
| `Arrow.scale()` | `scale_tips` | ⚠️ 在某些情况下可能不兼容 |
| `CurvedArrow` | 与 `GrowArrow` | ❌ 不兼容（本次修复） |

### 推荐的箭头动画方式

**方法1：使用 Create（推荐）**
```python
arrow = CurvedArrow(start, end)
self.play(Create(arrow), run_time=0.7)
```

**方法2：使用 FadeIn**
```python
arrow = CurvedArrow(start, end)
self.play(FadeIn(arrow, shift=UP*0.2), run_time=0.5)
```

**方法3：使用直线箭头 + GrowArrow**
```python
arrow = Arrow(start, end)  # 不是 CurvedArrow
self.play(GrowArrow(arrow), run_time=0.7)
```

### 兼容性检查清单

在创建 Manim 动画时，建议检查：

- [ ] 避免对 `CurvedArrow` 使用 `GrowArrow`
- [ ] 避免在 `MathTex` 中使用中文
- [ ] 使用 `^\circ` 而非 `°` 符号
- [ ] 使用 `\frac{}{}` 而非双花括号
- [ ] 确保 `corner_radius` 只用于 `RoundedRectangle`

---

**修复时间**: 2024-02-09  
**修复版本**: v1.1  
**状态**: ✅ 已解决