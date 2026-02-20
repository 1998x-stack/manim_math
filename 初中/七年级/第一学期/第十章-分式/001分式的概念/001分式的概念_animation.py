"""
001分式的概念 - Animation
使用 Manim 创建的数学教学视频

内容: 001分式的概念
目标观众: 学生
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


class Topic001分式的概念Animation(Scene):
    """
    001分式的概念 教学动画场景
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
        self.COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 高亮元素
        self.COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助元素
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_main_content()
        self.show_examples()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何布局"""
        # 定义关键位置
        self.center_pos = ORIGIN
        self.top_pos = UP * 6
        self.bottom_pos = DOWN * 6
        self.left_pos = LEFT * 4
        self.right_pos = RIGHT * 4
        
        # 定义网格位置用于摆放元素
        self.grid_positions = []
        rows, cols = 3, 3
        start_x, start_y = -3, 2
        spacing_x, spacing_y = 2, 2
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * spacing_x
                y = start_y - row * spacing_y
                self.grid_positions.append(np.array([x, y, 0]))
    
    def show_opening(self):
        """开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.5)
        
        # 标题
        title = Text(
            "001分式的概念",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=1.0)
        self.wait(1)
        
        # 清理
        self.play(FadeOut(title), run_time=0.5)
    
    def show_main_content(self):
        """主要内容展示"""
        # 根据主题创建相应内容
        content_text = Text(
            "正在学习001分式的概念的概念...",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3)
        
        self.play(Write(content_text), run_time=1.0)
        self.wait(2)
        
        # 示例元素
        example_elements = VGroup()
        for i in range(3):
            element = Circle(radius=0.5, color=self.COLOR_HIGHLIGHT, fill_opacity=0.7)
            element.move_to(self.grid_positions[i])
            example_elements.add(element)
        
        self.play(LaggedStart(*[Create(el) for el in example_elements], lag_ratio=0.5), run_time=2)
        self.wait(2)
        
        # 清理
        self.play(FadeOut(content_text), *[FadeOut(el) for el in example_elements], run_time=0.8)
    
    def show_examples(self):
        """示例演示"""
        example_text = Text(
            "让我们看一个例子:",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 4)
        
        self.play(Write(example_text), run_time=0.8)
        self.wait(1)
        
        # 创建示例
        example_visual = Square(side_length=2, color=self.COLOR_AUXILIARY)
        example_visual.move_to(ORIGIN)
        
        self.play(Create(example_visual), run_time=1.0)
        self.wait(2)
        
        # 清理
        self.play(FadeOut(example_text), FadeOut(example_visual), run_time=0.8)
    
    def show_summary(self):
        """总结回顾"""
        summary_points = VGroup(
            Text("✓ 今天我们学习了001分式的概念", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ 这是一个重要的数学概念", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SECONDARY),
            Text("✓ 多多练习才能掌握", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        )
        summary_points.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        summary_points.move_to(UP * 1)
        
        title = Text(
            "今天学到的知识：",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 4)
        
        self.play(Write(title), run_time=0.6)
        self.play(LaggedStart(*[Write(point) for point in summary_points], lag_ratio=0.8), run_time=2.5)
        
        self.wait(3)
        
        # 鼓励话语
        encouragement = Text(
            "你学得真棒！\\n继续加油哦！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Write(encouragement), run_time=1.0)
        self.wait(3)
        
        # 关注提醒
        follow_reminder = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(follow_reminder, shift=UP * 0.3), run_time=0.5)
        self.wait(3)
