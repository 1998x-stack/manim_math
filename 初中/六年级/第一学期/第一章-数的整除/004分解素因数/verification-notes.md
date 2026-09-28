# 004 分解素因数：数学规格、逐镜追溯与分层验收

## 数学约束

本课将合数写为素数乘积，不计素因数排列顺序，分解唯一。示例 `30=2×3×5`；`60=2×2×3×5=2²×3×5`。短除法每行满足 `被除数=素因数×整数商`，后一行被除数等于上一行整数商，最后商为 1。纯数学模型 `prime_factors(n)` 接受 `n≥2` 的整数，以覆盖素数边界例如 2；教学定义只针对合数。1、0、负整数与非整数不在该分解模型内。

## 场景逐镜追溯

| 方法 | learning_fact → 数据 → 屏上状态 | 渲染后关键帧检查 |
|---|---|---|
| `show_opening` | 将 30 进一步分解为 `2×3×5` | 四组普通分解式与素数乘积可辨 |
| `show_prime_composite` | 素数/合数定义与 1 的例外 | 中文 `Text` 与纯 LaTeX `MathTex` 独立，不压字 |
| `show_definition` | 30 的素因数为 2、3、5，素因数分解不计顺序唯一 | 各素因数标注与数学公式一致，无中文进入默认 MathTex |
| `show_division_30` | 30→15→5→1，左侧素除数 2、3、5 | 每行使用实际 `short_division_steps(30)`，各商与行号准确 |
| `show_division_60` | 60→30→15→5→1，左侧 2、2、3、5，最后写 `2²×3×5` | 4 行连续数据与指数表达吻合；未残留前一镜对象 |
| `show_summary` | 从最小素数尝试、能整除就继续除、商为 1 时结束 | 文字实际加入 Scene，所有对象位于竖屏安全区 |

## 分层验证

| 验证项 | 状态 | 证据与范围 |
|---|---|---|
| math | `pass` | 人工核对 30/60 全部短除法关系；源代码模型测试覆盖整数 2—500 的积、素数性、行间连续性 |
| syntax | `pass` | [本课 CI：Python 编译成功](https://github.com/1998x-stack/manim_math/actions/runs/35836918070/job/107102469310)，源码提交 `359f3c40c9cce45b3e52b32c71d95335b2033244` |
| ast | `not_run`（单独 Skill 审计） | 仍需执行 `audit_scene.py prime_factorization.py --json` 并复核所有告警；数学测试的 AST 提取不等于该审计 |
| unit_tests | `pass` | [本课 CI：因式分解与短除法算术回归成功](https://github.com/1998x-stack/manim_math/actions/runs/35836918070/job/107102469310)，不代表 Manim 渲染 |
| manim_render | `blocked` | 当前执行环境无完整可用 Manim、LaTeX、CJK 字体链路，未产生新视频 |
| frame_review | `not_run` | 待真实渲染后检查每一镜的数字与公式、Mobject 包围盒和 9:16 安全区 |
| ffprobe | `not_run` | 本次没有生成新 MP4；旧视频不作为新源码的媒体验收证据 |
| audio_review | `not_run` | 保留原视频和音轨，未修改 |

源码静态检查、数学测试与真实渲染须分开验收。
