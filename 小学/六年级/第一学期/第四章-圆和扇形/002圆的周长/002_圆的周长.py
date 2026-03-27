"""
圆的周长 - Circle Circumference Lesson
使用 Manim 创建的小学六年级数学教学视频

内容: 圆周率(pi)的概念、化曲为直的测量思想、圆周长公式 C=pi*d 和 C=2*pi*r
目标观众: 六年级小学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CircleCircumferenceLesson(Scene):
    """
    圆的周长 教学动画场景

    场景顺序:
    1. 开场钩子 - 提出问题
    2. 化曲为直 - 测量思想演示 (滚动法)
    3. 发现圆周率 - 多个圆的周长/直径比值恒定
    4. 圆周率 pi 的介绍
    5. 圆周长公式推导 C = pi*d = 2*pi*r
    6. 例题计算
    7. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色
        self.COLOR_CIRCLE = "#3498db"
        self.COLOR_DIAMETER = "#e74c3c"
        self.COLOR_CIRCUMFERENCE = "#2ecc71"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#f39c12"
        self.COLOR_PI = "#e74c3c"

        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_rolling_demo()
        self.scene_3_discover_pi()
        self.scene_4_pi_intro()
        self.scene_5_formula()
        self.scene_6_example()
        self.scene_7_outro()

    def setup_geometry(self):
        """初始化几何参数"""
        # 滚动演示用的圆
        self.roll_radius = 1.0
        self.roll_center = np.array([-3.0, 1.5, 0])

        # 发现 pi 用的三个圆 (不同大小)
        self.circle_radii = [0.6, 0.9, 1.2]

        # 验证: pi * d 应该等于周长
        for r in self.circle_radii:
            C = 2 * np.pi * r
            d = 2 * r
            ratio = C / d
            assert abs(ratio - np.pi) < 1e-10, f"Ratio check failed for r={r}"

    # =========================================================
    # Scene 1: Opening Hook
    # =========================================================
    def scene_1_opening(self):
        """开场: 提出问题引起兴趣"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 画一个圆
        circle = Circle(radius=1.5, color=self.COLOR_CIRCLE, stroke_width=4)
        circle.move_to(UP * 2.0)
        self.play(Create(circle), run_time=1.0)

        # 钩子问题
        hook = Text(
            "这个圆的周长是多少?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)

        self.play(Write(hook), run_time=0.8)
        self.wait(0.5)

        hook2 = Text(
            "弯曲的线怎么量?",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(circle),
            FadeOut(hook),
            FadeOut(hook2),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: Rolling Demo - 化曲为直
    # =========================================================
    def scene_2_rolling_demo(self):
        """演示圆在直线上滚动一圈, 展开为周长"""
        title = Text(
            "化曲为直",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        subtitle = Text(
            "让圆在直线上滚一圈",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 地面线
        r = self.roll_radius
        ground_y = -0.5
        # 圆心在 ground_y + r
        start_x = -3.5
        # 滚动距离 = 2*pi*r
        roll_distance = 2 * np.pi * r
        end_x = start_x + roll_distance

        ground_line = Line(
            np.array([start_x - 0.3, ground_y, 0]),
            np.array([end_x + 0.3, ground_y, 0]),
            color=GRAY_B,
            stroke_width=2
        )
        self.play(Create(ground_line), run_time=0.5)

        # 圆 -- 放在起点
        circle_center = np.array([start_x, ground_y + r, 0])
        rolling_circle = Circle(
            radius=r,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(circle_center)

        # 圆上标记点 (底部接触点)
        mark_dot = Dot(
            np.array([start_x, ground_y, 0]),
            color=self.COLOR_DIAMETER,
            radius=0.08
        )

        # 起点标记
        start_mark = Line(
            np.array([start_x, ground_y - 0.15, 0]),
            np.array([start_x, ground_y + 0.15, 0]),
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=3
        )
        start_label = Text(
            "起点",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_CIRCUMFERENCE
        ).next_to(start_mark, DOWN, buff=0.15)

        self.play(Create(rolling_circle), FadeIn(mark_dot), run_time=0.6)
        self.play(FadeIn(start_mark), FadeIn(start_label), run_time=0.3)
        self.wait(0.3)

        # 滚动动画: 圆向右滚动 2*pi*r
        # 使用 ValueTracker 控制滚动进度
        progress = ValueTracker(0.0)

        def update_circle(mob):
            t = progress.get_value()
            dx = t * roll_distance
            cx = start_x + dx
            cy = ground_y + r
            mob.move_to(np.array([cx, cy, 0]))
            # 旋转角 = dx / r (顺时针)
            mob.become(
                Circle(radius=r, color=self.COLOR_CIRCLE, stroke_width=3)
                .move_to(np.array([cx, cy, 0]))
                .rotate(-dx / r)
            )

        def update_dot(mob):
            t = progress.get_value()
            dx = t * roll_distance
            cx = start_x + dx
            cy = ground_y + r
            # 标记点绕圆心旋转, 初始在底部 (圆心正下方)
            angle = -dx / r  # 顺时针
            px = cx + r * np.sin(-angle)  # sin(-angle) for bottom start
            py = cy - r * np.cos(-angle)
            mob.move_to(np.array([px, py, 0]))

        rolling_circle.add_updater(update_circle)
        mark_dot.add_updater(update_dot)

        # 滚动中绘制轨迹线 (展开后的线段)
        trace_line = always_redraw(lambda: Line(
            np.array([start_x, ground_y - 0.05, 0]),
            np.array([start_x + progress.get_value() * roll_distance, ground_y - 0.05, 0]),
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=4
        ))
        self.add(trace_line)

        self.play(progress.animate.set_value(1.0), run_time=4.0, rate_func=linear)

        rolling_circle.clear_updaters()
        mark_dot.clear_updaters()
        self.remove(trace_line)

        # 终点标记
        final_trace = Line(
            np.array([start_x, ground_y - 0.05, 0]),
            np.array([end_x, ground_y - 0.05, 0]),
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=4
        )
        self.add(final_trace)

        end_mark = Line(
            np.array([end_x, ground_y - 0.15, 0]),
            np.array([end_x, ground_y + 0.15, 0]),
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=3
        )
        end_label = Text(
            "终点",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_CIRCUMFERENCE
        ).next_to(end_mark, DOWN, buff=0.15)

        self.play(FadeIn(end_mark), FadeIn(end_label), run_time=0.3)

        # 标注: 这段距离 = 周长
        brace = Brace(final_trace, DOWN, buff=0.5, color=self.COLOR_HIGHLIGHT)
        brace_label_cn = Text(
            "周长 C",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(brace, DOWN, buff=0.15)

        self.play(GrowFromCenter(brace), FadeIn(brace_label_cn), run_time=0.6)

        explain = Text(
            "圆滚一圈, 展开就是周长!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 也标注直径
        diam_line = Line(
            rolling_circle.get_left(),
            rolling_circle.get_right(),
            color=self.COLOR_DIAMETER,
            stroke_width=3
        )
        diam_label = Text(
            "d",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_DIAMETER
        ).next_to(diam_line, UP, buff=0.1)

        self.play(Create(diam_line), FadeIn(diam_label), run_time=0.5)

        question = Text(
            "周长和直径有什么关系?",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(ground_line), FadeOut(rolling_circle), FadeOut(mark_dot),
            FadeOut(start_mark), FadeOut(start_label),
            FadeOut(end_mark), FadeOut(end_label),
            FadeOut(final_trace), FadeOut(brace), FadeOut(brace_label_cn),
            FadeOut(explain), FadeOut(diam_line), FadeOut(diam_label),
            FadeOut(question),
            run_time=0.6
        )

    # =========================================================
    # Scene 3: Discover Pi
    # =========================================================
    def scene_3_discover_pi(self):
        """用三个不同大小的圆, 展示 C/d 总是约等于 3.14"""
        title = Text(
            "实验发现",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        subtitle = Text(
            "不同大小的圆, 周长/直径 = ?",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 三个圆的展示区域
        y_positions = [2.5, 0.0, -2.5]
        circle_colors = ["#3498db", "#2ecc71", "#e67e22"]

        all_elements = VGroup()

        for i, (r, y_pos, col) in enumerate(zip(self.circle_radii, y_positions, circle_colors)):
            d = 2 * r
            C = 2 * np.pi * r
            ratio = C / d

            # 圆
            circ = Circle(
                radius=r, color=col, stroke_width=3
            ).move_to(np.array([-2.5, y_pos, 0]))

            # 直径线
            diam = Line(
                circ.get_left(), circ.get_right(),
                color=self.COLOR_DIAMETER, stroke_width=2
            )

            # 直径标签
            d_text = MathTex(
                f"d={d:.1f}",
                font_size=20,
                color=self.COLOR_DIAMETER
            ).next_to(diam, DOWN, buff=0.08)

            # 周长值
            c_text_parts = VGroup(
                Text("C=", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_CIRCUMFERENCE),
                MathTex(f"{C:.2f}", font_size=20, color=self.COLOR_CIRCUMFERENCE)
            ).arrange(RIGHT, buff=0.05).move_to(np.array([0.8, y_pos + 0.3, 0]))

            # C/d 比值
            ratio_label = VGroup(
                Text("C/d=", font="Noto Sans CJK SC", font_size=20, color=WHITE),
                MathTex(f"{ratio:.4f}...", font_size=20, color=self.COLOR_PI)
            ).arrange(RIGHT, buff=0.05).move_to(np.array([3.0, y_pos + 0.3, 0]))

            group = VGroup(circ, diam, d_text, c_text_parts, ratio_label)
            all_elements.add(group)

            # 逐个动画
            self.play(Create(circ), run_time=0.5)
            self.play(Create(diam), FadeIn(d_text), run_time=0.4)
            self.play(FadeIn(c_text_parts), run_time=0.4)
            self.play(FadeIn(ratio_label), run_time=0.4)
            self.wait(0.3)

        # 高亮所有比值
        highlight_box = SurroundingRectangle(
            VGroup(*[group[-1] for group in all_elements]),
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )

        discovery = Text(
            "比值都约等于 3.14 !",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.0)

        self.play(Create(highlight_box), run_time=0.5)
        self.play(FadeIn(discovery, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(all_elements),
            FadeOut(highlight_box), FadeOut(discovery),
            run_time=0.6
        )

    # =========================================================
    # Scene 4: Introduce Pi
    # =========================================================
    def scene_4_pi_intro(self):
        """介绍圆周率 pi"""
        title = Text(
            "圆周率",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_PI
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # 大大的 pi 符号
        pi_symbol = MathTex(r"\pi", font_size=160, color=self.COLOR_PI)
        pi_symbol.move_to(UP * 2.5)
        self.play(Write(pi_symbol), run_time=1.0)

        # 定义
        def_line1 = VGroup(
            Text("圆周率 = ", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("周长", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_CIRCUMFERENCE),
            MathTex(r"\div", font_size=26, color=WHITE),
            Text("直径", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_DIAMETER),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.5)

        formula_def = MathTex(
            r"\pi = \frac{C}{d}",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(def_line1), run_time=0.6)
        self.play(Write(formula_def), run_time=0.8)
        self.wait(0.5)

        # pi 的值
        pi_value = MathTex(
            r"\pi = 3.14159265...",
            font_size=32,
            color=self.COLOR_PI
        ).move_to(DOWN * 1.8)

        self.play(Write(pi_value), run_time=0.8)

        # 特点说明
        features = VGroup(
            Text("无限不循环小数", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
            Text("永远除不尽!", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.2)

        self.play(FadeIn(features), run_time=0.5)
        self.wait(0.5)

        approx = VGroup(
            Text("计算时取近似值: ", font="Noto Sans CJK SC", font_size=24, color=WHITE),
            MathTex(r"\pi \approx 3.14", font_size=30, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.8)

        self.play(FadeIn(approx), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(pi_symbol),
            FadeOut(def_line1), FadeOut(formula_def),
            FadeOut(pi_value), FadeOut(features),
            FadeOut(approx),
            run_time=0.6
        )

    # =========================================================
    # Scene 5: Formula Derivation
    # =========================================================
    def scene_5_formula(self):
        """推导圆周长公式 C = pi*d = 2*pi*r"""
        title = Text(
            "圆周长公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # 画圆 + 标注直径和半径
        circ = Circle(radius=1.5, color=self.COLOR_CIRCLE, stroke_width=3)
        circ.move_to(UP * 2.5)
        center_dot = Dot(circ.get_center(), color=WHITE, radius=0.05)

        self.play(Create(circ), FadeIn(center_dot), run_time=0.8)

        # 直径
        diam_line = Line(
            circ.get_left(), circ.get_right(),
            color=self.COLOR_DIAMETER, stroke_width=3
        )
        d_label = MathTex("d", font_size=28, color=self.COLOR_DIAMETER)
        d_label.next_to(diam_line, DOWN, buff=0.1)

        self.play(Create(diam_line), FadeIn(d_label), run_time=0.5)

        # 半径
        radius_line = Line(
            circ.get_center(),
            circ.get_center() + UP * 1.5,
            color="#e67e22", stroke_width=3
        )
        r_label = MathTex("r", font_size=28, color="#e67e22")
        r_label.next_to(radius_line, RIGHT, buff=0.1)

        self.play(Create(radius_line), FadeIn(r_label), run_time=0.5)

        # d = 2r 关系
        relation = MathTex(r"d = 2r", font_size=28, color=GRAY_A)
        relation.move_to(UP * 0.3)
        self.play(FadeIn(relation), run_time=0.4)
        self.wait(0.3)

        # 公式推导 Step 1: 从定义出发
        step1_label = Text(
            "由定义:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(np.array([-3.0, -1.0, 0]))

        step1 = MathTex(
            r"\pi = \frac{C}{d}",
            font_size=36,
            color=WHITE
        ).next_to(step1_label, RIGHT, buff=0.3)

        self.play(FadeIn(step1_label), Write(step1), run_time=0.8)
        self.wait(0.5)

        # Step 2: 两边乘以 d
        step2_label = Text(
            "两边乘 d:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(np.array([-3.0, -2.2, 0]))

        step2 = MathTex(
            r"C = \pi d",
            font_size=42,
            color=self.COLOR_FORMULA
        ).next_to(step2_label, RIGHT, buff=0.3)

        box1 = SurroundingRectangle(step2, color=self.COLOR_FORMULA, buff=0.15, corner_radius=0.1)

        self.play(FadeIn(step2_label), Write(step2), run_time=0.8)
        self.play(Create(box1), run_time=0.4)

        formula1_tag = Text(
            "公式一",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_FORMULA
        ).next_to(box1, RIGHT, buff=0.15)
        self.play(FadeIn(formula1_tag), run_time=0.3)
        self.wait(0.5)

        # Step 3: 代入 d=2r
        step3_label = VGroup(
            Text("代入", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
            MathTex(r"d=2r", font_size=22, color=GRAY_A),
            Text(":", font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        ).arrange(RIGHT, buff=0.05).move_to(np.array([-2.8, -3.5, 0]))

        step3 = MathTex(
            r"C = 2\pi r",
            font_size=42,
            color=self.COLOR_FORMULA
        ).next_to(step3_label, RIGHT, buff=0.3)

        box2 = SurroundingRectangle(step3, color=self.COLOR_FORMULA, buff=0.15, corner_radius=0.1)

        self.play(FadeIn(step3_label), Write(step3), run_time=0.8)
        self.play(Create(box2), run_time=0.4)

        formula2_tag = Text(
            "公式二",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_FORMULA
        ).next_to(box2, RIGHT, buff=0.15)
        self.play(FadeIn(formula2_tag), run_time=0.3)
        self.wait(0.5)

        # 总结两个公式
        summary_box = RoundedRectangle(
            width=7.0, height=2.0,
            corner_radius=0.2,
            color=self.COLOR_HIGHLIGHT,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
            stroke_width=2
        ).move_to(DOWN * 5.5)

        summary_f1 = MathTex(
            r"C = \pi d",
            font_size=36,
            color=self.COLOR_FORMULA
        )
        summary_f2 = MathTex(
            r"C = 2\pi r",
            font_size=36,
            color=self.COLOR_FORMULA
        )
        summary_group = VGroup(summary_f1, summary_f2).arrange(RIGHT, buff=1.5)
        summary_group.move_to(summary_box.get_center())

        known_label = Text(
            "已知直径用左边, 已知半径用右边",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(summary_box, DOWN, buff=0.2)

        self.play(
            FadeIn(summary_box),
            FadeIn(summary_group),
            FadeIn(known_label),
            run_time=0.8
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(circ), FadeOut(center_dot),
            FadeOut(diam_line), FadeOut(d_label),
            FadeOut(radius_line), FadeOut(r_label),
            FadeOut(relation),
            FadeOut(step1_label), FadeOut(step1),
            FadeOut(step2_label), FadeOut(step2), FadeOut(box1), FadeOut(formula1_tag),
            FadeOut(step3_label), FadeOut(step3), FadeOut(box2), FadeOut(formula2_tag),
            FadeOut(summary_box), FadeOut(summary_group), FadeOut(known_label),
            run_time=0.6
        )

    # =========================================================
    # Scene 6: Example Problem
    # =========================================================
    def scene_6_example(self):
        """例题: 已知直径求周长, 已知半径求周长"""
        title = Text(
            "动手算一算",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # === Example 1: 直径=10cm ===
        ex1_label = Text(
            "例1: 圆的直径 d = 10 cm, 求周长",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 4.2)

        self.play(FadeIn(ex1_label), run_time=0.5)

        # 小圆图
        ex1_circle = Circle(radius=0.8, color=self.COLOR_CIRCLE, stroke_width=2)
        ex1_circle.move_to(np.array([-2.5, 2.5, 0]))
        ex1_diam = Line(
            ex1_circle.get_left(), ex1_circle.get_right(),
            color=self.COLOR_DIAMETER, stroke_width=2
        )
        ex1_d_label = MathTex("10", font_size=20, color=self.COLOR_DIAMETER)
        ex1_d_label.next_to(ex1_diam, DOWN, buff=0.05)

        self.play(Create(ex1_circle), Create(ex1_diam), FadeIn(ex1_d_label), run_time=0.6)

        # 计算步骤
        sol1_s1 = MathTex(
            r"C = \pi d",
            font_size=30, color=WHITE
        ).move_to(np.array([1.5, 3.0, 0]))

        sol1_s2 = MathTex(
            r"= 3.14 \times 10",
            font_size=30, color=WHITE
        ).next_to(sol1_s1, DOWN, buff=0.2, aligned_edge=LEFT)

        sol1_s3 = MathTex(
            r"= 31.4 \text{ cm}",
            font_size=30, color=self.COLOR_CIRCUMFERENCE
        ).next_to(sol1_s2, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(sol1_s1), run_time=0.5)
        self.play(Write(sol1_s2), run_time=0.5)
        self.play(Write(sol1_s3), run_time=0.5)

        ans_box1 = SurroundingRectangle(sol1_s3, color=self.COLOR_HIGHLIGHT, buff=0.1)
        self.play(Create(ans_box1), run_time=0.3)
        self.wait(1.0)

        # === Example 2: 半径=4cm ===
        ex2_label = Text(
            "例2: 圆的半径 r = 4 cm, 求周长",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(ex2_label), run_time=0.5)

        # 小圆图
        ex2_circle = Circle(radius=0.6, color=self.COLOR_CIRCLE, stroke_width=2)
        ex2_circle.move_to(np.array([-2.5, -1.5, 0]))
        ex2_radius = Line(
            ex2_circle.get_center(),
            ex2_circle.get_center() + RIGHT * 0.6,
            color="#e67e22", stroke_width=2
        )
        ex2_r_label = MathTex("4", font_size=20, color="#e67e22")
        ex2_r_label.next_to(ex2_radius, UP, buff=0.05)
        ex2_center = Dot(ex2_circle.get_center(), color=WHITE, radius=0.03)

        self.play(
            Create(ex2_circle), Create(ex2_radius),
            FadeIn(ex2_r_label), FadeIn(ex2_center),
            run_time=0.6
        )

        # 计算步骤
        sol2_s1 = MathTex(
            r"C = 2\pi r",
            font_size=30, color=WHITE
        ).move_to(np.array([1.5, -1.0, 0]))

        sol2_s2 = MathTex(
            r"= 2 \times 3.14 \times 4",
            font_size=30, color=WHITE
        ).next_to(sol2_s1, DOWN, buff=0.2, aligned_edge=LEFT)

        sol2_s3 = MathTex(
            r"= 25.12 \text{ cm}",
            font_size=30, color=self.COLOR_CIRCUMFERENCE
        ).next_to(sol2_s2, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(sol2_s1), run_time=0.5)
        self.play(Write(sol2_s2), run_time=0.5)
        self.play(Write(sol2_s3), run_time=0.5)

        ans_box2 = SurroundingRectangle(sol2_s3, color=self.COLOR_HIGHLIGHT, buff=0.1)
        self.play(Create(ans_box2), run_time=0.3)
        self.wait(1.0)

        # 提示
        tip = Text(
            "知直径用 C=pi*d, 知半径用 C=2*pi*r",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ex1_label), FadeOut(ex1_circle), FadeOut(ex1_diam), FadeOut(ex1_d_label),
            FadeOut(sol1_s1), FadeOut(sol1_s2), FadeOut(sol1_s3), FadeOut(ans_box1),
            FadeOut(ex2_label), FadeOut(ex2_circle), FadeOut(ex2_radius),
            FadeOut(ex2_r_label), FadeOut(ex2_center),
            FadeOut(sol2_s1), FadeOut(sol2_s2), FadeOut(sol2_s3), FadeOut(ans_box2),
            FadeOut(tip),
            run_time=0.6
        )

    # =========================================================
    # Scene 7: Summary & Outro
    # =========================================================
    def scene_7_outro(self):
        """总结与片尾"""
        # 总结标题
        summary_title = Text(
            "今天学到的知识",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.0)

        self.play(Write(summary_title), run_time=0.6)

        # 要点
        points = VGroup(
            self._make_point("1. 化曲为直: 让圆滚动展开为直线"),
            self._make_point("2. 圆周率: C/d 是一个固定值"),
        )
        points.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        points.move_to(UP * 3.0)

        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in points], lag_ratio=0.6), run_time=1.5)
        self.wait(0.3)

        # pi 值
        pi_line = VGroup(
            MathTex(r"\pi \approx 3.14", font_size=32, color=self.COLOR_PI),
            Text("  (无限不循环小数)", font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)

        self.play(FadeIn(pi_line), run_time=0.5)

        # 两个公式 (大号显眼)
        formula_box = RoundedRectangle(
            width=7.5, height=2.8,
            corner_radius=0.2,
            color=self.COLOR_FORMULA,
            fill_color="#2a2a4e",
            fill_opacity=0.8,
            stroke_width=2
        ).move_to(DOWN * 0.8)

        f1 = MathTex(r"C = \pi d", font_size=48, color=self.COLOR_FORMULA)
        f2 = MathTex(r"C = 2\pi r", font_size=48, color=self.COLOR_FORMULA)
        formulas = VGroup(f1, f2).arrange(DOWN, buff=0.5)
        formulas.move_to(formula_box.get_center())

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)
        self.wait(1.0)

        # 关注提示
        follow = Text(
            "关注我, 获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.6)

        # 作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 5.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B
        ).next_to(author_big, DOWN, buff=0.2)

        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(summary_title),
            FadeOut(points),
            FadeOut(pi_line),
            FadeOut(formula_box), FadeOut(f1), FadeOut(f2),
            FadeOut(follow),
            FadeOut(author_big), FadeOut(author_id),
            run_time=1.0
        )

    def _make_point(self, text):
        """创建要点文本"""
        return Text(
            text,
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
