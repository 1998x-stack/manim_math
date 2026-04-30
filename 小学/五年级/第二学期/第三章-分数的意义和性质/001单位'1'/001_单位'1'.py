"""
001_单位'1'.py — 单位「1」教学动画

知识点: 单位「1」的概念与分数的意义
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 单位「1」可以是一个物体、一个计量单位、一个整体
  2. 把单位「1」平均分成若干份，取其中几份就是分数
  3. 分数的意义: 3/4 = 把单位「1」平均分成4份取3份
  4. 视觉展示平均分的过程
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
COLOR_UNIT = "#3b82f6"
COLOR_PART = "#22c55e"
COLOR_FRAC = "#f59e0b"
COLOR_HL = "#fbbf24"
COLOR_STEP = "#a78bfa"
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class UnitOneLesson(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_what_is_unit_one()
        self.scene_3_equal_division()
        self.scene_4_fraction_meaning()
        self.scene_5_more_examples()
        self.scene_6_summary()
        self.scene_7_outro()

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "什么是单位「1」？", font=FONT, font_size=48, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "分数从这里开始！", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    def scene_2_what_is_unit_one(self):
        title = Text(
            "单位「1」是什么？", font=FONT, font_size=38,
            color=COLOR_UNIT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "一个物体、一个整体都可以看作单位「1」",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(defn), run_time=0.6)

        # 例子
        examples = [
            ("1个苹果", "一个物体"),
            ("1条线段", "一个计量单位"),
            ("全班同学", "一个整体"),
            ("一堆糖果", "一个集合"),
        ]

        rows = VGroup()
        for item_str, desc_str in examples:
            item_t = Text(item_str, font=FONT, font_size=26, color=COLOR_UNIT, weight=BOLD)
            arrow = MathTex(r"\rightarrow", font_size=24, color=GRAY_A)
            desc_t = Text(desc_str, font=FONT, font_size=22, color=WHITE)
            row = VGroup(item_t, arrow, desc_t).arrange(RIGHT, buff=0.3)
            rows.add(row)

        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.0)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)

        key = Text(
            "都可以用「1」来表示！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, defn, rows, key)), run_time=0.4)

    def scene_3_equal_division(self):
        title = Text(
            "平均分", font=FONT, font_size=38,
            color=COLOR_PART, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        intro = Text(
            "把单位「1」平均分成若干份",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(intro), run_time=0.5)

        # 矩形平均分成4份
        whole_rect = Rectangle(
            width=6.0, height=1.2,
            stroke_color=COLOR_UNIT, stroke_width=3,
            fill_color=COLOR_UNIT, fill_opacity=0.15
        ).move_to(UP * 2.5)
        whole_label = Text("单位「1」", font=FONT, font_size=20, color=COLOR_UNIT).next_to(whole_rect, UP, buff=0.1)
        self.play(Create(whole_rect), FadeIn(whole_label), run_time=0.5)

        # 分割线
        lines = VGroup()
        for i in range(1, 4):
            x = whole_rect.get_left()[0] + i * 1.5
            line = Line(
                np.array([x, whole_rect.get_top()[1], 0]),
                np.array([x, whole_rect.get_bottom()[1], 0]),
                color=WHITE, stroke_width=2
            )
            lines.add(line)

        self.play(Create(lines), run_time=0.6)

        # 标注"平均分成4份"
        div_label = Text(
            "平均分成 4 份", font=FONT, font_size=22, color=COLOR_PART
        ).next_to(whole_rect, DOWN, buff=0.2)
        self.play(FadeIn(div_label), run_time=0.3)

        # 标注每份
        for i in range(4):
            x = whole_rect.get_left()[0] + 0.75 + i * 1.5
            frac = MathTex(r"\frac{1}{4}", font_size=24, color=GRAY_A).move_to(
                np.array([x, whole_rect.get_center()[1], 0])
            )
            self.play(FadeIn(frac), run_time=0.2)

        self.wait(1.0)

        # 取其中3份
        highlight = Rectangle(
            width=4.5, height=1.2,
            stroke_color=COLOR_FRAC, stroke_width=0,
            fill_color=COLOR_FRAC, fill_opacity=0.35
        ).align_to(whole_rect, LEFT).align_to(whole_rect, UP)
        take_label = Text(
            "取其中 3 份", font=FONT, font_size=22, color=COLOR_FRAC
        ).move_to(DOWN * 0.5)
        result = MathTex(r"\frac{3}{4}", font_size=48, color=COLOR_HL).move_to(DOWN * 1.8)

        self.play(FadeIn(highlight), run_time=0.5)
        self.play(FadeIn(take_label), Write(result), run_time=0.6)
        self.play(Indicate(result, scale_factor=1.1, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, intro, whole_rect, whole_label, lines, div_label,
            highlight, take_label, result
        )), run_time=0.4)

    def scene_4_fraction_meaning(self):
        title = Text(
            "分数的意义", font=FONT, font_size=38,
            color=COLOR_FRAC, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 分数各部分
        frac = MathTex(r"\frac{3}{4}", font_size=72, color=COLOR_HL).move_to(UP * 3.0)
        self.play(Write(frac), run_time=0.6)

        # 分子说明
        num_label = Text("分子 = 3", font=FONT, font_size=24, color=COLOR_FRAC)
        num_desc = Text("取了几份", font=FONT, font_size=20, color=GRAY_A)
        num_group = VGroup(num_label, num_desc).arrange(RIGHT, buff=0.2).move_to(UP * 1.5)

        den_label = Text("分母 = 4", font=FONT, font_size=24, color=COLOR_UNIT)
        den_desc = Text("平均分成几份", font=FONT, font_size=20, color=GRAY_A)
        den_group = VGroup(den_label, den_desc).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)

        line_label = Text("分数线", font=FONT, font_size=24, color=WHITE)
        line_desc = Text("= 平均分", font=FONT, font_size=20, color=GRAY_A)
        line_group = VGroup(line_label, line_desc).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)

        self.play(FadeIn(num_group, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(den_group, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(line_group, shift=RIGHT * 0.2), run_time=0.5)

        meaning = Text(
            "把单位「1」平均分成4份，取其中3份",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        meaning_box = SurroundingRectangle(meaning, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(meaning, shift=UP * 0.2), Create(meaning_box), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title, frac, num_group, den_group, line_group, meaning, meaning_box
        )), run_time=0.4)

    def scene_5_more_examples(self):
        title = Text(
            "更多例子", font=FONT, font_size=36,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        examples = [
            (r"\frac{1}{2}", "一半", "把「1」平均分成2份取1份"),
            (r"\frac{2}{3}", "三分之二", "把「1」平均分成3份取2份"),
            (r"\frac{5}{8}", "八分之五", "把「1」平均分成8份取5份"),
        ]

        rows = VGroup()
        for frac_tex, read_str, meaning_str in examples:
            frac = MathTex(frac_tex, font_size=38, color=COLOR_HL)
            read_t = Text(read_str, font=FONT, font_size=22, color=WHITE)
            meaning_t = Text(meaning_str, font=FONT, font_size=18, color=GRAY_A)
            col = VGroup(
                VGroup(frac, read_t).arrange(RIGHT, buff=0.3),
                meaning_t
            ).arrange(DOWN, buff=0.15)
            rows.add(col)

        rows.arrange(DOWN, buff=0.7).move_to(UP * 1.5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        key = Text(
            "分母决定份数，分子决定取几份",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, rows, key)), run_time=0.4)

    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.0, height=6.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.3)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "单位「1」与分数", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 单位「1」：一个物体或整体", font=FONT, font_size=22, color=COLOR_UNIT),
            Text("2. 平均分：等分成若干份", font=FONT, font_size=22, color=COLOR_PART),
            Text("3. 分数：取其中的几份", font=FONT, font_size=22, color=COLOR_FRAC),
            Text("4. 分母=份数，分子=取几份", font=FONT, font_size=22, color=WHITE),
            Text("5. 分数线表示平均分", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "理解单位「1」是学分数的基础！",
            font=FONT, font_size=22, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

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
        self.play(FadeOut(VGroup(self.author_mob, author_id, follow)), run_time=0.8)


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql "001_单位'1'.py" UnitOneLesson
#   高质量:    manim -qh  "001_单位'1'.py" UnitOneLesson
#   4K:        manim -qk  "001_单位'1'.py" UnitOneLesson
# ======================================================================
