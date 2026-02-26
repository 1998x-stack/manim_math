"""
分式加减法 — 七年级数学教学动画
TikTok 竖屏 1080×1920

知识点：同分母加减、异分母通分加减、括号陷阱
作者  ：上海初高中数学直通车 @emptyandcalm
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
C_DENOM   = "#ef9a9a"   # 浅红  ─ 分母
C_NUMER   = "#4fc3f7"   # 浅蓝  ─ 分子
C_LCD     = "#ce93d8"   # 浅紫  ─ 公分母
C_CANCEL  = "#a5d6a7"   # 浅绿  ─ 约分/消去
C_RESULT  = GOLD        # 金色  ─ 最终结果
C_WARN    = "#ff8a65"   # 橙色  ─ 警告
C_WRONG   = "#ef5350"   # 红色  ─ 错误
C_CORRECT = "#66bb6a"   # 绿色  ─ 正确
C_STEP    = "#80cbc4"   # 绿松石 ─ 步骤标签
C_KEY     = YELLOW
C_TITLE   = "#ce93d8"
FONT      = "Noto Sans CJK SC"


# ════════════════════════════════════════════════
class FenshiJiaJian(Scene):
    """分式加减法教学动画（8 场景）"""

    # ────────────────────────────────────────────
    # 统一初始化
    # ────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG
        self.setup_layout()

        self.scene_1_opening()
        self.scene_2_same_denom_rule()
        self.scene_3_same_denom_example()
        self.scene_4_diff_denom_rule()
        self.scene_5_diff_denom_example()
        self.scene_6_bracket_trap()
        self.scene_7_summary()
        self.scene_8_outro()

    def setup_layout(self):
        """坐标参考 & 全局持久元素"""
        self.Y_AUTHOR  =  7.2
        self.Y_TITLE   =  5.8
        self.Y_STEP    =  5.0
        self.Y_F1      =  4.0
        self.Y_F2      =  2.6
        self.Y_F3      =  1.2
        self.Y_F4      = -0.2
        self.Y_F5      = -1.6
        self.Y_EXPLAIN = -3.0
        self.Y_CAPTION = -4.5

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * self.Y_AUTHOR)

    # ────────────────────────────────────────────
    # 辅助函数
    # ────────────────────────────────────────────
    def t(self, text, size=24, color=WHITE, **kw):
        """中文 Text 快捷方式"""
        return Text(text, font=FONT, font_size=size, color=color, **kw)

    def sc_title(self, text, color=C_TITLE):
        return self.t(text, size=36, color=color).move_to(UP * self.Y_TITLE)

    def step_lbl(self, text, color=C_STEP):
        return self.t(text, size=22, color=color).move_to(UP * self.Y_STEP)

    def hbox(self, mob, color=C_RESULT, buff=0.18):
        """高亮边框"""
        return SurroundingRectangle(mob, color=color, buff=buff,
                                    corner_radius=0.1)

    def card(self, lines, colors, width=7.2, stroke=C_STEP):
        """生成说明卡片 VGroup"""
        texts = VGroup(*[
            self.t(l, size=22, color=c) for l, c in zip(lines, colors)
        ]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        bg = RoundedRectangle(
            width=width, height=texts.height + 0.6,
            corner_radius=0.18,
            fill_color="#1e2a4a", fill_opacity=0.92,
            stroke_color=stroke, stroke_width=1.8
        )
        texts.move_to(bg)
        return VGroup(bg, texts)

    # ════════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ════════════════════════════════════════════
    def scene_1_opening(self):
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.35)

        title = self.t("分式加减法", size=52, color=C_TITLE).move_to(UP * 5.5)
        sub   = self.t("下面两种情况，你分清楚了吗？", size=26,
                        color=GRAY_A).move_to(UP * 4.55)
        self.play(Write(title), run_time=0.75)
        self.play(FadeIn(sub, shift=UP * 0.25), run_time=0.4)

        # 同分母示例
        lbl_s = self.t("① 同分母", size=22, color=C_DENOM).move_to(
            UP * 3.4 + LEFT * 2.3)
        f_same = MathTex(
            r"\frac{3}{x+1} + \frac{2}{x+1}",
            font_size=34, color=WHITE
        ).move_to(UP * 2.7 + LEFT * 2.3)

        # 异分母示例
        lbl_d = self.t("② 异分母", size=22, color=C_LCD).move_to(
            UP * 3.4 + RIGHT * 2.3)
        f_diff = MathTex(
            r"\frac{1}{x} + \frac{2}{x+1}",
            font_size=34, color=WHITE
        ).move_to(UP * 2.7 + RIGHT * 2.3)

        # 分割线
        divider = Line(UP * 3.8, UP * 1.8, color=GRAY_C, stroke_width=1.5)

        self.play(
            FadeIn(lbl_s, shift=RIGHT * 0.3),
            FadeIn(lbl_d, shift=LEFT * 0.3),
            run_time=0.45
        )
        self.play(
            Write(f_same), Write(f_diff),
            Create(divider),
            run_time=0.85
        )

        hint = self.t("方法不同，关键在于分母！", size=24,
                       color=C_KEY).move_to(UP * 1.2)
        self.play(FadeIn(hint, shift=UP * 0.25), run_time=0.5)
        self.wait(0.9)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(lbl_s), FadeOut(f_same),
            FadeOut(lbl_d), FadeOut(f_diff),
            FadeOut(divider), FadeOut(hint),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 2 — 同分母法则
    # ════════════════════════════════════════════
    def scene_2_same_denom_rule(self):
        title = self.sc_title("同分母加减法")
        self.play(Write(title), run_time=0.55)

        # 口诀
        mantra = self.t("分母不变，分子直接加减",
                         size=28, color=C_KEY).move_to(UP * 4.85)
        self.play(FadeIn(mantra, shift=UP * 0.2), run_time=0.5)

        # 通用公式
        rule = MathTex(
            r"\frac{A}{C} \pm \frac{B}{C} = \frac{A \pm B}{C}",
            font_size=44, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(rule), run_time=0.95)
        self.wait(0.35)

        # Brace 标注分母
        denom_brace = Brace(rule, direction=DOWN, color=C_DENOM, buff=0.08)
        denom_lbl   = self.t("分母 C 保持不变",
                              size=21, color=C_DENOM).next_to(
            denom_brace, DOWN, buff=0.15)
        self.play(Create(denom_brace), FadeIn(denom_lbl), run_time=0.55)

        # 分子高亮圈
        # 高亮 A±B 部分（右侧分子）
        numer_box = SurroundingRectangle(
            rule[0][7:12], color=C_NUMER, buff=0.08, corner_radius=0.08
        )
        numer_lbl = self.t("分子 A±B 直接运算",
                            size=21, color=C_NUMER).move_to(UP * 2.1)
        self.play(Create(numer_box), FadeIn(numer_lbl), run_time=0.5)
        self.wait(1.4)

        # 说明卡
        rule_card = self.card(
            ["规则：分母相同时", "→ 分母不变，分子加减"],
            [C_STEP, WHITE],
            stroke=C_DENOM
        ).move_to(UP * 0.8)
        self.play(FadeIn(rule_card, shift=UP * 0.3), run_time=0.55)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(mantra), FadeOut(rule),
            FadeOut(denom_brace), FadeOut(denom_lbl),
            FadeOut(numer_box), FadeOut(numer_lbl),
            FadeOut(rule_card),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 3 — 同分母例题
    # ════════════════════════════════════════════
    def scene_3_same_denom_example(self):
        title = self.sc_title("例题1：同分母")
        self.play(Write(title), run_time=0.5)

        lbl = self.step_lbl("原式")
        self.play(FadeIn(lbl), run_time=0.3)

        # 原式
        f0 = MathTex(
            r"\frac{3}{x+1} + \frac{2}{x+1}",
            font_size=42, color=WHITE
        ).move_to(UP * self.Y_F1)
        self.play(Write(f0), run_time=0.8)
        self.wait(0.35)

        # 步骤1
        lbl1 = self.step_lbl("分母不变，分子相加")
        self.play(Transform(lbl, lbl1), run_time=0.3)

        f1 = MathTex(
            r"= \frac{3 + 2}{x+1}",
            font_size=42, color=WHITE
        ).move_to(UP * self.Y_F2)
        self.play(Write(f1), run_time=0.75)

        # 高亮分子运算
        nb = SurroundingRectangle(f1[0][1:6], color=C_NUMER, buff=0.08,
                                   corner_radius=0.08)
        self.play(Create(nb), run_time=0.4)
        self.wait(0.4)

        # 结果
        lbl2 = self.step_lbl("计算分子")
        self.play(Transform(lbl, lbl2), FadeOut(nb), run_time=0.3)

        f2 = MathTex(
            r"= \frac{5}{x+1}",
            font_size=52, color=C_RESULT
        ).move_to(UP * self.Y_F3)
        res_box = self.hbox(f2, color=GOLD, buff=0.22)

        self.play(Write(f2), run_time=0.6)
        self.play(Create(res_box), run_time=0.4)
        self.play(Flash(f2, color=GOLD, flash_radius=1.2), run_time=0.45)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(lbl),
            FadeOut(f0), FadeOut(f1), FadeOut(f2), FadeOut(res_box),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 4 — 异分母法则（通分）
    # ════════════════════════════════════════════
    def scene_4_diff_denom_rule(self):
        title = self.sc_title("异分母加减法")
        self.play(Write(title), run_time=0.55)

        # 核心提示
        key = self.t("分母不同？先通分！", size=30,
                      color=C_KEY).move_to(UP * 4.85)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)

        # 流程图：4 步
        steps = ["不同分母", "找公分母", "化同分母", "分子加减"]
        colors = [C_DENOM, C_LCD, C_NUMER, C_RESULT]
        nodes = VGroup()
        for s, c in zip(steps, colors):
            box = RoundedRectangle(
                width=1.6, height=0.72, corner_radius=0.12,
                fill_color="#1e2a4a", fill_opacity=0.95,
                stroke_color=c, stroke_width=2
            )
            lbl = self.t(s, size=19, color=c)
            lbl.move_to(box)
            nodes.add(VGroup(box, lbl))

        nodes.arrange(RIGHT, buff=0.45).move_to(UP * 3.8)

        # 箭头
        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(
                nodes[i].get_right(), nodes[i+1].get_left(),
                buff=0.08, color=GRAY_B,
                tip_length=0.15, stroke_width=2.5
            )
            arrows.add(a)

        self.play(
            LaggedStart(*[FadeIn(n, shift=UP * 0.25) for n in nodes],
                        lag_ratio=0.18),
            run_time=0.85
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2),
            run_time=0.6
        )

        # 通用公式
        rule = MathTex(
            r"\frac{A}{B} \pm \frac{C}{D}"
            r"= \frac{A \cdot D \pm C \cdot B}{B \cdot D}",
            font_size=34, color=WHITE
        ).move_to(UP * 2.55)
        self.play(Write(rule), run_time=1.0)

        # 说明：BD 是公分母
        bd_brace = Brace(rule[0][-3:], direction=DOWN, color=C_LCD, buff=0.08)
        bd_lbl   = self.t("公分母 B·D",
                           size=20, color=C_LCD).next_to(bd_brace, DOWN, buff=0.12)
        self.play(Create(bd_brace), FadeIn(bd_lbl), run_time=0.5)
        self.wait(0.4)

        # 提示卡
        tip_card = self.card(
            ["公分母 = 各分母的最简公倍式",
             "分子同步乘对应因子",
             "通分后再加减分子"],
            [C_LCD, C_NUMER, C_RESULT],
            stroke=C_LCD
        ).move_to(UP * 0.7)
        self.play(FadeIn(tip_card, shift=UP * 0.3), run_time=0.6)
        self.wait(1.3)

        self.play(
            FadeOut(title), FadeOut(key),
            FadeOut(nodes), FadeOut(arrows),
            FadeOut(rule), FadeOut(bd_brace), FadeOut(bd_lbl),
            FadeOut(tip_card),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 5 — 异分母例题
    # ════════════════════════════════════════════
    def scene_5_diff_denom_example(self):
        title = self.sc_title("例题2：异分母")
        self.play(Write(title), run_time=0.5)

        lbl = self.step_lbl("原式（分母不同）")
        self.play(FadeIn(lbl), run_time=0.3)

        # 原式
        f0 = MathTex(
            r"\frac{1}{x} + \frac{2}{x+1}",
            font_size=42, color=WHITE
        ).move_to(UP * self.Y_F1)
        self.play(Write(f0), run_time=0.8)
        self.wait(0.3)

        # Step 1 — 找公分母
        lbl1 = self.step_lbl("第①步：找公分母")
        self.play(Transform(lbl, lbl1), run_time=0.3)

        # Step 1 — 找公分母
        lbl1 = self.step_lbl("第①步：找公分母")
        self.play(Transform(lbl, lbl1), run_time=0.3)

        # Fixed: Use Text + MathTex separately to avoid LaTeX Unicode issues
        lcd_lbl  = self.t("公分母 =", size=26, color=C_LCD)
        lcd_form = MathTex(r"x(x+1)", font_size=36, color=C_LCD)
        lcd_row  = VGroup(lcd_lbl, lcd_form).arrange(RIGHT, buff=0.25)
        lcd_row.move_to(UP * self.Y_F2)
        lcd_box = self.hbox(lcd_row, color=C_LCD, buff=0.18)
        self.play(Write(lcd_lbl), Write(lcd_form),
                  Create(lcd_box), run_time=0.8)
        self.wait(0.4)

        # Step 2 — 化同分母
        lbl2 = self.step_lbl("第②步：化同分母")
        self.play(Transform(lbl, lbl2), FadeOut(lcd_box), run_time=0.3)

        f1 = MathTex(
            r"= \frac{x+1}{x(x+1)} + \frac{2x}{x(x+1)}",
            font_size=34, color=WHITE
        ).move_to(UP * self.Y_F3)

        # 注释：1×(x+1) 和 2×x
        ann1 = self.t("1×(x+1)", size=18, color=C_NUMER).move_to(
            UP * self.Y_F3 + LEFT * 2.4 + UP * 0.62)
        ann2 = self.t("2×x", size=18, color=C_NUMER).move_to(
            UP * self.Y_F3 + RIGHT * 1.7 + UP * 0.62)

        self.play(Write(f1), run_time=0.85)
        self.play(
            FadeIn(ann1, shift=DOWN * 0.15),
            FadeIn(ann2, shift=DOWN * 0.15),
            run_time=0.45
        )
        self.wait(0.55)

        # Step 3 — 分子相加
        lbl3 = self.step_lbl("第③步：分子合并")
        self.play(Transform(lbl, lbl3),
                  FadeOut(ann1), FadeOut(ann2), run_time=0.3)

        f2 = MathTex(
            r"= \frac{(x+1) + 2x}{x(x+1)}",
            font_size=34, color=WHITE
        ).move_to(UP * self.Y_F4)
        self.play(Write(f2), run_time=0.75)
        self.wait(0.3)

        # Step 4 — 合并同类项
        lbl4 = self.step_lbl("第④步：合并同类项")
        self.play(Transform(lbl, lbl4), run_time=0.3)

        f3 = MathTex(
            r"= \frac{3x+1}{x(x+1)}",
            font_size=42, color=C_RESULT
        ).move_to(UP * self.Y_F5)
        res_box = self.hbox(f3, color=GOLD, buff=0.22)

        self.play(Write(f3), run_time=0.65)
        self.play(Create(res_box), run_time=0.4)
        self.play(Flash(f3, color=GOLD, flash_radius=1.1), run_time=0.45)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(lbl),
            FadeOut(f0), FadeOut(lcd_lbl), FadeOut(lcd_form),
            FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(res_box),
            run_time=0.45
        )

    # ════════════════════════════════════════════
    # Scene 6 — 括号陷阱（重点警示）
    # ════════════════════════════════════════════
    def scene_6_bracket_trap(self):
        """⚠️ 核心场景：减法时分子多项式必须加括号"""

        # ── 警告标题 ──
        warn_icon = self.t("⚠️", size=38).move_to(UP * 6.0 + LEFT * 2.9)
        warn_title = self.t("常见陷阱：忘加括号！",
                             size=32, color=C_WARN).move_to(UP * 5.8 + RIGHT * 0.5)
        self.play(FadeIn(warn_icon, scale=0.5), Write(warn_title), run_time=0.7)

        # ── 原式 ──
        lbl = self.step_lbl("原式（同分母减法）")
        self.play(FadeIn(lbl), run_time=0.3)

        f0 = MathTex(
            r"\frac{2}{a-1} - \frac{a-2}{a-1}",
            font_size=40, color=WHITE
        ).move_to(UP * self.Y_F1)
        self.play(Write(f0), run_time=0.8)
        self.wait(0.4)

        # ── 分屏：左错 / 右对 ──
        # 左侧：错误做法
        wrong_title = self.t("❌ 错误做法", size=22, color=C_WRONG).move_to(
            UP * 3.0 + LEFT * 2.2)
        wrong_f = MathTex(
            r"\frac{2 - a - 2}{a-1}",
            font_size=32, color=C_WRONG
        ).move_to(UP * 2.1 + LEFT * 2.2)
        wrong_explain = self.t("直接把分子抄过来", size=18,
                                color=C_WRONG).move_to(UP * 1.4 + LEFT * 2.2)

        # 右侧：正确做法
        right_title = self.t("✅ 正确做法", size=22, color=C_CORRECT).move_to(
            UP * 3.0 + RIGHT * 2.2)
        right_f = MathTex(
            r"\frac{2-(a-2)}{a-1}",
            font_size=32, color=C_CORRECT
        ).move_to(UP * 2.1 + RIGHT * 2.2)
        right_explain = self.t("分子要加括号！", size=18,
                                color=C_CORRECT).move_to(UP * 1.4 + RIGHT * 2.2)

        # 中间分割线
        split = Line(UP * 3.5, UP * 0.8, color=GRAY_C, stroke_width=1.5)

        self.play(
            Write(wrong_title), Write(right_title),
            Create(split),
            run_time=0.55
        )
        self.play(
            Write(wrong_f), Write(right_f),
            run_time=0.75
        )
        self.play(
            FadeIn(wrong_explain), FadeIn(right_explain),
            run_time=0.45
        )
        self.wait(0.5)

        # ── 展开过程对比 ──
        wrong_expand = MathTex(
            r"= \frac{-a}{a-1}",
            font_size=30, color=C_WRONG
        ).move_to(UP * 0.4 + LEFT * 2.2)

        right_expand1 = MathTex(
            r"= \frac{2-a+2}{a-1}",
            font_size=30, color=C_CORRECT
        ).move_to(UP * 0.4 + RIGHT * 2.2)
        right_expand2 = MathTex(
            r"= \frac{4-a}{a-1}",
            font_size=30, color=C_CORRECT
        ).move_to(UP * -0.4 + RIGHT * 2.2)

        # 错误结果标记
        cross = Cross(wrong_expand, stroke_color=C_WRONG,
                      stroke_width=2.5, scale_factor=0.9)

        self.play(Write(wrong_expand), Write(right_expand1), run_time=0.7)
        self.play(Create(cross), Write(right_expand2), run_time=0.6)
        self.wait(0.5)

        # 高亮正确结果
        final_box = self.hbox(right_expand2, color=GOLD, buff=0.18)
        self.play(Create(final_box), run_time=0.4)

        # ── 核心提醒卡 ──
        remind_bg = RoundedRectangle(
            width=7.5, height=1.3, corner_radius=0.18,
            fill_color="#2a1e0a", fill_opacity=0.95,
            stroke_color=C_WARN, stroke_width=2.5
        ).move_to(UP * self.Y_EXPLAIN)

        remind_text = self.t(
            "减法时，被减的多项式分子必须加括号，\n再去括号变号！",
            size=20, color=C_WARN
        ).move_to(remind_bg)

        self.play(FadeIn(remind_bg), Write(remind_text), run_time=0.65)
        self.wait(2.2)   # 重点，多等

        self.play(
            FadeOut(warn_icon), FadeOut(warn_title), FadeOut(lbl),
            FadeOut(f0), FadeOut(split),
            FadeOut(wrong_title), FadeOut(wrong_f), FadeOut(wrong_explain),
            FadeOut(wrong_expand), FadeOut(cross),
            FadeOut(right_title), FadeOut(right_f), FadeOut(right_explain),
            FadeOut(right_expand1), FadeOut(right_expand2), FadeOut(final_box),
            FadeOut(remind_bg), FadeOut(remind_text),
            run_time=0.5
        )

    # ════════════════════════════════════════════
    # Scene 7 — 总结
    # ════════════════════════════════════════════
    def scene_7_summary(self):
        title = self.sc_title("解题要点回顾", color=GOLD)
        self.play(Write(title), run_time=0.5)

        # 卡片 1 — 同分母
        c1 = self.card(
            ["同分母加减法", "分母不变，分子直接加减"],
            [C_DENOM, WHITE], stroke=C_DENOM
        ).move_to(UP * 4.4)

        # 卡片 2 — 异分母
        c2 = self.card(
            ["异分母加减法",
             "① 找最简公分母（LCD）",
             "② 化同分母",
             "③ 分子加减"],
            [C_LCD, WHITE, WHITE, C_RESULT],
            width=7.4, stroke=C_LCD
        ).move_to(UP * 2.7)

        # 卡片 3 — 括号陷阱
        c3 = self.card(
            ["⚠️ 减法陷阱",
             "被减分子是多项式 → 必须加括号！",
             "再去括号变号"],
            [C_WARN, WHITE, C_CANCEL],
            stroke=C_WARN
        ).move_to(UP * 0.7)

        for c in [c1, c2, c3]:
            self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.45)

        self.wait(1.8)

        self.play(FadeOut(title), FadeOut(c1), FadeOut(c2), FadeOut(c3),
                  run_time=0.5)

    # ════════════════════════════════════════════
    # Scene 8 — 片尾
    # ════════════════════════════════════════════
    def scene_8_outro(self):
        # 放大作者信息
        big_name = self.t("上海初高中数学直通车", size=40,
                           color=WHITE).move_to(UP * 2.2)
        big_id   = self.t("@emptyandcalm", size=30,
                           color=GRAY_B).move_to(UP * 1.1)

        self.play(Transform(self.author_bar, big_name), run_time=0.65)
        self.play(FadeIn(big_id, shift=UP * 0.3), run_time=0.4)

        cta = self.t("关注我，学更多数学技巧！",
                      size=28, color=C_KEY).move_to(UP * 0.0)
        self.play(FadeIn(cta, scale=1.06), run_time=0.5)

        # 符号装饰
        sym_data = [
            (r"\frac{A}{C}", LEFT * 3.0 + DOWN * 1.6, C_DENOM),
            (r"\pm",          LEFT * 1.5 + DOWN * 1.9, WHITE),
            (r"\frac{B}{C}",  ORIGIN   + DOWN * 1.6, C_NUMER),
            (r"=",            RIGHT * 1.4 + DOWN * 1.9, WHITE),
            (r"\frac{A \pm B}{C}", RIGHT * 3.0 + DOWN * 1.6, C_RESULT),
        ]
        syms = VGroup(*[
            MathTex(s, font_size=26, color=c).move_to(p)
            for s, p, c in sym_data
        ])
        self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in syms],
                               lag_ratio=0.12), run_time=0.8)

        # 数学符号闪光收尾
        self.play(
            *[Flash(s, color=s.get_color(), flash_radius=0.5)
              for s in [syms[0], syms[2], syms[4]]],
            run_time=0.6
        )
        self.wait(1.4)

        self.play(
            FadeOut(self.author_bar), FadeOut(big_id),
            FadeOut(cta), FadeOut(syms),
            run_time=0.8
        )


# ─────────────────────────────────────
# 渲染命令：
#   预览 → manim -pql fenshijiajian.py FenshiJiaJian
#   高清 → manim -qh  fenshijiajian.py FenshiJiaJian
# ─────────────────────────────────────