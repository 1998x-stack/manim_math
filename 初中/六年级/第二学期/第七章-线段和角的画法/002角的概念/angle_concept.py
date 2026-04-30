"""
角的概念 - Concept of Angles Animation
使用 Manim 创建的六年级数学教学视频

内容: 角的定义、表示方法、度量单位、形成过程、特殊角
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

修复内容:
1. 使用Text而不是Tex/MathTex来处理中文
2. 精确的角度计算
3. 修复LaTeX中文字符编译错误
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class AngleConcept(Scene):
    """
    角的概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 角的定义
    3. 角的表示方法
    4. 角的度量单位
    5. 角的旋转形成
    6. 特殊角介绍
    7. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要射线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要射线
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_ARC = "#2ecc71"          # 绿色 - 角度弧
        self.COLOR_VERTEX = "#f39c12"       # 橙色 - 顶点
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_angle_definition()
        self.show_angle_notation()
        self.show_angle_measurement()
        self.show_angle_formation()
        self.show_special_angles()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标 - 使用精确计算"""
        # 基准参数
        self.MAIN_OFFSET = UP * 1.5
        
        # 角的顶点
        self.O = ORIGIN + self.MAIN_OFFSET
        
        # 射线端点 - 精确计算60度角
        self.angle_value = np.pi / 3.0  # 精确的60度 = π/3 弧度
        self.ray_length = 2.5
        
        # 精确计算端点坐标
        self.A = self.O + np.array([self.ray_length, 0.0, 0.0])
        self.B = self.O + np.array([
            self.ray_length * np.cos(self.angle_value),
            self.ray_length * np.sin(self.angle_value),
            0.0
        ])
        
        # 角度弧参数
        self.arc_radius = 0.8
        
        print("✓ 几何初始化完成 (精确计算)")
        print(f"  顶点O: {self.O}")
        print(f"  端点A: {self.A}")
        print(f"  端点B: {self.B}")
        print(f"  角度: {np.degrees(self.angle_value):.1f}°")
    
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
        hook_text = Text(
            "什么是角?",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简单的角示意 - 精确60度
        simple_vertex = Dot(ORIGIN, color=self.COLOR_VERTEX, radius=0.08)
        simple_ray1 = Arrow(
            ORIGIN, RIGHT * 1.5,
            color=self.COLOR_PRIMARY,
            buff=0,
            stroke_width=4
        )
        
        # 精确60度方向
        angle_60 = np.pi / 3.0
        simple_ray2 = Arrow(
            ORIGIN, 
            np.array([1.5 * np.cos(angle_60), 1.5 * np.sin(angle_60), 0.0]),
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=4
        )
        simple_arc = Arc(
            radius=0.5,
            angle=angle_60,
            color=self.COLOR_ARC,
            stroke_width=3
        )
        
        simple_angle = VGroup(simple_vertex, simple_ray1, simple_ray2, simple_arc)
        
        self.play(Create(simple_angle), run_time=1.0)
        self.play(Flash(simple_arc, color=self.COLOR_ARC, flash_radius=0.4), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), FadeOut(simple_angle), run_time=0.5)
    
    def show_angle_definition(self):
        """场景2: 角的定义"""
        # 标题
        title = Text(
            "角的定义",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        subtitle = Text(
            "两条射线 + 公共端点",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)
        
        # Step 1: 顶点出现
        vertex = Dot(self.O, color=self.COLOR_VERTEX, radius=0.15)
        vertex_label = Text(
            "O",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(vertex, DOWN, buff=0.2)
        
        explain_vertex = Text(
            "顶点",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(GrowFromCenter(vertex), run_time=0.5)
        self.play(FadeIn(vertex_label), FadeIn(explain_vertex), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(explain_vertex), run_time=0.3)
        
        # Step 2: 第一条射线
        ray_OA = Arrow(
            self.O, self.A,
            color=self.COLOR_PRIMARY,
            buff=0,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12
        )
        
        point_A = Dot(self.A, color=WHITE, radius=0.08)
        label_A = Text(
            "A",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(point_A, RIGHT, buff=0.15)
        
        explain_ray1 = Text(
            "射线OA",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(Create(ray_OA), run_time=1.0)
        self.play(
            FadeIn(point_A),
            FadeIn(label_A),
            FadeIn(explain_ray1),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(FadeOut(explain_ray1), run_time=0.3)
        
        # Step 3: 第二条射线
        ray_OB = Arrow(
            self.O, self.B,
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12
        )
        
        point_B = Dot(self.B, color=WHITE, radius=0.08)
        label_B = Text(
            "B",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(point_B, UP + RIGHT * 0.5, buff=0.15)
        
        explain_ray2 = Text(
            "射线OB",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(Create(ray_OB), run_time=1.0)
        self.play(
            FadeIn(point_B),
            FadeIn(label_B),
            FadeIn(explain_ray2),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(FadeOut(explain_ray2), run_time=0.3)
        
        # Step 4: 角度弧
        angle_arc = Arc(
            radius=self.arc_radius,
            start_angle=0,
            angle=self.angle_value,
            color=self.COLOR_ARC,
            stroke_width=4
        ).shift(self.O)
        
        self.play(Create(angle_arc), run_time=0.8)
        self.play(Flash(angle_arc, color=self.COLOR_ARC, flash_radius=0.5), run_time=0.4)
        
        # Step 5: 标注部分
        vertex_annotation = Text(
            "顶点",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_VERTEX
        ).next_to(vertex, LEFT, buff=0.8)
        
        vertex_arrow = Arrow(
            vertex_annotation.get_right(),
            vertex.get_left(),
            color=self.COLOR_VERTEX,
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        edge_annotation = Text(
            "边",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_PRIMARY
        ).move_to(self.O + RIGHT * 1.5 + DOWN * 0.8)
        
        edge_arrow = Arrow(
            edge_annotation.get_top(),
            self.O + RIGHT * 1.2 + DOWN * 0.1,
            color=self.COLOR_PRIMARY,
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            FadeIn(vertex_annotation),
            Create(vertex_arrow),
            FadeIn(edge_annotation),
            Create(edge_arrow),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理标注
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(vertex_annotation),
            FadeOut(vertex_arrow),
            FadeOut(edge_annotation),
            FadeOut(edge_arrow),
            run_time=0.5
        )
        
        # 保存主要元素
        self.vertex = vertex
        self.vertex_label = vertex_label
        self.ray_OA = ray_OA
        self.ray_OB = ray_OB
        self.point_A = point_A
        self.point_B = point_B
        self.label_A = label_A
        self.label_B = label_B
        self.angle_arc = angle_arc
    
    def show_angle_notation(self):
        """场景3: 角的表示方法"""
        # 标题
        title = Text(
            "角的表示方法",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # 方法1: 三点表示法
        method1_title = Text(
            "方法一: 三个点",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        method1_formula = MathTex(
            r"\angle AOB",
            font_size=36
        ).next_to(method1_title, DOWN, buff=0.3)
        
        self.play(FadeIn(method1_title), run_time=0.5)
        self.play(Write(method1_formula), run_time=0.6)
        
        # 高亮相关点
        self.play(
            Flash(self.point_A, color=YELLOW),
            Flash(self.vertex, color=YELLOW),
            Flash(self.point_B, color=YELLOW),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 方法2: 顶点表示法
        method2_title = Text(
            "方法二: 顶点",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        method2_formula = MathTex(
            r"\angle O",
            font_size=36
        ).next_to(method2_title, DOWN, buff=0.3)
        
        self.play(
            ReplacementTransform(method1_title, method2_title),
            ReplacementTransform(method1_formula, method2_formula),
            run_time=0.6
        )
        
        self.play(
            Flash(self.vertex, color=YELLOW, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 方法3: 希腊字母
        method3_title = Text(
            "方法三: 希腊字母",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        method3_formula = MathTex(
            r"\angle \alpha",
            font_size=36
        ).next_to(method3_title, DOWN, buff=0.3)
        
        # 在角内部添加α标记
        alpha_label = MathTex(
            r"\alpha",
            font_size=28,
            color=self.COLOR_ARC
        ).move_to(self.O + np.array([0.5, 0.3, 0]))
        
        self.play(
            ReplacementTransform(method2_title, method3_title),
            ReplacementTransform(method2_formula, method3_formula),
            run_time=0.6
        )
        
        self.play(FadeIn(alpha_label, scale=0.8), run_time=0.5)
        self.wait(1.0)
        
        # 汇总三种方法
        summary_title = Text(
            "三种表示法:",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 3)
        
        summary_methods = MathTex(
            r"\angle AOB \quad \angle O \quad \angle \alpha",
            font_size=32
        ).next_to(summary_title, DOWN, buff=0.4)
        
        self.play(
            FadeOut(method3_title),
            FadeOut(method3_formula),
            FadeIn(summary_title),
            FadeIn(summary_methods),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(summary_title),
            FadeOut(summary_methods),
            FadeOut(alpha_label),
            run_time=0.5
        )
    
    def show_angle_measurement(self):
        """场景4: 角的度量单位"""
        # 标题
        title = Text(
            "角的度量",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # 度的定义
        degree_intro = Text(
            "度 (°) 是角的基本单位",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(degree_intro), run_time=0.6)
        self.wait(0.8)
        
        # 度与分的关系
        degree_minute = MathTex(
            r"1^\circ = 60'",
            font_size=36
        ).move_to(DOWN * 4)
        
        self.play(
            FadeOut(degree_intro),
            Write(degree_minute),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 分与秒的关系
        minute_second = MathTex(
            r"1' = 60''",
            font_size=36
        ).next_to(degree_minute, DOWN, buff=0.5)
        
        self.play(Write(minute_second), run_time=0.8)
        self.wait(1.0)
        
        # 完整关系
        full_relation = MathTex(
            r"1^\circ = 60' = 3600''",
            font_size=36
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(full_relation, shift=UP * 0.3),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 在当前角上标注度数 - 精确60度
        angle_measure = MathTex(
            r"60^\circ",
            font_size=32,
            color=self.COLOR_ARC
        ).move_to(self.O + np.array([1.2, 0.5, 0]))
        
        self.play(
            FadeOut(degree_minute),
            FadeOut(minute_second),
            FadeOut(full_relation),
            FadeIn(angle_measure, scale=0.8),
            run_time=0.8
        )
        
        # 高亮角度弧
        self.play(
            self.angle_arc.animate.set_stroke(width=6),
            Flash(self.angle_arc, color=self.COLOR_ARC, flash_radius=0.6),
            run_time=0.8
        )
        self.play(
            self.angle_arc.animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            run_time=0.5
        )
        
        # 保存角度标注
        self.angle_measure = angle_measure
    
    def show_angle_formation(self):
        """场景5: 角的旋转形成 - 使用精确计算"""
        # 标题
        title = Text(
            "角的形成",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        subtitle = Text(
            "射线绕端点旋转",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)
        
        # 清除原有元素（除了顶点）
        self.play(
            FadeOut(self.ray_OA),
            FadeOut(self.ray_OB),
            FadeOut(self.angle_arc),
            FadeOut(self.point_A),
            FadeOut(self.point_B),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.vertex_label),
            FadeOut(self.angle_measure),
            run_time=0.5
        )
        
        # 固定射线（水平）
        fixed_ray = Arrow(
            self.O, self.O + RIGHT * 2.5,
            color=self.COLOR_PRIMARY,
            buff=0,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12
        )
        
        self.play(Create(fixed_ray), run_time=0.8)
        
        # 使用ValueTracker控制旋转 - 精确角度
        angle_tracker = ValueTracker(0)
        
        # 旋转射线
        rotating_ray = always_redraw(
            lambda: Arrow(
                self.O,
                self.O + 2.5 * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0.0
                ]),
                color=self.COLOR_SECONDARY,
                buff=0,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.12
            )
        )
        
        # 动态角度弧
        dynamic_arc = always_redraw(
            lambda: Arc(
                radius=self.arc_radius,
                start_angle=0,
                angle=angle_tracker.get_value(),
                color=self.COLOR_ARC,
                stroke_width=4
            ).shift(self.O)
        )
        
        # 动态角度标注 - 精确显示
        dynamic_label = always_redraw(
            lambda: MathTex(
                f"{np.degrees(angle_tracker.get_value()):.0f}^\\circ",
                font_size=32,
                color=self.COLOR_ARC
            ).move_to(self.O + np.array([1.2, 0.6, 0]))
        )
        
        self.add(rotating_ray, dynamic_arc, dynamic_label)
        
        # 执行旋转动画
        explain_text = Text(
            "从0°开始旋转...",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain_text), run_time=0.5)
        self.wait(0.3)
        
        # 精确旋转到60度 (π/3)
        self.play(
            angle_tracker.animate.set_value(np.pi / 3.0),
            run_time=3.0,
            rate_func=smooth
        )
        
        self.play(
            FadeOut(explain_text),
            run_time=0.3
        )
        
        # 停留展示
        final_text = Text(
            "最终形成60°的角",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(final_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(final_text),
            FadeOut(fixed_ray),
            FadeOut(rotating_ray),
            FadeOut(dynamic_arc),
            FadeOut(dynamic_label),
            FadeOut(self.vertex),
            run_time=0.6
        )
    
    def show_special_angles(self):
        """场景6: 特殊角介绍 - 修复中文显示问题"""
        # 标题
        title = Text(
            "特殊的角",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # ===== 周角 (左侧) =====
        full_angle_title = Text(
            "周角",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(LEFT * 2 + UP * 3.5)
        
        full_circle_center = LEFT * 2 + UP * 1.5
        full_circle = Circle(
            radius=1.2,
            color=self.COLOR_ARC,
            stroke_width=5
        ).move_to(full_circle_center)
        
        # 添加箭头表示方向
        arrow_full = Arrow(
            full_circle_center + RIGHT * 1.2,
            full_circle_center + RIGHT * 1.2 + UP * 0.3,
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        full_angle_measure = MathTex(
            r"360^\circ",
            font_size=36,
            color=self.COLOR_ARC
        ).move_to(full_circle_center)
        
        # 修复: 使用VGroup组合中文Text和MathTex
        full_angle_text = Text(
            "周角 =",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        full_angle_math = MathTex(
            r"360^\circ",
            font_size=28,
            color=WHITE
        )
        full_angle_formula = VGroup(full_angle_text, full_angle_math).arrange(RIGHT, buff=0.15)
        full_angle_formula.move_to(LEFT * 2 + DOWN * 0.5)
        
        self.play(
            FadeIn(full_angle_title),
            Create(full_circle),
            Create(arrow_full),
            run_time=1.0
        )
        self.play(FadeIn(full_angle_measure), run_time=0.5)
        self.play(FadeIn(full_angle_formula), run_time=0.8)
        self.wait(1.0)
        
        # ===== 平角 (右侧) =====
        straight_angle_title = Text(
            "平角",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(RIGHT * 2 + UP * 3.5)
        
        straight_center = RIGHT * 2 + UP * 1.5
        straight_line = Line(
            straight_center + LEFT * 1.5,
            straight_center + RIGHT * 1.5,
            color=self.COLOR_PRIMARY,
            stroke_width=5
        )
        
        # 平角的弧（半圆） - 精确π弧度
        straight_arc = Arc(
            radius=0.5,
            start_angle=0,
            angle=np.pi,  # 精确的180度
            color=self.COLOR_ARC,
            stroke_width=4
        ).shift(straight_center)
        
        # 端点
        dot_left = Dot(straight_center + LEFT * 1.5, color=WHITE, radius=0.08)
        dot_right = Dot(straight_center + RIGHT * 1.5, color=WHITE, radius=0.08)
        dot_center = Dot(straight_center, color=self.COLOR_VERTEX, radius=0.12)
        
        straight_angle_measure = MathTex(
            r"180^\circ",
            font_size=36,
            color=self.COLOR_ARC
        ).move_to(straight_center + UP * 0.8)
        
        # 修复: 使用VGroup组合中文Text和MathTex
        straight_angle_text = Text(
            "平角 =",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        straight_angle_math = MathTex(
            r"180^\circ",
            font_size=28,
            color=WHITE
        )
        straight_angle_formula = VGroup(straight_angle_text, straight_angle_math).arrange(RIGHT, buff=0.15)
        straight_angle_formula.move_to(RIGHT * 2 + DOWN * 0.5)
        
        self.play(
            FadeIn(straight_angle_title),
            Create(straight_line),
            FadeIn(dot_left),
            FadeIn(dot_right),
            FadeIn(dot_center),
            run_time=1.0
        )
        self.play(Create(straight_arc), run_time=0.8)
        self.play(FadeIn(straight_angle_measure), run_time=0.5)
        self.play(FadeIn(straight_angle_formula), run_time=0.8)
        self.wait(1.2)
        
        # 对比说明
        comparison = Text(
            "周角是完整一圈, 平角是半圈",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(comparison, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理全部
        self.play(
            FadeOut(title),
            FadeOut(full_angle_title),
            FadeOut(full_circle),
            FadeOut(arrow_full),
            FadeOut(full_angle_measure),
            FadeOut(full_angle_formula),
            FadeOut(straight_angle_title),
            FadeOut(straight_line),
            FadeOut(straight_arc),
            FadeOut(dot_left),
            FadeOut(dot_right),
            FadeOut(dot_center),
            FadeOut(straight_angle_measure),
            FadeOut(straight_angle_formula),
            FadeOut(comparison),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾总结"""
        # 关键点卡片
        key_points = [
            "角 = 两条射线 + 公共端点",
            "表示: ∠AOB, ∠O, ∠α",
            "度量: 1° = 60' = 3600\"",
            "周角360°, 平角180°"
        ]
        
        cards = VGroup()
        for i, point in enumerate(key_points):
            card_bg = Rectangle(
                width=7,
                height=0.8,
                fill_color="#2c3e50",
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )
            
            card_text = Text(
                point,
                font="PingFang SC",
                font_size=20,
                color=WHITE
            )
            
            card = VGroup(card_bg, card_text)
            card.move_to(UP * (2 - i * 1.2))
            card.shift(LEFT * 10)  # 初始位置在左侧外
            cards.add(card)
        
        # 卡片依次滑入
        for card in cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.1)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(DOWN * 4)
        
        self.play(
            FadeOut(cards),
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学知识!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰小角度图标 - 精确45度
        angle_icons = VGroup()
        angle_45 = np.pi / 4.0  # 精确45度
        for i in range(5):
            vertex = Dot(ORIGIN, color=self.COLOR_VERTEX, radius=0.05)
            ray1 = Line(ORIGIN, RIGHT * 0.3, color=self.COLOR_PRIMARY, stroke_width=2)
            ray2 = Line(
                ORIGIN,
                np.array([0.3 * np.cos(angle_45), 0.3 * np.sin(angle_45), 0.0]),
                color=self.COLOR_SECONDARY,
                stroke_width=2
            )
            arc = Arc(
                radius=0.15,
                angle=angle_45,
                color=self.COLOR_ARC,
                stroke_width=2
            )
            
            icon = VGroup(vertex, ray1, ray2, arc)
            icon.scale(0.8)
            angle_icons.add(icon)
        
        angle_icons.arrange(RIGHT, buff=0.5).move_to(DOWN * 7)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in angle_icons],
            run_time=0.6
        )
        self.play(
            Rotate(angle_icons, angle=np.pi/2, run_time=1.2)
        )
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(angle_icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql angle_concept.py AngleConcept  # 快速预览 (低质量)
# manim -pqm angle_concept.py AngleConcept  # 中等质量
# manim -qh angle_concept.py AngleConcept   # 高质量渲染
# manim -qk angle_concept.py AngleConcept   # 4K质量渲染