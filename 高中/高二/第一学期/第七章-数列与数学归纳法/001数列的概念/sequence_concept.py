"""数列的概念：七镜头竖屏 Manim 教学动画（保留原有 Scene 入口）。"""

from manim import *

from sequence_data import arithmetic_terms, classification_samples, prefix_sums


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SequenceConcept(Scene):
    COLOR_PRIMARY = "#3498db"
    COLOR_SECONDARY = "#2ecc71"
    COLOR_HIGHLIGHT = "#e74c3c"
    COLOR_FORMULA = "#f39c12"
    COLOR_AUXILIARY = "#95a5a6"
    COLOR_SEQUENCE = "#9b59b6"
    CJK_FONT = "PingFang SC"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.setup_geometry()
        self.author_info = self._text(
            "上海初高中数学直通车 @emptyandcalm", 19,
            self.COLOR_AUXILIARY, UP * 6.75,
        )
        self.add(self.author_info)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_as_function()
        self.scene_4_representations()
        self.scene_5_classifications()
        self.scene_6_sum()
        self.scene_7_summary()
        self.play(FadeOut(self.author_info), run_time=0.4)

    def setup_geometry(self):
        self.sequence_indices = tuple(range(1, 9))
        self.example_sequence = arithmetic_terms(8)
        self.axes_x_range = [0, 9, 1]
        self.axes_y_range = [0, 18, 2]
        self.axes_width = 7.0
        self.axes_height = 4.5
        self.axes_offset = UP * 1.2
        self._verify_setup()

    def _verify_setup(self):
        assert len(self.example_sequence) == len(self.sequence_indices)
        assert all(value == 2 * index for index, value in zip(
            self.sequence_indices, self.example_sequence,
        ))
        assert all(0 <= value <= self.axes_y_range[1] for value in self.example_sequence)
        assert self.axes_width / 2 <= 4 and self.axes_height / 2 + 1.2 <= 7

    @staticmethod
    def _fit(mobject):
        # Check the displayed object's actual width, not just its center position.
        if mobject.width > 7.6:
            mobject.scale_to_fit_width(7.6)
        return mobject

    @staticmethod
    def _check_safe(*objects):
        for obj in objects:
            if not (-4 <= obj.get_left()[0] and obj.get_right()[0] <= 4
                    and -7 <= obj.get_bottom()[1] and obj.get_top()[1] <= 7):
                raise ValueError(f"竖屏安全区越界: {type(obj).__name__}")

    def _text(self, text, size, color, position):
        obj = Text(text, font=self.CJK_FONT, font_size=size, color=color)
        self._fit(obj).move_to(position)
        self._check_safe(obj)
        return obj

    def _math(self, expression, size, color, position):
        obj = MathTex(expression, font_size=size, color=color)
        self._fit(obj).move_to(position)
        self._check_safe(obj)
        return obj

    def _title(self, text):
        return self._text(text, 34, self.COLOR_PRIMARY, UP * 5.7)

    def _clear(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.45)

    def _axes(self):
        axes = Axes(
            x_range=self.axes_x_range, y_range=self.axes_y_range,
            x_length=self.axes_width, y_length=self.axes_height,
            axis_config={"include_numbers": True, "font_size": 17,
                         "color": self.COLOR_AUXILIARY},
            tips=False,
        ).move_to(self.axes_offset)
        self._check_safe(axes)
        return axes

    def _dots(self, axes, values):
        return VGroup(*(
            Dot(axes.c2p(index, value), radius=0.075, color=self.COLOR_SEQUENCE)
            for index, value in zip(self.sequence_indices, values)
        ))

    def scene_1_opening(self):
        title = self._title("发现这些数字的规律了吗？")
        numbers = self._math(r"1,2,3,5,8,13,21,\ldots", 35,
                             self.COLOR_HIGHLIGHT, UP * 3.1)
        floor_label = self._text("生活中的数列：楼层号", 27,
                                 self.COLOR_SECONDARY, UP * 0.9)
        floors = VGroup(*(
            self._text(f"{i}F", 28, WHITE, ORIGIN) for i in range(1, 6)
        )).arrange(RIGHT, buff=0.35).move_to(DOWN * 0.35)
        self._check_safe(floors)
        concept = self._text("按一定顺序排列的一列数", 27,
                             self.COLOR_FORMULA, DOWN * 2.4)
        self.play(Write(title), Write(numbers), run_time=1.0)
        self.play(FadeIn(floor_label), FadeIn(floors), run_time=0.8)
        self.play(FadeIn(concept), run_time=0.6)
        self.wait(0.6)
        self._clear(title, numbers, floor_label, floors, concept)

    def scene_2_definition(self):
        title = self._title("数列的概念")
        definition = self._text("数列：按一定顺序排列的一列数", 26,
                                WHITE, UP * 4.35)
        notation = self._math(r"\{a_n\}_{n\geq1}", 36,
                              self.COLOR_FORMULA, UP * 2.5)
        example = self._math(r"a_1,a_2,a_3,\ldots,a_n,\ldots", 30,
                             WHITE, UP * 1.25)
        terms = self._text("a₁ 为第 1 项，aₙ 为第 n 项", 25,
                           self.COLOR_SECONDARY, DOWN * 0.8)
        function = self._math(r"a_n=f(n),\quad n\in\mathbb{N}^{+}", 31,
                              self.COLOR_FORMULA, DOWN * 2.5)
        note = self._text("有穷数列的下标也可以只取前若干个正整数", 20,
                          self.COLOR_AUXILIARY, DOWN * 4.15)
        self.play(Write(title), FadeIn(definition), run_time=0.7)
        self.play(Write(notation), FadeIn(example), run_time=1.0)
        self.play(FadeIn(terms), FadeIn(function), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear(title, definition, notation, example, terms, function, note)

    def scene_3_as_function(self):
        title = self._title("数列是定义域离散的函数")
        axes = self._axes()
        dots = self._dots(axes, self.example_sequence)
        equation = self._math(r"a_n=2n\quad(n=1,2,\ldots)", 29,
                              self.COLOR_FORMULA, DOWN * 3.0)
        caption = self._text("每个正整数 n 对应唯一一个 aₙ", 24,
                             self.COLOR_SECONDARY, DOWN * 4.4)
        self.play(FadeIn(title), Create(axes), run_time=1.0)
        self.play(LaggedStart(*(GrowFromCenter(dot) for dot in dots),
                              lag_ratio=0.15), run_time=1.6)
        self.play(FadeIn(equation), FadeIn(caption), run_time=0.5)
        self.wait(0.8)
        self._clear(title, axes, dots, equation, caption)

    def scene_4_representations(self):
        title = self._title("数列的四种表示方法")
        self.play(FadeIn(title), run_time=0.4)
        panels = (
            ("① 通项公式法", r"a_n=2n"),
            ("② 递推公式法", r"a_1=2,\quad a_n=a_{n-1}+2\ (n\geq2)"),
            ("③ 列表法", r"\begin{array}{c|ccccc}n&1&2&3&4&5\\\hline a_n&2&4&6&8&10\end{array}"),
            ("④ 图像法", r"(1,2),(2,4),(3,6),\ldots"),
        )
        for name, formula in panels:
            label = self._text(name, 29, self.COLOR_SECONDARY, UP * 3.5)
            expression = self._math(formula, 28, self.COLOR_FORMULA, UP * 0.8)
            note = self._text("图像只包含离散点，不连接成连续曲线" if name.startswith("④")
                              else "这些表示描述的是同一个数列", 22,
                              self.COLOR_AUXILIARY, DOWN * 2.0)
            self.play(FadeIn(label), Write(expression), FadeIn(note), run_time=0.8)
            self.wait(0.45)
            self._clear(label, expression, note)
        self._clear(title)

    def scene_5_classifications(self):
        title = self._title("数列的分类")
        axes = self._axes()
        examples = classification_samples(len(self.sequence_indices))
        dots = self._dots(axes, examples["递增数列"])
        label = self._text("递增数列", 27, self.COLOR_SECONDARY, DOWN * 3.3)
        self.play(FadeIn(title), Create(axes), FadeIn(dots), FadeIn(label),
                  run_time=0.9)
        for name in ("递减数列", "常数列", "周期数列"):
            new_dots = self._dots(axes, examples[name])
            new_label = self._text(name, 27, self.COLOR_SECONDARY, DOWN * 3.3)
            self.play(Transform(dots, new_dots), ReplacementTransform(label, new_label),
                      run_time=0.8)
            label = new_label  # Keep the identity of the object actually on screen.
            self.wait(0.35)
        note = self._text("按项数还可以分为有穷数列和无穷数列", 23,
                          self.COLOR_AUXILIARY, DOWN * 4.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.65)
        self._clear(title, axes, dots, label, note)

    def scene_6_sum(self):
        title = self._title("数列的前 n 项和")
        formula = self._math(r"S_n=a_1+a_2+\cdots+a_n", 32,
                             self.COLOR_FORMULA, UP * 3.9)
        example = self._math(r"S_5=2+4+6+8+10", 32,
                             WHITE, UP * 1.9)
        answer = self._math(r"S_5=30", 38, self.COLOR_HIGHLIGHT, UP * 0.55)
        condition = self._math(r"a_n=S_n-S_{n-1}\quad(n\geq2)", 30,
                               self.COLOR_FORMULA, DOWN * 1.9)
        special = self._math(r"a_1=S_1", 30, self.COLOR_SECONDARY, DOWN * 3.05)
        self.play(FadeIn(title), Write(formula), run_time=0.8)
        self.play(Write(example), run_time=0.7)
        self.play(FadeIn(answer), run_time=0.4)
        self.play(Write(condition), FadeIn(special), run_time=0.8)
        self.wait(1.1)
        self._clear(title, formula, example, answer, condition, special)

    def scene_7_summary(self):
        title = self._title("数列核心要点")
        cards = VGroup(*(
            self._text(text, 23, color, ORIGIN)
            for text, color in (
                ("数列是一列按顺序排列的数", WHITE),
                ("数列是定义域离散的函数", self.COLOR_SECONDARY),
                ("通项、递推、列表、离散图像", self.COLOR_FORMULA),
                ("递增、递减、常数列、周期数列", self.COLOR_SEQUENCE),
                ("a₁=S₁；n≥2 时 aₙ=Sₙ−Sₙ₋₁", self.COLOR_HIGHLIGHT),
            )
        )).arrange(DOWN, buff=0.55).move_to(UP * 0.3)
        self._check_safe(cards)
        self.play(FadeIn(title), run_time=0.4)
        self.play(LaggedStart(*(FadeIn(card, shift=RIGHT * 0.2) for card in cards),
                              lag_ratio=0.22), run_time=1.5)
        self.wait(1.0)
        self._clear(title, cards)


# manim -pql sequence_concept.py SequenceConcept
