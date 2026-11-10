# 画廊数据契约与分类示例

当前兼容版 `assets/catalog.json` 的入口是 `levels[] → grades[] → semesters[] → chapters[] → topics[]`；旧 topic 常含 `id, number, name, docstring, pyFile, videoFile, hasVideo`。`videoFile=null` 时 `hasVideo=false`，旧路径与旧 ID 在兼容期原样保留。工具执行前保存基线，更新后按 ID 逐字段对比；已存在的视频不必然在稀疏检出中出现。

## 正交分类

课程位置（学段、年级、学期、教材、章节）与数学域（算术、几何、函数、统计等）分开管理；同一 Topic 可以属于多个课程定位与领域，未知信息留空。`external/` 不自动意味着高中内容。一个主题与 Scene/媒体不是一一对应；同目录多个 Python 文件、多个视频不能以第一个为权威。

## 静态失败样例

- 重复旧 `id`：报告冲突，不覆盖。
- `hasVideo=true` 且 `videoFile=null`：结构错误。
- 仅通过改名重新计算 ID：兼容性回归，应维护旧 ID 映射。
- 多个视频名都能模糊匹配：保留旧记录并标 `needs_review`，不根据第一个文件自动更新。

`check_catalog.py` 只读校验 JSON 结构；它不验证远程 URL/作品版权/数学真假，不能自行迁移 schema。
