"""
认识人民币 - 一年级下册 第四章
人民币的分类认识：分、角、元 单位
纸币与硬币的区分

作者: 上海初高中数学直通车 @emptyandcalm
格式: TikTok竖屏 (1080×1920)
"""

from manim import *
import numpy as np

# ── 全局配置：TikTok竖屏 ──────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ── 颜色常量 ─────────────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
GOLD_RMB       = "#d4a017"
RED_RMB        = "#c0392b"
GREEN_RMB      = "#27ae60"
BLUE_RMB       = "#2980b9"
PURPLE_RMB     = "#8e44ad"
COIN_GOLD      = "#f0c040"
COIN_SILVER    = "#b0b8c8"
TEXT_MAIN      = "#ffffff"
TEXT_SUB       = "#adb5bd"
TEXT_HIGHLIGHT = "#ffd700"
ACCENT_TEAL    = "#1abc9c"
CARD_BG        = "#16213e"


def make_banknote(width: float, height: float, face_color: str,
                  value_text: str, unit_text: str,
                  stripe_color: str = "#8B7355") -> VGroup:
    """
    Create a simplified banknote rectangle with value label.
    No corner_radius (forbidden in Manim 0.19).
    """
    body = Rectangle(width=width, height=height,
                     fill_color=face_color, fill_opacity=1,
                     stroke_color=WHITE, stroke_width=1.5)

    # Top stripe
    stripe = Rectangle(width=width, height=height * 0.18,
                       fill_color=stripe_color, fill_opacity=0.6,
                       stroke_width=0)
    stripe.align_to(body, UP).align_to(body, LEFT)

    # Value number
    val_num = Text(value_text, font="PingFang SC",
                   font_size=28, color=WHITE, weight=BOLD)
    val_num.move_to(body.get_center() + DOWN * 0.05)

    # Unit label below number
    val_unit = Text(unit_text, font="PingFang SC",
                    font_size=14, color=WHITE)
    val_unit.next_to(val_num, DOWN, buff=0.05)

    # "中国人民银行" tiny label
    bank_label = Text("中国人民银行", font="PingFang SC",
                      font_size=9, color="#cccccc")
    bank_label.align_to(body, DOWN).shift(UP * 0.12)

    return VGroup(body, stripe, val_num, val_unit, bank_label)


def make_coin(radius: float, face_color: str,
              value_text: str, unit_text: str) -> VGroup:
    """
    Create a simplified coin circle with value label.
    """
    outer = Circle(radius=radius,
                   fill_color=face_color, fill_opacity=1,
                   stroke_color=WHITE, stroke_width=1.5)
    inner = Circle(radius=radius * 0.78,
                   fill_color=face_color, fill_opacity=0,
                   stroke_color=WHITE, stroke_width=0.8,
                   stroke_opacity=0.5)
    # center hole (decorative)
    hole = Circle(radius=radius * 0.18,
                  fill_color=BG_COLOR, fill_opacity=1,
                  stroke_width=0)

    val_num = Text(value_text, font="PingFang SC",
                   font_size=int(radius * 42), color=WHITE, weight=BOLD)
    val_num.move_to(outer.get_center() + UP * radius * 0.15)

    val_unit = Text(unit_text, font="PingFang SC",
                    font_size=int(radius * 22), color=WHITE)
    val_unit.next_to(val_num, DOWN, buff=0.02)

    return VGroup(outer, inner, hole, val_num, val_unit)


class MoneyIntroLesson(Scene):
    """
    一年级下册 第四章 认识人民币
    场景序列:
      1. 开场 - 标题钩子
      2. 认识硬币（分）
      3. 认识硬币与纸币（角）
      4. 认识纸币（元）
      5. 分类：材质（纸币 vs 硬币）
      6. 分类：单位（元 角 分）
      7. 结尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识（全程保留）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author)

        self.scene_1_opening()
        self.scene_2_fen_coins()
        self.scene_3_jiao()
        self.scene_4_yuan_bills()
        self.scene_5_classify_material()
        self.scene_6_classify_unit()
        self.scene_7_outro()

    # ──────────────────────────────────────────────────────────────
    # Scene 1 · 开场钩子
    # ──────────────────────────────────────────────────────────────
    def scene_1_opening(self):
        # Background decorative coins
        deco_coins = VGroup()
        positions = [
            UP * 5.5 + LEFT * 3.2,
            UP * 4.8 + RIGHT * 3.5,
            UP * 3.0 + LEFT * 3.8,
            DOWN * 1.0 + RIGHT * 3.8,
        ]
        for pos in positions:
            c = Circle(radius=0.35, fill_color=COIN_GOLD,
                       fill_opacity=0.25, stroke_width=0)
            c.move_to(pos)
            deco_coins.add(c)

        self.play(FadeIn(deco_coins), run_time=0.5)

        # Main title
        title_line1 = Text("你认识", font="PingFang SC",
                           font_size=52, color=TEXT_MAIN)
        title_line2 = Text("人民币吗？", font="PingFang SC",
                           font_size=52, color=TEXT_HIGHLIGHT)
        title_group = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.2)
        title_group.move_to(UP * 5.5)

        self.play(Write(title_line1), run_time=0.7)
        self.play(Write(title_line2), run_time=0.7)
        self.wait(0.4)

        # Show a large gold coin as hook
        big_coin = make_coin(1.2, COIN_GOLD, "1", "元")
        big_coin.move_to(UP * 3.0)
        self.play(GrowFromCenter(big_coin), run_time=0.8)
        self.play(Indicate(big_coin, color=TEXT_HIGHLIGHT, scale_factor=1.15),
                  run_time=0.7)
        self.wait(0.3)

        # Sub-question
        sub = Text("今天我们来认识人民币！",
                   font="PingFang SC", font_size=30, color=TEXT_SUB)
        sub.move_to(UP * 1.5)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title_group),
            FadeOut(big_coin),
            FadeOut(sub),
            FadeOut(deco_coins),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 2 · 认识硬币：1分、2分、5分
    # ──────────────────────────────────────────────────────────────
    def scene_2_fen_coins(self):
        sec_title = Text("分——最小的单位",
                         font="PingFang SC", font_size=36,
                         color=GOLD_RMB)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        # Explanatory text
        intro = Text("硬币里有 1分、2分、5分",
                     font="PingFang SC", font_size=26, color=TEXT_SUB)
        intro.move_to(UP * 5.4)
        self.play(FadeIn(intro), run_time=0.4)

        # Create three fen coins
        coin_1f = make_coin(0.9, COIN_SILVER, "1", "分")
        coin_2f = make_coin(0.9, COIN_SILVER, "2", "分")
        coin_5f = make_coin(0.9, COIN_SILVER, "5", "分")

        coins_fen = VGroup(coin_1f, coin_2f, coin_5f)
        coins_fen.arrange(RIGHT, buff=0.7)
        coins_fen.move_to(UP * 3.4)

        for coin in coins_fen:
            self.play(GrowFromCenter(coin), run_time=0.45)

        # Labels below each coin
        label_1f = Text("1分", font="PingFang SC",
                        font_size=24, color=COIN_SILVER)
        label_2f = Text("2分", font="PingFang SC",
                        font_size=24, color=COIN_SILVER)
        label_5f = Text("5分", font="PingFang SC",
                        font_size=24, color=COIN_SILVER)

        label_1f.next_to(coin_1f, DOWN, buff=0.2)
        label_2f.next_to(coin_2f, DOWN, buff=0.2)
        label_5f.next_to(coin_5f, DOWN, buff=0.2)

        self.play(
            FadeIn(label_1f), FadeIn(label_2f), FadeIn(label_5f),
            run_time=0.4,
        )

        # Highlight 5fen
        self.play(Indicate(coin_5f, color=TEXT_HIGHLIGHT, scale_factor=1.2),
                  run_time=0.6)

        # Key fact box
        fact_bg = Rectangle(width=6.5, height=1.0,
                             fill_color=CARD_BG, fill_opacity=0.9,
                             stroke_color=COIN_SILVER, stroke_width=1.5)
        fact_bg.move_to(UP * 1.6)
        fact_text = Text("分 是最小的人民币单位",
                         font="PingFang SC", font_size=26, color=TEXT_MAIN)
        fact_text.move_to(fact_bg.get_center())
        self.play(FadeIn(fact_bg), Write(fact_text), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(sec_title), FadeOut(intro),
            FadeOut(coins_fen), FadeOut(label_1f), FadeOut(label_2f),
            FadeOut(label_5f), FadeOut(fact_bg), FadeOut(fact_text),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 3 · 认识角：硬币1角、2角，纸币5角
    # ──────────────────────────────────────────────────────────────
    def scene_3_jiao(self):
        sec_title = Text("角——中间的单位",
                         font="PingFang SC", font_size=36,
                         color=GREEN_RMB)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        intro = Text("硬币：1角、5角  纸币：1角、5角",
                     font="PingFang SC", font_size=22, color=TEXT_SUB)
        intro.move_to(UP * 5.4)
        self.play(FadeIn(intro), run_time=0.4)

        # Coins: 1 jiao, 5 jiao
        coin_1j = make_coin(0.95, COIN_GOLD, "1", "角")
        coin_5j = make_coin(0.95, COIN_GOLD, "5", "角")

        coins_jiao = VGroup(coin_1j, coin_5j)
        coins_jiao.arrange(RIGHT, buff=1.2)
        coins_jiao.move_to(UP * 3.8)

        coin_label_1j = Text("1角 硬币", font="PingFang SC",
                             font_size=22, color=COIN_GOLD)
        coin_label_5j = Text("5角 硬币", font="PingFang SC",
                             font_size=22, color=COIN_GOLD)
        coin_label_1j.next_to(coin_1j, DOWN, buff=0.2)
        coin_label_5j.next_to(coin_5j, DOWN, buff=0.2)

        for coin in coins_jiao:
            self.play(GrowFromCenter(coin), run_time=0.45)
        self.play(FadeIn(coin_label_1j), FadeIn(coin_label_5j), run_time=0.4)

        # Divider
        divider = DashedLine(
            LEFT * 3.8 + UP * 2.5,
            RIGHT * 3.8 + UP * 2.5,
            dash_length=0.15, color=TEXT_SUB, stroke_opacity=0.6
        )
        paper_header = Text("纸  币", font="PingFang SC",
                            font_size=20, color=TEXT_SUB)
        paper_header.move_to(UP * 2.2)
        self.play(Create(divider), FadeIn(paper_header), run_time=0.5)

        # Banknotes: 1 jiao, 5 jiao
        note_1j = make_banknote(2.0, 1.0, "#4a7c59", "1", "角", "#2d5a3e")
        note_5j = make_banknote(2.3, 1.0, "#2e7d4f", "5", "角", "#1a5c35")

        notes_jiao = VGroup(note_1j, note_5j)
        notes_jiao.arrange(RIGHT, buff=0.5)
        notes_jiao.move_to(UP * 1.0)

        note_label_1j = Text("1角 纸币", font="PingFang SC",
                             font_size=22, color=GREEN_RMB)
        note_label_5j = Text("5角 纸币", font="PingFang SC",
                             font_size=22, color=GREEN_RMB)
        note_label_1j.next_to(note_1j, DOWN, buff=0.15)
        note_label_5j.next_to(note_5j, DOWN, buff=0.15)

        for note in notes_jiao:
            self.play(FadeIn(note, shift=UP * 0.2), run_time=0.45)
        self.play(FadeIn(note_label_1j), FadeIn(note_label_5j), run_time=0.4)

        # Key fact
        fact_bg = Rectangle(width=6.5, height=1.0,
                             fill_color=CARD_BG, fill_opacity=0.9,
                             stroke_color=GREEN_RMB, stroke_width=1.5)
        fact_bg.move_to(DOWN * 1.0)
        fact_text = Text("角 有硬币也有纸币",
                         font="PingFang SC", font_size=26,
                         color=TEXT_MAIN)
        fact_text.move_to(fact_bg.get_center())
        self.play(FadeIn(fact_bg), Write(fact_text), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(intro),
            FadeOut(coins_jiao), FadeOut(coin_label_1j), FadeOut(coin_label_5j),
            FadeOut(divider), FadeOut(paper_header),
            FadeOut(notes_jiao), FadeOut(note_label_1j), FadeOut(note_label_5j),
            FadeOut(fact_bg), FadeOut(fact_text),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 4 · 认识元纸币：1, 2, 5, 10, 20, 50, 100 元
    # ──────────────────────────────────────────────────────────────
    def scene_4_yuan_bills(self):
        sec_title = Text("元——最常用的单位",
                         font="PingFang SC", font_size=36,
                         color=RED_RMB)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        intro = Text("1元还有硬币，其他元是纸币",
                     font="PingFang SC", font_size=24, color=TEXT_SUB)
        intro.move_to(UP * 5.4)
        self.play(FadeIn(intro), run_time=0.4)

        # 1 yuan coin
        coin_1y = make_coin(0.9, COIN_GOLD, "1", "元")
        coin_1y.move_to(UP * 4.3 + LEFT * 2.8)
        coin_1y_label = Text("1元 硬币", font="PingFang SC",
                             font_size=20, color=COIN_GOLD)
        coin_1y_label.next_to(coin_1y, DOWN, buff=0.15)

        self.play(GrowFromCenter(coin_1y), run_time=0.5)
        self.play(FadeIn(coin_1y_label), run_time=0.3)

        # Paper money panel
        note_data = [
            ("1",   "元", "#8B0000", "#6B0000"),
            ("2",   "元", "#006400", "#004d00"),
            ("5",   "元", "#8B4513", "#6b3410"),
            ("10",  "元", "#4B0082", "#380063"),
            ("20",  "元", "#B8860B", "#8a6508"),
            ("50",  "元", "#2F4F4F", "#1e3636"),
            ("100", "元", "#8B0000", "#6B0000"),
        ]

        # Show notes in two groups for readability
        group1_data = note_data[:4]   # 1, 2, 5, 10
        group2_data = note_data[4:]   # 20, 50, 100

        notes_group1 = VGroup(*[
            make_banknote(1.55, 0.82, d[2], d[0], d[1], d[3])
            for d in group1_data
        ])
        notes_group1.arrange(RIGHT, buff=0.18)
        notes_group1.move_to(UP * 3.0 + RIGHT * 0.5)

        self.play(FadeIn(notes_group1, shift=UP * 0.2), run_time=0.7)
        self.wait(0.3)

        notes_group2 = VGroup(*[
            make_banknote(1.75, 0.88, d[2], d[0], d[1], d[3])
            for d in group2_data
        ])
        notes_group2.arrange(RIGHT, buff=0.25)
        notes_group2.move_to(UP * 1.6 + RIGHT * 0.5)

        self.play(FadeIn(notes_group2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)

        # Highlight 100 yuan
        note_100 = notes_group2[2]
        self.play(Indicate(note_100, color=TEXT_HIGHLIGHT, scale_factor=1.15),
                  run_time=0.7)

        # Labels
        labels_row1 = VGroup(*[
            Text(d[0] + d[1], font="PingFang SC",
                 font_size=16, color=TEXT_SUB)
            for d in group1_data
        ])
        for lbl, note in zip(labels_row1, notes_group1):
            lbl.next_to(note, DOWN, buff=0.1)

        labels_row2 = VGroup(*[
            Text(d[0] + d[1], font="PingFang SC",
                 font_size=16, color=TEXT_SUB)
            for d in group2_data
        ])
        for lbl, note in zip(labels_row2, notes_group2):
            lbl.next_to(note, DOWN, buff=0.1)

        self.play(FadeIn(labels_row1), FadeIn(labels_row2), run_time=0.4)

        # Key fact
        fact_bg = Rectangle(width=6.8, height=1.1,
                             fill_color=CARD_BG, fill_opacity=0.9,
                             stroke_color=RED_RMB, stroke_width=1.5)
        fact_bg.move_to(DOWN * 0.8)
        fact_text = Text("共有 7 种面值的元币",
                         font="PingFang SC", font_size=26,
                         color=TEXT_MAIN)
        fact_text.move_to(fact_bg.get_center())
        self.play(FadeIn(fact_bg), Write(fact_text), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(sec_title), FadeOut(intro),
            FadeOut(coin_1y), FadeOut(coin_1y_label),
            FadeOut(notes_group1), FadeOut(notes_group2),
            FadeOut(labels_row1), FadeOut(labels_row2),
            FadeOut(fact_bg), FadeOut(fact_text),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 5 · 按材质分类：纸币 vs 硬币
    # ──────────────────────────────────────────────────────────────
    def scene_5_classify_material(self):
        sec_title = Text("按材质分类",
                         font="PingFang SC", font_size=38,
                         color=ACCENT_TEAL)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        # Two columns
        col_left_x  = -2.2
        col_right_x =  2.2

        # --- Left: 纸币 header ---
        paper_label = Text("纸 币", font="PingFang SC",
                           font_size=32, color=GREEN_RMB)
        paper_label.move_to(UP * 5.2 + RIGHT * col_left_x)

        paper_underline = Line(
            paper_label.get_left() + DOWN * 0.05,
            paper_label.get_right() + DOWN * 0.05,
            color=GREEN_RMB, stroke_width=2
        )

        # --- Right: 硬币 header ---
        coin_label = Text("硬 币", font="PingFang SC",
                          font_size=32, color=COIN_GOLD)
        coin_label.move_to(UP * 5.2 + RIGHT * col_right_x)

        coin_underline = Line(
            coin_label.get_left() + DOWN * 0.05,
            coin_label.get_right() + DOWN * 0.05,
            color=COIN_GOLD, stroke_width=2
        )

        self.play(
            Write(paper_label), Create(paper_underline),
            Write(coin_label), Create(coin_underline),
            run_time=0.6,
        )

        # Vertical divider
        v_div = DashedLine(
            UP * 4.8, DOWN * 2.0,
            dash_length=0.15, color=TEXT_SUB, stroke_opacity=0.5
        )
        self.play(Create(v_div), run_time=0.4)

        # Paper bills (left column)
        paper_items = VGroup(
            make_banknote(1.6, 0.78, "#4a7c59", "1", "角", "#2d5a3e"),
            make_banknote(1.6, 0.78, "#2e7d4f", "5", "角", "#1a5c35"),
            make_banknote(1.6, 0.78, "#8B0000", "1", "元", "#6B0000"),
            make_banknote(1.6, 0.78, "#006400", "5", "元", "#004d00"),
            make_banknote(1.6, 0.78, "#4B0082", "10", "元", "#380063"),
            make_banknote(1.6, 0.78, "#B8860B", "20", "元", "#8a6508"),
            make_banknote(1.6, 0.78, "#2F4F4F", "50", "元", "#1e3636"),
            make_banknote(1.6, 0.78, "#8B0000", "100", "元", "#6B0000"),
        )
        paper_items.arrange(DOWN, buff=0.12)
        paper_items.move_to(UP * 1.6 + RIGHT * col_left_x)

        # Coins (right column)
        coin_items = VGroup(
            make_coin(0.5, COIN_SILVER, "1", "分"),
            make_coin(0.5, COIN_SILVER, "2", "分"),
            make_coin(0.5, COIN_SILVER, "5", "分"),
            make_coin(0.5, COIN_GOLD,   "1", "角"),
            make_coin(0.5, COIN_GOLD,   "5", "角"),
            make_coin(0.5, COIN_GOLD,   "1", "元"),
        )
        coin_items.arrange(DOWN, buff=0.15)
        coin_items.move_to(UP * 1.6 + RIGHT * col_right_x)

        self.play(FadeIn(paper_items, shift=RIGHT * 0.3), run_time=0.7)
        self.play(FadeIn(coin_items, shift=LEFT * 0.3), run_time=0.7)
        self.wait(1.0)

        # Summary at bottom
        summary_bg = Rectangle(width=7.2, height=1.4,
                               fill_color=CARD_BG, fill_opacity=0.95,
                               stroke_color=ACCENT_TEAL, stroke_width=1.5)
        summary_bg.move_to(DOWN * 2.8)
        s1 = Text("纸币：印在纸上，面值较大",
                  font="PingFang SC", font_size=22, color=GREEN_RMB)
        s2 = Text("硬币：金属制造，便于携带",
                  font="PingFang SC", font_size=22, color=COIN_GOLD)
        VGroup(s1, s2).arrange(DOWN, buff=0.15).move_to(summary_bg.get_center())

        self.play(FadeIn(summary_bg), Write(s1), Write(s2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title),
            FadeOut(paper_label), FadeOut(paper_underline),
            FadeOut(coin_label), FadeOut(coin_underline),
            FadeOut(v_div),
            FadeOut(paper_items), FadeOut(coin_items),
            FadeOut(summary_bg), FadeOut(s1), FadeOut(s2),
            run_time=0.6,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 6 · 按单位分类：元 角 分
    # ──────────────────────────────────────────────────────────────
    def scene_6_classify_unit(self):
        sec_title = Text("按单位分类",
                         font="PingFang SC", font_size=38,
                         color=PURPLE_RMB)
        sec_title.move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        # Three unit headers
        yuan_hdr = Text("元", font="PingFang SC",
                        font_size=44, color=RED_RMB, weight=BOLD)
        jiao_hdr = Text("角", font="PingFang SC",
                        font_size=44, color=GREEN_RMB, weight=BOLD)
        fen_hdr  = Text("分", font="PingFang SC",
                        font_size=44, color=COIN_SILVER, weight=BOLD)

        headers = VGroup(yuan_hdr, jiao_hdr, fen_hdr)
        headers.arrange(RIGHT, buff=1.8)
        headers.move_to(UP * 5.2)

        self.play(
            FadeIn(yuan_hdr, shift=DOWN * 0.3),
            FadeIn(jiao_hdr, shift=DOWN * 0.3),
            FadeIn(fen_hdr,  shift=DOWN * 0.3),
            run_time=0.6,
        )

        # Underlines
        def make_underline(mob, color):
            return Line(mob.get_left() + DOWN * 0.08,
                        mob.get_right() + DOWN * 0.08,
                        color=color, stroke_width=2.5)

        ul_y = make_underline(yuan_hdr, RED_RMB)
        ul_j = make_underline(jiao_hdr, GREEN_RMB)
        ul_f = make_underline(fen_hdr, COIN_SILVER)
        self.play(Create(ul_y), Create(ul_j), Create(ul_f), run_time=0.4)

        # 元 column items
        yuan_col = VGroup(
            make_banknote(1.45, 0.72, "#8B0000", "1",   "元", "#6B0000"),
            make_banknote(1.45, 0.72, "#006400", "2",   "元", "#004d00"),
            make_banknote(1.45, 0.72, "#006400", "5",   "元", "#004d00"),
            make_banknote(1.45, 0.72, "#4B0082", "10",  "元", "#380063"),
            make_banknote(1.45, 0.72, "#B8860B", "20",  "元", "#8a6508"),
            make_banknote(1.45, 0.72, "#2F4F4F", "50",  "元", "#1e3636"),
            make_banknote(1.45, 0.72, "#8B0000", "100", "元", "#6B0000"),
            make_coin(0.45, COIN_GOLD, "1", "元"),
        )
        yuan_col.arrange(DOWN, buff=0.06)
        yuan_col.move_to(yuan_hdr.get_center() + DOWN * 3.5)

        # 角 column items
        jiao_col = VGroup(
            make_banknote(1.45, 0.72, "#4a7c59", "1", "角", "#2d5a3e"),
            make_banknote(1.45, 0.72, "#2e7d4f", "5", "角", "#1a5c35"),
            make_coin(0.45, COIN_GOLD, "1", "角"),
            make_coin(0.45, COIN_GOLD, "5", "角"),
        )
        jiao_col.arrange(DOWN, buff=0.18)
        jiao_col.move_to(jiao_hdr.get_center() + DOWN * 2.8)

        # 分 column items
        fen_col = VGroup(
            make_coin(0.48, COIN_SILVER, "1", "分"),
            make_coin(0.48, COIN_SILVER, "2", "分"),
            make_coin(0.48, COIN_SILVER, "5", "分"),
        )
        fen_col.arrange(DOWN, buff=0.28)
        fen_col.move_to(fen_hdr.get_center() + DOWN * 2.2)

        self.play(FadeIn(yuan_col), run_time=0.5)
        self.play(FadeIn(jiao_col), run_time=0.5)
        self.play(FadeIn(fen_col),  run_time=0.5)
        self.wait(0.5)

        # Indicate each column in turn
        self.play(Indicate(yuan_col, color=RED_RMB, scale_factor=1.05),
                  run_time=0.6)
        self.play(Indicate(jiao_col, color=GREEN_RMB, scale_factor=1.05),
                  run_time=0.6)
        self.play(Indicate(fen_col, color=COIN_SILVER, scale_factor=1.05),
                  run_time=0.6)

        # Key relation
        rel_bg = Rectangle(width=7.2, height=1.6,
                           fill_color=CARD_BG, fill_opacity=0.95,
                           stroke_color=PURPLE_RMB, stroke_width=1.5)
        rel_bg.move_to(DOWN * 4.8)

        r1 = Text("1元 = 10角", font="PingFang SC",
                  font_size=26, color=TEXT_HIGHLIGHT)
        r2 = Text("1角 = 10分", font="PingFang SC",
                  font_size=26, color=TEXT_HIGHLIGHT)
        VGroup(r1, r2).arrange(DOWN, buff=0.2).move_to(rel_bg.get_center())

        self.play(FadeIn(rel_bg), Write(r1), Write(r2), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(sec_title),
            FadeOut(headers), FadeOut(ul_y), FadeOut(ul_j), FadeOut(ul_f),
            FadeOut(yuan_col), FadeOut(jiao_col), FadeOut(fen_col),
            FadeOut(rel_bg), FadeOut(r1), FadeOut(r2),
            run_time=0.6,
        )

    # ──────────────────────────────────────────────────────────────
    # Scene 7 · 结尾
    # ──────────────────────────────────────────────────────────────
    def scene_7_outro(self):
        # Summary card
        summary_title = Text("人民币 — 总结",
                             font="PingFang SC", font_size=40,
                             color=TEXT_HIGHLIGHT)
        summary_title.move_to(UP * 4.5)
        self.play(Write(summary_title), run_time=0.7)

        items = [
            ("分", "最小单位：1分、2分、5分", COIN_SILVER),
            ("角", "中间单位：1角、2角、5角", GREEN_RMB),
            ("元", "常用单位：1~100元", RED_RMB),
        ]

        cards = VGroup()
        for i, (unit, desc, color) in enumerate(items):
            bg = Rectangle(width=7.0, height=1.1,
                           fill_color=CARD_BG, fill_opacity=0.95,
                           stroke_color=color, stroke_width=1.8)
            unit_t = Text(unit, font="PingFang SC",
                          font_size=36, color=color, weight=BOLD)
            desc_t = Text(desc, font="PingFang SC",
                          font_size=22, color=TEXT_MAIN)
            unit_t.move_to(bg.get_left() + RIGHT * 0.7)
            desc_t.move_to(bg.get_center() + RIGHT * 0.4)
            cards.add(VGroup(bg, unit_t, desc_t))

        cards.arrange(DOWN, buff=0.25)
        cards.move_to(UP * 1.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.45)

        self.wait(0.5)

        # Floating coins decoration
        deco = VGroup()
        offsets = [LEFT * 3.5 + DOWN * 1.5,
                   RIGHT * 3.5 + DOWN * 1.5,
                   LEFT * 3.5 + DOWN * 3.0,
                   RIGHT * 3.5 + DOWN * 3.0]
        for off in offsets:
            c = Circle(radius=0.28, fill_color=COIN_GOLD,
                       fill_opacity=0.5, stroke_width=0)
            c.move_to(off)
            deco.add(c)
        self.play(*[FadeIn(d, scale=0.3) for d in deco], run_time=0.5)

        # Follow call-to-action
        follow_bg = Rectangle(width=7.5, height=1.5,
                              fill_color="#0f3460", fill_opacity=0.95,
                              stroke_color=TEXT_HIGHLIGHT, stroke_width=2)
        follow_bg.move_to(DOWN * 3.8)
        follow_text = Text("关注我，获得更多数学技巧！",
                           font="PingFang SC", font_size=28,
                           color=TEXT_HIGHLIGHT)
        follow_text.move_to(follow_bg.get_center())

        self.play(FadeIn(follow_bg), Write(follow_text), run_time=0.7)

        # Author info large
        author_large = Text("上海初高中数学直通车 @emptyandcalm",
                            font="PingFang SC", font_size=22,
                            color=TEXT_SUB)
        author_large.move_to(DOWN * 5.2)
        self.play(FadeIn(author_large, shift=UP * 0.2), run_time=0.5)

        self.wait(2.5)

        self.play(
            FadeOut(summary_title), FadeOut(cards),
            FadeOut(deco), FadeOut(follow_bg), FadeOut(follow_text),
            FadeOut(author_large),
            run_time=1.0,
        )
