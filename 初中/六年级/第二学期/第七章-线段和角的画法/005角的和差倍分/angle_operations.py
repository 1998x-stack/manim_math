"""
角的和差倍分 - Angle Sum, Difference, Multiples, and Bisectors
使用 Manim 创建的六年级几何教学视频

内容: 角的加减、倍数关系、角平分线
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


class AngleOperations(Scene):
    """
    角的和差倍分教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 角的和 (∠AOB + ∠BOC = ∠AOC)
    3. 角的差 (∠AOC - ∠BOC = ∠AOB)
    4. 角的倍数关系
    5. 角平分线
    6. 综合应用示例
    7. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"    # 红色
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色
        self.COLOR_AUXILIARY = GRAY_B       # 灰色
        self.COLOR_ANGLE_1 = "#2ecc71"      # 绿色 - 角度1
        self.COLOR_ANGLE_2 = "#f39c12"      # 橙色 - 角度2
        self.COLOR_RESULT = "#9b59b6"       # 紫色 - 结果
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_angle_sum()
        self.scene_3_angle_difference()
        self.scene_4_angle_multiple()
        self.scene_5_angle_bisector()
        self.scene_6_application()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 场景2-3: 角的和与差
        self.O = np.array([0, 1, 0])  # 顶点位置
        
        # 角度定义 (弧度)
        angle_A = 140 * DEGREES
        angle_B = 80 * DEGREES
        angle_C = 20 * DEGREES
        
        # 射线长度
        ray_length = 2.5
        
        # 计算射线端点
        self.A = self.O + ray_length * np.array([np.cos(angle_A), np.sin(angle_A), 0])
        self.B = self.O + ray_length * np.array([np.cos(angle_B), np.sin(angle_B), 0])
        self.C = self.O + ray_length * np.array([np.cos(angle_C), np.sin(angle_C), 0])
        
        # 角度值 (度)
        self.angle_AOB = 60  # 140 - 80
        self.angle_BOC = 60  # 80 - 20
        self.angle_AOC = 120 # 140 - 20
        
        # 场景5-6: 角平分线
        self.O2 = np.array([0, 1, 0])
        
        angle_A2 = 150 * DEGREES
        angle_B2 = 30 * DEGREES
        angle_C2 = 90 * DEGREES  # 平分线
        
        self.A2 = self.O2 + ray_length * np.array([np.cos(angle_A2), np.sin(angle_A2), 0])
        self.B2 = self.O2 + ray_length * np.array([np.cos(angle_B2), np.sin(angle_B2), 0])
        self.C2 = self.O2 + ray_length * np.array([np.cos(angle_C2), np.sin(angle_C2), 0])
        
        self.angle_AOB2 = 120  # 150 - 30
        self.angle_AOC2 = 60   # 150 - 90
        self.angle_COB2 = 60   # 90 - 30
        
        print("✓ 几何数据初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "角可以像数字一样加减吗?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text, run_time=0.8))
        self.wait(0.5)
        
        # 三个角符号快闪
        angle_symbol_1 = self.create_angle_symbol(UP * 1, self.COLOR_ANGLE_1)
        angle_symbol_2 = self.create_angle_symbol(ORIGIN, self.COLOR_ANGLE_2)
        angle_symbol_3 = self.create_angle_symbol(DOWN * 1, self.COLOR_RESULT)
        
        angle_symbols = VGroup(angle_symbol_1, angle_symbol_2, angle_symbol_3)
        
        for symbol in angle_symbols:
            self.play(FadeIn(symbol, scale=0.5), Flash(symbol, color=YELLOW), run_time=0.3)
        
        self.wait(0.5)
        
        # 汇聚到中心
        self.play(
            *[symbol.animate.move_to(ORIGIN) for symbol in angle_symbols],
            run_time=1.0
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(angle_symbols),
            run_time=0.5
        )
    
    def create_angle_symbol(self, position, color):
        """创建角符号装饰"""
        # 简化的角符号: 两条线段 + 弧形
        line1 = Line(ORIGIN, RIGHT * 0.5, color=color, stroke_width=3)
        line2 = Line(ORIGIN, UP * 0.5, color=color, stroke_width=3)
        arc = Arc(radius=0.2, start_angle=0, angle=PI/2, color=color, stroke_width=2)
        
        symbol = VGroup(line1, line2, arc).move_to(position)
        return symbol
    
    def scene_2_angle_sum(self):
        """场景2: 角的和"""
        # 标题
        title = Text(
            "角的和",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title, run_time=0.6))
        
        # 绘制射线OA (绿色)
        ray_OA = Line(self.O, self.A, color=self.COLOR_ANGLE_1, stroke_width=3)
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(self.A, LEFT, buff=0.15)
        
        self.play(Create(ray_OA, run_time=0.5))
        self.play(FadeIn(label_A, scale=0.8), run_time=0.3)
        
        # 绘制射线OC (蓝色)
        ray_OC = Line(self.O, self.C, color=self.COLOR_PRIMARY, stroke_width=3)
        label_C = Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(self.C, RIGHT, buff=0.15)
        
        self.play(Create(ray_OC, run_time=0.5))
        self.play(FadeIn(label_C, scale=0.8), run_time=0.3)
        
        # 顶点O标注
        dot_O = Dot(self.O, radius=0.06, color=WHITE)
        label_O = Text("O", font="PingFang SC", font_size=24, color=WHITE).next_to(self.O, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_O), FadeIn(label_O), run_time=0.3)
        
        # 插入射线OB (橙色)
        ray_OB = Line(self.O, self.B, color=self.COLOR_ANGLE_2, stroke_width=3)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(self.B, UR, buff=0.15)
        
        self.play(Create(ray_OB, run_time=1.0))
        self.play(FadeIn(label_B, scale=0.8), run_time=0.3)
        
        # 标注角AOB (60°) - 绿色
        arc_AOB = Arc(
            radius=0.5,
            start_angle=80 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_1,
            stroke_width=3
        ).move_arc_center_to(self.O)
        
        angle_label_AOB = MathTex(r"60^\circ", font_size=24, color=self.COLOR_ANGLE_1).next_to(
            self.O + 0.8 * np.array([np.cos(110 * DEGREES), np.sin(110 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_AOB, run_time=0.6))
        self.play(FadeIn(angle_label_AOB, scale=0.8), run_time=0.4)
        self.wait(0.5)
        
        # 标注角BOC (60°) - 橙色
        arc_BOC = Arc(
            radius=0.5,
            start_angle=20 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_2,
            stroke_width=3
        ).move_arc_center_to(self.O)
        
        angle_label_BOC = MathTex(r"60^\circ", font_size=24, color=self.COLOR_ANGLE_2).next_to(
            self.O + 0.8 * np.array([np.cos(50 * DEGREES), np.sin(50 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_BOC, run_time=0.6))
        self.play(FadeIn(angle_label_BOC, scale=0.8), run_time=0.4)
        self.wait(0.5)
        
        # 说明文字
        explanation = Text(
            "把两个角拼在一起",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 闪烁强调
        self.play(
            Flash(arc_AOB, color=self.COLOR_ANGLE_1, flash_radius=0.6),
            Flash(arc_BOC, color=self.COLOR_ANGLE_2, flash_radius=0.6),
            run_time=0.6
        )
        
        # 显示角AOC (120°) - 紫色
        arc_AOC = Arc(
            radius=0.6,
            start_angle=20 * DEGREES,
            angle=120 * DEGREES,
            color=self.COLOR_RESULT,
            stroke_width=4
        ).move_arc_center_to(self.O)
        
        angle_label_AOC = MathTex(r"120^\circ", font_size=28, color=self.COLOR_RESULT).next_to(
            self.O + 1.0 * np.array([np.cos(80 * DEGREES), np.sin(80 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_AOC, run_time=1.0))
        self.play(FadeIn(angle_label_AOC, scale=0.8), run_time=0.4)
        self.wait(0.5)
        
        # 公式
        formula = MathTex(
            r"\angle AOB + \angle BOC = \angle AOC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 5)
        
        formula_value = MathTex(
            r"60^\circ + 60^\circ = 120^\circ",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        self.play(Write(formula, run_time=0.8))
        self.play(FadeIn(formula_value, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ray_OA),
            FadeOut(ray_OB),
            FadeOut(ray_OC),
            FadeOut(dot_O),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(label_O),
            FadeOut(arc_AOB),
            FadeOut(arc_BOC),
            FadeOut(arc_AOC),
            FadeOut(angle_label_AOB),
            FadeOut(angle_label_BOC),
            FadeOut(angle_label_AOC),
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(formula_value),
            run_time=0.6
        )
    
    def scene_3_angle_difference(self):
        """场景3: 角的差"""
        # 标题
        title = Text(
            "角的差",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title, run_time=0.6))
        
        # 绘制完整的几何图形
        ray_OA = Line(self.O, self.A, color=self.COLOR_ANGLE_1, stroke_width=3)
        ray_OC = Line(self.O, self.C, color=self.COLOR_PRIMARY, stroke_width=3)
        dot_O = Dot(self.O, radius=0.06, color=WHITE)
        
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(self.A, LEFT, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(self.C, RIGHT, buff=0.15)
        label_O = Text("O", font="PingFang SC", font_size=24, color=WHITE).next_to(self.O, DOWN, buff=0.15)
        
        self.play(
            Create(ray_OA),
            Create(ray_OC),
            FadeIn(dot_O),
            FadeIn(label_A),
            FadeIn(label_C),
            FadeIn(label_O),
            run_time=0.8
        )
        
        # 先显示整个大角AOC (120°)
        arc_AOC = Arc(
            radius=0.6,
            start_angle=20 * DEGREES,
            angle=120 * DEGREES,
            color=self.COLOR_RESULT,
            stroke_width=4
        ).move_arc_center_to(self.O)
        
        angle_label_AOC = MathTex(r"120^\circ", font_size=28, color=self.COLOR_RESULT).next_to(
            self.O + 1.0 * np.array([np.cos(80 * DEGREES), np.sin(80 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_AOC, run_time=1.0))
        self.play(FadeIn(angle_label_AOC, scale=0.8), run_time=0.4)
        self.wait(0.5)
        
        # 说明
        explanation = Text(
            "从大角中拿走一个小角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 添加射线OB
        ray_OB = Line(self.O, self.B, color=self.COLOR_ANGLE_2, stroke_width=3)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(self.B, UR, buff=0.15)
        
        self.play(Create(ray_OB), FadeIn(label_B), run_time=0.6)
        
        # 标注角BOC (要减去的角)
        arc_BOC = Arc(
            radius=0.5,
            start_angle=20 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_2,
            stroke_width=3,
            fill_opacity=0.3,
            fill_color=self.COLOR_ANGLE_2
        ).move_arc_center_to(self.O)
        
        angle_label_BOC = MathTex(r"60^\circ", font_size=24, color=self.COLOR_ANGLE_2).next_to(
            self.O + 0.8 * np.array([np.cos(50 * DEGREES), np.sin(50 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(FadeIn(arc_BOC), FadeIn(angle_label_BOC), run_time=0.6)
        self.wait(0.5)
        
        # 角BOC变淡 (表示减去)
        self.play(arc_BOC.animate.set_opacity(0.2), run_time=0.6)
        
        # 剩余角AOB高亮
        arc_AOB = Arc(
            radius=0.5,
            start_angle=80 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_1,
            stroke_width=4
        ).move_arc_center_to(self.O)
        
        angle_label_AOB = MathTex(r"60^\circ", font_size=28, color=self.COLOR_ANGLE_1).next_to(
            self.O + 0.8 * np.array([np.cos(110 * DEGREES), np.sin(110 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_AOB, run_time=0.8))
        self.play(FadeIn(angle_label_AOB, scale=0.8), Flash(arc_AOB, color=self.COLOR_ANGLE_1), run_time=0.6)
        self.wait(0.5)
        
        # 公式
        formula = MathTex(
            r"\angle AOC - \angle BOC = \angle AOB",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 5)
        
        formula_value = MathTex(
            r"120^\circ - 60^\circ = 60^\circ",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        self.play(Write(formula, run_time=0.8))
        self.play(FadeIn(formula_value, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, ray_OA, ray_OB, ray_OC, dot_O,
                label_A, label_B, label_C, label_O,
                arc_AOB, arc_BOC, arc_AOC,
                angle_label_AOB, angle_label_BOC, angle_label_AOC,
                explanation, formula, formula_value
            )),
            run_time=0.6
        )
    
    def scene_4_angle_multiple(self):
        """场景4: 角的倍数关系"""
        # 标题
        title = Text(
            "角的倍数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title, run_time=0.6))
        
        # 第一个60°角 (蓝色)
        O_left = LEFT * 1.5 + UP * 1
        A_left = O_left + 2 * np.array([np.cos(120 * DEGREES), np.sin(120 * DEGREES), 0])
        B_left = O_left + 2 * np.array([np.cos(60 * DEGREES), np.sin(60 * DEGREES), 0])
        
        ray_1 = Line(O_left, A_left, color=self.COLOR_PRIMARY, stroke_width=3)
        ray_2 = Line(O_left, B_left, color=self.COLOR_PRIMARY, stroke_width=3)
        
        arc_1 = Arc(
            radius=0.5,
            start_angle=60 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_arc_center_to(O_left)
        
        label_1 = MathTex(r"60^\circ", font_size=24, color=self.COLOR_PRIMARY).next_to(
            O_left + 0.8 * np.array([np.cos(90 * DEGREES), np.sin(90 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        angle_1 = VGroup(ray_1, ray_2, arc_1, label_1, Dot(O_left, radius=0.06))
        
        self.play(Create(angle_1), run_time=1.0)
        self.wait(0.5)
        
        # 第二个60°角 (淡蓝色) - 复制到右侧
        O_right = RIGHT * 1.5 + UP * 1
        A_right = O_right + 2 * np.array([np.cos(120 * DEGREES), np.sin(120 * DEGREES), 0])
        B_right = O_right + 2 * np.array([np.cos(60 * DEGREES), np.sin(60 * DEGREES), 0])
        
        ray_3 = Line(O_right, A_right, color=self.COLOR_PRIMARY, stroke_width=3, stroke_opacity=0.6)
        ray_4 = Line(O_right, B_right, color=self.COLOR_PRIMARY, stroke_width=3, stroke_opacity=0.6)
        
        arc_2 = Arc(
            radius=0.5,
            start_angle=60 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            stroke_opacity=0.6
        ).move_arc_center_to(O_right)
        
        label_2 = MathTex(r"60^\circ", font_size=24, color=self.COLOR_PRIMARY, fill_opacity=0.6).next_to(
            O_right + 0.8 * np.array([np.cos(90 * DEGREES), np.sin(90 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        angle_2 = VGroup(ray_3, ray_4, arc_2, label_2, Dot(O_right, radius=0.06, fill_opacity=0.6))
        
        self.play(FadeIn(angle_2, shift=LEFT * 0.5), run_time=0.8)
        self.wait(0.5)
        
        # 说明
        explanation = Text(
            "两个相等的角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 合并成120°的大角
        O_center = UP * 1
        A_center = O_center + 2.5 * np.array([np.cos(150 * DEGREES), np.sin(150 * DEGREES), 0])
        B_center = O_center + 2.5 * np.array([np.cos(30 * DEGREES), np.sin(30 * DEGREES), 0])
        
        ray_big_1 = Line(O_center, A_center, color=self.COLOR_RESULT, stroke_width=4)
        ray_big_2 = Line(O_center, B_center, color=self.COLOR_RESULT, stroke_width=4)
        
        arc_big = Arc(
            radius=0.6,
            start_angle=30 * DEGREES,
            angle=120 * DEGREES,
            color=self.COLOR_RESULT,
            stroke_width=4
        ).move_arc_center_to(O_center)
        
        label_big = MathTex(r"120^\circ", font_size=28, color=self.COLOR_RESULT).next_to(
            O_center + 1.0 * np.array([np.cos(90 * DEGREES), np.sin(90 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        angle_big = VGroup(ray_big_1, ray_big_2, arc_big, label_big, Dot(O_center, radius=0.06))
        
        self.play(
            FadeOut(angle_1),
            FadeOut(angle_2),
            FadeOut(explanation),
            FadeIn(angle_big),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 公式
        formula = MathTex(
            r"\angle AOC = 2 \times \angle AOB",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 5)
        
        formula_value = MathTex(
            r"120^\circ = 2 \times 60^\circ",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        self.play(Write(formula, run_time=0.8))
        self.play(FadeIn(formula_value, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, angle_big, formula, formula_value)),
            run_time=0.6
        )
    
    def scene_5_angle_bisector(self):
        """场景5: 角平分线"""
        # 标题
        title = Text(
            "角平分线",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title, run_time=0.6))
        
        # 绘制角AOB (120°)
        ray_OA = Line(self.O2, self.A2, color=self.COLOR_PRIMARY, stroke_width=3)
        ray_OB = Line(self.O2, self.B2, color=self.COLOR_PRIMARY, stroke_width=3)
        dot_O = Dot(self.O2, radius=0.06, color=WHITE)
        
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(self.A2, LEFT, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(self.B2, RIGHT, buff=0.15)
        label_O = Text("O", font="PingFang SC", font_size=24, color=WHITE).next_to(self.O2, DOWN, buff=0.15)
        
        arc_AOB = Arc(
            radius=0.6,
            start_angle=30 * DEGREES,
            angle=120 * DEGREES,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_arc_center_to(self.O2)
        
        angle_label_AOB = MathTex(r"120^\circ", font_size=28, color=self.COLOR_PRIMARY).next_to(
            self.O2 + 1.0 * np.array([np.cos(90 * DEGREES), np.sin(90 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(
            Create(ray_OA),
            Create(ray_OB),
            FadeIn(dot_O),
            FadeIn(label_A),
            FadeIn(label_B),
            FadeIn(label_O),
            run_time=0.8
        )
        
        self.play(Create(arc_AOB), FadeIn(angle_label_AOB), run_time=0.8)
        self.wait(0.5)
        
        # 说明
        explanation = Text(
            "平分成两个相等的角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 角平分线OC (虚线)
        ray_OC = DashedLine(
            self.O2,
            self.C2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            dash_length=0.1
        )
        label_C = Text("C", font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(self.C2, UP, buff=0.15)
        
        self.play(Create(ray_OC, run_time=1.5))
        self.play(FadeIn(label_C, scale=0.8), run_time=0.3)
        self.wait(0.5)
        
        # 标注∠AOC = 60° (绿色)
        arc_AOC = Arc(
            radius=0.5,
            start_angle=90 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_1,
            stroke_width=3
        ).move_arc_center_to(self.O2)
        
        angle_label_AOC = MathTex(r"60^\circ", font_size=24, color=self.COLOR_ANGLE_1).next_to(
            self.O2 + 0.8 * np.array([np.cos(120 * DEGREES), np.sin(120 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_AOC), FadeIn(angle_label_AOC), run_time=0.6)
        self.wait(0.5)
        
        # 标注∠COB = 60° (橙色)
        arc_COB = Arc(
            radius=0.5,
            start_angle=30 * DEGREES,
            angle=60 * DEGREES,
            color=self.COLOR_ANGLE_2,
            stroke_width=3
        ).move_arc_center_to(self.O2)
        
        angle_label_COB = MathTex(r"60^\circ", font_size=24, color=self.COLOR_ANGLE_2).next_to(
            self.O2 + 0.8 * np.array([np.cos(60 * DEGREES), np.sin(60 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(Create(arc_COB), FadeIn(angle_label_COB), run_time=0.6)
        self.wait(0.5)
        
        # 闪烁强调相等
        self.play(
            Flash(arc_AOC, color=self.COLOR_ANGLE_1, flash_radius=0.6),
            Flash(arc_COB, color=self.COLOR_ANGLE_2, flash_radius=0.6),
            run_time=0.8
        )
        
        # 公式
        formula = MathTex(
            r"\angle AOC = \angle COB = \frac{\angle AOB}{2}",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.2)
        
        formula_value = MathTex(
            r"60^\circ = 60^\circ = \frac{120^\circ}{2}",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeOut(explanation), Write(formula, run_time=0.8))
        self.play(FadeIn(formula_value, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, ray_OA, ray_OB, ray_OC, dot_O,
                label_A, label_B, label_C, label_O,
                arc_AOB, arc_AOC, arc_COB,
                angle_label_AOB, angle_label_AOC, angle_label_COB,
                formula, formula_value
            )),
            run_time=0.6
        )
    
    def scene_6_application(self):
        """场景6: 综合应用示例"""
        # 标题
        title = Text(
            "试一试",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title, run_time=0.6))
        
        # 题目
        problem = VGroup(
            Text("已知:", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"\angle AOC = 90^\circ", font_size=24, color=WHITE),
            MathTex(r"\angle BOC = 35^\circ", font_size=24, color=WHITE),
            Text("求:", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"\angle AOB = \ ?", font_size=24, color=self.COLOR_HIGHLIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 4)
        
        self.play(Write(problem, run_time=1.5))
        self.wait(1.0)
        
        # 绘制对应图形
        O_app = DOWN * 0.5
        A_app = O_app + 2.5 * np.array([np.cos(140 * DEGREES), np.sin(140 * DEGREES), 0])
        B_app = O_app + 2.5 * np.array([np.cos(85 * DEGREES), np.sin(85 * DEGREES), 0])
        C_app = O_app + 2.5 * np.array([np.cos(50 * DEGREES), np.sin(50 * DEGREES), 0])
        
        ray_OA = Line(O_app, A_app, color=self.COLOR_ANGLE_1, stroke_width=3)
        ray_OB = Line(O_app, B_app, color=self.COLOR_ANGLE_2, stroke_width=3)
        ray_OC = Line(O_app, C_app, color=self.COLOR_PRIMARY, stroke_width=3)
        
        label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(A_app, LEFT, buff=0.1)
        label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(B_app, UP, buff=0.1)
        label_C = Text("C", font="PingFang SC", font_size=20, color=WHITE).next_to(C_app, RIGHT, buff=0.1)
        label_O = Text("O", font="PingFang SC", font_size=20, color=WHITE).next_to(O_app, DOWN, buff=0.1)
        
        # 角AOC = 90°
        arc_AOC = Arc(
            radius=0.6,
            start_angle=50 * DEGREES,
            angle=90 * DEGREES,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_arc_center_to(O_app)
        
        label_AOC = MathTex(r"90^\circ", font_size=20, color=self.COLOR_PRIMARY).next_to(
            O_app + 0.9 * np.array([np.cos(95 * DEGREES), np.sin(95 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        # 角BOC = 35°
        arc_BOC = Arc(
            radius=0.4,
            start_angle=50 * DEGREES,
            angle=35 * DEGREES,
            color=self.COLOR_ANGLE_2,
            stroke_width=3
        ).move_arc_center_to(O_app)
        
        label_BOC = MathTex(r"35^\circ", font_size=20, color=self.COLOR_ANGLE_2).next_to(
            O_app + 0.6 * np.array([np.cos(67.5 * DEGREES), np.sin(67.5 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(
            Create(ray_OA),
            Create(ray_OB),
            Create(ray_OC),
            FadeIn(Dot(O_app, radius=0.06)),
            FadeIn(label_A),
            FadeIn(label_B),
            FadeIn(label_C),
            FadeIn(label_O),
            run_time=1.0
        )
        
        self.play(
            Create(arc_AOC),
            FadeIn(label_AOC),
            Create(arc_BOC),
            FadeIn(label_BOC),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 计算过程
        solution = VGroup(
            Text("解:", font="PingFang SC", font_size=22, color=GRAY_A),
            MathTex(r"\angle AOB = \angle AOC - \angle BOC", font_size=22, color=WHITE),
            MathTex(r"= 90^\circ - 35^\circ", font_size=22, color=WHITE),
            MathTex(r"= 55^\circ", font_size=26, color=self.COLOR_HIGHLIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 4.5)
        
        for step in solution:
            self.play(Write(step, run_time=0.6))
            self.wait(0.4)
        
        # 标注答案
        arc_AOB = Arc(
            radius=0.5,
            start_angle=85 * DEGREES,
            angle=55 * DEGREES,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        ).move_arc_center_to(O_app)
        
        label_AOB = MathTex(r"55^\circ", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            O_app + 0.8 * np.array([np.cos(112.5 * DEGREES), np.sin(112.5 * DEGREES), 0]),
            direction=ORIGIN,
            buff=0
        )
        
        self.play(
            Create(arc_AOB),
            FadeIn(label_AOB),
            Flash(arc_AOB, color=self.COLOR_HIGHLIGHT, flash_radius=0.6),
            run_time=1.0
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, problem, solution,
                ray_OA, ray_OB, ray_OC,
                label_A, label_B, label_C, label_O,
                arc_AOC, arc_BOC, arc_AOB,
                label_AOC, label_BOC, label_AOB
            )),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 片尾总结"""
        # 标题
        title = Text(
            "记住这些!",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title, run_time=0.6))
        
        # 四张要点卡片
        cards = VGroup()
        
        card_contents = [
            ("✓ 角的和", "两角拼在一起 (OB在内部)", self.COLOR_ANGLE_1),
            ("✓ 角的差", "大角减去小角", self.COLOR_ANGLE_2),
            ("✓ 角平分线", "平分成两个相等的角", self.COLOR_PRIMARY),
            ("✓ 注意", "度分秒要统一单位!", self.COLOR_HIGHLIGHT)
        ]
        
        for i, (point, detail, color) in enumerate(card_contents):
            point_text = Text(point, font="PingFang SC", font_size=24, color=color)
            detail_text = Text(detail, font="PingFang SC", font_size=18, color=GRAY_A)
            
            card = VGroup(point_text, detail_text).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            card.move_to(UP * (3 - i * 1.5))
            card.shift(LEFT * 10)  # 初始位置在左侧外
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小角符号装饰旋转
        decorations = VGroup(*[
            self.create_angle_symbol(
                follow_text.get_center() + 1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                GOLD
            ).scale(0.6)
            for i in range(6)
        ])
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(title, cards, self.author_info, author_id, follow_text, decorations)),
            run_time=1.0
        )


# 运行命令:
# manim -pql angle_operations.py AngleOperations  # 快速预览
# manim -qh angle_operations.py AngleOperations   # 高质量渲染