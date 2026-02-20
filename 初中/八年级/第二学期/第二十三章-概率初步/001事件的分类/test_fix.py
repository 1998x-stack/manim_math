#!/usr/bin/env python
"""
Test script to verify the LaTeX compilation fix
"""

from manim import *

# Test the specific components that were causing issues
class TestLatexFix(Scene):
    def construct(self):
        # Test the original problematic case (this would have failed)
        # prob_formula = MathTex(r"P(\text{必然事件}) = 1")  # This was the problem
        
        # Test the fixed version
        prob_label = Text(
            "概率:",
            font="Noto Sans CJK SC",  # Using the same font as the original
            font_size=28,
            color=WHITE
        )
        
        prob_value = MathTex(
            r"P = 1",
            font_size=36,
            color=GREEN
        )
        
        prob_group = VGroup(prob_label, prob_value)
        self.add(prob_group)
        self.wait(1)

if __name__ == "__main__":
    print("LaTeX fix test script created successfully")