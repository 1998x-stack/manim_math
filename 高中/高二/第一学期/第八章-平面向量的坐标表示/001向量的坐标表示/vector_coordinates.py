"""
向量的坐标表示 - Vector Coordinate Representation Animation
使用 Manim 创建的高中数学教学视频

内容: 向量坐标表示、单位向量、向量分解、向量模
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


class VectorCoordinates(Scene):
    """
    向量坐标表示教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. 单位向量介绍
    4. 向量坐标表示
    5. 向量分解
    6. 任意位置向量
    7. 向量模
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_VECTOR = "#e74c3c"        # 红色 - 主向量
        self.COLOR_UNIT_I = "#3498db"        # 蓝色 - 单位向量 i
        self.COLOR_UNIT_J = "#2ecc71"        # 绿色 - 单位向量 j
        self.COLOR_COMPONENT_X = "#3498db"   # 蓝色 - x 分量
        self.COLOR_COMPONENT_Y = "#2ecc71"   # 绿色 - y 分量
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        self.COLOR_AXES = WHITE              # 白色 - 坐标轴
        
        # 字体配置
        self.FONT = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.setup_axes()
        self.show_unit_vectors()
        self.show_vector_coordinates()
        self.show_vector_decomposition()
        self.show_arbitrary_vector()
        self.show_vector_magnitude()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook1 = Text(
            "如何用数字描述方向和大小？",
            font=self.FONT,
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        hook2 = Text(
            "向量的坐标表示！",
            font=self.FONT,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)
        
        # 向量箭头示意
        sample_vector = Arrow(
            start=ORIGIN + DOWN * 0.5,
            end=RIGHT * 2 + UP * 1.5 + DOWN * 0.5,
            color=self.COLOR_VECTOR,
            buff=0,
            stroke_width=6,
            tip_length=0.3
        )
        
        coord_label = MathTex(
            r"(x, y)",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).next_to(sample_vector.get_end(), UR, buff=0.2)
        
        self.play(GrowArrow(sample_vector), run_time=1.0)
        self.play(FadeIn(coord_label, scale=1.2), run_time=0.8)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook1),
            FadeOut(hook2),
            FadeOut(sample_vector),
            FadeOut(coord_label),
            run_time=0.5
        )
    
    def setup_axes(self):
        """场景2: 建立坐标系"""
        # 标题
        title = Text(
            "平面直角坐标系",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_AXES
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": self.COLOR_AXES,
                "include_numbers": True,
                "font_size": 20,
                "include_ticks": True,
            },
            tips=True,
        ).move_to(UP * 0.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
        
        self.play(Create(self.axes), run_time=1.2)
        self.play(
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=0.8
        )
        
        # 原点标记
        origin_dot = Dot(self.axes.c2p(0, 0), color=WHITE, radius=0.06)
        origin_label = MathTex("O", font_size=24).next_to(origin_dot, DL, buff=0.15)
        
        self.play(
            FadeIn(origin_dot),
            FadeIn(origin_label),
            run_time=0.6
        )
        
        # 说明文字
        explanation = Text(
            "向量可以用坐标表示",
            font=self.FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.8)
        self.wait(1.5)
        
        # 保存引用
        self.x_label = x_label
        self.y_label = y_label
        self.origin_dot = origin_dot
        self.origin_label = origin_label
        
        # 清理
        self.play(FadeOut(title), FadeOut(explanation), run_time=0.5)
    
    def show_unit_vectors(self):
        """场景3: 单位向量介绍"""
        # 副标题
        subtitle = Text(
            "基本单位向量",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 单位向量 i⃗
        unit_i = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(1, 0),
            color=self.COLOR_UNIT_I,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        i_label = MathTex(
            r"\vec{i} = (1, 0)",
            font_size=26,
            color=self.COLOR_UNIT_I
        ).next_to(self.axes.c2p(1, 0), DR, buff=0.3)
        
        self.play(GrowArrow(unit_i), run_time=1.0)
        self.play(Write(i_label), run_time=0.8)
        self.play(Flash(unit_i.get_end(), color=self.COLOR_UNIT_I, flash_radius=0.3), run_time=0.5)
        
        # 单位向量 j⃗
        unit_j = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(0, 1),
            color=self.COLOR_UNIT_J,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        j_label = MathTex(
            r"\vec{j} = (0, 1)",
            font_size=26,
            color=self.COLOR_UNIT_J
        ).next_to(self.axes.c2p(0, 1), UL, buff=0.3)
        
        self.play(GrowArrow(unit_j), run_time=1.0)
        self.play(Write(j_label), run_time=0.8)
        self.play(Flash(unit_j.get_end(), color=self.COLOR_UNIT_J, flash_radius=0.3), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "方向相互垂直，长度为1",
            font=self.FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=1.0)
        self.wait(1.5)
        
        # 保存引用
        self.unit_i = unit_i
        self.unit_j = unit_j
        self.i_label = i_label
        self.j_label = j_label
        
        # 淡化单位向量（保留但降低透明度）
        self.play(
            unit_i.animate.set_opacity(0.3),
            unit_j.animate.set_opacity(0.3),
            i_label.animate.set_opacity(0.3),
            j_label.animate.set_opacity(0.3),
            FadeOut(subtitle),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_vector_coordinates(self):
        """场景4: 向量坐标表示"""
        # 副标题
        subtitle = Text(
            "向量的坐标表示",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 点 P(2, 3)
        point_P = np.array([2, 3, 0])
        dot_P = Dot(self.axes.c2p(2, 3), color=self.COLOR_VECTOR, radius=0.08)
        label_P = MathTex(
            "P(2, 3)",
            font_size=24,
            color=self.COLOR_VECTOR
        ).next_to(dot_P, UR, buff=0.15)
        
        self.play(FadeIn(dot_P), run_time=0.6)
        self.play(Write(label_P), run_time=0.5)
        
        # 向量 a⃗
        vector_a = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(2, 3),
            color=self.COLOR_VECTOR,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        vector_label = MathTex(
            r"\vec{a}",
            font_size=28,
            color=self.COLOR_VECTOR
        ).move_to(self.axes.c2p(0.8, 1.8))
        
        self.play(GrowArrow(vector_a), run_time=1.0)
        self.play(Write(vector_label), run_time=0.6)
        
        # x 分量投影
        proj_x = DashedLine(
            self.axes.c2p(2, 3),
            self.axes.c2p(2, 0),
            dash_length=0.1,
            color=self.COLOR_AUXILIARY
        )
        
        x_brace = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(2, 0)),
            direction=DOWN,
            buff=0.1,
            color=self.COLOR_COMPONENT_X
        )
        x_brace_label = MathTex("x = 2", font_size=22, color=self.COLOR_COMPONENT_X).next_to(x_brace, DOWN, buff=0.1)
        
        self.play(Create(proj_x), run_time=0.8)
        self.play(
            FadeIn(x_brace),
            FadeIn(x_brace_label),
            run_time=0.6
        )
        
        # y 分量投影
        proj_y = DashedLine(
            self.axes.c2p(2, 3),
            self.axes.c2p(0, 3),
            dash_length=0.1,
            color=self.COLOR_AUXILIARY
        )
        
        y_brace = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(0, 3)),
            direction=LEFT,
            buff=0.1,
            color=self.COLOR_COMPONENT_Y
        )
        y_brace_label = MathTex("y = 3", font_size=22, color=self.COLOR_COMPONENT_Y).next_to(y_brace, LEFT, buff=0.1)
        
        self.play(Create(proj_y), run_time=0.8)
        self.play(
            FadeIn(y_brace),
            FadeIn(y_brace_label),
            run_time=0.6
        )
        
        # 向量坐标
        coord_formula = MathTex(
            r"\vec{a} = (2, 3)",
            font_size=32,
            color=self.COLOR_VECTOR
        ).move_to(DOWN * 4.5)
        
        self.play(Write(coord_formula), run_time=0.8)
        self.play(
            Flash(coord_formula, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 保存引用
        self.vector_a = vector_a
        self.dot_P = dot_P
        self.label_P = label_P
        self.vector_label = vector_label
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(x_brace),
            FadeOut(x_brace_label),
            FadeOut(y_brace),
            FadeOut(y_brace_label),
            FadeOut(coord_formula),
            run_time=0.6
        )
    
    def show_vector_decomposition(self):
        """场景5: 向量分解"""
        # 副标题
        subtitle = Text(
            "向量分解",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 公式
        decomp_formula = MathTex(
            r"\vec{a} = x\vec{i} + y\vec{j}",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(decomp_formula), run_time=1.0)
        self.wait(0.5)
        
        # 淡化原向量
        self.play(
            self.vector_a.animate.set_opacity(0.3),
            self.vector_label.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # x 方向分量: 2i⃗
        component_x = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(2, 0),
            color=self.COLOR_COMPONENT_X,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        component_x_label = MathTex(
            r"2\vec{i}",
            font_size=26,
            color=self.COLOR_COMPONENT_X
        ).next_to(self.axes.c2p(1, 0), DOWN, buff=0.3)
        
        self.play(GrowArrow(component_x), run_time=1.0)
        self.play(Write(component_x_label), run_time=0.6)
        
        # y 方向分量: 3j⃗
        component_y = Arrow(
            start=self.axes.c2p(2, 0),
            end=self.axes.c2p(2, 3),
            color=self.COLOR_COMPONENT_Y,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        component_y_label = MathTex(
            r"3\vec{j}",
            font_size=26,
            color=self.COLOR_COMPONENT_Y
        ).next_to(self.axes.c2p(2, 1.5), RIGHT, buff=0.3)
        
        self.play(GrowArrow(component_y), run_time=1.0)
        self.play(Write(component_y_label), run_time=0.6)
        
        # 平行四边形
        parallelogram = Polygon(
            self.axes.c2p(0, 0),
            self.axes.c2p(2, 0),
            self.axes.c2p(2, 3),
            self.axes.c2p(0, 3),
            stroke_color=self.COLOR_AUXILIARY,
            stroke_width=2,
            fill_opacity=0
        ).set_stroke(opacity=0.5)
        
        # 添加虚线边
        dashed_line = DashedLine(
            self.axes.c2p(0, 3),
            self.axes.c2p(0, 0),
            dash_length=0.1,
            color=self.COLOR_AUXILIARY
        ).set_opacity(0.5)
        
        dashed_line2 = DashedLine(
            self.axes.c2p(0, 3),
            self.axes.c2p(2, 3),
            dash_length=0.1,
            color=self.COLOR_AUXILIARY
        ).set_opacity(0.5)
        
        self.play(
            Create(dashed_line),
            Create(dashed_line2),
            run_time=1.0
        )
        
        # 向量叠加
        self.play(
            self.vector_a.animate.set_opacity(1),
            self.vector_label.animate.set_opacity(1),
            run_time=1.2
        )
        
        # 结果公式
        result_formula = MathTex(
            r"\vec{a} = (2, 3) = 2\vec{i} + 3\vec{j}",
            font_size=26
        ).move_to(DOWN * 4.5)
        
        self.play(Write(result_formula), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(decomp_formula),
            FadeOut(component_x),
            FadeOut(component_x_label),
            FadeOut(component_y),
            FadeOut(component_y_label),
            FadeOut(dashed_line),
            FadeOut(dashed_line2),
            FadeOut(result_formula),
            FadeOut(self.vector_a),
            FadeOut(self.vector_label),
            FadeOut(self.dot_P),
            FadeOut(self.label_P),
            run_time=0.6
        )
    
    def show_arbitrary_vector(self):
        """场景6: 任意位置向量"""
        # 副标题
        subtitle = Text(
            "任意位置的向量",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 点 A(-1, -1)
        dot_A = Dot(self.axes.c2p(-1, -1), color=self.COLOR_VECTOR, radius=0.08)
        label_A = MathTex(
            "A(-1, -1)",
            font_size=24,
            color=self.COLOR_VECTOR
        ).next_to(dot_A, DL, buff=0.15)
        
        self.play(FadeIn(dot_A), Write(label_A), run_time=0.6)
        
        # 点 B(2, 2)
        dot_B = Dot(self.axes.c2p(2, 2), color=self.COLOR_VECTOR, radius=0.08)
        label_B = MathTex(
            "B(2, 2)",
            font_size=24,
            color=self.COLOR_VECTOR
        ).next_to(dot_B, UR, buff=0.15)
        
        self.play(FadeIn(dot_B), Write(label_B), run_time=0.6)
        
        # 向量 AB⃗
        vector_AB = Arrow(
            start=self.axes.c2p(-1, -1),
            end=self.axes.c2p(2, 2),
            color=self.COLOR_VECTOR,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        vector_AB_label = MathTex(
            r"\overrightarrow{AB}",
            font_size=28,
            color=self.COLOR_VECTOR
        ).move_to(self.axes.c2p(0.3, 0.8))
        
        self.play(GrowArrow(vector_AB), run_time=1.0)
        self.play(Write(vector_AB_label), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\overrightarrow{AB} = (x_2 - x_1, y_2 - y_1)",
            font_size=26
        ).move_to(UP * 3.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 坐标标注
        coord_note = VGroup(
            MathTex(r"x_1 = -1,\  y_1 = -1", font_size=22, color=GRAY_A),
            MathTex(r"x_2 = 2,\  y_2 = 2", font_size=22, color=GRAY_A)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(UP * 2.5)
        
        self.play(FadeIn(coord_note), run_time=1.5)
        
        # 计算过程
        calc_x = MathTex(
            r"x_2 - x_1 = 2 - (-1) = 3",
            font_size=24,
            color=self.COLOR_COMPONENT_X
        ).move_to(DOWN * 3.5)
        
        calc_y = MathTex(
            r"y_2 - y_1 = 2 - (-1) = 3",
            font_size=24,
            color=self.COLOR_COMPONENT_Y
        ).move_to(DOWN * 4.2)
        
        self.play(Write(calc_x), run_time=1.2)
        self.play(Write(calc_y), run_time=1.2)
        
        # 结果
        result = MathTex(
            r"\overrightarrow{AB} = (3, 3)",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.2)
        
        self.play(Write(result), run_time=0.8)
        self.play(Flash(result, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        
        # 验证：平移向量到原点对比
        vector_AB_copy = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(3, 3),
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4,
            tip_length=0.2,
            stroke_opacity=0.6
        )
        
        self.play(GrowArrow(vector_AB_copy), run_time=1.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(formula),
            FadeOut(coord_note),
            FadeOut(calc_x),
            FadeOut(calc_y),
            FadeOut(result),
            FadeOut(vector_AB),
            FadeOut(vector_AB_label),
            FadeOut(vector_AB_copy),
            FadeOut(dot_A),
            FadeOut(label_A),
            FadeOut(dot_B),
            FadeOut(label_B),
            run_time=0.6
        )
    
    def show_vector_magnitude(self):
        """场景7: 向量模"""
        # 副标题
        subtitle = Text(
            "向量的模（长度）",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 向量 a⃗ = (3, 4)
        vector_a = Arrow(
            start=self.axes.c2p(0, 0),
            end=self.axes.c2p(3, 4),
            color=self.COLOR_VECTOR,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        vector_label = MathTex(
            r"\vec{a} = (3, 4)",
            font_size=28,
            color=self.COLOR_VECTOR
        ).next_to(self.axes.c2p(3, 4), UR, buff=0.2)
        
        self.play(GrowArrow(vector_a), run_time=1.0)
        self.play(Write(vector_label), run_time=0.8)
        
        # 直角三角形
        right_triangle = Polygon(
            self.axes.c2p(0, 0),
            self.axes.c2p(3, 0),
            self.axes.c2p(3, 4),
            stroke_color=self.COLOR_AUXILIARY,
            stroke_width=2,
            fill_opacity=0
        )
        
        # 虚线边
        triangle_leg_x = DashedLine(
            self.axes.c2p(0, 0),
            self.axes.c2p(3, 0),
            dash_length=0.1,
            color=self.COLOR_COMPONENT_X
        )
        
        triangle_leg_y = DashedLine(
            self.axes.c2p(3, 0),
            self.axes.c2p(3, 4),
            dash_length=0.1,
            color=self.COLOR_COMPONENT_Y
        )
        
        self.play(
            Create(triangle_leg_x),
            Create(triangle_leg_y),
            run_time=1.0
        )
        
        # 标注边长
        x_label = MathTex("x = 3", font_size=22, color=self.COLOR_COMPONENT_X).next_to(self.axes.c2p(1.5, 0), DOWN, buff=0.2)
        y_label = MathTex("y = 4", font_size=22, color=self.COLOR_COMPONENT_Y).next_to(self.axes.c2p(3, 2), RIGHT, buff=0.2)
        
        self.play(
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=0.8
        )
        
        # 直角符号
        right_angle = RightAngle(
            Line(self.axes.c2p(3, 0), self.axes.c2p(0, 0)),
            Line(self.axes.c2p(3, 0), self.axes.c2p(3, 4)),
            length=0.3,
            color=YELLOW
        )
        
        self.play(Create(right_angle), run_time=0.4)
        
        # 勾股定理
        pythagorean = MathTex(
            r"|\vec{a}|^2 = x^2 + y^2",
            font_size=26
        ).move_to(DOWN * 3.5)
        
        self.play(Write(pythagorean), run_time=1.0)
        
        # 代入计算
        calculation = MathTex(
            r"3^2 + 4^2 = 9 + 16 = 25",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.3)
        
        self.play(Write(calculation), run_time=1.5)
        
        # 结果
        result = MathTex(
            r"|\vec{a}| = 5",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.2)
        
        self.play(Write(result), run_time=0.8)
        
        # 通用公式
        general_formula = MathTex(
            r"|\vec{a}| = \sqrt{x^2 + y^2}",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(general_formula), run_time=1.0)
        
        self.wait(1.7)
        
        # 清理所有元素
        self.play(
            FadeOut(subtitle),
            FadeOut(vector_a),
            FadeOut(vector_label),
            FadeOut(triangle_leg_x),
            FadeOut(triangle_leg_y),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(right_angle),
            FadeOut(pythagorean),
            FadeOut(calculation),
            FadeOut(result),
            FadeOut(general_formula),
            # 清理坐标系相关元素
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.origin_dot),
            FadeOut(self.origin_label),
            FadeOut(self.unit_i),
            FadeOut(self.unit_j),
            FadeOut(self.i_label),
            FadeOut(self.j_label),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结与片尾"""
        # 要点卡片
        card1 = self.create_summary_card(
            "坐标表示",
            r"\vec{a} = (x, y)",
            self.COLOR_VECTOR,
            UP * 2
        )
        
        card2 = self.create_summary_card(
            "向量分解",
            r"\vec{a} = x\vec{i} + y\vec{j}",
            self.COLOR_UNIT_I,
            UP * 0.5
        )
        
        card3 = self.create_summary_card(
            "任意向量",
            r"\overrightarrow{AB} = (x_2-x_1, y_2-y_1)",
            self.COLOR_UNIT_J,
            DOWN * 1
        )
        
        card4 = self.create_summary_card(
            "向量模",
            r"|\vec{a}| = \sqrt{x^2 + y^2}",
            self.COLOR_HIGHLIGHT,
            DOWN * 2.5
        )
        
        cards = VGroup(card1, card2, card3, card4)
        
        # 卡片滑入
        for card in cards:
            card.shift(LEFT * 10)
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(cards), run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多向量知识！",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 向量装饰图标
        vector_icons = VGroup(*[
            Arrow(
                start=ORIGIN,
                end=RIGHT * 0.5 + UP * 0.3,
                color=c,
                buff=0,
                stroke_width=4,
                tip_length=0.15
            )
            for c in [self.COLOR_VECTOR, self.COLOR_UNIT_I, self.COLOR_UNIT_J]
        ]).arrange(RIGHT, buff=0.5).move_to(DOWN * 2)
        
        self.play(*[GrowArrow(icon) for icon in vector_icons], run_time=0.6)
        self.play(vector_icons.animate.scale(1.2), run_time=0.5)
        self.play(vector_icons.animate.scale(1/1.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(vector_icons),
            run_time=1.0
        )
    
    def create_summary_card(self, title_text, formula_tex, color, position):
        """创建总结卡片"""
        # 图标
        icon = Square(side_length=0.3, fill_color=color, fill_opacity=0.8, stroke_width=0)
        
        # 文字
        title = Text(title_text, font=self.FONT, font_size=24, color=WHITE)
        formula = MathTex(formula_tex, font_size=22, color=GRAY_A)
        
        text_group = VGroup(title, formula).arrange(DOWN, buff=0.12)
        
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card


# 运行命令示例:
# manim -pql vector_coordinates.py VectorCoordinates  # 快速预览
# manim -qh vector_coordinates.py VectorCoordinates   # 高质量输出