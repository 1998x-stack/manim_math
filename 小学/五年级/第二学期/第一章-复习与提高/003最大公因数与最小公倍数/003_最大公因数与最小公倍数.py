"""
003_最大公因数与最小公倍数.py — 最大公因数与最小公倍数 教学动画

知识点: 公因数、最大公因数(GCF)、公倍数、最小公倍数(LCM)、短除法
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 公因数与最大公因数的概念
  2. 公倍数与最小公倍数的概念
  3. 短除法求GCF和LCM (以12和18为例)
  4. 互素概念(公因数只有1)
  5. GCF(12,18)=6, LCM(12,18)=36
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
COLOR_GCF = "#3b82f6"         # 蓝色最大公因数
COLOR_LCM = "#22c55e"         # 绿色最小公倍数
COLOR_COMMON = "#f59e0b"      # 橙色公共部分
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_STEP = "#a78bfa"        # 紫色步骤
COLOR_WARN = "#ef4444"        # 红色重点
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class GCFLCMLesson(Scene):
    """
    最大公因数与最小公倍数教学动画
    场景:
      1. 开场钩子
      2. 公因数与最大公因数
      3. 公倍数与最小公倍数
      4. 短除法求GCF和LCM
      5. 互素概念
      6. 总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_gcf()
        self.scene_3_lcm()
        self.scene_4_short_division()
        self.scene_5_coprime()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "最大公因数", font=FONT, font_size=44, color=COLOR_GCF, weight=BOLD
        ).move_to(UP * 5.8)
        hook_and = Text(
            "与", font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 5.0)
        hook2 = Text(
            "最小公倍数", font=FONT, font_size=44, color=COLOR_LCM, weight=BOLD
        ).move_to(UP * 4.2)
        self.play(Write(hook1), run_time=0.5)
        self.play(Write(hook_and), run_time=0.3)
        self.play(Write(hook2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook_and, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 公因数与最大公因数
    # ------------------------------------------------------------------
    def scene_2_gcf(self):
        title = Text(
            "公因数与最大公因数", font=FONT, font_size=36,
            color=COLOR_GCF, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 12的因数
        f12_label = Text("12的因数：", font=FONT, font_size=22, color=COLOR_GCF)
        f12_nums = Text("1, 2, 3, 4, 6, 12", font=FONT, font_size=22, color=WHITE)
        f12 = VGroup(f12_label, f12_nums).arrange(RIGHT, buff=0.1).move_to(UP * 3.8)
        self.play(FadeIn(f12, shift=RIGHT * 0.3), run_time=0.5)

        # 18的因数
        f18_label = Text("18的因数：", font=FONT, font_size=22, color=COLOR_LCM)
        f18_nums = Text("1, 2, 3, 6, 9, 18", font=FONT, font_size=22, color=WHITE)
        f18 = VGroup(f18_label, f18_nums).arrange(RIGHT, buff=0.1).move_to(UP * 2.8)
        self.play(FadeIn(f18, shift=RIGHT * 0.3), run_time=0.5)

        # 公因数
        common_label = Text("公因数：", font=FONT, font_size=24, color=COLOR_COMMON, weight=BOLD)
        common_nums = Text("1, 2, 3, 6", font=FONT, font_size=24, color=COLOR_COMMON, weight=BOLD)
        common = VGroup(common_label, common_nums).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        self.play(FadeIn(common, shift=UP * 0.2), run_time=0.6)

        # 韦恩图
        circle_12 = Circle(radius=1.8, color=COLOR_GCF, stroke_width=2, fill_opacity=0.1, fill_color=COLOR_GCF)
        circle_18 = Circle(radius=1.8, color=COLOR_LCM, stroke_width=2, fill_opacity=0.1, fill_color=COLOR_LCM)
        circle_12.move_to(DOWN * 1.5 + LEFT * 1.0)
        circle_18.move_to(DOWN * 1.5 + RIGHT * 1.0)

        label_12 = Text("12", font=FONT, font_size=20, color=COLOR_GCF).move_to(DOWN * 0.2 + LEFT * 2.2)
        label_18 = Text("18", font=FONT, font_size=20, color=COLOR_LCM).move_to(DOWN * 0.2 + RIGHT * 2.2)

        only_12 = Text("4, 12", font=FONT, font_size=18, color=COLOR_GCF).move_to(DOWN * 1.5 + LEFT * 2.0)
        only_18 = Text("9, 18", font=FONT, font_size=18, color=COLOR_LCM).move_to(DOWN * 1.5 + RIGHT * 2.0)
        shared = Text("1,2,3,6", font=FONT, font_size=18, color=COLOR_COMMON).move_to(DOWN * 1.5)

        self.play(Create(circle_12), Create(circle_18), run_time=0.6)
        self.play(
            FadeIn(label_12), FadeIn(label_18),
            FadeIn(only_12), FadeIn(only_18), FadeIn(shared),
            run_time=0.5
        )

        # 最大公因数
        gcf_text = Text(
            "最大公因数 = 6", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.8)
        gcf_box = SurroundingRectangle(gcf_text, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(gcf_text, shift=UP * 0.2), Create(gcf_box), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, f12, f18, common,
                circle_12, circle_18, label_12, label_18,
                only_12, only_18, shared, gcf_text, gcf_box
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 公倍数与最小公倍数
    # ------------------------------------------------------------------
    def scene_3_lcm(self):
        title = Text(
            "公倍数与最小公倍数", font=FONT, font_size=36,
            color=COLOR_LCM, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 12的倍数
        m12_label = Text("12的倍数：", font=FONT, font_size=22, color=COLOR_GCF)
        m12_nums = Text("12, 24, 36, 48, 60, 72 ...", font=FONT, font_size=20, color=WHITE)
        m12 = VGroup(m12_label, m12_nums).arrange(RIGHT, buff=0.1).move_to(UP * 3.8)
        self.play(FadeIn(m12, shift=RIGHT * 0.3), run_time=0.5)

        # 18的倍数
        m18_label = Text("18的倍数：", font=FONT, font_size=22, color=COLOR_LCM)
        m18_nums = Text("18, 36, 54, 72, 90 ...", font=FONT, font_size=20, color=WHITE)
        m18 = VGroup(m18_label, m18_nums).arrange(RIGHT, buff=0.1).move_to(UP * 2.8)
        self.play(FadeIn(m18, shift=RIGHT * 0.3), run_time=0.5)

        # 公倍数
        common_label = Text("公倍数：", font=FONT, font_size=24, color=COLOR_COMMON, weight=BOLD)
        common_nums = Text("36, 72, 108 ...", font=FONT, font_size=24, color=COLOR_COMMON, weight=BOLD)
        common = VGroup(common_label, common_nums).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        self.play(FadeIn(common, shift=UP * 0.2), run_time=0.6)

        # 数轴展示
        num_line = NumberLine(
            x_range=[0, 78, 6], length=7.5,
            include_numbers=False, color=GRAY_A
        ).move_to(DOWN * 0.5)
        self.play(Create(num_line), run_time=0.5)

        # 12的倍数点
        dots_12 = VGroup()
        for m in [12, 24, 36, 48, 60, 72]:
            dot = Dot(num_line.n2p(m), color=COLOR_GCF, radius=0.08)
            label = Text(str(m), font=FONT, font_size=14, color=COLOR_GCF).next_to(dot, UP, buff=0.15)
            dots_12.add(VGroup(dot, label))
        self.play(FadeIn(dots_12), run_time=0.5)

        # 18的倍数点
        dots_18 = VGroup()
        for m in [18, 36, 54, 72]:
            dot = Dot(num_line.n2p(m), color=COLOR_LCM, radius=0.08)
            label = Text(str(m), font=FONT, font_size=14, color=COLOR_LCM).next_to(dot, DOWN, buff=0.15)
            dots_18.add(VGroup(dot, label))
        self.play(FadeIn(dots_18), run_time=0.5)

        # 标记公倍数
        for m in [36, 72]:
            star = Star(n=5, outer_radius=0.2, color=COLOR_COMMON, fill_opacity=1).move_to(num_line.n2p(m))
            self.play(FadeIn(star, scale=1.5), run_time=0.3)

        # 最小公倍数
        lcm_text = Text(
            "最小公倍数 = 36", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
        lcm_box = SurroundingRectangle(lcm_text, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(lcm_text, shift=UP * 0.2), Create(lcm_box), run_time=0.6)

        note = Text(
            "公倍数有无数个，最小公倍数只有一个",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, m12, m18, common, num_line,
                dots_12, dots_18, lcm_text, lcm_box, note
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 短除法求GCF和LCM
    # ------------------------------------------------------------------
    def scene_4_short_division(self):
        title = Text(
            "短除法", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        subtitle = Text(
            "以 12 和 18 为例", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 短除法过程
        # Step 1:  2 | 12  18
        div1_num = Text("2", font=FONT, font_size=30, color=COLOR_STEP, weight=BOLD).move_to(UP * 3.0 + LEFT * 2.5)
        div1_line_v = Line(UP * 3.4 + LEFT * 1.8, UP * 2.6 + LEFT * 1.8, color=WHITE, stroke_width=2)
        div1_line_h = Line(UP * 2.6 + LEFT * 1.8, UP * 2.6 + RIGHT * 1.5, color=WHITE, stroke_width=2)
        num1_12 = Text("12", font=FONT, font_size=28, color=WHITE).move_to(UP * 3.0 + LEFT * 0.5)
        num1_18 = Text("18", font=FONT, font_size=28, color=WHITE).move_to(UP * 3.0 + RIGHT * 0.8)

        self.play(
            FadeIn(div1_num), Create(div1_line_v), Create(div1_line_h),
            FadeIn(num1_12), FadeIn(num1_18),
            run_time=0.6
        )

        # Step 2:  3 | 6   9
        div2_num = Text("3", font=FONT, font_size=30, color=COLOR_STEP, weight=BOLD).move_to(UP * 2.0 + LEFT * 2.5)
        div2_line_v = Line(UP * 2.4 + LEFT * 1.8, UP * 1.6 + LEFT * 1.8, color=WHITE, stroke_width=2)
        div2_line_h = Line(UP * 1.6 + LEFT * 1.8, UP * 1.6 + RIGHT * 1.5, color=WHITE, stroke_width=2)
        num2_6 = Text("6", font=FONT, font_size=28, color=WHITE).move_to(UP * 2.0 + LEFT * 0.5)
        num2_9 = Text("9", font=FONT, font_size=28, color=WHITE).move_to(UP * 2.0 + RIGHT * 0.8)

        self.play(
            FadeIn(div2_num), Create(div2_line_v), Create(div2_line_h),
            FadeIn(num2_6), FadeIn(num2_9),
            run_time=0.6
        )

        # Step 3: 结果  2   3
        num3_2 = Text("2", font=FONT, font_size=28, color=COLOR_WARN).move_to(UP * 1.0 + LEFT * 0.5)
        num3_3 = Text("3", font=FONT, font_size=28, color=COLOR_WARN).move_to(UP * 1.0 + RIGHT * 0.8)
        self.play(FadeIn(num3_2), FadeIn(num3_3), run_time=0.5)
        self.wait(0.5)

        # GCF 计算
        gcf_label = Text("最大公因数：", font=FONT, font_size=24, color=COLOR_GCF)
        gcf_calc = MathTex(r"2 \times 3 = 6", font_size=36, color=COLOR_GCF)
        gcf_row = VGroup(gcf_label, gcf_calc).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        self.play(FadeIn(gcf_row, shift=UP * 0.2), run_time=0.6)

        gcf_note = Text(
            "左边除数相乘", font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(gcf_note), run_time=0.3)

        # LCM 计算
        lcm_label = Text("最小公倍数：", font=FONT, font_size=24, color=COLOR_LCM)
        lcm_calc = MathTex(r"2 \times 3 \times 2 \times 3 = 36", font_size=34, color=COLOR_LCM)
        lcm_row = VGroup(lcm_label, lcm_calc).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)
        self.play(FadeIn(lcm_row, shift=UP * 0.2), run_time=0.6)

        lcm_note = Text(
            "左边除数 x 底下商 全部相乘", font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(lcm_note), run_time=0.3)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle,
                div1_num, div1_line_v, div1_line_h, num1_12, num1_18,
                div2_num, div2_line_v, div2_line_h, num2_6, num2_9,
                num3_2, num3_3,
                gcf_row, gcf_note, lcm_row, lcm_note
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 互素概念
    # ------------------------------------------------------------------
    def scene_5_coprime(self):
        title = Text(
            "互素（互质）", font=FONT, font_size=38,
            color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "公因数只有1的两个数，叫互素",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.8)
        self.play(Write(defn), run_time=0.6)

        # 例子
        examples = [
            ("3 和 5", "公因数：1", "互素"),
            ("4 和 9", "公因数：1", "互素"),
            ("7 和 8", "公因数：1", "互素"),
            ("6 和 9", "公因数：1, 3", "不互素"),
        ]

        rows = VGroup()
        for pair_str, cf_str, result_str in examples:
            pair_t = Text(pair_str, font=FONT, font_size=22, color=COLOR_HL, weight=BOLD)
            arrow = MathTex(r"\rightarrow", font_size=22, color=GRAY_A)
            cf_t = Text(cf_str, font=FONT, font_size=20, color=WHITE)
            is_coprime = result_str == "互素"
            result_color = COLOR_LCM if is_coprime else COLOR_WARN
            result_t = Text(result_str, font=FONT, font_size=22, color=result_color, weight=BOLD)
            row = VGroup(pair_t, arrow, cf_t, result_t).arrange(RIGHT, buff=0.2)
            rows.add(row)

        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.0)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.3)

        note = Text(
            "互素的两个数，最大公因数为1",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 2.5)
        note2 = Text(
            "互素的两个数，最小公倍数为它们的积",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(note2, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, defn, rows, note, note2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 总结
    # ------------------------------------------------------------------
    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.0)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "最大公因数与最小公倍数", font=FONT,
            font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.2)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 公因数：几个数公有的因数", font=FONT, font_size=20, color=WHITE),
            Text("2. 最大公因数(GCF)：最大的那个", font=FONT, font_size=20, color=COLOR_GCF),
            Text("3. 公倍数：几个数公有的倍数", font=FONT, font_size=20, color=WHITE),
            Text("4. 最小公倍数(LCM)：最小的那个", font=FONT, font_size=20, color=COLOR_LCM),
            Text("5. 短除法：左乘得GCF，全乘得LCM", font=FONT, font_size=20, color=COLOR_STEP),
            Text("6. 互素：公因数只有1", font=FONT, font_size=20, color=COLOR_WARN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 0.0)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "短除法是核心工具！",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------
    def scene_7_outro(self):
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

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 003_最大公因数与最小公倍数.py GCFLCMLesson
#   高质量:    manim -qh  003_最大公因数与最小公倍数.py GCFLCMLesson
#   4K:        manim -qk  003_最大公因数与最小公倍数.py GCFLCMLesson
# ======================================================================
