"""
001_因数和倍数.py — 因数和倍数 教学动画

知识点:
  1. 在整数除法中, 如果商是整数且余数为0,
     则称被除数是除数和商的倍数, 除数和商是被除数的因数
  2. 例: 12÷3=4, 12是3和4的倍数, 3和4是12的因数
  3. 因数的特性: 个数有限, 最小因数是1, 最大因数是它本身
  4. 倍数的特性: 个数无限, 最小倍数是它本身, 没有最大倍数
  5. 求12的因数: 1,2,3,4,6,12
  6. 求3的倍数: 3,6,9,12,15,...

年级: 五年级第二学期
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
COLOR_FACTOR = "#3b82f6"      # 蓝色 — 因数
COLOR_MULTIPLE = "#22c55e"    # 绿色 — 倍数
COLOR_DIVIDEND = "#f97316"    # 橙色 — 被除数
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_PAIR = "#a78bfa"        # 紫色 — 因数对
COLOR_ARROW = "#ef4444"       # 红色箭头
COLOR_BOX = "#0f172a"         # 深色框背景
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class FactorMultipleLesson(Scene):
    """
    因数和倍数教学动画
    Scene 1: 开场钩子
    Scene 2: 核心概念 — 12÷3=4 引出因数与倍数定义
    Scene 3: 求12的所有因数 (因数对方法)
    Scene 4: 求3的倍数 (无限延伸)
    Scene 5: 总结框 — 因数与倍数的特性对比
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_find_factors()
        self.scene_4_find_multiples()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '12 和 3 之间有什么特殊关系？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "12 和 3 之间", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "有什么特殊关系？", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 两个圆形数字
        c12 = Circle(radius=1.0, color=COLOR_DIVIDEND, fill_opacity=0.2, stroke_width=4)
        t12 = Text("12", font=FONT, font_size=72, color=COLOR_DIVIDEND, weight=BOLD)
        g12 = VGroup(c12, t12).move_to(LEFT * 2.0 + UP * 1.0)

        c3 = Circle(radius=0.8, color=COLOR_FACTOR, fill_opacity=0.2, stroke_width=4)
        t3 = Text("3", font=FONT, font_size=64, color=COLOR_FACTOR, weight=BOLD)
        g3 = VGroup(c3, t3).move_to(RIGHT * 2.0 + UP * 1.0)

        self.play(GrowFromCenter(g12), run_time=0.7)
        self.play(GrowFromCenter(g3), run_time=0.6)

        # 问号
        q = Text("?", font=FONT, font_size=80, color=COLOR_HL, weight=BOLD)
        q.move_to(UP * 1.0)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(1.0)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, g12, g3, q)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 核心概念 — 12÷3=4
    # ------------------------------------------------------------------

    def scene_2_concept(self):
        """通过 12÷3=4 引出因数和倍数的定义"""

        title = Text(
            "因数和倍数", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 除法算式
        div_eq = MathTex(
            r"12", r"\div", r"3", r"=", r"4",
            font_size=64
        ).move_to(UP * 3.5)
        div_eq[0].set_color(COLOR_DIVIDEND)   # 12
        div_eq[2].set_color(COLOR_FACTOR)     # 3
        div_eq[4].set_color(COLOR_FACTOR)     # 4
        self.play(Write(div_eq), run_time=1.0)
        self.wait(0.5)

        # 条件说明
        cond = Text(
            "商是整数，余数为 0", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 2.5)
        self.play(FadeIn(cond, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # ===== 倍数关系 =====
        mult_label = Text(
            "倍数关系", font=FONT, font_size=30,
            color=COLOR_MULTIPLE, weight=BOLD
        ).move_to(UP * 1.3)
        self.play(Write(mult_label), run_time=0.4)

        mult_line1 = VGroup(
            MathTex("12", font_size=40, color=COLOR_DIVIDEND),
            Text(" 是 ", font=FONT, font_size=28, color=WHITE),
            MathTex("3", font_size=40, color=COLOR_FACTOR),
            Text(" 的倍数", font=FONT, font_size=28, color=COLOR_MULTIPLE),
        ).arrange(RIGHT, buff=0.08).move_to(UP * 0.5)

        mult_line2 = VGroup(
            MathTex("12", font_size=40, color=COLOR_DIVIDEND),
            Text(" 是 ", font=FONT, font_size=28, color=WHITE),
            MathTex("4", font_size=40, color=COLOR_FACTOR),
            Text(" 的倍数", font=FONT, font_size=28, color=COLOR_MULTIPLE),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 0.2)

        self.play(FadeIn(mult_line1, shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(mult_line2, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.5)

        # ===== 因数关系 =====
        fact_label = Text(
            "因数关系", font=FONT, font_size=30,
            color=COLOR_FACTOR, weight=BOLD
        ).move_to(DOWN * 1.3)
        self.play(Write(fact_label), run_time=0.4)

        fact_line1 = VGroup(
            MathTex("3", font_size=40, color=COLOR_FACTOR),
            Text(" 是 ", font=FONT, font_size=28, color=WHITE),
            MathTex("12", font_size=40, color=COLOR_DIVIDEND),
            Text(" 的因数", font=FONT, font_size=28, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 2.1)

        fact_line2 = VGroup(
            MathTex("4", font_size=40, color=COLOR_FACTOR),
            Text(" 是 ", font=FONT, font_size=28, color=WHITE),
            MathTex("12", font_size=40, color=COLOR_DIVIDEND),
            Text(" 的因数", font=FONT, font_size=28, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 2.8)

        self.play(FadeIn(fact_line1, shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(fact_line2, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.5)

        # 重要提醒
        note_box = RoundedRectangle(
            width=7.5, height=1.2, corner_radius=0.2,
            fill_color=COLOR_BOX, fill_opacity=0.9,
            stroke_color=COLOR_ARROW, stroke_width=2
        ).move_to(DOWN * 4.5)
        note_text = Text(
            "因数和倍数是相互依存的关系",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 4.3)
        note_sub = Text(
            "不能单独说谁是因数或谁是倍数",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.9)

        self.play(FadeIn(note_box), run_time=0.3)
        self.play(Write(note_text), run_time=0.6)
        self.play(FadeIn(note_sub, shift=UP * 0.15), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, div_eq, cond,
                mult_label, mult_line1, mult_line2,
                fact_label, fact_line1, fact_line2,
                note_box, note_text, note_sub
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 求12的所有因数 (因数对方法)
    # ------------------------------------------------------------------

    def scene_3_find_factors(self):
        """用一一配对法找出12的所有因数"""

        title = Text(
            "求12的所有因数", font=FONT, font_size=40,
            color=COLOR_FACTOR, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 方法说明
        method = Text(
            "用乘法一一配对", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(Write(method), run_time=0.5)

        # 因数对列表
        pairs = [
            (1, 12, r"1 \times 12 = 12"),
            (2, 6,  r"2 \times 6 = 12"),
            (3, 4,  r"3 \times 4 = 12"),
        ]

        pair_mobs = VGroup()
        y_start = 3.2
        for i, (a, b, tex) in enumerate(pairs):
            eq = MathTex(tex, font_size=40, color=WHITE).move_to(UP * (y_start - i * 1.2))

            # 高亮因数对标记
            left_circle = Circle(
                radius=0.35, color=COLOR_PAIR,
                fill_opacity=0.15, stroke_width=2.5
            ).move_to(eq[0][0].get_center())
            right_circle = Circle(
                radius=0.35, color=COLOR_PAIR,
                fill_opacity=0.15, stroke_width=2.5
            )
            # 找到第二个因数的位置
            if a == 1:
                right_circle.move_to(eq[0][2:4].get_center())
            elif a == 2:
                right_circle.move_to(eq[0][2].get_center())
            else:
                right_circle.move_to(eq[0][2].get_center())

            pair_group = VGroup(eq, left_circle, right_circle)
            pair_mobs.add(pair_group)

            self.play(Write(eq), run_time=0.7)
            self.play(
                Create(left_circle), Create(right_circle),
                run_time=0.4
            )
            self.wait(0.3)

        # 箭头指向因数集合
        arrow = Arrow(
            UP * 0.2, DOWN * 0.5,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(Create(arrow), run_time=0.3)

        # 因数集合 — 大框
        result_box = RoundedRectangle(
            width=7.8, height=2.2,
            corner_radius=0.25,
            fill_color=COLOR_BOX, fill_opacity=0.95,
            stroke_color=COLOR_FACTOR, stroke_width=3
        ).move_to(DOWN * 2.0)

        result_title = Text(
            "12的因数", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 1.15)

        factors_tex = MathTex(
            r"1,\ 2,\ 3,\ 4,\ 6,\ 12",
            font_size=48, color=COLOR_FACTOR
        ).move_to(DOWN * 2.1)

        count_text = Text(
            "共 6 个因数", font=FONT, font_size=22, color=COLOR_PAIR
        ).move_to(DOWN * 2.85)

        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result_title), run_time=0.4)
        self.play(Write(factors_tex), run_time=0.8)
        self.play(FadeIn(count_text, shift=UP * 0.15), run_time=0.4)
        self.wait(0.5)

        # 因数特性小结
        prop_title = Text(
            "因数的特性", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.0)

        prop1 = VGroup(
            Text("  个数有限", font=FONT, font_size=24, color=WHITE),
        ).move_to(DOWN * 4.7)
        prop2 = VGroup(
            Text("  最小因数是 ", font=FONT, font_size=24, color=WHITE),
            MathTex("1", font_size=32, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.04).move_to(DOWN * 5.3)
        prop3 = VGroup(
            Text("  最大因数是", font=FONT, font_size=24, color=WHITE),
            Text("它本身", font=FONT, font_size=24, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 5.9)

        self.play(Write(prop_title), run_time=0.4)
        self.play(FadeIn(prop1, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(prop2, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(prop3, shift=LEFT * 0.2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, method, pair_mobs, arrow,
                result_box, result_title, factors_tex, count_text,
                prop_title, prop1, prop2, prop3
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 求3的倍数 (无限延伸)
    # ------------------------------------------------------------------

    def scene_4_find_multiples(self):
        """展示3的倍数: 3,6,9,12,15,... 强调无限性"""

        title = Text(
            "求3的倍数", font=FONT, font_size=40,
            color=COLOR_MULTIPLE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        method = Text(
            "用乘法依次求出", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(Write(method), run_time=0.5)

        # 逐个显示 3×1, 3×2, 3×3, ...
        mult_data = [
            (1, 3,  r"3 \times 1 = 3"),
            (2, 6,  r"3 \times 2 = 6"),
            (3, 9,  r"3 \times 3 = 9"),
            (4, 12, r"3 \times 4 = 12"),
            (5, 15, r"3 \times 5 = 15"),
        ]

        eq_mobs = VGroup()
        result_circles = VGroup()
        y_start = 3.5
        for i, (n, val, tex) in enumerate(mult_data):
            eq = MathTex(tex, font_size=36, color=WHITE)
            eq.move_to(LEFT * 1.0 + UP * (y_start - i * 0.9))

            # 倍数结果圆圈
            rc = Circle(
                radius=0.4, color=COLOR_MULTIPLE,
                fill_opacity=0.2, stroke_width=2.5
            )
            rv = Text(
                str(val), font=FONT, font_size=28,
                color=COLOR_MULTIPLE, weight=BOLD
            )
            rg = VGroup(rc, rv).move_to(RIGHT * 2.8 + UP * (y_start - i * 0.9))

            eq_mobs.add(eq)
            result_circles.add(rg)

            self.play(Write(eq), run_time=0.5)
            self.play(GrowFromCenter(rg), run_time=0.3)

        # 省略号 — 无限延伸
        dots = MathTex(r"\cdots", font_size=52, color=COLOR_MULTIPLE)
        dots.move_to(LEFT * 1.0 + UP * (y_start - 5 * 0.9))
        dots_r = MathTex(r"\cdots", font_size=52, color=COLOR_MULTIPLE)
        dots_r.move_to(RIGHT * 2.8 + UP * (y_start - 5 * 0.9))

        self.play(FadeIn(dots, scale=0.5), FadeIn(dots_r, scale=0.5), run_time=0.5)
        self.wait(0.5)

        # 倍数集合框
        result_box = RoundedRectangle(
            width=7.8, height=1.8,
            corner_radius=0.25,
            fill_color=COLOR_BOX, fill_opacity=0.95,
            stroke_color=COLOR_MULTIPLE, stroke_width=3
        ).move_to(DOWN * 2.8)

        result_title = Text(
            "3的倍数", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 2.1)

        multiples_tex = MathTex(
            r"3,\ 6,\ 9,\ 12,\ 15,\ \cdots",
            font_size=44, color=COLOR_MULTIPLE
        ).move_to(DOWN * 2.9)

        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result_title), run_time=0.4)
        self.play(Write(multiples_tex), run_time=0.8)
        self.wait(0.5)

        # 倍数特性小结
        prop_title = Text(
            "倍数的特性", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.3)

        prop1 = Text(
            "  个数无限", font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 5.0)
        prop2 = VGroup(
            Text("  最小倍数是", font=FONT, font_size=24, color=WHITE),
            Text("它本身", font=FONT, font_size=24, color=COLOR_MULTIPLE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 5.6)
        prop3 = Text(
            "  没有最大倍数", font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 6.2)

        self.play(Write(prop_title), run_time=0.4)
        self.play(FadeIn(prop1, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(prop2, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(prop3, shift=LEFT * 0.2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, method, eq_mobs, result_circles,
                dots, dots_r,
                result_box, result_title, multiples_tex,
                prop_title, prop1, prop2, prop3
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结 — 因数与倍数对比
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        """对比总结因数和倍数的关键特性"""

        title = Text(
            "总结对比", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 因数总结框 =====
        f_box = RoundedRectangle(
            width=7.6, height=3.8,
            corner_radius=0.25,
            fill_color=COLOR_BOX, fill_opacity=0.95,
            stroke_color=COLOR_FACTOR, stroke_width=3
        ).move_to(UP * 2.5)

        f_title = Text(
            "因数", font=FONT, font_size=36,
            color=COLOR_FACTOR, weight=BOLD
        ).move_to(UP * 4.0)

        f1 = VGroup(
            Text("个数: ", font=FONT, font_size=24, color=GRAY_A),
            Text("有限", font=FONT, font_size=26, color=WHITE, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(UP * 3.2)
        f2 = VGroup(
            Text("最小因数: ", font=FONT, font_size=24, color=GRAY_A),
            MathTex("1", font_size=36, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.06).move_to(UP * 2.5)
        f3 = VGroup(
            Text("最大因数: ", font=FONT, font_size=24, color=GRAY_A),
            Text("它本身", font=FONT, font_size=26, color=COLOR_FACTOR, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(UP * 1.8)
        f_example = VGroup(
            Text("例: 12的因数 ", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"\{1,2,3,4,6,12\}", font_size=28, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.06).move_to(UP * 1.1)

        self.play(FadeIn(f_box), run_time=0.3)
        self.play(Write(f_title), run_time=0.4)
        self.play(FadeIn(f1, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(f2, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(f3, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(f_example, shift=LEFT * 0.2), run_time=0.4)
        self.wait(0.5)

        # ===== 倍数总结框 =====
        m_box = RoundedRectangle(
            width=7.6, height=3.8,
            corner_radius=0.25,
            fill_color=COLOR_BOX, fill_opacity=0.95,
            stroke_color=COLOR_MULTIPLE, stroke_width=3
        ).move_to(DOWN * 2.3)

        m_title = Text(
            "倍数", font=FONT, font_size=36,
            color=COLOR_MULTIPLE, weight=BOLD
        ).move_to(DOWN * 0.8)

        m1 = VGroup(
            Text("个数: ", font=FONT, font_size=24, color=GRAY_A),
            Text("无限", font=FONT, font_size=26, color=WHITE, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 1.6)
        m2 = VGroup(
            Text("最小倍数: ", font=FONT, font_size=24, color=GRAY_A),
            Text("它本身", font=FONT, font_size=26, color=COLOR_MULTIPLE, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 2.3)
        m3 = VGroup(
            Text("最大倍数: ", font=FONT, font_size=24, color=GRAY_A),
            Text("没有", font=FONT, font_size=26, color=COLOR_ARROW, weight=BOLD),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 3.0)
        m_example = VGroup(
            Text("例: 3的倍数 ", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"\{3,6,9,12,15,\cdots\}", font_size=28, color=COLOR_MULTIPLE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 3.7)

        self.play(FadeIn(m_box), run_time=0.3)
        self.play(Write(m_title), run_time=0.4)
        self.play(FadeIn(m1, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(m2, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(m3, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(m_example, shift=LEFT * 0.2), run_time=0.4)
        self.wait(0.5)

        # 核心公式回顾
        core_box = RoundedRectangle(
            width=7.6, height=1.6,
            corner_radius=0.2,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 5.8)

        core_eq = MathTex(
            r"a \div b = c",
            r"\quad (\text{R} = 0)",
            font_size=36, color=WHITE
        ).move_to(DOWN * 5.5)

        core_note = VGroup(
            MathTex("a", font_size=28, color=COLOR_DIVIDEND),
            Text(" 是 ", font=FONT, font_size=20, color=WHITE),
            MathTex("b", font_size=28, color=COLOR_FACTOR),
            Text(" 和 ", font=FONT, font_size=20, color=WHITE),
            MathTex("c", font_size=28, color=COLOR_FACTOR),
            Text(" 的倍数;  ", font=FONT, font_size=20, color=COLOR_MULTIPLE),
            MathTex("b", font_size=28, color=COLOR_FACTOR),
            Text(" 和 ", font=FONT, font_size=20, color=WHITE),
            MathTex("c", font_size=28, color=COLOR_FACTOR),
            Text(" 是 ", font=FONT, font_size=20, color=WHITE),
            MathTex("a", font_size=28, color=COLOR_DIVIDEND),
            Text(" 的因数", font=FONT, font_size=20, color=COLOR_FACTOR),
        ).arrange(RIGHT, buff=0.03).move_to(DOWN * 6.2)

        self.play(FadeIn(core_box), run_time=0.3)
        self.play(Write(core_eq), run_time=0.7)
        self.play(FadeIn(core_note, shift=UP * 0.15), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                f_box, f_title, f1, f2, f3, f_example,
                m_box, m_title, m1, m2, m3, m_example,
                core_box, core_eq, core_note
            )),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示 + 数字装饰"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 用因数和倍数的数字围绕旋转
        deco_nums = ["1", "2", "3", "4", "6", "12"]
        deco_colors = [
            COLOR_FACTOR, COLOR_MULTIPLE, COLOR_FACTOR,
            COLOR_MULTIPLE, COLOR_FACTOR, COLOR_DIVIDEND
        ]
        mini_group = VGroup()
        for i, (num, col) in enumerate(zip(deco_nums, deco_colors)):
            angle = i * PI / 3
            pos = DOWN * 2.8 + np.array([
                np.cos(angle) * 2.2,
                np.sin(angle) * 0.7,
                0.0
            ])
            circle = Circle(
                radius=0.32, color=col,
                fill_opacity=0.8, stroke_width=1.5
            )
            label = Text(
                num, font=FONT, font_size=24,
                color=WHITE, weight=BOLD
            )
            g = VGroup(circle, label).move_to(pos)
            mini_group.add(g)

        self.play(*[FadeIn(t, scale=0.3) for t in mini_group], run_time=0.5)
        self.play(
            Rotate(mini_group, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_group)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 001_因数和倍数.py FactorMultipleLesson
#   高质量:    manim -qh  001_因数和倍数.py FactorMultipleLesson
#   4K:        manim -qk  001_因数和倍数.py FactorMultipleLesson
# ======================================================================
