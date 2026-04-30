"""
频率与概率的关系 — 教学动画
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


class ProbabilityFrequency(Scene):
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
        self.scene_freq_def()
        self.scene_freq_chart()
        self.scene_limit()
        self.scene_history()
        self.scene_comparison()
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

        hook = Text("抛 10 次硬币：7次正面",
                    font="PingFang SC", font_size=34, color=self.C_TITLE,
                    ).move_to(UP * 5.7)
        hook2 = Text("抛 1000 次呢？",
                     font="PingFang SC", font_size=34, color=self.C_ORANGE,
                     ).move_to(UP * 5.0)
        self.play(Write(hook), run_time=0.6)
        self.play(Write(hook2), run_time=0.5)
        self.wait(0.5)

        freq10 = MathTex(r"f_{10} = \dfrac{7}{10} = 0.7",
                         font_size=42, color=self.C_RED).move_to(UP * 3.8)
        freq1000 = MathTex(r"f_{1000} \approx \dfrac{502}{1000} \approx 0.5",
                           font_size=42, color=self.C_GREEN).move_to(UP * 2.8)
        self.play(Write(freq10), run_time=0.5)
        self.wait(0.3)
        self.play(Write(freq1000), run_time=0.5)

        insight = Text("次数越多，频率越稳定！",
                       font="PingFang SC", font_size=30, color=self.C_TITLE,
                       ).move_to(UP * 1.5)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(chapter), FadeOut(hook), FadeOut(hook2),
                  FadeOut(freq10), FadeOut(freq1000), FadeOut(insight),
                  run_time=0.4)

    # ─────────── Scene 2 ───────────
    def scene_freq_def(self):
        title = Text("频率的定义",
                     font="PingFang SC", font_size=46, color=self.C_TITLE,
                     ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.5)

        formula_bg = self.card(7.6, 2.2, self.C_MAIN, UP * 5.1,
                               fill="#0f2a3a", alpha=0.95)
        formula = MathTex(r"f(A) = \dfrac{k}{n}",
                          font_size=60, color=WHITE).move_to(UP * 5.1)
        self.play(Create(formula_bg), Write(formula), run_time=0.7)

        # 标注 k 和 n
        k_bg = self.card(3.3, 1.4, self.C_ORANGE, UP * 3.6 + LEFT * 1.85)
        k_t  = Text("k = 事件发生次数",
                    font="PingFang SC", font_size=20, color=self.C_ORANGE,
                    ).move_to(UP * 3.6 + LEFT * 1.85)
        n_bg = self.card(3.3, 1.4, self.C_PURPLE, UP * 3.6 + RIGHT * 1.85)
        n_t  = Text("n = 试验总次数",
                    font="PingFang SC", font_size=20, color=self.C_PURPLE,
                    ).move_to(UP * 3.6 + RIGHT * 1.85)
        self.play(Create(k_bg), Write(k_t), Create(n_bg), Write(n_t),
                  run_time=0.6)

        # 特性
        props_bg = self.card(7.4, 2.8, self.C_PURPLE, UP * 1.9)
        p1 = Text("① 0 ≤ f(A) ≤ 1",
                  font="PingFang SC", font_size=24, color=WHITE)
        p2 = Text("② n 增大，f(A) 趋于稳定",
                  font="PingFang SC", font_size=24, color=self.C_RESULT)
        p3 = Text("③ 稳定值即为概率 P(A)",
                  font="PingFang SC", font_size=24, color=self.C_TITLE)
        VGroup(p1, p2, p3).arrange(DOWN, buff=0.25).move_to(UP * 1.9)
        self.play(Create(props_bg), *[Write(t) for t in [p1, p2, p3]],
                  run_time=0.8)

        diff_bg = self.card(7.4, 1.5, self.C_RED, UP * 0.3, fill="#2d0a0a")
        diff_t1 = Text("频率 ≠ 概率",
                       font="PingFang SC", font_size=26, color=self.C_RED)
        diff_t2 = Text("（频率是统计值，概率是理论值）",
                       font="PingFang SC", font_size=20, color=GRAY_A)
        VGroup(diff_t1, diff_t2).arrange(RIGHT, buff=0.2).move_to(UP * 0.3)
        self.play(Create(diff_bg), Write(diff_t1), FadeIn(diff_t2), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 3: frequency chart ───────────
    def scene_freq_chart(self):
        title = Text("频率随试验次数的变化",
                     font="PingFang SC", font_size=32, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 轴参数
        ax_origin = np.array([-3.2, 2.8, 0])
        ax_w, ax_h = 6.0, 3.0
        n_max, f_max = 60.0, 1.0

        def to_screen(n_val, f_val):
            sx = ax_origin[0] + (n_val / n_max) * ax_w
            sy = ax_origin[1] + (f_val / f_max) * ax_h
            return np.array([sx, sy, 0])

        # 轴
        x_axis = Arrow(ax_origin, ax_origin + RIGHT * (ax_w + 0.3),
                       buff=0, color=GRAY_A, stroke_width=2,
                       max_tip_length_to_length_ratio=0.05)
        y_axis = Arrow(ax_origin, ax_origin + UP * (ax_h + 0.3),
                       buff=0, color=GRAY_A, stroke_width=2,
                       max_tip_length_to_length_ratio=0.05)
        x_lbl = Text("n（试验次数）",
                     font="PingFang SC", font_size=16, color=GRAY_A,
                     ).move_to(ax_origin + RIGHT * (ax_w + 0.7) + DOWN * 0.2)
        y_lbl = Text("f（频率）",
                     font="PingFang SC", font_size=16, color=GRAY_A,
                     ).move_to(ax_origin + UP * (ax_h + 0.55) + RIGHT * 0.5)
        y_tick = MathTex(r"0.5", font_size=18, color=GRAY_A).move_to(
            ax_origin + UP * ax_h * 0.5 + LEFT * 0.4)
        y_tick1 = MathTex(r"1", font_size=18, color=GRAY_A).move_to(
            ax_origin + UP * ax_h + LEFT * 0.3)
        self.play(Create(x_axis), Create(y_axis), Write(x_lbl),
                  Write(y_lbl), Write(y_tick), Write(y_tick1), run_time=0.6)

        # 虚线 y=0.5
        dash = DashedLine(
            to_screen(0, 0.5), to_screen(n_max, 0.5),
            color=self.C_TITLE, dash_length=0.15, stroke_width=1.5,
        )
        dash_lbl = MathTex(r"P=0.5", font_size=18, color=self.C_TITLE,
                           ).move_to(to_screen(n_max, 0.5) + RIGHT * 0.45)
        self.play(Create(dash), Write(dash_lbl), run_time=0.4)

        # 模拟频率数据
        np.random.seed(42)
        flips = np.random.randint(0, 2, 60)
        cumf  = np.cumsum(flips) / np.arange(1, 61)

        # 关键点：1,3,5,8,12,20,30,45,60
        key_ns = [1, 3, 5, 8, 12, 20, 30, 45, 60]
        prev_pt = None
        for n_i in key_ns:
            f_i = cumf[n_i - 1]
            pt  = to_screen(n_i, f_i)
            col = self.C_RED if abs(f_i - 0.5) > 0.15 else self.C_GREEN
            d   = Dot(pt, radius=0.1, color=col)
            self.play(GrowFromCenter(d), run_time=0.22)
            if prev_pt is not None:
                seg = Line(prev_pt, pt, color=self.C_MAIN, stroke_width=2)
                self.play(Create(seg), run_time=0.15)
            prev_pt = pt

        insight = Text("n越大，频率越靠近 0.5！",
                       font="PingFang SC", font_size=24, color=self.C_TITLE,
                       ).move_to(UP * 1.3)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=0.4)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 4: limit ───────────
    def scene_limit(self):
        title = Text("频率的极限 = 概率",
                     font="PingFang SC", font_size=38, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 大字极限公式
        lim_bg = self.card(7.6, 2.2, self.C_MAIN, UP * 5.2,
                           fill="#0f2a3a", alpha=0.95)
        lim_f  = MathTex(r"n \to \infty,\quad f(A) \to P(A)",
                         font_size=44, color=WHITE).move_to(UP * 5.2)
        self.play(Create(lim_bg), Write(lim_f), run_time=0.8)

        # 箭头说明
        arrow_bg = self.card(7.4, 2.8, self.C_PURPLE, UP * 3.3)
        a1_l = Text("频率", font="PingFang SC",
                    font_size=28, color=self.C_ORANGE)
        a1_arr = MathTex(r"\xrightarrow{n\to\infty}", font_size=36, color=WHITE)
        a1_r = Text("概率", font="PingFang SC",
                    font_size=28, color=self.C_GREEN)
        a1_row = VGroup(a1_l, a1_arr, a1_r).arrange(RIGHT, buff=0.3)

        a2_l = Text("统计值", font="PingFang SC",
                    font_size=22, color=self.C_ORANGE)
        a2_arr = MathTex(r"\xrightarrow{\text{converge}}", font_size=30,
                         color=GRAY_A)
        a2_r = Text("理论值", font="PingFang SC",
                    font_size=22, color=self.C_GREEN)
        a2_row = VGroup(a2_l, a2_arr, a2_r).arrange(RIGHT, buff=0.3)
        VGroup(a1_row, a2_row).arrange(DOWN, buff=0.4).move_to(UP * 3.3)
        self.play(Create(arrow_bg), Write(a1_row), Write(a2_row), run_time=0.8)

        # 实际应用
        app_bg = self.card(7.4, 1.8, self.C_GREEN, UP * 1.6)
        app_t1 = Text("实际应用：大量重复试验",
                      font="PingFang SC", font_size=24, color=self.C_GREEN)
        app_t2 = Text("用频率估计概率",
                      font="PingFang SC", font_size=24, color=WHITE)
        VGroup(app_t1, app_t2).arrange(DOWN, buff=0.15).move_to(UP * 1.6)
        self.play(Create(app_bg), Write(app_t1), Write(app_t2), run_time=0.6)

        rule_bg = self.card(7.4, 1.4, self.C_TITLE, UP * 0.3, fill="#1a1000")
        rule_t  = Text("大数定律：试验次数越大，频率越稳定",
                       font="PingFang SC", font_size=22,
                       color=self.C_TITLE).move_to(UP * 0.3)
        self.play(Create(rule_bg), Write(rule_t), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 5: history ───────────
    def scene_history(self):
        title = Text("历史实验数据",
                     font="PingFang SC", font_size=42, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        sub = Text("科学家抛硬币实验记录",
                   font="PingFang SC", font_size=24, color=GRAY_A,
                   ).move_to(UP * 5.7)
        self.play(FadeIn(sub), run_time=0.3)

        # 手工表格：三行数据
        headers = ["实验者", "抛掷次数", "正面次数", "频率"]
        data    = [
            ("蒲丰",   "4040",   "2048",  "0.5069"),
            ("皮尔逊", "12000",  "6019",  "0.5016"),
            ("皮尔逊", "24000",  "12012", "0.5005"),
        ]
        col_xs  = [-3.1, -0.9, 0.9, 2.9]
        header_y = 4.8
        row_ys   = [3.9, 2.95, 2.0]

        # 表头背景
        hdr_bg = RoundedRectangle(corner_radius=0.15, width=7.6, height=0.75,
                                  color=self.C_MAIN, fill_color="#0f2a3a",
                                  fill_opacity=0.9, stroke_width=1.5,
                                  ).move_to(np.array([0, header_y, 0]))
        self.play(Create(hdr_bg), run_time=0.3)
        for x, h in zip(col_xs, headers):
            t = Text(h, font="PingFang SC",
                     font_size=19, color=self.C_MAIN,
                     ).move_to(np.array([x, header_y, 0]))
            self.play(Write(t), run_time=0.15)

        # 数据行
        for row_y, (name, n, k, f) in zip(row_ys, data):
            row_bg = RoundedRectangle(
                corner_radius=0.1, width=7.6, height=0.75,
                color=GRAY_B, fill_color="#16213e",
                fill_opacity=0.85, stroke_width=1,
            ).move_to(np.array([0, row_y, 0]))
            self.play(Create(row_bg), run_time=0.18)
            for x, val in zip(col_xs, [name, n, k, f]):
                col = self.C_RESULT if val == f else WHITE
                t   = Text(val, font="PingFang SC",
                           font_size=19, color=col,
                           ).move_to(np.array([x, row_y, 0]))
                self.play(Write(t), run_time=0.15)

        # 频率列高亮说明
        note_bg = self.card(7.4, 1.6, self.C_GREEN, UP * 0.9)
        note_t1 = Text("所有频率都接近 0.5",
                       font="PingFang SC", font_size=24, color=self.C_GREEN)
        note_t2 = Text("次数越多越精确！",
                       font="PingFang SC", font_size=22, color=WHITE)
        VGroup(note_t1, note_t2).arrange(DOWN, buff=0.15).move_to(UP * 0.9)
        self.play(Create(note_bg), Write(note_t1), Write(note_t2), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 6: comparison ───────────
    def scene_comparison(self):
        title = Text("频率 vs 概率",
                     font="PingFang SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 左：频率
        l_bg = self.card(3.5, 5.0, self.C_ORANGE, UP * 3.8 + LEFT * 1.9)
        lt   = Text("频率", font="PingFang SC",
                    font_size=32, color=self.C_ORANGE).move_to(
            UP * 5.5 + LEFT * 1.9)
        props_l = [
            "f = k/n",
            "统计/实验得到",
            "随机，每次不同",
            "n大时趋稳",
            "概率的估计值",
        ]
        l_items = VGroup(*[
            Text(s, font="PingFang SC", font_size=19, color=WHITE)
            for s in props_l
        ]).arrange(DOWN, buff=0.28).move_to(UP * 3.8 + LEFT * 1.9)

        # 右：概率
        r_bg = self.card(3.5, 5.0, self.C_MAIN, UP * 3.8 + RIGHT * 1.9)
        rt   = Text("概率", font="PingFang SC",
                    font_size=32, color=self.C_MAIN).move_to(
            UP * 5.5 + RIGHT * 1.9)
        props_r = [
            "P = m/n",
            "理论计算得到",
            "固定不变",
            "与试验次数无关",
            "频率的极限值",
        ]
        r_items = VGroup(*[
            Text(s, font="PingFang SC", font_size=19, color=WHITE)
            for s in props_r
        ]).arrange(DOWN, buff=0.28).move_to(UP * 3.8 + RIGHT * 1.9)

        self.play(Create(l_bg), Create(r_bg),
                  Write(lt), Write(rt), run_time=0.5)
        self.play(*[Write(t) for t in l_items],
                  *[Write(t) for t in r_items], run_time=0.9)

        link_bg = self.card(7.4, 1.4, self.C_TITLE, UP * 1.1, fill="#1a1000")
        link_t  = Text("频率是概率的近似；概率是频率的稳定值",
                       font="PingFang SC", font_size=21,
                       color=self.C_TITLE).move_to(UP * 1.1)
        self.play(Create(link_bg), Write(link_t), run_time=0.5)
        self.wait(2.0)
        self.fade_rest()

    # ─────────── Scene 7: practice ───────────
    def scene_quick_practice(self):
        title = Text("综合练习",
                     font="PingFang SC", font_size=44, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        items = [
            ("某射手射击100次中靶72次",
             r"f = \dfrac{72}{100} = 0.72",
             self.C_MAIN, "k=72, n=100"),
            ("估计该射手命中率约为",
             r"P \approx 0.72",
             self.C_GREEN, "用频率估计概率"),
            ("试验次数越多，估计越",
             r"\text{accurate}",
             self.C_PURPLE, "大数定律"),
        ]
        card_h = 1.72
        start_y, gap = 5.1, 1.82
        for i, (q, res, col, hint) in enumerate(items):
            pos = UP * (start_y - i * gap)
            bg  = self.card(7.6, card_h, col, pos)
            qt  = Text(q, font="PingFang SC", font_size=22, color=WHITE)
            rf  = MathTex(res, font_size=30, color=self.C_RESULT)
            ht  = Text(hint, font="PingFang SC",
                       font_size=18, color=GRAY_A)
            VGroup(qt, rf, ht).arrange(DOWN, buff=0.15).move_to(pos)
            self.play(Create(bg), Write(qt), run_time=0.30)
            self.play(Write(rf), FadeIn(ht), run_time=0.30)
            self.wait(0.22)

        self.wait(1.5)
        self.fade_rest()

    # ─────────── Scene 8: summary ───────────
    def scene_summary(self):
        title = Text("知识点总结",
                     font="PingFang SC", font_size=46, color=self.C_TITLE,
                     ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.4)

        blocks = [
            (self.C_MAIN,   UP * 5.5, "频率公式",
             r"f(A) = \dfrac{k}{n}"),
            (self.C_PURPLE, UP * 4.0, "极限关系",
             r"n\to\infty \Rightarrow f(A)\to P(A)"),
            (self.C_ORANGE, UP * 2.5, "频率",
             r"\text{statistical, varies each time}"),
            (self.C_GREEN,  UP * 1.0, "概率",
             r"\text{theoretical, fixed value}"),
            (self.C_RESULT, DOWN * 0.5, "用途",
             r"f \approx P \text{ (large }n\text{)}"),
        ]
        for col, pos, lbl, fml in blocks:
            bg = self.card(7.6, 1.3, col, pos)
            lt = Text(lbl, font="PingFang SC", font_size=22, color=col)
            ft = MathTex(fml, font_size=26, color=WHITE)
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
            MathTex(r"f(A)=\dfrac{k}{n}", font_size=30, color=self.C_MAIN),
            MathTex(r"n\to\infty \Rightarrow f\to P", font_size=30,
                    color=self.C_GREEN),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 1.8)
        self.play(*[Write(f) for f in deco], run_time=0.9)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.8)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# manim -pql probability_frequency.py ProbabilityFrequency
# manim -qh  probability_frequency.py ProbabilityFrequency