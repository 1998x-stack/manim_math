# A-Level P1 §1.3 — The quadratic formula

- **Input:** User-provided Cambridge P1 Coursebook (2018) §1.3, printed page 10 / PDF page 22; prior §1.1 and §1.2 lessons provide continuity.
- **Output:** `P1QuadraticFormula` scene, original visuals, 9:16 logical canvas / 1080×1920 target, dark theme; persistent `A-Level / PURE MATHEMATICS 1 / P1` header, §1.3 footer, no narration or external audio.
- **Core objective:** derive general formula from completing the square; distinguish exact roots, numerical approximation, and discriminant root count.
- **Runtime assumptions:** Manim Community + TeX + installed Chinese font (`Noto Sans CJK SC` or replacement); Scene real-render checks are outstanding unless explicitly performed.

| Shot | Approx. seconds* | `learning_fact` and linked math test | Screen objects / lifecycle | Frame / visualization check |
| --- | ---: | --- | --- | --- |
| 01 hook | 8 | Factorising does not directly handle all quadratics; `a≠0` is essential. `test_non_quadratic_rejected` | Persistent chrome: create; old/fresh equations + caption: create, then remove | Course mark visible; no text/formula overlap. |
| 02 recap | 10 | `(x+d)²=x²+2dx+d²`, so `x²+4x=(x+2)²−4`. `test_algebraic_completed_square_identity` | Three algebra lines sequential create; remove | Square identity legible, distinct levels. |
| 03 area | 13 | For x=d=2: 4+8+4=16. `test_geometry_tile_counts_and_domain` | One shared model, base 4 tiles→strips 8→corner 4; labels/caveat create; remove | Tile count, geometry layout, caption x=d=2 match. Illustrative only. |
| 04 derive | 18 | Divide by a and complete square; final formula, `Δ≥0` for real roots. `test_algebraic_completed_square_identity` | Five formula objects create sequentially, final highlight; remove | Any formula remains inside safe zone; ensure denominator a never zero. |
| 05 substitute | 13 | For a=2,b=−2,c=−1: Δ=12; exact roots `(1±√3)/2`. `test_exact_example_claims` | Original→coefficients→Δ→unsimplified→exact; remove | Negative coefficients must be displayed with signs. |
| 06 parabola | 13 | Roots equal x-intercepts, vertex `(1/2,−3/2)`. `test_exact_example_claims` | Axes, curve, two computed dots, vertex and dashed axis: create; remove | Graph within axes; vertex below x axis; intercepts at true roots. |
| 07 discriminant | 15 | `Δ=4k` for family `(x−1)²−k`; k=1/0/−1 implies 2/1/0 distinct real roots. `test_root_count_and_repeated_root` | Axes create; `ValueTracker` modifies same curve/root group; label `Transform` in place; remove | Mid-animation, tangent, no-real states: root dots match the actual curve; plot interval never zero-width. |
| 08 precision | 10 | Exact vs 3 s.f. and a≠0, Δ≥0, ±. `test_rounded_example_is_3sf` | Exact and approx plus 3 caution cards: create; remove | Decimal values have ≈ symbol, not =. |
| 09 practice | 14 | `3x²+2x−2=0` → Δ=28 → `(-1±√7)/3`. `test_practice_radicals_and_residual` | Problem/pause → Δ → solution → recap card; remain to end | Answer is exact; branch pair shown; cards legible. |

*Durations are rough teaching estimates; actual scene timing may differ depending on animation playback and reading pauses.

## Persistent object lifecycle

- `chrome_mobs`: created once in `chrome()`; kept throughout; not touched by `wipe()`.
- Each shot's main objects: created/updated only within that shot and faded via `wipe()`; old scene objects are not reanimated by recreating a different reference.
- Shot 07: `axes` and tracked `graph`/`dots` persist over all 3 k values; status `Transform` retains the source object; k itself is not an on-screen Mobject.

## Evidence and publishing

`math_claims`: supported by algebra plus 8 independent pure-Python tests. `syntax`: check using `py_compile`. `runtime_checkpoints`: authored at fixed states and execute during a real render; dynamic interpolation still requires representative-frame review. `manim_render`, `frame_review`, `ffprobe`, `audio_review`: **not run** in this preparation environment. No fabricated MP4/voice/music. Use Skill's `scripts/audit_scene.py` and render gate in an environment that has the external Manim dependencies.
