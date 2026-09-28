# 002 因数与倍数：分镜核对与分层验收

## 数学范围

本课讨论正整数 `n>0` 的正因数和正倍数。`a=bq` 且 `a,b,q>0` 时，`b,q` 是 `a` 的正因数，`a` 是 `b,q` 的正倍数。正整数 n 的正因数有限（最小为 1，最大为 n），正倍数 `n,2n,3n,...` 无限（最小为 n）。扩展到整数域，对任意非零整数 b，`0=b×0`，所以 0 是 b 的**整数倍数**，但不是正倍数。不得将“0 是倍数”与“最小正倍数是 n”误写成互相矛盾的同域命题。

## 可追溯的逐镜数学、数据和画面

| 方法 | learning_fact / 实际数据与屏幕对象 | 仍待渲染检查 |
|---|---|---|
| `show_opening` | 12 个圆点；平均分给 2、3、4、6 人的示例 | 圆点为 12 个；不因省略号误导为无限人数 |
| `show_definition` | `a=b×q` 的正整数前提；`12=3×4` | 条件、因数和倍数文字同屏且可读 |
| `show_find_factors` | `1×12`、`2×6`、`3×4` 三幅各 12 块数组；列出六个正因数 | 方块按真实行列排列；标注不压在方块上 |
| `show_find_multiples` | 从数据生成 3、6、9、12、15、18 的数轴 Dot | Dot 对应真实刻度，延伸箭头在安全区 |
| `show_special_rules` | `n=1×n`；`0=b×0` 且 `b≠0`；分隔两个讨论范围 | 正因数、整数倍数文字不交叠 |
| `show_summary` | 正整数的正因数、正倍数的数量与最值；0 的整数域补充 | 最后全部文字真实出现且字幕不出界 |

## 分层验证

| 层级 | 状态 | 证据与限制 |
|---|---|---|
| math | `pass` | 数学定义/例题人工核对，真实 Scene 纯函数提取的数学回归也通过 |
| syntax | `pass` | [本课 CI：两个 Python 文件的 py_compile 成功](https://github.com/1998x-stack/manim_math/actions/runs/35835949695/job/107099328146)，提交 `1369da9ca5280a5392c95ecf1122a5cfd4f4bb93` |
| ast | `pass`（仓库初中通用审计） | [Junior historical gotchas audit](https://github.com/1998x-stack/manim_math/actions/runs/35835949706) 成功；单独执行 Skill `audit_scene.py --json` 仍未记录 |
| unit_tests | `pass` | [本课 CI：Verify actual scene math helpers and scope 成功](https://github.com/1998x-stack/manim_math/actions/runs/35835949695/job/107099328146)；不代表 Scene 已运行 |
| manim_render | `blocked` | 当前容器没有 Manim，无法联网安装；本次 CI 不包含渲染 |
| frame_review | `not_run` | 待真实渲染后检查全部数组、数轴标注、讨论域切换和片尾包围盒 |
| ffprobe | `not_run` | 没有生成新 MP4；旧文件不能证明当前源码已渲染通过 |
| audio_review | `not_run` | 原视频与音轨均未修改 |

> 源码和数学回归通过不等于最终成片质量已验收。
