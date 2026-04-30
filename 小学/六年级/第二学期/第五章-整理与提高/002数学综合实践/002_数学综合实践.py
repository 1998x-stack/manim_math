"""
002数学综合实践 - 自行车里的数学
使用 Manim 创建的数学教学视频

内容: 齿轮比与路程计算 - 数学综合实践
目标观众: 六年级学生
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


class MathPracticeLesson(Scene):
    """
    数学综合实践 教学动画场景

    场景顺序:
    1. 开场钩子 - 自行车引入
    2. 齿轮比概念
    3. 齿轮比计算示例
    4. 路程公式引入
    5. 路程计算实例
    6. 节约用水应用
    7. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#3498db"
        self.COLOR_SECONDARY = "#e74c3c"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_ACCENT = "#2ecc71"
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_GEAR_FRONT = "#e67e22"
        self.COLOR_GEAR_REAR = "#1abc9c"
        self.COLOR_WHEEL = "#9b59b6"
        self.COLOR_WATER = "#3498db"

        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_gear_ratio_concept()
        self.scene_3_gear_ratio_calculation()
        self.scene_4_distance_formula()
        self.scene_5_distance_calculation()
        self.scene_6_water_saving()
        self.scene_7_summary_and_outro()

    def setup_geometry(self):
        """初始化几何数据"""
        # 齿轮参数
        self.front_gear_center = np.array([-1.5, 2.0, 0])
        self.rear_gear_center = np.array([2.0, 2.0, 0])
        self.front_gear_radius = 1.2
        self.rear_gear_radius = 0.6
        self.front_teeth = 48
        self.rear_teeth = 16

        # 车轮参数
        self.wheel_center = np.array([0, 0, 0])
        self.wheel_radius_real = 0.33  # 直径66cm -> 半径0.33m
        self.wheel_circumference = 2 * np.pi * self.wheel_radius_real

        # 齿轮比
        self.gear_ratio = self.front_teeth / self.rear_teeth  # = 3

        # 作者标识
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)

    # ------------------------------------------------------------------
    # Helper: create a gear-like circle with "teeth" marks
    # ------------------------------------------------------------------
    def create_gear(self, center, radius, n_teeth, color, label_text=None):
        """Create a simplified gear visualization."""
        gear_circle = Circle(
            radius=radius, color=color, stroke_width=3
        ).move_to(center)

        teeth_group = VGroup()
        for i in range(n_teeth):
            angle = i * TAU / n_teeth
            inner = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            outer = center + (radius + 0.12) * np.array(
                [np.cos(angle), np.sin(angle), 0]
            )
            tooth = Line(inner, outer, color=color, stroke_width=2)
            teeth_group.add(tooth)

        center_dot = Dot(center, color=color, radius=0.06)

        gear = VGroup(gear_circle, teeth_group, center_dot)

        if label_text is not None:
            label = Text(
                label_text,
                font="PingFang SC",
                font_size=18,
                color=color,
            ).next_to(gear_circle, DOWN, buff=0.25)
            gear.add(label)

        return gear

    # ------------------------------------------------------------------
    # Scene 1: Opening hook
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        self.play(FadeIn(self.author_label, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "骑自行车时\n蹬一圈能走多远?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.4,
        ).move_to(UP * 4.5)

        self.play(Write(hook), run_time=1.2)
        self.wait(0.6)

        # Simple bike silhouette: two wheels + frame lines
        wheel_l = Circle(radius=0.9, color=WHITE, stroke_width=2).move_to(
            LEFT * 1.8 + DOWN * 0.5
        )
        wheel_r = Circle(radius=0.9, color=WHITE, stroke_width=2).move_to(
            RIGHT * 1.8 + DOWN * 0.5
        )
        frame_1 = Line(
            wheel_l.get_center() + UP * 0.0,
            wheel_r.get_center() + UP * 0.0,
            color=WHITE,
            stroke_width=2,
        )
        frame_2 = Line(
            wheel_l.get_center(),
            wheel_l.get_center() + UR * 1.2,
            color=WHITE,
            stroke_width=2,
        )
        frame_3 = Line(
            wheel_r.get_center(),
            wheel_l.get_center() + UR * 1.2,
            color=WHITE,
            stroke_width=2,
        )
        seat = Line(
            wheel_l.get_center() + UR * 1.2,
            wheel_l.get_center() + UR * 1.2 + UP * 0.4,
            color=WHITE,
            stroke_width=3,
        )
        bike = VGroup(wheel_l, wheel_r, frame_1, frame_2, frame_3, seat).move_to(
            DOWN * 0.5
        )

        self.play(Create(bike), run_time=1.5)
        self.wait(0.8)

        subtitle = Text(
            "答案就藏在齿轮里!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(hook), FadeOut(bike), FadeOut(subtitle), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 2: Gear ratio concept
    # ------------------------------------------------------------------
    def scene_2_gear_ratio_concept(self):
        title = Text(
            "什么是齿轮比?",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # Front gear (large)
        front_center = np.array([-1.8, 2.5, 0])
        front = self.create_gear(
            front_center, 1.3, 24, self.COLOR_GEAR_FRONT
        )

        front_label = Text(
            "前齿轮(大)",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_GEAR_FRONT,
        ).next_to(front, DOWN, buff=0.3)

        # Rear gear (small)
        rear_center = np.array([2.0, 2.5, 0])
        rear = self.create_gear(
            rear_center, 0.65, 12, self.COLOR_GEAR_REAR
        )

        rear_label = Text(
            "后齿轮(小)",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_GEAR_REAR,
        ).next_to(rear, DOWN, buff=0.3)

        # Chain connecting them
        chain_top = Line(
            front_center + UP * 1.3,
            rear_center + UP * 0.65,
            color=GRAY_A,
            stroke_width=2,
        )
        chain_bot = Line(
            front_center + DOWN * 1.3,
            rear_center + DOWN * 0.65,
            color=GRAY_A,
            stroke_width=2,
        )

        self.play(Create(front), FadeIn(front_label), run_time=1.0)
        self.play(Create(rear), FadeIn(rear_label), run_time=1.0)
        self.play(Create(chain_top), Create(chain_bot), run_time=0.6)
        self.wait(0.5)

        # Explanation
        explain_1 = Text(
            "前齿轮转1圈",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GEAR_FRONT,
        ).move_to(DOWN * 1.0)

        explain_2 = Text(
            "后齿轮转几圈?",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GEAR_REAR,
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(explain_1), run_time=0.5)
        self.play(FadeIn(explain_2), run_time=0.5)

        # Rotate gears to show relationship
        self.play(
            Rotate(front, angle=TAU, about_point=front_center),
            Rotate(rear, angle=-TAU * 2, about_point=rear_center),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(0.5)

        # Formula
        formula_label = Text(
            "齿轮比公式",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 3.0)

        formula = MathTex(
            r"\text{Gear Ratio} = \frac{\text{Front Teeth}}{\text{Rear Teeth}}",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 3.8)

        # Chinese version beneath
        cn_line = VGroup(
            Text("齿轮比", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"=", font_size=28, color=WHITE),
            Text("前齿轮齿数", font="PingFang SC", font_size=22, color=self.COLOR_GEAR_FRONT),
            MathTex(r"\div", font_size=28, color=WHITE),
            Text("后齿轮齿数", font="PingFang SC", font_size=22, color=self.COLOR_GEAR_REAR),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.8)

        self.play(FadeIn(formula_label), run_time=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(FadeIn(cn_line), run_time=0.8)
        self.wait(1.5)

        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(front),
            FadeOut(rear),
            FadeOut(front_label),
            FadeOut(rear_label),
            FadeOut(chain_top),
            FadeOut(chain_bot),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(formula_label),
            FadeOut(formula),
            FadeOut(cn_line),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 3: Gear ratio calculation example
    # ------------------------------------------------------------------
    def scene_3_gear_ratio_calculation(self):
        title = Text(
            "齿轮比计算",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.7)

        # Problem statement
        problem = VGroup(
            Text("已知:", font="PingFang SC", font_size=26, color=GRAY_A),
            VGroup(
                Text("前齿轮", font="PingFang SC", font_size=24, color=self.COLOR_GEAR_FRONT),
                MathTex(r"= 48", font_size=28, color=WHITE),
                Text("齿", font="PingFang SC", font_size=24, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("后齿轮", font="PingFang SC", font_size=24, color=self.COLOR_GEAR_REAR),
                MathTex(r"= 16", font_size=28, color=WHITE),
                Text("齿", font="PingFang SC", font_size=24, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 3.5)

        self.play(Write(problem[0]), run_time=0.4)
        self.play(FadeIn(problem[1]), run_time=0.5)
        self.play(FadeIn(problem[2]), run_time=0.5)
        self.wait(0.5)

        # Step-by-step calculation
        step_label = Text(
            "求齿轮比:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.5)

        step1 = VGroup(
            Text("齿轮比", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"= \frac{48}{16}", font_size=36, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.5)

        step2 = VGroup(
            MathTex(r"= 3", font_size=36, color=self.COLOR_HIGHLIGHT),
        ).move_to(DOWN * 0.5)

        self.play(Write(step_label), run_time=0.5)
        self.play(Write(step1), run_time=1.0)
        self.wait(0.5)
        self.play(Write(step2), run_time=0.8)

        # Box highlight
        result_box = SurroundingRectangle(step2, color=self.COLOR_HIGHLIGHT, buff=0.2)
        self.play(Create(result_box), run_time=0.5)

        # Meaning
        meaning = VGroup(
            Text("含义: 前齿轮转1圈", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("后齿轮转3圈!", font="PingFang SC", font_size=24, color=self.COLOR_ACCENT),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)

        self.play(FadeIn(meaning), run_time=0.8)

        # Visual: show gears with teeth count
        mini_front = self.create_gear(
            np.array([-1.5, -4.5, 0]), 0.8, 16, self.COLOR_GEAR_FRONT
        )
        mini_rear = self.create_gear(
            np.array([1.5, -4.5, 0]), 0.4, 8, self.COLOR_GEAR_REAR
        )

        t48 = MathTex(r"48", font_size=22, color=self.COLOR_GEAR_FRONT).move_to(
            np.array([-1.5, -4.5, 0])
        )
        t16 = MathTex(r"16", font_size=22, color=self.COLOR_GEAR_REAR).move_to(
            np.array([1.5, -4.5, 0])
        )

        self.play(
            Create(mini_front),
            Create(mini_rear),
            FadeIn(t48),
            FadeIn(t16),
            run_time=0.8,
        )

        # Animate: front 1 turn, rear 3 turns
        self.play(
            Rotate(
                mini_front,
                angle=TAU,
                about_point=np.array([-1.5, -4.5, 0]),
            ),
            Rotate(
                mini_rear,
                angle=-TAU * 3,
                about_point=np.array([1.5, -4.5, 0]),
            ),
            run_time=2.0,
        )
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(step_label),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(result_box),
            FadeOut(meaning),
            FadeOut(mini_front),
            FadeOut(mini_rear),
            FadeOut(t48),
            FadeOut(t16),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: Distance formula
    # ------------------------------------------------------------------
    def scene_4_distance_formula(self):
        title = Text(
            "蹬一圈走多远?",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.7)

        # Key insight
        insight_1 = Text(
            "后齿轮 带动 车轮 一起转!",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 4.2)

        self.play(FadeIn(insight_1), run_time=0.6)

        # Wheel rolling visualization
        wheel_c = np.array([0, 2.0, 0])
        wheel = Circle(
            radius=1.0, color=self.COLOR_WHEEL, stroke_width=3
        ).move_to(wheel_c)
        wheel_dot = Dot(wheel_c + RIGHT * 1.0, color=WHITE, radius=0.08)
        spoke1 = Line(wheel_c, wheel_c + RIGHT * 1.0, color=GRAY_A, stroke_width=1.5)
        spoke2 = Line(wheel_c, wheel_c + UP * 1.0, color=GRAY_A, stroke_width=1.5)
        spoke3 = Line(wheel_c, wheel_c + LEFT * 1.0, color=GRAY_A, stroke_width=1.5)
        spoke4 = Line(wheel_c, wheel_c + DOWN * 1.0, color=GRAY_A, stroke_width=1.5)
        wheel_group = VGroup(wheel, spoke1, spoke2, spoke3, spoke4, wheel_dot)

        self.play(Create(wheel_group), run_time=1.0)

        # Rotate wheel one turn
        self.play(
            Rotate(wheel_group, angle=TAU, about_point=wheel_c),
            run_time=2.0,
        )
        self.wait(0.3)

        # Formula derivation
        formula_title = Text(
            "路程公式",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)

        line1 = VGroup(
            Text("路程", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            Text("车轮周长", font="PingFang SC", font_size=24, color=self.COLOR_WHEEL),
            MathTex(r"\times", font_size=30, color=WHITE),
            Text("车轮圈数", font="PingFang SC", font_size=24, color=self.COLOR_GEAR_REAR),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 1.5)

        line2 = VGroup(
            Text("车轮圈数", font="PingFang SC", font_size=22, color=GRAY_A),
            MathTex(r"=", font_size=28, color=GRAY_A),
            Text("齿轮比", font="PingFang SC", font_size=22, color=GRAY_A),
            MathTex(r"\times", font_size=28, color=GRAY_A),
            Text("蹬的圈数", font="PingFang SC", font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 2.8)

        self.play(FadeIn(formula_title), run_time=0.4)
        self.play(Write(line1), run_time=1.2)
        self.wait(0.5)
        self.play(FadeIn(line2), run_time=0.8)
        self.wait(0.5)

        # Combined formula
        combined_label = Text(
            "合并得到:",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.0)

        combined = VGroup(
            Text("路程", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            Text("周长", font="PingFang SC", font_size=24, color=self.COLOR_WHEEL),
            MathTex(r"\times", font_size=30, color=WHITE),
            Text("齿轮比", font="PingFang SC", font_size=24, color=self.COLOR_GEAR_FRONT),
            MathTex(r"\times", font_size=30, color=WHITE),
            Text("蹬的圈数", font="PingFang SC", font_size=24, color=self.COLOR_GEAR_REAR),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.0)

        box = SurroundingRectangle(combined, color=self.COLOR_HIGHLIGHT, buff=0.2)

        self.play(FadeIn(combined_label), run_time=0.4)
        self.play(Write(combined), run_time=1.0)
        self.play(Create(box), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(insight_1),
            FadeOut(wheel_group),
            FadeOut(formula_title),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(combined_label),
            FadeOut(combined),
            FadeOut(box),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: Distance calculation with real numbers
    # ------------------------------------------------------------------
    def scene_5_distance_calculation(self):
        title = Text(
            "实际计算",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.7)

        # Given information
        given = VGroup(
            Text("已知条件:", font="PingFang SC", font_size=24, color=GRAY_A),
            VGroup(
                Text("齿轮比", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"= 3", font_size=26, color=self.COLOR_GEAR_FRONT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("车轮直径", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"= 66", font_size=26, color=self.COLOR_WHEEL),
                Text("cm", font="PingFang SC", font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("蹬", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"1", font_size=26, color=self.COLOR_HIGHLIGHT),
                Text("圈", font="PingFang SC", font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 3.5)

        self.play(Write(given[0]), run_time=0.4)
        for item in given[1:]:
            self.play(FadeIn(item), run_time=0.4)
        self.wait(0.5)

        # Step 1: circumference
        s1_label = Text(
            "第1步: 求车轮周长",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.2)

        s1_math = MathTex(
            r"C = \pi \times d = \pi \times 66 \approx 207.35 \text{ cm}",
            font_size=26,
            color=WHITE,
        ).move_to(UP * 0.4)

        self.play(Write(s1_label), run_time=0.5)
        self.play(Write(s1_math), run_time=1.0)
        self.wait(0.5)

        # Step 2: wheel rotations
        s2_label = Text(
            "第2步: 车轮转几圈",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.6)

        s2_line = VGroup(
            Text("车轮圈数", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"= 3 \times 1 = 3", font_size=26, color=WHITE),
            Text("圈", font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.4)

        self.play(Write(s2_label), run_time=0.5)
        self.play(Write(s2_line), run_time=0.8)
        self.wait(0.5)

        # Step 3: total distance
        s3_label = Text(
            "第3步: 求路程",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.5)

        s3_line1 = VGroup(
            Text("路程", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"= 207.35 \times 3", font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.3)

        s3_line2 = VGroup(
            MathTex(r"\approx 622.04", font_size=28, color=self.COLOR_ACCENT),
            Text("cm", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"\approx 6.22", font_size=28, color=self.COLOR_ACCENT),
            Text("m", font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.2)

        self.play(Write(s3_label), run_time=0.5)
        self.play(Write(s3_line1), run_time=0.8)
        self.play(Write(s3_line2), run_time=0.8)

        # Final answer highlight
        answer_box = SurroundingRectangle(
            s3_line2, color=self.COLOR_HIGHLIGHT, buff=0.2
        )
        self.play(Create(answer_box), run_time=0.5)

        conclusion = Text(
            "蹬一圈约走6.22米!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(given),
            FadeOut(s1_label),
            FadeOut(s1_math),
            FadeOut(s2_label),
            FadeOut(s2_line),
            FadeOut(s3_label),
            FadeOut(s3_line1),
            FadeOut(s3_line2),
            FadeOut(answer_box),
            FadeOut(conclusion),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: Water saving application
    # ------------------------------------------------------------------
    def scene_6_water_saving(self):
        title = Text(
            "节约用水",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "数学帮助我们节约资源",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # Water tap dripping visualization
        tap_body = RoundedRectangle(
            width=0.8,
            height=1.2,
            corner_radius=0.1,
            color=GRAY_A,
            fill_opacity=0.3,
            fill_color=GRAY_A,
        ).move_to(UP * 3.0)

        tap_spout = RoundedRectangle(
            width=0.4,
            height=0.5,
            corner_radius=0.05,
            color=GRAY_A,
            fill_opacity=0.3,
            fill_color=GRAY_A,
        ).move_to(UP * 2.15)

        self.play(FadeIn(tap_body), FadeIn(tap_spout), run_time=0.6)

        # Dripping animation
        drops = VGroup()
        for i in range(5):
            drop = Circle(
                radius=0.08,
                color=self.COLOR_WATER,
                fill_opacity=0.8,
                fill_color=self.COLOR_WATER,
            ).move_to(UP * 1.85)
            drops.add(drop)

        for drop in drops:
            self.play(
                drop.animate.shift(DOWN * 1.5).set_opacity(0),
                run_time=0.3,
            )
            self.remove(drop)

        # Problem setup
        problem = VGroup(
            Text(
                "调查发现:",
                font="PingFang SC",
                font_size=24,
                color=self.COLOR_HIGHLIGHT,
            ),
            VGroup(
                Text("一个漏水龙头每天浪费", font="PingFang SC", font_size=20, color=WHITE),
                MathTex(r"12", font_size=26, color=self.COLOR_SECONDARY),
                Text("升水", font="PingFang SC", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)

        self.play(FadeIn(problem), run_time=0.8)
        self.wait(0.5)

        # Calculation
        calc_label = Text(
            "全校50个水龙头, 一年浪费多少?",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.0)

        calc_1 = VGroup(
            Text("每天:", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"12 \times 50 = 600", font_size=24, color=WHITE),
            Text("升", font="PingFang SC", font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.8)

        calc_2 = VGroup(
            Text("一年:", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"600 \times 365 = 219000", font_size=24, color=WHITE),
            Text("升", font="PingFang SC", font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.6)

        calc_3 = VGroup(
            MathTex(r"= 219", font_size=28, color=self.COLOR_SECONDARY),
            Text("吨!", font="PingFang SC", font_size=24, color=self.COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 4.4)

        self.play(Write(calc_label), run_time=0.7)
        self.play(Write(calc_1), run_time=0.8)
        self.play(Write(calc_2), run_time=0.8)
        self.play(Write(calc_3), run_time=0.6)

        result_box = SurroundingRectangle(calc_3, color=self.COLOR_SECONDARY, buff=0.2)
        self.play(Create(result_box), run_time=0.4)

        # Formula reminder
        formula_reminder = VGroup(
            Text("节水量", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"=", font_size=24, color=GRAY_A),
            Text("原用水量", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"-", font_size=24, color=GRAY_A),
            Text("现用水量", font="PingFang SC", font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 5.6)

        self.play(FadeIn(formula_reminder), run_time=0.6)

        message = Text(
            "修好水龙头, 就能节约219吨!",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(message, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(tap_body),
            FadeOut(tap_spout),
            FadeOut(problem),
            FadeOut(calc_label),
            FadeOut(calc_1),
            FadeOut(calc_2),
            FadeOut(calc_3),
            FadeOut(result_box),
            FadeOut(formula_reminder),
            FadeOut(message),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: Summary and outro
    # ------------------------------------------------------------------
    def scene_7_summary_and_outro(self):
        title = Text(
            "今天学到了什么?",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.7)

        # Process flow
        process_title = Text(
            "解决问题的步骤",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 4.3)

        steps_data = [
            ("发现问题", "#e74c3c"),
            ("建立模型", "#e67e22"),
            ("求解验证", "#2ecc71"),
            ("解释应用", "#3498db"),
        ]

        step_boxes = VGroup()
        arrows_group = VGroup()
        for i, (text, color) in enumerate(steps_data):
            box = RoundedRectangle(
                width=3.0,
                height=0.7,
                corner_radius=0.15,
                color=color,
                fill_opacity=0.2,
                fill_color=color,
                stroke_width=2,
            ).move_to(UP * (3.0 - i * 1.1))

            label = Text(
                text,
                font="PingFang SC",
                font_size=22,
                color=color,
            ).move_to(box.get_center())

            step_group = VGroup(box, label)
            step_boxes.add(step_group)

            if i > 0:
                arrow = Arrow(
                    step_boxes[i - 1].get_bottom(),
                    box.get_top(),
                    buff=0.08,
                    color=GRAY_A,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3,
                )
                arrows_group.add(arrow)

        self.play(Write(process_title), run_time=0.5)

        for i, step in enumerate(step_boxes):
            self.play(FadeIn(step, shift=RIGHT * 0.5), run_time=0.4)
            if i > 0 and i - 1 < len(arrows_group):
                self.play(GrowArrow(arrows_group[i - 1]), run_time=0.3)

        self.wait(0.8)

        # Key formulas recap
        recap_title = Text(
            "核心公式",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.0)

        formulas = VGroup(
            VGroup(
                Text("齿轮比", font="PingFang SC", font_size=20, color=self.COLOR_GEAR_FRONT),
                MathTex(r"= \frac{\text{Front}}{\text{Rear}}", font_size=24, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("路程", font="PingFang SC", font_size=20, color=self.COLOR_WHEEL),
                MathTex(r"= C \times n", font_size=24, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("节水量", font="PingFang SC", font_size=20, color=self.COLOR_WATER),
                MathTex(r"=", font_size=24, color=WHITE),
                Text("原量", font="PingFang SC", font_size=20, color=WHITE),
                MathTex(r"-", font_size=24, color=WHITE),
                Text("现量", font="PingFang SC", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(DOWN * 2.8)

        self.play(Write(recap_title), run_time=0.4)
        for f in formulas:
            self.play(FadeIn(f), run_time=0.5)
        self.wait(1.0)

        # Highlight message
        big_msg = Text(
            "数学就在身边!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(big_msg, scale=1.2), run_time=0.6)
        self.wait(1.0)

        # Fade everything out for outro
        self.play(
            FadeOut(title),
            FadeOut(process_title),
            FadeOut(step_boxes),
            FadeOut(arrows_group),
            FadeOut(recap_title),
            FadeOut(formulas),
            FadeOut(big_msg),
            run_time=0.6,
        )

        # Outro
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B,
        ).move_to(UP * 0.5)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.0)

        self.play(
            Transform(
                self.author_label,
                author_big,
            ),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(self.author_label),
            FadeOut(author_id),
            FadeOut(follow),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_数学综合实践.py MathPracticeLesson  # 快速预览
# manim -qm 002_数学综合实践.py MathPracticeLesson   # 中等质量
# manim -qh 002_数学综合实践.py MathPracticeLesson    # 高质量
