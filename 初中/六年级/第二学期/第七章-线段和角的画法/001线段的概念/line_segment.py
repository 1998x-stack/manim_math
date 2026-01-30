"""
线段的概念 - Line Segment Concepts Animation
使用 Manim 创建的六年级数学教学视频

内容: 线段的定义、性质、中点、度量和运算
目标观众: 六年级学生
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


class LineSegmentConcept(Scene):
    """
    线段概念教学动画场景
    
    场景顺序:
    1. 开场钩子 - 最短路径问题
    2. 线段定义 - 基本概念介绍
    3. 线段性质 - 两点间线段最短
    4. 线段中点 - 中点定义和性质
    5. 线段度量 - 如何测量线段
    6. 线段运算 - 线段的和与差
    7. 总结片尾 - 要点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主线段
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 辅助线段
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
        self.COLOR_POINT = "#2ecc71"        # 绿色 - 端点
        self.COLOR_MIDPOINT = "#f39c12"     # 橙色 - 中点
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 20
        self.FONT_SMALL = 18
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_shortest_property()
        self.scene_4_midpoint()
        self.scene_5_measurement()
        self.scene_6_operations()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标"""
        # 主线段AB (水平，便于理解)
        self.A = np.array([-3.0, 0, 0]) + UP * 2
        self.B = np.array([3.0, 0, 0]) + UP * 2
        self.AB_length = np.linalg.norm(self.B - self.A)  # 6.0
        
        # 中点M
        self.M = (self.A + self.B) / 2
        
        # 线段CD (较短，用于运算演示)
        self.C = np.array([-2.0, -2.0, 0]) + UP * 0.5
        self.D = np.array([2.0, -2.0, 0]) + UP * 0.5
        self.CD_length = np.linalg.norm(self.D - self.C)  # 4.0
        
        # 验证计算
        print(f"✓ AB长度: {self.AB_length:.2f}")
        print(f"✓ CD长度: {self.CD_length:.2f}")
        print(f"✓ 中点M: {self.M}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 - 最短路径问题"""
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
            "从A点到B点\n最短的路径是什么?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 点A和点B
        dot_A = Dot(self.A, color=self.COLOR_POINT, radius=0.12)
        dot_B = Dot(self.B, color=self.COLOR_POINT, radius=0.12)
        label_A_temp = Text("A", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                           color=WHITE).next_to(dot_A, LEFT, buff=0.15)
        label_B_temp = Text("B", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                           color=WHITE).next_to(dot_B, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(dot_B, scale=0.5),
            FadeIn(label_A_temp),
            FadeIn(label_B_temp),
            run_time=0.4
        )
        
        # 路径1: 曲线
        curved_path = CubicBezier(
            self.A,
            self.A + UP * 1.5 + RIGHT * 0.5,
            self.B + UP * 1.5 + LEFT * 0.5,
            self.B,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        curve_label = Text("?", font="Noto Sans CJK SC", font_size=24, 
                          color=self.COLOR_AUXILIARY).next_to(curved_path, UP, buff=0.1)
        
        self.play(Create(curved_path), FadeIn(curve_label), run_time=0.6)
        
        # 路径2: 折线
        zigzag_points = [
            self.A,
            self.A + RIGHT * 1.5 + UP * 0.8,
            self.A + RIGHT * 3.0 + DOWN * 0.5,
            self.A + RIGHT * 4.5 + UP * 0.8,
            self.B
        ]
        zigzag_path = VMobject(color=self.COLOR_AUXILIARY, stroke_width=3)
        zigzag_path.set_points_as_corners(zigzag_points)
        
        zigzag_label = Text("?", font="Noto Sans CJK SC", font_size=24, 
                           color=self.COLOR_AUXILIARY).next_to(zigzag_path, DOWN, buff=0.3)
        
        self.play(
            curved_path.animate.set_color(GRAY),
            curve_label.animate.set_opacity(0.3),
            Create(zigzag_path),
            FadeIn(zigzag_label),
            run_time=0.6
        )
        
        # 路径3: 直线段
        straight_path = Line(self.A, self.B, color=self.COLOR_PRIMARY, stroke_width=4)
        
        self.play(
            zigzag_path.animate.set_color(GRAY),
            zigzag_label.animate.set_opacity(0.3),
            Create(straight_path),
            run_time=0.6
        )
        
        # 直线段高亮
        self.play(
            Flash(straight_path, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            straight_path.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.4
        )
        
        check_mark = Text("✓", font_size=48, color=GREEN).next_to(straight_path, DOWN, buff=0.5)
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.3)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(curved_path),
            FadeOut(zigzag_path),
            FadeOut(curve_label),
            FadeOut(zigzag_label),
            FadeOut(check_mark),
            straight_path.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.5
        )
        
        # 保留元素
        self.dot_A = dot_A
        self.dot_B = dot_B
        self.label_A_temp = label_A_temp
        self.label_B_temp = label_B_temp
        self.segment_AB = straight_path
    
    def scene_2_definition(self):
        """场景2: 线段定义"""
        # 标题
        title = Text(
            "什么是线段?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 定义
        definition = VGroup(
            Text("线段是直线上", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            Text("两点之间的部分", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 4.5)
        
        self.play(Write(definition), run_time=1.2)
        
        # 端点高亮
        self.play(
            Indicate(self.dot_A, scale_factor=1.5, color=self.COLOR_POINT),
            Indicate(self.dot_B, scale_factor=1.5, color=self.COLOR_POINT),
            run_time=0.6
        )
        
        # 重新创建更好的标签
        self.play(
            FadeOut(self.label_A_temp),
            FadeOut(self.label_B_temp),
            run_time=0.3
        )
        
        label_A = Text("A", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                      color=WHITE).next_to(self.dot_A, LEFT, buff=0.15)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                      color=WHITE).next_to(self.dot_B, RIGHT, buff=0.15)
        
        self.play(FadeIn(label_A), FadeIn(label_B), run_time=0.4)
        
        # 强调"包括两个端点"
        emphasis = Text(
            "包括两个端点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POINT
        ).move_to(UP * 3.5)
        
        self.play(
            FadeIn(emphasis, shift=DOWN * 0.2),
            self.dot_A.animate.set_color(self.COLOR_POINT),
            self.dot_B.animate.set_color(self.COLOR_POINT),
            run_time=0.5
        )
        
        self.wait(0.8)
        
        # 长度标注
        brace = Brace(self.segment_AB, direction=DOWN, buff=0.15, color=YELLOW)
        length_text = Text("6", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                          color=YELLOW).next_to(brace, DOWN, buff=0.1)
        
        self.play(
            FadeOut(emphasis),
            Create(brace),
            Write(length_text),
            run_time=0.8
        )
        
        # 记号说明
        notation = MathTex(
            r"\text{记作: } AB \text{ 或 } |AB|",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        # 修正：避免中文在MathTex中
        notation = VGroup(
            Text("记作: ", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=GRAY_A),
            MathTex("AB", font_size=self.FONT_BODY, color=WHITE),
            Text(" 或 ", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=GRAY_A),
            MathTex("|AB|", font_size=self.FONT_BODY, color=WHITE)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4)
        
        self.play(FadeIn(notation, shift=UP * 0.2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(notation),
            FadeOut(brace),
            FadeOut(length_text),
            run_time=0.6
        )
        
        # 保留标签
        self.label_A = label_A
        self.label_B = label_B
    
    def scene_3_shortest_property(self):
        """场景3: 两点间线段最短"""
        # 标题
        title = Text(
            "两点之间，线段最短",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 重新绘制对比路径
        # 曲线
        curved_path = CubicBezier(
            self.A,
            self.A + UP * 1.5 + RIGHT * 0.5,
            self.B + UP * 1.5 + LEFT * 0.5,
            self.B,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        length_curved = Text(
            "约8.5",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).next_to(curved_path, UP, buff=0.05)
        
        self.play(Create(curved_path), run_time=0.7)
        self.play(FadeIn(length_curved), run_time=0.4)
        
        # 折线
        zigzag_points = [
            self.A,
            self.A + RIGHT * 1.5 + UP * 0.8,
            self.A + RIGHT * 3.0 + DOWN * 0.5,
            self.A + RIGHT * 4.5 + UP * 0.8,
            self.B
        ]
        zigzag_path = VMobject(color=self.COLOR_AUXILIARY, stroke_width=2)
        zigzag_path.set_points_as_corners(zigzag_points)
        
        length_zigzag = Text(
            "约7.2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).next_to(zigzag_path, DOWN, buff=0.3)
        
        self.play(Create(zigzag_path), run_time=0.7)
        self.play(FadeIn(length_zigzag), run_time=0.4)
        
        # 强调直线段
        length_straight = Text(
            "6.0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(DOWN * 3.8)
        
        self.play(
            Indicate(self.segment_AB, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            Write(length_straight),
            run_time=0.8
        )
        
        # 对比闪烁
        self.play(
            Flash(curved_path, color=GRAY),
            Flash(zigzag_path, color=GRAY),
            Flash(self.segment_AB, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        # 结论
        conclusion = Text(
            "线段是最短距离!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(curved_path),
            FadeOut(zigzag_path),
            FadeOut(length_curved),
            FadeOut(length_zigzag),
            FadeOut(length_straight),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_4_midpoint(self):
        """场景4: 线段的中点"""
        # 标题
        title = Text(
            "线段的中点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_MIDPOINT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 定义
        definition = Text(
            "将线段分成两条相等线段的点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4.7)
        
        self.play(Write(definition), run_time=1.0)
        
        # 中点出现
        dot_M = Dot(self.M, color=self.COLOR_MIDPOINT, radius=0.12)
        
        self.play(FadeIn(dot_M, scale=0.5), run_time=0.5)
        self.play(Flash(dot_M, color=self.COLOR_MIDPOINT, flash_radius=0.3), run_time=0.4)
        
        label_M = Text("M", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                      color=self.COLOR_MIDPOINT).next_to(dot_M, UP, buff=0.15)
        
        self.play(FadeIn(label_M), run_time=0.4)
        
        # 分段显示
        segment_AM = Line(self.A, self.M, color=self.COLOR_PRIMARY, stroke_width=4)
        segment_MB = Line(self.M, self.B, color=self.COLOR_SECONDARY, stroke_width=4)
        
        self.play(
            FadeOut(self.segment_AB),
            Create(segment_AM),
            Create(segment_MB),
            run_time=0.7
        )
        
        # 标注长度
        brace_AM = Brace(segment_AM, direction=DOWN, buff=0.15, color=self.COLOR_PRIMARY)
        length_AM = Text("3", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                        color=self.COLOR_PRIMARY).next_to(brace_AM, DOWN, buff=0.1)
        
        self.play(Create(brace_AM), Write(length_AM), run_time=0.7)
        
        brace_MB = Brace(segment_MB, direction=DOWN, buff=0.15, color=self.COLOR_SECONDARY)
        length_MB = Text("3", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                        color=self.COLOR_SECONDARY).next_to(brace_MB, DOWN, buff=0.1)
        
        self.play(Create(brace_MB), Write(length_MB), run_time=0.7)
        
        # 强调相等
        self.play(
            Indicate(length_AM, scale_factor=1.3),
            Indicate(length_MB, scale_factor=1.3),
            run_time=0.8
        )
        
        # 公式
        formula = VGroup(
            MathTex("AM = MB = ", font_size=self.FONT_SUBTITLE),
            MathTex(r"\frac{AB}{2}", font_size=self.FONT_SUBTITLE)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=1.2)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(formula),
            FadeOut(brace_AM),
            FadeOut(brace_MB),
            FadeOut(length_AM),
            FadeOut(length_MB),
            run_time=0.6
        )
        
        # 恢复单条线段
        self.segment_AB = Line(self.A, self.B, color=self.COLOR_PRIMARY, stroke_width=4)
        self.play(
            FadeOut(segment_AM),
            FadeOut(segment_MB),
            Create(self.segment_AB),
            run_time=0.4
        )
        
        # 保留中点
        self.dot_M = dot_M
        self.label_M = label_M
    
    def scene_5_measurement(self):
        """场景5: 线段的度量"""
        # 标题
        title = Text(
            "线段可以度量",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建刻度尺
        ruler = NumberLine(
            x_range=[0, 10, 1],
            length=8,
            include_numbers=True,
            numbers_to_include=list(range(11)),
            font_size=18,
            color=GRAY_A,
            include_ticks=True,
            tick_size=0.1
        ).move_to(DOWN * 4)
        
        # 尺子标签
        ruler_label = Text("厘米", font="Noto Sans CJK SC", font_size=16, 
                          color=GRAY_A).next_to(ruler, RIGHT, buff=0.2)
        
        self.play(
            ruler.animate.shift(UP * 6),  # 从下方滑入
            FadeIn(ruler_label.shift(UP * 6)),
            run_time=0.7
        )
        
        # 移动线段到尺子上
        ruler_center = ruler.get_center()
        target_y = ruler_center[1] + 0.6
        
        target_A = np.array([ruler.n2p(0)[0], target_y, 0])
        target_B = np.array([ruler.n2p(6)[0], target_y, 0])
        
        self.play(
            self.segment_AB.animate.put_start_and_end_on(target_A, target_B),
            self.dot_A.animate.move_to(target_A),
            self.dot_B.animate.move_to(target_B),
            self.dot_M.animate.move_to((target_A + target_B) / 2),
            self.label_A.animate.next_to(target_A, UP, buff=0.15),
            self.label_B.animate.next_to(target_B, UP, buff=0.15),
            self.label_M.animate.next_to((target_A + target_B) / 2, UP, buff=0.15),
            run_time=0.8
        )
        
        # 对齐刻度0
        indicator_0 = Line(
            ruler.n2p(0) + DOWN * 0.15,
            ruler.n2p(0) + UP * 0.15,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(
            Indicate(self.dot_A, scale_factor=1.5),
            Create(indicator_0),
            run_time=0.7
        )
        
        # 对齐刻度6
        indicator_6 = Line(
            ruler.n2p(6) + DOWN * 0.15,
            ruler.n2p(6) + UP * 0.15,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(
            Indicate(self.dot_B, scale_factor=1.5),
            Create(indicator_6),
            run_time=0.7
        )
        
        # 动态数字计数器
        tracker = ValueTracker(0)
        counter = DecimalNumber(
            0,
            num_decimal_places=1,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        counter.add_updater(lambda m: m.set_value(tracker.get_value()))
        
        self.add(counter)
        self.play(tracker.animate.set_value(6.0), run_time=1.1)
        counter.clear_updaters()
        
        # 单位标注
        unit_label = Text(
            "厘米",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).next_to(counter, RIGHT, buff=0.2)
        
        self.play(FadeIn(unit_label), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "用尺子测量长度",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理并移回中心
        self.play(
            FadeOut(title),
            FadeOut(ruler),
            FadeOut(ruler_label),
            FadeOut(indicator_0),
            FadeOut(indicator_6),
            FadeOut(counter),
            FadeOut(unit_label),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 恢复到原位置
        self.play(
            self.segment_AB.animate.put_start_and_end_on(self.A, self.B),
            self.dot_A.animate.move_to(self.A),
            self.dot_B.animate.move_to(self.B),
            self.dot_M.animate.move_to(self.M),
            self.label_A.animate.next_to(self.A, LEFT, buff=0.15),
            self.label_B.animate.next_to(self.B, RIGHT, buff=0.15),
            self.label_M.animate.next_to(self.M, UP, buff=0.15),
            run_time=0.6
        )
    
    def scene_6_operations(self):
        """场景6: 线段的和与差"""
        # 标题
        title = Text(
            "线段的和与差",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 新线段CD
        segment_CD = Line(self.C, self.D, color=self.COLOR_SECONDARY, stroke_width=4)
        dot_C = Dot(self.C, color=self.COLOR_POINT, radius=0.1)
        dot_D = Dot(self.D, color=self.COLOR_POINT, radius=0.1)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                      color=WHITE).next_to(dot_C, LEFT, buff=0.15)
        label_D = Text("D", font="Noto Sans CJK SC", font_size=self.FONT_LABEL, 
                      color=WHITE).next_to(dot_D, RIGHT, buff=0.15)
        
        self.play(
            Create(segment_CD),
            FadeIn(dot_C),
            FadeIn(dot_D),
            FadeIn(label_C),
            FadeIn(label_D),
            run_time=0.7
        )
        
        # 标注长度
        length_AB_label = Text("AB=6", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                              color=self.COLOR_PRIMARY).move_to(UP * 3.2 + LEFT * 2)
        length_CD_label = Text("CD=4", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                              color=self.COLOR_SECONDARY).move_to(UP * 3.2 + RIGHT * 2)
        
        self.play(
            Write(length_AB_label),
            Write(length_CD_label),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # === 线段的和 ===
        subtitle_add = Text(
            "线段的和",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(subtitle_add), run_time=0.5)
        
        # CD复制并移动到B点后
        segment_CD_copy = segment_CD.copy()
        dot_D_copy = dot_D.copy()
        
        # 计算目标位置：从B点开始，沿AB方向延伸
        direction = (self.B - self.A) / np.linalg.norm(self.B - self.A)
        new_C_pos = self.B
        new_D_pos = self.B + direction * self.CD_length
        
        self.play(
            segment_CD_copy.animate.put_start_and_end_on(new_C_pos, new_D_pos),
            dot_D_copy.animate.move_to(new_D_pos),
            run_time=1.0
        )
        
        # 显示结果
        result_add = VGroup(
            MathTex("AB + CD = ", font_size=self.FONT_SUBTITLE),
            Text("10", font="Noto Sans CJK SC", font_size=self.FONT_SUBTITLE, 
                color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.5)
        
        self.play(Write(result_add), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理加法
        self.play(
            FadeOut(subtitle_add),
            FadeOut(segment_CD_copy),
            FadeOut(dot_D_copy),
            FadeOut(result_add),
            run_time=0.5
        )
        
        # === 线段的差 ===
        subtitle_sub = Text(
            "线段的差",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(subtitle_sub), run_time=0.5)
        
        # 在AB上标记CD的长度
        mark_point = self.A + direction * self.CD_length
        segment_mark = Line(self.A, mark_point, color=self.COLOR_SECONDARY, stroke_width=6)
        segment_remain = Line(mark_point, self.B, color=self.COLOR_PRIMARY, stroke_width=6)
        
        self.play(
            FadeOut(self.segment_AB),
            Create(segment_mark),
            Create(segment_remain),
            run_time=0.8
        )
        
        # 标注剩余部分
        brace_remain = Brace(segment_remain, direction=DOWN, buff=0.15, color=GREEN)
        length_remain = Text("2", font="Noto Sans CJK SC", font_size=self.FONT_BODY, 
                            color=GREEN).next_to(brace_remain, DOWN, buff=0.1)
        
        self.play(Create(brace_remain), Write(length_remain), run_time=0.6)
        
        # 显示结果
        result_sub = VGroup(
            MathTex("AB - CD = ", font_size=self.FONT_SUBTITLE),
            Text("2", font="Noto Sans CJK SC", font_size=self.FONT_SUBTITLE, 
                color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.5)
        
        self.play(Write(result_sub), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理所有
        self.play(
            FadeOut(title),
            FadeOut(subtitle_sub),
            FadeOut(segment_CD),
            FadeOut(dot_C),
            FadeOut(dot_D),
            FadeOut(label_C),
            FadeOut(label_D),
            FadeOut(length_AB_label),
            FadeOut(length_CD_label),
            FadeOut(segment_mark),
            FadeOut(segment_remain),
            FadeOut(brace_remain),
            FadeOut(length_remain),
            FadeOut(result_sub),
            FadeOut(self.dot_A),
            FadeOut(self.dot_B),
            FadeOut(self.dot_M),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_M),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "线段知识总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.7)
        
        # 要点列表
        points = VGroup()
        
        point_1 = self.create_summary_point(
            "1",
            "线段是直线上两点之间的部分",
            self.COLOR_PRIMARY,
            UP * 3.5
        )
        points.add(point_1)
        
        point_2 = self.create_summary_point(
            "2",
            "两点之间，线段最短",
            self.COLOR_HIGHLIGHT,
            UP * 2.3
        )
        points.add(point_2)
        
        point_3 = self.create_summary_point(
            "3",
            "中点将线段分成两条相等的部分",
            self.COLOR_MIDPOINT,
            UP * 1.1
        )
        points.add(point_3)
        
        point_4 = self.create_summary_point(
            "4",
            "线段的长度可以用尺子度量",
            self.COLOR_PRIMARY,
            DOWN * 0.1
        )
        points.add(point_4)
        
        point_5 = self.create_summary_point(
            "5",
            "线段可以进行加法和减法运算",
            self.COLOR_SECONDARY,
            DOWN * 1.3
        )
        points.add(point_5)
        
        # 要点依次出现
        for i, point in enumerate(points):
            self.play(point.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(points) - 1:
                self.wait(0.2)
        
        self.wait(0.5)
        
        # 所有要点闪烁
        for point in points:
            self.play(Flash(point[0], color=YELLOW), run_time=0.2)
        
        self.wait(1.0)
        
        # 清理要点
        self.play(
            FadeOut(summary_title),
            FadeOut(points),
            run_time=0.5
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=1.0
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰线段
        decorative_segments = VGroup()
        for i in range(8):
            angle = i * PI / 4
            start = follow_text.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            end = follow_text.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            seg = Line(start, end, color=self.COLOR_PRIMARY, stroke_width=3)
            decorative_segments.add(seg)
        
        self.play(
            *[Create(seg) for seg in decorative_segments],
            run_time=0.6
        )
        
        self.play(
            Rotate(decorative_segments, angle=PI, run_time=1.5),
            rate_func=smooth
        )
        
        # 小图标
        icon_size = 0.25
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_PRIMARY, fill_opacity=0.8, stroke_width=0),
            Square(side_length=icon_size * 2, color=self.COLOR_SECONDARY, fill_opacity=0.8, stroke_width=0),
            Triangle(radius=icon_size * 1.2, color=self.COLOR_HIGHLIGHT, fill_opacity=0.8, stroke_width=0),
            RegularPolygon(n=5, radius=icon_size, color=self.COLOR_MIDPOINT, fill_opacity=0.8, stroke_width=0),
            RegularPolygon(n=6, radius=icon_size, color=self.COLOR_POINT, fill_opacity=0.8, stroke_width=0)
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 2)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorative_segments),
            FadeOut(icons),
            run_time=1.0
        )
    
    def create_summary_point(self, number, text, color, position):
        """创建总结要点卡片"""
        # 编号圆圈
        circle = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        num_text = Text(number, font="Noto Sans CJK SC", font_size=22, color=WHITE)
        icon = VGroup(circle, num_text)
        
        # 要点文字
        content = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        
        # 组合
        point = VGroup(icon, content).arrange(RIGHT, buff=0.3)
        point.move_to(position)
        
        # 初始位置在左侧外
        point.shift(LEFT * 10)
        
        return point


# 运行命令:
# manim -pql line_segment.py LineSegmentConcept  # 快速预览
# manim -qh line_segment.py LineSegmentConcept   # 高质量渲染