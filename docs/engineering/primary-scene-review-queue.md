# 小学多源码 Scene：第八批后复核队列

> 第三至第八批累计去除 33 份重复教学源码。本清单确认 Python 主入口，但不表示旧视频已经重渲染。

## 统计

- 小学 Python **240** 个（最初 273 个），多源码目录 **16** 个（最初 47 个）。
- **16 项源码入口均已静态核对，0 项 needs-review**。其中包含模型/测试文件和 run_path 历史兼容入口，不能进一步按数量盲删。
- 仍有 **6 项**历史 Gallery 源码与影子选择不同，需要视频核对；**2 项**多源码课程尚未收入历史 Gallery。
- 第八批对最后 11 项作出分类：10 项独立 Scene 去重，1 项《单位“1”》保留兼容入口。

## 尚有多个 Python 的 16 个知识点

| # | 知识点 | 同目录 Python 文件 | 当前 Gallery 源文件 | 静态主 Scene | 状态 |
|---:|---|---|---|---|---|
| 1 | `二年级 上册 / 0017、8、9的乘法口诀` | `001_7、8、9的乘法口诀.py` · `verify_geometry.py` · `you_shu_shu_de_chu_fa.py` | `you_shu_shu_de_chu_fa.py` | 已核对：`001_7、8、9的乘法口诀.py` · `MultiplyTableAnimation` | **请核对历史视频** |
| 2 | `二年级 上册 / 002有余数的除法` | `verify_geometry.py` · `you_shu_shu_de_chu_fa.py` | `you_shu_shu_de_chu_fa.py` | 已核对：`you_shu_shu_de_chu_fa.py` · `YouShuShuDeChuFa` | — |
| 3 | `二年级 下册 / 001统计（条形统计图二）` | `001_统计条形统计图二.py` · `001_统计（条形统计图二）.py` | `001_统计条形统计图二.py` | 已核对：`001_统计条形统计图二.py` · `BarChartTwoLesson` | — |
| 4 | `三年级 上册 / 001整十、整百数乘一位数` | `001_整十、整百数乘一位数.py` · `001_整十整百数乘一位数.py` | `001_整十整百数乘一位数.py` | 已核对：`001_整十整百数乘一位数.py` · `RoundNumberMultiplyLesson` | — |
| 5 | `三年级 上册 / 002两位数乘一位数（竖式计算）` | `002_两位数乘一位数.py` · `002_两位数乘一位数（竖式计算）.py` | `002_两位数乘一位数（竖式计算）.py` | 已核对：`002_两位数乘一位数.py` · `TwoDigitTimeOneLesson` | **请核对历史视频** |
| 6 | `三年级 上册 / 001年、月、日` | `001_年、月、日.py` · `001_年月日.py` | `001_年、月、日.py` | 已核对：`001_年月日.py` · `YearMonthDay` | **请核对历史视频** |
| 7 | `三年级 下册 / 001两位数乘两位数（竖式计算）` | `001_两位数乘两位数.py` · `001_两位数乘两位数（竖式计算）.py` | `001_两位数乘两位数.py` | 已核对：`001_两位数乘两位数.py` · `TwoDigitMultiplyLesson` | — |
| 8 | `三年级 下册 / 002两位数除两、三位数（试商）` | `002_两位数除两、三位数（试商）.py` · `002_两位数除两三位数.py` | `002_两位数除两、三位数（试商）.py` | 已核对：`002_两位数除两三位数.py` · `TwoDigitDivisionLesson` | **请核对历史视频** |
| 9 | `三年级 下册 / 001认识面积` | `001_认识面积.py` · `001认识面积_animation.py` | `001_认识面积.py` | 已核对：`001认识面积_animation.py` · `Topic001认识面积Animation` | **请核对历史视频** |
| 10 | `四年级 第一学期 / 001笔算乘法(竖式计算)` | `001_笔算乘法(竖式计算).py` · `001笔算乘法_竖式计算__animation.py` | `001笔算乘法_竖式计算__animation.py` | 已核对：`001_笔算乘法(竖式计算).py` · `ColumnMultiplicationLesson` | **请核对历史视频** |
| 11 | `五年级 第二学期 / 001单位'1'` | `001_单位'1'.py` · `001单位_1__animation.py` | `001单位_1__animation.py` | 已核对：`001_单位'1'.py` · `UnitOneLesson` | 旧入口通过 run_path 继承，保留 |
| 12 | `五年级 第一学期 / 001平均数的意义` | `001_平均数的意义.py` · `001平均数的意义_animation.py` | `001_平均数的意义.py` | 已核对：`001_平均数的意义.py` · `AverageMeaningLesson` | — |
| 13 | `五年级 第一学期 / 003等式的性质` | `003_等式的性质.py` · `003等式的性质_animation.py` | `003_等式的性质.py` | 已核对：`003_等式的性质.py` · `EqualityPropertyLesson` | — |
| 14 | `五年级 第一学期 / 005等面积法-同底等高` | `area_model.py` · `lesson.py` · `test_area_model.py` | `未收录` | 已核对：`lesson.py` · `EqualAreaMovingApex` | Gallery 未收录 |
| 15 | `五年级 第一学期 / 006等面积法-梯形蝴蝶模型` | `area_model.py` · `lesson.py` · `test_area_model.py` | `未收录` | 已核对：`lesson.py` · `TrapezoidButterflyArea` | Gallery 未收录 |
| 16 | `一年级 上册 / 001加法的初步认识` | `addition_intro.py` · `verify_geometry.py` | `addition_intro.py` | 已核对：`addition_intro.py` · `AdditionIntro` | — |

## 后续媒体门禁

运行 `python -m tools.primary_scene_shadow --require-complete` 和 `python tools/legacy_contract.py --expect-count 534`，之后逐课做真实 Manim 渲染、中文字体、关键帧与现存 MP4 来源核对。静态源码去重不应被表述为已经完成视频验收。
