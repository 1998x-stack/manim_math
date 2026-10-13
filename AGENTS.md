# Repository guidance for AI coding agents

Read `README.md`, `docs/README.md`, and `docs/architecture/manimgx-migration.md` first. This is a ManimGX math-education content repository, not a generic Python package. For task-specific work, load the appropriate `SKILL.md` in `.codex/skills/`, `.opencode/skills/`, or `.claude/skills/`; canonical content is in `skills/source/`.

## Runtime contract

- Target Python is 3.13+.
- Production animation code uses `manimgx`, not Manim Community Edition.
- New code should prefer `import manimgx as m`; migrated legacy scenes may temporarily use `from manimgx import *`.
- Never introduce `from manim import ...`, `import manim`, Cairo/OpenGL renderer internals, or ManimCE media/cache internals.
- Use `manimgx preview <scene.py>` for iterative preview and `manimgx render <scene.py>` for video output.
- Portrait output is 1080×1920. `config.frame_width` is derived by ManimGX; do not assign to it. Shared defaults live in `manim_math_gx.runtime`.
- Chinese/plain text uses ManimGX `Text`. Prefer the repository CJK font policy (`MANIM_MATH_CJK_FONT` / `manim_math_gx.CJK_FONT`) instead of adding new hard-coded platform-only font dependencies.
- `MathTex`/`Tex` are rendered through ManimGX's mitex/Typst path. Treat `TexTemplate`, `\\usepackage`, `\\newcommand`, `\\def`, package-specific environments, and glyph-path-dependent transforms as explicit migration work; do not silently assume TeXLive behavior.
- Run `python tools/manimgx_audit.py .` after migration edits. `tools/manimgx_migrate.py` is only for mechanically safe rewrites; do not extend it to guess ambiguous animation semantics.

## Content and quality rules

Preserve correctness of mathematics and geometric invariants; keep Chinese prose outside `MathTex`; do not silently change the intended Shanghai curriculum; treat the 9×16 frame and watermark as scene-level design constraints; use a low-quality/preview render and inspect representative frames before publishing. Never run `clean_pycache.sh` or broad cleanup as part of a documentation task. Do not rename existing scene or media paths without updating the gallery index, workflow, and explicit old-to-new mapping. Don't change or redistribute original music/media/licensed documents merely to reorganize directories. Never claim a scene was rendered or checked unless that check ran. Prefer small, independently reviewable changes and report commands actually run.

For migration work, preserve function-level mathematical logic unless a ManimGX API difference requires redesign. When redesign is required, separate mathematical/state computation from rendering so the computation remains testable without the renderer. Verify updater/time-dependent behavior at representative timestamps because ManimGX's simulation/timeline semantics are not assumed to be identical to ManimCE.

Entry points: `docs/architecture/architecture.md`, `docs/architecture/manimgx-migration.md`, `docs/architecture/categories.md`, `docs/engineering/scene-workflow.md`, `docs/engineering/quality-gates.md`, `skills/README.md`.
