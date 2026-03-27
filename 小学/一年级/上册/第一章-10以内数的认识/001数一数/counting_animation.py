"""
数一数 - Counting Animation
使用 Manim 创建的小学一年级数学教学视频

manim -qh counting_animation.py CountingAnimation

内容: 通过实物学习'点数法'（指一个数一个），做到手口一致，不重复不遗漏
目标观众: 一年级学生
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


class CountingAnimation(Scene):
    """
    数一数教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 数数演示
    3. 互动练习
    4. 总结回顾
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
        self.show_counting_demo()
        self.show_interactive_practice()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化计数相关的几何布局"""
        # 定义网格位置用于摆放物品
        self.grid_positions = []
        rows, cols = 2, 5  # 最多10个物品，2行5列
        start_x, start_y = -4, 2  # 起始位置
        spacing_x, spacing_y = 1.6, 2.5  # 间距
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * spacing_x
                y = start_y - row * spacing_y
                self.grid_positions.append(np.array([x, y, 0]))
        
        # 计数显示位置
        self.count_display_pos = UP * 5.5
        
        # 当前计数位置
        self.current_count_pos = UP * 4
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.5)
        
        # 标题
        title = Text(
            "数一数",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "学会一个一个地数",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 展示几个小动物
        animal1 = Circle(radius=0.4, color=self.COLOR_PRIMARY, fill_opacity=0.7).move_to(LEFT * 2 + UP * 2)
        animal2 = Square(side_length=0.8, color=self.COLOR_SECONDARY, fill_opacity=0.7).move_to(UP * 2)
        animal3 = Triangle(color=self.COLOR_HIGHLIGHT, fill_opacity=0.7).move_to(RIGHT * 2 + UP * 2)
        
        animal1_label = Text("?", font_size=32, color=WHITE).move_to(animal1.get_center())
        animal2_label = Text("?", font_size=32, color=WHITE).move_to(animal2.get_center())
        animal3_label = Text("?", font_size=32, color=WHITE).move_to(animal3.get_center())
        
        animals = VGroup(animal1, animal2, animal3)
        labels = VGroup(animal1_label, animal2_label, animal3_label)
        
        self.wait(0.5)
        self.play(
            Create(animal1),
            Create(animal2),
            Create(animal3),
            run_time=1.0
        )
        self.play(
            Write(animal1_label),
            Write(animal2_label),
            Write(animal3_label),
            run_time=0.6
        )
        
        # 提示文字
        hint = Text(
            "我们来数一数有多少个小动物吧！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理部分元素
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(labels),
            FadeOut(hint),
            run_time=0.5
        )
        
        # 保留动物用于下一个场景
        self.animals = animals
    
    def show_counting_demo(self):
        """场景2: 数数演示 - 用苹果作为例子"""
        # 清空之前的部分元素，保留作者信息
        if hasattr(self, 'animals'):
            self.play(FadeOut(self.animals), run_time=0.5)
        
        # 介绍数数的概念
        instruction = Text(
            "数数要一个一个地数哦！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(instruction), run_time=0.8)
        self.wait(1)
        
        # 展示5个苹果
        apples = VGroup()
        apple_labels = VGroup()
        
        for i in range(5):
            apple = Circle(radius=0.35, color="#e74c3c", fill_opacity=0.8)
            apple.move_to(self.grid_positions[i])
            
            stem = Line(apple.get_top(), apple.get_top() + UP * 0.2, color="#8B4513")
            leaf = Circle(radius=0.1, color=GREEN).move_to(apple.get_top() + UP * 0.15 + RIGHT * 0.1)
            
            apple_group = VGroup(apple, stem, leaf)
            apples.add(apple_group)
        
        self.play(LaggedStart(*[Create(apple) for apple in apples], lag_ratio=0.5), run_time=3)
        self.wait(1)
        
        # 开始数数演示
        self.count_numbers = VGroup()  # 存储计数数字以便后续清理
        
        # 隐藏当前数字的函数
        def hide_current_number():
            if len(self.count_numbers) > 0:
                last_num = self.count_numbers[-1]
                self.play(FadeOut(last_num), run_time=0.3)
        
        # 数数演示循环
        for i in range(5):
            # 显示当前数字
            current_num = Text(str(i + 1), font_size=60, color=self.COLOR_HIGHLIGHT).move_to(self.current_count_pos)
            self.count_numbers.add(current_num)
            
            if i > 0:
                # 隐藏之前的数字
                hide_current_number()
            
            # 高亮当前苹果
            highlight_circle = Circle(radius=0.45, color=self.COLOR_HIGHLIGHT, stroke_width=8)
            highlight_circle.move_to(apples[i].get_center())
            
            # 显示数字和高亮圆圈
            self.play(
                FadeIn(current_num),
                Create(highlight_circle),
                run_time=0.5
            )
            
            self.wait(0.8)
            
            # 移除高亮圆圈
            self.play(FadeOut(highlight_circle), run_time=0.3)
        
        # 最后显示总数
        total_text = Text("总共5个苹果！", font="Noto Sans CJK SC", font_size=32, color=self.COLOR_SECONDARY)
        total_text.move_to(DOWN * 4)
        
        self.play(Write(total_text), run_time=0.8)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(instruction),
            FadeOut(total_text),
            *[FadeOut(apple) for apple in apples],
            *[FadeOut(num) for num in self.count_numbers],
            run_time=0.8
        )
    
    def show_interactive_practice(self):
        """场景3: 互动练习 - 用星星作为例子"""
        # 显示练习指导
        practice_title = Text(
            "现在轮到你啦！",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        instruction = Text(
            "一起来数星星吧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(practice_title), run_time=0.6)
        self.play(Write(instruction), run_time=0.6)
        self.wait(1)
        
        # 展示6颗星星
        stars = VGroup()
        for i in range(6):
            star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.3)
            star.move_to(self.grid_positions[i])
            stars.add(star)
        
        self.play(LaggedStart(*[DrawBorderThenFill(star) for star in stars], lag_ratio=0.6), run_time=4)
        self.wait(1)
        
        # 学生跟随数数
        self.count_numbers = VGroup()  # 重新初始化计数数字组
        
        for i in range(6):
            # 显示当前数字
            current_num = Text(str(i + 1), font_size=60, color=self.COLOR_HIGHLIGHT).move_to(self.current_count_pos)
            self.count_numbers.add(current_num)
            
            if i > 0:
                # 隐藏之前的数字
                prev_num = self.count_numbers[-2]
                self.play(FadeOut(prev_num), run_time=0.3)
            
            # 高亮当前星星
            highlight = Circle(radius=0.4, color=self.COLOR_HIGHLIGHT, stroke_width=6)
            highlight.move_to(stars[i].get_center())
            
            # 显示数字和高亮
            self.play(
                FadeIn(current_num),
                Create(highlight),
                run_time=0.6
            )
            
            self.wait(0.7)
            
            # 移除高亮
            self.play(FadeOut(highlight), run_time=0.3)
        
        # 显示最终结果
        final_text = Text("答对啦！是6颗星星！", font="Noto Sans CJK SC", font_size=32, color=self.COLOR_SECONDARY)
        final_text.move_to(DOWN * 4)
        
        # 显示总数数字
        total_num = Text("6", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(self.count_display_pos)
        
        self.play(
            Write(final_text),
            Write(total_num),
            run_time=0.8
        )
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(practice_title),
            FadeOut(instruction),
            FadeOut(final_text),
            FadeOut(total_num),
            *[FadeOut(star) for star in stars],
            *[FadeOut(num) for num in self.count_numbers if num in self.mobjects],
            run_time=1.0
        )
    
    def show_summary(self):
        """场景4: 总结回顾"""
        # 总结要点
        points = VGroup(
            Text("✓ 数数时要一个一个地数", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ 手指指着物体，嘴巴说出数字", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SECONDARY),
            Text("✓ 不要重复数，也不要漏掉", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        )
        points.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        points.move_to(UP * 1)
        
        title = Text(
            "今天学到的知识：",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 4)
        
        self.play(Write(title), run_time=0.6)
        self.play(LaggedStart(*[Write(point) for point in points], lag_ratio=0.8), run_time=2.5)
        
        self.wait(3)
        
        # 鼓励话语
        encouragement = Text(
            "你已经学会了数数！\n继续加油哦！",
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


# 辅助类：绘制星星
class Star(Polygon):
    def __init__(self, outer_radius=1, inner_radius=0.4, color=YELLOW, fill_opacity=1, **kwargs):
        # 计算星星的顶点
        outer_points = []
        inner_points = []
        
        for i in range(5):
            angle_outer = i * 4 * PI / 5 - PI / 2
            angle_inner = (i + 0.5) * 4 * PI / 5 - PI / 2
            
            outer_points.append(np.array([
                outer_radius * np.cos(angle_outer),
                outer_radius * np.sin(angle_outer),
                0
            ]))
            
            inner_points.append(np.array([
                inner_radius * np.cos(angle_inner),
                inner_radius * np.sin(angle_inner),
                0
            ]))
        
        # 构建顶点数组（交替添加外顶点和内顶点）
        all_points = []
        for i in range(5):
            all_points.append(outer_points[i])
            all_points.append(inner_points[i])
        
        super().__init__(*all_points, color=color, fill_opacity=fill_opacity, **kwargs)