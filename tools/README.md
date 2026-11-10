# Engineering tools / 工程工具

> **Read-only by default.** 运行前确认工具的输入范围、写入路径和外部依赖。这里的扫描结果只代表对应检查层，不等于已完成 Manim 渲染或数学证明。

| 工具类型 | 当前入口 | 用途 |
| --- | --- | --- |
| 全仓库清单 | [`inventory_repository.py`](inventory_repository.py) | 从 Git 索引列出已追踪文件，统计分类/扩展名/实际检出状态，标记 `.DS_Store`、空 Python 文件和旧 `file://` 文档；只报告、不删除。 |
| 结构与镜像 | [`check_repository.py`](check_repository.py)、[`sync_skills.py`](sync_skills.py) | 检查文档/分类/技能包一致性；技能同步不带 `--check` 时会写入镜像。 |
| 课程及年级 | [`audit_curriculum.py`](audit_curriculum.py)、`audit_grade*.py`、`check_grade5.py` | 各自有独立的扫描范围和误报边界；合并规则前保留原工具行为。 |
| 小学 Python/Scene 全清单 | [`audit_primary_sources.py`](audit_primary_sources.py) | 扫描一年级至六年级及奥数 Python，识别直接 Scene、兼容入口、辅助与测试文件；明确报告稀疏检出遗漏，不导入 Manim。 |
| 小学主 Scene 影子映射 | [`primary_scene_shadow.py`](primary_scene_shadow.py) | 对 47 个多源码知识点使用人工静态审核清单建立只读 Scene 候选；只报告与旧 Gallery 源码/视频的差异。 |\n| 画廊与兼容 | [`audit_catalog.py`](audit_catalog.py)、[`legacy_contract.py`](legacy_contract.py) | 检查索引及旧字段/旧 ID 契约；现行索引生成入口是 `assets/build_catalog.py`，会写 JSON。 |

## 全文件清单（不触碰课程内容）

```bash
python tools/inventory_repository.py --root . --output /tmp/manim-filesystem-inventory.json
python -m unittest discover -s tests -p 'test_inventory_repository.py' -v
```

输出 `summary`、逐文件 `files[]` 与候选问题 `findings[]`，每个发现的 `code` 是复核线索而非自动删除指令。默认使用 `git ls-files`，没有检出的已追踪文件标记为 `NOT_CHECKED_OUT`，`complete_checkout=false` 时禁止声称整个课程已经检查。对非 Git 目录可加 `--include-untracked` 扫描工作目录；忽略 `.git` 和常见缓存/渲染中间目录。将 `--output` 放在仓库外以免反复扫描自己的生成报告。

小学源文件清单（默认报告语法错误，不尝试渲染）：

```bash
python tools/audit_primary_sources.py --output /tmp/manim-primary-sources.json
python -m unittest tests.test_audit_primary_sources -v
```

重复教学 Scene 第三批清理：[旧到新源码完整映射](../docs/engineering/primary-scene-deduplication.md)。该批删除 4 个冗余 Scene；旧基线清单只用于历史比较。

冻结的 273 文件初始基线与分批优化计划：[小学源码清单](../docs/engineering/primary-school-inventory.md)。如果报告的 `summary.complete_checkout` 为 `false`，扫描结果只代表实际检出的部分，不能当作全部课程验收。

\n小学多 Scene 影子检查（只读，不更新既有作品）：\n\n```bash\npython -m tools.primary_scene_shadow --output /tmp/manim-primary-scene-shadow.json\npython -m unittest tests.test_primary_scene_shadow -v\n```\n\n审核队列：[多源码知识点最新审核队列](../docs/engineering/primary-scene-review-queue.md)。只有完整 Python 源码检出时才可使用 `--require-complete` 作为全量检查。\n
详细迁移规则：[文件系统分类治理](../docs/engineering/filesystem-governance.md) · [验收门禁](../docs/engineering/quality-gates.md)。
