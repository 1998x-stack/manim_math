"""
减法运算性质 - Subtraction Property Animation
四年级第二学期 - 第一章 复习与提高

知识点: a - b - c = a - (b + c)
目标观众: 四年级学生
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


class SubtractionPropertyLesson(Scene):
    """
    减法运算性质教学动画

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 直观演示 - 方块可视化 10-3-4
    3. 规律总结 - 字母公式
    4. 例题讲解 - 125-36-64
    5. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#4fc3f7"     # 浅蓝 - 主色
        self.COLOR_ACCENT = "#ffb74d"      # 橙色 - 强调
        self.COLOR_SUCCESS = "#81c784"     # 绿色 - 结果
        self.COLOR_FORMULA = "#ce93d8"     # 紫色 - 公式
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_REMOVE = "#ef5350"      # 红色 - 减去

        self.scene_1_opening()
        self.scene_2_visual_demo()
        self.scene_3_formula()
        self.scene_4_example()
        self.scene_5_outro()

    # ─────────────────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息（顶部固定）
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_tag, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        title = Text(
            "减法运算性质",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "四年级 · 简便计算",
            font="Noto Sans CJK SC",
            font_size=28,
            color="#9ca3af",
        ).move_to(UP * 4.5)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 钩子问题
        hook_eq = MathTex(
            r"125 - 36 - 64 = \, ?",
            font_size=50,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 2.5)

        hook_line2 = Text(
            "你能一眼算出来吗？",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 1.4)

        self.play(Write(hook_eq), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 提示"有技巧"
        tip = Text(
            "有个超简单的技巧！",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(tip, scale=1.1), run_time=0.6)
        self.wait(0.8)

        # 清理场景
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook_eq),
            FadeOut(hook_line2),
            FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 2: 直观演示（方块可视化）
    # ─────────────────────────────────────────────────────────────
    def scene_2_visual_demo(self):
        # 标题
        demo_title = Text(
            "先来看一个小例子",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 6.2)
        self.play(FadeIn(demo_title), run_time=0.5)

        # 用10个方块代表10个苹果
        total = 10
        remove_b = 3
        remove_c = 4

        block_size = 0.55
        block_gap = 0.08

        # 创建10个方块
        blocks = VGroup()
        for i in range(total):
            rect = Square(
                side_length=block_size,
                fill_color=self.COLOR_PRIMARY,
                fill_opacity=0.85,
                stroke_color=WHITE,
                stroke_width=1.5,
            )
            blocks.add(rect)

        blocks.arrange(RIGHT, buff=block_gap)
        blocks.move_to(UP * 4.2)

        # 方块上方标签
        label_10 = Text(
            "共 10 个",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE,
        ).next_to(blocks, UP, buff=0.25)

        self.play(Create(blocks), run_time=0.7)
        self.play(FadeIn(label_10), run_time=0.3)

        # ── 方法一：连续减 ──
        method1_title = Text(
            "方法一：连续减两次",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 3.0)
        self.play(FadeIn(method1_title), run_time=0.4)

        # 先减 b=3（左边3个变红并画叉）
        self.play(
            *[blocks[i].animate.set_fill(color=self.COLOR_REMOVE, opacity=0.5).set_stroke(color=self.COLOR_REMOVE)
              for i in range(remove_b)],
            run_time=0.5,
        )
        cross1 = VGroup(*[
            Line(
                blocks[i].get_corner(DL),
                blocks[i].get_corner(UR),
                color=self.COLOR_REMOVE,
                stroke_width=3,
            )
            for i in range(remove_b)
        ])
        self.play(Create(cross1), run_time=0.4)

        step1_text = VGroup(
            Text("10 - 3", font="Noto Sans CJK SC", font_size=30, color=WHITE),
        ).move_to(UP * 2.0)
        self.play(FadeIn(step1_text), run_time=0.3)
        self.wait(0.3)

        # 再减 c=4（接下来4个变橙并画叉）
        self.play(
            *[blocks[i].animate.set_fill(color=self.COLOR_ACCENT, opacity=0.5).set_stroke(color=self.COLOR_ACCENT)
              for i in range(remove_b, remove_b + remove_c)],
            run_time=0.5,
        )
        cross2 = VGroup(*[
            Line(
                blocks[i].get_corner(DL),
                blocks[i].get_corner(UR),
                color=self.COLOR_ACCENT,
                stroke_width=3,
            )
            for i in range(remove_b, remove_b + remove_c)
        ])
        self.play(Create(cross2), run_time=0.4)

        step2_text = VGroup(
            Text("10 - 3 - 4", font="Noto Sans CJK SC", font_size=30, color=WHITE),
        ).move_to(UP * 2.0)
        self.play(Transform(step1_text, step2_text), run_time=0.3)
        self.wait(0.3)

        # 剩余3个绿色高亮
        remain_idx = list(range(remove_b + remove_c, total))
        self.play(
            *[blocks[i].animate.set_fill(color=self.COLOR_SUCCESS, opacity=0.9).set_stroke(color=self.COLOR_SUCCESS)
              for i in remain_idx],
            run_time=0.4,
        )

        result1_text = VGroup(
            Text("= ", font="Noto Sans CJK SC", font_size=30, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_SUCCESS),
        ).arrange(RIGHT, buff=0.05).move_to(UP * 1.2)
        self.play(FadeIn(result1_text), run_time=0.4)
        self.wait(0.8)

        # ── 重置方块，演示方法二 ──
        self.play(
            *[blocks[i].animate.set_fill(color=self.COLOR_REMOVE, opacity=0.5).set_stroke(color=self.COLOR_REMOVE)
              for i in range(remove_b)],
            *[blocks[i].animate.set_fill(color=self.COLOR_ACCENT, opacity=0.5).set_stroke(color=self.COLOR_ACCENT)
              for i in range(remove_b, remove_b + remove_c)],
            run_time=0.3,
        )

        method2_title = Text(
            "方法二：先合并再减",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 0.3)
        self.play(FadeIn(method2_title), run_time=0.4)

        # 大括号括住 b+c 部分
        bc_group = VGroup(*[blocks[i] for i in range(remove_b + remove_c)])
        brace_bc = Brace(bc_group, direction=DOWN, color=self.COLOR_FORMULA)
        brace_label = VGroup(
            Text("3 + 4 = ", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_FORMULA),
            Text("7", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.05)
        brace_label.next_to(brace_bc, DOWN, buff=0.15)

        self.play(Create(brace_bc), run_time=0.4)
        self.play(FadeIn(brace_label), run_time=0.4)
        self.wait(0.4)

        step3_text = Text(
            "10 - (3 + 4) = 10 - 7",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
        ).move_to(DOWN * 1.2)
        result2_text = VGroup(
            Text("= ", font="Noto Sans CJK SC", font_size=30, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_SUCCESS),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 2.0)

        self.play(FadeIn(step3_text), run_time=0.4)
        self.play(FadeIn(result2_text), run_time=0.4)
        self.wait(0.5)

        # 结论
        conclude = Text(
            "两种算法，结果完全一样！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(conclude, scale=1.05), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(demo_title),
            FadeOut(blocks),
            FadeOut(label_10),
            FadeOut(cross1),
            FadeOut(cross2),
            FadeOut(step1_text),
            FadeOut(result1_text),
            FadeOut(method1_title),
            FadeOut(method2_title),
            FadeOut(brace_bc),
            FadeOut(brace_label),
            FadeOut(step3_text),
            FadeOut(result2_text),
            FadeOut(conclude),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 3: 字母公式推导
    # ─────────────────────────────────────────────────────────────
    def scene_3_formula(self):
        # 标题
        formula_title = Text(
            "规律总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 6.2)
        self.play(FadeIn(formula_title), run_time=0.5)

        # 左边：a - b - c
        lhs = MathTex(r"a - b - c", font_size=60, color=WHITE)
        lhs.move_to(UP * 4.8)

        self.play(Write(lhs), run_time=0.8)
        self.wait(0.3)

        # 等号
        equal_sign = MathTex(r"=", font_size=60, color=self.COLOR_HIGHLIGHT)
        equal_sign.move_to(UP * 3.8)
        self.play(Write(equal_sign), run_time=0.4)

        # 右边：a - (b + c)
        rhs = MathTex(r"a - (b + c)", font_size=60, color=self.COLOR_FORMULA)
        rhs.move_to(UP * 2.8)
        self.play(Write(rhs), run_time=0.8)
        self.wait(0.5)

        # 解释文字框
        box = RoundedRectangle(
            width=7.5,
            height=3.0,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=self.COLOR_FORMULA,
            stroke_width=2,
        ).move_to(UP * 1.1)
        self.play(Create(box), run_time=0.4)

        explain1 = Text(
            "一个数连续减去两个数，",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
        ).move_to(UP * 1.7)

        explain2 = Text(
            "等于减去这两个数的和。",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 1.0)

        explain3 = Text(
            "反过来也成立！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SUCCESS,
        ).move_to(UP * 0.3)

        self.play(FadeIn(explain1), run_time=0.4)
        self.play(FadeIn(explain2), run_time=0.5)
        self.play(FadeIn(explain3), run_time=0.4)
        self.wait(1.0)

        # 括号说明箭头
        bracket_note = Text(
            "括号里的 b+c 先算",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.8)

        arrow_up = Arrow(
            start=bracket_note.get_top() + UP * 0.05,
            end=rhs.get_bottom() + DOWN * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.12,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(FadeIn(bracket_note), Create(arrow_up), run_time=0.6)
        self.wait(0.8)

        # 同时高亮两边公式
        self.play(
            Indicate(lhs, color=WHITE, scale_factor=1.1),
            Indicate(rhs, color=self.COLOR_FORMULA, scale_factor=1.1),
            run_time=0.8,
        )
        self.wait(0.6)

        # 清理
        self.play(
            FadeOut(formula_title),
            FadeOut(lhs),
            FadeOut(equal_sign),
            FadeOut(rhs),
            FadeOut(box),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(explain3),
            FadeOut(bracket_note),
            FadeOut(arrow_up),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 4: 例题讲解 125 - 36 - 64
    # ─────────────────────────────────────────────────────────────
    def scene_4_example(self):
        # 标题
        ex_title = Text(
            "例题讲解",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 6.2)
        self.play(FadeIn(ex_title), run_time=0.4)

        problem_label = Text(
            "计算：",
            font="Noto Sans CJK SC",
            font_size=32,
            color="#9ca3af",
        ).move_to(UP * 5.2)

        problem = MathTex(
            r"125 - 36 - 64",
            font_size=60,
            color=WHITE,
        ).move_to(UP * 4.2)

        self.play(FadeIn(problem_label), run_time=0.3)
        self.play(Write(problem), run_time=0.8)
        self.wait(0.5)

        # ─ 步骤一：观察规律 ─
        step1_label = Text(
            "第一步：观察 36 和 64",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 2.8)
        self.play(FadeIn(step1_label), run_time=0.4)

        # 彩色版题目
        problem_colored = VGroup(
            MathTex(r"125", font_size=60, color=WHITE),
            MathTex(r"-", font_size=60, color=WHITE),
            MathTex(r"36", font_size=60, color=self.COLOR_REMOVE),
            MathTex(r"-", font_size=60, color=WHITE),
            MathTex(r"64", font_size=60, color=self.COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.2)

        self.play(Transform(problem, problem_colored), run_time=0.5)

        # Brace 标注 36+64
        nums_vg = VGroup(problem_colored[2], problem_colored[4])
        brace_sum = Brace(nums_vg, direction=DOWN, color=self.COLOR_FORMULA)
        brace_sum_label = VGroup(
            Text("36 + 64 = ", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_FORMULA),
            Text("100", font="Noto Sans CJK SC", font_size=32, color=self.COLOR_SUCCESS),
            Text("  整百！", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.1)
        brace_sum_label.next_to(brace_sum, DOWN, buff=0.15)

        self.play(Create(brace_sum), run_time=0.5)
        self.play(FadeIn(brace_sum_label), run_time=0.5)
        self.wait(0.8)

        # ─ 步骤二：应用减法性质 ─
        step2_label = Text(
            "第二步：应用减法性质",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 1.2)
        self.play(FadeIn(step2_label), run_time=0.4)

        # = 125 - (36 + 64)
        eq1 = VGroup(
            MathTex(r"=", font_size=52, color=WHITE),
            MathTex(r"125", font_size=52, color=WHITE),
            MathTex(r"-", font_size=52, color=WHITE),
            MathTex(r"(", font_size=52, color=self.COLOR_FORMULA),
            MathTex(r"36", font_size=52, color=self.COLOR_REMOVE),
            MathTex(r"+", font_size=52, color=self.COLOR_FORMULA),
            MathTex(r"64", font_size=52, color=self.COLOR_ACCENT),
            MathTex(r")", font_size=52, color=self.COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 0.2)

        self.play(FadeIn(eq1), run_time=0.6)
        self.wait(0.3)

        # = 125 - 100
        eq2 = VGroup(
            MathTex(r"=", font_size=52, color=WHITE),
            MathTex(r"125", font_size=52, color=WHITE),
            MathTex(r"-", font_size=52, color=WHITE),
            MathTex(r"100", font_size=52, color=self.COLOR_SUCCESS),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.0)

        self.play(Write(eq2), run_time=0.6)
        self.wait(0.4)

        # ─ 步骤三：最终答案 ─
        result_box = RoundedRectangle(
            width=5.5,
            height=1.6,
            corner_radius=0.3,
            fill_color="#0d2137",
            fill_opacity=1.0,
            stroke_color=self.COLOR_SUCCESS,
            stroke_width=3,
        ).move_to(DOWN * 2.6)

        result_text = VGroup(
            MathTex(r"=", font_size=64, color=WHITE),
            MathTex(r"25", font_size=72, color=self.COLOR_SUCCESS),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.6)

        self.play(Create(result_box), run_time=0.4)
        self.play(Write(result_text), run_time=0.6)
        self.play(
            Flash(result_text, color=self.COLOR_SUCCESS, flash_radius=1.0, num_lines=10),
            run_time=0.6,
        )
        self.wait(0.4)

        # 关键提示
        key_msg = Text(
            "关键：36+64=100，整百数好算！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(key_msg, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(ex_title),
            FadeOut(problem_label),
            FadeOut(problem),
            FadeOut(step1_label),
            FadeOut(brace_sum),
            FadeOut(brace_sum_label),
            FadeOut(step2_label),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(result_box),
            FadeOut(result_text),
            FadeOut(key_msg),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────────────────────
    # Scene 5: 总结与片尾
    # ─────────────────────────────────────────────────────────────
    def scene_5_outro(self):
        # 总结标题
        summary_title = Text(
            "记住这个性质",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 6.0)
        self.play(FadeIn(summary_title), run_time=0.5)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8,
            height=2.2,
            corner_radius=0.4,
            fill_color="#16213e",
            fill_opacity=1.0,
            stroke_color=self.COLOR_FORMULA,
            stroke_width=3,
        ).move_to(UP * 4.5)

        formula_display = VGroup(
            MathTex(r"a - b - c", font_size=52, color=WHITE),
            MathTex(r"=", font_size=52, color=self.COLOR_HIGHLIGHT),
            MathTex(r"a - (b + c)", font_size=52, color=self.COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.5)

        self.play(Create(formula_box), run_time=0.4)
        self.play(Write(formula_display), run_time=0.8)
        self.wait(0.4)

        # 要点背景框
        point_bg = RoundedRectangle(
            width=7.8,
            height=4.2,
            corner_radius=0.4,
            fill_color="#16213e",
            fill_opacity=0.85,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
        ).move_to(UP * 2.0)
        self.play(Create(point_bg), run_time=0.3)

        # 三条要点
        points_data = [
            ("● 连续减两个数", "= 减两数之和", self.COLOR_SUCCESS),
            ("● 先合并括号内", "再一步计算", self.COLOR_ACCENT),
            ("● 找整百整千数", "是简便计算关键", self.COLOR_FORMULA),
        ]

        pt_rows = VGroup()
        for p1, p2, col in points_data:
            txt1 = Text(p1, font="Noto Sans CJK SC", font_size=24, color=col)
            txt2 = Text(p2, font="Noto Sans CJK SC", font_size=22, color=WHITE)
            row = VGroup(txt1, txt2).arrange(RIGHT, buff=0.3)
            pt_rows.add(row)

        pt_rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        pt_rows.move_to(UP * 2.0)

        for row in pt_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.8)

        # 练习题
        practice_title = Text(
            "再练一题！",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.8)
        practice_q = MathTex(
            r"200 - 73 - 27 = \, ?",
            font_size=50,
            color=WHITE,
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(practice_title), run_time=0.4)
        self.play(Write(practice_q), run_time=0.6)
        self.wait(0.8)

        practice_a_label = Text(
            "200-(73+27)=200-100=",
            font="Noto Sans CJK SC",
            font_size=24,
            color="#9ca3af",
        )
        practice_a_num = Text(
            "100",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_SUCCESS,
        )
        practice_a = VGroup(practice_a_label, practice_a_num).arrange(RIGHT, buff=0.1)
        practice_a.move_to(DOWN * 2.9)

        self.play(FadeIn(practice_a, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理过渡到片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(formula_box),
            FadeOut(formula_display),
            FadeOut(point_bg),
            FadeOut(pt_rows),
            FadeOut(practice_title),
            FadeOut(practice_q),
            FadeOut(practice_a),
            run_time=0.7,
        )

        # 片尾：作者大字
        outro_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE,
        ).move_to(UP * 1.5)

        outro_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color="#6b7280",
        ).move_to(UP * 0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.7)

        self.play(
            Transform(self.author_tag, outro_name),
            run_time=0.7,
        )
        self.play(FadeIn(outro_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)

        # 装饰星星
        star_positions = [
            UP * 3.5 + LEFT * 3.0,
            UP * 3.5 + RIGHT * 3.0,
            DOWN * 2.2 + LEFT * 2.5,
            DOWN * 2.2 + RIGHT * 2.5,
            DOWN * 3.5,
        ]
        stars = VGroup(*[
            Star(
                n=5,
                outer_radius=0.28,
                inner_radius=0.12,
                fill_color=self.COLOR_ACCENT,
                fill_opacity=0.9,
                stroke_width=0,
            ).move_to(pos)
            for pos in star_positions
        ])

        self.play(*[FadeIn(s, scale=0.5) for s in stars], run_time=0.6)
        self.play(
            *[s.animate.scale(1.3) for s in stars],
            rate_func=there_and_back,
            run_time=0.8,
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author_tag),
            FadeOut(outro_id),
            FadeOut(follow_text),
            FadeOut(stars),
            run_time=0.8,
        )
