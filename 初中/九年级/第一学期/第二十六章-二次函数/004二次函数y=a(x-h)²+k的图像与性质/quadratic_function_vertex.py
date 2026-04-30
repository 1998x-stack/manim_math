"""
二次函数顶点式 y=a(x-h)²+k 的图像与性质
Quadratic Function in Vertex Form - Manim Animation

适用年级: 九年级
主题: 二次函数的顶点式及其性质
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticFunctionVertex(Scene):
    """
    二次函数顶点式教学动画
    
    场景顺序:
    1. 开场钩子 - 引出顶点式
    2. 建立坐标系和基本抛物线 (a>0)
    3. 标注顶点坐标
    4. 对称轴
    5. a>0时的性质
    6. a<0时的对比
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PARABOLA_POSITIVE = "#3498db"  # 蓝色 - a>0的抛物线
        self.COLOR_PARABOLA_NEGATIVE = "#e74c3c"  # 红色 - a<0的抛物线
        self.COLOR_VERTEX = "#f39c12"             # 橙色 - 顶点
        self.COLOR_AXIS = "#2ecc71"               # 绿色 - 对称轴
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_create_parabola()
        self.scene_3_vertex_annotation()
        self.scene_4_axis_of_symmetry()
        self.scene_5_properties_a_positive()
        self.scene_6_compare_a_negative()
        self.scene_7_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何参数和坐标"""
        # ========== 第一条抛物线参数 (a>0) ==========
        self.a_positive = 0.5
        self.h = 1.0
        self.k = -2.0
        
        # ========== 第二条抛物线参数 (a<0) ==========
        self.a_negative = -0.4
        self.h2 = -1.0
        self.k2 = 2.0
        
        # ========== 坐标系设置 ==========
        self.axes_center = UP * 1.5
        self.x_range = [-4, 4, 1]
        self.y_range = [-3, 5, 1]
        
        # 创建坐标系 (稍后在场景中添加)
        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_ticks": True,
            },
            tips=False
        ).move_to(self.axes_center)
        
        # ========== 抛物线函数定义 ==========
        self.parabola_func = lambda x: self.a_positive * (x - self.h)**2 + self.k
        self.parabola_func2 = lambda x: self.a_negative * (x - self.h2)**2 + self.k2
        
        # ========== 验证几何计算 ==========
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何参数的正确性"""
        # 验证顶点在抛物线上
        y_at_vertex = self.parabola_func(self.h)
        assert abs(y_at_vertex - self.k) < 1e-6, f"顶点不在抛物线上: y({self.h}) = {y_at_vertex}, 期望 {self.k}"
        
        # 验证对称性
        test_offset = 2.0
        y_left = self.parabola_func(self.h - test_offset)
        y_right = self.parabola_func(self.h + test_offset)
        assert abs(y_left - y_right) < 1e-6, f"抛物线不对称: y({self.h - test_offset}) = {y_left}, y({self.h + test_offset}) = {y_right}"
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部常驻)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "如何一眼看出\n抛物线的顶点?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        self.wait(0.5)
        
        # 一般式
        general_form = MathTex(
            r"y = ax^2 + bx + c",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(general_form), run_time=0.8)
        self.wait(0.3)
        
        # 箭头
        arrow = Arrow(
            start=UP * 2.8,
            end=UP * 1.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow), run_time=0.4)
        
        # 顶点式
        vertex_form = MathTex(
            r"y = a(x-h)^2 + k",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(Write(vertex_form), run_time=1.0)
        
        # 高亮顶点式
        self.play(Indicate(vertex_form, scale_factor=1.1), run_time=0.6)
        self.wait(0.5)
        
        # 清理并保留
        self.play(
            FadeOut(hook),
            FadeOut(general_form),
            FadeOut(arrow),
            run_time=0.5
        )
        
        # 将顶点式移到顶部
        self.vertex_form_top = MathTex(
            r"y = a(x-h)^2 + k",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(vertex_form, self.vertex_form_top),
            run_time=0.6
        )
        
        # 保存引用
        self.vertex_form = vertex_form
    
    def scene_2_create_parabola(self):
        """场景2: 建立坐标系和基本抛物线"""
        # 创建坐标系
        self.play(Create(self.axes), run_time=1.2)
        
        # 创建抛物线
        self.parabola = self.axes.plot(
            self.parabola_func,
            x_range=[-3, 5],
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        self.play(Create(self.parabola), run_time=1.5)
        
        # 标记顶点
        vertex_coord = self.axes.c2p(self.h, self.k)
        self.vertex_dot = Dot(
            vertex_coord,
            color=self.COLOR_VERTEX,
            radius=0.1
        )
        
        self.play(
            FadeIn(self.vertex_dot, scale=0.5),
            Flash(self.vertex_dot, color=self.COLOR_VERTEX, flash_radius=0.3),
            run_time=0.6
        )
        
        # 顶点坐标标签
        self.vertex_label = MathTex(
            r"(1, -2)",
            font_size=24,
            color=self.COLOR_VERTEX
        ).next_to(self.vertex_dot, DOWN + RIGHT, buff=0.2)
        
        self.play(FadeIn(self.vertex_label), run_time=0.5)
        
        # 函数表达式
        function_eq = MathTex(
            r"y = 0.5(x-1)^2 - 2",
            font_size=28,
            color=self.COLOR_PARABOLA_POSITIVE
        ).move_to(UP * 5.2)
        
        self.play(Write(function_eq), run_time=0.8)
        self.wait(1.0)
        
        # 清理函数表达式
        self.play(FadeOut(function_eq), run_time=0.4)
    
    def scene_3_vertex_annotation(self):
        """场景3: 标注顶点坐标"""
        # 提示框
        hint_box = VGroup(
            Text(
                "顶点坐标",
                font="PingFang SC",
                font_size=28,
                color=WHITE
            ),
            MathTex(r"(h, k)", font_size=32, color=self.COLOR_VERTEX)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 4.5)
        
        self.play(FadeIn(hint_box, shift=UP * 0.3), run_time=0.5)
        
        # 公式分解 - 高亮h部分
        vertex_form_parts = MathTex(
            r"y = a(x-", r"h", r")^2 + k",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        vertex_form_parts[1].set_color(YELLOW)
        
        self.play(
            Transform(self.vertex_form, vertex_form_parts),
            run_time=0.3
        )
        self.play(Indicate(vertex_form_parts[1]), run_time=0.6)
        
        # h值箭头和标签
        h_arrow = Arrow(
            start=UP * 5.5 + LEFT * 0.5,
            end=self.axes.c2p(self.h, self.y_range[0]) + UP * 0.3,
            color=YELLOW,
            stroke_width=3
        )
        h_label = MathTex(r"h = 1", font_size=24, color=YELLOW).next_to(h_arrow.get_start(), UP, buff=0.1)
        
        self.play(
            GrowArrow(h_arrow),
            Write(h_label),
            run_time=0.4
        )
        self.wait(0.5)
        
        # 恢复公式颜色
        vertex_form_parts2 = MathTex(
            r"y = a(x-h)^2 + ", r"k",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        vertex_form_parts2[1].set_color(YELLOW)
        
        self.play(
            Transform(self.vertex_form, vertex_form_parts2),
            run_time=0.3
        )
        self.play(Indicate(vertex_form_parts2[1]), run_time=0.6)
        
        # k值箭头和标签
        k_arrow = Arrow(
            start=UP * 5.5 + RIGHT * 1.5,
            end=self.axes.c2p(self.x_range[1], self.k) + LEFT * 0.3,
            color=YELLOW,
            stroke_width=3
        )
        k_label = MathTex(r"k = -2", font_size=24, color=YELLOW).next_to(k_arrow.get_start(), UP, buff=0.1)
        
        self.play(
            GrowArrow(k_arrow),
            Write(k_label),
            run_time=0.4
        )
        
        # 整体高亮
        self.play(Flash(hint_box, color=self.COLOR_VERTEX), run_time=0.5)
        self.wait(2.0)
        
        # 恢复公式
        vertex_form_normal = MathTex(
            r"y = a(x-h)^2 + k",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Transform(self.vertex_form, vertex_form_normal), run_time=0.3)
        
        # 清理
        self.play(
            FadeOut(hint_box),
            FadeOut(h_arrow),
            FadeOut(k_arrow),
            FadeOut(h_label),
            FadeOut(k_label),
            run_time=0.5
        )
    
    def scene_4_axis_of_symmetry(self):
        """场景4: 对称轴"""
        # 对称轴虚线
        axis_bottom = self.axes.c2p(self.h, self.y_range[0])
        axis_top = self.axes.c2p(self.h, self.y_range[1])
        
        self.axis_line = DashedLine(
            axis_bottom,
            axis_top,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(self.axis_line), run_time=0.8)
        
        # 对称轴方程
        self.axis_eq = MathTex(
            r"x = h",
            font_size=26,
            color=self.COLOR_AXIS
        ).next_to(self.axis_line, UP, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(Write(self.axis_eq), run_time=0.6)
        
        # 说明文字
        symmetry_text = Text(
            "对称轴: 直线 x = 1",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(symmetry_text), run_time=0.4)
        
        # 标记对称点对
        # 解方程求对称点: 0.5(x-1)² - 2 = 0 → x = 1±2
        test_y = 0
        x1 = self.h - 2  # = -1
        x2 = self.h + 2  # = 3
        
        point_left = Dot(self.axes.c2p(x1, test_y), color=YELLOW, radius=0.08)
        point_right = Dot(self.axes.c2p(x2, test_y), color=YELLOW, radius=0.08)
        
        self.play(
            FadeIn(point_left),
            FadeIn(point_right),
            run_time=0.5
        )
        
        # 到对称轴的距离线
        distance_left = DashedLine(
            point_left.get_center(),
            self.axes.c2p(self.h, test_y),
            color=self.COLOR_AUXILIARY,
            dash_length=0.05,
            stroke_width=2
        )
        distance_right = DashedLine(
            self.axes.c2p(self.h, test_y),
            point_right.get_center(),
            color=self.COLOR_AUXILIARY,
            dash_length=0.05,
            stroke_width=2
        )
        
        self.play(
            Create(distance_left),
            Create(distance_right),
            run_time=0.6
        )
        
        # 等距标记
        equal_mark_left = MathTex("2", font_size=20, color=YELLOW).next_to(distance_left, DOWN, buff=0.1)
        equal_mark_right = MathTex("2", font_size=20, color=YELLOW).next_to(distance_right, DOWN, buff=0.1)
        
        self.play(
            FadeIn(equal_mark_left),
            FadeIn(equal_mark_right),
            run_time=0.4
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(point_left),
            FadeOut(point_right),
            FadeOut(distance_left),
            FadeOut(distance_right),
            FadeOut(equal_mark_left),
            FadeOut(equal_mark_right),
            FadeOut(symmetry_text),
            run_time=0.5
        )
    
    def scene_5_properties_a_positive(self):
        """场景5: a>0时的性质"""
        # a>0标注
        a_positive_text = Text(
            "当 a > 0 时",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_PARABOLA_POSITIVE
        ).move_to(DOWN * 4)
        
        self.play(Write(a_positive_text), run_time=0.5)
        
        # 开口向上箭头
        arrow_left = Arrow(
            start=self.axes.c2p(-2, self.parabola_func(-2)),
            end=self.axes.c2p(-2, self.parabola_func(-2)) + UP * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        arrow_right = Arrow(
            start=self.axes.c2p(4, self.parabola_func(4)),
            end=self.axes.c2p(4, self.parabola_func(4)) + UP * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        upward_text = Text(
            "开口向上",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)
        
        self.play(
            GrowArrow(arrow_left),
            GrowArrow(arrow_right),
            FadeIn(upward_text),
            run_time=0.6
        )
        
        # 最小值标注
        min_value_box = VGroup(
            Text("最小值", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"k = -2", font_size=26, color=self.COLOR_VERTEX)
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(self.vertex_dot, LEFT, buff=0.5)
        
        # 背景框
        bg_rect = SurroundingRectangle(
            min_value_box,
            color=self.COLOR_VERTEX,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=2
        )
        min_value_group = VGroup(bg_rect, min_value_box)
        
        self.play(FadeIn(min_value_group), run_time=0.7)
        
        # 高亮顶点
        self.play(Indicate(self.vertex_dot, scale_factor=1.3), run_time=0.6)
        
        # 性质说明
        property_text = Text(
            "当 x = h 时, y有最小值 k",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.7)
        
        self.play(FadeIn(property_text), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(arrow_left),
            FadeOut(arrow_right),
            FadeOut(upward_text),
            FadeOut(min_value_group),
            FadeOut(property_text),
            FadeOut(a_positive_text),
            run_time=0.6
        )
    
    def scene_6_compare_a_negative(self):
        """场景6: a<0时的对比"""
        # 原抛物线淡化
        self.play(
            self.parabola.animate.set_opacity(0.3),
            self.vertex_dot.animate.set_opacity(0.3),
            self.vertex_label.animate.set_opacity(0.3),
            self.axis_line.animate.set_opacity(0.3),
            self.axis_eq.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # 新抛物线
        parabola2 = self.axes.plot(
            self.parabola_func2,
            x_range=[-5, 3],
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=4
        )
        
        self.play(Create(parabola2), run_time=1.5)
        
        # 新顶点
        vertex_coord2 = self.axes.c2p(self.h2, self.k2)
        vertex_dot2 = Dot(
            vertex_coord2,
            color=self.COLOR_VERTEX,
            radius=0.1
        )
        
        self.play(
            FadeIn(vertex_dot2, scale=0.5),
            Flash(vertex_dot2, color=self.COLOR_VERTEX, flash_radius=0.3),
            run_time=0.6
        )
        
        # 新顶点坐标
        vertex_label2 = MathTex(
            r"(-1, 2)",
            font_size=24,
            color=self.COLOR_VERTEX
        ).next_to(vertex_dot2, UP + LEFT, buff=0.2)
        
        self.play(FadeIn(vertex_label2), run_time=0.5)
        
        # 新对称轴
        axis_bottom2 = self.axes.c2p(self.h2, self.y_range[0])
        axis_top2 = self.axes.c2p(self.h2, self.y_range[1])
        
        axis_line2 = DashedLine(
            axis_bottom2,
            axis_top2,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(axis_line2), run_time=0.8)
        
        # a<0标注
        a_negative_text = Text(
            "当 a < 0 时",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_PARABOLA_NEGATIVE
        ).move_to(DOWN * 4)
        
        self.play(Write(a_negative_text), run_time=0.5)
        
        # 开口向下箭头
        arrow_left2 = Arrow(
            start=self.axes.c2p(-4, self.parabola_func2(-4)),
            end=self.axes.c2p(-4, self.parabola_func2(-4)) + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        arrow_right2 = Arrow(
            start=self.axes.c2p(2, self.parabola_func2(2)),
            end=self.axes.c2p(2, self.parabola_func2(2)) + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        downward_text = Text(
            "开口向下",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)
        
        self.play(
            GrowArrow(arrow_left2),
            GrowArrow(arrow_right2),
            FadeIn(downward_text),
            run_time=0.6
        )
        
        # 最大值标注
        max_value_box = VGroup(
            Text("最大值", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(r"k = 2", font_size=26, color=self.COLOR_VERTEX)
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(vertex_dot2, RIGHT, buff=0.5)
        
        bg_rect2 = SurroundingRectangle(
            max_value_box,
            color=self.COLOR_VERTEX,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=2
        )
        max_value_group = VGroup(bg_rect2, max_value_box)
        
        self.play(FadeIn(max_value_group), run_time=0.7)
        
        # 高亮顶点
        self.play(Indicate(vertex_dot2, scale_factor=1.3), run_time=0.6)
        
        # 对比说明
        comparison_text = Text(
            "当 x = h 时, y有最大值 k",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.7)
        
        self.play(FadeIn(comparison_text), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(parabola2),
            FadeOut(vertex_dot2),
            FadeOut(vertex_label2),
            FadeOut(axis_line2),
            FadeOut(arrow_left2),
            FadeOut(arrow_right2),
            FadeOut(downward_text),
            FadeOut(max_value_group),
            FadeOut(comparison_text),
            FadeOut(a_negative_text),
            # 恢复原抛物线
            self.parabola.animate.set_opacity(1),
            self.vertex_dot.animate.set_opacity(1),
            self.vertex_label.animate.set_opacity(1),
            self.axis_line.animate.set_opacity(1),
            self.axis_eq.animate.set_opacity(1),
            run_time=0.6
        )
    
    def scene_7_summary_and_outro(self):
        """场景7: 总结与片尾"""
        # 清空所有场景元素
        self.play(
            FadeOut(self.axes),
            FadeOut(self.parabola),
            FadeOut(self.vertex_dot),
            FadeOut(self.vertex_label),
            FadeOut(self.axis_line),
            FadeOut(self.axis_eq),
            FadeOut(self.vertex_form),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "顶点式\n一眼看透抛物线!",
            font="PingFang SC",
            font_size=42,
            color=GOLD,
            line_spacing=1.3
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.7)
        
        # 创建卡片
        cards = VGroup()
        
        # 卡片1: 公式
        card1 = self.create_summary_card(
            MathTex(r"y = a(x-h)^2 + k", font_size=32, color=WHITE),
            "顶点式",
            self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        cards.add(card1)
        
        # 卡片2: 顶点
        card2 = self.create_summary_card(
            MathTex(r"(h, k)", font_size=28, color=WHITE),
            "顶点坐标",
            self.COLOR_VERTEX
        ).move_to(UP * 2)
        cards.add(card2)
        
        # 卡片3: 对称轴
        card3 = self.create_summary_card(
            MathTex(r"x = h", font_size=28, color=WHITE),
            "对称轴",
            self.COLOR_AXIS
        ).move_to(UP * 0.5)
        cards.add(card3)
        
        # 卡片4: a>0
        card4_content = VGroup(
            Text("开口向上", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"\text{最小值} = k", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        card4 = self.create_summary_card(
            card4_content,
            "a > 0",
            self.COLOR_PARABOLA_POSITIVE
        ).move_to(DOWN * 1)
        cards.add(card4)
        
        # 卡片5: a<0
        card5_content = VGroup(
            Text("开口向下", font="PingFang SC", font_size=22, color=WHITE),
            MathTex(r"\text{最大值} = k", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        card5 = self.create_summary_card(
            card5_content,
            "a < 0",
            self.COLOR_PARABOLA_NEGATIVE
        ).move_to(DOWN * 2.5)
        cards.add(card5)
        
        # 卡片依次出现
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 关键提示
        key_reminder = Text(
            "注意: h前有负号!",
            font="PingFang SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(key_reminder, shift=UP * 0.3), run_time=0.5)
        self.play(Indicate(key_reminder, scale_factor=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理总结内容
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(key_reminder),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多函数技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 抛物线图标
        decoration_parabolas = VGroup()
        for i in range(5):
            angle = i * 2 * PI / 5
            pos = 2.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 1
            
            # 小抛物线装饰
            mini_axes = Axes(
                x_range=[-1, 1],
                y_range=[-0.5, 0.5],
                x_length=0.6,
                y_length=0.6,
                axis_config={"include_ticks": False, "include_numbers": False},
                tips=False
            ).move_to(pos).set_opacity(0.6)
            
            mini_parabola = mini_axes.plot(
                lambda x: 0.3 * x**2 - 0.3,
                color=[self.COLOR_PARABOLA_POSITIVE, self.COLOR_PARABOLA_NEGATIVE][i % 2],
                stroke_width=2
            )
            
            decoration_parabolas.add(VGroup(mini_axes, mini_parabola))
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decoration_parabolas],
            run_time=0.6
        )
        self.play(Rotate(decoration_parabolas, angle=PI, run_time=1.5))
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_parabolas),
            run_time=1.0
        )
    
    def create_summary_card(self, content, title, color):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, title_text, content).arrange(RIGHT, buff=0.3)
        
        return card


# 运行命令:
# manim -pql quadratic_function_vertex.py QuadraticFunctionVertex  # 快速预览
# manim -qh quadratic_function_vertex.py QuadraticFunctionVertex   # 高质量渲染