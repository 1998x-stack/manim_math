"""
连加、连减、加减混合 - Manim 教学动画
一年级上册 第二章 10以内数的加减法

内容: 理解运算顺序从左往右依次计算
      连加: 2 + 3 + 1 = 6
      连减: 5 - 2 - 1 = 2
      加减混合: 5 + 2 - 3 = 4

目标: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# 颜色配置
COLOR_BG = "#1a1a2e"
COLOR_PRIMARY = "#4fc3f7"       # 淡蓝 - 主色
COLOR_SECONDARY = "#81c784"     # 淡绿 - 辅色
COLOR_ACCENT = "#ffb74d"        # 橙 - 强调色
COLOR_DANGER = "#ef9a9a"        # 淡红 - 减法
COLOR_TITLE = "#fff9c4"         # 淡黄 - 标题
COLOR_RESULT = "#ce93d8"        # 紫 - 结果
COLOR_ARROW = "#4dd0e1"         # 青 - 箭头
COLOR_BIRD = "#fff176"          # 黄 - 小鸟
COLOR_RULE = "#a5d6a7"          # 绿 - 规则文字


def make_bird(color=COLOR_BIRD, scale=1.0):
    """创建简单小鸟图形（用圆和三角形组合）"""
    body = Ellipse(width=0.5, height=0.3, color=color, fill_opacity=1, stroke_width=0)
    head = Circle(radius=0.12, color=color, fill_opacity=1, stroke_width=0).shift(RIGHT * 0.22 + UP * 0.12)
    # 翅膀
    wing = Arc(radius=0.2, start_angle=PI * 0.2, angle=PI * 0.6, color=color, stroke_width=3)
    wing.shift(LEFT * 0.05 + UP * 0.15)
    # 眼睛
    eye = Circle(radius=0.03, color=COLOR_BG, fill_opacity=1, stroke_width=0).shift(RIGHT * 0.3 + UP * 0.17)
    # 嘴巴
    beak = Triangle(color=COLOR_ACCENT, fill_opacity=1, stroke_width=0).scale(0.06).rotate(-PI / 6).shift(RIGHT * 0.38 + UP * 0.11)
    bird = VGroup(body, head, wing, eye, beak).scale(scale)
    return bird


class ConsecutiveOperationsLesson(Scene):
    """
    连加、连减、加减混合 教学动画场景

    场景顺序:
    1. 开场 - 引入连加概念（小鸟情境）
    2. 连加: 2 + 3 + 1 = 6，从左往右计算
    3. 连减: 5 - 2 - 1 = 2，从左往右计算
    4. 加减混合: 5 + 2 - 3 = 4，从左往右计算
    5. 规则总结 - 从左往右
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        self.scene_1_opening()
        self.scene_2_consecutive_addition()
        self.scene_3_consecutive_subtraction()
        self.scene_4_mixed_operations()
        self.scene_5_rule_summary()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # 场景 1: 开场
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者标识（顶部，全程保留）
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_tag, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        title = Text("连加、连减、加减混合", font="Noto Sans CJK SC", font_size=36, color=COLOR_TITLE)
        title.move_to(UP * 5.5)

        subtitle = Text("从左往右，依次计算", font="Noto Sans CJK SC", font_size=26, color=COLOR_PRIMARY)
        subtitle.move_to(UP * 4.6)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 情境图：树枝上的小鸟
        branch = Line(LEFT * 3.5, RIGHT * 3.5, color="#8d6e63", stroke_width=6)
        branch.move_to(UP * 2.5)
        self.play(Create(branch), run_time=0.4)

        # 最初有2只小鸟
        birds_init = VGroup(*[make_bird() for _ in range(2)])
        birds_init.arrange(RIGHT, buff=0.5)
        birds_init.move_to(UP * 3.1)
        self.play(FadeIn(birds_init), run_time=0.5)

        # 情境文字
        story = Text("树上有2只小鸟，", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        story.move_to(UP * 1.5)
        self.play(Write(story), run_time=0.6)
        self.wait(0.4)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(branch),
            FadeOut(birds_init),
            FadeOut(story),
            run_time=0.4,
        )

    # ─────────────────────────────────────────────
    # 场景 2: 连加 2 + 3 + 1 = 6
    # ─────────────────────────────────────────────
    def scene_2_consecutive_addition(self):
        # 场景标题
        sec_title = Text("连  加", font="Noto Sans CJK SC", font_size=38, color=COLOR_SECONDARY)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 情境演示 ──
        # 树枝
        branch = Line(LEFT * 3.8, RIGHT * 3.8, color="#8d6e63", stroke_width=6)
        branch.move_to(UP * 3.8)
        self.play(Create(branch), run_time=0.3)

        # 先有 2 只
        birds_2 = VGroup(*[make_bird(scale=0.85) for _ in range(2)])
        birds_2.arrange(RIGHT, buff=0.3)
        birds_2.move_to(UP * 4.4 + LEFT * 2.0)
        self.play(FadeIn(birds_2), run_time=0.4)

        label_2 = Text("2只", font="Noto Sans CJK SC", font_size=22, color=COLOR_PRIMARY)
        label_2.next_to(birds_2, DOWN, buff=0.1)
        self.play(FadeIn(label_2), run_time=0.3)

        desc1 = Text("树上先有2只，", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        desc1.move_to(UP * 2.8)
        self.play(Write(desc1), run_time=0.5)
        self.wait(0.3)

        # 又飞来 3 只
        birds_3 = VGroup(*[make_bird(color="#80cbc4", scale=0.85) for _ in range(3)])
        birds_3.arrange(RIGHT, buff=0.3)
        birds_3.move_to(UP * 4.4 + RIGHT * 1.2)
        self.play(FadeIn(birds_3, shift=DOWN * 0.3), run_time=0.5)

        label_3 = Text("又飞来3只", font="Noto Sans CJK SC", font_size=22, color="#80cbc4")
        label_3.next_to(birds_3, DOWN, buff=0.1)
        self.play(FadeIn(label_3), run_time=0.3)

        desc2 = Text("又飞来3只，", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        desc2.next_to(desc1, DOWN, buff=0.2)
        self.play(Write(desc2), run_time=0.5)
        self.wait(0.3)

        # 再飞来 1 只
        bird_1 = make_bird(color=COLOR_ACCENT, scale=0.85)
        bird_1.move_to(UP * 4.4 + RIGHT * 3.5)
        self.play(FadeIn(bird_1, shift=DOWN * 0.3), run_time=0.4)

        label_1 = Text("再来1只", font="Noto Sans CJK SC", font_size=22, color=COLOR_ACCENT)
        label_1.next_to(bird_1, DOWN, buff=0.1)
        self.play(FadeIn(label_1), run_time=0.3)

        desc3 = Text("再飞来1只。", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        desc3.next_to(desc2, DOWN, buff=0.2)
        self.play(Write(desc3), run_time=0.5)
        self.wait(0.5)

        # 问：现在共有几只？
        question = Text("现在共有几只？", font="Noto Sans CJK SC", font_size=26, color=COLOR_TITLE)
        question.move_to(UP * 1.0)
        self.play(Write(question), run_time=0.5)
        self.wait(0.6)

        # 淡出情境文字，进入计算
        self.play(
            FadeOut(branch),
            FadeOut(birds_2), FadeOut(label_2),
            FadeOut(birds_3), FadeOut(label_3),
            FadeOut(bird_1), FadeOut(label_1),
            FadeOut(desc1), FadeOut(desc2), FadeOut(desc3),
            FadeOut(question),
            run_time=0.4,
        )

        # ── 公式展示 ──
        formula_line = MathTex(r"2 + 3 + 1", font_size=64, color=WHITE)
        formula_line.move_to(UP * 2.5)
        self.play(Write(formula_line), run_time=0.7)
        self.wait(0.3)

        # 规则提示
        rule_txt = Text("从左往右依次计算", font="Noto Sans CJK SC", font_size=24, color=COLOR_RULE)
        rule_txt.move_to(UP * 1.5)
        arrow_lr = Arrow(LEFT * 2.5, RIGHT * 2.5, color=COLOR_RULE, buff=0)
        arrow_lr.move_to(UP * 1.0)
        self.play(FadeIn(rule_txt), Create(arrow_lr), run_time=0.5)

        # ── 步骤 1: 2 + 3 = 5 ──
        step1_label = Text("第一步：2 + 3", font="Noto Sans CJK SC", font_size=26, color=COLOR_PRIMARY)
        step1_label.move_to(UP * 0.1)
        self.play(Write(step1_label), run_time=0.5)

        # 高亮 "2 + 3" 部分
        bracket1 = Brace(formula_line[0][0:3], direction=DOWN, color=COLOR_PRIMARY)
        bracket1_label = MathTex(r"= 5", font_size=48, color=COLOR_PRIMARY)
        bracket1_label.next_to(bracket1, DOWN, buff=0.15)
        self.play(GrowFromCenter(bracket1), Write(bracket1_label), run_time=0.6)
        self.wait(0.5)

        # ── 步骤 2: 5 + 1 = 6 ──
        step2_label = Text("第二步：5 + 1", font="Noto Sans CJK SC", font_size=26, color=COLOR_ACCENT)
        step2_label.next_to(step1_label, DOWN, buff=0.2)
        self.play(Write(step2_label), run_time=0.5)

        step2_calc = MathTex(r"5 + 1 = 6", font_size=48, color=COLOR_ACCENT)
        step2_calc.next_to(step2_label, DOWN, buff=0.2)
        self.play(Write(step2_calc), run_time=0.5)
        self.wait(0.5)

        # ── 完整等式 ──
        full_eq = MathTex(r"2 + 3 + 1 = 6", font_size=64, color=COLOR_RESULT)
        full_eq.move_to(DOWN * 2.5)
        self.play(Write(full_eq), run_time=0.7)
        self.play(Indicate(full_eq, color=COLOR_RESULT, scale_factor=1.15), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(sec_title),
            FadeOut(formula_line),
            FadeOut(rule_txt), FadeOut(arrow_lr),
            FadeOut(step1_label), FadeOut(bracket1), FadeOut(bracket1_label),
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(full_eq),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 3: 连减 5 - 2 - 1 = 2
    # ─────────────────────────────────────────────
    def scene_3_consecutive_subtraction(self):
        sec_title = Text("连  减", font="Noto Sans CJK SC", font_size=38, color=COLOR_DANGER)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 情境演示 ──
        branch = Line(LEFT * 3.8, RIGHT * 3.8, color="#8d6e63", stroke_width=6)
        branch.move_to(UP * 4.0)
        self.play(Create(branch), run_time=0.3)

        # 5 只小鸟
        birds_all = VGroup(*[make_bird(scale=0.75) for _ in range(5)])
        birds_all.arrange(RIGHT, buff=0.2)
        birds_all.move_to(UP * 4.5)
        self.play(FadeIn(birds_all), run_time=0.5)

        desc_init = Text("树上有5只小鸟", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        desc_init.move_to(UP * 3.1)
        self.play(Write(desc_init), run_time=0.5)
        self.wait(0.4)

        # 飞走 2 只（交叉划掉前两只）
        cross_marks = VGroup()
        for i in range(2):
            c1 = Line(
                birds_all[i].get_corner(UL),
                birds_all[i].get_corner(DR),
                color=COLOR_DANGER, stroke_width=3,
            )
            c2 = Line(
                birds_all[i].get_corner(UR),
                birds_all[i].get_corner(DL),
                color=COLOR_DANGER, stroke_width=3,
            )
            cross_marks.add(c1, c2)

        desc_fly2 = Text("飞走2只，", font="Noto Sans CJK SC", font_size=24, color=COLOR_DANGER)
        desc_fly2.next_to(desc_init, DOWN, buff=0.2)
        self.play(Create(cross_marks), Write(desc_fly2), run_time=0.5)
        self.wait(0.3)

        # 再飞走 1 只
        cross2 = VGroup(
            Line(birds_all[2].get_corner(UL), birds_all[2].get_corner(DR), color=COLOR_DANGER, stroke_width=3),
            Line(birds_all[2].get_corner(UR), birds_all[2].get_corner(DL), color=COLOR_DANGER, stroke_width=3),
        )
        desc_fly1 = Text("再飞走1只。", font="Noto Sans CJK SC", font_size=24, color=COLOR_DANGER)
        desc_fly1.next_to(desc_fly2, DOWN, buff=0.2)
        self.play(Create(cross2), Write(desc_fly1), run_time=0.5)
        self.wait(0.3)

        question = Text("还有几只？", font="Noto Sans CJK SC", font_size=26, color=COLOR_TITLE)
        question.move_to(UP * 1.2)
        self.play(Write(question), run_time=0.4)
        self.wait(0.5)

        # 清理情境
        self.play(
            FadeOut(branch),
            FadeOut(birds_all),
            FadeOut(cross_marks), FadeOut(cross2),
            FadeOut(desc_init), FadeOut(desc_fly2), FadeOut(desc_fly1),
            FadeOut(question),
            run_time=0.4,
        )

        # ── 公式 ──
        formula_line = MathTex(r"5 - 2 - 1", font_size=64, color=WHITE)
        formula_line.move_to(UP * 2.5)
        self.play(Write(formula_line), run_time=0.6)
        self.wait(0.3)

        rule_txt = Text("从左往右依次计算", font="Noto Sans CJK SC", font_size=24, color=COLOR_RULE)
        rule_txt.move_to(UP * 1.5)
        arrow_lr = Arrow(LEFT * 2.5, RIGHT * 2.5, color=COLOR_RULE, buff=0)
        arrow_lr.move_to(UP * 1.0)
        self.play(FadeIn(rule_txt), Create(arrow_lr), run_time=0.5)

        # 步骤 1: 5 - 2 = 3
        step1_label = Text("第一步：5 - 2", font="Noto Sans CJK SC", font_size=26, color=COLOR_PRIMARY)
        step1_label.move_to(UP * 0.1)
        self.play(Write(step1_label), run_time=0.5)

        bracket1 = Brace(formula_line[0][0:3], direction=DOWN, color=COLOR_PRIMARY)
        bracket1_label = MathTex(r"= 3", font_size=48, color=COLOR_PRIMARY)
        bracket1_label.next_to(bracket1, DOWN, buff=0.15)
        self.play(GrowFromCenter(bracket1), Write(bracket1_label), run_time=0.6)
        self.wait(0.5)

        # 步骤 2: 3 - 1 = 2
        step2_label = Text("第二步：3 - 1", font="Noto Sans CJK SC", font_size=26, color=COLOR_ACCENT)
        step2_label.next_to(step1_label, DOWN, buff=0.2)
        self.play(Write(step2_label), run_time=0.5)

        step2_calc = MathTex(r"3 - 1 = 2", font_size=48, color=COLOR_ACCENT)
        step2_calc.next_to(step2_label, DOWN, buff=0.2)
        self.play(Write(step2_calc), run_time=0.5)
        self.wait(0.5)

        # 完整等式
        full_eq = MathTex(r"5 - 2 - 1 = 2", font_size=64, color=COLOR_RESULT)
        full_eq.move_to(DOWN * 2.5)
        self.play(Write(full_eq), run_time=0.7)
        self.play(Indicate(full_eq, color=COLOR_RESULT, scale_factor=1.15), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(sec_title),
            FadeOut(formula_line),
            FadeOut(rule_txt), FadeOut(arrow_lr),
            FadeOut(step1_label), FadeOut(bracket1), FadeOut(bracket1_label),
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(full_eq),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 4: 加减混合 5 + 2 - 3 = 4
    # ─────────────────────────────────────────────
    def scene_4_mixed_operations(self):
        sec_title = Text("加减混合", font="Noto Sans CJK SC", font_size=38, color=COLOR_PRIMARY)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 情境演示 ──
        branch = Line(LEFT * 3.8, RIGHT * 3.8, color="#8d6e63", stroke_width=6)
        branch.move_to(UP * 4.0)
        self.play(Create(branch), run_time=0.3)

        # 先有 5 只
        birds_5 = VGroup(*[make_bird(scale=0.75) for _ in range(5)])
        birds_5.arrange(RIGHT, buff=0.18)
        birds_5.move_to(UP * 4.5 + LEFT * 0.8)
        self.play(FadeIn(birds_5), run_time=0.4)

        desc1 = Text("树上有5只，", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        desc1.move_to(UP * 3.1)
        self.play(Write(desc1), run_time=0.5)
        self.wait(0.3)

        # 飞来 2 只
        birds_plus2 = VGroup(*[make_bird(color="#80cbc4", scale=0.75) for _ in range(2)])
        birds_plus2.arrange(RIGHT, buff=0.18)
        birds_plus2.move_to(UP * 4.5 + RIGHT * 2.5)
        self.play(FadeIn(birds_plus2, shift=DOWN * 0.3), run_time=0.4)

        desc2 = Text("飞来2只，", font="Noto Sans CJK SC", font_size=24, color=COLOR_SECONDARY)
        desc2.next_to(desc1, DOWN, buff=0.2)
        self.play(Write(desc2), run_time=0.4)
        self.wait(0.3)

        # 飞走 3 只（划掉前 3 只）
        all_birds_group = VGroup(*list(birds_5) + list(birds_plus2))
        cross_marks = VGroup()
        for i in range(3):
            bird_obj = all_birds_group[i]
            c1 = Line(bird_obj.get_corner(UL), bird_obj.get_corner(DR), color=COLOR_DANGER, stroke_width=3)
            c2 = Line(bird_obj.get_corner(UR), bird_obj.get_corner(DL), color=COLOR_DANGER, stroke_width=3)
            cross_marks.add(c1, c2)

        desc3 = Text("飞走3只。", font="Noto Sans CJK SC", font_size=24, color=COLOR_DANGER)
        desc3.next_to(desc2, DOWN, buff=0.2)
        self.play(Create(cross_marks), Write(desc3), run_time=0.5)
        self.wait(0.3)

        question = Text("还有几只？", font="Noto Sans CJK SC", font_size=26, color=COLOR_TITLE)
        question.move_to(UP * 1.2)
        self.play(Write(question), run_time=0.4)
        self.wait(0.5)

        # 清理情境
        self.play(
            FadeOut(branch),
            FadeOut(birds_5), FadeOut(birds_plus2),
            FadeOut(cross_marks),
            FadeOut(desc1), FadeOut(desc2), FadeOut(desc3),
            FadeOut(question),
            run_time=0.4,
        )

        # ── 公式 ──
        formula_line = MathTex(r"5 + 2 - 3", font_size=64, color=WHITE)
        formula_line.move_to(UP * 2.5)
        self.play(Write(formula_line), run_time=0.6)
        self.wait(0.3)

        rule_txt = Text("从左往右依次计算", font="Noto Sans CJK SC", font_size=24, color=COLOR_RULE)
        rule_txt.move_to(UP * 1.5)
        arrow_lr = Arrow(LEFT * 2.5, RIGHT * 2.5, color=COLOR_RULE, buff=0)
        arrow_lr.move_to(UP * 1.0)
        self.play(FadeIn(rule_txt), Create(arrow_lr), run_time=0.5)

        # 步骤 1: 5 + 2 = 7
        step1_label = Text("第一步：5 + 2", font="Noto Sans CJK SC", font_size=26, color=COLOR_PRIMARY)
        step1_label.move_to(UP * 0.1)
        self.play(Write(step1_label), run_time=0.5)

        bracket1 = Brace(formula_line[0][0:3], direction=DOWN, color=COLOR_PRIMARY)
        bracket1_label = MathTex(r"= 7", font_size=48, color=COLOR_PRIMARY)
        bracket1_label.next_to(bracket1, DOWN, buff=0.15)
        self.play(GrowFromCenter(bracket1), Write(bracket1_label), run_time=0.6)
        self.wait(0.5)

        # 步骤 2: 7 - 3 = 4
        step2_label = Text("第二步：7 - 3", font="Noto Sans CJK SC", font_size=26, color=COLOR_ACCENT)
        step2_label.next_to(step1_label, DOWN, buff=0.2)
        self.play(Write(step2_label), run_time=0.5)

        step2_calc = MathTex(r"7 - 3 = 4", font_size=48, color=COLOR_ACCENT)
        step2_calc.next_to(step2_label, DOWN, buff=0.2)
        self.play(Write(step2_calc), run_time=0.5)
        self.wait(0.5)

        # 完整等式
        full_eq = MathTex(r"5 + 2 - 3 = 4", font_size=64, color=COLOR_RESULT)
        full_eq.move_to(DOWN * 2.5)
        self.play(Write(full_eq), run_time=0.7)
        self.play(Indicate(full_eq, color=COLOR_RESULT, scale_factor=1.15), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(sec_title),
            FadeOut(formula_line),
            FadeOut(rule_txt), FadeOut(arrow_lr),
            FadeOut(step1_label), FadeOut(bracket1), FadeOut(bracket1_label),
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(full_eq),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 5: 规则总结
    # ─────────────────────────────────────────────
    def scene_5_rule_summary(self):
        # 总结标题
        sum_title = Text("计算规则总结", font="Noto Sans CJK SC", font_size=36, color=COLOR_TITLE)
        sum_title.move_to(UP * 5.8)
        self.play(Write(sum_title), run_time=0.6)

        # 黄金规则
        rule_box = RoundedRectangle(
            width=7.5, height=1.3, corner_radius=0.3,
            color=COLOR_ACCENT, fill_color=COLOR_ACCENT, fill_opacity=0.15, stroke_width=2,
        )
        rule_box.move_to(UP * 4.5)

        rule_text = Text("从左往右依次计算", font="Noto Sans CJK SC", font_size=32, color=COLOR_ACCENT)
        rule_text.move_to(rule_box.get_center())

        self.play(Create(rule_box), Write(rule_text), run_time=0.6)
        self.wait(0.3)

        # 三个公式展示
        formulas_data = [
            (r"2 + 3 + 1 = 6", "连  加", COLOR_SECONDARY),
            (r"5 - 2 - 1 = 2", "连  减", COLOR_DANGER),
            (r"5 + 2 - 3 = 4", "加减混合", COLOR_PRIMARY),
        ]

        cards = VGroup()
        for i, (formula, label_str, col) in enumerate(formulas_data):
            # 卡片背景
            card_bg = RoundedRectangle(
                width=7.2, height=1.5, corner_radius=0.25,
                color=col, fill_color=col, fill_opacity=0.12, stroke_width=1.5,
            )
            # 类型标签
            type_label = Text(label_str, font="Noto Sans CJK SC", font_size=20, color=col)
            type_label.move_to(card_bg.get_left() + RIGHT * 1.0)
            # 公式
            formula_tex = MathTex(formula, font_size=38, color=WHITE)
            formula_tex.move_to(card_bg.get_center() + RIGHT * 1.2)

            card = VGroup(card_bg, type_label, formula_tex)
            card.move_to(UP * (2.8 - i * 1.8))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=LEFT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(0.8)

        # 强调大箭头
        big_arrow = Arrow(LEFT * 3.5, RIGHT * 3.5, color=COLOR_ARROW, buff=0, stroke_width=6)
        big_arrow.move_to(DOWN * 2.8)
        arrow_label = Text("从左到右！", font="Noto Sans CJK SC", font_size=26, color=COLOR_ARROW)
        arrow_label.next_to(big_arrow, DOWN, buff=0.25)

        self.play(GrowArrow(big_arrow), run_time=0.6)
        self.play(FadeIn(arrow_label, scale=1.1), run_time=0.4)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(sum_title),
            FadeOut(rule_box), FadeOut(rule_text),
            FadeOut(cards),
            FadeOut(big_arrow), FadeOut(arrow_label),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 6: 片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color="#9e9e9e",
        ).move_to(UP * 0.6)

        self.play(Transform(self.author_tag, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=COLOR_ACCENT,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 装饰：三个算式闪现
        deco_formulas = VGroup(
            MathTex(r"2+3+1=6", font_size=28, color=COLOR_SECONDARY),
            MathTex(r"5-2-1=2", font_size=28, color=COLOR_DANGER),
            MathTex(r"5+2-3=4", font_size=28, color=COLOR_PRIMARY),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 2.5)

        self.play(FadeIn(deco_formulas, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_tag),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_formulas),
            run_time=0.8,
        )
        self.wait(0.5)
