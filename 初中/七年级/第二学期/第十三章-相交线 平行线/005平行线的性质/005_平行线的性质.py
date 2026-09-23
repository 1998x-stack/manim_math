"""七年级：由两直线平行推出同位角、内错角及同旁内角的关系。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 平行线的性质Animation(Scene):
    """使用同一组两条平行线和一条截线，展示三种不同的位置关系。"""

    def fit(self, mob):
        if mob.width > 7.5:
            mob.scale_to_fit_width(7.5)
        return mob

    def draw_configuration(self):
        top = Line(LEFT * 3 + UP * 2, RIGHT * 3 + UP * 2, color=BLUE)
        bottom = Line(LEFT * 3 + DOWN * 1.2, RIGHT * 3 + DOWN * 1.2, color=BLUE)
        transversal = Line(LEFT * 2.8 + DOWN * 3, RIGHT * 2.8 + UP * 3, color=WHITE)
        # 截线端点是 (-2.8,-3) 和 (2.8,3)，即 x=(2.8/3)y。
        upper_intersection = RIGHT * (2.8 / 3 * 2) + UP * 2
        lower_intersection = LEFT * (2.8 / 3 * 1.2) + DOWN * 1.2
        line_group = VGroup(top, bottom, transversal)
        self.play(Create(top), Create(bottom), Create(transversal), run_time=1.2)
        return line_group, upper_intersection, lower_intersection

    def property_slide(self, heading, offset_top, offset_bottom, conclusion, explanation, accent):
        title = self.fit(Text(heading, font_size=36, color=accent)).move_to(UP * 5.35)
        self.play(Write(title), run_time=0.65)
        lines, upper, lower = self.draw_configuration()
        marker_one = MathTex("1", font_size=30, color=accent).move_to(upper + offset_top)
        marker_two = MathTex("2", font_size=30, color=accent).move_to(lower + offset_bottom)
        marks = VGroup(marker_one, marker_two)
        formula = self.fit(MathTex(conclusion, font_size=43, color=accent)).move_to(DOWN * 4.2)
        caption = self.fit(Text(explanation, font_size=25, color=WHITE)).move_to(DOWN * 5.25)
        self.play(FadeIn(marks), run_time=0.6)
        self.play(Write(formula), FadeIn(caption), run_time=1.0)
        self.wait(1.6)
        self.play(FadeOut(VGroup(title, lines, marks, formula, caption)), run_time=0.55)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = self.fit(Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B))
        author.move_to(UP * 7.2)
        self.add(author)
        intro = Text("平行线的性质", font_size=48, color=GOLD).move_to(UP * 5.3)
        premise = self.fit(Text("前提：两直线平行，被第三条直线所截", font_size=28))
        premise.move_to(UP * 1.2)
        self.play(Write(intro), FadeIn(premise), run_time=1.1)
        self.wait(1.3)
        self.play(FadeOut(VGroup(intro, premise)), run_time=0.5)

        # 同位角：两交点都取右上方区域。上方是外角，下方是内角。
        self.property_slide("性质一：同位角相等", RIGHT * 0.36 + UP * 0.32,
                            RIGHT * 0.36 + UP * 0.32,
                            r"\angle 1=\angle 2", "两直线平行，同位角相等", GREEN)
        # 内错角：上交点左下方与下交点右上方均为锐角，且都在两线内部。
        self.property_slide("性质二：内错角相等", LEFT * 0.36 + DOWN * 0.32,
                            RIGHT * 0.36 + UP * 0.32,
                            r"\angle 1=\angle 2", "两直线平行，内错角相等", YELLOW)
        # 同旁内角：上交点右下（钝角）和下交点右上（锐角）互补。
        self.property_slide("性质三：同旁内角互补", RIGHT * 0.36 + DOWN * 0.32,
                            RIGHT * 0.36 + UP * 0.32,
                            r"\angle 1+\angle 2=180^{\circ}", "两直线平行，同旁内角互补", ORANGE)

        summary = self.fit(Text("先确认平行，再根据角的位置推关系", font_size=30, color=GOLD))
        summary.move_to(UP * 1.1)
        self.play(Write(summary), run_time=0.9)
        self.wait(2)
