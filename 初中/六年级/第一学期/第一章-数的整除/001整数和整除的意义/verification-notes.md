# 001 整数和整除的意义：修复与分层验收

## 数学条件

整数 `a,b` 且 `b≠0` 时，`b|a` 当且仅当存在整数 `q` 使 `a=bq`。均分 12 个方块时，组数 `b>0`、总数 `a≥0`，按 `a=bq+r` 且 `0≤r<b` 解释余数。本课“因数 ≤ 对应倍数”仅指正整数范围。`12÷5` 的整除判断由 `12=5×2+2` 及余数非零给出，不使用带省略号的伪等式。

## 逐镜验收

| 方法 | 数学命题 → 数据 → 屏上状态 | 实际渲染的待验关键帧 |
|---|---|---|
| `show_opening` | 12 个苹果分给 3 人，`12//3==4`，呈现问题 | 中文、署名不被裁剪 |
| `show_concept` | `a,b∈ℤ, b≠0`、`a=bq,q∈ℤ`、`b\mid a` | LaTeX 编译正常，定义和条件同屏 |
| `show_example_divisible` | `3×4=12`；12 个 Square 重排成 3 组，每组 4 个 | 初态/末态数物一一对应，余数 0 正确 |
| `show_example_not_divisible` | `5×2+2=12`；5 组各 2 个 + 剩余 2 个 | 12 个 Square 未丢失或重叠，余数及结论匹配 |
| `show_factor_multiple` | `12=3×4`，限定正整数 | 数值与关系对应，结论条件可见 |
| `show_notation` | `3|12`，`5∤12`，由余数核实 | 整除符号方向、颜色与解释一致 |
| `show_outro` | 定义、余数、正整数因数/倍数范围 | 所有文本在竖屏安全区 |

## 分层验证结果

| 层级 | 状态 | 证据及尚未覆盖的项目 |
|---|---|---|
| math | `pass`（示例与前提） | `12=3×4`、`12=5×2+2`、零除数排除；独立回归亦通过 |
| syntax | `pass` | [GitHub Actions：source/test py_compile 成功](https://github.com/1998x-stack/manim_math/actions/runs/35835924595/job/107099247078)；提交 `fdc6bd67a83b6d9c83e3570070e2dcf5a068d8a1` |
| ast | `pass`（仓库初中源码审计规则） | [Junior historical gotchas audit](https://github.com/1998x-stack/manim_math/actions/runs/35835924543) 成功；专门的 Skill `audit_scene.py --json` 尚未独立运行，不冒充该检查 |
| unit_tests | `pass` | 上述 GitHub Actions 的 `Verify arithmetic and scene source invariants` 步骤成功；这不验证实际画面 |
| manim_render | `blocked` | 当前本地容器无 Manim，且无法联网安装；CI 本项不做渲染 |
| frame_review | `not_run` | 需渲染后检查第一帧、全部分组终态、两种结论、符号与片尾的完整 Mobject 包围盒 |
| ffprobe | `not_run` | 未生成新 MP4；旧视频不可充当修复后视频验收 |
| audio_review | `not_run` | 保留原有视频与音轨，未对其做变更 |

> 静态及数学回归成功不等于真实 Manim 动画或视频已验收。
