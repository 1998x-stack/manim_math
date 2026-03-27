"""
长方形和正方形的面积 - 小学三年级下册
知识点: 长方形面积 = 长 × 宽 (S = a × b); 正方形面积 = 边长 × 边长 (S = a²)
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class RectSquareAreaLesson(Scene):
    """
    长方形和正方形的面积教学动画

    场景顺序:
    1. 开场引入 — 钩子问题
    2. 用面积单位铺满长方形 — 理解公式来源
    3. 长方形面积公式推导
    4. 正方形面积公式
    5. 例题演示
    6. 公式总结
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 颜色配置 ──────────────────────────────
        self.COL_RECT = "#3a86ff"        # 长方形蓝色
        self.COL_SQ   = "#06d6a0"        # 正方形绿色
        self.COL_UNIT = "#ffd166"        # 小格黄色
        self.COL_HL   = "#ef476f"        # 强调红色
        self.COL_FORM = "#ffffff"        # 公式白色
        self.COL_GRAY = "#9ca3af"        # 灰色辅助

        # ── 品牌标识 ──────────────────────────────
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.add(self.author)

        # ── 场景序列 ──────────────────────────────
        self.scene_opening()
        self.scene_tile_demo()
        self.scene_rect_formula()
        self.scene_square_formula()
        self.scene_examples()
        self.scene_summary()
        self.scene_outro()

    # ─────────────────────────────────────────────
    # 场景 1 · 开场引入
    # ─────────────────────────────────────────────
    def scene_opening(self):
        # 钩子问题
        hook = Text(
            "怎么快速算出\n这块地有多大？",
            font="PingFang SC",
            font_size=38,
            color=self.COL_HL,
            line_spacing=1.2,
        ).move_to(UP * 5.0)

        # 展示一个绿色"地块"
        land = Rectangle(
            width=3.6, height=2.2,
            fill_color="#2d6a4f",
            fill_opacity=0.85,
            stroke_color=self.COL_SQ,
            stroke_width=3,
        ).move_to(UP * 2.2)

        # 长宽标注
        brace_w = Brace(land, DOWN, buff=0.12, color=self.COL_GRAY)
        brace_w_lbl = Text("长 = 4 m", font="PingFang SC",
                           font_size=22, color=self.COL_GRAY).next_to(brace_w, DOWN, buff=0.1)
        brace_h = Brace(land, RIGHT, buff=0.12, color=self.COL_GRAY)
        brace_h_lbl = Text("宽 = 3 m", font="PingFang SC",
                           font_size=22, color=self.COL_GRAY).next_to(brace_h, RIGHT, buff=0.1)

        question_mark = Text("面积 = ?", font="PingFang SC",
                             font_size=32, color=self.COL_HL).move_to(UP * 2.2)

        title_main = Text("长方形和正方形的面积",
                          font="PingFang SC",
                          font_size=34, color=GOLD).move_to(DOWN * 1.6)

        self.play(Write(hook), run_time=0.9)
        self.play(Create(land), run_time=0.8)
        self.play(
            GrowFromEdge(brace_w, LEFT),
            FadeIn(brace_w_lbl, shift=DOWN * 0.2),
            GrowFromEdge(brace_h, DOWN),
            FadeIn(brace_h_lbl, shift=RIGHT * 0.2),
            run_time=0.7,
        )
        self.play(Write(question_mark), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(title_main, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(hook),
            FadeOut(land),
            FadeOut(brace_w), FadeOut(brace_w_lbl),
            FadeOut(brace_h), FadeOut(brace_h_lbl),
            FadeOut(question_mark),
            FadeOut(title_main),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 2 · 用面积单位铺满长方形
    # ─────────────────────────────────────────────
    def scene_tile_demo(self):
        sec_title = Text("用小方格铺一铺",
                         font="PingFang SC",
                         font_size=32, color=GOLD).move_to(UP * 6.2)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # 长方形: 4列 × 3行，每格边长 0.72
        cols, rows = 4, 3
        cell = 0.72
        rect_w = cols * cell   # 2.88
        rect_h = rows * cell   # 2.16

        # 画底部长方形框
        big_rect = Rectangle(
            width=rect_w, height=rect_h,
            stroke_color=self.COL_RECT,
            stroke_width=3,
            fill_opacity=0,
        ).move_to(UP * 3.2)

        self.play(Create(big_rect), run_time=0.7)

        # 长宽标注
        brace_cols = Brace(big_rect, DOWN, buff=0.1, color=self.COL_GRAY)
        lbl_cols = Text("长 = 4格", font="PingFang SC",
                        font_size=20, color=self.COL_GRAY).next_to(brace_cols, DOWN, buff=0.08)
        brace_rows = Brace(big_rect, RIGHT, buff=0.1, color=self.COL_GRAY)
        lbl_rows = Text("宽 = 3格", font="PingFang SC",
                        font_size=20, color=self.COL_GRAY).next_to(brace_rows, RIGHT, buff=0.08)

        self.play(
            GrowFromEdge(brace_cols, LEFT), FadeIn(lbl_cols),
            GrowFromEdge(brace_rows, DOWN), FadeIn(lbl_rows),
            run_time=0.6,
        )

        # 逐行铺入小方格
        all_cells = VGroup()
        rect_center = big_rect.get_center()
        start_x = rect_center[0] - rect_w / 2 + cell / 2
        start_y = rect_center[1] + rect_h / 2 - cell / 2

        for r in range(rows):
            for c in range(cols):
                sq = Square(
                    side_length=cell - 0.04,
                    fill_color=self.COL_UNIT,
                    fill_opacity=0.55,
                    stroke_color=self.COL_UNIT,
                    stroke_width=1.0,
                ).move_to(
                    np.array([start_x + c * cell, start_y - r * cell, 0])
                )
                all_cells.add(sq)

        # 逐行动画
        for r in range(rows):
            row_cells = VGroup(*[all_cells[r * cols + c] for c in range(cols)])
            self.play(
                LaggedStart(*[FadeIn(sq, scale=0.6) for sq in row_cells],
                            lag_ratio=0.15),
                run_time=0.55,
            )

        # 统计提示
        count_text = Text(
            "共 12 个小方格",
            font="PingFang SC",
            font_size=26, color=self.COL_HL,
        ).move_to(UP * 1.3)

        row_hint = Text(
            "每行 4 个，共 3 行",
            font="PingFang SC",
            font_size=22, color=self.COL_GRAY,
        ).next_to(count_text, DOWN, buff=0.25)

        formula_hint = Text("面积 = 每行个数 × 行数",
                            font="PingFang SC",
                            font_size=22, color=WHITE).move_to(UP * 0.2)

        formula_val = VGroup(
            Text("= 4 × 3 = ", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("12", font="PingFang SC",
                 font_size=30, color=self.COL_HL),
            Text(" 格", font="PingFang SC",
                 font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.08).next_to(formula_hint, DOWN, buff=0.2)

        self.play(FadeIn(count_text, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(row_hint), run_time=0.4)
        self.play(FadeIn(formula_hint), run_time=0.4)
        self.play(FadeIn(formula_val), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(sec_title),
            FadeOut(big_rect), FadeOut(all_cells),
            FadeOut(brace_cols), FadeOut(lbl_cols),
            FadeOut(brace_rows), FadeOut(lbl_rows),
            FadeOut(count_text), FadeOut(row_hint),
            FadeOut(formula_hint), FadeOut(formula_val),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 3 · 长方形面积公式推导
    # ─────────────────────────────────────────────
    def scene_rect_formula(self):
        sec_title = Text("长方形的面积",
                         font="PingFang SC",
                         font_size=34, color=self.COL_RECT).move_to(UP * 6.2)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # 画长方形  宽 3.6  高 2.2
        rect_w, rect_h = 3.6, 2.2
        rect = Rectangle(
            width=rect_w, height=rect_h,
            fill_color=self.COL_RECT,
            fill_opacity=0.25,
            stroke_color=self.COL_RECT,
            stroke_width=3,
        ).move_to(UP * 3.5)

        self.play(Create(rect), run_time=0.8)

        # 长标注
        brace_a = Brace(rect, DOWN, buff=0.12, color=WHITE)
        lbl_a = VGroup(
            Text("长", font="PingFang SC", font_size=22, color=WHITE),
            Text(" a", font="PingFang SC", font_size=22, color=self.COL_RECT),
        ).arrange(RIGHT, buff=0.05).next_to(brace_a, DOWN, buff=0.1)

        # 宽标注
        brace_b = Brace(rect, LEFT, buff=0.12, color=WHITE)
        lbl_b = VGroup(
            Text("宽", font="PingFang SC", font_size=22, color=WHITE),
            Text(" b", font="PingFang SC", font_size=22, color=self.COL_SQ),
        ).arrange(RIGHT, buff=0.05).next_to(brace_b, LEFT, buff=0.1)

        self.play(
            GrowFromEdge(brace_a, LEFT), FadeIn(lbl_a),
            GrowFromEdge(brace_b, DOWN), FadeIn(lbl_b),
            run_time=0.7,
        )
        self.wait(0.3)

        # 推导过程
        step1 = Text("面积 = 每行个数 × 行数",
                     font="PingFang SC",
                     font_size=22, color=self.COL_GRAY).move_to(UP * 1.6)

        step2 = Text("面积 = 长 × 宽",
                     font="PingFang SC",
                     font_size=26, color=WHITE).move_to(UP * 0.8)

        arrow_down = Arrow(step1.get_bottom(), step2.get_top(),
                           buff=0.1, color=self.COL_GRAY, stroke_width=2)

        self.play(FadeIn(step1, shift=UP * 0.3), run_time=0.5)
        self.play(Create(arrow_down), run_time=0.3)
        self.play(FadeIn(step2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)

        # 公式框
        formula_box_bg = RoundedRectangle(
            width=5.5, height=1.5,
            corner_radius=0.2,
            fill_color="#0d1b2a",
            fill_opacity=0.95,
            stroke_color=self.COL_RECT,
            stroke_width=2.5,
        ).move_to(DOWN * 0.3)

        formula_line1 = Text("长方形面积 = 长 × 宽",
                             font="PingFang SC",
                             font_size=26, color=WHITE).move_to(UP * 0.1)
        formula_line2 = MathTex(r"S = a \times b",
                                font_size=36, color=self.COL_RECT).move_to(DOWN * 0.6)

        self.play(Create(formula_box_bg), run_time=0.5)
        self.play(Write(formula_line1), run_time=0.7)
        self.play(Write(formula_line2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title),
            FadeOut(rect),
            FadeOut(brace_a), FadeOut(lbl_a),
            FadeOut(brace_b), FadeOut(lbl_b),
            FadeOut(step1), FadeOut(arrow_down), FadeOut(step2),
            FadeOut(formula_box_bg),
            FadeOut(formula_line1),
            FadeOut(formula_line2),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 4 · 正方形面积公式
    # ─────────────────────────────────────────────
    def scene_square_formula(self):
        sec_title = Text("正方形的面积",
                         font="PingFang SC",
                         font_size=34, color=self.COL_SQ).move_to(UP * 6.2)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # 正方形
        side = 2.6
        sq = Square(
            side_length=side,
            fill_color=self.COL_SQ,
            fill_opacity=0.25,
            stroke_color=self.COL_SQ,
            stroke_width=3,
        ).move_to(UP * 3.6)

        self.play(Create(sq), run_time=0.8)

        # 等长刻度线
        tick_len = 0.18
        ticks = VGroup()
        center = sq.get_center()
        for direction, perp in [
            (UP,    RIGHT),
            (DOWN,  RIGHT),
            (LEFT,  UP),
            (RIGHT, UP),
        ]:
            mid = center + direction * (side / 2)
            t = Line(
                mid - perp * tick_len,
                mid + perp * tick_len,
                color=YELLOW, stroke_width=2.5,
            )
            ticks.add(t)

        self.play(Create(ticks), run_time=0.4)

        brace_a = Brace(sq, DOWN, buff=0.12, color=WHITE)
        lbl_a = VGroup(
            Text("边长", font="PingFang SC", font_size=22, color=WHITE),
            Text(" a", font="PingFang SC", font_size=22, color=self.COL_SQ),
        ).arrange(RIGHT, buff=0.05).next_to(brace_a, DOWN, buff=0.1)

        self.play(GrowFromEdge(brace_a, LEFT), FadeIn(lbl_a), run_time=0.6)

        # 说明文字
        note = Text("正方形的长和宽相等",
                    font="PingFang SC",
                    font_size=24, color=self.COL_GRAY).move_to(UP * 1.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 公式推导
        derive = Text("面积 = 边长 × 边长",
                      font="PingFang SC",
                      font_size=26, color=WHITE).move_to(UP * 0.6)

        self.play(FadeIn(derive, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)

        formula_box_bg = RoundedRectangle(
            width=5.5, height=1.6,
            corner_radius=0.2,
            fill_color="#0d1b2a",
            fill_opacity=0.95,
            stroke_color=self.COL_SQ,
            stroke_width=2.5,
        ).move_to(DOWN * 0.35)

        formula_line1 = Text("正方形面积 = 边长 × 边长",
                             font="PingFang SC",
                             font_size=24, color=WHITE).move_to(UP * 0.1)
        formula_line2 = MathTex(r"S = a^2",
                                font_size=40, color=self.COL_SQ).move_to(DOWN * 0.65)

        self.play(Create(formula_box_bg), run_time=0.5)
        self.play(Write(formula_line1), run_time=0.7)
        self.play(Write(formula_line2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title),
            FadeOut(sq), FadeOut(ticks),
            FadeOut(brace_a), FadeOut(lbl_a),
            FadeOut(note), FadeOut(derive),
            FadeOut(formula_box_bg),
            FadeOut(formula_line1), FadeOut(formula_line2),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 5 · 例题演示
    # ─────────────────────────────────────────────
    def scene_examples(self):
        sec_title = Text("例题练习",
                         font="PingFang SC",
                         font_size=34, color=GOLD).move_to(UP * 6.2)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # ── 例题 1：长方形 ─────────────────────────
        ex1_title = Text("例1  长方形",
                         font="PingFang SC",
                         font_size=28, color=self.COL_RECT).move_to(UP * 5.3)
        self.play(FadeIn(ex1_title), run_time=0.4)

        # 长方形图  长=6 cm  宽=4 cm  → 显示比例 3.6:2.4
        rw, rh = 3.6, 2.4
        rect1 = Rectangle(
            width=rw, height=rh,
            fill_color=self.COL_RECT,
            fill_opacity=0.22,
            stroke_color=self.COL_RECT,
            stroke_width=2.5,
        ).move_to(UP * 3.3)

        br_w = Brace(rect1, DOWN, buff=0.1, color=self.COL_GRAY)
        lb_w = Text("6 cm", font="PingFang SC",
                    font_size=22, color=WHITE).next_to(br_w, DOWN, buff=0.08)
        br_h = Brace(rect1, RIGHT, buff=0.1, color=self.COL_GRAY)
        lb_h = Text("4 cm", font="PingFang SC",
                    font_size=22, color=WHITE).next_to(br_h, RIGHT, buff=0.08)

        self.play(Create(rect1), run_time=0.6)
        self.play(
            GrowFromEdge(br_w, LEFT), FadeIn(lb_w),
            GrowFromEdge(br_h, DOWN), FadeIn(lb_h),
            run_time=0.5,
        )

        # 解题步骤
        sol1_data = [
            ("S = 长 × 宽",    WHITE,         UP * 1.5),
            ("= 6 × 4",        self.COL_GRAY, UP * 0.85),
            ("= 24 (cm²)",     self.COL_HL,   UP * 0.2),
        ]
        sol1_texts = []
        for txt, col, pos in sol1_data:
            t = Text(txt, font="PingFang SC", font_size=26, color=col).move_to(pos)
            sol1_texts.append(t)
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.2)

        self.wait(0.8)

        # ── 例题 2：正方形 ─────────────────────────
        self.play(
            FadeOut(ex1_title),
            FadeOut(rect1), FadeOut(br_w), FadeOut(lb_w),
            FadeOut(br_h), FadeOut(lb_h),
            *[FadeOut(t) for t in sol1_texts],
            run_time=0.5,
        )

        ex2_title = Text("例2  正方形",
                         font="PingFang SC",
                         font_size=28, color=self.COL_SQ).move_to(UP * 5.3)
        self.play(FadeIn(ex2_title), run_time=0.4)

        sq2 = Square(
            side_length=2.8,
            fill_color=self.COL_SQ,
            fill_opacity=0.22,
            stroke_color=self.COL_SQ,
            stroke_width=2.5,
        ).move_to(UP * 3.3)

        br_sq = Brace(sq2, DOWN, buff=0.1, color=self.COL_GRAY)
        lb_sq = Text("5 cm", font="PingFang SC",
                     font_size=22, color=WHITE).next_to(br_sq, DOWN, buff=0.08)

        self.play(Create(sq2), run_time=0.6)
        self.play(GrowFromEdge(br_sq, LEFT), FadeIn(lb_sq), run_time=0.5)

        sol2_data = [
            ("S = 边长 × 边长",  WHITE,         UP * 1.5),
            ("= 5 × 5",          self.COL_GRAY, UP * 0.85),
            ("= 25 (cm²)",       self.COL_HL,   UP * 0.2),
        ]
        sol2_texts = []
        for txt, col, pos in sol2_data:
            t = Text(txt, font="PingFang SC", font_size=26, color=col).move_to(pos)
            sol2_texts.append(t)
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.2)

        self.wait(0.8)

        self.play(
            FadeOut(sec_title), FadeOut(ex2_title),
            FadeOut(sq2), FadeOut(br_sq), FadeOut(lb_sq),
            *[FadeOut(t) for t in sol2_texts],
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 6 · 公式总结
    # ─────────────────────────────────────────────
    def scene_summary(self):
        sec_title = Text("公式总结",
                         font="PingFang SC",
                         font_size=34, color=GOLD).move_to(UP * 6.2)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # ── 长方形卡片 ─────────────────────────────
        card_rect_bg = RoundedRectangle(
            width=6.5, height=3.0,
            corner_radius=0.25,
            fill_color="#112233",
            fill_opacity=0.95,
            stroke_color=self.COL_RECT,
            stroke_width=2.5,
        ).move_to(UP * 4.0)

        rect_icon = Rectangle(
            width=1.4, height=0.85,
            fill_color=self.COL_RECT,
            fill_opacity=0.6,
            stroke_color=self.COL_RECT,
            stroke_width=2,
        ).move_to(card_rect_bg.get_center() + UP * 0.75 + LEFT * 2.0)

        card_rect_title = Text("长方形",
                               font="PingFang SC",
                               font_size=26, color=self.COL_RECT
                               ).move_to(card_rect_bg.get_center() + UP * 0.75 + RIGHT * 0.5)
        card_rect_f1 = Text("面积 = 长 × 宽",
                            font="PingFang SC",
                            font_size=22, color=WHITE
                            ).move_to(card_rect_bg.get_center() + DOWN * 0.05)
        card_rect_f2 = MathTex(r"S = a \times b",
                               font_size=32, color=self.COL_RECT
                               ).move_to(card_rect_bg.get_center() + DOWN * 0.8)

        card_rect = VGroup(card_rect_bg, rect_icon, card_rect_title,
                           card_rect_f1, card_rect_f2)

        # ── 正方形卡片 ─────────────────────────────
        card_sq_bg = RoundedRectangle(
            width=6.5, height=3.0,
            corner_radius=0.25,
            fill_color="#112233",
            fill_opacity=0.95,
            stroke_color=self.COL_SQ,
            stroke_width=2.5,
        ).move_to(UP * 0.6)

        sq_icon = Square(
            side_length=0.9,
            fill_color=self.COL_SQ,
            fill_opacity=0.6,
            stroke_color=self.COL_SQ,
            stroke_width=2,
        ).move_to(card_sq_bg.get_center() + UP * 0.75 + LEFT * 2.0)

        card_sq_title = Text("正方形",
                             font="PingFang SC",
                             font_size=26, color=self.COL_SQ
                             ).move_to(card_sq_bg.get_center() + UP * 0.75 + RIGHT * 0.5)
        card_sq_f1 = Text("面积 = 边长 × 边长",
                          font="PingFang SC",
                          font_size=22, color=WHITE
                          ).move_to(card_sq_bg.get_center() + DOWN * 0.05)
        card_sq_f2 = MathTex(r"S = a^2",
                             font_size=32, color=self.COL_SQ
                             ).move_to(card_sq_bg.get_center() + DOWN * 0.8)

        card_sq = VGroup(card_sq_bg, sq_icon, card_sq_title,
                         card_sq_f1, card_sq_f2)

        self.play(FadeIn(card_rect, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(card_rect_f2, color=self.COL_RECT, scale_factor=1.15), run_time=0.6)
        self.play(FadeIn(card_sq, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(card_sq_f2, color=self.COL_SQ, scale_factor=1.15), run_time=0.6)

        # 记忆口诀
        tip = Text(
            "长×宽，边长²\n两个公式记心间！",
            font="PingFang SC",
            font_size=26,
            color=self.COL_HL,
            line_spacing=1.3,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(tip, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(sec_title),
            FadeOut(card_rect), FadeOut(card_sq),
            FadeOut(tip),
            run_time=0.7,
        )

    # ─────────────────────────────────────────────
    # 场景 7 · 片尾关注
    # ─────────────────────────────────────────────
    def scene_outro(self):
        author_big = Text("上海初高中数学直通车",
                          font="PingFang SC",
                          font_size=34, color=WHITE).move_to(UP * 2.0)
        author_id = Text("@emptyandcalm",
                         font="PingFang SC",
                         font_size=26, color="#9ca3af").move_to(UP * 1.1)
        follow = Text("关注我，学更多数学知识！",
                      font="PingFang SC",
                      font_size=28, color=GOLD).move_to(UP * 0.0)

        # 装饰：两个小图形
        deco_rect = Rectangle(
            width=1.2, height=0.75,
            fill_color=self.COL_RECT,
            fill_opacity=0.8,
            stroke_color=self.COL_RECT,
            stroke_width=2,
        ).move_to(DOWN * 1.5 + LEFT * 1.5)
        deco_sq = Square(
            side_length=0.75,
            fill_color=self.COL_SQ,
            fill_opacity=0.8,
            stroke_color=self.COL_SQ,
            stroke_width=2,
        ).move_to(DOWN * 1.5 + RIGHT * 1.5)

        formula_r = MathTex(r"S=a\times b", font_size=22,
                            color=WHITE).next_to(deco_rect, DOWN, buff=0.12)
        formula_s = MathTex(r"S=a^2", font_size=22,
                            color=WHITE).next_to(deco_sq, DOWN, buff=0.12)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(Write(follow), run_time=0.7)
        self.play(
            FadeIn(deco_rect, scale=0.5),
            FadeIn(deco_sq, scale=0.5),
            run_time=0.5,
        )
        self.play(FadeIn(formula_r), FadeIn(formula_s), run_time=0.4)

        self.play(
            Rotate(deco_rect, angle=2 * PI, run_time=1.2, rate_func=smooth),
            Rotate(deco_sq, angle=-2 * PI, run_time=1.2, rate_func=smooth),
        )
        self.wait(1.0)
