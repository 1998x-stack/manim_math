# 动画分镜｜全等与相似的区别

- 场景：`congruence_similarity_visual.py::CongruenceSimilarityVisual`，作为既有全等课件的独立拓展；AA 相似为衔接知识，勿把本片等同于原目录的课程要求。
- 七年级全等概念 + 后续相似概念预告；9:16 竖屏。中国字用 `Text`，英文缩写、边角公式用 `MathTex`。

## 数学规格
- 同一三角形经旋转、平移后的像与原三角形全等：三对对应边分别相等，三对对应角分别相等。
- 全等判定只在已建立对应点且三角形非退化时应用：SSS；SAS（强调 **夹角**）；ASA（强调 **夹边**）。这里只展示判定名称与条件，刚体运动画面本身并非三个判定定理的完整证明。
- 一组三角形再施以以中心为基准的 `k=1.35` 等比放大：对应角保持相等、对应边比均为 1.35，故相似但不全等。AA 相似指两个对应内角相等即可；AA **不能**单独推出全等。缩放中心不改变比例。
- 反例：`k≠1` 的相似三角形，角均对应相等却有不相等的边；SSA 不列为一般三角形的全等判定。

## 分镜
| 镜头 | learning_fact | 对象与动作 | check |
|---|---|---|---|
| 01 | 颜色一致的三条边确定对应关系 | 左右 `colored_triangle()` 的每条边分别是黄、绿、橙；`Rotate(right, π/3)` | 左右三条对应边长相等，刚体转动未变形 |
| 02 | 全等的 SSS/SAS/ASA 条件 | 中文 `valid_tests=VGroup(Text(...))` 出现；保留左右原对象 | 不将 SAS 写成任意两边一角；无默认 LaTeX 中文 |
| 03 | 相似 ≠ 全等，AA 属于相似判定 | `right.animate.scale(1.35, about_point=RIGHT*1.65)`；展示相似边比公式 | 三组边比确为 1.35，角度保持；右侧对象无越界 |

## 校验
- 纯数学：`python -m unittest discover -s external/triangle-core -p test_triangle_core_math.py -v`；验证刚体运动保长、缩放统一边比且保持角。
- 语法与 AST：`python -m py_compile congruence_similarity_visual.py` 和 Skill `scripts/audit_scene.py`。
- 低清渲染：`manim -pql congruence_similarity_visual.py CongruenceSimilarityVisual`，审核两图旋转/放大后包围盒、对应颜色、字幕与公式。
- 本分支尚无本片新 MP4；`manim_render` / `frame_review` / `ffprobe` / `audio_review` = `not_run`。
