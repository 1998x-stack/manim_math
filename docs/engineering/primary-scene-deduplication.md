# 小学第三批：重复教学 Scene 合并与旧路径映射

> 这是一次**明确删除**重复教学实现的源码治理记录（基线 main：`b9e09e32eb49662fedd5ac27534e572ceac15013`）。保留的 Scene 已增加无需 Manim 的数学验证；**本批没有重新生成、删除、修改任何 MP4**。现有视频名称与源码类名一致不等于已核实视频内容。

## 选择原则

1. 先核对 `description.json` / `storyboard.md` 的数学目标，保留教学内容覆盖更完整、能够单独维护和测试的实现，而不是机械地比较行数。
2. 保留已发布视频路径与稳定 `topic id`；如果既有 `pyFile` 指向被删除源码，则只修改对应课程的源码入口和随源码同步的说明，不重新分配 ID。
3. 同课除了两套完整实现，还存在未独立发布的短预览时，也删除冗余 Scene，使每个已治理的目录只保留一份可渲染的教学源码。
4. 不删除 `description.json`、`prompt.md`、`storyboard.md`、现有 MP4、纯数学或验证脚本；必要时同步修改测试和 GitHub Actions。
5. **历史的旧 Python 直接渲染命令不再适用**。下表给出明确替换命令；需要旧代码时应从删除前的 Git 历史查看，不能期待旧文件路径继续存在。

## 逐课删除与保留（全路径相对仓库根目录）

### 1. 一年级上册：连加、连减、加减混合

原目录：`小学/一年级/上册/第二章-10以内数的加减法/005连加、连减、加减混合/`

- **保留并更新**：`005_连加连减加减混合.py`，Scene `ConsecutiveOperationsLesson`。
- **删除**：`005_连加、连减、加减混合.py`，原 Scene `连加连减加减混合Animation`。
- 保留版完整展示三个算式 `2+3+1=6`、`5-2-1=2`、`5+2-3=4` 及从左往右运算顺序；将被删除版本的 `calculate_steps` 纯数学函数迁入保留版并保留边界检查。
- Gallery ID：`333882b1af`（不变），`pyFile` 从删除的文件更新到保留的文件；视频仍为 `ConsecutiveOperationsLesson_finish.mp4`。
- 新渲染命令：`manim -pql '005_连加连减加减混合.py' ConsecutiveOperationsLesson`。

### 2. 二年级上册：有余数的除法

原目录：`小学/二年级/上册/第三章-乘法、除法（二）/002有余数的除法/`

- **保留并更新**：`you_shu_shu_de_chu_fa.py`，Scene `YouShuShuDeChuFa`。
- **删除**：`002_有余数的除法.py`，原 Scene `有余数的除法Animation`。
- 两版均演示 13 个苹果平均分给 4 人，每人 3 个、余 1 个；保留实现将引题、分配和关系式拆成多个步骤。新增 `distribution_plan` 将每个苹果的原始编号和剩余物体编号确定为纯 Python 数据，Scene 按这些编号移动对象，且 `verify_geometry.py` 只核查唯一的教学源码。
- Gallery ID：`e5b1915a70`（不变），`pyFile` 原本已经指向保留文件；视频仍为 `YouShuShuDeChuFa_finish.mp4`。
- 新渲染命令：`manim -pql you_shu_shu_de_chu_fa.py YouShuShuDeChuFa`。

### 3. 三年级上册：两位数除以一位数（竖式计算）

原目录：`小学/三年级/上册/第四章-用一位数除/001两位数除以一位数（竖式计算）/`

- **保留并更新**：`001_两位数除以一位数.py`，Scene `TwoDigitDivideOneLesson`。
- **删除完整替代实现**：`001_两位数除以一位数_竖式计算.py`，原 Scene `LongDivisionLesson`。
- **删除冗余预览**：`001_两位数除以一位数（竖式计算）.py`，原 Scene `TwoDigitDivisionPreview`，同目录没有同名预览 MP4。
- 保留实现比另一份完整课程多出 `312 ÷ 3 = 104` 的商中间为 0 的教学例题，符合现有分镜和课程描述；新增 `long_division_trace` 逐位计算部分被除数、商数字和余数，独立测试普通整除、带余数和零占位。
- Gallery ID：`002f488641`（不变），`pyFile` 从被删除的 `LongDivisionLesson` 文件更新到保留文件；视频仍为 `TwoDigitDivideOneLesson_finish.mp4`。
- 新渲染命令：`manim -pql '001_两位数除以一位数.py' TwoDigitDivideOneLesson`。

## Gallery 合同与源码数量变化

- 删除 **4 个**独立 Scene 源文件，保留 **3 个**完整 Scene；受影响三个知识点目前各只有一个可渲染教学 Python 文件（可另有 `verify_geometry.py`）。
- 原小学的 47 个“含多个 Python 文件目录”减至 **45 个**：一年级连加连减和三年级竖式除法已从此类目录消失；二年级有余数除法仍保留 Scene + 验证脚本，故仍按多 Python 目录统计。
- `assets/catalog.json` 仅修改上述 **2 个**知识点的 `pyFile` 与从保留源码抽取的 `docstring`；没有更改任何 `id`、`videoFile`、`hasVideo`、章学期信息或条目数（534）。
- `assets/build_catalog.py` 不用改动：被治理的每个目录现在都只有一个教学 Python 源码，旧的排除 `verify_`/`test_` 规则会找到正确文件。新增测试显式检查这一点。
- `catalog/primary-scene-overrides.json` 移除已不再“多源码”的两课，并将有余数除法标记为静态确认；剩余 45 个目录仍由只读影子映射审查。

## 验收命令与不足

```bash
python -m unittest tests.test_grade_one_operations tests.test_primary_scene_deduplication -v
python '小学/二年级/上册/第三章-乘法、除法（二）/002有余数的除法/verify_geometry.py'
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
python tools/legacy_contract.py --expect-count 534
python tools/audit_catalog.py --skip-file-check
```

- 单元/属性测试主要覆盖加减运算、苹果分配不重复与不遗漏、竖式除法商和余数的 0～9 位规则，以及删除文件不存在的回归。
- GitHub Actions 执行这些静态检查后，才能声称其通过。
- 仍待在具备 Manim、中文字体、LaTeX、FFmpeg 的环境实际渲染三条保留 Scene，并核对开场、算法步骤、边界帧与已发布 MP4 是否对应。本次不声称已完成视频画面验收。
