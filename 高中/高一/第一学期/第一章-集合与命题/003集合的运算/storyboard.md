# 集合的运算｜与 `set_operations.py` 对应的可验分镜

## 数学规格和画面坐标

- 唯一全集 `U={1,2,3,4,5,6,7,8}`，`A={1,2,3,4}`，`B={3,4,5,6}`。三个运算和综合例题均不更换这三个集合；补集一律相对于 U。
- 圆 A/B 半径均为 1.55，圆心分别为 (-0.9,1.45)、(0.9,1.45)；全集矩形中心 (0,1.45)，宽 7.5，高 5.1。每个数字点的真实位置由 `SetOperations.MARKER_POSITIONS` 唯一给出。1、2 位于仅 A，3、4 位于交集，5、6 位于仅 B，7、8 位于仅 U 区域。
- 公式用 `MathTex`，中文用 `Text`；标题 y≈5.7、Venn 图 y≈1.45、定义 y≈-2.17、三条计算式 y≈-3.66/-4.48/-5.30。数值坐标检查不代替最终字体包围盒或关键帧审查。

| 镜头 / Scene 方法 | learning_fact / 给定条件 | 屏幕状态与实际数据 | 对象生命周期 | check |
|---|---|---|---|---|
| 1 `show_opening` | 所有运算对同一个 U/A/B 执行 | 同时显示全集矩形、重叠圆和 8 个标号 | 创建 `author_info`、`diagram`；标题与副标题退出 | 8 个编号唯一且各自位于正确区域 |
| 2 `show_intersection` | `A∩B={3,4}` | 紫色 `Intersection` 覆盖双圆交叠区，只强调数字 3、4 | 临时填充、公式和标题清场；保留 `diagram` 的同一引用 | 集合交集与两圆的内部归属一致 |
| 3 `show_union` | `A∪B={1,2,3,4,5,6}`，重复元素只写一次 | 绿色 `Union` 覆盖两圆；6 个数字依次强调 | 临时覆盖区与文字清场，保留底图 | 结果元素为 6 个而非 8 个 |
| 4 `show_complement` | `U\setminus A={5,6,7,8}` | 橙色 `Difference(U,A)` 覆盖大矩形中 A 以外的区域；强调包括圆外的 7、8 | 操作后完整移除 `diagram`，性质镜头不残留旧画面 | 明示 U，结果包含 7、8 且不含 1–4 |
| 5 `show_properties_1` | `A∩∅=∅`、`A∪∅=A`、`A∩A=A`、`A∪A=A` | 不再展示 Venn 图；四式逐条出现 | 公式组在本镜结束时退出 | 任意有限集和空集边界成立 |
| 6 `show_properties_2` | `A∪(U\setminus A)=U`、`A∩(U\setminus A)=∅`、`U\setminus(U\setminus A)=A` | 三个补集恒等式相对同一 U | 公式组在本镜结束时退出 | 任意 A⊆U，含 A=∅、A=U |
| 7 `show_example` | 在上述固定 U/A/B 上求 `(A∩B)`、`U\setminus(A∩B)`、`A∩(U\setminus B)` | 依次得到 `{3,4}`、`{1,2,5,6,7,8}`、`{1,2}`；强调第二式对应的 6 个数字 | 重新创建 `diagram`，与结果式一同退出 | 运算顺序及符号与真实元素一致 |
| 8 `show_outro` | 总结交并补 | 中文总结和原作者标识 | 所有可见对象退出 | 片尾无残留、无超出竖屏安全区 |

## 验证层级与保护

1. `python -m py_compile set_operations.py verify_set_operations.py`。
2. `python verify_set_operations.py`：纯 Python 从真实 Scene AST 提取数学模型、圆心半径及 8 个元素位置，校验所有交并补结论与退化输入。
3. `python .opencode/skills/manim-video-production/scripts/audit_scene.py <本课/set_operations.py> --json`；AST 告警逐条判断。
4. 在确有 Manim、TeX、中文字体时：`manim -ql set_operations.py SetOperations`；逐镜查看首帧、着色图层、中文、数学式、公式与具体数字的空间对应；高质量版本用 `ffprobe` 验证宽高、帧率及音轨。当前未执行的层级必须写 `not_run`，不得用旧 MP4 充当验收。
5. 不覆盖本课程原有 `.mp4` 或音轨；没有真实媒体验收前保持 PR 为 Draft。
