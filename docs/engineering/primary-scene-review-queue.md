# 小学多源码 Scene：第七批去重后的审核队列

> 由最初 47 个含多个 Python 文件的知识点目录起，第三批减少 2 个、第四批减少 6 个、第五批减少 4 个、第六批减少 5 个、第七批再减少 4 个，当前剩 **26 个**。该清单用于源码静态审核，不代表真实 Manim 渲染或视频匹配通过。

## 本次统计

- 小学 Python 文件 **250 个**，相对原始 273 个基线累计删除 **23 份**重复教学 Scene。
- 多 Python 知识点 **26 个**：**15** 个源码入口已静态核对，**11** 个待复核。
- 仍有 **6** 项影子建议源码与现行 Gallery `pyFile` 不同，需要后续媒体核验；不自动切换。
- 仍有 **2** 个多源码目录未被历史 Gallery 收录，后续单独处理。
- 本批涵盖《整数与整除》《圆的认识》《有理数的意义》《一元一次不等式解法》，三课将模板替换为真实分镜，一课保留完整旧课并增强数学验证；详见 [第七批去重记录](primary-scene-deduplication-batch7.md)。

## 运行方式

```bash
python -m unittest tests.test_primary_scene_deduplication_batch7 -v
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
```

## 尚有多个 Python 的 26 个知识点

| # | 知识点 | 同目录 Python 文件 | 当前 Gallery 源文件 | 静态主 Scene | 状态 |
|---:|---|---|---|---|---|
| 1 | `二年级 上册 / 001解决问题策略` | `001_解决问题策略.py` · `001解决问题策略_animation.py` | `001解决问题策略_animation.py` | 待复核 | — |
| 2 | `二年级 上册 / 0017、8、9的乘法口诀` | `001_7、8、9的乘法口诀.py` · `verify_geometry.py` · `you_shu_shu_de_chu_fa.py` | `you_shu_shu_de_chu_fa.py` | 已核对：`001_7、8、9的乘法口诀.py` · `MultiplyTableAnimation` | **请核对历史视频** |
| 3 | `二年级 上册 / 002有余数的除法` | `verify_geometry.py` · `you_shu_shu_de_chu_fa.py` | `you_shu_shu_de_chu_fa.py` | 已核对：`you_shu_shu_de_chu_fa.py` · `YouShuShuDeChuFa` | — |
| 4 | `二年级 上册 / 001认识角` | `001_认识角.py` · `001认识角_animation.py` | `001认识角_animation.py` | 待复核 | — |
| 5 | `二年级 上册 / 001东南西北` | `001_东南西北.py` · `001东南西北_animation.py` | `001_东南西北.py` | 待复核 | — |
| 6 | `二年级 下册 / 001统计（条形统计图二）` | `001_统计条形统计图二.py` · `001_统计（条形统计图二）.py` | `001_统计条形统计图二.py` | 已核对：`001_统计条形统计图二.py` · `BarChartTwoLesson` | — |
| 7 | `二年级 下册 / 001运算顺序` | `001_运算顺序.py` · `001运算顺序_animation.py` | `001运算顺序_animation.py` | 待复核 | — |
| 8 | `三年级 上册 / 001整十、整百数乘一位数` | `001_整十、整百数乘一位数.py` · `001_整十整百数乘一位数.py` | `001_整十整百数乘一位数.py` | 已核对：`001_整十整百数乘一位数.py` · `RoundNumberMultiplyLesson` | — |
| 9 | `三年级 上册 / 002两位数乘一位数（竖式计算）` | `002_两位数乘一位数.py` · `002_两位数乘一位数（竖式计算）.py` | `002_两位数乘一位数（竖式计算）.py` | 已核对：`002_两位数乘一位数.py` · `TwoDigitTimeOneLesson` | **请核对历史视频** |
| 10 | `三年级 上册 / 001年、月、日` | `001_年、月、日.py` · `001_年月日.py` | `001_年、月、日.py` | 已核对：`001_年月日.py` · `YearMonthDay` | **请核对历史视频** |
| 11 | `三年级 上册 / 001认识周长` | `001_认识周长.py` · `001认识周长_animation.py` | `001_认识周长.py` | 待复核 | — |
| 12 | `三年级 下册 / 001两位数乘两位数（竖式计算）` | `001_两位数乘两位数.py` · `001_两位数乘两位数（竖式计算）.py` | `001_两位数乘两位数.py` | 已核对：`001_两位数乘两位数.py` · `TwoDigitMultiplyLesson` | — |
| 13 | `三年级 下册 / 002两位数除两、三位数（试商）` | `002_两位数除两、三位数（试商）.py` · `002_两位数除两三位数.py` | `002_两位数除两、三位数（试商）.py` | 已核对：`002_两位数除两三位数.py` · `TwoDigitDivisionLesson` | **请核对历史视频** |
| 14 | `三年级 下册 / 001认识面积` | `001_认识面积.py` · `001认识面积_animation.py` | `001_认识面积.py` | 已核对：`001认识面积_animation.py` · `Topic001认识面积Animation` | **请核对历史视频** |
| 15 | `三年级 下册 / 001复式条形统计图` | `001_复式条形统计图.py` · `001复式条形统计图_animation.py` | `001_复式条形统计图.py` | 待复核 | — |
| 16 | `四年级 第二学期 / 001单式折线统计图` | `001_单式折线统计图.py` · `001单式折线统计图_animation.py` | `001单式折线统计图_animation.py` | 待复核 | — |
| 17 | `四年级 第一学期 / 001笔算乘法(竖式计算)` | `001_笔算乘法(竖式计算).py` · `001笔算乘法_竖式计算__animation.py` | `001笔算乘法_竖式计算__animation.py` | 已核对：`001_笔算乘法(竖式计算).py` · `ColumnMultiplicationLesson` | **请核对历史视频** |
| 18 | `四年级 第一学期 / 002笔算除法(试商与调商)` | `002_笔算除法(试商与调商).py` · `002_笔算除法.py` | `002_笔算除法.py` | 待复核 | — |
| 19 | `五年级 第二学期 / 001单位'1'` | `001_单位'1'.py` · `001单位_1__animation.py` | `001单位_1__animation.py` | 待复核 | — |
| 20 | `五年级 第一学期 / 001平均数的意义` | `001_平均数的意义.py` · `001平均数的意义_animation.py` | `001_平均数的意义.py` | 已核对：`001_平均数的意义.py` · `AverageMeaningLesson` | — |
| 21 | `五年级 第一学期 / 003等式的性质` | `003_等式的性质.py` · `003等式的性质_animation.py` | `003_等式的性质.py` | 已核对：`003_等式的性质.py` · `EqualityPropertyLesson` | — |
| 22 | `五年级 第一学期 / 005等面积法-同底等高` | `area_model.py` · `lesson.py` · `test_area_model.py` | `未收录` | 已核对：`lesson.py` · `EqualAreaMovingApex` | Gallery 未收录 |
| 23 | `五年级 第一学期 / 006等面积法-梯形蝴蝶模型` | `area_model.py` · `lesson.py` · `test_area_model.py` | `未收录` | 已核对：`lesson.py` · `TrapezoidButterflyArea` | Gallery 未收录 |
| 24 | `一年级 上册 / 001加法的初步认识` | `addition_intro.py` · `verify_geometry.py` | `addition_intro.py` | 已核对：`addition_intro.py` · `AdditionIntro` | — |
| 25 | `一年级 上册 / 001长方体` | `001_长方体.py` · `001长方体_animation.py` | `001_长方体.py` | 待复核 | — |
| 26 | `一年级 下册 / 001认识平面图形` | `001_认识平面图形.py` · `001认识平面图形_animation.py` | `001认识平面图形_animation.py` | 待复核 | — |

## 后续重点

- 继续核查剩余 11 个待复核知识点是否真为两套可渲染独立 Scene。不要把纯模型、测试或历史兼容入口误当重复课程删除。
- 对模板占位先完善真实数学分镜再删冗余版本，不能仅因旧文件名与 MP4 一致就断言视频已有新内容。
- 逐课执行真实 Manim 低清渲染、中文字体和关键帧检查，静态审计通过不等同于画面验收。
