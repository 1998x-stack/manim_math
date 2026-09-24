# 002 同类项与合并同类项：修复后分镜

入口：`like_terms.py::LikeTerms`；七年级第一学期，第九章整式，竖屏 9:16。原始 MP4/音轨不覆盖，源码修改不等于新视频已经渲染。

## 数学定义及本课数据

- 同类项必须含有相同的字母，而且每个相同字母的指数分别相同；仅仅总次数相同不够。系数可异，常数项互为同类项。`3x²y` 与 `-5x²y` 同类，`3x²y` 与 `3xy²` 不同类。
- 合并同类项，系数求代数和，字母和其指数不变；系数为零时该类项消失，而不是把指数变零。`3x²y+(-5x²y)=-2x²y`。
- 综合例题：`3x²y-5x²y+2xy+4x²y-xy` 中，`x²y` 类的系数为 `3-5+4=2`，`xy` 类的系数为 `2-1=1`，最终得到 `2x²y+xy`。

## 分镜 → 可见状态 → 验收

| 场景 | 可见状态与对象关系 | 数学检查 / 关键帧 |
|---|---|---|
| `show_opening` | 原式完整显示，并提出按字母、指数分组的问题 | 原式宽度经 `fit` 裁定；所有符号可读且未被截断 |
| `show_definition` | 将 `3x²y` 和 `-5x²y` 的字母部分分别作为 MathTex 独立参数进行框选 | 两框均围住同一个字母部分 `x²y`，不依赖 TeX 字形索引；系数不同不影响类别 |
| `show_examples` | 五组例子分行：三组正例与两组反例，中文字“与”单独使用 Text | 例子顺序和 `tests/test_grade7_like_terms_lesson.py` 的签名判别一致，不能把总次数相同误当作同类项 |
| `show_rule` | 三个蓝色正块和五个红色负块表示同种 `x²y`，配对抵消后保留两个红色块 | 屏幕方块数量分别为 3、5、2；公式系数 `3+(-5)=-2` 与图形符号一致；替换后维护对象引用 |
| `show_full_example` | 原式按 `x²y` 类、`xy` 类逐组呈现；每项负号保留在独立 MathTex 对象上 | 三个 `x²y` 项、两个 `xy` 项；`3-5+4=2`，`2-1=1`，最终为 `2x²y+xy` |
| `show_outro` | 三条可读结论和综合例题答案 | 不再整体旋转有文字的对象；最后淡出已添加对象与署名 |

## 生命周期 / 安全区

署名 y=6.7；当前镜头存在的对象由 `clear_content` 淡出，防止误淡出从未添加的临时对象。第 4 镜的 `negatives` 经 `ReplacementTransform` 替换为 `remaining`；之后只清理场景中实际存在的对象。式子通过 `fit(..., width=7.5)` 控制安全宽度，其他标签按最终渲染包围盒检查。第 3 镜五行中心为 3.8、1.85、-0.1、-2.05、-4.0，下一行说明向下 0.72，避免同一行文字遮挡。

## 验收状态区分

纯数学：`python -m unittest tests.test_grade7_like_terms_lesson -v`（或者 `python -m unittest discover -s tests -p 'test_grade7_like_terms_lesson.py' -v`）。
静态：`python -m py_compile like_terms.py`，以及 `.opencode/skills/manim-video-production/scripts/audit_scene.py`。
媒体验收：须在有 Manim/TeX/CJK 字体的环境实际运行 `manim -pql like_terms.py LikeTerms`，检查各镜边界、负号与块数量；生成新视频后再用 `ffprobe` 探测其规格。未执行的验收项必须标为 `not_run`，不能用现有 MP4 代替。
