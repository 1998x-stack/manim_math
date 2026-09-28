from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import pytest
from hypothesis import given, strategies as st

ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {relative}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


quadratic = load_module(
    "property_quadratic_model",
    "高中/A-Level/P1/01-Quadratics/06-quadratic-extrema/math_model.py",
)
probability_model = load_module(
    "property_probability_model",
    "高中/高三/第二学期/第十七章-概率论初步/002古典概型/classical_probability_math.py",
)

small_fraction = st.fractions(min_value=-20, max_value=20, max_denominator=12)
nonzero_fraction = small_fraction.filter(lambda value: value != 0)


@pytest.mark.property
@given(a=nonzero_fraction, b=small_fraction, c=small_fraction, x=small_fraction)
def test_quadratic_vertex_identity_is_algebraically_invariant(a, b, c, x):
    q = quadratic.Quadratic(a, b, c)
    assert q.verify_vertex_identity(x)


@pytest.mark.property
@given(a=nonzero_fraction, h=small_fraction, k=small_fraction, distance=small_fraction)
def test_quadratic_vertex_form_is_symmetric(a, h, k, distance):
    q = quadratic.Quadratic.from_vertex(a, h, k)
    assert q.h == h
    assert q.k == k
    assert q.value(h - distance) == q.value(h + distance)


@st.composite
def finite_probability_spaces(draw):
    size = draw(st.integers(min_value=1, max_value=30))
    favorable = draw(st.sets(st.integers(min_value=0, max_value=size - 1)))
    return tuple(range(size)), favorable


@pytest.mark.property
@given(space=finite_probability_spaces())
def test_classical_probability_matches_counting_ratio_and_complement(space):
    outcomes, favorable = space
    p = probability_model.probability(outcomes, favorable)
    complement = set(outcomes) - set(favorable)
    q = probability_model.probability(outcomes, complement)
    assert p == Fraction(len(favorable), len(outcomes))
    assert p + q == 1


@pytest.mark.property
@given(
    red=st.integers(min_value=0, max_value=30),
    blue=st.integers(min_value=0, max_value=30),
)
def test_ball_model_preserves_counting_probability(red, blue):
    if red + blue == 0:
        with pytest.raises(ValueError):
            probability_model.ball_outcomes(red, blue)
        return
    outcomes = probability_model.ball_outcomes(red, blue)
    red_outcomes = [ball for ball in outcomes if ball[0] == "红"]
    assert len(outcomes) == red + blue
    assert probability_model.probability(outcomes, red_outcomes) == Fraction(red, red + blue)
