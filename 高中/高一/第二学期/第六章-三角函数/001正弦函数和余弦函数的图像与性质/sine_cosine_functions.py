"""
正弦函数和余弦函数的图像与性质 - Sine and Cosine Functions
使用 Manim 创建的高中数学教学视频

内容: 正弦和余弦函数的定义域、值域、周期性、奇偶性、单调性及关系
目标观众: 高一学生
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


class SineCosineFunctions(Scene):
    """
    正弦和余弦函数教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 正弦函数图像绘制 (五点法)
    3. 正弦函数性质标注
    4. 余弦函数图像绘制 (五点法)
    5. 余弦函数性质标注
    6. 正弦余弦关系演示
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_SINE = "#e74c3c"          # 红色 - 正弦
        self.COLOR_COSINE = "#3498db"        # 蓝色 - 余弦
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 辅助
        self.COLOR_GRID = "#2c3e50"          # 网格
        self.COLOR_AXES = WHITE              # 坐标轴
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_sine_graph()
        self.show_sine_properties()
        self.show_cosine_graph()
        self.show_cosine_properties()
        self.show_relationship()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化坐标系和关键点"""
        # 坐标系参数
        self.x_min = 0
        self.x_max = 2 * PI
        self.y_min = -1.5
        self.y_max = 1.5
        
        # 创建坐标轴 (主内容区域)
        self.axes = Axes(
            x_range=[self.x_min, self.x_max + 0.5, PI/2],
            y_range=[self.y_min, self.y_max, 0.5],
            x_length=7,
            y_length=5,
            axis_config={
                "color": self.COLOR_AXES,
                "include_numbers": False,
                "include_tip": True,
            },
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
            }
        ).scale(0.85).move_to(UP * 1.5)
        
        # 自定义 x 轴标签
        self.x_labels = VGroup(
            MathTex("0", font_size=20).next_to(self.axes.c2p(0, 0), DOWN, buff=0.15),
            MathTex(r"\frac{\pi}{2}", font_size=20).next_to(self.axes.c2p(PI/2, 0), DOWN, buff=0.15),
            MathTex(r"\pi", font_size=20).next_to(self.axes.c2p(PI, 0), DOWN, buff=0.15),
            MathTex(r"\frac{3\pi}{2}", font_size=20).next_to(self.axes.c2p(3*PI/2, 0), DOWN, buff=0.15),
            MathTex(r"2\pi", font_size=20).next_to(self.axes.c2p(2*PI, 0), DOWN, buff=0.15),
        )
        
        # y 轴标签
        self.y_labels = VGroup(
            MathTex("-1", font_size=18).next_to(self.axes.c2p(0, -1), LEFT, buff=0.15),
            MathTex("0", font_size=18).next_to(self.axes.c2p(0, 0), LEFT, buff=0.15),
            MathTex("1", font_size=18).next_to(self.axes.c2p(0, 1), LEFT, buff=0.15),
        )
        
        # 正弦函数的五个关键点
        self.sin_key_coords = [
            (0, 0),
            (PI/2, 1),
            (PI, 0),
            (3*PI/2, -1),
            (2*PI, 0)
        ]
        
        # 余弦函数的五个关键点
        self.cos_key_coords = [
            (0, 1),
            (PI/2, 0),
            (PI, -1),
            (3*PI/2, 0),
            (2*PI, 1)
        ]
        
        # 验证设置
        print("✓ 几何设置完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子标题
        hook_title = Text(
            "正弦和余弦有什么区别?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_title), run_time=1.0)
        
        # 快速预览 - 单位圆旋转
        preview_circle = Circle(radius=1, color=WHITE).move_to(UP * 3)
        preview_radius = Line(ORIGIN, RIGHT, color=self.COLOR_SINE).move_to(UP * 3)
        
        preview_group = VGroup(preview_circle, preview_radius)
        
        self.play(Create(preview_circle), run_time=0.5)
        self.play(Create(preview_radius), run_time=0.3)
        self.play(Rotate(preview_radius, angle=2*PI, about_point=preview_circle.get_center()), run_time=1.5, rate_func=linear)
        
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(hook_title),
            FadeOut(preview_group),
            run_time=0.5
        )
    
    def show_sine_graph(self):
        """场景2: 正弦函数图像绘制"""
        # 标题
        title = Text(
            "正弦函数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SINE
        ).move_to(UP * 6.5)
        
        formula = MathTex(
            r"y = \sin x",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.2)
        
        # 创建坐标轴
        self.play(Create(self.axes), run_time=1.2)
        self.play(
            Write(self.x_labels),
            Write(self.y_labels),
            run_time=0.8
        )
        
        self.play(
            Write(title),
            Write(formula),
            run_time=0.8
        )
        
        # 五点法说明
        five_point_text = Text(
            "「五点法」绘图",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(five_point_text, shift=UP * 0.2), run_time=0.5)
        
        # 依次标记五个关键点
        sin_dots = VGroup()
        sin_dot_labels = VGroup()
        
        for i, (x, y) in enumerate(self.sin_key_coords):
            point = self.axes.c2p(x, y)
            dot = Dot(point, color=self.COLOR_SINE, radius=0.08)
            
            # 标签内容
            if i == 0:
                label_text = "(0, 0)"
            elif i == 1:
                label_text = r"(\frac{\pi}{2}, 1)"
            elif i == 2:
                label_text = r"(\pi, 0)"
            elif i == 3:
                label_text = r"(\frac{3\pi}{2}, -1)"
            else:
                label_text = r"(2\pi, 0)"
            
            label = MathTex(label_text, font_size=16, color=self.COLOR_SINE)
            
            # 根据位置调整标签方向
            if y > 0:
                label.next_to(dot, UP, buff=0.1)
            elif y < 0:
                label.next_to(dot, DOWN, buff=0.1)
            else:
                if i == 0:
                    label.next_to(dot, DL, buff=0.1)
                elif i == 2:
                    label.next_to(dot, UP, buff=0.1)
                else:
                    label.next_to(dot, DR, buff=0.1)
            
            sin_dots.add(dot)
            sin_dot_labels.add(label)
            
            self.play(
                FadeIn(dot, scale=0.5),
                Write(label),
                run_time=0.4
            )
        
        self.wait(0.5)
        
        # 连接成曲线
        self.sin_graph = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=self.COLOR_SINE,
            stroke_width=4
        )
        
        self.play(
            FadeOut(five_point_text),
            FadeOut(sin_dot_labels),
            run_time=0.3
        )
        
        self.play(Create(self.sin_graph), run_time=2.0, rate_func=smooth)
        
        # 高亮一个完整周期
        period_brace = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(2*PI, 0)),
            direction=DOWN,
            color=self.COLOR_HIGHLIGHT
        )
        period_label = MathTex(r"T = 2\pi", font_size=22, color=self.COLOR_HIGHLIGHT).next_to(period_brace, DOWN, buff=0.1)
        
        self.play(
            FadeIn(period_brace),
            Write(period_label),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(sin_dots),
            FadeOut(period_brace),
            FadeOut(period_label),
            run_time=0.5
        )
        
        # 保存标题和公式以便后续使用
        self.sine_title = title
        self.sine_formula = formula
    
    def show_sine_properties(self):
        """场景3: 正弦函数性质标注"""
        # 性质列表
        properties = VGroup(
            Text("定义域: R", font="PingFang SC", font_size=22, color=WHITE),
            Text("值域: [-1, 1]", font="PingFang SC", font_size=22, color=WHITE),
            Text("周期: 2π", font="PingFang SC", font_size=22, color=WHITE),
            Text("奇函数 (关于原点对称)", font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 4.5)
        
        # 依次显示性质
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)
        
        # 高亮值域
        range_highlight = Rectangle(
            width=self.axes.x_length,
            height=self.axes.c2p(0, 1)[1] - self.axes.c2p(0, -1)[1],
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            fill_opacity=0.1
        ).move_to(self.axes.c2p(PI, 0))
        
        self.play(Create(range_highlight), run_time=0.8)
        self.play(FadeOut(range_highlight), run_time=0.5)
        
        # 单调性标注
        monotone_text = Text(
            "单调递增: [-π/2, π/2]",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 6.5)
        
        # 高亮单调递增区间 (使用 [0, π/2] 作为可见示例)
        monotone_region = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[0, PI/2],
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        )
        
        self.play(Write(monotone_text), run_time=0.5)
        self.play(Create(monotone_region), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(properties),
            FadeOut(monotone_text),
            FadeOut(monotone_region),
            run_time=0.6
        )
    
    def show_cosine_graph(self):
        """场景4: 余弦函数图像绘制"""
        # 更新标题
        new_title = Text(
            "余弦函数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_COSINE
        ).move_to(UP * 6.5)
        
        new_formula = MathTex(
            r"y = \cos x",
            font_size=32,
            color=WHITE
        ).next_to(new_title, DOWN, buff=0.2)
        
        self.play(
            Transform(self.sine_title, new_title),
            Transform(self.sine_formula, new_formula),
            run_time=0.8
        )
        
        # 正弦曲线变淡
        self.play(self.sin_graph.animate.set_opacity(0.3), run_time=0.5)
        
        # 五点法说明
        five_point_text = Text(
            "「五点法」绘图",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(five_point_text, shift=UP * 0.2), run_time=0.5)
        
        # 依次标记余弦的五个关键点
        cos_dots = VGroup()
        cos_dot_labels = VGroup()
        
        for i, (x, y) in enumerate(self.cos_key_coords):
            point = self.axes.c2p(x, y)
            dot = Dot(point, color=self.COLOR_COSINE, radius=0.08)
            
            # 标签内容
            if i == 0:
                label_text = "(0, 1)"
            elif i == 1:
                label_text = r"(\frac{\pi}{2}, 0)"
            elif i == 2:
                label_text = r"(\pi, -1)"
            elif i == 3:
                label_text = r"(\frac{3\pi}{2}, 0)"
            else:
                label_text = r"(2\pi, 1)"
            
            label = MathTex(label_text, font_size=16, color=self.COLOR_COSINE)
            
            # 根据位置调整标签方向
            if y > 0:
                label.next_to(dot, UP, buff=0.1)
            elif y < 0:
                label.next_to(dot, DOWN, buff=0.1)
            else:
                if i == 1:
                    label.next_to(dot, RIGHT, buff=0.1)
                else:
                    label.next_to(dot, LEFT, buff=0.1)
            
            cos_dots.add(dot)
            cos_dot_labels.add(label)
            
            self.play(
                FadeIn(dot, scale=0.5),
                Write(label),
                run_time=0.4
            )
        
        self.wait(0.5)
        
        # 连接成曲线
        self.cos_graph = self.axes.plot(
            lambda x: np.cos(x),
            x_range=[0, 2*PI],
            color=self.COLOR_COSINE,
            stroke_width=4
        )
        
        self.play(
            FadeOut(five_point_text),
            FadeOut(cos_dot_labels),
            run_time=0.3
        )
        
        self.play(Create(self.cos_graph), run_time=2.0, rate_func=smooth)
        
        # 同时显示两条曲线对比
        self.play(self.sin_graph.animate.set_opacity(1.0), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(cos_dots), run_time=0.3)
    
    def show_cosine_properties(self):
        """场景5: 余弦函数性质标注"""
        # 性质列表
        properties = VGroup(
            Text("定义域: R", font="PingFang SC", font_size=22, color=WHITE),
            Text("值域: [-1, 1]", font="PingFang SC", font_size=22, color=WHITE),
            Text("周期: 2π", font="PingFang SC", font_size=22, color=WHITE),
            Text("偶函数 (关于y轴对称)", font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 4.5)
        
        # 依次显示性质
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)
        
        # 单调性标注
        monotone_text = Text(
            "单调递减: [0, π]",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 6.5)
        
        # 高亮单调递减区间
        monotone_region = self.axes.plot(
            lambda x: np.cos(x),
            x_range=[0, PI],
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        )
        
        self.play(Write(monotone_text), run_time=0.5)
        self.play(Create(monotone_region), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(properties),
            FadeOut(monotone_text),
            FadeOut(monotone_region),
            run_time=0.6
        )
    
    def show_relationship(self):
        """场景6: 正弦余弦关系演示"""
        # 清理之前的内容
        self.play(
            FadeOut(self.sine_title),
            FadeOut(self.sine_formula),
            run_time=0.5
        )
        
        # 新标题
        title = Text(
            "正弦与余弦的关系",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 关系式1: cos x = sin(x + π/2)
        formula_1 = MathTex(
            r"\cos x = \sin(x + \frac{\pi}{2})",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(formula_1), run_time=1.0)
        
        # 创建正弦曲线的副本并平移
        sin_copy = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=self.COLOR_SINE,
            stroke_width=4,
            stroke_opacity=0.5
        )
        
        # 平移动画 (向左平移 π/2)
        shift_amount = self.axes.c2p(PI/2, 0)[0] - self.axes.c2p(0, 0)[0]
        
        self.play(
            self.cos_graph.animate.set_opacity(0.3),
            run_time=0.3
        )
        
        self.play(
            sin_copy.animate.shift(LEFT * shift_amount),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 高亮重合
        self.play(
            Flash(self.axes.c2p(PI, 0), color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理并显示第二个关系
        self.play(
            FadeOut(sin_copy),
            self.cos_graph.animate.set_opacity(1.0),
            run_time=0.5
        )
        
        # 关系式2: sin x = cos(π/2 - x)
        formula_2 = MathTex(
            r"\sin x = \cos(\frac{\pi}{2} - x)",
            font_size=28,
            color=WHITE
        ).next_to(formula_1, DOWN, buff=0.3)
        
        self.play(Write(formula_2), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_1),
            FadeOut(formula_2),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 图像缩小移到上方
        graph_group = VGroup(self.axes, self.x_labels, self.y_labels, self.sin_graph, self.cos_graph)
        
        self.play(
            graph_group.animate.scale(0.5).to_edge(UP, buff=1.5),
            run_time=1.0
        )
        
        # 总结卡片
        summary_title = Text(
            "核心要点",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 2)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 性质对比卡片
        sine_card = VGroup(
            Text("y = sin x", font="PingFang SC", font_size=24, color=self.COLOR_SINE, weight=BOLD),
            Text("奇函数", font="PingFang SC", font_size=18, color=WHITE),
            Text("关于原点对称", font="PingFang SC", font_size=16, color=GRAY_A),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        cosine_card = VGroup(
            Text("y = cos x", font="PingFang SC", font_size=24, color=self.COLOR_COSINE, weight=BOLD),
            Text("偶函数", font="PingFang SC", font_size=18, color=WHITE),
            Text("关于y轴对称", font="PingFang SC", font_size=16, color=GRAY_A),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        cards = VGroup(sine_card, cosine_card).arrange(RIGHT, buff=1.5).move_to(UP * 0.5)
        
        for card in cards:
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
        
        # 共同性质
        common = Text(
            "定义域R, 值域[-1,1], 周期2π",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(common), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理图表
        self.play(
            FadeOut(graph_group),
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(common),
            run_time=0.8
        )
        
        # 片尾 - 关注提示
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
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
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 波浪线装饰
        wave_1 = self.axes.plot(
            lambda x: 0.5 * np.sin(x),
            x_range=[0, 4*PI],
            color=self.COLOR_SINE,
            stroke_width=3
        ).scale(0.3).move_to(DOWN * 2.5)
        
        wave_2 = self.axes.plot(
            lambda x: 0.5 * np.cos(x),
            x_range=[0, 4*PI],
            color=self.COLOR_COSINE,
            stroke_width=3
        ).scale(0.3).move_to(DOWN * 3)
        
        self.play(
            Create(wave_1),
            Create(wave_2),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(wave_1),
            FadeOut(wave_2),
            run_time=1.0
        )


# 运行命令:
# manim -pql sine_cosine_functions.py SineCosineFunctions  # 快速预览
# manim -qh sine_cosine_functions.py SineCosineFunctions   # 高质量 1080p
# manim -qk sine_cosine_functions.py SineCosineFunctions   # 4K质量