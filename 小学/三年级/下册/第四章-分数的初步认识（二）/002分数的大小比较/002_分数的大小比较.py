"""
分数的大小比较 - Fraction Size Comparison
三年级下册 第四章 分数的初步认识（二）

内容:
  1. 同分母分数比较 — 分母相同，分子大的分数大
  2. 同分子分数（几分之一）比较 — 分子相同，分母大的分数小
  3. 同分子分数（非1）拓展 — 2/3 与 2/5 的比较

格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 ─────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 调色板 ───────────────────────────────────────────
BG_COLOR    = "#1a1a2e"
C_GOLD      = "#f0c040"
C_BLUE      = "#4fc3f7"
C_GREEN     = "#66bb6a"
C_RED       = "#ef5350"
C_PURPLE    = "#ce93d8"
C_ORANGE    = "#ffa726"
C_GRAY      = "#90a4ae"
C_WHITE     = "#ffffff"
C_DARK_BLUE = "#0d2240"
C_HIGHLIGHT = "#fff176"

# ── 字体 ─────────────────────────────────────────────
FONT = "PingFang SC"


def cn(text, size=24, color=C_WHITE, **kwargs):
    """便捷中文 Text 工厂，统一字体。"""
    return Text(text, font=FONT, font_size=size, color=color, **kwargs)


def fraction_circle(radius=1.0, numerator=1, denominator=4,
                    fill_color=C_BLUE, bg_color=C_DARK_BLUE):
    """
    将圆均分成 denominator 份，填充 numerator 份，返回 VGroup。
    使用 AnnularSector(inner_radius=0) 精确绘制扇形。
    """
    group = VGroup()
    slice_angle = 2 * np.pi / denominator

    for i in range(denominator):
        # 从12点钟（π/2）开始，顺时针方向逐份绘制
        start = np.pi / 2 - i * slice_angle
        sector = AnnularSector(
            inner_radius=0,
            outer_radius=radius,
            start_angle=start,
            angle=-slice_angle,              # 负值 → 顺时针
            fill_opacity=1,
            stroke_width=2,
            color=fill_color if i < numerator else bg_color,
            stroke_color=C_WHITE,
        )
        group.add(sector)

    return group


def fraction_rect(width=2.0, height=0.6, numerator=1, denominator=4,
                  fill_color=C_GREEN, bg_color="#1b3a4b"):
    """
    将矩形横向均分成 denominator 份，填充 numerator 份，返回 VGroup。
    精确计算每份宽度，无臆想坐标。
    """
    group = VGroup()
    unit_w = width / denominator
    for i in range(denominator):
        # 精确偏移：第 i 格中心 x = (i + 0.5) * unit_w - width/2
        x_center = (i + 0.5) * unit_w - width / 2
        rect = Rectangle(
            width=unit_w,
            height=height,
            fill_color=fill_color if i < numerator else bg_color,
            fill_opacity=1,
            stroke_color=C_WHITE,
            stroke_width=2,
        )
        rect.shift(RIGHT * x_center)
        group.add(rect)
    return group


class FractionCompareLesson(Scene):
    """
    分数的大小比较教学动画

    场景顺序:
      1. show_opening     — 开场钩子
      2. show_same_denom  — 同分母分数比较
      3. show_unit_frac   — 同分子（分之一）比较
      4. show_non_unit    — 同分子非1 拓展
      5. show_summary     — 口诀总结
      6. show_outro       — 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 持久存在的作者标识（贯穿全程）
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=C_GRAY,
        ).move_to(UP * 7.0)
        self.add(self.author_tag)

        self.show_opening()
        self.show_same_denom()
        self.show_unit_frac()
        self.show_non_unit()
        self.show_summary()
        self.show_outro()

    # ═══════════════════════════════════════════════
    # 场景 1 : 开场钩子
    # ═══════════════════════════════════════════════
    def show_opening(self):
        title = cn("分数大小怎么比？", size=46, color=C_GOLD)
        title.move_to(UP * 5.5)

        sub = cn("3种方法，一次讲清！", size=28, color=C_WHITE)
        sub.move_to(UP * 4.5)

        items = VGroup(
            cn("① 分母相同 → 看分子", size=24, color=C_BLUE),
            cn("② 分子相同 → 看分母", size=24, color=C_GREEN),
            cn("③ 同分子非1 → 同样看分母", size=24, color=C_PURPLE),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        items.move_to(UP * 2.6)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(sub),
            FadeOut(items),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    # 场景 2 : 同分母分数比较  3/5 vs 2/5
    # ═══════════════════════════════════════════════
    def show_same_denom(self):
        # ─── 标题区 ───
        section_title = cn("① 同分母分数比大小", size=34, color=C_BLUE)
        section_title.move_to(UP * 6.2)
        rule_text = cn("分母相同，分子大的分数大", size=22, color=C_HIGHLIGHT)
        rule_text.move_to(UP * 5.4)

        self.play(Write(section_title), run_time=0.6)
        self.play(FadeIn(rule_text, shift=UP * 0.1), run_time=0.4)

        # ─── 例题行 ───
        eg_row = VGroup(
            cn("比较", size=26, color=C_WHITE),
            MathTex(r"\frac{3}{5}", font_size=52, color=C_ORANGE),
            cn("与", size=26, color=C_WHITE),
            MathTex(r"\frac{2}{5}", font_size=52, color=C_RED),
            cn("的大小", size=26, color=C_WHITE),
        ).arrange(RIGHT, buff=0.25)
        eg_row.move_to(UP * 4.3)

        self.play(FadeIn(eg_row), run_time=0.6)
        self.wait(0.3)

        # ─── 矩形色条 ───
        RECT_W, RECT_H = 3.8, 0.72

        bar_a = fraction_rect(RECT_W, RECT_H, 3, 5, fill_color=C_ORANGE)
        bar_a.move_to(UP * 2.8)

        bar_b = fraction_rect(RECT_W, RECT_H, 2, 5, fill_color=C_RED)
        bar_b.move_to(UP * 1.6)

        label_a = MathTex(r"\frac{3}{5}", font_size=42, color=C_ORANGE)
        label_a.next_to(bar_a, RIGHT, buff=0.25)
        label_b = MathTex(r"\frac{2}{5}", font_size=42, color=C_RED)
        label_b.next_to(bar_b, RIGHT, buff=0.25)

        self.play(Create(bar_a), run_time=0.8)
        self.play(FadeIn(label_a), run_time=0.3)
        self.play(Create(bar_b), run_time=0.8)
        self.play(FadeIn(label_b), run_time=0.3)
        self.wait(0.4)

        # ─── 分母相同说明 ───
        denom_note = cn("分母都是 5，分数单位相同！", size=22, color=C_HIGHLIGHT)
        denom_note.move_to(UP * 0.3)
        self.play(Write(denom_note), run_time=0.6)
        self.wait(0.4)

        # ─── 分子比较 ───
        numer_note = cn("分子：3 > 2，所以…", size=24, color=C_WHITE)
        numer_note.move_to(DOWN * 0.7)

        conclusion = VGroup(
            MathTex(r"\frac{3}{5}", font_size=62, color=C_ORANGE),
            MathTex(r">", font_size=58, color=C_WHITE),
            MathTex(r"\frac{2}{5}", font_size=62, color=C_RED),
        ).arrange(RIGHT, buff=0.35)
        conclusion.move_to(DOWN * 2.0)

        self.play(Write(numer_note), run_time=0.5)
        self.play(FadeIn(conclusion, scale=1.05), run_time=0.8)
        self.wait(1.5)

        # ─── 口诀高亮 ───
        rule_box = SurroundingRectangle(rule_text, color=C_HIGHLIGHT, buff=0.15)
        self.play(Create(rule_box), run_time=0.4)
        self.play(Indicate(rule_text, color=C_GOLD, scale_factor=1.08), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(section_title), FadeOut(rule_text), FadeOut(rule_box),
            FadeOut(eg_row),
            FadeOut(bar_a), FadeOut(bar_b),
            FadeOut(label_a), FadeOut(label_b),
            FadeOut(denom_note), FadeOut(numer_note),
            FadeOut(conclusion),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    # 场景 3 : 同分子（几分之一）比较  1/2 vs 1/4
    # ═══════════════════════════════════════════════
    def show_unit_frac(self):
        # ─── 标题区 ───
        section_title = cn("② 同分子分数（几分之一）", size=34, color=C_GREEN)
        section_title.move_to(UP * 6.2)
        rule_text = cn("分子相同，分母大的分数反而小", size=22, color=C_HIGHLIGHT)
        rule_text.move_to(UP * 5.4)

        self.play(Write(section_title), run_time=0.6)
        self.play(FadeIn(rule_text, shift=UP * 0.1), run_time=0.4)

        # ─── 例题行 ───
        eg_row = VGroup(
            cn("比较", size=26, color=C_WHITE),
            MathTex(r"\frac{1}{2}", font_size=52, color=C_BLUE),
            cn("与", size=26, color=C_WHITE),
            MathTex(r"\frac{1}{4}", font_size=52, color=C_PURPLE),
            cn("的大小", size=26, color=C_WHITE),
        ).arrange(RIGHT, buff=0.25)
        eg_row.move_to(UP * 4.3)

        self.play(FadeIn(eg_row), run_time=0.6)
        self.wait(0.3)

        # ─── 圆形图示 ───
        CIRC_R = 1.05

        circle_half = fraction_circle(CIRC_R, 1, 2, fill_color=C_BLUE)
        circle_half.move_to(LEFT * 2.3 + UP * 2.4)

        circle_quarter = fraction_circle(CIRC_R, 1, 4, fill_color=C_PURPLE)
        circle_quarter.move_to(RIGHT * 2.3 + UP * 2.4)

        label_half = MathTex(r"\frac{1}{2}", font_size=44, color=C_BLUE)
        label_half.next_to(circle_half, DOWN, buff=0.25)
        label_quarter = MathTex(r"\frac{1}{4}", font_size=44, color=C_PURPLE)
        label_quarter.next_to(circle_quarter, DOWN, buff=0.25)

        self.play(Create(circle_half), run_time=0.8)
        self.play(FadeIn(label_half), run_time=0.3)
        self.play(Create(circle_quarter), run_time=0.8)
        self.play(FadeIn(label_quarter), run_time=0.3)
        self.wait(0.4)

        # ─── 解释说明 ───
        explain_1 = cn("分成 2 份 → 每份更大", size=22, color=C_BLUE)
        explain_1.next_to(circle_half, DOWN, buff=0.7)
        explain_2 = cn("分成 4 份 → 每份更小", size=22, color=C_PURPLE)
        explain_2.next_to(circle_quarter, DOWN, buff=0.7)

        self.play(FadeIn(explain_1), run_time=0.4)
        self.play(FadeIn(explain_2), run_time=0.4)
        self.wait(0.5)

        # ─── 关键点 ───
        key_note = cn("分母：2 < 4，但 1/2 > 1/4！", size=24, color=C_HIGHLIGHT)
        key_note.move_to(DOWN * 0.5)
        self.play(Write(key_note), run_time=0.6)
        self.wait(0.4)

        # ─── 结论 ───
        conclusion = VGroup(
            MathTex(r"\frac{1}{2}", font_size=62, color=C_BLUE),
            MathTex(r">", font_size=58, color=C_WHITE),
            MathTex(r"\frac{1}{4}", font_size=62, color=C_PURPLE),
        ).arrange(RIGHT, buff=0.35)
        conclusion.move_to(DOWN * 1.9)

        self.play(FadeIn(conclusion, scale=1.05), run_time=0.8)
        self.wait(1.5)

        # ─── 口诀高亮 ───
        rule_box = SurroundingRectangle(rule_text, color=C_HIGHLIGHT, buff=0.15)
        self.play(Create(rule_box), run_time=0.4)
        self.play(Indicate(rule_text, color=C_GOLD, scale_factor=1.08), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(section_title), FadeOut(rule_text), FadeOut(rule_box),
            FadeOut(eg_row),
            FadeOut(circle_half), FadeOut(circle_quarter),
            FadeOut(label_half), FadeOut(label_quarter),
            FadeOut(explain_1), FadeOut(explain_2),
            FadeOut(key_note), FadeOut(conclusion),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    # 场景 4 : 同分子非1 拓展  2/3 vs 2/5
    # ═══════════════════════════════════════════════
    def show_non_unit(self):
        # ─── 标题区 ───
        section_title = cn("③ 同分子（非1）怎么比？", size=34, color=C_PURPLE)
        section_title.move_to(UP * 6.2)
        rule_text = cn("分子相同，分母越大，分数越小", size=22, color=C_HIGHLIGHT)
        rule_text.move_to(UP * 5.4)

        self.play(Write(section_title), run_time=0.6)
        self.play(FadeIn(rule_text, shift=UP * 0.1), run_time=0.4)

        # ─── 例题行 ───
        eg_row = VGroup(
            cn("比较", size=26, color=C_WHITE),
            MathTex(r"\frac{2}{3}", font_size=52, color=C_ORANGE),
            cn("与", size=26, color=C_WHITE),
            MathTex(r"\frac{2}{5}", font_size=52, color=C_GREEN),
            cn("的大小", size=26, color=C_WHITE),
        ).arrange(RIGHT, buff=0.25)
        eg_row.move_to(UP * 4.3)

        self.play(FadeIn(eg_row), run_time=0.6)
        self.wait(0.3)

        # ─── 矩形图示 ───
        RECT_W, RECT_H = 3.6, 0.7

        bar_23 = fraction_rect(RECT_W, RECT_H, 2, 3, fill_color=C_ORANGE)
        bar_23.move_to(UP * 2.9)

        bar_25 = fraction_rect(RECT_W, RECT_H, 2, 5, fill_color=C_GREEN)
        bar_25.move_to(UP * 1.7)

        label_23 = MathTex(r"\frac{2}{3}", font_size=42, color=C_ORANGE)
        label_23.next_to(bar_23, RIGHT, buff=0.25)
        label_25 = MathTex(r"\frac{2}{5}", font_size=42, color=C_GREEN)
        label_25.next_to(bar_25, RIGHT, buff=0.25)

        self.play(Create(bar_23), run_time=0.8)
        self.play(FadeIn(label_23), run_time=0.3)
        self.play(Create(bar_25), run_time=0.8)
        self.play(FadeIn(label_25), run_time=0.3)
        self.wait(0.4)

        # ─── 分数单位分析 ───
        unit_row = VGroup(
            cn("分数单位：", size=20, color=C_WHITE),
            MathTex(r"\frac{1}{3}", font_size=38, color=C_ORANGE),
            cn("  >  ", size=20, color=C_WHITE),
            MathTex(r"\frac{1}{5}", font_size=38, color=C_GREEN),
        ).arrange(RIGHT, buff=0.15)
        unit_row.move_to(UP * 0.4)

        self.play(FadeIn(unit_row), run_time=0.6)
        self.wait(0.3)

        # ─── 分子分析 ───
        numer_note = cn("分子都是 2 份，每份 1/3 > 1/5", size=22, color=C_WHITE)
        numer_note.move_to(DOWN * 0.5)
        self.play(Write(numer_note), run_time=0.5)
        self.wait(0.3)

        # ─── 结论 ───
        conclusion = VGroup(
            MathTex(r"\frac{2}{3}", font_size=62, color=C_ORANGE),
            MathTex(r">", font_size=58, color=C_WHITE),
            MathTex(r"\frac{2}{5}", font_size=62, color=C_GREEN),
        ).arrange(RIGHT, buff=0.35)
        conclusion.move_to(DOWN * 1.9)

        self.play(FadeIn(conclusion, scale=1.05), run_time=0.8)
        self.wait(1.5)

        # ─── 口诀高亮 ───
        rule_box = SurroundingRectangle(rule_text, color=C_HIGHLIGHT, buff=0.15)
        self.play(Create(rule_box), run_time=0.4)
        self.play(Indicate(rule_text, color=C_GOLD, scale_factor=1.08), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(section_title), FadeOut(rule_text), FadeOut(rule_box),
            FadeOut(eg_row),
            FadeOut(bar_23), FadeOut(bar_25),
            FadeOut(label_23), FadeOut(label_25),
            FadeOut(unit_row), FadeOut(numer_note),
            FadeOut(conclusion),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    # 场景 5 : 口诀总结
    # ═══════════════════════════════════════════════
    def show_summary(self):
        title = cn("口诀总结", size=40, color=C_GOLD)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        def make_card(header_txt, body_txt, accent):
            bg = RoundedRectangle(
                corner_radius=0.25,
                width=7.6,
                height=1.45,
                fill_color=accent,
                fill_opacity=0.18,
                stroke_color=accent,
                stroke_width=2,
            )
            header = cn(header_txt, size=24, color=accent)
            body   = cn(body_txt,   size=20, color=C_WHITE)
            content = VGroup(header, body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = make_card(
            "① 同分母分数",
            "分子大 → 分数大        例：3/5 > 2/5",
            C_BLUE,
        )
        card2 = make_card(
            "② 同分子（几分之一）",
            "分母大 → 分数小        例：1/2 > 1/4",
            C_GREEN,
        )
        card3 = make_card(
            "③ 同分子（非1）",
            "分母大 → 分数小        例：2/3 > 2/5",
            C_PURPLE,
        )

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.3)
        cards.move_to(UP * 2.9)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.15)

        # ─── 核心口诀横幅 ───
        banner_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=1.1,
            fill_color=C_GOLD,
            fill_opacity=0.22,
            stroke_color=C_GOLD,
            stroke_width=2.5,
        ).move_to(DOWN * 2.1)
        banner_txt = cn("分母同→看分子，分子同→看分母", size=25, color=C_GOLD)
        banner_txt.move_to(banner_bg.get_center())

        self.play(Create(banner_bg), run_time=0.4)
        self.play(Write(banner_txt), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(banner_bg),
            FadeOut(banner_txt),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════════
    # 场景 6 : 片尾关注
    # ═══════════════════════════════════════════════
    def show_outro(self):
        big_name = cn("上海初高中数学直通车", size=38, color=C_WHITE)
        big_name.move_to(UP * 1.5)
        big_id = cn("@emptyandcalm", size=30, color=C_GRAY)
        big_id.move_to(UP * 0.5)

        follow = cn("关注我，学更多数学技巧！", size=28, color=C_HIGHLIGHT)
        follow.move_to(DOWN * 0.6)

        self.play(
            ReplacementTransform(self.author_tag, big_name),
            run_time=0.7,
        )
        self.play(FadeIn(big_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2, scale=1.05), run_time=0.5)

        # ─── 彩色小圆装饰 ───
        colors = [C_BLUE, C_GREEN, C_PURPLE, C_ORANGE, C_RED]
        decos = VGroup(*[
            Circle(radius=0.22, fill_color=c, fill_opacity=0.9, stroke_width=0)
            .move_to(
                follow.get_center()
                + 2.4 * np.array([
                    np.cos(i * 2 * np.pi / 5),
                    np.sin(i * 2 * np.pi / 5),
                    0,
                ])
            )
            for i, c in enumerate(colors)
        ])

        self.play(*[FadeIn(d, scale=0.4) for d in decos], run_time=0.5)
        self.play(Rotate(decos, angle=2 * np.pi / 5, run_time=1.2))
        self.wait(1.5)

        self.play(
            FadeOut(big_name),
            FadeOut(big_id),
            FadeOut(follow),
            FadeOut(decos),
            run_time=0.8,
        )
