"""
分数的简单计算 - 三年级下册 第四章
同分母分数加减法教学动画

内容:
  - 同分母分数加法: 1/3 + 2/3 = 1
  - 用"1"的转化进行减法: 1 - 2/5 = 5/5 - 2/5 = 3/5
  - 规则总结: 分母不变，分子相加减

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

# 颜色配置
COLOR_BG = "#1a1a2e"
COLOR_PRIMARY = "#4ecdc4"       # 主色调 - 青绿
COLOR_SECONDARY = "#ff6b6b"     # 强调色 - 红
COLOR_ACCENT = "#ffd93d"        # 高亮 - 黄
COLOR_NUMERATOR = "#ff6b6b"     # 分子色
COLOR_DENOMINATOR = "#4ecdc4"   # 分母色
COLOR_HIGHLIGHT = "#ffd93d"     # 高亮色
COLOR_DIM = "#6b7280"           # 暗色文字


class SimpleFractionCalcLesson(Scene):
    """
    分数的简单计算教学动画

    场景顺序:
    1. 开场钩子
    2. 分数单位回顾
    3. 同分母加法: 1/3 + 2/3 = 1（饼图演示）
    4. 加法运算步骤（算理分解）
    5. 规则归纳: 分母不变，分子相加
    6. 1的转化: 1 = 5/5
    7. 减法可视化（饼图）
    8. 减法运算步骤
    9. 综合规则总结
    10. 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        # 作者信息（全程保留）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=COLOR_DIM
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        self.scene_01_hook()
        self.scene_02_fraction_unit_review()
        self.scene_03_addition_visual()
        self.scene_04_addition_steps()
        self.scene_05_rule_addition()
        self.scene_06_one_transform()
        self.scene_07_subtraction_visual()
        self.scene_08_subtraction_steps()
        self.scene_09_summary()
        self.scene_10_outro()

    # ─────────────────────────────────────────────────────────
    # 辅助函数
    # ─────────────────────────────────────────────────────────

    def make_pie_sector(self, center, radius, start_angle, end_angle,
                        fill_color, fill_opacity=0.85, stroke_color=WHITE,
                        stroke_width=2):
        """创建扇形（饼图的一个扇区）"""
        angle = end_angle - start_angle
        sector = Sector(
            radius=radius,
            start_angle=start_angle,
            angle=angle,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width
        )
        sector.move_to(center)
        return sector

    def make_circle_pie(self, center, radius, n_parts, filled_parts,
                        filled_color="#ff6b6b", empty_color="#2d3561",
                        stroke_color=WHITE, stroke_width=2):
        """创建n等分饼图，filled_parts个为填充色"""
        sectors = VGroup()
        angle_per_part = TAU / n_parts
        for i in range(n_parts):
            start = PI / 2 - i * angle_per_part  # 从顶部开始，顺时针
            color = filled_color if i < filled_parts else empty_color
            s = self.make_pie_sector(
                center, radius, start - angle_per_part, start,
                fill_color=color,
                stroke_color=stroke_color,
                stroke_width=stroke_width
            )
            sectors.add(s)
        return sectors

    def clear_scene_objects(self, *objects, run_time=0.5):
        """批量淡出元素"""
        valid = [obj for obj in objects if obj is not None]
        if valid:
            self.play(*[FadeOut(obj) for obj in valid], run_time=run_time)

    # ─────────────────────────────────────────────────────────
    # Scene 01: 开场钩子
    # ─────────────────────────────────────────────────────────

    def scene_01_hook(self):
        # 主标题
        title = Text(
            "分数也能加减法？",
            font="PingFang SC",
            font_size=48,
            color=COLOR_ACCENT,
            weight=BOLD
        ).move_to(UP * 5.5)

        subtitle = Text(
            "分母不变，分子相加减！",
            font="PingFang SC",
            font_size=30,
            color=COLOR_PRIMARY
        ).move_to(UP * 4.5)

        # 展示一个分数加法问题作为钩子
        hook_formula = MathTex(
            r"\frac{1}{3} + \frac{2}{3} = \, ?",
            font_size=72,
            color=WHITE
        ).move_to(UP * 2.5)

        # 装饰线
        line1 = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_PRIMARY, stroke_width=2)
        line1.move_to(UP * 4.1)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=DOWN * 0.3), run_time=0.5)
        self.play(Create(line1), run_time=0.4)
        self.play(Write(hook_formula), run_time=1.0)
        self.wait(1.0)

        # 用饼图直观展示
        pie_center = DOWN * 0.5
        pie = self.make_circle_pie(pie_center, 1.3, 3, 0,
                                   filled_color=COLOR_SECONDARY,
                                   empty_color="#2d3561")
        self.play(Create(pie), run_time=0.8)

        # 逐块填充
        self.play(pie[0].animate.set_fill(COLOR_PRIMARY, opacity=0.9), run_time=0.4)
        self.play(
            pie[1].animate.set_fill(COLOR_ACCENT, opacity=0.9),
            pie[2].animate.set_fill(COLOR_ACCENT, opacity=0.9),
            run_time=0.4
        )

        hint = Text(
            "看！拼在一起就是 1 个整体！",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.3)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.clear_scene_objects(title, subtitle, line1, hook_formula,
                                 pie, hint, run_time=0.6)

    # ─────────────────────────────────────────────────────────
    # Scene 02: 分数单位回顾
    # ─────────────────────────────────────────────────────────

    def scene_02_fraction_unit_review(self):
        sec_title = Text(
            "回顾：分数单位",
            font="PingFang SC",
            font_size=36,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.0)

        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # 展示 1/5 的意义：5等分，取1份
        explain1 = Text(
            "把整体平均分成 5 份",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.8)

        explain2_left = Text(
            "每份就是",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        frac_unit = MathTex(r"\frac{1}{5}", font_size=40, color=COLOR_ACCENT)
        explain2_group = VGroup(explain2_left, frac_unit).arrange(RIGHT, buff=0.15)
        explain2_group.move_to(UP * 4.0)

        self.play(Write(explain1), run_time=0.6)
        self.play(FadeIn(explain2_group), run_time=0.5)

        # 饼图展示 5 等分
        pie_center = UP * 1.5
        pie5 = self.make_circle_pie(pie_center, 1.5, 5, 1,
                                    filled_color=COLOR_ACCENT,
                                    empty_color="#2d3561")
        self.play(Create(pie5), run_time=0.8)

        # 标注分数单位
        unit_label = MathTex(r"\frac{1}{5}", font_size=32, color=COLOR_ACCENT)
        unit_label.move_to(pie_center + np.array([-1.0, 0.9, 0]))
        arrow = Arrow(
            unit_label.get_right() + RIGHT * 0.05,
            pie_center + np.array([-0.55, 0.35, 0]),
            color=COLOR_ACCENT, stroke_width=2, buff=0.05,
            max_tip_length_to_length_ratio=0.3
        )
        self.play(FadeIn(unit_label), Create(arrow), run_time=0.5)
        self.wait(0.5)

        # 继续: 3个1/5
        explain3_a = Text(
            "3 个",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        frac3 = MathTex(r"\frac{1}{5}", font_size=36, color=COLOR_ACCENT)
        is_text = Text(
            "合在一起就是",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        frac35 = MathTex(r"\frac{3}{5}", font_size=40, color=COLOR_PRIMARY)
        explain3_group = VGroup(explain3_a, frac3, is_text, frac35).arrange(RIGHT, buff=0.1)
        explain3_group.move_to(DOWN * 0.5)

        # 再填2份
        self.play(
            pie5[1].animate.set_fill(COLOR_ACCENT, opacity=0.9),
            pie5[2].animate.set_fill(COLOR_ACCENT, opacity=0.9),
            run_time=0.6
        )
        self.play(FadeIn(explain3_group), run_time=0.6)
        self.wait(1.0)

        # 关键结论
        conclusion = Text(
            "分子 = 有几个分数单位",
            font="PingFang SC",
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.8)
        box = SurroundingRectangle(conclusion, color=COLOR_HIGHLIGHT,
                                   corner_radius=0.15, buff=0.2)
        self.play(Write(conclusion), Create(box), run_time=0.6)
        self.wait(1.2)

        self.clear_scene_objects(sec_title, explain1, explain2_group,
                                 pie5, unit_label, arrow, explain3_group,
                                 conclusion, box, run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 03: 加法可视化（饼图）
    # ─────────────────────────────────────────────────────────

    def scene_03_addition_visual(self):
        sec_title = Text(
            "同分母加法",
            font="PingFang SC",
            font_size=38,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.2)

        formula_title = MathTex(
            r"\frac{1}{3} + \frac{2}{3} = \, ?",
            font_size=56,
            color=WHITE
        ).move_to(UP * 5.1)

        self.play(FadeIn(sec_title), run_time=0.4)
        self.play(Write(formula_title), run_time=0.8)

        # 饼图 1: 1/3（左边）
        left_center = np.array([-2.5, 2.0, 0])
        pie_left = self.make_circle_pie(left_center, 1.1, 3, 1,
                                        filled_color=COLOR_PRIMARY,
                                        empty_color="#2d3561")
        label_left = MathTex(r"\frac{1}{3}", font_size=40, color=COLOR_PRIMARY)
        label_left.next_to(pie_left, DOWN, buff=0.3)

        # 饼图 2: 2/3（右边）
        right_center = np.array([2.5, 2.0, 0])
        pie_right = self.make_circle_pie(right_center, 1.1, 3, 2,
                                         filled_color=COLOR_ACCENT,
                                         empty_color="#2d3561")
        label_right = MathTex(r"\frac{2}{3}", font_size=40, color=COLOR_ACCENT)
        label_right.next_to(pie_right, DOWN, buff=0.3)

        plus_sign = MathTex(r"+", font_size=56, color=WHITE).move_to(np.array([0, 2.0, 0]))

        self.play(Create(pie_left), Create(pie_right), run_time=0.8)
        self.play(Write(label_left), Write(label_right), run_time=0.5)
        self.play(FadeIn(plus_sign), run_time=0.3)
        self.wait(0.5)

        # 合并动画：两个饼图向中间合并
        combined_center = np.array([0, 0.0, 0])
        combined_pie = self.make_circle_pie(combined_center, 1.4, 3, 3,
                                            filled_color=COLOR_PRIMARY,
                                            empty_color=COLOR_PRIMARY)
        # 三份用不同颜色
        combined_pie[0].set_fill(COLOR_PRIMARY, opacity=0.9)
        combined_pie[1].set_fill(COLOR_ACCENT, opacity=0.9)
        combined_pie[2].set_fill(COLOR_ACCENT, opacity=0.9)

        combine_text = Text(
            "合并！",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(np.array([0, 3.4, 0]))

        self.play(Write(combine_text), run_time=0.4)
        self.play(
            pie_left.animate.move_to(combined_center),
            pie_right.animate.move_to(combined_center),
            FadeOut(plus_sign),
            FadeOut(label_left),
            FadeOut(label_right),
            run_time=0.8
        )
        self.play(
            FadeOut(pie_left),
            FadeOut(pie_right),
            FadeIn(combined_pie),
            FadeOut(combine_text),
            run_time=0.5
        )

        # 结果：正好是 1 个整体！
        equals_1 = MathTex(r"= \; 1", font_size=64, color=COLOR_HIGHLIGHT)
        equals_1.move_to(DOWN * 1.8)

        whole_label = Text(
            "刚好是 1 个整体！",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.8)

        self.play(Write(equals_1), run_time=0.6)
        self.play(
            Indicate(combined_pie, color=COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.6
        )
        self.play(FadeIn(whole_label, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.clear_scene_objects(sec_title, formula_title, combined_pie,
                                 equals_1, whole_label, run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 04: 加法运算步骤（算理分解）
    # ─────────────────────────────────────────────────────────

    def scene_04_addition_steps(self):
        sec_title = Text(
            "计算步骤",
            font="PingFang SC",
            font_size=36,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.2)
        self.play(FadeIn(sec_title), run_time=0.4)

        # 主算式
        main_eq = MathTex(
            r"\frac{1}{3} + \frac{2}{3}",
            font_size=60,
            color=WHITE
        ).move_to(UP * 4.8)
        self.play(Write(main_eq), run_time=0.7)
        self.wait(0.3)

        # 步骤 1: 分母相同
        step1_text = Text(
            "分母相同（都是 3）",
            font="PingFang SC",
            font_size=28,
            color=COLOR_ACCENT
        ).move_to(UP * 3.5)

        # 圈出分母（根据MathTex的实际位置做近似标记）
        den_circle_group = VGroup(
            Circle(radius=0.32, color=COLOR_ACCENT, stroke_width=3).move_to(
                main_eq.get_center() + np.array([0.38, -0.44, 0])
            ),
            Circle(radius=0.32, color=COLOR_ACCENT, stroke_width=3).move_to(
                main_eq.get_center() + np.array([2.0, -0.44, 0])
            )
        )

        self.play(Create(den_circle_group), run_time=0.5)
        self.play(Write(step1_text), run_time=0.5)
        self.wait(0.5)

        # 步骤 2: 分子相加
        step2_text = Text(
            "分子相加：1 + 2 = 3",
            font="PingFang SC",
            font_size=28,
            color=COLOR_PRIMARY
        ).move_to(UP * 2.5)
        num_add = MathTex(r"1 + 2 = 3", font_size=44, color=COLOR_PRIMARY)
        num_add.move_to(UP * 1.7)

        self.play(Write(step2_text), run_time=0.5)
        self.play(Write(num_add), run_time=0.6)
        self.wait(0.4)

        # 步骤 3: 分母不变 → 写出结果
        step3_text = Text(
            "分母不变（仍是 3）",
            font="PingFang SC",
            font_size=28,
            color=COLOR_DENOMINATOR
        ).move_to(UP * 0.8)

        # 完整算式
        full_eq = MathTex(
            r"\frac{1}{3} + \frac{2}{3} = \frac{3}{3} = 1",
            font_size=48,
            color=WHITE
        ).move_to(DOWN * 0.4)

        self.play(
            FadeOut(den_circle_group),
            Write(step3_text),
            run_time=0.5
        )
        self.play(Write(full_eq), run_time=0.9)

        # 强调整个算式
        equals_box = SurroundingRectangle(
            full_eq,
            color=COLOR_HIGHLIGHT, corner_radius=0.12, buff=0.2
        )
        self.play(Create(equals_box), run_time=0.5)

        result_note = Text(
            "分子分母相同 ➜ 等于 1",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.7)
        self.play(FadeIn(result_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        self.clear_scene_objects(sec_title, main_eq, step1_text,
                                 step2_text, num_add, step3_text,
                                 full_eq, equals_box, result_note,
                                 run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 05: 规则归纳（加法）
    # ─────────────────────────────────────────────────────────

    def scene_05_rule_addition(self):
        rule_title = Text(
            "加法规则",
            font="PingFang SC",
            font_size=38,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.2)
        self.play(FadeIn(rule_title), run_time=0.4)

        # 规则卡片
        rule_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.5, height=2.5,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 4.5)

        rule_line1 = Text(
            "同分母分数加法",
            font="PingFang SC",
            font_size=30,
            color=COLOR_ACCENT,
            weight=BOLD
        ).move_to(UP * 5.1)

        rule_line2 = Text(
            "分母不变，分子相加",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.4)

        rule_formula = MathTex(
            r"\frac{a}{n} + \frac{b}{n} = \frac{a+b}{n}",
            font_size=44,
            color=COLOR_PRIMARY
        ).move_to(UP * 3.7)

        self.play(Create(rule_box), run_time=0.5)
        self.play(Write(rule_line1), run_time=0.5)
        self.play(Write(rule_line2), run_time=0.5)
        self.play(Write(rule_formula), run_time=0.7)
        self.wait(0.5)

        # 两个练习例子
        ex_title = Text(
            "练一练",
            font="PingFang SC",
            font_size=30,
            color=COLOR_ACCENT
        ).move_to(UP * 2.5)
        self.play(Write(ex_title), run_time=0.4)

        # 例1: 2/7 + 3/7
        ex1_q = MathTex(
            r"\frac{2}{7} + \frac{3}{7} = \, ?",
            font_size=48, color=WHITE
        ).move_to(UP * 1.6)
        self.play(Write(ex1_q), run_time=0.6)
        self.wait(0.8)

        ex1_a = MathTex(
            r"= \frac{5}{7}",
            font_size=48, color=COLOR_HIGHLIGHT
        ).next_to(ex1_q, RIGHT, buff=0.3)
        self.play(Write(ex1_a), run_time=0.5)
        self.wait(0.5)

        # 例2: 3/8 + 4/8
        ex2_q = MathTex(
            r"\frac{3}{8} + \frac{4}{8} = \, ?",
            font_size=48, color=WHITE
        ).move_to(UP * 0.4)
        self.play(Write(ex2_q), run_time=0.6)
        self.wait(0.8)

        ex2_a = MathTex(
            r"= \frac{7}{8}",
            font_size=48, color=COLOR_HIGHLIGHT
        ).next_to(ex2_q, RIGHT, buff=0.3)
        self.play(Write(ex2_a), run_time=0.5)
        self.wait(1.5)

        self.clear_scene_objects(rule_title, rule_box, rule_line1, rule_line2,
                                 rule_formula, ex_title, ex1_q, ex1_a,
                                 ex2_q, ex2_a, run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 06: 1 的转化
    # ─────────────────────────────────────────────────────────

    def scene_06_one_transform(self):
        transform_title = Text(
            "关键技巧：1 的变身",
            font="PingFang SC",
            font_size=36,
            color=COLOR_ACCENT
        ).move_to(UP * 6.2)
        self.play(Write(transform_title), run_time=0.6)

        # 引入问题
        question = Text(
            "如果要计算",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.0)
        q_formula = MathTex(
            r"1 - \frac{2}{5}",
            font_size=60,
            color=WHITE
        ).move_to(UP * 4.0)

        self.play(FadeIn(question), run_time=0.4)
        self.play(Write(q_formula), run_time=0.7)
        self.wait(0.5)

        dilemma = Text(
            "分母不同，怎么减？",
            font="PingFang SC",
            font_size=28,
            color=COLOR_SECONDARY
        ).move_to(UP * 3.0)
        self.play(FadeIn(dilemma, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 转化思路
        idea_text = Text(
            "把 1 变成和 2/5 分母相同的分数！",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 1.9)
        self.play(Write(idea_text), run_time=0.6)

        # 大展示：1 = 5/5
        transform_eq = MathTex(
            r"1 = \frac{5}{5}",
            font_size=72,
            color=COLOR_ACCENT
        ).move_to(UP * 0.5)

        box_transform = SurroundingRectangle(
            transform_eq,
            color=COLOR_ACCENT, corner_radius=0.2, buff=0.3
        )

        self.play(Write(transform_eq), run_time=0.8)
        self.play(Create(box_transform), run_time=0.4)
        self.play(Indicate(transform_eq, color=COLOR_HIGHLIGHT, scale_factor=1.1), run_time=0.5)
        self.wait(0.5)

        # 更多例子
        more_examples = Text(
            "同理：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.1)

        ex_list = MathTex(
            r"1 = \frac{3}{3} = \frac{4}{4} = \frac{5}{5} = \frac{6}{6} = \cdots",
            font_size=34,
            color=COLOR_PRIMARY
        ).move_to(DOWN * 2.0)

        self.play(FadeIn(more_examples), run_time=0.4)
        self.play(Write(ex_list), run_time=0.8)
        self.wait(0.5)

        key_idea = Text(
            "分子分母相同的分数 = 1",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.1)
        key_box = SurroundingRectangle(
            key_idea, color=COLOR_HIGHLIGHT, corner_radius=0.15, buff=0.18
        )
        self.play(Write(key_idea), Create(key_box), run_time=0.6)
        self.wait(1.5)

        self.clear_scene_objects(transform_title, question, q_formula,
                                 dilemma, idea_text,
                                 transform_eq, box_transform,
                                 more_examples, ex_list, key_idea, key_box,
                                 run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 07: 减法可视化（饼图）
    # ─────────────────────────────────────────────────────────

    def scene_07_subtraction_visual(self):
        sec_title = Text(
            "用图来看减法",
            font="PingFang SC",
            font_size=36,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.2)

        formula_title = MathTex(
            r"1 - \frac{2}{5} = \, ?",
            font_size=56,
            color=WHITE
        ).move_to(UP * 5.1)

        self.play(FadeIn(sec_title), run_time=0.4)
        self.play(Write(formula_title), run_time=0.7)

        # 整体饼图（5/5）
        whole_center = np.array([0, 2.3, 0])
        whole_pie = self.make_circle_pie(whole_center, 1.3, 5, 5,
                                         filled_color=COLOR_PRIMARY,
                                         empty_color="#2d3561")

        whole_label_a = Text(
            "1 个整体（5 个",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        whole_label_frac = MathTex(r"\frac{1}{5}", font_size=28, color=COLOR_PRIMARY)
        whole_label_b = Text(
            "）",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        whole_label_group = VGroup(whole_label_a, whole_label_frac, whole_label_b).arrange(RIGHT, buff=0.08)
        whole_label_group.next_to(whole_pie, DOWN, buff=0.3)

        self.play(Create(whole_pie), run_time=0.7)
        self.play(FadeIn(whole_label_group), run_time=0.4)
        self.wait(0.5)

        # 标记要去掉的 2/5
        remove_label = Text(
            "去掉 2 份",
            font="PingFang SC",
            font_size=26,
            color=COLOR_SECONDARY
        ).move_to(UP * 0.8)

        self.play(FadeIn(remove_label, shift=UP * 0.2), run_time=0.4)

        # 把 2 份变成"要去掉"的颜色
        self.play(
            whole_pie[0].animate.set_fill(COLOR_SECONDARY, opacity=0.9),
            whole_pie[1].animate.set_fill(COLOR_SECONDARY, opacity=0.9),
            run_time=0.6
        )

        # 动画：2份消失
        self.play(
            whole_pie[0].animate.set_opacity(0.2),
            whole_pie[1].animate.set_opacity(0.2),
            run_time=0.5
        )
        self.play(
            FadeOut(whole_pie[0]),
            FadeOut(whole_pie[1]),
            run_time=0.4
        )

        # 剩余 3/5
        remain_label_a = Text(
            "剩下 3 份，就是",
            font="PingFang SC",
            font_size=26,
            color=COLOR_PRIMARY
        )
        remain_frac = MathTex(r"\frac{3}{5}", font_size=40, color=COLOR_HIGHLIGHT)
        remain_group = VGroup(remain_label_a, remain_frac).arrange(RIGHT, buff=0.15)
        remain_group.move_to(DOWN * 0.2)

        self.play(FadeIn(remain_group, shift=UP * 0.2), run_time=0.5)

        # 强调结果
        result_big = MathTex(
            r"1 - \frac{2}{5} = \frac{3}{5}",
            font_size=56,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.6)
        result_box = SurroundingRectangle(result_big, color=COLOR_HIGHLIGHT,
                                          corner_radius=0.15, buff=0.2)
        self.play(Write(result_big), run_time=0.7)
        self.play(Create(result_box), run_time=0.4)
        self.play(Indicate(result_big, scale_factor=1.08), run_time=0.5)
        self.wait(1.5)

        # 清理（保留2,3,4扇区）
        self.clear_scene_objects(
            sec_title, formula_title,
            whole_pie[2], whole_pie[3], whole_pie[4],
            whole_label_group, remove_label, remain_group,
            result_big, result_box,
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 08: 减法运算步骤
    # ─────────────────────────────────────────────────────────

    def scene_08_subtraction_steps(self):
        sec_title = Text(
            "减法计算步骤",
            font="PingFang SC",
            font_size=36,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.2)
        self.play(FadeIn(sec_title), run_time=0.4)

        # 原式
        original = MathTex(
            r"1 - \frac{2}{5}",
            font_size=60,
            color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(original), run_time=0.6)

        # Step 1: 把 1 转化
        step1_label = Text(
            "第一步：把 1 变成",
            font="PingFang SC",
            font_size=26,
            color=COLOR_ACCENT
        )
        frac_one = MathTex(r"\frac{5}{5}", font_size=44, color=COLOR_ACCENT)
        step1_group = VGroup(step1_label, frac_one).arrange(RIGHT, buff=0.15)
        step1_group.move_to(UP * 3.8)

        self.play(Write(step1_group), run_time=0.6)

        # 转化后的算式
        step1_eq = MathTex(
            r"= \frac{5}{5} - \frac{2}{5}",
            font_size=54,
            color=WHITE
        ).move_to(UP * 2.8)
        self.play(Write(step1_eq), run_time=0.7)
        self.wait(0.4)

        # Step 2: 分母相同
        step2_text = Text(
            "第二步：分母相同（都是 5）",
            font="PingFang SC",
            font_size=26,
            color=COLOR_DENOMINATOR
        ).move_to(UP * 1.8)
        self.play(Write(step2_text), run_time=0.5)

        # Step 3: 分子相减
        step3_text = Text(
            "第三步：分子相减：5 - 2 = 3",
            font="PingFang SC",
            font_size=26,
            color=COLOR_NUMERATOR
        ).move_to(UP * 1.0)
        num_sub = MathTex(r"5 - 2 = 3", font_size=44, color=COLOR_NUMERATOR)
        num_sub.move_to(UP * 0.2)

        self.play(Write(step3_text), run_time=0.5)
        self.play(Write(num_sub), run_time=0.5)
        self.wait(0.4)

        # 完整算式
        final_eq = MathTex(
            r"1 - \frac{2}{5} = \frac{5}{5} - \frac{2}{5} = \frac{3}{5}",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 1.0)

        result_box = SurroundingRectangle(
            final_eq, color=COLOR_HIGHLIGHT, corner_radius=0.12, buff=0.2
        )

        self.play(Write(final_eq), run_time=0.9)
        self.play(Create(result_box), run_time=0.4)

        # 最终结论
        final_label = Text(
            "答：结果是",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        final_frac = MathTex(r"\frac{3}{5}", font_size=44, color=COLOR_HIGHLIGHT)
        final_group = VGroup(final_label, final_frac).arrange(RIGHT, buff=0.15)
        final_group.move_to(DOWN * 2.5)

        self.play(FadeIn(final_group, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.clear_scene_objects(sec_title, original, step1_group,
                                 step1_eq, step2_text, step3_text, num_sub,
                                 final_eq, result_box, final_group,
                                 run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 09: 综合规则总结
    # ─────────────────────────────────────────────────────────

    def scene_09_summary(self):
        summary_title = Text(
            "总结",
            font="PingFang SC",
            font_size=42,
            color=COLOR_ACCENT,
            weight=BOLD
        ).move_to(UP * 6.3)
        self.play(Write(summary_title), run_time=0.5)

        # 规则大卡片背景
        card_bg = RoundedRectangle(
            corner_radius=0.4,
            width=7.8, height=5.0,
            fill_color="#0f3460",
            fill_opacity=0.97,
            stroke_color=COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 3.7)

        card_head = Text(
            "同分母分数加减法",
            font="PingFang SC",
            font_size=32,
            color=COLOR_ACCENT,
            weight=BOLD
        ).move_to(UP * 5.2)

        separator = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_PRIMARY,
                         stroke_width=1.5).move_to(UP * 4.75)

        rule_text1 = Text(
            "分母不变",
            font="PingFang SC",
            font_size=30,
            color=COLOR_DENOMINATOR
        ).move_to(UP * 4.3)

        rule_text2 = Text(
            "分子相加减",
            font="PingFang SC",
            font_size=30,
            color=COLOR_NUMERATOR
        ).move_to(UP * 3.7)

        separator2 = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_PRIMARY,
                          stroke_width=1.5).move_to(UP * 3.2)

        rule_formula = MathTex(
            r"\frac{a}{n} \pm \frac{b}{n} = \frac{a \pm b}{n}",
            font_size=48,
            color=WHITE
        ).move_to(UP * 2.3)

        self.play(Create(card_bg), run_time=0.5)
        self.play(Write(card_head), run_time=0.5)
        self.play(Create(separator), run_time=0.3)
        self.play(Write(rule_text1), run_time=0.4)
        self.play(Write(rule_text2), run_time=0.4)
        self.play(Create(separator2), run_time=0.3)
        self.play(Write(rule_formula), run_time=0.7)
        self.wait(0.5)

        # 特别提示：1 的转化
        special_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5, height=2.2,
            fill_color="#16213e",
            fill_opacity=0.97,
            stroke_color=COLOR_ACCENT,
            stroke_width=2.5
        ).move_to(UP * 0.5)

        special_head = Text(
            "特别提醒",
            font="PingFang SC",
            font_size=26,
            color=COLOR_ACCENT,
            weight=BOLD
        ).move_to(UP * 0.9)

        special_rule = Text(
            "遇到整数 1，先变成同分母分数",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 0.35)

        special_ex = MathTex(
            r"1 = \frac{n}{n}",
            font_size=36,
            color=COLOR_ACCENT
        ).move_to(DOWN * 0.25)

        self.play(Create(special_bg), run_time=0.4)
        self.play(Write(special_head), run_time=0.4)
        self.play(Write(special_rule), run_time=0.5)
        self.play(Write(special_ex), run_time=0.4)
        self.wait(0.5)

        # 两个完整例子回顾
        example_title = Text(
            "例题回顾",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        self.play(Write(example_title), run_time=0.4)

        ex1 = MathTex(
            r"\frac{1}{3} + \frac{2}{3} = \frac{3}{3} = 1",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 2.5)

        ex2 = MathTex(
            r"1 - \frac{2}{5} = \frac{5}{5} - \frac{2}{5} = \frac{3}{5}",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.6)

        self.play(Write(ex1), run_time=0.7)
        self.play(Write(ex2), run_time=0.7)
        self.wait(2.5)

        self.clear_scene_objects(
            summary_title, card_bg, card_head, separator,
            rule_text1, rule_text2, separator2, rule_formula,
            special_bg, special_head, special_rule, special_ex,
            example_title, ex1, ex2,
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────
    # Scene 10: 片尾
    # ─────────────────────────────────────────────────────────

    def scene_10_outro(self):
        # 作者信息放大
        author_main = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=COLOR_DIM
        ).move_to(UP * 1.5)

        self.play(
            FadeOut(self.author_label),
            FadeIn(author_main, shift=DOWN * 0.3),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 装饰：小分数
        frac_a = MathTex(r"\frac{1}{3}", font_size=40, color=COLOR_PRIMARY).move_to(
            DOWN * 1.5 + LEFT * 2.5
        )
        frac_b = MathTex(r"\frac{2}{3}", font_size=40, color=COLOR_ACCENT).move_to(
            DOWN * 1.5
        )
        frac_c = MathTex(r"\frac{3}{5}", font_size=40, color=COLOR_SECONDARY).move_to(
            DOWN * 1.5 + RIGHT * 2.5
        )
        fracs = VGroup(frac_a, frac_b, frac_c)

        self.play(
            FadeIn(frac_a, shift=UP * 0.3),
            FadeIn(frac_b, shift=UP * 0.3),
            FadeIn(frac_c, shift=UP * 0.3),
            run_time=0.6
        )

        equals_big = MathTex(
            r"\frac{1}{3} + \frac{2}{3} = 1",
            font_size=48,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.9)
        self.play(Write(equals_big), run_time=0.7)
        self.wait(2.0)

        # 全淡出
        self.play(
            FadeOut(author_main),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(fracs),
            FadeOut(equals_big),
            run_time=1.0
        )
