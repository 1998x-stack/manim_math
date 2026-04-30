"""
反证法 (Proof by Contradiction) - Manim 教学动画
八年级第一学期第十九章 - 几何证明

作者: 上海初高中数学直通车 @emptyandcalm
格式: TikTok 竖屏 1080×1920
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
BG_COLOR          = "#1a1a2e"
COLOR_TITLE       = "#FFD700"
COLOR_STEP1       = "#FF6B6B"    # 红 - 假设/否定
COLOR_STEP2       = "#FFA07A"    # 橙 - 推导/矛盾
COLOR_STEP3       = "#90EE90"    # 绿 - 结论
COLOR_ARROW       = "#87CEEB"    # 天蓝 - 箭头
COLOR_HIGHLIGHT   = "#FFD700"
COLOR_BODY        = "#E0E0E0"
COLOR_CONTRADICT  = "#FF3333"    # 矛盾！深红
COLOR_BOX1        = "#3D1515"    # Step1 框背景
COLOR_BOX2        = "#3D2A10"    # Step2 框背景
COLOR_BOX3        = "#153D15"    # Step3 框背景
COLOR_CARD_BORDER = "#555577"

FONT = "PingFang SC"


class ProofByContradiction(Scene):
    """
    反证法 完整教学动画
    场景：
    1. 开场钩子
    2. 概念介绍
    3. 三步骤图解
    4. 例题演示
    5. 口诀总结
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 持久作者信息
        self.author_bar = self._make_author_bar()

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_concept()
        self.scene_3_steps()
        self.scene_4_example()
        self.scene_5_summary()
        self.scene_6_outro()

    # ========================================================
    # Helper: 作者条
    # ========================================================
    def _make_author_bar(self):
        bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT,
            font_size=18,
            color=GRAY_B,
        ).move_to(UP * 7.2)
        return bar

    def _show_author(self):
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.15), run_time=0.35)

    # ========================================================
    # Scene 1: 开场钩子 (~5 秒)
    # ========================================================
    def scene_1_hook(self):
        self._show_author()

        # 钩子文字
        hook1 = Text(
            "想证明一件事成立…",
            font=FONT, font_size=30, color=COLOR_BODY
        ).move_to(UP * 5.0)

        hook2 = Text(
            "先假设它 不成立！",
            font=FONT, font_size=34, color=COLOR_STEP1
        ).move_to(UP * 3.8)

        # 大标题
        title_cn = Text(
            "反  证  法",
            font=FONT, font_size=60, color=COLOR_TITLE,
            weight=BOLD,
        ).move_to(UP * 2.0)

        title_en = Text(
            "Proof by Contradiction",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 1.0)

        grade_tag = Text(
            "八年级  ·  第十九章",
            font=FONT, font_size=20, color=GRAY_B,
        ).move_to(UP * 0.2)

        # 装饰线
        deco_line = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_TITLE, stroke_width=2)
        deco_line.move_to(UP * 1.55)

        self.play(Write(hook1), run_time=0.9)
        self.play(Write(hook2), run_time=0.9)
        self.wait(0.3)
        self.play(GrowFromCenter(title_cn), run_time=0.8)
        self.play(
            FadeIn(deco_line),
            FadeIn(title_en),
            FadeIn(grade_tag),
            run_time=0.5,
        )
        self.wait(1.0)

        # 淡出清场
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(title_cn), FadeOut(title_en),
            FadeOut(grade_tag), FadeOut(deco_line),
            run_time=0.5,
        )

    # ========================================================
    # Scene 2: 概念介绍 (~6 秒)
    # ========================================================
    def scene_2_concept(self):
        subtitle = Text(
            "什么是反证法？",
            font=FONT, font_size=38, color=COLOR_TITLE,
        ).move_to(UP * 5.5)

        # 正向思维 vs 反向思维图示
        label_direct = Text("直接证明", font=FONT, font_size=24, color=GRAY_A)
        label_contra  = Text("反证法", font=FONT, font_size=24, color=COLOR_STEP1)

        arrow_direct = Arrow(
            LEFT * 2.5, RIGHT * 2.5,
            color=GRAY_A, stroke_width=4, buff=0
        )
        arrow_contra = Arrow(
            RIGHT * 2.5, LEFT * 2.5,
            color=COLOR_STEP1, stroke_width=4, buff=0
        )

        # 端点标签
        goal_dot  = Dot(LEFT * 2.5, color=GRAY_A, radius=0.12)
        goal_txt  = Text("假设P成立", font=FONT, font_size=20, color=GRAY_A).next_to(goal_dot, LEFT, buff=0.15)
        result_dot = Dot(RIGHT * 2.5, color=GRAY_A, radius=0.12)
        result_txt = Text("Q成立", font=FONT, font_size=20, color=GRAY_A).next_to(result_dot, RIGHT, buff=0.15)

        neg_goal_dot  = Dot(RIGHT * 2.5, color=COLOR_STEP1, radius=0.12)
        neg_goal_txt  = Text("假设P不成立", font=FONT, font_size=20, color=COLOR_STEP1).next_to(neg_goal_dot, RIGHT, buff=0.15)
        contradict_dot = Dot(LEFT * 2.5, color=COLOR_CONTRADICT, radius=0.12)
        contradict_txt = Text("矛盾！", font=FONT, font_size=20, color=COLOR_CONTRADICT).next_to(contradict_dot, LEFT, buff=0.15)

        # 布局
        group_direct = VGroup(
            goal_dot, goal_txt, arrow_direct, result_dot, result_txt
        ).move_to(UP * 3.5)
        label_direct.next_to(group_direct, UP, buff=0.2)

        group_contra = VGroup(
            neg_goal_dot, neg_goal_txt, arrow_contra, contradict_dot, contradict_txt
        ).move_to(UP * 1.5)
        label_contra.next_to(group_contra, UP, buff=0.2)

        # 定义文字
        def_text = Text(
            "通过推出矛盾来反证原命题成立",
            font=FONT, font_size=24, color=COLOR_BODY,
        ).move_to(DOWN * 0.3)

        self.play(Write(subtitle), run_time=0.6)
        self.play(FadeIn(label_direct), Create(group_direct), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(label_contra), Create(group_contra), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(def_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(subtitle), FadeOut(label_direct), FadeOut(group_direct),
            FadeOut(label_contra), FadeOut(group_contra), FadeOut(def_text),
            run_time=0.5,
        )

    # ========================================================
    # Helper: 步骤框
    # ========================================================
    def _make_step_box(self, number_str, title_str, body_str,
                       box_color, fill_color, y_pos):
        """创建编号步骤框"""
        # 数字圆圈
        num_circle = Circle(radius=0.35, color=box_color,
                            fill_color=box_color, fill_opacity=1)
        num_text = Text(number_str, font=FONT, font_size=24,
                        color=WHITE, weight=BOLD)
        num_group = VGroup(num_circle, num_text).move_to(ORIGIN)
        num_text.move_to(num_circle.get_center())

        # 标题
        title = Text(title_str, font=FONT, font_size=26,
                     color=box_color, weight=BOLD)
        # 正文
        body = Text(body_str, font=FONT, font_size=20, color=COLOR_BODY)

        # 组合
        content = VGroup(title, body).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        row = VGroup(num_group, content).arrange(RIGHT, buff=0.35, aligned_edge=UP)

        # 背景框
        bg = RoundedRectangle(
            width=7.8, height=row.get_height() + 0.5,
            corner_radius=0.3,
            color=box_color, fill_color=fill_color,
            fill_opacity=1, stroke_width=2,
        )

        row.move_to(bg.get_center())
        group = VGroup(bg, row).move_to(np.array([0, y_pos, 0]))
        return group

    # ========================================================
    # Scene 3: 三步骤图解 (~15 秒)
    # ========================================================
    def scene_3_steps(self):
        section_title = Text(
            "反证法三步骤",
            font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 6.5)

        # 三个步骤框
        box1 = self._make_step_box(
            "1", "假设结论不成立",
            "否定要证明的结论（否定P）",
            COLOR_STEP1, COLOR_BOX1, 4.0
        )
        box2 = self._make_step_box(
            "2", "逻辑推理得矛盾",
            "由假设出发，推出与已知矛盾的结论",
            COLOR_STEP2, COLOR_BOX2, 1.0
        )
        box3 = self._make_step_box(
            "3", "原结论成立",
            "矛盾说明假设错误，∴ 结论正确",
            COLOR_STEP3, COLOR_BOX3, -2.0
        )

        # 连接箭头
        arrow1 = Arrow(
            UP * 2.5, UP * 1.8,
            color=COLOR_ARROW, stroke_width=5,
            max_tip_length_to_length_ratio=0.25, buff=0,
        )
        arrow2 = Arrow(
            DOWN * 0.5, DOWN * 1.2,
            color=COLOR_ARROW, stroke_width=5,
            max_tip_length_to_length_ratio=0.25, buff=0,
        )

        # 动画
        self.play(Write(section_title), run_time=0.5)
        self.play(FadeIn(box1, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(0.6)

        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(box2, shift=RIGHT * 0.3), run_time=0.8)

        # 矛盾闪烁效果
        bang_text = Text("矛盾！", font=FONT, font_size=32,
                         color=COLOR_CONTRADICT, weight=BOLD)
        bang_text.move_to(np.array([2.5, 1.0, 0]))
        cross = Cross(bang_text, color=COLOR_CONTRADICT, stroke_width=4)

        self.play(FadeIn(bang_text), run_time=0.4)
        self.play(
            bang_text.animate.scale(1.3).set_color(RED),
            run_time=0.3,
        )
        self.play(
            bang_text.animate.scale(1/1.3).set_color(COLOR_CONTRADICT),
            run_time=0.3,
        )
        self.wait(0.4)
        self.play(FadeOut(bang_text), run_time=0.3)

        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(FadeIn(box3, shift=RIGHT * 0.3), run_time=0.8)

        # 对勾动效
        check = Text("✓", font=FONT, font_size=40, color=COLOR_STEP3)
        check.move_to(np.array([2.8, -2.0, 0]))
        self.play(GrowFromCenter(check), run_time=0.5)
        self.play(
            check.animate.scale(1.3),
            run_time=0.25,
        )
        self.play(
            check.animate.scale(1/1.3),
            run_time=0.25,
        )

        self.wait(2.0)

        # 整体高亮回顾
        self.play(
            box1.animate.set_stroke(COLOR_STEP1, width=4),
            run_time=0.4,
        )
        self.wait(0.3)
        self.play(
            box2.animate.set_stroke(COLOR_STEP2, width=4),
            run_time=0.4,
        )
        self.wait(0.3)
        self.play(
            box3.animate.set_stroke(COLOR_STEP3, width=4),
            run_time=0.4,
        )
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(section_title),
            FadeOut(box1), FadeOut(box2), FadeOut(box3),
            FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(check),
            run_time=0.6,
        )

    # ========================================================
    # Scene 4: 例题演示 (~25 秒)
    # ========================================================
    def scene_4_example(self):
        # ---- 题目 ----
        example_label = Text(
            "例题",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT, weight=BOLD,
        ).move_to(UP * 6.5)

        prob_line1 = Text(
            "已知：n² 是偶数",
            font=FONT, font_size=26, color=COLOR_BODY,
        ).move_to(UP * 5.5)
        prob_line2 = Text(
            "求证：n 也是偶数",
            font=FONT, font_size=26, color=COLOR_BODY,
        ).move_to(UP * 4.8)

        self.play(Write(example_label), run_time=0.4)
        self.play(FadeIn(prob_line1), FadeIn(prob_line2), run_time=0.7)
        self.wait(0.8)

        # ---- Step 1 ----
        tag1 = Text("【第1步】假设结论不成立",
                    font=FONT, font_size=24, color=COLOR_STEP1, weight=BOLD)
        tag1.move_to(UP * 3.5)

        step1_body = Text(
            "假设 n 不是偶数，即 n 是奇数",
            font=FONT, font_size=23, color=COLOR_BODY,
        ).move_to(UP * 2.7)

        self.play(Write(tag1), run_time=0.5)
        self.play(FadeIn(step1_body), run_time=0.5)
        self.wait(0.7)

        # ---- Step 2 ----
        tag2 = Text("【第2步】推导，寻找矛盾",
                    font=FONT, font_size=24, color=COLOR_STEP2, weight=BOLD)
        tag2.move_to(UP * 1.6)

        deduction1 = Text(
            "设 n = 2k+1（k 为整数）",
            font=FONT, font_size=22, color=COLOR_BODY,
        ).move_to(UP * 0.8)

        formula_a = MathTex(
            r"n^2 = (2k+1)^2 = 4k^2 + 4k + 1",
            font_size=28, color=COLOR_BODY,
        ).move_to(UP * 0.0)

        formula_b = MathTex(
            r"= 2(2k^2 + 2k) + 1",
            font_size=28, color=COLOR_STEP2,
        ).move_to(DOWN * 0.7)

        self.play(Write(tag2), run_time=0.5)
        self.play(FadeIn(deduction1), run_time=0.5)
        self.play(Write(formula_a), run_time=0.9)
        self.play(Write(formula_b), run_time=0.7)
        self.wait(0.5)

        # n² 是奇数 → 矛盾！
        odd_text = Text(
            "∴ n² 是奇数",
            font=FONT, font_size=25, color=COLOR_STEP2,
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(odd_text), run_time=0.5)
        self.wait(0.4)

        # 矛盾爆炸效果
        contradict_box = RoundedRectangle(
            width=6.0, height=0.8,
            corner_radius=0.25,
            color=COLOR_CONTRADICT,
            fill_color="#4A0000",
            fill_opacity=1,
            stroke_width=3,
        ).move_to(DOWN * 2.5)

        contradict_text = Text(
            "矛盾！n² 已知是偶数",
            font=FONT, font_size=24, color=WHITE, weight=BOLD,
        ).move_to(DOWN * 2.5)

        self.play(
            GrowFromCenter(contradict_box),
            run_time=0.5,
        )
        self.play(Write(contradict_text), run_time=0.5)
        self.play(
            contradict_box.animate.set_stroke(RED, width=5),
            contradict_text.animate.set_color(COLOR_CONTRADICT),
            run_time=0.4,
        )
        self.play(
            contradict_box.animate.set_stroke(COLOR_CONTRADICT, width=3),
            contradict_text.animate.set_color(WHITE),
            run_time=0.3,
        )
        self.wait(0.8)

        # ---- Step 3 ----
        tag3 = Text("【第3步】得出结论",
                    font=FONT, font_size=24, color=COLOR_STEP3, weight=BOLD)
        tag3.move_to(DOWN * 3.5)

        conclusion = Text(
            "假设不成立，∴ n 是偶数  ✓",
            font=FONT, font_size=26, color=COLOR_STEP3, weight=BOLD,
        ).move_to(DOWN * 4.4)

        self.play(Write(tag3), run_time=0.5)
        self.play(
            GrowFromCenter(conclusion),
            run_time=0.6,
        )

        # 闪光效果
        self.play(
            conclusion.animate.set_color(COLOR_HIGHLIGHT),
            run_time=0.3,
        )
        self.play(
            conclusion.animate.set_color(COLOR_STEP3),
            run_time=0.3,
        )
        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(example_label),
            FadeOut(prob_line1), FadeOut(prob_line2),
            FadeOut(tag1), FadeOut(step1_body),
            FadeOut(tag2), FadeOut(deduction1),
            FadeOut(formula_a), FadeOut(formula_b),
            FadeOut(odd_text),
            FadeOut(contradict_box), FadeOut(contradict_text),
            FadeOut(tag3), FadeOut(conclusion),
            run_time=0.6,
        )

    # ========================================================
    # Scene 5: 口诀总结 (~5 秒)
    # ========================================================
    def scene_5_summary(self):
        summ_title = Text(
            "口诀记忆",
            font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 5.5)

        # 三行口诀，颜色对应三步
        mnem1 = Text("假设否定（反其道）",
                     font=FONT, font_size=30, color=COLOR_STEP1)
        mnem2 = Text("推出矛盾（找破绽）",
                     font=FONT, font_size=30, color=COLOR_STEP2)
        mnem3 = Text("反推结论（真相现）",
                     font=FONT, font_size=30, color=COLOR_STEP3)

        mnems = VGroup(mnem1, mnem2, mnem3).arrange(DOWN, buff=0.55)
        mnems.move_to(UP * 2.5)

        # 分隔线
        line_top = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_C, stroke_width=1.5)
        line_top.next_to(mnems, UP, buff=0.4)
        line_bot = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_C, stroke_width=1.5)
        line_bot.next_to(mnems, DOWN, buff=0.4)

        key_point = Text(
            "间接证明 = 用矛盾说话",
            font=FONT, font_size=26, color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.0)

        self.play(Write(summ_title), run_time=0.5)
        self.play(Create(line_top), run_time=0.3)
        for line in [mnem1, mnem2, mnem3]:
            self.play(FadeIn(line, shift=RIGHT * 0.4), run_time=0.5)
        self.play(Create(line_bot), run_time=0.3)
        self.play(FadeIn(key_point, scale=1.1), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(summ_title),
            FadeOut(line_top), FadeOut(line_bot),
            FadeOut(mnem1), FadeOut(mnem2), FadeOut(mnem3),
            FadeOut(key_point),
            run_time=0.5,
        )

    # ========================================================
    # Scene 6: 片尾关注 (~4 秒)
    # ========================================================
    def scene_6_outro(self):
        # 作者信息放大版
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=GRAY_B,
        ).move_to(UP * 0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)

        # 三个图标点 - 对应三步颜色
        dots = VGroup(
            Dot(LEFT * 1.2, color=COLOR_STEP1, radius=0.18),
            Dot(ORIGIN,     color=COLOR_STEP2, radius=0.18),
            Dot(RIGHT * 1.2, color=COLOR_STEP3, radius=0.18),
        ).move_to(DOWN * 1.8)

        # 移除持久作者条
        self.play(FadeOut(self.author_bar), run_time=0.3)

        self.play(
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.6,
        )
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(
            FadeIn(follow_text, shift=UP * 0.2),
            run_time=0.5,
        )
        self.play(
            *[GrowFromCenter(d) for d in dots],
            run_time=0.5,
        )
        self.play(Rotate(dots, angle=PI * 0.5, run_time=1.0))
        self.wait(1.0)

# # 快速预览
# manim -pql fanzhengfa.py ProofByContradiction

# # 高质量输出
# manim -qh fanzhengfa.py ProofByContradiction