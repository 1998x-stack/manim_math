# Test layout and commands

The repository is migrating to layered testing without breaking the existing unittest suites.

## Existing locations

- `tests/test_*.py`: repository-level unit/contract/regression tests
- `tools/tests/test_*.py`: tooling and historical pipeline regressions
- course-local `test_math.py` / `verify_*.py`: lesson-specific mathematics and source contracts

## New layered locations

- `tests/property/`: Hypothesis invariants over pure mathematical models
- future `tests/unit/`, `tests/contract/`, `tests/regression/`, `tests/render/`, `tests/acceptance/`

## Control files

- `test_manifest.json`: logical suites and representative Scene registry; each render records both requested preview dimensions and expected output dimensions
- `../tools/test_platform.py`: validation/change selection/matrix generation
- `../tools/media_probe.py`: hard ffprobe media checks
- `../tools/render_smoke.sh`: shared real-Manim smoke runner
- `../pytest.ini`: marker registry
- `requirements-property.txt`: focused property-test dependencies

## Fast checks

```bash
python tools/test_platform.py validate
python -m unittest tests.test_test_platform tests.test_media_probe -v
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest discover -s tools/tests -p 'test_*.py' -v
```

Property layer:

```bash
python -m pip install -r tests/requirements-property.txt
pytest -m property tests/property -q
```

Render selection example:

```bash
git diff --name-only BASE HEAD > /tmp/changed.txt
python tools/test_platform.py changed-matrix --paths-file /tmp/changed.txt
```

Real render smoke requires Manim, TeX/CJK and ffmpeg and should use `tools/render_smoke.sh` so local and CI semantics stay aligned. Do not assume the CLI `-r` request equals the final MP4 size: lesson code can override pixel dimensions, and the media gate checks the manifest's expected dimensions.
