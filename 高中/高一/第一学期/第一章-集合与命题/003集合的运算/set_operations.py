"""集合的运算：数据驱动的交集、并集、相对全集的补集教学动画。

预览：manim -ql set_operations.py SetOperations
正式渲染与逐帧验收必须在装有 Manim、TeX 和中文字体的环境执行。
"""

from manim import *
import numpy as np


# 所有镜头共用同一组集合，屏幕上的元素与这些数据一一对应。
ELEMENTS_U = (1, 2, 3, 4, 5, 6, 7, 8)
ELEMENTS_A = (1, 2, 3, 4)
ELEMENTS_B = (3, 4, 5, 6)

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SetOperations(Scene):
    """保留原有 Scene 入口及八个教学环节。"""

    FONT = "Noto Sans CJK SC"
    COLOR_A = "#e74c3c"
    COLOR_B = "#3498db"
    COLOR_INTERSECTION = "#9b59b6"
    COLOR_UNION = "#2ecc71"
    COLOR_COMPLEMENT = "#f39c12"
    BACKGROUND = "#1a1a2e"
    CIRCLE_RADIUS = 1.55
    CIRCLE_A_CENTER = np.array([-0.9, 1.45, 0.0])
    CIRCLE_B_CENTER = np.array([0.9, 1.45, 0.0])
    UNIVERSAL_CENTER = np.array([0.0, 1.45, 0.0])
    UNIVERSAL_WIDTH = 7.5
    UNIVERSAL_HEIGHT = 5.1
    # 1、2 只在 A；3、4 在交集；5、6 只在 B；7、8 只在全集。
    MARKER_POSITIONS = {
        1: (-1.83, 1.72), 2: (-1.48, 0.68),
        3: (0.0, 1.95), 4: (0.0, 0.86),
        5: (1.83, 1.72), 6: (1.48, 0.68),
        7: (-2.85, -0.43), 8: (2.85, -0.43),
    }

    def construct(self):
        self.camera.background_color = self.BACKGROUND
        self.U = set(ELEMENTS_U)
        self.A = set(ELEMENTS_A)
        self.B = set(ELEMENTS_B)
        self.intersection = self.A & self.B
        self.union = self.A | self.B
        self.complement = self.U - self.A
        self._validate_model_and_diagram()
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 19, GRAY_B)
        self.author_info.move_to(UP * 6.83)
        self.add(self.author_info)
        self.show_opening()
        self.show_intersection()
        self.show_union()
        self.show_complement()
        self.show_properties_1()
        self.show_properties_2()
        self.show_example()
        self.show_outro()

    def _validate_model_and_diagram(self):
        if not (self.A <= self.U and self.B <= self.U):
            raise ValueError("集合 A、B 必须是全集的子集")
        if len(self.MARKER_POSITIONS) != len(self.U) or set(self.MARKER_POSITIONS) != self.U:
            raise ValueError("每个元素必须且只能有一个屏幕位置")
        for value, (x, y) in self.MARKER_POSITIONS.items():
            p = np.array([x, y, 0.0])
            in_a = np.linalg.norm(p - self.CIRCLE_A_CENTER) < self.CIRCLE_RADIUS - 0.10
            in_b = np.linalg.norm(p - self.CIRCLE_B_CENTER) < self.CIRCLE_RADIUS - 0.10
            in_u = (abs(x) < self.UNIVERSAL_WIDTH / 2 - 0.13
                    and abs(y - self.UNIVERSAL_CENTER[1]) < self.UNIVERSAL_HEIGHT / 2 - 0.13)
            if not in_u or in_a != (value in self.A) or in_b != (value in self.B):
                raise ValueError(f"元素 {value} 的 Venn 位置与集合归属不符")

    def _text(self, content, size=27, color=WHITE):
        return Text(content, font=self.FONT, font_size=size, color=color)

    @staticmethod
    def _set_tex(values):
        return r"\{" + ", ".join(str(v) for v in sorted(values)) + r"\}" if values else r"\emptyset"

    def _formula(self, tex, size=32, color=WHITE):
        result = MathTex(tex, font_size=size, color=color)
        if result.width > 7.25:
            result.scale_to_fit_width(7.25)
        return result

    def _header(self, title, symbol=None, color=YELLOW):
        title_obj = self._text(title, 35, color).move_to(UP * 5.7)
        self.play(FadeIn(title_obj), run_time=0.5)
        if symbol is None:
            return VGroup(title_obj)
        symbol_obj = self._formula(symbol, 35, color).move_to(UP * 4.75)
        self.play(Write(symbol_obj), run_time=0.5)
        return VGroup(title_obj, symbol_obj)

    def _show_diagram(self):
        # 在同一个全集上同时展示 8 个具体元素；区域着色必须与这些点对应。
        self.universal_rect = Rectangle(
            width=self.UNIVERSAL_WIDTH, height=self.UNIVERSAL_HEIGHT,
            color=GRAY_B, stroke_width=3,
        ).move_to(self.UNIVERSAL_CENTER)
        self.circle_A = Circle(radius=self.CIRCLE_RADIUS, color=self.COLOR_A,
                               stroke_width=3).move_to(self.CIRCLE_A_CENTER)
        self.circle_B = Circle(radius=self.CIRCLE_RADIUS, color=self.COLOR_B,
                               stroke_width=3).move_to(self.CIRCLE_B_CENTER)
        self.universal_label = self._formula("U", 28).move_to(np.array([-3.25, 3.53, 0.0]))
        self.label_A = self._formula("A", 28, self.COLOR_A).move_to(np.array([-1.83, 2.72, 0.0]))
        self.label_B = self._formula("B", 28, self.COLOR_B).move_to(np.array([1.83, 2.72, 0.0]))
        self.markers = {}
        for number, (x, y) in self.MARKER_POSITIONS.items():
            color = (self.COLOR_INTERSECTION if number in self.intersection else
                     self.COLOR_A if number in self.A else
                     self.COLOR_B if number in self.B else GRAY_A)
            self.markers[number] = self._formula(str(number), 29, color).move_to([x, y, 0.0])
        self.diagram = VGroup(self.universal_rect, self.circle_A, self.circle_B,
                              self.universal_label, self.label_A, self.label_B,
                              *self.markers.values())
        self.play(FadeIn(self.diagram), run_time=0.9)

    def _region(self, operation):
        a = Circle(radius=self.CIRCLE_RADIUS).move_to(self.CIRCLE_A_CENTER)
        b = Circle(radius=self.CIRCLE_RADIUS).move_to(self.CIRCLE_B_CENTER)
        if operation == "intersection":
            region, color = Intersection(a, b), self.COLOR_INTERSECTION
        elif operation == "union":
            region, color = Union(a, b), self.COLOR_UNION
        else:
            whole = Rectangle(width=self.UNIVERSAL_WIDTH, height=self.UNIVERSAL_HEIGHT)
            whole.move_to(self.UNIVERSAL_CENTER)
            region, color = Difference(whole, a), self.COLOR_COMPLEMENT
        region.set_fill(color, opacity=0.48).set_stroke(width=0)
        return region

    def _show_operation(self, operation, heading, symbol, definition, explanation,
                        result, result_tex, example_lines, color):
        header = self._header(heading, symbol, color)
        region = self._region(operation)
        self.play(FadeIn(region), run_time=0.75)
        self.bring_to_front(self.diagram)  # 区域不能遮挡真实元素、圆边及集合标签。
        definition_obj = self._formula(definition, 26).move_to(DOWN * 2.17)
        explanation_obj = self._text(explanation, 22, GRAY_A).move_to(DOWN * 2.84)
        self.play(Write(definition_obj), FadeIn(explanation_obj), run_time=0.8)
        lines = VGroup()
        for i, line in enumerate(example_lines):
            item = self._formula(line, 27, color if i == len(example_lines) - 1 else WHITE)
            item.move_to(DOWN * (3.66 + 0.82 * i))
            lines.add(item)
            self.play(Write(item), run_time=0.55)
        self.play(*[Indicate(self.markers[n], color=YELLOW, scale_factor=1.24)
                    for n in sorted(result)], run_time=0.95)
        self.wait(0.6)
        self.play(FadeOut(header), FadeOut(region), FadeOut(definition_obj),
                  FadeOut(explanation_obj), FadeOut(lines), run_time=0.55)

    def show_opening(self):
        header = self._header("集合的三大运算", color=YELLOW)
        subtitle = self._text("交集 · 并集 · 补集", 28, GRAY_A).move_to(UP * 4.75)
        self.play(FadeIn(subtitle), run_time=0.45)
        self._show_diagram()
        self.wait(0.7)
        self.play(FadeOut(header), FadeOut(subtitle), run_time=0.5)

    def show_intersection(self):
        self._show_operation(
            "intersection", "交集", r"A\cap B",
            r"A\cap B=\{x\mid x\in A\ \mathrm{and}\ x\in B\}",
            "同时属于 A 和 B 的元素", self.intersection,
            r"A\cap B=" + self._set_tex(self.intersection),
            ["A=" + self._set_tex(self.A), "B=" + self._set_tex(self.B),
             r"A\cap B=" + self._set_tex(self.intersection)],
            self.COLOR_INTERSECTION,
        )

    def show_union(self):
        self._show_operation(
            "union", "并集", r"A\cup B",
            r"A\cup B=\{x\mid x\in A\ \mathrm{or}\ x\in B\}",
            "属于 A 或 B 的元素只计一次", self.union,
            r"A\cup B=" + self._set_tex(self.union),
            ["A=" + self._set_tex(self.A), "B=" + self._set_tex(self.B),
             r"A\cup B=" + self._set_tex(self.union)],
            self.COLOR_UNION,
        )

    def show_complement(self):
        self._show_operation(
            "complement", "补集", r"U\setminus A",
            r"U\setminus A=\{x\mid x\in U\ \mathrm{and}\ x\notin A\}",
            "相对全集 U，不属于 A 的元素", self.complement,
            r"U\setminus A=" + self._set_tex(self.complement),
            ["U=" + self._set_tex(self.U), "A=" + self._set_tex(self.A),
             r"U\setminus A=" + self._set_tex(self.complement)],
            self.COLOR_COMPLEMENT,
        )
        self.play(FadeOut(self.diagram), run_time=0.5)

    def _show_properties(self, heading, statements, note, color):
        header = self._header(heading, color=color)
        formulas = VGroup()
        for i, line in enumerate(statements):
            formula = self._formula(line, 37, WHITE).move_to(UP * (3.8 - 1.55 * i))
            formulas.add(formula)
            self.play(Write(formula), run_time=0.6)
        explanation = self._text(note, 23, GRAY_A).move_to(DOWN * 4.5)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.9)
        self.play(FadeOut(header), FadeOut(formulas), FadeOut(explanation), run_time=0.55)

    def show_properties_1(self):
        self._show_properties("交并运算性质", [
            r"A\cap\emptyset=\emptyset", r"A\cup\emptyset=A",
            r"A\cap A=A", r"A\cup A=A",
        ], "同一元素在集合中不重复计数", self.COLOR_UNION)

    def show_properties_2(self):
        self._show_properties("补集运算性质", [
            r"A\cup(U\setminus A)=U", r"A\cap(U\setminus A)=\emptyset",
            r"U\setminus(U\setminus A)=A",
        ], "所有补集运算都相对于固定全集 U", self.COLOR_COMPLEMENT)

    def show_example(self):
        header = self._header("综合应用", color=YELLOW)
        self._show_diagram()
        first = self._formula(r"(A\cap B)=" + self._set_tex(self.intersection), 29,
                              self.COLOR_INTERSECTION).move_to(DOWN * 2.5)
        second = self._formula(r"U\setminus(A\cap B)=" +
                               self._set_tex(self.U - self.intersection), 27,
                               self.COLOR_COMPLEMENT).move_to(DOWN * 3.55)
        third = self._formula(r"A\cap(U\setminus B)=" +
                              self._set_tex(self.A - self.B), 29,
                              self.COLOR_UNION).move_to(DOWN * 4.65)
        self.play(Write(first), run_time=0.7)
        self.play(Write(second), run_time=0.85)
        self.play(*[Indicate(self.markers[n], color=YELLOW)
                    for n in sorted(self.U - self.intersection)], run_time=0.85)
        self.play(Write(third), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(header), FadeOut(first), FadeOut(second),
                  FadeOut(third), FadeOut(self.diagram), run_time=0.7)

    def show_outro(self):
        title = self._text("交集 · 并集 · 补集", 39, YELLOW).move_to(UP * 1.5)
        subtitle = self._text("用同一组元素理解三个运算", 25, GRAY_A).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.65)
        self.wait(1.3)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(self.author_info), run_time=0.7)
