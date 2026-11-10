# 小学第七批：四门六年级课程单 Scene 治理

> 第七批在第六批工作分支上提交；保留与历史 MP4 名称相对应的 Scene 类及 `_animation.py` 文件，删除同课另一个独立教学 Python。**没有删除、重新编码或重新生成任何视频。**

## 审核与处理原则

- 检查课程 `description.json`、`storyboard.md` 与两套 Python 的实际教学内容，不以文件大小判断哪套是完整课程。
- 一元一次不等式、圆的认识、有理数的意义：原 `_animation.py` 只有“正在学习……”之类通用模板，先把数学示例、定义、图形和真实分镜写进保留文件，再删除旧短版。
- 整数与整除：原竖屏 `_animation.py` 已是完整的等分与余数教学，保留其分镜并补数学验证，不做无意义的整文件重写。
- 9:16 输出配置和顶部作者标识继续保留；旧视频 ID、文件和路径不变，但历史视频未重渲染。

## 四门课旧文件到新文件的映射

### 1. 一元一次不等式的解法

目录：`小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/004一元一次不等式的解法/`。

- **保留并优化**：`004一元一次不等式的解法_animation.py`，Scene `Topic004一元一次不等式的解法Animation`。
- **删除**：`004_一元一次不等式的解法.py`，旧 Scene `一元一次不等式的解法Animation`。

用 2x+3>7 推出 x>2，说明空心圆和向右箭头；用 -2x+3>7 推出 x<-2 强调负系数反向，并展示非严格不等式端点逻辑。新增 `solve_linear_inequality` 精确有理数模型。

- Gallery ID：`50da4a7d82`。Gallery 原本引用 `_animation.py`，无需切换。
- 当前渲染入口（在该目录执行）：`manim -pql '004一元一次不等式的解法_animation.py' Topic004一元一次不等式的解法Animation`。

### 2. 整数与整除

目录：`小学/六年级/第一学期/第一章-数的整除/001整数与整除/`。

- **保留并优化**：`001整数与整除_animation.py`，Scene `Topic001整数与整除Animation`。
- **删除**：`001_整数与整除.py`，旧 Scene `整数与整除Animation`。

竖屏版本本就包含 12 个点平均分 3 组、13 个点余 1 的真实课程；保留旧教学场景，新增 `integer_division` 处理正负整数商、余数和零除数边界，添加顶部作者标识。

- Gallery ID：`0f6a97a71a`。Gallery 原本引用 `_animation.py`，无需切换。
- 当前渲染入口（在该目录执行）：`manim -pql '001整数与整除_animation.py' Topic001整数与整除Animation`。

### 3. 圆的认识

目录：`小学/六年级/第一学期/第四章-圆和扇形/001圆的认识/`。

- **保留并优化**：`001圆的认识_animation.py`，Scene `Topic001圆的认识Animation`。
- **删除**：`001_圆的认识.py`，旧 Scene `圆的认识Animation`。

将通用模板重写成圆规定点定长旋转、圆心和半径、直径 d=2r、若干对称轴示范与总结。新增 `circle_measurements` 精确有理数关系。

- Gallery ID：`df4bbd48d1`。Gallery 原先 `pyFile` 指向删除的短预览，现精确切换到完整 Scene，旧 MP4 名称和路径不变。
- 当前渲染入口（在该目录执行）：`manim -pql '001圆的认识_animation.py' Topic001圆的认识Animation`。

### 4. 有理数的意义

目录：`小学/六年级/第一学期/第五章-有理数/001有理数的意义/`。

- **保留并优化**：`001有理数的意义_animation.py`，Scene `Topic001有理数的意义Animation`。
- **删除**：`001_有理数的意义.py`，旧 Scene `有理数的意义Animation`。

将通用模板重写成相反意义的正负数、整数/分数/0 分类、有限小数 0.125=1/8、循环小数 0.(3)=1/3。新增 `rational_fraction` 和 `pure_repeating_decimal` 精确化分数。

- Gallery ID：`982929f902`。Gallery 原本引用 `_animation.py`，无需切换。
- 当前渲染入口（在该目录执行）：`manim -pql '001有理数的意义_animation.py' Topic001有理数的意义Animation`。

## 稳定性和库存

- 本批删除 4 个冗余独立教学 Scene，小学 Python 数量从第五批后 259、第六批后 254，进一步降为 **250**；相对原始 273 共累计删除 23 个。
- 多 Python 文件知识点目录由 30 减至 **26**，其中 15 项静态审核、11 项待进一步核对。
- 原 Gallery **534** 条课程、四课历史 `id`、`videoFile`、`hasVideo` 保持不变。仅《圆的认识》原 `pyFile` 被删除，替换为保留的 `001圆的认识_animation.py` 并同步模块 docstring。
- 新增 `tests/test_primary_scene_deduplication_batch7.py`：唯一源码和 Scene、纯数学 AST 函数、画廊兼容与输入边界测试。

## 验证与限制

```bash
python -m unittest tests.test_primary_scene_deduplication_batch7 -v
python -m tools.primary_scene_shadow --require-complete --output /tmp/primary-scene-shadow.json
python tools/legacy_contract.py --expect-count 534
```

上述属于源码静态、数学及历史索引契约验证。**未对四课执行真实 Manim 低清渲染、字幕检查和 MP4 逐帧比对**。历史 MP4 仍可能包含旧模板画面，因此不能把源码修复直接称为视频修复。
