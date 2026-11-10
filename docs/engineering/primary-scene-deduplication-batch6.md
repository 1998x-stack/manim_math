# 小学第六批：重写 5 门六年级数学课程并删除重复 Scene

> 第六批基于第五批的开发分支，采取“先把保留入口改造成真正数学教学动画，再删除冗余 Scene”的原则。保留原先与历史发布视频相对应的 Scene 类名与 `*_animation.py` 源路径。**不会删除或重编码任何 MP4，也未将现有 MP4 认定为新代码的渲染结果。**

## 选择依据

- 对比这五个目录的两份 Python：较长的 `_animation.py` 原本是通用模板，实际存在“正在学习……的概念”占位内容；较短的 `_...py` 文件则包含实质数学例题。不能凭代码长度选择长文件为优。
- 先把较短文件中正确的数学示例与教材 `description.json`、`storyboard.md` 的范围吸收入保留版 `_animation.py`，再删除短版本，使课程目录只有一份直接 Scene。
- 每个保留文件有 9:16 竖屏配置、顶部作者标识、独立的多个教学阶段，MathTex 使用纯 LaTeX、中文解释放在 Text 中。
- 真实数值逻辑抽为标准库纯 Python 函数，增加不依赖 Manim 的边界测试；校验主源码内直接 Scene 类名与唯一性。

## 五门课保留/删除路径

### 1. 六年级上·一元一次方程的解法

目录：`小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/001一元一次方程的解法/`。

- **保留并重写** `001一元一次方程的解法_animation.py`，Scene：`Topic001一元一次方程的解法Animation`。
- **删除** `001_一元一次方程的解法.py`，旧 Scene：`一元一次方程的解法Animation`。
- 具体增强：去分母与代回检验、去括号与移项例题；精确有理数求解（Fraction）。
- 历史 Gallery ID：`b4fb824ca8`；Gallery 已指向保留版本。旧视频文件名仍为 `Topic001一元一次方程的解法Animation_finish.mp4`。
- 新渲染命令（从课程目录执行）：`manim -pql '001一元一次方程的解法_animation.py' Topic001一元一次方程的解法Animation`。

### 2. 六年级上·二元一次方程组

目录：`小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/002二元一次方程组/`。

- **保留并重写** `002二元一次方程组_animation.py`，Scene：`Topic002二元一次方程组Animation`。
- **删除** `002_二元一次方程组.py`，旧 Scene：`二元一次方程组Animation`。
- 具体增强：加减消元与代入消元两种方法；检查行列式并验证 (3,2) 同时满足两式。
- 历史 Gallery ID：`3875f23dcf`；Gallery 已同步切换到保留版本。旧视频文件名仍为 `Topic002二元一次方程组Animation_finish.mp4`。
- 新渲染命令（从课程目录执行）：`manim -pql '002二元一次方程组_animation.py' Topic002二元一次方程组Animation`。

### 3. 六年级上·不等式及其性质

目录：`小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/003不等式及其性质/`。

- **保留并重写** `003不等式及其性质_animation.py`，Scene：`Topic003不等式及其性质Animation`。
- **删除** `003_不等式及其性质.py`，旧 Scene：`不等式及其性质Animation`。
- 具体增强：同加同减、乘正负数、不等号反转与乘 0 成为等式；运算及符号判断。
- 历史 Gallery ID：`1994079dfc`；Gallery 已同步切换到保留版本。旧视频文件名仍为 `Topic003不等式及其性质Animation_finish.mp4`。
- 新渲染命令（从课程目录执行）：`manim -pql '003不等式及其性质_animation.py' Topic003不等式及其性质Animation`。

### 4. 六年级下·正比例

目录：`小学/六年级/第二学期/第二章-比例/001正比例/`。

- **保留并重写** `001正比例_animation.py`，Scene：`Topic001正比例Animation`。
- **删除** `001_正比例.py`，旧 Scene：`正比例Animation`。
- 具体增强：固定比值表、y=kx 正比例图像、零点的比值限制、非正比例反例。
- 历史 Gallery ID：`8883bec7e6`；Gallery 已指向保留版本。旧视频文件名仍为 `Topic001正比例Animation_finish.mp4`。
- 新渲染命令（从课程目录执行）：`manim -pql '001正比例_animation.py' Topic001正比例Animation`。

### 5. 六年级下·抽屉原理

目录：`小学/六年级/第二学期/第五章-整理与提高/001抽屉原理/`。

- **保留并重写** `001抽屉原理_animation.py`，Scene：`Topic001抽屉原理Animation`。
- **删除** `001_抽屉原理.py`，旧 Scene：`抽屉原理Animation`。
- 具体增强：4 个物体放 3 个盒子的反证、ceil(10/3)=4 的推广例题、一般数学下界。
- 历史 Gallery ID：`843369bcf3`；Gallery 已指向保留版本。旧视频文件名仍为 `Topic001抽屉原理Animation_finish.mp4`。
- 新渲染命令（从课程目录执行）：`manim -pql '001抽屉原理_animation.py' Topic001抽屉原理Animation`。

## 库存和 Gallery 变化

- 小学 `.py` 从第三批前的 273 个降至 **254 个**：累计删除 19 个独立重复 Scene；第五批之后为 259，本批再减少 5。
- 多 Python 的知识点目录由第六批前的 35 减为 **30 个**；其中 15 个已静态核对，15 个仍待审。
- Gallery 依旧保留 534 条课程，五课历史 `id`、`videoFile`、`hasVideo` 全部不变。只有二元一次方程组和不等式及其性质的 `pyFile` 以及配套 `docstring` 更新，其余三课 `pyFile` 原本已指向保留版。
- 用户已发布的视频并未重渲染，因此可能仍展示旧模板内容；本批不把源码升级表述为成片自动升级。

## 检查命令与验收局限

```bash
python -m unittest tests.test_primary_scene_deduplication_batch6 -v
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
python tools/legacy_contract.py --expect-count 534
```

测试对真实源文件进行 AST 静态检查，独立验证方程、有理数系数的方程组、不等号反转、正比例与抽屉原理的数学不变量。**尚未进行五课的真实 Manim 低清渲染和视频画面/字幕/时间轴验收**；这些需要 Manim、中文字体、LaTeX 和 FFmpeg 环境。
