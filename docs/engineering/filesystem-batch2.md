# Batch 02 / 历史资源与脚本归位

> 基线：PR #32 的 `78dfe78bb5d5a8587eb1bc9b70784969a1e59460`。这是**叠加在第一批上的独立变更**；课程/画廊未整体重组。禁止把只读审计当作无引用证明。

## 已实施路径映射

| 原入口 | 新的维护位置 | 兼容行为 |
| --- | --- | --- |
| `find_finish_mp4.sh` | `tools/legacy/find_finish_mp4.sh` | 原入口保留 Shell 转发器；新文件沿用旧 blob，调用方工作目录和参数不变。 |
| `小学/a.sh` | `tools/legacy/primary-pending-prompts.sh` | 原入口保留 Shell 转发器；新文件沿用旧 blob，调用方工作目录和参数不变。 |

这两份脚本**都会覆盖扫描目录内的输出 Markdown**，不在 CI 运行；重组没有改变这项历史行为，也没有执行它们。运行前检查已有 `finish_mp4_paths.md`、`todo_prompts.md`。相对路径转发器不能替代所有外部调用者的路径兼容验证，但保留了仓库内原入口。

## 实际分类与暂缓清理

| 资源组 | 观察 | 当前处理 |
| --- | --- | --- |
| `files/grade*.json`、`files/chuzhong.json` | 年级/学段课程数据，可能被 `files/*_arch_create.py` 或外部命令读取 | REVIEW：先做字符串引用、脚本行为和 JSON schema 审计；不移动。 |
| `files/*_arch_create.py`、`files/check_syntax.py` | 历史生成与检查脚本 | REVIEW：确认当前调用方/写入路径之后再决定迁移；不运行。 |
| `files/*.mp3`、`files/*.pdf`、`videos/*.mp4` | 历史媒体及资料；`concat_mp4.sh` 明确使用 `files/Away.mp3` | BLOCK：本批不移动、不删除、不重新编码。 |
| `skills/*.skill` | 与 `skills/source/*/SKILL.md` 不同的历史 Skill 归档 | REVIEW：需要确认内容和外部导入方式，不删除。 |
| `external/ceva_theorem.py` | Git 文件树显示为零字节 | REVIEW：可能是占位文件；没有用途和调用方证据前不能删除。 |
| `concat_mp4.sh`、`clean_pycache.sh`、`install_manim.sh` | 全树媒体处理/清理与跨平台安装入口 | REVIEW/BLOCK：这批保留原路径和内容，避免意外改变调用方及副作用。 |

## 可复现的引用审计

```bash
python tools/inventory_repository.py --root . --output /tmp/manim-filesystem-inventory.json
python tools/audit_resource_references.py --root . --output /tmp/manim-resource-references.json
python -m unittest discover -s tests -p 'test_audit_resource_references.py' -v
```

`audit_resource_references.py` 默认列出 Git 已追踪文件，扫描已检出的 UTF-8 小型文本中对候选文件的字面路径引用或唯一文件名提及。输出含 `scope`、`revision`、`complete_checkout`、`not_scanned_or_missing`、`candidates` 和逐项 `needs_review`。不匹配可能来自动态拼接、绝对路径、二进制文件或未检出的工作树；匹配也可能只是文档或测试字符串。**任何候选的自动删除/自动搬迁均不在本工具范围。**

## 验收与后续步骤

本批只移动两个历史脚本的维护副本，保留旧入口，不碰课程 Scene、画廊 ID、MP4/MP3/PDF。归档副本复用旧 Git blob SHA；新工具的隔离测试与 GitHub CI 通过后再考虑合并。下一批先在完整检出上生成清单，逐项人工核查 `files/` 数据的真实消费者、历史 Skill 的 import 使用、空 `.py` 的用途，再按已验证的依赖关系分批迁移。
