"""高三：两平面平行。定理完整前提与斜投影示意严格分离。"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE = "#4FC3F7"
PINK = "#F06292"
GREEN = "#81C784"
YELLOW = "#FFD54F"
PURPLE = "#CE93D8"


def iso(x, y, z):
    """三维坐标斜投影，仅用于展示有限平面片，不用于判断三维交点。"""
    return np.array([0.40 * (x - y), 0.182 * (x + y) + 0.52 * z, 0])


def fit_text(message, size=27, color=WHITE):
    label = Text(message, font_size=size, color=color)
    if label.width > 7.35:
        label.scale_to_fit_width(7.35)
    return label


def plane(z, color, extent=2.9):
    vertices = [iso(-extent, -1.5, z), iso(extent, -1.5, z),
                iso(extent, 1.5, z), iso(-extent, 1.5, z)]
    return Polygon(*vertices, color=color, fill_color=color,
                   fill_opacity=0.15, stroke_width=2.1)


class PlanePlaneParallelScene(Scene):
    """保留原七镜头 Scene 入口，并分别展示定理成立条件。"""

    def setup_geometry(self):
        self.alpha_normal = np.array((0.0, 0.0, 1.0))
        self.beta_normal = np.array((0.0, 0.0, 1.0))
        self.beta_origin = np.array((0.0, 0.0, 2.0))
        self.a_direction = np.array((1.0, 0.0, 0.0))
        self.b_direction = np.array((0.0, 1.0, 0.0))
        self.gamma_normal = np.array((0.0, 1.0, 0.0))
        assert np.linalg.norm(np.cross(self.a_direction, self.b_direction)) > 0.01
        assert np.isclose(np.dot(self.alpha_normal, self.a_direction), 0)
        assert np.isclose(np.dot(self.beta_normal, self.b_direction), 0)
        assert not np.isclose(np.dot(self.beta_origin, self.alpha_normal), 0)
        assert np.linalg.norm(np.cross(self.alpha_normal, self.gamma_normal)) > 0.01
        self.ab = np.array((0.0, 0.0, 2.0))
        self.cd = np.array((0.0, 0.0, 2.0))
        assert np.allclose(self.ab, self.cd)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = fit_text("上海初高中数学直通车  @emptyandcalm", 18, GRAY_B)
        self.author.move_to(UP * 7.2)
        self.add(self.author)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property()
        self.scene_5_corollary()
        self.scene_6_summary()
        self.scene_7_outro()

    def heading(self, title, subtitle):
        head = fit_text(title, 37, YELLOW).move_to(UP * 5.85)
        note = fit_text(subtitle, 22, GRAY_A).move_to(UP * 5.05)
        self.play(Write(head), FadeIn(note), run_time=0.65)

    def clear_lesson(self):
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(*[FadeOut(obj) for obj in visible], run_time=0.4)

    def two_planes(self, ztop=2.0):
        alpha, beta = plane(0, BLUE), plane(ztop, PINK)
        lab_a = MathTex(r"\alpha", font_size=40, color=BLUE).move_to(iso(3.25, 1.5, 0))
        lab_b = MathTex(r"\beta", font_size=40, color=PINK).move_to(iso(3.25, 1.5, ztop))
        self.play(Create(alpha), Write(lab_a), run_time=0.7)
        self.play(Create(beta), Write(lab_b), run_time=0.7)
        return alpha, beta

    def line(self, start, end, name, color, label_direction=RIGHT):
        obj = Line(iso(*start), iso(*end), color=color, stroke_width=3.3)
        label = MathTex(name, font_size=35, color=color)
        label.next_to(obj.get_end(), label_direction, buff=0.11)
        self.play(Create(obj), Write(label), run_time=0.6)
        return obj, label

    def scene_1_opening(self):
        self.heading("如何判定两个平面平行？", "平行的定义、判定和截线性质，各有必要条件")
        hook = fit_text("不能只记结论箭头，必须核对几何关系", 29, GREEN)
        hook.move_to(UP * 0.6)
        self.play(Write(hook), run_time=0.7)
        self.wait(0.7)
        self.clear_lesson()

    def scene_2_definition(self):
        self.heading("定义 · 两个平面无公共点", "平行四边形只是无限平面的有限示意")
        self.two_planes()
        statement = MathTex(r"\alpha\cap\beta=\varnothing"
                            r"\quad\Longleftrightarrow\quad\alpha\parallel\beta",
                            font_size=39, color=GREEN).move_to(DOWN * 3.7)
        self.play(Write(statement), run_time=0.85)
        self.wait(0.8)
        self.clear_lesson()

    def scene_3_criterion(self):
        self.heading("判定 · 面内两条相交线都平行另一个面", "两条面内平行线不够，必须在同一点相交")
        self.two_planes()
        self.line((-2.2, 0.2, 0), (2.2, 0.2, 0), "a", YELLOW)
        self.line((0.4, -1.3, 0), (0.4, 1.3, 0), "b", PURPLE, UP)
        p = Dot(iso(0.4, 0.2, 0), radius=0.12, color=GREEN)
        p_label = MathTex("P", font_size=31, color=GREEN).next_to(p, DOWN, buff=0.1)
        self.play(FadeIn(p), Write(p_label), run_time=0.4)
        conditions = MathTex(r"a,b\subset\alpha,\quad a\cap b=\{P\}",
                             font_size=35).move_to(DOWN * 2.6)
        parallel = MathTex(r"a\parallel\beta,\quad b\parallel\beta",
                           font_size=36).move_to(DOWN * 3.65)
        conclusion = MathTex(r"\Longrightarrow\ \alpha\parallel\beta",
                             font_size=42, color=GREEN).move_to(DOWN * 4.75)
        self.play(Write(conditions), Write(parallel), run_time=0.8)
        self.play(Write(conclusion), run_time=0.7)
        self.wait(0.85)
        self.clear_lesson()

    def scene_4_property(self):
        self.heading("性质 · 同一截面与两平面所成的交线平行", "第三平面 γ 必须分别与 α、β 相交")
        self.two_planes()
        gamma_vertices = [iso(-2.7, 0, -0.3), iso(2.7, 0, -0.3),
                          iso(2.7, 0, 2.3), iso(-2.7, 0, 2.3)]
        gamma = Polygon(*gamma_vertices, color=GREEN, fill_color=GREEN,
                        fill_opacity=0.14, stroke_width=2)
        gamma_label = MathTex(r"\gamma", font_size=38, color=GREEN)
        gamma_label.move_to(iso(-2.8, 0, 2.2))
        self.play(Create(gamma), Write(gamma_label), run_time=0.7)
        self.line((-2.5, 0, 0), (2.5, 0, 0), "a", YELLOW)
        self.line((-2.5, 0, 2), (2.5, 0, 2), "b", PURPLE)
        intersections = MathTex(r"\alpha\cap\gamma=a,\quad\beta\cap\gamma=b",
                                font_size=32).move_to(DOWN * 3.45)
        result = MathTex(r"\alpha\parallel\beta\ \Longrightarrow\ a\parallel b",
                         font_size=36, color=GREEN).move_to(DOWN * 4.6)
        self.play(Write(intersections), Write(result), run_time=0.8)
        self.wait(0.8)
        self.clear_lesson()

    def scene_5_corollary(self):
        self.heading("推论 · 夹在平行平面间的平行线段等长", "两个端点必须分别位于同一对平行平面")
        self.two_planes()
        self.line((-1.4, 0.1, 0), (-1.4, 0.1, 2), "AB", YELLOW, UP)
        self.line((1.4, 0.1, 0), (1.4, 0.1, 2), "CD", PURPLE, UP)
        premise = MathTex(r"AB\parallel CD,\quad A,C\in\alpha,\ B,D\in\beta",
                          font_size=31).move_to(DOWN * 3.3)
        result = MathTex(r"\alpha\parallel\beta\ \Longrightarrow\ |AB|=|CD|",
                         font_size=39, color=GREEN).move_to(DOWN * 4.55)
        self.play(Write(premise), run_time=0.7)
        self.play(Write(result), run_time=0.7)
        self.wait(0.85)
        self.clear_lesson()

    def scene_6_summary(self):
        self.heading("面面平行 · 条件不能省略", "错误的无条件箭头会让正确的定理变成假命题")
        lines = (("定义：两个平面无公共点", BLUE),
                 ("判定：面内两相交线都平行另一面", YELLOW),
                 ("性质：第三平面分别截出两条平行交线", PURPLE),
                 ("推论：两面间平行线段等长，端点要在两面", GREEN))
        for i, (message, color) in enumerate(lines):
            label = fit_text(message, 26, color).move_to([0, 3.2 - 1.55 * i, 0])
            self.play(FadeIn(label, shift=RIGHT * 0.2), run_time=0.5)
        counter = fit_text("反例：两条平行面内线都平行另一面，仍不足以定面面平行", 20)
        counter.move_to(DOWN * 4.0)
        self.play(FadeIn(counter), run_time=0.65)
        self.wait(1.0)
        self.clear_lesson()

    def scene_7_outro(self):
        closing = fit_text("先看条件是否满足，再用判定或性质", 30, GREEN)
        closing.move_to(UP * 0.5)
        self.play(Write(closing), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(closing), FadeOut(self.author), run_time=0.6)
