"""Tiny scene used by the optional real-render integration test.

This deliberately tests rendering and media handling, not course mathematics or CJK/LaTeX.
"""
from manim import *

config.pixel_width = 270
config.pixel_height = 480
config.frame_width = 9
config.frame_height = 16


class VideoBuildSmoke(Scene):
    def construct(self):
        self.camera.background_color = '#1a1a2e'
        title = Text('VIDEO BUILD', font_size=36)
        dot = Dot(color=BLUE).shift(DOWN)
        self.add(title)
        self.play(FadeIn(dot), run_time=0.4)
        self.wait(0.2)
