# 第三阶段：课程资产审计、确定性索引与数学场景验证

> 状态：分阶段实施。`tools/audit_curriculum.py` 是第一批只读审计工具；本文件中的其他模块、指标和迁移步骤为待实现任务，不代表仓库已完成全量审计或渲染。

## 1. 当前依据与边界

- 现有 [phase-2 蓝图](../architecture/phase-2-blueprint.md)、[稳定身份 ADR](../architecture/adr-0001-stable-identities.md) 和 `tools/legacy_contract.py` 负责旧 Gallery 身份与索引契约；第三阶段不得另造一套相冲突的 ID 体系。
- 当前 `assets/build_catalog.py` 对课程目录选取第一个候选 `.py`、对独立专题选 AST 中第一个类；视频使用目录枚举及文件名启发式关联。仅依赖文件名或顺序无法保证候选正确。
- 当前结构 CI 仅稀疏检出文档、工具和旧 catalog，不包含小学/初中/高中/external 的完整源码和媒体；测试通过不表示课程内容或成片均合格。
- 历史 `prompt.md`、媒体和 Scene 保持只读，不通过自动去重或批量搬迁修改。课程版本、权利、数学命题与真实 Scene 类名必须有证据，不从文件夹名猜测。

## 2. 工作包与依赖顺序

| 工作包 | 实现内容 | 可检验交付物与停止条件 |
| --- | --- | --- |
| P3.0 只读课程清单（本 PR） | 扫描含 `description.json`、`prompt.md` 或 `storyboard.md` 的目录；解析 JSON、Prompt `<problem>`、直继承 Scene 候选；记录缺失、冲突、多成片及共享模板指纹 | `tools/audit_curriculum.py`、隔离 fixture 测试、确定性 JSON；不读取视频字节、不改变课程文件；真实仓库覆盖率尚待完整检出验证 |
| P3.1 基线与人工待判队列 | 对完整课程树运行审计，存储固定 revision、结果 sha256、缺陷统计及去重候选；将只有 `.py` 而无三类元数据的目录另行盘点；统计每学段实际覆盖率 | 目录全集与审计集合差异清单、错误/警告分离、无未经审核的自动修复；旧 Gallery 的 534 项仍可通过 legacy contract 追溯 |
| P3.2 明确 Scene/媒体关联 | 在不改变旧索引字段的影子模式中引入显式 `scene_class`、`source`、`artifact_id`；AST 发现仅产出候选；遇辅助类、多源码、多 Scene、动态继承、同名媒体时标记 `needs_review` | 针对辅助类排在 Scene 前、多 Scene、无 Scene、别名、损坏源码和多视频的回归测试；无意改变 `id/pyFile/videoFile/hasVideo` 的项目数为零 |
| P3.3 数学与排版验证 | 逐知识点形成数学规格、反例与临界构型；将纯计算与 `Scene.construct()` 解耦；增加边界/退化与中文布局检查 | 有数学断言和证明依据、真实场景低清渲染日志、关键帧人工验收；静态扫描不得宣称证明数学正确 |
| P3.4 安全发布与增量迁移 | 为确定关联的 Scene 建立 build/artifact 清单；对明确许可的媒体做无覆盖后处理；在旧 ID/URL 兼容检查后逐批迁移 | 旧链接与 catalog 兼容测试、ffprobe、发布回退方案；发生 URL/ID 漂移或媒体未授权时停止 |

P3.0 可以先做，P3.2 不得绕过 P3.1 的基线冻结；P3.4 依赖逐条完成 P3.2/P3.3 的验收。`verified`、`rendered`、`published` 必须分别由不同证据支持。

## 3. 如何运行只读审计

在包含完整课程目录的本地检出中：

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/audit_curriculum.py --root . --output /tmp/manim-curriculum-audit.json --fail-on none
python tools/legacy_contract.py --expect-count 534
```

审计结果包括 `records[]`、`issue_counts` 和 `shared_prompt_templates[]`。所有路径相对于 `--root` 输出，文件枚举经排序，便于在相同检出版本中比较。`--fail-on error` 是默认模式：无效 JSON/字段类型或无法读取 Prompt 导致失败；缺文件、内容不匹配、Scene 候选不明确、重复模板归为待审警告，可选 `--fail-on warning` 用于逐批治理。`--output` 仅写显式给出的报告路径；不自动改写知识点 Prompt、JSON、Scene、视频或 Gallery。

**重要局限**：当前扫描只收录具有至少一个三类元数据文件的目录。只有 `.py` 而无三类元数据、课程树之外的 `external/`、Manim 的动态/间接继承及所有真实视频内容，不在本报告的自动确认范围。共享模板指纹只将第一个完整 `<problem>` 标签块替换为占位符；相同指纹表明模板字符串一致，不意味着其余 Prompt 经语义审查可安全删除。

## 4. 检查与发布门禁

1. **静态结构层**：现有稀疏 CI 执行工具 fixture 单测及 legacy catalog 契约；不得把空课程树下的工具返回零错误解释为 534 条课程已审计。
2. **完整内容层**：人工触发或独立工作流完整检出课程源码与小型文本资产，产出真实审计报告和目录全集覆盖统计；避免自动下载全部大视频仅为读取名称。
3. **数学层**：证明条件、定义域和退化处理必须由数学规格或测试确认；数字近似仅作为补充证据。
4. **渲染层**：固定实际 Manim、FFmpeg、字体与系统环境，低清关键帧审查通过后才高质量发布；每个修改 Scene 留下命令和结果。
5. **兼容层**：每次修改索引或目录前对旧索引快照进行逐字段差异比较；无意变更的 legacy ID、路径和已发布 URL 数量必须为零。

## 5. 下一批具体改动目标

- 完善扫描器的导入别名和跨文件继承诊断，但不执行待扫描脚本；抽取只有 `.py` 的候选目录形成覆盖差集。
- 将 `description.json` 的基础结构与课程路径规范转换成版本化 JSON Schema，先软警告历史异常，再对新增作品强约束。
- 为每个知识点引入人工审核的 manifest，记录确切 Scene 类名、对应视频与许可。`assets/build_catalog.py` 在影子模式读取 manifest 并输出对比报告；未经确认时不改变旧 Gallery。
- 对几何专题及小学典型题型各取少量样本，进行数学断言、字幕安全区检查和低清渲染；通过后再扩展到其他年级。
