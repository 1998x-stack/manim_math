# 下一阶段风险登记与潜在优化点

> 2026-09-23 静态阅读主分支 `00421dc42993e21ccdaa807949f60781388a6312` 的局部证据；下列风险不等于已复现的线上故障。测试与环境不完整时，报告 `not_run`，不把怀疑写成运行事实。详细执行依赖见 `docs/architecture/next-iteration-execution-plan.md`。

| 优先级/类型 | 证据及触发条件 | 潜在影响 | 最小修复和回归验收 |
| --- | --- | --- | --- |
| P0 / 前端数据注入 | `assets/index.html` 在 `renderLevelTabs`、`renderSidebar`、`renderChapter`、`renderOverviewChapterList`、`performSearch` 中使用 `innerHTML` 拼接目录来源文本，已有 `escHtml` 仅用于部分位置；video src 同样为模板属性 | 若有人把标记或属性语法写入 catalog 来源字段，可能插入非预期 DOM/脚本；这不是已经证明可远程利用的结论 | 将不可信文本统一送入 `textContent`，URL 使用经校验的 `video.src` 或 DOM attribute setter；恶意尖括号/引号/ampersand/Unicode fixture 在页面与搜索中均只能作为文本展示，旧布局和点击不回退 |
| P0 / 作品匹配错误 | `assets/build_catalog.py` 的 `find_scene_py`、`find_scene_class` 选择首个匹配文件/类，视频 fallback 按 stem 包含关系匹配 | 多源文件/辅助类可能作为 Scene，视频错绑；glob 迭代无明确稳定排序可能导致不同生成内容 | 显式 Scene ID/类名与媒体 manifest；多候选输出 `needs_review`；测试 EulerLineScene/GeometryCalculator、双 Scene、同名/相似名视频、不同目录枚举次序 |
| P0 / 公开媒体可达性 | `.github/workflows/deploy-gallery.yml` 仅上传 `index.html`/`catalog.json`；`index.html` 的 `videoUrl()` 生成 GitHub Raw `main` URL | `hasVideo=true` 只表示扫描时看到本地匹配名称，不代表 Pages 可播放；未来搬迁或版本更新可让旧目录引用漂移 | 建立 URL 与本地媒体状态两个字段；真实 HTTP 测试分辨 200/404/重定向/超时/不可播；旧 URL 有冻结清单，迁移前后逐项确认 |
| P1 / 历史契约对比 | `tools/legacy_contract.py` 排序记录只保留按 ID 的字段；原始 hash 包括格式和统计字段，不能单独定位导航顺序变化 | JSON 美化触发噪声；年级/章节内顺序变化仅有整体 hash 告警；可掩盖真正的导航回归 | 增加独立的顺序向量/semantic hash/raw hash，比较输出区分 formatting、navigation、entity 字段；有明确允许变更清单和 fixture |
| P1 / 部署时序 | 构建后目录可能仍引用随 `main` 更新的视频，页面与视频并未绑定同一提交版本 | 页面快照与视频版本不一致，回溯困难 | Artifact/Publication 保存 revision、sha256 与显式 URL；实测旧 URL 兼容；冻结生产目录与媒体版本后再修改 |
| P1 / 跨课程检查 | `tools/audit_curriculum.py` 只静态识别直接继承候选，同时年级专用的 `audit_grade2/3/4/6.py` 和 `check_grade5.py` 各有独立规则/CLI | 误报与遗漏难横向比较，跨年级重复逻辑易漂移 | 统一诊断结构 `rule_id, location, severity, evidence, status`；保留各年级数学特有规则；固定样例中旧 error 无回退，无法解析的继承标记 needs_review |
| P1 / CI 覆盖 | `.github/workflows/validate-architecture.yml` 稀疏检出仅 `assets/catalog.json` 等，不含课程源文件；`audit_catalog.py --skip-file-check` | 结构 CI 通过易被误读为源文件/视频全部存在并可渲染 | 每一门禁输出扫描范围、文件数、执行环境、时间、证据 URL 与 not_run 项；相关课程源码 PR 使用实际检出文件的独立工作流 |
| P1 / Skills 包结构 | 原 `tools/sync_skills.py` 仅扫描 `*/SKILL.md`，且三个 Agent 的 `prompt-to-scene` 目前只有 SKILL.md | 新增 `references` 或 `scripts` 后镜像丢失却 CI 仍通过 | 本 PR 将整个目录同步并检测缺失、差异、孤儿和符号链接；不得自动执行或删除未知内容；加入临时目录测试 |
| P1 / 数学退化 | `external/euler_line.py` 的 `circumcenter` 对低于固定判别阈值的构型返回重心，`foot_of_perpendicular` 和垂直平分线有零长度除数路径 | 退化三角形可能显示伪造外心、NaN 或无效几何关系 | 先写共线/重合/近退化/极端尺度与非有限坐标测试，返回明确结果/异常；旧 Scene 行为变更必须真实渲染复核 |
| P2 / 文档/分类 | `docs/architecture/architecture.md` 的欧拉线示例域码 `geometry.triangle.centers` 与注册表 `geometry.euclidean.triangle.centers` 不一致 | 人工复制示例会生成不符合 taxonomy 的 v2 数据 | 更正示例，编写引用/代码块检查避免 drift；不能因文档修复直接推断历史主题分类 |

## 审核清单

每个修复 PR 都要标注：直接读取到的风险证据、最小可重复 fixture、影响范围、故障注入预期、实际运行记录、人工待判项、对旧 ID/URL 的差异、回滚命令及未运行项目。GitHub 中 `main` 持续变更，实施前重新检查同一路径是否已被其他 PR 修复，避免重复提交或覆盖并行工作。
