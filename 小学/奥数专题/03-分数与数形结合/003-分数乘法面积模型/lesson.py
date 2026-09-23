"""分数乘法面积模型：3/4 的 2/3 是 6/12。"""
from fractions import Fraction
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


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
        title = Text("分数乘法：看见重叠面积", font=FONT, font_size=34).move_to(UP * 6.25)
        prompt = MathTex(r"\frac34\times\frac23=?", font_size=45).move_to(UP * 4.85)
        self.play(Write(title), Write(prompt))
        # 4 列 × 3 行；第一阶段蓝色 9 格，第二阶段黄色重叠 6 格。
        cells = VGroup()
        for row in range(3):
            for col in range(4):
                cell = Square(side_length=1.28, stroke_color=GREY_B, stroke_width=2)
                cell.move_to(np.array([(col - 1.5) * 1.28, 1.0 + (1 - row) * 1.28, 0]))
                cells.add(cell)
        self.play(Create(cells))
        selected = [cells[row * 4 + col] for row in range(3) for col in range(3)]
        self.play(*(cell.animate.set_fill(BLUE_D, opacity=0.65) for cell in selected))
        label1 = Text("先涂满 4 列中的 3 列", font=FONT, font_size=28).move_to(DOWN * 2.5)
        self.play(FadeIn(label1))
        band = SurroundingRectangle(VGroup(*[cells[i] for i in range(8)]), color=GREEN_B, buff=0.06)
        self.play(Create(band))
        label2 = Text("再取其中的 3 行中的 2 行", font=FONT, font_size=27).move_to(DOWN * 3.25)
        self.play(ReplacementTransform(label1, label2))
        overlap = [cells[row * 4 + col] for row in range(2) for col in range(3)]
        self.play(*(cell.animate.set_fill(YELLOW, opacity=0.85) for cell in overlap))
        answer = MathTex(r"\frac34\times\frac23=\frac6{12}=\frac12", font_size=36, color=YELLOW)
        answer.move_to(DOWN * 4.55)
        note = Text("黄色 6 格 / 全部 12 格", font=FONT, font_size=27).move_to(DOWN * 5.6)
        self.play(Write(answer), FadeIn(note))
        self.wait(2)
