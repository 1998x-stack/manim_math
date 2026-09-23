"""平方差公式：先以 a>b>0 的真实几何拆拼证明，再说明一般恒等式。

Scene 入口保持 DifferenceOfSquares，未覆盖现有 MP4。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
PURPLE_AREA = "#9b59b6"
BLUE_AREA = "#3498db"
GREEN_AREA = "#2ecc71"
RED_AREA = "#e67e22"
SAFE_WIDTH = 7.4


def area_geometry(a, b):
    """仅计算数学尺寸；场景图形必须使用同一份结果。

    a>b>0 才能作为两块正面积矩形的剪拼示意；一般代数恒等式不受此限制。
    """
    import math

    try:
        valid = math.isfinite(a) and math.isfinite(b) and a > b > 0
    except (TypeError, ValueError):
        valid = False
    if not valid:
        raise ValueError("几何拆拼要求有限实数 a>b>0")
    h = a - b
    pieces = ((a, h), (h, b))
    target = (a + b, h)
    if a * a - b * b != pieces[0][0] * pieces[0][1] + pieces[1][0] * pieces[1][1]:
        raise AssertionError("分块面积错误")
    return {"a": a, "b": b, "h": h, "cut_area": b * b,
            "original_area": a * a, "pieces": pieces, "target": target,
            "remaining_area": a * a - b * b}


class DifferenceOfSquares(Scene):
    """七镜头：代数展开、减去小正方形、实际两块拼接和逆用。"""

    def fit(self, mob, max_width=SAFE_WIDTH):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, caption):
        return self.fit(Text(caption, font_size=38, color=YELLOW)).move_to(UP * 5.5)

    def mathline(self, latex, y, color=WHITE, size=42):
        return self.fit(MathTex(latex, color=color, font_size=size)).move_to(UP * y)

    def label(self, value, y, color=GRAY_A):
        return self.fit(Text(value, color=color, font_size=25)).move_to(UP * y)

    def clear_content(self):
        visible = [mob for mob in tuple(self.mobjects) if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.geometry = area_geometry(3.6, 1.2)
        self.a = self.geometry["a"]
        self.b = self.geometry["b"]
        self.h = self.geometry["h"]
        self.square_center = DOWN * 0.7
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_info)
        self.scene_1_opening()
        self.scene_2_formula_intro()
        self.scene_3_build_square_a()
        self.scene_4_subtract_square_b()
        self.scene_5_rearrange_rectangles()
        self.scene_6_concrete_example()
        self.scene_7_outro()

    def scene_1_opening(self):
        title = self.heading("平方差：少算一次乘法")
        question = self.mathline(r"(x+2)(x-2)=\,?", 2.5, BLUE_AREA, 54)
        hint = self.label("先观察：两个括号只有中间符号不同", -0.6, YELLOW)
        self.play(Write(title), Write(question), run_time=0.95)
        self.play(FadeIn(hint), run_time=0.55)
        self.wait(1)
        self.clear_content()

    def scene_2_formula_intro(self):
        title = self.heading("先用分配律验证")
        lines = VGroup(
            self.mathline(r"(a+b)(a-b)", 3.5, BLUE_AREA, 46),
            self.mathline(r"=a^2-ab+ab-b^2", 1.8, WHITE, 42),
            self.mathline(r"=a^2-b^2", 0.1, GREEN_AREA, 48),
        )
        note = self.label("中间两项互为相反数，正好抵消", -2.0, YELLOW)
        self.play(Write(title), run_time=0.6)
        for line in lines:
            self.play(Write(line), run_time=0.65)
        self.play(FadeIn(note), run_time=0.55)
        self.wait(1.1)
        self.clear_content()

    def scene_3_build_square_a(self):
        title = self.heading("面积图：先画边长 a 的正方形")
        self.square_a = Square(side_length=self.a, color=PURPLE_AREA,
                               fill_color=PURPLE_AREA, fill_opacity=0.18,
                               stroke_width=3).move_to(self.square_center)
        top = MathTex("a", font_size=32).next_to(self.square_a, UP, buff=0.18)
        side = MathTex("a", font_size=32).next_to(self.square_a, LEFT, buff=0.18)
        self.big_labels = VGroup(top, side)
        area = self.mathline(r"S_{\text{大正方形}}=a^2", -4.5, PURPLE_AREA, 35)
        self.play(Write(title), Create(self.square_a), run_time=0.9)
        self.play(Write(self.big_labels), Write(area), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(area), run_time=0.35)
        # square_a 与 big_labels 是下一镜头实际在屏对象，不创建复制品。

    def scene_4_subtract_square_b(self):
        title = self.heading("减去右上角边长 b 的正方形")
        self.cut = Square(side_length=self.b, color=RED_AREA,
                          fill_color=RED_AREA, fill_opacity=0.7,
                          stroke_width=2).move_to(
                              self.square_center + RIGHT * (self.h / 2)
                              + UP * (self.h / 2)
                          )
        cut_label = MathTex(r"b^2", font_size=33, color=WHITE).move_to(self.cut)
        # 底块宽 a、高 a-b；左上块宽 a-b、高 b，恰好覆盖 L 形的两块非交叠区域。
        self.bottom_rect = Rectangle(width=self.a, height=self.h,
                                     color=BLUE_AREA, stroke_width=2,
                                     fill_color=BLUE_AREA, fill_opacity=0.55)
        self.bottom_rect.move_to(self.square_center + DOWN * (self.b / 2))
        self.upper_rect = Rectangle(width=self.h, height=self.b,
                                    color=GREEN_AREA, stroke_width=2,
                                    fill_color=GREEN_AREA, fill_opacity=0.55)
        self.upper_rect.move_to(self.square_center + LEFT * (self.b / 2)
                                + UP * (self.h / 2))
        note = self.mathline(r"S_{\text{剩余}}=a^2-b^2", -4.6, YELLOW, 38)
        self.play(Write(title), FadeIn(self.cut), FadeIn(cut_label), run_time=0.8)
        self.play(FadeIn(self.bottom_rect), FadeIn(self.upper_rect), run_time=0.7)
        self.play(Write(note), run_time=0.65)
        self.wait(1.0)
        self.play(FadeOut(self.square_a), FadeOut(self.cut), FadeOut(cut_label),
                  FadeOut(self.big_labels), FadeOut(title), FadeOut(note),
                  run_time=0.55)
        # 只保留 bottom_rect、upper_rect 两块，下一镜头移动它们本身。

    def scene_5_rearrange_rectangles(self):
        title = self.heading("剪拼不改变面积")
        guide = self.label("把左上块转过来，拼在底块的右边", 3.4, YELLOW)
        self.play(Write(title), FadeIn(guide), run_time=0.75)
        # 目标：底块 x∈[-(a+b)/2, (a-b)/2]；旋转块 x∈[(a-b)/2,(a+b)/2]。
        # 二者 y∈[-0.8-(a-b)/2, -0.8+(a-b)/2]，共边不重叠也没有缝隙。
        self.play(
            self.bottom_rect.animate.move_to([-self.b / 2, -0.8, 0]),
            self.upper_rect.animate.rotate(-PI / 2).move_to([self.a / 2, -0.8, 0]),
            run_time=1.7,
        )
        self.final_parts = VGroup(self.bottom_rect, self.upper_rect)
        outline = SurroundingRectangle(self.final_parts, color=YELLOW, buff=0,
                                       stroke_width=3)
        width_label = MathTex(r"a+b", font_size=33, color=YELLOW).next_to(
            self.final_parts, UP, buff=0.18
        )
        height_label = MathTex(r"a-b", font_size=33, color=YELLOW).next_to(
            self.final_parts, RIGHT, buff=0.18
        )
        conclusion = self.mathline(r"(a+b)(a-b)=a^2-b^2", -4.5, YELLOW, 41)
        self.play(Create(outline), Write(width_label), Write(height_label), run_time=0.85)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.5)
        self.clear_content()

    def scene_6_concrete_example(self):
        title = self.heading("回到开头的例题")
        line1 = self.mathline(r"(x+2)(x-2)", 3.7, BLUE_AREA, 50)
        line2 = self.mathline(r"=x^2-2^2", 1.5, WHITE, 47)
        result = self.mathline(r"=x^2-4", -0.7, GREEN_AREA, 52)
        note = self.label("几何图用 a>b>0；代数恒等式对任意实数 a、b 成立", -3.2, YELLOW)
        self.play(Write(title), Write(line1), run_time=0.95)
        self.play(Write(line2), run_time=0.65)
        self.play(Write(result), run_time=0.65)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.3)
        self.clear_content()

    def scene_7_outro(self):
        title = self.heading("逆用公式：因式分解")
        reverse = self.mathline(r"a^2-b^2=(a+b)(a-b)", 3.1, BLUE_AREA, 42)
        example = self.mathline(r"x^2-9=(x+3)(x-3)", 0.5, GREEN_AREA, 39)
        note = self.label("两平方相减，写成和与差的乘积", -2.1, YELLOW)
        self.play(Write(title), Write(reverse), run_time=0.9)
        self.play(Write(example), FadeIn(note), run_time=0.9)
        self.wait(1.2)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.7)
