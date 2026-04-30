"""
事件的分类 - 概率初步教学动画
使用 Manim 创建的八年级概率入门教学视频

内容: 必然事件、不可能事件、随机事件的定义和概率
目标观众: 八年级学生
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


class EventClassification(Scene):
    """
    事件分类教学动画场景
    
    场景顺序:
    1. 开场钩子 - 抛硬币
    2. 引出三类事件
    3. 必然事件详解
    4. 不可能事件详解
    5. 随机事件详解
    6. 概率数轴
    7. 三类事件对比
    8. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CERTAIN = "#2ecc71"      # 绿色 - 必然事件
        self.COLOR_IMPOSSIBLE = "#e74c3c"   # 红色 - 不可能事件
        self.COLOR_RANDOM = "#3498db"       # 蓝色 - 随机事件
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_classification_overview()
        self.show_certain_event()
        self.show_impossible_event()
        self.show_random_event()
        self.show_probability_line()
        self.show_comparison()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 抛硬币"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 硬币图标（用圆形模拟）
        coin = Circle(
            radius=0.8,
            color=GOLD,
            fill_opacity=0.8,
            stroke_width=4
        ).move_to(UP * 3.5)
        
        # 硬币上的标记
        coin_mark = Text(
            "¥1",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(coin.get_center())
        
        coin_group = VGroup(coin, coin_mark)
        
        self.play(FadeIn(coin_group, scale=0.8), run_time=0.5)
        
        # 硬币旋转
        self.play(
            Rotate(coin_group, angle=2*PI, run_time=1.5, rate_func=linear),
            run_time=1.5
        )
        
        # 钩子问题
        hook = Text(
            "抛硬币，一定正面朝上吗？",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(Write(hook), run_time=1.2)
        self.wait(1.2)
        
        # 答案提示
        answer = Text(
            "不一定！这就是随机事件",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_RANDOM
        ).move_to(ORIGIN)
        
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(coin_group),
            FadeOut(hook),
            FadeOut(answer),
            run_time=0.6
        )
    
    def show_classification_overview(self):
        """场景2: 引出三类事件"""
        # 标题
        title = Text(
            "事件的分类",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 三个分类框
        box1 = Rectangle(
            width=3.5,
            height=1.2,
            color=self.COLOR_CERTAIN,
            stroke_width=3,
            fill_opacity=0.1
        )
        
        box2 = Rectangle(
            width=3.5,
            height=1.2,
            color=self.COLOR_IMPOSSIBLE,
            stroke_width=3,
            fill_opacity=0.1
        )
        
        box3 = Rectangle(
            width=3.5,
            height=1.2,
            color=self.COLOR_RANDOM,
            stroke_width=3,
            fill_opacity=0.1
        )
        
        # 文字
        text1 = Text(
            "必然事件",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_CERTAIN
        )
        
        text2 = Text(
            "不可能事件",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_IMPOSSIBLE
        )
        
        text3 = Text(
            "随机事件",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_RANDOM
        )
        
        # 组合
        event1 = VGroup(box1, text1).move_to(UP * 2.5)
        event2 = VGroup(box2, text2).move_to(UP * 0.8)
        event3 = VGroup(box3, text3).move_to(DOWN * 0.9)
        
        # 依次显示
        self.play(FadeIn(event1, shift=RIGHT * 0.5), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(event2, shift=RIGHT * 0.5), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(event3, shift=RIGHT * 0.5), run_time=0.8)
        self.wait(0.5)
        
        # 连接箭头
        arrow1 = Arrow(
            title.get_bottom() + DOWN * 0.2,
            event1.get_top() + UP * 0.2,
            color=self.COLOR_AUXILIARY,
            buff=0,
            stroke_width=3
        )
        
        arrow2 = Arrow(
            title.get_bottom() + DOWN * 0.2,
            event2.get_top() + UP * 0.2,
            color=self.COLOR_AUXILIARY,
            buff=0,
            stroke_width=3
        )
        
        arrow3 = Arrow(
            title.get_bottom() + DOWN * 0.2,
            event3.get_top() + UP * 0.2,
            color=self.COLOR_AUXILIARY,
            buff=0,
            stroke_width=3
        )
        
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 保存用于后续高亮
        self.event_boxes = VGroup(event1, event2, event3)
        self.arrows = VGroup(arrow1, arrow2, arrow3)
        
        # 移到侧边
        all_elements = VGroup(title, self.event_boxes, self.arrows)
        self.play(
            all_elements.animate.scale(0.5).move_to(RIGHT * 3 + UP * 3.5),
            run_time=0.8
        )
        
        self.overview_title = title
    
    def show_certain_event(self):
        """场景3: 必然事件详解"""
        # 高亮必然事件框
        self.play(
            Indicate(self.event_boxes[0], scale_factor=1.3, color=self.COLOR_CERTAIN),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "必然事件 (Certain Event)",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_CERTAIN
        ).move_to(UP * 5 + LEFT * 0.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 定义
        definition = Text(
            "一定会发生的事件",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(0.5)
        
        # 例子1：太阳
        example1_title = Text(
            "例子1:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 2.5)
        
        # 太阳图标
        sun = Circle(radius=0.4, color=YELLOW, fill_opacity=0.8).move_to(UP * 2 + LEFT * 0.8)
        sun_rays = VGroup(*[
            Line(ORIGIN, 0.6 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]), color=YELLOW)
            for i in range(8)
        ]).move_to(sun.get_center())
        
        sun_group = VGroup(sun, sun_rays)
        
        example1_text = Text(
            "太阳从东方升起",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(sun_group, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(example1_title),
            FadeIn(sun_group, scale=0.8),
            FadeIn(example1_text),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 例子2：水
        example2_title = Text(
            "例子2:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3 + LEFT * 2.5)
        
        # 水滴图标
        water = Polygon(
            [0, 0.5, 0],
            [-0.3, 0, 0],
            [0, -0.5, 0],
            [0.3, 0, 0],
            color=BLUE,
            fill_opacity=0.6
        ).move_to(UP * 0.3 + LEFT * 0.8)
        
        # 向下箭头
        arrow_down = Arrow(
            water.get_bottom() + DOWN * 0.1,
            water.get_bottom() + DOWN * 0.5,
            color=BLUE,
            buff=0,
            stroke_width=4
        )
        
        example2_text = Text(
            "水往低处流",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(water, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(example2_title),
            FadeIn(water),
            GrowArrow(arrow_down),
            FadeIn(example2_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 概率公式 - Split to avoid LaTeX Chinese character error
        prob_label = Text(
            "概率:",
            font=self.FONT_CHINESE,
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2 + LEFT * 2)
        
        prob_value = MathTex(
            r"P = 1",
            font_size=36,
            color=self.COLOR_CERTAIN
        ).next_to(prob_label, RIGHT, buff=0.3)
        
        prob_group = VGroup(prob_label, prob_value).move_to(DOWN * 2)
        
        self.play(Write(prob_group), run_time=1.0)
        
        # 框住公式
        prob_box = SurroundingRectangle(
            prob_group,
            color=self.COLOR_CERTAIN,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(prob_box), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example1_title),
            FadeOut(sun_group),
            FadeOut(example1_text),
            FadeOut(example2_title),
            FadeOut(water),
            FadeOut(arrow_down),
            FadeOut(example2_text),
            FadeOut(prob_group),
            FadeOut(prob_box),
            run_time=0.6
        )
    
    def show_impossible_event(self):
        """场景4: 不可能事件详解"""
        # 高亮不可能事件框
        self.play(
            Indicate(self.event_boxes[1], scale_factor=1.3, color=self.COLOR_IMPOSSIBLE),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "不可能事件 (Impossible Event)",
            font=self.FONT_CHINESE,
            font_size=30,
            color=self.COLOR_IMPOSSIBLE
        ).move_to(UP * 5 + LEFT * 0.3)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 定义
        definition = Text(
            "一定不会发生的事件",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(0.5)
        
        # 例子1：水往高处流
        example1_title = Text(
            "例子1:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 2.5)
        
        # 水滴和向上箭头（禁止符号）
        water = Polygon(
            [0, 0.5, 0],
            [-0.3, 0, 0],
            [0, -0.5, 0],
            [0.3, 0, 0],
            color=BLUE,
            fill_opacity=0.6
        ).move_to(UP * 2 + LEFT * 0.8)
        
        arrow_up = Arrow(
            water.get_top() + UP * 0.1,
            water.get_top() + UP * 0.5,
            color=RED,
            buff=0,
            stroke_width=4
        )
        
        # 禁止符号
        cross = VGroup(
            Line(UL * 0.4, DR * 0.4, color=RED, stroke_width=4),
            Line(UR * 0.4, DL * 0.4, color=RED, stroke_width=4)
        ).move_to(water.get_center())
        
        example1_text = Text(
            "水往高处流",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(water, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(example1_title),
            FadeIn(water),
            GrowArrow(arrow_up),
            Create(cross),
            FadeIn(example1_text),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 例子2：石头浮水面
        example2_title = Text(
            "例子2:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3 + LEFT * 2.5)
        
        # 石头图标
        stone = Circle(
            radius=0.3,
            color=GRAY,
            fill_opacity=0.8
        ).move_to(UP * 0.3 + LEFT * 0.8)
        
        # 水面线
        water_surface = Line(
            LEFT * 1.5,
            RIGHT * 0.5,
            color=BLUE,
            stroke_width=3
        ).move_to(UP * 0.3 + LEFT * 0.3)
        
        # 禁止符号
        cross2 = VGroup(
            Line(UL * 0.35, DR * 0.35, color=RED, stroke_width=4),
            Line(UR * 0.35, DL * 0.35, color=RED, stroke_width=4)
        ).move_to(stone.get_center())
        
        example2_text = Text(
            "石头浮在水面上",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(stone, RIGHT, buff=0.8)
        
        self.play(
            FadeIn(example2_title),
            FadeIn(stone),
            Create(water_surface),
            Create(cross2),
            FadeIn(example2_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 概率公式
        prob_label = Text(
            "概率:",
            font=self.FONT_CHINESE,
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2 + LEFT * 2)
        
        prob_value = MathTex(
            r"P = 0",
            font_size=36,
            color=self.COLOR_IMPOSSIBLE
        ).next_to(prob_label, RIGHT, buff=0.3)
        
        prob_group = VGroup(prob_label, prob_value).move_to(DOWN * 2)
        
        self.play(Write(prob_group), run_time=1.0)
        
        # 框住公式
        prob_box = SurroundingRectangle(
            prob_group,
            color=self.COLOR_IMPOSSIBLE,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(prob_box), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example1_title),
            FadeOut(water),
            FadeOut(arrow_up),
            FadeOut(cross),
            FadeOut(example1_text),
            FadeOut(example2_title),
            FadeOut(stone),
            FadeOut(water_surface),
            FadeOut(cross2),
            FadeOut(example2_text),
            FadeOut(prob_group),
            FadeOut(prob_box),
            run_time=0.6
        )
    
    def show_random_event(self):
        """场景5: 随机事件详解"""
        # 高亮随机事件框
        self.play(
            Indicate(self.event_boxes[2], scale_factor=1.3, color=self.COLOR_RANDOM),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "随机事件 (Random Event)",
            font=self.FONT_CHINESE,
            font_size=30,
            color=self.COLOR_RANDOM
        ).move_to(UP * 5 + LEFT * 0.3)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 定义
        definition = Text(
            "可能发生也可能不发生的事件",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(0.5)
        
        # 例子1：抛硬币
        example1_title = Text(
            "例子1:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 2.5)
        
        # 硬币
        coin = Circle(
            radius=0.4,
            color=GOLD,
            fill_opacity=0.8,
            stroke_width=3
        ).move_to(UP * 2 + LEFT * 0.8)
        
        coin_text = Text(
            "¥",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(coin.get_center())
        
        coin_group = VGroup(coin, coin_text)
        
        # 问号
        question = Text(
            "?",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_RANDOM
        ).next_to(coin, UP, buff=0.2)
        
        example1_text = Text(
            "抛硬币正面朝上",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(coin_group, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(example1_title),
            FadeIn(coin_group, scale=0.8),
            FadeIn(question),
            FadeIn(example1_text),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 例子2：天气
        example2_title = Text(
            "例子2:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3 + LEFT * 2.5)
        
        # 云朵图标
        cloud = VGroup(
            Circle(radius=0.25, fill_opacity=0.6, color=BLUE_D).move_to(LEFT * 0.2),
            Circle(radius=0.3, fill_opacity=0.6, color=BLUE_D).move_to(ORIGIN),
            Circle(radius=0.25, fill_opacity=0.6, color=BLUE_D).move_to(RIGHT * 0.2)
        ).move_to(UP * 0.3 + LEFT * 0.8)
        
        # 雨滴
        rain = VGroup(*[
            Line(
                ORIGIN,
                DOWN * 0.3,
                color=BLUE,
                stroke_width=2
            ).move_to(cloud.get_bottom() + DOWN * 0.3 + RIGHT * (i * 0.3 - 0.3))
            for i in range(3)
        ])
        
        question2 = Text(
            "?",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_RANDOM
        ).next_to(cloud, UP, buff=0.1)
        
        example2_text = Text(
            "明天会下雨",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).next_to(cloud, RIGHT, buff=0.8)
        
        self.play(
            FadeIn(example2_title),
            FadeIn(cloud),
            FadeIn(rain),
            FadeIn(question2),
            FadeIn(example2_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 概率公式
        prob_label = Text(
            "概率:",
            font=self.FONT_CHINESE,
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2 + LEFT * 2.2)
        
        prob_value = MathTex(
            r"0 < P < 1",
            font_size=36,
            color=self.COLOR_RANDOM
        ).next_to(prob_label, RIGHT, buff=0.3)
        
        prob_group = VGroup(prob_label, prob_value).move_to(DOWN * 2)
        
        self.play(Write(prob_group), run_time=1.0)
        
        # 框住公式
        prob_box = SurroundingRectangle(
            prob_group,
            color=self.COLOR_RANDOM,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(prob_box), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example1_title),
            FadeOut(coin_group),
            FadeOut(question),
            FadeOut(example1_text),
            FadeOut(example2_title),
            FadeOut(cloud),
            FadeOut(rain),
            FadeOut(question2),
            FadeOut(example2_text),
            FadeOut(prob_group),
            FadeOut(prob_box),
            run_time=0.6
        )
    
    def show_probability_line(self):
        """场景6: 概率数轴"""
        # 清除侧边概览
        self.play(
            FadeOut(self.overview_title),
            FadeOut(self.event_boxes),
            FadeOut(self.arrows),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "概率数轴",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建数轴
        number_line = NumberLine(
            x_range=[0, 1, 0.25],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24,
            include_ticks=True,
            tick_size=0.1
        ).move_to(UP * 1.5)
        
        self.play(Create(number_line), run_time=1.5)
        self.wait(0.5)
        
        # 标记 P=0 (不可能事件)
        dot_0 = Dot(
            number_line.n2p(0),
            radius=0.12,
            color=self.COLOR_IMPOSSIBLE
        )
        
        label_0 = Text(
            "不可能",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_IMPOSSIBLE
        ).next_to(dot_0, UP, buff=0.3)
        
        self.play(
            FadeIn(dot_0, scale=0.5),
            FadeIn(label_0),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 标记 P=1 (必然事件)
        dot_1 = Dot(
            number_line.n2p(1),
            radius=0.12,
            color=self.COLOR_CERTAIN
        )
        
        label_1 = Text(
            "必然",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_CERTAIN
        ).next_to(dot_1, UP, buff=0.3)
        
        self.play(
            FadeIn(dot_1, scale=0.5),
            FadeIn(label_1),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 标记中间区域 (随机事件)
        random_line = Line(
            number_line.n2p(0.1),
            number_line.n2p(0.9),
            color=self.COLOR_RANDOM,
            stroke_width=8
        )
        
        self.play(Create(random_line), run_time=1.0)
        
        # 添加 Brace
        brace = Brace(random_line, direction=DOWN, buff=0.3, color=self.COLOR_RANDOM)
        brace_label = Text(
            "随机事件",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_RANDOM
        ).next_to(brace, DOWN, buff=0.1)
        
        self.play(
            GrowFromCenter(brace),
            FadeIn(brace_label),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 说明文字
        explanation = Text(
            "概率越大，事件越可能发生",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(number_line),
            FadeOut(dot_0),
            FadeOut(label_0),
            FadeOut(dot_1),
            FadeOut(label_1),
            FadeOut(random_line),
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(explanation),
            run_time=0.8
        )
    
    def show_comparison(self):
        """场景7: 三类事件对比"""
        # 标题
        title = Text(
            "三类事件对比",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建对比表
        # 列标题
        col1 = Text("必然事件", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_CERTAIN).move_to(UP * 3.5 + LEFT * 2.5)
        col2 = Text("不可能事件", font=self.FONT_CHINESE, font_size=22, color=self.COLOR_IMPOSSIBLE).move_to(UP * 3.5)
        col3 = Text("随机事件", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_RANDOM).move_to(UP * 3.5 + RIGHT * 2.5)
        
        self.play(
            FadeIn(col1),
            FadeIn(col2),
            FadeIn(col3),
            run_time=0.8
        )
        
        # 分隔线
        line1 = Line(UP * 3, DOWN * 3, color=GRAY).move_to(LEFT * 1.25)
        line2 = Line(UP * 3, DOWN * 3, color=GRAY).move_to(RIGHT * 1.25)
        
        self.play(Create(line1), Create(line2), run_time=0.5)
        
        # 第一行：定义
        row1_title = Text("定义", font=self.FONT_CHINESE, font_size=20, color=GRAY_A).move_to(UP * 2.3 + LEFT * 3.8)
        
        def1 = Text("一定\n发生", font=self.FONT_CHINESE, font_size=18, color=WHITE).move_to(UP * 2 + LEFT * 2.5)
        def2 = Text("一定不\n发生", font=self.FONT_CHINESE, font_size=18, color=WHITE).move_to(UP * 2)
        def3 = Text("可能发生\n可能不发生", font=self.FONT_CHINESE, font_size=16, color=WHITE).move_to(UP * 2 + RIGHT * 2.5)
        
        self.play(
            FadeIn(row1_title),
            FadeIn(def1),
            FadeIn(def2),
            FadeIn(def3),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 第二行：概率
        row2_title = Text("概率", font=self.FONT_CHINESE, font_size=20, color=GRAY_A).move_to(UP * 0.5 + LEFT * 3.8)
        
        prob1 = MathTex("P = 1", font_size=28, color=self.COLOR_CERTAIN).move_to(UP * 0.5 + LEFT * 2.5)
        prob2 = MathTex("P = 0", font_size=28, color=self.COLOR_IMPOSSIBLE).move_to(UP * 0.5)
        prob3 = MathTex("0 < P < 1", font_size=24, color=self.COLOR_RANDOM).move_to(UP * 0.5 + RIGHT * 2.5)
        
        self.play(
            FadeIn(row2_title),
            Write(prob1),
            Write(prob2),
            Write(prob3),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 第三行：例子
        row3_title = Text("例子", font=self.FONT_CHINESE, font_size=20, color=GRAY_A).move_to(DOWN * 1.3 + LEFT * 3.8)
        
        ex1 = Text("太阳\n东升", font=self.FONT_CHINESE, font_size=18, color=WHITE).move_to(DOWN * 1.5 + LEFT * 2.5)
        ex2 = Text("水往\n高处流", font=self.FONT_CHINESE, font_size=18, color=WHITE).move_to(DOWN * 1.5)
        ex3 = Text("抛硬币\n正面朝上", font=self.FONT_CHINESE, font_size=16, color=WHITE).move_to(DOWN * 1.5 + RIGHT * 2.5)
        
        self.play(
            FadeIn(row3_title),
            FadeIn(ex1),
            FadeIn(ex2),
            FadeIn(ex3),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(col1), FadeOut(col2), FadeOut(col3),
            FadeOut(line1), FadeOut(line2),
            FadeOut(row1_title), FadeOut(def1), FadeOut(def2), FadeOut(def3),
            FadeOut(row2_title), FadeOut(prob1), FadeOut(prob2), FadeOut(prob3),
            FadeOut(row3_title), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景8: 片尾总结"""
        # 核心要点
        key_point = VGroup(
            Text(
                "记住概率范围:",
                font=self.FONT_CHINESE,
                font_size=32,
                color=WHITE
            ),
            MathTex(
                r"0 \leq P \leq 1",
                font_size=40,
                color=self.COLOR_HIGHLIGHT
            ).shift(DOWN * 0.8)
        ).move_to(UP * 3)
        
        self.play(FadeIn(key_point, scale=1.1), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(FadeOut(key_point), run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=44,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多概率知识！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 装饰 - 硬币旋转
        coins = VGroup(*[
            VGroup(
                Circle(radius=0.25, color=GOLD, fill_opacity=0.8),
                Text("¥", font=self.FONT_CHINESE, font_size=18, color=WHITE)
            ).move_to(2.5 * np.array([np.cos(i * PI / 2.5), np.sin(i * PI / 2.5), 0]) + DOWN * 3)
            for i in range(5)
        ])
        
        self.play(
            *[FadeIn(coin, scale=0.5) for coin in coins],
            run_time=0.6
        )
        
        self.play(
            Rotate(coins, angle=2*PI, run_time=2, rate_func=linear),
            run_time=2
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(coins),
            run_time=1.0
        )


# 运行命令:
# manim -pql event_classification.py EventClassification  # 快速预览
# manim -qh event_classification.py EventClassification   # 高质量渲染