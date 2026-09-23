# 质量门禁与可追溯验证

| 门禁 | 阶段 | 判据 | 证据 |
| --- | --- | --- | --- |
| 目录 | 文档/Skills | 分类索引可定位新文件、旧路径仍有入口、各 Agent Skills 内容完全一致 | `python tools/sync_skills.py --check`; `python tools/check_repository.py` |
| 语法 | 代码 | `py_compile` 通过；Scene 类名与实际调用一致 | 执行日志 |
| 数学 | 动画 | 前提完整；方程/定理/构型的边界样例正确；误差阈值有依据 | 纯 Python 测试、符号检查、证明引用 |
| 版面 | 动画 | 字幕、点标、公式均在画面内，无关键遮挡，中文字体可读 | 低清渲染、关键帧审核 |
| 渲染 | 视频 | 场景可完整渲染，分辨率、帧率、时长与设计一致 | CLI 日志、ffprobe |
| 发布 | 画廊 | topic/scene 关联完整；旧链接/ID 不意外消失，明确版权与媒体来源 | 新旧 catalog 差异、链接检查 |

`tools/check_repository.py` 只校验此次文档和 Skills 的结构性约束；**不运行 Manim、不验证数学内容、不检测媒体版权**。任何 PR 中不得把结构检查通过说成数学或画质验收。`external/euler_line.py` 的退化三角形行为是单独的风险点，重构计算器时应先写针对退化点的回归测试。

## 推荐本地命令

```bash
python tools/sync_skills.py --check
python tools/check_repository.py
python -m py_compile assets/build_catalog.py
python assets/build_catalog.py
manim -pql external/euler_line.py EulerLineScene
```

完整画质验证需本地渲染环境与人工审核，轻量 CI 不作等价替代。
