"""
分式方程 — 七年级数学教学动画
TikTok 竖屏 1080×1920  (~70 秒)

核心教学点:
  · 三步解法（去分母 → 解方程 → 必须检验！）
  · 增根陷阱：使分母为 0 的根要舍去

作者: 上海初高中数学直通车  @emptyandcalm
"""

from manim import *
import numpy as np

# ────────────────────────────────────────────────
# 全局配置
# ────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ────────────────────────────────────────────────
# 颜色系统
# ────────────────────────────────────────────────
BG        = "#1a1a2e"
C_DENOM   = "#ef9a9a"   # 浅红  — 分母 / LCD 强调
C_NUMER   = "#4fc3f7"   # 浅蓝  — 分子 / 整式化
C_LCD     = "#ce93d8"   # 浅紫  — 最简公分母框
C_STEP    = "#80cbc4"   # 绿松石 — 步骤标签
C_RESULT  = GOLD        # 金色  — 最终结果
C_WARN    = "#ff8a65"   # 橙色  — 警告
C_WRONG   = "#ef5350"   # 红色  — 错误 / 增根
C_CORRECT = "#66bb6a"   # 绿色  — 正确 / 检验通过
C_CHECK   = "#fff176"   # 浅黄  — 检验高亮
C_TITLE   = "#ce93d8"   # 标题色
FONT      = "Noto Sans CJK SC"


# ════════════════════════════════════════════════
class FenshiFangCheng(Scene):
    """分式方程教学动画（8 场景）"""

    # ───────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG
        self.setup_layout()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_three_steps()
        self.scene_4_example1()
        self.scene_5_extraneous_root()
        self.scene_6_why_check()
        self.scene_7_summary()
        self.scene_8_outro()

    # ───────────────────────────────────────────
    # 初始化
    # ───────────────────────────────────────────
    def setup_layout(self):
        self.Y_AUTHOR =  7.2
        self.Y_TITLE  =  5.8
        self.Y_STEP   =  5.0
        self.Y_F1     =  4.0
        self.Y_F2     =  2.8
        self.Y_F3     =  1.6
        self.Y_F4     =  0.4
        self.Y_F5     = -0.8
        self.Y_F6     = -2.0
        self.Y_EXPL   = -3.4
        self.Y_CAP    = -4.8

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * self.Y_AUTHOR)

    # ───────────────────────────────────────────
    # 辅助方法
    # ───────────────────────────────────────────
    def t(self, txt, size=24, color=WHITE, **kw):
        return Text(txt, font=FONT, font_size=size, color=color, **kw)

    def sc_title(self, txt, color=C_TITLE):
        return self.t(txt, size=36, color=color).move_to(UP * self.Y_TITLE)

    def step_lbl(self, txt, color=C_STEP):
        return self.t(txt, size=22, color=color).move_to(UP * self.Y_STEP)

    def hbox(self, mob, color=C_RESULT, buff=0.18):
        return SurroundingRectangle(
            mob, color=color, buff=buff, corner_radius=0.1)

    def card(self, lines, colors, width=7.3, stroke=C_STEP, bg="#1e2a4a"):
        txts = VGroup(*[
            self.t(l, size=21, color=c) for l, c in zip(lines, colors)
        ]).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        bg_rect = RoundedRectangle(
            width=width, height=txts.height + 0.55,
            corner_radius=0.18,
            fill_color=bg, fill_opacity=0.93,
            stroke_color=stroke, stroke_width=1.9
        )
        txts.move_to(bg_rect)
        return VGroup(bg_rect, txts)

    def step_box(self, num, title, color):
        """三步法中的单个步骤方块"""
        box = RoundedRectangle(
            width=2.3, height=1.4, corner_radius=0.2,
            fill_color="#1e2a4a", fill_opacity=0.95,
            stroke_color=color, stroke_width=2.2
        )
        num_t  = self.t(num, size=28, color=color)
        name_t = self.t(title, size=19, color=WHITE)
        VGroup(num_t, name_t).arrange(DOWN, buff=0.18).move_to(box)
        return VGroup(box, num_t, name_t)

    # ════════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ════════════════════════════════════════════
    def scene_1_opening(self):
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.35)

        title = self.t("分式方程", size=54, color=C_TITLE).move_to(UP * 5.55)
        sub   = self.t("这道题暗藏陷阱，你能发现吗？",
                        size=25, color=GRAY_A).move_to(UP * 4.6)
        self.play(Write(title), run_time=0.75)
        self.play(FadeIn(sub, shift=UP * 0.25), run_time=0.42)

        # 钩子方程
        hook_eq = MathTex(
            r"\frac{x}{x-1} = \frac{1}{x-1} + 2",
            font_size=44, color=WHITE
        ).move_to(UP * 3.3)
        self.play(Write(hook_eq), run_time=0.95)

        # 看似普通，实则陷阱
        trap_lbl = self.t("⚠️  求解后一定要检验！",
                           size=26, color=C_WARN).move_to(UP * 2.1)
        self.play(FadeIn(trap_lbl, scale=1.08), run_time=0.5)
        self.wait(0.9)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(hook_eq), FadeOut(trap_lbl),
            run_time=0.42
        )

    # ════════════════════════════════════════════
    # Scene 2 — 什么是分式方程
    # ════════════════════════════════════════════
    def scene_2_definition(self):
        title = self.sc_title("什么是分式方程？")
        self.play(Write(title), run_time=0.55)

        # 对比：整式方程 vs 分式方程
        int_lbl = self.t("整式方程", size=22, color=C_NUMER).move_to(
            UP * 4.65 + LEFT * 2.3)
        int_eq  = MathTex(r"2x - 3 = 5", font_size=34, color=WHITE).move_to(
            UP * 3.85 + LEFT * 2.3)

        fra_lbl = self.t("分式方程", size=22, color=C_DENOM).move_to(
            UP * 4.65 + RIGHT * 2.3)
        fra_eq  = MathTex(
            r"\frac{1}{x-1} = 2", font_size=34, color=WHITE
        ).move_to(UP * 3.85 + RIGHT * 2.3)

        divider = Line(
            UP * 5.1 + ORIGIN, UP * 2.8 + ORIGIN,
            color=GRAY_C, stroke_width=1.5
        )

        self.play(
            FadeIn(int_lbl, shift=RIGHT * 0.3),
            FadeIn(fra_lbl, shift=LEFT  * 0.3),
            Create(divider),
            run_time=0.5
        )
        self.play(Write(int_eq), Write(fra_eq), run_time=0.8)

        # 高亮分式方程分母中的 x
        denom_box = SurroundingRectangle(
            fra_eq[0][4:7], color=C_DENOM, buff=0.1, corner_radius=0.08
        )
        denom_note = self.t("分母含未知数！", size=20, color=C_DENOM).move_to(
            UP * 3.0 + RIGHT * 2.3)
        self.play(Create(denom_box), FadeIn(denom_note), run_time=0.55)

        # 核心定义
        def_card = self.card(
            ["分母中含有未知数的方程",
             "叫做  分式方程"],
            [GRAY_A, WHITE],
            stroke=C_DENOM
        ).move_to(UP * 1.8)
        self.play(FadeIn(def_card, shift=UP * 0.3), run_time=0.6)
        self.wait(1.3)

        self.play(
            FadeOut(title), FadeOut(int_lbl), FadeOut(int_eq),
            FadeOut(fra_lbl), FadeOut(fra_eq),
            FadeOut(divider), FadeOut(denom_box), FadeOut(denom_note),
            FadeOut(def_card),
            run_time=0.42
        )

    # ════════════════════════════════════════════
    # Scene 3 — 三步解法
    # ════════════════════════════════════════════
    def scene_3_three_steps(self):
        title = self.sc_title("解分式方程：三步法")
        self.play(Write(title), run_time=0.55)

        # 三个步骤方块
        b1 = self.step_box("①", "去分母", C_NUMER)
        b2 = self.step_box("②", "解方程", C_STEP)
        b3 = self.step_box("③", "检  验", C_WARN)

        steps_row = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.6).move_to(UP * 4.05)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in [b1, b2, b3]],
                        lag_ratio=0.2),
            run_time=0.8
        )

        # 箭头
        a1 = Arrow(b1.get_right(), b2.get_left(), buff=0.08,
                   color=GRAY_B, tip_length=0.18, stroke_width=2.5)
        a2 = Arrow(b2.get_right(), b3.get_left(), buff=0.08,
                   color=GRAY_B, tip_length=0.18, stroke_width=2.5)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.5)

        # 各步骤说明
        desc1 = self.card(
            ["两边同乘", "最简公分母"],
            [GRAY_A, C_LCD], width=2.6, stroke=C_NUMER
        ).move_to(UP * 2.6 + b1.get_center()[0] * RIGHT)

        desc2 = self.card(
            ["化为整式方程", "求解"],
            [GRAY_A, WHITE], width=2.6, stroke=C_STEP
        ).move_to(UP * 2.6 + b2.get_center()[0] * RIGHT)

        desc3 = self.card(
            ["代入原分母", "是否为零？"],
            [GRAY_A, C_WARN], width=2.6, stroke=C_WARN, bg="#2a1e0a"
        ).move_to(UP * 2.6 + b3.get_center()[0] * RIGHT)

        self.play(
            LaggedStart(FadeIn(desc1), FadeIn(desc2), FadeIn(desc3),
                        lag_ratio=0.2),
            run_time=0.7
        )

        # 增根警示
        warn_card = self.card(
            ["增根 = 使公分母为 0 的解",
             "发现增根 → 舍去！方程无解"],
            [C_WARN, C_WRONG],
            stroke=C_WARN, bg="#2a1a1a"
        ).move_to(UP * 1.0)
        self.play(FadeIn(warn_card, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(steps_row), FadeOut(a1), FadeOut(a2),
            FadeOut(desc1), FadeOut(desc2), FadeOut(desc3),
            FadeOut(warn_card),
            run_time=0.42
        )

    # ════════════════════════════════════════════
    # Scene 4 — 例题1（正常，x = 3/2 ✓）
    # ════════════════════════════════════════════
    def scene_4_example1(self):
        title = self.sc_title("例题1：正常解法")
        self.play(Write(title), run_time=0.5)

        lbl = self.step_lbl("原式")
        self.play(FadeIn(lbl), run_time=0.28)

        # ── 原式 ──
        eq0 = MathTex(
            r"\frac{1}{x-1} = 2",
            font_size=44, color=WHITE
        ).move_to(UP * self.Y_F1)
        self.play(Write(eq0), run_time=0.8)
        self.wait(0.3)

        # ── 最简公分母 ──
        lbl1 = self.step_lbl("第①步：找最简公分母")
        self.play(Transform(lbl, lbl1), run_time=0.28)

        lcd_lbl  = self.t("最简公分母 =", size=24, color=C_LCD)
        lcd_form = MathTex(r"(x-1)", font_size=36, color=C_LCD)
        lcd_row  = VGroup(lcd_lbl, lcd_form).arrange(RIGHT, buff=0.3)
        lcd_row.move_to(UP * self.Y_F2)
        lcd_box  = self.hbox(lcd_row, color=C_LCD, buff=0.18)

        self.play(
            Write(lcd_lbl), Write(lcd_form), Create(lcd_box),
            run_time=0.7
        )
        self.wait(0.3)

        # ── 去分母 ──
        lbl2 = self.step_lbl("第①步：两边乘 (x-1) 去分母")
        self.play(Transform(lbl, lbl2), FadeOut(lcd_box), run_time=0.28)

        eq1 = MathTex(
            r"1 = 2(x-1)",
            font_size=40, color=WHITE
        ).move_to(UP * self.Y_F3)
        arrow_hint = self.t("两边 × (x-1)", size=19, color=C_LCD).move_to(
            UP * self.Y_F3 + RIGHT * 2.8)
        self.play(Write(eq1), FadeIn(arrow_hint), run_time=0.75)

        # ── 展开整理 ──
        lbl3 = self.step_lbl("第②步：整理整式方程")
        self.play(Transform(lbl, lbl3),
                  FadeOut(arrow_hint), run_time=0.28)

        eq2 = MathTex(
            r"1 = 2x - 2",
            font_size=40, color=WHITE
        ).move_to(UP * self.Y_F4)
        eq3 = MathTex(
            r"2x = 3",
            font_size=40, color=WHITE
        ).move_to(UP * self.Y_F5)

        self.play(Write(eq2), run_time=0.65)
        self.play(Write(eq3), run_time=0.55)

        # ── 求解 ──
        eq4 = MathTex(
            r"x = \frac{3}{2}",
            font_size=46, color=C_RESULT
        ).move_to(UP * self.Y_F6)
        self.play(Write(eq4), run_time=0.6)

        # 临时金框
        tmp_box = self.hbox(eq4, color=GOLD)
        self.play(Create(tmp_box), run_time=0.35)
        self.wait(0.3)

        # ── 检验 ──
        lbl4 = self.step_lbl("第③步：检验（代入分母）")
        self.play(Transform(lbl, lbl4), FadeOut(tmp_box), run_time=0.28)

        check_bg = RoundedRectangle(
            width=7.0, height=2.8, corner_radius=0.2,
            fill_color="#0a2a0a", fill_opacity=0.93,
            stroke_color=C_CORRECT, stroke_width=2
        ).move_to(UP * self.Y_EXPL)

        ck_line1 = self.t("将 x = 3/2 代入分母 (x-1)：",
                           size=21, color=GRAY_A)
        ck_eq    = MathTex(
            r"x-1 = \frac{3}{2}-1 = \frac{1}{2} \neq 0",
            font_size=32, color=C_CHECK
        )
        ck_line2 = self.t("✅  分母不为零，x = 3/2 是合法解！",
                           size=21, color=C_CORRECT)

        ck_content = VGroup(ck_line1, ck_eq, ck_line2).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT)
        ck_content.move_to(check_bg)

        self.play(FadeIn(check_bg), run_time=0.35)
        self.play(
            Write(ck_line1), Write(ck_eq), Write(ck_line2),
            run_time=1.0
        )
        self.play(Flash(ck_line2, color=C_CORRECT, flash_radius=3.0), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(lbl),
            FadeOut(eq0), FadeOut(lcd_lbl), FadeOut(lcd_form),
            FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(eq4),
            FadeOut(check_bg), FadeOut(ck_content),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 5 — 例题2（增根！x = 1 被舍去）
    # ════════════════════════════════════════════
    def scene_5_extraneous_root(self):
        title = self.sc_title("例题2：陷阱！增根出现", color=C_WARN)
        self.play(Write(title), run_time=0.55)

        lbl = self.step_lbl("原式（看起来正常）")
        self.play(FadeIn(lbl), run_time=0.28)

        # ── 原式 ──
        eq0 = MathTex(
            r"\frac{x}{x-1} = \frac{1}{x-1} + 2",
            font_size=40, color=WHITE
        ).move_to(UP * self.Y_F1)
        self.play(Write(eq0), run_time=0.9)
        self.wait(0.3)

        # ── LCD ──
        lbl1 = self.step_lbl("最简公分母 = (x-1)")
        self.play(Transform(lbl, lbl1), run_time=0.28)

        lcd_row = VGroup(
            self.t("最简公分母 =", size=22, color=C_LCD),
            MathTex(r"(x-1)", font_size=34, color=C_LCD)
        ).arrange(RIGHT, buff=0.25).move_to(UP * self.Y_F2)
        lcd_box = self.hbox(lcd_row, color=C_LCD, buff=0.15)
        self.play(Write(lcd_row[0]), Write(lcd_row[1]),
                  Create(lcd_box), run_time=0.65)
        self.wait(0.25)

        # ── 去分母 ──
        lbl2 = self.step_lbl("第①步：两边乘 (x-1)，去分母")
        self.play(Transform(lbl, lbl2), FadeOut(lcd_box), run_time=0.28)

        eq1 = MathTex(
            r"x = 1 + 2(x-1)",
            font_size=38, color=WHITE
        ).move_to(UP * self.Y_F3)
        self.play(Write(eq1), run_time=0.75)

        # ── 展开整理 ──
        lbl3 = self.step_lbl("第②步：展开，整理")
        self.play(Transform(lbl, lbl3), run_time=0.28)

        eq2 = MathTex(
            r"x = 2x - 1",
            font_size=38, color=WHITE
        ).move_to(UP * self.Y_F4)
        eq3 = MathTex(
            r"x = 1",
            font_size=40, color=C_CHECK
        ).move_to(UP * self.Y_F5)
        self.play(Write(eq2), run_time=0.6)
        self.play(Write(eq3), run_time=0.55)

        # 临时金框（表面上"求得"答案）
        tmp_box = self.hbox(eq3, color=GOLD, buff=0.2)
        self.play(Create(tmp_box), run_time=0.35)
        self.wait(0.5)

        # ── 检验 —— 发现增根！──
        lbl4 = self.step_lbl("第③步：检验！！！")
        self.play(Transform(lbl, lbl4), FadeOut(tmp_box), run_time=0.28)

        # 检验框（背景先出现，内容逐步写入）
        check_bg = RoundedRectangle(
            width=7.2, height=3.2, corner_radius=0.2,
            fill_color="#2a0a0a", fill_opacity=0.95,
            stroke_color=C_WRONG, stroke_width=2.5
        ).move_to(UP * self.Y_EXPL + DOWN * 0.3)

        ck1 = self.t("将 x = 1 代入分母 (x-1)：", size=21, color=GRAY_A)
        ck2 = MathTex(
            r"x - 1 = 1 - 1 = 0",
            font_size=36, color=C_WRONG
        )
        ck3 = self.t("⚠️  分母 = 0！！！", size=24, color=C_WRONG)

        ck_content = VGroup(ck1, ck2, ck3).arrange(DOWN, buff=0.25,
                                                     aligned_edge=LEFT)
        ck_content.move_to(check_bg)

        self.play(FadeIn(check_bg), run_time=0.35)
        self.play(Write(ck1), run_time=0.6)
        self.play(Write(ck2), run_time=0.55)

        # 数字"0"脉冲闪烁 + 分母框变红
        self.play(
            ck2.animate.set_color(C_WRONG).scale(1.1),
            run_time=0.4
        )
        self.play(
            ck2.animate.scale(1.0 / 1.1),
            run_time=0.25
        )
        self.play(Write(ck3), run_time=0.5)

        # 大叉 + 震动
        big_cross = Cross(eq3, stroke_color=C_WRONG, stroke_width=5,
                          scale_factor=0.95)
        self.play(Create(big_cross), run_time=0.5)
        self.play(
            big_cross.animate.scale(1.05),
            run_time=0.18
        )
        self.play(
            big_cross.animate.scale(1.0 / 1.05),
            run_time=0.18
        )

        # 增根标签 + 结论
        zengen_lbl = self.t("增根！舍去！",
                             size=32, color=C_WRONG).move_to(
            UP * self.Y_F6 + RIGHT * 1.5)
        self.play(FadeIn(zengen_lbl, scale=1.15), run_time=0.5)
        self.play(Flash(zengen_lbl, color=C_WRONG, flash_radius=1.8), run_time=0.45)

        # 最终结论
        conclusion_bg = RoundedRectangle(
            width=6.5, height=0.85, corner_radius=0.18,
            fill_color="#2a0a0a", fill_opacity=0.95,
            stroke_color=C_WRONG, stroke_width=2
        ).move_to(UP * self.Y_CAP + UP * 0.5)
        conclusion = self.t("此方程无解！",
                             size=30, color=C_WRONG).move_to(conclusion_bg)
        self.play(FadeIn(conclusion_bg), Write(conclusion), run_time=0.6)
        self.wait(2.0)   # 核心概念，让学生消化

        self.play(
            FadeOut(title), FadeOut(lbl),
            FadeOut(eq0), FadeOut(lcd_row), FadeOut(eq1),
            FadeOut(eq2), FadeOut(eq3), FadeOut(big_cross),
            FadeOut(zengen_lbl),
            FadeOut(check_bg), FadeOut(ck_content),
            FadeOut(conclusion_bg), FadeOut(conclusion),
            run_time=0.5
        )

    # ════════════════════════════════════════════
    # Scene 6 — 为什么必须检验？
    # ════════════════════════════════════════════
    def scene_6_why_check(self):
        title = self.sc_title("为什么必须检验？")
        self.play(Write(title), run_time=0.55)

        # 原因卡
        reason_card = self.card(
            ["去分母时，两边同乘了含未知数的式子",
             "可能引入原方程中不存在的根",
             "这些多余的根叫做  增根"],
            [GRAY_A, GRAY_A, C_WARN],
            stroke=C_WARN, bg="#2a1a0a", width=7.5
        ).move_to(UP * 4.2)
        self.play(FadeIn(reason_card, shift=UP * 0.3), run_time=0.65)

        # 增根定义框
        def_lbl = self.t("【增根的定义】", size=24, color=C_WARN).move_to(UP * 2.5)
        def_card = self.card(
            ["代入最简公分母后，使分母 = 0 的根",
             "就是增根，必须舍去"],
            [WHITE, C_WRONG],
            stroke=C_WRONG, bg="#2a0a0a"
        ).move_to(UP * 1.5)
        self.play(Write(def_lbl), run_time=0.4)
        self.play(FadeIn(def_card, shift=UP * 0.25), run_time=0.55)

        # 黄金口诀
        rule_bg = RoundedRectangle(
            width=7.5, height=1.1, corner_radius=0.2,
            fill_color="#1a2a0a", fill_opacity=0.95,
            stroke_color=C_CORRECT, stroke_width=2.5
        ).move_to(UP * 0.0)
        rule = self.t("检验步骤是解分式方程必不可少的一步！",
                       size=22, color=C_CORRECT).move_to(rule_bg)
        self.play(FadeIn(rule_bg), Write(rule), run_time=0.65)
        self.wait(1.8)

        self.play(
            FadeOut(title),
            FadeOut(reason_card), FadeOut(def_lbl), FadeOut(def_card),
            FadeOut(rule_bg), FadeOut(rule),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 7 — 总结：解题口诀三步法
    # ════════════════════════════════════════════
    def scene_7_summary(self):
        title = self.sc_title("解分式方程口诀", color=GOLD)
        self.play(Write(title), run_time=0.5)

        step_data = [
            ("第①步", "去分母",
             ["两边同乘最简公分母", "化分式方程为整式方程"],
             C_NUMER),
            ("第②步", "解方程",
             ["按整式方程解法", "求出 x 的值"],
             C_STEP),
            ("第③步", "必须检验！",
             ["代入最简公分母", "若分母=0 → 增根，舍去"],
             C_WARN),
        ]

        cards = VGroup()
        y_positions = [4.5, 3.0, 1.5]

        for (num, name, lines, color), y in zip(step_data, y_positions):
            # 步骤号+名称
            header = VGroup(
                self.t(num,  size=22, color=color),
                self.t(name, size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.35)

            # 描述行
            desc_lines = VGroup(*[
                self.t(l, size=19, color=GRAY_A) for l in lines
            ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)

            content = VGroup(header, desc_lines).arrange(
                DOWN, buff=0.22, aligned_edge=LEFT)

            bg = RoundedRectangle(
                width=7.4, height=content.height + 0.5,
                corner_radius=0.18,
                fill_color="#1e2a4a", fill_opacity=0.93,
                stroke_color=color, stroke_width=1.9
            )
            content.move_to(bg).align_to(bg, LEFT).shift(RIGHT * 0.4)

            step_card = VGroup(bg, content)
            step_card.move_to(UP * y)
            cards.add(step_card)

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.45), run_time=0.42)

        # 底部强调
        emph_bg = RoundedRectangle(
            width=7.5, height=0.85, corner_radius=0.18,
            fill_color="#2a1a0a", fill_opacity=0.93,
            stroke_color=C_WARN, stroke_width=2.2
        ).move_to(UP * 0.0)
        emph = self.t("检验不是可选项，是必选项！",
                       size=24, color=C_WARN).move_to(emph_bg)
        self.play(FadeIn(emph_bg), Write(emph), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(cards),
            FadeOut(emph_bg), FadeOut(emph),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 8 — 片尾
    # ════════════════════════════════════════════
    def scene_8_outro(self):
        big_name = self.t("上海初高中数学直通车", size=40,
                           color=WHITE).move_to(UP * 2.2)
        big_id   = self.t("@emptyandcalm", size=30,
                           color=GRAY_B).move_to(UP * 1.1)

        self.play(Transform(self.author_bar, big_name), run_time=0.65)
        self.play(FadeIn(big_id, shift=UP * 0.3), run_time=0.4)

        cta = self.t("关注我，学更多数学技巧！",
                      size=28, color=GOLD).move_to(UP * 0.05)
        self.play(FadeIn(cta, scale=1.07), run_time=0.5)

        # 公式符号装饰
        sym_data = [
            (r"\frac{x}{x-1}",          LEFT * 3.0 + DOWN * 1.8, C_DENOM),
            (r"=",                       LEFT * 1.3 + DOWN * 2.0, WHITE),
            (r"\frac{1}{x-1} + 2",      RIGHT * 1.2 + DOWN * 1.8, C_NUMER),
            (r"\xrightarrow{\times(x-1)}", LEFT * 0.6 + DOWN * 3.2, C_LCD),
            (r"x = 1 \;\text{?}",        RIGHT * 2.8 + DOWN * 3.2, C_WRONG),
        ]
        syms = VGroup(*[
            MathTex(s, font_size=24, color=c).move_to(p)
            for s, p, c in sym_data
        ])
        self.play(
            LaggedStart(*[FadeIn(s, scale=0.5) for s in syms],
                        lag_ratio=0.15),
            run_time=0.85
        )

        # 最后闪烁
        cross_sym = MathTex(r"\times", font_size=40,
                             color=C_WRONG).move_to(RIGHT * 2.8 + DOWN * 3.2)
        self.play(FadeIn(cross_sym, scale=1.3), run_time=0.4)
        self.wait(1.3)

        self.play(
            FadeOut(self.author_bar), FadeOut(big_id),
            FadeOut(cta), FadeOut(syms), FadeOut(cross_sym),
            run_time=0.8
        )


# ─────────────────────────────────────────────
# 渲染命令：
#   预览 → manim -pql fenshifangcheng.py FenshiFangCheng
#   高清 → manim -qh  fenshifangcheng.py FenshiFangCheng
# ─────────────────────────────────────────────