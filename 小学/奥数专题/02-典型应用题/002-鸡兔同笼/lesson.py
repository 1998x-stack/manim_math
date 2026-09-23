"""鸡兔同笼：先假设全是鸡，再补出兔子多出的两条腿。"""
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def solve_chicken_rabbit(heads: int, legs: int) -> tuple[int, int]:
    if type(heads) is not int or type(legs) is not int or heads < 0:
        raise ValueError("heads and legs must be nonnegative integers")
    extra = legs - 2 * heads
    if extra < 0 or extra % 2 or extra > 2 * heads:
        raise ValueError("no nonnegative whole-animal solution")
    rabbits = extra // 2
    return heads - rabbits, rabbits


def animal(symbol: str, center, color) -> VGroup:
    head = Circle(radius=0.35, color=color).move_to(center)
    letter = Text(symbol, font=FONT, font_size=24, color=color).move_to(center)
    feet = VGroup(*[
        Line(head.get_bottom() + RIGHT * offset, head.get_bottom() + RIGHT * offset + DOWN * 0.25, color=color)
        for offset in ([-0.22, -0.07, 0.07, 0.22] if symbol == "兔" else [-0.17, 0.17])
    ])
    return VGroup(head, letter, feet)


class ChickenRabbitScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        chickens, rabbits = solve_chicken_rabbit(8, 22)
        title = Text("鸡兔同笼：假设法", font=FONT, font_size=36).move_to(UP * 6.25)
        given = Text("8 个头，22 条腿，各有几只？", font=FONT, font_size=29).move_to(UP * 4.9)
        self.play(Write(title), FadeIn(given))
        centers = [np.array([-3.1 + 2.05 * col, 2.7 - 1.5 * row, 0]) for row in range(2) for col in range(4)]
        birds = [animal("鸡", p, BLUE_B) for p in centers]
        self.play(LaggedStart(*(FadeIn(b) for b in birds), lag_ratio=0.08))
        hint = Text("先假设 8 只全是鸡", font=FONT, font_size=29).move_to(DOWN * 1.55)
        base = MathTex(r"8\times2=16", font_size=37).move_to(DOWN * 2.55)
        self.play(FadeIn(hint), Write(base))
        extra = MathTex(r"22-16=6", font_size=36).move_to(DOWN * 3.65)
        self.play(Write(extra))
        # 每换一只兔子，恰好多出两条腿；共替换三只。
        replacements = [animal("兔", centers[k], YELLOW) for k in range(rabbits)]
        self.play(*(ReplacementTransform(birds[k], replacements[k]) for k in range(rabbits)), run_time=2)
        answer = MathTex(r"6\div2=3\quad 8-3=5", font_size=36, color=YELLOW).move_to(DOWN * 4.75)
        conclude = Text(f"鸡 {chickens} 只，兔 {rabbits} 只", font=FONT, font_size=32, color=YELLOW).move_to(DOWN * 5.8)
        self.play(Write(answer), FadeIn(conclude))
        self.wait(2)
