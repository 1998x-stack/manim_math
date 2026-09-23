# Repository guidance for AI coding agents

Read `README.md` and `docs/README.md` first. This is a Manim Community Edition math-education content repository, not a generic Python package. For task-specific work, load the appropriate `SKILL.md` in `.codex/skills/`, `.opencode/skills/`, or `.claude/skills/`; canonical content is in `skills/source/`.

Rules: preserve correctness of mathematics and geometric invariants; keep Chinese prose outside `MathTex`; do not silently change the intended Shanghai curriculum; treat the 9×16 frame and watermark as scene-level design constraints; use a low-quality render and inspect representative frames before publishing. Never run `clean_pycache.sh` or broad cleanup as part of a documentation task. Do not rename existing scene or media paths without updating the gallery index, workflow, and explicit old-to-new mapping. Don't change or redistribute original music/media/licensed documents merely to reorganize directories. Never claim a scene was rendered or checked unless that check ran. Prefer small, independently reviewable changes and report commands actually run.

Entry points: `docs/architecture/architecture.md`, `docs/architecture/categories.md`, `docs/engineering/scene-workflow.md`, `docs/engineering/quality-gates.md`, `skills/README.md`.
