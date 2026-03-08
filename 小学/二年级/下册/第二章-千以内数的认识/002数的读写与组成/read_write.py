"""
数的读写与组成 - 二年级数学教学动画
Reading, Writing and Composition of Numbers

格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染:
  manim -pql read_write.py ReadWriteNumbers
  manim -qh  read_write.py ReadWriteNumbers
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ReadWriteNumbers(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.F    = "Noto Sans CJK SC"
        self.CB   = "#42A5F5"   # 百位色
        self.CT   = "#66BB6A"   # 十位色
        self.CO   = "#CE93D8"   # 个位色
        self.CY   = GOLD
        self.CZERO = "#EF5350"  # 零的强调色

        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.F, font_size=20, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.s1_hook()
        self.s2_place_table()
        self.s3_read_rules()
        self.s4_analyze_304()
        self.s5_analyze_580()
        self.s6_analyze_256()
        self.s7_summary()
        self.s8_outro()

    # ── helpers ──────────────────────────────────

    def _place_table(self, digits, highlight_zero=True):
        """
        创建三格位值表，digits = [百,十,个]（字符串）
        返回 VGroup（table）
        """
        cols_cfg = [
            ("百位", self.CB, digits[0]),
            ("十位", self.CT, digits[1]),
            ("个位", self.CO, digits[2]),
        ]
        cells = []
        for name, color, dig in cols_cfg:
            box = Rectangle(
                width=2.1, height=2.2,
                fill_color="#1A1A2E", fill_opacity=0.9,
                stroke_color=color, stroke_width=3
            )
            dig_color = self.CZERO if (dig == "0" and highlight_zero) else WHITE
            dig_t = Text(dig, font=self.F, font_size=64,
                         color=dig_color, weight=BOLD
                         ).move_to(box.get_center() + UP * 0.28)
            name_t = Text(name, font=self.F, font_size=24,
                          color=color).move_to(box.get_center() + DOWN * 0.52)
            cells.append(VGroup(box, dig_t, name_t))

        tbl = VGroup(*cells).arrange(RIGHT, buff=0)
        return tbl

    def _decomp_row(self, hundreds, tens, ones, y):
        """
        x个百 + y个十 + z个一 横排
        """
        parts = [
            (f"{hundreds}个百", self.CB),
            ("+", WHITE),
            (f"{tens}个十", self.CT),
            ("+", WHITE),
            (f"{ones}个一", self.CO),
        ]
        row = VGroup(*[
            Text(p, font=self.F, font_size=32, color=c)
            for p, c in parts
        ]).arrange(RIGHT, buff=0.2)
        row.move_to(UP * y)
        return row

    def _num_big(self, num_str, color, y):
        bg = RoundedRectangle(
            corner_radius=0.3, width=3.2, height=1.2,
            fill_color="#0D1B2A", fill_opacity=0.9,
            stroke_color=color, stroke_width=3
        ).move_to(UP * y)
        t = Text(num_str, font=self.F, font_size=64,
                 color=color, weight=BOLD).move_to(bg.get_center())
        return VGroup(bg, t)

    def _read_box(self, reading, y):
        """读作：XXXX 绿色框"""
        bg = RoundedRectangle(
            corner_radius=0.3, width=5.0, height=1.0,
            fill_color="#1B5E20", fill_opacity=0.8,
            stroke_color="#A5D6A7", stroke_width=2.5
        ).move_to(UP * y)
        row = VGroup(
            Text("读作：", font=self.F, font_size=28, color=GRAY_A),
            Text(reading, font=self.F, font_size=32,
                 color="#A5D6A7", weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(bg.get_center())
        return VGroup(bg, row)

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
        h1 = Text("304", font=self.F, font_size=100,
                  color=self.CY, weight=BOLD).move_to(UP * 4.8)
        h2 = Text("读作什么？", font=self.F, font_size=52,
                  color=WHITE).move_to(UP * 3.7)

        zero_flash = Text("0", font=self.F, font_size=80,
                          color=self.CZERO, weight=BOLD).move_to(UP * 2.0)
        tip = Text("中间的零，读还是不读？", font=self.F,
                   font_size=30, color=GRAY_A).move_to(UP * 1.0)

        self.play(Write(h1), run_time=0.7)
        self.play(FadeIn(h2, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(zero_flash, scale=1.2), run_time=0.5)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.0)
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(zero_flash),
                  FadeOut(tip), run_time=0.4)

    # ── Scene 2 ──────────────────────────────────

    def s2_place_table(self):
        title = Text("数的读写与组成", font=self.F, font_size=44,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 位值表 304
        tbl = self._place_table(["3", "0", "4"])
        tbl.move_to(UP * 4.5)
        self.play(GrowFromCenter(tbl), run_time=0.7)

        # 标注零
        zero_cell = tbl[1]  # 十位
        brace_z = Brace(zero_cell, direction=DOWN, color=self.CZERO)
        zero_tip = Text("0在十位，有特殊规则！", font=self.F,
                        font_size=26, color=self.CZERO
                        ).next_to(brace_z, DOWN, buff=0.15)
        self.play(Create(brace_z), FadeIn(zero_tip), run_time=0.5)

        # 读法展示
        read_row = self._read_box("三百零四", y=2.0)
        self.play(GrowFromCenter(read_row), run_time=0.5)
        self.play(Flash(read_row, color="#A5D6A7", flash_radius=2.5), run_time=0.4)

        # 另一个数：580
        tbl2 = self._place_table(["5", "8", "0"])
        tbl2.move_to(UP * 0.2)
        read2 = self._read_box("五百八十", y=-1.3)

        self.play(FadeIn(tbl2), run_time=0.5)
        self.play(GrowFromCenter(read2), run_time=0.5)

        tip2 = Text("末尾的0不读！", font=self.F,
                    font_size=26, color=GRAY_A).move_to(DOWN * 2.3)
        self.play(FadeIn(tip2), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(tbl), FadeOut(brace_z),
            FadeOut(zero_tip), FadeOut(read_row),
            FadeOut(tbl2), FadeOut(read2), FadeOut(tip2),
            run_time=0.4
        )

    # ── Scene 3 ──────────────────────────────────

    def s3_read_rules(self):
        title = Text("读数规则", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        rule_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=4.0,
            fill_color="#212121", fill_opacity=0.65,
            stroke_color=GRAY_B, stroke_width=2
        ).move_to(UP * 3.8)
        self.play(FadeIn(rule_bg), run_time=0.3)

        rules = [
            ("① 从最高位（百位）读起",        WHITE,       30, 5.5),
            ("② 中间有0 → 读一个 零",          self.CZERO,  30, 4.6),
            ("   例：304 → 三百零四",           GRAY_A,      26, 3.85),
            ("③ 末尾有0 → 不读",               self.CT,     30, 2.9),
            ("   例：580 → 五百八十",           GRAY_A,      26, 2.15),
        ]
        for text, color, size, y in rules:
            t = Text(text, font=self.F, font_size=size, color=color)
            t.move_to(UP * y)
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.2)

        # 对比例题
        ex_bg = RoundedRectangle(
            corner_radius=0.25, width=7.0, height=1.1,
            fill_color="#1B3A1B", fill_opacity=0.7,
            stroke_color=self.CT, stroke_width=2
        ).move_to(UP * 1.0)
        ex_row = VGroup(
            Text("300", font=self.F, font_size=36, color=WHITE, weight=BOLD),
            Text("→", font=self.F, font_size=32, color=GRAY_B),
            Text("三百", font=self.F, font_size=36, color=self.CT, weight=BOLD),
            Text("（末尾两个0都不读）", font=self.F, font_size=24, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(ex_bg.get_center())
        self.play(FadeIn(ex_bg), Write(ex_row), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(title), FadeOut(rule_bg), FadeOut(ex_bg),
                  FadeOut(ex_row), run_time=0.4)
        # rules text faded with rule_bg container implicitly

    # ── Scene 4 — 304 分解 ───────────────────────

    def s4_analyze_304(self):
        title = Text("304 的组成", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 大数字
        num = self._num_big("304", self.CY, y=5.0)
        self.play(GrowFromCenter(num), run_time=0.5)

        # 位值表
        tbl = self._place_table(["3", "0", "4"])
        tbl.move_to(UP * 3.5)
        self.play(FadeIn(tbl, shift=UP * 0.3), run_time=0.5)

        # 分解行
        decomp = self._decomp_row("3", "0", "4", y=1.9)
        self.play(Write(decomp), run_time=0.7)

        # 展开式
        expand = VGroup(
            Text("= 300", font=self.F, font_size=32, color=self.CB, weight=BOLD),
            Text("+", font=self.F, font_size=32, color=WHITE),
            Text("0", font=self.F, font_size=32, color=self.CZERO, weight=BOLD),
            Text("+", font=self.F, font_size=32, color=WHITE),
            Text("4", font=self.F, font_size=32, color=self.CO, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.9)
        self.play(FadeIn(expand, shift=UP * 0.2), run_time=0.5)

        # 结果读法框
        read = self._read_box("三百零四", y=-0.5)
        self.play(GrowFromCenter(read), run_time=0.5)

        # 强调零
        zero_tip = Text("中间有0，一定要读出来！", font=self.F,
                        font_size=26, color=self.CZERO).move_to(DOWN * 1.7)
        self.play(FadeIn(zero_tip, scale=1.1), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(title), FadeOut(num), FadeOut(tbl),
                  FadeOut(decomp), FadeOut(expand),
                  FadeOut(read), FadeOut(zero_tip), run_time=0.4)

    # ── Scene 5 — 580 分解 ───────────────────────

    def s5_analyze_580(self):
        title = Text("580 的组成", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        num = self._num_big("580", "#29B6F6", y=5.0)
        self.play(GrowFromCenter(num), run_time=0.5)

        tbl = self._place_table(["5", "8", "0"], highlight_zero=True)
        tbl.move_to(UP * 3.5)
        self.play(FadeIn(tbl, shift=UP * 0.3), run_time=0.5)

        decomp = self._decomp_row("5", "8", "0", y=1.9)
        self.play(Write(decomp), run_time=0.7)

        expand = VGroup(
            Text("= 500", font=self.F, font_size=32, color=self.CB, weight=BOLD),
            Text("+", font=self.F, font_size=32, color=WHITE),
            Text("80", font=self.F, font_size=32, color=self.CT, weight=BOLD),
            Text("+", font=self.F, font_size=32, color=WHITE),
            Text("0", font=self.F, font_size=32, color=self.CZERO, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.9)
        self.play(FadeIn(expand), run_time=0.5)

        read = self._read_box("五百八十", y=-0.5)
        self.play(GrowFromCenter(read), run_time=0.5)

        zero_tip = Text("末尾的0，不用读出来！", font=self.F,
                        font_size=26, color=self.CT).move_to(DOWN * 1.7)
        self.play(FadeIn(zero_tip, scale=1.1), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(title), FadeOut(num), FadeOut(tbl),
                  FadeOut(decomp), FadeOut(expand),
                  FadeOut(read), FadeOut(zero_tip), run_time=0.4)

    # ── Scene 6 — 256 分解 ───────────────────────

    def s6_analyze_256(self):
        title = Text("256 的组成", font=self.F, font_size=46,
                     color=self.CY, weight=BOLD).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        num = self._num_big("256", "#AB47BC", y=5.0)
        self.play(GrowFromCenter(num), run_time=0.5)

        tbl = self._place_table(["2", "5", "6"], highlight_zero=False)
        tbl.move_to(UP * 3.5)
        self.play(FadeIn(tbl, shift=UP * 0.3), run_time=0.5)

        decomp = self._decomp_row("2", "5", "6", y=1.9)
        self.play(Write(decomp), run_time=0.7)

        # 标准展开
        expand = VGroup(
            Text("= 200", font=self.F, font_size=32, color=self.CB, weight=BOLD),
            Text("+ 50 +", font=self.F, font_size=32, color=WHITE),
            Text("6", font=self.F, font_size=32, color=self.CO, weight=BOLD),
            Text("= 256", font=self.F, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.9)
        self.play(FadeIn(expand), run_time=0.5)

        read = self._read_box("二百五十六", y=-0.4)
        self.play(GrowFromCenter(read), run_time=0.5)

        # 进阶说法
        extra_bg = RoundedRectangle(
            corner_radius=0.25, width=7.0, height=1.2,
            fill_color="#2E1B4E", fill_opacity=0.7,
            stroke_color="#AB47BC", stroke_width=2
        ).move_to(DOWN * 1.7)
        extra_row = VGroup(
            Text("还可说：", font=self.F, font_size=26, color=GRAY_A),
            Text("25个十", font=self.F, font_size=28,
                 color=self.CT, weight=BOLD),
            Text("和", font=self.F, font_size=26, color=WHITE),
            Text("6个一", font=self.F, font_size=28,
                 color=self.CO, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(extra_bg.get_center())
        self.play(FadeIn(extra_bg), FadeIn(extra_row), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(title), FadeOut(num), FadeOut(tbl),
                  FadeOut(decomp), FadeOut(expand), FadeOut(read),
                  FadeOut(extra_bg), FadeOut(extra_row), run_time=0.4)

    # ── Scene 7 Summary ──────────────────────────

    def s7_summary(self):
        title = Text("知识总结", font=self.F, font_size=54,
                     color=self.CY, weight=BOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        cards_data = [
            ("中间有0，读零",   "304 → 三百零四",          "#7B1FA2", "#CE93D8", 4.5),
            ("末尾有0，不读",   "580 → 五百八十",          "#1565C0", "#42A5F5", 2.5),
            ("数的组成",        "256 = 2百+5十+6一",       "#00695C", "#4DB6AC", 0.5),
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

        cheer = Text("掌握读写，数学无忧！", font=self.F,
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