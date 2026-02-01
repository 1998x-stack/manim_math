"""
二次函数顶点式 y=a(x-h)²+k 的图像与性质
Quadratic Function Vertex Form Animation

内容: 顶点坐标、对称轴、开口方向、最值性质
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticVertexForm(Scene):
    """
    二次函数顶点式教学动画
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. 顶点概念讲解
    4. 参数a的作用
    5. 最值性质
    6. 性质总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 初始化配色方案
        self.setup_colors()
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 验证几何计算
        self.verify_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_setup_axes()
        self.scene_3_vertex_concept()
        self.scene_4_parameter_a()
        self.scene_5_extreme_values()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_colors(self):
        """初始化颜色配置"""
        self.COLOR_PARABOLA_POSITIVE = "#e74c3c"  # 红色 - a>0
        self.COLOR_PARABOLA_NEGATIVE = "#3498db"  # 蓝色 - a<0
        self.COLOR_VERTEX = "#2ecc71"             # 绿色 - 顶点
        self.COLOR_AXIS_OF_SYMMETRY = "#f39c12"  # 橙色 - 对称轴
        self.COLOR_COORDINATE = WHITE             # 白色 - 坐标系
        self.COLOR_FORMULA = GOLD                 # 金色 - 公式
        self.COLOR_HIGHLIGHT = YELLOW             # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B             # 灰色 - 辅助
    
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ========== 抛物线参数 ==========
        # 示例1: y = 0.5(x-1)² - 2
        self.a1 = 0.5
        self.h1 = 1.0
        self.k1 = -2.0
        
        # 示例2: a>0对比 y = 0.4(x+1)² + 1
        self.a_pos = 0.4
        self.h_compare = -1.0
        self.k_compare = 1.0
        
        # 示例3: a<0对比 y = -0.4(x+1)² + 1
        self.a_neg = -0.4
        
        # ========== 坐标系配置 ==========
        self.axes_config = {
            'x_range': [-5, 5, 1],
            'y_range': [-3, 5, 1],
            'x_length': 7,
            'y_length': 12,
            'axis_config': {
                'include_numbers': True,
                'font_size': 18,
                'color': self.COLOR_COORDINATE,
                'numbers_to_exclude': [0]  # 原点标注单独处理
            }
        }
        
        # 坐标系偏移
        self.axes_offset = DOWN * 0.5
        
        # ========== 定义函数 ==========
        self.func1 = lambda x: self.a1 * (x - self.h1)**2 + self.k1
        self.func_pos = lambda x: self.a_pos * (x - self.h_compare)**2 + self.k_compare
        self.func_neg = lambda x: self.a_neg * (x - self.h_compare)**2 + self.k_compare
        self.func_standard = lambda x: x**2
        
        # ========== 缓存关键坐标 ==========
        # 这些会在创建axes后初始化
        self.vertex_pos_1 = None  # (h1, k1)在Manim坐标
        self.vertex_pos_compare = None  # (h_compare, k_compare)在Manim坐标
    
    def verify_geometry(self):
        """验证几何计算正确性"""
        epsilon = 1e-6
        
        # 验证顶点性质: f(h) = k
        assert abs(self.func1(self.h1) - self.k1) < epsilon, f"顶点1错误: f({self.h1}) = {self.func1(self.h1)} ≠ {self.k1}"
        assert abs(self.func_pos(self.h_compare) - self.k_compare) < epsilon, "顶点2错误"
        assert abs(self.func_neg(self.h_compare) - self.k_compare) < epsilon, "顶点3错误"
        
        # 验证对称性
        for func, h in [(self.func1, self.h1), (self.func_pos, self.h_compare)]:
            for delta in [0.5, 1.0, 1.5]:
                left_val = func(h - delta)
                right_val = func(h + delta)
                assert abs(left_val - right_val) < epsilon, f"对称性错误 at h={h}, delta={delta}"
        
        # 验证a>0时的最小值性质
        for dx in [-0.5, 0.5, 1.0]:
            y_side = self.func1(self.h1 + dx)
            assert y_side >= self.k1 - epsilon, f"最小值错误: f({self.h1+dx}) = {y_side} < k={self.k1}"
        
        # 验证a<0时的最大值性质
        for dx in [-0.5, 0.5, 1.0]:
            y_side = self.func_neg(self.h_compare + dx)
            assert y_side <= self.k_compare + epsilon, f"最大值错误: f({self.h_compare+dx}) = {y_side} > k={self.k_compare}"
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息（顶部，贯穿全片）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "抛物线的顶点在哪?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=0.8)
        self.wait(0.4)
        
        # 公式预览
        formula_preview = MathTex(
            r"y = a(x-h)^2 + k",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(formula_preview, scale=0.8), run_time=0.5)
        self.play(Flash(formula_preview, color=YELLOW, flash_radius=0.5), run_time=0.4)
        self.wait(0.5)
        
        # 清理钩子，保留公式
        self.play(FadeOut(hook_question), run_time=0.4)
        
        # 公式移到顶部
        self.play(
            formula_preview.animate.scale(0.7).move_to(UP * 6),
            run_time=0.5
        )
        
        # 保存公式引用
        self.formula_header = formula_preview
    
    def scene_2_setup_axes(self):
        """场景2: 建立坐标系 (5-10秒)"""
        # 创建坐标系
        self.axes = Axes(**self.axes_config).shift(self.axes_offset)
        
        # 初始化顶点坐标（Manim坐标）
        self.vertex_pos_1 = self.axes.c2p(self.h1, self.k1)
        self.vertex_pos_compare = self.axes.c2p(self.h_compare, self.k_compare)
        
        # 原点标签
        origin_label = MathTex("O", font_size=20, color=WHITE).next_to(
            self.axes.c2p(0, 0), DL, buff=0.15
        )
        
        # 坐标系动画
        self.play(Create(self.axes), run_time=1.5)
        self.play(FadeIn(origin_label), run_time=0.3)
        self.wait(0.3)
        
        # 标准抛物线 y=x² (辅助参考，淡色)
        standard_parabola = self.axes.plot(
            self.func_standard,
            x_range=[-2.2, 2.2],  # 限制范围避免超出边界
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        standard_parabola.set_stroke(opacity=0.4)
        
        # 说明文字
        explain_text = Text(
            "先看标准形式 y=x²",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(Create(standard_parabola), run_time=1.2)
        self.play(FadeIn(explain_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 清理说明，标准抛物线淡化
        self.play(FadeOut(explain_text), run_time=0.3)
        self.play(standard_parabola.animate.set_stroke(opacity=0.15), run_time=0.4)
        
        # 保存引用
        self.standard_parabola = standard_parabola
        self.origin_label = origin_label
    
    def scene_3_vertex_concept(self):
        """场景3: 顶点概念讲解 (10-25秒)"""
        # 淡出标准抛物线
        self.play(FadeOut(self.standard_parabola), run_time=0.3)
        
        # 新抛物线 y = 0.5(x-1)² - 2
        # 计算安全绘制范围: 确保y值在[-3, 5]内
        # 对于 y = 0.5(x-1)² - 2, 当 y=5 时, x ≈ ±2.7
        parabola_1 = self.axes.plot(
            self.func1,
            x_range=[-1.7, 3.7],  # 限制范围避免超出y边界
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        self.play(Create(parabola_1), run_time=1.5)
        self.wait(0.3)
        
        # 顶点
        vertex_dot = Dot(self.vertex_pos_1, color=self.COLOR_VERTEX, radius=0.12)
        vertex_label = Text(
            "V",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_VERTEX,
            weight=BOLD
        ).next_to(vertex_dot, UR, buff=0.15)
        
        vertex_label_2 = Text(
            "顶点",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_VERTEX
        ).next_to(vertex_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(
            FadeIn(vertex_dot, scale=0.5),
            run_time=0.5
        )
        self.play(Flash(vertex_dot, color=self.COLOR_VERTEX, flash_radius=0.3), run_time=0.4)
        self.play(
            Write(vertex_label),
            FadeIn(vertex_label_2),
            run_time=0.5
        )
        
        # 对称轴
        axis_line = DashedLine(
            self.axes.c2p(self.h1, -3),
            self.axes.c2p(self.h1, 5),
            color=self.COLOR_AXIS_OF_SYMMETRY,
            dash_length=0.1,
            stroke_width=2
        )
        
        axis_label = MathTex(
            r"x = h",
            font_size=22,
            color=self.COLOR_AXIS_OF_SYMMETRY
        ).next_to(axis_line.get_top(), RIGHT, buff=0.2)
        
        self.play(Create(axis_line), run_time=0.8)
        self.play(Write(axis_label), run_time=0.5)
        self.wait(0.4)
        
        # 顶点坐标标注
        vertex_coords = MathTex(
            r"V(h, k) = (1, -2)",
            font_size=24,
            color=WHITE
        ).next_to(self.vertex_pos_1, RIGHT, buff=0.8)
        
        # 连线
        coord_line = DashedLine(
            self.vertex_pos_1,
            vertex_coords.get_left(),
            color=GRAY_B,
            dash_length=0.08,
            stroke_width=1.5
        )
        
        self.play(
            Create(coord_line),
            FadeIn(vertex_coords, shift=LEFT * 0.3),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 强调h和k
        formula_highlight = MathTex(
            r"y = a(x-{{h}})^2 + {{k}}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        formula_highlight.set_color_by_tex("h", self.COLOR_AXIS_OF_SYMMETRY)
        formula_highlight.set_color_by_tex("k", self.COLOR_VERTEX)
        
        self.play(
            FadeIn(formula_highlight, shift=DOWN * 0.2),
            run_time=0.5
        )
        self.wait(0.4)
        
        # 说明文字
        explain_1 = Text(
            "h 决定左右位置",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        explain_2 = Text(
            "k 决定上下位置",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explain_1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(explain_2, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)  # 关键概念停留
        
        # 清理
        self.play(
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(formula_highlight),
            FadeOut(coord_line),
            FadeOut(vertex_coords),
            run_time=0.5
        )
        
        # 保存引用（后续场景会用到）
        self.parabola_1 = parabola_1
        self.vertex_dot_1 = vertex_dot
        self.vertex_label_1 = VGroup(vertex_label, vertex_label_2)
        self.axis_line_1 = axis_line
        self.axis_label_1 = axis_label
    
    def scene_4_parameter_a(self):
        """场景4: 参数a的作用 (25-40秒)"""
        # 清除旧元素
        self.play(
            FadeOut(self.parabola_1),
            FadeOut(self.vertex_dot_1),
            FadeOut(self.vertex_label_1),
            FadeOut(self.axis_line_1),
            FadeOut(self.axis_label_1),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "参数 a 控制开口方向",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        self.wait(0.3)
        
        # a>0 抛物线
        # 计算安全范围: y = 0.4(x+1)² + 1, 当y=5时, x ≈ -4.16 或 2.16
        parabola_pos = self.axes.plot(
            self.func_pos,
            x_range=[-4.1, 2.1],  # 限制在合理范围内
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        vertex_dot_pos = Dot(
            self.vertex_pos_compare,
            color=self.COLOR_PARABOLA_POSITIVE,
            radius=0.1
        )
        
        label_pos = Text(
            "a > 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PARABOLA_POSITIVE,
            weight=BOLD
        ).next_to(self.vertex_pos_compare, LEFT, buff=0.8)
        
        explain_pos = Text(
            "开口向上",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_PARABOLA_POSITIVE
        ).next_to(label_pos, DOWN, buff=0.1, aligned_edge=LEFT)
        
        self.play(Create(parabola_pos), run_time=1.2)
        self.play(
            FadeIn(vertex_dot_pos, scale=0.5),
            run_time=0.4
        )
        self.play(
            Write(label_pos),
            FadeIn(explain_pos),
            run_time=0.6
        )
        
        # 向上箭头
        up_arrow = Arrow(
            self.vertex_pos_compare,
            self.vertex_pos_compare + UP * 1.5,
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(up_arrow), run_time=0.5)
        self.wait(0.8)
        
        # a<0 抛物线
        # 计算安全范围: y = -0.4(x+1)² + 1, 当y=-3时, x ≈ -4.16 或 2.16
        parabola_neg = self.axes.plot(
            self.func_neg,
            x_range=[-4.1, 2.1],  # 限制在合理范围内
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=4
        )
        
        vertex_dot_neg = Dot(
            self.vertex_pos_compare,
            color=self.COLOR_PARABOLA_NEGATIVE,
            radius=0.1
        )
        
        label_neg = Text(
            "a < 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PARABOLA_NEGATIVE,
            weight=BOLD
        ).next_to(self.vertex_pos_compare, RIGHT, buff=0.8)
        
        explain_neg = Text(
            "开口向下",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_PARABOLA_NEGATIVE
        ).next_to(label_neg, DOWN, buff=0.1, aligned_edge=LEFT)
        
        self.play(Create(parabola_neg), run_time=1.2)
        self.play(
            FadeIn(vertex_dot_neg, scale=0.5),
            run_time=0.4
        )
        self.play(
            Write(label_neg),
            FadeIn(explain_neg),
            run_time=0.6
        )
        
        # 向下箭头
        down_arrow = Arrow(
            self.vertex_pos_compare,
            self.vertex_pos_compare + DOWN * 1.5,
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(down_arrow), run_time=0.5)
        self.wait(0.5)
        
        # 对比闪烁
        self.play(
            Flash(parabola_pos, color=self.COLOR_PARABOLA_POSITIVE, flash_radius=1.0),
            run_time=0.5
        )
        self.play(
            Flash(parabola_neg, color=self.COLOR_PARABOLA_NEGATIVE, flash_radius=1.0),
            run_time=0.5
        )
        self.wait(1.0)
        
        # 清理，保留a>0用于下一场景
        self.play(
            FadeOut(title),
            FadeOut(parabola_neg),
            FadeOut(vertex_dot_neg),
            FadeOut(label_neg),
            FadeOut(explain_neg),
            FadeOut(down_arrow),
            run_time=0.5
        )
        
        # 保存引用
        self.parabola_pos = parabola_pos
        self.vertex_dot_pos = vertex_dot_pos
        self.label_pos = label_pos
        self.explain_pos = explain_pos
        self.up_arrow = up_arrow
    
    def scene_5_extreme_values(self):
        """场景5: 最值性质 (40-55秒)"""
        # 如果a>0抛物线不在场景中，重新创建（通常已经存在）
        # 这里假设从scene_4保留下来
        
        # 移除上一场景的标签，切换到新抛物线示例
        self.play(
            FadeOut(self.parabola_pos),
            FadeOut(self.vertex_dot_pos),
            FadeOut(self.label_pos),
            FadeOut(self.explain_pos),
            FadeOut(self.up_arrow),
            run_time=0.5
        )
        
        # 使用示例1的抛物线 y = 0.5(x-1)² - 2
        parabola_min = self.axes.plot(
            self.func1,
            x_range=[-1.7, 3.7],  # 限制范围
            color=self.COLOR_PARABOLA_POSITIVE,
            stroke_width=4
        )
        
        vertex_dot_min = Dot(
            self.vertex_pos_1,
            color=self.COLOR_VERTEX,
            radius=0.12
        )
        
        self.play(Create(parabola_min), run_time=0.8)
        self.play(FadeIn(vertex_dot_min, scale=0.5), run_time=0.4)
        
        # 标题
        title = Text(
            "a > 0 时，顶点是最低点",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_PARABOLA_POSITIVE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)
        
        # 最小值标注 - 使用Brace
        brace = Brace(
            Line(self.vertex_pos_1, self.vertex_pos_1 + DOWN * 0.01),
            direction=LEFT,
            buff=0.15,
            color=self.COLOR_VERTEX
        )
        
        min_label = MathTex(
            r"y_{\min} = k = -2",
            font_size=22,
            color=self.COLOR_VERTEX
        ).next_to(brace, LEFT, buff=0.1)
        
        self.play(GrowFromCenter(brace), run_time=0.5)
        self.play(Write(min_label), run_time=0.6)
        self.wait(0.5)
        
        # 动态追踪点演示
        t = ValueTracker(-3)
        
        tracking_dot = always_redraw(lambda: Dot(
            self.axes.c2p(t.get_value(), self.func1(t.get_value())),
            color=YELLOW,
            radius=0.1
        ))
        
        y_value_display = always_redraw(lambda: DecimalNumber(
            self.func1(t.get_value()),
            num_decimal_places=1,
            font_size=20,
            color=YELLOW
        ).next_to(tracking_dot.get_center(), UP, buff=0.25))
        
        self.add(tracking_dot, y_value_display)
        self.wait(0.3)
        
        # 从左滑到顶点
        self.play(t.animate.set_value(self.h1), run_time=2.0, rate_func=linear)
        self.wait(0.8)  # 在顶点处停留
        
        # 从顶点滑到右边
        self.play(t.animate.set_value(4), run_time=1.5, rate_func=linear)
        self.wait(0.4)
        
        # 清理追踪演示
        self.play(
            FadeOut(tracking_dot),
            FadeOut(y_value_display),
            run_time=0.4
        )
        
        # 公式强调
        formula_emphasis = MathTex(
            r"\text{当 } x = h \text{ 时，} y_{\min} = k",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(formula_emphasis, scale=0.9),
            Flash(formula_emphasis, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 切换到a<0示例
        self.play(
            FadeOut(title),
            FadeOut(brace),
            FadeOut(min_label),
            FadeOut(formula_emphasis),
            run_time=0.4
        )
        
        # a<0抛物线
        parabola_max = self.axes.plot(
            self.func_neg,
            x_range=[-4.1, 2.1],  # 限制范围
            color=self.COLOR_PARABOLA_NEGATIVE,
            stroke_width=4
        )
        
        vertex_dot_max = Dot(
            self.vertex_pos_compare,
            color=self.COLOR_VERTEX,
            radius=0.12
        )
        
        title_max = Text(
            "a < 0 时，顶点是最高点",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_PARABOLA_NEGATIVE
        ).move_to(UP * 5.5)
        
        max_label = MathTex(
            r"y_{\max} = k = 1",
            font_size=22,
            color=self.COLOR_VERTEX
        ).next_to(self.vertex_pos_compare, RIGHT, buff=0.5)
        
        self.play(
            Transform(parabola_min, parabola_max),
            Transform(vertex_dot_min, vertex_dot_max),
            run_time=1.0
        )
        
        self.play(FadeIn(title_max, shift=DOWN * 0.2), run_time=0.5)
        self.play(Write(max_label), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(parabola_min),
            FadeOut(vertex_dot_min),
            FadeOut(title_max),
            FadeOut(max_label),
            run_time=0.5
        )
    
    def scene_6_summary(self):
        """场景6: 性质总结 (55-65秒)"""
        # 清空场景（保留axes和author_info）
        all_mobjects = [mob for mob in self.mobjects if mob not in [self.axes, self.author_info, self.origin_label]]
        if all_mobjects:
            self.play(*[FadeOut(mob) for mob in all_mobjects], run_time=0.6)
        
        # 标题
        title = Text(
            "性质总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.4)
        
        # 公式卡片
        formula_box = SurroundingRectangle(
            MathTex(r"y = a(x-h)^2 + k", font_size=32, color=self.COLOR_FORMULA),
            color=self.COLOR_FORMULA,
            buff=0.2,
            stroke_width=2
        )
        formula_group = VGroup(
            formula_box,
            MathTex(r"y = a(x-h)^2 + k", font_size=32, color=self.COLOR_FORMULA)
        ).arrange(RIGHT, buff=0).move_to(UP * 4.5)
        
        self.play(FadeIn(formula_group, shift=RIGHT * 0.5), run_time=0.5)
        
        # 性质卡片
        def create_property_card(icon_color, title_text, content_text, position):
            """创建属性卡片"""
            icon = Circle(radius=0.2, fill_color=icon_color, fill_opacity=1, stroke_width=0)
            title = Text(title_text, font="Noto Sans CJK SC", font_size=22, color=WHITE, weight=BOLD)
            content = Text(content_text, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            
            card = VGroup(icon, title, content).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            card.move_to(position + LEFT * 10)  # 初始在左侧屏幕外
            return card
        
        card_1 = create_property_card(
            self.COLOR_VERTEX,
            "顶点",
            "(h, k)",
            UP * 2.5
        )
        
        card_2 = create_property_card(
            self.COLOR_AXIS_OF_SYMMETRY,
            "对称轴",
            "x = h",
            UP * 1.2
        )
        
        card_3 = create_property_card(
            self.COLOR_PARABOLA_POSITIVE,
            "a > 0",
            "开口向上, 最小值 k",
            DOWN * 0.1
        )
        
        card_4 = create_property_card(
            self.COLOR_PARABOLA_NEGATIVE,
            "a < 0",
            "开口向下, 最大值 k",
            DOWN * 1.4
        )
        
        # 卡片依次滑入
        for card in [card_1, card_2, card_3, card_4]:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.2)
        
        # 全体闪烁强调
        all_cards = VGroup(card_1, card_2, card_3, card_4)
        for card in all_cards:
            self.play(Flash(card, color=YELLOW, flash_radius=0.3), run_time=0.3)
        
        self.wait(1.5)  # 给观众消化时间
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_group),
            FadeOut(all_cards),
            run_time=0.5
        )
    
    def scene_7_outro(self):
        """场景7: 片尾关注 (65-75秒)"""
        # 清空所有元素
        all_mobjects = [mob for mob in self.mobjects if mob != self.author_info]
        if all_mobjects:
            self.play(*[FadeOut(mob) for mob in all_mobjects], run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注引导
        follow_text = Text(
            "关注我，学更多二次函数技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(
            Write(follow_text),
            Flash(follow_text, color=YELLOW, flash_radius=0.5),
            run_time=0.7
        )
        
        # 装饰抛物线
        decorative_parabolas = VGroup()
        colors = [self.COLOR_PARABOLA_POSITIVE, self.COLOR_VERTEX, self.COLOR_PARABOLA_NEGATIVE]
        
        for i, color in enumerate(colors):
            small_axes = Axes(
                x_range=[-1, 1, 1],
                y_range=[-1, 1, 1],
                x_length=0.8,
                y_length=0.8,
                axis_config={'stroke_width': 0}
            )
            small_parabola = small_axes.plot(
                lambda x: 0.5 * x**2,
                x_range=[-1, 1],
                color=color,
                stroke_width=3
            )
            
            parabola_group = VGroup(small_axes, small_parabola)
            angle = i * 2 * PI / 3
            position = 2 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 2.5
            parabola_group.move_to(position)
            decorative_parabolas.add(parabola_group)
        
        self.play(*[FadeIn(p, scale=0.5) for p in decorative_parabolas], run_time=0.5)
        self.play(Rotate(decorative_parabolas, angle=PI, run_time=1.5))
        
        # 闪烁强调
        self.play(
            Flash(follow_text, color=YELLOW, flash_radius=0.5),
            run_time=0.4
        )
        self.play(
            Flash(follow_text, color=YELLOW, flash_radius=0.5),
            run_time=0.4
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorative_parabolas),
            run_time=1.2
        )


# ==================== 运行命令 ====================
# 快速预览:
#   manim -pql quadratic_vertex_form.py QuadraticVertexForm
#
# 高质量渲染:
#   manim -qh quadratic_vertex_form.py QuadraticVertexForm
#
# 4K质量:
#   manim -qk quadratic_vertex_form.py QuadraticVertexForm