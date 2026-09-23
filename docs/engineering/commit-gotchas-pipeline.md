# Commit → Gotchas → TODO → 视频：历史归因与验收手册

本页连接已有 [`historical-gotchas.md`](historical-gotchas.md)、[`highschool-historical-gotchas-20260923.md`](highschool-historical-gotchas-20260923.md)、`references/Error.md` 与逐年级审计器，不取代它们。**Git 提交标题表明修改意图，不等于已核实根因；AST 命中不等于经视频验证的错误；测试通过不等于课程画面已验收。**

## 1. 历史 commits → 真实修改文件 → gotchas

在完整检出的 Git 历史中运行：

```bash
python tools/commit_gotchas.py history --output docs/engineering/commit-gotchas.generated.json
# 只扫描前 20 个 commit 做快速试跑：
python tools/commit_gotchas.py history --max-commits 20 --output /tmp/commit-sample.json
```

机器索引包含每条疑似修复 commit 的 SHA、message、链接、Git diff 实际涉及的文件路径，以及所有可达非合并提交的文件触达频次。2026-09-23 的 [完整历史 CI](https://github.com/1998x-stack/manim_math/actions/runs/35828312845) 处理 316 个可达非合并 commit，筛出 113 个修复关键词提交及 4994 个不同的历史变动路径。统计口径是 CI 当时可达的提交与历史文件路径，**不包含已删除分支上不可达的对象**，也不表示 4994 个当前源文件有故障。历史 JSON 位于该 CI 的 `historical-gotchas-and-full-todo` 工件。

经查看实际 diff，可复用的证据包括：

| 实际提交 | 修改内容 | 应归纳的 gotcha / 检查 |
| --- | --- | --- |
| [`c2e74aa`](https://github.com/1998x-stack/manim_math/commit/c2e74aa45674fc20c5f81a4911eb86bd018c169d) | 小学四年级三位数乘两位数竖屏课件：将全局画幅配置从 `construct` 内移至 Scene 初始化前。 | 画幅应在相机初始化之前配置；最终比例需实际渲染核验。 |
| [`bc81f46`](https://github.com/1998x-stack/manim_math/commit/bc81f46c1ffbcb27ea54287716750fe379c28edf) | 高一任意角、三角函数相关源码修正了角度标签、Tex 中文和 `self.play(self.play(...))`。 | `UNICODE_IN_TEX`、`CHINESE_IN_TEX`、`NESTED_PLAY`；另应检查三角函数周期定义域与 `ω=0`。 |
| [`634340a`](https://github.com/1998x-stack/manim_math/commit/634340ac0d19d10dbdc49b28e272c6254248539e) | `tools/repair_highschool_gotchas.py` 修正 AST UTF-8 **字节列偏移**被误作 Unicode 字符列偏移的历史问题。 | 改写含中文源码时不可直接用 AST `col_offset` 切割 Unicode `str`；新扫描器只报告源文件和行号，不批量改写源码。 |

源自 `references/Error.md` 的其它稳定规则：H01/H06 默认 TeX 中文、H02 Unicode 角度符号、H03 `Sector` 的不支持参数、H04 TeX 组、H05 Arrow `scale` 兼容、H07 Rectangle `corner_radius`。**显式设置 `TexTemplateLibrary.ctex` 的课件不能直接认定为默认 TeX 中文故障**；应结合当前模板、字体和实际渲染检查。教材数学内容不能仅靠 AST 判定正误。

## 2. 单 Scene 构建：Python 依赖 → Manim → FFmpeg → 原子成片

`tools/build_video.py` 仅在仓库 `.venv` 创建 Python 环境并安装 Manim，**系统依赖 FFmpeg、Cairo/Pango、LaTeX、中文字体需按操作系统单独安装**，不会执行未经确认的 `sudo`/`brew`/`apt-get` 或覆盖系统 Python。新增加的 [.github/workflows/video-build-smoke.yml](../../.github/workflows/video-build-smoke.yml) 提供 Ubuntu 临时 runner 的系统安装与**真实短场景**渲染/合成集成检查，不对课程数学、中文 LaTeX 或正式成片质量背书。

```bash
# 首次：创建仓库本地 venv，渲染一个明确的 Scene：
python tools/build_video.py external/euler_line.py EulerLineScene --install --quality l
# 后续：指定具有使用权的音乐；仅本次临时过程文件会被清理：
python tools/build_video.py external/euler_line.py EulerLineScene \
  --music files/Away.mp3 --quality h --force
# 可显式选择输出文件：
python tools/build_video.py external/euler_line.py EulerLineScene \
  --output external/euler_line_finish.mp4 --music files/Away.mp3 --force
```

脚本先 AST 校验源码与 Scene 类，再在独立临时 `--media_dir` 渲染；确认只得到一个非空 `built.mp4` 后，可将显式选定的背景音乐循环、用 FFmpeg 合成音轨。**当前合成策略是用背景音乐替换原视频音轨，不是将两条音轨混音**。全部完成才以同一卷内 `os.replace` 提交目标 MP4。已有目标文件必须明确指定 `--force`，构建失败会保留原视频；不会扫描或删除仓库里其它 MP4。`--quality h` 选择高画质预设，最终分辨率、竖屏比例仍取决于 Scene 配置。发布前需人工核对音轨权利、画幅、音画时长、LaTeX、中文字体、布局与数学准确性。

## 3. TODO.json：按批次扫描，按证据修复并保持覆盖

```bash
# 重新扫描当前 4 个课程目录的全部 Python 源码：
python tools/commit_gotchas.py scan --output TODO.json
# 或保留已有批次结果，按 100 文件逐批增量处理：
python tools/commit_gotchas.py scan --batch 0 --batch-size 100 --output TODO.json
python tools/commit_gotchas.py scan --batch 1 --batch-size 100 --output TODO.json
# ...一直执行到 total_batches - 1。
```

`total_python_files`/`scanned_file_count` 和 `scanned_files` 每个源文件的 SHA-256 是覆盖凭据。每条 AST 候选都有稳定 ID、具体位置、规则、优先级、历史线索、源文件哈希、处理状态与静态/数学/渲染/视觉四种**独立**检查状态。初次命中为 `needs_review`，核实后才可标为 `verified` 或记录有明确根据的 `false_positive`；源码 SHA 变化时，旧状态不能自动复用。已消失的命中会在重扫中移除，已经修复的历史事实须独立记录在 [2026-09-23 全量修复文档](full-audit-findings-20260923.md)。

首轮扫描覆盖 613/613 个文件共 7 批，命中 8 个候选；5 个对应课件源码已修复，3 个为显式 ctex 模板的静态规则例外。仓库当前跟踪的 [`TODO.json`](../../TODO.json) 已包含**修复后**的 613 个文件 SHA-256、余下三条例外和 `render: pending`/`visual: pending`，不应把 `outstanding: 0` 误读为全部课程视频已验收。

按批修复步骤是：对照对应历史 diff 与源码定位 → 依据课程公式和画面确认缺陷 → 修源码与添加回归 → 重扫并比对哈希 → 实际低清渲染与关键帧审查 → 逐项记录数学、渲染和视觉结果 → 审核后发布。

## 4. CI 门槛与已知局限

[`commit-gotchas-video.yml`](../../.github/workflows/commit-gotchas-video.yml) 使用完整可达 Git 历史、以批次扫描全部课程 Python 文件，执行构建器/扫描器/修复课件的依赖轻量回归；若出现 P0 语法错误，会将本 CI 标为失败。非 P0 的规则命中仍需逐项人工核查，避免无证据地批量修源码。它不安装完整 TeX 字体环境，不执行 613 个 Scene 的视频渲染。

[`video-build-smoke.yml`](../../.github/workflows/video-build-smoke.yml) 单独在 Linux 临时 runner 安装 Manim/FFmpeg 依赖，渲染**短测试 Scene**，合成测试生成的音频，并用 ffprobe 验证视频与音频流；是否通过以对应 GitHub Actions 运行结果为准。即便此项通过，也不意味着五个修复课件已经实际渲染或高分辨率成片检查完成。临时具备 `contents:write` 的一次性自动修复工作流已在生成 `TODO.json` 后删除；普通 PR 测试仅需 `contents:read`。
