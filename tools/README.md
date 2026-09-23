# Engineering tools / 工程工具

> **Read-only by default.** 运行前确认输入范围、输出路径和外部依赖；扫描结果不等于 Manim 渲染或数学证明通过。

| 类型 | 当前入口 | 用途 |
| --- | --- | --- |
| 全仓库清单 | [`inventory_repository.py`](inventory_repository.py) | 根据 Git 索引统计分类/扩展名/检出状态，记录缓存、空源码与历史本机链接候选；只报告。 |
| 历史引用审计 | [`audit_resource_references.py`](audit_resource_references.py) | 只读列出 `files/` 混合资源、旧 Skill、根 Shell、空 `.py` 的字面引用和待审状态；不依据无匹配结果删除文件。 |
| 历史 Shell | [`legacy/`](legacy/README.md) | 保存两个原样归档的扫描脚本；根目录和 `小学/a.sh` 旧入口保留转发。执行前检查可能被覆盖的输出文件。 |
| 结构与镜像 | [`check_repository.py`](check_repository.py)、[`sync_skills.py`](sync_skills.py) | 检查文档/分类/技能一致性；技能同步不带 `--check` 时会写入镜像。 |
| 课程及年级 | [`audit_curriculum.py`](audit_curriculum.py)、`audit_grade*.py`、`check_grade5.py` | 独立的课程/源码规则与检查范围；规则收敛前保留现有行为。 |
| 画廊与兼容 | [`audit_catalog.py`](audit_catalog.py)、[`legacy_contract.py`](legacy_contract.py) | 检查索引及历史 ID/字段；生产索引生成器 `assets/build_catalog.py` 会写 JSON。 |

## 全量只读清单与引用候选

```bash
python tools/inventory_repository.py --root . --output /tmp/manim-filesystem-inventory.json
python tools/audit_resource_references.py --root . --output /tmp/manim-resource-references.json
python -m unittest discover -s tests -p 'test_inventory_repository.py' -v
python -m unittest discover -s tests -p 'test_audit_resource_references.py' -v
```

默认使用 `git ls-files`；稀疏检出中未取得的文件标记为未扫描，不可视作删除或确认无引用。可使用 `--include-untracked` 审计隔离测试目录。`--output` 建议写到仓库外，避免将报告再次纳入扫描。引用命中只是文本线索，不能直接证明运行依赖。

详细说明：[第一批分类规则](../docs/engineering/filesystem-governance.md) · [第二批执行记录](../docs/engineering/filesystem-batch2.md) · [验收门禁](../docs/engineering/quality-gates.md)。
