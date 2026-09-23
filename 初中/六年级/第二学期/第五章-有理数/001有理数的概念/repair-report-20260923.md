# 001 有理数的概念｜修复与验收记录（2026-09-23）

## 范围

原 Scene：`RationalNumbers`；只修复本课 Python 与对应分镜，新增回归测试。`prompt.md`、`description.json`、现有 MP4、音轨均未改动。根据 `.opencode/skills/manim-video-production/SKILL.md` 按层报告，不把历史视频当作修复后的视频。

## 当前源码所见问题与处理

| 类型 | 原源码表现 | 修复 |
|---|---|---|
| observed_error（数学/图像不对应） | 数轴上 `0.5` 标在 1.5、`-0.8` 标在 -1.8；另有 `-1/3` 使用近似点值却没有说明 | 示例数值与 `line.n2p(value)` 同源，使用准确的 -3、-1、0、1/2、3，分数用循环/标准分式符号 |
| potential_risk（对象生命周期/布局） | 判断勾叉在数字平移前定位；正数判断位置可能落在判定框之外 | 采用 2×2 固定卡片，数字和答案均根据对应卡片中心定位；每镜构造一次 VGroup，淡出时引用原对象 |
| observed_error（表述） | 用未定义的 `\text{fractions}` 表示分数集合，容易与有理数整体定义混淆 | 使用 `\mathbb{Q}=\{p/q\mid p,q\in\mathbb{Z},q\ne0\}`，示例给出整数与有限小数的整数比 |
| potential_risk（9:16 安全区） | 原标签与大字号文本可能靠边，旧视频无法说明当前源码状态 | 顶部品牌中心 y=6.7、标题 y=5.65；实际包围盒仍需渲染抽帧检查 |

## 验证分层

| 类别 | 状态 | 依据/下一步 |
|---|---|---|
| math | pass（已列出的示例与分类） | Python `fractions.Fraction` 核算；数学论证仍以分镜中的给定条件为准 |
| syntax | pass（本地副本） | `python -m py_compile rational_numbers.py` |
| ast | pass（专项检查） | `python -m unittest discover -s . -p test_rational_numbers.py -v` 检查数轴标签、七镜入口、中文公式混排和嵌套 `self.play` |
| unit_tests | pass（本地副本） | 5 tests，均通过；在 CI 重跑以核实实际 PR 文件 |
| skill audit_scene.py | not_run | 本地未取得 skill 审计脚本运行副本；需在仓库 CI 环境执行，逐条处理警告 |
| manim_render | blocked | 当前执行环境未安装 Manim；运行 `manim -ql rational_numbers.py RationalNumbers` |
| frame_review | blocked | 需检查全部镜头实际 Mobject 包围盒、中文字体、分数上下间距、分类树连线、不同镜头切换及动态状态 |
| ffprobe | not_run | 未产生新 MP4；完成正式渲染后核对 1080×1920、时长、帧率与轨道 |
| audio_review | not_run | 本次未修改原视频或原音频；任何新音轨须另行授权与验收 |

**结论**：已提交源码与专项测试；尚未取得真实渲染与媒体层的 pass，不能认定本课已经完成视频验收，也不能据此把整个学期标记为已修复。