"""鸡兔同笼：八个头的图阵中逐个加两条腿，用可见数量解释假设法。"""
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def solve_chicken_rabbit(heads: int, legs: int) -> tuple[int, int]:
    if type(heads) is not int or type(legs) is not int or heads < 0:
        raise ValueError("heads and legs must be nonnegative integers")
    extra = legs - 2 * heads
    if extra < 0 or extra % 2 or extra > 2 * heads:
        raise ValueError("no nonnegative whole-animal solution")
    rabbits = extra // 2
    return heads - rabbits, rabbits


def animal(symbol: str, center, color) -> VGroup:
    """头永远只有一个；鸡有 2 条腿、兔有 4 条腿，腿可被逐条看见。"""
    center = np.array(center, dtype=float)
    head = Circle(radius=.30, color=color, fill_color=color, fill_opacity=.14).move_to(center)
    name = Text(symbol, font=FONT, font_size=22, color=color).move_to(center)
    offsets = (-.17, .17) if symbol == "鸡" else (-.24, -.08, .08, .24)
    feet = VGroup(*(Line(center + [dx, -.31, 0], center + [dx, -.65, 0],
                          color=GREEN_B if symbol == "兔" and abs(dx) < .15 else color,
                          stroke_width=6) for dx in offsets))
    return VGroup(head, name, feet)


class ChickenRabbitScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        chickens, rabbits = solve_chicken_rabbit(8, 22)
        title = Text("鸡兔同笼：把多出的腿画出来", font=FONT, font_size=34).move_to(UP * 6.22)
        question = Text("8 个头，22 条腿，鸡和兔各几只？", font=FONT, font_size=27).move_to(UP * 5.13)
        self.play(Write(title), FadeIn(question))
        centers = [np.array([-2.9 + 1.93 * col, 2.8 - 1.55 * row, 0])
                   for row in range(2) for col in range(4)]
        birds = [animal("鸡", p, BLUE_B) for p in centers]
        self.play(LaggedStart(*(FadeIn(bird) for bird in birds), lag_ratio=.12), run_time=2)
        baseline = Text("先全当鸡：每个头下画 2 条腿", font=FONT, font_size=27).move_to(DOWN * 1.14)
        count = MathTex(r"8\times2=16", font_size=36, color=BLUE_B).move_to(DOWN * 2.14)
        self.play(FadeIn(baseline), Write(count))
        hint = MathTex(r"22-16=6", font_size=38, color=YELLOW).move_to(DOWN * 3.10)
        self.play(Write(hint))
        extra_groups = VGroup()
        for k in range(rabbits):
            x = -2.1 + k * 2.1
            pair = VGroup(Dot([x - .15, -4.12, 0], radius=.105, color=GREEN_B),
                          Dot([x + .15, -4.12, 0], radius=.105, color=GREEN_B))
            extra_groups.add(pair)
        self.play(FadeIn(extra_groups))
        self.wait(.5)
        for k in range(rabbits):
            rabbit = animal("兔", centers[k], YELLOW)
            new_count = MathTex(str(18 + 2 * k), font_size=36, color=GREEN_B).move_to(DOWN * 2.14)
            self.play(ReplacementTransform(birds[k], rabbit),
                      Indicate(extra_groups[k], color=GREEN_B),
                      ReplacementTransform(count, new_count), run_time=.9)
            birds[k], count = rabbit, new_count
        bracket = Brace(extra_groups, DOWN, color=GREEN_B)
        explain = Text("3 组，每组补 2 条腿", font=FONT, font_size=25, color=GREEN_B).next_to(bracket, DOWN, buff=.12)
        answer = MathTex(r"6\div2=3\,,\quad8-3=5", font_size=35, color=YELLOW).move_to(DOWN * 5.65)
        self.play(GrowFromCenter(bracket), FadeIn(explain))
        self.play(Write(answer))
        self.wait(2)
