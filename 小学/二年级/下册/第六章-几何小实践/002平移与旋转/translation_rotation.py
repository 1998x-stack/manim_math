"""
平移与旋转 - 二年级几何小实践
使用 Manim 创建的数学教学动画
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

# 快速预览 (480p)
manim -pql translation_rotation.py TranslationRotation

# 高质量 (1080p)
manim -pqh translation_rotation.py TranslationRotation
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TranslationRotation(Scene):
    """
    平移与旋转教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 平移概念
    3. 平移生活例子
    4. 旋转概念
    5. 旋转生活例子
    6. 对比总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#4ecdc4"
        self.COLOR_SECONDARY = "#ff6b6b"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据 (如果有需要)
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_translation_concept()
        self.show_translation_examples()
        self.show_rotation_concept()
        self.show_rotation_examples()
        self.show_comparison()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化几何数据（如果需要精确计算）"""
        # 定义一些常用位置，确保安全边界
        self.CENTER = ORIGIN
        self.LEFT_POS = LEFT * 3
        self.RIGHT_POS = RIGHT * 3
        self.UP_POS = UP * 2
        self.DOWN_POS = DOWN * 2
        
        # 平移距离
        self.TRANSLATE_DIST = 3.0
        
        # 旋转角度
        self.ROTATE_ANGLE = PI / 2
        
        # 验证边界 (可选项)
        self.verify_bounds()
    
    def verify_bounds(self):
        """简单边界验证"""
        # 检查常用位置是否在安全边界内
        safe_x = 4.0
        safe_y_top = 6.0
        safe_y_bottom = -7.0
        positions = [self.LEFT_POS, self.RIGHT_POS, self.UP_POS, self.DOWN_POS]
        for pos in positions:
            assert abs(pos[0]) <= safe_x, f"X坐标超出边界: {pos[0]}"
            assert safe_y_bottom <= pos[1] <= safe_y_top, f"Y坐标超出边界: {pos[1]}"
        print("✓ 边界验证通过")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "平移与旋转，\n你会区分吗？",
            font="PingFang SC",
            font_size=48,
            color=GOLD,
            line_spacing=1.2
        ).move_to(UP * 3)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简单图形
        rect = Rectangle(width=2, height=1.5, color=self.COLOR_PRIMARY, fill_opacity=0.5).move_to(LEFT * 2 + DOWN)
        circle = Circle(radius=0.8, color=self.COLOR_SECONDARY, fill_opacity=0.5).move_to(RIGHT * 2 + DOWN)
        
        self.play(FadeIn(rect), FadeIn(circle), run_time=0.6)
        self.wait(1.0)
        
        # 清理钩子文字，保留图形和作者信息
        self.play(FadeOut(hook_text), run_time=0.4)
        
        # 保存图形以便后续使用
        self.rect = rect
        self.circle = circle
        self.author_info = author_info
    
    def show_translation_concept(self):
        """场景2: 平移概念"""
        # 高亮矩形
        self.play(self.rect.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        # 创建箭头
        arrow = Arrow(
            start=self.rect.get_center() + RIGHT * 0.5,
            end=self.rect.get_center() + RIGHT * (self.TRANSLATE_DIST - 0.5),
            color=self.COLOR_AUXILIARY,
            stroke_width=8
        )
        self.play(Create(arrow), run_time=0.5)
        
        # 矩形平移
        self.play(self.rect.animate.shift(RIGHT * self.TRANSLATE_DIST), run_time=1.0)
        self.wait(0.3)
        
        # 创建一个半透明的副本留在终点，原矩形复位
        rect_copy = self.rect.copy().set_opacity(0.3)
        self.add(rect_copy)
        self.play(self.rect.animate.shift(LEFT * self.TRANSLATE_DIST), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "平移：物体沿直线移动\n方向、大小、形状不变",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 4)
        
        self.play(Write(explain), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(arrow), FadeOut(rect_copy), FadeOut(explain), run_time=0.5)
        self.play(self.rect.animate.set_color(self.COLOR_PRIMARY), run_time=0.3)
    
    def show_translation_examples(self):
        """场景3: 平移生活例子"""
        # 电梯例子
        elevator_bg = Rectangle(width=2, height=4, color=GRAY, stroke_width=3).move_to(LEFT * 3)
        elevator_car = Rectangle(width=1.5, height=1.2, color=self.COLOR_PRIMARY, fill_opacity=0.7).move_to(LEFT * 3 + DOWN * 1.5)
        
        self.play(FadeIn(elevator_bg), FadeIn(elevator_car), run_time=0.5)
        
        # 电梯上升
        self.play(elevator_car.animate.shift(UP * 2.5), run_time=1.0)
        self.wait(0.2)
        # 电梯下降
        self.play(elevator_car.animate.shift(DOWN * 2.5), run_time=1.0)
        
        # 文字标签
        label_elevator = Text("电梯升降", font="PingFang SC", font_size=22, color=WHITE).next_to(elevator_bg, DOWN, buff=0.3)
        self.play(FadeIn(label_elevator), run_time=0.3)
        
        # 推拉窗户例子 (右侧)
        window_frame = Rectangle(width=2, height=2, color=GRAY, stroke_width=3).move_to(RIGHT * 3)
        window_pane = Rectangle(width=1.8, height=1.8, color=self.COLOR_SECONDARY, fill_opacity=0.5).move_to(RIGHT * 3)
        
        self.play(FadeIn(window_frame), FadeIn(window_pane), run_time=0.5)
        
        # 窗户右移
        self.play(window_pane.animate.shift(RIGHT * 1.5), run_time=0.8)
        self.wait(0.2)
        # 窗户左移
        self.play(window_pane.animate.shift(LEFT * 1.5), run_time=0.8)
        
        label_window = Text("推拉窗户", font="PingFang SC", font_size=22, color=WHITE).next_to(window_frame, DOWN, buff=0.3)
        self.play(FadeIn(label_window), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理例子
        self.play(
            FadeOut(elevator_bg), FadeOut(elevator_car), FadeOut(label_elevator),
            FadeOut(window_frame), FadeOut(window_pane), FadeOut(label_window),
            run_time=0.6
        )
    
    def show_rotation_concept(self):
        """场景4: 旋转概念"""
        # 创建风车 (四个扇形)
        center = ORIGIN
        radius = 1.5
        colors = [self.COLOR_PRIMARY, self.COLOR_SECONDARY, BLUE_C, PURPLE]
        blades = VGroup()
        for i, color in enumerate(colors):
            angle_start = i * PI / 2
            blade = Sector(
                radius=radius,
                start_angle=angle_start,
                angle=PI / 2,
                color=color,
                fill_opacity=0.7,
                stroke_width=1
            ).move_to(center)
            blades.add(blade)
        
        # 中心点
        center_dot = Dot(center, color=self.COLOR_HIGHLIGHT, radius=0.1)
        
        self.play(Create(blades), FadeIn(center_dot), run_time=1.0)
        
        # 旋转半圈，展示运动
        self.play(blades.animate.rotate(PI), run_time=2.0, rate_func=smooth)
        self.wait(0.3)
        
        # 绘制旋转路径 (弧线)
        arc = ArcBetweenPoints(
            start=blades[0].get_arc_center() + radius * RIGHT,
            end=blades[0].get_arc_center() + radius * UP,
            radius=radius,
            color=YELLOW,
            stroke_width=4
        )
        self.play(Create(arc), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "旋转：物体绕固定点转动\n形状大小不变，方向改变",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 4)
        
        self.play(Write(explain), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(blades), FadeOut(center_dot), FadeOut(arc), FadeOut(explain), run_time=0.6)
    
    def show_rotation_examples(self):
        """场景5: 旋转生活例子"""
        # 钟表指针
        clock_center = LEFT * 3
        clock_face = Circle(radius=1.5, color=GRAY, stroke_width=3).move_to(clock_center)
        hand = Line(
            start=clock_center,
            end=clock_center + UP * 1.2,
            color=self.COLOR_PRIMARY,
            stroke_width=6
        )
        # 添加刻度标记
        marks = VGroup()
        for angle in np.linspace(0, 2*PI, 12, endpoint=False):
            mark = Line(
                clock_center + 1.3 * np.array([np.sin(angle), np.cos(angle), 0]),
                clock_center + 1.5 * np.array([np.sin(angle), np.cos(angle), 0]),
                color=GRAY_B
            )
            marks.add(mark)
        
        self.play(FadeIn(clock_face), FadeIn(marks), FadeIn(hand), run_time=0.8)
        
        # 指针旋转 (从12点到3点)
        self.play(hand.animate.rotate(-PI/2, about_point=clock_center), run_time=1.0)
        self.wait(0.2)
        self.play(hand.animate.rotate(PI/2, about_point=clock_center), run_time=1.0)
        
        label_clock = Text("钟表指针", font="PingFang SC", font_size=22, color=WHITE).next_to(clock_face, DOWN, buff=0.3)
        self.play(FadeIn(label_clock), run_time=0.3)
        
        # 陀螺 (简单圆锥)
        spintop_center = RIGHT * 3
        spintop = VGroup(
            Triangle(color=self.COLOR_SECONDARY, fill_opacity=0.7).scale(0.8).rotate(PI/2).move_to(spintop_center + DOWN*0.5),
            Line(spintop_center + DOWN*0.2, spintop_center + DOWN*1.2, color=GRAY, stroke_width=4),
            Circle(radius=0.15, color=GRAY, fill_opacity=1).move_to(spintop_center + DOWN*1.2)
        )
        spintop.move_to(spintop_center)
        
        self.play(FadeIn(spintop), run_time=0.5)
        
        # 陀螺旋转
        self.play(spintop.animate.rotate(2*PI, about_point=spintop_center + DOWN*1.2), run_time=1.5)
        
        label_spintop = Text("陀螺", font="PingFang SC", font_size=22, color=WHITE).next_to(spintop, DOWN, buff=0.3)
        self.play(FadeIn(label_spintop), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(clock_face), FadeOut(marks), FadeOut(hand), FadeOut(label_clock),
            FadeOut(spintop), FadeOut(label_spintop),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 对比总结"""
        # 左侧: 电梯缩略
        elevator_small = VGroup(
            Rectangle(width=1, height=2, color=GRAY, stroke_width=2).move_to(LEFT * 2.5 + DOWN),
            Rectangle(width=0.8, height=0.6, color=self.COLOR_PRIMARY, fill_opacity=0.7).move_to(LEFT * 2.5 + DOWN - UP*0.7)
        )
        # 右侧: 风车缩略
        blades_small = VGroup()
        radius_small = 0.8
        center_small = RIGHT * 2.5 + DOWN
        colors = [self.COLOR_PRIMARY, self.COLOR_SECONDARY, BLUE_C, PURPLE]
        for i, color in enumerate(colors):
            angle_start = i * PI / 2
            blade = Sector(
                radius=radius_small,
                start_angle=angle_start,
                angle=PI / 2,
                color=color,
                fill_opacity=0.7,
                stroke_width=1
            ).move_to(center_small)
            blades_small.add(blade)
        center_dot_small = Dot(center_small, color=YELLOW, radius=0.05)
        blades_small.add(center_dot_small)
        
        self.play(FadeIn(elevator_small), FadeIn(blades_small), run_time=0.8)
        
        # 电梯上下移动一次
        self.play(elevator_small[1].animate.shift(UP * 0.5), run_time=0.5)
        self.play(elevator_small[1].animate.shift(DOWN * 0.5), run_time=0.5)
        
        # 风车旋转一圈
        self.play(blades_small[:-1].animate.rotate(2*PI, about_point=center_small), run_time=1.5)
        
        # 总结文字
        summary = Text(
            "平移：沿直线移动\n旋转：绕点转动",
            font="PingFang SC",
            font_size=30,
            color=GOLD,
            line_spacing=1.2
        ).move_to(DOWN * 2)
        
        self.play(Write(summary), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(elevator_small), FadeOut(blades_small), FadeOut(summary), run_time=0.6)
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_big = Text(
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
        
        self.play(Transform(self.author_info, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何知识！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰小图形 (两个小箭头旋转)
        arrow1 = Arrow(LEFT*0.3, RIGHT*0.3, color=GOLD).move_to(DOWN * 2 + LEFT)
        arrow2 = Arrow(LEFT*0.3, RIGHT*0.3, color=GOLD).move_to(DOWN * 2 + RIGHT)
        self.play(FadeIn(arrow1), FadeIn(arrow2), run_time=0.4)
        self.play(
            Rotate(arrow1, angle=2*PI, about_point=arrow1.get_center()),
            Rotate(arrow2, angle=-2*PI, about_point=arrow2.get_center()),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(arrow1),
            FadeOut(arrow2),
            run_time=1.0
        )