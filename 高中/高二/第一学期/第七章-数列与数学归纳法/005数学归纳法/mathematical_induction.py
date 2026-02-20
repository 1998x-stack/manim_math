"""
数学归纳法教学动画 - Mathematical Induction Teaching Animation
使用 Manim 创建的高二数学教学视频

内容: 数学归纳法的原理、步骤、应用
目标观众: 高二学生
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


class MathematicalInduction(Scene):
    """
    数学归纳法教学动画场景
    
    场景顺序:
    1. 开场钩子 - 多米诺骨牌
    2. 数学归纳法介绍
    3. 两个步骤概览
    4. 步骤1详解 - 归纳奠基
    5. 步骤2详解 - 归纳递推
    6. 完整证明示例
    7. 应用场景
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调递推
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键步骤
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_DOMINO = "#8e44ad"       # 紫色 - 多米诺骨牌
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 成功/成立
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_introduction()
        self.show_two_steps()
        self.show_base_case()
        self.show_inductive_step()
        self.show_complete_example()
        self.show_applications()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化几何位置和数据"""
        # 多米诺骨牌配置
        self.domino_count = 8
        self.domino_spacing = 0.8
        self.domino_width = 0.4
        self.domino_height = 1.2
        self.domino_y = 1.0
        
        # 多米诺位置
        self.domino_positions = [
            np.array([-3.5 + i * self.domino_spacing, self.domino_y, 0])
            for i in range(self.domino_count)
        ]
        
        # 步骤框配置
        self.step_box_width = 3.5
        self.step_box_height = 2.0
        
        print("✓ 几何数据初始化完成")
    
    def create_domino(self, position):
        """创建单个多米诺骨牌"""
        domino = Rectangle(
            width=self.domino_width,
            height=self.domino_height,
            color=self.COLOR_DOMINO,
            fill_opacity=0.8,
            stroke_width=2
        )
        domino.move_to(position)
        return domino
    
    def show_opening(self):
        """场景1: 开场钩子 - 多米诺骨牌效应"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何证明无限个命题?",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=1.0)
        self.wait(0.5)
        
        # 创建多米诺骨牌
        self.dominoes = VGroup(*[
            self.create_domino(pos) for pos in self.domino_positions
        ])
        
        # 多米诺骨牌依次竖立
        self.play(
            LaggedStart(
                *[FadeIn(domino, shift=DOWN * 0.3) for domino in self.dominoes],
                lag_ratio=0.1
            ),
            run_time=1.5
        )
        
        self.wait(0.3)
        
        # 第一块开始倒下
        self.play(
            Rotate(
                self.dominoes[0],
                angle=-PI / 5,
                about_point=self.dominoes[0].get_bottom() + DOWN * 0.01
            ),
            run_time=0.4
        )
        
        # 连锁反应
        for i in range(1, self.domino_count):
            self.play(
                Rotate(
                    self.dominoes[i],
                    angle=-PI / 5,
                    about_point=self.dominoes[i].get_bottom() + DOWN * 0.01
                ),
                run_time=0.25
            )
        
        self.wait(0.8)
        
        # 清理钩子文字，保留多米诺（缩小移到背景）
        self.play(
            FadeOut(hook_question),
            self.dominoes.animate.scale(0.5).move_to(DOWN * 5).set_opacity(0.3),
            run_time=0.6
        )
    
    def show_introduction(self):
        """场景2: 数学归纳法介绍"""
        # 标题
        title = Text(
            "数学归纳法",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "Mathematical Induction",
            font_size=28,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 定义
        definition = Text(
            "证明与正整数n有关命题的方法",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        
        # 核心思想框
        core_idea = VGroup(
            Text("核心思想:", font="Noto Sans CJK SC", font_size=32, color=self.COLOR_HIGHLIGHT),
            Text("如同多米诺骨牌", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            Text("推倒第一块 + 传递效应", font="Noto Sans CJK SC", font_size=26, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 1.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(text, shift=RIGHT * 0.3) for text in core_idea],
                lag_ratio=0.3
            ),
            run_time=1.5
        )
        
        # 指向多米诺的箭头
        arrow_to_domino = Arrow(
            core_idea.get_bottom() + DOWN * 0.3,
            self.dominoes.get_top() + UP * 0.5,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(GrowArrow(arrow_to_domino), run_time=0.6)
        
        # 让多米诺再次倒下（快速）
        self.play(
            self.dominoes.animate.set_opacity(1.0),
            run_time=0.3
        )
        
        for i in range(self.domino_count):
            self.play(
                Rotate(
                    self.dominoes[i],
                    angle=-PI / 6,
                    about_point=self.dominoes[i].get_bottom() + DOWN * 0.01
                ),
                run_time=0.15
            )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(core_idea),
            FadeOut(arrow_to_domino),
            self.dominoes.animate.set_opacity(0.2),
            run_time=0.6
        )
        
        # 保留标题但缩小
        self.title_small = VGroup(title, subtitle).copy()
        self.play(
            self.title_small.animate.scale(0.6).move_to(UP * 7),
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_two_steps(self):
        """场景3: 两个步骤概览"""
        # 场景标题
        scene_title = Text(
            "两个必要步骤",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 步骤1框
        step1_box = RoundedRectangle(
            width=self.step_box_width,
            height=self.step_box_height,
            corner_radius=0.15,
            color=self.COLOR_SUCCESS,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(np.array([-2.2, 2.5, 0]))
        
        step1_title = Text(
            "步骤1",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).move_to(step1_box.get_top() + DOWN * 0.4)
        
        step1_name = Text(
            "归纳奠基",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(step1_box.get_center() + UP * 0.2)
        
        step1_subtitle = Text(
            "Base Case",
            font_size=22,
            color=GRAY_A
        ).move_to(step1_box.get_center() + DOWN * 0.3)
        
        step1_content = MathTex(
            r"n = 1",
            font_size=36,
            color=self.COLOR_SUCCESS
        ).move_to(step1_box.get_center() + DOWN * 0.8)
        
        step1_group = VGroup(step1_box, step1_title, step1_name, step1_subtitle, step1_content)
        
        self.play(
            FadeIn(step1_box, shift=RIGHT * 0.5),
            run_time=0.5
        )
        self.play(
            Write(step1_title),
            Write(step1_name),
            FadeIn(step1_subtitle),
            run_time=0.8
        )
        self.play(Write(step1_content), run_time=0.5)
        
        self.wait(0.5)
        
        # 步骤2框
        step2_box = RoundedRectangle(
            width=self.step_box_width,
            height=self.step_box_height,
            corner_radius=0.15,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(np.array([2.2, 2.5, 0]))
        
        step2_title = Text(
            "步骤2",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(step2_box.get_top() + DOWN * 0.4)
        
        step2_name = Text(
            "归纳递推",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(step2_box.get_center() + UP * 0.2)
        
        step2_subtitle = Text(
            "Inductive Step",
            font_size=22,
            color=GRAY_A
        ).move_to(step2_box.get_center() + DOWN * 0.3)
        
        step2_content = MathTex(
            r"k \Rightarrow k+1",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(step2_box.get_center() + DOWN * 0.8)
        
        step2_group = VGroup(step2_box, step2_title, step2_name, step2_subtitle, step2_content)
        
        self.play(
            FadeIn(step2_box, shift=LEFT * 0.5),
            run_time=0.5
        )
        self.play(
            Write(step2_title),
            Write(step2_name),
            FadeIn(step2_subtitle),
            run_time=0.8
        )
        self.play(Write(step2_content), run_time=0.5)
        
        self.wait(0.5)
        
        # 连接箭头
        arrow_between = Arrow(
            step1_box.get_right() + RIGHT * 0.1,
            step2_box.get_left() + LEFT * 0.1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_between), run_time=0.6)
        
        # 结论框
        conclusion_box = RoundedRectangle(
            width=6.0,
            height=1.5,
            corner_radius=0.15,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(DOWN * 1.5)
        
        conclusion_text = Text(
            "对所有 n ≥ 1 成立",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(conclusion_box.get_center())
        
        arrows_to_conclusion = VGroup(
            Arrow(
                step1_box.get_bottom() + DOWN * 0.1,
                conclusion_box.get_top() + UP * 0.1 + LEFT * 1.5,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=2
            ),
            Arrow(
                step2_box.get_bottom() + DOWN * 0.1,
                conclusion_box.get_top() + UP * 0.1 + RIGHT * 1.5,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=2
            )
        )
        
        self.play(
            *[GrowArrow(arrow) for arrow in arrows_to_conclusion],
            run_time=0.8
        )
        
        self.play(
            FadeIn(conclusion_box, scale=0.9),
            Write(conclusion_text),
            run_time=1.0
        )
        
        # 强调缺一不可
        emphasis = Text(
            "两步缺一不可!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=RED
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(emphasis, shift=UP * 0.3, scale=1.2), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(step1_group),
            FadeOut(step2_group),
            FadeOut(arrow_between),
            FadeOut(arrows_to_conclusion),
            FadeOut(conclusion_box),
            FadeOut(conclusion_text),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_base_case(self):
        """场景4: 步骤1详解 - 归纳奠基"""
        # 场景标题
        scene_title = Text(
            "步骤1: 归纳奠基",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 说明
        explanation = Text(
            "验证 n=1 (或 n=n₀) 时命题成立",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        
        # 公式框
        formula_box = RoundedRectangle(
            width=5.0,
            height=1.5,
            corner_radius=0.12,
            color=self.COLOR_SUCCESS,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(UP * 3)
        
        formula = MathTex(
            r"n = 1 \text{ or } n = n_0",
            font_size=36,
            color=WHITE
        ).move_to(formula_box.get_center())
        
        self.play(
            FadeIn(formula_box, scale=0.9),
            Write(formula),
            run_time=1.0
        )
        
        # 多米诺第一块高亮
        first_domino_highlight = self.dominoes[0].copy()
        first_domino_highlight.set_color(self.COLOR_SUCCESS).set_stroke(width=4)
        
        self.play(
            self.dominoes.animate.set_opacity(1.0),
            run_time=0.3
        )
        
        self.play(
            Indicate(self.dominoes[0], scale_factor=1.4, color=self.COLOR_SUCCESS),
            run_time=1.0
        )
        
        # 类比文字
        analogy = VGroup(
            Text("类比:", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SUCCESS),
            Text("确保第一块骨牌能推倒", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 0.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(text, shift=RIGHT * 0.3) for text in analogy],
                lag_ratio=0.3
            ),
            run_time=1.0
        )
        
        # 箭头
        arrow_to_first = Arrow(
            analogy.get_bottom() + DOWN * 0.3,
            self.dominoes[0].get_top() + UP * 0.3,
            color=self.COLOR_SUCCESS,
            stroke_width=3
        )
        
        self.play(GrowArrow(arrow_to_first), run_time=0.5)
        
        # 检查标记
        check_mark = Text(
            "✓",
            font_size=72,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.5)
        self.play(Indicate(check_mark, scale_factor=1.3), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(explanation),
            FadeOut(formula_box),
            FadeOut(formula),
            FadeOut(analogy),
            FadeOut(arrow_to_first),
            FadeOut(check_mark),
            self.dominoes.animate.set_opacity(0.2),
            run_time=0.6
        )
    
    def show_inductive_step(self):
        """场景5: 步骤2详解 - 归纳递推"""
        # 场景标题
        scene_title = Text(
            "步骤2: 归纳递推",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 说明
        explanation = Text(
            "假设 n=k 成立, 证明 n=k+1 也成立",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        
        # 假设框
        assumption_box = RoundedRectangle(
            width=5.5,
            height=1.2,
            corner_radius=0.12,
            color=BLUE,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(UP * 3.2)
        
        assumption_label = Text(
            "假设:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=BLUE
        ).next_to(assumption_box.get_left(), RIGHT, buff=0.3).align_to(assumption_box, UP).shift(DOWN * 0.25)
        
        assumption_formula = MathTex(
            r"P(k) \text{ is true}",
            font_size=32,
            color=WHITE
        ).move_to(assumption_box.get_center())
        
        self.play(
            FadeIn(assumption_box, scale=0.9),
            Write(assumption_label),
            run_time=0.6
        )
        self.play(Write(assumption_formula), run_time=0.8)
        
        # 箭头
        arrow_down = Arrow(
            assumption_box.get_bottom() + DOWN * 0.1,
            assumption_box.get_bottom() + DOWN * 1.0,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        arrow_label = Text(
            "证明",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(arrow_down, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(arrow_down),
            FadeIn(arrow_label),
            run_time=0.6
        )
        
        # 证明框
        proof_box = RoundedRectangle(
            width=5.5,
            height=1.2,
            corner_radius=0.12,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(UP * 1.0)
        
        proof_label = Text(
            "证明:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(proof_box.get_left(), RIGHT, buff=0.3).align_to(proof_box, UP).shift(DOWN * 0.25)
        
        proof_formula = MathTex(
            r"P(k+1) \text{ is true}",
            font_size=32,
            color=WHITE
        ).move_to(proof_box.get_center())
        
        self.play(
            FadeIn(proof_box, scale=0.9),
            Write(proof_label),
            run_time=0.6
        )
        self.play(Write(proof_formula), run_time=0.8)
        
        # 多米诺k和k+1
        self.play(
            self.dominoes.animate.set_opacity(1.0),
            run_time=0.3
        )
        
        domino_restorations = []
        for i, domino in enumerate(self.dominoes):
            original_domino = self.create_domino(self.domino_positions[i])
            domino_restorations.append(Transform(domino, original_domino))
        
        self.play(*domino_restorations, run_time=0.2)
        
        # 高亮第k块和第k+1块
        k_index = 3  # 选择中间的多米诺作为k
        
        k_label = MathTex(r"k", font_size=28, color=BLUE).next_to(self.dominoes[k_index], DOWN, buff=0.2)
        k1_label = MathTex(r"k+1", font_size=28, color=self.COLOR_SECONDARY).next_to(self.dominoes[k_index + 1], DOWN, buff=0.2)
        
        self.play(
            Write(k_label),
            Write(k1_label),
            run_time=0.6
        )
        
        # k倒下
        self.play(
            Rotate(
                self.dominoes[k_index],
                angle=-PI / 5,
                about_point=self.dominoes[k_index].get_bottom() + DOWN * 0.01
            ),
            Flash(self.dominoes[k_index], color=BLUE, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(0.3)
        
        # k+1倒下
        self.play(
            Rotate(
                self.dominoes[k_index + 1],
                angle=-PI / 5,
                about_point=self.dominoes[k_index + 1].get_bottom() + DOWN * 0.01
            ),
            Flash(self.dominoes[k_index + 1], color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.5
        )
        
        # 类比文字
        analogy = VGroup(
            Text("类比:", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SECONDARY),
            Text("第k块倒下 → 第k+1块倒下", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(text, shift=RIGHT * 0.3) for text in analogy],
                lag_ratio=0.3
            ),
            run_time=1.0
        )
        
        # 关键点强调
        key_point = Text(
            "传递性保证了无限传递!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(explanation),
            FadeOut(assumption_box),
            FadeOut(assumption_label),
            FadeOut(assumption_formula),
            FadeOut(arrow_down),
            FadeOut(arrow_label),
            FadeOut(proof_box),
            FadeOut(proof_label),
            FadeOut(proof_formula),
            FadeOut(k_label),
            FadeOut(k1_label),
            FadeOut(analogy),
            FadeOut(key_point),
            self.dominoes.animate.set_opacity(0.2),
            run_time=0.6
        )
    
    def show_complete_example(self):
        """场景6: 完整证明示例"""
        # 例题
        problem_title = Text(
            "完整示例",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(problem_title), run_time=0.6)
        
        problem = MathTex(
            r"1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        problem_box = SurroundingRectangle(
            problem,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            Write(problem),
            Create(problem_box),
            run_time=1.2
        )
        
        self.wait(0.8)
        
        # 步骤1: 归纳奠基
        step1_label = Text(
            "步骤1: n=1",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(step1_label, shift=RIGHT * 0.3), run_time=0.5)
        
        verification_left = MathTex(
            r"\text{left} = 1",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.0 + LEFT * 2)
        
        verification_right = MathTex(
            r"\text{right} = \frac{1 \times 2}{2} = 1",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.0 + RIGHT * 1.5)
        
        self.play(
            Write(verification_left),
            Write(verification_right),
            run_time=1.0
        )
        
        check1 = Text(
            "✓",
            font_size=48,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(check1, scale=0.5), run_time=0.4)
        
        self.wait(0.5)
        
        # 步骤2: 归纳递推
        step2_label = Text(
            "步骤2: k → k+1",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.2)
        
        self.play(FadeIn(step2_label, shift=RIGHT * 0.3), run_time=0.5)
        
        # 假设k成立
        assumption = MathTex(
            r"1 + 2 + \cdots + k = \frac{k(k+1)}{2}",
            font_size=26,
            color=BLUE
        ).move_to(UP * 0.5)
        
        assumption_label = Text(
            "假设:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=BLUE
        ).next_to(assumption, LEFT, buff=0.3)
        
        self.play(
            Write(assumption_label),
            Write(assumption),
            run_time=1.0
        )
        
        # 证明k+1
        proof_start = MathTex(
            r"1 + 2 + \cdots + k + (k+1)",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        proof_label = Text(
            "证明:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_SECONDARY
        ).next_to(proof_start, LEFT, buff=0.3)
        
        self.play(
            Write(proof_label),
            Write(proof_start),
            run_time=0.8
        )
        
        # 代换
        proof_substitute = MathTex(
            r"= \frac{k(k+1)}{2} + (k+1)",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.2)
        
        self.play(Write(proof_substitute), run_time=0.8)
        
        # 化简
        proof_simplify = MathTex(
            r"= \frac{k(k+1) + 2(k+1)}{2}",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.9)
        
        self.play(Write(proof_simplify), run_time=0.8)
        
        # 最终结果
        proof_final = MathTex(
            r"= \frac{(k+1)(k+2)}{2}",
            font_size=26,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 2.6)
        
        self.play(Write(proof_final), run_time=0.8)
        
        # 结论框
        conclusion = Text(
            "恰好是 n=k+1 时的形式!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.8)
        
        conclusion_box = SurroundingRectangle(
            conclusion,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(conclusion_box, scale=0.9),
            Write(conclusion),
            run_time=1.0
        )
        
        # 最终检查标记
        check2 = Text(
            "✓",
            font_size=56,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(check2, scale=0.5), run_time=0.5)
        self.play(Indicate(check2, scale_factor=1.3), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(problem_title),
            FadeOut(problem),
            FadeOut(problem_box),
            FadeOut(step1_label),
            FadeOut(verification_left),
            FadeOut(verification_right),
            FadeOut(check1),
            FadeOut(step2_label),
            FadeOut(assumption_label),
            FadeOut(assumption),
            FadeOut(proof_label),
            FadeOut(proof_start),
            FadeOut(proof_substitute),
            FadeOut(proof_simplify),
            FadeOut(proof_final),
            FadeOut(conclusion),
            FadeOut(conclusion_box),
            FadeOut(check2),
            run_time=0.6
        )
    
    def show_applications(self):
        """场景7: 应用场景"""
        # 标题
        app_title = Text(
            "数学归纳法的应用",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(app_title), run_time=0.6)
        
        # 应用卡片数据
        applications = [
            ("恒等式证明", r"1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}", self.COLOR_PRIMARY),
            ("不等式证明", r"2^n > n^2 \text{ for } n \geq 5", self.COLOR_SECONDARY),
            ("整除性证明", r"n^3 - n \text{ is divisible by } 6", self.COLOR_SUCCESS)
        ]
        
        cards = VGroup()
        y_positions = [3, 0.5, -2]
        
        for i, (title, formula, color) in enumerate(applications):
            # 卡片框
            card_box = RoundedRectangle(
                width=7.0,
                height=1.8,
                corner_radius=0.12,
                color=color,
                fill_opacity=0.1,
                stroke_width=3
            ).move_to(np.array([0, y_positions[i], 0]))
            
            # 标题
            card_title = Text(
                title,
                font="Noto Sans CJK SC",
                font_size=28,
                color=color
            ).move_to(card_box.get_top() + DOWN * 0.4)
            
            # 公式
            card_formula = MathTex(
                formula,
                font_size=24,
                color=WHITE
            ).move_to(card_box.get_center() + DOWN * 0.2)
            
            card_group = VGroup(card_box, card_title, card_formula)
            cards.add(card_group)
            
            # 初始位置在左侧外
            card_group.shift(LEFT * 10)
        
        # 卡片依次滑入
        for card in cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.6)
            self.wait(0.3)
        
        # 全部高亮
        self.play(
            *[Indicate(card, scale_factor=1.05) for card in cards],
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(app_title),
            FadeOut(cards),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结与片尾"""
        # 清理顶部标题
        self.play(FadeOut(self.title_small), run_time=0.3)
        
        # 核心要点总结
        summary_title = Text(
            "数学归纳法核心要点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点卡片
        summary_points = [
            "① 归纳奠基: 验证起点",
            "② 归纳递推: k → k+1",
            "③ 两步缺一不可",
            "④ 适用于正整数命题"
        ]
        
        summary_cards = VGroup()
        y_start = 3.5
        y_gap = 1.3
        
        for i, point in enumerate(summary_points):
            card = Text(
                point,
                font="Noto Sans CJK SC",
                font_size=28,
                color=WHITE
            ).move_to(np.array([0, y_start - i * y_gap, 0]))
            
            # 图标
            icon = Text(
                "▸",
                font_size=32,
                color=self.COLOR_HIGHLIGHT
            ).next_to(card, LEFT, buff=0.3)
            
            card_group = VGroup(icon, card)
            summary_cards.add(card_group)
        
        # 依次出现
        self.play(
            LaggedStart(
                *[FadeIn(card, shift=RIGHT * 0.3) for card in summary_cards],
                lag_ratio=0.3
            ),
            run_time=2.0
        )
        
        self.wait(1.0)
        
        # 多米诺完整连锁效果
        self.play(
            self.dominoes.animate.set_opacity(1.0).move_to(DOWN * 3).scale(1.5),
            run_time=0.6
        )
        
        domino_restorations = []
        for i, domino in enumerate(self.dominoes):
            original_domino = self.create_domino(self.domino_positions[i])
            domino_restorations.append(Transform(domino, original_domino))
        
        self.play(*domino_restorations, run_time=0.2)
        
        # 完整连锁
        for i in range(self.domino_count):
            self.play(
                Rotate(
                    self.dominoes[i],
                    angle=-PI / 5,
                    about_point=self.dominoes[i].get_bottom() + DOWN * 0.01
                ),
                run_time=0.2
            )
        
        self.wait(0.5)
        
        # 清理并显示作者信息
        self.play(
            FadeOut(summary_title),
            FadeOut(summary_cards),
            FadeOut(self.dominoes),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰: 数学符号
        decorations = VGroup(
            MathTex(r"n=1", font_size=28, color=self.COLOR_SUCCESS),
            MathTex(r"k \to k+1", font_size=28, color=self.COLOR_SECONDARY),
            MathTex(r"\forall n \geq 1", font_size=28, color=self.COLOR_PRIMARY)
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(dec, scale=0.5) for dec in decorations],
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql mathematical_induction.py MathematicalInduction  # 快速预览
# manim -qh mathematical_induction.py MathematicalInduction   # 高质量 (1080p)
# manim -qk mathematical_induction.py MathematicalInduction   # 4K质量