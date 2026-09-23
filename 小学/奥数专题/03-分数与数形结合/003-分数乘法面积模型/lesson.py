"""分数面积模型：在同一个单位正方形上依次选列、选行，只计真实交集。"""
from fractions import Fraction
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def area_product(selected_columns: int, columns: int, selected_rows: int, rows: int) -> Fraction:
    if not all(type(v) is int for v in (selected_columns, columns, selected_rows, rows)):
        raise ValueError("integer grid dimensions required")
    if not (columns > 0 and rows > 0 and 0 <= selected_columns <= columns and 0 <= selected_rows <= rows):
        raise ValueError("invalid grid selection")
    return Fraction(selected_columns * selected_rows, columns * rows)


class FractionAreaScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        assert area_product(3, 4, 2, 3) == Fraction(1, 2)
        title = Text("分数相乘：两个方向的面积交集", font=FONT, font_size=33).move_to(UP * 6.22)
        question = MathTex(r"\frac34\times\frac23=?", font_size=45).move_to(UP * 5.02)
        self.play(Write(title), Write(question))
        # 整个矩形是单位 1，12 格严格等面积，每一格占整体 1/12。
        step, x0, y0 = 1.25, -1.875, 3.1
        cells = [[Square(side_length=step, color=GREY_B, stroke_width=2,
                         fill_color=BG, fill_opacity=1).move_to([x0 + c * step, y0 - r * step, 0])
                  for c in range(4)] for r in range(3)]
        grid = VGroup(*(cells[r][c] for r in range(3) for c in range(4)))
        self.play(Create(grid), run_time=1.5)
        left_caption = Text("整体 = 1（12 个等面积小格）", font=FONT, font_size=26).move_to(DOWN * 1.04)
        self.play(FadeIn(left_caption))

        # 列选中占整体 3/4；单独的行选中占整体 2/3。
        chosen_cols = VGroup(*(cells[r][c] for r in range(3) for c in range(3)))
        col_outline = SurroundingRectangle(chosen_cols, color=BLUE_B, buff=.045, stroke_width=4)
        self.play(*(cells[r][c].animate.set_fill(BLUE_D, opacity=.7)
                    for r in range(3) for c in range(3)), run_time=1.3)
        col_note = Text("蓝色 3 列：取整体的 3/4", font=FONT, font_size=26, color=BLUE_B).move_to(DOWN * 2.06)
        self.play(Create(col_outline), FadeIn(col_note))
        self.wait(.6)

        chosen_rows = VGroup(*(cells[r][c] for r in range(2) for c in range(4)))
        row_outline = SurroundingRectangle(chosen_rows, color=GREEN_B, buff=.09, stroke_width=4)
        row_note = Text("绿色边框 2 行：取整体的 2/3", font=FONT, font_size=26, color=GREEN_B).move_to(DOWN * 3.0)
        self.play(Create(row_outline), FadeIn(row_note))
        # 两个选区交集恰是 3 列 × 2 行 = 6 格；没有涂黄的蓝格不属于交集。
        intersections = [cells[r][c] for r in range(2) for c in range(3)]
        self.play(*(cell.animate.set_fill(YELLOW, opacity=.88) for cell in intersections), run_time=1.4)
        digits = VGroup(*(MathTex(str(i + 1), font_size=29, color=BLACK).move_to(cell)
                          for i, cell in enumerate(intersections)))
        self.play(LaggedStart(*(FadeIn(number) for number in digits), lag_ratio=.14))
        conclusion = Text("黄色交集 6 格，全部共 12 格", font=FONT, font_size=27).move_to(DOWN * 4.2)
        formula = MathTex(r"\frac34\times\frac23=\frac{3\times2}{4\times3}=\frac6{12}=\frac12",
                          font_size=31, color=YELLOW).move_to(DOWN * 5.32)
        self.play(FadeIn(conclusion), Write(formula))
        self.wait(2)
