"""
分式的约分 - 七年级数学教学动画
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
    manim -pql fenshi_yufen.py FenshiYufen   # 快速预览
    manim -qh  fenshi_yufen.py FenshiYufen   # 高质量
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置
# ══════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ══════════════════════════════════════════════════
#  调色板
# ══════════════════════════════════════════════════
BG_COLOR    = "#1a1a2e"
C_PRIMARY   = "#4fc3f7"   # 浅蓝
C_FACTOR    = "#f9a825"   # 金黄   公因式
C_CANCEL    = "#ef5350"   # 红色   划去
C_RESULT    = "#66bb6a"   # 绿色   结果
C_HIGHLIGHT = "#fff176"   # 亮黄
C_STEP      = "#ce93d8"   # 紫色   步骤
C_CARD_BG   = "#16213e"   # 深蓝
C_SUBTITLE  = "#b0bec5"   # 灰白
C_WRONG     = "#ef5350"

# ══════════════════════════════════════════════════
#  字号
# ══════════════════════════════════════════════════
FONT    = "Noto Sans CJK SC"
FS_BIG  = 52
FS_TTL  = 38
FS_SUB  = 28
FS_BODY = 24
FS_SM   = 20
FS_XS   = 17
FS_FORM = 36
FS_AUTH = 20


# ══════════════════════════════════════════════════
#  工具：带删除线的 Mobject（模拟约分划消）
# ══════════════════════════════════════════════════
def strikethrough(mob, color=C_CANCEL):
    """在 mob 上方画一条斜线，模拟约分划消。"""
    x0, y0 = mob.get_left()[0],  mob.get_bottom()[1]
    x1, y1 = mob.get_right()[0], mob.get_top()[1]
    return Line(
        np.array([x0, y0, 0]),
        np.array([x1, y1, 0]),
        color=color, stroke_width=4,
    )


class FenshiYufen(Scene):
    """
    分式的约分教学动画
    Scene 1 : 开场钩子                  (0–6s)
    Scene 2 : 约分定义 + 最简分式       (6–15s)
    Scene 3 : 核心例题 (x²-1)/(x+1)    (15–33s)
    Scene 4 : 进阶例题 符号处理         (33–46s)
    Scene 5 : 三步走总结 + 易错提醒     (46–55s)
    Scene 6 : 片尾                      (55–62s)
    """

    # ──────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author_bar = self._make_author_bar()
        self.add(self.author_bar)

        self.scene_1_hook()
        self.scene_2_definition()
        self.scene_3_example1()
        self.scene_4_example2()
        self.scene_5_summary()
        self.scene_6_outro()

    # ══════════════════════════════════════════
    #  SCENE 1 — 开场钩子
    # ══════════════════════════════════════════
    def scene_1_hook(self):
        hook_q = Text(
            "这两个式子相等吗？",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).move_to(UP * 5.5)
        self.play(FadeIn(hook_q, shift=DOWN * 0.3), run_time=0.5)

        # 左：(x²-1)/(x+1)
        lhs = MathTex(
            r"\dfrac{x^2-1}{x+1}",
            font_size=60, color=C_FACTOR,
        ).move_to(UP * 4.0 + LEFT * 2.2)

        # 问号
        q_mark = Text("?", font=FONT, font_size=FS_BIG, color=C_HIGHLIGHT).move_to(UP * 4.0)

        # 右：x-1
        rhs = MathTex(r"x-1", font_size=60, color=C_RESULT).move_to(UP * 4.0 + RIGHT * 2.2)

        self.play(Write(lhs), run_time=0.5)
        self.play(FadeIn(q_mark, scale=0.4), run_time=0.3)
        self.play(Write(rhs), run_time=0.4)
        self.wait(0.3)

        # 揭示：约分能化简！
        bridge = Text(
            "「约分」可以把左边化成右边！",
            font=FONT, font_size=FS_BODY, color=C_PRIMARY,
        ).move_to(UP * 2.5)
        self.play(FadeIn(bridge, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 主标题
        main_title = Text(
            "分式的约分",
            font=FONT, font_size=FS_BIG, color=C_FACTOR, weight=BOLD,
        ).move_to(UP * 1.2)
        self.play(Write(main_title), run_time=0.6)
        self.wait(0.4)

        # 缩小移顶
        self.play(
            FadeOut(VGroup(hook_q, lhs, q_mark, rhs, bridge)),
            main_title.animate.scale(0.5).move_to(UP * 6.0).set_color(C_SUBTITLE),
            run_time=0.5,
        )
        self.small_title = main_title

    # ══════════════════════════════════════════
    #  SCENE 2 — 约分定义
    # ══════════════════════════════════════════
    def scene_2_definition(self):
        sec = self._section_title("① 约分的定义", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # ── 分数类比 ──
        analog_label = Text(
            "先回忆分数约分：",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(UP * 5.5)
        self.play(FadeIn(analog_label), run_time=0.3)

        f_orig = MathTex(r"\dfrac{6}{8}", font_size=52, color=WHITE)
        arr    = Arrow(LEFT * 0.5, RIGHT * 0.5, color=C_PRIMARY, buff=0,
                       stroke_width=5, max_tip_length_to_length_ratio=0.25)
        f_simp = MathTex(r"\dfrac{3}{4}", font_size=52, color=C_RESULT)
        div_c  = Text("÷ 2", font=FONT, font_size=FS_SM, color=C_FACTOR)
        analog_row = VGroup(f_orig, arr, f_simp).arrange(RIGHT, buff=0.45).move_to(UP * 4.6)
        div_c.next_to(arr, UP, buff=0.1)

        self.play(Write(f_orig), run_time=0.4)
        self.play(GrowArrow(arr), FadeIn(div_c), run_time=0.4)
        self.play(Write(f_simp), run_time=0.4)
        self.wait(0.3)

        # ── 定义框 ──
        defn_text = Text(
            "把分式的分子、分母的公因式约去",
            font=FONT, font_size=FS_BODY, color=WHITE,
        ).move_to(UP * 3.2)
        defn_bg = RoundedRectangle(
            width=defn_text.width + 0.9, height=0.9,
            corner_radius=0.2, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=C_FACTOR, stroke_width=2.5,
        ).move_to(defn_text.get_center())
        self.play(FadeIn(defn_bg), Write(defn_text), run_time=0.6)
        self.wait(0.3)

        # ── 最简分式 ──
        simp_label = Text(
            "约分后若分子分母再无公因式，即：",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(UP * 1.9)
        simp_box_text = Text(
            "最简分式",
            font=FONT, font_size=FS_TTL, color=C_RESULT, weight=BOLD,
        ).move_to(UP * 0.9)
        simp_box = SurroundingRectangle(
            simp_box_text, color=C_RESULT, buff=0.28,
            corner_radius=0.2, stroke_width=3,
        )
        goal_note = Text(
            "约分的目标：把分式化为最简分式",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(simp_label), run_time=0.3)
        self.play(Write(simp_box_text), Create(simp_box), run_time=0.5)
        self.play(FadeIn(goal_note), run_time=0.3)
        self.wait(1.2)

        all_s2 = VGroup(sec, analog_label, analog_row, div_c,
                        defn_bg, defn_text, simp_label, simp_box_text,
                        simp_box, goal_note)
        self.play(FadeOut(all_s2), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 3 — 核心例题 (x²-1)/(x+1)
    # ══════════════════════════════════════════
    def scene_3_example1(self):
        sec = self._section_title("② 例题精讲", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # ── 原式 ──
        orig = MathTex(
            r"\dfrac{x^2-1}{x+1}",
            font_size=68, color=C_FACTOR,
        ).move_to(UP * 5.4)
        self.play(Write(orig), run_time=0.6)
        self.wait(0.2)

        # ── STEP 1：因式分解分子 ──
        step1_tag = self._step_tag("Step 1", "分子因式分解", UP * 4.3)
        self.play(FadeIn(step1_tag, shift=RIGHT * 0.3), run_time=0.4)

        # x²-1 = (x+1)(x-1)
        factored = MathTex(
            r"= \dfrac{(x+1)(x-1)}{x+1}",
            font_size=60, color=WHITE,
        ).move_to(UP * 3.4)
        self.play(Write(factored), run_time=0.6)

        # 差平方公式提示
        sq_note = Text(
            "（利用平方差公式：a²-b² = (a+b)(a-b)）",
            font=FONT, font_size=FS_XS, color=C_SUBTITLE,
        ).next_to(factored, DOWN, buff=0.2)
        self.play(FadeIn(sq_note), run_time=0.3)
        self.wait(0.3)

        # ── STEP 2：高亮公因式 ──
        step2_tag = self._step_tag("Step 2", "找出公因式", UP * 2.2)
        self.play(FadeIn(step2_tag, shift=RIGHT * 0.3), run_time=0.4)

        # 重新写一遍，分子 (x+1) 标黄，分母 (x+1) 标黄
        factored_hl = MathTex(
            r"\dfrac{(x+1)(x-1)}{(x+1)}",
            font_size=58,
        ).move_to(UP * 1.3)
        factored_hl[1].set_color(C_FACTOR)
        factored_hl[3].set_color(C_FACTOR)

        # 把 factored 变换到 factored_hl
        self.play(ReplacementTransform(factored.copy(), factored_hl), run_time=0.6)
        self.wait(0.2)

        # 框住公因式
        box_num = SurroundingRectangle(factored_hl[1], color=C_FACTOR, buff=0.08, stroke_width=2)
        box_den = SurroundingRectangle(factored_hl[3], color=C_FACTOR, buff=0.08, stroke_width=2)
        cf_label = Text("公因式！", font=FONT, font_size=FS_SM, color=C_FACTOR).next_to(box_num, RIGHT, buff=0.2)
        self.play(Create(box_num), Create(box_den), FadeIn(cf_label), run_time=0.5)
        self.wait(0.3)

        # ── STEP 3：划去公因式 ──
        step3_tag = self._step_tag("Step 3", "约去公因式", DOWN * 0.0)
        self.play(FadeIn(step3_tag, shift=RIGHT * 0.3), run_time=0.4)

        # 划去 (x+1)
        strike_num = strikethrough(factored_hl[1], C_CANCEL)
        strike_den = strikethrough(factored_hl[3], C_CANCEL)
        self.play(Create(strike_num), Create(strike_den), run_time=0.5)
        self.wait(0.2)

        # ── 结果 ──
        result = MathTex(r"= x - 1", font_size=72, color=C_RESULT).move_to(DOWN * 1.3)
        result_rect = SurroundingRectangle(result, color=C_RESULT, buff=0.28,
                                           corner_radius=0.18, stroke_width=3)
        self.play(Write(result), Create(result_rect), run_time=0.6)
        self.wait(0.2)

        # 条件
        cond = Text(
            "（x ≠ -1，保证分母不为零）",
            font=FONT, font_size=FS_XS, color=C_SUBTITLE,
        ).next_to(result_rect, DOWN, buff=0.2)
        self.play(FadeIn(cond), run_time=0.3)
        self.wait(0.5)

        # ── 代入验证（x = 2）──
        verify_label = Text(
            "验证（令 x = 2）：",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(DOWN * 2.8)
        verify_calc = MathTex(
            r"\dfrac{2^2-1}{2+1} = \dfrac{3}{3} = 1 \quad;\quad 2-1=1 \quad \checkmark",
            font_size=36, color=C_RESULT,
        ).move_to(DOWN * 3.7)
        self.play(FadeIn(verify_label), run_time=0.3)
        self.play(Write(verify_calc), run_time=0.6)
        self.wait(1.5)

        # 清理
        all_s3 = VGroup(
            sec, orig, step1_tag, factored, sq_note,
            step2_tag, factored_hl, box_num, box_den, cf_label,
            step3_tag, strike_num, strike_den,
            result, result_rect, cond, verify_label, verify_calc,
        )
        self.play(FadeOut(all_s3), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 4 — 进阶例题（符号处理）
    # ══════════════════════════════════════════
    def scene_4_example2(self):
        sec = self._section_title("③ 进阶：注意符号！", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # ── 原式 ──
        orig2 = MathTex(
            r"\dfrac{x^2-2x}{2x-x^2}",
            font_size=64, color=C_FACTOR,
        ).move_to(UP * 5.3)
        self.play(Write(orig2), run_time=0.6)
        self.wait(0.2)

        # Step 1：分子提 x
        s1_tag = self._step_tag("Step 1", "分子提公因式 x", UP * 4.2)
        self.play(FadeIn(s1_tag, shift=RIGHT * 0.3), run_time=0.3)

        step1 = MathTex(
            r"= \dfrac{x(x-2)}{2x - x^2}",
            font_size=58, color=WHITE,
        ).move_to(UP * 3.4)
        self.play(Write(step1), run_time=0.5)
        self.wait(0.2)

        # Step 2：分母提 -x（或先提 x 再提 -1）
        s2_tag = self._step_tag("Step 2", "分母提公因式", UP * 2.4)
        self.play(FadeIn(s2_tag, shift=RIGHT * 0.3), run_time=0.3)

        step2a = MathTex(
            r"= \dfrac{x(x-2)}{x(2-x)}",
            font_size=58, color=WHITE,
        ).move_to(UP * 1.6)
        self.play(Write(step2a), run_time=0.5)
        self.wait(0.2)

        # 关键：(2-x) = -(x-2)
        sign_note_bg = RoundedRectangle(
            width=6.8, height=0.95,
            corner_radius=0.2, fill_color="#2a1a1a", fill_opacity=0.97,
            stroke_color=C_CANCEL, stroke_width=2.5,
        ).move_to(UP * 0.5)
        sign_note = Text(
            "注意：(2-x) = -(x-2)  符号要处理！",
            font=FONT, font_size=FS_SM, color=C_CANCEL,
        ).move_to(sign_note_bg.get_center())
        self.play(FadeIn(sign_note_bg), Write(sign_note), run_time=0.5)
        self.wait(0.3)

        step2b = MathTex(
            r"= \dfrac{x(x-2)}{-x(x-2)}",
            font_size=58, color=WHITE,
        ).move_to(DOWN * 0.5)
        self.play(Write(step2b), run_time=0.5)
        self.wait(0.2)

        # Step 3：划去 x(x-2)
        s3_tag = self._step_tag("Step 3", "约去公因式", DOWN * 1.5)
        self.play(FadeIn(s3_tag, shift=RIGHT * 0.3), run_time=0.3)

        # 高亮标色
        step2b_hl = MathTex(
            r"\dfrac{",
            r"x(x-2)",    # [1] 分子
            r"}{",
            r"-x(x-2)",   # [3] 分母
            r"}",
            font_size=54,
        ).move_to(DOWN * 2.4)
        step2b_hl[1].set_color(C_FACTOR)
        step2b_hl[3].set_color(C_FACTOR)
        self.play(ReplacementTransform(step2b.copy(), step2b_hl), run_time=0.5)

        strike_n2 = strikethrough(step2b_hl[1], C_CANCEL)
        # 分母 "-x(x-2)" 里只划去 "x(x-2)" 部分（近似处理：划整体）
        strike_d2 = strikethrough(step2b_hl[3], C_CANCEL)
        self.play(Create(strike_n2), Create(strike_d2), run_time=0.5)
        self.wait(0.2)

        # 结果 -1
        result2 = MathTex(r"= -1", font_size=72, color=C_RESULT).move_to(DOWN * 3.7)
        result2_rect = SurroundingRectangle(result2, color=C_RESULT, buff=0.28,
                                            corner_radius=0.18, stroke_width=3)
        self.play(Write(result2), Create(result2_rect), run_time=0.5)
        cond2 = Text(
            "（x ≠ 0，x ≠ 2）",
            font=FONT, font_size=FS_XS, color=C_SUBTITLE,
        ).next_to(result2_rect, DOWN, buff=0.15)
        self.play(FadeIn(cond2), run_time=0.3)
        self.wait(1.5)

        all_s4 = VGroup(
            sec, orig2, s1_tag, step1, s2_tag, step2a,
            sign_note_bg, sign_note, step2b,
            s3_tag, step2b_hl, strike_n2, strike_d2,
            result2, result2_rect, cond2,
        )
        self.play(FadeOut(all_s4), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 5 — 三步走总结 + 易错提醒
    # ══════════════════════════════════════════
    def scene_5_summary(self):
        sec = self._section_title("约分三步走", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        cards_data = [
            ("Step 1", "分子、分母各自因式分解",   C_PRIMARY,  UP * 4.5),
            ("Step 2", "找出分子分母的公因式",      C_FACTOR,   UP * 2.2),
            ("Step 3", "约去公因式 → 最简分式",     C_RESULT,   DOWN * 0.1),
        ]

        cards = VGroup()
        for tag, body, color, pos in cards_data:
            card = self._step_card(tag, body, color, pos)
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.55)
            self.wait(0.2)

        self.wait(0.3)

        # ⚠️ 易错提醒
        warn_bg = RoundedRectangle(
            width=7.6, height=1.7,
            corner_radius=0.25, fill_color="#2a0a0a", fill_opacity=0.97,
            stroke_color=C_CANCEL, stroke_width=2.5,
        ).move_to(DOWN * 2.5)
        warn_icon = Text("⚠️", font=FONT, font_size=FS_SUB).move_to(warn_bg.get_center() + LEFT * 3.0)
        warn_lines = VGroup(
            Text("易错 1：只约了分子/分母的一部分", font=FONT, font_size=FS_XS, color=C_CANCEL),
            Text("易错 2：符号处理错误（(2-x) ≠ (x-2)）", font=FONT, font_size=FS_XS, color=C_CANCEL),
            Text("易错 3：漏写约分条件（分母 ≠ 0）", font=FONT, font_size=FS_XS, color=C_CANCEL),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(warn_icon, RIGHT, buff=0.3)
        warn_content = VGroup(warn_icon, warn_lines)
        warn_content.move_to(warn_bg.get_center())

        self.play(FadeIn(warn_bg), FadeIn(warn_content), run_time=0.6)
        self.wait(2.0)

        all_s5 = VGroup(sec, cards, warn_bg, warn_content)
        self.play(FadeOut(all_s5), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 6 — 片尾
    # ══════════════════════════════════════════
    def scene_6_outro(self):
        big = Text(
            "分式的约分",
            font=FONT, font_size=FS_BIG, color=C_FACTOR, weight=BOLD,
        ).move_to(UP * 2.5)
        self.play(Write(big), run_time=0.6)

        aname = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=FS_SUB + 4, color=WHITE,
        ).move_to(UP * 0.8)
        aid = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).next_to(aname, DOWN, buff=0.22)
        self.play(FadeIn(aname, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(aid), run_time=0.3)

        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=C_SUBTITLE, stroke_width=1).move_to(DOWN * 0.4)
        self.play(Create(divider), run_time=0.3)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰：几个约分算式
        deco = VGroup(
            MathTex(r"\frac{x^2-1}{x+1}=x-1", font_size=22, color=C_FACTOR),
            MathTex(r"\frac{2x}{4x^2}=\frac{1}{2x}", font_size=22, color=C_RESULT),
            MathTex(r"\frac{x(x-2)}{-x(x-2)}=-1", font_size=22, color=C_PRIMARY),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.0)
        self.play(FadeIn(deco, shift=UP * 0.2), run_time=0.5)
        self.play(Wiggle(deco, scale_value=1.06), run_time=0.8)

        slogan = Text(
            "每天一道题，数学不再难！",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(slogan), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(big, aname, aid, divider, follow, deco, slogan)),
            FadeOut(VGroup(self.small_title, self.author_bar)),
            run_time=0.8,
        )

    # ══════════════════════════════════════════
    #  工具方法
    # ══════════════════════════════════════════
    def _make_author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=FS_AUTH, color=GRAY_B,
        ).move_to(UP * 6.9)

    def _section_title(self, text: str, pos):
        bar = Rectangle(
            width=0.12, height=0.55,
            fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0,
        )
        lbl = Text(text, font=FONT, font_size=FS_SUB, color=C_PRIMARY)
        grp = VGroup(bar, lbl).arrange(RIGHT, buff=0.2)
        grp.move_to(pos)
        return grp

    def _step_tag(self, tag_str: str, body_str: str, pos):
        """左侧彩色标签 + 右侧说明文字"""
        tag = Text(tag_str, font=FONT, font_size=FS_SM, color=C_STEP, weight=BOLD)
        tag_box = SurroundingRectangle(tag, color=C_STEP, buff=0.1, corner_radius=0.1, stroke_width=2)
        body = Text(body_str, font=FONT, font_size=FS_SM, color=C_SUBTITLE)
        grp = VGroup(VGroup(tag_box, tag), body).arrange(RIGHT, buff=0.3)
        grp.move_to(pos)
        return grp

    def _step_card(self, tag_str: str, body_str: str, color, pos):
        """总结用卡片"""
        tag_mob  = Text(tag_str,  font=FONT, font_size=FS_SM + 2, color=color, weight=BOLD)
        body_mob = Text(body_str, font=FONT, font_size=FS_BODY,   color=WHITE)
        content  = VGroup(tag_mob, body_mob).arrange(RIGHT, buff=0.4)
        bg = RoundedRectangle(
            width=7.6, height=content.height + 0.6,
            corner_radius=0.22, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=color, stroke_width=2.5,
        )
        card = VGroup(bg, content)
        content.move_to(bg.get_center())
        card.move_to(pos)
        return card