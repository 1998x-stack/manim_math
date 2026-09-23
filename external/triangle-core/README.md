# 三角形核心知识点｜五集可视化专题

按 `.claude/skills/manim-video-production/SKILL.md` 的数学规格 → 分镜 → 独立 Scene → 数学回归 → 静态扫描 → 真实预览 → 成片探测分层推进。新增文件均独立于原有课程脚本、Prompt 和历史视频；**不将旧 MP4 视为本次新作品**。

| 集 | 核心问题与教学产出 | 课程位置 / 实际 Scene |
|---|---|---|
| 01 | 内角和 180°、过顶点作平行线的证明、外角定理 | [七年级内角和新增场景](../../初中/七年级/第二学期/第十四章-三角形/003三角形的内角和定理/triangle_angle_visual.py)：`TriangleAngleSumVisual`；[分镜](../../初中/七年级/第二学期/第十四章-三角形/003三角形的内角和定理/triangle_angle_visual_storyboard.md) |
| 02 | 三边严格不等式、两圆交点、等号退化 | [七年级三边关系新增场景](../../初中/七年级/第二学期/第十四章-三角形/002三角形的三边关系/triangle_inequality_visual.py)：`TriangleInequalityVisual`；[分镜](../../初中/七年级/第二学期/第十四章-三角形/002三角形的三边关系/triangle_inequality_visual_storyboard.md) |
| 03 | 全等刚体运动、SSS/SAS/ASA 条件与 AA 相似的区别 | [七年级全等概念拓展场景](../../初中/七年级/第二学期/第十四章-三角形/005全等三角形的概念与性质/congruence_similarity_visual.py)：`CongruenceSimilarityVisual`；[分镜](../../初中/七年级/第二学期/第十四章-三角形/005全等三角形的概念与性质/congruence_similarity_visual_storyboard.md) |
| 04 | 重心/外心/垂心/内心、四心位置变化、欧拉线 | [独立几何专题](four-centers/four_centers_visual.py)：`FourCentersVisual`；[分镜](four-centers/four_centers_storyboard.md) |
| 05 | 面积法/弦长的正弦定理、辅助高的余弦定理 | [高一解斜三角形新增场景](../../高中/高一/第二学期/第五章-三角比/008解斜三角形/triangle_laws_visual.py)：`TriangleLawsVisual`；[分镜](../../高中/高一/第二学期/第五章-三角比/008解斜三角形/triangle_laws_visual_storyboard.md) |

## 独立数学回归与静态检查

```bash
# 从仓库根目录执行；无须 Manim，但需要 numpy。
python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v

# GitHub PR 上的 .github/workflows/triangle-core-visualizations.yml：
# - 对五个新 Scene 编译语法；检查 Scene 类、MathTex 中文和嵌套 play；
# - 调用本 Skill 的 scripts/audit_scene.py（ERROR 视为失败，WARN 另需复核）；
# - 通过 AST 单独加载源码中的 upper_vertex、triangle_centers 真正执行数学边界回归。
```

## 真实预览/成片的后续门槛

在安装了 Manim Community Edition、FFmpeg、LaTeX、中文字体及 NumPy 的机器上，分别进入五个场景所在目录，运行：

```bash
manim -pql triangle_angle_visual.py TriangleAngleSumVisual
manim -pql triangle_inequality_visual.py TriangleInequalityVisual
manim -pql congruence_similarity_visual.py CongruenceSimilarityVisual
manim -pql four_centers_visual.py FourCentersVisual
manim -pql triangle_laws_visual.py TriangleLawsVisual
```

以上五条命令**各自在相应源码目录执行**，不是在仓库根目录直接执行。首帧、变化中帧、退化/钝角构型、证明公式、结尾和完整 Mobject 包围盒均需逐镜复核；若选择 `--resolution 1080,1920` 正式渲染，应核实 Manim 宽高参数次序，并对输出用 `ffprobe` 检查像素、时长、帧率及已有声轨。仅在音乐版权/配音权利明确且人工试听通过后输出独立后期文件；不得静默覆盖原视频或音乐。

## 当前实证状态

源码与分镜：已写入工作分支。数学回归/语法/AST：测试与 CI 工作流已创建，具体是否通过以对应 Actions 日志为准；**不将文件存在视为测试通过**。Manim 渲染、关键帧人工复核、正式新 MP4、媒体与音轨检查：`not_run`。最终发布前应逐项补上证据。
