"""笔算除法：用 1476 ÷ 28 示范试商、调商和余数检验。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

DIVIDEND = 1476
DIVISOR = 28
QUOTIENT, REMAINDER = divmod(DIVIDEND, DIVISOR)
assert (QUOTIENT, REMAINDER) == (52, 20)
assert DIVIDEND == DIVISOR * QUOTIENT + REMAINDER
assert 0 <= REMAINDER < DIVISOR


class TrialQuotientAdjustmentLesson(Scene):
    """估商 50 后调为 52；正确的余数小于除数。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("笔算除法：试商与调商", font_size=36).to_edge(UP, buff=0.75)
        self.play(Write(title))
        equation = MathTex(r"1476 \div 28 =\ ?", font_size=48).shift(UP * 3.5)
        self.play(Write(equation))

        estimate = VGroup(
            Text("先试商 50：", font_size=30),
            MathTex(r"28\times50=1400", font_size=36),
        ).arrange(DOWN, buff=0.3).move_to(UP * 1.5)
        self.play(FadeIn(estimate))
        trial_remainder = MathTex(r"1476-1400=76", font_size=38).next_to(estimate, DOWN, buff=0.6)
        note = Text("余数 76 不小于除数 28，需要调商", font_size=24).next_to(trial_remainder, DOWN, buff=0.4)
        self.play(Write(trial_remainder), FadeIn(note))
        self.wait(1)

        adjusted = MathTex(r"28\times52=1456", font_size=42).move_to(UP * 1.0)
        remainder = MathTex(r"1476-1456=20<28", font_size=38).next_to(adjusted, DOWN, buff=0.55)
        self.play(FadeOut(estimate), FadeOut(trial_remainder), FadeOut(note))
        self.play(Write(adjusted), Write(remainder))
        answer = VGroup(MathTex(r"1476\div28=52", font_size=43),
                        Text("余", font_size=30), MathTex("20", font_size=43))
        answer.arrange(RIGHT, buff=0.2).next_to(remainder, DOWN, buff=0.8)
        self.play(Write(answer))
        self.wait(2)


if __name__ == "__main__":
    # manim -ql '002_笔算除法(试商与调商).py' TrialQuotientAdjustmentLesson
    pass
