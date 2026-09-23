# Reviews / 审查记录

> **Evidence first.** 按审查范围区分历史清单、源码观察与真实运行证据；`needs_review` 不等于已验证缺陷，已有 `.mp4` 不等于可用的发布成片。

| 分类 | 文档 | 使用方法 |
| --- | --- | --- |
| Current reviews | [八年级源码审计](grade8-source-audit.md) | 按其记录的提交版本、扫描范围及证据复核。 |
| Legacy snapshots | [历史清单归档](legacy/README.md) | 查看旧待修复列表及旧成片路径；其中本机 `file://` 链接不是当前构建或发布来源。 |
| Filesystem policy | [文件系统与迁移约定](../engineering/filesystem-governance.md) | 判断何种文件允许清理、需保留兼容入口或禁止自动迁移。 |

若需判断作品是否仍有问题，优先运行对应年级审计、数学测试与真实 Scene 渲染；不要将历史路径列表直接转换成当前删除清单。
