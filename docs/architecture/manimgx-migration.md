# ManimGX migration architecture

Status: **v1 migration branch** (`feat/manimgx-migration-v1`).

## Goal

Replace the repository's Manim Community Edition runtime with ManimGX while preserving
its mathematical content, vertical-video geometry, Chinese typography, validation
pipeline, reusable agents/skills, and existing scene-level abstractions.

This is not a global search/replace.  ManimGX deliberately implements a typed subset of
ManimCE and changes renderer, configuration, typesetting, CLI and some animation
semantics.

## Target runtime

- Python: 3.13+
- ManimGX: 0.1.1 (pinned during migration)
- Scene imports: `from manimgx import *` or preferably `import manimgx as m` for new code
- Preview: `manimgx preview path/to/scene.py`
- Render: `manimgx render path/to/scene.py`
- Portrait output: `manimgx render path/to/scene.py -r 1080x1920`
- Shared repository conventions: `manim_math_gx.runtime`

## Architecture boundary

```text
math/topic scene
    |
    |  ManimGX public Python API
    v
Scene / Mobject / Animation / Text / MathTex
    |
    +---- repository conventions: manim_math_gx.runtime
    |
    v
ManimGX Python timeline
    |
    v
Rust / wgpu renderer + in-process x264
```

Do not recreate ManimCE internals in the compatibility package.  If a scene needs an
old renderer-specific implementation, redesign the scene around a ManimGX public API.

## API migration matrix

| Area | ManimCE pattern | ManimGX target | Policy |
|---|---|---|---|
| import | `from manim import *` | `from manimgx import *` | automatic |
| namespaced import | `import manim as m` | `import manimgx as m` | automatic |
| portrait pixels | `config.pixel_width/height` | same | preserve |
| frame height | `config.frame_height = 16` | same | preserve |
| frame width | `config.frame_width = 9` | derived from aspect ratio | remove assignment |
| background | `config.background_color` / `self.camera.background_color` | supported | preserve |
| basic mobjects | `Circle`, `Line`, `VGroup`, ... | ManimGX equivalents | migrate/import |
| creation | `Create`, `Write`, `FadeIn`, ... | ManimGX equivalents where available | verify by smoke test |
| transforms | `.animate`, `Transform`, ... | ManimGX equivalents | verify timing/updaters |
| text | `Text(..., font=...)` | `Text` | normalize CJK font policy |
| math | `MathTex`, `Tex` | mitex -> Typst pipeline | visual + syntax audit |
| TeX templates | `TexTemplate`, packages/macros | no direct assumption | manual redesign |
| renderer flags | Cairo/OpenGL options | wgpu engine | remove/redesign |
| CLI | `manim ...` | `manimgx preview/render ...` | scripts/workflows migration |
| media internals | CE cache/partial-movie APIs | ManimGX output model | redesign tooling |

## Chinese text policy

Existing scenes often hard-code `PingFang SC`, which is appropriate on macOS but is not
a portable Linux CI contract.  New or migrated shared components should use
`manim_math_gx.CJK_FONT`; it defaults to `Noto Sans CJK SC` and can be overridden with
`MANIM_MATH_CJK_FONT`.

Migration acceptance for a Chinese scene requires:

1. no tofu/missing glyphs;
2. no changed line wrapping that collides with mathematical objects;
3. baseline and bounding-box review for mixed Chinese + Latin text;
4. Linux CI has the selected CJK font installed;
5. platform-specific fonts may remain only when the scene is explicitly platform-bound.

## Math typesetting policy

ManimGX parses LaTeX-like math through mitex/Typst.  Ordinary `MathTex` expressions are
migrated first.  The following trigger manual review:

- `TexTemplate` / `tex_template`;
- `\\usepackage`;
- `\\newcommand` / `\\def`;
- package-specific environments or commands;
- scenes relying on exact glyph/path identity for transforms.

For these scenes, compare formulas semantically and visually; do not force a textual
conversion if Typst-native markup is clearer.

## Migration phases

### Phase 0 — inventory and guardrails

- Pin ManimGX and Python version.
- Add `tools/manimgx_audit.py`.
- Add `tools/manimgx_migrate.py` for only mechanically safe rewrites.
- Add ManimGX-specific CI.
- Block new `manim` imports on this branch.

### Phase 1 — shared runtime

- Establish portrait render profile and CJK policy.
- Migrate repository-wide helper modules before leaf scenes.
- Replace CE configuration/media assumptions with ManimGX public APIs.

### Phase 2 — representative scenes

Migrate one scene from each behavior family before bulk conversion:

- pure geometry;
- coordinate axes/graphs;
- Chinese-heavy explanation;
- `MathTex`-heavy algebra;
- updater/`ValueTracker` animation;
- camera/3D scene;
- image/SVG asset scene;
- long-form timeline with many transitions.

Each family becomes a tested migration template.

### Phase 3 — bulk scene migration

1. run `python tools/manimgx_migrate.py --write`;
2. run `python tools/manimgx_audit.py`;
3. group remaining findings by API family, not by folder;
4. fix shared helper/function logic first;
5. render representative scenes continuously;
6. migrate remaining topic folders in batches.

### Phase 4 — production pipeline

Replace ManimCE invocations in shell scripts, agents, skills and Actions workflows with
`manimgx preview` / `manimgx render`.  Rework any script that assumes ManimCE's media
folder, partial movie cache, Cairo/OpenGL renderer or old quality flags.

### Phase 5 — visual regression and cut-over

For migrated scenes compare:

- duration/timeline;
- output resolution and FPS;
- mathematical labels and glyphs;
- object positions and safe margins;
- color/opacity/stroke widths;
- updater trajectories at selected timestamps;
- audio/video synchronization where present.

When the audit reaches zero ManimCE imports and all selected smoke renders pass, the
branch can become the default runtime.

## Definition of done

- `grep`/audit finds no active ManimCE imports in production Python.
- No assignment to ManimGX read-only `config.frame_width`.
- No production command invokes the old `manim` CLI.
- Shared helpers have no dependency on ManimCE renderer/media internals.
- All high-risk TeX constructs have an explicit decision/test.
- CJK typography passes on the supported render platform(s).
- CI runs on Python 3.13+ and installs the pinned ManimGX release.
- Representative 2D, formula, updater and 3D scenes render successfully.
- Existing content-validation/geometry checks continue to pass or have documented
  ManimGX-native replacements.
