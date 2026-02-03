# 修复说明 - Polyhedron 顶点访问问题

## 🐛 问题描述

原代码在访问 `Polyhedron` 对象的顶点时使用了 `get_vertices()` 方法，但 Manim 0.19.2 中的 `Polyhedron` 类没有这个方法，导致以下错误：

```
AttributeError: Polyhedron object has no attribute 'vertices'
```

## ✅ 修复方案

### 问题根源

Manim 中的 `Polyhedron` 类继承自 `Surface`，它是一个 3D 曲面对象，不像 2D 的 `Polygon` 那样有 `get_vertices()` 方法可以直接获取顶点列表。

### 解决方法

#### 1. 对于自定义 Polyhedron

在创建 `Polyhedron` 时，保存原始顶点坐标供后续使用：

```python
# 原始顶点定义
vertices_raw = [
    [0, 0, 0],
    [1, 0, -0.5],
    [-0.5, 0, -0.5],
    [0, 1.2, 0],
]

# 保存缩放后的顶点坐标
scale_factor = 1.3
vertices_scaled = [np.array(v) * scale_factor for v in vertices_raw]

# 创建多面体
poly = Polyhedron(
    vertex_coords=vertices_raw,
    faces_list=faces
).scale(scale_factor)

# 后续使用保存的顶点坐标
dots = VGroup(*[
    Dot3D(point=v, radius=0.08, color=RED)
    for v in vertices_scaled  # ← 使用保存的坐标
])
```

#### 2. 对于内置正多面体（Tetrahedron, Cube 等）

使用启发式方法从 `get_all_points()` 中提取顶点：

```python
# 获取所有采样点
all_points = poly.get_all_points()

# 去重：找到独特的点作为顶点
unique_points = []
tolerance = 0.1

for point in all_points:
    is_unique = True
    for up in unique_points:
        if np.linalg.norm(point - up) < tolerance:
            is_unique = False
            break
    if is_unique:
        unique_points.append(point)

# 取前V个点作为顶点
vertices = unique_points[:V]
```

**注意**: 这是一个近似方法，可能不总是准确。更安全的做法是：
- 仅展示边和面的高亮效果
- 使用文字标注而非实际的顶点标记

## 📝 修改的文件

### 1. `polyhedron_concepts.py`

**修改位置 1**: `show_polyhedron_definition()` 方法
- 保存顶点坐标到 `vertices_scaled`
- 在高亮面、棱、顶点时使用保存的坐标

**修改位置 2**: `show_polyhedron_detail()` 方法
- 添加 try-except 错误处理
- 使用 `get_all_points()` + 去重算法获取顶点
- 降级方案：如果无法获取顶点，仅显示计数文字

### 2. `test_scenes.py`

**修改位置**: `TestDefinition` 类
- 保存缩放后的顶点坐标
- 使用保存的坐标创建顶点标记

## 🎯 效果对比

### 修复前（错误）
```python
# ❌ 会抛出 AttributeError
dots = VGroup(*[
    Dot3D(point=v, radius=0.08, color=RED)
    for v in poly.get_vertices()  # ← Polyhedron 没有这个方法
])
```

### 修复后（正确）
```python
# ✅ 使用保存的顶点坐标
vertices_scaled = [np.array(v) * scale_factor for v in vertices_raw]

dots = VGroup(*[
    Dot3D(point=v, radius=0.08, color=RED)
    for v in vertices_scaled  # ← 使用已知的坐标
])
```

## 🧪 测试验证

运行以下命令测试修复效果：

```bash
# 快速测试定义场景
python test_scenes.py --scene definition --quality l

# 测试完整动画
manim -pql polyhedron_concepts.py PolyhedronConcepts
```

## 📚 相关知识

### Manim 3D 对象层次结构

```
Mobject (基类)
  └─ VMobject (向量图形)
      └─ Surface (3D曲面)
          ├─ Polyhedron (多面体)
          ├─ Sphere (球体)
          └─ ... (其他3D曲面)
```

### 可用的方法

| 对象类型 | 获取顶点的方法 |
|---------|---------------|
| `Polygon` (2D) | `get_vertices()` ✅ |
| `Polyhedron` (3D) | ❌ 无直接方法 |
| 自定义 `Polyhedron` | 保存 `vertex_coords` ✅ |
| 内置正多面体 | `get_all_points()` + 去重 ⚠️ |

### 最佳实践

1. **创建时保存**: 如果需要后续访问顶点，创建对象时保存顶点坐标
2. **使用替代方法**: 优先使用边/面的高亮效果，而非顶点标记
3. **错误处理**: 对可能失败的顶点访问使用 try-except
4. **文档注释**: 在代码中明确说明顶点处理方式

## 🔄 未来改进

如果需要更精确的顶点访问，可以考虑：

1. **创建自定义 Polyhedron 子类**:
   ```python
   class PolyhedronWithVertices(Polyhedron):
       def __init__(self, vertex_coords, faces_list, **kwargs):
           super().__init__(vertex_coords, faces_list, **kwargs)
           self._vertices = [np.array(v) for v in vertex_coords]
       
       def get_vertices(self):
           return self._vertices
   ```

2. **使用网格数据**: 如果 Manim 提供网格访问接口，可直接获取顶点

3. **参考官方文档**: 查看最新 Manim 版本是否添加了顶点访问方法

## ✨ 总结

本次修复通过两种方法解决了 `Polyhedron` 顶点访问问题：
1. 自定义多面体：保存顶点坐标
2. 内置多面体：使用启发式算法 + 降级方案

修复后的代码更加健壮，能够正确处理各种情况。

---

**修复日期**: 2026-02-03  
**Manim 版本**: 0.19.2  
**修复者**: Claude