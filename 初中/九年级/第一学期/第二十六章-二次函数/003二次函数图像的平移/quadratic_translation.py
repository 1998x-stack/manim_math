"""
二次函数图像平移 - Quadratic Function Graph Translation
使用 Manim 创建的中学数学教学视频

内容: 二次函数 y=ax² 的图像平移规律
- 上下平移: y = ax² ± k
- 左右平移: y = a(x ∓ h)²
- 综合平移: y = a(x - h)² + k

目标观众: 九年级学生
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


class QuadraticTranslation(Scene):
    """
    二次函数图像平移教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系与基准函数
    3. 上下平移演示
    4. 左右平移演示
    5. 综合平移演示
    6. 总结与口诀
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"      # 红色 - 原始函数
        self.COLOR_VERTICAL = "#3498db"     # 蓝色 - 上下平移
        self.COLOR_HORIZONTAL = "#2ecc71"   # 绿色 - 左右平移
        self.COLOR_COMBINED = "#f39c12"     # 橙色 - 综合平移
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_AXIS = WHITE
        
        # 执行动画序列
        self.show_opening()
        self.setup_axes_and_base_function()
        self.show_vertical_translation()
        self.show_horizontal_translation()
        self.show_combined_translation()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 抓住注意力"""
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
            "抛物线会跳舞?",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.9)
        
        # 小抛物线演示
        demo_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-0.5, 2, 1],
            x_length=3,
            y_length=2,
            axis_config={"include_tip": False, "stroke_width": 2}
        ).move_to(UP * 2.5)
        
        demo_parabola = demo_axes.plot(
            lambda x: 0.5 * x**2,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        demo_group = VGroup(demo_axes, demo_parabola).scale(0.8)
        
        self.play(FadeIn(demo_group), run_time=0.8)
        self.wait(0.3)
        
        # 上下移动
        self.play(demo_group.animate.shift(UP * 0.6), run_time=0.5)
        self.play(demo_group.animate.shift(DOWN * 0.6), run_time=0.5)
        
        # 左右移动
        self.play(demo_group.animate.shift(RIGHT * 0.8), run_time=0.5)
        self.play(demo_group.animate.shift(LEFT * 0.8), run_time=0.5)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(demo_group),
            run_time=0.5
        )
    
    def setup_axes_and_base_function(self):
        """场景2: 建立坐标系与基准函数 y = x²"""
        # 创建坐标系
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 6, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to(DOWN * 0.5)
        
        # 添加坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
        
        self.play(
            Create(self.axes),
            Write(x_label),
            Write(y_label),
            run_time=1.2
        )
        
        # 绘制基准函数 y = x²
        self.graph_original = self.axes.plot(
            lambda x: x**2,
            color=self.COLOR_PRIMARY,
            stroke_width=4,
            x_range=[-2.5, 2.5]
        )
        
        self.play(Create(self.graph_original), run_time=1.5)
        
        # 函数标签
        label_original = MathTex(
            r"y = x^2",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(label_original, shift=UP * 0.2), run_time=0.5)
        
        # 标记顶点 (0, 0)
        vertex_dot = Dot(
            self.axes.c2p(0, 0),
            color=self.COLOR_HIGHLIGHT,
            radius=0.08
        )
        
        vertex_label = MathTex(
            r"(0, 0)",
            font_size=24,
            color=WHITE
        ).next_to(vertex_dot, DOWN + RIGHT, buff=0.15)
        
        self.play(
            FadeIn(vertex_dot, scale=0.5),
            Flash(vertex_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.2),
            run_time=0.5
        )
        self.play(FadeIn(vertex_label), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理顶点标记，保留基准函数但变灰
        self.play(
            FadeOut(vertex_dot),
            FadeOut(vertex_label),
            FadeOut(label_original),
            self.graph_original.animate.set_color(self.COLOR_AUXILIARY).set_stroke(width=2),
            run_time=0.5
        )
        
        # 保存坐标轴标签供后续使用
        self.x_label = x_label
        self.y_label = y_label
    
    def show_vertical_translation(self):
        """场景3: 上下平移演示"""
        # 标题
        title_vertical = Text(
            "上下平移",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_VERTICAL
        ).move_to(UP * 6.5)
        
        self.play(Write(title_vertical), run_time=0.6)
        
        # 通用公式
        formula_base = MathTex(
            r"y = x^2 \rightarrow y = x^2 + k",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(formula_base), run_time=0.8)
        self.wait(0.4)
        
        # === 上移演示 k = 2 ===
        # 公式变化
        formula_up = MathTex(
            r"y = x^2 + 2",
            font_size=36,
            color=self.COLOR_VERTICAL
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_up), run_time=0.6)
        
        # 绘制上移抛物线
        graph_up = self.axes.plot(
            lambda x: x**2 + 2,
            color=self.COLOR_VERTICAL,
            stroke_width=4,
            x_range=[-2.5, 2.5]
        )
        
        self.play(Create(graph_up), run_time=1.2)
        
        # 向上箭头
        arrow_up = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, 2),
            color=self.COLOR_VERTICAL,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_up), run_time=0.4)
        
        # 新顶点
        vertex_up = Dot(
            self.axes.c2p(0, 2),
            color=self.COLOR_VERTICAL,
            radius=0.08
        )
        
        vertex_up_label = MathTex(
            r"(0, 2)",
            font_size=24,
            color=WHITE
        ).next_to(vertex_up, UP + RIGHT, buff=0.15)
        
        self.play(
            FadeIn(vertex_up, scale=0.5),
            Flash(vertex_up, color=self.COLOR_VERTICAL, flash_radius=0.2),
            run_time=0.4
        )
        self.play(FadeIn(vertex_up_label), run_time=0.3)
        
        # 提示文字
        hint_up = Text(
            "k > 0  向上平移",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint_up, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 清理上移元素
        self.play(
            FadeOut(graph_up),
            FadeOut(arrow_up),
            FadeOut(vertex_up),
            FadeOut(vertex_up_label),
            FadeOut(hint_up),
            FadeOut(formula_up),
            run_time=0.5
        )
        
        # === 下移演示 k = -1 ===
        # 公式变化
        formula_down = MathTex(
            r"y = x^2 - 1",
            font_size=36,
            color=self.COLOR_VERTICAL
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_down), run_time=0.6)
        
        # 绘制下移抛物线
        graph_down = self.axes.plot(
            lambda x: x**2 - 1,
            color=self.COLOR_VERTICAL,
            stroke_width=4,
            x_range=[-2.5, 2.5]
        )
        
        self.play(Create(graph_down), run_time=1.2)
        
        # 向下箭头
        arrow_down = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, -1),
            color=self.COLOR_VERTICAL,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_down), run_time=0.4)
        
        # 新顶点
        vertex_down = Dot(
            self.axes.c2p(0, -1),
            color=self.COLOR_VERTICAL,
            radius=0.08
        )
        
        vertex_down_label = MathTex(
            r"(0, -1)",
            font_size=24,
            color=WHITE
        ).next_to(vertex_down, DOWN + RIGHT, buff=0.15)
        
        self.play(
            FadeIn(vertex_down, scale=0.5),
            Flash(vertex_down, color=self.COLOR_VERTICAL, flash_radius=0.2),
            run_time=0.4
        )
        self.play(FadeIn(vertex_down_label), run_time=0.3)
        
        # 提示文字
        hint_down = Text(
            "k < 0  向下平移",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint_down, shift=UP * 0.2), run_time=0.5)
        
        # 口诀
        slogan_v = Text(
            "上加下减",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(slogan_v, scale=1.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title_vertical),
            FadeOut(formula_base),
            FadeOut(formula_down),
            FadeOut(graph_down),
            FadeOut(arrow_down),
            FadeOut(vertex_down),
            FadeOut(vertex_down_label),
            FadeOut(hint_down),
            FadeOut(slogan_v),
            run_time=0.6
        )
        
        # 恢复原始函数颜色
        self.play(
            self.graph_original.animate.set_color(self.COLOR_PRIMARY).set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.3)
        
        # 再次变灰
        self.play(
            self.graph_original.animate.set_color(self.COLOR_AUXILIARY).set_stroke(width=2),
            run_time=0.3
        )
    
    def show_horizontal_translation(self):
        """场景4: 左右平移演示"""
        # 标题
        title_horizontal = Text(
            "左右平移",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HORIZONTAL
        ).move_to(UP * 6.5)
        
        self.play(Write(title_horizontal), run_time=0.6)
        
        # 通用公式
        formula_base = MathTex(
            r"y = x^2 \rightarrow y = (x - h)^2",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(formula_base), run_time=0.8)
        self.wait(0.4)
        
        # === 右移演示 h = 2 ===
        # 公式变化
        formula_right = MathTex(
            r"y = (x - 2)^2",
            font_size=36,
            color=self.COLOR_HORIZONTAL
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_right), run_time=0.6)
        
        # 绘制右移抛物线
        graph_right = self.axes.plot(
            lambda x: (x - 2)**2,
            color=self.COLOR_HORIZONTAL,
            stroke_width=4,
            x_range=[-0.5, 4.5]
        )
        
        self.play(Create(graph_right), run_time=1.2)
        
        # 向右箭头
        arrow_right = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(2, 0),
            color=self.COLOR_HORIZONTAL,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_right), run_time=0.4)
        
        # 新顶点
        vertex_right = Dot(
            self.axes.c2p(2, 0),
            color=self.COLOR_HORIZONTAL,
            radius=0.08
        )
        
        vertex_right_label = MathTex(
            r"(2, 0)",
            font_size=24,
            color=WHITE
        ).next_to(vertex_right, UP + RIGHT, buff=0.15)
        
        self.play(
            FadeIn(vertex_right, scale=0.5),
            Flash(vertex_right, color=self.COLOR_HORIZONTAL, flash_radius=0.2),
            run_time=0.4
        )
        self.play(FadeIn(vertex_right_label), run_time=0.3)
        
        # 提示文字
        hint_right = Text(
            "h > 0  向右平移",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint_right, shift=UP * 0.2), run_time=0.5)
        
        # 特别提示
        warning = Text(
            "注意: (x - 2) 向右!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.3)
        
        self.play(FadeIn(warning, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 清理右移元素
        self.play(
            FadeOut(graph_right),
            FadeOut(arrow_right),
            FadeOut(vertex_right),
            FadeOut(vertex_right_label),
            FadeOut(hint_right),
            FadeOut(warning),
            FadeOut(formula_right),
            run_time=0.5
        )
        
        # === 左移演示 h = -1 (实际是 x+1) ===
        # 公式变化
        formula_left = MathTex(
            r"y = (x + 1)^2",
            font_size=36,
            color=self.COLOR_HORIZONTAL
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_left), run_time=0.6)
        
        # 绘制左移抛物线
        graph_left = self.axes.plot(
            lambda x: (x + 1)**2,
            color=self.COLOR_HORIZONTAL,
            stroke_width=4,
            x_range=[-3.5, 1.5]
        )
        
        self.play(Create(graph_left), run_time=1.2)
        
        # 向左箭头
        arrow_left = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(-1, 0),
            color=self.COLOR_HORIZONTAL,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_left), run_time=0.4)
        
        # 新顶点
        vertex_left = Dot(
            self.axes.c2p(-1, 0),
            color=self.COLOR_HORIZONTAL,
            radius=0.08
        )
        
        vertex_left_label = MathTex(
            r"(-1, 0)",
            font_size=24,
            color=WHITE
        ).next_to(vertex_left, UP + LEFT, buff=0.15)
        
        self.play(
            FadeIn(vertex_left, scale=0.5),
            Flash(vertex_left, color=self.COLOR_HORIZONTAL, flash_radius=0.2),
            run_time=0.4
        )
        self.play(FadeIn(vertex_left_label), run_time=0.3)
        
        # 提示文字
        hint_left = Text(
            "(x + 1) 向左!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint_left, shift=UP * 0.2), run_time=0.6)
        
        # 口诀
        slogan_h = Text(
            "左加右减",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(slogan_h, scale=1.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title_horizontal),
            FadeOut(formula_base),
            FadeOut(formula_left),
            FadeOut(graph_left),
            FadeOut(arrow_left),
            FadeOut(vertex_left),
            FadeOut(vertex_left_label),
            FadeOut(hint_left),
            FadeOut(slogan_h),
            run_time=0.6
        )
        
        # 恢复原始函数颜色
        self.play(
            self.graph_original.animate.set_color(self.COLOR_PRIMARY).set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.3)
        
        # 再次变灰
        self.play(
            self.graph_original.animate.set_color(self.COLOR_AUXILIARY).set_stroke(width=2),
            run_time=0.3
        )
    
    def show_combined_translation(self):
        """场景5: 综合平移演示"""
        # 标题
        title_combined = Text(
            "综合平移",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_COMBINED
        ).move_to(UP * 6.5)
        
        self.play(Write(title_combined), run_time=0.6)
        
        # 完整公式
        formula_combined = MathTex(
            r"y = (x - 1)^2 + 2",
            font_size=36,
            color=self.COLOR_COMBINED
        ).move_to(UP * 5.5)
        
        self.play(Write(formula_combined), run_time=0.8)
        self.wait(0.4)
        
        # === 步骤1: 先向右平移 ===
        step1_text = Text(
            "① 先向右平移 1",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.3)
        
        self.play(FadeIn(step1_text, shift=DOWN * 0.2), run_time=0.6)
        
        # 绘制中间状态 y = (x-1)²
        graph_mid = self.axes.plot(
            lambda x: (x - 1)**2,
            color=self.COLOR_COMBINED,
            stroke_width=3,
            stroke_opacity=0.6,
            x_range=[-1.5, 3.5]
        )
        
        self.play(Create(graph_mid), run_time=1.2)
        
        # 向右箭头
        arrow_h = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(1, 0),
            color=self.COLOR_HORIZONTAL,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_h), run_time=0.5)
        
        # 中间顶点
        vertex_mid = Dot(
            self.axes.c2p(1, 0),
            color=self.COLOR_COMBINED,
            radius=0.07
        )
        
        self.play(FadeIn(vertex_mid, scale=0.5), run_time=0.3)
        self.wait(1.0)
        
        # === 步骤2: 再向上平移 ===
        step2_text = Text(
            "② 再向上平移 2",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(step2_text, shift=DOWN * 0.2), run_time=0.5)
        
        # 计算平移量: 从(1,0)到(1,2)需要向上移动多少屏幕单位
        # axes.c2p(1, 0) → axes.c2p(1, 2) 的差值
        shift_amount = self.axes.c2p(1, 2) - self.axes.c2p(1, 0)
        
        # 平移中间抛物线和顶点
        self.play(
            graph_mid.animate.shift(shift_amount),
            vertex_mid.animate.shift(shift_amount),
            run_time=1.2
        )
        
        # 向上箭头
        arrow_v = Arrow(
            self.axes.c2p(1, 0),
            self.axes.c2p(1, 2),
            color=self.COLOR_VERTICAL,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_v), run_time=0.4)
        
        # 最终顶点高亮
        self.play(
            vertex_mid.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.3),
            Flash(vertex_mid, color=self.COLOR_HIGHLIGHT, flash_radius=0.25),
            run_time=0.5
        )
        
        # 最终顶点标签
        vertex_final_label = MathTex(
            r"(1, 2)",
            font_size=28,
            color=WHITE
        ).next_to(self.axes.c2p(1, 2), UP + RIGHT, buff=0.15)
        
        self.play(FadeIn(vertex_final_label), run_time=0.4)
        
        # 加粗最终抛物线
        self.play(
            graph_mid.animate.set_stroke(width=5, opacity=1),
            run_time=0.5
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title_combined),
            FadeOut(formula_combined),
            FadeOut(step1_text),
            FadeOut(step2_text),
            FadeOut(graph_mid),
            FadeOut(arrow_h),
            FadeOut(arrow_v),
            FadeOut(vertex_mid),
            FadeOut(vertex_final_label),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 总结与口诀"""
        # 标题
        title_summary = Text(
            "平移口诀",
            font="PingFang SC",
            font_size=44,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title_summary), run_time=0.6)
        
        # 通用公式
        formula_general = MathTex(
            r"y = a(x - h)^2 + k",
            font_size=40,
            color=WHITE
        ).move_to(UP * 5.2)
        
        self.play(Write(formula_general), run_time=0.8)
        self.wait(0.4)
        
        # 口诀卡片
        card_width = 6
        card_height = 0.8
        
        # 卡片1: 左加右减
        card1_bg = RoundedRectangle(
            corner_radius=0.15,
            width=card_width,
            height=card_height,
            color=self.COLOR_HORIZONTAL,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(UP * 3.8)
        
        card1_text = Text(
            "左加右减",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HORIZONTAL,
            weight=BOLD
        ).move_to(card1_bg.get_center())
        
        card1 = VGroup(card1_bg, card1_text)
        
        self.play(FadeIn(card1, shift=RIGHT * 0.3), run_time=0.6)
        
        # 卡片2: 上加下减
        card2_bg = RoundedRectangle(
            corner_radius=0.15,
            width=card_width,
            height=card_height,
            color=self.COLOR_VERTICAL,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(UP * 2.6)
        
        card2_text = Text(
            "上加下减",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_VERTICAL,
            weight=BOLD
        ).move_to(card2_bg.get_center())
        
        card2 = VGroup(card2_bg, card2_text)
        
        self.play(FadeIn(card2, shift=RIGHT * 0.3), run_time=0.6)
        
        # 完整口诀
        full_slogan = Text(
            "左加右减, 上加下减!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 1.2)
        
        self.play(FadeIn(full_slogan, scale=1.2), run_time=0.6)
        self.wait(0.4)
        
        # 四个小示例抛物线
        demo_axes_config = {
            "x_range": [-1.5, 1.5, 1],
            "y_range": [-0.5, 1.5, 1],
            "x_length": 1.2,
            "y_length": 1.2,
            "axis_config": {"include_tip": False, "stroke_width": 1}
        }
        
        # 右上: 向右
        demo1_axes = Axes(**demo_axes_config).move_to(UP * 0.2 + RIGHT * 2.5).scale(0.5)
        demo1_graph = demo1_axes.plot(lambda x: (x - 0.5)**2, color=self.COLOR_HORIZONTAL, stroke_width=2)
        demo1_label = Text("右", font="PingFang SC", font_size=18, color=WHITE).next_to(demo1_axes, DOWN, buff=0.1)
        demo1 = VGroup(demo1_axes, demo1_graph, demo1_label)
        
        # 左上: 向左
        demo2_axes = Axes(**demo_axes_config).move_to(UP * 0.2 + LEFT * 2.5).scale(0.5)
        demo2_graph = demo2_axes.plot(lambda x: (x + 0.5)**2, color=self.COLOR_HORIZONTAL, stroke_width=2)
        demo2_label = Text("左", font="PingFang SC", font_size=18, color=WHITE).next_to(demo2_axes, DOWN, buff=0.1)
        demo2 = VGroup(demo2_axes, demo2_graph, demo2_label)
        
        # 右下: 向上
        demo3_axes = Axes(**demo_axes_config).move_to(DOWN * 1.2 + RIGHT * 2.5).scale(0.5)
        demo3_graph = demo3_axes.plot(lambda x: x**2 + 0.5, color=self.COLOR_VERTICAL, stroke_width=2)
        demo3_label = Text("上", font="PingFang SC", font_size=18, color=WHITE).next_to(demo3_axes, DOWN, buff=0.1)
        demo3 = VGroup(demo3_axes, demo3_graph, demo3_label)
        
        # 左下: 向下
        demo4_axes = Axes(**demo_axes_config).move_to(DOWN * 1.2 + LEFT * 2.5).scale(0.5)
        demo4_graph = demo4_axes.plot(lambda x: x**2 - 0.3, color=self.COLOR_VERTICAL, stroke_width=2)
        demo4_label = Text("下", font="PingFang SC", font_size=18, color=WHITE).next_to(demo4_axes, DOWN, buff=0.1)
        demo4 = VGroup(demo4_axes, demo4_graph, demo4_label)
        
        demo_group = VGroup(demo1, demo2, demo3, demo4)
        
        self.play(
            FadeIn(demo1, shift=LEFT * 0.2),
            FadeIn(demo2, shift=RIGHT * 0.2),
            FadeIn(demo3, shift=LEFT * 0.2),
            FadeIn(demo4, shift=RIGHT * 0.2),
            run_time=2.0,
            lag_ratio=0.3
        )
        
        self.wait(1.0)
        
        # 高亮公式中的参数
        h_highlight = SurroundingRectangle(
            formula_general[0][6:9],  # "- h" 部分
            color=self.COLOR_HORIZONTAL,
            buff=0.05
        )
        
        k_highlight = SurroundingRectangle(
            formula_general[0][-3:],  # "+ k" 部分
            color=self.COLOR_VERTICAL,
            buff=0.05
        )
        
        self.play(
            Create(h_highlight),
            Create(k_highlight),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理所有元素
        self.play(
            FadeOut(title_summary),
            FadeOut(formula_general),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(full_slogan),
            FadeOut(demo_group),
            FadeOut(h_highlight),
            FadeOut(k_highlight),
            FadeOut(self.axes),
            FadeOut(self.graph_original),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者名称放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        
        # 抖音ID
        douyin_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(douyin_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰抛物线
        num_parabolas = 5
        parabolas = VGroup()
        
        for i in range(num_parabolas):
            angle = i * 2 * PI / num_parabolas
            pos = 2.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 3
            
            mini_axes = Axes(
                x_range=[-0.5, 0.5, 1],
                y_range=[0, 0.5, 1],
                x_length=0.5,
                y_length=0.5,
                axis_config={"include_tip": False, "stroke_width": 1}
            ).move_to(pos).scale(0.6)
            
            colors = [self.COLOR_PRIMARY, self.COLOR_VERTICAL, self.COLOR_HORIZONTAL, 
                     self.COLOR_COMBINED, GOLD]
            mini_graph = mini_axes.plot(
                lambda x: x**2,
                color=colors[i],
                stroke_width=2
            )
            
            parabolas.add(VGroup(mini_axes, mini_graph))
        
        self.play(
            *[FadeIn(p, scale=0.5) for p in parabolas],
            run_time=0.8,
            lag_ratio=0.1
        )
        
        # 旋转动画
        self.play(
            Rotate(parabolas, angle=PI, run_time=1.5)
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(douyin_id),
            FadeOut(follow_text),
            FadeOut(parabolas),
            run_time=1.0
        )


# 运行命令:
# manim -pql quadratic_translation.py QuadraticTranslation  # 快速预览
# manim -qh quadratic_translation.py QuadraticTranslation   # 高质量 (1080p)