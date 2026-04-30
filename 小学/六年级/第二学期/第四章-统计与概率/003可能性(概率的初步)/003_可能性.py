"""
003_可能性.py - 可能性(概率的初步) 教学动画

知识点: 从定性描述(可能/一定/不可能)过渡到定量描述(概率)
        P(事件) = 事件发生的结果数 / 总结果数
        概率值在0到1之间
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 抛硬币猜正反，你能猜对几次？
  2. 定性描述: 一定/可能/不可能
  3. 引入概率: 从"可能"到"多大可能" - 量化可能性
  4. 概率公式: P = 有利结果数 / 总结果数
  5. 例1: 抛硬币 P(正) = 1/2
  6. 例2: 掷骰子 P(偶数) = 3/6 = 1/2
  7. 概率的范围: 0 <= P <= 1
  8. 片尾
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
COLOR_PROB = "#3b82f6"       # 蓝色概率
COLOR_CERTAIN = "#22c55e"    # 绿色一定
COLOR_POSSIBLE = "#f59e0b"   # 橙色可能
COLOR_IMPOSSIBLE = "#ef4444" # 红色不可能
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_FORMULA = "#38bdf8"    # 浅蓝公式
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
COLOR_COIN = "#facc15"       # 金色硬币
COLOR_DICE = "#e2e8f0"       # 骰子白色
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class ProbabilityIntroLesson(Scene):
    """
    可能性(概率的初步)教学动画
    场景顺序:
      1. 开场钩子: 抛硬币
      2. 定性描述: 一定/可能/不可能
      3. 从定性到定量: 引入概率概念
      4. 概率公式
      5. 例1: 抛硬币
      6. 例2: 掷骰子
      7. 概率的范围 0~1
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_qualitative()
        self.scene_3_to_quantitative()
        self.scene_4_formula()
        self.scene_5_coin_example()
        self.scene_6_dice_example()
        self.scene_7_probability_range()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子
        hook1 = Text(
            "抛一枚硬币", font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 5.0)
        hook2 = Text(
            "你能猜对几次?", font=FONT, font_size=50,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.8)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 硬币动画 - 金色圆
        coin = Circle(
            radius=1.2, color=COLOR_COIN, fill_opacity=0.9,
            stroke_color=WHITE, stroke_width=3
        ).move_to(UP * 1.0)
        coin_text = Text(
            "正", font=FONT, font_size=60, color="#92400e", weight=BOLD
        ).move_to(coin.get_center())
        coin_group = VGroup(coin, coin_text)

        self.play(FadeIn(coin_group, scale=0.5), run_time=0.8)

        # 硬币翻转效果
        coin_text_back = Text(
            "反", font=FONT, font_size=60, color="#92400e", weight=BOLD
        ).move_to(coin.get_center())

        self.play(
            coin_group.animate.scale(0.1),
            run_time=0.2, rate_func=rush_into
        )
        self.remove(coin_text)
        coin_group_back = VGroup(coin, coin_text_back)
        self.add(coin_group_back)
        self.play(
            coin_group_back.animate.scale(10),
            run_time=0.2, rate_func=rush_from
        )

        self.wait(0.3)
        # 再翻回来
        self.play(
            coin_group_back.animate.scale(0.1),
            run_time=0.2, rate_func=rush_into
        )
        self.remove(coin_text_back)
        coin_group_final = VGroup(coin, coin_text)
        self.add(coin_group_final)
        self.play(
            coin_group_final.animate.scale(10),
            run_time=0.2, rate_func=rush_from
        )

        # 问号
        question = Text(
            "?", font=FONT, font_size=80, color=COLOR_ACCENT
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(question, scale=2), run_time=0.5)
        self.wait(1.0)

        # 引入
        intro = Text(
            "今天我们来学习 -- 可能性", font=FONT, font_size=30, color=WHITE
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(intro, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(coin_group_final), FadeOut(question), FadeOut(intro),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 定性描述 - 一定/可能/不可能
    # ------------------------------------------------------------------
    def scene_2_qualitative(self):
        title = Text(
            "描述可能性的三个词", font=FONT, font_size=36,
            color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 三个类别
        y_start = 3.0
        gap = 3.2

        # --- 一定 ---
        certain_badge = RoundedRectangle(
            width=2.0, height=0.7, corner_radius=0.2,
            color=COLOR_CERTAIN, fill_opacity=0.9
        ).move_to(UP * y_start + LEFT * 2.5)
        certain_label = Text(
            "一定", font=FONT, font_size=28, color=WHITE, weight=BOLD
        ).move_to(certain_badge.get_center())

        certain_example = Text(
            "太阳从东方升起", font=FONT, font_size=22, color=GRAY_A
        ).next_to(certain_badge, RIGHT, buff=0.4)

        self.play(FadeIn(certain_badge), Write(certain_label), run_time=0.5)
        self.play(FadeIn(certain_example, shift=RIGHT * 0.2), run_time=0.5)

        # --- 可能 ---
        possible_badge = RoundedRectangle(
            width=2.0, height=0.7, corner_radius=0.2,
            color=COLOR_POSSIBLE, fill_opacity=0.9
        ).move_to(UP * (y_start - gap) + LEFT * 2.5)
        possible_label = Text(
            "可能", font=FONT, font_size=28, color=WHITE, weight=BOLD
        ).move_to(possible_badge.get_center())

        possible_example = Text(
            "明天可能会下雨", font=FONT, font_size=22, color=GRAY_A
        ).next_to(possible_badge, RIGHT, buff=0.4)

        self.play(FadeIn(possible_badge), Write(possible_label), run_time=0.5)
        self.play(FadeIn(possible_example, shift=RIGHT * 0.2), run_time=0.5)

        # --- 不可能 ---
        impossible_badge = RoundedRectangle(
            width=2.4, height=0.7, corner_radius=0.2,
            color=COLOR_IMPOSSIBLE, fill_opacity=0.9
        ).move_to(UP * (y_start - 2 * gap) + LEFT * 2.3)
        impossible_label = Text(
            "不可能", font=FONT, font_size=28, color=WHITE, weight=BOLD
        ).move_to(impossible_badge.get_center())

        impossible_example = Text(
            "人能飞上月球(不借助工具)", font=FONT, font_size=20, color=GRAY_A
        ).next_to(impossible_badge, RIGHT, buff=0.4)

        self.play(FadeIn(impossible_badge), Write(impossible_label), run_time=0.5)
        self.play(FadeIn(impossible_example, shift=RIGHT * 0.2), run_time=0.5)

        self.wait(1.5)

        # 问题引导
        question = Text(
            "但是'可能'到底有多大?", font=FONT, font_size=30,
            color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(certain_badge), FadeOut(certain_label), FadeOut(certain_example),
            FadeOut(possible_badge), FadeOut(possible_label), FadeOut(possible_example),
            FadeOut(impossible_badge), FadeOut(impossible_label), FadeOut(impossible_example),
            FadeOut(question),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 从定性到定量
    # ------------------------------------------------------------------
    def scene_3_to_quantitative(self):
        title = Text(
            "用数字衡量可能性", font=FONT, font_size=36,
            color=COLOR_PROB
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 概率的概念
        concept1 = Text(
            "可能性可以用一个数来表示", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        concept2 = Text(
            "这个数就叫做", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.2)
        prob_word = Text(
            "概率", font=FONT, font_size=56, color=COLOR_PROB, weight=BOLD
        ).move_to(UP * 2.0)

        self.play(FadeIn(concept1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(concept2, shift=UP * 0.2), run_time=0.5)
        self.play(
            FadeIn(prob_word, scale=0.5), run_time=0.6
        )
        self.play(
            Flash(prob_word, color=COLOR_PROB, flash_radius=0.8, num_lines=12),
            run_time=0.5
        )

        # 数轴展示
        number_line = NumberLine(
            x_range=[0, 1, 0.5],
            length=7,
            color=WHITE,
            include_numbers=False,
            include_tip=True
        ).move_to(DOWN * 0.5)

        # 手动添加数字标签
        label_0 = MathTex("0", font_size=28, color=WHITE).next_to(
            number_line.n2p(0), DOWN, buff=0.3
        )
        label_half = MathTex(r"\frac{1}{2}", font_size=28, color=WHITE).next_to(
            number_line.n2p(0.5), DOWN, buff=0.3
        )
        label_1 = MathTex("1", font_size=28, color=WHITE).next_to(
            number_line.n2p(1), DOWN, buff=0.3
        )

        self.play(Create(number_line), run_time=0.8)
        self.play(FadeIn(label_0), FadeIn(label_half), FadeIn(label_1), run_time=0.5)

        # 三个区域标注
        imp_text = Text(
            "不可能", font=FONT, font_size=20, color=COLOR_IMPOSSIBLE
        ).next_to(number_line.n2p(0), UP, buff=0.5)
        cert_text = Text(
            "一定", font=FONT, font_size=20, color=COLOR_CERTAIN
        ).next_to(number_line.n2p(1), UP, buff=0.5)

        imp_dot = Dot(number_line.n2p(0), color=COLOR_IMPOSSIBLE, radius=0.12)
        cert_dot = Dot(number_line.n2p(1), color=COLOR_CERTAIN, radius=0.12)

        self.play(
            FadeIn(imp_dot), FadeIn(imp_text),
            FadeIn(cert_dot), FadeIn(cert_text),
            run_time=0.6
        )

        # 可能 区间
        brace = Brace(
            Line(number_line.n2p(0.05), number_line.n2p(0.95)),
            direction=DOWN, buff=0.6, color=COLOR_POSSIBLE
        )
        brace_text = Text(
            "可能(概率越大越可能)", font=FONT, font_size=18, color=COLOR_POSSIBLE
        ).next_to(brace, DOWN, buff=0.15)

        self.play(FadeIn(brace), FadeIn(brace_text), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(concept1), FadeOut(concept2), FadeOut(prob_word),
            FadeOut(number_line), FadeOut(label_0), FadeOut(label_half), FadeOut(label_1),
            FadeOut(imp_text), FadeOut(cert_text), FadeOut(imp_dot), FadeOut(cert_dot),
            FadeOut(brace), FadeOut(brace_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 概率公式
    # ------------------------------------------------------------------
    def scene_4_formula(self):
        title = Text(
            "概率公式", font=FONT, font_size=38, color=COLOR_FORMULA
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.5, height=2.5, corner_radius=0.3,
            color=COLOR_FORMULA, fill_opacity=0.08,
            stroke_width=2
        ).move_to(UP * 2.5)

        # 分两行展示: 中文说明 + 公式
        line1_cn = Text(
            "P(事件) =", font=FONT, font_size=30, color=WHITE
        )
        line1_frac = MathTex(
            r"\frac{\text{favorable outcomes}}{\text{total outcomes}}",
            font_size=36, color=COLOR_FORMULA
        )
        # Actually use Chinese text separately
        line1_cn2 = Text(
            "事件发生的结果数", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 2.9)

        frac_line = Line(
            LEFT * 2.2, RIGHT * 2.2, color=WHITE, stroke_width=2
        ).move_to(UP * 2.4)

        line1_cn3 = Text(
            "所有可能的结果总数", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 1.9)

        p_label = MathTex(
            r"P = ", font_size=40, color=WHITE
        ).move_to(UP * 2.4 + LEFT * 3.0)

        self.play(FadeIn(formula_box), run_time=0.4)
        self.play(Write(p_label), run_time=0.4)
        self.play(
            FadeIn(line1_cn2, shift=DOWN * 0.2),
            Create(frac_line),
            run_time=0.6
        )
        self.play(FadeIn(line1_cn3, shift=UP * 0.2), run_time=0.5)

        self.wait(1.5)

        # 关键性质
        prop1 = VGroup(
            Text("P = 0", font=FONT, font_size=24, color=COLOR_IMPOSSIBLE),
            Text("  :  不可能事件", font=FONT, font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)

        prop2 = VGroup(
            Text("P = 1", font=FONT, font_size=24, color=COLOR_CERTAIN),
            Text("  :  必然事件", font=FONT, font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5)

        prop3 = VGroup(
            MathTex(r"0 \leq P \leq 1", font_size=30, color=COLOR_HL),
            Text("  :  概率在0和1之间", font=FONT, font_size=20, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)

        self.play(FadeIn(prop1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(prop2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(prop3, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula_box),
            FadeOut(p_label), FadeOut(line1_cn2), FadeOut(frac_line), FadeOut(line1_cn3),
            FadeOut(prop1), FadeOut(prop2), FadeOut(prop3),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 例1 - 抛硬币
    # ------------------------------------------------------------------
    def scene_5_coin_example(self):
        title = VGroup(
            Text("例1", font=FONT, font_size=32, color=COLOR_HL),
            Text("  抛硬币", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 问题
        question = Text(
            "抛一枚硬币，正面朝上的概率?",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.3)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)

        # 硬币展示 - 正面和反面
        coin_front = Circle(
            radius=0.9, color=COLOR_COIN, fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=2
        ).move_to(UP * 2.0 + LEFT * 1.8)
        coin_front_text = Text(
            "正", font=FONT, font_size=40, color="#92400e", weight=BOLD
        ).move_to(coin_front.get_center())
        front_group = VGroup(coin_front, coin_front_text)

        coin_back = Circle(
            radius=0.9, color="#94a3b8", fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=2
        ).move_to(UP * 2.0 + RIGHT * 1.8)
        coin_back_text = Text(
            "反", font=FONT, font_size=40, color="#334155", weight=BOLD
        ).move_to(coin_back.get_center())
        back_group = VGroup(coin_back, coin_back_text)

        self.play(
            FadeIn(front_group, scale=0.5),
            FadeIn(back_group, scale=0.5),
            run_time=0.6
        )

        # 分析
        total_label = Text(
            "总共 2 种结果", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(total_label, shift=UP * 0.2), run_time=0.5)

        favor_label = Text(
            "正面朝上: 1 种", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(favor_label, shift=UP * 0.2), run_time=0.5)

        # 高亮正面硬币
        highlight_ring = Circle(
            radius=1.05, color=COLOR_HL, stroke_width=4
        ).move_to(coin_front.get_center())
        self.play(Create(highlight_ring), run_time=0.4)

        # 计算
        step1_p = MathTex(r"P(", font_size=36, color=WHITE).move_to(DOWN * 2.5 + LEFT * 2.8)
        step1_cn = Text("正面", font=FONT, font_size=22, color=COLOR_HL).next_to(step1_p, RIGHT, buff=0.05)
        step1_eq = MathTex(r") = \frac{1}{2}", font_size=36, color=COLOR_FORMULA).next_to(step1_cn, RIGHT, buff=0.05)

        step1_group = VGroup(step1_p, step1_cn, step1_eq)

        self.play(FadeIn(step1_group, shift=UP * 0.2), run_time=0.7)

        # 结果强调
        result_box = RoundedRectangle(
            width=5.0, height=1.0, corner_radius=0.2,
            color=COLOR_PROB, fill_opacity=0.15, stroke_width=2
        ).move_to(DOWN * 4.5)
        result_text_parts = VGroup(
            Text("正面朝上的概率是 ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"\frac{1}{2}", font_size=36, color=COLOR_PROB),
        ).arrange(RIGHT, buff=0.1).move_to(result_box.get_center())

        self.play(
            FadeIn(result_box), FadeIn(result_text_parts),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(front_group), FadeOut(back_group),
            FadeOut(total_label), FadeOut(favor_label), FadeOut(highlight_ring),
            FadeOut(step1_group),
            FadeOut(result_box), FadeOut(result_text_parts),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 例2 - 掷骰子
    # ------------------------------------------------------------------
    def scene_6_dice_example(self):
        title = VGroup(
            Text("例2", font=FONT, font_size=32, color=COLOR_HL),
            Text("  掷骰子", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        question = Text(
            "掷一个骰子，点数为偶数的概率?",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.3)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)

        # 6个骰子面
        dice_faces = VGroup()
        face_colors = [GRAY_A] * 6
        face_positions = [
            UP * 2.5 + LEFT * 2.5,
            UP * 2.5 + ORIGIN,
            UP * 2.5 + RIGHT * 2.5,
            UP * 0.5 + LEFT * 2.5,
            UP * 0.5 + ORIGIN,
            UP * 0.5 + RIGHT * 2.5,
        ]

        for i in range(6):
            face_sq = RoundedRectangle(
                width=1.5, height=1.5, corner_radius=0.15,
                color=COLOR_DICE, fill_opacity=0.12,
                stroke_width=2
            ).move_to(face_positions[i])
            face_num = MathTex(
                str(i + 1), font_size=48, color=WHITE
            ).move_to(face_sq.get_center())
            face_group = VGroup(face_sq, face_num)
            dice_faces.add(face_group)

        self.play(
            *[FadeIn(f, scale=0.7) for f in dice_faces],
            run_time=0.8
        )

        # 标注总数
        total_label = Text(
            "总共 6 种结果", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(total_label, shift=UP * 0.2), run_time=0.4)

        # 高亮偶数 (2, 4, 6) - 索引 1, 3, 5
        even_indices = [1, 3, 5]
        highlight_rings = VGroup()
        for idx in even_indices:
            ring = RoundedRectangle(
                width=1.7, height=1.7, corner_radius=0.15,
                color=COLOR_HL, stroke_width=4
            ).move_to(face_positions[idx])
            highlight_rings.add(ring)

        favor_label = Text(
            "偶数: 2, 4, 6 共 3 种", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.0)

        self.play(
            *[Create(r) for r in highlight_rings],
            FadeIn(favor_label, shift=UP * 0.2),
            run_time=0.7
        )

        # 计算
        step1_p = MathTex(r"P(", font_size=34, color=WHITE).move_to(DOWN * 3.5 + LEFT * 3.0)
        step1_cn = Text("偶数", font=FONT, font_size=20, color=COLOR_HL).next_to(step1_p, RIGHT, buff=0.05)
        step1_close = MathTex(r") = \frac{3}{6} = \frac{1}{2}", font_size=34, color=COLOR_FORMULA).next_to(step1_cn, RIGHT, buff=0.05)

        step1_group = VGroup(step1_p, step1_cn, step1_close)
        self.play(FadeIn(step1_group, shift=UP * 0.2), run_time=0.7)

        # 结果
        result_box = RoundedRectangle(
            width=6.0, height=1.0, corner_radius=0.2,
            color=COLOR_PROB, fill_opacity=0.15, stroke_width=2
        ).move_to(DOWN * 5.5)
        result_parts = VGroup(
            Text("偶数的概率也是 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\frac{1}{2}", font_size=34, color=COLOR_PROB),
            Text(" !", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(result_box.get_center())

        self.play(FadeIn(result_box), FadeIn(result_parts), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(dice_faces), FadeOut(total_label),
            FadeOut(highlight_rings), FadeOut(favor_label),
            FadeOut(step1_group),
            FadeOut(result_box), FadeOut(result_parts),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 概率的范围 0 <= P <= 1
    # ------------------------------------------------------------------
    def scene_7_probability_range(self):
        title = Text(
            "概率的范围", font=FONT, font_size=38, color=COLOR_ACCENT
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        number_line = NumberLine(
            x_range=[0, 1, 0.25],
            length=7,
            color=WHITE,
            include_numbers=False,
            include_tip=False,
            tick_size=0.15
        ).move_to(UP * 3.0)

        # 刻度标签
        tick_labels = VGroup()
        for val in [0, 0.25, 0.5, 0.75, 1]:
            if val == 0.5:
                lab = MathTex(r"\frac{1}{2}", font_size=22, color=WHITE)
            elif val == 0.25:
                lab = MathTex(r"\frac{1}{4}", font_size=22, color=WHITE)
            elif val == 0.75:
                lab = MathTex(r"\frac{3}{4}", font_size=22, color=WHITE)
            else:
                lab = MathTex(str(int(val)), font_size=24, color=WHITE)
            lab.next_to(number_line.n2p(val), DOWN, buff=0.25)
            tick_labels.add(lab)

        self.play(Create(number_line), run_time=0.7)
        self.play(FadeIn(tick_labels), run_time=0.4)

        # P=0 不可能
        dot0 = Dot(number_line.n2p(0), color=COLOR_IMPOSSIBLE, radius=0.15)
        label0 = Text(
            "不可能", font=FONT, font_size=20, color=COLOR_IMPOSSIBLE
        ).next_to(dot0, UP, buff=0.4)
        example0 = Text(
            "掷骰子得7", font=FONT, font_size=16, color=GRAY_B
        ).next_to(label0, UP, buff=0.15)

        self.play(FadeIn(dot0, scale=0.5), FadeIn(label0), FadeIn(example0), run_time=0.6)

        # P=1 一定
        dot1 = Dot(number_line.n2p(1), color=COLOR_CERTAIN, radius=0.15)
        label1 = Text(
            "一定发生", font=FONT, font_size=20, color=COLOR_CERTAIN
        ).next_to(dot1, UP, buff=0.4)
        example1 = Text(
            "掷骰子得1~6", font=FONT, font_size=16, color=GRAY_B
        ).next_to(label1, UP, buff=0.15)

        self.play(FadeIn(dot1, scale=0.5), FadeIn(label1), FadeIn(example1), run_time=0.6)

        # P=1/2 抛硬币
        dot_half = Dot(number_line.n2p(0.5), color=COLOR_PROB, radius=0.15)
        label_half = Text(
            "抛硬币正面", font=FONT, font_size=18, color=COLOR_PROB
        ).next_to(dot_half, UP, buff=0.4)

        self.play(FadeIn(dot_half, scale=0.5), FadeIn(label_half), run_time=0.5)

        # P=1/6 掷骰子某个点
        dot_sixth = Dot(number_line.n2p(1/6), color=COLOR_POSSIBLE, radius=0.12)
        label_sixth = VGroup(
            Text("掷骰子", font=FONT, font_size=16, color=COLOR_POSSIBLE),
            Text("得1", font=FONT, font_size=16, color=COLOR_POSSIBLE),
        ).arrange(DOWN, buff=0.05).next_to(dot_sixth, DOWN, buff=0.6)

        self.play(FadeIn(dot_sixth, scale=0.5), FadeIn(label_sixth), run_time=0.5)

        self.wait(1.0)

        # 总结公式框
        summary_box = RoundedRectangle(
            width=7.0, height=2.8, corner_radius=0.3,
            color=COLOR_ACCENT, fill_opacity=0.08, stroke_width=2
        ).move_to(DOWN * 2.0)

        sum_title = Text(
            "概率总结", font=FONT, font_size=30, color=COLOR_ACCENT, weight=BOLD
        ).move_to(DOWN * 0.8)

        sum_line1 = VGroup(
            MathTex(r"P = \frac{\text{favorable}}{\text{total}}", font_size=28, color=WHITE),
        ).move_to(DOWN * 1.6)
        # Replace with readable version
        sum_line1_cn = VGroup(
            Text("P =", font=FONT, font_size=24, color=WHITE),
            Text(" 有利结果数 / 总结果数", font=FONT, font_size=22, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.6)

        sum_line2 = MathTex(
            r"0 \leq P \leq 1", font_size=34, color=COLOR_HL
        ).move_to(DOWN * 2.5)

        sum_line3 = VGroup(
            Text("P=0 不可能", font=FONT, font_size=18, color=COLOR_IMPOSSIBLE),
            Text("   ", font=FONT, font_size=18),
            Text("P=1 一定", font=FONT, font_size=18, color=COLOR_CERTAIN),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 3.3)

        self.play(FadeIn(summary_box), run_time=0.3)
        self.play(Write(sum_title), run_time=0.4)
        self.play(FadeIn(sum_line1_cn), run_time=0.5)
        self.play(Write(sum_line2), run_time=0.5)
        self.play(FadeIn(sum_line3), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(number_line), FadeOut(tick_labels),
            FadeOut(dot0), FadeOut(label0), FadeOut(example0),
            FadeOut(dot1), FadeOut(label1), FadeOut(example1),
            FadeOut(dot_half), FadeOut(label_half),
            FadeOut(dot_sixth), FadeOut(label_sixth),
            FadeOut(summary_box), FadeOut(sum_title),
            FadeOut(sum_line1_cn), FadeOut(sum_line2), FadeOut(sum_line3),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------
    def scene_8_outro(self):
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm", font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 小装饰 - 骰子图标
        icons = VGroup()
        for i in range(5):
            angle = i * TAU / 5
            dot_icon = Circle(
                radius=0.25, color=COLOR_PROB, fill_opacity=0.7, stroke_width=0
            ).move_to(
                DOWN * 3.5 + np.array([np.cos(angle) * 2.0, np.sin(angle) * 0.6, 0])
            )
            icons.add(dot_icon)

        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql 003_可能性.py ProbabilityIntroLesson  # 快速预览
# manim -qm 003_可能性.py ProbabilityIntroLesson   # 中等质量
# manim -qh 003_可能性.py ProbabilityIntroLesson    # 高质量
