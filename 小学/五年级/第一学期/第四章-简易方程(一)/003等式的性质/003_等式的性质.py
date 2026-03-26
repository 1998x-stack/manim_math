"""
003_等式的性质.py — 等式的性质 教学动画

知识点: 等式的两条基本性质
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 性质一: 等式两边同时加上或减去同一个数，等式仍然成立
  2. 性质二: 等式两边同时乘以或除以同一个非零数，等式仍然成立
  3. 视觉: 天平/平衡隐喻
  4. 举例: 若 a=b, 则 a+3=b+3; 若 a=b, 则 2a=2b
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
COLOR_BALANCE = "#3b82f6"       # 蓝色天平
COLOR_EQ = "#22c55e"            # 绿色等式
COLOR_ADD = "#f59e0b"           # 橙色加减
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_MUL = "#a78bfa"           # 紫色乘除
COLOR_WARN = "#ef4444"          # 红色重点
COLOR_PROP = "#06b6d4"          # 青色性质标题
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
FONT = "Noto Sans CJK SC"


class EqualityPropertyLesson(Scene):
    """
    等式的性质教学动画
    场景:
      1. 开场钩子
      2. 性质一: 加减同一个数
      3. 性质二: 乘除同一个非零数
      4. 举例应用
      5. 总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_property_add_sub()
        self.scene_3_property_mul_div()
        self.scene_4_examples()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建天平
    # ------------------------------------------------------------------

    def _create_balance(self, center=ORIGIN, beam_width=5.0):
        """创建一个简易天平，返回 (整体VGroup, 左盘中心, 右盘中心, 横梁)"""
        # 底座三角形
        base_tri = Triangle(
            fill_color=COLOR_BALANCE, fill_opacity=0.6,
            stroke_color=COLOR_BALANCE, stroke_width=2
        ).scale(0.4).move_to(center + DOWN * 0.6)

        # 支柱
        pillar = Line(
            center + DOWN * 0.35, center + UP * 0.5,
            color=COLOR_BALANCE, stroke_width=4
        )

        # 横梁
        half_w = beam_width / 2
        beam = Line(
            center + UP * 0.5 + LEFT * half_w,
            center + UP * 0.5 + RIGHT * half_w,
            color=COLOR_BALANCE, stroke_width=4
        )

        # 左右吊绳
        rope_len = 0.6
        left_rope = Line(
            beam.get_left(), beam.get_left() + DOWN * rope_len,
            color=GRAY_B, stroke_width=2
        )
        right_rope = Line(
            beam.get_right(), beam.get_right() + DOWN * rope_len,
            color=GRAY_B, stroke_width=2
        )

        # 左右盘
        pan_w = 1.6
        left_pan = Line(
            left_rope.get_end() + LEFT * pan_w / 2,
            left_rope.get_end() + RIGHT * pan_w / 2,
            color=GRAY_A, stroke_width=3
        )
        right_pan = Line(
            right_rope.get_end() + LEFT * pan_w / 2,
            right_rope.get_end() + RIGHT * pan_w / 2,
            color=GRAY_A, stroke_width=3
        )

        balance = VGroup(base_tri, pillar, beam, left_rope, right_rope, left_pan, right_pan)
        left_center = left_pan.get_center() + UP * 0.35
        right_center = right_pan.get_center() + UP * 0.35

        return balance, left_center, right_center, beam

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "等式两边动了", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "天平还平衡吗？", font=FONT, font_size=48, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 天平
        balance, lc, rc, beam = self._create_balance(center=UP * 0.5, beam_width=5.0)
        self.play(FadeIn(balance, shift=UP * 0.3), run_time=0.8)

        # 左右放等量
        left_val = MathTex("5", font_size=44, color=COLOR_ADD).move_to(lc)
        right_val = MathTex("5", font_size=44, color=COLOR_ADD).move_to(rc)
        eq_sign = MathTex("=", font_size=52, color=COLOR_EQ).move_to(UP * 0.5)

        self.play(FadeIn(left_val), FadeIn(right_val), FadeIn(eq_sign), run_time=0.6)
        self.wait(0.5)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 2.0)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(hook1, hook2, balance, left_val, right_val, eq_sign, q)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 性质一 — 加减同一个数
    # ------------------------------------------------------------------

    def scene_2_property_add_sub(self):
        title = Text(
            "性质一", font=FONT, font_size=38,
            color=COLOR_PROP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 性质文字
        prop_text1 = Text(
            "等式两边同时加上或减去",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.3)
        prop_text2 = Text(
            "同一个数，等式仍然成立",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.7)
        self.play(Write(prop_text1), run_time=0.5)
        self.play(Write(prop_text2), run_time=0.5)

        # 天平演示加法
        balance, lc, rc, beam = self._create_balance(center=UP * 1.0, beam_width=5.0)
        self.play(FadeIn(balance), run_time=0.5)

        # 初始: a = b
        left_a = MathTex("a", font_size=42, color=WHITE).move_to(lc)
        right_b = MathTex("b", font_size=42, color=WHITE).move_to(rc)
        eq_sign = MathTex("=", font_size=48, color=COLOR_EQ).move_to(UP * 1.0)
        self.play(FadeIn(left_a), FadeIn(right_b), FadeIn(eq_sign), run_time=0.5)

        init_eq = MathTex("a = b", font_size=40, color=COLOR_EQ).move_to(DOWN * 1.0)
        self.play(Write(init_eq), run_time=0.5)
        self.wait(0.5)

        # 加法: 两边 +3
        add_label = Text(
            "两边同时 +3", font=FONT, font_size=26, color=COLOR_ADD, weight=BOLD
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(add_label, shift=UP * 0.2), run_time=0.5)

        # 左边加 +3
        plus3_left = MathTex("+3", font_size=36, color=COLOR_ADD).move_to(lc + RIGHT * 0.7)
        plus3_right = MathTex("+3", font_size=36, color=COLOR_ADD).move_to(rc + RIGHT * 0.7)
        self.play(
            FadeIn(plus3_left, shift=DOWN * 0.3),
            FadeIn(plus3_right, shift=DOWN * 0.3),
            run_time=0.6
        )

        result_eq = MathTex("a + 3 = b + 3", font_size=42, color=COLOR_HL)
        result_eq.move_to(DOWN * 3.5)
        self.play(Write(result_eq), run_time=0.6)
        self.play(Indicate(result_eq, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(0.5)

        # 减法: 两边 -c
        sub_label = Text(
            "两边同时 -c", font=FONT, font_size=26, color=COLOR_ADD, weight=BOLD
        ).move_to(DOWN * 2.2)
        sub_eq = MathTex("a - c = b - c", font_size=42, color=COLOR_HL)
        sub_eq.move_to(DOWN * 5.0)

        self.play(
            FadeOut(add_label),
            FadeIn(sub_label, shift=UP * 0.2),
            run_time=0.4
        )
        self.play(Write(sub_eq), run_time=0.6)
        self.wait(0.5)

        # 天平依然平衡
        still = Text(
            "天平依然平衡！", font=FONT, font_size=28,
            color=COLOR_EQ, weight=BOLD
        ).move_to(DOWN * 6.5)
        self.play(FadeIn(still, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(
                title, prop_text1, prop_text2, balance,
                left_a, right_b, eq_sign, plus3_left, plus3_right,
                init_eq, sub_label, result_eq, sub_eq, still
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 性质二 — 乘除同一个非零数
    # ------------------------------------------------------------------

    def scene_3_property_mul_div(self):
        title = Text(
            "性质二", font=FONT, font_size=38,
            color=COLOR_PROP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 性质文字
        prop_text1 = Text(
            "等式两边同时乘以或除以",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.3)
        prop_text2 = Text(
            "同一个非零数，等式仍然成立",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.7)
        self.play(Write(prop_text1), run_time=0.5)
        self.play(Write(prop_text2), run_time=0.5)

        # 天平演示乘法
        balance, lc, rc, beam = self._create_balance(center=UP * 1.0, beam_width=5.0)
        self.play(FadeIn(balance), run_time=0.5)

        # 初始: a = b
        left_a = MathTex("a", font_size=42, color=WHITE).move_to(lc)
        right_b = MathTex("b", font_size=42, color=WHITE).move_to(rc)
        eq_sign = MathTex("=", font_size=48, color=COLOR_EQ).move_to(UP * 1.0)
        self.play(FadeIn(left_a), FadeIn(right_b), FadeIn(eq_sign), run_time=0.5)

        init_eq = MathTex("a = b", font_size=40, color=COLOR_EQ).move_to(DOWN * 1.0)
        self.play(Write(init_eq), run_time=0.5)
        self.wait(0.5)

        # 乘法: 两边 ×2
        mul_label = Text(
            "两边同时 x2", font=FONT, font_size=26, color=COLOR_MUL, weight=BOLD
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(mul_label, shift=UP * 0.2), run_time=0.5)

        times2_left = MathTex(r"\times 2", font_size=36, color=COLOR_MUL).move_to(lc + RIGHT * 0.8)
        times2_right = MathTex(r"\times 2", font_size=36, color=COLOR_MUL).move_to(rc + RIGHT * 0.8)
        self.play(
            FadeIn(times2_left, shift=DOWN * 0.3),
            FadeIn(times2_right, shift=DOWN * 0.3),
            run_time=0.6
        )

        result_eq = MathTex("2a = 2b", font_size=44, color=COLOR_HL)
        result_eq.move_to(DOWN * 3.5)
        self.play(Write(result_eq), run_time=0.6)
        self.play(Indicate(result_eq, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(0.5)

        # 除法提示
        div_label = Text(
            "两边同时 /c (c!=0)", font=FONT, font_size=24, color=COLOR_MUL, weight=BOLD
        ).move_to(DOWN * 2.2)
        div_eq = MathTex(r"\frac{a}{c} = \frac{b}{c}", font_size=44, color=COLOR_HL)
        div_eq.move_to(DOWN * 5.0)

        self.play(
            FadeOut(mul_label),
            FadeIn(div_label, shift=UP * 0.2),
            run_time=0.4
        )
        self.play(Write(div_eq), run_time=0.6)
        self.wait(0.5)

        # 警告: 除数不能为0
        warn = Text(
            "注意：除数不能为 0 ！",
            font=FONT, font_size=26, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 6.5)
        warn_box = SurroundingRectangle(
            warn, color=COLOR_WARN, stroke_width=2, buff=0.15, corner_radius=0.1
        )
        self.play(FadeIn(warn, shift=UP * 0.2), Create(warn_box), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(
                title, prop_text1, prop_text2, balance,
                left_a, right_b, eq_sign, times2_left, times2_right,
                init_eq, div_label, result_eq, div_eq, warn, warn_box
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 举例应用
    # ------------------------------------------------------------------

    def scene_4_examples(self):
        title = Text(
            "举例验证", font=FONT, font_size=36,
            color=COLOR_EQ, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 例1: 数字验证加法
        ex1_title = Text(
            "例 1：验证性质一", font=FONT, font_size=26, color=COLOR_PROP
        ).move_to(UP * 4.2)
        self.play(Write(ex1_title), run_time=0.4)

        ex1_line1_label = Text("已知：", font=FONT, font_size=22, color=GRAY_A)
        ex1_line1_math = MathTex("10 = 10", font_size=36, color=WHITE)
        ex1_g1 = VGroup(ex1_line1_label, ex1_line1_math).arrange(RIGHT, buff=0.15).move_to(UP * 3.2)
        self.play(FadeIn(ex1_g1), run_time=0.5)

        ex1_line2_label = Text("两边 +5：", font=FONT, font_size=22, color=COLOR_ADD)
        ex1_line2_math = MathTex("10 + 5 = 10 + 5", font_size=36, color=WHITE)
        ex1_g2 = VGroup(ex1_line2_label, ex1_line2_math).arrange(RIGHT, buff=0.15).move_to(UP * 2.2)
        self.play(FadeIn(ex1_g2, shift=UP * 0.2), run_time=0.5)

        ex1_line3_math = MathTex("15 = 15", font_size=40, color=COLOR_EQ)
        ex1_check = MathTex(r"\checkmark", font_size=40, color=COLOR_EQ)
        ex1_g3 = VGroup(ex1_line3_math, ex1_check).arrange(RIGHT, buff=0.2).move_to(UP * 1.2)
        self.play(Write(ex1_g3), run_time=0.6)
        self.play(Indicate(ex1_g3, scale_factor=1.05, color=COLOR_EQ), run_time=0.4)
        self.wait(0.5)

        # 例2: 字母验证乘法
        ex2_title = Text(
            "例 2：验证性质二", font=FONT, font_size=26, color=COLOR_PROP
        ).move_to(DOWN * 0.2)
        self.play(Write(ex2_title), run_time=0.4)

        ex2_line1_label = Text("已知：", font=FONT, font_size=22, color=GRAY_A)
        ex2_line1_math = MathTex("a = b", font_size=36, color=WHITE)
        ex2_g1 = VGroup(ex2_line1_label, ex2_line1_math).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.2)
        self.play(FadeIn(ex2_g1), run_time=0.5)

        ex2_line2_label = Text("两边 x3：", font=FONT, font_size=22, color=COLOR_MUL)
        ex2_line2_math = MathTex(r"a \times 3 = b \times 3", font_size=36, color=WHITE)
        ex2_g2 = VGroup(ex2_line2_label, ex2_line2_math).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.2)
        self.play(FadeIn(ex2_g2, shift=UP * 0.2), run_time=0.5)

        ex2_line3_math = MathTex("3a = 3b", font_size=40, color=COLOR_HL)
        ex2_check = MathTex(r"\checkmark", font_size=40, color=COLOR_HL)
        ex2_g3 = VGroup(ex2_line3_math, ex2_check).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.2)
        self.play(Write(ex2_g3), run_time=0.6)
        self.play(Indicate(ex2_g3, scale_factor=1.05, color=COLOR_HL), run_time=0.4)
        self.wait(0.5)

        # 例3: 解方程应用
        ex3_title = Text(
            "例 3：解方程应用", font=FONT, font_size=26, color=COLOR_PROP
        ).move_to(DOWN * 4.5)
        self.play(Write(ex3_title), run_time=0.4)

        ex3_eq = MathTex("x + 7 = 15", font_size=38, color=WHITE).move_to(DOWN * 5.3)
        self.play(Write(ex3_eq), run_time=0.5)

        ex3_step_label = Text("两边 -7：", font=FONT, font_size=22, color=COLOR_ADD)
        ex3_step_math = MathTex("x + 7 - 7 = 15 - 7", font_size=34, color=WHITE)
        ex3_g_step = VGroup(ex3_step_label, ex3_step_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 6.2)
        self.play(FadeIn(ex3_g_step, shift=UP * 0.2), run_time=0.5)

        ex3_result = MathTex("x = 8", font_size=44, color=COLOR_HL)
        ex3_result.move_to(DOWN * 7.0)
        self.play(Write(ex3_result), run_time=0.6)
        self.play(Indicate(ex3_result, scale_factor=1.1, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, ex1_title, ex1_g1, ex1_g2, ex1_g3,
                ex2_title, ex2_g1, ex2_g2, ex2_g3,
                ex3_title, ex3_eq, ex3_g_step, ex3_result
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "等式的性质", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.5)
        self.play(Write(sum_title), run_time=0.5)

        # 性质一
        p1_title = Text(
            "性质一", font=FONT, font_size=26, color=COLOR_PROP, weight=BOLD
        ).move_to(UP * 2.3 + LEFT * 2.0)
        p1_text = Text(
            "两边加减同一个数，等式成立",
            font=FONT, font_size=20, color=WHITE
        ).move_to(UP * 1.6)
        p1_formula = MathTex(
            r"a = b \;\Rightarrow\; a \pm c = b \pm c",
            font_size=32, color=COLOR_ADD
        ).move_to(UP * 0.8)

        self.play(FadeIn(p1_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(p1_text, shift=RIGHT * 0.3), run_time=0.4)
        self.play(Write(p1_formula), run_time=0.6)
        self.wait(0.3)

        # 分隔线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY, stroke_width=1).move_to(UP * 0.1)
        self.play(Create(sep), run_time=0.3)

        # 性质二
        p2_title = Text(
            "性质二", font=FONT, font_size=26, color=COLOR_PROP, weight=BOLD
        ).move_to(DOWN * 0.7 + LEFT * 2.0)
        p2_text = Text(
            "两边乘除同一个非零数，等式成立",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 1.4)
        p2_formula = MathTex(
            r"a = b \;\Rightarrow\; a \times c = b \times c",
            font_size=32, color=COLOR_MUL
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(p2_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(p2_text, shift=RIGHT * 0.3), run_time=0.4)
        self.play(Write(p2_formula), run_time=0.6)
        self.wait(0.3)

        # 关键提醒
        tip = Text(
            "记住：除数不能为零！",
            font=FONT, font_size=24, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                box, sum_title,
                p1_title, p1_text, p1_formula,
                sep,
                p2_title, p2_text, p2_formula,
                tip
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
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
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 003_等式的性质.py EqualityPropertyLesson
#   高质量:    manim -qh  003_等式的性质.py EqualityPropertyLesson
#   4K:        manim -qk  003_等式的性质.py EqualityPropertyLesson
# ======================================================================
