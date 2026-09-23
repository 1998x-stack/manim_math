# Commit → Gotchas → TODO → 视频构建：可复现治理流程

本页是跨学段的工程入口；不替代 [`historical-gotchas.md`](historical-gotchas.md)、[`highschool-historical-gotchas-20260923.md`](highschool-historical-gotchas-20260923.md) 或已有年级专项审计。历史提交标题只是**问题线索**，只有核对 diff、当前代码和运行证据后才能判定当前仍有缺陷。历史 MP4 不代表修复后的 Scene 通过验收。

## 1. 历史提交：改过哪些文件、修了什么问题

经核对下列提交的文件列表与 patch，提炼出首批跨学段回归模式：

| 证据提交 | 改动文件 / 修复事实 | 提炼的 gotcha / 对应检查 |
| --- | --- | --- |
| [`c2e74aa`](https://github.com/1998x-stack/manim_math/commit/c2e74aa45674fc20c5f81a4911eb86bd018c169d) | `小学/四年级/第一学期/第三章-数的运算——三位数乘两位数/001笔算乘法(竖式计算)/001_笔算乘法(竖式计算).py`：竖屏配置从 `construct` 移至 Scene 初始化前。 | 相机建立之后设置全局画幅太晚；检查 `config.frame_*`/`pixel_*` 的初始化顺序和最终帧比例（目前需要人工/渲染审查）。 |
| [`bc81f46`](https://github.com/1998x-stack/manim_math/commit/bc81f46c1ffbcb27ea54287716750fe379c28edf) | 高一的 `001_任意角与弧度制.py`、`any_angle_trigonometry.py` 和正弦课程源码：修正角度标签、含中文 Tex、以及 `self.play(self.play(...))` 的嵌套动画。 | `UNICODE_IN_TEX`、`CHINESE_IN_TEX`、`NESTED_PLAY`；三角函数周期还需检验 `|ω|` 与 `ω=0` 边界。 |
| [`634340a`](https://github.com/1998x-stack/manim_math/commit/634340ac0d19d10dbdc49b28e272c6254248539e) | `tools/repair_highschool_gotchas.py`：纠正自动修复器把 AST UTF-8 字节列偏移当作 Unicode 字符偏移的错误。 | 需要改写源码时，不允许直接以 `col_offset` 切割 Unicode 字符串；本次扫描器只报告行号，不自动批量改源码。 |

此外，原始七条 Manim API/LaTeX 故障见 [`references/Error.md`](references/Error.md)：H01/H06 中文 Tex、H02 角度符号、H03 Sector 参数、H04 TeX 分组、H05 Arrow scale 参数、H07 Rectangle 圆角参数；新增 AST 扫描器覆盖可静态判断的模式，TeX 自定义模板和动画画面仍须人工审查。其它教育内容改动不应仅凭 `fix` 提交名称就被当成已证实的同类故障。

### 获取整个可见历史及文件修改频次

```bash
# 在完整本地仓库中运行；只读 Git 历史，不修改课程文件。
python tools/commit_gotchas.py history --output docs/engineering/commit-gotchas.generated.json
# 可先限制历史做快速试跑：
python tools/commit_gotchas.py history --max-commits 20 --output /tmp/commit-sample.json
```

输出包含扫描的非合并提交数、是否为完整历史、疑似修复提交的 SHA / message / GitHub 链接 / 实际改动文件列表，以及按修改次数排序的文件清单。**完整历史要求非浅克隆且所有相关 refs 在本地可见**；`--all` 不等于 GitHub 中所有已删除分支或不可达提交。生成文件是机器索引，不应当把 message 自动转成经过验证的根因。

## 2. 单个 Scene：依赖 → 渲染 → 原子覆盖 → 清理 → 音乐

首次安装前自行在相应 OS 安装 FFmpeg、Cairo/Pango、TeX 和课程所需中文字体。脚本不执行 `sudo`、`apt-get`、`brew` 或 `--break-system-packages`；Manim Python 依赖仅安装在仓库内 `.venv`。首次使用 `--install`，后续如已安装可省略：

```bash
python tools/build_video.py external/euler_line.py EulerLineScene --install --quality l
# 仅显式指定的素材会参与合成；确认拥有音乐使用权：
python tools/build_video.py external/euler_line.py EulerLineScene \
  --music files/Away.mp3 --quality h --force
# 自定义输出路径：
python tools/build_video.py external/euler_line.py EulerLineScene \
  --output external/euler_line_finish.mp4 --music files/Away.mp3 --force
```

脚本先对源码执行 AST 解析并确认 Scene 类名，接着使用临时 `--media_dir` 执行 Manim，确认唯一且非空的 `built.mp4`；选用背景音乐时执行 `ffmpeg`，循环音轨并将背景音乐作为输出音轨（**不保留原视频音轨**）。全部成功后才通过同一目录内的 `os.replace` 提交目标 MP4。`--force` 是覆盖已存在成片的显式授权；失败时旧文件保持原样，临时渲染文件自动清理。未指定音乐时仅输出视频；此流水线不遍历整个仓库、不自动修改画廊索引、不删除历史媒体。

生产发布前还应验证分辨率、时长、是否出现音画截断、中文字形、布局与数学正确性。`--quality h` 是高清质量预设，具体画幅由 Scene 自身配置决定；脚本不会假定每个课程均为同一比例。`--install` 需要可用网络与构建依赖；课程有额外第三方库时应在 `.venv` 中单独安装。当前 CI 不安装 Manim、FFmpeg 或音乐素材，也**不**声称已渲染任何视频。

## 3. 分批扫描，生成且更新 TODO.json

```bash
# 扫描小学、初中、高中和独立专题的全部 Python 源码：
python tools/commit_gotchas.py scan --output TODO.json
# 大仓库推荐按 100 个文件逐批处理；batch 从 0 开始：
python tools/commit_gotchas.py scan --batch 0 --batch-size 100 --output TODO.json
python tools/commit_gotchas.py scan --batch 1 --batch-size 100 --output TODO.json
# ...直到 batch=total_batches-1；每次运行追加/重扫指定批次。
```

`TODO.json` 的 `total_python_files`、`scanned_file_count`、`total_batches` 和 `scanned_files` 提供覆盖证据；未扫文件不能标记已通过。每个命中包含路径、行号、规则、P0/P1/P2、源码 SHA-256、参考的 Hxx、状态，以及静态/数学/渲染/视觉四种验收阶段。命中默认 `needs_review`，不能把 AST 提示直接写成已确定 Bug。人工确认后可将 `status` 维护为 `verified`（已审查处理）或 `false_positive`，并在 `checks` 中标记已实际运行的阶段；仅当源文件 SHA-256 未变化时，重扫才沿用旧状态，防止修改代码后沿用过时验收。对当前批次中不再出现的旧命中，扫描器会移除该候选；需要永久记录的历史事实应保留在本文或对应年级审计文档。

P0 语法错误属于确定故障；P1 的 API 或动画用法需要核对实际 Manim 版本；P2 的 TeX 中文和角度问题还要考虑自定义 CJK 模板及字体，不能自动全局替换。教育数学内容还需逐课人工检查相应定义域、几何坐标、概率条件和教材准确性；静态规则无法宣称覆盖全部数学错误。

每批流程为：**生成候选 → 查看对应历史 diff 与当前行 → 修源码并添加数学/AST 回归用例 → 重扫 → 低清渲染和视觉检查 → 标注各项验证证据 → 按年级提交小型 PR**。不同年级既有审计器可继续运行；新增扫描器是横向风险索引，不替代原有检查。

## 4. CI 验收与当前完成范围

`.github/workflows/commit-gotchas-video.yml` 在 PR 中运行 AST/流水线单测，对 sparse-checkout 的课程源码执行第 0 批扫描，校验 JSON 结构并上传 `gotchas-first-batch-todo` 工件。由于仓库已有大量历史待复核风险，该工作流**不会因 P2 候选数量非零而失败**；已确认的修复必须通过对应年级专项 CI 和实际渲染才能关闭。仓库根目录最初的 `TODO.json` 只是未扫描的计划基线；真实的第一批命中以 CI 工件或本地扫描后的结果为准，不能将初始空清单解读为全仓库零缺陷。
