"""
点的对称变换 - Point Symmetry Transformations
平面直角坐标系中点关于坐标轴和原点的对称

使用 Manim 创建的七年级数学教学视频
内容: 关于x轴对称、关于y轴对称、关于原点对称
目标观众: 七年级学生
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


class PointSymmetry(Scene):
    """
    点的对称变换教学动画
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系和原点P
    3. 关于x轴对称
    4. 关于y轴对称
    5. 关于原点对称
    6. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 原点P
        self.COLOR_SYMMETRY_X = "#e74c3c"   # 红色 - 关于x轴对称
        self.COLOR_SYMMETRY_Y = "#2ecc71"   # 绿色 - 关于y轴对称
        self.COLOR_SYMMETRY_O = "#f39c12"   # 橙色 - 关于原点对称
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_AXES = WHITE             # 白色 - 坐标轴
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_coordinate_system()
        self.show_symmetry_over_x_axis()
        self.show_symmetry_over_y_axis()
        self.show_symmetry_over_origin()
        self.show_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一管理坐标"""
        
        # ===== 坐标系配置 =====
        self.AXES_SCALE = 0.85
        self.AXES_OFFSET = UP * 1.5
        
        # 坐标系单位长度
        self.UNIT_LENGTH = 0.7
        
        # ===== 创建坐标系 =====
        self.axes = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=self.UNIT_LENGTH * 8,
            y_length=self.UNIT_LENGTH * 8,
            background_line_style={
                "stroke_color": "#2c3e50",
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={
                "stroke_color": self.COLOR_AXES,
                "stroke_width": 2,
                "include_numbers": True,
                "numbers_to_exclude": [0],
                "font_size": 18,
            }
        ).scale(self.AXES_SCALE).shift(self.AXES_OFFSET)
        
        # ===== 原点 =====
        self.origin = self.axes.c2p(0, 0)
        
        # ===== 原始点P及其对称点的逻辑坐标 =====
        # 原点P在第一象限
        self.coord_P = np.array([2, 3, 0])
        self.point_P = self.axes.c2p(2, 3)
        
        # 关于x轴对称：(x, y) → (x, -y)
        self.coord_Px = np.array([2, -3, 0])
        self.point_Px = self.axes.c2p(2, -3)
        
        # 关于y轴对称：(x, y) → (-x, y)
        self.coord_Py = np.array([-2, 3, 0])
        self.point_Py = self.axes.c2p(-2, 3)
        
        # 关于原点对称：(x, y) → (-x, -y)
        self.coord_Po = np.array([-2, -3, 0])
        self.point_Po = self.axes.c2p(-2, -3)
        
        # ===== 垂足（用于x轴和y轴对称）=====
        self.foot_x = self.axes.c2p(2, 0)   # P在x轴上的投影
        self.foot_y = self.axes.c2p(0, 3)   # P在y轴上的投影
        
        # ===== 验证几何关系 =====
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证对称点的正确性"""
        epsilon = 1e-6
        
        # 验证关于x轴对称：P'的x坐标与P相同，y坐标相反
        P_coords = self.axes.p2c(self.point_P)
        Px_coords = self.axes.p2c(self.point_Px)
        
        assert abs(P_coords[0] - Px_coords[0]) < epsilon, "x轴对称: x坐标应相同"
        assert abs(P_coords[1] + Px_coords[1]) < epsilon, "x轴对称: y坐标应互为相反数"
        
        # 验证关于y轴对称：P''的y坐标与P相同，x坐标相反
        Py_coords = self.axes.p2c(self.point_Py)
        
        assert abs(P_coords[0] + Py_coords[0]) < epsilon, "y轴对称: x坐标应互为相反数"
        assert abs(P_coords[1] - Py_coords[1]) < epsilon, "y轴对称: y坐标应相同"
        
        # 验证关于原点对称：P'''的x和y坐标都与P相反
        Po_coords = self.axes.p2c(self.point_Po)
        
        assert abs(P_coords[0] + Po_coords[0]) < epsilon, "原点对称: x坐标应互为相反数"
        assert abs(P_coords[1] + Po_coords[1]) < epsilon, "原点对称: y坐标应互为相反数"
        
        # 验证到对称轴/对称中心的距离
        dist_P_to_x = abs(P_coords[1])
        dist_Px_to_x = abs(Px_coords[1])
        assert abs(dist_P_to_x - dist_Px_to_x) < epsilon, "到x轴距离应相等"
        
        dist_P_to_y = abs(P_coords[0])
        dist_Py_to_y = abs(Py_coords[0])
        assert abs(dist_P_to_y - dist_Py_to_y) < epsilon, "到y轴距离应相等"
        
        dist_P_to_O = np.linalg.norm(self.point_P - self.origin)
        dist_Po_to_O = np.linalg.norm(self.point_Po - self.origin)
        assert abs(dist_P_to_O - dist_Po_to_O) < epsilon, "到原点距离应相等"
        
        # 验证P、O、Po三点共线
        vec_OP = self.point_P - self.origin
        vec_OPo = self.point_Po - self.origin
        cross_product = np.cross(vec_OP[:2], vec_OPo[:2])
        assert abs(cross_product) < epsilon, "P、O、Po应该共线"
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "点的对称\n有什么规律?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 一个点和它的三个"影子"闪烁
        mystery_P = Dot(ORIGIN, color=self.COLOR_PRIMARY, radius=0.12)
        mystery_dots = VGroup(
            Dot(UP * 1.5, color=self.COLOR_SYMMETRY_X, radius=0.10),
            Dot(LEFT * 1.5, color=self.COLOR_SYMMETRY_Y, radius=0.10),
            Dot(DOWN * 1.5 + LEFT * 1.5, color=self.COLOR_SYMMETRY_O, radius=0.10)
        ).shift(DOWN * 0.5)
        
        self.play(FadeIn(mystery_P, scale=0.5), run_time=0.5)
        self.play(Flash(mystery_P, color=self.COLOR_PRIMARY, flash_radius=0.3), run_time=0.4)
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in mystery_dots],
            run_time=0.5
        )
        
        for _ in range(2):
            self.play(
                *[Flash(dot, color=dot.get_color(), flash_radius=0.25) for dot in mystery_dots],
                run_time=0.3
            )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(mystery_P),
            FadeOut(mystery_dots),
            run_time=0.5
        )
    
    def show_coordinate_system(self):
        """场景2: 建立坐标系和原点P (5-6秒)"""
        # 创建坐标轴
        self.play(Create(self.axes), run_time=1.0)
        
        # 原点标记
        self.origin_dot = Dot(self.origin, color=GRAY_A, radius=0.06)
        origin_label = Text("O", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(self.origin_dot, DL, buff=0.12)
        
        self.play(
            FadeIn(self.origin_dot, scale=0.5),
            Write(origin_label),
            run_time=0.5
        )
        
        # 点P出现
        self.dot_P = Dot(self.point_P, color=self.COLOR_PRIMARY, radius=0.12)
        self.label_P = MathTex("P(2, 3)", font_size=24, color=WHITE).next_to(self.dot_P, UR, buff=0.15)
        
        self.play(FadeIn(self.dot_P, scale=0.5), run_time=0.5)
        self.play(Flash(self.dot_P, color=self.COLOR_PRIMARY, flash_radius=0.3), run_time=0.4)
        self.play(Write(self.label_P), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "从这个点开始探索对称",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(explain), FadeOut(origin_label), run_time=0.4)
        
        # 保留坐标轴、原点、P点
        self.origin_label = origin_label  # 保存引用以便后续使用
    
    def show_symmetry_over_x_axis(self):
        """场景3: 关于x轴对称 (12-15秒)"""
        # 标题
        title = Text(
            "关于 x 轴对称",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SYMMETRY_X
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # x轴高亮
        x_axis_highlight = self.axes.x_axis.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke(width=4)
        self.play(Create(x_axis_highlight), run_time=0.5)
        
        # P到x轴的垂线
        perpendicular = DashedLine(
            self.point_P,
            self.foot_x,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(perpendicular), run_time=0.7)
        
        # 垂足闪烁
        foot_dot = Dot(self.foot_x, color=self.COLOR_HIGHLIGHT, radius=0.08)
        self.play(FadeIn(foot_dot, scale=0.5), run_time=0.3)
        self.play(Flash(foot_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.4)
        
        # 对称点P'出现
        dot_Px = Dot(self.point_Px, color=self.COLOR_SYMMETRY_X, radius=0.12)
        label_Px = MathTex("P'(2, -3)", font_size=24, color=self.COLOR_SYMMETRY_X).next_to(dot_Px, DR, buff=0.15)
        
        self.play(FadeIn(dot_Px, scale=0.5), run_time=0.5)
        self.play(Flash(dot_Px, color=self.COLOR_SYMMETRY_X, flash_radius=0.3), run_time=0.4)
        self.play(Write(label_Px), run_time=0.5)
        
        # 连线PP'
        line_PPx = Line(self.point_P, self.point_Px, color=self.COLOR_SYMMETRY_X, stroke_width=2)
        self.play(Create(line_PPx), run_time=0.6)
        
        # 距离标注
        dist_P = abs(self.coord_P[1])
        dist_Px = abs(self.coord_Px[1])
        
        brace_P = Brace(Line(self.point_P, self.foot_x), direction=RIGHT, buff=0.1, color=YELLOW)
        brace_label_P = MathTex(f"{dist_P}", font_size=20, color=YELLOW).next_to(brace_P, RIGHT, buff=0.05)
        
        brace_Px = Brace(Line(self.foot_x, self.point_Px), direction=RIGHT, buff=0.1, color=YELLOW)
        brace_label_Px = MathTex(f"{dist_Px}", font_size=20, color=YELLOW).next_to(brace_Px, RIGHT, buff=0.05)
        
        self.play(
            FadeIn(brace_P),
            FadeIn(brace_label_P),
            FadeIn(brace_Px),
            FadeIn(brace_label_Px),
            run_time=0.8
        )
        
        # 规律公式
        formula = MathTex(
            r"(x, y) \rightarrow (x, -y)",
            font_size=28,
            color=self.COLOR_SYMMETRY_X
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=0.7)
        
        # 重点提示
        highlight = Text(
            "横坐标不变，纵坐标取反",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(x_axis_highlight),
            FadeOut(perpendicular),
            FadeOut(foot_dot),
            FadeOut(line_PPx),
            FadeOut(brace_P),
            FadeOut(brace_label_P),
            FadeOut(brace_Px),
            FadeOut(brace_label_Px),
            FadeOut(formula),
            FadeOut(highlight),
            run_time=0.6
        )
        
        # 保留对称点但变淡
        self.play(
            dot_Px.animate.set_opacity(0.3),
            label_Px.animate.set_opacity(0.3),
            run_time=0.3
        )
        
        # 保存引用
        self.dot_Px = dot_Px
        self.label_Px = label_Px
    
    def show_symmetry_over_y_axis(self):
        """场景4: 关于y轴对称 (12-15秒)"""
        # 标题
        title = Text(
            "关于 y 轴对称",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SYMMETRY_Y
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # y轴高亮
        y_axis_highlight = self.axes.y_axis.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke(width=4)
        self.play(Create(y_axis_highlight), run_time=0.5)
        
        # P到y轴的垂线
        perpendicular = DashedLine(
            self.point_P,
            self.foot_y,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(perpendicular), run_time=0.7)
        
        # 垂足闪烁
        foot_dot = Dot(self.foot_y, color=self.COLOR_HIGHLIGHT, radius=0.08)
        self.play(FadeIn(foot_dot, scale=0.5), run_time=0.3)
        self.play(Flash(foot_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.4)
        
        # 对称点P''出现
        dot_Py = Dot(self.point_Py, color=self.COLOR_SYMMETRY_Y, radius=0.12)
        label_Py = MathTex("P''(-2, 3)", font_size=24, color=self.COLOR_SYMMETRY_Y).next_to(dot_Py, UL, buff=0.15)
        
        self.play(FadeIn(dot_Py, scale=0.5), run_time=0.5)
        self.play(Flash(dot_Py, color=self.COLOR_SYMMETRY_Y, flash_radius=0.3), run_time=0.4)
        self.play(Write(label_Py), run_time=0.5)
        
        # 连线PP''
        line_PPy = Line(self.point_P, self.point_Py, color=self.COLOR_SYMMETRY_Y, stroke_width=2)
        self.play(Create(line_PPy), run_time=0.6)
        
        # 距离标注
        dist_P = abs(self.coord_P[0])
        dist_Py = abs(self.coord_Py[0])
        
        brace_P = Brace(Line(self.point_P, self.foot_y), direction=UP, buff=0.1, color=YELLOW)
        brace_label_P = MathTex(f"{dist_P}", font_size=20, color=YELLOW).next_to(brace_P, UP, buff=0.05)
        
        brace_Py = Brace(Line(self.foot_y, self.point_Py), direction=UP, buff=0.1, color=YELLOW)
        brace_label_Py = MathTex(f"{dist_Py}", font_size=20, color=YELLOW).next_to(brace_Py, UP, buff=0.05)
        
        self.play(
            FadeIn(brace_P),
            FadeIn(brace_label_P),
            FadeIn(brace_Py),
            FadeIn(brace_label_Py),
            run_time=0.8
        )
        
        # 规律公式
        formula = MathTex(
            r"(x, y) \rightarrow (-x, y)",
            font_size=28,
            color=self.COLOR_SYMMETRY_Y
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=0.7)
        
        # 重点提示
        highlight = Text(
            "纵坐标不变，横坐标取反",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(y_axis_highlight),
            FadeOut(perpendicular),
            FadeOut(foot_dot),
            FadeOut(line_PPy),
            FadeOut(brace_P),
            FadeOut(brace_label_P),
            FadeOut(brace_Py),
            FadeOut(brace_label_Py),
            FadeOut(formula),
            FadeOut(highlight),
            run_time=0.6
        )
        
        # 保留对称点但变淡
        self.play(
            dot_Py.animate.set_opacity(0.3),
            label_Py.animate.set_opacity(0.3),
            run_time=0.3
        )
        
        # 保存引用
        self.dot_Py = dot_Py
        self.label_Py = label_Py
    
    def show_symmetry_over_origin(self):
        """场景5: 关于原点对称 (12-15秒)"""
        # 标题
        title = Text(
            "关于原点对称",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SYMMETRY_O
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 原点高亮
        self.play(
            Indicate(self.origin_dot, scale_factor=2.5, color=self.COLOR_HIGHLIGHT),
            run_time=0.7
        )
        
        # 从P画线穿过原点
        line_through_O = DashedLine(
            self.point_P + (self.point_P - self.origin) * 0.2,  # 稍微延伸
            self.origin - (self.point_P - self.origin) * 1.5,   # 延伸到对侧
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(line_through_O), run_time=1.0)
        
        # 在对侧标记对称点位置
        symmetric_marker = Dot(self.point_Po, color=self.COLOR_HIGHLIGHT, radius=0.08)
        self.play(FadeIn(symmetric_marker, scale=0.5), run_time=0.3)
        self.play(Flash(symmetric_marker, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.4)
        
        # 对称点P'''出现
        dot_Po = Dot(self.point_Po, color=self.COLOR_SYMMETRY_O, radius=0.12)
        label_Po = MathTex("P'''(-2, -3)", font_size=24, color=self.COLOR_SYMMETRY_O).next_to(dot_Po, DL, buff=0.15)
        
        self.play(
            Transform(symmetric_marker, dot_Po),
            run_time=0.5
        )
        self.remove(symmetric_marker)
        self.add(dot_Po)
        
        self.play(Flash(dot_Po, color=self.COLOR_SYMMETRY_O, flash_radius=0.3), run_time=0.4)
        self.play(Write(label_Po), run_time=0.5)
        
        # 完整连线（变色强调）
        line_PPo = Line(self.point_P, self.point_Po, color=self.COLOR_SYMMETRY_O, stroke_width=3)
        self.play(
            FadeOut(line_through_O),
            Create(line_PPo),
            run_time=0.7
        )
        
        # 距离标注
        dist_P = np.linalg.norm(self.point_P - self.origin)
        dist_Po = np.linalg.norm(self.point_Po - self.origin)
        
        # 使用弧线标注距离
        arc_P = Arc(
            radius=0.5,
            start_angle=np.arctan2((self.point_P - self.origin)[1], (self.point_P - self.origin)[0]),
            angle=PI/6,
            color=YELLOW
        ).move_arc_center_to(self.origin)
        
        arc_Po = Arc(
            radius=0.5,
            start_angle=np.arctan2((self.point_Po - self.origin)[1], (self.point_Po - self.origin)[0]),
            angle=PI/6,
            color=YELLOW
        ).move_arc_center_to(self.origin)
        
        # 简化：使用文字标注
        dist_label_P = Text("d", font="Noto Sans CJK SC", font_size=20, color=YELLOW).move_to(
            (self.point_P + self.origin) / 2 + UR * 0.3
        )
        dist_label_Po = Text("d", font="Noto Sans CJK SC", font_size=20, color=YELLOW).move_to(
            (self.point_Po + self.origin) / 2 + DL * 0.3
        )
        
        self.play(
            FadeIn(dist_label_P),
            FadeIn(dist_label_Po),
            run_time=0.7
        )
        
        # 规律公式
        formula = MathTex(
            r"(x, y) \rightarrow (-x, -y)",
            font_size=28,
            color=self.COLOR_SYMMETRY_O
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=0.7)
        
        # 重点提示
        highlight = Text(
            "横、纵坐标都取反",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        
        # 三点共线说明
        explain = Text(
            "三点共线且原点平分",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6.3)
        
        self.play(FadeIn(explain, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_PPo),
            FadeOut(dist_label_P),
            FadeOut(dist_label_Po),
            FadeOut(formula),
            FadeOut(highlight),
            FadeOut(explain),
            run_time=0.6
        )
        
        # 保存引用
        self.dot_Po = dot_Po
        self.label_Po = label_Po
    
    def show_summary_and_outro(self):
        """场景6: 总结与关注 (8-10秒)"""
        # 所有点恢复显示
        self.play(
            self.dot_Px.animate.set_opacity(1),
            self.label_Px.animate.set_opacity(1),
            self.dot_Py.animate.set_opacity(1),
            self.label_Py.animate.set_opacity(1),
            run_time=0.5
        )
        
        # 坐标系缩小淡化
        self.play(
            self.axes.animate.scale(0.6).fade(0.7),
            VGroup(
                self.dot_P, self.label_P,
                self.dot_Px, self.label_Px,
                self.dot_Py, self.label_Py,
                self.dot_Po, self.label_Po,
                self.origin_dot
            ).animate.scale(0.6).shift(UP * 0.5),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "对称规律总结",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.5)
        
        # 三条规律
        rule1 = VGroup(
            Text("关于 x 轴:", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SYMMETRY_X),
            MathTex(r"(x, y) \rightarrow (x, -y)", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2)
        
        rule2 = VGroup(
            Text("关于 y 轴:", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SYMMETRY_Y),
            MathTex(r"(x, y) \rightarrow (-x, y)", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1)
        
        rule3 = VGroup(
            Text("关于原点:", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SYMMETRY_O),
            MathTex(r"(x, y) \rightarrow (-x, -y)", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        
        rules = VGroup(rule1, rule2, rule3)
        
        for i, rule in enumerate(rules):
            self.play(FadeIn(rule, shift=RIGHT * 0.5), run_time=0.4)
            if i < len(rules) - 1:
                self.wait(0.3)
        
        # 装饰框
        box = SurroundingRectangle(
            rules,
            color=self.COLOR_PRIMARY,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(box), run_time=0.5)
        self.wait(1.0)
        
        # 作者信息放大
        self.play(
            self.author_info.animate.scale(1.8).move_to(UP * 1).set_color(WHITE),
            FadeOut(summary_title),
            FadeOut(rules),
            FadeOut(box),
            FadeOut(self.axes),
            FadeOut(self.dot_P),
            FadeOut(self.label_P),
            FadeOut(self.dot_Px),
            FadeOut(self.label_Px),
            FadeOut(self.dot_Py),
            FadeOut(self.label_Py),
            FadeOut(self.dot_Po),
            FadeOut(self.label_Po),
            FadeOut(self.origin_dot),
            run_time=0.7
        )
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画 - 四个小点代表四个点
        decorations = VGroup(*[
            Dot(radius=0.10, color=color)
            .move_to(follow_text.get_center() + 1.8 * direction)
            for color, direction in zip(
                [self.COLOR_PRIMARY, self.COLOR_SYMMETRY_X, self.COLOR_SYMMETRY_Y, self.COLOR_SYMMETRY_O],
                [UR, DR, DL, UL]
            )
        ])
        
        self.play(*[FadeIn(dot, scale=0.5) for dot in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_info, follow_text, decorations)),
            run_time=1.0
        )


# ========== 运行命令 ==========
# manim -pql point_symmetry.py PointSymmetry  # 快速预览
# manim -qh point_symmetry.py PointSymmetry   # 高质量 1080p
# manim -qk point_symmetry.py PointSymmetry   # 4K质量