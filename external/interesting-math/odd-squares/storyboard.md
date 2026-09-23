# 奇数为什么能拼出正方形？｜数学规格与分镜

- audience：小学高年级／初一；先修：奇数、平方数、面积、正方形。
- source：独立数学探索；未声明教材版本。制作依据：`.claude/skills/manim-video-production/SKILL.md`。
- learning objective：能说出第 n 层为什么恰有 2n−1 个单位格，并解释 n 层恰好构成 n×n 的正方形。
- format：逻辑 9×16，1080×1920，深色；无外部媒体、无配乐；目标约 16–22 s（以实际渲染为准）。

## 数学规格

- claim：对正整数 n，1+3+…+(2n−1)=n²；空和 n=0 时两边皆为 0。
- assumptions/domain：n∈非负整数；格子不重叠、单位边长相同；第 n 层从 (n−1,j)，0≤j<n，及 (i,n−1)，0≤i<n−1 取得。
- justification：新层是最右一列 n 格加最上一行 n−1 格，共 2n−1 格；逐层恰好覆盖 [0,n−1]² 的所有整点格。
- counterexample/edge：n=0 不画第 0 层；n<0 无此铺砖定义。有限层的动画展示了构造规则，普遍结论由按 n 延续的同一构造得到，而非只凭五幅图猜测。
- tests：`test_math.py::VisualMathTests.test_odd_squares` 比较独立求和、每层格数和互不重叠的整方形覆盖。

## 分镜

| shot | learning_fact | 屏上状态和生命周期 | 动画／约时 | check |
| --- | --- | --- | --- | --- |
| 01 | 要研究逐个奇数的和 | title、hint、formula `0=0²` 新建，持续存在 | 字幕和起始等式，约 2 s | 读得清、起始空和成立 |
| 02 | 第 n 层恰好补齐一个大正方形 | 每一层 `cells` 新建且保持；同一 `formula` 对象用 `Transform` 更新 | 依次绘制 n=1…5，约 10 s | 显示 1、3、5、7、9 格；各层无重复；显示等式对应当下方格总数 |
| 03 | 总结一般公式 | `conclusion` 新建；方格仍保留 | 最后写出求和公式并停留，约 3 s | 公式和格子不重叠、下方字幕在安全区 |

- objects：`title,hint,formula` 01 创建／保留；`cells(n)` 02 创建／全保留；`conclusion` 03 创建；无虚构的中途删除与音轨。
- safe frame：公式 y≈−3，结论 y≈−5.15；主图逻辑宽约 3.45，高约 3.45；逐帧边界仍需用真实 Mobject 包围盒验收。

## 验收记录

| math | syntax | ast | unit_tests | manim_render | frame_review | ffprobe | audio_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| not_run | not_run | not_run | not_run | blocked（本次环境无 Manim） | not_run | not_run | not_run（无音轨） |

本文件写入不代表上述检查已运行；执行与结果见上层 `README.md` 后续维护记录。
