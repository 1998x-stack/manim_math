"""
分式方程 — 解法与增根 教学动画
Fractional Equations: Solution Method & Extraneous Roots

目标受众 : 八年级 第二学期 第二十一章
格式     : TikTok 竖屏 1080×1920
作者     : 上海初高中数学直通车 @emptyandcalm

例题     : 1/(x-1) = 2/(x²-1)
结论     : x=1 是增根 → 原方程无解

渲染:
  manim -pql fractional_equation_animation.py FractionalEquation   # 快速
  manim -qh  fractional_equation_animation.py FractionalEquation   # 高质量
"""

from manim import *
import numpy as np

# ── 全局：TikTok 竖屏 ────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

CJK  = "PingFang SC"

# ── 配色 ────────────────────────────────────────────────────
BG            = "#1a1a2e"
C_TITLE       = GOLD
C_FRAC        = "#00d4ff"     # 分式蓝
C_LCD         = "#a8e6cf"     # 公分母绿
C_STEP        = "#74b9ff"     # 步骤蓝
C_SOLVE       = "#ffeaa7"     # 整式黄
C_CHECK       = "#55efc4"     # 检验绿
C_BAD         = "#ff6b6b"     # 增根/错误红
C_ARROW       = "#74b9ff"
C_SUB         = GRAY_A
C_AUTHOR      = GRAY_B
C_BOX_FILL    = "#16213e"


# ════════════════════════════════════════════════════════════
class FractionalEquation(Scene):
    """
    七场景分式方程教学动画

    ① 开场钩子
    ② 分式方程定义
    ③ 四步解法总览
    ④ 步骤1+2：找公分母 & 去分母
    ⑤ 步骤3：解整式方程
    ⑥ 步骤4：检验增根（最戏剧化）
    ⑦ 总结 & 片尾
    """

    def construct(self):
        self.camera.background_color = BG
        self.author_bar = self._author_bar()
        self.add(self.author_bar)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_four_steps()
        self.scene4_remove_denom()
        self.scene5_solve_integral()
        self.scene6_verify_extraneous()
        self.scene7_outro()

    # ────────────────────────────────────────────────────────
    # 工具函数
    # ────────────────────────────────────────────────────────

    def _author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=CJK, font_size=18, color=C_AUTHOR
        ).move_to(UP * 7.2)

    def _title(self, text, font_size=38, color=C_TITLE):
        """带底部装饰线的标题"""
        t = Text(text, font=CJK, font_size=font_size, color=color)
        bar = Line(
            t.get_left()  + DOWN * 0.10,
            t.get_right() + DOWN * 0.10,
            color=color, stroke_width=2.5
        )
        return VGroup(t, bar)

    def _rbox(self, mob, color=C_STEP, buff=0.28, fo=0.12):
        """圆角高亮框"""
        return RoundedRectangle(
            width=mob.get_width() + buff * 2,
            height=mob.get_height() + buff * 2,
            corner_radius=0.18,
            color=color, fill_color=color,
            fill_opacity=fo, stroke_width=2
        ).move_to(mob)

    def _step_tag(self, n, label_cn, color=C_STEP):
        """步骤标签: ① + 中文说明"""
        circle = Circle(radius=0.28, color=color,
                        fill_color=color, fill_opacity=0.9, stroke_width=0)
        num = Text(str(n), font=CJK, font_size=20, color=BG,
                   weight=BOLD).move_to(circle)
        text = Text(label_cn, font=CJK, font_size=24, color=color)
        return VGroup(VGroup(circle, num), text).arrange(RIGHT, buff=0.18)

    def _clear(self, *mobs):
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=0.45)

    # ────────────────────────────────────────────────────────
    # Scene 1 — 开场钩子
    # ────────────────────────────────────────────────────────
    def scene1_hook(self):
        hook = Text(
            "遇到分母含 x 的方程怎么办？",
            font=CJK, font_size=29, color=C_SUB
        ).move_to(UP * 5.5)

        # 主方程
        eq = MathTex(
            r"\frac{1}{x-1} = \frac{2}{x^2-1}",
            font_size=62, color=C_FRAC
        ).move_to(UP * 3.5)
        eq_box = self._rbox(eq, color=C_FRAC, buff=0.4, fo=0.08)

        grade = Text(
            "八年级 · 分式方程",
            font=CJK, font_size=22, color=GRAY_B
        ).move_to(UP * 2.0)

        encourage = Text(
            "四步搞定，轻松拿分！",
            font=CJK, font_size=30, color=C_LCD
        ).move_to(UP * 0.5)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.55)
        self.play(Write(eq), run_time=1.1)
        self.play(Create(eq_box), run_time=0.45)
        self.play(FadeIn(grade), run_time=0.35)
        self.wait(0.3)
        self.play(
            eq.animate.set_color(C_TITLE),
            run_time=0.25
        )
        self.play(
            eq.animate.set_color(C_FRAC),
            run_time=0.25
        )
        self.play(FadeIn(encourage, shift=UP * 0.25), run_time=0.5)
        self.wait(0.8)

        self._clear(hook, eq, eq_box, grade, encourage)

    # ────────────────────────────────────────────────────────
    # Scene 2 — 什么是分式方程
    # ────────────────────────────────────────────────────────
    def scene2_definition(self):
        title = self._title("分式方程", font_size=40)
        title.move_to(UP * 6.2)

        defn = Text(
            "分母中含有未知数的方程",
            font=CJK, font_size=27, color=C_SUB
        ).move_to(UP * 5.0)

        # 对比栏
        left_label  = Text("整式方程", font=CJK, font_size=26, color=C_SUB).move_to(UP * 3.5 + LEFT * 2.4)
        right_label = Text("分式方程", font=CJK, font_size=26, color=C_FRAC).move_to(UP * 3.5 + RIGHT * 2.4)
        divider     = DashedLine(UP * 4.3, UP * 1.5, color=GRAY_B, dash_length=0.12).move_to(ORIGIN + UP * 2.9)

        left_eq  = MathTex(r"x^2 - 5x + 6 = 0",  font_size=30, color=C_SUB).move_to(UP * 2.5 + LEFT * 2.3)
        right_eq = MathTex(
            r"\frac{1}{x-1} = \frac{2}{x^2-1}",
            font_size=30, color=C_FRAC
        ).move_to(UP * 2.5 + RIGHT * 2.3)

        left_note  = Text("分母无 x", font=CJK, font_size=20, color=GRAY_B).move_to(UP * 1.6 + LEFT * 2.3)
        right_note = Text("分母含 x  ✓", font=CJK, font_size=20, color=C_FRAC).move_to(UP * 1.6 + RIGHT * 2.3)

        # 关键提示
        key = Text(
            "增根检验是分式方程独有的步骤！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(UP * 0.3)
        key_box = self._rbox(key, color=C_BAD, buff=0.22, fo=0.07)

        self.play(Write(title[0]), Create(title[1]), run_time=0.6)
        self.play(FadeIn(defn, shift=DOWN * 0.2), run_time=0.45)
        self.play(
            FadeIn(left_label), FadeIn(right_label),
            Create(divider), run_time=0.55
        )
        self.play(FadeIn(left_eq), FadeIn(right_eq), run_time=0.5)
        self.play(FadeIn(left_note), FadeIn(right_note), run_time=0.4)
        self.wait(0.3)
        self.play(Create(key_box), FadeIn(key), run_time=0.55)
        self.wait(1.0)

        self._clear(title, defn, left_label, right_label, divider,
                    left_eq, right_eq, left_note, right_note, key_box, key)

    # ────────────────────────────────────────────────────────
    # Scene 3 — 四步解法总览
    # ────────────────────────────────────────────────────────
    def scene3_four_steps(self):
        title = self._title("解题四步法", font_size=38)
        title.move_to(UP * 6.2)

        steps_data = [
            (1, "找最简公分母",   C_LCD,   UP * 4.5),
            (2, "去分母",        C_STEP,  UP * 3.2),
            (3, "解整式方程",    C_SOLVE, UP * 1.9),
            (4, "检验（增根）",  C_BAD,   UP * 0.6),
        ]

        step_mobs = []
        for n, label, color, pos in steps_data:
            s = self._step_tag(n, label, color).move_to(pos)
            step_mobs.append(s)

        # 箭头连接各步
        arrows = VGroup(*[
            Arrow(
                step_mobs[i].get_bottom() + DOWN * 0.05,
                step_mobs[i+1].get_top()  + UP   * 0.05,
                color=GRAY_B, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.22, buff=0.08
            )
            for i in range(3)
        ])

        # 步骤4 特别强调框
        step4_box = self._rbox(step_mobs[3], color=C_BAD, buff=0.22, fo=0.1)

        key_note = Text(
            "第4步最重要，忘了就丢分！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(DOWN * 1.0)

        self.play(Write(title[0]), Create(title[1]), run_time=0.55)
        for i, s in enumerate(step_mobs):
            self.play(FadeIn(s, shift=RIGHT * 0.35), run_time=0.35)
            if i < 3:
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.play(Create(step4_box), run_time=0.4)
        self.play(
            step_mobs[3].animate.set_color(C_TITLE),
            run_time=0.25
        )
        self.play(
            step_mobs[3].animate.set_color(C_BAD),
            run_time=0.25
        )
        self.play(FadeIn(key_note), run_time=0.4)
        self.wait(1.0)

        self._clear(title, *step_mobs, arrows, step4_box, key_note)

    # ────────────────────────────────────────────────────────
    # Scene 4 — 步骤1+2：找公分母 & 去分母
    # ────────────────────────────────────────────────────────
    def scene4_remove_denom(self):
        # 例题标题
        eg_title = self._title("例题", font_size=34, color=C_TITLE)
        eg_title.move_to(UP * 6.5)

        # 原方程（保留整个场景）
        orig_eq = MathTex(
            r"\frac{1}{x-1} = \frac{2}{x^2-1}",
            font_size=52, color=C_FRAC
        ).move_to(UP * 5.2)
        orig_box = self._rbox(orig_eq, color=C_FRAC, buff=0.3, fo=0.07)

        self.play(Write(eg_title[0]), Create(eg_title[1]), run_time=0.5)
        self.play(Write(orig_eq), Create(orig_box), run_time=0.8)
        self.wait(0.35)

        # ── 步骤1：找最简公分母 ──────────────────────────────
        s1_tag = self._step_tag(1, "找最简公分母", C_LCD).move_to(UP * 3.8)
        self.play(FadeIn(s1_tag, shift=RIGHT * 0.3), run_time=0.45)

        # 标注两个分母
        denom1_arrow = Arrow(
            UP * 4.9 + LEFT * 2.3,
            UP * 4.2 + LEFT * 2.5,
            color=C_LCD, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.28, buff=0.05
        )
        denom2_arrow = Arrow(
            UP * 4.9 + RIGHT * 2.0,
            UP * 4.2 + RIGHT * 2.2,
            color=C_LCD, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.28, buff=0.05
        )
        denom1_label = MathTex(r"x-1", font_size=28, color=C_LCD).move_to(UP * 5.3 + LEFT * 2.5)
        denom2_label = MathTex(r"x^2-1", font_size=28, color=C_LCD).move_to(UP * 5.3 + RIGHT * 2.2)

        self.play(
            FadeIn(denom1_label), GrowArrow(denom1_arrow),
            FadeIn(denom2_label), GrowArrow(denom2_arrow),
            run_time=0.6
        )
        self.wait(0.3)

        # 分解 x²-1
        factor_label = Text("分解：", font=CJK, font_size=24, color=C_SUB)
        factor_eq    = MathTex(r"x^2-1 = (x-1)(x+1)", font_size=34, color=C_LCD)
        factor_group = VGroup(factor_label, factor_eq).arrange(RIGHT, buff=0.2)
        factor_group.move_to(UP * 2.8)
        factor_box = self._rbox(factor_group, color=C_LCD, buff=0.22, fo=0.08)

        self.play(FadeIn(factor_label), Write(factor_eq), Create(factor_box), run_time=0.75)
        self.wait(0.3)

        # LCD 展示
        lcd_label = Text("最简公分母：", font=CJK, font_size=24, color=C_LCD)
        lcd_eq    = MathTex(r"x^2 - 1", font_size=38, color=C_TITLE)
        lcd_group = VGroup(lcd_label, lcd_eq).arrange(RIGHT, buff=0.2)
        lcd_group.move_to(UP * 1.5)
        lcd_box = self._rbox(lcd_group, color=C_TITLE, buff=0.28, fo=0.12)

        self.play(
            FadeIn(lcd_label), Write(lcd_eq),
            Create(lcd_box), run_time=0.65
        )
        self.wait(0.4)

        # ── 步骤2：两边同乘 LCD ──────────────────────────────
        s2_tag = self._step_tag(2, "两边同乘最简公分母", C_STEP).move_to(UP * 0.3)
        self.play(FadeIn(s2_tag, shift=RIGHT * 0.3), run_time=0.45)

        # 乘法标注
        mult_note = Text(
            "×(x²-1) 后，约分化简",
            font=CJK, font_size=24, color=C_STEP
        ).move_to(DOWN * 0.7)
        self.play(FadeIn(mult_note), run_time=0.4)
        self.wait(0.35)

        # 结果：整式方程
        integral_result = MathTex(
            r"(x+1) = 2",
            font_size=52, color=C_SOLVE
        ).move_to(DOWN * 2.0)
        integral_box = self._rbox(integral_result, color=C_SOLVE, buff=0.32, fo=0.1)

        arrive_arrow = Arrow(
            UP * 0.0, DOWN * 1.4,
            color=C_ARROW, stroke_width=3,
            max_tip_length_to_length_ratio=0.22, buff=0.1
        )

        self.play(GrowArrow(arrive_arrow), run_time=0.45)
        self.play(Write(integral_result), Create(integral_box), run_time=0.75)
        self.wait(0.4)

        # 整式方程标注
        integral_label = Text(
            "整式方程！",
            font=CJK, font_size=22, color=C_SOLVE
        ).next_to(integral_box, RIGHT, buff=0.25)
        self.play(FadeIn(integral_label), run_time=0.35)
        self.wait(0.9)

        # 清场（保留 orig_eq 和 orig_box 留给下一场）
        self._clear(
            eg_title, s1_tag, denom1_arrow, denom2_arrow,
            denom1_label, denom2_label,
            factor_group, factor_box,
            lcd_group, lcd_box,
            s2_tag, mult_note, arrive_arrow,
            integral_label
        )

        # 把整式方程移上去作为下一场的起点
        self.play(
            integral_result.animate.move_to(UP * 4.2).set_color(C_SOLVE),
            integral_box.animate.move_to(UP * 4.2),
            orig_eq.animate.move_to(UP * 5.8).scale(0.72),
            orig_box.animate.move_to(UP * 5.8).scale(0.72),
            run_time=0.6
        )
        # 存储供后续场景使用
        self._orig_eq       = orig_eq
        self._orig_box      = orig_box
        self._integral_eq   = integral_result
        self._integral_box  = integral_box

    # ────────────────────────────────────────────────────────
    # Scene 5 — 步骤3：解整式方程
    # ────────────────────────────────────────────────────────
    def scene5_solve_integral(self):
        s3_tag = self._step_tag(3, "解整式方程", C_SOLVE).move_to(UP * 3.0)
        self.play(FadeIn(s3_tag, shift=RIGHT * 0.3), run_time=0.45)

        # x+1 = 2 → x = 1  变换动画
        step_a = MathTex(r"x + 1 = 2", font_size=48, color=C_SOLVE).move_to(UP * 1.6)
        step_b = MathTex(r"x = 2 - 1", font_size=48, color=C_SOLVE).move_to(UP * 0.2)
        step_c = MathTex(r"x = 1",     font_size=56, color=C_TITLE) .move_to(DOWN * 1.4)
        step_c_box = self._rbox(step_c, color=C_TITLE, buff=0.38, fo=0.14)

        arr_ab = Arrow(
            step_a.get_bottom() + DOWN * 0.05,
            step_b.get_top()    + UP   * 0.05,
            color=C_ARROW, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22, buff=0.08
        )
        arr_bc = Arrow(
            step_b.get_bottom() + DOWN * 0.05,
            step_c.get_top()    + UP   * 0.05,
            color=C_ARROW, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22, buff=0.08
        )

        self.play(Write(step_a), run_time=0.6)
        self.play(GrowArrow(arr_ab), run_time=0.35)
        self.play(Write(step_b), run_time=0.55)
        self.play(GrowArrow(arr_bc), run_time=0.35)
        self.play(Write(step_c), Create(step_c_box), run_time=0.65)
        self.wait(0.5)

        # 先别庆祝！
        caution_bg = Text(
            "先别高兴！",
            font=CJK, font_size=32, color=C_BAD
        ).move_to(DOWN * 3.0)
        caution_sub = Text(
            "分式方程必须检验增根！",
            font=CJK, font_size=26, color=C_BAD
        ).move_to(DOWN * 3.9)

        self.play(FadeIn(caution_bg, scale=1.15), run_time=0.4)
        self.play(FadeIn(caution_sub), run_time=0.35)
        self.wait(0.8)

        # 清场，保留 x=1 供下一场
        self._clear(
            s3_tag, step_a, arr_ab, step_b, arr_bc,
            caution_bg, caution_sub
        )
        self.play(
            step_c.animate.move_to(UP * 3.2).scale(0.82).set_color(C_SOLVE),
            step_c_box.animate.move_to(UP * 3.2).scale(0.82),
            run_time=0.5
        )
        self._sol_mob = step_c
        self._sol_box = step_c_box

    # ────────────────────────────────────────────────────────
    # Scene 6 — 步骤4：检验增根（最戏剧化）
    # ────────────────────────────────────────────────────────
    def scene6_verify_extraneous(self):
        s4_tag = self._step_tag(4, "检验", C_BAD).move_to(UP * 2.0)
        self.play(FadeIn(s4_tag, shift=RIGHT * 0.3), run_time=0.45)

        verify_desc = Text(
            "将 x=1 代入最简公分母 x²-1",
            font=CJK, font_size=25, color=C_SUB
        ).move_to(UP * 0.8)
        self.play(FadeIn(verify_desc), run_time=0.45)
        self.wait(0.3)

        # 代入计算
        calc1 = MathTex(
            r"x^2 - 1 \big|_{x=1}",
            font_size=42, color=C_CHECK
        ).move_to(DOWN * 0.5)
        self.play(Write(calc1), run_time=0.65)

        arrow_calc = MathTex(r"=", font_size=38, color=C_ARROW).next_to(calc1, RIGHT, buff=0.25)
        calc2 = MathTex(r"1^2 - 1", font_size=42, color=C_CHECK).next_to(arrow_calc, RIGHT, buff=0.25)
        self.play(FadeIn(arrow_calc), Write(calc2), run_time=0.55)
        self.wait(0.3)

        # = 0  — 变红！
        arrow_calc2 = MathTex(r"=", font_size=38, color=C_ARROW).next_to(calc2, RIGHT, buff=0.25)
        zero_result = MathTex(r"0", font_size=54, color=C_BAD).next_to(arrow_calc2, RIGHT, buff=0.22)

        self.play(FadeIn(arrow_calc2), Write(zero_result), run_time=0.5)
        self.play(
            zero_result.animate.scale(1.35),
            run_time=0.3
        )
        self.play(
            zero_result.animate.scale(1 / 1.35),
            run_time=0.3
        )
        self.wait(0.3)

        # 大叉号
        cross = Cross(
            stroke_color=C_BAD,
            stroke_width=12,
            scale_factor=0.8
        ).move_to(DOWN * 2.3)
        zero_box = self._rbox(
            VGroup(calc1, arrow_calc, calc2, arrow_calc2, zero_result),
            color=C_BAD, buff=0.28, fo=0.10
        )

        self.play(Create(zero_box), run_time=0.45)
        self.play(Create(cross), run_time=0.55)
        self.wait(0.25)

        # 增根说明
        extraneous_title = Text(
            "增根！",
            font=CJK, font_size=42, color=C_BAD, weight=BOLD
        ).move_to(DOWN * 3.5)
        extraneous_sub = Text(
            "x=1 使最简公分母为 0，必须舍去",
            font=CJK, font_size=22, color=C_BAD
        ).move_to(DOWN * 4.4)

        self.play(
            FadeIn(extraneous_title, scale=0.7),
            run_time=0.45
        )
        self.play(FadeIn(extraneous_sub), run_time=0.35)
        self.wait(0.5)

        # 舍去动画 — 划掉 x=1
        strike = Line(
            self._sol_mob.get_left()  + LEFT  * 0.1,
            self._sol_mob.get_right() + RIGHT * 0.1,
            color=C_BAD, stroke_width=6
        )
        self.play(Create(strike), run_time=0.5)
        self.play(
            self._sol_mob.animate.set_opacity(0.3),
            self._sol_box.animate.set_opacity(0.3),
            run_time=0.35
        )
        self.wait(0.4)

        # 最终结论
        conclusion = Text(
            "原方程无解",
            font=CJK, font_size=40, color=C_TITLE, weight=BOLD
        ).move_to(DOWN * 5.5)
        conclusion_box = self._rbox(conclusion, color=C_TITLE, buff=0.35, fo=0.14)

        self.play(Create(conclusion_box), FadeIn(conclusion), run_time=0.7)
        self.play(
            Indicate(conclusion, color=C_TITLE, scale_factor=1.08),
            run_time=0.55
        )
        self.wait(1.5)

        # 清场
        self._clear(
            self._orig_eq, self._orig_box,
            self._integral_eq, self._integral_box,
            self._sol_mob, self._sol_box, strike,
            s4_tag, verify_desc,
            calc1, arrow_calc, calc2, arrow_calc2, zero_result, zero_box,
            cross, extraneous_title, extraneous_sub,
            conclusion, conclusion_box
        )

    # ────────────────────────────────────────────────────────
    # Scene 7 — 总结与片尾
    # ────────────────────────────────────────────────────────
    def scene7_outro(self):
        # 解题框架卡片
        sum_title = self._title("解题四步法", font_size=36)
        sum_title.move_to(UP * 5.8)

        step_rows = VGroup(
            self._step_tag(1, "找最简公分母",  C_LCD),
            self._step_tag(2, "去分母",        C_STEP),
            self._step_tag(3, "解整式方程",    C_SOLVE),
            self._step_tag(4, "检验（增根）",  C_BAD),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        step_rows.move_to(UP * 3.8)

        # 口诀
        mantra = Text(
            "检验这步别跳过，增根舍去不丢分！",
            font=CJK, font_size=24, color=C_BAD
        ).move_to(UP * 1.5)
        mantra_box = self._rbox(mantra, color=C_BAD, buff=0.24, fo=0.09)

        self.play(Write(sum_title[0]), Create(sum_title[1]), run_time=0.55)
        for row in step_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.32)
        self.play(Create(mantra_box), FadeIn(mantra), run_time=0.55)
        self.wait(0.9)

        # 清场 → 片尾
        self._clear(sum_title, step_rows, mantra, mantra_box)
        self.play(FadeOut(self.author_bar), run_time=0.2)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=CJK, font_size=38, color=WHITE
        ).move_to(UP * 1.2)
        author_id = Text(
            "@emptyandcalm",
            font=CJK, font_size=28, color=C_AUTHOR
        ).move_to(UP * 0.1)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=CJK, font_size=28, color=C_BAD
        ).move_to(DOWN * 1.2)

        # 装饰：小分式
        deco = VGroup(
            MathTex(r"\frac{1}{x-1} = \frac{2}{x^2-1}", font_size=24, color=GRAY_B),
            MathTex(r"\Rightarrow x=1 \text{ (extraneous)}", font_size=22, color=GRAY_B),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 3.0)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.55)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco), run_time=0.4)
        self.wait(1.5)
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow),     FadeOut(deco),
            run_time=1.0
        )