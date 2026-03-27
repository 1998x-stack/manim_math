"""
认识图形（一）- 球
小学一年级上册 第三章
使用 Manim 创建的小学数学教学视频

内容: 球的特征 - 从各个方向看都是圆，可以任意滚动
目标观众: 小学一年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SphereLesson(Scene):
    """
    球的认识教学动画

    场景顺序:
    1. 开场 - 引出球
    2. 认识球 - 展示球是圆的
    3. 各个方向看都是圆
    4. 球可以任意滚动
    5. 生活中的球
    6. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_BALL = "#e74c3c"
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_SECONDARY = "#3498db"
        self.COLOR_GREEN = "#2ecc71"
        self.COLOR_PURPLE = "#9b59b6"
        self.COLOR_TEXT = WHITE
        self.COLOR_SUBTEXT = "#b0b8c8"

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_introduce_sphere()
        self.scene_3_all_directions()
        self.scene_4_rolling()
        self.scene_5_real_life()
        self.scene_6_outro()

    def make_sphere(self, center, radius, base_color, highlight_color="#ffffff", fill_opacity=1.0):
        """
        用2D圆 + 高光点模拟球体外观
        返回 VGroup(主圆, 阴影圆, 高光圆)
        """
        center_arr = np.array(center)

        # 主圆（球体）
        main_circle = Circle(
            radius=radius,
            color=base_color,
            fill_color=base_color,
            fill_opacity=fill_opacity,
            stroke_width=3,
            stroke_color=base_color,
        ).move_to(center_arr)

        # 暗部（右下方，模拟阴影）
        shadow_offset = np.array([radius * 0.25, -radius * 0.25, 0])
        shadow = Circle(
            radius=radius * 0.6,
            color="#000000",
            fill_color="#000000",
            fill_opacity=0.15,
            stroke_width=0,
        ).move_to(center_arr + shadow_offset)

        # 高光圆（左上方小亮点，模拟3D光照效果）
        highlight_offset = np.array([-radius * 0.3, radius * 0.3, 0])
        highlight = Circle(
            radius=radius * 0.25,
            color=highlight_color,
            fill_color=highlight_color,
            fill_opacity=0.5,
            stroke_width=0,
        ).move_to(center_arr + highlight_offset)

        return VGroup(main_circle, shadow, highlight)

    def scene_1_opening(self):
        """场景1: 开场引入"""
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "你认识这个形状吗？",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        # 画一个大球在中间
        ball = self.make_sphere(center=[0, 1.5, 0], radius=2.0, base_color=self.COLOR_BALL)
        self.play(GrowFromCenter(ball[0]), run_time=0.8)
        self.play(FadeIn(ball[1]), FadeIn(ball[2]), run_time=0.4)
        self.wait(0.3)

        # 问号闪烁效果
        question = Text(
            "？",
            font="Heiti SC",
            font_size=80,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.5)
        self.play(FadeIn(question, scale=0.5), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(question), run_time=0.3)

        # 答案文字
        answer = Text(
            "这是球！",
            font="Heiti SC",
            font_size=52,
            color=WHITE,
        ).move_to(DOWN * 1.5)
        self.play(Write(answer), run_time=0.7)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(ball),
            FadeOut(answer),
            run_time=0.5,
        )

        self.author = author

    def scene_2_introduce_sphere(self):
        """场景2: 认识球 - 展示球的基本外形"""
        # 标题
        title = Text(
            "认识球",
            font="Heiti SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 大球居中展示
        big_ball = self.make_sphere(
            center=[0, 2.0, 0], radius=2.2, base_color=self.COLOR_BALL
        )
        self.play(GrowFromCenter(big_ball[0]), run_time=1.0)
        self.play(FadeIn(big_ball[1]), FadeIn(big_ball[2]), run_time=0.4)

        # 标注"球"
        label_ball = Text(
            "球",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_BALL,
        ).move_to(DOWN * 0.5)
        self.play(Write(label_ball), run_time=0.5)
        self.wait(0.4)

        # 描述特征: 圆圆的
        feature1 = Text(
            "球是圆圆的",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_SECONDARY,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(feature1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 球轻微跳动动画
        self.play(big_ball.animate.shift(UP * 0.2), run_time=0.3)
        self.play(big_ball.animate.shift(DOWN * 0.2), run_time=0.3)
        self.wait(0.3)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(big_ball),
            FadeOut(label_ball),
            FadeOut(feature1),
            run_time=0.5,
        )

    def scene_3_all_directions(self):
        """场景3: 从各个方向看都是圆"""
        # 标题
        title = Text(
            "从各个方向看",
            font="Heiti SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        title2 = Text(
            "都是圆！",
            font="Heiti SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)
        self.play(Write(title2), run_time=0.4)

        # 主球在中央
        ball_center = np.array([0, 1.8, 0])
        main_ball = self.make_sphere(
            center=ball_center, radius=1.8, base_color=self.COLOR_BALL
        )
        self.play(GrowFromCenter(main_ball[0]), run_time=0.8)
        self.play(FadeIn(main_ball[1]), FadeIn(main_ball[2]), run_time=0.3)

        self.wait(0.3)

        # 4个方向的箭头和标签
        arrow_specs = [
            # (start, end, label_text, label_pos)
            (ball_center + UP * 3.2, ball_center + UP * 2.0, "从上看", ball_center + UP * 3.7),
            (ball_center + DOWN * 2.8, ball_center + DOWN * 1.9, "从下看", ball_center + DOWN * 3.3),
            (ball_center + LEFT * 3.2, ball_center + LEFT * 2.0, "从左看", ball_center + LEFT * 3.9),
            (ball_center + RIGHT * 3.2, ball_center + RIGHT * 2.0, "从右看", ball_center + RIGHT * 3.9),
        ]

        arrows = []
        dir_labels = []
        for start, end, label_str, label_pos in arrow_specs:
            arr = Arrow(
                start=start,
                end=end,
                color=self.COLOR_HIGHLIGHT,
                buff=0.05,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.3,
            )
            lbl = Text(
                label_str,
                font="Heiti SC",
                font_size=22,
                color=self.COLOR_SUBTEXT,
            ).move_to(label_pos)
            arrows.append(arr)
            dir_labels.append(lbl)

        # 依次显示箭头和标签
        for arr, lbl in zip(arrows, dir_labels):
            self.play(GrowArrow(arr), FadeIn(lbl), run_time=0.4)

        self.wait(0.5)

        # 结论框
        conclusion_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=1.1,
            fill_color="#1e3a5f",
            fill_opacity=0.9,
            stroke_color=self.COLOR_SECONDARY,
            stroke_width=2,
        ).move_to(DOWN * 3.0)

        conclusion = Text(
            "从任何方向看，都是圆形！",
            font="Heiti SC",
            font_size=28,
            color=WHITE,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(conclusion_bg), Write(conclusion), run_time=0.7)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(title2),
            FadeOut(main_ball),
            *[FadeOut(a) for a in arrows],
            *[FadeOut(l) for l in dir_labels],
            FadeOut(conclusion_bg),
            FadeOut(conclusion),
            run_time=0.5,
        )

    def scene_4_rolling(self):
        """场景4: 球可以任意滚动"""
        # 标题
        title = Text(
            "球可以任意滚动",
            font="Heiti SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 地面线
        ground = Line(
            start=np.array([-4.0, 0.5, 0]),
            end=np.array([4.0, 0.5, 0]),
            color="#4a5568",
            stroke_width=4,
        )
        self.play(Create(ground), run_time=0.4)

        # 球在地面上滚动
        ball_radius = 1.2
        ball_y = 0.5 + ball_radius
        start_x = -2.8
        end_x = 2.8
        ball_center_start = np.array([start_x, ball_y, 0])

        rolling_ball = self.make_sphere(
            center=ball_center_start, radius=ball_radius, base_color=self.COLOR_GREEN
        )
        self.play(GrowFromCenter(rolling_ball[0]), run_time=0.5)
        self.play(FadeIn(rolling_ball[1]), FadeIn(rolling_ball[2]), run_time=0.3)

        # 旋转指示线（在球内，显示旋转）
        spin_line = Line(
            start=ball_center_start + UP * ball_radius * 0.8,
            end=ball_center_start + DOWN * ball_radius * 0.8,
            color=WHITE,
            stroke_width=3,
        )
        self.play(FadeIn(spin_line), run_time=0.2)

        distance = end_x - start_x  # 5.6

        # 向右滚动
        self.play(
            rolling_ball.animate.shift(RIGHT * distance),
            spin_line.animate.shift(RIGHT * distance),
            run_time=1.8,
            rate_func=linear,
        )
        self.wait(0.2)

        # 向左滚动
        self.play(
            rolling_ball.animate.shift(LEFT * distance),
            spin_line.animate.shift(LEFT * distance),
            run_time=1.8,
            rate_func=linear,
        )
        self.wait(0.3)
        self.play(FadeOut(spin_line), run_time=0.2)

        # 说明可以各个方向滚
        diag_label = Text(
            "还能朝各个方向滚！",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_SECONDARY,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(diag_label, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)

        # 多方向箭头从球中心向外辐射
        arrow_directions = [
            RIGHT * 1.8,
            UP * 1.8,
            UP * 1.2 + RIGHT * 1.2,
            DOWN * 1.2 + RIGHT * 1.2,
            LEFT * 1.8,
            DOWN * 1.8,
        ]
        ball_current_center = ball_center_start  # 球已回到左侧，估算当前位置
        # 球已经回到 start_x，实际中 animate 后位置不变
        dir_arrows = VGroup(
            *[
                Arrow(
                    start=ball_center_start + d * 0.1,
                    end=ball_center_start + d,
                    color=self.COLOR_HIGHLIGHT,
                    buff=0.0,
                    stroke_width=4,
                    max_tip_length_to_length_ratio=0.3,
                )
                for d in arrow_directions
            ]
        )

        self.play(
            *[GrowArrow(a) for a in dir_arrows],
            run_time=0.7,
        )
        self.wait(0.8)

        # 结论框
        conclusion_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=1.1,
            fill_color="#1e3a5f",
            fill_opacity=0.9,
            stroke_color=self.COLOR_GREEN,
            stroke_width=2,
        ).move_to(DOWN * 3.2)
        conclusion_text = Text(
            "球可以向任意方向滚动！",
            font="Heiti SC",
            font_size=28,
            color=WHITE,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(conclusion_box), Write(conclusion_text), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ground),
            FadeOut(rolling_ball),
            FadeOut(diag_label),
            FadeOut(dir_arrows),
            FadeOut(conclusion_box),
            FadeOut(conclusion_text),
            run_time=0.5,
        )

    def scene_5_real_life(self):
        """场景5: 生活中的球"""
        # 标题
        title = Text(
            "生活中的球",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "你能找到哪些球呢？",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_SUBTEXT,
        ).move_to(UP * 5.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)

        # 展示4种球（用颜色区分不同球类）
        ball_configs = [
            {"center": [-2.5, 3.2, 0], "radius": 0.9, "color": "#27ae60", "label": "足球"},
            {"center": [2.0, 3.2, 0], "radius": 0.9, "color": "#e67e22", "label": "篮球"},
            {"center": [-2.5, 0.8, 0], "radius": 0.75, "color": "#f1c40f", "label": "网球"},
            {"center": [2.0, 0.8, 0], "radius": 0.75, "color": "#3498db", "label": "地球仪"},
        ]

        all_balls = []
        all_labels = []

        for cfg in ball_configs:
            b = self.make_sphere(
                center=cfg["center"],
                radius=cfg["radius"],
                base_color=cfg["color"],
            )
            lbl = Text(
                cfg["label"],
                font="Heiti SC",
                font_size=24,
                color=WHITE,
            ).next_to(b[0], DOWN, buff=0.2)

            all_balls.append(b)
            all_labels.append(lbl)

        # 依次出现每个球
        for b, lbl in zip(all_balls, all_labels):
            self.play(GrowFromCenter(b[0]), run_time=0.4)
            self.play(FadeIn(b[1]), FadeIn(b[2]), run_time=0.2)
            self.play(Write(lbl), run_time=0.3)

        self.wait(0.5)

        # 强调：它们都是球！
        same_feature = Text(
            "它们都是球，",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_SECONDARY,
        ).move_to(DOWN * 1.5)
        same_feature2 = Text(
            "从各个方向看都是圆！",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_SECONDARY,
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(same_feature, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(same_feature2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 所有球一起轻轻弹跳
        self.play(*[b.animate.shift(UP * 0.25) for b in all_balls], run_time=0.3)
        self.play(*[b.animate.shift(DOWN * 0.25) for b in all_balls], run_time=0.3)
        self.wait(0.5)

        # 清理
        all_to_fade = [title, subtitle, same_feature, same_feature2] + all_balls + all_labels
        self.play(*[FadeOut(m) for m in all_to_fade], run_time=0.6)

    def scene_6_outro(self):
        """场景6: 总结 + 片尾"""
        # 总结标题
        summary_title = Text(
            "记住球的特征",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.0)
        self.play(Write(summary_title), run_time=0.6)

        # 大球居中
        hero_ball = self.make_sphere(
            center=[0, 2.5, 0], radius=2.0, base_color=self.COLOR_BALL
        )
        self.play(GrowFromCenter(hero_ball[0]), run_time=0.8)
        self.play(FadeIn(hero_ball[1]), FadeIn(hero_ball[2]), run_time=0.3)

        # 特征1框
        feature_bg_1 = RoundedRectangle(
            corner_radius=0.25,
            width=7.8,
            height=1.0,
            fill_color="#1e3a5f",
            fill_opacity=0.9,
            stroke_color=self.COLOR_SECONDARY,
            stroke_width=2,
        ).move_to(DOWN * 0.8)
        feature1 = Text(
            "从各个方向看都是圆",
            font="Heiti SC",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 0.8)

        # 特征2框
        feature_bg_2 = RoundedRectangle(
            corner_radius=0.25,
            width=7.8,
            height=1.0,
            fill_color="#1e3a5f",
            fill_opacity=0.9,
            stroke_color=self.COLOR_GREEN,
            stroke_width=2,
        ).move_to(DOWN * 2.2)
        feature2 = Text(
            "可以任意方向滚动",
            font="Heiti SC",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(feature_bg_1), Write(feature1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(feature_bg_2), Write(feature2), run_time=0.6)
        self.wait(0.8)

        # 球的高光绕球旋转一圈（模拟3D旋转）
        self.play(
            Rotate(hero_ball[2], angle=TAU, about_point=np.array([0, 2.5, 0])),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.5)

        # 清理内容
        self.play(
            FadeOut(summary_title),
            FadeOut(hero_ball),
            FadeOut(feature_bg_1),
            FadeOut(feature1),
            FadeOut(feature_bg_2),
            FadeOut(feature2),
            run_time=0.5,
        )

        # 片尾作者信息放大
        outro_name = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 1.5)
        outro_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=30,
            color="#6b7280",
        ).move_to(UP * 0.5)

        self.play(Transform(self.author, outro_name), run_time=0.8)
        self.play(FadeIn(outro_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.2, scale=1.05), run_time=0.6)

        # 装饰：5个小球
        colors = [
            self.COLOR_BALL,
            self.COLOR_GREEN,
            self.COLOR_SECONDARY,
            self.COLOR_PURPLE,
            self.COLOR_HIGHLIGHT,
        ]
        deco_balls = VGroup(
            *[
                self.make_sphere(
                    center=[
                        2.5 * np.cos(i * TAU / 5),
                        -2.5 + 0.5 * np.sin(i * TAU / 5),
                        0,
                    ],
                    radius=0.35,
                    base_color=colors[i],
                )
                for i in range(5)
            ]
        )

        self.play(*[GrowFromCenter(b[0]) for b in deco_balls], run_time=0.6)
        self.play(
            *[FadeIn(b[1]) for b in deco_balls],
            *[FadeIn(b[2]) for b in deco_balls],
            run_time=0.3,
        )

        # 小球绕中心旋转
        self.play(
            Rotate(deco_balls, angle=TAU, about_point=np.array([0, -2.5, 0])),
            run_time=2.0,
            rate_func=smooth,
        )

        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(self.author),
            FadeOut(outro_id),
            FadeOut(follow_text),
            FadeOut(deco_balls),
            run_time=1.0,
        )
