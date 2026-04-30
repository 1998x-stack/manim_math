"""
无理数的概念 - Manim 教学动画
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
COLOR_BG         = "#1a1a2e"
COLOR_IRRATIONAL = "#ff7043"   # 橙红  — 无理数
COLOR_RATIONAL   = "#4fc3f7"   # 天蓝  — 有理数
COLOR_SQRT2      = "#66bb6a"   # 绿    — √2
COLOR_PI         = "#ce93d8"   # 紫    — π
COLOR_DIGIT      = "#ffd54f"   # 金黄  — 小数位
COLOR_FORMULA    = "#ffd54f"
COLOR_AXIS       = "#b0bec5"
COLOR_AUTHOR     = "#78909c"
FONT = "PingFang SC"

# √2 展开的小数位（前30位）
SQRT2_DIGITS = "1.41421356237309504880168872420"
# π 展开的小数位（前30位）
PI_DIGITS    = "3.14159265358979323846264338327"


class IrrationalNumberConcept(Scene):
    """
    场景顺序:
    1. 开场钩子   — 正方形对角线引出 √2
    2. 有理数回顾  — 有限/循环小数
    3. √2 的小数展开 — 无限不循环
    4. π 的小数展开
    5. 无理数定义  — 判断方法
    6. 数轴上的无理数
    7. 总结+片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_rational_review()
        self.scene_sqrt2_digits()
        self.scene_pi_digits()
        self.scene_definition()
        self.scene_number_line()
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

        title = Text("无理数", font=FONT, font_size=54, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        hook = Text("边长为 1 的正方形，\n对角线有多长？",
                    font=FONT, font_size=30, color=WHITE, line_spacing=1.3)
        hook.move_to(UP * 5.0)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 正方形 + 对角线
        sq = Square(side_length=2.0, color=COLOR_RATIONAL,
                    fill_color=COLOR_RATIONAL, fill_opacity=0.15, stroke_width=3)
        sq.move_to(UP * 2.5)
        self.play(Create(sq), run_time=0.6)

        # 边长标注
        side_lbl = MathTex(r"1", font_size=32, color=COLOR_RATIONAL)
        side_lbl.next_to(sq, DOWN, buff=0.12)
        side_lbl2 = MathTex(r"1", font_size=32, color=COLOR_RATIONAL)
        side_lbl2.next_to(sq, RIGHT, buff=0.12)
        self.play(FadeIn(side_lbl), FadeIn(side_lbl2), run_time=0.3)

        # 对角线
        c = sq.get_center()
        s = 1.0  # half side in manim coords
        diag = Line(
            sq.get_corner(DL),
            sq.get_corner(UR),
            color=COLOR_SQRT2, stroke_width=4
        )
        self.play(Create(diag), run_time=0.5)

        # 勾股定理推导
        pyth = MathTex(
            r"d = \sqrt{1^2 + 1^2} = \sqrt{2}",
            font_size=34, color=COLOR_SQRT2
        )
        pyth.next_to(sq, RIGHT, buff=0.3)
        self.play(Write(pyth), run_time=0.6)

        # 近似值
        approx = MathTex(r"\approx 1.41421\ldots", font_size=30, color=YELLOW)
        approx.next_to(pyth, DOWN, buff=0.2)
        self.play(FadeIn(approx, shift=UP * 0.2), run_time=0.5)

        question = Text("这个数是有理数吗？", font=FONT, font_size=28, color=YELLOW)
        question.move_to(DOWN * 1.2)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, hook, sq, side_lbl, side_lbl2,
            diag, pyth, approx, question
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 2  有理数回顾
    # ══════════════════════════════════════════════
    def scene_rational_review(self):
        sec = Text("有理数的小数特点", font=FONT, font_size=34, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 两类有理数
        cat1_title = Text("有限小数", font=FONT, font_size=28, color=COLOR_RATIONAL)
        cat1_title.move_to(LEFT * 2.5 + UP * 5.8)

        cat2_title = Text("无限循环小数", font=FONT, font_size=28, color=COLOR_RATIONAL)
        cat2_title.move_to(RIGHT * 2.2 + UP * 5.8)

        sep = Line(UP * 6.1, UP * 1.5, color=GRAY, stroke_width=1)
        self.play(
            FadeIn(cat1_title), FadeIn(cat2_title),
            Create(sep), run_time=0.5
        )

        examples_left = [
            r"0.5",
            r"0.75",
            r"-1.25",
            r"3.14",
        ]
        examples_right = [
            r"0.\overline{3} = 0.3333\ldots",
            r"0.\overline{6} = 0.6666\ldots",
            r"0.\overline{142857}",
            r"1.2\overline{73}",
        ]

        all_ex = VGroup()
        for i, (le, re) in enumerate(zip(examples_left, examples_right)):
            y = 4.7 - i * 0.85
            lm = MathTex(le, font_size=28, color=COLOR_RATIONAL)
            lm.move_to(LEFT * 2.5 + UP * y)
            rm = MathTex(re, font_size=24, color=COLOR_RATIONAL)
            rm.move_to(RIGHT * 2.2 + UP * y)
            sh = Line(LEFT * 4.2 + UP * (y - 0.38),
                      RIGHT * 4.2 + UP * (y - 0.38),
                      color=GRAY, stroke_width=0.6, stroke_opacity=0.4)
            self.play(FadeIn(lm), FadeIn(rm), Create(sh), run_time=0.4)
            all_ex.add(lm, rm, sh)

        # 关键结论框
        concl = Text("有理数 = 有限小数  或  无限循环小数",
                     font=FONT, font_size=24, color=COLOR_RATIONAL)
        concl.move_to(UP * 1.0)
        box_c = SurroundingRectangle(concl, color=COLOR_RATIONAL, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(concl), Create(box_c), run_time=0.5)

        # 引出问题
        q = Text("√2 是有限小数或循环小数吗？",
                 font=FONT, font_size=26, color=YELLOW)
        q.move_to(DOWN * 0.5)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(
            sec, cat1_title, cat2_title, sep,
            all_ex, concl, box_c, q
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 3  √2 小数展开动画
    # ══════════════════════════════════════════════
    def scene_sqrt2_digits(self):
        sec = Text("√2 的小数展开", font=FONT, font_size=36, color=COLOR_SQRT2)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        sqrt2_label = MathTex(r"\sqrt{2} =", font_size=44, color=COLOR_SQRT2)
        sqrt2_label.move_to(LEFT * 3.0 + UP * 5.8)
        self.play(Write(sqrt2_label), run_time=0.4)

        # 逐位显示小数（分段）
        # 整数部分 "1."
        int_part = MathTex(r"1.", font_size=40, color=WHITE)
        int_part.next_to(sqrt2_label, RIGHT, buff=0.15)
        self.play(Write(int_part), run_time=0.3)

        # 小数部分分批出现（每批4位）
        decimal_str = "41421356237309504880"
        batch_size = 4
        batches = [decimal_str[i:i+batch_size]
                   for i in range(0, len(decimal_str), batch_size)]

        digit_mobs = VGroup()
        # 分两行显示
        row1_str = decimal_str[:10]
        row2_str = decimal_str[10:20]

        row1 = MathTex(row1_str, font_size=36, color=COLOR_DIGIT)
        row1.next_to(int_part, RIGHT, buff=0.05)

        dots1 = MathTex(r"\ldots", font_size=36, color=GRAY)
        dots1.next_to(row1, RIGHT, buff=0.05)

        row2 = MathTex(row2_str, font_size=36, color=COLOR_DIGIT)
        row2.next_to(int_part, DOWN + RIGHT * 3.2, buff=0.4)
        row2.align_to(row1, LEFT)

        dots2 = MathTex(r"\ldots", font_size=36, color=GRAY)
        dots2.next_to(row2, RIGHT, buff=0.05)

        # 逐位打字效果（用整行分批）
        for char in row1_str:
            pass  # 直接整行显示

        self.play(Write(row1), run_time=1.2)
        self.play(Write(dots1), run_time=0.3)
        self.play(FadeIn(row2, shift=DOWN * 0.1), run_time=0.8)
        self.play(Write(dots2), run_time=0.3)

        # 高亮：不循环
        no_repeat = Text("无重复的循环节！", font=FONT, font_size=26, color=YELLOW)
        no_repeat.move_to(UP * 3.0)
        arrow_nr = Arrow(no_repeat.get_bottom(),
                         no_repeat.get_bottom() + DOWN * 0.7,
                         color=YELLOW, stroke_width=2,
                         max_tip_length_to_length_ratio=0.25)
        self.play(FadeIn(no_repeat, shift=UP * 0.2), Create(arrow_nr), run_time=0.5)

        # 更多位数对比 — 显示特定几位，说明不循环
        compare_text = Text("每一位都不能预测，永远不循环",
                            font=FONT, font_size=24, color=WHITE)
        compare_text.move_to(UP * 1.8)
        self.play(FadeIn(compare_text, shift=UP * 0.2), run_time=0.4)

        # √2 ≈ 1.41421356...  精确值
        precise = MathTex(
            r"\sqrt{2} \approx 1.41421356\ldots",
            font_size=36, color=COLOR_SQRT2
        )
        precise.move_to(UP * 0.5)
        box_p = SurroundingRectangle(precise, color=COLOR_SQRT2, buff=0.18, corner_radius=0.1)
        self.play(Write(precise), Create(box_p), run_time=0.6)

        # 验证
        val_text = MathTex(
            r"(\sqrt{2})^2 = 2\ \checkmark",
            font_size=32, color=COLOR_SQRT2
        )
        val_text.move_to(DOWN * 0.7)
        self.play(Write(val_text), run_time=0.4)

        self.wait(1.2)
        self.play(FadeOut(VGroup(
            sec, sqrt2_label, int_part, row1, dots1,
            row2, dots2, no_repeat, arrow_nr,
            compare_text, precise, box_p, val_text
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 4  π 的小数展开
    # ══════════════════════════════════════════════
    def scene_pi_digits(self):
        sec = Text("π 的小数展开", font=FONT, font_size=36, color=COLOR_PI)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        pi_label = MathTex(r"\pi =", font_size=44, color=COLOR_PI)
        pi_label.move_to(LEFT * 3.5 + UP * 5.8)
        self.play(Write(pi_label), run_time=0.4)

        # 整数+小数
        int_pi = MathTex(r"3.", font_size=40, color=WHITE)
        int_pi.next_to(pi_label, RIGHT, buff=0.15)
        self.play(Write(int_pi), run_time=0.3)

        pi_dec = "14159265358979323846"
        pi_row1 = pi_dec[:10]
        pi_row2 = pi_dec[10:20]

        row1 = MathTex(pi_row1, font_size=36, color=COLOR_DIGIT)
        row1.next_to(int_pi, RIGHT, buff=0.05)
        dots1 = MathTex(r"\ldots", font_size=36, color=GRAY)
        dots1.next_to(row1, RIGHT, buff=0.05)

        row2 = MathTex(pi_row2, font_size=36, color=COLOR_DIGIT)
        row2.align_to(row1, LEFT).next_to(row1, DOWN, buff=0.35)
        dots2 = MathTex(r"\ldots", font_size=36, color=GRAY)
        dots2.next_to(row2, RIGHT, buff=0.05)

        self.play(Write(row1), run_time=1.0)
        self.play(Write(dots1), run_time=0.3)
        self.play(FadeIn(row2, shift=DOWN * 0.1), run_time=0.7)
        self.play(Write(dots2), run_time=0.3)

        # π 的来源
        origin = Text("π = 圆的周长 ÷ 直径（任意圆）", font=FONT, font_size=24, color=WHITE)
        origin.move_to(UP * 3.0)
        self.play(FadeIn(origin, shift=UP * 0.2), run_time=0.4)

        # 画一个圆说明
        circ = Circle(radius=0.7, color=COLOR_PI, stroke_width=3)
        circ.move_to(LEFT * 2.5 + UP * 1.5)
        diam = Line(circ.get_left(), circ.get_right(),
                    color=WHITE, stroke_width=2, stroke_opacity=0.7)
        circ_lbl = MathTex(r"C", font_size=26, color=COLOR_PI)
        circ_lbl.next_to(circ, UP, buff=0.1)
        d_lbl = MathTex(r"d", font_size=26, color=WHITE)
        d_lbl.next_to(diam, DOWN, buff=0.1)
        pi_frac = MathTex(r"\pi = \frac{C}{d}", font_size=34, color=COLOR_PI)
        pi_frac.next_to(circ, RIGHT, buff=0.5)

        self.play(Create(circ), Create(diam), run_time=0.5)
        self.play(
            FadeIn(circ_lbl), FadeIn(d_lbl),
            Write(pi_frac), run_time=0.5
        )

        precise_pi = MathTex(
            r"\pi \approx 3.14159265\ldots",
            font_size=34, color=COLOR_PI
        )
        precise_pi.move_to(DOWN * 0.5)
        box_pi = SurroundingRectangle(precise_pi, color=COLOR_PI, buff=0.18, corner_radius=0.1)
        self.play(Write(precise_pi), Create(box_pi), run_time=0.6)

        self.wait(1.2)
        self.play(FadeOut(VGroup(
            sec, pi_label, int_pi, row1, dots1, row2, dots2,
            origin, circ, diam, circ_lbl, d_lbl, pi_frac,
            precise_pi, box_pi
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 5  无理数定义
    # ══════════════════════════════════════════════
    def scene_definition(self):
        sec = Text("什么是无理数？", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        defn_box = RoundedRectangle(
            width=7.8, height=1.5, corner_radius=0.18,
            color=COLOR_IRRATIONAL,
            fill_color=COLOR_IRRATIONAL, fill_opacity=0.15, stroke_width=2
        ).move_to(UP * 5.6)

        defn_line1 = Text("无限不循环小数", font=FONT, font_size=32, color=WHITE)
        defn_line2 = Text("叫做无理数", font=FONT, font_size=32, color=COLOR_IRRATIONAL)
        defn_grp = VGroup(defn_line1, defn_line2).arrange(RIGHT, buff=0.2)
        defn_grp.move_to(defn_box.get_center())

        self.play(Create(defn_box), run_time=0.4)
        self.play(Write(defn_grp), run_time=0.6)

        # 判断方法
        method_title = Text("判断方法：", font=FONT, font_size=28, color=YELLOW)
        method_title.move_to(LEFT * 1.5 + UP * 4.3)

        steps = [
            "① 能否化为分数 p/q（p,q整数，q≠0）？",
            "② 小数是有限的还是无限循环的？",
            "③ 如果都不能 → 无理数",
        ]
        step_mobs = VGroup()
        for i, s in enumerate(steps):
            sm = Text(s, font=FONT, font_size=22, color=WHITE)
            sm.move_to(UP * (3.5 - i * 0.75))
            sm.align_to(LEFT * 0.4, LEFT)
            step_mobs.add(sm)

        self.play(FadeIn(method_title, shift=RIGHT * 0.2), run_time=0.4)
        for sm in step_mobs:
            self.play(FadeIn(sm, shift=RIGHT * 0.15), run_time=0.35)

        # 例子判断表
        examples = [
            (r"\sqrt{2}",      "无限不循环",   "✓ 无理数", COLOR_IRRATIONAL),
            (r"\pi",           "无限不循环",   "✓ 无理数", COLOR_IRRATIONAL),
            (r"0.\overline{3}","无限循环",      "✗ 有理数", COLOR_RATIONAL),
            (r"1.5",           "有限小数",      "✗ 有理数", COLOR_RATIONAL),
            (r"\sqrt{4} = 2",  "整数",          "✗ 有理数", COLOR_RATIONAL),
        ]

        all_ex = VGroup()
        for i, (num, desc, verdict, col) in enumerate(examples):
            y = 1.0 - i * 0.85
            num_m = MathTex(num, font_size=28, color=col)
            num_m.move_to(LEFT * 3.2 + UP * y)
            desc_m = Text(desc, font=FONT, font_size=20, color=GRAY_A)
            desc_m.move_to(LEFT * 0.2 + UP * y)
            verd_m = Text(verdict, font=FONT, font_size=20, color=col)
            verd_m.move_to(RIGHT * 2.8 + UP * y)
            sh = Line(LEFT * 4.2 + UP * (y - 0.38),
                      RIGHT * 4.2 + UP * (y - 0.38),
                      color=GRAY, stroke_width=0.6, stroke_opacity=0.4)
            self.play(
                FadeIn(num_m), FadeIn(desc_m), FadeIn(verd_m), Create(sh),
                run_time=0.4
            )
            all_ex.add(num_m, desc_m, verd_m, sh)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            sec, defn_box, defn_grp,
            method_title, step_mobs, all_ex
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 6  数轴上的无理数
    # ══════════════════════════════════════════════
    def scene_number_line(self):
        sec = Text("无理数在数轴上的位置", font=FONT, font_size=32, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 主数轴
        nl = NumberLine(
            x_range=[-1, 4, 1], length=7.0,
            include_numbers=True, include_tip=True,
            numbers_to_exclude=[],
            color=COLOR_AXIS, font_size=26,
            tip_width=0.18, tip_height=0.18,
        )
        nl.move_to(UP * 5.2)
        self.play(Create(nl), run_time=0.8)

        # ── √2 在数轴上的精确位置 ──
        sqrt2_val = np.sqrt(2)  # ≈ 1.41421
        sqrt2_pt = nl.number_to_point(sqrt2_val)

        # 几何作图：以原点为圆心，斜边为半径
        # 正方形斜边 = √2
        # 在数轴下方画正方形
        sq_side = nl.number_to_point(1) - nl.number_to_point(0)  # 1 单位长度向量
        sq_len = np.linalg.norm(sq_side)  # 数轴上1单位对应的像素距离

        origin_pt = nl.number_to_point(0)
        one_pt    = nl.number_to_point(1)

        # 正方形（1×1）在数轴下方
        sq_offset = DOWN * sq_len
        sq = Polygon(
            origin_pt,
            one_pt,
            one_pt + sq_offset,
            origin_pt + sq_offset,
            color=COLOR_RATIONAL,
            fill_color=COLOR_RATIONAL, fill_opacity=0.15,
            stroke_width=2
        )
        diag_line = Line(origin_pt, one_pt + sq_offset,
                         color=COLOR_SQRT2, stroke_width=3)
        diag_label = MathTex(r"\sqrt{2}", font_size=24, color=COLOR_SQRT2)
        diag_mid = (origin_pt + one_pt + sq_offset) / 2
        diag_label.move_to(diag_mid + LEFT * 0.35 + DOWN * 0.1)

        self.play(Create(sq), run_time=0.6)
        self.play(Create(diag_line), Write(diag_label), run_time=0.5)

        # 以原点为圆心、√2 为半径画弧，截数轴得√2位置
        # 弧从正方形斜边终点旋转到数轴
        arc = Arc(
            radius=sq_len * np.sqrt(2),
            start_angle=-np.pi / 2 + np.arctan(1),  # 斜边终点方向
            angle=np.pi / 2 - np.arctan(1),          # 转到数轴水平
            color=COLOR_SQRT2, stroke_width=2,
            stroke_opacity=0.6
        )
        arc.move_arc_center_to(origin_pt)

        sqrt2_dot = Dot(sqrt2_pt, radius=0.12, color=COLOR_SQRT2)
        sqrt2_lbl = MathTex(r"\sqrt{2}", font_size=28, color=COLOR_SQRT2)
        sqrt2_lbl.next_to(sqrt2_dot, UP, buff=0.25)

        self.play(Create(arc), run_time=0.8)
        self.play(FadeIn(sqrt2_dot, scale=0.5), Write(sqrt2_lbl), run_time=0.4)

        # ── π 的位置 ──
        pi_val = np.pi  # ≈ 3.14159
        pi_pt = nl.number_to_point(pi_val)
        pi_dot = Dot(pi_pt, radius=0.12, color=COLOR_PI)
        pi_lbl = MathTex(r"\pi", font_size=28, color=COLOR_PI)
        pi_lbl.next_to(pi_dot, UP, buff=0.25)
        pi_approx = MathTex(r"\approx 3.14159\ldots", font_size=22, color=COLOR_PI)
        pi_approx.next_to(pi_lbl, RIGHT, buff=0.1)

        self.play(FadeIn(pi_dot, scale=0.5), Write(pi_lbl), run_time=0.4)
        self.play(FadeIn(pi_approx, shift=UP * 0.1), run_time=0.3)

        # 说明：数轴上每个点都有对应的实数
        explain = Text("数轴上每个点对应唯一实数（有理数或无理数）",
                       font=FONT, font_size=22, color=WHITE)
        explain.move_to(UP * 2.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)

        # 实数分类小结
        real_title = Text("实数", font=FONT, font_size=26, color=GOLD)
        real_title.move_to(LEFT * 0.3 + UP * 1.2)

        lbrace_area = VGroup(
            Text("有理数", font=FONT, font_size=22, color=COLOR_RATIONAL).move_to(LEFT * 2.0 + UP * 0.3),
            Text("无理数", font=FONT, font_size=22, color=COLOR_IRRATIONAL).move_to(RIGHT * 1.2 + UP * 0.3),
        )

        self.play(FadeIn(real_title), FadeIn(lbrace_area), run_time=0.5)

        formula_r = Text("实数 = 有理数 ∪ 无理数",
                         font=FONT, font_size=26, color=YELLOW)
        formula_r.move_to(DOWN * 0.6)
        box_r = SurroundingRectangle(formula_r, color=YELLOW, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(formula_r), Create(box_r), run_time=0.5)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            sec, nl, sq, diag_line, diag_label, arc,
            sqrt2_dot, sqrt2_lbl, pi_dot, pi_lbl, pi_approx,
            explain, real_title, lbrace_area, formula_r, box_r
        )), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 7  总结 + 片尾
    # ══════════════════════════════════════════════
    def scene_outro(self):
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.3)

        sum_title = Text("本节要点", font=FONT, font_size=36, color=GOLD)
        sum_title.move_to(UP * 7.0)
        self.play(Write(sum_title), run_time=0.4)

        # 每条 (is_math, content, col)
        # 第3条含中文，拆成 MathTex + Text 拼合
        points_plain = [
            "无理数 = 无限不循环小数",
            "不能写成 p/q 的形式",
            None,                          # 第3条特殊处理
            "有理数 + 无理数 = 实数",
            "数轴上每个点对应唯一实数",
        ]
        points_color = [
            COLOR_IRRATIONAL,
            COLOR_IRRATIONAL,
            COLOR_IRRATIONAL,
            YELLOW,
            WHITE,
        ]

        point_mobs = VGroup()
        for i in range(len(points_plain)):
            col = points_color[i]
            y = 5.6 - i * 1.05
            anchor = UP * y + RIGHT * 0.4

            if points_plain[i] is None:
                # 第3条：MathTex 部分 + Text 部分拼合
                math_part = MathTex(r"\sqrt{2},\ \sqrt{3},\ \pi", font_size=30, color=col)
                text_part = Text("都是无理数", font=FONT, font_size=24, color=col)
                mob = VGroup(math_part, text_part).arrange(RIGHT, buff=0.15)
            else:
                mob = Text(points_plain[i], font=FONT, font_size=24, color=col)

            mob.move_to(anchor)
            mob.align_to(LEFT * 0.3, LEFT)
            dot = Dot(radius=0.07, color=col).next_to(mob, LEFT, buff=0.2)
            grp = VGroup(dot, mob)
            point_mobs.add(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.35)

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

        # 装饰：滚动小数 — 用固定彩色列表替代不支持的 Color(hue=...) API
        rainbow_colors = [
            "#ff6b6b", "#ffa94d", "#ffd43b", "#69db7c",
            "#74c0fc", "#e599f7", "#f783ac", "#a9e34b",
            "#63e6be", "#ff8787",
        ]
        digits_deco = VGroup(*[
            MathTex(d, font_size=22, color=rainbow_colors[i % len(rainbow_colors)])
            .move_to(DOWN * 2.3 + RIGHT * (-4.0 + i * 0.85))
            for i, d in enumerate(["1", ".", "4", "1", "4", "2", "1", "3", "5", "6"])
        ])
        self.play(*[FadeIn(d, shift=UP * 0.2) for d in digits_deco], run_time=0.6)

        finale = MathTex(r"\sqrt{2} \approx 1.41421\ldots",
                         font_size=38, color=COLOR_SQRT2)
        finale.move_to(DOWN * 3.5)
        self.play(Write(finale), run_time=0.6)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            self.author_obj, author_id, follow,
            digits_deco, finale
        )), run_time=0.8)


# 渲染:
#   manim -pql irrational_concept.py IrrationalNumberConcept
#   manim -qh  irrational_concept.py IrrationalNumberConcept