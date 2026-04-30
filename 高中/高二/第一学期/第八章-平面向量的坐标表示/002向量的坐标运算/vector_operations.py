"""
平面向量的坐标运算 - Vector Coordinate Operations
使用 Manim 创建的高中数学教学视频

内容: 向量加法、减法、数乘、平行条件
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


class VectorCoordinateOperations(Scene):
    """
    平面向量坐标运算教学动画
    
    场景顺序:
    1. 开场钩子
    2. 向量表示
    3. 向量加法
    4. 向量减法
    5. 数乘运算
    6. 平行条件
    7. 总结关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_VECTOR_A = "#e74c3c"      # 红色 - 向量a
        self.COLOR_VECTOR_B = "#3498db"      # 蓝色 - 向量b
        self.COLOR_RESULT = "#2ecc71"        # 绿色 - 结果向量
        self.COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
        self.COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助
        self.COLOR_COORDINATE = WHITE        # 白色 - 坐标轴
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_vector_representation()
        self.show_vector_addition()
        self.show_vector_subtraction()
        self.show_scalar_multiplication()
        self.show_parallel_condition()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化所有向量和坐标数据"""
        # 坐标系配置
        self.SCALE = 0.8
        self.OFFSET = UP * 1.0
        
        # 向量a的坐标 (2, 1)
        self.a_coords = np.array([2, 1, 0])
        self.a_start = ORIGIN
        self.a_end = self.a_coords * self.SCALE + self.OFFSET
        
        # 向量b的坐标 (1, 2)
        self.b_coords = np.array([1, 2, 0])
        self.b_start = ORIGIN
        self.b_end = self.b_coords * self.SCALE + self.OFFSET
        
        # 向量加法结果 (3, 3)
        self.sum_coords = self.a_coords + self.b_coords
        self.sum_end = self.sum_coords * self.SCALE + self.OFFSET
        
        # 向量减法结果 (1, -1)
        self.diff_coords = self.a_coords - self.b_coords
        self.diff_end = self.diff_coords * self.SCALE + self.OFFSET
        
        # 数乘结果 2a (4, 2)
        self.scaled_coords = 2 * self.a_coords
        self.scaled_end = self.scaled_coords * self.SCALE + self.OFFSET
        
        # 验证计算
        self.verify_geometry()
        
        # 创建坐标系（但不添加到场景）
        self.axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-2, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "include_numbers": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).scale(self.SCALE).shift(self.OFFSET)
        
        # 坐标轴标签
        self.x_label = MathTex("x").next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        self.y_label = MathTex("y").next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
    
    def verify_geometry(self):
        """验证向量计算的正确性"""
        epsilon = 1e-6
        
        # 验证加法
        sum_check = self.a_coords + self.b_coords
        if not np.allclose(self.sum_coords, sum_check, atol=epsilon):
            print(f"WARNING: 向量加法计算错误!")
        
        # 验证减法
        diff_check = self.a_coords - self.b_coords
        if not np.allclose(self.diff_coords, diff_check, atol=epsilon):
            print(f"WARNING: 向量减法计算错误!")
        
        # 验证数乘
        scaled_check = 2 * self.a_coords
        if not np.allclose(self.scaled_coords, scaled_check, atol=epsilon):
            print(f"WARNING: 向量数乘计算错误!")
        
        print("✓ 向量计算验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color="#95a5a6"
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "向量怎么算？",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        self.wait(0.5)
        
        # 创建坐标系
        self.play(
            Create(self.axes),
            Write(self.x_label),
            Write(self.y_label),
            run_time=1.2
        )
        self.wait(0.8)
        
        # 清理钩子
        self.play(FadeOut(hook), run_time=0.4)
    
    def show_vector_representation(self):
        """场景2: 向量的坐标表示"""
        # 标题
        title = Text(
            "向量的坐标表示",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 绘制向量a
        vector_a = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(2, 1),
            buff=0,
            color=self.COLOR_VECTOR_A,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        label_a = MathTex(
            r"\vec{a} = (2, 1)",
            color=self.COLOR_VECTOR_A,
            font_size=28
        ).next_to(vector_a.get_end(), UR, buff=0.2)
        
        self.play(GrowArrow(vector_a), run_time=0.8)
        self.play(Write(label_a), run_time=0.5)
        self.wait(0.5)
        
        # 绘制向量b
        vector_b = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(1, 2),
            buff=0,
            color=self.COLOR_VECTOR_B,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        label_b = MathTex(
            r"\vec{b} = (1, 2)",
            color=self.COLOR_VECTOR_B,
            font_size=28
        ).next_to(vector_b.get_end(), UL, buff=0.2)
        
        self.play(GrowArrow(vector_b), run_time=0.8)
        self.play(Write(label_b), run_time=0.5)
        
        # 通用公式
        formula = MathTex(
            r"\vec{v} = (x, y)",
            font_size=26,
            color="#95a5a6"
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(1.5)
        
        # 保存对象供后续使用
        self.vector_a = vector_a
        self.vector_b = vector_b
        self.label_a = label_a
        self.label_b = label_b
        
        # 清理
        self.play(FadeOut(title), FadeOut(formula), run_time=0.4)
    
    def show_vector_addition(self):
        """场景3: 向量加法"""
        # 标题
        title = Text(
            "向量加法",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 平移向量b到向量a的终点
        vector_b_copy = Arrow(
            self.axes.c2p(2, 1),
            self.axes.c2p(3, 3),
            buff=0,
            color=self.COLOR_VECTOR_B,
            stroke_opacity=0.5,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )
        
        b_copy_label = MathTex(
            r"\vec{b}",
            color=self.COLOR_VECTOR_B,
            font_size=24
        ).next_to(vector_b_copy.get_center(), RIGHT, buff=0.15)
        
        self.play(
            TransformFromCopy(self.vector_b, vector_b_copy),
            TransformFromCopy(self.label_b, b_copy_label),
            run_time=1.0
        )
        
        # 平行四边形辅助线
        parallelogram = Polygon(
            self.axes.c2p(0, 0),
            self.axes.c2p(2, 1),
            self.axes.c2p(3, 3),
            self.axes.c2p(1, 2),
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            stroke_opacity=0.3,
            fill_opacity=0
        )
        
        self.play(Create(parallelogram), run_time=0.8)
        
        # 结果向量
        result_vector = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(3, 3),
            buff=0,
            color=self.COLOR_RESULT,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.15
        )
        
        result_label = MathTex(
            r"\vec{a} + \vec{b} = (3, 3)",
            color=self.COLOR_RESULT,
            font_size=28
        ).next_to(result_vector.get_end(), UR, buff=0.25)
        
        self.play(GrowArrow(result_vector), run_time=1.0)
        self.play(Write(result_label), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\vec{a} + \vec{b} = (x_1 + x_2, y_1 + y_2)",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        calculation = MathTex(
            r"= (2 + 1, 1 + 2) = (3, 3)",
            font_size=24,
            color="#95a5a6"
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(FadeIn(formula), run_time=0.5)
        self.play(Write(calculation), run_time=0.8)
        
        # 高亮结果
        self.play(Indicate(result_vector, scale_factor=1.1), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(parallelogram),
            FadeOut(vector_b_copy),
            FadeOut(b_copy_label),
            FadeOut(result_vector),
            FadeOut(result_label),
            FadeOut(formula),
            FadeOut(calculation),
            run_time=0.6
        )
    
    def show_vector_subtraction(self):
        """场景4: 向量减法"""
        # 标题
        title = Text(
            "向量减法",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 绘制-b向量
        neg_vector_b = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(-1, -2),
            buff=0,
            color=self.COLOR_VECTOR_B,
            stroke_width=6,
            stroke_opacity=0.6,
            max_tip_length_to_length_ratio=0.15
        )
        
        neg_label = MathTex(
            r"-\vec{b} = (-1, -2)",
            color=self.COLOR_VECTOR_B,
            font_size=26
        ).next_to(neg_vector_b.get_end(), DL, buff=0.2)
        
        self.play(GrowArrow(neg_vector_b), run_time=0.8)
        self.play(Write(neg_label), run_time=0.5)
        
        # 说明
        explanation = Text(
            "减法 = 加上相反向量",
            font="PingFang SC",
            font_size=22,
            color="#95a5a6"
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 结果向量
        diff_vector = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(1, -1),
            buff=0,
            color=self.COLOR_RESULT,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.15
        )
        
        diff_label = MathTex(
            r"\vec{a} - \vec{b} = (1, -1)",
            color=self.COLOR_RESULT,
            font_size=28
        ).next_to(diff_vector.get_end(), DR, buff=0.25)
        
        self.play(
            FadeOut(explanation),
            GrowArrow(diff_vector),
            run_time=0.8
        )
        self.play(Write(diff_label), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\vec{a} - \vec{b} = (x_1 - x_2, y_1 - y_2)",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 5)
        
        calculation = MathTex(
            r"= (2 - 1, 1 - 2) = (1, -1)",
            font_size=24,
            color="#95a5a6"
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(FadeIn(formula), run_time=0.5)
        self.play(Write(calculation), run_time=0.8)
        
        # 高亮结果
        self.play(Indicate(diff_vector, scale_factor=1.1), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(neg_vector_b),
            FadeOut(neg_label),
            FadeOut(diff_vector),
            FadeOut(diff_label),
            FadeOut(formula),
            FadeOut(calculation),
            run_time=0.6
        )
    
    def show_scalar_multiplication(self):
        """场景5: 数乘运算"""
        # 标题
        title = Text(
            "数乘运算",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 复制向量a用于变换
        vector_a_copy = self.vector_a.copy()
        
        # 2倍向量
        scaled_vector = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(4, 2),
            buff=0,
            color=self.COLOR_RESULT,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.15
        )
        
        scaled_label = MathTex(
            r"2\vec{a} = (4, 2)",
            color=self.COLOR_RESULT,
            font_size=28
        ).next_to(scaled_vector.get_end(), UR, buff=0.25)
        
        self.play(
            Transform(vector_a_copy, scaled_vector),
            run_time=1.2
        )
        self.play(Write(scaled_label), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\lambda \vec{a} = (\lambda x, \lambda y)",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        calculation = MathTex(
            r"2\vec{a} = (2 \times 2, 2 \times 1) = (4, 2)",
            font_size=24,
            color="#95a5a6"
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(FadeIn(formula), run_time=0.5)
        self.play(Write(calculation), run_time=0.8)
        
        # 长度对比标注
        brace_original = Brace(self.vector_a, direction=DOWN, buff=0.1, color=self.COLOR_VECTOR_A)
        brace_label_1 = Text(
            "长度 = L",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_VECTOR_A
        ).next_to(brace_original, DOWN, buff=0.1)
        
        brace_scaled = Brace(vector_a_copy, direction=UP, buff=0.1, color=self.COLOR_RESULT)
        brace_label_2 = Text(
            "长度 = 2L",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_RESULT
        ).next_to(brace_scaled, UP, buff=0.1)
        
        self.play(
            FadeIn(brace_original),
            Write(brace_label_1),
            FadeIn(brace_scaled),
            Write(brace_label_2),
            run_time=1.0
        )
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(vector_a_copy),
            FadeOut(scaled_label),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(brace_original),
            FadeOut(brace_label_1),
            FadeOut(brace_scaled),
            FadeOut(brace_label_2),
            run_time=0.6
        )
    
    def show_parallel_condition(self):
        """场景6: 平行条件"""
        # 标题
        title = Text(
            "向量平行条件",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 示例平行向量 c = (2, 1), d = (4, 2)
        vector_c = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(2, 1),
            buff=0,
            color="#e74c3c",
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        vector_d = Arrow(
            self.axes.c2p(0, -1),
            self.axes.c2p(4, 1),
            buff=0,
            color="#c0392b",
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        label_c = MathTex(
            r"\vec{c} = (2, 1)",
            color="#e74c3c",
            font_size=26
        ).next_to(vector_c.get_end(), UR, buff=0.2)
        
        label_d = MathTex(
            r"\vec{d} = (4, 2)",
            color="#c0392b",
            font_size=26
        ).next_to(vector_d.get_end(), DR, buff=0.2)
        
        self.play(
            GrowArrow(vector_c),
            GrowArrow(vector_d),
            run_time=1.0
        )
        self.play(
            Write(label_c),
            Write(label_d),
            run_time=0.6
        )
        
        # 平行标记
        parallel_text = Text(
            "c ∥ d",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(parallel_text, scale=1.2), run_time=0.5)
        self.wait(0.5)
        
        # 公式
        formula = MathTex(
            r"\vec{a} \parallel \vec{b} \Leftrightarrow x_1 y_2 - x_2 y_1 = 0",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(formula), run_time=0.8)
        
        # 验证计算
        verification = MathTex(
            r"2 \times 2 - 4 \times 1 = 4 - 4 = 0 \; \checkmark",
            font_size=24,
            color=self.COLOR_RESULT
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(Write(verification), run_time=1.0)
        
        # 高亮关键
        self.play(
            Indicate(formula),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(vector_c),
            FadeOut(vector_d),
            FadeOut(label_c),
            FadeOut(label_d),
            FadeOut(parallel_text),
            FadeOut(formula),
            FadeOut(verification),
            run_time=0.6
        )
        
        # 清理原始向量
        self.play(
            FadeOut(self.vector_a),
            FadeOut(self.vector_b),
            FadeOut(self.label_a),
            FadeOut(self.label_b),
            run_time=0.4
        )
    
    def show_summary(self):
        """场景7: 总结与关注"""
        # 清理坐标系
        self.play(
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "向量坐标运算总结",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 创建公式卡片
        card_1 = self.create_formula_card(
            "加法",
            r"\vec{a} + \vec{b} = (x_1 + x_2, y_1 + y_2)",
            self.COLOR_RESULT,
            UP * 3
        )
        
        card_2 = self.create_formula_card(
            "减法",
            r"\vec{a} - \vec{b} = (x_1 - x_2, y_1 - y_2)",
            self.COLOR_RESULT,
            UP * 1.5
        )
        
        card_3 = self.create_formula_card(
            "数乘",
            r"\lambda \vec{a} = (\lambda x, \lambda y)",
            self.COLOR_RESULT,
            ORIGIN
        )
        
        card_4 = self.create_formula_card(
            "平行",
            r"\vec{a} \parallel \vec{b} \Leftrightarrow x_1 y_2 - x_2 y_1 = 0",
            self.COLOR_HIGHLIGHT,
            DOWN * 1.5,
            formula_size=20
        )
        
        cards = VGroup(card_1, card_2, card_3, card_4)
        
        # 卡片依次滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(DOWN * 4)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color="#95a5a6"
        ).next_to(author_name, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰
        decorations = VGroup(*[
            Dot(
                follow_text.get_center() + 1.8 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]),
                radius=0.08,
                color=self.COLOR_HIGHLIGHT
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in decorations],
            run_time=0.5
        )
        self.play(
            *[Flash(dot, color=self.COLOR_HIGHLIGHT) for dot in decorations],
            run_time=0.8
        )
        
        self.wait(2)
    
    def create_formula_card(self, label, formula, color, position, formula_size=22):
        """创建公式卡片"""
        # 标签
        label_text = Text(
            label,
            font="PingFang SC",
            font_size=26,
            color=color,
            weight=BOLD
        )
        
        # 公式
        formula_text = MathTex(
            formula,
            font_size=formula_size,
            color=WHITE
        )
        
        # 组合
        card = VGroup(label_text, formula_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql vector_operations.py VectorCoordinateOperations  # 快速预览
# manim -qh vector_operations.py VectorCoordinateOperations   # 高质量渲染