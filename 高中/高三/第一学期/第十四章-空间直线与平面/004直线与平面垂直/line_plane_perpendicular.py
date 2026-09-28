"""高三：直线与平面垂直。空间直角由三维向量判定，不依赖投影角度。"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE = "#4FC3F7"
YELLOW = "#FFD54F"
PINK = "#F06292"
PURPLE = "#CE93D8"
GREEN = "#A5D6A7"


def iso(x, y, z):
    """3D->2D 斜投影：不保角，禁止把投影夹角作为空间直角。"""
    return np.array([0.425 * (x - y), 0.1925 * (x + y) + 0.55 * z, 0.0])


def fit_text(message, size=27, color=WHITE):
    label = Text(message, font_size=size, color=color)
    if label.width > 7.3:
        label.scale_to_fit_width(7.3)
    return label


def plane_patch():
    corners = [iso(-3, -1.6, 0), iso(3, -1.6, 0),
               iso(3, 1.6, 0), iso(-3, 1.6, 0)]
    return Polygon(*corners, color=BLUE, fill_color=BLUE,
                   fill_opacity=0.14, stroke_width=2.2)


class LinePlanePerpendicularScene(Scene):
    """保留原入口与七镜顺序；数学结论基于三维数据。"""

    def setup_geometry(self):
        self.normal = np.array([0.0, 0.0, 1.0])
        self.m_direction = np.array([1.0, 0.0, 0.0])
        self.n_direction = np.array([0.0, 1.0, 0.0])
        self.l_direction = np.array([0.0, 0.0, 1.0])
        assert np.linalg.norm(np.cross(self.m_direction, self.n_direction)) > 0.1
        assert np.isclose(np.dot(self.l_direction, self.m_direction), 0)
        assert np.isclose(np.dot(self.l_direction, self.n_direction), 0)
        assert np.allclose(self.l_direction, self.normal)
        self.offset_line = np.array([0.0, 0.8, 0.0])
        assert np.isclose(np.dot(self.offset_line, self.normal), 0)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = fit_text("上海初高中数学直通车  @emptyandcalm", 18, GRAY_B)
        self.author.move_to(UP * 7.2)
        self.add(self.author)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property1()
        self.scene_5_property2()
        self.scene_6_summary()
        self.scene_7_outro()

    def heading(self, title, subtitle):
        t = fit_text(title, 37, YELLOW).move_to(UP * 5.8)
        sub = fit_text(subtitle, 23, GRAY_A).move_to(UP * 5.0)
        self.play(Write(t), FadeIn(sub), run_time=0.65)

    def clear_lesson(self):
        others = [obj for obj in self.mobjects if obj is not self.author]
        if others:
            self.play(*[FadeOut(obj) for obj in others], run_time=0.4)

    def make_line(self, start, end, name, color, label_direction=RIGHT):
        line = Line(iso(*start), iso(*end), color=color, stroke_width=3.5)
        symbol = MathTex(name, font_size=38, color=color)
        symbol.next_to(line.get_end(), label_direction, buff=0.14)
        self.play(Create(line), Write(symbol), run_time=0.6)
        return line, symbol

    def scene_1_opening(self):
        self.heading("直线与平面垂直", "透视画面可能不呈现90°，空间垂直看三维方向")
        intro = fit_text("定义 · 判定 · 两个基本性质", 30, PURPLE).move_to(UP * 0.6)
        self.play(Write(intro), run_time=0.8)
        self.wait(0.75)
        self.clear_lesson()

    def scene_2_definition(self):
        self.heading("定义 · 线面垂直", "直线与平面内每一条直线所成角都是90°")
        self.play(Create(plane_patch()), run_time=0.6)
        self.make_line((-2, 0, 0), (2, 0, 0), "m", PINK)
        self.make_line((0, -1.5, 0), (0, 1.5, 0), "n", PURPLE, UP)
        self.make_line((0, 0, 0), (0, 0, 2.4), "l", YELLOW, UP)
        # 斜投影不保角：仅显示经三维点积验证的公式，不绘制伪直角方框。
        basis = MathTex(r"\vec u_l=(0,0,1),\quad\vec u_m=(1,0,0)",
                        font_size=33).move_to(DOWN * 3.25)
        formula = MathTex(r"\forall\,m\subset\alpha,\ l\perp m"
                          r"\quad\Longleftrightarrow\quad l\perp\alpha",
                          font_size=32, color=GREEN).move_to(DOWN * 4.45)
        self.play(Write(basis), run_time=0.6)
        self.play(Write(formula), run_time=0.75)
        self.wait(0.85)
        self.clear_lesson()

    def scene_3_criterion(self):
        self.heading("判定 · 两条相交的面内直线", "只与面内一条直线垂直，不足以判定线面垂直")
        self.play(Create(plane_patch()), run_time=0.6)
        self.make_line((-2, 0, 0), (2, 0, 0), "m", PINK)
        self.make_line((0, -1.5, 0), (0, 1.5, 0), "n", PURPLE, UP)
        self.make_line((0, 0, 0), (0, 0, 2.4), "l", YELLOW, UP)
        p = Dot(iso(0, 0, 0), radius=0.12, color=GREEN)
        p_label = MathTex("P", font_size=35, color=GREEN).next_to(p, DOWN, buff=0.14)
        self.play(FadeIn(p), Write(p_label), run_time=0.4)
        conditions = MathTex(r"m,n\subset\alpha,\quad m\cap n=\{P\}",
                             font_size=35).move_to(DOWN * 2.75)
        orthogonal = MathTex(r"l\perp m,\quad l\perp n", font_size=37)
        orthogonal.move_to(DOWN * 3.75)
        result = MathTex(r"\Longrightarrow\ l\perp\alpha", font_size=44,
                         color=GREEN).move_to(DOWN * 4.85)
        self.play(Write(conditions), Write(orthogonal), run_time=0.85)
        self.play(Write(result), run_time=0.6)
        self.wait(0.9)
        self.clear_lesson()

    def scene_4_property1(self):
        self.heading("性质 1 · 同面垂线互相平行", "两条直线都垂直于 α，方向均为平面法向量")
        self.play(Create(plane_patch()), run_time=0.6)
        self.make_line((-1.5, 0, 0), (-1.5, 0, 2.4), "l_1", YELLOW, UP)
        self.make_line((1.5, 0, 0), (1.5, 0, 2.4), "l_2", PINK, UP)
        note = fit_text("两个方向向量都是 (0,0,1) 的倍数", 25, PURPLE)
        note.move_to(DOWN * 3.0)
        conclusion = MathTex(r"l_1\perp\alpha,\ l_2\perp\alpha"
                              r"\ \Longrightarrow\ l_1\parallel l_2",
                              font_size=34, color=GREEN).move_to(DOWN * 4.25)
        self.play(Write(note), Write(conclusion), run_time=0.85)
        self.wait(0.9)
        self.clear_lesson()

    def scene_5_property2(self):
        self.heading("性质 2 · 垂直于面内任一直线", "注意：空间直线垂直不要求两线实际相交")
        self.play(Create(plane_patch()), run_time=0.6)
        self.make_line((-2, 0.8, 0), (2, 0.8, 0), "m", PINK)
        self.make_line((0, 0, 0), (0, 0, 2.4), "l", YELLOW, UP)
        foot = Dot(iso(0, 0, 0), radius=0.12, color=GREEN)
        self.play(FadeIn(foot), run_time=0.35)
        # m 不经过垂足；作过垂足且与 m 平行的辅助线，再用真实方向向量判断角度。
        parallel_at_foot = DashedLine(iso(-1.5, 0, 0), iso(1.5, 0, 0),
                                      color=GREEN, dash_length=0.12)
        self.play(Create(parallel_at_foot), run_time=0.6)
        prem = MathTex(r"l\perp\alpha,\quad m\subset\alpha", font_size=37)
        prem.move_to(DOWN * 3.3)
        result = MathTex(r"\Longrightarrow\ \angle(l,m)=90^\circ",
                         font_size=39, color=GREEN).move_to(DOWN * 4.5)
        self.play(Write(prem), Write(result), run_time=0.8)
        self.wait(1.0)
        self.clear_lesson()

    def scene_6_summary(self):
        self.heading("线面垂直 · 四个要点", "每条结论都有需要核查的空间前提")
        rows = (("定义：垂直于平面内每一条直线", BLUE),
                ("判定：垂直于面内两条相交直线", PINK),
                ("性质：同面两垂线互相平行", PURPLE),
                ("性质：与面内任一直线成90°", GREEN))
        for index, (line, color) in enumerate(rows):
            label = fit_text(line, 28, color).move_to([0, 3.4 - 1.5 * index, 0])
            self.play(FadeIn(label, shift=RIGHT * 0.2), run_time=0.45)
        self.wait(1.0)
        self.clear_lesson()

    def scene_7_outro(self):
        end = fit_text("判断空间直角：核查交点与三维方向", 29, GREEN)
        end.move_to(UP * 0.5)
        self.play(Write(end), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(end), FadeOut(self.author), run_time=0.6)
