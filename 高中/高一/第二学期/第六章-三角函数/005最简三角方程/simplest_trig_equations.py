"""
最简三角方程 - Manim 教学动画
The Simplest Trigonometric Equations

内容: sin x = a, cos x = a, tan x = a 的通解
目标观众: 高一学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场钩子
2. sin x = a 图解
3. sin x = a 通解公式
4. cos x = a 展示
5. tan x = a 展示
6. 特殊值汇总
7. 片尾关注
"""

from manim import *
import numpy as np

# ===== 全局配置 - TikTok竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 品牌信息 =====
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "Noto Sans CJK SC"

# ===== 配色方案 =====
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主函数曲线
COLOR_SECONDARY = "#e74c3c"    # 红色 - 辅助线/交点
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式

# ===== 字体大小 =====
FONT_SIZE_TITLE = 36
FONT_SIZE_SUBTITLE = 28
FONT_SIZE_BODY = 22
FONT_SIZE_FORMULA = 28
FONT_SIZE_LABEL = 20
FONT_SIZE_SMALL = 18


class SimplestTrigEquations(Scene):
    """最简三角方程教学动画主场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 作者信息（全程显示）
        self.author_info = Text(
            f"{AUTHOR_NAME} {AUTHOR_ID}",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_LABEL,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.add(self.author_info)
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_sin_graph()
        self.scene_3_sin_formula()
        self.scene_4_cos_equation()
        self.scene_5_tan_equation()
        self.scene_6_special_values()
        self.scene_7_outro()
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 钩子问题
        hook_text = Text(
            "如何解 sin x = 1/2?",
            font=AUTHOR_FONT,
            font_size=42,
            color=WHITE
        ).move_to(UP * 3)
        
        # 副标题
        subtitle = Text(
            "答案有无数个！",
            font=AUTHOR_FONT,
            font_size=32,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        # 动画
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(subtitle, scale=1.2), run_time=0.5)
        self.play(Flash(subtitle, color=COLOR_HIGHLIGHT, flash_radius=1.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def scene_2_sin_graph(self):
        """场景2: sin x = a 图解 (12-15秒)"""
        # 创建坐标轴（缩放到适应竖屏）
        self.axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=6,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
            },
            tips=False
        ).move_to(UP * 1.5)
        
        # 添加x轴标签
        x_labels = VGroup()
        x_positions = [-2*PI, -PI, 0, PI, 2*PI]
        x_labels_text = [r"-2\pi", r"-\pi", r"0", r"\pi", r"2\pi"]
        
        for pos, label_text in zip(x_positions, x_labels_text):
            label = MathTex(label_text, font_size=FONT_SIZE_SMALL, color=GRAY_B)
            label.next_to(self.axes.c2p(pos, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        # y轴标签
        y_labels = VGroup()
        for y_val in [-1, 0, 1]:
            label = MathTex(str(y_val), font_size=FONT_SIZE_SMALL, color=GRAY_B)
            label.next_to(self.axes.c2p(0, y_val), LEFT, buff=0.2)
            y_labels.add(label)
        
        # 标题
        title = VGroup(
            Text("正弦方程:", font=AUTHOR_FONT, font_size=FONT_SIZE_SUBTITLE, color=WHITE),
            MathTex(r"\sin x = \frac{1}{2}", font_size=FONT_SIZE_FORMULA, color=COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 6)
        
        # 创建sin曲线
        self.sin_graph = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[-2*PI, 2*PI],
            color=COLOR_PRIMARY,
            stroke_width=3
        )
        
        # 水平线 y = 1/2
        a_value = 0.5
        h_line = DashedLine(
            self.axes.c2p(-2*PI, a_value),
            self.axes.c2p(2*PI, a_value),
            color=COLOR_SECONDARY,
            stroke_width=2,
            dash_length=0.1
        )
        
        h_line_label = MathTex(
            r"y = \frac{1}{2}",
            font_size=FONT_SIZE_BODY,
            color=COLOR_SECONDARY
        ).next_to(self.axes.c2p(2*PI, a_value), RIGHT, buff=0.2)
        
        # 计算交点
        # sin x = 1/2 的解: x = π/6, 5π/6, π/6+2π, 5π/6+2π, ...
        x_solutions = [
            PI/6,
            5*PI/6,
            PI/6 + 2*PI,
            5*PI/6 + 2*PI,
        ]
        
        # 在[-2π, 2π]范围内的所有解
        all_solutions = []
        for k in range(-1, 2):
            all_solutions.append(PI/6 + 2*k*PI)
            all_solutions.append(5*PI/6 + 2*k*PI)
        
        # 过滤在范围内的解
        visible_solutions = [x for x in all_solutions if -2*PI <= x <= 2*PI]
        
        # 创建交点
        intersection_dots = VGroup()
        intersection_labels = VGroup()
        
        for i, x_val in enumerate(visible_solutions[:5]):  # 只显示5个点避免拥挤
            dot = Dot(
                self.axes.c2p(x_val, a_value),
                color=COLOR_HIGHLIGHT,
                radius=0.08
            )
            intersection_dots.add(dot)
        
        # 动画序列
        self.play(Create(self.axes), Write(x_labels), Write(y_labels), run_time=1.0)
        self.play(Write(title), run_time=0.6)
        self.play(Create(self.sin_graph), run_time=1.5)
        self.wait(0.3)
        
        self.play(Create(h_line), Write(h_line_label), run_time=0.8)
        self.wait(0.3)
        
        # 逐个标记交点
        for dot in intersection_dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.25)
        
        # 强调周期性
        period_arrow_1 = Arrow(
            self.axes.c2p(PI/6, -1.2),
            self.axes.c2p(PI/6 + 2*PI, -1.2),
            color=COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        period_label = Text(
            "周期 2π",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY,
            color=COLOR_HIGHLIGHT
        ).next_to(period_arrow_1, DOWN, buff=0.2)
        
        self.play(
            GrowArrow(period_arrow_1),
            FadeIn(period_label),
            run_time=1.0
        )
        self.wait(1.5)
        
        # 清理部分元素，保留主要图形
        self.play(
            FadeOut(title),
            FadeOut(h_line_label),
            FadeOut(period_arrow_1),
            FadeOut(period_label),
            FadeOut(intersection_dots),
            run_time=0.6
        )
        
        # 保存元素供后续使用
        self.h_line = h_line
        self.x_labels = x_labels
        self.y_labels = y_labels
    
    def scene_3_sin_formula(self):
        """场景3: sin x = a 通解公式 (10-12秒)"""
        # 标题
        title = Text(
            "通解公式",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_FORMULA
        ).move_to(UP * 6)
        
        # 公式框
        formula_box = Rectangle(
            width=7,
            height=3.5,
            color=COLOR_FORMULA,
            stroke_width=2,
            fill_opacity=0.05
        ).move_to(DOWN * 4.5)
        
        # 通解公式（分步展示）
        formula_1 = MathTex(
            r"x = \arcsin a + 2k\pi",
            font_size=FONT_SIZE_FORMULA,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        or_text = Text(
            "或",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).next_to(formula_1, DOWN, buff=0.3)
        
        formula_2 = MathTex(
            r"x = \pi - \arcsin a + 2k\pi",
            font_size=FONT_SIZE_FORMULA,
            color=WHITE
        ).next_to(or_text, DOWN, buff=0.3)
        
        # 简化形式
        simplified = MathTex(
            r"x = k\pi + (-1)^k \arcsin a",
            font_size=FONT_SIZE_FORMULA + 2,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        # 参数说明
        condition = MathTex(
            r"k \in \mathbb{Z}, \; |a| \leq 1",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).next_to(simplified, DOWN, buff=0.4)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Create(formula_box), run_time=0.5)
        
        self.play(Write(formula_1), run_time=1.0)
        self.wait(0.5)
        
        self.play(FadeIn(or_text), run_time=0.3)
        self.play(Write(formula_2), run_time=1.0)
        self.wait(0.8)
        
        # 展示简化形式
        self.play(
            FadeIn(simplified, shift=UP*0.3),
            formula_1.animate.set_opacity(0.3),
            formula_2.animate.set_opacity(0.3),
            or_text.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        # 强调矩形框
        self.play(
            formula_box.animate.set_stroke(COLOR_HIGHLIGHT, width=4),
            run_time=0.4
        )
        
        self.play(Write(condition), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_box),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(or_text),
            FadeOut(simplified),
            FadeOut(condition),
            FadeOut(self.axes),
            FadeOut(self.sin_graph),
            FadeOut(self.h_line),
            FadeOut(self.x_labels),
            FadeOut(self.y_labels),
            run_time=0.6
        )
    
    def scene_4_cos_equation(self):
        """场景4: cos x = a 快速展示 (8-10秒)"""
        # 标题
        title = VGroup(
            Text("余弦方程:", font=AUTHOR_FONT, font_size=FONT_SIZE_SUBTITLE, color=WHITE),
            MathTex(r"\cos x = \frac{1}{2}", font_size=FONT_SIZE_FORMULA, color=COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 6)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=6,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False
        ).move_to(UP * 1.5)
        
        # cos曲线
        cos_graph = axes.plot(
            lambda x: np.cos(x),
            x_range=[-2*PI, 2*PI],
            color=COLOR_PRIMARY,
            stroke_width=3
        )
        
        # 水平线 y = 1/2
        a_value = 0.5
        h_line = DashedLine(
            axes.c2p(-2*PI, a_value),
            axes.c2p(2*PI, a_value),
            color=COLOR_SECONDARY,
            stroke_width=2,
            dash_length=0.1
        )
        
        # 计算交点: cos x = 1/2, x = ±π/3 + 2kπ
        visible_solutions = [
            -PI/3 - 2*PI,
            PI/3 - 2*PI,
            -PI/3,
            PI/3,
            -PI/3 + 2*PI,
            PI/3 + 2*PI,
        ]
        
        # 过滤范围
        visible_solutions = [x for x in visible_solutions if -2*PI <= x <= 2*PI]
        
        # 创建交点
        intersection_dots = VGroup(*[
            Dot(axes.c2p(x, a_value), color=COLOR_HIGHLIGHT, radius=0.08)
            for x in visible_solutions[:5]
        ])
        
        # 通解公式
        formula = MathTex(
            r"x = \pm \arccos a + 2k\pi",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        formula_box = SurroundingRectangle(
            formula,
            color=COLOR_FORMULA,
            buff=0.3,
            corner_radius=0.1
        )
        
        condition = MathTex(
            r"k \in \mathbb{Z}, \; |a| \leq 1",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).next_to(formula, DOWN, buff=0.3)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(cos_graph), run_time=1.2)
        self.play(Create(h_line), run_time=0.6)
        
        for dot in intersection_dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)
        
        self.play(
            Create(formula_box),
            Write(formula),
            run_time=1.0
        )
        self.play(Write(condition), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(cos_graph),
            FadeOut(h_line),
            FadeOut(intersection_dots),
            FadeOut(formula_box),
            FadeOut(formula),
            FadeOut(condition),
            run_time=0.6
        )
    
    def scene_5_tan_equation(self):
        """场景5: tan x = a 展示 (8-10秒)"""
        # 标题
        title = VGroup(
            Text("正切方程:", font=AUTHOR_FONT, font_size=FONT_SIZE_SUBTITLE, color=WHITE),
            MathTex(r"\tan x = 1", font_size=FONT_SIZE_FORMULA, color=COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 6)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False
        ).move_to(UP * 1.5)
        
        # tan曲线（分段绘制，避免奇点）
        tan_graphs = VGroup()
        
        # 分3段绘制
        segments = [
            (-PI, -PI/2 + 0.3),
            (-PI/2 + 0.3, PI/2 - 0.3),
            (PI/2 + 0.3, PI)
        ]
        
        for x_min, x_max in segments:
            graph = axes.plot(
                lambda x: np.tan(x),
                x_range=[x_min, x_max],
                color=COLOR_PRIMARY,
                stroke_width=3,
                use_smoothing=False
            )
            tan_graphs.add(graph)
        
        # 渐近线
        asymptotes = VGroup(
            DashedLine(
                axes.c2p(-PI/2, -3),
                axes.c2p(-PI/2, 3),
                color=GRAY_B,
                stroke_width=1,
                dash_length=0.08
            ),
            DashedLine(
                axes.c2p(PI/2, -3),
                axes.c2p(PI/2, 3),
                color=GRAY_B,
                stroke_width=1,
                dash_length=0.08
            )
        )
        
        # 水平线 y = 1
        a_value = 1.0
        h_line = DashedLine(
            axes.c2p(-PI, a_value),
            axes.c2p(PI, a_value),
            color=COLOR_SECONDARY,
            stroke_width=2,
            dash_length=0.1
        )
        
        # 交点: tan x = 1, x = π/4 + kπ
        visible_solutions = [
            PI/4 - PI,
            PI/4,
            PI/4 + PI,
        ]
        
        # 过滤范围（实际上都在范围内）
        visible_solutions = [x for x in visible_solutions if -PI <= x <= PI]
        
        # 创建交点
        intersection_dots = VGroup(*[
            Dot(axes.c2p(x, a_value), color=COLOR_HIGHLIGHT, radius=0.08)
            for x in visible_solutions
        ])
        
        # 通解公式
        formula = MathTex(
            r"x = \arctan a + k\pi",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        formula_box = SurroundingRectangle(
            formula,
            color=COLOR_FORMULA,
            buff=0.3,
            corner_radius=0.1
        )
        
        condition = MathTex(
            r"k \in \mathbb{Z}",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).next_to(formula, DOWN, buff=0.3)
        
        # 周期强调
        period_note = Text(
            "周期为 π（注意不是 2π）",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SMALL,
            color=COLOR_HIGHLIGHT
        ).next_to(condition, DOWN, buff=0.3)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(asymptotes), run_time=0.6)
        
        for graph in tan_graphs:
            self.play(Create(graph), run_time=0.4)
        
        self.play(Create(h_line), run_time=0.6)
        
        for dot in intersection_dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.25)
        
        self.play(
            Create(formula_box),
            Write(formula),
            run_time=1.0
        )
        self.play(Write(condition), run_time=0.5)
        self.play(FadeIn(period_note, shift=UP*0.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(tan_graphs),
            FadeOut(asymptotes),
            FadeOut(h_line),
            FadeOut(intersection_dots),
            FadeOut(formula_box),
            FadeOut(formula),
            FadeOut(condition),
            FadeOut(period_note),
            run_time=0.6
        )
    
    def scene_6_special_values(self):
        """场景6: 特殊值汇总 (8-10秒)"""
        # 标题
        title = Text(
            "特殊值速记",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=GOLD
        ).move_to(UP * 6.5)
        
        # 创建卡片
        cards = VGroup()
        
        # 卡片数据
        card_data = [
            (r"\sin x = 0", r"x = k\pi", UP * 3),
            (r"\sin x = 1", r"x = \frac{\pi}{2} + 2k\pi", UP * 1.5),
            (r"\sin x = -1", r"x = -\frac{\pi}{2} + 2k\pi", ORIGIN),
            (r"\cos x = 0", r"x = \frac{\pi}{2} + k\pi", DOWN * 1.5),
            (r"\cos x = 1", r"x = 2k\pi", DOWN * 3),
            (r"\cos x = -1", r"x = \pi + 2k\pi", DOWN * 4.5),
        ]
        
        for equation, solution, position in card_data:
            # 方程
            eq = MathTex(equation, font_size=FONT_SIZE_BODY, color=WHITE)
            
            # 箭头
            arrow = MathTex(r"\Rightarrow", font_size=FONT_SIZE_BODY, color=GRAY_A)
            
            # 解
            sol = MathTex(solution, font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
            
            # 组合
            card = VGroup(eq, arrow, sol).arrange(RIGHT, buff=0.3)
            
            # 背景框
            bg = SurroundingRectangle(
                card,
                color=GRAY_B,
                stroke_width=1,
                buff=0.2,
                corner_radius=0.1,
                fill_opacity=0.05
            )
            
            card_with_bg = VGroup(bg, card)
            card_with_bg.move_to(position)
            
            # 初始位置在左侧外
            card_with_bg.shift(LEFT * 10)
            
            cards.add(card_with_bg)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.wait(0.5)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.4
            )
            if i < len(cards) - 1:
                self.wait(0.1)
        
        # 整体强调
        highlight_box = SurroundingRectangle(
            cards,
            color=COLOR_HIGHLIGHT,
            stroke_width=3,
            buff=0.4,
            corner_radius=0.2
        )
        
        self.play(Create(highlight_box), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(highlight_box),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 片尾关注 (6-8秒)"""
        # 作者名放大
        author_name = Text(
            AUTHOR_NAME,
            font=AUTHOR_FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            AUTHOR_ID,
            font=AUTHOR_FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP*0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=AUTHOR_FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP*0.3, scale=1.1), run_time=0.6)
        
        # 三角函数图标装饰
        icons = VGroup(
            MathTex(r"\sin", font_size=36, color="#3498db"),
            MathTex(r"\cos", font_size=36, color="#e74c3c"),
            MathTex(r"\tan", font_size=36, color="#2ecc71")
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        # 旋转动画
        self.play(
            Rotate(icons, angle=PI/6),
            run_time=1.5,
            rate_func=there_and_back
        )
        
        self.wait(0.5)
        
        # 总结文字
        summary = Text(
            "掌握通解，轻松解题！",
            font=AUTHOR_FONT,
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary, shift=UP*0.3), run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            FadeOut(summary),
            run_time=1.0
        )


# ===== 运行说明 =====
"""
渲染命令:

快速预览（低质量）:
manim -pql simplest_trig_equations.py SimplestTrigEquations

中等质量:
manim -qm simplest_trig_equations.py SimplestTrigEquations

高质量（1080p）:
manim -qh simplest_trig_equations.py SimplestTrigEquations

4K质量:
manim -qk simplest_trig_equations.py SimplestTrigEquations

透明背景:
manim -qh -t simplest_trig_equations.py SimplestTrigEquations

GIF格式:
manim -qm --format gif simplest_trig_equations.py SimplestTrigEquations
"""