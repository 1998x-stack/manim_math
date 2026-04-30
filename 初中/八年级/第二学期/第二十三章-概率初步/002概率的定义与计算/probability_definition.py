"""
概率的定义与计算 — 教学动画
目标受众: 八年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ProbabilityDefinition(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.C_TITLE  = "#f9ca24"
        self.C_MAIN   = "#22a6b3"
        self.C_RED    = "#eb4d4b"
        self.C_GREEN  = "#6ab04c"
        self.C_PURPLE = "#a29bfe"
        self.C_ORANGE = "#f0932b"
        self.C_RESULT = "#badc58"

        self.scene_opening()
        self.scene_basic_events()
        self.scene_formula()
        self.scene_ex_dice()
        self.scene_ex_balls()
        self.scene_prob_range()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    def card(self, w, h, col, pos, fill="#16213e", alpha=0.85):
        return RoundedRectangle(
            corner_radius=0.28, width=w, height=h,
            color=col, stroke_width=2,
            fill_color=fill, fill_opacity=alpha,
        ).move_to(pos)

    def fade_rest(self):
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author], run_time=0.45)

    # ─────────── Scene 1 ───────────
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        chapter = Text("八年级 · 第二十三章 · 概率初步",
                       font="PingFang SC", font_size=20, color=GRAY_B,
                       ).move_to(UP * 6.55)
        self.play(FadeIn(chapter), run_time=0.3)

        hook = Text("掷骰子，出现 6 的可能性有多大？",
                    font="PingFang SC", font_size=30, color=self.C_TITLE,
                    ).move_to(UP * 5.7)
        self.play(Write(hook), run_time=0.7)

        # 大骰子示意（六边形 + 点）
        die = RegularPolygon(n=6, radius=1.3, color=self.C_MAIN,
                             fill_color="#0f2a3a", fill_opacity=0.9,
                             ).move_to(UP * 4.0)
        die_label = MathTex(r"1,2,3,4,5,6", font_size=34,
                            color=WHITE).move_to(UP * 4.0)
        self.play(Create(die), Write(die_label), run_time=0.7)

        q_bg = self.card(5.5, 1.5, self.C_RED, UP * 2.5)
        q_f  = MathTex(r"P(\text{six}) = \;?", font_size=48, color=WHITE
                       ).move_to(UP * 2.5)
        self.play(Create(q_bg), Write(q_f), run_time=0.6)
        self.wait(0.6)

        ans_bg = self.card(5.5, 1.5, self.C_GREEN, UP * 1.0,
                           fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"P = \dfrac{1}{6}", font_size=52, color=WHITE
                         ).move_to(UP * 1.0)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(chapter), FadeOut(hook), FadeOut(die),
                  FadeOut(die_label), FadeOut(q_bg), FadeOut(q_f),
                  FadeOut(ans_bg), FadeOut(ans_f), run_time=0.4)

    # ─────────── Scene 2 ───────────
    def scene_basic_events(self):
        title = Text("基本事件与等可能性",
                     font="PingFang SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.5)

        # 6 dots for a die
        n_cols = 6
        xs = [-2.25 + i * 0.9 for i in range(n_cols)]
        y_dot = 5.1
        cols = [self.C_MAIN, self.C_PURPLE, self.C_ORANGE,
                self.C_MAIN, self.C_PURPLE, self.C_ORANGE]
        dots, labels = [], []
        for i, (x, c) in enumerate(zip(xs, cols)):
            d = Circle(radius=0.32, color=c,
                       fill_color=c, fill_opacity=0.85,
                       ).move_to(np.array([x, y_dot, 0]))
            lbl = Text(str(i + 1), font="PingFang SC",
                       font_size=22, color=WHITE,
                       ).move_to(np.array([x, y_dot, 0]))
            dots.append(d); labels.append(lbl)

        for d, l in zip(dots, labels):
            self.play(GrowFromCenter(d), Write(l), run_time=0.25)

        equal_t = Text("6个结果：等可能（每个概率相同）",
                       font="PingFang SC", font_size=24, color=GRAY_A,
                       ).move_to(UP * 4.0)
        self.play(FadeIn(equal_t), run_time=0.4)

        # 高亮"6"这个结果
        surr = SurroundingRectangle(dots[5], color=self.C_RED,
                                    buff=0.12, corner_radius=0.1)
        target_t = Text("目标事件：出现6",
                        font="PingFang SC", font_size=26, color=self.C_RED,
                        ).move_to(UP * 3.0)
        self.play(Create(surr), Write(target_t), run_time=0.6)

        # 定义文字
        def_bg = self.card(7.4, 2.4, self.C_MAIN, UP * 1.7)
        def_l1 = Text("基本事件：试验的每个可能结果",
                      font="PingFang SC", font_size=24, color=WHITE)
        def_l2 = Text("等可能性：每个基本事件概率相同",
                      font="PingFang SC", font_size=24, color=self.C_RESULT)
        VGroup(def_l1, def_l2).arrange(DOWN, buff=0.2).move_to(UP * 1.7)
        self.play(Create(def_bg), Write(def_l1), Write(def_l2), run_time=0.7)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 3 ───────────
    def scene_formula(self):
        title = Text("核心公式",
                     font="PingFang SC", font_size=46, color=self.C_TITLE,
                     ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.5)

        formula_bg = self.card(7.6, 2.4, self.C_MAIN, UP * 5.1,
                               fill="#0f2a3a", alpha=0.95)
        formula = MathTex(r"P(A) = \dfrac{m}{n}",
                          font_size=64, color=WHITE).move_to(UP * 5.1)
        self.play(Create(formula_bg), Write(formula), run_time=0.8)

        # 用箭头标注 m 和 n
        m_label_bg = self.card(3.2, 1.4, self.C_ORANGE, UP * 3.5)
        m_text = Text("m = A包含的\n基本事件数",
                      font="PingFang SC", font_size=22, color=self.C_ORANGE,
                      ).move_to(UP * 3.5)
        n_label_bg = self.card(3.2, 1.4, self.C_PURPLE, UP * 3.5)
        n_text = Text("n = 基本事件\n总数",
                      font="PingFang SC", font_size=22, color=self.C_PURPLE,
                      ).move_to(UP * 3.5)

        VGroup(m_label_bg, m_text).move_to(UP * 3.5 + LEFT * 1.9)
        VGroup(n_label_bg, n_text).move_to(UP * 3.5 + RIGHT * 1.9)
        self.play(Create(m_label_bg), Write(m_text),
                  Create(n_label_bg), Write(n_text), run_time=0.7)

        # 条件
        cond_bg = self.card(7.4, 1.6, self.C_GREEN, UP * 2.1)
        cond_f  = MathTex(r"0 \leq P(A) \leq 1",
                          font_size=48, color=WHITE).move_to(UP * 2.3)
        cond_t  = Text("概率介于 0 和 1 之间",
                       font="PingFang SC", font_size=22, color=GRAY_A,
                       ).move_to(UP * 1.85)
        self.play(Create(cond_bg), Write(cond_f), FadeIn(cond_t), run_time=0.7)

        # 三类事件
        events_bg = self.card(7.4, 2.8, self.C_PURPLE, UP * 0.5)
        ev1 = VGroup(
            Text("P=0：不可能事件",
                 font="PingFang SC", font_size=22, color=self.C_RED),
            Text("P=1：必然事件",
                 font="PingFang SC", font_size=22, color=self.C_GREEN),
            Text("0<P<1：随机事件",
                 font="PingFang SC", font_size=22, color=self.C_TITLE),
        ).arrange(DOWN, buff=0.22).move_to(UP * 0.5)
        self.play(Create(events_bg), *[Write(t) for t in ev1], run_time=0.7)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 4 ───────────
    def scene_ex_dice(self):
        title = Text("例题 1  掷骰子",
                     font="PingFang SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_MAIN, UP * 5.5)
        prob_t = Text("掷一个骰子，求 P(偶数)",
                      font="PingFang SC", font_size=28, color=WHITE,
                      ).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_t), run_time=0.7)

        # 画6个点
        xs = [-2.25 + i * 0.9 for i in range(6)]
        dots, lbls = [], []
        for i, x in enumerate(xs):
            c = self.C_GREEN if (i + 1) % 2 == 0 else GRAY_B
            d = Circle(radius=0.3, color=c,
                       fill_color=c, fill_opacity=0.85,
                       ).move_to(np.array([x, 4.2, 0]))
            l = Text(str(i + 1), font="PingFang SC",
                     font_size=20, color=WHITE,
                     ).move_to(np.array([x, 4.2, 0]))
            dots.append(d); lbls.append(l)

        self.play(*[GrowFromCenter(d) for d in dots],
                  *[Write(l) for l in lbls], run_time=0.6)

        n_bg = self.card(7.2, 1.3, self.C_PURPLE, UP * 3.1)
        n_t  = Text("基本事件总数 n = 6",
                    font="PingFang SC", font_size=26, color=WHITE,
                    ).move_to(UP * 3.1)
        m_bg = self.card(7.2, 1.3, self.C_ORANGE, UP * 1.9)
        m_t  = Text("偶数 {2,4,6}，m = 3",
                    font="PingFang SC", font_size=26, color=WHITE,
                    ).move_to(UP * 1.9)
        self.play(Create(n_bg), Write(n_t), run_time=0.4)
        self.play(Create(m_bg), Write(m_t), run_time=0.4)

        step = MathTex(r"P(\text{even}) = \dfrac{3}{6} = \dfrac{1}{2}",
                       font_size=48, color=self.C_TITLE).move_to(UP * 0.7)
        self.play(Write(step), run_time=0.6)

        ans_bg = self.card(6.5, 1.5, self.C_RESULT, DOWN * 0.5,
                           fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"P(\text{even}) = \frac{1}{2}",
                         font_size=50, color=WHITE).move_to(DOWN * 0.5)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07),
                  run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 5 ───────────
    def scene_ex_balls(self):
        title = Text("例题 2  摸球问题",
                     font="PingFang SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.5, self.C_MAIN, UP * 5.5)
        prob_t  = Text("袋中 3红 2蓝，随机摸 1 球，P(红球)?",
                       font="PingFang SC", font_size=24, color=WHITE,
                       ).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_t), run_time=0.7)

        # 画5个球
        ball_xs = [-1.8 + i * 0.9 for i in range(5)]
        ball_y  = 4.1
        colors  = [self.C_RED]*3 + [self.C_MAIN]*2
        balls, ball_lbls = [], []
        for i, (x, c) in enumerate(zip(ball_xs, colors)):
            b = Circle(radius=0.35, color=c,
                       fill_color=c, fill_opacity=0.85,
                       ).move_to(np.array([x, ball_y, 0]))
            lbl_str = "R" if i < 3 else "B"
            l = Text(lbl_str, font="PingFang SC",
                     font_size=20, color=WHITE,
                     ).move_to(np.array([x, ball_y, 0]))
            balls.append(b); ball_lbls.append(l)

        self.play(*[GrowFromCenter(b) for b in balls],
                  *[Write(l) for l in ball_lbls], run_time=0.6)

        n_bg = self.card(7.2, 1.3, self.C_PURPLE, UP * 3.0)
        n_t  = Text("基本事件总数 n = 5",
                    font="PingFang SC", font_size=26, color=WHITE,
                    ).move_to(UP * 3.0)
        m_bg = self.card(7.2, 1.3, self.C_RED, UP * 1.8)
        m_t  = Text("红球事件 m = 3",
                    font="PingFang SC", font_size=26, color=WHITE,
                    ).move_to(UP * 1.8)
        self.play(Create(n_bg), Write(n_t), run_time=0.4)
        self.play(Create(m_bg), Write(m_t), run_time=0.4)

        step = MathTex(r"P(\text{red}) = \dfrac{3}{5}",
                       font_size=52, color=self.C_TITLE).move_to(UP * 0.6)
        self.play(Write(step), run_time=0.6)

        ans_bg = self.card(6.5, 1.5, self.C_RESULT, DOWN * 0.6,
                           fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"P(\text{red}) = \dfrac{3}{5}",
                         font_size=50, color=WHITE).move_to(DOWN * 0.6)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07),
                  run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 6 ───────────
    def scene_prob_range(self):
        title = Text("概率的范围",
                     font="PingFang SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 数轴
        line = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_A,
                    stroke_width=3).move_to(UP * 5.1)
        tick0 = Line(UP * 0.18, DOWN * 0.18, color=WHITE,
                     stroke_width=2).move_to(UP * 5.1 + LEFT * 3.5)
        tick1 = Line(UP * 0.18, DOWN * 0.18, color=WHITE,
                     stroke_width=2).move_to(UP * 5.1 + RIGHT * 3.5)
        l0 = MathTex(r"0", font_size=28, color=WHITE).next_to(tick0, DOWN, buff=0.15)
        l1 = MathTex(r"1", font_size=28, color=WHITE).next_to(tick1, DOWN, buff=0.15)
        self.play(Create(line), Create(tick0), Create(tick1),
                  Write(l0), Write(l1), run_time=0.6)

        # 三个区域标注
        lbl_impossible = Text("不可能\nP=0", font="PingFang SC",
                              font_size=20, color=self.C_RED,
                              ).move_to(UP * 5.1 + LEFT * 3.5 + UP * 0.7)
        lbl_certain    = Text("必然\nP=1", font="PingFang SC",
                              font_size=20, color=self.C_GREEN,
                              ).move_to(UP * 5.1 + RIGHT * 3.5 + UP * 0.7)
        lbl_random     = Text("随机事件 0<P<1",
                              font="PingFang SC", font_size=22,
                              color=self.C_TITLE,
                              ).move_to(UP * 4.3)
        self.play(Write(lbl_impossible), Write(lbl_certain),
                  FadeIn(lbl_random), run_time=0.6)

        # 三道例子
        eg_data = [
            ("P = 0", "太阳从西边升起", self.C_RED,   UP * 3.3),
            ("P = 1", "明天太阳从东边升起", self.C_GREEN, UP * 2.3),
            ("P = 1/2", "抛硬币正面朝上", self.C_TITLE, UP * 1.3),
        ]
        for pstr, desc, col, pos in eg_data:
            bg = self.card(7.0, 0.95, col, pos)
            t  = VGroup(
                Text(pstr, font="PingFang SC", font_size=22, color=col),
                Text(desc, font="PingFang SC", font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(t), run_time=0.4)

        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 7 ───────────
    def scene_quick_practice(self):
        title = Text("综合练习",
                     font="PingFang SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        items = [
            (r"\text{Coin toss: } P(\text{head})",
             r"= \dfrac{1}{2}", self.C_GREEN, "n=2, m=1"),
            (r"\text{2R 3B, draw 1: } P(R)",
             r"= \dfrac{2}{5}", self.C_MAIN,  "n=5, m=2"),
            (r"\text{Die: } P(\text{>4})",
             r"= \dfrac{2}{6}=\dfrac{1}{3}", self.C_PURPLE, "n=6, m=2 (5,6)"),
        ]
        card_h = 1.72
        start_y, gap = 5.1, 1.80
        for i, (prob, res, col, hint) in enumerate(items):
            pos = UP * (start_y - i * gap)
            bg  = self.card(7.6, card_h, col, pos)
            pf  = MathTex(prob, font_size=28, color=WHITE)
            rf  = MathTex(res,  font_size=30, color=self.C_RESULT)
            ht  = Text(hint, font="PingFang SC",
                       font_size=19, color=GRAY_A)
            VGroup(VGroup(pf, rf).arrange(RIGHT, buff=0.3), ht
                   ).arrange(DOWN, buff=0.12).move_to(pos)
            self.play(Create(bg), run_time=0.15)
            self.play(Write(pf), run_time=0.28)
            self.play(Write(rf), FadeIn(ht), run_time=0.30)
            self.wait(0.20)

        self.wait(1.5)
        self.fade_rest()

    # ─────────── Scene 8 ───────────
    def scene_summary(self):
        title = Text("知识点总结",
                     font="PingFang SC", font_size=46, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        blocks = [
            (self.C_MAIN,   UP * 5.5,  "核心公式",
             r"P(A)=\dfrac{m}{n}"),
            (self.C_GREEN,  UP * 4.0,  "概率范围",
             r"0 \leq P(A) \leq 1"),
            (self.C_ORANGE, UP * 2.5,  "等可能性",
             r"n\ \text{equally likely outcomes}"),
            (self.C_PURPLE, UP * 1.0,  "例题",
             r"P(\text{even on die})=\dfrac{3}{6}=\dfrac{1}{2}"),
            (self.C_RESULT, DOWN * 0.5,"摸球",
             r"P(\text{red})=\dfrac{3}{5}"),
        ]
        for col, pos, lbl, fml in blocks:
            bg = self.card(7.6, 1.3, col, pos)
            lt = Text(lbl, font="PingFang SC", font_size=22, color=col)
            ft = MathTex(fml, font_size=28, color=WHITE)
            VGroup(lt, ft).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(lt), Write(ft), run_time=0.42)

        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 9 ───────────
    def scene_outro(self):
        big = Text("上海初高中数学直通车",
                   font="PingFang SC", font_size=38, color=WHITE,
                   ).move_to(UP * 2.5)
        uid = Text("@emptyandcalm",
                   font="PingFang SC", font_size=28, color=GRAY_B,
                   ).move_to(UP * 1.7)
        self.play(Transform(self.author, big), run_time=0.8)
        self.play(FadeIn(uid, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，学更多数学知识！",
                      font="PingFang SC", font_size=30,
                      color=self.C_TITLE).move_to(UP * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        deco = VGroup(
            MathTex(r"P(A)=\dfrac{m}{n}", font_size=30, color=self.C_MAIN),
            MathTex(r"0\leq P(A)\leq 1",  font_size=30, color=self.C_GREEN),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 1.8)
        self.play(*[Write(f) for f in deco], run_time=0.9)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.8)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# manim -pql probability_definition.py ProbabilityDefinition
# manim -qh  probability_definition.py ProbabilityDefinition