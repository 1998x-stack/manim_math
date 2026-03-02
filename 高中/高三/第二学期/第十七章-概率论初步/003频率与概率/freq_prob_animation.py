"""
频率与概率 - 高三数学教学动画
概率论初步: 频率与概率的关系、大数定律
目标: 高三学生 | 格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 - TikTok竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

AUTHOR_FONT = "Noto Sans CJK SC"

# 颜色方案
BG_COLOR = "#1a1a2e"
COLOR_FREQ = "#e74c3c"       # 红色 - 频率线
COLOR_PROB = "#3498db"       # 蓝色 - 概率虚线
COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 强调
COLOR_GREEN = "#2ecc71"      # 绿色 - 正面
COLOR_ORANGE = "#e67e22"     # 橙色 - 反面/背面
COLOR_AXES = "#7f8c8d"       # 灰色 - 坐标轴
COLOR_CARD = "#16213e"       # 深蓝 - 卡片背景
COLOR_GOLD = "#f39c12"


class FreqProbAnimation(Scene):
    """
    频率与概率教学动画
    场景:
    1. 开场钩子
    2. 频率定义与公式
    3. 抛硬币模拟 (小n, 波动大)
    4. 大数定律 (n增大, 收敛)
    5. 频率与概率关系总结
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_data()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_simulation_small_n()
        self.scene_4_law_of_large_numbers()
        self.scene_5_summary()
        self.scene_6_outro()

    # ================================================================
    #   数据初始化
    # ================================================================

    def setup_data(self):
        """预计算所有模拟数据（seed 固定，保证可复现）"""
        np.random.seed(42)
        self.N = 200
        flips = np.random.randint(0, 2, self.N)   # 0=反面, 1=正面
        cum = np.cumsum(flips)
        self.trial_nums = np.arange(1, self.N + 1)
        self.freqs = cum / self.trial_nums           # 运行频率

        # 关键检查点
        self.freq_n10  = self.freqs[9]
        self.freq_n50  = self.freqs[49]
        self.freq_n100 = self.freqs[99]
        self.freq_n200 = self.freqs[199]

    # ================================================================
    #   Scene 1: 开场钩子
    # ================================================================

    def scene_1_opening(self):
        # 作者信息（常驻顶部）
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=AUTHOR_FONT, font_size=18, color=COLOR_AXES
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 大钩子问题
        q1 = Text("抛一枚硬币", font=AUTHOR_FONT, font_size=52, color=WHITE)
        q2 = Text("1000 次", font=AUTHOR_FONT, font_size=72, color=COLOR_HIGHLIGHT)
        q3 = Text("正面大约出现几次?", font=AUTHOR_FONT, font_size=42, color=WHITE)
        hook = VGroup(q1, q2, q3).arrange(DOWN, buff=0.35).move_to(UP * 4.5)

        self.play(Write(q1), run_time=0.6)
        self.play(FadeIn(q2, scale=1.2), run_time=0.5)
        self.play(Write(q3), run_time=0.6)
        self.wait(0.6)

        # 硬币图标
        coin_h = Circle(radius=0.6, fill_color=COLOR_GOLD, fill_opacity=1,
                        stroke_color=WHITE, stroke_width=3)
        h_text = Text("正", font=AUTHOR_FONT, font_size=28, color=WHITE)
        coin_head = VGroup(coin_h, h_text).move_to(LEFT * 2 + UP * 1.8)

        coin_t = Circle(radius=0.6, fill_color=COLOR_ORANGE, fill_opacity=1,
                        stroke_color=WHITE, stroke_width=3)
        t_text = Text("反", font=AUTHOR_FONT, font_size=28, color=WHITE)
        coin_tail = VGroup(coin_t, t_text).move_to(RIGHT * 2 + UP * 1.8)

        self.play(
            GrowFromCenter(coin_head),
            GrowFromCenter(coin_tail),
            run_time=0.6
        )

        # 答案悬念
        ans = Text("约 500 次？", font=AUTHOR_FONT, font_size=38, color=COLOR_GREEN)
        ans.move_to(UP * 0.3)
        self.play(FadeIn(ans, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)

        key = Text("这就是频率与概率的关系！", font=AUTHOR_FONT,
                   font_size=32, color=COLOR_FREQ)
        key.move_to(DOWN * 0.8)
        self.play(Write(key), run_time=0.7)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook), FadeOut(coin_head), FadeOut(coin_tail),
            FadeOut(ans), FadeOut(key),
            run_time=0.5
        )

    # ================================================================
    #   Scene 2: 频率的定义与公式
    # ================================================================

    def scene_2_definition(self):
        # 标题
        title = Text("频率的定义", font=AUTHOR_FONT, font_size=44,
                     color=COLOR_HIGHLIGHT)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # ---- 公式说明 ----
        desc1 = Text("n 次试验中，事件 A 发生了 m 次", font=AUTHOR_FONT,
                     font_size=28, color=GRAY_A)
        desc1.move_to(UP * 5.0)
        self.play(FadeIn(desc1, shift=UP * 0.2), run_time=0.5)

        # MathTex 公式
        formula = MathTex(
            r"f_n(A) = \frac{m}{n}",
            font_size=72, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(formula), run_time=0.8)

        # 彩色标注
        m_label = Text("事件发生次数", font=AUTHOR_FONT, font_size=22,
                       color=COLOR_FREQ)
        n_label = Text("总试验次数", font=AUTHOR_FONT, font_size=22,
                       color=COLOR_PROB)
        m_label.move_to(LEFT * 1.8 + UP * 2.5)
        n_label.move_to(RIGHT * 1.5 + UP * 2.5)

        arr_m = Arrow(m_label.get_right(), formula.get_left() + UP * 0.3,
                      buff=0.1, color=COLOR_FREQ, stroke_width=2)
        arr_n = Arrow(n_label.get_left(), formula.get_right() + DOWN * 0.15,
                      buff=0.1, color=COLOR_PROB, stroke_width=2)

        self.play(
            FadeIn(m_label), FadeIn(n_label),
            GrowArrow(arr_m), GrowArrow(arr_n),
            run_time=0.6
        )
        self.wait(0.4)

        # ---- 数值示例 ----
        eg_title = Text("例：掷骰子10次，3点出现4次", font=AUTHOR_FONT,
                        font_size=26, color=GRAY_A)
        eg_title.move_to(UP * 1.4)

        eg_formula = MathTex(
            r"f_{10}(A) = \frac{4}{10} = 0.4",
            font_size=56, color=COLOR_GREEN
        ).move_to(UP * 0.3)

        self.play(FadeIn(eg_title), run_time=0.4)
        self.play(Write(eg_formula), run_time=0.7)
        self.wait(0.3)

        # ---- 三条性质 ----
        prop_title = Text("频率的三条性质", font=AUTHOR_FONT,
                          font_size=32, color=COLOR_HIGHLIGHT)
        prop_title.move_to(DOWN * 0.8)
        self.play(Write(prop_title), run_time=0.5)

        # ✅ 最简洁修复：scene_2_definition 中直接构建
        prop1 = VGroup(
            Text("① ", font=AUTHOR_FONT, font_size=26, color=COLOR_HIGHLIGHT),
            MathTex(r"0 \leq f_n(A) \leq 1", font_size=30, color=WHITE),
            Text("频率在0到1之间", font=AUTHOR_FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2)

        prop2 = VGroup(
            Text("② ", font=AUTHOR_FONT, font_size=26, color=COLOR_HIGHLIGHT),
            MathTex(r"f = 1", font_size=30, color=WHITE),
            Text("必然事件频率为1", font=AUTHOR_FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2)

        prop3 = VGroup(
            Text("③ ", font=AUTHOR_FONT, font_size=26, color=COLOR_HIGHLIGHT),
            MathTex(r"f = 0", font_size=30, color=WHITE),
            Text("不可能事件频率为0", font=AUTHOR_FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2)

        props = VGroup(prop1, prop2, prop3).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to(DOWN * 2.6)

        for prop in props:
            self.play(FadeIn(prop, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.1)

        self.wait(1.0)

        # ---- 随机波动性提示 ----
        wave_hint = Text("⚠ 频率具有随机波动性！", font=AUTHOR_FONT,
                         font_size=30, color=COLOR_ORANGE)
        wave_hint.move_to(DOWN * 4.8)
        box = SurroundingRectangle(wave_hint, color=COLOR_ORANGE,
                                   buff=0.15, corner_radius=0.1)
        self.play(Create(box), Write(wave_hint), run_time=0.6)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(VGroup(title, desc1, formula, m_label, n_label,
                           arr_m, arr_n, eg_title, eg_formula,
                           prop_title, props, wave_hint, box)),
            run_time=0.5
        )

    def _make_prop(self, num_str, math_left, math_right_or_text, cn_str, use_text_for_middle=False):
        """
        创建一条性质行
        use_text_for_middle=True 时，中间部分用 Text 而非 MathTex
        """
        num = Text(num_str, font=AUTHOR_FONT, font_size=26, color=COLOR_HIGHLIGHT)
        desc = Text(cn_str, font=AUTHOR_FONT, font_size=22, color=GRAY_A)

        if use_text_for_middle:
            # ✅ 含中文的部分用 Text，纯数学用 MathTex，再组合
            mid = Text(math_right_or_text, font=AUTHOR_FONT, font_size=24, color=WHITE)
            row = VGroup(num, mid, desc).arrange(RIGHT, buff=0.2)
        else:
            formula = MathTex(math_left, font_size=32, color=WHITE)
            row = VGroup(num, formula, desc).arrange(RIGHT, buff=0.2)
        return row

    # ================================================================
    #   Scene 3: 小n时频率波动大
    # ================================================================

    def scene_3_simulation_small_n(self):
        title = Text("频率的随机波动性", font=AUTHOR_FONT, font_size=40,
                     color=COLOR_FREQ)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        subtitle = Text("试验次数少时，频率很不稳定", font=AUTHOR_FONT,
                        font_size=26, color=GRAY_A)
        subtitle.move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---- 建立坐标轴（仅前30次）----
        axes = Axes(
            x_range=[0, 31, 5],
            y_range=[0, 1.05, 0.25],
            x_length=6.5,
            y_length=4.0,
            axis_config={
                "color": COLOR_AXES,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.15,
            },
            x_axis_config={"numbers_to_include": [5, 10, 15, 20, 25, 30]},
            y_axis_config={"numbers_to_include": [0.25, 0.5, 0.75, 1.0]},
        ).move_to(DOWN * 0.5)

        x_label = Text("试验次数 n", font=AUTHOR_FONT, font_size=22,
                       color=COLOR_AXES).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("频率", font=AUTHOR_FONT, font_size=22,
                       color=COLOR_AXES).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI/2)

        self.play(Create(axes), run_time=0.8)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)

        # 概率基准线 P = 0.5
        prob_line = DashedLine(
            axes.c2p(0, 0.5), axes.c2p(31, 0.5),
            color=COLOR_PROB, dash_length=0.12, stroke_width=2.5
        )
        prob_label = MathTex(r"P(A) = 0.5", font_size=30, color=COLOR_PROB)
        prob_label.next_to(axes.c2p(31, 0.5), RIGHT, buff=0.05)
        self.play(Create(prob_line), FadeIn(prob_label), run_time=0.5)

        # ---- 逐步绘制频率折线（前30次）----
        n_show = 30
        points = [axes.c2p(i + 1, self.freqs[i]) for i in range(n_show)]
        freq_dot = Dot(points[0], radius=0.06, color=COLOR_FREQ)
        self.play(FadeIn(freq_dot), run_time=0.2)

        # 动态绘制折线
        line_segments = VGroup()
        dots = VGroup(freq_dot)

        tracker = ValueTracker(0)
        current_point = [points[0]]

        # 批量绘制前 30 段
        for i in range(1, n_show):
            seg = Line(points[i - 1], points[i], color=COLOR_FREQ, stroke_width=2.5)
            dot = Dot(points[i], radius=0.05, color=COLOR_FREQ)
            line_segments.add(seg)
            dots.add(dot)
            self.play(Create(seg), FadeIn(dot), run_time=0.08)

        self.wait(0.3)

        # 标注波动
        wave_text = Text("波动很大！", font=AUTHOR_FONT, font_size=32,
                         color=COLOR_ORANGE)
        wave_text.move_to(DOWN * 3.8)

        arrow_wave = Arrow(
            wave_text.get_top(),
            axes.c2p(5, self.freqs[4]),
            buff=0.1, color=COLOR_ORANGE, stroke_width=2
        )

        self.play(
            FadeIn(wave_text, shift=UP * 0.3),
            GrowArrow(arrow_wave),
            run_time=0.6
        )

        # 当前n值显示
        n_val_text = Text("n = 30", font=AUTHOR_FONT, font_size=28,
                          color=COLOR_HIGHLIGHT)
        freq_val_text = Text(f"f = {self.freqs[29]:.3f}", font=AUTHOR_FONT,
                             font_size=28, color=COLOR_FREQ)
        VGroup(n_val_text, freq_val_text).arrange(RIGHT, buff=0.5).move_to(DOWN * 5.0)

        self.play(FadeIn(n_val_text), FadeIn(freq_val_text), run_time=0.4)
        self.wait(0.8)

        # 清场 (保留 axes, prob_line, prob_label 到下一场景)
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(wave_text), FadeOut(arrow_wave),
            FadeOut(n_val_text), FadeOut(freq_val_text),
            run_time=0.4
        )

        # 保存给下一场景使用
        self._axes = axes
        self._x_label = x_label
        self._y_label = y_label
        self._prob_line = prob_line
        self._prob_label = prob_label
        self._small_n_lines = line_segments
        self._small_n_dots = dots

    # ================================================================
    #   Scene 4: 大数定律 - n 增大，频率趋向概率
    # ================================================================

    def scene_4_law_of_large_numbers(self):
        # 新标题
        title = Text("大数定律", font=AUTHOR_FONT, font_size=48,
                     color=COLOR_HIGHLIGHT)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        subtitle = Text("n 越大，频率越接近概率", font=AUTHOR_FONT,
                        font_size=30, color=GRAY_A)
        subtitle.move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---- 扩展坐标轴到 n=200 ----
        axes2 = Axes(
            x_range=[0, 210, 50],
            y_range=[0, 1.05, 0.25],
            x_length=6.5,
            y_length=4.0,
            axis_config={
                "color": COLOR_AXES,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.15,
            },
            x_axis_config={"numbers_to_include": [50, 100, 150, 200]},
            y_axis_config={"numbers_to_include": [0.25, 0.5, 0.75, 1.0]},
        ).move_to(DOWN * 0.5)

        x_label2 = Text("试验次数 n", font=AUTHOR_FONT, font_size=22,
                        color=COLOR_AXES).next_to(axes2.x_axis, DOWN, buff=0.3)
        y_label2 = Text("频率", font=AUTHOR_FONT, font_size=22,
                        color=COLOR_AXES).next_to(axes2.y_axis, LEFT, buff=0.1).rotate(PI/2)

        # 过渡：用新坐标轴替换旧坐标轴
        self.play(
            Transform(self._axes, axes2),
            FadeOut(self._small_n_lines),
            FadeOut(self._small_n_dots),
            FadeOut(self._x_label),
            FadeOut(self._y_label),
            run_time=0.6
        )
        self.play(FadeIn(x_label2), FadeIn(y_label2), run_time=0.3)

        # 新的概率基准线
        prob_line2 = DashedLine(
            axes2.c2p(0, 0.5), axes2.c2p(210, 0.5),
            color=COLOR_PROB, dash_length=0.12, stroke_width=2.5
        )
        prob_label2 = MathTex(r"P(A) = 0.5", font_size=28, color=COLOR_PROB)
        prob_label2.next_to(axes2.c2p(210, 0.5), RIGHT, buff=0.05)
        self.play(
            Transform(self._prob_line, prob_line2),
            Transform(self._prob_label, prob_label2),
            run_time=0.4
        )

        # ---- 绘制完整200次频率折线 ----
        # 用 ParametricFunction 流畅显示
        def freq_func(t):
            idx = max(0, min(int(t) - 1, self.N - 1))
            return axes2.c2p(t, self.freqs[idx])

        # 构建折线点集
        all_points = [axes2.c2p(i + 1, self.freqs[i]) for i in range(self.N)]

        freq_polyline = VMobject(color=COLOR_FREQ, stroke_width=2.5)
        freq_polyline.set_points_as_corners(all_points)

        self.play(Create(freq_polyline), run_time=3.5, rate_func=linear)

        # ---- 阶段标注 ----
        # 前期: 波动大
        brace_early = BraceBetweenPoints(
            axes2.c2p(0, -0.12), axes2.c2p(50, -0.12), direction=DOWN
        )
        early_label = Text("n 小：波动大", font=AUTHOR_FONT, font_size=22,
                           color=COLOR_ORANGE)
        early_label.next_to(brace_early, DOWN, buff=0.1)

        self.play(FadeIn(brace_early), FadeIn(early_label), run_time=0.5)

        # 后期: 收敛
        brace_late = BraceBetweenPoints(
            axes2.c2p(150, -0.12), axes2.c2p(200, -0.12), direction=DOWN
        )
        late_label = Text("n 大：趋于稳定", font=AUTHOR_FONT, font_size=22,
                          color=COLOR_GREEN)
        late_label.next_to(brace_late, DOWN, buff=0.1)

        self.play(FadeIn(brace_late), FadeIn(late_label), run_time=0.5)
        self.wait(0.5)

        # ---- 核心公式 ----
        core_formula = MathTex(
            r"n \to \infty \Rightarrow f_n(A) \to P(A)",
            font_size=40, color=WHITE
        ).move_to(DOWN * 4.0)

        box_formula = SurroundingRectangle(
            core_formula, color=COLOR_HIGHLIGHT, buff=0.2, corner_radius=0.1
        )

        self.play(
            Write(core_formula),
            Create(box_formula),
            run_time=0.8
        )
        self.wait(0.4)

        # ---- 大数定律说明 ----
        law_title = Text("大数定律", font=AUTHOR_FONT, font_size=32,
                         color=COLOR_HIGHLIGHT)
        law_title.move_to(DOWN * 5.3)
        law_desc = Text("试验次数足够大时，频率稳定于概率",
                        font=AUTHOR_FONT, font_size=24, color=GRAY_A)
        law_desc.move_to(DOWN * 6.0)

        self.play(FadeIn(law_title), FadeIn(law_desc), run_time=0.5)
        self.wait(1.2)

        # 清场，保存折线供下场景用
        self._freq_polyline = freq_polyline
        self._axes2 = axes2
        self._x_label2 = x_label2
        self._y_label2 = y_label2

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(brace_early), FadeOut(early_label),
            FadeOut(brace_late), FadeOut(late_label),
            FadeOut(core_formula), FadeOut(box_formula),
            FadeOut(law_title), FadeOut(law_desc),
            FadeOut(self._axes), FadeOut(self._freq_polyline),
            FadeOut(self._prob_line), FadeOut(self._prob_label),
            FadeOut(x_label2), FadeOut(y_label2),
            run_time=0.6
        )

    # ================================================================
    #   Scene 5: 频率与概率关系总结
    # ================================================================
    def scene_5_summary(self):
        title = Text("频率  vs  概率", font=AUTHOR_FONT, font_size=46,
                    color=COLOR_HIGHLIGHT)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        card_freq = self._make_card(
            "频率  f_n(A)",
            ["随机的、变化的", "每次试验结果不同",
            "取决于试验次数 n", "= m/n（可计算）"],
            COLOR_FREQ, LEFT * 2.0 + UP * 2.5
        )
        card_prob = self._make_card(
            "概率  P(A)",
            ["确定的、稳定的", "事件本身的性质",
            "不随试验次数变化", "频率的极限（稳定值）"],
            COLOR_PROB, RIGHT * 2.0 + UP * 2.5
        )
        self.play(FadeIn(card_freq, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(card_prob, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.5)

        arrow_left = Arrow(ORIGIN + UP * 2.5 + LEFT * 0.5,
                        ORIGIN + UP * 2.5 + LEFT * 0.05,
                        buff=0, color=COLOR_HIGHLIGHT, stroke_width=2)
        arrow_right = Arrow(ORIGIN + UP * 2.5 + RIGHT * 0.05,
                            ORIGIN + UP * 2.5 + RIGHT * 0.5,
                            buff=0, color=COLOR_HIGHLIGHT, stroke_width=2)
        n_grow = Text("n↑", font=AUTHOR_FONT, font_size=22,
                    color=COLOR_HIGHLIGHT).move_to(UP * 2.5)
        self.play(GrowArrow(arrow_left), GrowArrow(arrow_right),
                FadeIn(n_grow), run_time=0.4)

        rel_1 = Text("概率是频率的稳定值", font=AUTHOR_FONT, font_size=30, color=WHITE)
        rel_2 = Text("频率是概率的近似值", font=AUTHOR_FONT, font_size=30, color=WHITE)
        VGroup(rel_1, rel_2).arrange(DOWN, buff=0.35).move_to(DOWN * 0.8)
        icon_1 = Text("→", font=AUTHOR_FONT, font_size=30, color=COLOR_GREEN)
        icon_2 = Text("≈", font=AUTHOR_FONT, font_size=36, color=COLOR_GREEN)
        icon_1.next_to(rel_1, LEFT, buff=0.2)
        icon_2.next_to(rel_2, LEFT, buff=0.2)
        self.play(FadeIn(rel_1, shift=UP * 0.2), FadeIn(icon_1), run_time=0.5)
        self.play(FadeIn(rel_2, shift=UP * 0.2), FadeIn(icon_2), run_time=0.5)
        self.wait(0.4)

        approx_math = MathTex(r"f_n(A) \approx P(A)",
                            font_size=42, color=COLOR_HIGHLIGHT)
        approx_note = Text("（n 足够大）", font=AUTHOR_FONT,
                        font_size=32, color=COLOR_HIGHLIGHT)
        approx = VGroup(approx_math, approx_note).arrange(RIGHT, buff=0.3)
        approx.move_to(DOWN * 2.3)
        approx_box = SurroundingRectangle(approx, color=COLOR_HIGHLIGHT,
                                        buff=0.2, corner_radius=0.12)
        self.play(Write(approx_math), FadeIn(approx_note),
                Create(approx_box), run_time=0.7)
        self.wait(0.4)

        motto_bg = RoundedRectangle(width=7.5, height=1.0, corner_radius=0.2,
                                    fill_color=COLOR_CARD, fill_opacity=0.9,
                                    stroke_color=COLOR_GOLD, stroke_width=2)
        motto_bg.move_to(DOWN * 4.0)
        motto = Text("「次数越多，频率越稳，越接近概率」",
                    font=AUTHOR_FONT, font_size=24, color=COLOR_GOLD)
        motto.move_to(DOWN * 4.0)
        self.play(FadeIn(motto_bg), Write(motto), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(
                title, card_freq, card_prob,
                arrow_left, arrow_right, n_grow,
                rel_1, rel_2, icon_1, icon_2,
                approx, approx_box,
                motto_bg, motto
            )),
            run_time=0.5
        )

    def _make_card(self, title_str, items, color, position):
        """创建对比卡片"""
        title_text = Text(title_str, font=AUTHOR_FONT, font_size=24, color=color)

        item_group = VGroup(*[
            Text(f"• {item}", font=AUTHOR_FONT, font_size=20, color=GRAY_A)
            for item in items
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        content = VGroup(title_text, item_group).arrange(DOWN, buff=0.3)

        bg = RoundedRectangle(
            width=max(content.width + 0.6, 3.4),
            height=content.height + 0.5,
            corner_radius=0.15,
            fill_color=COLOR_CARD,
            fill_opacity=0.95,
            stroke_color=color,
            stroke_width=2
        )

        card = VGroup(bg, content)
        content.move_to(bg.get_center())
        card.move_to(position)
        return card

    # ================================================================
    #   Scene 6: 片尾
    # ================================================================

    def scene_6_outro(self):
        # 总结横幅
        summary_title = Text("本节要点", font=AUTHOR_FONT, font_size=38,
                             color=COLOR_HIGHLIGHT)
        summary_title.move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.4)

        key_points = VGroup(
            Text("① 频率 = 事件发生次数 / 总次数", font=AUTHOR_FONT,
                 font_size=26, color=WHITE),
            Text("② 0 ≤ 频率 ≤ 1，频率有随机波动", font=AUTHOR_FONT,
                 font_size=26, color=WHITE),
            Text("③ n 越大，频率越趋近于概率", font=AUTHOR_FONT,
                 font_size=26, color=COLOR_GREEN),
            Text("④ 大数定律：频率稳定于概率", font=AUTHOR_FONT,
                 font_size=26, color=COLOR_GOLD),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        key_points.move_to(UP * 2.5)

        for kp in key_points:
            self.play(FadeIn(kp, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(0.8)

        # 作者放大
        author_big = Text("上海初高中数学直通车",
                          font=AUTHOR_FONT, font_size=38, color=WHITE)
        author_id = Text("@emptyandcalm",
                         font=AUTHOR_FONT, font_size=28, color=COLOR_AXES)
        VGroup(author_big, author_id).arrange(DOWN, buff=0.2).move_to(DOWN * 1.5)

        self.play(
            FadeOut(summary_title), FadeOut(key_points),
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow = Text("关注我，获得更多数学技巧！",
                      font=AUTHOR_FONT, font_size=32, color=COLOR_HIGHLIGHT)
        follow.move_to(DOWN * 3.0)
        follow_box = SurroundingRectangle(
            follow, color=COLOR_HIGHLIGHT, buff=0.2, corner_radius=0.1
        )

        self.play(
            FadeIn(follow, scale=1.1),
            Create(follow_box),
            run_time=0.6
        )

        # 装饰：闪烁圆环
        rings = VGroup(*[
            Circle(radius=0.15 + 0.1 * i, color=COLOR_HIGHLIGHT,
                   stroke_width=1.5, fill_opacity=0)
            .move_to(DOWN * 3.0)
            for i in range(4)
        ])
        self.play(
            *[ring.animate.scale(3).set_opacity(0) for ring in rings],
            run_time=1.2, rate_func=linear
        )

        # 频率公式动画收尾
        final_formula = MathTex(
            r"f_n(A) \xrightarrow{n \to \infty} P(A)",
            font_size=48, color=WHITE
        ).move_to(DOWN * 5.0)
        self.play(Write(final_formula), run_time=0.8)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(VGroup(
                self.author_bar,
                author_big, author_id,
                follow, follow_box,
                final_formula
            )),
            run_time=1.0
        )
        self.wait(0.5)


# ================================================================
#   入口
# ================================================================
# 渲染命令:
#   预览: manim -pql freq_prob_animation.py FreqProbAnimation
#   高清: manim -qh  freq_prob_animation.py FreqProbAnimation