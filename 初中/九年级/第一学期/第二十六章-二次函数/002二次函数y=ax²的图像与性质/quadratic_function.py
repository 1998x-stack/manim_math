"""
二次函数 y=ax² 的图像与性质
Quadratic Function y=ax² - Properties and Graph

使用 Manim 创建的九年级数学教学视频
内容: 二次函数 y=ax² 的图像特征、顶点、对称轴、开口方向、增减性
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


class QuadraticFunction(Scene):
    """
    二次函数 y=ax² 教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. a>0 的情况
    4. a<0 的情况
    5. |a|对开口大小的影响
    6. 性质总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PARABOLA_POSITIVE = "#e74c3c"  # 红色 - a>0
        self.COLOR_PARABOLA_NEGATIVE = "#3498db"  # 蓝色 - a<0
        self.COLOR_VERTEX = "#2ecc71"             # 绿色 - 顶点
        self.COLOR_AXIS = "#f39c12"               # 橙色 - 对称轴
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 执行动画序列
        self.show_opening()
        self.show_coordinate_system()
        self.show_positive_a()
        self.show_negative_a()
        self.show_a_magnitude_effect()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
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
            "抛物线的秘密在哪里?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 快速闪现抛物线轮廓
        outline_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=3,
            axis_config={"stroke_width": 0}
        ).move_to(UP * 2)
        
        outline = outline_axes.plot(
            lambda x: x**2,
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        self.play(Create(outline), run_time=0.6)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(outline),
            run_time=0.4
        )
    
    def show_coordinate_system(self):
        """场景2: 建立坐标系"""
        # 创建坐标系 - 竖屏适配
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 5, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18,
            },
            tips=True
        ).move_to(UP * 0.5)
        
        # 坐标轴标签
        x_label = Text("x", font_size=24).next_to(self.axes.x_axis, RIGHT, buff=0.2)
        y_label = Text("y", font_size=24).next_to(self.axes.y_axis, UP, buff=0.2)
        
        self.play(Create(self.axes), run_time=1.2)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 原点标记
        self.origin_dot = Dot(
            self.axes.c2p(0, 0),
            color=self.COLOR_VERTEX,
            radius=0.08
        )
        
        origin_label = Text(
            "O",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(self.origin_dot, DL, buff=0.15)
        
        self.play(FadeIn(self.origin_dot, scale=0.5), run_time=0.3)
        self.play(FadeIn(origin_label), run_time=0.3)
        
        # 顶点标注
        vertex_label = Text(
            "顶点: (0, 0)",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_VERTEX
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(vertex_label, shift=UP * 0.2), run_time=0.5)
        
        # 对称轴
        self.symmetry_axis = DashedLine(
            self.axes.c2p(0, -3),
            self.axes.c2p(0, 5),
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=2
        )
        
        axis_label = Text(
            "对称轴: x = 0",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_AXIS
        ).move_to(DOWN * 5.2)
        
        self.play(Create(self.symmetry_axis), run_time=0.8)
        self.play(FadeIn(axis_label), run_time=0.5)
        
        self.wait(0.8)
        
        # 清理标签
        self.play(
            FadeOut(vertex_label),
            FadeOut(axis_label),
            FadeOut(origin_label),
            FadeOut(x_label),
            FadeOut(y_label),
            self.symmetry_axis.animate.set_opacity(0.3),
            run_time=0.5
        )
    
    def show_positive_a(self):
        """场景3: a>0 的情况"""
        # 标题
        title = Text(
            "当 a > 0 时",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PARABOLA_POSITIVE,
            weight=BOLD
        ).move_to(UP * 6)
        
        # 公式
        formula = MathTex(
            r"y = x^2",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=0.8)
        
        # 绘制抛物线
        self.parabola_pos = self.axes.plot(
            lambda x: x**2,
            x_range=[-2.5, 2.5],
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=5
        )
        
        self.play(Create(self.parabola_pos), run_time=2.0)
        
        # 开口方向箭头
        arrow_up = Arrow(
            self.axes.c2p(0, 1.5),
            self.axes.c2p(0, 3),
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.2
        )
        
        arrow_label = Text(
            "开口向上",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_PARABOLA_POSITIVE
        ).next_to(arrow_up, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_up), run_time=0.5)
        self.play(FadeIn(arrow_label), run_time=0.3)
        
        # 最小值标注
        min_label = VGroup(
            Text("最小值:", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            MathTex("y_{\\text{min}} = 0", font_size=20, color=self.COLOR_VERTEX)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4)
        
        self.play(FadeIn(min_label), run_time=0.5)
        self.play(Flash(self.origin_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.4)
        
        # 增减性标注
        # 左侧递减
        decreasing_label = Text(
            "递减",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(self.axes.c2p(-1.8, 2))
        
        decreasing_arrow = Arrow(
            self.axes.c2p(-1.5, 2.5),
            self.axes.c2p(-0.5, 0.5),
            color=GRAY_A,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 右侧递增
        increasing_label = Text(
            "递增",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(self.axes.c2p(1.8, 2))
        
        increasing_arrow = Arrow(
            self.axes.c2p(0.5, 0.5),
            self.axes.c2p(1.5, 2.5),
            color=GRAY_A,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            FadeIn(decreasing_label),
            GrowArrow(decreasing_arrow),
            run_time=0.5
        )
        self.play(
            FadeIn(increasing_label),
            GrowArrow(increasing_arrow),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(arrow_up),
            FadeOut(arrow_label),
            FadeOut(min_label),
            FadeOut(decreasing_label),
            FadeOut(decreasing_arrow),
            FadeOut(increasing_label),
            FadeOut(increasing_arrow),
            self.parabola_pos.animate.set_opacity(0.2),
            run_time=0.6
        )
    
    def show_negative_a(self):
        """场景4: a<0 的情况"""
        # 标题
        title = Text(
            "当 a < 0 时",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PARABOLA_NEGATIVE,
            weight=BOLD
        ).move_to(UP * 6)
        
        # 公式
        formula = MathTex(
            r"y = -x^2",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=0.8)
        
        # 绘制抛物线
        self.parabola_neg = self.axes.plot(
            lambda x: -x**2,
            x_range=[-2.5, 2.5],
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=5
        )
        
        self.play(Create(self.parabola_neg), run_time=2.0)
        
        # 开口方向箭头
        arrow_down = Arrow(
            self.axes.c2p(0, -1.5),
            self.axes.c2p(0, -2.8),
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.2
        )
        
        arrow_label = Text(
            "开口向下",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_PARABOLA_NEGATIVE
        ).next_to(arrow_down, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_down), run_time=0.5)
        self.play(FadeIn(arrow_label), run_time=0.3)
        
        # 最大值标注
        max_label = VGroup(
            Text("最大值:", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            MathTex("y_{\\text{max}} = 0", font_size=20, color=self.COLOR_VERTEX)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4)
        
        self.play(FadeIn(max_label), run_time=0.5)
        self.play(Flash(self.origin_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.4)
        
        # 增减性标注
        # 左侧递增
        increasing_label = Text(
            "递增",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(self.axes.c2p(-1.8, -2))
        
        increasing_arrow = Arrow(
            self.axes.c2p(-1.5, -2.5),
            self.axes.c2p(-0.5, -0.5),
            color=GRAY_A,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 右侧递减
        decreasing_label = Text(
            "递减",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).move_to(self.axes.c2p(1.8, -2))
        
        decreasing_arrow = Arrow(
            self.axes.c2p(0.5, -0.5),
            self.axes.c2p(1.5, -2.5),
            color=GRAY_A,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            FadeIn(increasing_label),
            GrowArrow(increasing_arrow),
            run_time=0.5
        )
        self.play(
            FadeIn(decreasing_label),
            GrowArrow(decreasing_arrow),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(arrow_down),
            FadeOut(arrow_label),
            FadeOut(max_label),
            FadeOut(increasing_label),
            FadeOut(increasing_arrow),
            FadeOut(decreasing_label),
            FadeOut(decreasing_arrow),
            self.parabola_neg.animate.set_opacity(0.2),
            run_time=0.6
        )
    
    def show_a_magnitude_effect(self):
        """场景5: |a|对开口大小的影响"""
        # 清空旧抛物线
        self.play(
            FadeOut(self.parabola_pos),
            FadeOut(self.parabola_neg),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "|a| 的大小影响开口",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.7)
        
        # 绘制三条抛物线对比
        # y = 0.5x² (最宽)
        para_05 = self.axes.plot(
            lambda x: 0.5 * x**2,
            x_range=[-3, 3],
            color="#ff7675",  # 浅红色
            stroke_width=4
        )
        
        label_05 = MathTex(
            r"a = 0.5",
            font_size=20,
            color="#ff7675"
        ).move_to(self.axes.c2p(2.5, 3.5))
        
        self.play(Create(para_05), run_time=1.0)
        self.play(FadeIn(label_05), run_time=0.3)
        
        # y = x² (标准)
        para_1 = self.axes.plot(
            lambda x: x**2,
            x_range=[-2.5, 2.5],
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        label_1 = MathTex(
            r"a = 1",
            font_size=20,
            color=self.COLOR_PARABOLA_POSITIVE
        ).move_to(self.axes.c2p(2, 4.2))
        
        self.play(Create(para_1), run_time=1.0)
        self.play(FadeIn(label_1), run_time=0.3)
        
        # y = 2x² (最窄)
        para_2 = self.axes.plot(
            lambda x: 2 * x**2,
            x_range=[-1.8, 1.8],
            color="#c0392b",  # 深红色
            stroke_width=4
        )
        
        label_2 = MathTex(
            r"a = 2",
            font_size=20,
            color="#c0392b"
        ).move_to(self.axes.c2p(1.3, 4.5))
        
        self.play(Create(para_2), run_time=1.0)
        self.play(FadeIn(label_2), run_time=0.3)
        
        # 对比动画
        self.play(
            Indicate(para_2, scale_factor=1.05, color="#c0392b"),
            run_time=0.8
        )
        self.play(
            Indicate(para_05, scale_factor=1.05, color="#ff7675"),
            run_time=0.8
        )
        
        # 结论文字
        conclusion = Text(
            "|a| 越大，开口越小",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(para_05),
            FadeOut(para_1),
            FadeOut(para_2),
            FadeOut(label_05),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 性质总结"""
        # 清空坐标系
        self.play(
            FadeOut(self.axes),
            FadeOut(self.origin_dot),
            FadeOut(self.symmetry_axis),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "性质总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 背景装饰抛物线
        bg_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 3, 1],
            x_length=3,
            y_length=2.5,
            axis_config={"stroke_width": 0}
        ).move_to(UP * 5)
        
        bg_parabola = bg_axes.plot(
            lambda x: 0.5 * x**2,
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=2,
            stroke_opacity=0.3
        )
        
        self.play(FadeIn(bg_parabola), run_time=0.5)
        
        # 性质卡片
        cards = VGroup()
        
        # 卡片1: 顶点
        card_1 = self.create_property_card(
            "顶点",
            "(0, 0)",
            self.COLOR_VERTEX,
            UP * 2.5
        )
        cards.add(card_1)
        
        # 卡片2: 对称轴
        card_2 = self.create_property_card(
            "对称轴",
            "x = 0 (y轴)",
            self.COLOR_AXIS,
            UP * 1
        )
        cards.add(card_2)
        
        # 卡片3: a>0
        card_3 = self.create_property_card(
            "a > 0",
            "开口向上, 最小值 0",
            self.COLOR_PARABOLA_POSITIVE,
            DOWN * 0.5
        )
        cards.add(card_3)
        
        # 卡片4: a<0
        card_4 = self.create_property_card(
            "a < 0",
            "开口向下, 最大值 0",
            self.COLOR_PARABOLA_NEGATIVE,
            DOWN * 2
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 整体强调
        self.play(
            Flash(cards, color=self.COLOR_HIGHLIGHT, flash_radius=1.0, num_lines=12),
            run_time=0.8
        )
        
        # 重点提示
        highlight_text = Text(
            "掌握 y=ax² , 轻松解题!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(bg_parabola),
            FadeOut(cards),
            FadeOut(highlight_text),
            run_time=0.6
        )
    
    def create_property_card(self, title_text, content_text, color, position):
        """创建性质卡片"""
        # 图标圆
        icon = Circle(
            radius=0.15,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title = Text(
            title_text,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )
        
        # 内容
        content = Text(
            content_text,
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title, content).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 抛物线装饰
        deco_parabolas = VGroup()
        
        for i in range(3):
            small_axes = Axes(
                x_range=[-1, 1, 1],
                y_range=[0, 1, 1],
                x_length=1,
                y_length=0.8,
                axis_config={"stroke_width": 0}
            )
            
            para = small_axes.plot(
                lambda x: 0.8 * x**2,
                color=[self.COLOR_PARABOLA_POSITIVE, GOLD, self.COLOR_PARABOLA_NEGATIVE][i],
                stroke_width=3
            )
            
            deco_parabolas.add(para)
        
        deco_parabolas.arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)
        
        self.play(
            *[Create(para, run_time=1.0) for para in deco_parabolas],
        )
        
        # 旋转动画
        self.play(
            Rotate(deco_parabolas, angle=PI, run_time=1.5),
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_parabolas),
            run_time=1.0
        )


# 运行命令:
# manim -pql quadratic_function.py QuadraticFunction  # 快速预览
# manim -qh quadratic_function.py QuadraticFunction   # 高质量
# manim -qk quadratic_function.py QuadraticFunction   # 4K质量