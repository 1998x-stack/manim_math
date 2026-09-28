# 随机事件与概率：可核验分镜

入口：`probability.py::ProbabilityScene`；竖屏逻辑尺寸 9×16，输出目标 1080×1920。每页切换时清理上一页的实际屏上对象，重要对象在 `show()` 中检查 Mobject 实际包围盒（横向 ±4.1，纵向 ±7.1）。旧 MP4 不代表本次修复已完成渲染。

| 页 | learning_fact / 给定条件 | 屏上对象与关键帧 | check |
| --- | --- | --- | --- |
| 1 开场 | 一次普通硬币抛掷结果尚未确定 | 硬币轮廓、问号、抛掷情景 | 概念未暗示所有硬币必定公平；问号在轮廓内 |
| 2 三类事件 | 普通硬币、一次抛掷、仅正反两种结果 | 三张卡片：正面 / 正面或反面 / 正面且反面 | 对照本页的限定试验识别随机、必然、不可能事件 |
| 3 概率范围 | 任意事件的概率介于 0 与 1 之间 | 数轴刻度 0、0.5、1，另列两个端点事件卡片 | `0≤P(A)≤1`；0.5 只是刻度值，不把所有随机事件固定成 0.5 |
| 4 韦恩图 | A、B 均为样本空间内的事件 | Ω 内两相交圆、交集与并集文字 | 实际图形交叠；示意面积不被用作概率值 |
| 5 加法公式 | 已知 P(A)=0.5、P(B)=0.4、P(A∩B)=0.2 | 同一韦恩图、扣除重复交集、结果 0.7 | `union_probability()` 校验三元组的相容性、并集数值与互斥边界 |
| 6 互补公式 | 10 个等可能结果，其中 6 个属于 A、4 个属于补集 | 10 个等面积小格，6 橙 4 紫、结果 0.6 / 0.4 | 格子数和概率一致；`complement_probability()` 核对 1−P(A) |
| 7 总结 | 概率范围、归一性、并集、互补 | 依次显示四条纯数学 LaTeX 公式 | 避免中文直接传入 MathTex；最大显示宽度 7.6 |
| 8 片尾 | 先确定样本空间，再分析事件 | 结语与署名 | 渲染时检查字幕可读和安全区 |

## 验证状态（本次源码修复）

- `math`: pass（`test_probability_math.py`，7 个测试方法，含反例和端点）。
- `syntax`: pass（`python -m py_compile probability.py probability_math.py test_probability_math.py`）。
- `ast`: not_run（完整仓库审计脚本尚未在此环境运行）。
- `manim_render` / `frame_review` / `ffprobe` / `audio_review`: not_run（当前环境未安装 Manim/TeX 渲染链，且未输出或覆盖任何 MP4）。

运行数学回归：在本课目录下执行 `python -m unittest -v test_probability_math.py`；可用 Manim/LaTeX 环境下运行 `manim -pql probability.py ProbabilityScene` 后，逐页检查首帧、换页、文字与公式的实际可见状态。