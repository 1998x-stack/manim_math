"""
认识千 - 二年级数学教学动画
Understanding 1000

格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染:
  manim -pql thousand.py UnderstandThousand
  manim -qh  thousand.py UnderstandThousand
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# 方块尺寸（单位：逻辑坐标）
CELL = 0.58


class UnderstandThousand(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.F   = "PingFang SC"
        self.C1  = "#42A5F5"   # 单个方块色
        self.C10 = "#26C6DA"   # 十方块色
        self.C100 = "#66BB6A"  # 百方块色
        self.C1000 = "#FFA726" # 千方块色
        self.CY  = GOLD

        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.F, font_size=20, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.s1_hook()
        self.s2_one_block()
        self.s3_ten_blocks()
        self.s4_hundred_blocks()
        self.s5_thousand_blocks()
        self.s6_place_value()
        self.s7_summary()
        self.s8_outro()

    # ── helpers ──────────────────────────────────

    def _block(self, pos=ORIGIN, color=None, size=CELL):
        if color is None:
            color = self.C1
        sq = Square(
            side_length=size,
            fill_color=color, fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=1.2
        ).move_to(pos)
        return sq

    def _row_of_n(self, n, color, y_center, x_start=None):
        """创建 n 个方块的横排，返回 VGroup"""
        total_w = n * CELL
        if x_start is None:
            x_start = -total_w / 2 + CELL / 2
        blocks = VGroup(*[
            self._block(
                pos=np.array([x_start + i * CELL, y_center, 0]),
                color=color
            )
            for i in range(n)
        ])
        return blocks

    def _grid_nxm(self, n_cols, n_rows, color, center=ORIGIN):
        """n_cols × n_rows 方块网格，返回 VGroup"""
        total_w = n_cols * CELL
        total_h = n_rows * CELL
        cx, cy = center[0], center[1]
        x0 = cx - total_w / 2 + CELL / 2
        y0 = cy + total_h / 2 - CELL / 2
        blocks = VGroup(*[
            self._block(
                pos=np.array([x0 + j * CELL, y0 - i * CELL, 0]),
                color=color
            )
            for i in range(n_rows)
            for j in range(n_cols)
        ])
        return blocks

    def _place_cell(self, digit_str, name_str, bg, stroke, w=1.6, h=2.0):
        box = Rectangle(
            width=w, height=h,
            fill_color=bg, fill_opacity=0.8,
            stroke_color=stroke, stroke_width=2.5
        )
        dig = Text(digit_str, font=self.F, font_size=44,
                   color=WHITE, weight=BOLD).move_to(box.get_center() + UP * 0.32)
        nam = Text(name_str, font=self.F, font_size=22,
                   color=stroke).move_to(box.get_center() + DOWN * 0.45)
        return VGroup(box, dig, nam)

    def _card(self, main, sub, bg, stroke, y):
        box = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.7,
            fill_color=bg, fill_opacity=0.65,
            stroke_color=stroke, stroke_width=2.5
        ).move_to(UP * y)
        m = Text(main, font=self.F, font_size=30,
                 color=WHITE, weight=BOLD).move_to(UP * y + UP * 0.33)
        s = Text(sub, font=self.F, font_size=22,
                 color=GRAY_A).move_to(UP * y + DOWN * 0.33)
        return VGroup(box, m, s)

    # ── Scene 1 ──────────────────────────────────

    def s1_hook(self):
        h1 = Text("1000", font=self.F, font_size=100,
                  color=self.CY, weight=BOLD).move_to(UP * 4.8)
        h2 = Text("有多大？", font=self.F, font_size=52,
                  color=WHITE).move_to(UP * 3.7)

        # 几个小方块飞散
        dots = VGroup(*[
            self._block(
                pos=np.array([(i % 5 - 2) * 0.7, 1.5 - (i // 5) * 0.7, 0]),
                color=self.C1
            )
            for i in range(15)
        ])

        self.play(Write(h1), run_time=0.7)
        self.play(FadeIn(h2, shift=UP * 0.3), run_time=0.5)
        self.play(LaggedStart(*[GrowFromCenter(b) for b in dots],
                              lag_ratio=0.05), run_time=0.9)
        q = Text("还有更多……", font=self.F, font_size=32,
                 color=GRAY_A).move_to(UP * 0.2)
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(dots), FadeOut(q), run_time=0.4)

    # ── Scene 2 ──────────────────────────────────

    def s2_one_block(self):
        title = Text("从1开始", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        blk = self._block(pos=UP * 4.0, color=self.C1, size=CELL * 1.4)
        lbl = Text("1个一", font=self.F, font_size=36,
                   color=self.C1).move_to(UP * 3.1)

        self.play(GrowFromCenter(blk), run_time=0.5)
        self.play(FadeIn(lbl), run_time=0.4)

        eq = VGroup(
            Text("10个一", font=self.F, font_size=32, color=self.C1),
            Text("=", font=self.F, font_size=32, color=WHITE),
            Text("1个十", font=self.F, font_size=32, color=self.C10),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.1)

        self.play(FadeIn(eq, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(blk), FadeOut(lbl), FadeOut(eq), run_time=0.4)

    # ── Scene 3 ──────────────────────────────────

    def s3_ten_blocks(self):
        title = Text("10个一 = 1个十", font=self.F, font_size=40,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 10 块横排逐个弹出
        row = self._row_of_n(10, self.C10, y_center=4.2)
        for i, b in enumerate(row):
            self.play(GrowFromCenter(b), run_time=0.12)

        # 计数标签
        count_lbl = Text("10个", font=self.F, font_size=28,
                         color=GRAY_A).next_to(row, DOWN, buff=0.2)
        brace = Brace(row, direction=DOWN, color=GRAY_B)
        self.play(Create(brace), FadeIn(count_lbl), run_time=0.5)

        # 收缩为一个"十"方块
        ten_block = self._block(pos=ORIGIN + UP * 4.2, color=self.C10, size=CELL * 1.4)
        ten_lbl = Text("1个十", font=self.F, font_size=36,
                       color=self.C10).move_to(UP * 3.2)

        self.play(
            Transform(row, ten_block),
            FadeOut(brace), FadeOut(count_lbl),
            run_time=0.7
        )
        self.play(FadeIn(ten_lbl), run_time=0.4)

        eq = VGroup(
            Text("10个十", font=self.F, font_size=32, color=self.C10),
            Text("=", font=self.F, font_size=32, color=WHITE),
            Text("1个百", font=self.F, font_size=32, color=self.C100),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.1)
        self.play(FadeIn(eq, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(title), FadeOut(row), FadeOut(ten_lbl),
                  FadeOut(ten_block), FadeOut(eq), run_time=0.4)

    # ── Scene 4 ──────────────────────────────────

    def s4_hundred_blocks(self):
        title = Text("10个十 = 1个百", font=self.F, font_size=40,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 10×10 网格（代表100）——分10行逐行出现
        grid = self._grid_nxm(10, 10, self.C100,
                              center=np.array([0.0, 2.8, 0]))

        n_per_row = 10
        for row_i in range(10):
            row_blocks = VGroup(*grid[row_i * n_per_row:(row_i + 1) * n_per_row])
            self.play(
                LaggedStart(*[GrowFromCenter(b) for b in row_blocks], lag_ratio=0.04),
                run_time=0.3
            )

        count_lbl = Text("100个小方块 = 1个百", font=self.F,
                         font_size=28, color=self.C100).move_to(DOWN * 0.7)
        self.play(FadeIn(count_lbl), run_time=0.5)

        # 缩成一个"百"方块
        hundred_block = self._block(pos=UP * 2.8, color=self.C100, size=CELL * 1.6)
        hundred_lbl = Text("1个百", font=self.F, font_size=36,
                           color=self.C100).move_to(UP * 1.7)
        self.play(
            Transform(grid, hundred_block),
            FadeOut(count_lbl),
            run_time=0.7
        )
        self.play(FadeIn(hundred_lbl), run_time=0.4)

        eq = VGroup(
            Text("10个百", font=self.F, font_size=32, color=self.C100),
            Text("=", font=self.F, font_size=32, color=WHITE),
            Text("1个千", font=self.F, font_size=32, color=self.C1000),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.6)
        self.play(FadeIn(eq, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(hundred_block),
                  FadeOut(hundred_lbl), FadeOut(eq), run_time=0.4)

    # ── Scene 5 ──────────────────────────────────

    def s5_thousand_blocks(self):
        title = Text("10个百 = 1个千！", font=self.F, font_size=40,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 用 10 个"百"方块叠成一列，代表 1000
        hundred_blocks = VGroup(*[
            self._block(
                pos=np.array([-1.8, 4.5 - i * (CELL * 1.6 + 0.08), 0]),
                color=self.C100, size=CELL * 1.6
            )
            for i in range(10)
        ])

        for b in hundred_blocks:
            self.play(GrowFromCenter(b), run_time=0.18)

        count_lbl = Text("10个百", font=self.F, font_size=30,
                         color=self.C100).move_to(np.array([-1.8, -2.0, 0]))
        self.play(FadeIn(count_lbl), run_time=0.4)

        # 大箭头 → 收缩成 "1千" 大方块
        arr = Arrow(LEFT * 0.2 + UP * 2.2, RIGHT * 0.6 + UP * 2.2,
                    color=YELLOW, stroke_width=5,
                    max_tip_length_to_length_ratio=0.25)
        self.play(Create(arr), run_time=0.4)

        thousand_block = self._block(pos=np.array([2.2, 2.2, 0]),
                                     color=self.C1000, size=CELL * 3.0)
        thousand_inner = Text("1000", font=self.F, font_size=30,
                              color=WHITE, weight=BOLD
                              ).move_to(thousand_block.get_center())
        self.play(GrowFromCenter(thousand_block),
                  FadeIn(thousand_inner), run_time=0.6)
        self.play(Flash(thousand_block, color=self.C1000, flash_radius=2.0), run_time=0.5)

        thousand_lbl = Text("1个千", font=self.F, font_size=36,
                            color=self.C1000, weight=BOLD
                            ).move_to(np.array([2.2, 0.3, 0]))
        self.play(FadeIn(thousand_lbl), run_time=0.4)

        # 关键公式
        formula_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.1,
            fill_color="#1B3A1B", fill_opacity=0.7,
            stroke_color=self.C1000, stroke_width=2.5
        ).move_to(DOWN * 1.2)
        formula_row = VGroup(
            Text("10", font=self.F, font_size=38, color=self.C100, weight=BOLD),
            Text("个百 =", font=self.F, font_size=34, color=WHITE),
            Text("1000", font=self.F, font_size=38, color=self.C1000, weight=BOLD),
            Text("= 1个千", font=self.F, font_size=34, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(formula_bg.get_center())
        self.play(FadeIn(formula_bg), Write(formula_row), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(hundred_blocks), FadeOut(count_lbl),
            FadeOut(arr), FadeOut(thousand_block), FadeOut(thousand_inner),
            FadeOut(thousand_lbl), FadeOut(formula_bg), FadeOut(formula_row),
            run_time=0.4
        )

    # ── Scene 6 ──────────────────────────────────

    def s6_place_value(self):
        title = Text("认识千位", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 位值表：千 百 十 个
        cells_data = [
            ("1", "千位", "#E65100", "#FF8A65"),
            ("0", "百位", "#1565C0", "#42A5F5"),
            ("0", "十位", "#1B5E20", "#66BB6A"),
            ("0", "个位", "#4A148C", "#CE93D8"),
        ]

        cells = VGroup(*[
            self._place_cell(d, n, bg, st)
            for d, n, bg, st in cells_data
        ]).arrange(RIGHT, buff=0.1).move_to(UP * 4.2)

        self.play(GrowFromCenter(cells), run_time=0.8)

        # 标注"千位"
        brace_k = Brace(cells[0], direction=UP, color=GOLD)
        brace_lbl = Text("新位！千位", font=self.F, font_size=26,
                         color=GOLD).next_to(brace_k, UP, buff=0.1)
        self.play(Create(brace_k), FadeIn(brace_lbl), run_time=0.5)

        # 顺序说明
        order_txt = Text("从右起：个、十、百、千", font=self.F,
                         font_size=28, color=WHITE).move_to(UP * 2.3)
        arr_right = Arrow(RIGHT * 1.8 + UP * 2.3, LEFT * 1.8 + UP * 2.3,
                          color=GRAY_B, stroke_width=3,
                          max_tip_length_to_length_ratio=0.15)
        self.play(Write(order_txt), Create(arr_right), run_time=0.6)

        # 示例：1000
        ex_lbl = Text("例：1000 读作 一千", font=self.F,
                      font_size=30, color=self.CY).move_to(UP * 1.3)
        self.play(FadeIn(ex_lbl, shift=UP * 0.3), run_time=0.5)

        # 更新数字：2000
        cells2_data = [
            ("2", "千位", "#E65100", "#FF8A65"),
            ("0", "百位", "#1565C0", "#42A5F5"),
            ("0", "十位", "#1B5E20", "#66BB6A"),
            ("0", "个位", "#4A148C", "#CE93D8"),
        ]
        cells2 = VGroup(*[
            self._place_cell(d, n, bg, st)
            for d, n, bg, st in cells2_data
        ]).arrange(RIGHT, buff=0.1).move_to(UP * 4.2)

        ex2 = Text("2000 → 千位是2，表示2个千", font=self.F,
                   font_size=26, color=GRAY_A).move_to(UP * 0.3)
        self.play(Transform(cells, cells2), FadeOut(ex_lbl), run_time=0.5)
        self.play(FadeIn(ex2), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(cells), FadeOut(brace_k),
            FadeOut(brace_lbl), FadeOut(order_txt), FadeOut(arr_right),
            FadeOut(ex2), run_time=0.4
        )

    # ── Scene 7 Summary ──────────────────────────

    def s7_summary(self):
        title = Text("知识总结", font=self.F, font_size=54,
                     color=self.CY, weight=BOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        cards_data = [
            ("10个百 = 1个千",    "1000 = 10 × 100",        "#B71C1C", "#EF5350", 4.5),
            ("千位是最高位",       "个、十、百、千 从右数",    "#1565C0", "#42A5F5", 2.5),
            ("1000个一 = 1个千",  "想象1000块小积木！",       "#00695C", "#4DB6AC", 0.5),
        ]
        cards = []
        for main, sub, bg, stroke, y in cards_data:
            c = self._card(main, sub, bg, stroke, y)
            c.shift(LEFT * 11)
            cards.append(c)
            self.add(c)

        for c in cards:
            self.play(c.animate.shift(RIGHT * 11), run_time=0.45)
            self.wait(0.18)

        cheer = Text("掌握千，数字无极限！", font=self.F,
                     font_size=32, color=YELLOW).move_to(DOWN * 1.5)
        self.play(FadeIn(cheer, scale=1.1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(title), FadeOut(cheer),
                  *[FadeOut(c) for c in cards], run_time=0.4)

    # ── Scene 8 Outro ────────────────────────────

    def s8_outro(self):
        stars = VGroup(*[
            Star(n=5, outer_radius=0.3, inner_radius=0.13,
                 fill_color=GOLD, fill_opacity=0.9, stroke_width=0
                 ).move_to(3.0 * np.array([np.cos(i*TAU/8), np.sin(i*TAU/8), 0]))
            for i in range(8)
        ])
        self.play(LaggedStart(*[GrowFromCenter(s) for s in stars],
                              lag_ratio=0.08), run_time=0.9)

        author_big = Text("上海初高中数学直通车", font=self.F,
                          font_size=40, color=WHITE, weight=BOLD).move_to(UP * 2.0)
        author_id  = Text("@emptyandcalm", font=self.F,
                          font_size=30, color=GRAY_B).move_to(UP * 1.1)
        self.play(Transform(self.author_bar, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text("关注我，获得更多数学技巧！", font=self.F,
                      font_size=30, color=GOLD).move_to(DOWN * 0.2)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.play(Rotate(stars, angle=TAU), run_time=2.0)
        self.wait(0.4)
        self.play(FadeOut(self.author_bar), FadeOut(author_id),
                  FadeOut(follow), FadeOut(stars), run_time=0.8)