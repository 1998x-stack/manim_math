---
name: safe-repository-migration
description: 安全整理和迁移课程源码、Prompt、文档、视频与画廊关联；涉及批量重命名、目录移动、旧 URL、稳定 ID 或清理文件时使用。
---

# Safe repository migration｜可回退迁移

本技能不要求外部 Skill；按需阅读 `references/migration-checklist.md`。`scripts/check_moves.py` 只读检查旧→新路径 JSON 是否重复、越界及目标覆盖风险；不执行移动，也不依赖第三方包。

## 迁移步骤

1. 保存基线：列明每个原路径、类型、哈希、引用/相对路径、索引 ID、网页 URL、文件权限和资源许可；未知的公开链接不得猜测为无人使用。
2. 拆分文档迁移与场景/媒体迁移。对不可替代的历史 MP4、音频及 PDF，先制定保留策略，不将目录整洁作为删除依据。
3. 用 `references/migration-checklist.md` 创建明确的逐项映射 JSON，运行 `python scripts/check_moves.py path/to/moves.json --root .`；该脚本只能发现部分路径冲突，不能证实线上 URL 可用。
4. 源码/媒体迁移前先保证旧 ID 与旧 URL 的兼容入口，并修复索引扫描范围、工作流触发器、导入与素材相对路径；未准备好时仅提交设计，不做文件移动。
5. 小批量实施并核对旧新 catalog、语法/数学/渲染/页面差异；每批保留独立回退提交。任何异常立即停止扩大范围，记录差异，不自动覆盖。

## 完成定义

旧入口可追溯，显式 ID/Scene/媒体关联没有无意变化，实际检查与未检查项明确分开。禁止未经批准执行清理脚本、大规模文件移动、破坏性 `git reset` 或整库重编码。
