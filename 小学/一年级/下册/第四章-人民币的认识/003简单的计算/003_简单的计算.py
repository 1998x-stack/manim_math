"""
人民币的认识 - 简单的计算
一年级下册 第四章
内容：单位相同的加减、单位不同的加减（需要换算）、满十进一
格式：TikTok竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 颜色配置
COLOR_BG = "#1a1a2e"
COLOR_YUAN = "#f39c12"    # 元 - 金色
COLOR_JIAO = "#3498db"   # 角 - 蓝色
COLOR_HIGHLIGHT = YELLOW
COLOR_RESULT = "#e74c3c"  # 结果 - 红色
COLOR_ARROW = "#9b59b6"   # 箭头 - 紫色
COLOR_CARD = "#16213e"    # 卡片背景
COLOR_HINT = "#a0aec0"    # 提示文字


def make_coin(label_text, color, radius=0.55, font_size=28):
    """创建硬币图形"""
    circle = Circle(radius=radius, color=color, fill_color=color,
                    fill_opacity=0.25, stroke_width=3)
    label = Text(label_text, font="Noto Sans CJK SC",
                 font_size=font_size, color=color)
    return VGroup(circle, label)


def make_bill_card(amount_text, unit_text, color, width=1.8, height=1.0):
    """创建纸币卡片"""
    rect = Rectangle(width=width, height=height, color=color,
                     fill_color=COLOR_CARD, fill_opacity=0.9,
                     stroke_width=2.5)
    amount = Text(amount_text, font="Noto Sans CJK SC",
                  font_size=36, color=color)
    unit = Text(unit_text, font="Noto Sans CJK SC",
                font_size=20, color=color)
    label_group = VGroup(amount, unit).arrange(RIGHT, buff=0.08)
    label_group.move_to(rect.get_center())
    return VGroup(rect, label_group)


class SimpleMoneyCalcLesson(Scene):
    """
    简单的人民币计算教学动画

    场景顺序：
    1. 开场钩子
    2. 同单位加法：3角 + 5角 = 8角
    3. 不同单位加法：1元2角 + 5角 = 1元7角（换算步骤）
    4. 满十进一概念
    5. 片尾关注
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        self.scene_1_opening()
        self.scene_2_same_unit()
        self.scene_3_different_unit()
        self.scene_4_carry_concept()
        self.scene_5_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息（固定顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.4)

        # 章节标题
        chapter = Text("人民币的认识", font="Noto Sans CJK SC",
                       font_size=26, color=COLOR_HINT).move_to(UP * 6.0)
        self.play(FadeIn(chapter), run_time=0.4)

        # 大标题
        title = Text("简单的计算", font="Noto Sans CJK SC",
                     font_size=52, color=COLOR_YUAN).move_to(UP * 5.0)
        self.play(Write(title), run_time=0.8)

        # 钩子问题
        hook_line1 = Text("买东西怎么算钱？", font="Noto Sans CJK SC",
                          font_size=34, color=WHITE).move_to(UP * 3.8)
        hook_line2 = Text("元和角怎么相加？", font="Noto Sans CJK SC",
                          font_size=34, color=COLOR_HIGHLIGHT).move_to(UP * 3.1)
        self.play(FadeIn(hook_line1, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 硬币示例
        coin_3 = make_coin("3角", COLOR_JIAO).move_to(LEFT * 2.5 + UP * 1.5)
        plus_sign = Text("+", font="Noto Sans CJK SC",
                         font_size=44, color=WHITE).move_to(UP * 1.5)
        coin_5 = make_coin("5角", COLOR_JIAO).move_to(RIGHT * 2.5 + UP * 1.5)

        self.play(
            GrowFromCenter(coin_3),
            GrowFromCenter(coin_5),
            run_time=0.6
        )
        self.play(FadeIn(plus_sign), run_time=0.3)
        self.wait(0.5)

        # 清除
        self.play(
            FadeOut(title), FadeOut(chapter),
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(coin_3), FadeOut(plus_sign), FadeOut(coin_5),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: 同单位加法 3角 + 5角 = 8角
    # ─────────────────────────────────────────────
    def scene_2_same_unit(self):
        scene_title = Text("单位相同  直接加",
                           font="Noto Sans CJK SC",
                           font_size=34, color=COLOR_JIAO).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.7)

        example_label = Text("例题 1", font="Noto Sans CJK SC",
                              font_size=24, color=COLOR_HINT).move_to(UP * 4.9)
        self.play(FadeIn(example_label), run_time=0.3)

        # 硬币展示区
        coin_y = 3.5

        # 3枚1角硬币
        coins_3 = VGroup(*[
            make_coin("1角", COLOR_JIAO, radius=0.42, font_size=22)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.18).move_to(LEFT * 2.8 + UP * coin_y)

        # 5枚1角硬币
        coins_5 = VGroup(*[
            make_coin("1角", COLOR_JIAO, radius=0.42, font_size=22)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.18).move_to(RIGHT * 1.5 + UP * coin_y)

        label_3 = Text("3角", font="Noto Sans CJK SC",
                       font_size=30, color=COLOR_JIAO).next_to(coins_3, DOWN, buff=0.15)
        label_5 = Text("5角", font="Noto Sans CJK SC",
                       font_size=30, color=COLOR_JIAO).next_to(coins_5, DOWN, buff=0.15)

        self.play(Create(coins_3), run_time=0.7)
        self.play(FadeIn(label_3), run_time=0.3)
        self.play(Create(coins_5), run_time=0.7)
        self.play(FadeIn(label_5), run_time=0.3)
        self.wait(0.4)

        # 计算公式
        eq_y = 1.8

        t_3jiao = Text("3角", font="Noto Sans CJK SC",
                       font_size=44, color=COLOR_JIAO)
        t_plus = Text("+", font="Noto Sans CJK SC",
                      font_size=44, color=WHITE)
        t_5jiao = Text("5角", font="Noto Sans CJK SC",
                       font_size=44, color=COLOR_JIAO)
        t_eq = Text("=", font="Noto Sans CJK SC",
                    font_size=44, color=WHITE)
        t_q = Text("?", font="Noto Sans CJK SC",
                   font_size=44, color=COLOR_HINT)

        formula = VGroup(t_3jiao, t_plus, t_5jiao, t_eq, t_q).arrange(
            RIGHT, buff=0.25).move_to(UP * eq_y)

        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)

        # 提示框
        hint_box = RoundedRectangle(
            width=7.2, height=1.1,
            corner_radius=0.2,
            color=COLOR_JIAO, fill_color="#0a2240",
            fill_opacity=0.85, stroke_width=2
        ).move_to(UP * 0.5)
        hint_text1 = Text("单位相同（都是角）",
                          font="Noto Sans CJK SC",
                          font_size=24, color=COLOR_JIAO)
        hint_text2 = Text("直接把数字相加：3 + 5 = 8",
                          font="Noto Sans CJK SC",
                          font_size=24, color=WHITE)
        hint_group = VGroup(hint_text1, hint_text2).arrange(
            DOWN, buff=0.1).move_to(hint_box.get_center())

        self.play(Create(hint_box), run_time=0.4)
        self.play(Write(hint_group), run_time=0.8)
        self.wait(0.6)

        # 替换 "?" 为 "8角"
        t_8jiao = Text("8角", font="Noto Sans CJK SC",
                       font_size=44, color=COLOR_RESULT)
        t_8jiao.move_to(t_q.get_center())

        self.play(ReplacementTransform(t_q, t_8jiao), run_time=0.6)
        self.play(Flash(t_8jiao, color=COLOR_RESULT,
                        flash_radius=0.6, line_length=0.2), run_time=0.5)
        self.wait(0.4)

        # 结论
        conclusion = Text("3角 + 5角 = 8角", font="Noto Sans CJK SC",
                          font_size=30, color=COLOR_RESULT).move_to(DOWN * 0.8)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(scene_title), FadeOut(example_label),
            FadeOut(coins_3), FadeOut(label_3),
            FadeOut(coins_5), FadeOut(label_5),
            FadeOut(formula), FadeOut(t_8jiao),
            FadeOut(hint_box), FadeOut(hint_group),
            FadeOut(conclusion),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 3: 不同单位加法 1元2角 + 5角 = 1元7角
    # ─────────────────────────────────────────────
    def scene_3_different_unit(self):
        scene_title = Text("单位不同  先换算",
                           font="Noto Sans CJK SC",
                           font_size=34, color=COLOR_YUAN).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.7)

        example_label = Text("例题 2", font="Noto Sans CJK SC",
                              font_size=24, color=COLOR_HINT).move_to(UP * 4.9)
        self.play(FadeIn(example_label), run_time=0.3)

        # 问题展示
        prob_y = 4.0

        t_1y2j = Text("1元2角", font="Noto Sans CJK SC",
                      font_size=42, color=WHITE)
        t_plus = Text("+", font="Noto Sans CJK SC",
                      font_size=42, color=WHITE)
        t_5j = Text("5角", font="Noto Sans CJK SC",
                    font_size=42, color=COLOR_JIAO)
        t_eq = Text("=", font="Noto Sans CJK SC",
                    font_size=42, color=WHITE)
        t_q = Text("?", font="Noto Sans CJK SC",
                   font_size=42, color=COLOR_HINT)

        problem = VGroup(t_1y2j, t_plus, t_5j, t_eq, t_q).arrange(
            RIGHT, buff=0.20).move_to(UP * prob_y)

        self.play(Write(problem), run_time=1.0)
        self.wait(0.5)

        # 钱币展示
        wallet_y = 2.4
        bill_1yuan = make_bill_card("1", "元", COLOR_YUAN, width=1.5, height=0.9)
        bill_1yuan.move_to(LEFT * 3.0 + UP * wallet_y)

        coin_2j = make_coin("2角", COLOR_JIAO, radius=0.40, font_size=22)
        coin_2j.move_to(LEFT * 1.4 + UP * wallet_y)

        coin_5j = make_coin("5角", COLOR_JIAO, radius=0.40, font_size=22)
        coin_5j.move_to(RIGHT * 0.4 + UP * wallet_y)

        plus1 = Text("+", font="Noto Sans CJK SC",
                     font_size=28, color=WHITE).move_to(LEFT * 2.2 + UP * wallet_y)
        plus2 = Text("+", font="Noto Sans CJK SC",
                     font_size=28, color=WHITE).move_to(LEFT * 0.5 + UP * wallet_y)

        self.play(GrowFromCenter(bill_1yuan), run_time=0.5)
        self.play(FadeIn(plus1), GrowFromCenter(coin_2j), run_time=0.4)
        self.play(FadeIn(plus2), GrowFromCenter(coin_5j), run_time=0.4)
        self.wait(0.4)

        # 步骤1：换算单位
        step1_title = Text("第一步：换算单位",
                           font="Noto Sans CJK SC",
                           font_size=26, color=COLOR_YUAN).move_to(UP * 1.3)
        self.play(Write(step1_title), run_time=0.5)

        convert_box = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.2,
            color=COLOR_YUAN, fill_color="#1a0a00",
            fill_opacity=0.85, stroke_width=2
        ).move_to(UP * 0.1)

        conv_line1 = Text("1元 = 10角",
                          font="Noto Sans CJK SC",
                          font_size=26, color=COLOR_YUAN)
        conv_line2 = Text("1元2角 = 10角 + 2角 = 12角",
                          font="Noto Sans CJK SC",
                          font_size=26, color=WHITE)
        conv_group = VGroup(conv_line1, conv_line2).arrange(
            DOWN, buff=0.15).move_to(convert_box.get_center())

        self.play(Create(convert_box), run_time=0.4)
        self.play(Write(conv_line1), run_time=0.6)
        self.play(Write(conv_line2), run_time=0.7)
        self.wait(0.8)

        # 步骤2：角与角相加
        step2_title = Text("第二步：角 + 角",
                           font="Noto Sans CJK SC",
                           font_size=26, color=COLOR_JIAO).move_to(DOWN * 1.4)
        self.play(Write(step2_title), run_time=0.5)

        add_box = RoundedRectangle(
            width=7.5, height=1.5,
            corner_radius=0.2,
            color=COLOR_JIAO, fill_color="#001a30",
            fill_opacity=0.85, stroke_width=2
        ).move_to(DOWN * 2.5)

        add_line1 = Text("12角 + 5角 = 17角",
                         font="Noto Sans CJK SC",
                         font_size=28, color=WHITE)
        add_line2 = Text("（12 + 5 = 17，单位都是角）",
                         font="Noto Sans CJK SC",
                         font_size=22, color=COLOR_HINT)
        add_group = VGroup(add_line1, add_line2).arrange(
            DOWN, buff=0.12).move_to(add_box.get_center())

        self.play(Create(add_box), run_time=0.4)
        self.play(Write(add_line1), run_time=0.6)
        self.play(Write(add_line2), run_time=0.5)
        self.wait(0.8)

        # 步骤3：转回元和角
        step3_box = RoundedRectangle(
            width=7.5, height=1.5,
            corner_radius=0.2,
            color=COLOR_RESULT, fill_color="#1a0010",
            fill_opacity=0.85, stroke_width=2
        ).move_to(DOWN * 4.2)

        step3_line1 = Text("17角 = 10角 + 7角 = 1元7角",
                           font="Noto Sans CJK SC",
                           font_size=26, color=WHITE)
        step3_line2 = Text("（满10角进1元）",
                           font="Noto Sans CJK SC",
                           font_size=22, color=COLOR_RESULT)
        step3_group = VGroup(step3_line1, step3_line2).arrange(
            DOWN, buff=0.12).move_to(step3_box.get_center())

        self.play(Create(step3_box), run_time=0.4)
        self.play(Write(step3_line1), run_time=0.7)
        self.play(Write(step3_line2), run_time=0.5)
        self.wait(0.8)

        # 替换问号为答案
        t_answer = Text("1元7角", font="Noto Sans CJK SC",
                        font_size=42, color=COLOR_RESULT)
        t_answer.move_to(t_q.get_center())
        self.play(ReplacementTransform(t_q, t_answer), run_time=0.6)
        self.play(Flash(t_answer, color=COLOR_RESULT,
                        flash_radius=0.7, line_length=0.2), run_time=0.5)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(scene_title), FadeOut(example_label),
            FadeOut(problem), FadeOut(t_answer),
            FadeOut(bill_1yuan), FadeOut(coin_2j), FadeOut(coin_5j),
            FadeOut(plus1), FadeOut(plus2),
            FadeOut(step1_title), FadeOut(convert_box), FadeOut(conv_group),
            FadeOut(step2_title), FadeOut(add_box), FadeOut(add_group),
            FadeOut(step3_box), FadeOut(step3_group),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 4: 满十进一 概念总结
    # ─────────────────────────────────────────────
    def scene_4_carry_concept(self):
        # 标题
        concept_title = Text("满十进一",
                             font="Noto Sans CJK SC",
                             font_size=50, color=COLOR_YUAN).move_to(UP * 5.8)
        self.play(Write(concept_title), run_time=0.7)

        sub_title = Text("进位规则",
                         font="Noto Sans CJK SC",
                         font_size=28, color=COLOR_HINT).move_to(UP * 5.0)
        self.play(FadeIn(sub_title), run_time=0.4)

        # 10枚1角硬币排列
        coins_y = 3.2
        coins_row = VGroup(*[
            make_coin("1角", COLOR_JIAO, radius=0.36, font_size=17)
            for _ in range(10)
        ]).arrange(RIGHT, buff=0.06).move_to(UP * coins_y)

        label_10jiao = Text("10角", font="Noto Sans CJK SC",
                            font_size=26, color=COLOR_JIAO).next_to(
            coins_row, DOWN, buff=0.15)

        self.play(LaggedStart(
            *[GrowFromCenter(c) for c in coins_row],
            lag_ratio=0.1
        ), run_time=1.2)
        self.play(FadeIn(label_10jiao), run_time=0.3)
        self.wait(0.5)

        # 箭头向下
        arrow_down = Arrow(
            start=UP * 2.1, end=UP * 1.1,
            color=COLOR_ARROW, buff=0.1, stroke_width=6,
            max_tip_length_to_length_ratio=0.25
        )
        arrow_label = Text("换成", font="Noto Sans CJK SC",
                           font_size=24, color=COLOR_ARROW).next_to(
            arrow_down, RIGHT, buff=0.15)

        self.play(GrowArrow(arrow_down), FadeIn(arrow_label), run_time=0.6)

        # 变为1元纸币
        bill_1y = make_bill_card("1", "元", COLOR_YUAN, width=1.8, height=1.0)
        bill_1y.move_to(UP * 0.2)

        self.play(
            FadeOut(coins_row),
            FadeOut(label_10jiao),
            run_time=0.4
        )
        self.play(GrowFromCenter(bill_1y), run_time=0.6)

        rule_text = Text("10角 = 1元",
                         font="Noto Sans CJK SC",
                         font_size=34, color=COLOR_RESULT).move_to(DOWN * 1.0)
        self.play(FadeIn(rule_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 口诀卡
        slogan_box = RoundedRectangle(
            width=7.6, height=2.8,
            corner_radius=0.25,
            color=COLOR_YUAN,
            fill_color="#0d1b2a",
            fill_opacity=0.95,
            stroke_width=2.5
        ).move_to(DOWN * 3.0)

        slogan1 = Text("口诀记住：",
                       font="Noto Sans CJK SC",
                       font_size=26, color=COLOR_HINT)
        slogan2 = Text("单位相同，直接相加",
                       font="Noto Sans CJK SC",
                       font_size=28, color=COLOR_JIAO)
        slogan3 = Text("单位不同，先换算再加",
                       font="Noto Sans CJK SC",
                       font_size=28, color=COLOR_YUAN)
        slogan4 = Text("满 10 角 = 1 元（进一位）",
                       font="Noto Sans CJK SC",
                       font_size=28, color=COLOR_RESULT)

        slogan_group = VGroup(slogan1, slogan2, slogan3, slogan4).arrange(
            DOWN, buff=0.18).move_to(slogan_box.get_center())

        self.play(Create(slogan_box), run_time=0.5)
        self.play(LaggedStart(
            FadeIn(slogan1),
            FadeIn(slogan2),
            FadeIn(slogan3),
            FadeIn(slogan4),
            lag_ratio=0.35
        ), run_time=1.5)
        self.wait(1.8)

        # 清场概念区，转入例题回顾
        self.play(
            FadeOut(concept_title), FadeOut(sub_title),
            FadeOut(arrow_down), FadeOut(arrow_label),
            FadeOut(bill_1y), FadeOut(rule_text),
            FadeOut(slogan_box), FadeOut(slogan_group),
            run_time=0.6
        )

        # 两道例题并排回顾
        ex1_box = RoundedRectangle(
            width=7.8, height=1.8,
            corner_radius=0.2,
            color=COLOR_JIAO,
            fill_color=COLOR_CARD,
            fill_opacity=0.9,
            stroke_width=2
        ).move_to(UP * 2.5)

        ex1_title_t = Text("例 1  同单位",
                           font="Noto Sans CJK SC",
                           font_size=24, color=COLOR_JIAO)
        ex1_formula_t = Text("3角 + 5角 = 8角",
                             font="Noto Sans CJK SC",
                             font_size=30, color=COLOR_RESULT)
        VGroup(ex1_title_t, ex1_formula_t).arrange(
            DOWN, buff=0.15).move_to(ex1_box.get_center())

        ex2_box = RoundedRectangle(
            width=7.8, height=2.5,
            corner_radius=0.2,
            color=COLOR_YUAN,
            fill_color=COLOR_CARD,
            fill_opacity=0.9,
            stroke_width=2
        ).move_to(DOWN * 0.2)

        ex2_title_t = Text("例 2  不同单位",
                           font="Noto Sans CJK SC",
                           font_size=24, color=COLOR_YUAN)
        ex2_step1_t = Text("1元2角 = 12角",
                           font="Noto Sans CJK SC",
                           font_size=24, color=COLOR_HINT)
        ex2_step2_t = Text("12角 + 5角 = 17角",
                           font="Noto Sans CJK SC",
                           font_size=24, color=WHITE)
        ex2_step3_t = Text("17角 = 1元7角",
                           font="Noto Sans CJK SC",
                           font_size=24, color=COLOR_RESULT)
        VGroup(ex2_title_t, ex2_step1_t, ex2_step2_t, ex2_step3_t).arrange(
            DOWN, buff=0.12).move_to(ex2_box.get_center())

        self.play(Create(ex1_box), run_time=0.4)
        self.play(FadeIn(ex1_title_t), FadeIn(ex1_formula_t), run_time=0.6)
        self.wait(0.4)
        self.play(Create(ex2_box), run_time=0.4)
        self.play(FadeIn(ex2_title_t), FadeIn(ex2_step1_t), run_time=0.4)
        self.play(FadeIn(ex2_step2_t), run_time=0.4)
        self.play(FadeIn(ex2_step3_t), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(ex1_box), FadeOut(ex1_title_t), FadeOut(ex1_formula_t),
            FadeOut(ex2_box), FadeOut(ex2_title_t),
            FadeOut(ex2_step1_t), FadeOut(ex2_step2_t), FadeOut(ex2_step3_t),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 5: 片尾关注
    # ─────────────────────────────────────────────
    def scene_5_outro(self):
        author_big = Text("上海初高中数学直通车",
                          font="Noto Sans CJK SC",
                          font_size=36, color=WHITE).move_to(UP * 1.5)
        author_id = Text("@emptyandcalm",
                         font="Noto Sans CJK SC",
                         font_size=28, color=COLOR_HINT).move_to(UP * 0.6)

        follow_text = Text("关注我，学更多数学知识！",
                           font="Noto Sans CJK SC",
                           font_size=30, color=COLOR_HIGHLIGHT).move_to(DOWN * 0.4)

        self.play(Transform(self.author_info, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.5)

        # 硬币装饰
        coins_deco = VGroup(
            make_coin("1元", COLOR_YUAN, radius=0.45, font_size=22).move_to(
                LEFT * 3.0 + DOWN * 2.0),
            make_coin("5角", COLOR_JIAO, radius=0.40, font_size=20).move_to(
                LEFT * 1.5 + DOWN * 2.3),
            make_coin("1角", COLOR_JIAO, radius=0.35, font_size=18).move_to(
                ORIGIN + DOWN * 2.0),
            make_coin("5角", COLOR_JIAO, radius=0.40, font_size=20).move_to(
                RIGHT * 1.5 + DOWN * 2.3),
            make_coin("1元", COLOR_YUAN, radius=0.45, font_size=22).move_to(
                RIGHT * 3.0 + DOWN * 2.0),
        )
        self.play(LaggedStart(
            *[GrowFromCenter(c) for c in coins_deco],
            lag_ratio=0.15
        ), run_time=1.0)

        self.play(
            *[Flash(c, color=COLOR_YUAN, flash_radius=0.5, line_length=0.15)
              for c in coins_deco],
            run_time=0.8
        )

        self.wait(1.5)

        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(coins_deco),
            run_time=1.0
        )


# 运行命令：
# manim -qm 003_简单的计算.py SimpleMoneyCalcLesson
