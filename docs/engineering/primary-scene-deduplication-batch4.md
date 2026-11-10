# 小学第四批：删除 6 份冗余教学 Scene 并增强保留源码

> 对应 PR：第四批独立分支 `refactor/primary-deduplicate-scenes-batch4-20261110`。本批发生的是 Git 源码删除，**没有删除、修改、重新编码任何 MP4**；删除的直接渲染入口不再可用，需根据下列映射更新旧命令。保留的历史成片未进行画面对比或渲染验证。

## 统一操作

- 只在确认为同课的两份独立 Manim Scene 时删除一份（主实现内容丰富、数学职责可检测），不误删除纯模型、单元测试、历史目录素材。
- 每门课保留一份教学源码及 Scene 名称，并加入可脱离 Manim 运行的纯数学/契约函数以及回归测试。
- Gallery 原有课程 `id`、`videoFile`、`hasVideo` 与总条目数（534）全部维持，仅将其中 5 条指向被删除源码的 `pyFile` 与对应源码 `docstring` 更新为保留文件。五年级《解简易方程》原本已指向保留源码，无需修改 Gallery 路径。
- 依据现有发布视频文件名与保留场景类名一致来选择候选，不将此误认为对 MP4 真实来源的已完成验证。

## 六课删除映射

### 1. 四年级上：线段、射线、直线

课程目录：`小学/四年级/第一学期/第五章-几何小实践——圆与角/001线段、射线、直线/`。

**保留** `001_线段射线直线.py`，Scene `LineSegmentRayLesson`。

**删除** `001_线段、射线、直线.py`，旧 Scene `SegmentRayLineLesson`。

提取 `shape_traits()` 统一给三类图形的端点、长度与延伸方向表格供值，避免重复手写不一致。

- Gallery topic ID：`6ce457db4d`；视频：`LineSegmentRayLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '001_线段射线直线.py' LineSegmentRayLesson`。

### 2. 五年级上：用字母表示数

课程目录：`小学/五年级/第一学期/第四章-简易方程(一)/001用字母表示数/`。

**保留** `001_用字母表示数.py`，Scene `LetterRepresentLesson`。

**删除** `001用字母表示数_animation.py`，旧 Scene `Topic001用字母表示数Animation`。

保留加法交换律、面积公式与代数简写的完整分镜，新增 `literal_product()` 验证 `5a`、`2a`、系数 0/1/-1 与非法输入。

- Gallery topic ID：`2e1ca2aed3`；视频：`LetterRepresentLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '001_用字母表示数.py' LetterRepresentLesson`。

### 3. 五年级上：方程的意义

课程目录：`小学/五年级/第一学期/第四章-简易方程(一)/002方程的意义/`。

**保留** `002_方程的意义.py`，Scene `EquationMeaningLesson`。

**删除** `002方程的意义_animation.py`，旧 Scene `Topic002方程的意义Animation`。

保留方程定义、实例辨别、集合关系及总结；新增 `is_equation()`，直接核对本课六个式子是否含未知数且为等式。

- Gallery topic ID：`a85b511269`；视频：`EquationMeaningLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '002_方程的意义.py' EquationMeaningLesson`。

### 4. 五年级上：解简易方程

课程目录：`小学/五年级/第一学期/第四章-简易方程(一)/004解简易方程/`。

**保留** `004_解简易方程.py`，Scene `SolveEquationLesson`。

**删除** `004解简易方程_animation.py`，旧 Scene `Topic004解简易方程Animation`。

保留完整两步方程演示，新增 `solve_linear_equation()` 基于标准库 `Fraction` 精确检查 `x+8=15` 和 `3x=24`、分数解及无效系数。

- Gallery topic ID：`de012f5986`；视频：`SolveEquationLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '004_解简易方程.py' SolveEquationLesson`。

### 5. 六年级下：平均数、中位数、众数

课程目录：`小学/六年级/第二学期/第四章-统计与概率/002平均数、中位数、众数/`。

**保留** `002_平均数中位数众数.py`，Scene `MeanMedianModeLesson`。

**删除** `002_平均数、中位数、众数.py`，旧 Scene `平均数中位数众数Animation`。

保留成绩展示、排序、均值、众数与极值影响的完整场景，新增 `describe_data()` 精确处理奇偶数量、多众数与无众数输入；实际数据样本用于 Scene 校验。

- Gallery topic ID：`c989d22f18`；视频：`MeanMedianModeLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '002_平均数中位数众数.py' MeanMedianModeLesson`。

### 6. 六年级下：可能性（概率初步）

课程目录：`小学/六年级/第二学期/第四章-统计与概率/003可能性(概率的初步)/`。

**保留** `003_可能性.py`，Scene `ProbabilityIntroLesson`。

**删除** `003_可能性(概率的初步).py`，旧 Scene `可能性概率的初步Animation`。

保留定性可能性、硬币和骰子等完整案例；新增 `probability_from_equal_outcomes()` 用精确分数检查结果，并将画面公式限定为等可能结果。

- Gallery topic ID：`c01d77a5f9`；视频：`ProbabilityIntroLesson_finish.mp4`（不变）。
- 新渲染命令：`manim -pql '003_可能性.py' ProbabilityIntroLesson`。

## 文件数与审核队列

- 第三批结束时小学 Python 269 个，多 Python 知识点目录 45 个；本批删掉 6 个冗余独立 Scene，第四批后分别为 **263 个**和 **39 个**。
- 多源码影子映射现在是 39 个目录：15 项静态核对，24 项待人工复核；删掉的六课已成为“唯一教学源码”，不再出现在多源码映射中。
- 第二、三批的历史快照是历史记录，不能用来推断当前文件仍存在。详情见 [最新审核清单](primary-scene-review-queue.md)。

## 回归与验收边界

```bash
python -m unittest tests.test_primary_scene_deduplication_batch4 -v
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
python tools/legacy_contract.py --expect-count 534
python tools/audit_catalog.py --skip-file-check
```

测试范围涵盖 6 个知识点各只有一个直接 Scene、删除源文件不存在、Gallery 精确 ID/视频路径、代数简写、方程识别与求解、统计量、等可能条件下的概率、三类线的端点和延伸性质。真实 Manim 渲染与现有成片逐帧比对仍需在具备字体、LaTeX、FFmpeg 的环境完成。
