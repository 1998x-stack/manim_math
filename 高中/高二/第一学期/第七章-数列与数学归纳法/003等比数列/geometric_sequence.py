"""
等比数列教学动画 - Geometric Sequence Teaching Animation
使用 Manim 创建的高二数学教学视频

内容: 等比数列的定义、通项公式、前n项和、特殊情况
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


class GeometricSequence(Scene):
    """
    等比数列教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义与公比
    3. 通项公式推导
    4. 几何可视化
    5. 前n项和公式
    6. 特殊情况 q=1
    7. 无穷等比数列
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数列
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调公比
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键公式
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
        self.COLOR_GEOMETRIC = "#9b59b6"    # 紫色 - 几何表示
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_general_term()
        self.show_geometric_visualization()
        self.show_sum_formula()
        self.show_special_case()
        self.show_infinite_series()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化几何位置和数据"""
        # 数列项位置 (横向排列)
        self.term_spacing = 1.8
        self.term_y = 2.0
        self.term_positions = [
            np.array([-3.0 + i * self.term_spacing, self.term_y, 0])
            for i in range(5)
        ]
        
        # 示例数列参数
        self.example_a1 = 2
        self.example_q = 2
        self.example_terms = [self.example_a1 * (self.example_q ** i) for i in range(5)]
        
        # 公式位置
        self.formula_center = np.array([0, 0, 0])
        
        print("✓ 几何数据初始化完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "1, 2, 4, 8, 16...",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        hook_text = Text(
            "规律是什么?",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(hook_question), run_time=1.0)
        self.play(FadeIn(hook_text, shift=UP * 0.3), run_time=0.5)
        
        # 动态数字序列展示
        numbers = [1, 2, 4, 8, 16]
        number_mobs = VGroup(*[
            Text(str(n), font="PingFang SC", font_size=56, color=self.COLOR_PRIMARY)
            for n in numbers
        ])
        
        # 排列在中央
        number_mobs.arrange(RIGHT, buff=0.8).move_to(UP * 1)
        
        # 依次出现
        self.play(
            LaggedStart(
                *[FadeIn(num, scale=0.5) for num in number_mobs],
                lag_ratio=0.3
            ),
            run_time=2.0
        )
        
        # 箭头和倍数关系
        arrows = VGroup()
        ratio_labels = VGroup()
        
        for i in range(len(numbers) - 1):
            arrow = Arrow(
                number_mobs[i].get_right() + RIGHT * 0.1,
                number_mobs[i + 1].get_left() + LEFT * 0.1,
                buff=0.1,
                color=self.COLOR_SECONDARY,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)
            
            label = MathTex(r"\times 2", font_size=28, color=self.COLOR_SECONDARY)
            label.next_to(arrow, UP, buff=0.05)
            ratio_labels.add(label)
        
        self.play(
            LaggedStart(
                *[GrowArrow(arrow) for arrow in arrows],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[FadeIn(label, shift=DOWN * 0.2) for label in ratio_labels],
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hook_text),
            FadeOut(number_mobs),
            FadeOut(arrows),
            FadeOut(ratio_labels),
            run_time=0.6
        )
    
    def show_definition(self):
        """场景2: 定义与公比"""
        # 标题
        title = Text(
            "等比数列",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "Geometric Sequence",
            font_size=28,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 定义文字
        definition = Text(
            "从第2项起，每项与前一项的比为常数",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        
        # 数列项展示
        term_labels = VGroup()
        term_values = VGroup()
        
        for i in range(5):
            # 符号标签
            if i < 4:
                label = MathTex(f"a_{{{i+1}}}", font_size=32, color=WHITE)
            else:
                label = MathTex(r"\cdots", font_size=32, color=WHITE)
            
            label.move_to(self.term_positions[i] + UP * 0.5)
            term_labels.add(label)
            
            # 数值 (示例: 2, 4, 8, 16, ...)
            if i < 4:
                value = Text(
                    str(self.example_terms[i]),
                    font="PingFang SC",
                    font_size=40,
                    color=self.COLOR_PRIMARY
                )
                value.move_to(self.term_positions[i])
                term_values.add(value)
        
        self.play(
            LaggedStart(
                *[FadeIn(label, shift=UP * 0.2) for label in term_labels],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[FadeIn(value, scale=0.8) for value in term_values],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        # 公比箭头和标注
        ratio_arrows = VGroup()
        ratio_labels = VGroup()
        
        for i in range(3):
            arrow = Arrow(
                self.term_positions[i] + RIGHT * 0.4,
                self.term_positions[i + 1] + LEFT * 0.4,
                buff=0,
                color=self.COLOR_SECONDARY,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.12
            )
            ratio_arrows.add(arrow)
            
            # 公比标签
            ratio_label = MathTex(
                r"\times q",
                font_size=28,
                color=self.COLOR_SECONDARY
            )
            ratio_label.next_to(arrow, DOWN, buff=0.15)
            ratio_labels.add(ratio_label)
        
        self.play(
            LaggedStart(
                *[GrowArrow(arrow) for arrow in ratio_arrows],
                lag_ratio=0.15
            ),
            run_time=1.2
        )
        
        self.play(
            LaggedStart(
                *[Write(label) for label in ratio_labels],
                lag_ratio=0.15
            ),
            run_time=1.0
        )
        
        # 公比定义公式
        ratio_formula = MathTex(
            r"\frac{a_{n+1}}{a_n} = q",
            r"\quad (q \neq 0)",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        formula_box = SurroundingRectangle(
            ratio_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(ratio_formula), run_time=1.0)
        self.play(Create(formula_box), run_time=0.5)
        
        # 公比说明
        ratio_note = Text(
            "q 称为公比 (common ratio)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2.8)
        
        self.play(FadeIn(ratio_note), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(term_values),
            FadeOut(ratio_arrows),
            FadeOut(ratio_labels),
            FadeOut(ratio_formula),
            FadeOut(formula_box),
            FadeOut(ratio_note),
            run_time=0.6
        )
        
        # 保留标题和符号标签
        self.title_small = VGroup(title, subtitle).copy()
        self.play(
            self.title_small.animate.scale(0.6).move_to(UP * 7),
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )
        
        self.term_labels_kept = term_labels
    
    def show_general_term(self):
        """场景3: 通项公式推导"""
        # 场景标题
        scene_title = Text(
            "通项公式",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 清理之前的数列项标签
        self.play(FadeOut(self.term_labels_kept), run_time=0.3)
        
        # 推导步骤
        step_y_start = 3.5
        step_spacing = 1.0
        
        step1 = MathTex(
            r"a_1",
            font_size=36,
            color=WHITE
        ).move_to(np.array([0, step_y_start, 0]))
        
        step2 = MathTex(
            r"a_2 = a_1 \cdot q",
            font_size=36,
            color=WHITE
        ).move_to(np.array([0, step_y_start - step_spacing, 0]))
        
        step3 = MathTex(
            r"a_3 = a_1 \cdot q^2",
            font_size=36,
            color=WHITE
        ).move_to(np.array([0, step_y_start - 2 * step_spacing, 0]))
        
        step4 = MathTex(
            r"a_4 = a_1 \cdot q^3",
            font_size=36,
            color=WHITE
        ).move_to(np.array([0, step_y_start - 3 * step_spacing, 0]))
        
        dots = MathTex(
            r"\vdots",
            font_size=36,
            color=WHITE
        ).move_to(np.array([0, step_y_start - 4 * step_spacing, 0]))
        
        # 逐步展示
        self.play(Write(step1), run_time=0.6)
        self.wait(0.3)
        
        self.play(TransformMatchingTex(step1.copy(), step2), run_time=0.8)
        self.wait(0.3)
        
        self.play(Write(step3), run_time=0.8)
        self.wait(0.3)
        
        self.play(Write(step4), run_time=0.8)
        self.wait(0.3)
        
        self.play(FadeIn(dots), run_time=0.4)
        
        # 通项公式
        general_formula = MathTex(
            r"a_n = a_1 \cdot q^{n-1}",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        formula_box = SurroundingRectangle(
            general_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.15,
            stroke_width=3
        )
        
        # 指数规律标注
        exponent_note = VGroup(
            MathTex(r"n=1: q^0", font_size=28, color=GRAY_A),
            MathTex(r"n=2: q^1", font_size=28, color=GRAY_A),
            MathTex(r"n=3: q^2", font_size=28, color=GRAY_A),
            MathTex(r"n=4: q^3", font_size=28, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(RIGHT * 3 + UP * 1.5)
        
        # 箭头指向指数
        arrow_to_exponent = Arrow(
            exponent_note.get_left() + LEFT * 0.3,
            step2.get_right() + RIGHT * 0.3,
            color=self.COLOR_SECONDARY,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.1
        )
        
        self.play(
            Write(exponent_note),
            GrowArrow(arrow_to_exponent),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 通项公式出现
        self.play(
            FadeOut(exponent_note),
            FadeOut(arrow_to_exponent),
            run_time=0.4
        )
        
        self.play(
            Write(general_formula),
            Create(formula_box),
            run_time=1.2
        )
        
        # 重点停留
        self.play(
            Indicate(general_formula, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(dots),
            run_time=0.5
        )
        
        # 保留通项公式但缩小移到顶部
        self.general_formula_kept = VGroup(general_formula, formula_box)
        self.play(
            self.general_formula_kept.animate.scale(0.7).move_to(UP * 5.5 + LEFT * 0.5),
            run_time=0.5
        )
    
    def show_geometric_visualization(self):
        """场景4: 几何可视化 (用正方形面积表示)"""
        # 场景标题
        scene_title = Text(
            "几何倍增",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_GEOMETRIC
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "以面积为例: q = 2",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 创建正方形序列 (q=2, 边长倍增)
        base_size = 0.6
        squares = []
        area_labels = []
        
        # 计算位置 (底部对齐)
        y_baseline = 0
        x_positions = []
        x_current = -3.5
        
        for i in range(4):
            side_length = base_size * (2 ** i)
            square = Square(
                side_length=side_length,
                color=self.COLOR_GEOMETRIC,
                fill_opacity=0.3,
                stroke_width=3
            )
            
            # 底部对齐
            square.move_to(np.array([x_current + side_length / 2, y_baseline + side_length / 2, 0]))
            squares.append(square)
            x_positions.append(x_current + side_length / 2)
            
            # 面积标签
            area = self.example_a1 * (self.example_q ** i)
            label = Text(
                f"S={area}",
                font="PingFang SC",
                font_size=20,
                color=WHITE
            )
            label.move_to(square.get_center())
            area_labels.append(label)
            
            x_current += side_length + 0.4
        
        # 依次生长正方形
        self.play(FadeIn(squares[0], scale=0.5), run_time=0.6)
        self.play(FadeIn(area_labels[0]), run_time=0.3)
        self.wait(0.3)
        
        for i in range(1, 4):
            self.play(GrowFromCenter(squares[i]), run_time=0.7)
            self.play(FadeIn(area_labels[i]), run_time=0.3)
            self.wait(0.3)
        
        # 公比关系箭头
        ratio_arrows = []
        ratio_labels = []
        
        for i in range(3):
            arrow = Arrow(
                squares[i].get_right() + RIGHT * 0.15,
                squares[i + 1].get_left() + LEFT * 0.15,
                color=self.COLOR_SECONDARY,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.1
            )
            ratio_arrows.append(arrow)
            
            label = MathTex(r"\times 4", font_size=24, color=self.COLOR_SECONDARY)
            label.next_to(arrow, UP, buff=0.1)
            ratio_labels.append(label)
        
        self.play(
            LaggedStart(
                *[GrowArrow(arrow) for arrow in ratio_arrows],
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        
        self.play(
            LaggedStart(
                *[Write(label) for label in ratio_labels],
                lag_ratio=0.2
            ),
            run_time=0.8
        )
        
        # 强调几何倍增
        highlight_text = Text(
            "面积呈几何倍数增长!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(explanation),
            FadeOut(VGroup(*squares)),
            FadeOut(VGroup(*area_labels)),
            FadeOut(VGroup(*ratio_arrows)),
            FadeOut(VGroup(*ratio_labels)),
            FadeOut(highlight_text),
            run_time=0.6
        )
    
    def show_sum_formula(self):
        """场景5: 前n项和公式 (q≠1)"""
        # 场景标题
        scene_title = Text(
            "前n项和",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 条件说明
        condition = MathTex(
            r"\text{when } q \neq 1:",
            font_size=32,
            color=GRAY_A,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(condition), run_time=0.5)
        
        # 推导步骤
        step_y = 3.0
        step_gap = 0.9
        
        # Sn的展开式
        sum_expansion = MathTex(
            r"S_n = a_1 + a_1 q + a_1 q^2 + \cdots + a_1 q^{n-1}",
            font_size=30,
            color=WHITE
        ).move_to(np.array([0, step_y, 0]))
        
        # qSn的展开式
        q_sum_expansion = MathTex(
            r"q S_n = a_1 q + a_1 q^2 + \cdots + a_1 q^{n-1} + a_1 q^n",
            font_size=30,
            color=WHITE
        ).move_to(np.array([0, step_y - step_gap, 0]))
        
        # 错位相减
        subtraction = MathTex(
            r"S_n - q S_n = a_1 - a_1 q^n",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(np.array([0, step_y - 2 * step_gap, 0]))
        
        # 因式分解
        factorization = MathTex(
            r"S_n (1 - q) = a_1 (1 - q^n)",
            font_size=32,
            color=WHITE
        ).move_to(np.array([0, step_y - 3 * step_gap, 0]))
        
        # 最终公式
        final_formula = MathTex(
            r"S_n = \frac{a_1 (1 - q^n)}{1 - q}",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        # 逐步展示推导
        self.play(Write(sum_expansion), run_time=1.2)
        self.wait(0.5)
        
        self.play(Write(q_sum_expansion), run_time=1.2)
        self.wait(0.5)
        
        # 标注错位相减
        method_label = Text(
            "错位相减法",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(q_sum_expansion, RIGHT, buff=0.5)
        
        self.play(FadeIn(method_label, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.3)
        
        # 相减结果
        self.play(
            TransformMatchingTex(
                VGroup(sum_expansion.copy(), q_sum_expansion.copy()),
                subtraction
            ),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 因式分解
        self.play(Write(factorization), run_time=1.0)
        self.wait(0.5)
        
        self.play(FadeOut(method_label), run_time=0.3)
        
        # 最终公式
        formula_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.15,
            stroke_width=3
        )
        
        self.play(
            Write(final_formula),
            Create(formula_box),
            run_time=1.2
        )
        
        # 重点停留
        self.play(
            Indicate(final_formula, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(condition),
            FadeOut(sum_expansion),
            FadeOut(q_sum_expansion),
            FadeOut(subtraction),
            FadeOut(factorization),
            run_time=0.5
        )
        
        # 保留求和公式
        self.sum_formula_kept = VGroup(final_formula, formula_box)
        self.play(
            self.sum_formula_kept.animate.scale(0.65).move_to(UP * 4.5 + RIGHT * 0.5),
            run_time=0.5
        )
    
    def show_special_case(self):
        """场景6: 特殊情况 q=1"""
        # 场景标题
        scene_title = Text(
            "特殊情况",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 条件
        condition = MathTex(
            r"\text{when } q = 1:",
            font_size=36,
            color=self.COLOR_SECONDARY,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 3.5)
        
        self.play(Write(condition), run_time=0.6)
        
        # 说明
        explanation = Text(
            "数列变为常数列",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 常数列可视化 (所有项高度相同的矩形)
        constant_height = 1.2
        constant_rects = []
        
        for i in range(5):
            rect = Rectangle(
                width=0.5,
                height=constant_height,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.4,
                stroke_width=2
            )
            rect.move_to(np.array([-2.5 + i * 1.2, 0.5, 0]))
            constant_rects.append(rect)
        
        # 依次出现
        self.play(
            LaggedStart(
                *[FadeIn(rect, shift=UP * 0.3) for rect in constant_rects],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        # 标注相同
        equal_labels = []
        for i in range(4):
            label = MathTex(r"=", font_size=32, color=WHITE)
            label.move_to(
                (constant_rects[i].get_right() + constant_rects[i + 1].get_left()) / 2
            )
            equal_labels.append(label)
        
        self.play(
            LaggedStart(
                *[FadeIn(label) for label in equal_labels],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        
        # 求和公式
        sum_formula_q1 = MathTex(
            r"S_n = n \cdot a_1",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        formula_box = SurroundingRectangle(
            sum_formula_q1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.15,
            stroke_width=3
        )
        
        # 推导说明
        derivation = MathTex(
            r"S_n = a_1 + a_1 + \cdots + a_1 \text{ (n terms)}",
            font_size=28,
            color=GRAY_A,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(derivation), run_time=0.8)
        self.wait(0.5)
        
        self.play(
            Write(sum_formula_q1),
            Create(formula_box),
            run_time=1.0
        )
        
        # 强调简化
        emphasis = Text(
            "简化为等差数列求和!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(emphasis, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(condition),
            FadeOut(explanation),
            FadeOut(VGroup(*constant_rects)),
            FadeOut(VGroup(*equal_labels)),
            FadeOut(derivation),
            FadeOut(sum_formula_q1),
            FadeOut(formula_box),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_infinite_series(self):
        """场景7: 无穷等比数列 (|q|<1时)"""
        # 场景标题
        scene_title = Text(
            "无穷等比数列",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_GEOMETRIC
        ).move_to(UP * 6)
        
        self.play(Write(scene_title), run_time=0.6)
        
        # 条件
        condition = MathTex(
            r"\text{when } |q| < 1:",
            font_size=36,
            color=self.COLOR_SECONDARY,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 4.8)
        
        self.play(Write(condition), run_time=0.6)
        
        # 说明
        explanation = Text(
            "数列项趋于0, 级数收敛",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 衰减柱状图 (q=0.5)
        base_height = 2.5
        decay_factor = 0.5
        y_baseline = -1
        
        bars = []
        for i in range(7):
            height = base_height * (decay_factor ** i)
            bar = Rectangle(
                width=0.5,
                height=height,
                color=self.COLOR_GEOMETRIC,
                fill_opacity=0.5,
                stroke_width=2
            )
            bar.move_to(np.array([-3 + i * 1.0, y_baseline + height / 2, 0]))
            bars.append(bar)
        
        # 依次出现
        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, DOWN) for bar in bars],
                lag_ratio=0.15
            ),
            run_time=2.0
        )
        
        # 极限线
        limit_line = DashedLine(
            LEFT * 4 + y_baseline * UP,
            RIGHT * 4 + y_baseline * UP,
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.1,
            stroke_width=2
        )
        
        limit_label = Text(
            "y = 0",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(limit_line, RIGHT, buff=0.2)
        
        self.play(
            Create(limit_line),
            FadeIn(limit_label),
            run_time=0.8
        )
        
        # 无穷和公式
        infinity_formula = MathTex(
            r"S_{\infty} = \frac{a_1}{1 - q}",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        formula_box = SurroundingRectangle(
            infinity_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.15,
            stroke_width=3
        )
        
        # 推导说明
        derivation = MathTex(
            r"\lim_{n \to \infty} q^n = 0",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(derivation), run_time=0.6)
        self.wait(0.4)
        
        self.play(
            Write(infinity_formula),
            Create(formula_box),
            run_time=1.0
        )
        
        # 收敛动画
        self.play(
            Indicate(limit_line, scale_factor=1.0, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(condition),
            FadeOut(explanation),
            FadeOut(VGroup(*bars)),
            FadeOut(limit_line),
            FadeOut(limit_label),
            FadeOut(derivation),
            FadeOut(infinity_formula),
            FadeOut(formula_box),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结与片尾"""
        # 清理之前保留的公式
        self.play(
            FadeOut(self.title_small),
            FadeOut(self.general_formula_kept),
            FadeOut(self.sum_formula_kept),
            run_time=0.5
        )
        
        # 核心公式汇总
        summary_title = Text(
            "等比数列核心公式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 公式卡片
        cards = VGroup()
        
        card_data = [
            ("通项", r"a_n = a_1 \cdot q^{n-1}", self.COLOR_PRIMARY),
            ("求和(q≠1)", r"S_n = \frac{a_1(1-q^n)}{1-q}", self.COLOR_FORMULA),
            ("求和(q=1)", r"S_n = n \cdot a_1", self.COLOR_SECONDARY),
            ("无穷和", r"S_{\infty} = \frac{a_1}{1-q} \; (|q|<1)", self.COLOR_GEOMETRIC)
        ]
        
        y_start = 2.5
        y_gap = 1.8
        
        for i, (title, formula, color) in enumerate(card_data):
            # 标题
            title_text = Text(
                title,
                font="PingFang SC",
                font_size=28,
                color=color
            )
            
            # 公式
            formula_tex = MathTex(
                formula,
                font_size=32,
                color=WHITE
            )
            
            # 组合
            card = VGroup(title_text, formula_tex).arrange(RIGHT, buff=0.5)
            card.move_to(np.array([0, y_start - i * y_gap, 0]))
            
            # 边框
            box = SurroundingRectangle(
                card,
                color=color,
                buff=0.2,
                corner_radius=0.1,
                stroke_width=2
            )
            
            card_group = VGroup(box, card)
            cards.add(card_group)
            
            # 初始位置在左侧外
            card_group.shift(LEFT * 10)
        
        # 卡片依次滑入
        for card in cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 清理并放大作者信息
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
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
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰: 数字序列闪烁
        decoration_numbers = VGroup(*[
            Text(str(2**i), font="PingFang SC", font_size=24, color=self.COLOR_PRIMARY)
            for i in range(6)
        ])
        decoration_numbers.arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(num, scale=0.5) for num in decoration_numbers],
                lag_ratio=0.1
            ),
            run_time=1.0
        )
        
        # 箭头动画
        decoration_arrows = VGroup()
        for i in range(5):
            arrow = Arrow(
                decoration_numbers[i].get_right() + RIGHT * 0.05,
                decoration_numbers[i + 1].get_left() + LEFT * 0.05,
                buff=0,
                color=self.COLOR_SECONDARY,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.1
            )
            decoration_arrows.add(arrow)
        
        self.play(
            LaggedStart(
                *[GrowArrow(arrow) for arrow in decoration_arrows],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_numbers),
            FadeOut(decoration_arrows),
            run_time=1.0
        )


# 运行命令:
# manim -pql geometric_sequence.py GeometricSequence  # 快速预览
# manim -qh geometric_sequence.py GeometricSequence   # 高质量 (1080p)
# manim -qk geometric_sequence.py GeometricSequence   # 4K质量