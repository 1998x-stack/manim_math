# Testing Playbook

This document turns the repository testing strategy into concrete authoring and release rules.

## 1. Hard gates before scoring

A quality score never overrides a hard failure. A change is blocked when any of the following is true:

- mathematical regression fails;
- repository/lesson contract fails;
- registered changed Scene cannot render;
- generated media has no video stream, wrong dimensions, invalid FPS, or non-positive duration;
- a historical P0 regression returns;
- required render-domain coverage disappears from the manifest.

## 2. Test case template

Every non-trivial mathematical or rendering bug should be expressed as:

```text
ID / regression reference:
Risk:
Layer: unit | property | contract | integration | render | media | regression | acceptance
Given:
When:
Then:
Boundary/negative case:
Isolation requirements:
Evidence produced:
```

For pure math code, prefer exact arithmetic and invariant checks. For Scene code, keep mathematical assertions outside Manim when possible and use real render tests for integration behavior.

## 3. Lesson acceptance checklist

A maintained lesson should progressively obtain:

- deterministic math/model tests;
- domain and boundary cases;
- source/metadata contract checks;
- Scene import/discovery;
- real low-quality render;
- TeX and CJK success;
- media probe;
- representative frame evidence;
- safe-zone/visual review;
- regression link for each historical defect.

A low-quality smoke render proves execution and media structure only. It does not prove visual correctness, pedagogy, or production readiness. The manifest separates requested render dimensions from expected media dimensions because a lesson may set `config.pixel_width` / `config.pixel_height` and legitimately override the CLI `-r` request; ffprobe validates the expected output contract.

## 4. Fault-injection matrix

| Failure | Layer | Expected behavior |
| --- | --- | --- |
| malformed JSON/metadata | contract | fail fast with actionable path |
| missing Scene source | contract | manifest validation fails |
| duplicate manifest id | contract | manifest validation fails |
| invalid lesson math boundary | unit/property | deterministic failing assertion |
| sibling Python import unavailable | render | render fails on CI, not hidden by cwd assumptions |
| missing CJK font | render | real render fails or visual evidence exposes fallback |
| TeX/dvisvgm failure | render | Manim job fails |
| Scene exception halfway through | render | non-zero job, no accepted media |
| empty MP4 | media | media gate fails |
| landscape output for portrait contract | media | dimension gate fails |
| zero/invalid FPS | media | media gate fails |
| zero duration | media | media gate fails |
| ffmpeg frame extraction failure | acceptance evidence | render job fails |
| shared global state/order dependency | regression/isolation | suite must pass independently and in aggregate |
| generated media written into lesson directory | isolation | prohibited; CI writes to runner temp only |

## 5. CI policy

### Local

Use the smallest relevant command:

```bash
python tools/test_platform.py validate
python -m unittest tests.test_test_platform tests.test_media_probe -v
pytest -m property tests/property -q
```

### Pull request

- source/contract checks;
- affected historical regression suites;
- changed registered lesson render;
- if render infrastructure changes with no registered lesson change, run the PR representative tier;
- property tests when pure model targets change.

### Main

- full repository unittest/tool regression;
- main representative render tier after every merge.

### Nightly

- all registered render domains;
- media validation and frame artifacts;
- future mutation/performance/long-running checks.

## 6. Render tiers

The manifest tier means minimum automatic cadence:

- `pr`: representative infrastructure smoke and nightly; infrastructure changes include both CLI-sized and lesson-forced 1080×1920 representatives;
- `main`: main + nightly;
- `nightly`: nightly only.

A registered lesson changed directly in a PR is rendered regardless of tier.

## 7. Quality score

Use the score for dashboards and prioritisation, never as a substitute for hard gates.

| Dimension | Points |
| --- | ---: |
| mathematical correctness and boundaries | 25 |
| property/invariant strength | 10 |
| source/lesson/skill contracts | 15 |
| real Scene integration/render | 20 |
| media integrity | 10 |
| regression coverage | 10 |
| visual acceptance evidence | 10 |

Interpretation:

- 90–100: release candidate, if all hard gates pass;
- 75–89: maintainable but acceptance gaps remain;
- 60–74: remediation required before broad rollout;
- below 60: incomplete quality evidence.

Do not award render/media/visual points from source inspection alone.

## 8. Flaky-test policy

A rerun is diagnostic evidence, not a fix.

1. record the failing test and run;
2. reproduce;
3. identify nondeterministic input/state;
4. quarantine only when necessary to unblock unrelated work;
5. open a repair task;
6. remove quarantine after deterministic stability is demonstrated.

Repeated blind reruns are not an accepted CI practice.

## 9. Regression discipline

For every confirmed bug:

```text
reproduce -> add failing regression -> fix -> pass -> keep permanently
```

Prefer stable identifiers in test names/comments, for example `regression_pr_159_unicode_ast_span`, rather than dates alone.

## 10. Expansion plan

1. six curriculum domains represented in render manifest;
2. changed-lesson PR rendering;
3. property tests on pure math models;
4. extend property coverage to reusable coordinate/geometry helpers;
5. add mutation testing for pure Python only;
6. automate safe-zone/frame analysis where robust;
7. track flaky rate, render coverage, escaped defects and CI runtime.
