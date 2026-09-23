"""用真实 n×n 格阵、L 形增量和边长标注解释连续奇数之和。

Render: manim external/interesting-math/odd-squares/scene.py OddSquaresScene
"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"
PALETTE = (BLUE_C, TEAL_C, GREEN_C, GOLD_C, PURPLE_C)


def odd_layer(n):
    """新增一条竖边和一条不重复计数的横边：共 2n-1 格。"""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return [(n - 1, j) for j in range(n)] + [(i, n - 1) for i in range(n - 1)]


def odd_sum(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return sum(2 * k - 1 for k in range(1, n + 1))


class OddSquaresScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP * 7))
        title = Text("奇数为什么能拼出正方形？", font=FONT,
                     font_size=34).move_to(UP * 6.25)
        hint = Text("每一层都是一个不重叠的 L 形", font=FONT,
                    font_size=26).move_to(UP * 5.05)
        addition = MathTex(r"1=1+0", font_size=35).move_to(UP * 3.55)
        running = MathTex(r"0=0^2", font_size=39).move_to(DOWN * 3.25)
        self.play(Write(title), FadeIn(hint), Write(addition), Write(running))

        size = 0.69
        center = np.array([0, 0.45, 0])
        border = None
        dimensions = None
        for n in range(1, 6):
            # Fixed world coordinates: old cells stay put as each geometric layer arrives.
            new_cells = VGroup(*[
                Square(side_length=size * 0.97, stroke_width=1.4,
                       stroke_color=BACKGROUND, fill_color=PALETTE[n - 1],
                       fill_opacity=0.95)
                .move_to(center + np.array([(x - 2) * size, (y - 2) * size, 0]))
                for x, y in odd_layer(n)
            ])
            frame_center = center + np.array([(n - 5) * size / 2,
                                              (n - 5) * size / 2, 0])
            next_border = Square(side_length=n * size, color=WHITE,
                                 stroke_width=2).move_to(frame_center)
            width = MathTex(str(n), color=YELLOW, font_size=30).next_to(
                next_border, DOWN, buff=0.13)
            height = MathTex(str(n), color=YELLOW, font_size=30).next_to(
                next_border, LEFT, buff=0.16)
            next_dims = VGroup(width, height)
            next_addition = MathTex(
                rf"{2*n-1}={n}+{n-1}", font_size=36).move_to(UP * 3.55)
            next_running = MathTex(
                "+".join(str(2*k-1) for k in range(1, n+1))
                + rf"={n}^2", font_size=36).move_to(DOWN * 3.25)
            animations = [LaggedStart(*[FadeIn(tile, shift=UP * 0.12)
                                          for tile in new_cells], lag_ratio=0.07),
                          Transform(addition, next_addition),
                          Transform(running, next_running)]
            if border is None:
                animations += [Create(next_border), FadeIn(next_dims)]
                border, dimensions = next_border, next_dims
            else:
                animations += [Transform(border, next_border),
                               Transform(dimensions, next_dims)]
            self.play(*animations, run_time=1.75)
            self.wait(0.4)

        # The geometric difference of consecutive squares is precisely the L strip.
        difference = MathTex(r"n^2-(n-1)^2=2n-1", font_size=38,
                             color=YELLOW).move_to(DOWN * 4.6)
        conclusion = MathTex(r"\sum_{k=1}^{n}(2k-1)=n^2", font_size=40,
                             color=TEAL_C).move_to(DOWN * 5.7)
        self.play(Write(difference), Write(conclusion))
        self.wait(2)
