"""Repository-level ManimGX runtime conventions.

This module is intentionally small: scene code should use ManimGX directly.  The
helpers here only encode conventions that are shared by this repository (portrait
frame geometry, CJK font selection, and migration assertions).
"""

from __future__ import annotations

from dataclasses import dataclass
import os

import manimgx as m


@dataclass(frozen=True, slots=True)
class RenderProfile:
    pixel_width: int = 1080
    pixel_height: int = 1920
    frame_height: float = 16.0
    frame_rate: float = 60.0
    background_color: str = "#000000"

    @property
    def frame_width(self) -> float:
        return self.frame_height * self.pixel_width / self.pixel_height


PORTRAIT_1080P = RenderProfile()
CJK_FONT = os.getenv("MANIM_MATH_CJK_FONT", "Noto Sans CJK SC")


def configure_render(profile: RenderProfile = PORTRAIT_1080P) -> RenderProfile:
    """Apply a repository render profile to ManimGX.

    ManimGX derives ``config.frame_width`` from ``frame_height`` and the pixel
    aspect ratio.  Never assign ``config.frame_width`` directly.
    """

    m.config.pixel_width = profile.pixel_width
    m.config.pixel_height = profile.pixel_height
    m.config.frame_height = profile.frame_height
    m.config.frame_rate = profile.frame_rate
    m.config.background_color = profile.background_color
    return profile


def assert_profile(profile: RenderProfile = PORTRAIT_1080P, *, tolerance: float = 1e-9) -> None:
    """Fail fast when the active ManimGX frame geometry differs from the profile."""

    actual = m.config.frame_width
    expected = profile.frame_width
    if abs(actual - expected) > tolerance:
        raise RuntimeError(
            f"ManimGX frame width mismatch: expected {expected:g}, got {actual:g}. "
            "Set pixel_width/pixel_height/frame_height; do not assign frame_width."
        )


def cjk_text(text: str, *args: object, font: str | None = None, **kwargs: object) -> m.Text:
    """Create Chinese/plain text with the repository's configurable CJK font."""

    return m.Text(text, *args, font=font or CJK_FONT, **kwargs)
