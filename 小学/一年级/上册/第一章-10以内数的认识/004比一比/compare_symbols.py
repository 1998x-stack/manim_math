"""
compare_symbols.py  ──  比一比（>, <, =）
一年级上册·第一章·10以内数的认识

内容: 大于、小于、等于符号的认识与使用
目标: TikTok 竖屏 1080×1920，约55秒
作者: 上海初高中数学直通车  @emptyandcalm
"""

from manim import *
import numpy as np

# ════════════════════════════════════════════════════
# 全局配置
# ════════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG_COLOR   = "#1a1a2e"
C_GT       = "#e74c3c"   # 红  > 大于
C_LT       = "#3498db"   # 蓝  < 小于
C_EQ       = "#2ecc71"   # 绿  = 等于
C_ACTIVE   = "#f1c40f"   # 黄  高亮
C_PASSIVE  = "#374151"   # 暗  非关注
C_LINE     = "#9ca3af"   # 灰  连线
C_DIM      = "#888899"
FONT       = "PingFang SC"

# 布局常量（与 verify_compare.py 一致）
ROW_Y    = 2.6
R        = 0.38
SPACING  = 0.9
LEFT_CX  = -2.0
RIGHT_CX =  2.0

LEFT_COLORS  = ["#ef4444","#f97316","#eab308","#22c55e"]
RIGHT_COLORS = ["#60a5fa","#a78bfa","#f472b6","#34d399"]


def row_centers(n, cx, cy, sp=SPACING):
    return [np.array([cx + (i-(n-1)/2.0)*sp, cy, 0.0]) for i in range(n)]


def make_circles(n, cx, cy, color=None, colors=None):
    """生成一排 n 个彩色圆（含数字编号）"""
    grp = VGroup()
    positions = row_centers(n, cx, cy)
    pool = LEFT_COLORS if cx < 0 else RIGHT_COLORS
    for i, pos in enumerate(positions):
        col = (colors[i] if colors else (color if color else pool[i % len(pool)]))
        circle = Circle(radius=R, fill_color=col, fill_opacity=1,
                        stroke_color=WHITE, stroke_width=2).move_to(pos)
        grp.add(circle)
    return grp


# ════════════════════════════════════════════════════
# 主场景
# ════════════════════════════════════════════════════
class CompareSymbols(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_DIM,
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_greater()
        self.scene_3_less()
        self.scene_4_equal()
        self.scene_5_rule()
        self.scene_6_practice()
        self.scene_7_outro()

    # ─────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────
    def scene_1_hook(self):
        title = Text("比一比", font=FONT, font_size=60, color=C_ACTIVE)
        title.move_to(UP * 5.6)
        sub = Text("谁多谁少？", font=FONT, font_size=36, color=WHITE)
        sub.move_to(UP * 4.7)
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 三个符号依次飞入
        sym_gt = MathTex(r">", font_size=90, color=C_GT).move_to(LEFT * 2.5 + UP * 2.8)
        sym_eq = MathTex(r"=", font_size=90, color=C_EQ).move_to(UP * 2.8)
        sym_lt = MathTex(r"<", font_size=90, color=C_LT).move_to(RIGHT * 2.5 + UP * 2.8)

        for sym in [sym_gt, sym_eq, sym_lt]:
            self.play(GrowFromCenter(sym), run_time=0.3)
        self.wait(0.6)

        label_gt = Text("大于", font=FONT, font_size=26, color=C_GT).next_to(sym_gt, DOWN, buff=0.2)
        label_eq = Text("等于", font=FONT, font_size=26, color=C_EQ).next_to(sym_eq, DOWN, buff=0.2)
        label_lt = Text("小于", font=FONT, font_size=26, color=C_LT).next_to(sym_lt, DOWN, buff=0.2)
        self.play(
            FadeIn(label_gt), FadeIn(label_eq), FadeIn(label_lt),
            run_time=0.4,
        )
        self.wait(0.8)
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(sym_gt), FadeOut(sym_eq), FadeOut(sym_lt),
            FadeOut(label_gt), FadeOut(label_eq), FadeOut(label_lt),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 2: 大于号 >
    # ─────────────────────────────────────────
    def scene_2_greater(self):
        sec_title = Text("大于号  >", font=FONT, font_size=42, color=C_GT)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        # 左3个，右2个
        left_n, right_n = 3, 2
        left_circles  = make_circles(left_n,  LEFT_CX,  ROW_Y)
        right_circles = make_circles(right_n, RIGHT_CX, ROW_Y)

        # 圆依次出现
        for c in left_circles:
            self.play(GrowFromCenter(c), run_time=0.18)
        for c in right_circles:
            self.play(GrowFromCenter(c), run_time=0.18)

        # ── 一一对应连线
        lc = row_centers(left_n,  LEFT_CX,  ROW_Y)
        rc = row_centers(right_n, RIGHT_CX, ROW_Y)
        line_y = ROW_Y - 0.85

        match_lines = VGroup()
        for i in range(right_n):
            line = DashedLine(
                np.array([lc[i][0], line_y, 0]),
                np.array([rc[i][0], line_y, 0]),
                color=C_LINE, stroke_width=2, dash_length=0.1,
            )
            match_lines.add(line)
            self.play(Create(line), run_time=0.25)

        # 左侧第3个（多出的）高亮红色
        extra = left_circles[2]
        self.play(
            extra.animate.set_fill(C_GT).set_stroke(color=C_ACTIVE, width=5),
            run_time=0.35,
        )
        extra_lbl = Text("多1个！", font=FONT, font_size=24, color=C_GT)
        extra_lbl.next_to(extra, UP, buff=0.2)
        self.play(FadeIn(extra_lbl, scale=1.2), run_time=0.3)
        self.wait(0.3)

        # 结论
        conclusion = VGroup(
            Text("左边", font=FONT, font_size=32, color=WHITE),
            Text(" 多 ", font=FONT, font_size=32, color=C_GT),
            Text("→", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.5)
        self.play(FadeIn(conclusion), run_time=0.4)

        formula = MathTex(r"3 > 2", font_size=72, color=C_GT)
        formula.move_to(DOWN * 1.8)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(left_circles), FadeOut(right_circles),
            FadeOut(match_lines), FadeOut(extra_lbl),
            FadeOut(conclusion), FadeOut(formula),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 3: 小于号 <
    # ─────────────────────────────────────────
    def scene_3_less(self):
        sec_title = Text("小于号  <", font=FONT, font_size=42, color=C_LT)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        # 左2个，右3个
        left_n, right_n = 2, 3
        left_circles  = make_circles(left_n,  LEFT_CX,  ROW_Y)
        right_circles = make_circles(right_n, RIGHT_CX, ROW_Y)

        for c in [*left_circles, *right_circles]:
            self.play(GrowFromCenter(c), run_time=0.18)

        lc = row_centers(left_n,  LEFT_CX,  ROW_Y)
        rc = row_centers(right_n, RIGHT_CX, ROW_Y)
        line_y = ROW_Y - 0.85

        match_lines = VGroup()
        for i in range(left_n):
            line = DashedLine(
                np.array([lc[i][0], line_y, 0]),
                np.array([rc[i][0], line_y, 0]),
                color=C_LINE, stroke_width=2, dash_length=0.1,
            )
            match_lines.add(line)
            self.play(Create(line), run_time=0.25)

        # 右侧第3个（多出的）高亮蓝色
        extra = right_circles[2]
        self.play(
            extra.animate.set_fill(C_LT).set_stroke(color=C_ACTIVE, width=5),
            run_time=0.35,
        )
        extra_lbl = Text("多1个！", font=FONT, font_size=24, color=C_LT)
        extra_lbl.next_to(extra, UP, buff=0.2)
        self.play(FadeIn(extra_lbl, scale=1.2), run_time=0.3)
        self.wait(0.3)

        conclusion = VGroup(
            Text("右边", font=FONT, font_size=32, color=WHITE),
            Text(" 多 ", font=FONT, font_size=32, color=C_LT),
            Text("→", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.5)
        self.play(FadeIn(conclusion), run_time=0.4)

        formula = MathTex(r"2 < 3", font_size=72, color=C_LT)
        formula.move_to(DOWN * 1.8)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(left_circles), FadeOut(right_circles),
            FadeOut(match_lines), FadeOut(extra_lbl),
            FadeOut(conclusion), FadeOut(formula),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 4: 等于号 =
    # ─────────────────────────────────────────
    def scene_4_equal(self):
        sec_title = Text("等于号  =", font=FONT, font_size=42, color=C_EQ)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        left_n = right_n = 3
        left_circles  = make_circles(left_n,  LEFT_CX,  ROW_Y)
        right_circles = make_circles(right_n, RIGHT_CX, ROW_Y)

        for c in [*left_circles, *right_circles]:
            self.play(GrowFromCenter(c), run_time=0.18)

        lc = row_centers(left_n,  LEFT_CX,  ROW_Y)
        rc = row_centers(right_n, RIGHT_CX, ROW_Y)
        line_y = ROW_Y - 0.85

        match_lines = VGroup()
        for i in range(left_n):
            line = DashedLine(
                np.array([lc[i][0], line_y, 0]),
                np.array([rc[i][0], line_y, 0]),
                color=C_EQ, stroke_width=2, dash_length=0.1,
            )
            match_lines.add(line)
            self.play(Create(line), run_time=0.22)

        # 全部绿色高亮
        self.play(
            *[c.animate.set_stroke(color=C_EQ, width=5) for c in left_circles],
            *[c.animate.set_stroke(color=C_EQ, width=5) for c in right_circles],
            run_time=0.4,
        )

        equal_lbl = Text("一样多！", font=FONT, font_size=32, color=C_EQ)
        equal_lbl.move_to(DOWN * 0.5)
        self.play(FadeIn(equal_lbl, scale=1.2), run_time=0.4)

        formula = MathTex(r"3 = 3", font_size=72, color=C_EQ)
        formula.move_to(DOWN * 1.8)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(left_circles), FadeOut(right_circles),
            FadeOut(match_lines), FadeOut(equal_lbl), FadeOut(formula),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 5: 口诀
    # ─────────────────────────────────────────
    def scene_5_rule(self):
        title = Text("记住口诀！", font=FONT, font_size=44, color=C_ACTIVE)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 口诀卡片
        card = RoundedRectangle(
            width=7.5, height=2.6, corner_radius=0.35,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=C_ACTIVE, stroke_width=3,
        ).move_to(UP * 4.2)

        line_a = Text("开口朝大数", font=FONT, font_size=34, color=WHITE)
        line_b = Text("尖尖对小数", font=FONT, font_size=34, color=WHITE)
        VGroup(line_a, line_b).arrange(DOWN, buff=0.35).move_to(card)

        self.play(Create(card), run_time=0.4)
        self.play(Write(line_a), run_time=0.5)
        self.play(Write(line_b), run_time=0.5)
        self.wait(0.3)

        # 动态演示符号方向
        demo_y = UP * 1.3

        # > 演示
        sym_gt  = MathTex(r">", font_size=80, color=C_GT).move_to(LEFT * 2.0 + demo_y)
        num_3   = MathTex(r"3", font_size=60, color=C_GT).next_to(sym_gt, LEFT, buff=0.3)
        num_2   = MathTex(r"2", font_size=60, color=WHITE).next_to(sym_gt, RIGHT, buff=0.3)
        arrow_open = Arrow(
            sym_gt.get_left() + RIGHT*0.1,
            num_3.get_right(),
            color=C_GT, buff=0.05, stroke_width=4,
            max_tip_length_to_length_ratio=0.3,
        )
        lbl_open = Text("开口→大数3", font=FONT, font_size=18, color=C_GT)
        lbl_open.next_to(sym_gt, DOWN, buff=1.1)

        self.play(FadeIn(num_3), Write(sym_gt), FadeIn(num_2), run_time=0.5)
        self.play(GrowArrow(arrow_open), FadeIn(lbl_open), run_time=0.4)

        # < 演示
        sym_lt  = MathTex(r"<", font_size=80, color=C_LT).move_to(RIGHT * 2.0 + demo_y)
        num_2b  = MathTex(r"2", font_size=60, color=WHITE).next_to(sym_lt, LEFT, buff=0.3)
        num_3b  = MathTex(r"3", font_size=60, color=C_LT).next_to(sym_lt, RIGHT, buff=0.3)
        arrow_open2 = Arrow(
            sym_lt.get_right() + LEFT*0.1,
            num_3b.get_left(),
            color=C_LT, buff=0.05, stroke_width=4,
            max_tip_length_to_length_ratio=0.3,
        )
        lbl_open2 = Text("开口→大数3", font=FONT, font_size=18, color=C_LT)
        lbl_open2.next_to(sym_lt, DOWN, buff=1.1)

        self.play(FadeIn(num_2b), Write(sym_lt), FadeIn(num_3b), run_time=0.5)
        self.play(GrowArrow(arrow_open2), FadeIn(lbl_open2), run_time=0.4)

        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(card), FadeOut(line_a), FadeOut(line_b),
            FadeOut(sym_gt), FadeOut(num_3), FadeOut(num_2),
            FadeOut(arrow_open), FadeOut(lbl_open),
            FadeOut(sym_lt), FadeOut(num_2b), FadeOut(num_3b),
            FadeOut(arrow_open2), FadeOut(lbl_open2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 6: 练习
    # ─────────────────────────────────────────
    def scene_6_practice(self):
        title = Text("填填看！", font=FONT, font_size=44, color=C_ACTIVE)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.4)

        # 三道题依次呈现
        questions = [
            (4, 2, ">", C_GT,  r"4 > 2"),
            (2, 4, "<", C_LT,  r"2 < 4"),
            (3, 3, "=", C_EQ,  r"3 = 3"),
        ]

        y_start = UP * 4.5
        rows = VGroup()

        for i, (left_n, right_n, sym_str, col, formula_str) in enumerate(questions):
            y = UP * (4.5 - i * 1.5)

            # 左侧圆点
            lc_small = row_centers(left_n, -3.0, y[1], sp=0.5)
            rc_small = row_centers(right_n,  3.0, y[1], sp=0.5)

            left_dots = VGroup(*[
                Circle(radius=0.18, fill_color=LEFT_COLORS[j % 4],
                       fill_opacity=1, stroke_width=0).move_to(p)
                for j, p in enumerate(lc_small)
            ])
            right_dots = VGroup(*[
                Circle(radius=0.18, fill_color=RIGHT_COLORS[j % 4],
                       fill_opacity=1, stroke_width=0).move_to(p)
                for j, p in enumerate(rc_small)
            ])

            # 问号占位
            blank = Text("?", font=FONT, font_size=40, color=C_ACTIVE)
            blank.move_to(y)

            row = VGroup(left_dots, blank, right_dots)
            rows.add(row)
            self.play(
                LaggedStart(*[GrowFromCenter(d) for d in [*left_dots, *right_dots]],
                            lag_ratio=0.08),
                FadeIn(blank),
                run_time=0.5,
            )

        self.wait(0.5)

        # 逐行揭晓答案
        for i, (left_n, right_n, sym_str, col, formula_str) in enumerate(questions):
            y = UP * (4.5 - i * 1.5)
            sym_tex = MathTex(sym_str, font_size=44, color=col)
            sym_tex.move_to(y)
            blank_obj = rows[i][1]
            self.play(Transform(blank_obj, sym_tex), run_time=0.35)
            self.play(Indicate(sym_tex, scale_factor=1.4, color=col), run_time=0.3)

        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(rows), run_time=0.5)

    # ─────────────────────────────────────────
    # Scene 7: 片尾
    # ─────────────────────────────────────────
    def scene_7_outro(self):
        card = RoundedRectangle(
            width=7.5, height=3.5, corner_radius=0.4,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=C_ACTIVE, stroke_width=3,
        ).move_to(UP * 4.2)

        summary = VGroup(
            VGroup(MathTex(r">", font_size=40, color=C_GT),
                   Text(" 大于：左大右小", font=FONT, font_size=28, color=WHITE)
                   ).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"<", font_size=40, color=C_LT),
                   Text(" 小于：左小右大", font=FONT, font_size=28, color=WHITE)
                   ).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"=", font_size=40, color=C_EQ),
                   Text(" 等于：两边一样多", font=FONT, font_size=28, color=WHITE)
                   ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(card)

        self.play(Create(card), run_time=0.4)
        for line in summary:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(0.4)

        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=36, color=WHITE).move_to(UP * 0.8)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=26, color=C_DIM).move_to(UP * 0.0)
        follow     = Text("关注我，学更多数学！",
                          font=FONT, font_size=30, color=C_ACTIVE).move_to(DOWN * 0.9)

        self.play(Transform(self.author_bar, author_big), run_time=0.5)
        self.play(FadeIn(author_id), FadeIn(follow, scale=1.1), run_time=0.5)

        # 符号环绕
        deco = VGroup(
            MathTex(r">", font_size=50, color=C_GT).move_to(LEFT * 3.0 + DOWN * 2.5),
            MathTex(r"=", font_size=50, color=C_EQ).move_to(DOWN * 2.8),
            MathTex(r"<", font_size=50, color=C_LT).move_to(RIGHT * 3.0 + DOWN * 2.5),
        )
        self.play(LaggedStart(*[GrowFromCenter(d) for d in deco], lag_ratio=0.2), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(self.author_bar), FadeOut(author_id), FadeOut(follow),
                  FadeOut(card), FadeOut(summary), FadeOut(deco), run_time=1.0)


# ════════════════════════════════════════════════════
# manim -pql compare_symbols.py CompareSymbols
# manim -qh  compare_symbols.py CompareSymbols
# ════════════════════════════════════════════════════