"""
克与千克的进率 - 二年级数学教学动画
Gram & Kilogram Conversion Rate

格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染:
  manim -pql conversion_rate.py ConversionRate   # 预览
  manim -qh  conversion_rate.py ConversionRate   # 高质量
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ConversionRate(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.F  = "Noto Sans CJK SC"
        self.CG = "#80DEEA"   # 克色
        self.CK = "#29B6F6"   # 千克色
        self.CY = GOLD
        self.CH = "#FFD700"

        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.F, font_size=20, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.s1_hook()
        self.s2_definition()
        self.s3_decompose()
        self.s4_conversion()
        self.s5_compound()
        self.s6_summary()
        self.s7_outro()

    # ── helpers ──────────────────────────────────

    def _unit_box(self, label, value, bg, stroke, pos):
        """单位展示方块：上面大数字，下面单位名称"""
        box = RoundedRectangle(
            corner_radius=0.3, width=2.6, height=1.7,
            fill_color=bg, fill_opacity=0.8,
            stroke_color=stroke, stroke_width=3
        ).move_to(pos)
        val_t = Text(value, font=self.F, font_size=52,
                     color=WHITE, weight=BOLD).move_to(pos + UP * 0.22)
        lbl_t = Text(label, font=self.F, font_size=26,
                     color=stroke).move_to(pos + DOWN * 0.45)
        return VGroup(box, val_t, lbl_t)

    def _step_row(self, parts, colors, sizes, y):
        """横排文字行，parts/colors/sizes 一一对应"""
        mobs = VGroup(*[
            Text(p, font=self.F, font_size=s, color=c)
            for p, c, s in zip(parts, colors, sizes)
        ]).arrange(RIGHT, buff=0.22)
        mobs.move_to(UP * y)
        return mobs

    def _card(self, main, sub, bg, stroke, y):
        box = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.7,
            fill_color=bg, fill_opacity=0.65,
            stroke_color=stroke, stroke_width=2.5
        ).move_to(UP * y)
        m = Text(main, font=self.F, font_size=30,
                 color=WHITE, weight=BOLD).move_to(UP * y + UP * 0.33)
        s = Text(sub,  font=self.F, font_size=22,
                 color=GRAY_A).move_to(UP * y + DOWN * 0.33)
        return VGroup(box, m, s)

    # ── Scene 1 ──────────────────────────────────

    def s1_hook(self):
        h1 = Text("1千克", font=self.F, font_size=96,
                  color=self.CY, weight=BOLD).move_to(UP * 4.8)
        h2 = Text("等于多少克？", font=self.F, font_size=52,
                  color=WHITE).move_to(UP * 3.7)

        # 两个砝码图（圆形）
        w_kg = Circle(radius=0.8, fill_color="#1565C0", fill_opacity=0.9,
                      stroke_color=self.CK, stroke_width=4).move_to(LEFT * 2 + UP * 1.5)
        w_kg_t = Text("1kg", font=self.F, font_size=34,
                      color=WHITE, weight=BOLD).move_to(w_kg.get_center())
        q = Text("?克", font=self.F, font_size=52,
                 color=YELLOW).move_to(RIGHT * 2 + UP * 1.5)

        self.play(Write(h1), run_time=0.7)
        self.play(FadeIn(h2, shift=UP * 0.3), run_time=0.5)
        self.play(GrowFromCenter(VGroup(w_kg, w_kg_t)), FadeIn(q), run_time=0.6)
        self.wait(0.9)
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(w_kg),
                  FadeOut(w_kg_t), FadeOut(q), run_time=0.4)

    # ── Scene 2 ──────────────────────────────────

    def s2_definition(self):
        title = Text("克与千克的进率", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.7)

        # 千克 box ←→ 克 box
        box_kg = self._unit_box("千克", "1", "#0D47A1", self.CK, LEFT * 2.2 + UP * 3.5)
        box_g  = self._unit_box("克",   "1000", "#00695C", self.CG, RIGHT * 2.2 + UP * 3.5)

        self.play(GrowFromCenter(box_kg), GrowFromCenter(box_g), run_time=0.7)

        # 双向箭头
        arr_r = Arrow(LEFT * 0.7 + UP * 3.5, RIGHT * 0.7 + UP * 3.5,
                      color=YELLOW, stroke_width=5,
                      max_tip_length_to_length_ratio=0.2)
        self.play(Create(arr_r), run_time=0.4)

        # 公式
        formula = VGroup(
            Text("1", font=self.F, font_size=46, color=self.CK, weight=BOLD),
            Text("千克", font=self.F, font_size=42, color=WHITE),
            Text("=", font=self.F, font_size=46, color=WHITE),
            Text("1000", font=self.F, font_size=46, color=self.CG, weight=BOLD),
            Text("克", font=self.F, font_size=42, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.6)
        self.play(Write(formula), run_time=0.9)

        rate_lbl = Text("进率是 1000", font=self.F, font_size=32,
                        color=self.CH).move_to(UP * 0.4)
        self.play(FadeIn(rate_lbl, scale=1.1), run_time=0.5)

        # 副说明
        info_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=1.8,
            fill_color="#1A237E", fill_opacity=0.5,
            stroke_color=BLUE_C, stroke_width=2
        ).move_to(DOWN * 1.0)
        i1 = Text("千克和克之间相差1000倍", font=self.F, font_size=27, color=WHITE)
        i2 = Text("1kg = 1000g", font=self.F, font_size=28,
                  color=self.CG, weight=BOLD)
        VGroup(i1, i2).arrange(DOWN, buff=0.25).move_to(info_bg.get_center())

        self.play(FadeIn(info_bg), Write(i1), run_time=0.6)
        self.play(FadeIn(i2), run_time=0.4)
        self.wait(1.8)

        self.play(FadeOut(title), FadeOut(box_kg), FadeOut(box_g),
                  FadeOut(arr_r), FadeOut(formula), FadeOut(rate_lbl),
                  FadeOut(info_bg), FadeOut(i1), FadeOut(i2), run_time=0.4)

    # ── Scene 3 ──────────────────────────────────

    def s3_decompose(self):
        title = Text("为什么进率是1000？", font=self.F, font_size=40,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 1千克 大圆
        kg_circle = Circle(
            radius=1.1, fill_color="#0D47A1", fill_opacity=0.85,
            stroke_color=self.CK, stroke_width=5
        ).move_to(UP * 4.5)
        kg_txt = Text("1千克", font=self.F, font_size=38,
                      color=WHITE, weight=BOLD).move_to(kg_circle.get_center())
        self.play(GrowFromCenter(VGroup(kg_circle, kg_txt)), run_time=0.6)

        # 依次展示分解
        rows_data = [
            (["= 10个", "100克"], [WHITE, self.CG], [32, 36], 3.0),
            (["= 100个", "10克"],  [WHITE, self.CG], [32, 36], 2.0),
            (["= 1000个", "1克"],  [WHITE, self.CG], [32, 36], 1.0),
        ]
        rows = []
        for parts, colors, sizes, y in rows_data:
            r = self._step_row(parts, colors, sizes, y)
            rows.append(r)
            self.play(FadeIn(r, shift=LEFT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 高亮最后一行（结论）
        highlight_box = SurroundingRectangle(rows[-1], color=YELLOW,
                                             buff=0.2, corner_radius=0.15)
        self.play(Create(highlight_box), run_time=0.4)

        conclude = Text("所以 1千克 = 1000克 ✓", font=self.F,
                        font_size=30, color=YELLOW).move_to(DOWN * 0.3)
        self.play(Write(conclude), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(kg_circle), FadeOut(kg_txt),
            *[FadeOut(r) for r in rows],
            FadeOut(highlight_box), FadeOut(conclude), run_time=0.4
        )

    # ── Scene 4 ──────────────────────────────────

    def s4_conversion(self):
        title = Text("单位换算练习", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # ── 千克 → 克 ──────────────────────────
        conv_bg1 = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.2,
            fill_color="#1B3A4B", fill_opacity=0.7,
            stroke_color=self.CK, stroke_width=2
        ).move_to(UP * 4.5)

        q1 = VGroup(
            Text("3", font=self.F, font_size=46, color=self.CK, weight=BOLD),
            Text("千克 = ?克", font=self.F, font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.8)

        a1 = VGroup(
            Text("3×1000 =", font=self.F, font_size=34, color=GRAY_A),
            Text("3000", font=self.F, font_size=46, color=self.CG, weight=BOLD),
            Text("克", font=self.F, font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.15)

        arr_down1 = Arrow(UP * 5.7, UP * 5.1,
                          color=YELLOW, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)
        tip1 = Text("千克→克：×1000", font=self.F, font_size=22,
                    color=YELLOW).next_to(arr_down1, RIGHT, buff=0.2)

        self.play(FadeIn(conv_bg1), Write(q1), run_time=0.6)
        self.play(Create(arr_down1), FadeIn(tip1), run_time=0.4)
        self.play(FadeIn(a1, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.8)

        # ── 克 → 千克 ──────────────────────────
        conv_bg2 = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.2,
            fill_color="#1B3A2B", fill_opacity=0.7,
            stroke_color=self.CG, stroke_width=2
        ).move_to(UP * 1.5)

        q2 = VGroup(
            Text("5000", font=self.F, font_size=46, color=self.CG, weight=BOLD),
            Text("克 = ?千克", font=self.F, font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 1.8)

        a2 = VGroup(
            Text("5000÷1000 =", font=self.F, font_size=34, color=GRAY_A),
            Text("5", font=self.F, font_size=46, color=self.CK, weight=BOLD),
            Text("千克", font=self.F, font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.15)

        tip2 = Text("克→千克：÷1000", font=self.F, font_size=22,
                    color="#80DEEA").move_to(UP * 0.3)

        self.play(FadeIn(conv_bg2), Write(q2), run_time=0.6)
        self.play(FadeIn(tip2), run_time=0.4)
        self.play(FadeIn(a2, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(conv_bg1), FadeOut(q1),
            FadeOut(a1), FadeOut(arr_down1), FadeOut(tip1),
            FadeOut(conv_bg2), FadeOut(q2), FadeOut(a2), FadeOut(tip2),
            run_time=0.4
        )

    # ── Scene 5 ──────────────────────────────────

    def s5_compound(self):
        title = Text("综合换算", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        question = VGroup(
            Text("2千克500克 = ?克", font=self.F, font_size=38, color=WHITE),
        ).move_to(UP * 5.0)
        self.play(Write(question), run_time=0.6)

        # 步骤框
        bg = RoundedRectangle(
            corner_radius=0.3, width=7.5, height=4.5,
            fill_color="#212121", fill_opacity=0.6,
            stroke_color=GRAY_B, stroke_width=2
        ).move_to(UP * 2.5)
        self.play(FadeIn(bg), run_time=0.3)

        steps = [
            (["第一步：", "2千克", " = 2×1000 = ", "2000克"],
             [GRAY_A, self.CK, GRAY_A, self.CG], [28, 32, 28, 32], 4.2),
            (["第二步：", "500克", " 保持不变"],
             [GRAY_A, self.CG, GRAY_A], [28, 32, 28], 3.2),
            (["第三步：", "2000", "+", "500", "="],
             [GRAY_A, self.CG, WHITE, self.CG, WHITE], [28, 32, 32, 32, 32], 2.2),
        ]

        for parts, colors, sizes, y in steps:
            row = self._step_row(parts, colors, sizes, y)
            self.play(Write(row), run_time=0.6)
            self.wait(0.4)

        # 结果大框
        res_box = RoundedRectangle(
            corner_radius=0.35, width=4.5, height=1.5,
            fill_color="#1B5E20", fill_opacity=0.9,
            stroke_color="#A5D6A7", stroke_width=3
        ).move_to(UP * 0.4)
        res_row = VGroup(
            Text("= ", font=self.F, font_size=44, color=WHITE),
            Text("2500", font=self.F, font_size=56,
                 color=self.CG, weight=BOLD),
            Text("克", font=self.F, font_size=44, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(res_box.get_center())

        self.play(GrowFromCenter(res_box), run_time=0.5)
        self.play(Write(res_row), run_time=0.5)
        self.play(Flash(res_box, color=self.CG, flash_radius=2.5), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(title), FadeOut(question), FadeOut(bg),
                  FadeOut(res_box), FadeOut(res_row), run_time=0.4)
        # (steps faded with bg)

    # ── Scene 6 ──────────────────────────────────

    def s6_summary(self):
        title = Text("知识总结", font=self.F, font_size=54,
                     color=self.CY, weight=BOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        cards_data = [
            ("1千克 = 1000克",  "进率是 1000",         "#1565C0", "#42A5F5", 4.5),
            ("千克→克：×1000",  "单位变小，数变大",     "#00695C", "#4DB6AC", 2.5),
            ("克→千克：÷1000",  "单位变大，数变小",     "#4A148C", "#AB47BC", 0.5),
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

        cheer = Text("掌握进率，换算无忧！", font=self.F,
                     font_size=32, color=YELLOW).move_to(DOWN * 1.5)
        self.play(FadeIn(cheer, scale=1.1), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(title), FadeOut(cheer),
                  *[FadeOut(c) for c in cards], run_time=0.4)

    # ── Scene 7 Outro ────────────────────────────

    def s7_outro(self):
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