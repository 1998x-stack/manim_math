# manim_math industrial testing strategy

## Purpose

Quality is not Python coverage alone. A lesson is releasable only when its mathematical model, repository contracts, Manim execution and generated media satisfy their gates.

## Quality model

```text
Static -> Unit/Math -> Property -> Contract -> Scene -> Render -> Media -> Regression
```

| Layer | Main question | Examples |
| --- | --- | --- |
| static | Can source/contracts be parsed? | compileall, AST/catalog/skill audits |
| unit/math | Are deterministic helpers correct? | examples, boundaries |
| property | Do invariants hold over an input space? | geometry/algebra properties |
| contract | Does a lesson expose required structure? | files, metadata, Scene naming |
| scene | Does math feed a valid Scene? | import/discovery/integration |
| render | Can Manim + TeX + CJK execute it? | low-quality real render |
| media | Is generated video structurally valid? | ffprobe, frames |
| regression | Did a historical failure return? | gotchas, bug-specific tests |

Prioritise by `failure probability * impact * change frequency`.

## CI levels

1. Local: changed compile/unit/control-plane checks, target <1 minute.
2. Pull request: static, unit/math, contract, regression and affected render smoke.
3. Main: full repository integration gate after every merge; PR-head green is not sufficient evidence after sequential merges.
4. Nightly: expensive representative real renders, media probes, later property/mutation/stress work.

## Layout

Existing tests remain in place initially. New tests should use `tests/unit`, `tests/property`, `tests/contract`, `tests/regression`, `tests/render`, and `tests/acceptance`. Course-local `test_math.py` remains valid when tightly coupled to a lesson; `tools/tests` remains tooling regression coverage.

## Control plane

`tests/test_manifest.json` inventories logical suites and representative renders. `tools/test_platform.py` validates the manifest, classifies changed lesson directories and selects render tiers without importing Manim.

A render entry has a stable id, domain, source path, Scene class and tier. A low-quality smoke render must never be described as full video acceptance.

## Regression discipline

Every confirmed bug follows `reproduce -> failing test -> fix -> passing test -> permanent regression`. Tests should reference an issue/PR or stable gotcha identifier where practical.

## Isolation

Tests must not depend on execution order, network access, mutable shared state, wall-clock time or uncontrolled randomness. Render jobs write only to runner temporary directories and never overwrite checked-in MP4 files.

## Metrics

Track count, pass rate, runtime, flaky rate, render coverage, regression count and escaped defects. Coverage is diagnostic, not the release target. Mutation testing should first target pure math/model/helper code.

## Rollout

1. Establish the control plane and main/nightly gates without moving legacy tests.
2. Register representative renders for every curriculum domain.
3. Add changed-lesson PR render selection.
4. Migrate/new-write tests into layered directories.
5. Add property testing for pure math models.
6. Add mutation testing for stable pure-Python modules.
7. Expand render/media acceptance toward every maintained lesson.
