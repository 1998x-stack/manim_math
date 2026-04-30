"""
无理方程 — 平方法与增根检验 教学动画
Irrational Equations: Squaring Method & Extraneous Root Verification

年级: 八年级  学期: 第二学期  章节: 第二十一章
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车  @emptyandcalm

例题: √(2x+1) = x - 1
结论: x=0 增根（舍去），x=4 有效解

渲染命令:
  manim -pql irrational_equation_animation.py IrrationalEquation   # 快速预览
  manim -qh  irrational_equation_animation.py IrrationalEquation   # 高质量
"""

from manim import *
import numpy as np

# ── TikTok 竖屏 ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

CJK = "PingFang SC"

# ── 配色 ────────────────────────────────────────────────────
BG         = "#1a1a2e"
C_TITLE    = GOLD
C_SQRT     = "#00d4ff"    # 根式蓝
C_SQUARE   = "#a8e6cf"    # 平方绿
C_SOLVE    = "#ffeaa7"    # 整式黄
C_GOOD     = "#55efc4"    # 有效根绿
C_BAD      = "#ff6b6b"    # 增根红
C_STEP     = "#74b9ff"    # 步骤蓝
C_ARROW    = "#74b9ff"
C_SUB      = GRAY_A
C_AUTHOR   = GRAY_B


# ════════════════════════════════════════════════════════════
class IrrationalEquation(Scene):

    def construct(self):
        self.camera.background_color = BG
        self._bar = self._author_bar()
        self.add(self._bar)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_four_steps()
        self.scene4_square_both_sides()
        self.scene5_solve_quadratic()
        self.scene6_verify()
        self.scene7_outro()

    # ── 工具 ─────────────────────────────────────────────────

    def _author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=CJK, font_size=18, color=C_AUTHOR
        ).move_to(UP * 7.2)

    def _title_mob(self, txt, font_size=38, color=C_TITLE):
        t  = Text(txt, font=CJK, font_size=font_size, color=color)
        ul = Line(
            t.get_left()  + DOWN * 0.10,
            t.get_right() + DOWN * 0.10,
            color=color, stroke_width=2.5
        )
        return VGroup(t, ul)

    def _rbox(self, mob, color=C_STEP, buff=0.28, fo=0.12):
        return RoundedRectangle(
            width=mob.get_width() + buff * 2,
            height=mob.get_height() + buff * 2,
            corner_radius=0.18,
            color=color, fill_color=color,
            fill_opacity=fo, stroke_width=2
        ).move_to(mob)

    def _step_tag(self, n, label, color=C_STEP):
        c = Circle(radius=0.28, color=color,
                   fill_color=color, fill_opacity=0.9, stroke_width=0)
        num = Text(str(n), font=CJK, font_size=20, color=BG,
                   weight=BOLD).move_to(c)
        txt = Text(label, font=CJK, font_size=24, color=color)
        return VGroup(VGroup(c, num), txt).arrange(RIGHT, buff=0.18)

    def _clear(self, *mobs):
        if mobs:
            self.play(*[FadeOut(m, run_time=0.4) for m in mobs])

    def _vdivider(self, y_top, y_bot, x=0.0):
        """竖向分隔线"""
        return DashedLine(
            np.array([x, y_top, 0]),
            np.array([x, y_bot, 0]),
            color=GRAY_B, dash_length=0.14, stroke_width=1.5
        )

    # ────────────────────────────────────────────────────────
    # Scene 1 — 开场钩子
    # ────────────────────────────────────────────────────────
    def scene1_hook(self):
        hook = Text(
            "看到根号别怕，一招搞定！",
            font=CJK, font_size=28, color=C_SUB
        ).move_to(UP * 5.5)

        eq = MathTex(
            r"\sqrt{2x+1} = x - 1",
            font_size=64, color=C_SQRT
        ).move_to(UP * 3.5)
        eq_box = self._rbox(eq, color=C_SQRT, buff=0.42, fo=0.08)

        grade = Text(
            "八年级 · 无理方程",
            font=CJK, font_size=22, color=GRAY_B
        ).move_to(UP * 2.0)

        tip = Text(
            "两边平方，去掉根号！",
            font=CJK, font_size=30, color=C_SQUARE
        ).move_to(UP * 0.5)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.55)
        self.play(Write(eq), run_time=1.1)
        self.play(Create(eq_box), run_time=0.4)
        self.play(FadeIn(grade), run_time=0.35)
        # 根号闪烁高亮
        self.play(eq.animate.set_color(C_TITLE), run_time=0.22)
        self.play(eq.animate.set_color(C_SQRT),  run_time=0.22)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.45)
        self.wait(0.8)
        self._clear(hook, eq, eq_box, grade, tip)

    # ────────────────────────────────────────────────────────
    # Scene 2 — 什么是无理方程
    # ────────────────────────────────────────────────────────
    def scene2_definition(self):
        title = self._title_mob("无理方程", font_size=40)
        title.move_to(UP * 6.2)

        defn = Text(
            "根号内含有未知数的方程",
            font=CJK, font_size=27, color=C_SUB
        ).move_to(UP * 5.0)

        # 两列对比
        col_l  = Text("有理方程", font=CJK, font_size=26, color=C_SUB).move_to(UP * 3.8 + LEFT * 2.4)
        col_r  = Text("无理方程", font=CJK, font_size=26, color=C_SQRT).move_to(UP * 3.8 + RIGHT * 2.4)
        div    = self._vdivider(4.4, 1.4)

        # 示例
        eq_l = MathTex(r"x^2 - 4 = 0",             font_size=30, color=C_SUB) .move_to(UP * 2.8 + LEFT  * 2.4)
        eq_r = MathTex(r"\sqrt{2x+1} = x-1",        font_size=30, color=C_SQRT).move_to(UP * 2.8 + RIGHT * 2.4)
        no_l = Text("根号无 x  ✓",  font=CJK, font_size=19, color=GRAY_B).move_to(UP * 2.0 + LEFT  * 2.4)
        no_r = Text("根号有 x  ✓",  font=CJK, font_size=19, color=C_SQRT).move_to(UP * 2.0 + RIGHT * 2.4)

        # 警告
        warn = Text(
            "两边平方可能产生增根！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(UP * 0.6)
        warn_box = self._rbox(warn, color=C_BAD, buff=0.22, fo=0.07)

        self.play(Write(title[0]), Create(title[1]), run_time=0.55)
        self.play(FadeIn(defn, shift=DOWN * 0.2), run_time=0.4)
        self.play(FadeIn(col_l), FadeIn(col_r), Create(div), run_time=0.5)
        self.play(FadeIn(eq_l), FadeIn(eq_r), run_time=0.45)
        self.play(FadeIn(no_l), FadeIn(no_r), run_time=0.4)
        self.play(Create(warn_box), FadeIn(warn), run_time=0.55)
        self.wait(1.0)
        self._clear(title, defn, col_l, col_r, div, eq_l, eq_r, no_l, no_r, warn_box, warn)

    # ────────────────────────────────────────────────────────
    # Scene 3 — 四步解法总览
    # ────────────────────────────────────────────────────────
    def scene3_four_steps(self):
        title = self._title_mob("解题四步法", font_size=38)
        title.move_to(UP * 6.2)

        data = [
            (1, "整理（根号在一边）", C_SQRT,   UP * 4.5),
            (2, "两边平方",          C_SQUARE, UP * 3.2),
            (3, "解整式方程",        C_SOLVE,  UP * 1.9),
            (4, "检验（增根！）",    C_BAD,    UP * 0.6),
        ]
        steps = [self._step_tag(n, l, c).move_to(p) for n, l, c, p in data]

        arrows = VGroup(*[
            Arrow(
                steps[i].get_bottom() + DOWN * 0.04,
                steps[i+1].get_top()  + UP   * 0.04,
                color=GRAY_B, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.22, buff=0.06
            )
            for i in range(3)
        ])

        step4_box = self._rbox(steps[3], color=C_BAD, buff=0.22, fo=0.10)

        note = Text(
            "第4步最关键，漏掉直接丢分！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(DOWN * 0.9)

        self.play(Write(title[0]), Create(title[1]), run_time=0.55)
        for i, s in enumerate(steps):
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.32)
            if i < 3:
                self.play(GrowArrow(arrows[i]), run_time=0.28)
        self.play(Create(step4_box), run_time=0.38)
        self.play(
            steps[3].animate.set_color(C_TITLE), run_time=0.22
        )
        self.play(
            steps[3].animate.set_color(C_BAD), run_time=0.22
        )
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear(title, *steps, arrows, step4_box, note)

    # ────────────────────────────────────────────────────────
    # Scene 4 — 步骤1+2：整理与两边平方
    # ────────────────────────────────────────────────────────
    def scene4_square_both_sides(self):
        # 例题标题 + 原方程（全程保留）
        eg_title = self._title_mob("例题", font_size=34, color=C_TITLE)
        eg_title.move_to(UP * 6.5)

        orig_eq = MathTex(
            r"\sqrt{2x+1} = x - 1",
            font_size=52, color=C_SQRT
        ).move_to(UP * 5.2)
        orig_box = self._rbox(orig_eq, color=C_SQRT, buff=0.3, fo=0.07)

        self.play(Write(eg_title[0]), Create(eg_title[1]), run_time=0.48)
        self.play(Write(orig_eq), Create(orig_box), run_time=0.85)
        self.wait(0.3)

        # ── 步骤①：已整理 ──────────────────────────────────
        s1 = self._step_tag(1, "根号已在左边，已整理", C_SQRT).move_to(UP * 3.8)
        check1 = MathTex(r"\checkmark", font_size=36, color=C_GOOD).next_to(s1, RIGHT, buff=0.25)
        self.play(FadeIn(s1, shift=RIGHT * 0.3), run_time=0.42)
        self.play(Write(check1), run_time=0.3)
        self.wait(0.25)

        # ── 步骤②：两边平方 ────────────────────────────────
        s2 = self._step_tag(2, "两边平方，去根号", C_SQUARE).move_to(UP * 2.8)
        self.play(FadeIn(s2, shift=RIGHT * 0.3), run_time=0.42)

        # 平方箭头
        sq_arrow = Arrow(
            UP * 2.3, UP * 1.4,
            color=C_ARROW, stroke_width=3,
            max_tip_length_to_length_ratio=0.22, buff=0.1
        )
        sq_note = Text("两边²", font=CJK, font_size=22, color=C_SQUARE
                       ).next_to(sq_arrow, RIGHT, buff=0.18)
        self.play(GrowArrow(sq_arrow), FadeIn(sq_note), run_time=0.45)

        # 平方后等式
        sq_eq = MathTex(
            r"2x+1 = (x-1)^2",
            font_size=46, color=C_SQUARE
        ).move_to(UP * 0.8)
        sq_box = self._rbox(sq_eq, color=C_SQUARE, buff=0.28, fo=0.08)
        self.play(Write(sq_eq), Create(sq_box), run_time=0.75)
        self.wait(0.3)

        # 展开右边
        expand_note = Text("展开右边：", font=CJK, font_size=23, color=C_SUB)
        expand_eq   = MathTex(
            r"2x+1 = x^2 - 2x + 1",
            font_size=44, color=C_SQUARE
        )
        expand_grp = VGroup(expand_note, expand_eq).arrange(RIGHT, buff=0.2)
        expand_grp.move_to(DOWN * 0.6)

        expand_arrow = Arrow(
            sq_eq.get_bottom() + DOWN * 0.06,
            expand_grp.get_top() + UP * 0.06,
            color=C_ARROW, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2, buff=0.08
        )
        self.play(GrowArrow(expand_arrow), run_time=0.38)
        self.play(FadeIn(expand_note), Write(expand_eq), run_time=0.7)
        self.wait(0.3)

        # 移项整理
        move_note  = Text("移项整理：", font=CJK, font_size=23, color=C_SUB)
        rearr_eq   = MathTex(
            r"x^2 - 4x = 0",
            font_size=50, color=C_SOLVE
        )
        rearr_grp = VGroup(move_note, rearr_eq).arrange(RIGHT, buff=0.2)
        rearr_grp.move_to(DOWN * 2.0)
        rearr_box = self._rbox(rearr_grp, color=C_SOLVE, buff=0.28, fo=0.1)

        rearr_arrow = Arrow(
            expand_grp.get_bottom() + DOWN * 0.06,
            rearr_grp.get_top()     + UP   * 0.06,
            color=C_ARROW, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2, buff=0.08
        )
        self.play(GrowArrow(rearr_arrow), run_time=0.35)
        self.play(FadeIn(move_note), Write(rearr_eq), Create(rearr_box), run_time=0.75)
        self.wait(0.6)

        # 整式方程标注
        integral_tag = Text(
            "整式方程！",
            font=CJK, font_size=22, color=C_SOLVE
        ).next_to(rearr_box, RIGHT, buff=0.22)
        self.play(FadeIn(integral_tag), run_time=0.35)
        self.wait(0.9)

        # 清场：移走辅助元素，把整理结果移上去供下一场用
        self._clear(
            eg_title, s1, check1, s2,
            sq_arrow, sq_note,
            sq_box, expand_arrow, expand_grp,
            rearr_arrow, integral_tag
        )
        # 保留 orig_eq, orig_box, sq_eq, rearr_eq 供下场过渡
        self.play(
            orig_eq.animate.move_to(UP * 5.8).scale(0.70),
            orig_box.animate.move_to(UP * 5.8).scale(0.70),
            rearr_grp.animate.move_to(UP * 4.5).scale(0.85),
            rearr_box.animate.move_to(UP * 4.5).scale(0.85),
            FadeOut(sq_eq),
            run_time=0.55
        )
        # 存储供后续场景
        self._orig_eq    = orig_eq
        self._orig_box   = orig_box
        self._rearr_grp  = rearr_grp
        self._rearr_box  = rearr_box
        self._rearr_eq   = rearr_eq    # 单独存 MathTex 用于引用

    # ────────────────────────────────────────────────────────
    # Scene 5 — 步骤3：解整式方程（因式分解）
    # ────────────────────────────────────────────────────────
    def scene5_solve_quadratic(self):
        s3 = self._step_tag(3, "解整式方程", C_SOLVE).move_to(UP * 3.2)
        self.play(FadeIn(s3, shift=RIGHT * 0.3), run_time=0.42)

        # 提公因式
        fact_note = Text("提公因式：", font=CJK, font_size=24, color=C_SUB)
        fact_eq   = MathTex(r"x(x-4) = 0", font_size=48, color=C_SOLVE)
        fact_grp  = VGroup(fact_note, fact_eq).arrange(RIGHT, buff=0.2)
        fact_grp.move_to(UP * 1.8)

        arr_fact = Arrow(
            self._rearr_grp.get_bottom() + DOWN * 0.05,
            fact_grp.get_top()           + UP   * 0.05,
            color=C_ARROW, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.22, buff=0.08
        )
        self.play(GrowArrow(arr_fact), run_time=0.38)
        self.play(FadeIn(fact_note), Write(fact_eq), run_time=0.65)
        self.wait(0.3)

        # 零乘积 → 两个解
        zero_note = Text("零乘积定理：", font=CJK, font_size=24, color=C_SUB)
        zero_eq   = MathTex(r"x = 0 \quad \text{or} \quad x = 4",
                            font_size=44, color=C_SOLVE)
        zero_grp  = VGroup(zero_note, zero_eq).arrange(RIGHT, buff=0.2)
        zero_grp.move_to(UP * 0.2)
        zero_box  = self._rbox(zero_grp, color=C_SOLVE, buff=0.3, fo=0.1)

        arr_zero = Arrow(
            fact_grp.get_bottom() + DOWN * 0.05,
            zero_grp.get_top()    + UP   * 0.05,
            color=C_ARROW, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.22, buff=0.08
        )
        self.play(GrowArrow(arr_zero), run_time=0.35)
        self.play(FadeIn(zero_note), Write(zero_eq),
                  Create(zero_box), run_time=0.75)
        self.wait(0.5)

        # 警告：必须检验！
        caution = Text(
            "先别高兴！必须代入原方程检验！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(DOWN * 1.5)
        caution_box = self._rbox(caution, color=C_BAD, buff=0.22, fo=0.08)

        self.play(Create(caution_box), FadeIn(caution), run_time=0.55)
        self.wait(0.85)

        # 清场，保留 orig_eq 和 two-sol group 供下场
        self._clear(
            s3, arr_fact, fact_grp, arr_zero, caution, caution_box
        )
        self.play(
            zero_grp.animate.move_to(UP * 3.5).scale(0.85),
            zero_box.animate.move_to(UP * 3.5).scale(0.85),
            run_time=0.5
        )
        self._zero_grp = zero_grp
        self._zero_box = zero_box

    # ────────────────────────────────────────────────────────
    # Scene 6 — 步骤4：双列检验（最戏剧化）
    # ────────────────────────────────────────────────────────
    def scene6_verify(self):
        s4 = self._step_tag(4, "检验", C_BAD).move_to(UP * 2.6)
        self.play(FadeIn(s4, shift=RIGHT * 0.3), run_time=0.42)

        # 分隔线
        div = self._vdivider(2.1, -5.5)
        self.play(Create(div), run_time=0.38)

        # ── 两列标题 ─────────────────────────────────────────
        # 左: x=0 (红), 右: x=4 (绿)
        lbl0 = Text("代入 x = 0", font=CJK, font_size=26, color=C_BAD) .move_to(UP * 1.6 + LEFT  * 2.3)
        lbl4 = Text("代入 x = 4", font=CJK, font_size=26, color=C_GOOD).move_to(UP * 1.6 + RIGHT * 2.3)
        self.play(FadeIn(lbl0), FadeIn(lbl4), run_time=0.42)

        # ── 左列：x = 0 ──────────────────────────────────────
        # 左边
        lhs0_label = Text("左边 =", font=CJK, font_size=21, color=C_SUB).move_to(UP * 0.7 + LEFT * 2.7)
        lhs0_calc  = MathTex(
            r"\sqrt{1} = 1",
            font_size=32, color=C_BAD
        ).move_to(UP * 0.7 + LEFT * 1.6)

        # 右边
        rhs0_label = Text("右边 =", font=CJK, font_size=21, color=C_SUB).move_to(DOWN * 0.2 + LEFT * 2.7)
        rhs0_calc  = MathTex(
            r"0 - 1 = -1",
            font_size=32, color=C_BAD
        ).move_to(DOWN * 0.2 + LEFT * 1.65)

        # 右边 < 0 标注
        b_neg = Text("右边 < 0", font=CJK, font_size=22, color=C_BAD
                     ).move_to(DOWN * 1.1 + LEFT * 2.3)
        b_neg_box = self._rbox(b_neg, color=C_BAD, buff=0.18, fo=0.12)

        self.play(FadeIn(lhs0_label), Write(lhs0_calc), run_time=0.52)
        self.play(FadeIn(rhs0_label), Write(rhs0_calc), run_time=0.52)
        self.play(Create(b_neg_box), FadeIn(b_neg), run_time=0.45)

        # 左列大叉
        cross0 = Cross(
            stroke_color=C_BAD, stroke_width=10, scale_factor=0.55
        ).move_to(DOWN * 2.2 + LEFT * 2.3)
        bad_label = Text("增根，舍去", font=CJK, font_size=22, color=C_BAD
                         ).move_to(DOWN * 3.1 + LEFT * 2.3)

        self.play(Create(cross0), run_time=0.5)
        self.play(FadeIn(bad_label), run_time=0.35)
        self.wait(0.4)

        # ── 右列：x = 4 ──────────────────────────────────────
        # 左边
        lhs4_label = Text("左边 =", font=CJK, font_size=21, color=C_SUB).move_to(UP * 0.7 + RIGHT * 1.4)
        lhs4_calc  = MathTex(
            r"\sqrt{9} = 3",
            font_size=32, color=C_GOOD
        ).move_to(UP * 0.7 + RIGHT * 2.55)

        # 右边
        rhs4_label = Text("右边 =", font=CJK, font_size=21, color=C_SUB).move_to(DOWN * 0.2 + RIGHT * 1.4)
        rhs4_calc  = MathTex(
            r"4 - 1 = 3",
            font_size=32, color=C_GOOD
        ).move_to(DOWN * 0.2 + RIGHT * 2.55)

        # 相等标注
        equal_note = Text("左边 = 右边", font=CJK, font_size=22, color=C_GOOD
                          ).move_to(DOWN * 1.1 + RIGHT * 2.3)
        equal_box = self._rbox(equal_note, color=C_GOOD, buff=0.18, fo=0.12)

        self.play(FadeIn(lhs4_label), Write(lhs4_calc), run_time=0.52)
        self.play(FadeIn(rhs4_label), Write(rhs4_calc), run_time=0.52)
        self.play(Create(equal_box), FadeIn(equal_note), run_time=0.45)

        # 右列大勾
        check4 = MathTex(
            r"\checkmark",
            font_size=72, color=C_GOOD
        ).move_to(DOWN * 2.2 + RIGHT * 2.3)
        good_label = Text("有效解", font=CJK, font_size=22, color=C_GOOD
                          ).move_to(DOWN * 3.1 + RIGHT * 2.3)

        self.play(Write(check4), run_time=0.5)
        self.play(FadeIn(good_label), run_time=0.35)
        self.wait(0.5)

        # ── 最终结论 ─────────────────────────────────────────
        answer_label = Text("答：", font=CJK, font_size=26, color=C_TITLE)
        answer_eq    = MathTex(r"x = 4", font_size=48, color=C_TITLE)
        answer_grp   = VGroup(answer_label, answer_eq).arrange(RIGHT, buff=0.2)
        answer_grp.move_to(DOWN * 4.5)
        answer_box = self._rbox(answer_grp, color=C_TITLE, buff=0.35, fo=0.15)

        self.play(Create(answer_box), FadeIn(answer_label),
                  Write(answer_eq), run_time=0.7)
        self.play(
            Indicate(answer_grp, color=C_TITLE, scale_factor=1.08),
            run_time=0.55
        )
        self.wait(1.5)

        # 清场
        self._clear(
            self._orig_eq, self._orig_box,
            self._rearr_grp, self._rearr_box,
            self._zero_grp,  self._zero_box,
            s4, div,
            lbl0, lbl4,
            lhs0_label, lhs0_calc, rhs0_label, rhs0_calc,
            b_neg, b_neg_box, cross0, bad_label,
            lhs4_label, lhs4_calc, rhs4_label, rhs4_calc,
            equal_note, equal_box, check4, good_label,
            answer_grp, answer_box
        )

    # ────────────────────────────────────────────────────────
    # Scene 7 — 总结与片尾
    # ────────────────────────────────────────────────────────
    def scene7_outro(self):
        title = self._title_mob("解题四步法", font_size=36)
        title.move_to(UP * 5.8)

        steps = VGroup(
            self._step_tag(1, "整理（根号在一边）", C_SQRT),
            self._step_tag(2, "两边平方",          C_SQUARE),
            self._step_tag(3, "解整式方程",        C_SOLVE),
            self._step_tag(4, "检验（增根！）",    C_BAD),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        steps.move_to(UP * 3.8)

        mantra = Text(
            "B≥0 才是真，代入验，增根舍！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(UP * 1.5)
        mantra_box = self._rbox(mantra, color=C_BAD, buff=0.24, fo=0.08)

        self.play(Write(title[0]), Create(title[1]), run_time=0.55)
        for row in steps:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.30)
        self.play(Create(mantra_box), FadeIn(mantra), run_time=0.52)
        self.wait(0.9)

        # 清场 → 片尾
        self._clear(title, steps, mantra, mantra_box)
        self.play(FadeOut(self._bar), run_time=0.2)

        author_big = Text(
            "上海初高中数学直通车",
            font=CJK, font_size=38, color=WHITE
        ).move_to(UP * 1.2)
        author_id = Text(
            "@emptyandcalm",
            font=CJK, font_size=28, color=C_AUTHOR
        ).move_to(UP * 0.1)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=CJK, font_size=28, color=C_BAD
        ).move_to(DOWN * 1.2)

        deco = VGroup(
            MathTex(r"\sqrt{2x+1} = x-1", font_size=26, color=GRAY_B),
            MathTex(r"\Rightarrow x=0\text{ (extraneous)},\; x=4", font_size=22, color=GRAY_B),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 2.9)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.55)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco), run_time=0.4)
        self.wait(1.5)
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow),     FadeOut(deco),
            run_time=0.9
        )