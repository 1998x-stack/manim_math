"""
抛物线的几何性质 - Manim 教学动画
Parabola Properties Animation

内容: 抛物线 y²=2px (p>0) 的几何性质
- 范围与对称性
- 离心率 e=1
- 通径长度 2p
- 焦半径公式 |PF|=x₀+p/2
- 光学反射性质

目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ParabolaProperties(Scene):
    """
    抛物线几何性质教学动画场景
    
    场景顺序:
    1. 开场钩子 (4s)
    2. 抛物线定义 (7s)
    3. 几何性质 - 范围与对称性 (7s)
    4. 离心率 e=1 (6s)
    5. 通径 (8s)
    6. 焦半径公式 (9s)
    7. 光学性质 (13s)
    8. 总结 + 片尾 (21s)
    总计: ~75秒
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ========== 配色方案 ==========
        self.COLOR_PARABOLA = "#3498db"      # 蓝色 - 抛物线主体
        self.COLOR_FOCUS = "#e74c3c"         # 红色 - 焦点
        self.COLOR_DIRECTRIX = "#2ecc71"     # 绿色 - 准线
        self.COLOR_CHORD = "#f39c12"         # 橙色 - 弦（通径）
        self.COLOR_LIGHT = "#f1c40f"         # 黄色 - 光线
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 辅助线
        self.COLOR_AXIS = WHITE              # 坐标轴
        
        # ========== 字体大小规范 ==========
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 20
        self.FONT_SMALL = 18
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_properties()
        self.scene_4_eccentricity()
        self.scene_5_latus_rectum()
        self.scene_6_focal_radius()
        self.scene_7_optics()
        self.scene_8_summary()
    
    def setup_geometry(self):
        """初始化抛物线和所有几何元素（已通过 verify_geometry.py 验证）"""
        # ========== 基准参数 ==========
        self.p = 1.5  # 焦参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.0
        
        # ========== 焦点和准线 ==========
        self.F = np.array([self.p/2, 0, 0]) * self.SCALE + self.OFFSET
        self.directrix_x = (-self.p/2) * self.SCALE + self.OFFSET[0]
        
        # ========== 顶点 ==========
        self.O = np.array([0, 0, 0]) * self.SCALE + self.OFFSET
        
        # ========== 通径端点 ==========
        self.A_latus = np.array([self.p/2, self.p, 0]) * self.SCALE + self.OFFSET
        self.B_latus = np.array([self.p/2, -self.p, 0]) * self.SCALE + self.OFFSET
        
        # ========== 坐标轴范围 ==========
        self.x_range = [-2, 6, 1]
        self.y_range = [-4, 4, 1]
        
        print("✓ 几何初始化完成")
        print(f"  焦点 F = {self.F}")
        print(f"  准线 x = {self.directrix_x}")
        print(f"  参数 p = {self.p}")
    
    def parabola_function(self, x):
        """抛物线函数 y = √(2px)"""
        axes_x = self.axes.p2c(np.array([x, 0, 0]))[0]
        
        if axes_x < 0:
            return np.nan
        
        y_raw = np.sqrt(2 * self.p * axes_x)
        return y_raw
    
    def parabola_point(self, x_val):
        """返回抛物线上的点坐标（上半支）"""
        if x_val < 0:
            return None
        y_val = np.sqrt(2 * self.p * x_val)
        return self.axes.c2p(x_val, y_val)
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-4秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "为什么卫星天线是抛物面?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 卫星天线图标（简化版）
        satellite = VGroup(
            # 天线抛物面
            Arc(radius=1.2, start_angle=-PI/3, angle=2*PI/3, 
                color=self.COLOR_PARABOLA, stroke_width=6),
            # 焦点接收器
            Dot(ORIGIN, radius=0.15, color=self.COLOR_FOCUS),
            # 支撑杆
            Line(ORIGIN, DOWN*0.8, color=GRAY, stroke_width=3)
        ).scale(0.8).move_to(UP * 3)
        
        self.play(FadeIn(satellite, scale=0.5), run_time=0.5)
        
        # 提示文字
        hint = Text(
            "答案就在抛物线的性质中!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(satellite),
            FadeOut(hint),
            run_time=0.5
        )
        
        # 作者信息移至顶部小字
        self.author_info.generate_target()
        self.author_info.target.scale(0.8).move_to(UP * 7.5)
        self.play(MoveToTarget(self.author_info), run_time=0.3)
    
    def scene_2_definition(self):
        """场景2: 抛物线定义 (4-11秒)"""
        # 标题
        title = Text(
            "抛物线的定义",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 创建坐标轴
        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=7,
            y_length=6,
            axis_config={"color": self.COLOR_AXIS, "stroke_width": 2},
            tips=False
        ).move_to(UP * 1.5)
        
        self.play(Create(self.axes), run_time=1.0)
        
        # 焦点F
        focus_dot = Dot(self.F, color=self.COLOR_FOCUS, radius=0.12)
        focus_label = Text("F", font="PingFang SC", 
                          font_size=self.FONT_LABEL, 
                          color=self.COLOR_FOCUS).next_to(focus_dot, DOWN, buff=0.1)
        focus_label_detail = Text("焦点", font="PingFang SC",
                                  font_size=self.FONT_SMALL,
                                  color=self.COLOR_FOCUS).next_to(focus_label, DOWN, buff=0.05)
        
        self.play(FadeIn(focus_dot, scale=0.5), run_time=0.3)
        self.play(Flash(focus_dot, color=self.COLOR_FOCUS, flash_radius=0.3), run_time=0.3)
        self.play(FadeIn(focus_label), FadeIn(focus_label_detail), run_time=0.3)
        
        # 准线
        directrix_start = self.axes.c2p(self.directrix_x/self.SCALE, self.y_range[0])
        directrix_end = self.axes.c2p(self.directrix_x/self.SCALE, self.y_range[1])
        directrix = DashedLine(directrix_start, directrix_end,
                              color=self.COLOR_DIRECTRIX,
                              dash_length=0.1,
                              stroke_width=3)
        directrix_label = Text("准线", font="PingFang SC",
                              font_size=self.FONT_SMALL,
                              color=self.COLOR_DIRECTRIX).next_to(directrix, LEFT, buff=0.2).shift(UP*2)
        
        self.play(Create(directrix), FadeIn(directrix_label), run_time=0.8)
        
        # 定义文字
        definition = Text(
            "到焦点F的距离 = 到准线的距离",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(Write(definition), run_time=1.0)
        
        # 绘制抛物线（动态生成）
        # 上半支
        parabola_upper = self.axes.plot(
            lambda x: self.parabola_function(x),
            x_range=[0, 4, 0.1],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        # 下半支
        parabola_lower = self.axes.plot(
            lambda x: -self.parabola_function(x),
            x_range=[0, 4, 0.1],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        self.play(
            Create(parabola_upper),
            Create(parabola_lower),
            run_time=2.5
        )
        
        # 标准方程
        equation = MathTex(r"y^2 = 2px", font_size=40, color=self.COLOR_HIGHLIGHT)
        equation.move_to(DOWN * 4.5)
        
        self.play(Write(equation), run_time=0.8)
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(focus_label_detail),
            FadeOut(directrix_label),
            run_time=0.4
        )
        
        # 方程移至顶部
        equation.generate_target()
        equation.target.scale(0.7).move_to(UP * 5.5)
        self.play(MoveToTarget(equation), run_time=0.4)
        
        # 保留元素
        self.parabola = VGroup(parabola_upper, parabola_lower)
        self.focus_dot = focus_dot
        self.focus_label = focus_label
        self.directrix = directrix
        self.equation = equation
    
    def scene_3_properties(self):
        """场景3: 几何性质 - 范围与对称性 (11-18秒)"""
        # 标题
        title = Text(
            "范围与对称性",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 范围说明
        range_text = MathTex(
            r"x \geq 0, \quad y \in \mathbb{R}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(range_text), run_time=0.6)
        
        # x≥0 区域高亮
        x_min_screen = self.axes.c2p(0, self.y_range[0])
        x_max_screen = self.axes.c2p(self.x_range[1], self.y_range[1])
        region = Rectangle(
            width=x_max_screen[0] - x_min_screen[0],
            height=x_max_screen[1] - x_min_screen[1],
            stroke_width=0,
            fill_color=self.COLOR_PARABOLA,
            fill_opacity=0.15
        ).move_to((x_min_screen + x_max_screen) / 2)
        
        self.play(FadeIn(region), run_time=0.8)
        
        # 对称性标题
        symmetry_title = Text(
            "关于x轴对称",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeOut(range_text), FadeIn(symmetry_title), run_time=0.5)
        
        # 选取对称点
        x_sym = 2.0
        P1_pos = self.parabola_point(self.axes.c2p(x_sym, 0)[0])
        P2_pos = np.array([P1_pos[0], 2*self.OFFSET[1] - P1_pos[1], 0])
        
        P1_dot = Dot(P1_pos, color=YELLOW, radius=0.08)
        P2_dot = Dot(P2_pos, color=YELLOW, radius=0.08)
        
        P1_label = MathTex(r"P_1", font_size=self.FONT_LABEL, color=YELLOW).next_to(P1_dot, UR, buff=0.1)
        P2_label = MathTex(r"P_2", font_size=self.FONT_LABEL, color=YELLOW).next_to(P2_dot, DR, buff=0.1)
        
        self.play(FadeIn(P1_dot), FadeIn(P1_label), run_time=0.3)
        self.play(TransformFromCopy(P1_dot, P2_dot), TransformFromCopy(P1_label, P2_label), run_time=0.8)
        
        # 连线
        symmetric_line = Line(P1_pos, P2_pos, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(symmetric_line), run_time=0.5)
        
        # x轴高亮
        x_axis_highlight = self.axes.get_x_axis().copy().set_color(YELLOW).set_stroke(width=4)
        self.play(ShowPassingFlash(x_axis_highlight, time_width=0.8), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(region),
            FadeOut(symmetry_title),
            FadeOut(P1_dot),
            FadeOut(P2_dot),
            FadeOut(P1_label),
            FadeOut(P2_label),
            FadeOut(symmetric_line),
            run_time=0.5
        )
    
    def scene_4_eccentricity(self):
        """场景4: 离心率 e=1 (18-24秒)"""
        # 标题
        title = Text(
            "离心率",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"e = \frac{|PF|}{d}",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 选取点P
        x_p = 2.0
        P_pos = self.parabola_point(self.axes.c2p(x_p, 0)[0])
        P_dot = Dot(P_pos, color=YELLOW, radius=0.1)
        P_label = MathTex(r"P", font_size=self.FONT_LABEL, color=YELLOW).next_to(P_dot, UR, buff=0.1)
        
        self.play(FadeIn(P_dot), FadeIn(P_label), run_time=0.3)
        
        # 画 |PF|
        line_PF = Line(P_pos, self.F, color=self.COLOR_FOCUS, stroke_width=3)
        PF_label = MathTex(r"|PF|", font_size=self.FONT_SMALL, color=self.COLOR_FOCUS).next_to(
            (P_pos + self.F)/2, RIGHT, buff=0.1)
        
        self.play(Create(line_PF), FadeIn(PF_label), run_time=0.6)
        
        # 画 d (到准线的垂线)
        foot_on_directrix = np.array([self.directrix_x, P_pos[1], 0])
        perpendicular = DashedLine(P_pos, foot_on_directrix, 
                                   color=self.COLOR_DIRECTRIX, 
                                   dash_length=0.08,
                                   stroke_width=3)
        d_label = MathTex(r"d", font_size=self.FONT_SMALL, color=self.COLOR_DIRECTRIX).next_to(
            (P_pos + foot_on_directrix)/2, UP, buff=0.1)
        
        self.play(Create(perpendicular), FadeIn(d_label), run_time=0.6)
        
        # 计算结果
        calculation = MathTex(
            r"e = 1",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)
        
        self.play(Write(calculation), run_time=1.0)
        self.play(Indicate(calculation, scale_factor=1.2), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(line_PF),
            FadeOut(PF_label),
            FadeOut(perpendicular),
            FadeOut(d_label),
            FadeOut(calculation),
            run_time=0.5
        )
    
    def scene_5_latus_rectum(self):
        """场景5: 通径 (24-32秒)"""
        # 标题
        title = Text(
            "通径",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CHORD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 定义
        definition = Text(
            "过焦点且垂直于对称轴的弦",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(definition), run_time=0.6)
        
        # 创建焦点点（如果不存在）
        focus_dot = getattr(self, 'focus_dot', None)
        if focus_dot is None:
            focus_dot = Dot(self.F, color=self.COLOR_FOCUS, radius=0.12)
        
        # 焦点闪烁
        self.play(Flash(focus_dot, color=self.COLOR_FOCUS, flash_radius=0.4), run_time=0.4)
        
        # 画通径AB
        chord_AB = Line(self.A_latus, self.B_latus, 
                       color=self.COLOR_CHORD, 
                       stroke_width=5)
        
        self.play(Create(chord_AB), run_time=1.0)
        
        # 端点
        A_dot = Dot(self.A_latus, color=self.COLOR_CHORD, radius=0.08)
        B_dot = Dot(self.B_latus, color=self.COLOR_CHORD, radius=0.08)
        
        A_label = MathTex(r"A", font_size=20, color=self.COLOR_CHORD).next_to(A_dot, RIGHT, buff=0.1)
        B_label = MathTex(r"B", font_size=20, color=self.COLOR_CHORD).next_to(B_dot, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(A_dot), FadeIn(B_dot),
            FadeIn(A_label), FadeIn(B_label),
            run_time=0.4
        )
        
        # 标注长度
        brace = Brace(chord_AB, direction=RIGHT, buff=0.1, color=YELLOW)
        length_label = MathTex(r"2p", font_size=22, color=YELLOW).next_to(brace, RIGHT, buff=0.1)
        
        self.play(
            GrowFromCenter(brace),
            Write(length_label),
            run_time=1.0
        )
        
        # 公式框 - 修复：使用 Text 来显示中文
        formula_box = VGroup(
            Text("通径", font="PingFang SC", font_size=28, color=WHITE),
            MathTex(r"= 2p", font_size=32, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5)
        
        self.play(FadeIn(formula_box), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(chord_AB),
            FadeOut(A_dot),
            FadeOut(B_dot),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(brace),
            FadeOut(length_label),
            FadeOut(formula_box),
            run_time=0.5
        )
    
    def scene_6_focal_radius(self):
        """场景6: 焦半径公式 (32-41秒)"""
        # 标题
        title = Text(
            "焦半径公式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 选取点P
        x_p = 3.0
        P_pos = self.parabola_point(self.axes.c2p(x_p, 0)[0])
        P_dot = Dot(P_pos, color=YELLOW, radius=0.1)
        
        # 计算实际坐标用于标注
        x_real = (P_pos[0] - self.OFFSET[0]) / self.SCALE
        y_real = (P_pos[1] - self.OFFSET[1]) / self.SCALE
        
        P_label = MathTex(r"P(x_0, y_0)", font_size=self.FONT_LABEL, color=YELLOW).next_to(P_dot, UR, buff=0.1)
        
        self.play(FadeIn(P_dot), FadeIn(P_label), run_time=0.5)
        
        # 画 |PF|
        line_PF = Line(P_pos, self.F, color=self.COLOR_FOCUS, stroke_width=4)
        self.play(Create(line_PF), run_time=0.6)
        
        # 回顾 e=1
        recall = Text(
            "因为 e = 1",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(recall), run_time=0.7)
        
        # 所以 |PF| = d
        step1 = MathTex(
            r"|PF| = d",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.3)
        
        self.play(Write(step1), run_time=0.8)
        
        # 画到准线的距离
        foot_directrix = np.array([self.directrix_x, P_pos[1], 0])
        perpendicular = DashedLine(P_pos, foot_directrix,
                                   color=self.COLOR_AUXILIARY,
                                   dash_length=0.08,
                                   stroke_width=2)
        
        self.play(Create(perpendicular), run_time=0.6)
        
        # d = x₀ + p/2
        step2 = MathTex(
            r"d = x_0 + \frac{p}{2}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 5.1)
        
        self.play(Write(step2), run_time=0.8)
        
        # 推导框
        derivation_box = SurroundingRectangle(
            VGroup(step1, step2),
            color=self.COLOR_HIGHLIGHT,
            buff=0.2
        )
        self.play(Create(derivation_box), run_time=0.5)
        
        # 结论
        conclusion = MathTex(
            r"|PF| = x_0 + \frac{p}{2}",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.2)
        
        self.play(Write(conclusion), run_time=1.0)
        self.play(Indicate(conclusion, scale_factor=1.15), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(line_PF),
            FadeOut(recall),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(perpendicular),
            FadeOut(derivation_box),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def scene_7_optics(self):
        """场景7: 光学性质 (41-54秒)"""
        # 标题
        title = Text(
            "光学反射性质",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_LIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "平行于轴的光线, 反射后都通过焦点",
            font="PingFang SC",
            font_size=self.FONT_BODY - 2,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.7)
        
        # 选取3个点进行演示
        test_points = [
            (1.5, "浅"),
            (2.5, "中"),
            (3.5, "深"),
        ]
        
        rays_group = VGroup()
        
        for x_val, desc in test_points:
            # 点P
            P_pos = self.parabola_point(self.axes.c2p(x_val, 0)[0])
            if P_pos is None:
                continue
            
            P_dot = Dot(P_pos, radius=0.06, color=YELLOW)
            
            # 入射光线（从左侧平行于x轴）
            ray_start = P_pos + LEFT * 2
            incident_ray = Arrow(
                ray_start, P_pos,
                color=self.COLOR_LIGHT,
                stroke_width=3,
                buff=0,
                max_tip_length_to_length_ratio=0.15
            )
            
            # 反射光线（指向焦点）
            reflected_ray = Arrow(
                P_pos, self.F,
                color=self.COLOR_LIGHT,
                stroke_width=3,
                buff=0,
                max_tip_length_to_length_ratio=0.15
            )
            
            # 动画
            self.play(FadeIn(P_dot), run_time=0.2)
            self.play(GrowArrow(incident_ray), run_time=0.6)
            self.play(GrowArrow(reflected_ray), run_time=0.6)
            
            rays_group.add(P_dot, incident_ray, reflected_ray)
            
            # 短暂停顿
            self.wait(0.3)
        
        # 焦点闪烁
        self.play(
            Flash(self.focus_dot, color=self.COLOR_FOCUS, flash_radius=0.5, num_lines=16),
            Indicate(self.focus_dot, scale_factor=1.5),
            run_time=0.6
        )
        
        # 结论
        conclusion = Text(
            "所有反射光线都汇聚于焦点F!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(conclusion), run_time=0.8)
        
        # 应用场景图标
        applications = VGroup(
            # 卫星天线
            VGroup(
                Text("卫星天线", font="PingFang SC", font_size=16, color=WHITE),
                Arc(radius=0.4, start_angle=-PI/3, angle=2*PI/3, color=self.COLOR_PARABOLA, stroke_width=3),
                Dot(ORIGIN, radius=0.05, color=self.COLOR_FOCUS)
            ).arrange(DOWN, buff=0.1),
            
            # 汽车前灯
            VGroup(
                Text("汽车前灯", font="PingFang SC", font_size=16, color=WHITE),
                Arc(radius=0.4, start_angle=-PI/3, angle=2*PI/3, color=self.COLOR_PARABOLA, stroke_width=3).rotate(PI),
                Dot(ORIGIN, radius=0.05, color=self.COLOR_LIGHT)
            ).arrange(DOWN, buff=0.1)
        ).arrange(RIGHT, buff=1.5).move_to(DOWN * 6)
        
        self.play(FadeIn(applications, shift=UP*0.3), run_time=1.0)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(rays_group),
            FadeOut(conclusion),
            FadeOut(applications),
            run_time=0.6
        )
    
    def scene_8_summary(self):
        """场景8: 总结 + 片尾 (54-75秒)"""
        # 抛物线和坐标轴缩小移至顶部
        entire_scene = VGroup(
            self.axes,
            self.parabola,
            self.focus_dot,
            self.focus_label,
            self.directrix
        )
        
        entire_scene.generate_target()
        entire_scene.target.scale(0.5).move_to(UP * 4)
        
        self.play(MoveToTarget(entire_scene), run_time=0.8)
        
        # 知识点卡片
        cards_data = [
            ("范围", r"x \geq 0, \, y \in \mathbb{R}", self.COLOR_PARABOLA),
            ("离心率", r"e = 1 \text{ (定值)}", self.COLOR_HIGHLIGHT),
            ("通径", r"2p", self.COLOR_CHORD),
            ("焦半径", r"|PF| = x_0 + \frac{p}{2}", self.COLOR_FOCUS),
            ("光学性质", r"\text{反射汇聚于焦点}", self.COLOR_LIGHT),
        ]
        
        cards = VGroup()
        y_start = 1.5
        y_step = 0.9
        
        for i, (title_cn, formula_tex, color) in enumerate(cards_data):
            # 使用Text处理中文，MathTex处理公式
            title_text = Text(title_cn, font="PingFang SC", 
                            font_size=22, color=color, weight=BOLD)
            
            # 处理公式中的中文
            if "定值" in formula_tex or "焦点" in formula_tex:
                # 分离中文和数学部分
                if "定值" in formula_tex:
                    formula = VGroup(
                        MathTex(r"e = 1", font_size=20, color=WHITE),
                        Text("(定值)", font="PingFang SC", font_size=16, color=GRAY_A)
                    ).arrange(RIGHT, buff=0.1)
                else:  # 反射汇聚于焦点
                    formula = Text("反射汇聚于焦点", font="PingFang SC", 
                                 font_size=18, color=GRAY_A)
            else:
                formula = MathTex(formula_tex, font_size=20, color=GRAY_A)
            
            card = VGroup(
                Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0),
                title_text,
                formula
            ).arrange(RIGHT, buff=0.25)
            
            card.move_to(np.array([0, y_start - i * y_step, 0]))
            card.shift(LEFT * 10)  # 初始在左侧外
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight_text = Text(
            "掌握抛物线, 轻松解题!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(entire_scene),
            FadeOut(cards),
            FadeOut(highlight_text),
            FadeOut(self.equation),
            run_time=0.5
        )
        
        # ========== 片尾关注 ==========
        # 作者名放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 抛物线装饰动画
        parabola_icons = VGroup(*[
            Arc(radius=0.3, start_angle=-PI/3, angle=2*PI/3, 
                color=self.COLOR_PARABOLA, stroke_width=3)
            .rotate(i * PI/3)
            .shift(2 * np.array([np.cos(i * PI/3), np.sin(i * PI/3), 0]))
            for i in range(6)
        ]).move_to(follow_text.get_center())
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in parabola_icons],
            run_time=0.8
        )
        self.play(Rotate(parabola_icons, angle=PI/3, run_time=2.0))
        
        # 小图标
        mini_icons = VGroup(
            Dot(radius=0.2, color=self.COLOR_FOCUS),
            Dot(radius=0.2, color=self.COLOR_PARABOLA),
            Dot(radius=0.2, color=self.COLOR_CHORD),
            Dot(radius=0.2, color=self.COLOR_LIGHT),
            Dot(radius=0.2, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in mini_icons], run_time=0.8)
        self.wait(2.0)
        
        # 全部淡出 - 过滤兼容的mobjects类型
        if self.mobjects:
            self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)


# 渲染命令:
# manim -pql parabola_properties.py ParabolaProperties  # 快速预览 (低质量)
# manim -qm parabola_properties.py ParabolaProperties   # 中等质量
# manim -qh parabola_properties.py ParabolaProperties   # 高质量 (1080p)
# manim -qk parabola_properties.py ParabolaProperties   # 4K质量