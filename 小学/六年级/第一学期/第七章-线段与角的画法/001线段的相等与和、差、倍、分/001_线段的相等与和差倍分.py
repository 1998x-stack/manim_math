"""
001_线段的相等与和差倍分.py — 线段的相等与和、差、倍、分 教学动画

知识点: 线段相等的画法(尺规作图)、线段的和差倍分
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 线段相等——用圆规截取等长线段
  3. 线段的和 (EF = AB + CD)
  4. 线段的差 (EF = AB - CD)
  5. 线段的倍 (CD = 2AB)
  6. 线段的分 (CD = AB/2 即中点)
  7. 综合练习
  8. 总结
  9. 片尾
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
COLOR_SEG_A = "#3b82f6"       # 蓝色 线段AB
COLOR_SEG_B = "#f59e0b"       # 橙色 线段CD
COLOR_RESULT = "#22c55e"      # 绿色 结果线段
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_COMPASS = "#ef4444"     # 红色 圆规弧
COLOR_AUTHOR = "#6b7280"      # 灰色
COLOR_RAY = "#94a3b8"         # 射线颜色
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class SegmentRelationsLesson(Scene):
    """
    线段的相等与和、差、倍、分 教学动画
    场景顺序:
      1. 开场钩子
      2. 线段相等——用圆规截取
      3. 线段的和 (EF = AB + CD)
      4. 线段的差 (EF = AB - CD)
      5. 线段的倍 (CD = 2AB)
      6. 线段的分 (CD = AB/2)
      7. 综合练习
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_equal_segment()
        self.scene_3_segment_sum()
        self.scene_4_segment_diff()
        self.scene_5_segment_multiple()
        self.scene_6_segment_division()
        self.scene_7_practice()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子
        hook1 = Text(
            "线段也能做加减乘除?",
            font=FONT, font_size=38, color=COLOR_HL
        ).move_to(UP * 5.0)

        hook2 = Text(
            "尺规作图的基本功!",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.0)

        self.play(Write(hook1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 展示一把尺子和圆规图示（简化为线段和弧）
        ruler = Rectangle(
            width=5, height=0.3, color=WHITE, fill_opacity=0.15,
            stroke_width=2
        ).move_to(UP * 1.5)

        # 圆规示意 — 两条线组成V字
        compass_leg1 = Line(ORIGIN, DOWN * 1.8 + LEFT * 0.4, color=COLOR_COMPASS, stroke_width=3)
        compass_leg2 = Line(ORIGIN, DOWN * 1.8 + RIGHT * 0.4, color=COLOR_COMPASS, stroke_width=3)
        compass_group = VGroup(compass_leg1, compass_leg2).move_to(DOWN * 0.5)
        compass_arc = Arc(
            radius=0.8, start_angle=PI * 0.65, angle=-PI * 0.3,
            color=COLOR_COMPASS, stroke_width=2
        ).move_to(compass_group.get_bottom() + UP * 0.2)

        self.play(
            FadeIn(ruler),
            Create(compass_group),
            Create(compass_arc),
            run_time=1.0
        )
        self.wait(1.0)

        # 标题
        title = Text(
            "线段的相等与和、差、倍、分",
            font=FONT, font_size=32, color=GOLD
        ).move_to(DOWN * 3.0)

        self.play(Write(title), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(ruler), FadeOut(compass_group), FadeOut(compass_arc),
            FadeOut(title),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 线段相等 — 用圆规截取
    # ------------------------------------------------------------------

    def scene_2_equal_segment(self):
        sec_title = Text(
            "一、画一条线段等于已知线段",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.7)

        # 已知线段 AB
        seg_len_ab = 3.0  # 逻辑长度
        pt_A = np.array([-3.5, 3.5, 0])
        pt_B = pt_A + np.array([seg_len_ab, 0, 0])

        seg_AB = Line(pt_A, pt_B, color=COLOR_SEG_A, stroke_width=4)
        dot_A = Dot(pt_A, color=WHITE, radius=0.06)
        dot_B = Dot(pt_B, color=WHITE, radius=0.06)
        label_A = MathTex("A", font_size=24, color=WHITE).next_to(pt_A, DOWN, buff=0.15)
        label_B = MathTex("B", font_size=24, color=WHITE).next_to(pt_B, DOWN, buff=0.15)

        known_text = Text("已知线段 AB", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 4.6)

        self.play(FadeIn(known_text), run_time=0.3)
        self.play(
            Create(seg_AB), FadeIn(dot_A), FadeIn(dot_B),
            Write(label_A), Write(label_B),
            run_time=0.8
        )
        self.wait(0.5)

        # 步骤 1: 画射线
        step1 = Text("步骤1: 画一条射线", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 1.5)
        self.play(FadeIn(step1), run_time=0.4)

        ray_start = np.array([-3.5, 0.5, 0])
        ray_end = ray_start + np.array([7.0, 0, 0])

        ray = Line(ray_start, ray_end, color=COLOR_RAY, stroke_width=2)
        # Arrow tip at the end
        ray_arrow = Arrow(
            ray_end - np.array([0.5, 0, 0]), ray_end,
            color=COLOR_RAY, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.3
        )

        dot_C = Dot(ray_start, color=WHITE, radius=0.06)
        label_C = MathTex("C", font_size=24, color=WHITE).next_to(ray_start, DOWN, buff=0.15)

        self.play(Create(ray), FadeIn(ray_arrow), FadeIn(dot_C), Write(label_C), run_time=0.8)
        self.wait(0.3)

        # 步骤 2: 圆规量取 AB 长度
        step2 = Text(
            "步骤2: 用圆规量取 AB 的长度",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 1.5)

        self.play(ReplacementTransform(step1, step2), run_time=0.4)

        # 在 AB 上画弧示意量取
        compass_arc_ab = Arc(
            radius=seg_len_ab, start_angle=PI * 0.05, angle=-PI * 0.1,
            color=COLOR_COMPASS, stroke_width=2.5
        ).move_to(pt_A + RIGHT * seg_len_ab / 2 + DOWN * 0.2)
        # flash A
        self.play(
            Flash(dot_A, color=COLOR_COMPASS, flash_radius=0.3, run_time=0.4),
        )
        self.play(Create(compass_arc_ab), run_time=0.6)
        self.wait(0.3)

        # 步骤 3: 在射线上截取
        step3 = Text(
            "步骤3: 在射线上截取 CD = AB",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 1.5)
        self.play(ReplacementTransform(step2, step3), run_time=0.4)

        # 截取点 D
        pt_D = ray_start + np.array([seg_len_ab, 0, 0])
        dot_D = Dot(pt_D, color=WHITE, radius=0.06)
        label_D = MathTex("D", font_size=24, color=WHITE).next_to(pt_D, DOWN, buff=0.15)

        # 画弧: 从 C 出发到 D
        compass_arc_cd = Arc(
            radius=seg_len_ab,
            start_angle=PI * 0.08,
            angle=-PI * 0.16,
            arc_center=ray_start,
            color=COLOR_COMPASS,
            stroke_width=2.5
        )

        self.play(Create(compass_arc_cd), run_time=0.8)
        self.play(FadeIn(dot_D), Write(label_D), run_time=0.4)

        # 标记 CD 变色
        seg_CD = Line(ray_start, pt_D, color=COLOR_RESULT, stroke_width=5)
        self.play(Create(seg_CD), run_time=0.5)

        # 等长标记
        tick_ab = self._tick_mark(pt_A, pt_B, COLOR_SEG_A)
        tick_cd = self._tick_mark(ray_start, pt_D, COLOR_RESULT)

        self.play(FadeIn(tick_ab), FadeIn(tick_cd), run_time=0.4)

        # 结论
        result_tex = MathTex(r"CD = AB", font_size=32, color=COLOR_RESULT).move_to(DOWN * 2.0)
        self.play(Write(result_tex), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            *[FadeOut(m) for m in [
                sec_title, known_text,
                seg_AB, dot_A, dot_B, label_A, label_B,
                ray, ray_arrow, dot_C, label_C,
                compass_arc_ab, compass_arc_cd,
                seg_CD, dot_D, label_D,
                tick_ab, tick_cd,
                result_tex, step3
            ]],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 线段的和
    # ------------------------------------------------------------------

    def scene_3_segment_sum(self):
        sec_title = Text(
            "二、线段的和",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.6)

        # 已知 AB 和 CD
        ab_len = 2.5
        cd_len = 1.8

        pt_A = np.array([-3.5, 4.0, 0])
        pt_B = pt_A + RIGHT * ab_len
        seg_AB = Line(pt_A, pt_B, color=COLOR_SEG_A, stroke_width=4)
        lab_A = MathTex("A", font_size=22).next_to(pt_A, DOWN, buff=0.12)
        lab_B = MathTex("B", font_size=22).next_to(pt_B, DOWN, buff=0.12)
        ab_brace = Brace(seg_AB, UP, buff=0.1, color=COLOR_SEG_A)
        ab_brace_lab = MathTex("AB", font_size=22, color=COLOR_SEG_A).next_to(ab_brace, UP, buff=0.08)

        pt_C = np.array([0.5, 4.0, 0])
        pt_D = pt_C + RIGHT * cd_len
        seg_CD = Line(pt_C, pt_D, color=COLOR_SEG_B, stroke_width=4)
        lab_C = MathTex("C", font_size=22).next_to(pt_C, DOWN, buff=0.12)
        lab_D = MathTex("D", font_size=22).next_to(pt_D, DOWN, buff=0.12)
        cd_brace = Brace(seg_CD, UP, buff=0.1, color=COLOR_SEG_B)
        cd_brace_lab = MathTex("CD", font_size=22, color=COLOR_SEG_B).next_to(cd_brace, UP, buff=0.08)

        self.play(
            Create(seg_AB), Write(lab_A), Write(lab_B),
            FadeIn(ab_brace), FadeIn(ab_brace_lab),
            run_time=0.7
        )
        self.play(
            Create(seg_CD), Write(lab_C), Write(lab_D),
            FadeIn(cd_brace), FadeIn(cd_brace_lab),
            run_time=0.7
        )
        self.wait(0.3)

        # 画射线
        task_text = Text(
            "画线段 EF = AB + CD",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 2.2)
        self.play(FadeIn(task_text), run_time=0.5)

        ray_origin = np.array([-3.5, 0.8, 0])
        ray_tip = ray_origin + RIGHT * 7.0

        ray_line = Line(ray_origin, ray_tip, color=COLOR_RAY, stroke_width=2)
        ray_arr = Arrow(
            ray_tip - RIGHT * 0.5, ray_tip,
            color=COLOR_RAY, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        dot_E = Dot(ray_origin, color=WHITE, radius=0.06)
        lab_E = MathTex("E", font_size=22).next_to(ray_origin, DOWN, buff=0.12)

        self.play(Create(ray_line), FadeIn(ray_arr), FadeIn(dot_E), Write(lab_E), run_time=0.6)

        # 第一步: 截取 EM = AB
        pt_M = ray_origin + RIGHT * ab_len
        arc1 = Arc(
            radius=ab_len, start_angle=PI * 0.06, angle=-PI * 0.12,
            arc_center=ray_origin, color=COLOR_COMPASS, stroke_width=2
        )
        dot_M = Dot(pt_M, color=WHITE, radius=0.06)
        lab_M = MathTex("M", font_size=22).next_to(pt_M, DOWN, buff=0.12)

        step1_text = Text("截取 EM = AB", font=FONT, font_size=20, color=COLOR_SEG_A).move_to(DOWN * 1.0)
        self.play(FadeIn(step1_text), run_time=0.3)
        self.play(Create(arc1), run_time=0.5)
        self.play(FadeIn(dot_M), Write(lab_M), run_time=0.4)

        seg_EM = Line(ray_origin, pt_M, color=COLOR_SEG_A, stroke_width=4)
        self.play(Create(seg_EM), run_time=0.4)

        # 第二步: 截取 MF = CD
        pt_F = pt_M + RIGHT * cd_len
        arc2 = Arc(
            radius=cd_len, start_angle=PI * 0.08, angle=-PI * 0.16,
            arc_center=pt_M, color=COLOR_COMPASS, stroke_width=2
        )
        dot_F = Dot(pt_F, color=WHITE, radius=0.06)
        lab_F = MathTex("F", font_size=22).next_to(pt_F, DOWN, buff=0.12)

        step2_text = Text("截取 MF = CD", font=FONT, font_size=20, color=COLOR_SEG_B).move_to(DOWN * 1.0)
        self.play(ReplacementTransform(step1_text, step2_text), run_time=0.3)
        self.play(Create(arc2), run_time=0.5)
        self.play(FadeIn(dot_F), Write(lab_F), run_time=0.4)

        seg_MF = Line(pt_M, pt_F, color=COLOR_SEG_B, stroke_width=4)
        self.play(Create(seg_MF), run_time=0.4)

        # 结果
        seg_EF = Line(ray_origin, pt_F, color=COLOR_RESULT, stroke_width=5)
        self.play(
            FadeOut(step2_text),
            Create(seg_EF),
            run_time=0.5
        )

        result_eq = MathTex(r"EF = AB + CD", font_size=32, color=COLOR_RESULT).move_to(DOWN * 2.5)
        ef_brace = Brace(seg_EF, DOWN, buff=0.15, color=COLOR_RESULT)
        ef_lab = MathTex("EF", font_size=22, color=COLOR_RESULT).next_to(ef_brace, DOWN, buff=0.08)

        self.play(Write(result_eq), FadeIn(ef_brace), FadeIn(ef_lab), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 线段的差
    # ------------------------------------------------------------------

    def scene_4_segment_diff(self):
        sec_title = Text(
            "三、线段的差",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.6)

        # 已知 AB > CD
        ab_len = 3.2
        cd_len = 1.5

        pt_A = np.array([-3.5, 4.0, 0])
        pt_B = pt_A + RIGHT * ab_len
        seg_AB = Line(pt_A, pt_B, color=COLOR_SEG_A, stroke_width=4)
        lab_A = MathTex("A", font_size=22).next_to(pt_A, DOWN, buff=0.12)
        lab_B = MathTex("B", font_size=22).next_to(pt_B, DOWN, buff=0.12)
        ab_brace = Brace(seg_AB, UP, buff=0.1, color=COLOR_SEG_A)
        ab_lab = MathTex("AB", font_size=22, color=COLOR_SEG_A).next_to(ab_brace, UP, buff=0.08)

        pt_C = np.array([1.0, 4.0, 0])
        pt_D = pt_C + RIGHT * cd_len
        seg_CD = Line(pt_C, pt_D, color=COLOR_SEG_B, stroke_width=4)
        lab_C = MathTex("C", font_size=22).next_to(pt_C, DOWN, buff=0.12)
        lab_D = MathTex("D", font_size=22).next_to(pt_D, DOWN, buff=0.12)
        cd_brace = Brace(seg_CD, UP, buff=0.1, color=COLOR_SEG_B)
        cd_lab = MathTex("CD", font_size=22, color=COLOR_SEG_B).next_to(cd_brace, UP, buff=0.08)

        self.play(
            Create(seg_AB), Write(lab_A), Write(lab_B),
            FadeIn(ab_brace), FadeIn(ab_lab),
            run_time=0.7
        )
        self.play(
            Create(seg_CD), Write(lab_C), Write(lab_D),
            FadeIn(cd_brace), FadeIn(cd_lab),
            run_time=0.7
        )

        cond_text = Text(
            "( AB > CD )", font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 2.8)
        self.play(FadeIn(cond_text), run_time=0.3)

        task_text = Text(
            "画线段 EF = AB - CD",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 2.2)
        self.play(FadeIn(task_text), run_time=0.5)

        # 射线
        ray_origin = np.array([-3.5, 0.8, 0])
        ray_tip = ray_origin + RIGHT * 7.0
        ray_line = Line(ray_origin, ray_tip, color=COLOR_RAY, stroke_width=2)
        ray_arr = Arrow(
            ray_tip - RIGHT * 0.5, ray_tip,
            color=COLOR_RAY, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        dot_E = Dot(ray_origin, color=WHITE, radius=0.06)
        lab_E = MathTex("E", font_size=22).next_to(ray_origin, DOWN, buff=0.12)
        self.play(Create(ray_line), FadeIn(ray_arr), FadeIn(dot_E), Write(lab_E), run_time=0.6)

        # 第一步: 截取 EM = AB (整段)
        pt_M = ray_origin + RIGHT * ab_len
        arc1 = Arc(
            radius=ab_len, start_angle=PI * 0.05, angle=-PI * 0.1,
            arc_center=ray_origin, color=COLOR_COMPASS, stroke_width=2
        )
        dot_M = Dot(pt_M, color=WHITE, radius=0.06)
        lab_M = MathTex("M", font_size=22).next_to(pt_M, DOWN, buff=0.12)

        step1_txt = Text("截取 EM = AB", font=FONT, font_size=20, color=COLOR_SEG_A).move_to(DOWN * 1.0)
        self.play(FadeIn(step1_txt), run_time=0.3)
        self.play(Create(arc1), run_time=0.5)
        self.play(FadeIn(dot_M), Write(lab_M), run_time=0.4)
        seg_EM = Line(ray_origin, pt_M, color=COLOR_SEG_A, stroke_width=4)
        self.play(Create(seg_EM), run_time=0.4)

        # 第二步: 从 M 向 E 方向截取 MF = CD
        pt_F = pt_M + LEFT * cd_len  # 反方向截取
        arc2 = Arc(
            radius=cd_len, start_angle=PI * 0.9, angle=PI * 0.2,
            arc_center=pt_M, color=COLOR_COMPASS, stroke_width=2
        )
        dot_F = Dot(pt_F, color=WHITE, radius=0.06)
        lab_F = MathTex("F", font_size=22).next_to(pt_F, DOWN + LEFT * 0.3, buff=0.12)

        step2_txt = Text(
            "从 M 向 E 截取 MF = CD",
            font=FONT, font_size=20, color=COLOR_SEG_B
        ).move_to(DOWN * 1.0)
        self.play(ReplacementTransform(step1_txt, step2_txt), run_time=0.3)
        self.play(Create(arc2), run_time=0.5)
        self.play(FadeIn(dot_F), Write(lab_F), run_time=0.4)

        # 标出 MF
        seg_MF = Line(pt_M, pt_F, color=COLOR_SEG_B, stroke_width=3)
        self.play(Create(seg_MF), run_time=0.3)

        # 结果 EF
        seg_EF = Line(ray_origin, pt_F, color=COLOR_RESULT, stroke_width=5)
        self.play(FadeOut(step2_txt), Create(seg_EF), run_time=0.5)

        result_eq = MathTex(r"EF = AB - CD", font_size=32, color=COLOR_RESULT).move_to(DOWN * 2.5)
        self.play(Write(result_eq), run_time=0.6)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 线段的倍 (CD = 2AB)
    # ------------------------------------------------------------------

    def scene_5_segment_multiple(self):
        sec_title = Text(
            "四、线段的倍",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.6)

        ab_len = 2.0

        pt_A = np.array([-3.0, 4.0, 0])
        pt_B = pt_A + RIGHT * ab_len
        seg_AB = Line(pt_A, pt_B, color=COLOR_SEG_A, stroke_width=4)
        lab_A = MathTex("A", font_size=22).next_to(pt_A, DOWN, buff=0.12)
        lab_B = MathTex("B", font_size=22).next_to(pt_B, DOWN, buff=0.12)
        ab_brace = Brace(seg_AB, UP, buff=0.1, color=COLOR_SEG_A)
        ab_lab = MathTex("AB", font_size=22, color=COLOR_SEG_A).next_to(ab_brace, UP, buff=0.08)

        self.play(
            Create(seg_AB), Write(lab_A), Write(lab_B),
            FadeIn(ab_brace), FadeIn(ab_lab),
            run_time=0.7
        )

        task_text = Text(
            "画线段 CD = 2AB",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 2.5)
        self.play(FadeIn(task_text), run_time=0.5)

        # 射线
        ray_origin = np.array([-3.5, 1.0, 0])
        ray_tip = ray_origin + RIGHT * 7.5
        ray_line = Line(ray_origin, ray_tip, color=COLOR_RAY, stroke_width=2)
        ray_arr = Arrow(
            ray_tip - RIGHT * 0.5, ray_tip,
            color=COLOR_RAY, stroke_width=2, buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        dot_C = Dot(ray_origin, color=WHITE, radius=0.06)
        lab_C = MathTex("C", font_size=22).next_to(ray_origin, DOWN, buff=0.12)
        self.play(Create(ray_line), FadeIn(ray_arr), FadeIn(dot_C), Write(lab_C), run_time=0.6)

        # 第一次截取 CM = AB
        pt_M = ray_origin + RIGHT * ab_len
        arc1 = Arc(
            radius=ab_len, start_angle=PI * 0.06, angle=-PI * 0.12,
            arc_center=ray_origin, color=COLOR_COMPASS, stroke_width=2
        )
        dot_M = Dot(pt_M, color=WHITE, radius=0.06)
        lab_M = MathTex("M", font_size=22).next_to(pt_M, DOWN, buff=0.12)

        step_txt = Text("第1次: 截取 CM = AB", font=FONT, font_size=20, color=COLOR_SEG_A).move_to(DOWN * 1.0)
        self.play(FadeIn(step_txt), run_time=0.3)
        self.play(Create(arc1), run_time=0.5)
        self.play(FadeIn(dot_M), Write(lab_M), run_time=0.4)

        seg_CM = Line(ray_origin, pt_M, color=COLOR_SEG_A, stroke_width=4)
        self.play(Create(seg_CM), run_time=0.3)

        # 第二次截取 MD = AB
        pt_D = pt_M + RIGHT * ab_len
        arc2 = Arc(
            radius=ab_len, start_angle=PI * 0.06, angle=-PI * 0.12,
            arc_center=pt_M, color=COLOR_COMPASS, stroke_width=2
        )
        dot_D = Dot(pt_D, color=WHITE, radius=0.06)
        lab_D = MathTex("D", font_size=22).next_to(pt_D, DOWN, buff=0.12)

        step2_txt = Text("第2次: 截取 MD = AB", font=FONT, font_size=20, color=COLOR_SEG_A).move_to(DOWN * 1.0)
        self.play(ReplacementTransform(step_txt, step2_txt), run_time=0.3)
        self.play(Create(arc2), run_time=0.5)
        self.play(FadeIn(dot_D), Write(lab_D), run_time=0.4)

        seg_MD = Line(pt_M, pt_D, color=COLOR_SEG_A, stroke_width=4)
        self.play(Create(seg_MD), run_time=0.3)

        # 结果高亮
        seg_CD = Line(ray_origin, pt_D, color=COLOR_RESULT, stroke_width=5)
        self.play(FadeOut(step2_txt), Create(seg_CD), run_time=0.5)

        result_eq = MathTex(r"CD = 2AB", font_size=32, color=COLOR_RESULT).move_to(DOWN * 2.5)

        # 用花括号标注两段
        tick_cm = self._tick_mark(ray_origin, pt_M, COLOR_SEG_A)
        tick_md = self._tick_mark(pt_M, pt_D, COLOR_SEG_A)

        self.play(
            Write(result_eq),
            FadeIn(tick_cm), FadeIn(tick_md),
            run_time=0.6
        )

        explain = Text(
            "截取 2 次 AB 的长度",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 线段的分 (CD = AB/2)
    # ------------------------------------------------------------------

    def scene_6_segment_division(self):
        sec_title = Text(
            "五、线段的等分",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.6)

        ab_len = 4.0

        pt_A = np.array([-3.0, 3.5, 0])
        pt_B = pt_A + RIGHT * ab_len
        seg_AB = Line(pt_A, pt_B, color=COLOR_SEG_A, stroke_width=4)
        dot_A = Dot(pt_A, color=WHITE, radius=0.06)
        dot_B = Dot(pt_B, color=WHITE, radius=0.06)
        lab_A = MathTex("A", font_size=22).next_to(pt_A, DOWN, buff=0.12)
        lab_B = MathTex("B", font_size=22).next_to(pt_B, DOWN, buff=0.12)

        self.play(
            Create(seg_AB), FadeIn(dot_A), FadeIn(dot_B),
            Write(lab_A), Write(lab_B),
            run_time=0.7
        )

        task_text = Text(
            "画线段 AB 的中点 M",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 2.2)
        self.play(FadeIn(task_text), run_time=0.5)

        explain = Text(
            "中点把线段分成相等的两半",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 1.4)
        self.play(FadeIn(explain), run_time=0.4)

        # 中点
        pt_M = (pt_A + pt_B) / 2
        half_len = ab_len / 2

        # 方法: 从两端画等长弧找交点 (简化演示)
        # 从 A 画弧
        arc_from_A = Arc(
            radius=half_len * 1.2,
            start_angle=-PI * 0.15,
            angle=PI * 0.3,
            arc_center=pt_A,
            color=COLOR_COMPASS, stroke_width=2
        )
        # 从 B 画弧
        arc_from_B = Arc(
            radius=half_len * 1.2,
            start_angle=PI * 0.85,
            angle=-PI * 0.3,
            arc_center=pt_B,
            color=COLOR_COMPASS, stroke_width=2
        )

        step1_txt = Text(
            "从 A、B 各画弧 (半径相同)",
            font=FONT, font_size=20, color=COLOR_COMPASS
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(step1_txt), run_time=0.3)
        self.play(Create(arc_from_A), Create(arc_from_B), run_time=0.8)

        # 弧的上交点和下交点 (计算)
        r = half_len * 1.2
        d = ab_len  # A到B的距离
        # 交点 y 偏移: sqrt(r^2 - (d/2)^2)
        y_offset = np.sqrt(r**2 - (d / 2)**2)

        intersection_top = pt_M + UP * y_offset
        intersection_bot = pt_M + DOWN * y_offset

        dot_top = Dot(intersection_top, color=COLOR_COMPASS, radius=0.05)
        dot_bot = Dot(intersection_bot, color=COLOR_COMPASS, radius=0.05)
        self.play(FadeIn(dot_top), FadeIn(dot_bot), run_time=0.3)

        # 连线得到中垂线（仅标记中点）
        perp_line = DashedLine(
            intersection_top, intersection_bot,
            color=COLOR_ACCENT, stroke_width=2, dash_length=0.1
        )
        self.play(Create(perp_line), run_time=0.5)

        dot_M = Dot(pt_M, color=COLOR_RESULT, radius=0.08)
        lab_M = MathTex("M", font_size=24, color=COLOR_RESULT).next_to(pt_M, DOWN, buff=0.15)

        self.play(
            FadeOut(step1_txt),
            FadeIn(dot_M, scale=0.5),
            Write(lab_M),
            run_time=0.5
        )
        self.play(Flash(dot_M, color=COLOR_RESULT, flash_radius=0.3), run_time=0.4)

        # 标注两段相等
        tick_AM = self._tick_mark(pt_A, pt_M, COLOR_RESULT)
        tick_MB = self._tick_mark(pt_M, pt_B, COLOR_RESULT)

        result_grp = VGroup(
            MathTex(r"AM = MB = \frac{1}{2} AB", font_size=28, color=COLOR_RESULT)
        ).move_to(DOWN * 2.5)

        self.play(
            FadeIn(tick_AM), FadeIn(tick_MB),
            Write(result_grp),
            run_time=0.6
        )

        note = Text(
            "M 是 AB 的中点",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 综合练习
    # ------------------------------------------------------------------

    def scene_7_practice(self):
        sec_title = Text(
            "六、综合练习",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.6)

        # 题目
        q_text = Text(
            "已知线段 a 和 b (a > b)",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.5)
        self.play(FadeIn(q_text), run_time=0.4)

        # 画出 a 和 b
        a_len = 3.0
        b_len = 1.5

        pt_a1 = np.array([-3.5, 3.5, 0])
        pt_a2 = pt_a1 + RIGHT * a_len
        seg_a = Line(pt_a1, pt_a2, color=COLOR_SEG_A, stroke_width=4)
        lab_a = MathTex("a", font_size=24, color=COLOR_SEG_A).next_to(
            (pt_a1 + pt_a2) / 2, UP, buff=0.15
        )

        pt_b1 = np.array([0.5, 3.5, 0])
        pt_b2 = pt_b1 + RIGHT * b_len
        seg_b = Line(pt_b1, pt_b2, color=COLOR_SEG_B, stroke_width=4)
        lab_b = MathTex("b", font_size=24, color=COLOR_SEG_B).next_to(
            (pt_b1 + pt_b2) / 2, UP, buff=0.15
        )

        self.play(Create(seg_a), Write(lab_a), run_time=0.5)
        self.play(Create(seg_b), Write(lab_b), run_time=0.5)

        # 练习题列表
        exercises = [
            (r"(1)\ 2a + b", 2 * a_len + b_len),
            (r"(2)\ a - b", a_len - b_len),
            (r"(3)\ 3b", 3 * b_len),
            (r"(4)\ \frac{1}{2}a + b", a_len / 2 + b_len),
        ]

        y_base = 1.5
        items = VGroup()
        result_segs = []

        for i, (tex, length) in enumerate(exercises):
            y_pos = y_base - i * 1.8

            eq_mob = MathTex(tex, font_size=26, color=WHITE).move_to(
                np.array([-2.5, y_pos, 0])
            )
            items.add(eq_mob)

            # 结果线段 (右边示意)
            seg_start = np.array([0.0, y_pos, 0])
            seg_end = seg_start + RIGHT * min(length, 6.0)  # cap for display
            # scale if too long
            display_len = length
            scale_factor = 1.0
            if display_len > 5.5:
                scale_factor = 5.5 / display_len
                seg_end = seg_start + RIGHT * 5.5
            res_seg = Line(seg_start, seg_end, color=COLOR_RESULT, stroke_width=3)

            result_segs.append((eq_mob, res_seg))

        # Animate each exercise
        for idx, (eq_mob, res_seg) in enumerate(result_segs):
            self.play(Write(eq_mob), run_time=0.5)
            eq_sign = MathTex("=", font_size=24, color=GRAY_A).next_to(eq_mob, RIGHT, buff=0.2)
            self.play(FadeIn(eq_sign), Create(res_seg), run_time=0.5)
            self.wait(0.4)

        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        sec_title = Text(
            "总结",
            font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(sec_title), run_time=0.5)

        items_data = [
            ("相等", "用圆规截取, CD = AB", COLOR_SEG_A),
            ("和", "依次截取, EF = AB + CD", "#22c55e"),
            ("差", "反向截取, EF = AB - CD", "#f59e0b"),
            ("倍", "重复截取, CD = nAB", COLOR_ACCENT),
            ("分", "等分线段, 找中点等", COLOR_COMPASS),
        ]

        y_start = 4.0
        card_group = VGroup()

        for i, (label, desc, color) in enumerate(items_data):
            y_pos = y_start - i * 1.5

            # 小圆形图标
            icon = Circle(
                radius=0.25, fill_color=color, fill_opacity=0.9,
                stroke_width=0
            ).move_to(np.array([-3.2, y_pos, 0]))

            label_text = Text(
                label, font=FONT, font_size=24, color=WHITE
            ).next_to(icon, RIGHT, buff=0.3)

            desc_text = Text(
                desc, font=FONT, font_size=18, color=GRAY_A
            ).next_to(label_text, DOWN, buff=0.08, aligned_edge=LEFT)

            card = VGroup(icon, label_text, desc_text)
            card_group.add(card)

        for card in card_group:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(0.5)

        # 核心公式框
        box = RoundedRectangle(
            width=7.0, height=2.5, corner_radius=0.3,
            color=GOLD, stroke_width=2, fill_color=GOLD, fill_opacity=0.08
        ).move_to(DOWN * 3.5)

        key_title = Text(
            "核心技能: 用圆规截取线段",
            font=FONT, font_size=24, color=GOLD
        ).move_to(DOWN * 2.6)

        key_point = Text(
            "所有运算都基于\n\"在射线上截取等长线段\"",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 3.8)

        self.play(Create(box), Write(key_title), run_time=0.6)
        self.play(FadeIn(key_point), run_time=0.5)
        self.wait(2.0)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author_mob],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.3)

        self.play(
            ReplacementTransform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.2, scale=1.05), run_time=0.6)

        # 装饰线段
        deco = VGroup()
        for j in range(5):
            seg = Line(
                LEFT * (2.0 - j * 0.3) + DOWN * 3,
                RIGHT * (2.0 - j * 0.3) + DOWN * 3,
                color=interpolate_color(ManimColor(COLOR_SEG_A), ManimColor(COLOR_RESULT), j / 4),
                stroke_width=3
            ).shift(DOWN * j * 0.3)
            deco.add(seg)

        self.play(*[Create(s) for s in deco], run_time=0.6)
        self.wait(2.0)

        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.0
        )

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def _tick_mark(self, p1, p2, color, n=1):
        """在线段中间画等长标记 (小竖线)"""
        mid = (p1 + p2) / 2
        direction = p2 - p1
        perp = np.array([-direction[1], direction[0], 0])
        perp = perp / np.linalg.norm(perp) * 0.12

        ticks = VGroup()
        if n == 1:
            ticks.add(Line(mid - perp, mid + perp, color=color, stroke_width=2))
        else:
            spacing = 0.08
            for i in range(n):
                offset = direction / np.linalg.norm(direction) * spacing * (i - (n - 1) / 2)
                pos = mid + offset
                ticks.add(Line(pos - perp, pos + perp, color=color, stroke_width=2))
        return ticks
