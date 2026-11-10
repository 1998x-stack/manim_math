# 小学第五批：四门六年级课程删除重复独立 Scene

> 第五批基于第四批 PR #174 的工作分支堆叠。这里的“删除”是从当前 Git 分支删除 Python 源文件，**并未修改任何旧视频 MP4**。删除的 Scene 类名和原 Python 路径不再可直接运行，历史版本可由 Git 历史恢复。

## 选保留源码的依据

- 对比同目录两份 Scene 的实际讲解结构、数学目标及旧 Gallery 的 `videoFile`。四门课各存在一套多段完整教学 Scene 和一套短演示 Scene；保留多段课程并补数学测试，删除短演示。
- 旧 Gallery 的 `id`、`videoFile`、`hasVideo` 和课程总数保持不变。仅《比与分数、除法的关系》原 `pyFile` 指向被删源码，因此需要精确指向完整课程；其余三项无需修改 `pyFile`。
- 不删除课程描述、Prompt、Storyboard、纯数学模型、验证脚本、视频素材；不认为旧 MP4 名称匹配主 Scene 就等同于渲染来源证明。

## 四门课程旧→新映射

### 1. 比与分数、除法的关系

课程目录：`小学/六年级/第一学期/第三章-比和比例/002比与分数、除法的关系/`。

**保留**：`002_比与分数除法的关系.py`，Scene `RatioFractionDivisionLesson`。

**删除**：`002_比与分数、除法的关系.py`，原 Scene `比与分数除法的关系Animation`。

新增 `ratio_value`，对整数前项、非零后项返回精确分数；Scene 检查 3:5、3:4、2:5 的等值形式。保留完整概念、名称表、例题、区别与零分母禁忌。

- Gallery topic ID：`dc6c271f43`；视频：`RatioFractionDivisionLesson_finish.mp4`（不变）。
- Gallery `pyFile`：从短 Scene 更新为完整 Scene。
- 现在的渲染命令：`manim -pql '002_比与分数除法的关系.py' RatioFractionDivisionLesson`（需在该课程目录下运行）。

### 2. 最大公因数和最小公倍数（深化）

课程目录：`小学/六年级/第一学期/第一章-数的整除/003最大公因数和最小公倍数(深化)/`。

**保留**：`003_最大公因数与最小公倍数.py`，Scene `GcfLcmLesson`。

**删除**：`003_最大公因数和最小公倍数(深化).py`，原 Scene `最大公因数和最小公倍数深化Animation`。

新增 `gcd_lcm_values`，精确检查 12/18、12/18/24、8/15、36/24；保留质因数分解、短除法、文氏图、三数、互素与应用场景。

- Gallery topic ID：`912515c904`；视频：`GcfLcmLesson_finish.mp4`（不变）。
- Gallery `pyFile`：原本已指向保留版，保持不变。
- 现在的渲染命令：`manim -pql '003_最大公因数与最小公倍数.py' GcfLcmLesson`（需在该课程目录下运行）。

### 3. 线段的相等与和、差、倍、分

课程目录：`小学/六年级/第一学期/第七章-线段与角的画法/001线段的相等与和、差、倍、分/`。

**保留**：`001_线段的相等与和差倍分.py`，Scene `SegmentRelationsLesson`。

**删除**：`001_线段的相等与和、差、倍、分.py`，原 Scene `线段相等与和差倍分Animation`。

新增 `segment_lengths` 检查线段和、差、倍、中点一半，要求 AB 与 CD 非负且 AB≥CD；保留尺规作图、分段相加相减、倍与中点完整分镜。

- Gallery topic ID：`5ea56a3e0f`；视频：`SegmentRelationsLesson_finish.mp4`（不变）。
- Gallery `pyFile`：原本已指向保留版，保持不变。
- 现在的渲染命令：`manim -pql '001_线段的相等与和差倍分.py' SegmentRelationsLesson`（需在该课程目录下运行）。

### 4. 余角、补角、对顶角

课程目录：`小学/六年级/第一学期/第七章-线段与角的画法/002余角、补角、对顶角/`。

**保留**：`002_余角补角对顶角.py`，Scene `ComplementarySupplementaryVerticalLesson`。

**删除**：`002_余角、补角、对顶角.py`，原 Scene `余角补角对顶角Animation`。

新增 `angle_partner`、`crossing_angles` 检查 90° 互余、180° 互补、对顶角相等；Scene 检查 52°→38°、75°→105°、70°/110° 等例子；保留定义、证明与综合练习。

- Gallery topic ID：`70666cc6c2`；视频：`ComplementarySupplementaryVerticalLesson_finish.mp4`（不变）。
- Gallery `pyFile`：原本已指向保留版，保持不变。
- 现在的渲染命令：`manim -pql '002_余角补角对顶角.py' ComplementarySupplementaryVerticalLesson`（需在该课程目录下运行）。

## 源码库存与测试

- 原基线小学 273 个 Python；第三批 269、第四批 263、第五批去重四份后 **259 个**。
- 多 Python 源码的知识点目录从上一批 39 减为 **35**；当前影子审核清单中 15 个已静态核对、20 个仍待人工确认。
- 新增 `tests/test_primary_scene_deduplication_batch5.py`，用 AST 从真实主源码提取纯数学函数进行数学回归，不导入 Manim，不加载旧视频。覆盖商与约分的等价、正整数 GCD×LCM=a×b、线段和差倍半、互余互补和对顶角的几何条件。
- 更新影子映射清单、稀疏源码 CI 与画廊路径测试，避免删除文件后仍被直接引用。

## 验证命令

```bash
python -m unittest tests.test_primary_scene_deduplication_batch5 -v
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
python tools/legacy_contract.py --expect-count 534
```

**局限**：上述属于数学与源码质量检查；没有真实运行本批四条 Manim Scene 进行视频渲染、逐帧审查或 MP4 内容真实性对比。待具备字体/LaTeX/FFmpeg 的执行环境进行低清渲染验收。
