from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class AxisymmetricFigures(Scene):
    """
    轴对称图形教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 概念讲解
    3. 常见图形判断
    4. 互动练习
    5. 总结
    6. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"
        self.COLOR_SECONDARY = "#2ecc71"
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_AUXILIARY = "#95a5a6"
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_concept()
        self.show_common_figures()
        self.show_practice()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标"""
        # 基准参数
        self.SCALE = 1.0
        self.OFFSET = ORIGIN
        
        # 长方形顶点 (宽4, 高3)
        self.rect_verts = [
            np.array([-2, -1.5, 0]),
            np.array([2, -1.5, 0]),
            np.array([2, 1.5, 0]),
            np.array([-2, 1.5, 0])
        ]
        
        # 正方形顶点 (边长3)
        self.square_verts = [
            np.array([-1.5, -1.5, 0]),
            np.array([1.5, -1.5, 0]),
            np.array([1.5, 1.5, 0]),
            np.array([-1.5, 1.5, 0])
        ]
        
        # 等腰三角形顶点 (底边4, 高3)
        self.tri_verts = [
            np.array([-2, -1.5, 0]),
            np.array([2, -1.5, 0]),
            np.array([0, 1.5, 0])
        ]
        
        # 平行四边形顶点 (非轴对称)
        self.para_verts = [
            np.array([-2, -1.5, 0]),
            np.array([1.5, -1.5, 0]),
            np.array([2, 1.5, 0]),
            np.array([-1.5, 1.5, 0])
        ]
        
        # 验证几何边界
        self.verify_boundaries()
    
    def verify_boundaries(self):
        """验证所有元素在安全边界内"""
        safe_x = 4.0
        safe_y = 7.0
        
        for verts in [self.rect_verts, self.square_verts, self.tri_verts, self.para_verts]:
            for v in verts:
                assert abs(v[0]) < safe_x, f"X坐标超出边界: {v[0]}"
                assert abs(v[1]) < safe_y, f"Y坐标超出边界: {v[1]}"
        
        print("✓ 边界验证通过")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这些图形藏着什么秘密?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 创建四个小图形
        rect = Polygon(*self.rect_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.5).move_to(LEFT * 3 + UP * 2)
        square = Polygon(*self.square_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.5).move_to(RIGHT * 3 + UP * 2)
        circle = Circle(radius=1.5, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.5).move_to(LEFT * 3 + DOWN * 1)
        tri = Polygon(*self.tri_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.5).move_to(RIGHT * 3 + DOWN * 1)
        
        self.play(
            GrowFromCenter(rect),
            GrowFromCenter(square),
            GrowFromCenter(circle),
            GrowFromCenter(tri),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.5)
        
        # 保存图形用于后续场景
        self.opening_rect = rect
        self.opening_square = square
        self.opening_circle = circle
        self.opening_tri = tri
    
    def show_concept(self):
        """场景2: 概念讲解"""
        # 放大长方形到中心
        big_rect = Polygon(*self.rect_verts, color=self.COLOR_PRIMARY, stroke_width=3)
        
        self.play(
            Transform(self.opening_rect, big_rect),
            FadeOut(self.opening_square),
            FadeOut(self.opening_circle),
            FadeOut(self.opening_tri),
            run_time=1.0
        )
        
        # 画出竖对称轴
        axis_v = DashedLine(UP * 4, DOWN * 4, color=self.COLOR_SECONDARY, stroke_width=3)
        
        self.play(Create(axis_v), run_time=1.0)
        
        # 对折动画：左半部分反射到右边
        left_half = Polygon(
            self.rect_verts[0],
            np.array([0, -1.5, 0]),
            np.array([0, 1.5, 0]),
            self.rect_verts[3],
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            fill_opacity=0.5
        )
        
        reflected_left_half = Polygon(
            np.array([0, -1.5, 0]),
            self.rect_verts[1],
            self.rect_verts[2],
            np.array([0, 1.5, 0]),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            fill_opacity=0.5
        )
        
        self.play(Create(left_half), run_time=0.5)
        self.play(Transform(left_half, reflected_left_half), run_time=2.0)
        
        # 显示“完全重合”
        coincide_text = Text(
            "完全重合!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(coincide_text), run_time=0.8)
        self.wait(1.0)
        
        # 显示定义
        def_text_1 = Text(
            "轴对称图形",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        def_text_2 = Text(
            "对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).next_to(axis_v, RIGHT, buff=0.3)
        
        self.play(Write(def_text_1), run_time=0.8)
        self.play(Write(def_text_2), run_time=0.6)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(self.opening_rect),
            FadeOut(left_half),
            FadeOut(axis_v),
            FadeOut(coincide_text),
            FadeOut(def_text_1),
            FadeOut(def_text_2),
            run_time=0.6
        )
    
    def show_common_figures(self):
        """场景3: 常见图形判断"""
        # 1. 长方形
        rect = Polygon(*self.rect_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.8)
        axis_v = DashedLine(UP * 3, DOWN * 3, color=self.COLOR_SECONDARY, stroke_width=2)
        axis_h = DashedLine(LEFT * 4, RIGHT * 4, color=self.COLOR_SECONDARY, stroke_width=2)
        
        self.play(GrowFromCenter(rect), run_time=0.5)
        self.play(Create(axis_v), Create(axis_h), run_time=0.8)
        
        count_text_1 = Text(
            "2条对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(count_text_1), run_time=0.6)
        self.wait(1.5)
        
        # 2. 正方形
        square = Polygon(*self.square_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.8)
        square_axes = VGroup(
            DashedLine(UP * 3, DOWN * 3, color=self.COLOR_SECONDARY, stroke_width=2),
            DashedLine(LEFT * 3, RIGHT * 3, color=self.COLOR_SECONDARY, stroke_width=2),
            DashedLine(UP * 3 + LEFT * 3, DOWN * 3 + RIGHT * 3, color=self.COLOR_SECONDARY, stroke_width=2),
            DashedLine(UP * 3 + RIGHT * 3, DOWN * 3 + LEFT * 3, color=self.COLOR_SECONDARY, stroke_width=2)
        )
        
        self.play(
            FadeOut(rect),
            FadeOut(axis_v),
            FadeOut(axis_h),
            FadeOut(count_text_1),
            GrowFromCenter(square),
            run_time=0.8
        )
        self.play(Create(square_axes), run_time=1.0)
        
        count_text_2 = Text(
            "4条对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(count_text_2), run_time=0.6)
        self.wait(1.5)
        
        # 3. 圆形
        circle = Circle(radius=1.5, color=self.COLOR_PRIMARY, stroke_width=3)
        circle_axis = DashedLine(UP * 3, DOWN * 3, color=self.COLOR_SECONDARY, stroke_width=2)
        
        self.play(
            FadeOut(square),
            FadeOut(square_axes),
            FadeOut(count_text_2),
            GrowFromCenter(circle),
            run_time=0.8
        )
        self.play(Create(circle_axis), run_time=0.5)
        self.play(Rotate(circle_axis, angle=2*PI, about_point=ORIGIN, run_time=3.0))
        
        count_text_3 = Text(
            "无数条对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(count_text_3), run_time=0.6)
        self.wait(1.5)
        
        # 4. 等腰三角形
        tri = Polygon(*self.tri_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.8)
        tri_axis = DashedLine(UP * 3, DOWN * 3, color=self.COLOR_SECONDARY, stroke_width=2)
        
        self.play(
            FadeOut(circle),
            FadeOut(circle_axis),
            FadeOut(count_text_3),
            GrowFromCenter(tri),
            run_time=0.8
        )
        self.play(Create(tri_axis), run_time=0.5)
        
        count_text_4 = Text(
            "1条对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(count_text_4), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(tri),
            FadeOut(tri_axis),
            FadeOut(count_text_4),
            run_time=0.6
        )
    
    def show_practice(self):
        """场景4: 互动练习"""
        # 平行四边形
        para = Polygon(*self.para_verts, color=self.COLOR_PRIMARY, stroke_width=3)
        
        question_text = Text(
            "它是轴对称图形吗?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(GrowFromCenter(para), Write(question_text), run_time=1.0)
        self.wait(2.0)
        
        # 尝试对折
        left_half_para = Polygon(
            self.para_verts[0],
            np.array([0, -1.5, 0]),
            np.array([0, 1.5, 0]),
            self.para_verts[3],
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            fill_opacity=0.5
        )
        
        # 反射后的左半部分（不会重合）
        reflected_left_half_para = Polygon(
            np.array([0, -1.5, 0]),
            self.para_verts[1],
            self.para_verts[2],
            np.array([0, 1.5, 0]),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            fill_opacity=0.5
        )
        
        self.play(Create(left_half_para), run_time=0.5)
        self.play(Transform(left_half_para, reflected_left_half_para), run_time=2.0)
        
        # 显示答案
        answer_text = Text(
            "不是!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=RED
        ).move_to(DOWN * 4)
        
        explanation_text = Text(
            "对折后不能完全重合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(Write(answer_text), run_time=0.6)
        self.play(Write(explanation_text), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(para),
            FadeOut(question_text),
            FadeOut(left_half_para),
            FadeOut(answer_text),
            FadeOut(explanation_text),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景5: 总结"""
        # 四个小图形
        rect_small = Polygon(*self.rect_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.3).move_to(LEFT * 3 + UP * 3)
        square_small = Polygon(*self.square_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.3).move_to(LEFT * 1 + UP * 3)
        circle_small = Circle(radius=1.5, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.3).move_to(RIGHT * 1 + UP * 3)
        tri_small = Polygon(*self.tri_verts, color=self.COLOR_PRIMARY, stroke_width=3).scale(0.3).move_to(RIGHT * 3 + UP * 3)
        
        self.play(
            GrowFromCenter(rect_small),
            GrowFromCenter(square_small),
            GrowFromCenter(circle_small),
            GrowFromCenter(tri_small),
            run_time=1.0
        )
        
        # 总结文字
        summary_text_1 = Text(
            "对折后完全重合",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1)
        
        summary_text_2 = Text(
            "轴对称图形",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 1)
        
        summary_text_3 = Text(
            "对称轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 2.5)
        
        self.play(Write(summary_text_1), run_time=0.8)
        self.wait(1.0)
        self.play(Write(summary_text_2), run_time=0.8)
        self.wait(1.0)
        self.play(Write(summary_text_3), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(rect_small),
            FadeOut(square_small),
            FadeOut(circle_small),
            FadeOut(tri_small),
            FadeOut(summary_text_1),
            FadeOut(summary_text_2),
            FadeOut(summary_text_3),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景6: 片尾关注"""
        # 作者信息放大
        big_author_name = Text(
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
            Transform(self.author_info, big_author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小图形装饰
        decorations = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=self.COLOR_PRIMARY, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql axisymmetric_figures.py AxisymmetricFigures  # 快速预览
# manim -qh axisymmetric_figures.py AxisymmetricFigures   # 高质量