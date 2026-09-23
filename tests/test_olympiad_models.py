"""Expose both arithmetic and geometric elementary-olympiad tests to CI."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "小学" / "奥数专题"


def load_test(filename, module_name):
    source = ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, source)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MathModelsTest = load_test("test_math_models.py", "olympiad_math_models").MathModelsTest
VisualContractsTest = load_test("test_visual_contracts.py", "olympiad_visual_contracts").VisualContractsTest
