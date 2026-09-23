# 004 分解素因数：数学规格、逐镜追溯与分层验收

## 数学约束

本课将大于 1 的合数写为素数乘积，不计素因数排列顺序，分解唯一。示例 `30=2×3×5`；`60=2×2×3×5=2²×3×5`。短除法每行必须满足 `被除数=素因数×整数商`，后一行被除数等于上一行整数商，最后商为 1。纯数学模型 `prime_factors(n)` 接受 `n≥2` 的整数（便于验证素数边界，例如 2），1、0、负整数与非整数不在该分解模型内；教学定义只针对合数。

## 场景逐镜追溯

| 方法 | learning_fact → 数据 → 屏上状态 | 渲染后关键帧检查 |
|---|---|---|
| `show_opening` | 将 30 进一步分解为 `2×3×5` | 四组普通分解式与素数乘积可辨 |
| `show_prime_composite` | 素数/合数定义与 1 的例外 | 中文 `Text` 与纯 LaTeX `MathTex` 独立，不压字 |
| `show_definition` | 30 的素因数为 2、3、5，素因数分解不计顺序唯一 | 各素因数标注与数学公式一致，无中文进入默认 MathTex |
| `show_division_30` | 30→15→5→1，左侧素除数 2、3、5 | 每行使用实际 `short_division_steps(30)`，各商与行号准确 |
| `show_division_60` | 60→30→15→5→1，左侧 2、2、3、5，最后写 `2²×3×5` | 4 行连续数据与指数表达吻合；未残留前一镜对象 |
| `show_summary` | 最小素数开始尝试、用素数继续除、商为 1 时结束 | 文字真正加入 Scene，所有对象位于竖屏安全区 |

## 验证记录

| 验证项 | 状态 | 证据与范围 |
|---|---|---|
| math | `pass`（人工复核核心例子） | 30/60 各行整数关系与乘积正确；专项数学测试仍需运行 |
| syntax | `not_run` | 需执行 `python -m py_compile prime_factorization.py verify_prime_factorization.py` |
| ast | `not_run` | 需执行 Skill `audit_scene.py prime_factorization.py --json` 并审查结果 |
| unit_tests | `not_run` | `python verify_prime_factorization.py` 将从实际源码 AST 提取模型运行，不代替 Manim 渲染 |
| manim_render | `blocked` | 当前执行环境未提供可用 Manim/TeX/CJK 字体的完整渲染链路 |
| frame_review | `not_run` | 待真实渲染后逐镜检查标签、数值、所有 Mobject 包围盒与 9:16 安全区 |
| ffprobe | `not_run` | 本次尚未生成新 MP4，仓库旧文件不可充当新源码的媒体验收 |
| audio_review | `not_run` | 保留已有 MP4 及原始音轨，不替换也不清理 |

源码静态检查、数学测试与真实渲染必须分别验收。
