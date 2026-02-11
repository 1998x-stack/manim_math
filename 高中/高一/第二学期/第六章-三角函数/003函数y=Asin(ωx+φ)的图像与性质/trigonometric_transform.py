"""
三角函数 y=Asin(ωx+φ)+B 的图像与性质
Manim 教学动画 - TikTok 竖屏版

内容: 参数 A, ω, φ, B 的几何意义及图像变换
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


class TrigonometricTransform(Scene):
    """
    三角函数图像变换教学动画
    
    场景顺序:
    1. 开场钩子
    2. 基础函数 y=sin(x)
    3. 参数 A - 振幅
    4. 参数 ω - 周期
    5. 参数 φ - 相位
    6. 参数 B - 纵向平移
    7. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主函数
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_AMPLITUDE = "#2ecc71"    # 绿色 - 振幅
        self.COLOR_PERIOD = "#f39c12"       # 橙色 - 周期
        self.COLOR_PHASE = "#9b59b6"        # 紫色 - 相位
        self.COLOR_SHIFT = GOLD             # 金色 - 平移
        
        # 字体配置
        self.AUTHOR_FONT = "Noto Sans CJK SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_base_function()
        self.show_amplitude()
        self.show_period()
        self.show_phase()
        self.show_vertical_shift()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.AUTHOR_FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "掌握这个公式",
            font=self.AUTHOR_FONT,
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        hook_text_2 = Text(
            "解题快人一步！",
            font=self.AUTHOR_FONT,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_text), run_time=0.8)
        self.play(FadeIn(hook_text_2, shift=UP * 0.2), run_time=0.5)
        
        # 公式登场
        self.formula = MathTex(
            r"y = A\sin(\omega x + \varphi) + B",
            font_size=48,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(self.formula, scale=1.2), run_time=0.8)
        self.play(Flash(self.formula, color=self.COLOR_HIGHLIGHT, flash_radius=1.0), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hook_text_2),
            run_time=0.5
        )
        
        # 公式缩小移至顶部
        self.play(
            self.formula.animate.scale(0.75).move_to(UP * 6),
            run_time=0.6
        )
    
    def show_base_function(self):
        """场景2: 基础函数 y=sin(x)"""
        # 标题
        title = Text(
            "标准正弦函数",
            font=self.AUTHOR_FONT,
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=[-PI, 3*PI, PI/2],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=10,
            axis_config={
                "include_numbers": False,
                "font_size": 18,
                "include_ticks": True,
                "tick_size": 0.05,
            },
            tips=False
        ).scale(0.65).shift(DOWN * 0.5)
        
        # 添加 x 轴标签 (特殊位置)
        x_labels = VGroup()
        x_positions = [
            (-PI, r"-\pi"),
            (-PI/2, r"-\frac{\pi}{2}"),
            (0, r"0"),
            (PI/2, r"\frac{\pi}{2}"),
            (PI, r"\pi"),
            (3*PI/2, r"\frac{3\pi}{2}"),
            (2*PI, r"2\pi"),
            (5*PI/2, r"\frac{5\pi}{2}"),
        ]
        
        for x_val, label_tex in x_positions:
            label = MathTex(label_tex, font_size=16)
            label.next_to(self.axes.c2p(x_val, 0), DOWN, buff=0.15)
            x_labels.add(label)
        
        # y 轴标签
        y_labels = VGroup()
        for y_val in [-2, -1, 1, 2]:
            label = MathTex(str(y_val), font_size=16)
            label.next_to(self.axes.c2p(0, y_val), LEFT, buff=0.15)
            y_labels.add(label)
        
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_labels), FadeIn(y_labels), run_time=0.5)
        
        # 绘制 y=sin(x)
        self.graph_sin = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[-PI, 3*PI],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(self.graph_sin), run_time=2.0)
        
        # 标注关键点
        # 最大值点
        max_point_1 = self.axes.c2p(PI/2, 1)
        max_point_2 = self.axes.c2p(5*PI/2, 1)
        
        # 最小值点
        min_point = self.axes.c2p(3*PI/2, -1)
        
        # 零点
        zero_points = [
            self.axes.c2p(0, 0),
            self.axes.c2p(PI, 0),
            self.axes.c2p(2*PI, 0),
        ]
        
        max_dots = VGroup(
            Dot(max_point_1, color=self.COLOR_AMPLITUDE, radius=0.08),
            Dot(max_point_2, color=self.COLOR_AMPLITUDE, radius=0.08)
        )
        
        min_dot = Dot(min_point, color=self.COLOR_AMPLITUDE, radius=0.08)
        
        zero_dots = VGroup(*[
            Dot(point, color=GRAY_A, radius=0.06)
            for point in zero_points
        ])
        
        self.play(FadeIn(max_dots), FadeIn(min_dot), FadeIn(zero_dots), run_time=0.6)
        
        # 振幅标注 (双向箭头)
        amplitude_arrow = DoubleArrow(
            start=self.axes.c2p(PI/2, -1),
            end=self.axes.c2p(PI/2, 1),
            color=self.COLOR_AMPLITUDE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        amplitude_label = Text(
            "振幅=1",
            font=self.AUTHOR_FONT,
            font_size=20,
            color=self.COLOR_AMPLITUDE
        ).next_to(amplitude_arrow, RIGHT, buff=0.2)
        
        self.play(Create(amplitude_arrow), FadeIn(amplitude_label), run_time=0.8)
        
        # 周期标注 (括号)
        period_brace = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(2*PI, 0)),
            direction=DOWN,
            color=self.COLOR_PERIOD,
            buff=0.1
        )
        
        period_label = MathTex(
            r"T = 2\pi",
            font_size=24,
            color=self.COLOR_PERIOD
        ).next_to(period_brace, DOWN, buff=0.1)
        
        self.play(Create(period_brace), FadeIn(period_label), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "标准正弦函数：振幅1，周期2π",
            font=self.AUTHOR_FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(amplitude_arrow),
            FadeOut(amplitude_label),
            FadeOut(period_brace),
            FadeOut(period_label),
            FadeOut(explanation),
            FadeOut(max_dots),
            FadeOut(min_dot),
            FadeOut(zero_dots),
            run_time=0.6
        )
        
        # 保留坐标系、标签和曲线
        self.x_labels = x_labels
        self.y_labels = y_labels
    
    def show_amplitude(self):
        """场景3: 参数 A - 振幅变化"""
        # 标题
        title = Text(
            "参数 A：振幅",
            font=self.AUTHOR_FONT,
            font_size=36,
            color=self.COLOR_AMPLITUDE
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 公式变化: sin(x) → 2sin(x)
        formula_new = MathTex(
            r"y = 2\sin(x)",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula, formula_new), run_time=0.8)
        
        # 绘制 y=2sin(x)
        graph_2sin = self.axes.plot(
            lambda x: 2 * np.sin(x),
            x_range=[-PI, 3*PI],
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        self.play(Create(graph_2sin), run_time=1.5)
        
        # 振幅对比线
        amp_line_old = DashedLine(
            self.axes.c2p(-PI, 1),
            self.axes.c2p(3*PI, 1),
            color=self.COLOR_PRIMARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        amp_line_new = DashedLine(
            self.axes.c2p(-PI, 2),
            self.axes.c2p(3*PI, 2),
            color=self.COLOR_SECONDARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(amp_line_old), Create(amp_line_new), run_time=0.6)
        
        # 标注
        label_1 = MathTex(r"A=1", font_size=20, color=self.COLOR_PRIMARY).next_to(amp_line_old, RIGHT, buff=0.1)
        label_2 = MathTex(r"A=2", font_size=20, color=self.COLOR_SECONDARY).next_to(amp_line_new, RIGHT, buff=0.1)
        
        self.play(FadeIn(label_1), FadeIn(label_2), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "A=2：图像纵向拉伸2倍",
            font=self.AUTHOR_FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 高亮最大值点
        max_point_new = self.axes.c2p(PI/2, 2)
        max_dot = Dot(max_point_new, color=self.COLOR_HIGHLIGHT, radius=0.1)
        
        self.play(FadeIn(max_dot, scale=0.5), run_time=0.4)
        self.play(Flash(max_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(amp_line_old),
            FadeOut(amp_line_new),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(explanation),
            FadeOut(max_dot),
            FadeOut(self.graph_sin),  # 移除旧曲线
            run_time=0.6
        )
        
        # 更新基准曲线
        self.graph_sin = graph_2sin
    
    def show_period(self):
        """场景4: 参数 ω - 周期变化"""
        # 标题
        title = Text(
            "参数 ω：周期",
            font=self.AUTHOR_FONT,
            font_size=36,
            color=self.COLOR_PERIOD
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 公式变化: 2sin(x) → 2sin(2x)
        formula_new = MathTex(
            r"y = 2\sin(2x)",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula, formula_new), run_time=0.8)
        
        # 周期公式
        period_formula = MathTex(
            r"T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi",
            font_size=28,
            color=self.COLOR_PERIOD
        ).move_to(UP * 5)
        
        self.play(FadeIn(period_formula), run_time=0.8)
        
        # 绘制 y=2sin(2x)
        graph_omega = self.axes.plot(
            lambda x: 2 * np.sin(2 * x),
            x_range=[-PI, 3*PI],
            color=self.COLOR_PERIOD,
            stroke_width=4
        )
        
        self.play(Create(graph_omega), run_time=2.0)
        
        # 周期标注 - 旧周期
        period_brace_old = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(2*PI, 0)),
            direction=DOWN,
            color=self.COLOR_PRIMARY,
            buff=0.5
        )
        
        period_label_old = MathTex(
            r"T = 2\pi",
            font_size=20,
            color=self.COLOR_PRIMARY
        ).next_to(period_brace_old, DOWN, buff=0.1)
        
        # 周期标注 - 新周期
        period_brace_new = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(PI, 0)),
            direction=UP,
            color=self.COLOR_PERIOD,
            buff=0.3
        )
        
        period_label_new = MathTex(
            r"T = \pi",
            font_size=20,
            color=self.COLOR_PERIOD
        ).next_to(period_brace_new, UP, buff=0.1)
        
        self.play(
            Create(period_brace_old),
            FadeIn(period_label_old),
            run_time=0.6
        )
        
        self.play(
            Create(period_brace_new),
            FadeIn(period_label_new),
            run_time=0.6
        )
        
        # 说明文字
        explanation = Text(
            "ω=2：周期缩短一半",
            font=self.AUTHOR_FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        explanation_2 = Text(
            "图像横向压缩",
            font=self.AUTHOR_FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6.6)
        
        self.play(FadeIn(explanation), FadeIn(explanation_2), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(period_formula),
            FadeOut(period_brace_old),
            FadeOut(period_label_old),
            FadeOut(period_brace_new),
            FadeOut(period_label_new),
            FadeOut(explanation),
            FadeOut(explanation_2),
            FadeOut(self.graph_sin),
            run_time=0.6
        )
        
        # 更新基准曲线
        self.graph_sin = graph_omega
    
    def show_phase(self):
        """场景5: 参数 φ - 相位平移"""
        # 标题
        title = Text(
            "参数 φ：初相位",
            font=self.AUTHOR_FONT,
            font_size=36,
            color=self.COLOR_PHASE
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 公式变化: 2sin(2x) → 2sin(2x+π/4)
        formula_new = MathTex(
            r"y = 2\sin(2x + \frac{\pi}{4})",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula, formula_new), run_time=0.8)
        
        # 平移公式
        shift_formula = MathTex(
            r"\text{shift} = -\frac{\varphi}{\omega} = -\frac{\pi/4}{2} = -\frac{\pi}{8}",
            font_size=24,
            color=self.COLOR_PHASE
        ).move_to(UP * 5)
        
        self.play(FadeIn(shift_formula), run_time=0.8)
        
        # 绘制 y=2sin(2x+π/4)
        graph_phi = self.axes.plot(
            lambda x: 2 * np.sin(2 * x + PI/4),
            x_range=[-PI, 3*PI],
            color=self.COLOR_PHASE,
            stroke_width=4
        )
        
        self.play(Create(graph_phi), run_time=2.0)
        
        # 水平位移箭头 - 显示从某个特征点的移动
        # 原曲线过零点在 x=0
        # 新曲线过零点在 x=-π/8
        
        point_old = self.axes.c2p(0, 0)
        point_new = self.axes.c2p(-PI/8, 0)
        
        shift_arrow = Arrow(
            point_old,
            point_new,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        # 标注点
        dot_old = Dot(point_old, color=self.COLOR_PERIOD, radius=0.08)
        dot_new = Dot(point_new, color=self.COLOR_PHASE, radius=0.08)
        
        self.play(
            FadeIn(dot_old),
            FadeIn(dot_new),
            Create(shift_arrow),
            run_time=1.0
        )
        
        # 说明文字
        explanation = Text(
            "φ>0：图像向左平移",
            font=self.AUTHOR_FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        explanation_2 = Text(
            "(注意：是 -φ/ω)",
            font=self.AUTHOR_FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(DOWN * 6.6)
        
        self.play(FadeIn(explanation), FadeIn(explanation_2), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(shift_formula),
            FadeOut(shift_arrow),
            FadeOut(dot_old),
            FadeOut(dot_new),
            FadeOut(explanation),
            FadeOut(explanation_2),
            FadeOut(self.graph_sin),
            run_time=0.6
        )
        
        # 更新基准曲线
        self.graph_sin = graph_phi
    
    def show_vertical_shift(self):
        """场景6: 参数 B - 纵向平移"""
        # 标题
        title = Text(
            "参数 B：纵向平移",
            font=self.AUTHOR_FONT,
            font_size=36,
            color=self.COLOR_SHIFT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 公式变化: 最终形式
        formula_new = MathTex(
            r"y = 2\sin(2x + \frac{\pi}{4}) + 1",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula, formula_new), run_time=0.8)
        
        # 绘制最终曲线 y=2sin(2x+π/4)+1
        graph_final = self.axes.plot(
            lambda x: 2 * np.sin(2 * x + PI/4) + 1,
            x_range=[-PI, 3*PI],
            color=self.COLOR_SHIFT,
            stroke_width=4
        )
        
        self.play(Create(graph_final), run_time=2.0)
        
        # 中轴线 y=1
        midline = DashedLine(
            self.axes.c2p(-PI, 1),
            self.axes.c2p(3*PI, 1),
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.08,
            stroke_width=3
        )
        
        midline_label = MathTex(
            r"y = 1",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(midline, RIGHT, buff=0.1)
        
        self.play(Create(midline), FadeIn(midline_label), run_time=0.8)
        
        # 垂直平移箭头
        arrow_start = self.axes.c2p(PI/8, 0)
        arrow_end = self.axes.c2p(PI/8, 1)
        
        vertical_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow_label = Text(
            "+1",
            font=self.AUTHOR_FONT,
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(vertical_arrow, RIGHT, buff=0.1)
        
        self.play(Create(vertical_arrow), FadeIn(arrow_label), run_time=0.8)
        
        # 最值标注
        max_point = self.axes.c2p(PI/8, 3)
        min_point = self.axes.c2p(PI/8 + PI, -1)
        
        max_dot = Dot(max_point, color=self.COLOR_AMPLITUDE, radius=0.08)
        min_dot = Dot(min_point, color=self.COLOR_AMPLITUDE, radius=0.08)
        
        max_label = MathTex(
            r"y_{\max} = 3",
            font_size=20,
            color=self.COLOR_AMPLITUDE
        ).next_to(max_dot, UR, buff=0.1)
        
        min_label = MathTex(
            r"y_{\min} = -1",
            font_size=20,
            color=self.COLOR_AMPLITUDE
        ).next_to(min_dot, DR, buff=0.1)
        
        self.play(
            FadeIn(max_dot),
            FadeIn(min_dot),
            FadeIn(max_label),
            FadeIn(min_label),
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "B=1：图像整体上移1单位",
            font=self.AUTHOR_FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        explanation_2 = Text(
            "最大值3，最小值-1",
            font=self.AUTHOR_FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6.6)
        
        self.play(FadeIn(explanation), FadeIn(explanation_2), run_time=0.6)
        self.wait(2.5)
        
        # 清理 - 保留最终曲线用于总结
        self.play(
            FadeOut(title),
            FadeOut(midline),
            FadeOut(midline_label),
            FadeOut(vertical_arrow),
            FadeOut(arrow_label),
            FadeOut(max_dot),
            FadeOut(min_dot),
            FadeOut(max_label),
            FadeOut(min_label),
            FadeOut(explanation),
            FadeOut(explanation_2),
            FadeOut(self.graph_sin),
            run_time=0.6
        )
        
        self.graph_final = graph_final
    
    def show_summary(self):
        """场景7: 性质总结 + 片尾"""
        # 清除坐标系，保留公式
        self.play(
            FadeOut(self.axes),
            FadeOut(self.x_labels),
            FadeOut(self.y_labels),
            FadeOut(self.graph_final),
            run_time=0.8
        )
        
        # 公式居中放大
        formula_final = MathTex(
            r"y = A\sin(\omega x + \varphi) + B",
            font_size=48,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Transform(self.formula, formula_final), run_time=0.8)
        
        # 性质卡片
        card_1 = self.create_property_card(
            "A",
            "振幅",
            r"|A|",
            self.COLOR_AMPLITUDE
        ).move_to(UP * 1.5)
        
        card_2 = self.create_property_card(
            r"\omega",
            "周期",
            r"T = \frac{2\pi}{\omega}",
            self.COLOR_PERIOD
        ).move_to(UP * 0.2)
        
        card_3 = self.create_property_card(
            r"\varphi",
            "相位",
            r"\text{shift} = -\frac{\varphi}{\omega}",
            self.COLOR_PHASE
        ).move_to(DOWN * 1.1)
        
        card_4 = self.create_property_card(
            "B",
            "平移",
            r"y \in [B-|A|, B+|A|]",
            self.COLOR_SHIFT
        ).move_to(DOWN * 2.4)
        
        # 卡片依次出现
        cards = VGroup(card_1, card_2, card_3, card_4)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
            self.wait(0.3)
        
        # 总结文字
        summary = Text(
            "四个参数，掌控三角函数全貌",
            font=self.AUTHOR_FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理进入片尾
        self.play(
            FadeOut(self.formula),
            FadeOut(cards),
            FadeOut(summary),
            run_time=0.8
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.AUTHOR_FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.AUTHOR_FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=self.AUTHOR_FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 波浪装饰
        wave_1 = self.axes.plot(
            lambda x: 0.5 * np.sin(3 * x),
            x_range=[-3, 3],
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).shift(DOWN * 2.5)
        
        wave_2 = self.axes.plot(
            lambda x: 0.5 * np.sin(3 * x + PI/3),
            x_range=[-3, 3],
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).shift(DOWN * 3.2)
        
        wave_3 = self.axes.plot(
            lambda x: 0.5 * np.sin(3 * x + 2*PI/3),
            x_range=[-3, 3],
            color=self.COLOR_AMPLITUDE,
            stroke_width=3
        ).shift(DOWN * 3.9)
        
        waves = VGroup(wave_1, wave_2, wave_3)
        
        self.play(Create(waves), run_time=1.2)
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(waves),
            run_time=1.2
        )
    
    def create_property_card(self, param, name_cn, formula, color):
        """创建参数性质卡片"""
        # 参数符号
        param_text = MathTex(
            param,
            font_size=36,
            color=color
        )
        
        # 中文名称
        name_text = Text(
            name_cn,
            font=self.AUTHOR_FONT,
            font_size=24,
            color=WHITE
        )
        
        # 公式
        formula_text = MathTex(
            formula,
            font_size=22,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(param_text, name_text, formula_text).arrange(RIGHT, buff=0.4)
        
        return card


# 运行命令:
# manim -pql trigonometric_transform.py TrigonometricTransform  # 快速预览
# manim -qh trigonometric_transform.py TrigonometricTransform   # 高质量渲染