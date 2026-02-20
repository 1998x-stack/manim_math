"""
向量的线性运算 - Vector Linear Operations
使用 Manim 创建的九年级数学教学视频

知识点: 向量的线性运算
- 向量加法（三角形法则、平行四边形法则）
- 向量数乘（伸缩变换）
- 基底与向量分解
- 平行向量

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


class VectorLinearOperations(Scene):
    """
    向量线性运算教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 向量加法
    3. 向量数乘
    4. 基底概念
    5. 向量分解
    6. 平行向量
    7. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_VECTOR_A = "#e74c3c"        # 红色 - 向量a
        self.COLOR_VECTOR_B = "#3498db"        # 蓝色 - 向量b
        self.COLOR_VECTOR_SUM = "#2ecc71"      # 绿色 - 和向量
        self.COLOR_BASIS_E1 = "#f39c12"        # 橙色 - 基向量e1
        self.COLOR_BASIS_E2 = "#9b59b6"        # 紫色 - 基向量e2
        self.COLOR_HIGHLIGHT = YELLOW          # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助线
        self.COLOR_AXES = WHITE                # 白色 - 坐标轴
        
        # 初始化向量数据
        self.setup_vectors()
        
        # 执行动画序列
        self.show_opening()
        self.show_vector_addition()
        self.show_scalar_multiplication()
        self.show_basis_concept()
        self.show_vector_decomposition()
        self.show_parallel_vectors()
        self.show_summary()
    
    def setup_vectors(self):
        """初始化所有向量数据"""
        # ========== 原点 ==========
        self.origin = ORIGIN
        
        # ========== 基本向量 ==========
        self.vec_a = np.array([2, 1, 0])
        self.vec_b = np.array([1, 2, 0])
        
        # ========== 向量加法 ==========
        self.vec_sum = self.vec_a + self.vec_b
        
        # ========== 向量数乘 ==========
        self.vec_2a = 2 * self.vec_a
        self.vec_half_a = 0.5 * self.vec_a
        self.vec_neg_a = -1 * self.vec_a
        
        # ========== 基向量 ==========
        self.e1 = np.array([1, 0, 0])
        self.e2 = np.array([0.5, 1, 0])
        
        # 计算分解系数
        A_matrix = np.column_stack([self.e1[:2], self.e2[:2]])
        lambdas = np.linalg.solve(A_matrix, self.vec_a[:2])
        self.lambda1 = lambdas[0]
        self.lambda2 = lambdas[1]
        
        # ========== 平行向量 ==========
        self.vec_b_parallel = 2 * self.vec_a
        
        print("✓ 向量数据初始化完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "什么是向量？\n它有什么用？",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 几个示例箭头
        example_arrows = VGroup(
            Arrow(ORIGIN, RIGHT * 1.5, color=RED, buff=0).shift(UP * 2),
            Arrow(ORIGIN, UP * 1.5, color=BLUE, buff=0).shift(UP * 2 + RIGHT * 2),
            Arrow(ORIGIN, UR * 1.2, color=GREEN, buff=0).shift(UP * 2 + LEFT * 2)
        )
        
        for arrow in example_arrows:
            self.play(GrowArrow(arrow), run_time=0.4)
        
        # 闪烁
        self.play(
            *[Flash(arrow.get_end(), color=arrow.get_color(), flash_radius=0.3) for arrow in example_arrows],
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(example_arrows),
            run_time=0.5
        )
    
    def show_vector_addition(self):
        """场景2: 向量加法"""
        # 标题
        title = Text(
            "向量的加法",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建向量 a
        arrow_a = Arrow(
            self.origin, self.vec_a,
            color=self.COLOR_VECTOR_A,
            buff=0,
            stroke_width=6
        ).shift(UP * 1.5)
        
        label_a = MathTex(r"\vec{a}", font_size=28, color=self.COLOR_VECTOR_A).next_to(arrow_a, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_a), run_time=0.8)
        self.play(Write(label_a), run_time=0.4)
        
        # 创建向量 b
        arrow_b = Arrow(
            self.origin, self.vec_b,
            color=self.COLOR_VECTOR_B,
            buff=0,
            stroke_width=6
        ).shift(UP * 1.5)
        
        label_b = MathTex(r"\vec{b}", font_size=28, color=self.COLOR_VECTOR_B).next_to(arrow_b, UP, buff=0.2)
        
        self.play(GrowArrow(arrow_b), run_time=0.8)
        self.play(Write(label_b), run_time=0.4)
        
        # 说明：首尾相接
        explanation = Text(
            "首尾相接",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        # 平移向量 b 到 a 的终点
        arrow_b_shifted = Arrow(
            arrow_a.get_end(), arrow_a.get_end() + self.vec_b,
            color=self.COLOR_VECTOR_B,
            buff=0,
            stroke_width=6
        )
        
        label_b_shifted = MathTex(r"\vec{b}", font_size=28, color=self.COLOR_VECTOR_B).next_to(
            arrow_b_shifted.get_center(), RIGHT, buff=0.2
        )
        
        self.play(
            Transform(arrow_b.copy(), arrow_b_shifted),
            Transform(label_b.copy(), label_b_shifted),
            run_time=1.2
        )
        
        self.add(arrow_b_shifted, label_b_shifted)
        
        # 绘制和向量
        arrow_sum = Arrow(
            self.origin, self.vec_sum,
            color=self.COLOR_VECTOR_SUM,
            buff=0,
            stroke_width=8
        ).shift(UP * 1.5)
        
        label_sum = MathTex(r"\vec{a}+\vec{b}", font_size=30, color=self.COLOR_VECTOR_SUM).next_to(
            arrow_sum.get_center(), UL, buff=0.2
        )
        
        self.play(GrowArrow(arrow_sum), run_time=1.0)
        self.play(Write(label_sum), run_time=0.6)
        
        self.wait(1.0)
        
        # 过渡：平行四边形法则
        self.play(FadeOut(explanation), run_time=0.3)
        
        transition = Text(
            "平行四边形法则",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(transition), run_time=0.8)
        
        # 绘制平行四边形
        para_line_1 = DashedLine(
            arrow_a.get_end(), arrow_sum.get_end(),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        para_line_2 = DashedLine(
            arrow_b.get_end(), arrow_sum.get_end(),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(
            Create(para_line_1),
            Create(para_line_2),
            run_time=1.5
        )
        
        # 强调
        emphasis = Text(
            "两种方法，同一结果",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GOLD
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(emphasis),
            Flash(arrow_sum.get_end(), color=self.COLOR_VECTOR_SUM, flash_radius=0.5),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow_a),
            FadeOut(arrow_b),
            FadeOut(arrow_b_shifted),
            FadeOut(arrow_sum),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_b_shifted),
            FadeOut(label_sum),
            FadeOut(para_line_1),
            FadeOut(para_line_2),
            FadeOut(transition),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_scalar_multiplication(self):
        """场景3: 向量数乘"""
        # 标题
        title = Text(
            "向量的数乘",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 原向量 a
        arrow_a = Arrow(
            self.origin, self.vec_a,
            color=self.COLOR_VECTOR_A,
            buff=0,
            stroke_width=6
        ).shift(UP * 1.5)
        
        label_a = MathTex(r"\vec{a}", font_size=28, color=self.COLOR_VECTOR_A).next_to(arrow_a, DOWN, buff=0.2)
        
        self.play(GrowArrow(arrow_a), Write(label_a), run_time=0.8)
        self.play(Indicate(arrow_a), run_time=0.5)
        
        # 说明：λ > 0，同向
        explanation_pos = Text(
            "λ > 0，同向",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation_pos), run_time=0.8)
        
        # 2a
        arrow_2a = Arrow(
            self.origin, self.vec_2a,
            color=self.COLOR_VECTOR_A,
            buff=0,
            stroke_width=6
        ).shift(DOWN * 1.5)
        
        # Apply opacity separately if needed
        arrow_2a.set_opacity(0.7)
        
        label_2a = MathTex(r"2\vec{a}", font_size=28, color=self.COLOR_VECTOR_A).next_to(arrow_2a, DOWN, buff=0.2)
        
        self.play(GrowArrow(arrow_2a), run_time=1.0)
        self.play(Write(label_2a), run_time=0.5)
        
        # 0.5a
        arrow_half_a = Arrow(
            self.origin, self.vec_half_a,
            color=self.COLOR_VECTOR_A,
            buff=0,
            stroke_width=6
        ).shift(UP * 0)
        
        # Apply opacity separately if needed
        arrow_half_a.set_opacity(0.5)
        
        label_half_a = MathTex(r"0.5\vec{a}", font_size=26, color=self.COLOR_VECTOR_A).next_to(
            arrow_half_a, DOWN, buff=0.15
        )
        
        self.play(GrowArrow(arrow_half_a), run_time=1.0)
        self.play(Write(label_half_a), run_time=0.5)
        
        self.wait(1.0)
        
        # 说明：λ < 0，反向
        self.play(FadeOut(explanation_pos), run_time=0.3)
        
        explanation_neg = Text(
            "λ < 0，反向",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation_neg), run_time=0.8)
        
        # -a
        arrow_neg_a = Arrow(
            self.origin, self.vec_neg_a,
            color=PURPLE,
            buff=0,
            stroke_width=6
        ).shift(UP * 3.5)
        
        label_neg_a = MathTex(r"-\vec{a}", font_size=28, color=PURPLE).next_to(arrow_neg_a, DOWN, buff=0.2)
        
        self.play(GrowArrow(arrow_neg_a), run_time=1.0)
        self.play(Write(label_neg_a), run_time=0.5)
        
        # 强调
        emphasis = Text(
            "方向相反，长度相同",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GOLD
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(emphasis),
            Flash(arrow_neg_a.get_end(), color=PURPLE, flash_radius=0.4),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow_a),
            FadeOut(arrow_2a),
            FadeOut(arrow_half_a),
            FadeOut(arrow_neg_a),
            FadeOut(label_a),
            FadeOut(label_2a),
            FadeOut(label_half_a),
            FadeOut(label_neg_a),
            FadeOut(explanation_neg),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_basis_concept(self):
        """场景4: 基底概念"""
        # 标题
        title = Text(
            "基底",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": self.COLOR_AXES, "stroke_width": 1.5},
            tips=False
        ).shift(DOWN * 0.5)
        
        self.play(Create(axes), run_time=1.0)
        
        # 基向量 e1
        arrow_e1 = Arrow(
            axes.c2p(0, 0), axes.c2p(self.e1[0], self.e1[1]),
            color=self.COLOR_BASIS_E1,
            buff=0,
            stroke_width=6
        )
        
        label_e1 = MathTex(r"\vec{e}_1", font_size=28, color=self.COLOR_BASIS_E1).next_to(
            arrow_e1, DOWN, buff=0.15
        )
        
        self.play(GrowArrow(arrow_e1), run_time=0.8)
        self.play(Write(label_e1), run_time=0.4)
        
        # 基向量 e2
        arrow_e2 = Arrow(
            axes.c2p(0, 0), axes.c2p(self.e2[0], self.e2[1]),
            color=self.COLOR_BASIS_E2,
            buff=0,
            stroke_width=6
        )
        
        label_e2 = MathTex(r"\vec{e}_2", font_size=28, color=self.COLOR_BASIS_E2).next_to(
            arrow_e2, LEFT, buff=0.15
        )
        
        self.play(GrowArrow(arrow_e2), run_time=0.8)
        self.play(Write(label_e2), run_time=0.4)
        
        # 说明
        explanation = Text(
            "不共线！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        # 强调不共线
        self.play(
            Wiggle(arrow_e1, scale_value=1.2),
            Wiggle(arrow_e2, scale_value=1.2),
            run_time=1.0
        )
        
        # 过渡
        transition = Text(
            "任意向量都可以分解",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(transition), run_time=1.2)
        
        self.wait(2.0)
        
        # 保留坐标系和基向量，清理其他
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(transition),
            run_time=0.5
        )
        
        # 保存为场景变量供下一场景使用
        self.axes = axes
        self.arrow_e1 = arrow_e1
        self.arrow_e2 = arrow_e2
        self.label_e1 = label_e1
        self.label_e2 = label_e2
    
    def show_vector_decomposition(self):
        """场景5: 向量分解"""
        # 标题
        title = Text(
            "向量的分解",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 目标向量 a
        arrow_a = Arrow(
            self.axes.c2p(0, 0), self.axes.c2p(self.vec_a[0], self.vec_a[1]),
            color=RED,
            buff=0,
            stroke_width=7
        )
        
        label_a = MathTex(r"\vec{a}", font_size=30, color=RED).next_to(arrow_a, UR, buff=0.15)
        
        self.play(GrowArrow(arrow_a), run_time=1.0)
        self.play(Write(label_a), run_time=0.4)
        
        # 问题
        question = Text(
            "如何用 e₁ 和 e₂ 表示 a？",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(question), run_time=1.0)
        
        # 从 a 的终点画平行线
        a_end = self.axes.c2p(self.vec_a[0], self.vec_a[1])
        
        # 平行于 e2 的线
        parallel_e2_start = a_end
        parallel_e2_end = self.axes.c2p(self.lambda1 * self.e1[0], 0)
        parallel_e2 = DashedLine(
            parallel_e2_start, parallel_e2_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        # 平行于 e1 的线
        parallel_e1_start = a_end
        parallel_e1_end = self.axes.c2p(0, self.lambda2 * self.e2[1])
        parallel_e1 = DashedLine(
            parallel_e1_start, parallel_e1_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(parallel_e2), run_time=1.0)
        self.play(Create(parallel_e1), run_time=1.0)
        
        # λ1·e1 向量
        arrow_lambda1_e1 = Arrow(
            self.axes.c2p(0, 0), self.axes.c2p(self.lambda1 * self.e1[0], 0),
            color=self.COLOR_BASIS_E1,
            buff=0,
            stroke_width=5
        )
        
        label_lambda1_e1 = MathTex(
            rf"{self.lambda1:.1f}\vec{{e}}_1",
            font_size=24,
            color=self.COLOR_BASIS_E1
        ).next_to(arrow_lambda1_e1, DOWN, buff=0.1)
        
        self.play(
            Indicate(arrow_lambda1_e1),
            run_time=0.8
        )
        self.play(GrowArrow(arrow_lambda1_e1), run_time=0.8)
        self.play(Write(label_lambda1_e1), run_time=0.5)
        
        # λ2·e2 向量
        arrow_lambda2_e2 = Arrow(
            self.axes.c2p(0, 0), self.axes.c2p(0, self.lambda2 * self.e2[1]),
            color=self.COLOR_BASIS_E2,
            buff=0,
            stroke_width=5
        )
        
        label_lambda2_e2 = MathTex(
            rf"{self.lambda2:.1f}\vec{{e}}_2",
            font_size=24,
            color=self.COLOR_BASIS_E2
        ).next_to(arrow_lambda2_e2, LEFT, buff=0.1)
        
        self.play(
            Indicate(arrow_lambda2_e2),
            run_time=0.8
        )
        self.play(GrowArrow(arrow_lambda2_e2), run_time=0.8)
        self.play(Write(label_lambda2_e2), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\vec{a} = \lambda_1\vec{e}_1 + \lambda_2\vec{e}_2",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeOut(question),
            FadeIn(formula),
            run_time=1.0
        )
        
        # 具体数值
        specific_formula = MathTex(
            rf"\vec{{a}} = {self.lambda1:.1f}\vec{{e}}_1 + {self.lambda2:.1f}\vec{{e}}_2",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 6.5)
        
        self.play(Write(specific_formula), run_time=1.2)
        self.play(Flash(specific_formula.get_center(), color=GOLD, flash_radius=0.8), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.axes),
            FadeOut(self.arrow_e1),
            FadeOut(self.arrow_e2),
            FadeOut(self.label_e1),
            FadeOut(self.label_e2),
            FadeOut(arrow_a),
            FadeOut(label_a),
            FadeOut(parallel_e1),
            FadeOut(parallel_e2),
            FadeOut(arrow_lambda1_e1),
            FadeOut(arrow_lambda2_e2),
            FadeOut(label_lambda1_e1),
            FadeOut(label_lambda2_e2),
            FadeOut(formula),
            FadeOut(specific_formula),
            run_time=0.6
        )
    
    def show_parallel_vectors(self):
        """场景6: 平行向量"""
        # 标题
        title = Text(
            "平行向量",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 向量 a
        arrow_a = Arrow(
            self.origin, self.vec_a,
            color=self.COLOR_VECTOR_A,
            buff=0,
            stroke_width=6
        ).shift(UP * 1.5)
        
        label_a = MathTex(r"\vec{a}", font_size=28, color=self.COLOR_VECTOR_A).next_to(arrow_a, DOWN, buff=0.2)
        
        self.play(GrowArrow(arrow_a), Write(label_a), run_time=1.0)
        
        # 平行向量 b = 2a
        arrow_b_parallel = Arrow(
            self.origin, self.vec_b_parallel,
            color=self.COLOR_VECTOR_B,
            buff=0,
            stroke_width=6
        ).shift(DOWN * 1.5)
        
        label_b_parallel = MathTex(r"\vec{b}", font_size=28, color=self.COLOR_VECTOR_B).next_to(
            arrow_b_parallel, DOWN, buff=0.2
        )
        
        self.play(GrowArrow(arrow_b_parallel), run_time=1.0)
        self.play(Write(label_b_parallel), run_time=0.5)
        
        # 平行符号
        parallel_symbol = MathTex(r"\parallel", font_size=40, color=YELLOW).move_to(LEFT * 3 + UP * 0.5)
        
        self.play(Create(parallel_symbol), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\vec{a} \parallel \vec{b} \Leftrightarrow \vec{a} = \lambda\vec{b}",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(formula), run_time=1.0)
        
        # 说明
        explanation = Text(
            "方向相同或相反",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=1.0)
        
        # 示例
        example = MathTex(
            r"\vec{b} = 2\vec{a}",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 6.5)
        
        self.play(Write(example), run_time=1.0)
        self.play(Flash(arrow_b_parallel.get_end(), color=self.COLOR_VECTOR_B, flash_radius=0.5), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow_a),
            FadeOut(arrow_b_parallel),
            FadeOut(label_a),
            FadeOut(label_b_parallel),
            FadeOut(parallel_symbol),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(example),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结 + 片尾"""
        # 总结卡片
        card_1 = self.create_summary_card(
            "向量加法 - 首尾相接",
            UP * 2.5
        )
        
        card_2 = self.create_summary_card(
            "向量数乘 - 伸缩变换",
            UP * 1
        )
        
        card_3 = self.create_summary_card(
            "基底分解 - a=λ₁e₁+λ₂e₂",
            DOWN * 0.5
        )
        
        card_4 = self.create_summary_card(
            "平行向量 - a=λb",
            DOWN * 2
        )
        
        self.play(card_1.animate.shift(RIGHT * 0), run_time=0.8)
        self.wait(0.1)
        self.play(card_2.animate.shift(RIGHT * 0), run_time=0.8)
        self.wait(0.1)
        self.play(card_3.animate.shift(RIGHT * 0), run_time=0.8)
        self.wait(0.1)
        self.play(card_4.animate.shift(RIGHT * 0), run_time=0.8)
        
        all_cards = VGroup(card_1, card_2, card_3, card_4)
        
        # 闪烁
        self.play(
            *[Flash(card.get_center(), color=YELLOW, flash_radius=0.5) for card in all_cards],
            run_time=0.6
        )
        
        # 关键提示
        key_point = Text(
            "理解向量，掌握线性代数基础！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GOLD
        ).move_to(DOWN * 4)
        
        self.play(Write(key_point), run_time=1.2)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.7)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.8)
        
        # 装饰动画（箭头旋转）
        decorations = VGroup(*[
            Arrow(ORIGIN, RIGHT * 0.3, color=GOLD, buff=0, stroke_width=4)
            .rotate(i * TAU / 5, about_point=ORIGIN)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * TAU / 5), np.sin(i * TAU / 5), 0]))
            for i in range(5)
        ])
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=TAU, run_time=2.0))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(all_cards),
            FadeOut(key_point),
            FadeOut(self.author_info),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )
    
    def create_summary_card(self, content, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=self.COLOR_HIGHLIGHT, fill_opacity=1, stroke_width=0)
        
        # 内容
        text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql vector_linear_operations.py VectorLinearOperations  # 快速预览
# manim -qh vector_linear_operations.py VectorLinearOperations   # 高质量渲染