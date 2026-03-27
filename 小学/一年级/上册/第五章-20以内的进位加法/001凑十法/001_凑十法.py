"""
凑十法 - 20以内的进位加法
一年级上册 第五章
目标受众: 一年级小学生
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


class MakeTenMethod(Scene):
    """
    凑十法教学动画

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 核心概念 - 什么是凑十法
    3. 例题1: 9+6 的凑十过程
    4. 例题2: 8+5 的凑十过程
    5. 总结口诀
    6. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TITLE = "#f1c40f"        # 金色 - 标题
        self.COLOR_NUM_RED = "#e74c3c"      # 红色 - 大数
        self.COLOR_NUM_BLUE = "#3498db"     # 蓝色 - 小数
        self.COLOR_TEN = "#2ecc71"          # 绿色 - 10
        self.COLOR_SPLIT = "#f39c12"        # 橙色 - 拆分
        self.COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 高亮
        self.COLOR_GRAY = "#95a5a6"
        self.FONT = "PingFang SC"

        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_example1()
        self.scene_4_example2()
        self.scene_5_summary()
        self.scene_6_outro()

    # ─────────────────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者标识
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.3)
        self.author = author

        # 主标题
        title = Text(
            "凑十法",
            font=self.FONT,
            font_size=72,
            color=self.COLOR_TITLE,
            weight=BOLD
        ).move_to(UP * 5.5)

        subtitle = Text(
            "20以内进位加法的秘密武器",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_GRAY
        ).move_to(UP * 4.5)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 钩子问题
        hook_q = Text(
            "9 + 6 = ?",
            font=self.FONT,
            font_size=80,
            color=WHITE
        ).move_to(UP * 2.0)

        hook_sub = Text(
            "你会算吗？",
            font=self.FONT,
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.8)

        self.play(FadeIn(hook_q, scale=0.8), run_time=0.7)
        self.play(FadeIn(hook_sub, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook_q),
            FadeOut(hook_sub),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 2: 核心概念
    # ─────────────────────────────────────────────────────────────
    def scene_2_concept(self):
        concept_title = Text(
            "什么是凑十法？",
            font=self.FONT,
            font_size=44,
            color=self.COLOR_TITLE,
            weight=BOLD
        ).move_to(UP * 6.0)

        self.play(Write(concept_title), run_time=0.7)

        # 核心思路文字说明
        step1 = Text(
            "① 看大数",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_RED
        ).move_to(UP * 4.5 + LEFT * 1.5)

        step2 = Text(
            "② 拆小数",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_BLUE
        ).move_to(UP * 3.2 + LEFT * 1.5)

        step3 = Text(
            "③ 先凑十",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_TEN
        ).move_to(UP * 1.9 + LEFT * 1.5)

        step4 = Text(
            "④ 再加余",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.6 + LEFT * 1.5)

        steps = VGroup(step1, step2, step3, step4)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 十的方块图示
        ten_box = self._make_ten_frame().move_to(DOWN * 2.0)
        ten_label = Text(
            "满10就进位！",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_TEN
        ).move_to(DOWN * 4.0)

        self.play(Create(ten_box), run_time=0.8)
        self.play(Write(ten_label), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(concept_title),
            FadeOut(steps),
            FadeOut(ten_box),
            FadeOut(ten_label),
            run_time=0.5
        )

    def _make_ten_frame(self):
        """创建10格框示意图"""
        boxes = VGroup()
        cols = 5
        rows = 2
        box_size = 0.55
        gap = 0.08
        total_w = cols * (box_size + gap) - gap
        total_h = rows * (box_size + gap) - gap
        start_x = -total_w / 2
        start_y = total_h / 2

        for r in range(rows):
            for c in range(cols):
                x = start_x + c * (box_size + gap) + box_size / 2
                y = start_y - r * (box_size + gap) - box_size / 2
                box = Square(
                    side_length=box_size,
                    color=self.COLOR_TEN,
                    fill_color=self.COLOR_TEN,
                    fill_opacity=0.3,
                    stroke_width=2
                )
                box.move_to([x, y, 0])
                boxes.add(box)

        label = Text(
            "10格框",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_TEN
        ).next_to(boxes, DOWN, buff=0.2)
        return VGroup(boxes, label)

    # ─────────────────────────────────────────────────────────────
    # Scene 3: 例题1 - 9 + 6
    # ─────────────────────────────────────────────────────────────
    def scene_3_example1(self):
        # 例题标题
        ex_label = Text(
            "例题 1",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_GRAY
        ).move_to(UP * 7.0 + LEFT * 2.5)

        self.play(FadeIn(ex_label), run_time=0.3)

        # 问题展示
        problem = Text(
            "9 + 6 = ?",
            font=self.FONT,
            font_size=64,
            color=WHITE
        ).move_to(UP * 5.7)

        self.play(Write(problem), run_time=0.6)
        self.wait(0.3)

        # 画出9个红圆 + 6个蓝圆
        circles_9 = self._make_circles(9, self.COLOR_NUM_RED)
        circles_6 = self._make_circles(6, self.COLOR_NUM_BLUE)

        circles_9.arrange(RIGHT, buff=0.18)
        circles_6.arrange(RIGHT, buff=0.18)

        all_circles = VGroup(circles_9, circles_6)
        all_circles.arrange(RIGHT, buff=0.45)
        all_circles.move_to(UP * 3.8)

        label_9 = Text(
            "9个",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_RED
        ).next_to(circles_9, DOWN, buff=0.12)
        label_6 = Text(
            "6个",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_BLUE
        ).next_to(circles_6, DOWN, buff=0.12)

        self.play(
            LaggedStart(*[FadeIn(c, scale=0.5) for c in circles_9], lag_ratio=0.05),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.5) for c in circles_6], lag_ratio=0.05),
            run_time=0.6
        )
        self.play(FadeIn(label_9), FadeIn(label_6), run_time=0.3)
        self.wait(0.3)

        # Step B: 看大数 9，想需要几凑十
        think_text = Text(
            "看大数 9",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_RED
        ).move_to(UP * 2.4)

        think_text2 = Text(
            "9 + 1 = 10",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_RED
        ).move_to(UP * 1.7)

        self.play(Write(think_text), run_time=0.5)
        self.play(Write(think_text2), run_time=0.5)
        self.wait(0.5)

        # 高亮9个红圆
        self.play(
            *[Indicate(c, scale_factor=1.2, color=self.COLOR_HIGHLIGHT)
              for c in circles_9],
            run_time=0.6
        )

        # Step C: 把6拆成1和5
        split_text = Text(
            "把 6 拆成 1 和 5",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_SPLIT
        ).move_to(UP * 0.8)

        self.play(Write(split_text), run_time=0.5)

        # 高亮第1个蓝圆为橙色
        circles_6[0].set_color(self.COLOR_SPLIT)
        self.play(
            Indicate(circles_6[0], scale_factor=1.3, color=self.COLOR_SPLIT),
            run_time=0.5
        )

        brace_1 = Brace(circles_6[0], DOWN, buff=0.05, color=self.COLOR_SPLIT)
        brace_1_label = Text(
            "1",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_SPLIT
        ).next_to(brace_1, DOWN, buff=0.05)

        circles_6_rest = VGroup(*[circles_6[i] for i in range(1, 6)])
        brace_5 = Brace(circles_6_rest, DOWN, buff=0.05, color=self.COLOR_NUM_BLUE)
        brace_5_label = Text(
            "5",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_BLUE
        ).next_to(brace_5, DOWN, buff=0.05)

        self.play(
            Create(brace_1), Write(brace_1_label),
            Create(brace_5), Write(brace_5_label),
            run_time=0.6
        )
        self.wait(0.5)

        # Step D: 9 + 1 = 10
        step_d_text = Text(
            "9 + 1 = 10",
            font=self.FONT,
            font_size=38,
            color=self.COLOR_TEN
        ).move_to(DOWN * 0.5)

        self.play(Write(step_d_text), run_time=0.5)

        # 把第1个蓝圆复制移到9个红圆旁边变绿
        orange_circle = circles_6[0].copy()
        target_pos = circles_9[-1].get_center() + RIGHT * 0.55
        self.play(
            orange_circle.animate.move_to(target_pos).set_color(self.COLOR_TEN),
            run_time=0.6
        )

        new_group = VGroup(*circles_9, orange_circle)
        ten_box_highlight = SurroundingRectangle(
            new_group, color=self.COLOR_TEN, buff=0.1, corner_radius=0.15
        )
        ten_label2 = Text(
            "= 10",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_TEN
        ).next_to(ten_box_highlight, RIGHT, buff=0.12)
        self.play(Create(ten_box_highlight), Write(ten_label2), run_time=0.5)
        self.wait(0.4)

        # Step E: 10 + 5 = 15
        step_e_text = Text(
            "10 + 5 = 15",
            font=self.FONT,
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.7)

        self.play(Write(step_e_text), run_time=0.5)
        self.wait(0.5)

        # 最终答案
        answer = Text(
            "9 + 6 = 15",
            font=self.FONT,
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(answer, scale=0.9), run_time=0.6)
        self.play(Indicate(answer, scale_factor=1.05, color=YELLOW), run_time=0.5)
        self.wait(1.5)

        # 清理
        to_fade = VGroup(
            ex_label, problem,
            circles_9, circles_6, label_9, label_6,
            think_text, think_text2, split_text,
            brace_1, brace_1_label, brace_5, brace_5_label,
            step_d_text, orange_circle, ten_box_highlight, ten_label2,
            step_e_text, answer
        )
        self.play(FadeOut(to_fade), run_time=0.5)

    def _make_circles(self, n, color):
        """创建n个填色圆点"""
        circles = VGroup()
        for _ in range(n):
            c = Circle(
                radius=0.22,
                color=color,
                fill_color=color,
                fill_opacity=0.85,
                stroke_width=2
            )
            circles.add(c)
        return circles

    # ─────────────────────────────────────────────────────────────
    # Scene 4: 例题2 - 8 + 5
    # ─────────────────────────────────────────────────────────────
    def scene_4_example2(self):
        # 例题标题
        ex_label = Text(
            "例题 2",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_GRAY
        ).move_to(UP * 7.0 + LEFT * 2.5)

        self.play(FadeIn(ex_label), run_time=0.3)

        # 问题
        problem = Text(
            "8 + 5 = ?",
            font=self.FONT,
            font_size=64,
            color=WHITE
        ).move_to(UP * 5.7)

        self.play(Write(problem), run_time=0.6)
        self.wait(0.3)

        # 画出8个红圆 + 5个蓝圆
        circles_8 = self._make_circles(8, self.COLOR_NUM_RED)
        circles_5 = self._make_circles(5, self.COLOR_NUM_BLUE)

        circles_8.arrange(RIGHT, buff=0.18)
        circles_5.arrange(RIGHT, buff=0.18)

        all_circles = VGroup(circles_8, circles_5)
        all_circles.arrange(RIGHT, buff=0.55)
        all_circles.move_to(UP * 3.8)

        label_8 = Text(
            "8个",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_RED
        ).next_to(circles_8, DOWN, buff=0.12)
        label_5 = Text(
            "5个",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_BLUE
        ).next_to(circles_5, DOWN, buff=0.12)

        self.play(
            LaggedStart(*[FadeIn(c, scale=0.5) for c in circles_8], lag_ratio=0.05),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.5) for c in circles_5], lag_ratio=0.05),
            run_time=0.6
        )
        self.play(FadeIn(label_8), FadeIn(label_5), run_time=0.3)
        self.wait(0.3)

        # 看大数 8，需要2凑十
        think_text = Text(
            "看大数 8",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_RED
        ).move_to(UP * 2.4)

        think_text2 = Text(
            "8 + 2 = 10",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_NUM_RED
        ).move_to(UP * 1.7)

        self.play(Write(think_text), run_time=0.5)
        self.play(Write(think_text2), run_time=0.5)
        self.wait(0.4)

        # 把5拆成2和3
        split_text = Text(
            "把 5 拆成 2 和 3",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_SPLIT
        ).move_to(UP * 0.8)

        self.play(Write(split_text), run_time=0.5)

        # 高亮蓝圆前2个为橙色
        circles_5[0].set_color(self.COLOR_SPLIT)
        circles_5[1].set_color(self.COLOR_SPLIT)
        self.play(
            Indicate(circles_5[0], scale_factor=1.3, color=self.COLOR_SPLIT),
            Indicate(circles_5[1], scale_factor=1.3, color=self.COLOR_SPLIT),
            run_time=0.5
        )

        circles_5_first2 = VGroup(circles_5[0], circles_5[1])
        brace_2 = Brace(circles_5_first2, DOWN, buff=0.05, color=self.COLOR_SPLIT)
        brace_2_label = Text(
            "2",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_SPLIT
        ).next_to(brace_2, DOWN, buff=0.05)

        circles_5_last3 = VGroup(*[circles_5[i] for i in range(2, 5)])
        brace_3 = Brace(circles_5_last3, DOWN, buff=0.05, color=self.COLOR_NUM_BLUE)
        brace_3_label = Text(
            "3",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NUM_BLUE
        ).next_to(brace_3, DOWN, buff=0.05)

        self.play(
            Create(brace_2), Write(brace_2_label),
            Create(brace_3), Write(brace_3_label),
            run_time=0.6
        )
        self.wait(0.4)

        # 8 + 2 = 10
        step_d_text = Text(
            "8 + 2 = 10",
            font=self.FONT,
            font_size=38,
            color=self.COLOR_TEN
        ).move_to(DOWN * 0.5)

        self.play(Write(step_d_text), run_time=0.5)

        # 把2个橙色圆移到8旁边变绿
        moved_c0 = circles_5[0].copy()
        moved_c1 = circles_5[1].copy()
        target_pos_0 = circles_8[-1].get_center() + RIGHT * 0.55
        target_pos_1 = circles_8[-1].get_center() + RIGHT * 1.07
        self.play(
            moved_c0.animate.move_to(target_pos_0).set_color(self.COLOR_TEN),
            moved_c1.animate.move_to(target_pos_1).set_color(self.COLOR_TEN),
            run_time=0.5
        )

        new_group_8 = VGroup(*circles_8, moved_c0, moved_c1)
        ten_box_8 = SurroundingRectangle(
            new_group_8, color=self.COLOR_TEN, buff=0.1, corner_radius=0.15
        )
        ten_label_8 = Text(
            "= 10",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_TEN
        ).next_to(ten_box_8, RIGHT, buff=0.1)
        self.play(Create(ten_box_8), Write(ten_label_8), run_time=0.5)
        self.wait(0.4)

        # 10 + 3 = 13
        step_e_text = Text(
            "10 + 3 = 13",
            font=self.FONT,
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.7)

        self.play(Write(step_e_text), run_time=0.5)
        self.wait(0.4)

        # 最终答案
        answer = Text(
            "8 + 5 = 13",
            font=self.FONT,
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(answer, scale=0.9), run_time=0.6)
        self.play(Indicate(answer, scale_factor=1.05, color=YELLOW), run_time=0.5)
        self.wait(1.5)

        # 清理
        to_fade = VGroup(
            ex_label, problem,
            circles_8, circles_5, label_8, label_5,
            think_text, think_text2, split_text,
            brace_2, brace_2_label, brace_3, brace_3_label,
            step_d_text, moved_c0, moved_c1, ten_box_8, ten_label_8,
            step_e_text, answer
        )
        self.play(FadeOut(to_fade), run_time=0.5)

    # ─────────────────────────────────────────────────────────────
    # Scene 5: 总结口诀
    # ─────────────────────────────────────────────────────────────
    def scene_5_summary(self):
        # 标题
        sum_title = Text(
            "凑十法 口诀",
            font=self.FONT,
            font_size=48,
            color=self.COLOR_TITLE,
            weight=BOLD
        ).move_to(UP * 6.0)

        self.play(Write(sum_title), run_time=0.7)

        # 口诀卡片
        step_names = ["第一步", "第二步", "第三步", "第四步"]
        step_contents = ["看大数", "拆小数", "先凑十", "再加余"]
        step_colors = [
            self.COLOR_NUM_RED,
            self.COLOR_NUM_BLUE,
            self.COLOR_TEN,
            self.COLOR_HIGHLIGHT,
        ]

        cards = VGroup()
        for i in range(4):
            num = Text(
                step_names[i],
                font=self.FONT,
                font_size=22,
                color=self.COLOR_GRAY
            )
            content = Text(
                step_contents[i],
                font=self.FONT,
                font_size=38,
                color=step_colors[i],
                weight=BOLD
            )
            row = VGroup(num, content).arrange(RIGHT, buff=0.4)
            cards.add(row)

        cards.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        cards.move_to(UP * 2.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.4)
            self.wait(0.15)

        self.wait(0.5)

        # 两道例题公式回顾
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_GRAY, stroke_width=1)
        divider.move_to(DOWN * 0.2)
        self.play(Create(divider), run_time=0.4)

        formula_title = Text(
            "两个例子",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_GRAY
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(formula_title), run_time=0.3)

        # 9+6 分解
        f1_left = Text("9 + 6", font=self.FONT, font_size=30, color=WHITE)
        f1_mid = Text("=", font=self.FONT, font_size=30, color=self.COLOR_GRAY)
        f1_right = Text(
            "9 + 1 + 5 = 10 + 5 = 15",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_TEN
        )
        f1 = VGroup(f1_left, f1_mid, f1_right).arrange(RIGHT, buff=0.2)
        f1.move_to(DOWN * 1.8)

        # 8+5 分解
        f2_left = Text("8 + 5", font=self.FONT, font_size=30, color=WHITE)
        f2_mid = Text("=", font=self.FONT, font_size=30, color=self.COLOR_GRAY)
        f2_right = Text(
            "8 + 2 + 3 = 10 + 3 = 13",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_TEN
        )
        f2 = VGroup(f2_left, f2_mid, f2_right).arrange(RIGHT, buff=0.2)
        f2.move_to(DOWN * 2.9)

        self.play(FadeIn(f1), run_time=0.5)
        self.play(FadeIn(f2), run_time=0.5)
        self.wait(0.5)

        # 强调语
        emphasis = Text(
            "先凑10，再加余！",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.2)

        self.play(FadeIn(emphasis, scale=0.9), run_time=0.5)
        self.play(Indicate(emphasis, scale_factor=1.05), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(sum_title),
            FadeOut(cards),
            FadeOut(divider),
            FadeOut(formula_title),
            FadeOut(f1),
            FadeOut(f2),
            FadeOut(emphasis),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 6: 片尾关注
    # ─────────────────────────────────────────────────────────────
    def scene_6_outro(self):
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=38,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_GRAY
        ).move_to(UP * 0.5)

        self.play(Transform(self.author, author_name), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰：五个彩色星星
        deco = VGroup()
        colors = [
            self.COLOR_NUM_RED,
            self.COLOR_NUM_BLUE,
            self.COLOR_TEN,
            self.COLOR_SPLIT,
            self.COLOR_HIGHLIGHT
        ]
        for i, col in enumerate(colors):
            angle = i * 2 * PI / len(colors)
            pos = np.array([2.5 * np.cos(angle), 2.5 * np.sin(angle), 0]) + DOWN * 2.8
            star = Star(
                n=5,
                outer_radius=0.28,
                inner_radius=0.12,
                color=col,
                fill_color=col,
                fill_opacity=0.9
            )
            star.move_to(pos)
            deco.add(star)

        self.play(
            LaggedStart(*[FadeIn(s, scale=0.5) for s in deco], lag_ratio=0.1),
            run_time=0.7
        )
        self.play(Rotate(deco, angle=PI), run_time=1.5)
        self.wait(0.5)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=1.0
        )
