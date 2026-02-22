"""
函数y=Asin(ωx+φ)的图像与性质 - 三角函数变换教学动画
使用 Manim 创建的中学数学教学视频

内容: 函数y=Asin(ωx+φ)的参数A、ω、φ、B对图像的影响
目标观众: 高中学生
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


class 函数yAsinωxφ的图像与性质(Scene):
    """
    函数y=Asin(ωx+φ)的图像与性质教学动画场景

    场景顺序:
    1. 开场介绍
    2. 基础正弦函数回顾
    3. 振幅A的作用
    4. 频率ω的作用
    5. 相位φ的作用
    6. 垂直平移B的作用
    7. 参数联动演示
    8. 总结回顾
    9. 片尾关注
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"    # 红色 - 强调
        self.COLOR_SECONDARY = "#3498db"  # 蓝色 - 坐标轴/基础函数
        self.COLOR_HIGHLIGHT = YELLOW     # 黄色 - 重要元素
        self.COLOR_AUXILIARY = GRAY_B     # 灰色 - 辅助线
        self.COLOR_FUNCTION = BLUE        # 蓝色 - 函数图像
        self.COLOR_TRANSFORMED = RED      # 红色 - 变换后图像

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_base_sine()
        self.show_amplitude_effect()
        self.show_frequency_effect()
        self.show_phase_effect()
        self.show_vertical_shift_effect()
        self.show_param_interplay()
        self.show_summary()
        self.show_outro()

    def setup_geometry(self):
        """初始化坐标系和其他几何参数"""
        # 用于后续函数绘制的参数
        self.x_range = [-4, 4, 1]  # x范围
        self.y_range = [-4, 4, 1]  # y范围

        # 初始参数值
        self.A_init = 1.0
        self.omega_init = 1.0
        self.phi_init = 0.0
        self.B_init = 0.0

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "函数y=Asin(ωx+φ)的图像与性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 主函数公式
        formula = MathTex(
            "y = A \\sin(\\omega x + \\varphi) + B",
            font_size=40
        ).move_to(UP * 5)

        self.play(Write(formula), run_time=1.0)

        # 提示文字
        hint = Text(
            "四个参数如何影响图像？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)

        self.play(FadeIn(hint, shift=DOWN * 0.3), run_time=0.5)
        self.wait(1.5)

        # 保留重要元素，清理其他
        self.title_keep = title
        self.formula_keep = formula

        self.play(
            FadeOut(hint),
            run_time=0.5
        )

    def show_base_sine(self):
        """场景2: 基础正弦函数回顾"""
        # 保存上一部分的元素位置
        title_group = VGroup(self.title_keep, self.formula_keep)
        self.play(title_group.animate.to_edge(UP).shift(DOWN * 0.5), run_time=0.8)

        # 创建坐标系
        axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            axis_config={"color": self.COLOR_SECONDARY},
            x_axis_config={
                "numbers_to_include": np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2),
                "include_tip": True,
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 4, 1),
                "include_tip": True,
                "label_direction": LEFT,
            },
            tips=True
        )

        # 添加轴标签
        x_label = axes.get_x_axis_label(Tex("$x$", font_size=24), edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(Tex("$y$", font_size=24), edge=LEFT, direction=LEFT)

        axes_group = VGroup(axes, x_label, y_label)
        axes_group.scale(0.8).move_to(UP * 1.5)

        self.play(Create(axes_group), run_time=1.0)

        # 绘制基础正弦函数 y = sin(x)
        base_graph = axes.plot(lambda x: np.sin(x), color=self.COLOR_FUNCTION, x_range=[-4, 4])

        self.play(Create(base_graph), run_time=1.5)

        # 标记关键特征：振幅、周期
        # 振幅标记
        amp_brace = Brace(Line(axes.c2p(0, 0), axes.c2p(0, 1)), direction=RIGHT, color=YELLOW)
        amp_text = Tex("振幅: 1", font_size=20).next_to(amp_brace, RIGHT)
        amplitude_group = VGroup(amp_brace, amp_text)

        self.play(GrowFromCenter(amp_brace), Write(amp_text), run_time=0.8)

        # 周期标记
        period_line = Line(
            axes.c2p(0, -1.5),
            axes.c2p(2*np.pi, -1.5),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        period_brace = Brace(period_line, direction=DOWN, color=YELLOW)
        period_text = Tex("周期: 2\\pi", font_size=20).next_to(period_brace, DOWN)
        period_group = VGroup(period_line, period_brace, period_text)

        self.play(Create(period_line), GrowFromCenter(period_brace), Write(period_text), run_time=1.0)

        self.wait(1.5)

        # 保存重要元素供后续使用
        self.axes = axes
        self.base_graph = base_graph

        # 清理部分元素
        self.play(
            FadeOut(amplitude_group),
            FadeOut(period_group),
            run_time=0.6
        )

    def show_amplitude_effect(self):
        """场景3: 振幅A的作用"""
        # 更新公式
        new_formula = MathTex(
            "y = A \\sin(x)",
            "\\quad A =", "2",
            font_size=36
        ).move_to(UP * 6.5)

        self.play(TransformMatchingShapes(self.formula_keep, new_formula), run_time=0.8)
        self.formula_keep = new_formula

        # 原始函数变虚线
        original_dashed = DashedVMobject(self.base_graph, num_dashes=30)
        self.play(Transform(self.base_graph, original_dashed), run_time=0.8)

        # A=2的函数图像
        amp_2_graph = self.axes.plot(lambda x: 2 * np.sin(x), color=self.COLOR_TRANSFORMED, x_range=[-4, 4])

        self.play(Create(amp_2_graph), run_time=1.2)

        # 标记新的振幅
        amp_brace_new = Brace(Line(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, 2)
        ), direction=RIGHT, color=self.COLOR_HIGHLIGHT)
        amp_text_new = Tex("振幅: 2", font_size=20).next_to(amp_brace_new, RIGHT)

        self.play(GrowFromCenter(amp_brace_new), Write(amp_text_new), run_time=0.8)

        # 显示A对振幅的影响
        a_impact = Tex("A越大，图像拉伸越厉害", font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.5)
        self.play(FadeIn(a_impact, shift=UP * 0.3), run_time=0.5)

        self.wait(1.5)

        # 保存当前状态
        self.current_graph = amp_2_graph
        self.amp_brace = amp_brace_new
        self.amp_text = amp_text_new

        self.play(
            FadeOut(a_impact),
            run_time=0.5
        )

    def show_frequency_effect(self):
        """场景4: 频率ω的作用"""
        # 更新公式
        new_formula = MathTex(
            "y = 2 \\sin(", "\\omega", "x)",
            "\\quad \\omega =", "2",
            font_size=36
        ).move_to(UP * 6.5)

        self.play(TransformMatchingShapes(self.formula_keep, new_formula), run_time=0.8)
        self.formula_keep = new_formula

        # 保持原函数作为参考（更虚一些）
        ref_graph = DashedVMobject(self.current_graph, num_dashes=20)
        self.play(Transform(self.current_graph, ref_graph), run_time=0.6)

        # ω=2的函数图像（周期变为π）
        freq_2_graph = self.axes.plot(lambda x: 2 * np.sin(2*x), color=self.COLOR_TRANSFORMED, x_range=[-4, 4])

        self.play(Create(freq_2_graph), run_time=1.2)

        # 标记新周期
        period_line_new = Line(
            self.axes.c2p(0, -2.5),
            self.axes.c2p(np.pi, -2.5),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        period_brace_new = Brace(period_line_new, direction=DOWN, color=YELLOW)
        period_text_new = Tex("周期: \\pi", font_size=20).next_to(period_brace_new, DOWN)

        self.play(Create(period_line_new), GrowFromCenter(period_brace_new), Write(period_text_new), run_time=1.0)

        # 显示ω对周期的影响公式
        period_formula = Tex("周期 T = \\frac{2\\pi}{\\omega}", font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.5)
        self.play(FadeIn(period_formula, shift=UP * 0.3), run_time=0.5)

        self.wait(1.5)

        # 保存当前状态
        self.current_graph = freq_2_graph
        self.period_line = period_line_new
        self.period_brace = period_brace_new
        self.period_text = period_text_new

        self.play(
            FadeOut(period_formula),
            run_time=0.5
        )

    def show_phase_effect(self):
        """场景5: 相位φ的作用"""
        # 更新公式
        new_formula = MathTex(
            "y = 2 \\sin(2x + ", "\\varphi", ")",
            "\\quad \\varphi =", "\\frac{\\pi}{4}",
            font_size=36
        ).move_to(UP * 6.5)

        self.play(TransformMatchingShapes(self.formula_keep, new_formula), run_time=0.8)
        self.formula_keep = new_formula

        # 保持原函数作为参考
        ref_graph = DashedVMobject(self.current_graph, num_dashes=20)
        self.play(Transform(self.current_graph, ref_graph), run_time=0.6)

        # φ=π/4的函数图像（左移）
        phase_shift_graph = self.axes.plot(lambda x: 2 * np.sin(2*x + np.pi/4), color=self.COLOR_TRANSFORMED, x_range=[-4, 4])

        self.play(Create(phase_shift_graph), run_time=1.2)

        # 显示相位移动
        shift_arrow = Arrow(
            self.axes.c2p(-np.pi/8, 2),
            self.axes.c2p(0, 2),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        shift_label = Tex("左移 $\\frac{\\pi}{8}$", font_size=20, color=self.COLOR_HIGHLIGHT).next_to(shift_arrow, UP)

        self.play(GrowArrow(shift_arrow), Write(shift_label), run_time=0.8)

        # 显示相位公式
        phase_explanation = Tex("相位: $\\omega x + \\varphi$, 初相: $\\varphi$", font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.5)
        self.play(FadeIn(phase_explanation, shift=UP * 0.3), run_time=0.5)

        self.wait(1.5)

        # 保存当前状态
        self.current_graph = phase_shift_graph
        self.shift_arrow = shift_arrow
        self.shift_label = shift_label

        self.play(
            FadeOut(phase_explanation),
            run_time=0.5
        )

    def show_vertical_shift_effect(self):
        """场景6: 垂直平移B的作用"""
        # 更新公式
        new_formula = MathTex(
            "y = 2 \\sin(2x + \\frac{\\pi}{4}) + ", "B",
            "\\quad B =", "1",
            font_size=36
        ).move_to(UP * 6.5)

        self.play(TransformMatchingShapes(self.formula_keep, new_formula), run_time=0.8)
        self.formula_keep = new_formula

        # 保持原函数作为参考
        ref_graph = DashedVMobject(self.current_graph, num_dashes=20)
        self.play(Transform(self.current_graph, ref_graph), run_time=0.6)

        # B=1的函数图像（向上平移1）
        vertical_shift_graph = self.axes.plot(lambda x: 2 * np.sin(2*x + np.pi/4) + 1, color=self.COLOR_TRANSFORMED, x_range=[-4, 4])

        self.play(Create(vertical_shift_graph), run_time=1.2)

        # 显示垂直移动
        v_shift_arrow = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, 1),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        v_shift_label = Tex("上移 1", font_size=20, color=self.COLOR_HIGHLIGHT).next_to(v_shift_arrow, RIGHT)

        self.play(GrowArrow(v_shift_arrow), Write(v_shift_label), run_time=0.8)

        # 显示整体函数
        full_formula = MathTex(
            "y = A \\sin(\\omega x + \\varphi) + B",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)

        self.play(Write(full_formula), run_time=0.8)

        self.wait(1.5)

        # 保存当前最终状态
        self.final_graph = vertical_shift_graph
        self.full_formula = full_formula

    def show_param_interplay(self):
        """场景7: 参数联动演示"""
        # 清理之前的所有辅助标记
        to_fade_out = []
        if hasattr(self, 'shift_arrow'):
            to_fade_out.append(self.shift_arrow)
        if hasattr(self, 'shift_label'):
            to_fade_out.append(self.shift_label)
        if hasattr(self, 'v_shift_arrow'):
            to_fade_out.append(self.v_shift_arrow)
        if hasattr(self, 'v_shift_label'):
            to_fade_out.append(self.v_shift_label)

        if to_fade_out:
            self.play(*[FadeOut(obj) for obj in to_fade_out], run_time=0.5)

        # 展示参数的作用总结
        param_grid = VGroup()

        # A参数说明
        a_title = Tex("A (振幅)", font_size=28, color=self.COLOR_FUNCTION).to_edge(UP).shift(LEFT * 3)
        a_desc = Tex("控制图像高度", font_size=20).next_to(a_title, DOWN)
        a_example = MathTex("A=1 \\to A=3", font_size=24).next_to(a_desc, DOWN)
        a_group = VGroup(a_title, a_desc, a_example).arrange(DOWN, buff=0.2).shift(LEFT * 3)

        # ω参数说明
        w_title = Tex("\\omega (频率)", font_size=28, color=self.COLOR_FUNCTION).to_edge(UP)
        w_desc = Tex("控制图像密度", font_size=20).next_to(w_title, DOWN)
        w_example = MathTex("\\omega=1 \\to \\omega=2", font_size=24).next_to(w_desc, DOWN)
        w_group = VGroup(w_title, w_desc, w_example).arrange(DOWN, buff=0.2)

        # φ参数说明
        p_title = Tex("\\varphi (相位)", font_size=28, color=self.COLOR_FUNCTION).to_edge(UP).shift(RIGHT * 3)
        p_desc = Tex("控制图像平移", font_size=20).next_to(p_title, DOWN)
        p_example = MathTex("\\varphi=0 \\to \\varphi=\\frac{\\pi}{4}", font_size=24).next_to(p_desc, DOWN)
        p_group = VGroup(p_title, p_desc, p_example).arrange(DOWN, buff=0.2).shift(RIGHT * 3)

        # 整体布局
        param_grid.add(a_group, w_group, p_group)

        self.play(
            FadeIn(a_group, shift=DOWN * 0.5),
            FadeIn(w_group, shift=DOWN * 0.5),
            FadeIn(p_group, shift=DOWN * 0.5),
            run_time=1.0
        )

        # 稍作停顿
        self.wait(1.5)

        # 演示函数图像随参数变化
        # 先还原到基础函数便于演示
        basic_graph = self.axes.plot(lambda x: np.sin(x), color=self.COLOR_SECONDARY, x_range=[-4, 4])
        self.play(Transform(self.final_graph, basic_graph), run_time=1.0)

        # 演示各个参数的叠加效果
        # A=2
        graph_a2 = self.axes.plot(lambda x: 2 * np.sin(x), color=self.COLOR_FUNCTION, x_range=[-4, 4])
        self.play(Transform(self.final_graph, graph_a2), run_time=0.8)

        # ω=2
        graph_w2 = self.axes.plot(lambda x: 2 * np.sin(2*x), color=self.COLOR_FUNCTION, x_range=[-4, 4])
        self.play(Transform(self.final_graph, graph_w2), run_time=0.8)

        # φ=π/4
        graph_pshift = self.axes.plot(lambda x: 2 * np.sin(2*x + np.pi/4), color=self.COLOR_FUNCTION, x_range=[-4, 4])
        self.play(Transform(self.final_graph, graph_pshift), run_time=0.8)

        # B=1 (final)
        graph_final = self.axes.plot(lambda x: 2 * np.sin(2*x + np.pi/4) + 1, color=self.COLOR_TRANSFORMED, x_range=[-4, 4])
        self.play(Transform(self.final_graph, graph_final), run_time=0.8)

        self.wait(1.5)

    def show_summary(self):
        """场景8: 总结回顾"""
        # 清理之前的元素
        self.play(
            FadeOut(self.formula_keep),
            FadeOut(self.full_formula),
            self.play(*[FadeOut(m) for m in self.mobjects]),  # 清理所有其他元素
            run_time=0.8
        )

        # 重新创建重要的视觉元素以便总结
        # 坐标系
        summary_axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            axis_config={"color": self.COLOR_SECONDARY},
            x_axis_config={
                "numbers_to_include": np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2),
                "include_tip": True,
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 4, 1),
                "include_tip": True,
            },
            tips=True
        )
        summary_axes.scale(0.7).move_to(UP * 1)

        # 最终变换函数
        final_func_graph = summary_axes.plot(
            lambda x: 2 * np.sin(2*x + np.pi/4) + 1,
            color=self.COLOR_TRANSFORMED,
            x_range=[-4, 4]
        )

        self.play(Create(summary_axes), run_time=0.8)
        self.play(Create(final_func_graph), run_time=1.2)

        # 参数总结
        summary_title = Text(
            "参数作用总结",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)

        # 参数说明列表
        a_summary = Tex("• $A$: 振幅，控制图像纵向拉伸", font_size=28).move_to(UP * 4)
        omega_summary = Tex("• $\\omega$: 频率，控制周期 $T = \\frac{2\\pi}{\\omega}$", font_size=28).move_to(UP * 3)
        phi_summary = Tex("• $\\varphi$: 初相，控制水平平移", font_size=28).move_to(UP * 2)
        b_summary = Tex("• $B$: 垂直平移量", font_size=28).move_to(UP * 1)

        summary_list = VGroup(a_summary, omega_summary, phi_summary, b_summary)
        summary_list.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(LEFT * 1.5)

        self.play(Write(summary_title), run_time=0.5)
        self.play(Write(a_summary), run_time=0.6)
        self.play(Write(omega_summary), run_time=0.6)
        self.play(Write(phi_summary), run_time=0.6)
        self.play(Write(b_summary), run_time=0.6)

        self.wait(2.0)

    def show_outro(self):
        """场景9: 片尾关注"""
        # 清理之前的元素
        self.play(self.play(*[FadeOut(m) for m in self.mobjects]), run_time=1.0)

        # 作者信息
        author_name = Text(
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

        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我, 学更多三角函数知识!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW
        ).move_to(ORIGIN)

        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)

        # 波浪函数装饰
        wave_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 1, 1],
            axis_config={"include_ticks": False, "stroke_width": 0},
            tips=False
        ).scale(0.3).move_to(DOWN * 2)

        wave_graph = wave_axes.plot(lambda x: 0.5 * np.sin(2*x), color=GOLD, x_range=[-5, 5])

        self.play(Create(wave_graph), run_time=1.0)

        # 旋转装饰
        self.play(Rotate(wave_graph, angle=PI, run_time=2))

        self.wait(2.0)


if __name__ == "__main__":
    # 运行命令:
    # manim -pql 003_函数y=Asin(ωx+φ)的图像与性质.py 函数yAsinωxφ的图像与性质  # 快速预览
    # manim -qh 003_函数y=Asin(ωx+φ)的图像与性质.py 函数yAsinωxφ的图像与性质   # 高质量
    pass