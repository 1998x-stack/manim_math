"""
002_找次品.py — 找次品（用天平找轻的次品）教学动画

知识点: 用天平找次品（轻的），三分法，⌈log₃n⌉ 次称量
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心逻辑:
  9个外观相同的球，其中1个轻→次品
  三分法: 分成 (3,3,3)
  第1次称: 取两组各3个放天平→翘起一边有次品 (或平衡→第三组)
  第2次称: 从3个中取2个→同理找出
  结论: 9个球只需2次! 规律: ⌈log₃n⌉
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_BALL = "#3b82f6"       # 蓝色普通球
COLOR_DEFECT = "#ef4444"     # 红色次品球
COLOR_SCALE = "#a78bfa"      # 紫色天平
COLOR_GROUP = "#22c55e"      # 绿色分组
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ORANGE = "#f59e0b"     # 橙色
COLOR_AUTHOR = "#6b7280"     # 灰色作者
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class DefectiveItemLesson(Scene):
    """
    找次品教学动画
    Scene 1: 开场钩子 — 9个球，怎么找次品？
    Scene 2: 三分法策略 — 分成3组
    Scene 3: 第1次称量 — 天平动画
    Scene 4: 第2次称量 — 从3个中找1个
    Scene 5: 规律总结 — ⌈log₃n⌉
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_split_strategy()
        self.scene_3_first_weigh()
        self.scene_4_second_weigh()
        self.scene_5_formula_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建球
    # ------------------------------------------------------------------

    def _make_ball(self, label_text, color=COLOR_BALL, radius=0.32):
        """创建一个带编号的球"""
        ball = Circle(
            radius=radius, color=color,
            fill_color=color, fill_opacity=0.7, stroke_width=2
        )
        label = Text(
            str(label_text), font=FONT, font_size=22, color=WHITE
        )
        label.move_to(ball.get_center())
        return VGroup(ball, label)

    def _make_ball_row(self, numbers, color=COLOR_BALL, spacing=0.78):
        """创建一行球"""
        balls = VGroup(*[self._make_ball(n, color=color) for n in numbers])
        balls.arrange(RIGHT, buff=spacing - 0.64)
        return balls

    # ------------------------------------------------------------------
    # 辅助: 创建天平
    # ------------------------------------------------------------------

    def _make_scale(self, center=ORIGIN, beam_width=5.0, post_height=1.8):
        """创建简易天平 (杆+支点+两个托盘)，返回字典"""
        # 支点三角形
        pivot = Triangle(
            fill_color=COLOR_SCALE, fill_opacity=0.8,
            stroke_color=COLOR_SCALE, stroke_width=2
        ).scale(0.25).move_to(center)

        # 立柱
        post = Line(
            center + DOWN * 0.2,
            center + DOWN * post_height * 0.5,
            color=COLOR_SCALE, stroke_width=3
        )

        # 底座
        base = Line(
            center + DOWN * post_height * 0.5 + LEFT * 0.8,
            center + DOWN * post_height * 0.5 + RIGHT * 0.8,
            color=COLOR_SCALE, stroke_width=4
        )

        # 横梁
        beam = Line(
            center + LEFT * beam_width / 2,
            center + RIGHT * beam_width / 2,
            color=COLOR_SCALE, stroke_width=4
        )

        # 左右托盘
        tray_w = 1.8
        left_tray = Line(
            center + LEFT * beam_width / 2 + LEFT * tray_w / 2 + DOWN * 0.05,
            center + LEFT * beam_width / 2 + RIGHT * tray_w / 2 + DOWN * 0.05,
            color=COLOR_SCALE, stroke_width=5
        )
        right_tray = Line(
            center + RIGHT * beam_width / 2 + LEFT * tray_w / 2 + DOWN * 0.05,
            center + RIGHT * beam_width / 2 + RIGHT * tray_w / 2 + DOWN * 0.05,
            color=COLOR_SCALE, stroke_width=5
        )

        # 吊绳
        left_strings = VGroup(
            Line(beam.get_left(), left_tray.get_left(), color=COLOR_SCALE, stroke_width=1.5),
            Line(beam.get_left(), left_tray.get_right(), color=COLOR_SCALE, stroke_width=1.5),
        )
        right_strings = VGroup(
            Line(beam.get_right(), right_tray.get_left(), color=COLOR_SCALE, stroke_width=1.5),
            Line(beam.get_right(), right_tray.get_right(), color=COLOR_SCALE, stroke_width=1.5),
        )

        scale_group = VGroup(
            post, base, pivot, beam,
            left_tray, right_tray,
            left_strings, right_strings
        )

        return {
            "group": scale_group,
            "pivot": pivot,
            "beam": beam,
            "left_tray": left_tray,
            "right_tray": right_tray,
            "left_strings": left_strings,
            "right_strings": right_strings,
            "center": center,
            "beam_width": beam_width,
        }

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '9个球，1个轻次品，最少称几次？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "9个外观相同的球", font=FONT, font_size=38, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "1个是轻的次品", font=FONT, font_size=38, color=COLOR_DEFECT
        ).move_to(UP * 4.6)
        hook3 = Text(
            "用天平最少称几次？", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.5)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)
        self.play(Write(hook3), run_time=0.7)

        # 展示9个球 — 3×3 排列
        self.nine_balls = VGroup()
        for row in range(3):
            for col in range(3):
                num = row * 3 + col + 1
                ball = self._make_ball(num)
                ball.move_to(
                    np.array([
                        (col - 1) * 1.0,
                        -(row - 1) * 1.0,
                        0.0
                    ])
                )
                self.nine_balls.add(ball)

        self.play(
            LaggedStart(
                *[GrowFromCenter(b) for b in self.nine_balls],
                lag_ratio=0.08
            ),
            run_time=1.5
        )

        # 问号
        q = Text("?", font=FONT, font_size=80, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 2.5)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(1.0)

        # 清理钩子文字和问号，保留球
        self.play(FadeOut(VGroup(hook1, hook2, hook3, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 三分法策略 — 分成3组(3,3,3)
    # ------------------------------------------------------------------

    def scene_2_split_strategy(self):
        """展示三分法: 9个球分成3组各3个"""

        title = Text(
            "三分法策略", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step_text = Text(
            "关键: 尽量平均分成3份",
            font=FONT, font_size=28, color=COLOR_GROUP
        ).move_to(UP * 4.5)
        self.play(Write(step_text), run_time=0.6)

        # 动画: 将3×3排列的球重新分成3组, 每组一行
        # 分组位置
        group_y = [1.2, 0.0, -1.2]
        group_labels_text = ["第1组", "第2组", "第3组"]
        group_colors = ["#3b82f6", "#22c55e", "#f59e0b"]

        target_positions = []
        for g in range(3):
            for i in range(3):
                x = (i - 1) * 1.0
                y = group_y[g]
                target_positions.append(np.array([x, y, 0.0]))

        # 动画移动球到分组位置
        anims = []
        for idx, ball in enumerate(self.nine_balls):
            anims.append(ball.animate.move_to(target_positions[idx]))
        self.play(*anims, run_time=1.2)

        # 画分组框 + 标签
        self.group_rects = VGroup()
        self.group_labels = VGroup()
        for g in range(3):
            rect = RoundedRectangle(
                width=3.6, height=1.0,
                corner_radius=0.15,
                stroke_color=group_colors[g],
                stroke_width=2.5, fill_opacity=0
            ).move_to(np.array([0, group_y[g], 0]))

            label = Text(
                group_labels_text[g], font=FONT, font_size=22,
                color=group_colors[g]
            ).next_to(rect, LEFT, buff=0.2)

            self.group_rects.add(rect)
            self.group_labels.add(label)

        self.play(
            *[Create(r) for r in self.group_rects],
            *[FadeIn(l) for l in self.group_labels],
            run_time=0.8
        )

        # 说明文字
        explain = Text(
            "每组3个球，共3组",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 2.8)

        formula_text = VGroup(
            Text("9 ", font=FONT, font_size=30, color=WHITE),
            Text("= 3 + 3 + 3", font=FONT, font_size=30, color=COLOR_GROUP)
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3.7)

        self.play(Write(explain), run_time=0.5)
        self.play(FadeIn(formula_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理文字，保留球和分组框
        self.play(
            FadeOut(VGroup(title, step_text, explain, formula_text)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 第1次称量
    # ------------------------------------------------------------------

    def scene_3_first_weigh(self):
        """第1次称: 取第1组和第2组放天平两边"""

        title = Text(
            "第1次称量", font=FONT, font_size=40,
            color=COLOR_SCALE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step_text = Text(
            "取第1组和第2组放天平两边",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.5)
        self.play(Write(step_text), run_time=0.6)

        # 淡出分组框和标签
        self.play(
            FadeOut(VGroup(self.group_rects, self.group_labels)),
            run_time=0.3
        )

        # 将第3组球移到旁边等待
        group3_balls = VGroup(*[self.nine_balls[i] for i in [6, 7, 8]])
        self.play(
            group3_balls.animate.move_to(RIGHT * 3.2 + DOWN * 3.5).scale(0.75),
            run_time=0.6
        )
        wait_label = Text(
            "第3组\n等待", font=FONT, font_size=18, color=COLOR_ORANGE
        ).next_to(group3_balls, DOWN, buff=0.2)
        self.play(FadeIn(wait_label), run_time=0.3)

        # 创建天平
        scale_center = DOWN * 0.5
        scale = self._make_scale(center=scale_center, beam_width=5.0, post_height=1.6)
        self.play(FadeIn(scale["group"]), run_time=0.8)

        # 将第1组球移到天平左边
        group1_balls = VGroup(*[self.nine_balls[i] for i in [0, 1, 2]])
        left_pos = scale_center + LEFT * 2.5 + UP * 0.5
        self.play(
            group1_balls.animate.arrange(RIGHT, buff=0.12).scale(0.7).move_to(left_pos),
            run_time=0.7
        )

        left_label = Text(
            "第1组", font=FONT, font_size=20, color="#3b82f6"
        ).next_to(group1_balls, UP, buff=0.15)
        self.play(FadeIn(left_label), run_time=0.2)

        # 将第2组球移到天平右边
        group2_balls = VGroup(*[self.nine_balls[i] for i in [3, 4, 5]])
        right_pos = scale_center + RIGHT * 2.5 + UP * 0.5
        self.play(
            group2_balls.animate.arrange(RIGHT, buff=0.12).scale(0.7).move_to(right_pos),
            run_time=0.7
        )

        right_label = Text(
            "第2组", font=FONT, font_size=20, color=COLOR_GROUP
        ).next_to(group2_balls, UP, buff=0.15)
        self.play(FadeIn(right_label), run_time=0.2)
        self.wait(0.5)

        # ★ 天平倾斜动画: 假设次品在第1组，左边轻→左翘
        # 横梁绕支点旋转
        tilt_angle = 12 * DEGREES
        tilt_group = VGroup(
            scale["beam"],
            scale["left_tray"], scale["right_tray"],
            scale["left_strings"], scale["right_strings"],
            group1_balls, group2_balls,
            left_label, right_label
        )

        self.play(
            Rotate(tilt_group, angle=tilt_angle, about_point=scale_center),
            run_time=1.2,
            rate_func=there_and_back_with_pause
        )

        # 结果说明 — 三种情况
        result_box = RoundedRectangle(
            width=7.5, height=3.2,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_SCALE, stroke_width=2
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(result_box), run_time=0.3)

        r1 = VGroup(
            Text("左边翘起 ", font=FONT, font_size=22, color=COLOR_HL),
            Text("→ 次品在第1组", font=FONT, font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.05)

        r2 = VGroup(
            Text("右边翘起 ", font=FONT, font_size=22, color=COLOR_HL),
            Text("→ 次品在第2组", font=FONT, font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.05)

        r3 = VGroup(
            Text("两边平衡 ", font=FONT, font_size=22, color=COLOR_HL),
            Text("→ 次品在第3组", font=FONT, font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.05)

        results = VGroup(r1, r2, r3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        results.move_to(DOWN * 4.5)

        self.play(
            LaggedStart(
                FadeIn(r1, shift=LEFT * 0.3),
                FadeIn(r2, shift=LEFT * 0.3),
                FadeIn(r3, shift=LEFT * 0.3),
                lag_ratio=0.3
            ),
            run_time=1.0
        )

        key_insight = Text(
            "无论哪种情况，都缩小到3个球！",
            font=FONT, font_size=24, color=COLOR_GROUP, weight=BOLD
        ).move_to(DOWN * 6.3)
        self.play(FadeIn(key_insight, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, step_text,
                scale["group"],
                group1_balls, group2_balls, group3_balls,
                left_label, right_label, wait_label,
                result_box, r1, r2, r3, key_insight
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 第2次称量 — 从3个球中找出1个
    # ------------------------------------------------------------------

    def scene_4_second_weigh(self):
        """第2次称: 从3个球中取2个称，找出次品"""

        title = Text(
            "第2次称量", font=FONT, font_size=40,
            color=COLOR_SCALE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step_text = Text(
            "剩下3个球，取其中2个称",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.5)
        self.play(Write(step_text), run_time=0.6)

        # 创建3个球 (标记为 A, B, C)
        ball_a = self._make_ball("A", color=COLOR_BALL)
        ball_b = self._make_ball("B", color=COLOR_BALL)
        ball_c = self._make_ball("C", color=COLOR_BALL)
        three_balls = VGroup(ball_a, ball_b, ball_c).arrange(RIGHT, buff=0.6)
        three_balls.move_to(UP * 3.0)
        self.play(
            LaggedStart(
                *[GrowFromCenter(b) for b in three_balls],
                lag_ratio=0.15
            ),
            run_time=0.6
        )

        # 提示: 其中1个是次品(轻)
        hint = Text(
            "其中1个是轻的次品",
            font=FONT, font_size=22, color=COLOR_DEFECT
        ).move_to(UP * 2.2)
        self.play(FadeIn(hint), run_time=0.3)
        self.wait(0.3)

        # 创建天平
        scale_center = DOWN * 0.2
        scale = self._make_scale(center=scale_center, beam_width=4.0, post_height=1.4)
        self.play(FadeIn(scale["group"]), run_time=0.6)

        # A 和 B 放天平, C 在旁边
        self.play(
            ball_a.animate.scale(0.85).move_to(scale_center + LEFT * 2.0 + UP * 0.5),
            ball_b.animate.scale(0.85).move_to(scale_center + RIGHT * 2.0 + UP * 0.5),
            ball_c.animate.scale(0.85).move_to(RIGHT * 3.5 + DOWN * 1.8),
            run_time=0.7
        )

        c_wait = Text(
            "等待", font=FONT, font_size=18, color=COLOR_ORANGE
        ).next_to(ball_c, DOWN, buff=0.15)
        self.play(FadeIn(c_wait), run_time=0.2)
        self.wait(0.3)

        # 结果分析框
        result_box = RoundedRectangle(
            width=7.5, height=3.6,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_SCALE, stroke_width=2
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(result_box), run_time=0.3)

        case1_title = Text(
            "情况1: A翘起", font=FONT, font_size=24, color=COLOR_HL
        )
        case1_detail = Text(
            "→ A是次品(轻)", font=FONT, font_size=22, color=COLOR_DEFECT
        )
        case1 = VGroup(case1_title, case1_detail).arrange(RIGHT, buff=0.1)

        case2_title = Text(
            "情况2: B翘起", font=FONT, font_size=24, color=COLOR_HL
        )
        case2_detail = Text(
            "→ B是次品(轻)", font=FONT, font_size=22, color=COLOR_DEFECT
        )
        case2 = VGroup(case2_title, case2_detail).arrange(RIGHT, buff=0.1)

        case3_title = Text(
            "情况3: 平衡", font=FONT, font_size=24, color=COLOR_HL
        )
        case3_detail = Text(
            "→ C是次品(轻)", font=FONT, font_size=22, color=COLOR_DEFECT
        )
        case3 = VGroup(case3_title, case3_detail).arrange(RIGHT, buff=0.1)

        cases = VGroup(case1, case2, case3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        cases.move_to(DOWN * 4.2)

        self.play(
            LaggedStart(
                FadeIn(case1, shift=LEFT * 0.3),
                FadeIn(case2, shift=LEFT * 0.3),
                FadeIn(case3, shift=LEFT * 0.3),
                lag_ratio=0.3
            ),
            run_time=1.0
        )

        # 结论
        conclusion = Text(
            "第2次一定能找到次品！",
            font=FONT, font_size=28, color=COLOR_GROUP, weight=BOLD
        ).move_to(DOWN * 6.3)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)

        # 大字结论
        big_result = Text(
            "9个球 → 只需2次！",
            font=FONT, font_size=34, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 7.0)
        self.play(Write(big_result), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, step_text, hint,
                scale["group"],
                ball_a, ball_b, ball_c, c_wait,
                result_box, cases,
                conclusion, big_result
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 规律总结 — ⌈log₃n⌉
    # ------------------------------------------------------------------

    def scene_5_formula_summary(self):
        """总结三分法规律和公式"""

        title = Text(
            "规律总结", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 回顾过程: 树状图
        # 9 → 3 → 1
        level0 = Text("9个球", font=FONT, font_size=28, color=WHITE)
        level0.move_to(UP * 4.0)

        arrow1 = Arrow(
            UP * 3.65, UP * 3.0,
            color=COLOR_SCALE, stroke_width=2.5, buff=0.05,
            max_tip_length_to_length_ratio=0.2
        )
        weigh1_label = Text(
            "第1次称", font=FONT, font_size=20, color=COLOR_SCALE
        ).next_to(arrow1, RIGHT, buff=0.15)

        level1 = Text("3个球", font=FONT, font_size=28, color=COLOR_GROUP)
        level1.move_to(UP * 2.5)

        arrow2 = Arrow(
            UP * 2.15, UP * 1.5,
            color=COLOR_SCALE, stroke_width=2.5, buff=0.05,
            max_tip_length_to_length_ratio=0.2
        )
        weigh2_label = Text(
            "第2次称", font=FONT, font_size=20, color=COLOR_SCALE
        ).next_to(arrow2, RIGHT, buff=0.15)

        level2 = Text("1个球", font=FONT, font_size=28, color=COLOR_DEFECT)
        level2.move_to(UP * 1.0)

        found_label = Text(
            "找到次品！", font=FONT, font_size=24, color=COLOR_DEFECT
        ).next_to(level2, RIGHT, buff=0.3)

        # 逐步出现
        self.play(Write(level0), run_time=0.4)
        self.play(Create(arrow1), FadeIn(weigh1_label), run_time=0.4)
        self.play(Write(level1), run_time=0.4)
        self.play(Create(arrow2), FadeIn(weigh2_label), run_time=0.4)
        self.play(Write(level2), FadeIn(found_label), run_time=0.4)
        self.wait(0.6)

        # 每次除以3的关键
        divide_text = Text(
            "每次称量，范围缩小到原来的",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 0.5)
        divide_frac = MathTex(
            r"\frac{1}{3}", font_size=42, color=COLOR_HL
        ).next_to(divide_text, RIGHT, buff=0.1)
        self.play(Write(divide_text), Write(divide_frac), run_time=0.7)
        self.wait(0.5)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8, height=3.8,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(formula_box), run_time=0.3)

        formula_title = Text(
            "称量次数公式", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 2.3)
        self.play(Write(formula_title), run_time=0.4)

        # 公式: 次数 = ⌈log₃n⌉
        formula_lhs = Text(
            "称量次数 = ", font=FONT, font_size=32, color=WHITE
        )
        formula_rhs = MathTex(
            r"\lceil \log_3 n \rceil",
            font_size=48, color=COLOR_HL
        )
        formula_main = VGroup(formula_lhs, formula_rhs).arrange(RIGHT, buff=0.1)
        formula_main.move_to(DOWN * 3.3)
        self.play(Write(formula_main), run_time=0.9)
        self.wait(0.5)

        # 举例验证
        examples = VGroup(
            VGroup(
                MathTex(r"n=3:", font_size=28, color=WHITE),
                MathTex(r"\lceil\log_3 3\rceil = 1", font_size=28, color=COLOR_GROUP),
                Text(" 次", font=FONT, font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                MathTex(r"n=9:", font_size=28, color=WHITE),
                MathTex(r"\lceil\log_3 9\rceil = 2", font_size=28, color=COLOR_GROUP),
                Text(" 次", font=FONT, font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                MathTex(r"n=27:", font_size=28, color=WHITE),
                MathTex(r"\lceil\log_3 27\rceil = 3", font_size=28, color=COLOR_GROUP),
                Text(" 次", font=FONT, font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        examples.move_to(DOWN * 5.0)

        self.play(
            LaggedStart(
                *[FadeIn(e, shift=LEFT * 0.2) for e in examples],
                lag_ratio=0.25
            ),
            run_time=0.9
        )
        self.wait(0.5)

        # 关键提示
        key_tip = Text(
            "关键: 尽量分成3等份！",
            font=FONT, font_size=26, color=COLOR_ORANGE, weight=BOLD
        ).move_to(DOWN * 6.5)
        self.play(FadeIn(key_tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                level0, arrow1, weigh1_label,
                level1, arrow2, weigh2_label,
                level2, found_label,
                divide_text, divide_frac,
                formula_box, formula_title, formula_main,
                examples, key_tip
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 6个小球围绕旋转
        colors = [COLOR_BALL, COLOR_DEFECT, COLOR_GROUP,
                  COLOR_ORANGE, COLOR_SCALE, COLOR_HL]
        mini_balls = VGroup(*[
            Circle(
                radius=0.18,
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(b, scale=0.3) for b in mini_balls], run_time=0.5)
        self.play(Rotate(mini_balls, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_balls)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 002_找次品.py DefectiveItemLesson
#   高质量:    manim -qh  002_找次品.py DefectiveItemLesson
#   4K:        manim -qk  002_找次品.py DefectiveItemLesson
# ======================================================================
