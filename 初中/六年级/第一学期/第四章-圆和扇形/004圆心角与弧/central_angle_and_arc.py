"""
圆心角与弧 - Central Angle and Arc Animation
使用 Manim 创建的小学六年级数学教学视频

内容: 圆心角的定义、弧的定义、圆心角与弧的关系、弧长公式
目标观众: 小学六年级学生
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


class CentralAngleAndArc(Scene):
    """
    圆心角与弧教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出圆心角
    2. 定义圆心角 - 顶点在圆心的角
    3. 定义弧 - 圆心角所对的弧
    4. 关系演示 - 角度与弧长的关系
    5. 弧长公式推导 - l = (n/360) × 2πr
    6. 实例计算 - 巩固知识
    7. 总结与片尾 - 强化记忆
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 主蓝色 - 圆
        self.COLOR_ANGLE = "#e74c3c"        # 红色 - 圆心角
        self.COLOR_ARC = "#f39c12"          # 橙色 - 弧
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮黄色
        self.COLOR_AUXILIARY = GRAY_B       # 辅助灰色
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
        self.COLOR_COMPARISON = "#9b59b6"   # 紫色 - 对比元素
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_define_central_angle()
        self.scene_3_define_arc()
        self.scene_4_relationship()
        self.scene_5_arc_length_formula()
        self.scene_6_example()
        self.scene_7_conclusion()
    
    def setup_geometry(self):
        """初始化圆和角度的几何数据"""
        # 基准参数
        self.center = ORIGIN + UP * 1.5  # 圆心位置
        self.radius = 2.0  # 半径
        
        # 创建主圆
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.center)
        
        # 预设角度（用于演示）
        self.angle_A_deg = 30  # 第一个半径的角度（度）
        self.angle_B_deg = 120  # 第二个半径的角度（度）
        
        # 计算圆周上的点
        angle_A_rad = self.angle_A_deg * DEGREES
        angle_B_rad = self.angle_B_deg * DEGREES
        
        self.point_A = self.center + self.radius * np.array([
            np.cos(angle_A_rad), 
            np.sin(angle_A_rad), 
            0
        ])
        
        self.point_B = self.center + self.radius * np.array([
            np.cos(angle_B_rad), 
            np.sin(angle_B_rad), 
            0
        ])
        
        # 圆心角大小
        self.central_angle_deg = self.angle_B_deg - self.angle_A_deg  # 90度
        
        print(f"✓ 几何初始化完成")
        print(f"  圆心: {self.center}")
        print(f"  半径: {self.radius}")
        print(f"  点A: {self.point_A}")
        print(f"  点B: {self.point_B}")
        print(f"  圆心角: {self.central_angle_deg}°")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "什么是圆心角？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=1.0)
        
        # 圆形从中心生长
        self.play(GrowFromCenter(self.circle), run_time=1.2)
        
        # 圆心点闪烁
        self.center_dot = Dot(
            self.center,
            radius=0.08,
            color=self.COLOR_HIGHLIGHT
        )
        
        self.play(FadeIn(self.center_dot, scale=1.5), run_time=0.5)
        self.play(Flash(self.center_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.4)
        
        # 问号出现
        question_mark = Text(
            "?",
            font_size=70,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.center + RIGHT * 1.2 + UP * 0.8)
        
        self.play(FadeIn(question_mark, scale=1.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(question_mark),
            FadeOut(hook_question),
            run_time=0.5
        )
    
    def scene_2_define_central_angle(self):
        """场景2: 定义圆心角"""
        # 标题
        title = Text(
            "圆心角",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_ANGLE
        ).move_to(UP * 5.8)
        
        # 定义
        definition = Text(
            "顶点在圆心的角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.1)
        
        self.play(
            Write(title),
            FadeIn(definition),
            run_time=0.8
        )
        
        # 绘制半径OA
        radius_OA = Line(
            self.center,
            self.point_A,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        self.play(Create(radius_OA), run_time=0.8)
        
        # 标注点A
        label_A = Text(
            "A",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(self.point_A, UR, buff=0.15)
        
        self.play(FadeIn(label_A), run_time=0.4)
        
        # 绘制半径OB
        radius_OB = Line(
            self.center,
            self.point_B,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        self.play(Create(radius_OB), run_time=0.8)
        
        # 标注点B
        label_B = Text(
            "B",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(self.point_B, UL, buff=0.15)
        
        self.play(FadeIn(label_B), run_time=0.4)
        
        # 标注圆心O
        label_O = Text(
            "O",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(self.center, DOWN, buff=0.2)
        
        self.play(FadeIn(label_O), run_time=0.4)
        
        # 圆心角弧形标记
        angle_arc = Arc(
            radius=0.5,
            start_angle=self.angle_A_deg * DEGREES,
            angle=(self.angle_B_deg - self.angle_A_deg) * DEGREES,
            arc_center=self.center,
            color=self.COLOR_ANGLE,
            stroke_width=4
        )
        
        self.play(Create(angle_arc), run_time=0.8)
        
        # 角度标签
        angle_label = MathTex(
            r"\angle AOB",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(
            self.center + 0.9 * np.array([
                np.cos((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
                np.sin((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
                0
            ])
        )
        
        self.play(FadeIn(angle_label), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "顶点O在圆心",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 保存元素供后续使用
        self.radius_OA = radius_OA
        self.radius_OB = radius_OB
        self.label_A = label_A
        self.label_B = label_B
        self.label_O = label_O
        self.angle_arc = angle_arc
        self.angle_label = angle_label
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explanation),
            run_time=0.5
        )
    
    def scene_3_define_arc(self):
        """场景3: 定义弧"""
        # 标题
        title_arc = Text(
            "弧",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_ARC
        ).move_to(UP * 5.8)
        
        # 定义
        definition_arc = Text(
            "圆心角所对的圆周部分",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.1)
        
        self.play(
            Write(title_arc),
            FadeIn(definition_arc),
            run_time=0.8
        )
        
        # 弧高亮显示
        arc_highlight = Arc(
            radius=self.radius,
            start_angle=self.angle_A_deg * DEGREES,
            angle=(self.angle_B_deg - self.angle_A_deg) * DEGREES,
            arc_center=self.center,
            color=self.COLOR_ARC,
            stroke_width=6
        )
        
        self.play(Create(arc_highlight), run_time=1.5)
        
        # 弧标记符号 "⌒"
        arc_symbol = Text(
            "⌒",
            font_size=32,
            color=self.COLOR_ARC
        ).move_to(
            self.center + (self.radius + 0.5) * np.array([
                np.cos((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
                np.sin((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
                0
            ])
        )
        
        # 弧标签 "AB"
        arc_label_text = Text(
            "AB",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ARC
        ).next_to(arc_symbol, DOWN, buff=0.05)
        
        arc_label_group = VGroup(arc_symbol, arc_label_text)
        
        self.play(FadeIn(arc_label_group), run_time=0.6)
        
        # 箭头指示
        arrow_target = self.center + self.radius * np.array([
            np.cos((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
            np.sin((self.angle_A_deg + self.angle_B_deg) / 2 * DEGREES),
            0
        ])
        
        arrow = Arrow(
            start=DOWN * 3.5 + LEFT * 1.5,
            end=arrow_target,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        hint = Text(
            "这就是弧",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(
            GrowArrow(arrow),
            FadeIn(hint),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 保存元素
        self.arc_highlight = arc_highlight
        self.arc_label_group = arc_label_group
        
        # 清理
        self.play(
            FadeOut(title_arc),
            FadeOut(definition_arc),
            FadeOut(arrow),
            FadeOut(hint),
            run_time=0.5
        )
    
    def scene_4_relationship(self):
        """场景4: 关系演示 - 角度与弧长"""
        # 清理之前的元素
        self.play(
            FadeOut(self.radius_OA),
            FadeOut(self.radius_OB),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_O),
            FadeOut(self.angle_arc),
            FadeOut(self.angle_label),
            FadeOut(self.arc_highlight),
            FadeOut(self.arc_label_group),
            run_time=0.6
        )
        
        # 标题
        title_relationship = Text(
            "圆心角越大，弧越长",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(title_relationship, shift=DOWN * 0.2), run_time=0.6)
        
        # 三个不同大小的圆心角
        angles = [30, 60, 90]  # 度
        colors = [BLUE_C, self.COLOR_ARC, self.COLOR_ANGLE]
        
        # 创建三组圆心角和弧
        angle_arcs = VGroup()
        arc_highlights = VGroup()
        angle_labels = VGroup()
        
        for i, angle in enumerate(angles):
            # 圆心角标记
            angle_arc = Arc(
                radius=0.4 + i * 0.15,
                start_angle=0,
                angle=angle * DEGREES,
                arc_center=self.center,
                color=colors[i],
                stroke_width=3
            )
            angle_arcs.add(angle_arc)
            
            # 对应的弧
            arc_high = Arc(
                radius=self.radius,
                start_angle=0,
                angle=angle * DEGREES,
                arc_center=self.center,
                color=colors[i],
                stroke_width=5
            )
            arc_highlights.add(arc_high)
            
            # 角度标签
            angle_label_text = MathTex(
                f"{angle}^\\circ",
                font_size=22,
                color=colors[i]
            ).move_to(
                self.center + (0.8 + i * 0.2) * np.array([
                    np.cos(angle / 2 * DEGREES),
                    np.sin(angle / 2 * DEGREES),
                    0
                ])
            )
            angle_labels.add(angle_label_text)
        
        # 依次显示
        for i in range(3):
            self.play(
                Create(angle_arcs[i]),
                Create(arc_highlights[i]),
                run_time=0.8
            )
            self.play(FadeIn(angle_labels[i]), run_time=0.3)
            if i < 2:
                self.wait(0.4)
        
        self.wait(1.0)
        
        # 说明文字
        proportion_text = Text(
            "在同圆中，角度与弧长成正比",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(proportion_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title_relationship),
            FadeOut(angle_arcs),
            FadeOut(arc_highlights),
            FadeOut(angle_labels),
            FadeOut(proportion_text),
            run_time=0.6
        )
    
    def scene_5_arc_length_formula(self):
        """场景5: 弧长公式推导"""
        # 标题
        title_formula = Text(
            "弧长公式",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(title_formula, shift=DOWN * 0.2), run_time=0.6)
        
        # Step 1: 圆周长公式
        c_text = Text("圆周长", font="PingFang SC", font_size=26)
        eq1 = MathTex("=", font_size=26)
        formula_c = MathTex("2\\pi r", font_size=26, color=self.COLOR_FORMULA)
        
        formula_circumference = VGroup(c_text, eq1, formula_c).arrange(RIGHT, buff=0.15)
        formula_circumference.move_to(UP * 3.5)
        
        self.play(Write(formula_circumference), run_time=1.2)
        
        # 360°标注
        angle_360 = Arc(
            radius=0.6,
            start_angle=0,
            angle=2*PI,
            arc_center=self.center,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        angle_360_label = MathTex(
            "360^\\circ",
            font_size=28,
            color=self.COLOR_AUXILIARY
        ).next_to(angle_360, RIGHT, buff=0.3)
        
        self.play(
            Create(angle_360),
            FadeIn(angle_360_label),
            run_time=0.8
        )
        
        # 说明
        explanation_1 = Text(
            "整圆对应360°",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(explanation_1), run_time=0.5)
        self.wait(1.0)
        
        # n°角度标注
        angle_n_deg = 60
        angle_n = Arc(
            radius=0.6,
            start_angle=0,
            angle=angle_n_deg * DEGREES,
            arc_center=self.center,
            color=self.COLOR_ANGLE,
            stroke_width=4
        )
        
        n_label = MathTex(
            "n^\\circ",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(
            self.center + 1.0 * np.array([
                np.cos(angle_n_deg / 2 * DEGREES),
                np.sin(angle_n_deg / 2 * DEGREES),
                0
            ])
        )
        
        self.play(
            FadeOut(angle_360),
            FadeOut(angle_360_label),
            FadeOut(explanation_1),
            Create(angle_n),
            FadeIn(n_label),
            run_time=0.8
        )
        
        # Step 2: 比例关系
        arc_len_text = Text("弧长", font="PingFang SC", font_size=24)
        div1 = MathTex("/", font_size=24)
        circum_text = Text("圆周长", font="PingFang SC", font_size=24)
        eq2 = MathTex("=", font_size=24)
        n_text = MathTex("n", font_size=24)
        div2 = MathTex("/", font_size=24)
        deg_360 = MathTex("360", font_size=24)
        
        formula_proportion = VGroup(
            arc_len_text, div1, circum_text, eq2, n_text, div2, deg_360
        ).arrange(RIGHT, buff=0.12)
        formula_proportion.move_to(DOWN * 1.5)
        
        self.play(Write(formula_proportion), run_time=1.5)
        self.wait(1.0)
        
        # Step 3: 最终公式
        l_text = Text("弧长", font="PingFang SC", font_size=28)
        eq_final = MathTex("=", font_size=28)
        formula_final_math = MathTex(
            r"\frac{n}{360} \times 2\pi r",
            font_size=32,
            color=self.COLOR_FORMULA
        )
        
        formula_final = VGroup(l_text, eq_final, formula_final_math).arrange(RIGHT, buff=0.15)
        formula_final.move_to(DOWN * 3.5)
        
        self.play(
            FadeOut(formula_proportion),
            Write(formula_final),
            run_time=1.2
        )
        
        # 公式高亮
        self.play(
            formula_final.animate.scale(1.2).set_color(YELLOW),
            run_time=0.6
        )
        
        self.play(
            Flash(formula_final, color=YELLOW, flash_radius=1.0),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 保存公式
        self.formula_final = formula_final
        
        # 清理其他元素
        self.play(
            FadeOut(title_formula),
            FadeOut(formula_circumference),
            FadeOut(angle_n),
            FadeOut(n_label),
            run_time=0.6
        )
    
    def scene_6_example(self):
        """场景6: 实例计算"""
        # 公式移至顶部
        self.play(
            self.formula_final.animate.move_to(UP * 6).scale(0.6),
            run_time=0.8
        )
        
        # 例题标题
        example_title = Text(
            "例题",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 题目条件
        problem_line1 = Text(
            "已知: r = 3, n = 60°",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4)
        
        problem_line2 = Text(
            "求: 弧长",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 3.4)
        
        self.play(
            Write(problem_line1),
            Write(problem_line2),
            run_time=1.0
        )
        
        # 示意图
        example_radius = 1.2
        example_center = UP * 1.2
        
        example_circle = Circle(
            radius=example_radius,
            color=self.COLOR_PRIMARY,
            stroke_width=2
        ).move_to(example_center)
        
        example_arc = Arc(
            radius=example_radius,
            start_angle=0,
            angle=60 * DEGREES,
            arc_center=example_center,
            color=self.COLOR_ARC,
            stroke_width=4
        )
        
        self.play(
            Create(example_circle),
            Create(example_arc),
            run_time=1.0
        )
        
        # 标注
        r_label = MathTex(
            "r=3",
            font_size=22,
            color=WHITE
        ).move_to(example_center + RIGHT * 0.6)
        
        angle_label_60 = MathTex(
            "60^\\circ",
            font_size=22,
            color=self.COLOR_ANGLE
        ).move_to(example_center + 0.6 * np.array([np.cos(30*DEGREES), np.sin(30*DEGREES), 0]))
        
        self.play(
            FadeIn(r_label),
            FadeIn(angle_label_60),
            run_time=0.6
        )
        
        # 计算步骤
        solution_text = Text("解:", font="PingFang SC", font_size=24, color=GRAY_A)
        solution_text.move_to(DOWN * 1.3 + LEFT * 3.5)
        self.play(FadeIn(solution_text), run_time=0.3)
        
        # 步骤1
        step1_l = MathTex("l", font_size=24)
        step1_eq = MathTex("=", font_size=24)
        step1_formula = MathTex(r"\frac{60}{360} \times 2\pi \times 3", font_size=24)
        
        step_1 = VGroup(step1_l, step1_eq, step1_formula).arrange(RIGHT, buff=0.12)
        step_1.move_to(DOWN * 2.0)
        
        self.play(Write(step_1), run_time=1.2)
        
        # 步骤2
        step2_eq = MathTex("=", font_size=24)
        step2_simplify = MathTex(r"\frac{1}{6} \times 6\pi", font_size=24)
        
        step_2 = VGroup(step2_eq, step2_simplify).arrange(RIGHT, buff=0.12)
        step_2.next_to(step_1, DOWN, aligned_edge=LEFT, buff=0.3)
        step_2.shift(RIGHT * 0.5)
        
        self.play(Write(step_2), run_time=1.0)
        
        # 答案
        answer_eq = MathTex("=", font_size=28)
        answer_value = MathTex(r"\pi", font_size=32, color=self.COLOR_FORMULA)
        
        answer = VGroup(answer_eq, answer_value).arrange(RIGHT, buff=0.12)
        answer.next_to(step_2, DOWN, aligned_edge=LEFT, buff=0.3)
        answer.shift(RIGHT * 0.5)
        
        self.play(Write(answer), run_time=0.8)
        
        # 答案高亮
        self.play(
            answer.animate.set_color(YELLOW).scale(1.2),
            run_time=0.6
        )
        
        # 答案框
        answer_box = SurroundingRectangle(
            answer,
            color=YELLOW,
            buff=0.2,
            stroke_width=3
        )
        
        self.play(Create(answer_box), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(problem_line1),
            FadeOut(problem_line2),
            FadeOut(example_circle),
            FadeOut(example_arc),
            FadeOut(r_label),
            FadeOut(angle_label_60),
            FadeOut(solution_text),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(answer),
            FadeOut(answer_box),
            FadeOut(self.formula_final),
            FadeOut(self.circle),
            FadeOut(self.center_dot),
            run_time=0.6
        )
    
    def scene_7_conclusion(self):
        """场景7: 总结与片尾"""
        # 知识点卡片
        card_1 = self.create_knowledge_card(
            "圆心角: 顶点在圆心的角",
            UP * 3
        )
        
        card_2 = self.create_knowledge_card(
            "弧: 圆心角对应的圆周部分",
            UP * 1.8
        )
        
        card_3 = self.create_knowledge_card(
            "角度越大 → 弧越长",
            UP * 0.6
        )
        
        # 公式卡片
        formula_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_FORMULA,
            fill_opacity=1,
            stroke_width=0
        )
        
        formula_label = Text(
            "弧长公式",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        formula_math = MathTex(
            r"l = \frac{n}{360} \times 2\pi r",
            font_size=24,
            color=self.COLOR_FORMULA
        )
        
        formula_card = VGroup(formula_icon, formula_label, formula_math).arrange(RIGHT, buff=0.25)
        formula_card.move_to(DOWN * 0.8)
        
        # 依次显示卡片
        self.play(FadeIn(card_1, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(card_2, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(card_3, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(formula_card, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(formula_card),
            run_time=0.6
        )
        
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_big),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        decorative_circles = VGroup(*[
            Circle(
                radius=0.25,
                color=self.COLOR_PRIMARY,
                stroke_width=3
            ).move_to(
                follow_text.get_center() + 1.8 * np.array([
                    np.cos(i * PI / 3),
                    np.sin(i * PI / 3),
                    0
                ])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in decorative_circles],
            run_time=0.6
        )
        
        self.play(Rotate(decorative_circles, angle=PI, run_time=1.5))
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorative_circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, text, position):
        """创建知识点卡片"""
        # 图标
        icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 文字
        content = Text(
            text,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, content).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql central_angle_and_arc.py CentralAngleAndArc  # 快速预览
# manim -qh central_angle_and_arc.py CentralAngleAndArc   # 高质量渲染