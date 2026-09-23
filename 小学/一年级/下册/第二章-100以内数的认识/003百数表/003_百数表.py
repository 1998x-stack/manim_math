"""一年级《百数表》：1～100，横向 +1、纵向 +10、右下斜向 +11。

保留 1～10、11～20……91～100 的课程排列方式。
特别注意：每行末尾的整十数，与本行前九个数的十位不相同。
渲染：manim -pql 003_百数表.py HundredChartLesson
"""

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
BG = "#1a1a2e"
CELL = "#16213e"
BORDER = "#0f3460"
TEXT = "#e0e0e0"
GOLD = "#f1c40f"
ROW = "#e74c3c"
COLUMN = "#3498db"
DIAGONAL = "#2ecc71"


def chart_number(row, col):
    """10×10 百数表的零起始行列索引。"""
    if type(row) is not int or type(col) is not int or not (0 <= row < 10 and 0 <= col < 10):
        raise ValueError("百数表行列索引必须是 0～9 的整数")
    return row * 10 + col + 1


def row_numbers(row):
    return tuple(chart_number(row, col) for col in range(10))


def column_numbers(col):
    return tuple(chart_number(row, col) for row in range(10))


def diagonal_numbers(start_col=0):
    """从首行指定列向右下方取数；逐步 +11，到边界停止。"""
    if type(start_col) is not int or not 0 <= start_col < 10:
        raise ValueError("起始列必须是 0～9 的整数")
    return tuple(chart_number(row, start_col + row) for row in range(10 - start_col))


class HundredChartLesson(Scene):
    """六个阶段：引题、建表、横向、纵向、右下斜向、总结。"""

    def construct(self):
        self.camera.background_color = BG
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.add(self.author_label)
        self.scene_1_opening()
        self.scene_2_build_chart()
        self.scene_3_row_pattern()
        self.scene_4_col_pattern()
        self.scene_5_diagonal_pattern()
        self.scene_6_outro()

    def scene_1_opening(self):
        title = Text("百数表", font=FONT, font_size=72, color=GOLD)
        title.move_to(UP * 5.4)
        subtitle = Text(
            "1 到 100，藏着什么秘密？", font=FONT, font_size=32, color=TEXT,
        ).move_to(UP * 4.2)
        examples = VGroup(*[
            Text(str(value), font=FONT, font_size=44, color=GOLD)
            for value in (1, 10, 25, 50, 75, 100)
        ]).arrange_in_grid(rows=2, cols=3, buff=(1.1, 0.9)).move_to(UP * 0.8)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(number) for number in examples], lag_ratio=0.2), run_time=1.3)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(examples), run_time=0.5)

    def scene_2_build_chart(self):
        self.chart_title = Text("百数表", font=FONT, font_size=40, color=GOLD)
        self.chart_title.move_to(UP * 6.3)
        self.play(Write(self.chart_title), run_time=0.6)
        cells = VGroup()
        numbers = VGroup()
        self.cm = []
        self.nm = []
        size = 0.72
        for row in range(10):
            cell_row = []
            number_row = []
            for col in range(10):
                x = -3.6 + (col + 0.5) * size
                y = 3.6 - (row + 0.5) * size
                box = Square(
                    side_length=size, fill_color=CELL, fill_opacity=0.95,
                    stroke_color=BORDER, stroke_width=1.5,
                ).move_to([x, y, 0])
                number = Text(
                    str(chart_number(row, col)), font=FONT,
                    font_size=22, color=TEXT,
                ).move_to([x, y, 0])
                cell_row.append(box)
                number_row.append(number)
                cells.add(box)
                numbers.add(number)
            self.cm.append(cell_row)
            self.nm.append(number_row)
        self.chart_group = VGroup(cells, numbers).move_to(UP * 0.3)
        for row in range(10):
            self.play(
                LaggedStart(*[
                    FadeIn(VGroup(self.cm[row][col], self.nm[row][col]))
                    for col in range(10)
                ], lag_ratio=0.05), run_time=0.36,
            )
        self.wait(0.6)

    def _set_title(self, label, color):
        title = Text(label, font=FONT, font_size=36, color=color).move_to(UP * 6.3)
        self.play(ReplacementTransform(self.chart_title, title), run_time=0.5)
        self.chart_title = title

    def _hint(self, sentence):
        hint = Text(sentence, font=FONT, font_size=23, color=GOLD)
        if hint.width > 8.0:
            hint.scale_to_fit_width(8.0)
        hint.move_to(DOWN * 5.8)
        self.play(FadeIn(hint), run_time=0.3)
        self.wait(1)
        self.play(FadeOut(hint), run_time=0.25)

    def _highlight(self, positions, color):
        self.play(*[
            animation
            for row, col in positions
            for animation in (
                self.cm[row][col].animate.set_fill(color, opacity=0.9),
                self.nm[row][col].animate.set_color(WHITE),
            )
        ], run_time=0.5)

    def _reset(self, positions):
        self.play(*[
            animation
            for row, col in positions
            for animation in (
                self.cm[row][col].animate.set_fill(CELL, opacity=0.95),
                self.nm[row][col].animate.set_color(TEXT),
            )
        ], run_time=0.3)

    def scene_3_row_pattern(self):
        self._set_title("横着看 → 相邻两个数 +1", ROW)
        for row, sentence in (
            (0, "1～9 依次加1，10是整十数"),
            (1, "11～19 十位是1；20 十位是2"),
            (4, "41～49 十位是4；50 十位是5"),
        ):
            positions = [(row, col) for col in range(10)]
            self._highlight(positions, ROW)
            # 单独突出行末整十数，防止误教「整行十位相同」。
            self.play(
                self.cm[row][9].animate.set_fill(GOLD, opacity=0.95),
                self.nm[row][9].animate.set_color(BLACK), run_time=0.3,
            )
            self._hint(sentence)
            self._reset(positions)

    def scene_4_col_pattern(self):
        self._set_title("竖着看 ↓ 相邻两个数 +10", COLUMN)
        for col, sentence in (
            (0, "1、11、21、31……个位都是1"),
            (1, "2、12、22、32……个位都是2"),
            (9, "10、20、30、40……个位都是0"),
        ):
            positions = [(row, col) for row in range(10)]
            self._highlight(positions, COLUMN)
            self._hint(sentence)
            self._reset(positions)

    def scene_5_diagonal_pattern(self):
        self._set_title("斜着看 ↘ 相邻两个数 +11", DIAGONAL)
        for start_col, sentence in (
            (0, "1 → 12 → 23 → … → 100，每次加11"),
            (1, "2 → 13 → 24 → … → 90，每次加11"),
        ):
            positions = [(row, start_col + row) for row in range(10 - start_col)]
            self._highlight(positions, DIAGONAL)
            self._hint(sentence)
            self._reset(positions)
        # 不延用原代码中「整行十位相同」的错误总结。
        self._set_title("百数表的三个规律", GOLD)
        summary = VGroup(
            Text("→ 横向相邻 +1", font=FONT, font_size=28, color=ROW),
            Text("↓ 纵向相邻 +10", font=FONT, font_size=28, color=COLUMN),
            Text("↘ 右下斜向相邻 +11", font=FONT, font_size=28, color=DIAGONAL),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 5.1)
        self.play(LaggedStart(*[FadeIn(line) for line in summary], lag_ratio=0.4), run_time=1.3)
        self.wait(1.5)
        self.play(FadeOut(summary), run_time=0.4)

    def scene_6_outro(self):
        self.play(
            FadeOut(self.chart_group), FadeOut(self.chart_title),
            FadeOut(self.author_label), run_time=0.6,
        )
        title = Text("百数表：横加1，竖加10，右下加11", font=FONT,
                     font_size=31, color=GOLD).move_to(UP * 2)
        author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=25, color=GRAY_B).move_to(DOWN * 1)
        self.play(Write(title), FadeIn(author), run_time=0.8)
        self.wait(2)
