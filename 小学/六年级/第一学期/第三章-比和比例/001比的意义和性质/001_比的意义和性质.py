"""
001_比的意义和性质.py — 比的意义和性质 教学动画

知识点: 比的意义、比值、比的基本性质、化简比
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 比的意义: 两个数量之间的倍数关系
  3. 比的各部分名称: 前项、比号、后项
  4. 比值: 前项除以后项
  5. 比的基本性质: 前项和后项同乘或同除
  6. 化简比: 化成最简整数比
  7. 例题: 小数比和分数比的化简
  8. 总结
  9. 片尾
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
COLOR_FRONT = "#3b82f6"       # 蓝色 前项
COLOR_BACK = "#f59e0b"        # 橙色 后项
COLOR_RATIO_SIGN = "#ef4444"  # 红色 比号
COLOR_RESULT = "#22c55e"      # 绿色 结果
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_PROPERTY = "#38bdf8"    # 天蓝色 性质
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class RatioMeaningAndProperties(Scene):
    """
    比的意义和性质教学动画
    场景顺序:
      1. 开场钩子
      2. 比的意义 — 生活实例引入
      3. 比的各部分名称
      4. 比值的计算
      5. 比的基本性质
      6. 化简比 (整数比)
      7. 化简比 (小数比和分数比)
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_meaning()
        self.scene_3_parts()
        self.scene_4_ratio_value()
        self.scene_5_property()
        self.scene_6_simplify_integer()
        self.scene_7_simplify_decimal_fraction()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 6:9 和 2:3 一样吗？"""

        # 作者信息 (顶部)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook1 = Text(
            "比的意义和性质",
            font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "6 : 9  和  2 : 3  一样吗？",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 预览: 两个比并列
        ratio_left = MathTex(r"6 : 9", font_size=80, color=COLOR_FRONT)
        eq_sign = MathTex(r"=", font_size=80, color=COLOR_HL)
        ratio_right = MathTex(r"2 : 3", font_size=80, color=COLOR_RESULT)
        question = MathTex(r"?", font_size=80, color=COLOR_HL)

        preview = VGroup(ratio_left, eq_sign, ratio_right, question).arrange(RIGHT, buff=0.3)
        preview.move_to(UP * 2.2)

        self.play(FadeIn(preview, scale=0.5), run_time=0.8)
        self.wait(0.6)

        hint = Text(
            "学完这节课你就知道了！",
            font=FONT, font_size=30, color=COLOR_ACCENT
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, preview, hint)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 比的意义
    # ------------------------------------------------------------------

    def scene_2_meaning(self):
        """比的意义: 两个数量之间的倍数关系"""

        title = Text(
            "比的意义", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        # 生活实例
        example_title = Text(
            "生活中的比",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 5.3)
        self.play(FadeIn(example_title), run_time=0.3)

        # 例子: 果汁和水 --- 用矩形条表示
        bar_w = 7.0
        bar_h = 0.9
        bar_cy = 3.8

        # 果汁: 2份 (蓝)
        juice_parts = 2
        water_parts = 3
        total_parts = juice_parts + water_parts
        part_w = bar_w / total_parts

        juice_group = VGroup()
        for i in range(juice_parts):
            rect = Rectangle(
                width=part_w - 0.06, height=bar_h,
                fill_color=COLOR_FRONT, fill_opacity=0.75,
                stroke_color=WHITE, stroke_width=1.5
            )
            x_pos = -bar_w / 2 + part_w / 2 + i * part_w
            rect.move_to(np.array([x_pos, bar_cy, 0]))
            juice_group.add(rect)

        # 水: 3份 (橙)
        water_group = VGroup()
        for i in range(water_parts):
            rect = Rectangle(
                width=part_w - 0.06, height=bar_h,
                fill_color=COLOR_BACK, fill_opacity=0.75,
                stroke_color=WHITE, stroke_width=1.5
            )
            x_pos = -bar_w / 2 + part_w / 2 + (juice_parts + i) * part_w
            rect.move_to(np.array([x_pos, bar_cy, 0]))
            water_group.add(rect)

        bar_all = VGroup(juice_group, water_group)
        self.play(Create(bar_all), run_time=0.6)

        # 标注
        juice_label = Text("果汁 2 份", font=FONT, font_size=22, color=COLOR_FRONT)
        juice_brace = Brace(juice_group, direction=UP, buff=0.05, color=COLOR_FRONT)
        juice_label.next_to(juice_brace, UP, buff=0.08)

        water_label = Text("水 3 份", font=FONT, font_size=22, color=COLOR_BACK)
        water_brace = Brace(water_group, direction=UP, buff=0.05, color=COLOR_BACK)
        water_label.next_to(water_brace, UP, buff=0.08)

        self.play(
            FadeIn(juice_brace), FadeIn(juice_label),
            FadeIn(water_brace), FadeIn(water_label),
            run_time=0.5
        )
        self.wait(0.3)

        # 比的表达
        ratio_text_1 = Text("果汁和水的比是", font=FONT, font_size=28, color=WHITE)
        ratio_math_1 = MathTex(r"2 : 3", font_size=56, color=WHITE)
        ratio_row_1 = VGroup(ratio_text_1, ratio_math_1).arrange(RIGHT, buff=0.2)
        ratio_row_1.move_to(UP * 2.0)
        self.play(FadeIn(ratio_row_1), run_time=0.5)

        # 定义框
        def_box = Rectangle(
            width=7.8, height=2.0,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(UP * 0.2)
        def_t1 = Text(
            "比表示两个数量之间的",
            font=FONT, font_size=26, color=WHITE
        )
        def_t2 = Text(
            "倍数关系",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        )
        def_t3_label = Text("记作 ", font=FONT, font_size=26, color=WHITE)
        def_t3_math = MathTex(r"a : b", font_size=44, color=WHITE)
        def_t3_comma = Text("，读作 a 比 b", font=FONT, font_size=26, color=WHITE)
        def_row3 = VGroup(def_t3_label, def_t3_math, def_t3_comma).arrange(RIGHT, buff=0.12)
        def_content = VGroup(def_t1, def_t2, def_row3).arrange(DOWN, buff=0.15)
        def_content.move_to(UP * 0.2)
        self.play(Create(def_box), FadeIn(def_content), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, example_title,
            bar_all, juice_brace, juice_label, water_brace, water_label,
            ratio_row_1, def_box, def_content
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 比的各部分名称
    # ------------------------------------------------------------------

    def scene_3_parts(self):
        """比的各部分: 前项、比号、后项"""

        title = Text(
            "比的各部分名称",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 大比式: 2 : 3
        front = MathTex(r"2", font_size=120, color=COLOR_FRONT).move_to(LEFT * 2.0 + UP * 3.8)
        colon = MathTex(r":", font_size=120, color=COLOR_RATIO_SIGN).move_to(UP * 3.8)
        back = MathTex(r"3", font_size=120, color=COLOR_BACK).move_to(RIGHT * 2.0 + UP * 3.8)

        self.play(Write(front), Write(colon), Write(back), run_time=0.7)
        self.wait(0.3)

        # 标注前项
        front_arrow = Arrow(
            start=LEFT * 2.0 + UP * 2.4,
            end=LEFT * 2.0 + UP * 2.9,
            color=COLOR_FRONT, stroke_width=3, buff=0.1
        )
        front_label = Text("前项", font=FONT, font_size=28, color=COLOR_FRONT)
        front_label.next_to(front_arrow, DOWN, buff=0.1)
        self.play(Create(front_arrow), FadeIn(front_label), run_time=0.4)

        # 标注比号
        colon_arrow = Arrow(
            start=ORIGIN + UP * 2.4,
            end=ORIGIN + UP * 2.9,
            color=COLOR_RATIO_SIGN, stroke_width=3, buff=0.1
        )
        colon_label = Text("比号", font=FONT, font_size=28, color=COLOR_RATIO_SIGN)
        colon_label.next_to(colon_arrow, DOWN, buff=0.1)
        self.play(Create(colon_arrow), FadeIn(colon_label), run_time=0.4)

        # 标注后项
        back_arrow = Arrow(
            start=RIGHT * 2.0 + UP * 2.4,
            end=RIGHT * 2.0 + UP * 2.9,
            color=COLOR_BACK, stroke_width=3, buff=0.1
        )
        back_label = Text("后项", font=FONT, font_size=28, color=COLOR_BACK)
        back_label.next_to(back_arrow, DOWN, buff=0.1)
        self.play(Create(back_arrow), FadeIn(back_label), run_time=0.4)
        self.wait(0.5)

        # 注意事项
        note_box = Rectangle(
            width=7.5, height=1.6,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=2
        ).move_to(DOWN * 0.3)
        note1 = Text("注意: 比号 \":\" 不能写成除号", font=FONT, font_size=24, color=COLOR_ACCENT)
        note2 = Text("后项不能为 0 (除数不能为0)", font=FONT, font_size=24, color=COLOR_ACCENT)
        note_content = VGroup(note1, note2).arrange(DOWN, buff=0.15)
        note_content.move_to(DOWN * 0.3)
        self.play(Create(note_box), FadeIn(note_content), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, front, colon, back,
            front_arrow, front_label,
            colon_arrow, colon_label,
            back_arrow, back_label,
            note_box, note_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 比值
    # ------------------------------------------------------------------

    def scene_4_ratio_value(self):
        """比值: 前项除以后项"""

        title = Text(
            "比值", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 定义
        def_t1 = Text("比值 = 前项", font=FONT, font_size=28, color=WHITE)
        def_sign = MathTex(r"\div", font_size=42, color=WHITE)
        def_t2 = Text("后项", font=FONT, font_size=28, color=WHITE)
        def_row = VGroup(def_t1, def_sign, def_t2).arrange(RIGHT, buff=0.15)
        def_row.move_to(UP * 5.2)
        self.play(FadeIn(def_row), run_time=0.5)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 4.5)
        self.play(Create(sep), run_time=0.2)

        # 例1: 6:3 = 2
        ex1_label = Text("例 1:", font=FONT, font_size=26, color=GRAY_A)
        ex1_ratio = MathTex(r"6 : 3", font_size=56, color=WHITE)
        ex1_row1 = VGroup(ex1_label, ex1_ratio).arrange(RIGHT, buff=0.3)
        ex1_row1.move_to(UP * 3.7)
        self.play(FadeIn(ex1_row1), run_time=0.4)

        ex1_calc_t = Text("比值 = ", font=FONT, font_size=26, color=WHITE)
        ex1_calc_m = MathTex(r"6 \div 3 = 2", font_size=50, color=COLOR_RESULT)
        ex1_row2 = VGroup(ex1_calc_t, ex1_calc_m).arrange(RIGHT, buff=0.15)
        ex1_row2.move_to(UP * 2.7)
        self.play(Write(ex1_row2), run_time=0.6)

        note1 = Text("(比值是整数)", font=FONT, font_size=22, color=GRAY_A)
        note1.next_to(ex1_row2, RIGHT, buff=0.15)
        self.play(FadeIn(note1), run_time=0.3)

        # 例2: 3:4 = 3/4
        ex2_label = Text("例 2:", font=FONT, font_size=26, color=GRAY_A)
        ex2_ratio = MathTex(r"3 : 4", font_size=56, color=WHITE)
        ex2_row1 = VGroup(ex2_label, ex2_ratio).arrange(RIGHT, buff=0.3)
        ex2_row1.move_to(UP * 1.5)
        self.play(FadeIn(ex2_row1), run_time=0.4)

        ex2_calc_t = Text("比值 = ", font=FONT, font_size=26, color=WHITE)
        ex2_calc_m = MathTex(r"3 \div 4 = \frac{3}{4}", font_size=50, color=COLOR_RESULT)
        ex2_row2 = VGroup(ex2_calc_t, ex2_calc_m).arrange(RIGHT, buff=0.15)
        ex2_row2.move_to(UP * 0.4)
        self.play(Write(ex2_row2), run_time=0.6)

        note2 = Text("(比值是分数)", font=FONT, font_size=22, color=GRAY_A)
        note2.next_to(ex2_row2, RIGHT, buff=0.15)
        self.play(FadeIn(note2), run_time=0.3)

        # 例3: 1:3 = 0.333...
        ex3_label = Text("例 3:", font=FONT, font_size=26, color=GRAY_A)
        ex3_ratio = MathTex(r"1 : 3", font_size=56, color=WHITE)
        ex3_row1 = VGroup(ex3_label, ex3_ratio).arrange(RIGHT, buff=0.3)
        ex3_row1.move_to(DOWN * 0.8)
        self.play(FadeIn(ex3_row1), run_time=0.4)

        ex3_calc_t = Text("比值 = ", font=FONT, font_size=26, color=WHITE)
        ex3_calc_m = MathTex(r"1 \div 3 = 0.333\ldots", font_size=50, color=COLOR_RESULT)
        ex3_row2 = VGroup(ex3_calc_t, ex3_calc_m).arrange(RIGHT, buff=0.15)
        ex3_row2.move_to(DOWN * 1.9)
        self.play(Write(ex3_row2), run_time=0.6)

        note3 = Text("(比值是小数)", font=FONT, font_size=22, color=GRAY_A)
        note3.next_to(ex3_row2, RIGHT, buff=0.15)
        self.play(FadeIn(note3), run_time=0.3)
        self.wait(0.4)

        # 总结框
        summary_box = RoundedRectangle(
            width=7.5, height=1.5, corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.85,
            stroke_color=COLOR_RESULT, stroke_width=2
        ).move_to(DOWN * 3.8)
        summary_text = Text(
            "比值可以是整数、分数或小数",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.8)
        self.play(Create(summary_box), FadeIn(summary_text), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, def_row, sep,
            ex1_row1, ex1_row2, note1,
            ex2_row1, ex2_row2, note2,
            ex3_row1, ex3_row2, note3,
            summary_box, summary_text
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 比的基本性质
    # ------------------------------------------------------------------

    def scene_5_property(self):
        """比的基本性质: 前项和后项同乘或同除，比值不变"""

        title = Text(
            "比的基本性质",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 性质文字
        prop_box = Rectangle(
            width=8.0, height=2.4,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_PROPERTY, stroke_width=2.5
        ).move_to(UP * 4.5)
        prop_t1 = Text(
            "比的前项和后项同时乘以",
            font=FONT, font_size=26, color=WHITE
        )
        prop_t2 = Text(
            "或除以相同的数（0除外），",
            font=FONT, font_size=26, color=WHITE
        )
        prop_t3 = Text(
            "比值不变。",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        )
        prop_content = VGroup(prop_t1, prop_t2, prop_t3).arrange(DOWN, buff=0.12)
        prop_content.move_to(UP * 4.5)
        self.play(Create(prop_box), FadeIn(prop_content), run_time=0.6)
        self.wait(0.5)

        # 演示: 同乘
        demo_title_1 = Text("同乘:", font=FONT, font_size=28, color=COLOR_PROPERTY)
        demo_title_1.move_to(UP * 2.8 + LEFT * 3.0)
        self.play(FadeIn(demo_title_1), run_time=0.3)

        # 2:3 -> ×2 -> 4:6
        ratio_1 = MathTex(r"2 : 3", font_size=64, color=WHITE).move_to(UP * 2.8)
        self.play(Write(ratio_1), run_time=0.5)

        # 乘以2的箭头和标注
        arrow_mul_front = Arrow(
            start=UP * 2.3 + LEFT * 0.8,
            end=UP * 1.3 + LEFT * 0.8,
            color=COLOR_HL, stroke_width=3
        )
        mul_label_front = MathTex(r"\times 2", font_size=30, color=COLOR_HL)
        mul_label_front.next_to(arrow_mul_front, LEFT, buff=0.1)

        arrow_mul_back = Arrow(
            start=UP * 2.3 + RIGHT * 0.8,
            end=UP * 1.3 + RIGHT * 0.8,
            color=COLOR_HL, stroke_width=3
        )
        mul_label_back = MathTex(r"\times 2", font_size=30, color=COLOR_HL)
        mul_label_back.next_to(arrow_mul_back, RIGHT, buff=0.1)

        self.play(
            Create(arrow_mul_front), FadeIn(mul_label_front),
            Create(arrow_mul_back), FadeIn(mul_label_back),
            run_time=0.5
        )

        ratio_2 = MathTex(r"4 : 6", font_size=64, color=WHITE).move_to(UP * 0.8)
        self.play(Write(ratio_2), run_time=0.5)

        # 验证比值
        check_1_t = Text("比值: ", font=FONT, font_size=22, color=GRAY_A)
        check_1_m = MathTex(r"2 \div 3 = \frac{2}{3}", font_size=36, color=COLOR_RESULT)
        check_1 = VGroup(check_1_t, check_1_m).arrange(RIGHT, buff=0.1)
        check_1.move_to(DOWN * 0.0 + LEFT * 1.5)

        check_2_t = Text("比值: ", font=FONT, font_size=22, color=GRAY_A)
        check_2_m = MathTex(r"4 \div 6 = \frac{2}{3}", font_size=36, color=COLOR_RESULT)
        check_2 = VGroup(check_2_t, check_2_m).arrange(RIGHT, buff=0.1)
        check_2.move_to(DOWN * 0.0 + RIGHT * 2.0)

        self.play(FadeIn(check_1), FadeIn(check_2), run_time=0.5)

        equal_sign = Text("比值相等！", font=FONT, font_size=26, color=COLOR_HL)
        equal_sign.move_to(DOWN * 0.8)
        self.play(FadeIn(equal_sign), run_time=0.3)
        self.wait(0.5)

        # 类比说明
        analogy_box = RoundedRectangle(
            width=7.5, height=1.5, corner_radius=0.2,
            fill_color="#3b1f6e", fill_opacity=0.85,
            stroke_color=COLOR_ACCENT, stroke_width=2
        ).move_to(DOWN * 2.2)
        analogy_t1 = Text("类似于分数的基本性质!", font=FONT, font_size=26, color=WHITE)
        analogy_t2 = MathTex(r"\frac{a}{b} = \frac{a \times c}{b \times c}", font_size=40, color=COLOR_ACCENT)
        analogy_content = VGroup(analogy_t1, analogy_t2).arrange(DOWN, buff=0.1)
        analogy_content.move_to(DOWN * 2.2)
        self.play(Create(analogy_box), FadeIn(analogy_content), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, prop_box, prop_content,
            demo_title_1, ratio_1,
            arrow_mul_front, mul_label_front,
            arrow_mul_back, mul_label_back,
            ratio_2, check_1, check_2, equal_sign,
            analogy_box, analogy_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 化简比 (整数比)
    # ------------------------------------------------------------------

    def scene_6_simplify_integer(self):
        """化简整数比: 6:9 = 2:3"""

        title = Text(
            "化简比", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        subtitle = Text(
            "化成最简整数比",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 什么是最简整数比
        explain_box = Rectangle(
            width=7.5, height=1.4,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_PROPERTY, stroke_width=2
        ).move_to(UP * 4.3)
        explain_t = Text(
            "前项和后项是互质的整数",
            font=FONT, font_size=24, color=COLOR_PROPERTY
        ).move_to(UP * 4.3)
        self.play(Create(explain_box), FadeIn(explain_t), run_time=0.4)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 3.3)
        self.play(Create(sep), run_time=0.2)

        # 例题: 6:9
        ex_label = Text("例:", font=FONT, font_size=28, color=GRAY_A)
        ex_t1 = Text("化简", font=FONT, font_size=28, color=WHITE)
        ex_ratio = MathTex(r"6 : 9", font_size=64, color=WHITE)
        ex_row = VGroup(ex_label, ex_t1, ex_ratio).arrange(RIGHT, buff=0.2)
        ex_row.move_to(UP * 2.5)
        self.play(FadeIn(ex_row), run_time=0.5)

        # 步骤1: 找最大公因数
        step1_label = Text("第1步", font=FONT, font_size=22, color=COLOR_ACCENT)
        step1_t = Text(" 找最大公因数", font=FONT, font_size=22, color=WHITE)
        step1_row = VGroup(step1_label, step1_t).arrange(RIGHT, buff=0.1)
        step1_row.move_to(UP * 1.5 + LEFT * 1.5)
        self.play(FadeIn(step1_row), run_time=0.3)

        gcd_text = MathTex(r"6 = 2 \times 3,\quad 9 = 3 \times 3", font_size=40, color=WHITE)
        gcd_text.move_to(UP * 0.8)
        self.play(Write(gcd_text), run_time=0.6)

        gcd_result_t = Text("最大公因数 = ", font=FONT, font_size=24, color=WHITE)
        gcd_result_m = MathTex(r"3", font_size=52, color=COLOR_HL)
        gcd_result_row = VGroup(gcd_result_t, gcd_result_m).arrange(RIGHT, buff=0.15)
        gcd_result_row.move_to(UP * 0.1)
        self.play(FadeIn(gcd_result_row), run_time=0.4)

        # 步骤2: 前项后项同除
        step2_label = Text("第2步", font=FONT, font_size=22, color=COLOR_ACCENT)
        step2_t = Text(" 前项后项同除以 3", font=FONT, font_size=22, color=WHITE)
        step2_row = VGroup(step2_label, step2_t).arrange(RIGHT, buff=0.1)
        step2_row.move_to(DOWN * 0.8 + LEFT * 1.0)
        self.play(FadeIn(step2_row), run_time=0.3)

        simplify_eq = MathTex(
            r"6 : 9 = (6 \div 3) : (9 \div 3) = 2 : 3",
            font_size=44, color=WHITE
        ).move_to(DOWN * 1.8)
        self.play(Write(simplify_eq), run_time=0.8)

        # 结果框
        result_box = RoundedRectangle(
            width=5.0, height=1.3, corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.85,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 3.2)
        result_t1 = Text("最简比:", font=FONT, font_size=26, color=WHITE)
        result_m = MathTex(r"2 : 3", font_size=60, color=COLOR_RESULT)
        result_content = VGroup(result_t1, result_m).arrange(RIGHT, buff=0.3)
        result_content.move_to(DOWN * 3.2)
        self.play(Create(result_box), FadeIn(result_content), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, subtitle, explain_box, explain_t, sep,
            ex_row, step1_row, gcd_text, gcd_result_row,
            step2_row, simplify_eq, result_box, result_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 化简小数比和分数比
    # ------------------------------------------------------------------

    def scene_7_simplify_decimal_fraction(self):
        """化简小数比和分数比"""

        title = Text(
            "化简小数比和分数比",
            font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.3)

        # ------ 小数比 ------
        dec_label = Text("小数比:", font=FONT, font_size=28, color=COLOR_PROPERTY)
        dec_label.move_to(UP * 5.3 + LEFT * 2.5)
        self.play(FadeIn(dec_label), run_time=0.3)

        dec_problem = MathTex(r"0.6 : 0.9", font_size=60, color=WHITE)
        dec_problem.move_to(UP * 5.3 + RIGHT * 1.0)
        self.play(Write(dec_problem), run_time=0.5)

        dec_step1_t = Text("先化成整数比:", font=FONT, font_size=24, color=GRAY_A)
        dec_step1_t.move_to(UP * 4.4 + LEFT * 2.0)
        self.play(FadeIn(dec_step1_t), run_time=0.3)

        dec_step1 = MathTex(
            r"0.6 : 0.9 = 6 : 9",
            font_size=48, color=WHITE
        ).move_to(UP * 3.6)

        dec_step1_note = Text("(同乘10)", font=FONT, font_size=22, color=COLOR_HL)
        dec_step1_note.next_to(dec_step1, RIGHT, buff=0.2)
        self.play(Write(dec_step1), FadeIn(dec_step1_note), run_time=0.6)

        dec_step2_t = Text("再化简:", font=FONT, font_size=24, color=GRAY_A)
        dec_step2_t.move_to(UP * 2.8 + LEFT * 2.5)
        self.play(FadeIn(dec_step2_t), run_time=0.3)

        dec_step2 = MathTex(
            r"6 : 9 = 2 : 3",
            font_size=48, color=COLOR_RESULT
        ).move_to(UP * 2.0)

        dec_step2_note = Text("(同除3)", font=FONT, font_size=22, color=COLOR_HL)
        dec_step2_note.next_to(dec_step2, RIGHT, buff=0.2)
        self.play(Write(dec_step2), FadeIn(dec_step2_note), run_time=0.6)
        self.wait(0.6)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 1.0)
        self.play(Create(sep), run_time=0.2)

        # ------ 分数比 ------
        frac_label = Text("分数比:", font=FONT, font_size=28, color=COLOR_PROPERTY)
        frac_label.move_to(UP * 0.3 + LEFT * 2.5)
        self.play(FadeIn(frac_label), run_time=0.3)

        frac_problem = MathTex(
            r"\frac{1}{3} : \frac{1}{2}",
            font_size=60, color=WHITE
        ).move_to(UP * 0.3 + RIGHT * 1.0)
        self.play(Write(frac_problem), run_time=0.5)

        frac_step1_t = Text("先化成整数比:", font=FONT, font_size=24, color=GRAY_A)
        frac_step1_t.move_to(DOWN * 0.7 + LEFT * 2.0)
        self.play(FadeIn(frac_step1_t), run_time=0.3)

        frac_step1 = MathTex(
            r"\frac{1}{3} : \frac{1}{2} = 2 : 3",
            font_size=48, color=WHITE
        ).move_to(DOWN * 1.5)

        frac_step1_note = Text("(同乘6)", font=FONT, font_size=22, color=COLOR_HL)
        frac_step1_note.next_to(frac_step1, RIGHT, buff=0.2)
        self.play(Write(frac_step1), FadeIn(frac_step1_note), run_time=0.6)

        frac_step2_t = Text("已是最简整数比!", font=FONT, font_size=24, color=COLOR_RESULT)
        frac_step2_t.move_to(DOWN * 2.3)
        self.play(FadeIn(frac_step2_t), run_time=0.3)
        self.wait(0.5)

        # 方法总结框
        method_box = Rectangle(
            width=7.8, height=2.0,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 4.0)
        method_t1 = Text("化简方法:", font=FONT, font_size=26, color=COLOR_HL)
        method_t2 = Text("小数比 -> 先化成整数比 -> 再约分", font=FONT, font_size=22, color=WHITE)
        method_t3 = Text("分数比 -> 同乘分母的最小公倍数", font=FONT, font_size=22, color=WHITE)
        method_content = VGroup(method_t1, method_t2, method_t3).arrange(DOWN, buff=0.12)
        method_content.move_to(DOWN * 4.0)
        self.play(Create(method_box), FadeIn(method_content), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title,
            dec_label, dec_problem, dec_step1_t, dec_step1, dec_step1_note,
            dec_step2_t, dec_step2, dec_step2_note,
            sep,
            frac_label, frac_problem, frac_step1_t, frac_step1, frac_step1_note,
            frac_step2_t,
            method_box, method_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        """总结: 核心知识点"""

        title = Text(
            "总结", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 卡片1: 比的意义
        card1 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=COLOR_FRONT, stroke_width=2.5
        ).move_to(UP * 5.0)
        c1_t = Text("比的意义", font=FONT, font_size=28, color=COLOR_FRONT)
        c1_c = Text("表示两个数量的倍数关系  a : b",
                     font=FONT, font_size=22, color=WHITE)
        c1_content = VGroup(c1_t, c1_c).arrange(DOWN, buff=0.12)
        c1_content.move_to(UP * 5.0)
        self.play(Create(card1), FadeIn(c1_content), run_time=0.5)

        # 卡片2: 各部分名称
        card2 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#422006", fill_opacity=0.9,
            stroke_color=COLOR_BACK, stroke_width=2.5
        ).move_to(UP * 2.9)
        c2_t = Text("各部分名称", font=FONT, font_size=28, color=COLOR_BACK)
        c2_c = Text("前项 : 后项  (后项不为0)",
                     font=FONT, font_size=22, color=WHITE)
        c2_content = VGroup(c2_t, c2_c).arrange(DOWN, buff=0.12)
        c2_content.move_to(UP * 2.9)
        self.play(Create(card2), FadeIn(c2_content), run_time=0.5)

        # 卡片3: 比值
        card3 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#14532d", fill_opacity=0.9,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(UP * 0.8)
        c3_t = Text("比值", font=FONT, font_size=28, color=COLOR_RESULT)
        c3_t2 = Text("比值 = 前项", font=FONT, font_size=22, color=WHITE)
        c3_m = MathTex(r"\div", font_size=34, color=WHITE)
        c3_t3 = Text("后项 (可以是整数、小数或分数)", font=FONT, font_size=22, color=WHITE)
        c3_row = VGroup(c3_t2, c3_m, c3_t3).arrange(RIGHT, buff=0.08)
        c3_content = VGroup(c3_t, c3_row).arrange(DOWN, buff=0.12)
        c3_content.move_to(UP * 0.8)
        self.play(Create(card3), FadeIn(c3_content), run_time=0.5)

        # 卡片4: 比的基本性质
        card4 = Rectangle(
            width=7.8, height=2.2,
            fill_color="#1e1b4b", fill_opacity=0.9,
            stroke_color=COLOR_PROPERTY, stroke_width=2.5
        ).move_to(DOWN * 1.5)
        c4_t = Text("比的基本性质", font=FONT, font_size=28, color=COLOR_PROPERTY)
        c4_c = Text("前项和后项同乘或同除(0除外)", font=FONT, font_size=22, color=WHITE)
        c4_m = MathTex(
            r"(a \times c) : (b \times c) = a : b",
            font_size=38, color=WHITE
        )
        c4_content = VGroup(c4_t, c4_c, c4_m).arrange(DOWN, buff=0.1)
        c4_content.move_to(DOWN * 1.5)
        self.play(Create(card4), FadeIn(c4_content), run_time=0.5)

        # 卡片5: 化简比
        card5 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#3b1f6e", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=2.5
        ).move_to(DOWN * 3.8)
        c5_t = Text("化简比", font=FONT, font_size=28, color=COLOR_ACCENT)
        c5_c = MathTex(
            r"6 : 9 = 2 : 3",
            font_size=44, color=WHITE
        )
        c5_content = VGroup(c5_t, c5_c).arrange(DOWN, buff=0.12)
        c5_content.move_to(DOWN * 3.8)
        self.play(Create(card5), FadeIn(c5_content), run_time=0.5)

        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title,
            card1, c1_content,
            card2, c2_content,
            card3, c3_content,
            card4, c4_content,
            card5, c5_content
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        """片尾: 关注提示"""

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(Transform(self.author_mob, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.5)

        # 装饰: 比的符号
        deco = VGroup(
            MathTex(r"6 : 9", font_size=46, color=COLOR_FRONT).shift(LEFT * 2.5 + DOWN * 2.6),
            MathTex(r"=", font_size=46, color=COLOR_HL).shift(LEFT * 0.5 + DOWN * 2.6),
            MathTex(r"2 : 3", font_size=46, color=COLOR_RESULT).shift(RIGHT * 1.5 + DOWN * 2.6),
        )
        self.play(*[FadeIn(f, scale=0.5) for f in deco], run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=0.8
        )
