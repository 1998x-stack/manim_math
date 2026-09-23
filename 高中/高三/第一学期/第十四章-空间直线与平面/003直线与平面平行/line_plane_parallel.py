"""高三：直线与平面平行，判定与性质的条件分离并可视化。"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE = "#4FC3F7"
GREEN = "#81C784"
GOLD = "#FFD54F"
PINK = "#F06292"
PURPLE = "#CE93D8"


def iso(x, y, z):
    """三维点的二维透视示意，不用二维交点推断三维位置。"""
    return np.array([0.425 * (x - y), 0.1925 * (x + y) + 0.55 * z, 0.0])


def text_line(message, size=26, color=WHITE):
    text = Text(message, font_size=size, color=color)
    if text.width > 7.35:
        text.scale_to_fit_width(7.35)
    return text


def plane_alpha():
    corners = [iso(-3, -1.6, 0), iso(3, -1.6, 0),
               iso(3, 1.6, 0), iso(-3, 1.6, 0)]
    return Polygon(*corners, color=BLUE, fill_color=BLUE,
                   fill_opacity=0.14, stroke_width=2.2)


def plane_beta():
    """y=0 上的竖直平面，与 alpha:z=0 的交线为 x 轴。"""
    vertices = [iso(-2.6, 0, 0), iso(2.6, 0, 0),
                iso(2.6, 0, 2.1), iso(-2.6, 0, 2.1)]
    return Polygon(*vertices, color=GREEN, fill_color=GREEN,
                   fill_opacity=0.17, stroke_width=2.2)


class LinePlaneParallelScene(Scene):
    """保留既有入口与六镜顺序。"""

    def setup_geometry(self):
        # alpha:z=0；m=(t,0,0)，l=(t,0,1.2)，beta:y=0。
        self.line_origin = np.array([0.0, 0.0, 1.2])
        self.intersection_origin = np.zeros(3)
        self.direction = np.array([1.0, 0.0, 0.0])
        self.normal_alpha = np.array([0.0, 0.0, 1.0])
        self.normal_beta = np.array([0.0, 1.0, 0.0])
        assert np.isclose(np.dot(self.normal_alpha, self.direction), 0)
        assert np.isclose(np.dot(self.normal_beta, self.direction), 0)
        assert not np.isclose(np.dot(self.line_origin, self.normal_alpha), 0)
        assert np.isclose(np.dot(self.line_origin, self.normal_beta), 0)
        # 性质图的交线：两平面法向量的叉积平行于 x 轴。
        assert np.allclose(np.abs(np.cross(self.normal_alpha,
                                           self.normal_beta)), self.direction)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = text_line("上海初高中数学直通车  @emptyandcalm", 18, GRAY_B)
        self.author.move_to(UP * 7.2)
        self.add(self.author)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property()
        self.scene_5_summary()
        self.scene_6_outro()

    def heading(self, headline, subtitle):
        title = text_line(headline, 36, GOLD).move_to(UP * 5.8)
        sub = text_line(subtitle, 23, GRAY_A).move_to(UP * 5.0)
        self.play(Write(title), FadeIn(sub), run_time=0.65)

    def clear_lesson(self):
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(*[FadeOut(obj) for obj in visible], run_time=0.4)

    def show_line(self, a, b, symbol, color):
        segment = Line(iso(*a), iso(*b), color=color, stroke_width=3.5)
        label = MathTex(symbol, font_size=39, color=color)
        label.next_to(segment.get_end(), RIGHT, buff=0.13)
        self.play(Create(segment), Write(label), run_time=0.7)
        return segment, label

    def scene_1_opening(self):
        self.heading("直线与平面平行", "定义、判定、性质三者的条件不同")
        question = text_line("直线方向与平面内一条直线相同，就一定平行吗？",
                             28, PURPLE).move_to(UP * 1.0)
        answer = text_line("不一定：还要检查这条直线是否在平面外", 27, PINK)
        answer.move_to(DOWN * 1.0)
        self.play(Write(question), run_time=0.7)
        self.play(FadeIn(answer), run_time=0.7)
        self.wait(0.8)
        self.clear_lesson()

    def scene_2_definition(self):
        self.heading("定义 · 线面平行", "整条直线与平面没有公共点")
        alpha = plane_alpha()
        alpha_label = MathTex(r"\alpha", color=BLUE, font_size=42)
        alpha_label.move_to(iso(3.3, 1.6, 0))
        self.play(Create(alpha), Write(alpha_label), run_time=0.7)
        self.show_line((-2.2, 0, 1.2), (2.2, 0, 1.2), "l", GOLD)
        shadow = DashedLine(iso(-2.2, 0, 0), iso(2.2, 0, 0),
                            color=BLUE, dash_length=0.12)
        vertical = DashedLine(iso(-2.2, 0, 0), iso(-2.2, 0, 1.2),
                              color=GRAY_A, dash_length=0.12)
        self.play(Create(shadow), Create(vertical), run_time=0.65)
        statement = MathTex(r"l\cap\alpha=\varnothing\ \Longleftrightarrow\ l\parallel\alpha",
                            font_size=38, color=GOLD).move_to(DOWN * 3.75)
        self.play(Write(statement), run_time=0.8)
        self.wait(0.85)
        self.clear_lesson()

    def scene_3_criterion(self):
        self.heading("判定 · 面外线平行面内线", "前提必须同时包含：面内线、线线平行、面外线")
        alpha = plane_alpha()
        self.play(Create(alpha), run_time=0.6)
        self.show_line((-2, 0, 0), (2, 0, 0), "m", PINK)
        self.show_line((-2, 0, 1.2), (2, 0, 1.2), "l", GOLD)
        premise = MathTex(r"m\subset\alpha,\quad l\parallel m",
                          font_size=37).move_to(DOWN * 2.85)
        outside = text_line("且 l 不在平面 α 内", 28, PURPLE).move_to(DOWN * 3.85)
        conclusion = MathTex(r"\Longrightarrow\ l\parallel\alpha",
                             font_size=44, color=GOLD).move_to(DOWN * 5.0)
        self.play(Write(premise), Write(outside), run_time=0.8)
        self.play(Write(conclusion), run_time=0.65)
        self.wait(0.9)
        self.clear_lesson()

    def scene_4_property(self):
        self.heading("性质 · 交线与面外线平行", "β 经过 l，且与 α 相交于直线 m")
        alpha, beta = plane_alpha(), plane_beta()
        self.play(Create(alpha), Create(beta), run_time=0.9)
        self.show_line((-2.2, 0, 1.2), (2.2, 0, 1.2), "l", GOLD)
        self.show_line((-2.6, 0, 0), (2.6, 0, 0), "m", PINK)
        plane_names = VGroup(
            MathTex(r"\alpha", color=BLUE, font_size=40).move_to(iso(2.8, 1.7, 0)),
            MathTex(r"\beta", color=GREEN, font_size=40).move_to(iso(-2.7, 0, 1.7)),
        )
        self.play(Write(plane_names), run_time=0.55)
        premise = MathTex(r"l\parallel\alpha,\quad l\subset\beta",
                          font_size=34).move_to(DOWN * 3.0)
        second = MathTex(r"\alpha\cap\beta=m",
                         font_size=37).move_to(DOWN * 4.0)
        conclusion = MathTex(r"\Longrightarrow\ l\parallel m",
                             font_size=44, color=GOLD).move_to(DOWN * 5.0)
        self.play(Write(premise), Write(second), run_time=0.75)
        self.play(Write(conclusion), run_time=0.65)
        self.wait(0.9)
        self.clear_lesson()

    def scene_5_summary(self):
        self.heading("两个定理怎样区分？", "不省略面外、过线及相交等前提")
        first = text_line("判定：面外 l ∥ 面内 m ⇒ l ∥ α", 29, PURPLE)
        first.move_to(UP * 2.5)
        second = text_line("性质：l ∥ α 且 β 过 l，交线 m ∥ l", 27, PINK)
        second.move_to(UP * 0.9)
        counter = text_line("反例：l、m 同在 α 内时，即使 l ∥ m，l 也不平行 α",
                            23, GOLD).move_to(DOWN * 2.4)
        self.play(Write(first), Write(second), run_time=0.9)
        self.play(FadeIn(counter), run_time=0.7)
        self.wait(1.0)
        self.clear_lesson()

    def scene_6_outro(self):
        takehome = text_line("先验证前提，再应用线面平行定理", 30, GOLD)
        takehome.move_to(UP * 0.6)
        self.play(Write(takehome), run_time=0.7)
        self.wait(1.1)
        self.play(FadeOut(takehome), FadeOut(self.author), run_time=0.6)
