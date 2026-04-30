"""
抛物线的定义与标准方程 - Manim 教学动画
Parabola: Definition and Standard Equation

内容: 抛物线定义、焦点、准线、标准方程、四种开口
目标观众: 高二学生
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


class ParabolaDefinitionAndEquation(Scene):
    """
    抛物线定义与标准方程教学动画
    
    场景顺序:
    1. 开场钩子
    2. 抛物线定义
    3. 焦点和准线
    4. 标准方程（y²=2px）
    5. 四种开口方向
    6. 参数p的意义
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PARABOLA = "#e74c3c"       # 红色 - 抛物线主体
        self.COLOR_FOCUS = "#f39c12"          # 橙色 - 焦点
        self.COLOR_DIRECTRIX = "#3498db"      # 蓝色 - 准线
        self.COLOR_DISTANCE = "#2ecc71"       # 绿色 - 距离线
        self.COLOR_POINT_P = "#e91e63"        # 粉色 - 动点P
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_focus_directrix()
        self.scene_4_standard_equation()
        self.scene_5_four_directions()
        self.scene_6_parameter_p()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化抛物线和所有几何元素"""
        # 抛物线参数
        self.p = 2.0  # 焦准距
        
        # 缩放和偏移
        self.SCALE = 0.8
        self.OFFSET = UP * 1.0
        
        # 焦点位置（开口向右）
        self.F = np.array([self.p/2, 0, 0]) * self.SCALE + self.OFFSET
        
        # 准线位置
        self.directrix_x = -self.p/2
        
        print(f"✓ 几何初始化完成: p={self.p}, F=({self.F[0]:.2f}, {self.F[1]:.2f})")
    
    def parabola_point(self, x):
        """抛物线上的点（上半支）y = √(2px)"""
        if x < 0:
            return self.OFFSET
        y = np.sqrt(2 * self.p * x)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def parabola_point_lower(self, x):
        """抛物线下半支 y = -√(2px)"""
        if x < 0:
            return self.OFFSET
        y = -np.sqrt(2 * self.p * x)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "这个曲线随处可见!",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=0.8)
        self.wait(0.3)
        
        # 简化图标（使用抛物线形状）
        icon_1 = Arc(
            radius=0.6,
            start_angle=PI,
            angle=PI,
            color=self.COLOR_PARABOLA,
            stroke_width=4
        ).move_to(UP * 4 + LEFT * 2.5)
        
        icon_2 = Arc(
            radius=0.6,
            start_angle=PI,
            angle=PI,
            color=self.COLOR_PARABOLA,
            stroke_width=4
        ).move_to(UP * 4)
        
        icon_3 = Arc(
            radius=0.6,
            start_angle=PI,
            angle=PI,
            color=self.COLOR_PARABOLA,
            stroke_width=4
        ).move_to(UP * 4 + RIGHT * 2.5)
        
        # 图标文字
        icon_1_text = Text("喷泉", font="PingFang SC", font_size=16, color=GRAY_A).next_to(icon_1, DOWN, buff=0.1)
        icon_2_text = Text("投篮", font="PingFang SC", font_size=16, color=GRAY_A).next_to(icon_2, DOWN, buff=0.1)
        icon_3_text = Text("桥拱", font="PingFang SC", font_size=16, color=GRAY_A).next_to(icon_3, DOWN, buff=0.1)
        
        icons = VGroup(icon_1, icon_2, icon_3)
        texts = VGroup(icon_1_text, icon_2_text, icon_3_text)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], lag_ratio=0.3),
            LaggedStart(*[FadeIn(text) for text in texts], lag_ratio=0.3),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 图标变换为抛物线
        parabola_preview = VGroup(
            FunctionGraph(
                lambda x: np.sqrt(2 * self.p * x) if x >= 0 else 0,
                x_range=[0, 4],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(self.SCALE).move_to(self.OFFSET),
            FunctionGraph(
                lambda x: -np.sqrt(2 * self.p * x) if x >= 0 else 0,
                x_range=[0, 4],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(self.SCALE).move_to(self.OFFSET)
        )
        
        self.play(
            FadeOut(icons),
            FadeOut(texts),
            FadeOut(hook),
            Create(parabola_preview),
            run_time=1.0
        )
        
        self.wait(0.5)
        
        # 保留抛物线预览
        self.parabola_preview = parabola_preview
    
    def scene_2_definition(self):
        """场景2: 抛物线定义"""
        # 标题
        title = Text(
            "抛物线的定义",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 焦点 F
        self.F_dot = Dot(self.F, color=self.COLOR_FOCUS, radius=0.12)
        F_label = MathTex("F", color=self.COLOR_FOCUS, font_size=28).next_to(self.F_dot, DOWN, buff=0.15)
        
        self.play(
            FadeIn(self.F_dot),
            Write(F_label),
            run_time=0.4
        )
        
        # 准线 l
        self.directrix = DashedLine(
            np.array([self.directrix_x, -4, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            np.array([self.directrix_x, 4, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            color=self.COLOR_DIRECTRIX,
            stroke_width=3,
            dash_length=0.1
        )
        
        l_label = MathTex("l", color=self.COLOR_DIRECTRIX, font_size=28).next_to(
            self.directrix.get_start(), DOWN, buff=0.2
        )
        
        self.play(
            Create(self.directrix),
            Write(l_label),
            run_time=0.6
        )
        
        # 创建抛物线路径（用于动点移动）
        parabola_path = FunctionGraph(
            lambda x: np.sqrt(2 * self.p * x) if x >= 0 else 0,
            x_range=[0.2, 4],
            color=self.COLOR_PARABOLA,
            stroke_width=0
        ).scale(self.SCALE).move_to(self.OFFSET)
        
        # 动点 P
        P_dot = Dot(color=self.COLOR_POINT_P, radius=0.10)
        P_label = MathTex("P", color=self.COLOR_POINT_P, font_size=24).add_updater(
            lambda m: m.next_to(P_dot, UR, buff=0.1)
        )
        
        # 距离线段 PF
        line_PF = always_redraw(
            lambda: Line(
                P_dot.get_center(),
                self.F_dot.get_center(),
                color=self.COLOR_DISTANCE,
                stroke_width=2
            )
        )
        
        # 垂线到准线
        perpendicular = always_redraw(
            lambda: DashedLine(
                P_dot.get_center(),
                np.array([self.directrix_x * self.SCALE + self.OFFSET[0], P_dot.get_center()[1], 0]),
                color=self.COLOR_DISTANCE,
                stroke_width=2,
                dash_length=0.08
            )
        )
        
        # 距离标签
        dist_label_PF = always_redraw(
            lambda: Text(
                f"{np.linalg.norm(P_dot.get_center() - self.F_dot.get_center()) / self.SCALE:.1f}",
                font="PingFang SC",
                font_size=18,
                color=self.COLOR_DISTANCE
            ).next_to(line_PF.get_center(), LEFT, buff=0.05)
        )
        
        dist_label_d = always_redraw(
            lambda: Text(
                f"{abs(P_dot.get_center()[0] - (self.directrix_x * self.SCALE + self.OFFSET[0])) / self.SCALE:.1f}",
                font="PingFang SC",
                font_size=18,
                color=self.COLOR_DISTANCE
            ).next_to(perpendicular.get_center(), RIGHT, buff=0.05)
        )
        
        # 初始化P点
        P_dot.move_to(self.parabola_point(1.0))
        
        self.play(
            FadeIn(P_dot),
            FadeIn(P_label),
            run_time=0.4
        )
        
        self.play(
            Create(line_PF),
            Create(perpendicular),
            run_time=0.4
        )
        
        self.play(
            FadeIn(dist_label_PF),
            FadeIn(dist_label_d),
            run_time=0.4
        )
        
        # P点沿抛物线移动
        self.play(
            MoveAlongPath(P_dot, parabola_path),
            run_time=4.0,
            rate_func=smooth
        )
        
        # 定义公式
        definition = MathTex(
            r"|PF| = d",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 4.5)
        
        definition_box = SurroundingRectangle(
            definition,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(definition),
            Create(definition_box),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(line_PF),
            FadeOut(perpendicular),
            FadeOut(dist_label_PF),
            FadeOut(dist_label_d),
            FadeOut(definition_box),
            FadeOut(F_label),
            FadeOut(l_label),
            run_time=0.6
        )
        
        # 保留定义公式，移到角落
        self.definition = definition
        self.play(
            self.definition.animate.scale(0.7).move_to(UP * 4.8 + LEFT * 2.5),
            run_time=0.4
        )
    
    def scene_3_focus_directrix(self):
        """场景3: 焦点和准线"""
        # 副标题
        subtitle = Text(
            "焦点与准线",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_FOCUS
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 焦点高亮
        self.play(
            self.F_dot.animate.scale(1.3),
            run_time=0.3
        )
        self.play(
            self.F_dot.animate.scale(1/1.3),
            run_time=0.3
        )
        
        # 焦点坐标
        F_coords = MathTex(
            r"F(\frac{p}{2}, 0)",
            color=self.COLOR_FOCUS,
            font_size=24
        ).next_to(self.F_dot, DOWN, buff=0.3)
        
        self.play(Write(F_coords), run_time=0.6)
        
        # 准线高亮
        self.play(Indicate(self.directrix, color=self.COLOR_DIRECTRIX), run_time=0.6)
        
        # 准线方程
        directrix_text = Text("x = ", font="PingFang SC", font_size=22, color=WHITE)
        directrix_eq = MathTex(r"-\frac{p}{2}", font_size=22, color=WHITE)
        directrix_formula = VGroup(directrix_text, directrix_eq).arrange(RIGHT, buff=0.05).next_to(
            self.directrix, LEFT, buff=0.3
        ).shift(UP * 2)
        
        self.play(Write(directrix_formula), run_time=0.6)
        
        # 标注焦准距p
        p_line = Line(
            self.F,
            np.array([self.directrix_x, 0, 0]) * self.SCALE + self.OFFSET,
            color=YELLOW,
            stroke_width=3
        )
        
        p_label = MathTex("p", color=YELLOW, font_size=28).next_to(p_line, DOWN, buff=0.1)
        
        self.play(
            Create(p_line),
            Write(p_label),
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "F 不在 l 上",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(F_coords),
            FadeOut(directrix_formula),
            FadeOut(p_line),
            FadeOut(p_label),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def scene_4_standard_equation(self):
        """场景4: 标准方程（y²=2px）"""
        # 副标题
        subtitle = Text(
            "标准方程（开口向右）",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=7,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to(self.OFFSET)
        
        self.play(Create(axes), run_time=0.6)
        
        # 完整抛物线（上下对称）
        parabola_complete = VGroup(
            FunctionGraph(
                lambda x: np.sqrt(2 * self.p * x) if x >= 0 else 0,
                x_range=[0, 4],
                color=self.COLOR_PARABOLA,
                stroke_width=4
            ).scale(self.SCALE).move_to(self.OFFSET),
            FunctionGraph(
                lambda x: -np.sqrt(2 * self.p * x) if x >= 0 else 0,
                x_range=[0, 4],
                color=self.COLOR_PARABOLA,
                stroke_width=4
            ).scale(self.SCALE).move_to(self.OFFSET)
        )
        
        self.play(
            Transform(self.parabola_preview, parabola_complete),
            run_time=1.0
        )
        
        # 标准方程
        standard_eq = MathTex(
            r"y^2 = 2px",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.8)
        
        eq_box = SurroundingRectangle(
            standard_eq,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(standard_eq),
            Create(eq_box),
            run_time=1.0
        )
        
        # 参数条件
        p_condition = MathTex(
            r"p > 0",
            color=GRAY_A,
            font_size=24
        ).next_to(standard_eq, RIGHT, buff=0.5)
        
        self.play(Write(p_condition), run_time=0.5)
        
        # 焦点和准线公式
        focus_text = Text("焦点: ", font="PingFang SC", font_size=20, color=GRAY_A)
        focus_formula = MathTex(r"F(\frac{p}{2}, 0)", font_size=20)
        focus_line = VGroup(focus_text, focus_formula).arrange(RIGHT, buff=0.1).move_to(DOWN * 5)
        
        directrix_text2 = Text("准线: ", font="PingFang SC", font_size=20, color=GRAY_A)
        directrix_formula2 = MathTex(r"x = -\frac{p}{2}", font_size=20)
        directrix_line = VGroup(directrix_text2, directrix_formula2).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.8)
        
        self.play(
            FadeIn(focus_line),
            FadeIn(directrix_line),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(eq_box),
            FadeOut(p_condition),
            FadeOut(focus_line),
            FadeOut(directrix_line),
            run_time=0.6
        )
        
        # 保留坐标系、抛物线和标准方程
        self.axes = axes
        self.standard_eq = standard_eq
        
        self.play(
            self.standard_eq.animate.scale(0.7).move_to(UP * 4.8 + RIGHT * 2),
            run_time=0.4
        )
    
    def scene_5_four_directions(self):
        """场景5: 四种开口方向"""
        # 清空场景
        self.play(
            FadeOut(self.axes),
            FadeOut(self.parabola_preview),
            FadeOut(self.F_dot),
            FadeOut(self.directrix),
            FadeOut(self.definition),
            FadeOut(self.standard_eq),
            run_time=0.5
        )
        
        # 副标题
        subtitle = Text(
            "四种开口方向",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 参数
        small_scale = 0.35
        small_p = 1.5
        
        # 位置
        positions = {
            "right": UP * 2.5 + LEFT * 2,
            "left": UP * 2.5 + RIGHT * 2,
            "up": DOWN * 2.5 + LEFT * 2,
            "down": DOWN * 2.5 + RIGHT * 2,
        }
        
        # 右开口：y² = 2px
        parabola_right = VGroup(
            FunctionGraph(
                lambda x: np.sqrt(2 * small_p * x) if x >= 0 else 0,
                x_range=[0, 3],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale),
            FunctionGraph(
                lambda x: -np.sqrt(2 * small_p * x) if x >= 0 else 0,
                x_range=[0, 3],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale)
        ).move_to(positions["right"])
        
        eq_right = MathTex(r"y^2 = 2px", font_size=18, color=WHITE).next_to(parabola_right, DOWN, buff=0.2)
        
        self.play(
            Create(parabola_right),
            Write(eq_right),
            run_time=0.8
        )
        
        # 左开口：y² = -2px
        parabola_left = VGroup(
            FunctionGraph(
                lambda x: np.sqrt(2 * small_p * (-x)) if x <= 0 else 0,
                x_range=[-3, 0],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale),
            FunctionGraph(
                lambda x: -np.sqrt(2 * small_p * (-x)) if x <= 0 else 0,
                x_range=[-3, 0],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale)
        ).move_to(positions["left"])
        
        eq_left = MathTex(r"y^2 = -2px", font_size=18, color=WHITE).next_to(parabola_left, DOWN, buff=0.2)
        
        self.play(
            Create(parabola_left),
            Write(eq_left),
            run_time=0.8
        )
        
        # 上开口：x² = 2py
        parabola_up = VGroup(
            FunctionGraph(
                lambda y: np.sqrt(2 * small_p * y) if y >= 0 else 0,
                x_range=[0, 3],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale).rotate(PI/2, about_point=ORIGIN),
            FunctionGraph(
                lambda y: -np.sqrt(2 * small_p * y) if y >= 0 else 0,
                x_range=[0, 3],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale).rotate(PI/2, about_point=ORIGIN)
        ).move_to(positions["up"])
        
        eq_up = MathTex(r"x^2 = 2py", font_size=18, color=WHITE).next_to(parabola_up, DOWN, buff=0.2)
        
        self.play(
            Create(parabola_up),
            Write(eq_up),
            run_time=0.8
        )
        
        # 下开口：x² = -2py
        parabola_down = VGroup(
            FunctionGraph(
                lambda y: np.sqrt(2 * small_p * (-y)) if y <= 0 else 0,
                x_range=[-3, 0],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale).rotate(PI/2, about_point=ORIGIN),
            FunctionGraph(
                lambda y: -np.sqrt(2 * small_p * (-y)) if y <= 0 else 0,
                x_range=[-3, 0],
                color=self.COLOR_PARABOLA,
                stroke_width=3
            ).scale(small_scale).rotate(PI/2, about_point=ORIGIN)
        ).move_to(positions["down"])
        
        eq_down = MathTex(r"x^2 = -2py", font_size=18, color=WHITE).next_to(parabola_down, DOWN, buff=0.2)
        
        self.play(
            Create(parabola_down),
            Write(eq_down),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理所有
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.6
        )
    
    def scene_6_parameter_p(self):
        """场景6: 参数p的意义"""
        # 副标题
        subtitle = Text(
            "参数 p 的意义",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 三个不同p值的抛物线
        parabola_p1 = FunctionGraph(
            lambda x: np.sqrt(2 * 1.0 * x) if x >= 0 else 0,
            x_range=[0, 4],
            color=BLUE,
            stroke_width=3
        ).scale(self.SCALE).move_to(self.OFFSET).set_opacity(0.6)
        
        label_p1 = Text("p = 1", font="PingFang SC", font_size=20, color=BLUE).move_to(
            self.parabola_point(3.5) + RIGHT * 0.8
        )
        
        self.play(
            Create(parabola_p1),
            FadeIn(label_p1),
            run_time=0.8
        )
        
        parabola_p2 = FunctionGraph(
            lambda x: np.sqrt(2 * 2.0 * x) if x >= 0 else 0,
            x_range=[0, 4],
            color=self.COLOR_PARABOLA,
            stroke_width=3
        ).scale(self.SCALE).move_to(self.OFFSET).set_opacity(0.6)
        
        label_p2 = Text("p = 2", font="PingFang SC", font_size=20, color=self.COLOR_PARABOLA).move_to(
            np.array([4, np.sqrt(2 * 2.0 * 4), 0]) * self.SCALE + self.OFFSET + RIGHT * 0.8
        )
        
        self.play(
            Create(parabola_p2),
            FadeIn(label_p2),
            run_time=0.8
        )
        
        parabola_p4 = FunctionGraph(
            lambda x: np.sqrt(2 * 4.0 * x) if x >= 0 else 0,
            x_range=[0, 4],
            color=GREEN,
            stroke_width=3
        ).scale(self.SCALE).move_to(self.OFFSET).set_opacity(0.6)
        
        label_p4 = Text("p = 4", font="PingFang SC", font_size=20, color=GREEN).move_to(
            np.array([4, np.sqrt(2 * 4.0 * 4), 0]) * self.SCALE + self.OFFSET + RIGHT * 0.8
        )
        
        self.play(
            Create(parabola_p4),
            FadeIn(label_p4),
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "p 越大，开口越宽",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        note = Text(
            "p 是焦准距",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(
            FadeIn(explanation),
            FadeIn(note),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与关注"""
        # 总结标题
        summary_title = Text(
            "抛物线核心公式",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 关键公式卡片
        formula_1_text = Text("定义: ", font="PingFang SC", font_size=22, color=GRAY_A)
        formula_1_eq = MathTex(r"|PF| = d", font_size=22)
        formula_1 = VGroup(formula_1_text, formula_1_eq).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        
        formula_2_text = Text("开口向右: ", font="PingFang SC", font_size=22, color=GRAY_A)
        formula_2_eq = MathTex(r"y^2 = 2px", font_size=22)
        formula_2 = VGroup(formula_2_text, formula_2_eq).arrange(RIGHT, buff=0.1).move_to(UP * 2.5)
        
        formula_3_text = Text("焦点: ", font="PingFang SC", font_size=22, color=GRAY_A)
        formula_3_eq = MathTex(r"F(\frac{p}{2}, 0)", font_size=22)
        formula_3 = VGroup(formula_3_text, formula_3_eq).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        
        formula_4_text = Text("准线: ", font="PingFang SC", font_size=22, color=GRAY_A)
        formula_4_eq = MathTex(r"x = -\frac{p}{2}", font_size=22)
        formula_4 = VGroup(formula_4_text, formula_4_eq).arrange(RIGHT, buff=0.1).move_to(UP * 0.5)
        
        formulas = VGroup(formula_1, formula_2, formula_3, formula_4)
        
        # 卡片依次滑入
        for formula in formulas:
            formula.shift(LEFT * 10)
            self.play(formula.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.1)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(formulas),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 结束
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql parabola.py ParabolaDefinitionAndEquation  # 快速预览
# manim -qh parabola.py ParabolaDefinitionAndEquation   # 高质量 1080p