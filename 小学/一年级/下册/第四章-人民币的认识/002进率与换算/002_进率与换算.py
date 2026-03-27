"""
002_进率与换算.py — 人民币进率与换算 教学动画

知识点: 1元=10角, 1角=10分, 1元=100分
  - 核心口诀: 1元=10角, 1角=10分
  - 单名数换算: 如 5元=(50)角, 70角=(7)元
  - 理解十进制在货币中的应用
年级: 一年级下册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_YUAN = "#f59e0b"      # 金色 — 元
COLOR_JIAO = "#3b82f6"      # 蓝色 — 角
COLOR_FEN  = "#22c55e"      # 绿色 — 分
COLOR_HL   = "#fbbf24"      # 黄色高亮
COLOR_ARROW= "#e879f9"      # 紫色箭头
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


def make_coin(label_text, color, radius=0.5, font_size=28):
    """创建一枚硬币图形"""
    circle = Circle(radius=radius, fill_color=color, fill_opacity=0.85,
                    stroke_color=WHITE, stroke_width=2)
    label = Text(label_text, font=FONT, font_size=font_size, color=WHITE)
    label.move_to(circle.get_center())
    return VGroup(circle, label)


def make_label_box(text_str, color, font_size=32, width=2.0, height=0.7):
    """创建带圆角的标注框"""
    box = RoundedRectangle(corner_radius=0.15, width=width, height=height,
                           fill_color=color, fill_opacity=0.25,
                           stroke_color=color, stroke_width=2)
    txt = Text(text_str, font=FONT, font_size=font_size, color=color)
    txt.move_to(box.get_center())
    return VGroup(box, txt)


# ======================================================================
# 主场景
# ======================================================================

class MoneyConversionLesson(Scene):
    """
    人民币进率与换算教学动画
    场景顺序:
      1. 开场钩子 — 换钱游戏
      2. 认识元、角、分
      3. 核心口诀: 1元=10角
      4. 核心口诀: 1角=10分
      5. 推导: 1元=100分
      6. 换算练习: 元到角
      7. 换算练习: 角到元
      8. 总结口诀
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识 (全程保留)
        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.add(self.author_bar)

        self.scene_1_opening()
        self.scene_2_units()
        self.scene_3_yuan_to_jiao()
        self.scene_4_jiao_to_fen()
        self.scene_5_yuan_to_fen()
        self.scene_6_convert_yuan_jiao()
        self.scene_7_convert_jiao_yuan()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 场景 1 — 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        hook = Text("换钱游戏", font=FONT, font_size=56, color=COLOR_HL)
        hook.move_to(UP * 5.0)

        question = Text("1元能换几角?", font=FONT, font_size=40, color=WHITE)
        question.move_to(UP * 3.6)

        # 1元硬币
        coin_1yuan = make_coin("1元", COLOR_YUAN, radius=0.9, font_size=36)
        coin_1yuan.move_to(UP * 1.5)

        # 10枚1角硬币排成两行
        jiao_coins = VGroup()
        for i in range(10):
            c = make_coin("1角", COLOR_JIAO, radius=0.38, font_size=16)
            row = i // 5
            col = i % 5
            c.move_to(np.array([-1.8 + col * 0.95, -0.7 - row * 1.0, 0]))
            jiao_coins.add(c)

        eq_arrow = Arrow(UP * 0.45, DOWN * 0.1, buff=0.1, color=COLOR_ARROW,
                         stroke_width=5, max_tip_length_to_length_ratio=0.18)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.play(GrowFromCenter(coin_1yuan), run_time=0.8)
        self.play(Create(eq_arrow), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in jiao_coins],
                              lag_ratio=0.08), run_time=1.2)
        self.wait(0.6)

        self.play(FadeOut(hook), FadeOut(question), FadeOut(coin_1yuan),
                  FadeOut(eq_arrow), FadeOut(jiao_coins), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 2 — 认识元、角、分
    # ------------------------------------------------------------------

    def scene_2_units(self):
        title = Text("人民币的单位", font=FONT, font_size=44, color=COLOR_HL)
        title.move_to(UP * 5.8)

        yuan_card = make_label_box("元", COLOR_YUAN, font_size=48, width=2.2, height=1.1)
        jiao_card = make_label_box("角", COLOR_JIAO, font_size=48, width=2.2, height=1.1)
        fen_card  = make_label_box("分", COLOR_FEN,  font_size=48, width=2.2, height=1.1)

        cards = VGroup(yuan_card, jiao_card, fen_card)
        cards.arrange(DOWN, buff=0.6)
        cards.move_to(UP * 2.5)

        # 大到小箭头
        arrow1 = Arrow(yuan_card.get_bottom() + DOWN * 0.05,
                       jiao_card.get_top()    + UP   * 0.05,
                       buff=0.0, color=WHITE, stroke_width=3,
                       max_tip_length_to_length_ratio=0.2)
        arrow2 = Arrow(jiao_card.get_bottom() + DOWN * 0.05,
                       fen_card.get_top()     + UP   * 0.05,
                       buff=0.0, color=WHITE, stroke_width=3,
                       max_tip_length_to_length_ratio=0.2)

        note = Text("从大到小", font=FONT, font_size=28, color=GRAY_A)
        note.move_to(DOWN * 3.5)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(yuan_card, shift=RIGHT * 0.3), run_time=0.4)
        self.play(GrowArrow(arrow1), run_time=0.3)
        self.play(FadeIn(jiao_card, shift=RIGHT * 0.3), run_time=0.4)
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(FadeIn(fen_card,  shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(title), FadeOut(cards), FadeOut(arrow1),
                  FadeOut(arrow2), FadeOut(note), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 3 — 1元 = 10角
    # ------------------------------------------------------------------

    def scene_3_yuan_to_jiao(self):
        title = Text("1元 = 10角", font=FONT, font_size=50, color=COLOR_YUAN)
        title.move_to(UP * 6.0)

        coin_yuan = make_coin("1元", COLOR_YUAN, radius=1.0, font_size=40)
        coin_yuan.move_to(np.array([-2.2, 2.8, 0]))

        equal_sign = Text("=", font=FONT, font_size=60, color=WHITE)
        equal_sign.move_to(np.array([0.0, 2.8, 0]))

        # 10枚1角硬币
        jiao_group = VGroup()
        for i in range(10):
            c = make_coin("1角", COLOR_JIAO, radius=0.36, font_size=15)
            row = i // 5
            col = i % 5
            c.move_to(np.array([1.0 + col * 0.82, 3.3 - row * 0.82, 0]))
            jiao_group.add(c)

        # 进率口诀框
        rule_box = RoundedRectangle(corner_radius=0.2, width=6.5, height=1.0,
                                    fill_color="#1a3a1a", fill_opacity=0.8,
                                    stroke_color=COLOR_YUAN, stroke_width=3)
        rule_box.move_to(UP * 0.8)

        rule_text = Text("1元 = 10角  (进率是 10)", font=FONT, font_size=30,
                         color=COLOR_YUAN)
        rule_text.move_to(rule_box.get_center())

        deci_text = Text("元到角，乘以 10", font=FONT, font_size=28, color=GRAY_A)
        deci_text.move_to(DOWN * 0.5)

        self.play(Write(title), run_time=0.6)
        self.play(GrowFromCenter(coin_yuan), run_time=0.7)
        self.play(Write(equal_sign), run_time=0.3)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in jiao_group],
                              lag_ratio=0.06), run_time=1.0)
        self.wait(0.4)

        self.play(Create(rule_box), run_time=0.5)
        self.play(Write(rule_text), run_time=0.6)
        self.play(FadeIn(deci_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(coin_yuan), FadeOut(equal_sign),
                  FadeOut(jiao_group), FadeOut(rule_box), FadeOut(rule_text),
                  FadeOut(deci_text), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 4 — 1角 = 10分
    # ------------------------------------------------------------------

    def scene_4_jiao_to_fen(self):
        title = Text("1角 = 10分", font=FONT, font_size=50, color=COLOR_JIAO)
        title.move_to(UP * 6.0)

        coin_jiao = make_coin("1角", COLOR_JIAO, radius=1.0, font_size=40)
        coin_jiao.move_to(np.array([-2.2, 2.8, 0]))

        equal_sign = Text("=", font=FONT, font_size=60, color=WHITE)
        equal_sign.move_to(np.array([0.0, 2.8, 0]))

        fen_group = VGroup()
        for i in range(10):
            c = make_coin("1分", COLOR_FEN, radius=0.36, font_size=15)
            row = i // 5
            col = i % 5
            c.move_to(np.array([1.0 + col * 0.82, 3.3 - row * 0.82, 0]))
            fen_group.add(c)

        rule_box = RoundedRectangle(corner_radius=0.2, width=6.5, height=1.0,
                                    fill_color="#0d2a1a", fill_opacity=0.8,
                                    stroke_color=COLOR_JIAO, stroke_width=3)
        rule_box.move_to(UP * 0.8)

        rule_text = Text("1角 = 10分  (进率是 10)", font=FONT, font_size=30,
                         color=COLOR_JIAO)
        rule_text.move_to(rule_box.get_center())

        deci_text = Text("角到分，乘以 10", font=FONT, font_size=28, color=GRAY_A)
        deci_text.move_to(DOWN * 0.5)

        self.play(Write(title), run_time=0.6)
        self.play(GrowFromCenter(coin_jiao), run_time=0.7)
        self.play(Write(equal_sign), run_time=0.3)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in fen_group],
                              lag_ratio=0.06), run_time=1.0)
        self.wait(0.4)

        self.play(Create(rule_box), run_time=0.5)
        self.play(Write(rule_text), run_time=0.6)
        self.play(FadeIn(deci_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(coin_jiao), FadeOut(equal_sign),
                  FadeOut(fen_group), FadeOut(rule_box), FadeOut(rule_text),
                  FadeOut(deci_text), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 5 — 1元 = 100分 (推导)
    # ------------------------------------------------------------------

    def scene_5_yuan_to_fen(self):
        title = Text("1元 = 100分", font=FONT, font_size=50, color=COLOR_HL)
        title.move_to(UP * 6.2)

        # 推导步骤
        step1_a = Text("1元", font=FONT, font_size=36, color=COLOR_YUAN)
        step1_eq = Text("=", font=FONT, font_size=36, color=WHITE)
        step1_b = Text("10角", font=FONT, font_size=36, color=COLOR_JIAO)
        step1 = VGroup(step1_a, step1_eq, step1_b).arrange(RIGHT, buff=0.25)
        step1.move_to(UP * 4.5)

        arrow_down = Arrow(UP * 4.0, UP * 3.2, buff=0.05, color=GRAY_A,
                           stroke_width=3, max_tip_length_to_length_ratio=0.2)
        note_10 = Text("每角再换10分", font=FONT, font_size=22, color=GRAY_A)
        note_10.next_to(arrow_down, RIGHT, buff=0.15)

        step2_a = Text("10角", font=FONT, font_size=36, color=COLOR_JIAO)
        step2_eq = Text("=", font=FONT, font_size=36, color=WHITE)
        step2_b = Text("100分", font=FONT, font_size=36, color=COLOR_FEN)
        step2 = VGroup(step2_a, step2_eq, step2_b).arrange(RIGHT, buff=0.25)
        step2.move_to(UP * 2.8)

        therefore_line = Line(LEFT * 3.0, RIGHT * 3.0, color=GRAY_A, stroke_width=1.5)
        therefore_line.move_to(UP * 1.8)

        concl_a = Text("1元", font=FONT, font_size=44, color=COLOR_YUAN)
        concl_eq = Text("=", font=FONT, font_size=44, color=WHITE)
        concl_b = Text("100分", font=FONT, font_size=44, color=COLOR_FEN)
        conclusion = VGroup(concl_a, concl_eq, concl_b).arrange(RIGHT, buff=0.3)
        conclusion.move_to(UP * 1.0)

        concl_box = RoundedRectangle(corner_radius=0.2, width=5.0, height=1.1,
                                     fill_color="#2a1a00", fill_opacity=0.8,
                                     stroke_color=COLOR_HL, stroke_width=3)
        concl_box.move_to(conclusion.get_center())

        formula_text = Text("10 x 10 = 100", font=FONT, font_size=30, color=GRAY_A)
        formula_text.move_to(DOWN * 0.3)

        memory_text = Text("记住: 元到分，乘以 100", font=FONT, font_size=28,
                           color=COLOR_HL)
        memory_text.move_to(DOWN * 1.4)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(step1, shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arrow_down), FadeIn(note_10), run_time=0.5)
        self.play(FadeIn(step2, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(0.4)
        self.play(Create(therefore_line), run_time=0.4)
        self.play(Create(concl_box), run_time=0.4)
        self.play(Write(conclusion), run_time=0.7)
        self.play(FadeIn(formula_text), run_time=0.4)
        self.play(FadeIn(memory_text, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(title), FadeOut(step1), FadeOut(arrow_down),
                  FadeOut(note_10), FadeOut(step2), FadeOut(therefore_line),
                  FadeOut(concl_box), FadeOut(conclusion), FadeOut(formula_text),
                  FadeOut(memory_text), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 6 — 换算练习: 元到角
    # ------------------------------------------------------------------

    def scene_6_convert_yuan_jiao(self):
        title = Text("换算练习", font=FONT, font_size=44, color=COLOR_HL)
        title.move_to(UP * 6.2)

        subtitle = Text("元 换 角", font=FONT, font_size=34, color=COLOR_YUAN)
        subtitle.move_to(UP * 5.4)

        rule = Text("x 10", font=FONT, font_size=28, color=COLOR_YUAN)
        rule.move_to(UP * 4.7)

        # 例1: 5元 = ? 角
        ex1_q_a = Text("5元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex1_q_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex1_q_b = Text("(   )角", font=FONT, font_size=42, color=GRAY_A)
        ex1_q = VGroup(ex1_q_a, ex1_q_eq, ex1_q_b).arrange(RIGHT, buff=0.3)
        ex1_q.move_to(UP * 3.5)

        ex1_hint_a = Text("5", font=FONT, font_size=34, color=COLOR_YUAN)
        ex1_hint_x = Text("x", font=FONT, font_size=34, color=WHITE)
        ex1_hint_b = Text("10", font=FONT, font_size=34, color=COLOR_YUAN)
        ex1_hint_eq= Text("=", font=FONT, font_size=34, color=WHITE)
        ex1_hint_c = Text("50", font=FONT, font_size=34, color=COLOR_JIAO)
        ex1_hint = VGroup(ex1_hint_a, ex1_hint_x, ex1_hint_b,
                          ex1_hint_eq, ex1_hint_c).arrange(RIGHT, buff=0.2)
        ex1_hint.move_to(UP * 2.5)

        ex1_ans_a = Text("5元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex1_ans_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex1_ans_b = Text("50角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex1_ans = VGroup(ex1_ans_a, ex1_ans_eq, ex1_ans_b).arrange(RIGHT, buff=0.3)
        ex1_ans.move_to(UP * 1.4)

        ex1_check = Text("V", font=FONT, font_size=50, color=COLOR_FEN)
        ex1_check.next_to(ex1_ans, RIGHT, buff=0.3)

        # 例2: 3元 = ? 角
        ex2_q_a = Text("3元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex2_q_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex2_q_b = Text("(   )角", font=FONT, font_size=42, color=GRAY_A)
        ex2_q = VGroup(ex2_q_a, ex2_q_eq, ex2_q_b).arrange(RIGHT, buff=0.3)
        ex2_q.move_to(DOWN * 0.2)

        ex2_ans_a = Text("3元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex2_ans_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex2_ans_b = Text("30角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex2_ans = VGroup(ex2_ans_a, ex2_ans_eq, ex2_ans_b).arrange(RIGHT, buff=0.3)
        ex2_ans.move_to(DOWN * 1.2)

        ex2_check = Text("V", font=FONT, font_size=50, color=COLOR_FEN)
        ex2_check.next_to(ex2_ans, RIGHT, buff=0.3)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(subtitle), FadeIn(rule), run_time=0.4)

        self.play(FadeIn(ex1_q, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ex1_hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex1_ans, shift=UP * 0.2), run_time=0.5)
        self.play(Write(ex1_check), run_time=0.3)
        self.wait(0.8)

        self.play(FadeIn(ex2_q, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ex2_ans, shift=UP * 0.2), run_time=0.5)
        self.play(Write(ex2_check), run_time=0.3)
        self.wait(1.2)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(rule),
                  FadeOut(ex1_q), FadeOut(ex1_hint),
                  FadeOut(ex1_ans), FadeOut(ex1_check),
                  FadeOut(ex2_q), FadeOut(ex2_ans), FadeOut(ex2_check),
                  run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 7 — 换算练习: 角到元
    # ------------------------------------------------------------------

    def scene_7_convert_jiao_yuan(self):
        title = Text("换算练习", font=FONT, font_size=44, color=COLOR_HL)
        title.move_to(UP * 6.2)

        subtitle = Text("角 换 元", font=FONT, font_size=34, color=COLOR_JIAO)
        subtitle.move_to(UP * 5.4)

        rule = Text("÷ 10", font=FONT, font_size=28, color=COLOR_JIAO)
        rule.move_to(UP * 4.7)

        # 例1: 70角 = ? 元
        ex1_q_a = Text("70角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex1_q_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex1_q_b = Text("(   )元", font=FONT, font_size=42, color=GRAY_A)
        ex1_q = VGroup(ex1_q_a, ex1_q_eq, ex1_q_b).arrange(RIGHT, buff=0.3)
        ex1_q.move_to(UP * 3.5)

        ex1_hint_a = Text("70", font=FONT, font_size=34, color=COLOR_JIAO)
        ex1_hint_x = Text("÷", font=FONT, font_size=34, color=WHITE)
        ex1_hint_b = Text("10", font=FONT, font_size=34, color=COLOR_JIAO)
        ex1_hint_eq= Text("=", font=FONT, font_size=34, color=WHITE)
        ex1_hint_c = Text("7", font=FONT, font_size=34, color=COLOR_YUAN)
        ex1_hint = VGroup(ex1_hint_a, ex1_hint_x, ex1_hint_b,
                          ex1_hint_eq, ex1_hint_c).arrange(RIGHT, buff=0.2)
        ex1_hint.move_to(UP * 2.5)

        ex1_ans_a = Text("70角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex1_ans_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex1_ans_b = Text("7元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex1_ans = VGroup(ex1_ans_a, ex1_ans_eq, ex1_ans_b).arrange(RIGHT, buff=0.3)
        ex1_ans.move_to(UP * 1.4)

        ex1_check = Text("V", font=FONT, font_size=50, color=COLOR_FEN)
        ex1_check.next_to(ex1_ans, RIGHT, buff=0.3)

        # 例2: 40角 = ? 元
        ex2_q_a = Text("40角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex2_q_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex2_q_b = Text("(   )元", font=FONT, font_size=42, color=GRAY_A)
        ex2_q = VGroup(ex2_q_a, ex2_q_eq, ex2_q_b).arrange(RIGHT, buff=0.3)
        ex2_q.move_to(DOWN * 0.2)

        ex2_ans_a = Text("40角", font=FONT, font_size=42, color=COLOR_JIAO)
        ex2_ans_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        ex2_ans_b = Text("4元", font=FONT, font_size=42, color=COLOR_YUAN)
        ex2_ans = VGroup(ex2_ans_a, ex2_ans_eq, ex2_ans_b).arrange(RIGHT, buff=0.3)
        ex2_ans.move_to(DOWN * 1.2)

        ex2_check = Text("V", font=FONT, font_size=50, color=COLOR_FEN)
        ex2_check.next_to(ex2_ans, RIGHT, buff=0.3)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(subtitle), FadeIn(rule), run_time=0.4)

        self.play(FadeIn(ex1_q, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ex1_hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex1_ans, shift=UP * 0.2), run_time=0.5)
        self.play(Write(ex1_check), run_time=0.3)
        self.wait(0.8)

        self.play(FadeIn(ex2_q, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(ex2_ans, shift=UP * 0.2), run_time=0.5)
        self.play(Write(ex2_check), run_time=0.3)
        self.wait(1.2)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(rule),
                  FadeOut(ex1_q), FadeOut(ex1_hint),
                  FadeOut(ex1_ans), FadeOut(ex1_check),
                  FadeOut(ex2_q), FadeOut(ex2_ans), FadeOut(ex2_check),
                  run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 8 — 总结口诀
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text("进率口诀总结", font=FONT, font_size=44, color=COLOR_HL)
        title.move_to(UP * 6.0)

        # 三行口诀
        r1_a = Text("1元", font=FONT, font_size=42, color=COLOR_YUAN)
        r1_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        r1_b = Text("10角", font=FONT, font_size=42, color=COLOR_JIAO)
        row1 = VGroup(r1_a, r1_eq, r1_b).arrange(RIGHT, buff=0.3)
        row1.move_to(UP * 4.0)

        r2_a = Text("1角", font=FONT, font_size=42, color=COLOR_JIAO)
        r2_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        r2_b = Text("10分", font=FONT, font_size=42, color=COLOR_FEN)
        row2 = VGroup(r2_a, r2_eq, r2_b).arrange(RIGHT, buff=0.3)
        row2.move_to(UP * 2.8)

        r3_a = Text("1元", font=FONT, font_size=42, color=COLOR_YUAN)
        r3_eq= Text("=", font=FONT, font_size=42, color=WHITE)
        r3_b = Text("100分", font=FONT, font_size=42, color=COLOR_FEN)
        row3 = VGroup(r3_a, r3_eq, r3_b).arrange(RIGHT, buff=0.3)
        row3.move_to(UP * 1.6)

        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_A, stroke_width=1.5)
        sep.move_to(UP * 0.8)

        tip_title = Text("换算方法:", font=FONT, font_size=30, color=COLOR_HL)
        tip_title.move_to(UP * 0.1)

        tip1_lbl = Text("大单位到小单位:", font=FONT, font_size=26, color=GRAY_A)
        tip1_val = Text("x 进率", font=FONT, font_size=26, color=COLOR_YUAN)
        tip1 = VGroup(tip1_lbl, tip1_val).arrange(RIGHT, buff=0.3)
        tip1.move_to(DOWN * 0.7)

        tip2_lbl = Text("小单位到大单位:", font=FONT, font_size=26, color=GRAY_A)
        tip2_val = Text("÷ 进率", font=FONT, font_size=26, color=COLOR_JIAO)
        tip2 = VGroup(tip2_lbl, tip2_val).arrange(RIGHT, buff=0.3)
        tip2.move_to(DOWN * 1.5)

        memory_box = RoundedRectangle(corner_radius=0.2, width=7.0, height=1.0,
                                      fill_color="#2a1a2e", fill_opacity=0.8,
                                      stroke_color=COLOR_HL, stroke_width=2)
        memory_box.move_to(DOWN * 3.0)
        memory_txt = Text("进率是10，十进制货币!", font=FONT, font_size=28,
                          color=COLOR_HL)
        memory_txt.move_to(memory_box.get_center())

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(row1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(row2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(row3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(tip_title), run_time=0.3)
        self.play(FadeIn(tip1, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(tip2, shift=UP * 0.2), run_time=0.4)
        self.play(Create(memory_box), Write(memory_txt), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(title), FadeOut(row1), FadeOut(row2), FadeOut(row3),
                  FadeOut(sep), FadeOut(tip_title), FadeOut(tip1), FadeOut(tip2),
                  FadeOut(memory_box), FadeOut(memory_txt), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 9 — 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        big_author = Text("上海初高中数学直通车", font=FONT, font_size=38,
                          color=WHITE)
        big_author.move_to(UP * 2.0)

        author_id = Text("@emptyandcalm", font=FONT, font_size=30,
                         color=COLOR_AUTHOR)
        author_id.move_to(UP * 1.0)

        follow_text = Text("关注我，获得更多数学技巧!", font=FONT, font_size=32,
                           color=COLOR_HL)
        follow_text.move_to(ORIGIN)

        # 三个硬币图标装饰
        deco_yuan  = make_coin("元", COLOR_YUAN, radius=0.5, font_size=24)
        deco_jiao  = make_coin("角", COLOR_JIAO, radius=0.5, font_size=24)
        deco_fen   = make_coin("分", COLOR_FEN,  radius=0.5, font_size=24)
        deco_coins = VGroup(deco_yuan, deco_jiao, deco_fen)
        deco_coins.arrange(RIGHT, buff=0.6)
        deco_coins.move_to(DOWN * 1.8)

        key_eq_a = Text("1元", font=FONT, font_size=34, color=COLOR_YUAN)
        key_eq_b = Text("=", font=FONT, font_size=34, color=WHITE)
        key_eq_c = Text("10角", font=FONT, font_size=34, color=COLOR_JIAO)
        key_eq_d = Text("=", font=FONT, font_size=34, color=WHITE)
        key_eq_e = Text("100分", font=FONT, font_size=34, color=COLOR_FEN)
        key_eq = VGroup(key_eq_a, key_eq_b, key_eq_c,
                        key_eq_d, key_eq_e).arrange(RIGHT, buff=0.2)
        key_eq.move_to(DOWN * 3.2)

        self.play(
            Transform(self.author_bar, big_author),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in deco_coins],
                              lag_ratio=0.2), run_time=0.8)
        self.play(FadeIn(key_eq, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(self.author_bar), FadeOut(author_id),
                  FadeOut(follow_text), FadeOut(deco_coins),
                  FadeOut(key_eq), run_time=0.8)
