"""
002_余角补角对顶角.py -- 余角、补角、对顶角 教学动画

知识点: 余角、补角、对顶角的定义与性质
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 余角: 两角之和等于 90 度
  3. 余角计算练习
  4. 补角: 两角之和等于 180 度
  5. 补角计算练习
  6. 对顶角: 定义与性质
  7. 对顶角相等的证明
  8. 综合练习
  9. 总结
  10. 片尾
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_ANGLE_A = "#3b82f6"       # 蓝色 角A
COLOR_ANGLE_B = "#f59e0b"       # 橙色 角B
COLOR_RESULT = "#22c55e"        # 绿色 结果
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_ACCENT = "#a78bfa"        # 紫色强调
COLOR_RED = "#ef4444"           # 红色
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
COLOR_LINE = "#e2e8f0"          # 浅灰 线段
COLOR_RIGHT_ANGLE = "#22d3ee"   # 青色 直角
COLOR_VERT_1 = "#f472b6"        # 粉色 对顶角1
COLOR_VERT_2 = "#34d399"        # 绿色 对顶角2
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class ComplementarySupplementaryVerticalLesson(Scene):
    """
    余角、补角、对顶角教学动画

    场景顺序:
      1.  开场钩子
      2.  余角定义 (图示 + 公式)
      3.  余角计算小练
      4.  补角定义 (图示 + 公式)
      5.  补角计算小练
      6.  对顶角定义 (两线相交)
      7.  对顶角相等的推理
      8.  综合练习
      9.  总结
      10. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_complementary_def()
        self.scene_3_complementary_practice()
        self.scene_4_supplementary_def()
        self.scene_5_supplementary_practice()
        self.scene_6_vertical_angles_def()
        self.scene_7_vertical_angles_proof()
        self.scene_8_combined_practice()
        self.scene_9_summary()
        self.scene_10_outro()

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _author(self):
        """顶部作者信息"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)

    def _section_title(self, text, color=COLOR_HL, y=5.5):
        return Text(text, font=FONT, font_size=36, color=color).move_to(UP * y)

    def _body_text(self, text, y=0, size=24, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color).move_to(UP * y)

    def _clear(self, *mobjects, run_time=0.5):
        if mobjects:
            self.play(*[FadeOut(m) for m in mobjects], run_time=run_time)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author_mob = self._author()
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "两条线一交叉",
            font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 4.5)
        hook2 = Text(
            "藏着哪些角的秘密?",
            font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 3.5)
        self.play(Write(hook), run_time=0.8)
        self.play(Write(hook2), run_time=0.8)

        # Quick intersecting lines preview
        origin = np.array([0, 0.5, 0])
        p1 = origin + np.array([-2.5, 1.5, 0])
        p2 = origin + np.array([2.5, -1.5, 0])
        p3 = origin + np.array([-2.0, -1.8, 0])
        p4 = origin + np.array([2.0, 1.8, 0])

        line1 = Line(p1, p2, color=COLOR_LINE, stroke_width=3)
        line2 = Line(p3, p4, color=COLOR_LINE, stroke_width=3)

        self.play(Create(line1), Create(line2), run_time=1.0)

        # question marks at the four angles
        qmarks = VGroup()
        offsets = [UP * 0.8 + LEFT * 0.6, UP * 0.8 + RIGHT * 0.6,
                   DOWN * 0.8 + LEFT * 0.6, DOWN * 0.8 + RIGHT * 0.6]
        for off in offsets:
            q = Text("?", font=FONT, font_size=32, color=COLOR_ACCENT).move_to(origin + off)
            qmarks.add(q)
        self.play(*[FadeIn(q, scale=0.5) for q in qmarks], run_time=0.6)
        self.wait(0.8)

        topic = Text(
            "余角  补角  对顶角",
            font=FONT, font_size=36, color=WHITE
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(topic, shift=UP * 0.3), run_time=0.6)
        self.wait(0.6)

        self._clear(hook, hook2, line1, line2, qmarks, topic)

    # ------------------------------------------------------------------
    # Scene 2: 余角定义
    # ------------------------------------------------------------------

    def scene_2_complementary_def(self):
        title = self._section_title("一、余角", color=COLOR_ANGLE_A)
        self.play(Write(title), run_time=0.6)

        # 90-degree angle with two sub-angles
        vertex = np.array([0, 2.0, 0])
        ray_right = vertex + np.array([3.0, 0, 0])
        ray_up = vertex + np.array([0, 3.0, 0])

        # Dividing ray at 35 degrees from horizontal
        angle_split_rad = np.radians(35)
        ray_mid_len = 3.0
        ray_mid = vertex + ray_mid_len * np.array([np.cos(angle_split_rad), np.sin(angle_split_rad), 0])

        line_h = Line(vertex, ray_right, color=COLOR_LINE, stroke_width=3)
        line_v = Line(vertex, ray_up, color=COLOR_LINE, stroke_width=3)
        line_m = Line(vertex, ray_mid, color=COLOR_HL, stroke_width=3)

        # Right angle mark
        ra_size = 0.3
        ra_mark = VGroup(
            Line(vertex + RIGHT * ra_size, vertex + RIGHT * ra_size + UP * ra_size, color=COLOR_RIGHT_ANGLE, stroke_width=2),
            Line(vertex + UP * ra_size, vertex + RIGHT * ra_size + UP * ra_size, color=COLOR_RIGHT_ANGLE, stroke_width=2),
        )

        self.play(Create(line_h), Create(line_v), run_time=0.6)
        self.play(FadeIn(ra_mark), run_time=0.3)

        # angle A (blue) from horizontal to mid ray
        arc_a = Arc(
            radius=0.8, start_angle=0, angle=angle_split_rad,
            arc_center=vertex, color=COLOR_ANGLE_A, stroke_width=3
        )
        label_a = MathTex(r"\angle 1", color=COLOR_ANGLE_A, font_size=28).move_to(
            vertex + 1.15 * np.array([np.cos(angle_split_rad / 2), np.sin(angle_split_rad / 2), 0])
        )

        # angle B (orange) from mid ray to vertical
        angle_b_val = np.pi / 2 - angle_split_rad
        arc_b = Arc(
            radius=0.9, start_angle=angle_split_rad, angle=angle_b_val,
            arc_center=vertex, color=COLOR_ANGLE_B, stroke_width=3
        )
        label_b = MathTex(r"\angle 2", color=COLOR_ANGLE_B, font_size=28).move_to(
            vertex + 1.25 * np.array([np.cos(angle_split_rad + angle_b_val / 2),
                                       np.sin(angle_split_rad + angle_b_val / 2), 0])
        )

        self.play(Create(line_m), run_time=0.6)
        self.play(Create(arc_a), FadeIn(label_a), run_time=0.6)
        self.play(Create(arc_b), FadeIn(label_b), run_time=0.6)

        # Degree labels
        deg_a_text = MathTex(r"35^\circ", color=COLOR_ANGLE_A, font_size=26).move_to(
            vertex + 1.6 * np.array([np.cos(angle_split_rad / 2), np.sin(angle_split_rad / 2), 0])
        )
        deg_b_text = MathTex(r"55^\circ", color=COLOR_ANGLE_B, font_size=26).move_to(
            vertex + 1.7 * np.array([np.cos(angle_split_rad + angle_b_val / 2),
                                      np.sin(angle_split_rad + angle_b_val / 2), 0])
        )
        self.play(FadeIn(deg_a_text), FadeIn(deg_b_text), run_time=0.5)

        # Definition text
        defn1 = Text(
            "如果两个角的和等于 90\u00b0",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 1.5)
        defn2 = Text(
            "那么这两个角互为余角",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(defn1), run_time=0.5)
        self.play(FadeIn(defn2), run_time=0.5)

        # Formula
        formula = MathTex(
            r"\angle 1 + \angle 2 = 90^\circ",
            color=COLOR_RESULT, font_size=36
        ).move_to(DOWN * 3.5)
        box = SurroundingRectangle(formula, color=COLOR_RESULT, buff=0.25, corner_radius=0.1)

        self.play(Write(formula), run_time=0.6)
        self.play(Create(box), run_time=0.4)
        self.wait(1.5)

        # Note
        note = Text(
            "\"互为\"表示两个角的关系",
            font=FONT, font_size=20, color=COLOR_ACCENT
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.wait(1.0)

        self.comp_elements = VGroup(
            title, line_h, line_v, line_m, ra_mark,
            arc_a, arc_b, label_a, label_b,
            deg_a_text, deg_b_text,
            defn1, defn2, formula, box, note
        )
        self._clear(self.comp_elements)

    # ------------------------------------------------------------------
    # Scene 3: 余角计算练习
    # ------------------------------------------------------------------

    def scene_3_complementary_practice(self):
        title = self._section_title("余角计算", color=COLOR_ANGLE_A, y=5.5)
        self.play(Write(title), run_time=0.5)

        q = Text(
            "已知 \u22201 = 52\u00b0, 求 \u22201 的余角",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(FadeIn(q), run_time=0.5)

        # Step by step
        s1 = MathTex(r"\angle 1 + \angle 2 = 90^\circ", font_size=32, color=WHITE).move_to(UP * 2.5)
        self.play(Write(s1), run_time=0.6)

        s2 = MathTex(r"\angle 2 = 90^\circ - 52^\circ", font_size=32, color=WHITE).move_to(UP * 1.3)
        self.play(Write(s2), run_time=0.6)

        s3 = MathTex(r"\angle 2 = 38^\circ", font_size=36, color=COLOR_RESULT).move_to(UP * 0.0)
        box_ans = SurroundingRectangle(s3, color=COLOR_RESULT, buff=0.2, corner_radius=0.1)
        self.play(Write(s3), Create(box_ans), run_time=0.6)
        self.wait(1.2)

        # Quick second example
        q2 = Text(
            "想一想: 45\u00b0 的余角是多少?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(q2), run_time=0.5)
        self.wait(0.8)

        ans2 = MathTex(r"90^\circ - 45^\circ = 45^\circ", font_size=30, color=COLOR_RESULT).move_to(DOWN * 3.3)
        note2 = Text(
            "45\u00b0 的余角还是 45\u00b0!",
            font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(DOWN * 4.3)
        self.play(Write(ans2), run_time=0.5)
        self.play(FadeIn(note2), run_time=0.4)
        self.wait(1.0)

        self._clear(title, q, s1, s2, s3, box_ans, q2, ans2, note2)

    # ------------------------------------------------------------------
    # Scene 4: 补角定义
    # ------------------------------------------------------------------

    def scene_4_supplementary_def(self):
        title = self._section_title("二、补角", color=COLOR_ANGLE_B)
        self.play(Write(title), run_time=0.6)

        # 180-degree straight angle with two sub-angles
        vertex = np.array([0, 2.5, 0])
        ray_left = vertex + np.array([-3.5, 0, 0])
        ray_right = vertex + np.array([3.5, 0, 0])

        # Dividing ray at 130 degrees from positive-x direction
        angle_split_rad = np.radians(130)
        ray_mid_len = 3.0
        ray_mid = vertex + ray_mid_len * np.array([np.cos(angle_split_rad), np.sin(angle_split_rad), 0])

        line_base = Line(ray_left, ray_right, color=COLOR_LINE, stroke_width=3)
        line_m = Line(vertex, ray_mid, color=COLOR_HL, stroke_width=3)

        self.play(Create(line_base), run_time=0.5)

        # angle A (blue) from 0 to split = 130 degrees
        arc_a = Arc(
            radius=0.8, start_angle=0, angle=angle_split_rad,
            arc_center=vertex, color=COLOR_ANGLE_A, stroke_width=3
        )
        label_a = MathTex(r"\angle 1", color=COLOR_ANGLE_A, font_size=28).move_to(
            vertex + 1.1 * np.array([np.cos(angle_split_rad / 2), np.sin(angle_split_rad / 2), 0])
        )

        # angle B (orange) from split to 180 = 50 degrees
        angle_b_val = np.pi - angle_split_rad
        arc_b = Arc(
            radius=0.7, start_angle=angle_split_rad, angle=angle_b_val,
            arc_center=vertex, color=COLOR_ANGLE_B, stroke_width=3
        )
        label_b = MathTex(r"\angle 2", color=COLOR_ANGLE_B, font_size=28).move_to(
            vertex + 1.05 * np.array([np.cos(angle_split_rad + angle_b_val / 2),
                                       np.sin(angle_split_rad + angle_b_val / 2), 0])
        )

        self.play(Create(line_m), run_time=0.6)
        self.play(Create(arc_a), FadeIn(label_a), run_time=0.6)
        self.play(Create(arc_b), FadeIn(label_b), run_time=0.6)

        # Degree labels
        deg_a_text = MathTex(r"130^\circ", color=COLOR_ANGLE_A, font_size=24).move_to(
            vertex + 1.55 * np.array([np.cos(angle_split_rad / 2), np.sin(angle_split_rad / 2), 0])
        )
        deg_b_text = MathTex(r"50^\circ", color=COLOR_ANGLE_B, font_size=24).move_to(
            vertex + 1.45 * np.array([np.cos(angle_split_rad + angle_b_val / 2),
                                       np.sin(angle_split_rad + angle_b_val / 2), 0])
        )
        self.play(FadeIn(deg_a_text), FadeIn(deg_b_text), run_time=0.5)

        # Straight angle indicator
        straight_lbl = MathTex(r"180^\circ", font_size=22, color=COLOR_LINE).move_to(
            vertex + DOWN * 0.5
        )
        self.play(FadeIn(straight_lbl), run_time=0.3)

        # Definition
        defn1 = Text(
            "如果两个角的和等于 180\u00b0",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 0.8)
        defn2 = Text(
            "那么这两个角互为补角",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(defn1), run_time=0.5)
        self.play(FadeIn(defn2), run_time=0.5)

        # Formula
        formula = MathTex(
            r"\angle 1 + \angle 2 = 180^\circ",
            color=COLOR_RESULT, font_size=36
        ).move_to(DOWN * 3.0)
        box = SurroundingRectangle(formula, color=COLOR_RESULT, buff=0.25, corner_radius=0.1)

        self.play(Write(formula), Create(box), run_time=0.7)
        self.wait(1.5)

        # comparison note
        compare = Text(
            "余角之和 90\u00b0  vs  补角之和 180\u00b0",
            font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(compare, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.supp_elements = VGroup(
            title, line_base, line_m,
            arc_a, arc_b, label_a, label_b,
            deg_a_text, deg_b_text, straight_lbl,
            defn1, defn2, formula, box, compare
        )
        self._clear(self.supp_elements)

    # ------------------------------------------------------------------
    # Scene 5: 补角计算练习
    # ------------------------------------------------------------------

    def scene_5_supplementary_practice(self):
        title = self._section_title("补角计算", color=COLOR_ANGLE_B, y=5.5)
        self.play(Write(title), run_time=0.5)

        q = Text(
            "已知 \u22201 = 75\u00b0, 求 \u22201 的补角",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(FadeIn(q), run_time=0.5)

        s1 = MathTex(r"\angle 1 + \angle 2 = 180^\circ", font_size=32, color=WHITE).move_to(UP * 2.5)
        self.play(Write(s1), run_time=0.6)

        s2 = MathTex(r"\angle 2 = 180^\circ - 75^\circ", font_size=32, color=WHITE).move_to(UP * 1.3)
        self.play(Write(s2), run_time=0.6)

        s3 = MathTex(r"\angle 2 = 105^\circ", font_size=36, color=COLOR_RESULT).move_to(UP * 0.0)
        box_ans = SurroundingRectangle(s3, color=COLOR_RESULT, buff=0.2, corner_radius=0.1)
        self.play(Write(s3), Create(box_ans), run_time=0.6)
        self.wait(1.2)

        # Extra question
        q2 = Text(
            "想一想: 90\u00b0 的补角是多少?",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(q2), run_time=0.5)
        self.wait(0.8)

        ans2 = MathTex(r"180^\circ - 90^\circ = 90^\circ", font_size=30, color=COLOR_RESULT).move_to(DOWN * 3.3)
        note2 = Text(
            "90\u00b0 的补角是 90\u00b0, 也就是直角!",
            font=FONT, font_size=20, color=COLOR_ACCENT
        ).move_to(DOWN * 4.3)
        self.play(Write(ans2), run_time=0.5)
        self.play(FadeIn(note2), run_time=0.4)
        self.wait(1.0)

        self._clear(title, q, s1, s2, s3, box_ans, q2, ans2, note2)

    # ------------------------------------------------------------------
    # Scene 6: 对顶角定义
    # ------------------------------------------------------------------

    def scene_6_vertical_angles_def(self):
        title = self._section_title("三、对顶角", color=COLOR_VERT_1)
        self.play(Write(title), run_time=0.6)

        # Two intersecting lines
        origin = np.array([0, 2.0, 0])
        angle1 = np.radians(25)   # line 1 tilt
        angle2 = np.radians(140)  # line 2 tilt
        length = 3.2

        p1 = origin + length * np.array([np.cos(angle1), np.sin(angle1), 0])
        p2 = origin - length * np.array([np.cos(angle1), np.sin(angle1), 0])
        p3 = origin + length * np.array([np.cos(angle2), np.sin(angle2), 0])
        p4 = origin - length * np.array([np.cos(angle2), np.sin(angle2), 0])

        line1 = Line(p2, p1, color=COLOR_LINE, stroke_width=3)
        line2 = Line(p4, p3, color=COLOR_LINE, stroke_width=3)

        self.play(Create(line1), Create(line2), run_time=0.8)

        # Label the vertex
        o_dot = Dot(origin, color=WHITE, radius=0.06)
        o_label = Text("O", font=FONT, font_size=20, color=WHITE).next_to(o_dot, DOWN + LEFT, buff=0.15)
        self.play(FadeIn(o_dot), FadeIn(o_label), run_time=0.3)

        # Four angles:
        # angle1 (between line1+ and line2+): from angle1 to angle2 CCW
        # angle2 (between line2+ and line1-): from angle2 to angle1+pi CCW
        # angle3 (between line1- and line2-): from angle1+pi to angle2+pi CCW  (= angle1)
        # angle4 (between line2- and line1+): from angle2+pi to angle1+2pi CCW (= angle2)

        a1_start = angle1
        a1_sweep = angle2 - angle1   # ~115 deg

        a2_start = angle2
        a2_sweep = (angle1 + np.pi) - angle2  # ~65 deg

        a3_start = angle1 + np.pi
        a3_sweep = (angle2 + np.pi) - (angle1 + np.pi)  # same as a1_sweep

        a4_start = angle2 + np.pi
        a4_sweep = (angle1 + 2 * np.pi) - (angle2 + np.pi)  # same as a2_sweep

        # Draw angle arcs: pair 1 (pink), pair 2 (green)
        arc1 = Arc(radius=0.6, start_angle=a1_start, angle=a1_sweep,
                   arc_center=origin, color=COLOR_VERT_1, stroke_width=3)
        arc3 = Arc(radius=0.6, start_angle=a3_start, angle=a3_sweep,
                   arc_center=origin, color=COLOR_VERT_1, stroke_width=3)

        arc2 = Arc(radius=0.5, start_angle=a2_start, angle=a2_sweep,
                   arc_center=origin, color=COLOR_VERT_2, stroke_width=3)
        arc4 = Arc(radius=0.5, start_angle=a4_start, angle=a4_sweep,
                   arc_center=origin, color=COLOR_VERT_2, stroke_width=3)

        # Labels
        def angle_label_pos(start, sweep, r=1.0):
            mid = start + sweep / 2
            return origin + r * np.array([np.cos(mid), np.sin(mid), 0])

        lbl1 = MathTex(r"\angle 1", color=COLOR_VERT_1, font_size=26).move_to(angle_label_pos(a1_start, a1_sweep))
        lbl3 = MathTex(r"\angle 3", color=COLOR_VERT_1, font_size=26).move_to(angle_label_pos(a3_start, a3_sweep))
        lbl2 = MathTex(r"\angle 2", color=COLOR_VERT_2, font_size=26).move_to(angle_label_pos(a2_start, a2_sweep, 0.95))
        lbl4 = MathTex(r"\angle 4", color=COLOR_VERT_2, font_size=26).move_to(angle_label_pos(a4_start, a4_sweep, 0.95))

        # Animate pairs
        self.play(Create(arc1), FadeIn(lbl1), run_time=0.5)
        self.play(Create(arc3), FadeIn(lbl3), run_time=0.5)
        self.play(
            arc1.animate.set_stroke(width=5),
            arc3.animate.set_stroke(width=5),
            run_time=0.4
        )

        pair1_note = Text(
            "\u22201 和 \u22203 是对顶角",
            font=FONT, font_size=22, color=COLOR_VERT_1
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(pair1_note), run_time=0.4)
        self.wait(0.6)

        self.play(Create(arc2), FadeIn(lbl2), run_time=0.5)
        self.play(Create(arc4), FadeIn(lbl4), run_time=0.5)
        self.play(
            arc2.animate.set_stroke(width=5),
            arc4.animate.set_stroke(width=5),
            run_time=0.4
        )

        pair2_note = Text(
            "\u22202 和 \u22204 也是对顶角",
            font=FONT, font_size=22, color=COLOR_VERT_2
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(pair2_note), run_time=0.4)
        self.wait(0.6)

        # reset stroke
        self.play(
            arc1.animate.set_stroke(width=3),
            arc3.animate.set_stroke(width=3),
            arc2.animate.set_stroke(width=3),
            arc4.animate.set_stroke(width=3),
            run_time=0.3
        )

        # Definition
        defn = Text(
            "对顶角: 两边互为反向延长线",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 3.2)

        prop = Text(
            "性质: 对顶角相等",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 4.2)
        box_prop = SurroundingRectangle(prop, color=COLOR_HL, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(defn), run_time=0.5)
        self.play(Write(prop), Create(box_prop), run_time=0.6)
        self.wait(1.5)

        self.vert_elements = VGroup(
            title, line1, line2, o_dot, o_label,
            arc1, arc2, arc3, arc4,
            lbl1, lbl2, lbl3, lbl4,
            pair1_note, pair2_note,
            defn, prop, box_prop
        )

        # Store geometry info for next scene
        self.vert_origin = origin
        self.vert_a1_start = a1_start
        self.vert_a1_sweep = a1_sweep
        self.vert_a2_start = a2_start
        self.vert_a2_sweep = a2_sweep
        self.vert_line1 = line1
        self.vert_line2 = line2
        self.vert_o_dot = o_dot

        self._clear(self.vert_elements)

    # ------------------------------------------------------------------
    # Scene 7: 对顶角相等的推理
    # ------------------------------------------------------------------

    def scene_7_vertical_angles_proof(self):
        title = self._section_title("为什么对顶角相等?", color=COLOR_HL)
        self.play(Write(title), run_time=0.6)

        # Re-draw simpler intersecting lines
        origin = np.array([0, 2.5, 0])
        angle1 = np.radians(20)
        angle2 = np.radians(145)
        length = 2.8

        p1 = origin + length * np.array([np.cos(angle1), np.sin(angle1), 0])
        p2 = origin - length * np.array([np.cos(angle1), np.sin(angle1), 0])
        p3 = origin + length * np.array([np.cos(angle2), np.sin(angle2), 0])
        p4 = origin - length * np.array([np.cos(angle2), np.sin(angle2), 0])

        line1 = Line(p2, p1, color=COLOR_LINE, stroke_width=3)
        line2 = Line(p4, p3, color=COLOR_LINE, stroke_width=3)
        self.play(Create(line1), Create(line2), run_time=0.6)

        a1_sweep = angle2 - angle1  # ~125 deg
        a2_sweep = (angle1 + np.pi) - angle2  # ~55 deg

        arc1 = Arc(radius=0.55, start_angle=angle1, angle=a1_sweep,
                   arc_center=origin, color=COLOR_VERT_1, stroke_width=3)
        arc2 = Arc(radius=0.45, start_angle=angle2, angle=a2_sweep,
                   arc_center=origin, color=COLOR_VERT_2, stroke_width=3)

        lbl1 = MathTex(r"\angle 1", color=COLOR_VERT_1, font_size=24).move_to(
            origin + 0.9 * np.array([np.cos(angle1 + a1_sweep / 2), np.sin(angle1 + a1_sweep / 2), 0])
        )
        lbl2 = MathTex(r"\angle 2", color=COLOR_VERT_2, font_size=24).move_to(
            origin + 0.85 * np.array([np.cos(angle2 + a2_sweep / 2), np.sin(angle2 + a2_sweep / 2), 0])
        )

        # angle 3 = angle from angle1+pi to angle2+pi (same measure as angle1)
        arc3 = Arc(radius=0.55, start_angle=angle1 + np.pi, angle=a1_sweep,
                   arc_center=origin, color=COLOR_VERT_1, stroke_width=3, stroke_opacity=0.4)

        self.play(Create(arc1), FadeIn(lbl1), Create(arc2), FadeIn(lbl2), Create(arc3), run_time=0.7)

        # Reasoning: angle1 + angle2 = 180 (supplementary on a straight line)
        proof_y = -0.3
        step1_cn = Text("因为 \u22201 和 \u22202 构成平角:", font=FONT, font_size=22, color=WHITE).move_to(UP * proof_y)
        step1_eq = MathTex(r"\angle 1 + \angle 2 = 180^\circ", font_size=30, color=WHITE).move_to(UP * (proof_y - 0.9))

        self.play(FadeIn(step1_cn), run_time=0.5)
        self.play(Write(step1_eq), run_time=0.6)

        step2_cn = Text("同理 \u22202 和 \u22203 也构成平角:", font=FONT, font_size=22, color=WHITE).move_to(UP * (proof_y - 2.0))
        step2_eq = MathTex(r"\angle 2 + \angle 3 = 180^\circ", font_size=30, color=WHITE).move_to(UP * (proof_y - 2.9))

        self.play(FadeIn(step2_cn), run_time=0.5)
        self.play(Write(step2_eq), run_time=0.6)

        step3_cn = Text("两式相减:", font=FONT, font_size=22, color=WHITE).move_to(UP * (proof_y - 4.0))
        step3_eq = MathTex(r"\angle 1 - \angle 3 = 0", font_size=30, color=WHITE).move_to(UP * (proof_y - 4.9))

        self.play(FadeIn(step3_cn), run_time=0.5)
        self.play(Write(step3_eq), run_time=0.6)

        conclusion = MathTex(r"\angle 1 = \angle 3", font_size=38, color=COLOR_HL).move_to(UP * (proof_y - 6.2))
        box_c = SurroundingRectangle(conclusion, color=COLOR_HL, buff=0.2, corner_radius=0.1)

        self.play(Write(conclusion), Create(box_c), run_time=0.7)
        self.play(Flash(conclusion, color=COLOR_HL, flash_radius=0.5), run_time=0.5)
        self.wait(1.5)

        all_proof = VGroup(
            title, line1, line2,
            arc1, arc2, arc3, lbl1, lbl2,
            step1_cn, step1_eq, step2_cn, step2_eq,
            step3_cn, step3_eq, conclusion, box_c
        )
        self._clear(all_proof)

    # ------------------------------------------------------------------
    # Scene 8: 综合练习
    # ------------------------------------------------------------------

    def scene_8_combined_practice(self):
        title = self._section_title("综合练习", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        # Problem: Two lines intersect. One angle = 70 degrees.
        # Find the other three angles.
        q = Text(
            "两直线相交, 其中一个角为 70\u00b0",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.2)
        q2 = Text(
            "求其余三个角",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.4)
        self.play(FadeIn(q), FadeIn(q2), run_time=0.6)

        # Draw figure
        origin = np.array([0, 1.2, 0])
        a1 = np.radians(0)
        a2 = np.radians(70)
        length = 2.5

        p1 = origin + length * np.array([np.cos(a1), np.sin(a1), 0])
        p2 = origin - length * np.array([np.cos(a1), np.sin(a1), 0])
        p3 = origin + length * np.array([np.cos(a2), np.sin(a2), 0])
        p4 = origin - length * np.array([np.cos(a2), np.sin(a2), 0])

        l1 = Line(p2, p1, color=COLOR_LINE, stroke_width=3)
        l2 = Line(p4, p3, color=COLOR_LINE, stroke_width=3)
        self.play(Create(l1), Create(l2), run_time=0.6)

        # angle arcs
        arc_70 = Arc(radius=0.55, start_angle=a1, angle=np.radians(70),
                     arc_center=origin, color=COLOR_VERT_1, stroke_width=3)
        lbl_70 = MathTex(r"70^\circ", color=COLOR_VERT_1, font_size=22).move_to(
            origin + 0.9 * np.array([np.cos(np.radians(35)), np.sin(np.radians(35)), 0])
        )
        self.play(Create(arc_70), FadeIn(lbl_70), run_time=0.5)

        # Step 1: supplementary angle
        step_y = -1.0
        s1_cn = Text(
            "邻补角 (补角关系):",
            font=FONT, font_size=22, color=COLOR_ANGLE_B
        ).move_to(UP * step_y)
        s1_eq = MathTex(r"180^\circ - 70^\circ = 110^\circ", font_size=30, color=WHITE).move_to(UP * (step_y - 0.8))

        arc_110 = Arc(radius=0.45, start_angle=np.radians(70), angle=np.radians(110),
                      arc_center=origin, color=COLOR_VERT_2, stroke_width=3)
        lbl_110 = MathTex(r"110^\circ", color=COLOR_VERT_2, font_size=20).move_to(
            origin + 0.85 * np.array([np.cos(np.radians(125)), np.sin(np.radians(125)), 0])
        )
        self.play(FadeIn(s1_cn), Write(s1_eq), Create(arc_110), FadeIn(lbl_110), run_time=0.8)

        # Step 2: vertical angle
        s2_cn = Text(
            "对顶角 (相等):",
            font=FONT, font_size=22, color=COLOR_VERT_1
        ).move_to(UP * (step_y - 1.9))
        s2_eq = MathTex(r"70^\circ", font_size=30, color=COLOR_VERT_1).move_to(UP * (step_y - 2.7))

        arc_70b = Arc(radius=0.55, start_angle=np.radians(180), angle=np.radians(70),
                      arc_center=origin, color=COLOR_VERT_1, stroke_width=3)
        lbl_70b = MathTex(r"70^\circ", color=COLOR_VERT_1, font_size=20).move_to(
            origin + 0.9 * np.array([np.cos(np.radians(215)), np.sin(np.radians(215)), 0])
        )
        self.play(FadeIn(s2_cn), Write(s2_eq), Create(arc_70b), FadeIn(lbl_70b), run_time=0.8)

        # Step 3: last angle
        s3_cn = Text(
            "最后一个 (对顶角):",
            font=FONT, font_size=22, color=COLOR_VERT_2
        ).move_to(UP * (step_y - 3.6))
        s3_eq = MathTex(r"110^\circ", font_size=30, color=COLOR_VERT_2).move_to(UP * (step_y - 4.4))

        arc_110b = Arc(radius=0.45, start_angle=np.radians(250), angle=np.radians(110),
                       arc_center=origin, color=COLOR_VERT_2, stroke_width=3)
        lbl_110b = MathTex(r"110^\circ", color=COLOR_VERT_2, font_size=20).move_to(
            origin + 0.85 * np.array([np.cos(np.radians(305)), np.sin(np.radians(305)), 0])
        )
        self.play(FadeIn(s3_cn), Write(s3_eq), Create(arc_110b), FadeIn(lbl_110b), run_time=0.8)
        self.wait(1.0)

        # Conclusion
        ans_text = Text(
            "四个角: 70\u00b0, 110\u00b0, 70\u00b0, 110\u00b0",
            font=FONT, font_size=24, color=COLOR_RESULT
        ).move_to(DOWN * 6.5)
        box_ans = SurroundingRectangle(ans_text, color=COLOR_RESULT, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(ans_text), Create(box_ans), run_time=0.6)
        self.wait(1.5)

        all_elems = VGroup(
            title, q, q2, l1, l2,
            arc_70, lbl_70, arc_110, lbl_110,
            arc_70b, lbl_70b, arc_110b, lbl_110b,
            s1_cn, s1_eq, s2_cn, s2_eq, s3_cn, s3_eq,
            ans_text, box_ans
        )
        self._clear(all_elems)

    # ------------------------------------------------------------------
    # Scene 9: 总结
    # ------------------------------------------------------------------

    def scene_9_summary(self):
        title = self._section_title("总结", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        cards_data = [
            ("余角", r"\angle A + \angle B = 90^\circ", COLOR_ANGLE_A, "两角之和为 90\u00b0"),
            ("补角", r"\angle A + \angle B = 180^\circ", COLOR_ANGLE_B, "两角之和为 180\u00b0"),
            ("对顶角", r"\angle 1 = \angle 3", COLOR_VERT_1, "两线相交, 对顶角相等"),
        ]

        cards = VGroup()
        for i, (name, formula_str, color, desc) in enumerate(cards_data):
            y_pos = 3.5 - i * 2.8

            # colored bar
            bar = Line(LEFT * 3.5, LEFT * 3.5 + UP * 1.8, color=color, stroke_width=6).move_to(
                LEFT * 3.3 + UP * y_pos
            )

            name_text = Text(name, font=FONT, font_size=30, color=color).move_to(
                LEFT * 1.5 + UP * (y_pos + 0.5)
            )

            formula_mob = MathTex(formula_str, font_size=30, color=WHITE).move_to(
                RIGHT * 0.5 + UP * (y_pos + 0.5)
            )

            desc_text = Text(desc, font=FONT, font_size=20, color=GRAY_A).move_to(
                UP * (y_pos - 0.3)
            )

            card = VGroup(bar, name_text, formula_mob, desc_text)
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.7)

        self.wait(0.5)

        # Key insight
        key = Text(
            "记住口诀:",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        mnemonic = Text(
            "余九补十八, 对顶角相等",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        box_m = SurroundingRectangle(mnemonic, color=COLOR_HL, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(key), run_time=0.4)
        self.play(Write(mnemonic), Create(box_m), run_time=0.7)
        self.wait(2.0)

        self._clear(title, cards, key, mnemonic, box_m)

    # ------------------------------------------------------------------
    # Scene 10: 片尾
    # ------------------------------------------------------------------

    def scene_10_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=COLOR_AUTHOR
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_big),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.6)

        # Small decorative angle icon
        deco_origin = np.array([0, -3.0, 0])
        deco_l1 = Line(deco_origin, deco_origin + np.array([1.5, 0, 0]), color=COLOR_ANGLE_A, stroke_width=3)
        deco_l2 = Line(deco_origin, deco_origin + np.array([1.0, 1.2, 0]), color=COLOR_ANGLE_B, stroke_width=3)
        deco_arc = Arc(radius=0.5, start_angle=0, angle=np.arctan2(1.2, 1.0),
                       arc_center=deco_origin, color=COLOR_HL, stroke_width=2)
        deco = VGroup(deco_l1, deco_l2, deco_arc)

        self.play(Create(deco), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=1.0
        )


# ======================================================================
if __name__ == "__main__":
    pass
