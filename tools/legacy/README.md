# Legacy scripts · 历史维护脚本

此目录保存两份脚本的原始 Git blob。旧入口 `../../find_finish_mp4.sh` 和 `../../小学/a.sh` 是保留参数及调用时工作目录的兼容转发器。

| 文件 | 用途 | 运行前检查 |
| --- | --- | --- |
| `find_finish_mp4.sh` | 搜索历史 `_finish.mp4`，生成绝对本机链接清单 | 会覆盖目标根目录的 `finish_mp4_paths.md`。 |
| `primary-pending-prompts.sh` | 根据 Prompt、视频和 Python 行数的旧规则查找候选 | 会覆盖目标根目录的 `todo_prompts.md`；结果不是数学或渲染验收。 |

这两个脚本是历史工具而非当前 CI 入口，不在本 PR 中执行。`concat_mp4.sh`、`clean_pycache.sh` 会修改或删除本地文件，仍保留原路径，需单独审查后才能迁移或运行。新审计优先使用只读 `tools/inventory_repository.py` 与 `tools/audit_resource_references.py`。
