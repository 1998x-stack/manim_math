# Category 分类规则

**Category 是检索标签，不等于文件夹。** 保持课程目录作为现有主导航；跨学段几何、工具和实验作品可按概念/领域检索。字段使用稳定机器值 + 中文显示名；允许单值和多值区分。

| 维度 | 字段 | 推荐值/约定 |
| --- | --- | --- |
| 学段 | `level` | `primary`, `junior`, `senior`, `cross-level`；按实际学习目标标注 |
| 教材 | `curriculum` | 教材版本、学制、年级、学期、章节、知识点编码；缺失时 `null`，禁止猜测 |
| 数学领域 | `domains[]` | `arithmetic`, `algebra`, `geometry.euclidean`, `geometry.analytic`, `functions`, `statistics`, `probability`, `number-theory`, `calculus`, `mathematical-thinking` |
| 表现形式 | `visualizations[]` | `construction`, `proof`, `graph`, `transformation`, `simulation`, `worked-example` |
| 内容资产 | `kind` | `lesson`, `exploration`, `reference`, `template`, `tool`, `media` |
| 生产状态 | `status` | `planned`, `draft`, `verified`, `rendered`, `published`, `legacy-imported`；状态不等同于数学真伪 |
| 媒体 | `media` | `source`, `raw-video`, `final-video`, `audio`, `image`, `publication` |

**规则**：一份动画可以含多个领域/知识点；不能仅靠文件名自动确定教材版本、知识范围或证明类型；原始媒体与二次剪辑通过 artifact 关联而不是放在同一个语义类别。独立专题 `external/` 按数学分类归档，但不能自动认定为高中内容。

## 物理目录建议

```text
content/curriculum/{level}/{grade}/{semester}/{chapter}/{topic-id}/
content/explorations/{domain}/{topic-id}/
math/{domain}/                   # 可复用的定义、证明和验证
manim_components/                # 只放经过抽取和测试的绘图组件
production/{scene-id}/           # 渲染配置/清单，不直接跟踪缓存
assets/                          # 当前画廊入口，暂时保留
```

这是一套**未来布局**；现存 `小学/初中/高中/external` 仍为有效代码入口。不要在引入 manifest 与兼容索引之前实施整库搬迁。
