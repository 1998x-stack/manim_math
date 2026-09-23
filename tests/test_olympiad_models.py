"""Expose the independent elementary-olympiad math tests to repository unittest discovery."""
import importlib.util
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1] / "小学" / "奥数专题" / "test_math_models.py"
SPEC = importlib.util.spec_from_file_location("olympiad_math_models", SOURCE)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

# unittest discover picks up this imported TestCase without importing Manim.
MathModelsTest = module.MathModelsTest
