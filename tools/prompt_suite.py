#!/usr/bin/env python3
"""Repository entrypoint for the standalone curriculum Prompt Skill."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1] / "skills/source/curriculum-prompt-suite/scripts/prompt_suite.py"), run_name="__main__")
