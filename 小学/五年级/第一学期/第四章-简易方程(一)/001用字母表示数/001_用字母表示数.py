"""
001_用字母表示数.py — 用字母表示数 教学动画

知识点: 用字母表示运算定律、计算公式、数量关系，以及简写规则
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 字母表示运算定律: a+b=b+a (加法交换律)
  2. 字母表示公式: S=ab (长方形面积), v=s/t (速度)
  3. 简写规则:
     - 数字在字母前: a×5 → 5a
     - 省略乘号: 2×a → 2a, a×b → ab
     - 省略1: 1×b → b
     - 相同字母相乘: a×a → a²
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
COLOR_LAW = "#3b82f6"           # 蓝色运算定律
COLOR_FORMULA = "#22c55e"       # 绿色公式
COLOR_LETTER = "#f59e0b"        # 橙色字母
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_RULE = "#a78bfa"          # 紫色简写规则
COLOR_WARN = "#ef4444"          # 红色重点
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
COLOR_ARROW = "#ec4899"         # 粉色箭头
FONT = "Noto Sans CJK SC"


class LetterRepresentLesson(Scene):
    """
    用字母表示数 教学动画
    场景:
      1. 开场钩子
      2. 字母表示运算定律
      3. 字母表示公式
      4. 简写规则
      5. 总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_laws()
        self.scene_3_formulas()
        self.scene_4_simplification()
        self.scene_5_summary()
        self.scene_6_outro()

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
            "用字母表示数", font=FONT, font_size=48,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "数学从此更简洁！", font=FONT, font_size=36,
            color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        # 展示字母从数字中"诞生"
        nums = VGroup(
            MathTex("1,\\ 2,\\ 3,\\ \\dots", font_size=48, color=GRAY_A),
        ).move_to(UP * 1.5)
        self.play(Write(nums), run_time=0.6)

        arrow_down = Arrow(
            UP * 0.6, DOWN * 0.4,
            color=COLOR_ARROW, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(Create(arrow_down), run_time=0.4)

        letters = MathTex(
            "a,\\ b,\\ c,\\ x,\\ y,\\ \\dots",
            font_size=52, color=COLOR_LETTER
        ).move_to(DOWN * 0.5)
        self.play(Write(letters), run_time=0.8)

        hint = Text(
            "用字母代替任意的数！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(hook1, hook2, nums, arrow_down, letters, hint)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 字母表示运算定律
    # ------------------------------------------------------------------

    def scene_2_laws(self):
        title = Text(
            "字母表示运算定律", font=FONT, font_size=36,
            color=COLOR_LAW, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 加法交换律
        law1_label = Text(
            "加法交换律", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.8)
        law1_eq = MathTex(
            r"a + b = b + a", font_size=44, color=COLOR_LAW
        ).move_to(UP * 2.8)

        self.play(Write(law1_label), run_time=0.4)
        self.play(Write(law1_eq), run_time=0.7)
        self.wait(0.3)

        # 加法结合律
        law2_label = Text(
            "加法结合律", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.5)
        law2_eq = MathTex(
            r"(a + b) + c = a + (b + c)",
            font_size=38, color=COLOR_LAW
        ).move_to(UP * 0.5)

        self.play(Write(law2_label), run_time=0.4)
        self.play(Write(law2_eq), run_time=0.7)
        self.wait(0.3)

        # 乘法交换律
        law3_label = Text(
            "乘法交换律", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 0.8)
        law3_eq = MathTex(
            r"a \times b = b \times a",
            font_size=44, color=COLOR_LAW
        ).move_to(DOWN * 1.8)

        self.play(Write(law3_label), run_time=0.4)
        self.play(Write(law3_eq), run_time=0.7)
        self.wait(0.3)

        # 乘法分配律
        law4_label = Text(
            "乘法分配律", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.1)
        law4_eq = MathTex(
            r"a \times (b + c) = a \times b + a \times c",
            font_size=30, color=COLOR_LAW
        ).move_to(DOWN * 4.1)

        self.play(Write(law4_label), run_time=0.4)
        self.play(Write(law4_eq), run_time=0.8)
        self.wait(0.3)

        # 好处提示
        benefit = Text(
            "简洁、通用、一目了然",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(benefit, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, law1_label, law1_eq,
                law2_label, law2_eq,
                law3_label, law3_eq,
                law4_label, law4_eq, benefit
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 字母表示公式
    # ------------------------------------------------------------------

    def scene_3_formulas(self):
        title = Text(
            "字母表示公式", font=FONT, font_size=36,
            color=COLOR_FORMULA, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 长方形面积
        rect = Rectangle(
            width=3.5, height=2.0,
            color=COLOR_FORMULA, fill_color=COLOR_FORMULA,
            fill_opacity=0.2, stroke_width=3
        ).move_to(UP * 2.5)

        label_a = MathTex("a", font_size=36, color=COLOR_LETTER)
        label_a.next_to(rect, DOWN, buff=0.2)
        label_b = MathTex("b", font_size=36, color=COLOR_LETTER)
        label_b.next_to(rect, RIGHT, buff=0.2)

        self.play(Create(rect), run_time=0.6)
        self.play(FadeIn(label_a), FadeIn(label_b), run_time=0.4)

        f1_label = Text(
            "长方形面积：", font=FONT, font_size=24, color=WHITE
        )
        f1_eq = MathTex(r"S = a \times b", font_size=40, color=COLOR_FORMULA)
        f1 = VGroup(f1_label, f1_eq).arrange(RIGHT, buff=0.15).move_to(UP * 0.3)
        self.play(Write(f1), run_time=0.7)
        self.wait(0.5)

        # 速度公式
        f2_label = Text(
            "速度公式：", font=FONT, font_size=24, color=WHITE
        )
        f2_eq = MathTex(r"v = s \div t", font_size=40, color=COLOR_FORMULA)
        f2 = VGroup(f2_label, f2_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.2)
        self.play(Write(f2), run_time=0.7)
        self.wait(0.3)

        # 路程公式
        f3_label = Text(
            "路程公式：", font=FONT, font_size=24, color=WHITE
        )
        f3_eq = MathTex(r"s = v \times t", font_size=40, color=COLOR_FORMULA)
        f3 = VGroup(f3_label, f3_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.7)
        self.play(Write(f3), run_time=0.7)
        self.wait(0.3)

        benefit = Text(
            "公式用字母表示，适用于所有情况",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(benefit, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, rect, label_a, label_b,
                f1, f2, f3, benefit
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 简写规则
    # ------------------------------------------------------------------

    def scene_4_simplification(self):
        title = Text(
            "简写规则", font=FONT, font_size=38,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 规则1: 省略乘号，数字在前
        r1_title = Text(
            "数字在字母前面，省略乘号",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(r1_title), run_time=0.5)

        r1_before = MathTex(r"a \times 5", font_size=42, color=GRAY_A)
        r1_arrow = MathTex(r"\Rightarrow", font_size=42, color=COLOR_ARROW)
        r1_after = MathTex(r"5a", font_size=48, color=COLOR_HL)
        r1_eq = VGroup(r1_before, r1_arrow, r1_after).arrange(
            RIGHT, buff=0.4
        ).move_to(UP * 2.8)
        self.play(Write(r1_before), run_time=0.4)
        self.play(Write(r1_arrow), run_time=0.3)
        self.play(Write(r1_after), run_time=0.4)
        self.play(
            Indicate(r1_after, scale_factor=1.1, color=COLOR_HL),
            run_time=0.4
        )
        self.wait(0.3)

        # 规则2: 省略乘号 (2×a → 2a)
        r2_before = MathTex(r"2 \times a", font_size=42, color=GRAY_A)
        r2_arrow = MathTex(r"\Rightarrow", font_size=42, color=COLOR_ARROW)
        r2_after = MathTex(r"2a", font_size=48, color=COLOR_HL)
        r2_eq = VGroup(r2_before, r2_arrow, r2_after).arrange(
            RIGHT, buff=0.4
        ).move_to(UP * 1.5)
        self.play(Write(r2_before), run_time=0.4)
        self.play(Write(r2_arrow), run_time=0.3)
        self.play(Write(r2_after), run_time=0.4)
        self.wait(0.3)

        # 规则3: 字母与字母相乘，省略乘号
        r3_title = Text(
            "字母与字母相乘，省略乘号",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 0.2)
        self.play(Write(r3_title), run_time=0.5)

        r3_before = MathTex(r"a \times b", font_size=42, color=GRAY_A)
        r3_arrow = MathTex(r"\Rightarrow", font_size=42, color=COLOR_ARROW)
        r3_after = MathTex(r"ab", font_size=48, color=COLOR_HL)
        r3_eq = VGroup(r3_before, r3_arrow, r3_after).arrange(
            RIGHT, buff=0.4
        ).move_to(DOWN * 0.9)
        self.play(Write(r3_before), run_time=0.4)
        self.play(Write(r3_arrow), run_time=0.3)
        self.play(Write(r3_after), run_time=0.4)
        self.wait(0.3)

        # 规则4: 相同字母相乘 (a×a → a²)
        r4_title = Text(
            "相同字母相乘，用平方表示",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 2.2)
        self.play(Write(r4_title), run_time=0.5)

        r4_before = MathTex(r"a \times a", font_size=42, color=GRAY_A)
        r4_arrow = MathTex(r"\Rightarrow", font_size=42, color=COLOR_ARROW)
        r4_after = MathTex(r"a^{2}", font_size=48, color=COLOR_HL)
        r4_eq = VGroup(r4_before, r4_arrow, r4_after).arrange(
            RIGHT, buff=0.4
        ).move_to(DOWN * 3.3)
        self.play(Write(r4_before), run_time=0.4)
        self.play(Write(r4_arrow), run_time=0.3)
        self.play(Write(r4_after), run_time=0.4)
        self.play(
            Indicate(r4_after, scale_factor=1.1, color=COLOR_HL),
            run_time=0.4
        )
        self.wait(0.3)

        # 规则5: 1省略 (1×b → b)
        r5_title = Text(
            "1与字母相乘，省略1",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 4.6)
        self.play(Write(r5_title), run_time=0.5)

        r5_before = MathTex(r"1 \times b", font_size=42, color=GRAY_A)
        r5_arrow = MathTex(r"\Rightarrow", font_size=42, color=COLOR_ARROW)
        r5_after = MathTex(r"b", font_size=48, color=COLOR_HL)
        r5_eq = VGroup(r5_before, r5_arrow, r5_after).arrange(
            RIGHT, buff=0.4
        ).move_to(DOWN * 5.7)
        self.play(Write(r5_before), run_time=0.4)
        self.play(Write(r5_arrow), run_time=0.3)
        self.play(Write(r5_after), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title,
                r1_title, r1_eq,
                r2_eq,
                r3_title, r3_eq,
                r4_title, r4_eq,
                r5_title, r5_eq,
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=8.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.3)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "用字母表示数", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 字母可以表示任意的数",
                 font=FONT, font_size=22, color=WHITE),
            Text("2. 用字母表示运算定律",
                 font=FONT, font_size=22, color=COLOR_LAW),
            Text("    a+b = b+a",
                 font=FONT, font_size=20, color=GRAY_A),
            Text("3. 用字母表示公式",
                 font=FONT, font_size=22, color=COLOR_FORMULA),
            Text("    S=ab   v=s/t",
                 font=FONT, font_size=20, color=GRAY_A),
            Text("4. 简写规则：",
                 font=FONT, font_size=22, color=COLOR_RULE),
            Text("    数字在前，省略乘号",
                 font=FONT, font_size=20, color=GRAY_A),
            Text("    a*a 写成 a\u00b2，省略1",
                 font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.35)
            self.wait(0.15)

        tip = Text(
            "记住：数字在前，乘号省略！",
            font=FONT, font_size=24, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
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
#   快速预览:  manim -pql 001_用字母表示数.py LetterRepresentLesson
#   高质量:    manim -qh  001_用字母表示数.py LetterRepresentLesson
#   4K:        manim -qk  001_用字母表示数.py LetterRepresentLesson
# ======================================================================
