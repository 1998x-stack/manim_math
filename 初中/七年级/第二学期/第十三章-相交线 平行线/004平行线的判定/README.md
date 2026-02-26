# 平行线的判定 - Manim 动画

这是一个使用 Manim 制作的初中数学教学动画，展示了平行线的三种判定方法。

## 内容概要

该动画详细演示了平行线的三种判定方法：

1. **同位角相等** ⟹ 两直线平行
2. **内错角相等** ⟹ 两直线平行  
3. **同旁内角互补** ⟹ 两直线平行

这体现了“由角的关系推断线的关系”的核心思想。

## 文件结构

- `final_parallel_determination.py` - 主动画代码
- `parallel_line_determination.py` - 初步实现代码
- `verify_geometry.py` - 几何验证脚本
- `storyboard.md` - 动画分镜脚本
- `prompt.md` - 原始需求文档

## 运行要求

- Python 3.7+
- Manim 0.19.2
- NumPy

安装依赖：
```bash
pip install manim==0.19.2 numpy
```

## 运行方式

### 预览动画（低质量，快速渲染）：
```bash
manim -pql final_parallel_determination.py ParallelLineDetermination
```

### 高质量渲染：
```bash
manim -pqh final_parallel_determination.py ParallelLineDetermination
```

### 仅生成视频最后一帧（用于预览）：
```bash
manim -s -ql final_parallel_determination.py ParallelLineDetermination
```

## 动画特色

- **TikTok竖屏格式**：1080×1920像素，适合手机观看
- **精准几何计算**：所有坐标均通过NumPy精确计算，确保几何关系正确
- **清晰视觉引导**：使用颜色编码突出重点概念
- **中文支持**：使用正确的字体设置显示中文文本
- **教育导向**：按照教学逻辑组织内容，便于学生理解

## 几何验证

代码包含了完整的几何验证系统，确保：
- 两条直线真正平行
- 截线正确穿过两条平行线
- 角度关系准确（同位角、内错角、同旁内角）
- 所有元素在安全边界内

## 教学要点

动画强调的核心概念是"由角推线"，即通过角度关系来判断直线是否平行，这与平行线性质（由线推角）正好相反。

## 制作信息

- 作者：上海初高中数学直通车
- 社交媒体：@emptyandcalm
- 适用年级：七年级
- 章节：第十三章 相交线 平行线