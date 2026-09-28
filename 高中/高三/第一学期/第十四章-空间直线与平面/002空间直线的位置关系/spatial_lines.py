"""高三：空间两条直线的位置关系（正交三维模型 + 二维等角投影）。"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FLOOR = "#4FC3F7"
LINE_A = "#FFD54F"
LINE_B = "#F06292"
POINT = "#FF8A65"
SKEW = "#CE93D8"
GREEN = "#A5D6A7"


def iso(point):
    """仅用于显示：投影后二维角度不等于实际空间夹角。"""
    x, y, z = point
    return np.array([0.85 * (x - y) * np.cos(np.pi / 6),
                     0.6 * (x + y) * np.sin(np.pi / 6) + 0.6 * z, 0.0])


def screen_text(message, size=27, color=WHITE):
    label = Text(message, font_size=size, color=color)
    if label.width > 7.3:
        label.scale_to_fit_width(7.3)
    return label


def floor_patch():
    points = ((-2.5, -1.7, 0), (2.5, -1.7, 0),
              (2.5, 1.7, 0), (-2.5, 1.7, 0))
    return Polygon(*[iso(p) for p in points], color=FLOOR,
                   fill_color=FLOOR, fill_opacity=0.13, stroke_width=2)


class SpatialLinesScene(Scene):
    """保留原 Scene 入口和八镜结构。"""

    def setup_geometry(self):
        # 真实三维坐标。两条异面直线：a=(t,0,0)，b=(0,s,1.5)。
        self.a0 = np.array([0.0, 0.0, 0.0])
        self.b0 = np.array([0.0, 0.0, 1.5])
        self.ua = np.array([1.0, 0.0, 0.0])
        self.ub = np.array([0.0, 1.0, 0.0])
        self.common = self.b0 - self.a0
        assert np.linalg.norm(np.cross(self.ua, self.ub)) > 0.01
        assert abs(np.dot(self.common, np.cross(self.ua, self.ub))) > 0.01
        assert np.isclose(np.dot(self.common, self.ua), 0.0)
        assert np.isclose(np.dot(self.common, self.ub), 0.0)
        self.theta = np.degrees(np.arccos(np.clip(
            abs(np.dot(self.ua, self.ub)) /
            (np.linalg.norm(self.ua) * np.linalg.norm(self.ub)), 0, 1)))
        self.distance = float(np.linalg.norm(self.common))
        assert np.isclose(self.theta, 90.0)
        assert np.isclose(self.distance, 1.5)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = screen_text("上海初高中数学直通车  @emptyandcalm", 18, GRAY_B)
        self.author.move_to(UP * 7.2)
        self.add(self.author)
        self.scene_1_opening()
        self.scene_2_intersect()
        self.scene_3_parallel()
        self.scene_4_skew()
        self.scene_5_skew_angle()
        self.scene_6_common_perp()
        self.scene_7_summary()
        self.scene_8_outro()

    def _title(self, title, subtitle):
        header = screen_text(title, 37, SKEW).move_to(UP * 5.85)
        note = screen_text(subtitle, 23, GRAY_A).move_to(UP * 5.0)
        self.play(Write(header), FadeIn(note), run_time=0.7)

    def _clear(self):
        visible = [m for m in self.mobjects if m is not self.author]
        if visible:
            self.play(*[FadeOut(m) for m in visible], run_time=0.45)

    def _labelled_line(self, start, end, name, color):
        line = Line(iso(start), iso(end), color=color, stroke_width=3.5)
        label = MathTex(name, color=color, font_size=37).next_to(line.get_end(), RIGHT, buff=0.13)
        return line, label

    def _skew_lines(self):
        a, la = self._labelled_line((-2, 0, 0), (2, 0, 0), "a", LINE_A)
        b, lb = self._labelled_line((0, -2, 1.5), (0, 2, 1.5), "b", LINE_B)
        return a, la, b, lb

    def scene_1_opening(self):
        self._title("空间两条直线有几种位置关系？", "关键：是否共面，是否有公共点")
        for index, (txt, color) in enumerate((("相交", LINE_A),
                                              ("平行", LINE_B),
                                              ("异面", SKEW))):
            word = screen_text(txt, 38, color).move_to([0, 2.8 - index * 1.5, 0])
            self.play(FadeIn(word), run_time=0.45)
        self.wait(0.7)
        self._clear()

    def scene_2_intersect(self):
        self._title("① 相交直线", "两条不同直线：共面，恰有一个公共点")
        plane = floor_patch()
        a, la = self._labelled_line((-2, 0, 0), (2, 0, 0), "a", LINE_A)
        b, lb = self._labelled_line((0, -1.6, 0), (0, 1.6, 0), "b", LINE_B)
        dot = Dot(iso((0, 0, 0)), color=POINT, radius=0.13)
        point_label = MathTex("P", font_size=37, color=POINT).next_to(dot, UP, buff=0.1)
        self.play(Create(plane), run_time=0.7)
        self.play(Create(a), Create(b), Write(la), Write(lb), run_time=0.9)
        self.play(FadeIn(dot), Write(point_label), run_time=0.55)
        result = screen_text("共面，并且只有一个公共点 P", 28, GREEN).move_to(DOWN * 3.5)
        self.play(Write(result), run_time=0.7)
        self.wait(0.75)
        self._clear()

    def scene_3_parallel(self):
        self._title("② 平行直线", "两条不同直线：共面，没有公共点")
        plane = floor_patch()
        a, la = self._labelled_line((-2, 0.7, 0), (2, 0.7, 0), "a", LINE_A)
        b, lb = self._labelled_line((-2, -0.7, 0), (2, -0.7, 0), "b", LINE_B)
        self.play(Create(plane), run_time=0.6)
        self.play(Create(a), Create(b), Write(la), Write(lb), run_time=0.8)
        condition = MathTex(r"a\parallel b,\quad a\ne b", font_size=40,
                            color=GREEN).move_to(DOWN * 3.3)
        self.play(Write(condition), run_time=0.7)
        self.wait(0.8)
        self._clear()

    def scene_4_skew(self):
        self._title("③ 异面直线", "不共面；投影交叉不代表空间相交")
        plane = floor_patch()
        a, la, b, lb = self._skew_lines()
        shadow = DashedLine(iso((0, -2, 0)), iso((0, 2, 0)),
                            color=SKEW, dash_length=0.13)
        support = DashedLine(iso((0, 2, 0)), iso((0, 2, 1.5)),
                             color=GRAY_B, dash_length=0.11)
        self.play(Create(plane), Create(a), Create(b), run_time=1.0)
        self.play(Write(la), Write(lb), Create(shadow), Create(support), run_time=0.7)
        note = screen_text("a 在地面；b 在上方且方向不同", 27, GREEN)
        note.move_to(DOWN * 3.5)
        self.play(Write(note), run_time=0.6)
        self.wait(0.8)
        self._clear()

    def scene_5_skew_angle(self):
        self._title("异面直线所成的角", "过同一点 O，分别作与 a、b 平行的直线")
        origin = iso(self.a0)
        dot = Dot(origin, radius=0.12, color=POINT)
        lbl_o = MathTex("O", font_size=35, color=POINT).next_to(dot, DOWN, buff=0.13)
        # b' 的两端 z=0，确实穿过 O，且方向向量与原 b 同为 (0,1,0)。
        aprime, lab_a = self._labelled_line((-1.8, 0, 0), (1.8, 0, 0),
                                             "a'", LINE_A)
        bprime, lab_b = self._labelled_line((0, -1.8, 0), (0, 1.8, 0),
                                             "b'", LINE_B)
        self.play(FadeIn(dot), Write(lbl_o), run_time=0.5)
        self.play(Create(aprime), Create(bprime), Write(lab_a), Write(lab_b),
                  run_time=0.9)
        # 等角投影不保角，严禁将二维投影圆弧标成真实空间 90°。
        formula = MathTex(r"\cos\theta=\frac{|\vec u\cdot\vec v|}"
                           r"{|\vec u|\,|\vec v|}", font_size=38)
        formula.move_to(DOWN * 3.2)
        angle = MathTex(r"\vec u=(1,0,0),\quad\vec v=(0,1,0)",
                        font_size=34, color=GREEN).move_to(DOWN * 4.25)
        result = MathTex(r"\theta=90^\circ", font_size=46, color=SKEW)
        result.move_to(DOWN * 5.25)
        self.play(Write(formula), Write(angle), run_time=0.8)
        self.play(Write(result), run_time=0.6)
        self.wait(0.9)
        self._clear()

    def scene_6_common_perp(self):
        self._title("公垂线段与异面直线的距离", "垂足必须分别位于两条直线上")
        plane = floor_patch()
        a, la, b, lb = self._skew_lines()
        foot_a, foot_b = iso(self.a0), iso(self.b0)
        bridge = Line(foot_a, foot_b, color=GREEN, stroke_width=4)
        m = Dot(foot_a, color=POINT, radius=0.10)
        n = Dot(foot_b, color=POINT, radius=0.10)
        lbl_m = MathTex("M", font_size=33, color=POINT).next_to(m, LEFT, buff=0.1)
        lbl_n = MathTex("N", font_size=33, color=POINT).next_to(n, RIGHT, buff=0.1)
        self.play(Create(plane), Create(a), Create(b), Write(la), Write(lb),
                  run_time=0.9)
        self.play(Create(bridge), FadeIn(m), FadeIn(n), Write(lbl_m), Write(lbl_n),
                  run_time=0.8)
        perpendicular = MathTex(r"MN\perp a,\quad MN\perp b",
                                font_size=36, color=GREEN).move_to(DOWN * 3.6)
        distance = MathTex(r"d(a,b)=|MN|=1.5", font_size=39,
                           color=GREEN).move_to(DOWN * 4.65)
        self.play(Write(perpendicular), Write(distance), run_time=0.8)
        self.wait(0.9)
        self._clear()

    def scene_7_summary(self):
        self._title("三种位置关系 · 对比", "先判断是否共面，再判断公共点")
        items = (("相交：共面，一个公共点", LINE_A),
                 ("平行：共面，没有公共点", LINE_B),
                 ("异面：不共面，没有公共点", SKEW))
        for i, (message, color) in enumerate(items):
            row = screen_text(message, 29, color).move_to([0, 3.1 - i * 1.55, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.55)
        note = screen_text("没有公共点 ≠ 一定平行；还可能异面", 25, GREEN)
        note.move_to(DOWN * 3.2)
        self.play(Write(note), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def scene_8_outro(self):
        ending = screen_text("用三维坐标判断，别被二维投影误导", 29, GREEN)
        ending.move_to(UP * 1.0)
        self.play(Write(ending), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(ending), FadeOut(self.author), run_time=0.6)
