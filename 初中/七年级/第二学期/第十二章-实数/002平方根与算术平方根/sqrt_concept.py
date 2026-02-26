"""
平方根与算术平方根 - Manim 教学动画
七年级第二学期 第十二章
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色常量 ──────────────────────────────────────
COLOR_BG        = "#1a1a2e"
COLOR_POS_ROOT  = "#4fc3f7"   # 天蓝  — 正平方根
COLOR_NEG_ROOT  = "#ff7043"   # 橙红  — 负平方根
COLOR_ARITH     = "#66bb6a"   # 绿    — 算术平方根
COLOR_ZERO      = "#ce93d8"   # 紫    — 零
COLOR_FORMULA   = "#ffd54f"   # 金黄  — 公式
COLOR_WARN      = "#ef5350"   # 红    — 警告（负数无平方根）
COLOR_AXIS      = "#b0bec5"   # 灰白  — 数轴
COLOR_AUTHOR    = "#78909c"
FONT = "Noto Sans CJK SC"


class SquareRootConcept(Scene):
    """
    场景顺序:
    1. 开场钩子   — 面积反推边长
    2. 平方根定义  — x²=a → x=±√a
    3. 三种情况   — 正数/零/负数
    4. 算术平方根  — √a 的特殊含义
    5. 关键公式   — √(a²)=|a|
    6. 计算练习
    7. 总结+片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_definition()
        self.scene_three_cases()
        self.scene_arithmetic_sqrt()
        self.scene_key_formula()
        self.scene_practice()
        self.scene_outro()

    # ══════════════════════════════════════════════
    # Scene 1  开场钩子
    # ══════════════════════════════════════════════
    def scene_opening(self):
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * 7.3)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_obj = author

        title = Text("平方根", font=FONT, font_size=54, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        hook = Text("一块正方形瓷砖面积是 9，\n边长是多少？",
                    font=FONT, font_size=30, color=WHITE, line_spacing=1.3)
        hook.move_to(UP * 5.0)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)

        # 正方形 + 面积标注
        sq = Square(side_length=2.2, color=COLOR_POS_ROOT,
                    fill_color=COLOR_POS_ROOT, fill_opacity=0.25, stroke_width=3)
        sq.move_to(UP * 2.4)
        area_label = MathTex(r"S = 9", font_size=42, color=COLOR_FORMULA)
        area_label.move_to(sq.get_center())
        self.play(FadeIn(sq, scale=0.6), run_time=0.6)
        self.play(Write(area_label), run_time=0.4)

        # 边长问号
        side_q = MathTex(r"x = \,?", font_size=44, color=YELLOW)
        side_q.next_to(sq, DOWN, buff=0.45)
        self.play(FadeIn(side_q, scale=0.8), run_time=0.4)
        self.play(Indicate(side_q, scale_factor=1.2, color=YELLOW), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(title, hook, sq, area_label, side_q)), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 2  平方根定义
    # ══════════════════════════════════════════════
    def scene_definition(self):
        sec = Text("什么是平方根？", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 6.2)
        self.play(Write(sec), run_time=0.5)

        # 核心关系式
        eq = MathTex(r"x^2 = a \quad (a \geq 0)", font_size=48, color=WHITE)
        eq.move_to(UP * 5.0)
        self.play(Write(eq), run_time=0.7)

        defn = Text("则 x 叫做 a 的平方根", font=FONT, font_size=28, color=COLOR_POS_ROOT)
        defn.move_to(UP * 4.1)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.5)

        # 符号
        symbol = MathTex(r"x = \pm\sqrt{a}", font_size=52, color=COLOR_FORMULA)
        symbol.move_to(UP * 3.0)
        box = SurroundingRectangle(symbol, color=COLOR_FORMULA, buff=0.2, corner_radius=0.12)
        self.play(Write(symbol), Create(box), run_time=0.7)

        # ±  注释
        pm_label = Text("± 表示两个值", font=FONT, font_size=22, color=YELLOW)
        pm_label.next_to(box, RIGHT, buff=0.2)
        self.play(FadeIn(pm_label, shift=LEFT * 0.2), run_time=0.4)

        # 具体例子  x²=9 → x=±3
        ex_eq = MathTex(r"x^2 = 9", font_size=44, color=WHITE)
        ex_eq.move_to(LEFT * 1.5 + UP * 1.5)

        ex_sq = Square(side_length=1.6,
                       color=COLOR_POS_ROOT, fill_color=COLOR_POS_ROOT,
                       fill_opacity=0.28, stroke_width=2)
        ex_sq.move_to(LEFT * 3.2 + UP * 1.5)
        ex_sq_label = MathTex(r"S=9", font_size=26, color=COLOR_POS_ROOT)
        ex_sq_label.move_to(ex_sq.get_center())

        self.play(FadeIn(ex_sq, scale=0.7), Write(ex_sq_label), run_time=0.5)
        self.play(Write(ex_eq), run_time=0.4)

        arrow = Arrow(ex_eq.get_bottom() + DOWN * 0.05,
                      ex_eq.get_bottom() + DOWN * 0.85,
                      color=WHITE, buff=0.05, stroke_width=2,
                      max_tip_length_to_length_ratio=0.25)
        result = MathTex(r"x = \pm 3", font_size=44, color=COLOR_FORMULA)
        result.next_to(arrow, DOWN, buff=0.1).align_to(ex_eq, LEFT)

        self.play(Create(arrow), run_time=0.3)
        self.play(Write(result), run_time=0.5)

        # +3 和 -3 用颜色区分
        pos3 = MathTex(r"+3", font_size=36, color=COLOR_POS_ROOT)
        neg3 = MathTex(r"-3", font_size=36, color=COLOR_NEG_ROOT)
        arrow_r = Arrow(result.get_right() + RIGHT * 0.1,
                        result.get_right() + RIGHT * 1.5,
                        color=GRAY, buff=0.05, stroke_width=1.5,
                        max_tip_length_to_length_ratio=0.3)
        pos3.next_to(arrow_r.get_end(), UP, buff=0.15)
        neg3.next_to(arrow_r.get_end(), DOWN, buff=0.15)

        self.play(Create(arrow_r), FadeIn(pos3), FadeIn(neg3), run_time=0.5)

        pos_check = MathTex(r"(+3)^2 = 9\ \checkmark", font_size=26, color=COLOR_POS_ROOT)
        neg_check = MathTex(r"(-3)^2 = 9\ \checkmark", font_size=26, color=COLOR_NEG_ROOT)
        pos_check.next_to(pos3, RIGHT, buff=0.3)
        neg_check.next_to(neg3, RIGHT, buff=0.3)
        self.play(FadeIn(pos_check), FadeIn(neg_check), run_time=0.5)

        self.wait(1.2)
        self.play(FadeOut(VGroup(
            sec, eq, defn, symbol, box, pm_label,
            ex_sq, ex_sq_label, ex_eq, arrow, result,
            arrow_r, pos3, neg3, pos_check, neg_check
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 3  三种情况
    # ══════════════════════════════════════════════
    def scene_three_cases(self):
        sec = Text("平方根的三种情况", font=FONT, font_size=34, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        cases = [
            # (条件文字, formula, 结论文字, 正方形颜色, 列x)
            ("a > 0",
             r"\sqrt{4} = \pm 2",
             "两个平方根\n互为相反数",
             COLOR_POS_ROOT, -3.0),
            ("a = 0",
             r"\sqrt{0} = 0",
             "唯一平方根\n就是 0",
             COLOR_ZERO, 0.0),
            ("a < 0",
             r"\sqrt{-4} = \;?",
             "没有平方根！",
             COLOR_WARN, 3.0),
        ]

        all_mobs = VGroup()
        for cond, formula, desc, col, x in cases:
            cond_txt = Text(cond, font=FONT, font_size=26, color=col)
            cond_txt.move_to(RIGHT * x + UP * 5.8)

            sq = Square(side_length=1.0, color=col,
                        fill_color=col, fill_opacity=0.3, stroke_width=2)
            sq.move_to(RIGHT * x + UP * 4.5)

            f_tex = MathTex(formula, font_size=28, color=col)
            f_tex.move_to(RIGHT * x + UP * 3.1)
            f_box = SurroundingRectangle(f_tex, color=col, buff=0.1, corner_radius=0.08)

            desc_lines = desc.split("\n")
            desc_mob = VGroup(*[
                Text(l, font=FONT, font_size=20, color=col) for l in desc_lines
            ]).arrange(DOWN, buff=0.1).move_to(RIGHT * x + UP * 2.1)

            self.play(
                FadeIn(cond_txt, shift=DOWN * 0.2),
                FadeIn(sq, scale=0.6),
                run_time=0.4
            )
            self.play(
                Write(f_tex), Create(f_box),
                FadeIn(desc_mob),
                run_time=0.5
            )

            # 负数那列加 ✗
            if col == COLOR_WARN:
                cross = Text("✗", font=FONT, font_size=48, color=COLOR_WARN)
                cross.move_to(sq.get_center())
                self.play(FadeIn(cross, scale=0.5), run_time=0.3)
                all_mobs.add(cross)

            all_mobs.add(cond_txt, sq, f_tex, f_box, desc_mob)

        # 负数数轴 — 数轴左侧禁区
        nl = NumberLine(
            x_range=[-4, 4, 1], length=7.2,
            include_numbers=True, include_tip=True,
            numbers_to_exclude=[],
            color=COLOR_AXIS, font_size=22,
            tip_width=0.18, tip_height=0.18,
        )
        nl.move_to(UP * 0.5)
        self.play(Create(nl), run_time=0.7)

        # 非负区域高亮（a≥0 才有平方根）
        pos_hl = Line(nl.number_to_point(0), nl.number_to_point(3.8),
                      color=COLOR_POS_ROOT, stroke_width=9, stroke_opacity=0.6)
        zero_dot = Dot(nl.number_to_point(0), radius=0.13, color=COLOR_ZERO)
        neg_zone = Line(nl.number_to_point(-3.8), nl.number_to_point(-0.05),
                        color=COLOR_WARN, stroke_width=9, stroke_opacity=0.4)

        self.play(Create(pos_hl), Create(neg_zone), FadeIn(zero_dot), run_time=0.6)

        hl_label = Text("a ≥ 0  才有平方根", font=FONT, font_size=24, color=YELLOW)
        hl_label.move_to(DOWN * 0.7)
        box_hl = SurroundingRectangle(hl_label, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(hl_label), Create(box_hl), run_time=0.5)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            sec, all_mobs,
            nl, pos_hl, neg_zone, zero_dot,
            hl_label, box_hl
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 4  算术平方根
    # ══════════════════════════════════════════════
    def scene_arithmetic_sqrt(self):
        sec = Text("算术平方根", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 6.8)
        self.play(Write(sec), run_time=0.5)

        defn = Text("非负的那个平方根，叫做算术平方根",
                    font=FONT, font_size=26, color=WHITE)
        defn.move_to(UP * 6.0)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.5)

        # 对比表：平方根 vs 算术平方根
        # 9的例子
        title_sq = Text("平方根", font=FONT, font_size=30, color=COLOR_POS_ROOT)
        title_sq.move_to(LEFT * 2.5 + UP * 5.0)

        title_ar = Text("算术平方根", font=FONT, font_size=30, color=COLOR_ARITH)
        title_ar.move_to(RIGHT * 2.0 + UP * 5.0)

        sep_v = Line(UP * 5.5, UP * 0.5, color=GRAY, stroke_width=1)
        self.play(
            FadeIn(title_sq), FadeIn(title_ar),
            Create(sep_v),
            run_time=0.5
        )

        rows = [
            (r"9 \rightarrow \pm 3",           r"9 \rightarrow \sqrt{9} = 3"),
            (r"25 \rightarrow \pm 5",           r"25 \rightarrow \sqrt{25} = 5"),
            (r"\frac{1}{4} \rightarrow \pm\frac{1}{2}",
             r"\frac{1}{4} \rightarrow \sqrt{\frac{1}{4}}=\frac{1}{2}"),
            (r"0 \rightarrow 0",                r"0 \rightarrow \sqrt{0} = 0"),
        ]

        all_rows = VGroup()
        for i, (left_s, right_s) in enumerate(rows):
            y = 4.0 - i * 1.0
            lm = MathTex(left_s, font_size=28, color=COLOR_POS_ROOT)
            lm.move_to(LEFT * 2.5 + UP * y)
            rm = MathTex(right_s, font_size=28, color=COLOR_ARITH)
            rm.move_to(RIGHT * 2.0 + UP * y)
            sep_h = Line(LEFT * 4.2 + UP * (y - 0.45),
                         RIGHT * 4.2 + UP * (y - 0.45),
                         color=GRAY, stroke_width=0.7, stroke_opacity=0.5)
            self.play(
                FadeIn(lm, shift=RIGHT * 0.2),
                FadeIn(rm, shift=LEFT * 0.2),
                Create(sep_h),
                run_time=0.45
            )
            all_rows.add(lm, rm, sep_h)

        # 关键区别
        diff1 = Text("平方根：有 ±  两个值", font=FONT, font_size=26, color=COLOR_POS_ROOT)
        diff1.move_to(LEFT * 0.5 + DOWN * 0.8)
        diff2 = Text("算术平方根：只取  ≥ 0  的那个",
                     font=FONT, font_size=26, color=COLOR_ARITH)
        diff2.move_to(LEFT * 0.5 + DOWN * 1.7)

        box_arith = RoundedRectangle(
            width=6.5, height=1.15, corner_radius=0.15,
            color=COLOR_ARITH, fill_color=COLOR_ARITH, fill_opacity=0.12, stroke_width=1.5
        ).move_to(diff2.get_center())

        self.play(
            FadeIn(diff1, shift=UP * 0.2),
            FadeIn(diff2, shift=UP * 0.2),
            Create(box_arith),
            run_time=0.6
        )

        # √a ≥ 0 结论
        concl = MathTex(r"\sqrt{a} \geq 0 \quad (a \geq 0)", font_size=38, color=YELLOW)
        concl.move_to(DOWN * 3.2)
        box_c = SurroundingRectangle(concl, color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(Write(concl), Create(box_c), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            sec, defn,
            title_sq, title_ar, sep_v,
            all_rows,
            diff1, diff2, box_arith,
            concl, box_c
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 5  关键公式 √(a²)=|a|
    # ══════════════════════════════════════════════
    def scene_key_formula(self):
        sec = Text("一个重要公式", font=FONT, font_size=36, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.4)

        formula = MathTex(r"\sqrt{a^2} = |a|", font_size=56, color=COLOR_FORMULA)
        formula.move_to(UP * 5.8)
        box_f = SurroundingRectangle(formula, color=COLOR_FORMULA, buff=0.25, corner_radius=0.12)
        self.play(Write(formula), Create(box_f), run_time=0.7)

        why = Text("为什么不直接写 a ？", font=FONT, font_size=26, color=WHITE)
        why.move_to(UP * 4.6)
        self.play(FadeIn(why, shift=UP * 0.2), run_time=0.4)

        # 验证：a=3 和 a=-3
        cases_data = [
            (r"a = 3", r"\sqrt{3^2}=\sqrt{9}=3=|3|",    COLOR_POS_ROOT),
            (r"a = -3",r"\sqrt{(-3)^2}=\sqrt{9}=3=|-3|",COLOR_NEG_ROOT),
        ]
        for i, (cond, derivation, col) in enumerate(cases_data):
            y = 3.5 - i * 1.4
            cond_t = MathTex(cond, font_size=32, color=col)
            cond_t.move_to(LEFT * 1.8 + UP * y)
            deriv_t = MathTex(derivation, font_size=26, color=col)
            deriv_t.next_to(cond_t, DOWN, buff=0.2)
            self.play(Write(cond_t), run_time=0.4)
            self.play(Write(deriv_t), run_time=0.5)

        insight = Text("结果永远 ≥ 0，所以要用绝对值",
                       font=FONT, font_size=24, color=YELLOW)
        insight.move_to(UP * 0.5)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=0.5)

        # 常见错误对比
        err_box = RoundedRectangle(
            width=7.0, height=1.8, corner_radius=0.15,
            color=COLOR_WARN, fill_color=COLOR_WARN, fill_opacity=0.1, stroke_width=1.5
        ).move_to(DOWN * 1.8)
        err_title = Text("✗  常见错误", font=FONT, font_size=22, color=COLOR_WARN)
        err_title.move_to(err_box.get_top() + DOWN * 0.3)
        err_wrong = MathTex(r"\sqrt{a^2} = a", font_size=32, color=COLOR_WARN)
        err_wrong.move_to(err_box.get_center() + UP * 0.1)
        err_note = Text("当 a<0 时此式不成立！", font=FONT, font_size=20, color=COLOR_WARN)
        err_note.move_to(err_box.get_center() + DOWN * 0.45)

        self.play(Create(err_box), FadeIn(err_title), run_time=0.4)
        self.play(Write(err_wrong), FadeIn(err_note), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(Group(
            sec, formula, box_f, why,
            err_box, err_title, err_wrong, err_note,
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 6  计算练习
    # ══════════════════════════════════════════════
    def scene_practice(self):
        # 清屏（防上场残留）
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.3)

        sec = Text("练一练", font=FONT, font_size=40, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.4)

        problems = [
            # (题干, 答案, 颜色)
            (r"\sqrt{36}",                        r"= 6",         COLOR_ARITH),
            (r"36 \text{ 的平方根}",              r"= \pm 6",     COLOR_POS_ROOT),
            (r"\sqrt{(-7)^2}",                    r"= 7",         COLOR_ARITH),
            (r"\sqrt{\frac{9}{16}}",              r"= \frac{3}{4}",COLOR_ARITH),
            (r"-\sqrt{0.25}",                     r"= -0.5",      COLOR_NEG_ROOT),
        ]

        y_start = 5.6
        all_p = VGroup()
        for i, (prob, ans, col) in enumerate(problems):
            y = y_start - i * 1.1
            bullet = Dot(radius=0.07, color=col).move_to(LEFT * 3.8 + UP * y)

            if "text" in prob:
                # 含 \text{} 的用 MathTex 但注意中文不能在MathTex里
                # 改用 Text + MathTex 拼合
                prob_mob = Text("36 的平方根", font=FONT, font_size=28, color=WHITE)
                prob_mob.move_to(LEFT * 1.0 + UP * y)
            else:
                prob_mob = MathTex(prob, font_size=32, color=WHITE)
                prob_mob.move_to(LEFT * 1.5 + UP * y)

            ans_mob = MathTex(ans, font_size=32, color=col)
            ans_mob.next_to(prob_mob, RIGHT, buff=0.25)

            self.play(FadeIn(bullet), run_time=0.15)
            self.play(Write(prob_mob), run_time=0.35)
            self.play(Write(ans_mob), run_time=0.35)
            all_p.add(bullet, prob_mob, ans_mob)

        tip = Text("算术平方根 ≥ 0，平方根有两个（a>0时）",
                   font=FONT, font_size=22, color=YELLOW)
        tip.move_to(DOWN * 0.5)
        box_tip = SurroundingRectangle(tip, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(tip), Create(box_tip), run_time=0.5)

        self.wait(1.3)
        self.play(FadeOut(VGroup(sec, all_p, tip, box_tip)), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 7  总结 + 片尾
    # ══════════════════════════════════════════════
    def scene_outro(self):
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.3)

        sum_title = Text("本节要点", font=FONT, font_size=36, color=GOLD)
        sum_title.move_to(UP * 7.0)
        self.play(Write(sum_title), run_time=0.4)

        # 每条: (类型, 内容, 颜色)
        # 类型 "math"=MathTex, "text"=Text, "mixed"=MathTex+Text拼合
        points = [
            ("math",  r"x^2 = a \Rightarrow x = \pm\sqrt{a}", COLOR_FORMULA),
            ("text",  "正数的平方根有两个，互为相反数",          COLOR_POS_ROOT),
            ("text",  "0 的平方根是 0",                         COLOR_ZERO),
            ("text",  "负数没有平方根",                          COLOR_WARN),
            # ↓ \text{中文} 不能在 MathTex，拆为 mixed
            ("mixed", (r"\sqrt{a} \geq 0", "（算术平方根）"),    COLOR_ARITH),
            ("math",  r"\sqrt{a^2} = |a|",                      COLOR_FORMULA),
        ]

        point_mobs = VGroup()
        for i, (kind, content, col) in enumerate(points):
            y = 5.6 - i * 1.05
            if kind == "math":
                mob = MathTex(content, font_size=30, color=col)
            elif kind == "mixed":
                m_part = MathTex(content[0], font_size=30, color=col)
                t_part = Text(content[1], font=FONT, font_size=22, color=col)
                mob = VGroup(m_part, t_part).arrange(RIGHT, buff=0.12)
            else:
                mob = Text(content, font=FONT, font_size=24, color=col)
            mob.move_to(UP * y + RIGHT * 0.4)
            mob.align_to(LEFT * 0.3, LEFT)
            dot = Dot(radius=0.07, color=col).next_to(mob, LEFT, buff=0.2)
            grp = VGroup(dot, mob)
            point_mobs.add(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.32)

        self.wait(1.5)
        self.play(FadeOut(VGroup(sum_title, point_mobs)), run_time=0.5)

        # 片尾
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE)
        author_big.move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=COLOR_AUTHOR)
        author_id.next_to(author_big, DOWN, buff=0.3)

        self.play(Transform(self.author_obj, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=YELLOW)
        follow.move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：三个旋转正方形
        deco = VGroup(*[
            Square(side_length=s,
                   color=c, fill_color=c, fill_opacity=0.5, stroke_width=2)
            .move_to(DOWN * 2.3 + RIGHT * x)
            for s, c, x in [(0.5, COLOR_POS_ROOT, -2.0),
                             (0.6, COLOR_ARITH,    0.0),
                             (0.5, COLOR_NEG_ROOT,  2.0)]
        ])
        self.play(*[FadeIn(d, scale=0.4) for d in deco], run_time=0.5)
        self.play(Rotate(deco, angle=PI / 4, run_time=0.8))

        finale = MathTex(r"\sqrt{a^2} = |a|", font_size=46, color=COLOR_FORMULA)
        finale.move_to(DOWN * 3.8)
        self.play(Write(finale), run_time=0.6)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            self.author_obj, author_id, follow, deco, finale
        )), run_time=0.8)


# 渲染:
#   manim -pql sqrt_concept.py SquareRootConcept   # 快速预览
#   manim -qh  sqrt_concept.py SquareRootConcept   # 高质量