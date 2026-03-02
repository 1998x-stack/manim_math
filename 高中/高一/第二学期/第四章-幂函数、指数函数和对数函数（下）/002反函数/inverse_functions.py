"""
反函数 - Manim 教学动画
Inverse Functions

内容: 反函数定义、图像对称性、性质、单调性条件
目标观众: 高一学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场钩子
2. 反函数定义
3. 图像对称性（核心）
4. 对称性验证
5. 反函数性质
6. 单调性条件
7. 总结与片尾
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
COLOR_PRIMARY = "#3498db"      # 蓝色 - 原函数
COLOR_SECONDARY = "#e74c3c"    # 红色 - 反函数
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 对称轴y=x
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式框
COLOR_SYMMETRIC = "#9b59b6"    # 紫色 - 对称点

# ===== 字体大小 =====
FONT_SIZE_TITLE = 36
FONT_SIZE_SUBTITLE = 28
FONT_SIZE_BODY = 22
FONT_SIZE_FORMULA = 28
FONT_SIZE_LABEL = 20
FONT_SIZE_SMALL = 18


class InverseFunctions(Scene):
    """反函数教学动画主场景"""
    
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
        self.scene_2_definition()
        self.scene_3_symmetry()
        self.scene_4_verification()
        self.scene_5_properties()
        self.scene_6_monotonic()
        self.scene_7_outro()
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 钩子问题
        hook_text = VGroup(
            Text(
                "已知",
                font=AUTHOR_FONT,
                font_size=38,
                color=WHITE
            ),
            MathTex(r"y = 2^x", font_size=40, color=COLOR_PRIMARY),
            Text(
                "如何求 x？",
                font=AUTHOR_FONT,
                font_size=38,
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.4).move_to(UP * 3)
        
        # 答案
        answer = VGroup(
            MathTex(r"x = \log_2 y", font_size=38, color=COLOR_SECONDARY),
            Text(
                "这就是反函数！",
                font=AUTHOR_FONT,
                font_size=36,
                color=COLOR_HIGHLIGHT
            )
        ).arrange(DOWN, buff=0.5).move_to(UP * 0.5)
        
        # 动画
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(answer[0], shift=UP*0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(answer[1], scale=1.2), run_time=0.5)
        self.play(Flash(answer[1], color=COLOR_HIGHLIGHT, flash_radius=1.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(answer),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 反函数定义 (10-12秒)"""
        # 标题
        title = Text(
            "反函数的定义",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 原函数
        original_func = MathTex(
            r"y = f(x)",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        # 双向箭头
        double_arrow = MathTex(
            r"\Updownarrow",
            font_size=48,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        # 反函数形式1
        inverse_func_1 = MathTex(
            r"x = f^{-1}(y)",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_SECONDARY
        ).move_to(UP * 1.5)
        
        # 说明文字
        explanation = Text(
            "x 与 y 互换角色",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 0.3)
        
        # 标准形式
        inverse_func_2 = MathTex(
            r"y = f^{-1}(x)",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_SECONDARY
        ).move_to(DOWN * 2)
        
        standard_label = Text(
            "(标准形式)",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(inverse_func_2, DOWN, buff=0.2)
        
        # 条件说明
        condition = VGroup(
            Text("条件:", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY, color=WHITE),
            Text("一一对应关系", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 4)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Write(original_func), run_time=0.8)
        self.wait(0.2)
        
        # 箭头摆动效果
        self.play(
            FadeIn(double_arrow, shift=DOWN*0.2),
            run_time=0.6
        )
        
        self.play(Write(inverse_func_1), run_time=1.0)
        self.wait(0.3)
        
        self.play(FadeIn(explanation, shift=UP*0.2), run_time=1.2)
        self.wait(0.5)
        
        self.play(
            Write(inverse_func_2),
            FadeIn(standard_label),
            run_time=1.0
        )
        self.wait(0.3)
        
        self.play(FadeIn(condition, shift=UP*0.3), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original_func),
            FadeOut(double_arrow),
            FadeOut(inverse_func_1),
            FadeOut(explanation),
            FadeOut(inverse_func_2),
            FadeOut(standard_label),
            FadeOut(condition),
            run_time=0.6
        )
    
    def scene_3_symmetry(self):
        """场景3: 图像对称性（核心）(12-15秒)"""
        # 标题
        title = Text(
            "图像关于 y=x 对称",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        # 创建坐标轴（适合显示 2^x 和 log_2 x）
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18,
            },
            tips=False
        ).move_to(DOWN * 0.5)
        
        # 对称轴 y=x
        symmetry_line = DashedLine(
            axes.c2p(-1, -1),
            axes.c2p(5, 5),
            color=COLOR_HIGHLIGHT,
            stroke_width=3,
            dash_length=0.1
        )
        
        symmetry_label = MathTex(
            r"y = x",
            font_size=FONT_SIZE_BODY,
            color=COLOR_HIGHLIGHT
        ).next_to(axes.c2p(4, 4), UR, buff=0.2)
        
        # 原函数 y = 2^x
        original_graph = axes.plot(
            lambda x: 2 ** x,
            x_range=[-1, 3],
            color=COLOR_PRIMARY,
            stroke_width=3
        )
        
        original_label = MathTex(
            r"y = 2^x",
            font_size=FONT_SIZE_BODY,
            color=COLOR_PRIMARY
        ).next_to(axes.c2p(2.5, 5), UP, buff=0.1)
        
        # 反函数 y = log_2 x
        inverse_graph = axes.plot(
            lambda x: np.log2(x),
            x_range=[0.3, 5],
            color=COLOR_SECONDARY,
            stroke_width=3
        )
        
        inverse_label = MathTex(
            r"y = \log_2 x",
            font_size=FONT_SIZE_BODY,
            color=COLOR_SECONDARY
        ).next_to(axes.c2p(5, 2.3), RIGHT, buff=0.1)
        
        # 对称点对
        # 点 (1, 2) 在原函数上
        point1 = Dot(axes.c2p(1, 2), color=COLOR_PRIMARY, radius=0.08)
        point1_label = MathTex(r"(1, 2)", font_size=FONT_SIZE_SMALL, color=COLOR_PRIMARY).next_to(point1, UL, buff=0.1)
        
        # 点 (2, 1) 在反函数上
        point2 = Dot(axes.c2p(2, 1), color=COLOR_SECONDARY, radius=0.08)
        point2_label = MathTex(r"(2, 1)", font_size=FONT_SIZE_SMALL, color=COLOR_SECONDARY).next_to(point2, DR, buff=0.1)
        
        # 连线
        connecting_line = DashedLine(
            point1.get_center(),
            point2.get_center(),
            color=COLOR_SYMMETRIC,
            stroke_width=2,
            dash_length=0.08
        )
        
        # 更多对称点对
        symmetric_pairs = [
            (0, 1, 1, 0),
            (2, 4, 4, 2),
        ]
        
        additional_dots = VGroup()
        for x1, y1, x2, y2 in symmetric_pairs:
            dot1 = Dot(axes.c2p(x1, y1), color=COLOR_SYMMETRIC, radius=0.06)
            dot2 = Dot(axes.c2p(x2, y2), color=COLOR_SYMMETRIC, radius=0.06)
            additional_dots.add(dot1, dot2)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Create(axes), run_time=1.0)
        
        # 对称轴
        self.play(
            Create(symmetry_line),
            Write(symmetry_label),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 原函数
        self.play(
            Create(original_graph),
            Write(original_label),
            run_time=1.5
        )
        self.wait(0.3)
        
        # 标记点 (1,2)
        self.play(
            FadeIn(point1, scale=0.5),
            Write(point1_label),
            run_time=0.4
        )
        self.wait(0.2)
        
        # 反射动画：(1,2) → (2,1)
        moving_dot = point1.copy()
        self.add(moving_dot)
        
        self.play(
            Create(connecting_line),
            run_time=0.5
        )
        
        self.play(
            moving_dot.animate.move_to(point2.get_center()),
            run_time=1.0
        )
        
        self.remove(moving_dot)
        self.play(
            FadeIn(point2, scale=0.5),
            Write(point2_label),
            run_time=0.4
        )
        self.wait(0.3)
        
        # 绘制反函数
        self.play(
            Create(inverse_graph),
            Write(inverse_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 显示更多对称点对
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in additional_dots],
            run_time=1.2
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(symmetry_line),
            FadeOut(symmetry_label),
            FadeOut(original_graph),
            FadeOut(original_label),
            FadeOut(inverse_graph),
            FadeOut(inverse_label),
            FadeOut(point1),
            FadeOut(point1_label),
            FadeOut(point2),
            FadeOut(point2_label),
            FadeOut(connecting_line),
            FadeOut(additional_dots),
            run_time=0.6
        )
    
    def scene_4_verification(self):
        """场景4: 对称性验证 (8-10秒)"""
        # 标题
        title = Text(
            "对称验证",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 验证点对
        pairs_data = [
            (r"(0, 1) \Leftrightarrow (1, 0)", UP * 3.5),
            (r"(1, 2) \Leftrightarrow (2, 1)", UP * 2),
            (r"(2, 4) \Leftrightarrow (4, 2)", UP * 0.5),
        ]
        
        pairs = VGroup()
        
        for formula, position in pairs_data:
            pair = MathTex(
                formula,
                font_size=FONT_SIZE_FORMULA,
                color=WHITE
            ).move_to(position)
            
            check_mark = MathTex(
                r"\checkmark",
                font_size=FONT_SIZE_FORMULA,
                color=COLOR_FORMULA
            ).next_to(pair, RIGHT, buff=0.3)
            
            pair_group = VGroup(pair, check_mark)
            pairs.add(pair_group)
        
        # 一般公式
        general_formula_cn = VGroup(
            MathTex(r"(a,\, b)", font_size=FONT_SIZE_BODY + 2, color=WHITE),
            Text("在 f 上", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY + 2, color=WHITE),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 2)
        
        general_formula_cn = Text(
            "若 (a,b) 在 f 上",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY + 2,
            color=WHITE
        ).move_to(DOWN * 2)
        
        arrow_down = MathTex(
            r"\Downarrow",
            font_size=36,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        general_inverse = Text(
            "则 (b,a) 在 f⁻¹ 上",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY + 2,
            color=COLOR_SECONDARY
        ).move_to(DOWN * 4)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        
        # 逐个展示点对
        for pair in pairs:
            self.play(
                Write(pair[0]),
                run_time=0.8
            )
            self.play(
                FadeIn(pair[1], scale=1.2),
                run_time=0.4
            )
            self.wait(0.2)
        
        self.wait(0.5)
        
        # 一般公式
        self.play(Write(general_formula_cn), run_time=1.0)
        self.play(
            FadeIn(arrow_down, shift=DOWN*0.2),
            run_time=0.5
        )
        self.play(Write(general_inverse), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(pairs),
            FadeOut(general_formula_cn),
            FadeOut(arrow_down),
            FadeOut(general_inverse),
            run_time=0.6
        )
    
    def scene_5_properties(self):
        """场景5: 反函数性质 (10-12秒)"""
        # 标题
        title = Text(
            "反函数性质",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 性质卡片
        properties_data = [
            (r"f(f^{-1}(x)) = x", "复合为恒等", UP * 3.5, COLOR_FORMULA),
            (r"f^{-1}(f(x)) = x", "可交换复合", UP * 1.5, COLOR_FORMULA),
            (r"(f^{-1})^{-1} = f", "互为反函数", DOWN * 0.5, COLOR_SECONDARY),
        ]
        
        cards = VGroup()
        
        for i, (formula, desc, position, color) in enumerate(properties_data):
            # 公式
            formula_tex = MathTex(
                formula,
                font_size=FONT_SIZE_FORMULA,
                color=color
            )
            
            # 描述
            desc_text = Text(
                desc,
                font=AUTHOR_FONT,
                font_size=FONT_SIZE_SMALL,
                color=GRAY_A
            )
            
            # 组合
            card_content = VGroup(formula_tex, desc_text).arrange(DOWN, buff=0.2)
            
            # 背景框
            card_bg = SurroundingRectangle(
                card_content,
                color=color,
                buff=0.3,
                corner_radius=0.1,
                stroke_width=2,
                fill_opacity=0.05
            )
            
            card = VGroup(card_bg, card_content).move_to(position)
            
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            
            cards.add(card)
        
        # 数值验证示例
        example = VGroup(
            MathTex(r"f(x) = 2^x", font_size=FONT_SIZE_BODY, color=COLOR_PRIMARY),
            MathTex(r"f^{-1}(x) = \log_2 x", font_size=FONT_SIZE_BODY, color=COLOR_SECONDARY),
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 3)
        
        verification = MathTex(
            r"f(f^{-1}(2)) = 2^{\log_2 2} = 2^1 = 2 \;\checkmark",
            font_size=FONT_SIZE_SMALL + 2,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.8
            )
            self.wait(0.3)
        
        self.wait(0.5)
        
        # 数值验证
        self.play(
            *[Write(eq) for eq in example],
            run_time=1.0
        )
        self.play(Write(verification), run_time=1.2)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(example),
            FadeOut(verification),
            run_time=0.6
        )
    
    def scene_6_monotonic(self):
        """场景6: 单调性条件 (8-10秒)"""
        # 标题
        title = Text(
            "单调函数必有反函数",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 创建小坐标轴
        axes_config = {
            "x_range": [-2, 2, 1],
            "y_range": [-2, 2, 1],
            "x_length": 2.5,
            "y_length": 2.5,
            "axis_config": {"color": GRAY_B, "stroke_width": 1.5},
            "tips": False
        }
        
        # 单调递增
        axes1 = Axes(**axes_config).move_to(UP * 3 + LEFT * 2.5)
        func1 = axes1.plot(lambda x: 0.5 * x, color=COLOR_FORMULA, stroke_width=2)
        label1 = Text("单调递增", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=WHITE).next_to(axes1, DOWN, buff=0.2)
        check1 = MathTex(r"\checkmark", font_size=24, color=COLOR_FORMULA).next_to(label1, DOWN, buff=0.1)
        group1 = VGroup(axes1, func1, label1, check1)
        
        # 单调递减
        axes2 = Axes(**axes_config).move_to(UP * 3 + RIGHT * 2.5)
        func2 = axes2.plot(lambda x: -0.5 * x, color=COLOR_FORMULA, stroke_width=2)
        label2 = Text("单调递减", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=WHITE).next_to(axes2, DOWN, buff=0.2)
        check2 = MathTex(r"\checkmark", font_size=24, color=COLOR_FORMULA).next_to(label2, DOWN, buff=0.1)
        group2 = VGroup(axes2, func2, label2, check2)
        
        # 非单调
        axes3 = Axes(**axes_config).move_to(UP * 0.2)
        func3 = axes3.plot(lambda x: x**2 - 1, x_range=[-1.5, 1.5], color=RED, stroke_width=2)
        label3 = Text("非单调", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=WHITE).next_to(axes3, DOWN, buff=0.2)
        cross = MathTex(r"\times", font_size=28, color=RED).next_to(label3, DOWN, buff=0.1)
        group3 = VGroup(axes3, func3, label3, cross)
        
        # 水平线测试说明
        horizontal_line = DashedLine(
            axes3.c2p(-1.5, 0),
            axes3.c2p(1.5, 0),
            color=YELLOW,
            stroke_width=2,
            dash_length=0.08
        )
        
        explanation = Text(
            "水平线测试: 单调函数只交一次",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        # 结论
        conclusion = VGroup(
            Text("单调函数", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"\Rightarrow", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT),
            Text("一一对应", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"\Rightarrow", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT),
            Text("有反函数", font=AUTHOR_FONT, font_size=FONT_SIZE_BODY, color=COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 4.5)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        
        # 展示三种情况
        self.play(
            Create(axes1),
            Create(func1),
            run_time=0.8
        )
        self.play(
            Write(label1),
            FadeIn(check1, scale=1.2),
            run_time=0.6
        )
        
        self.play(
            Create(axes2),
            Create(func2),
            run_time=0.8
        )
        self.play(
            Write(label2),
            FadeIn(check2, scale=1.2),
            run_time=0.6
        )
        
        self.play(
            Create(axes3),
            Create(func3),
            run_time=0.8
        )
        self.play(
            Write(label3),
            FadeIn(cross, scale=1.2),
            run_time=0.6
        )
        
        # 水平线测试
        self.play(
            Create(horizontal_line),
            Write(explanation),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 结论
        self.play(
            *[FadeIn(obj, shift=RIGHT*0.2) for obj in conclusion],
            run_time=1.0
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(group1),
            FadeOut(group2),
            FadeOut(group3),
            FadeOut(horizontal_line),
            FadeOut(explanation),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结与片尾 (8-10秒)"""
        # 标题
        title = Text(
            "反函数三要素",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=GOLD
        ).move_to(UP * 6.5)
        
        # 三大要素卡片
        cards_data = [
            ("定义", "x与y互换角色", COLOR_PRIMARY),
            ("对称性", "图像关于y=x对称", COLOR_HIGHLIGHT),
            ("性质", "f(f⁻¹(x))=x", COLOR_FORMULA)
        ]
        
        cards = VGroup()
        
        for i, (title_text, content, color) in enumerate(cards_data):
            # 标题
            card_title = Text(
                title_text,
                font=AUTHOR_FONT,
                font_size=FONT_SIZE_BODY,
                color=WHITE
            )
            
            # 内容
            card_content = Text(
                content,
                font=AUTHOR_FONT,
                font_size=FONT_SIZE_SMALL + 2,
                color=GRAY_A
            )
            
            # 组合
            card_group = VGroup(card_title, card_content).arrange(DOWN, buff=0.2)
            
            # 背景框
            card_bg = SurroundingRectangle(
                card_group,
                color=color,
                buff=0.3,
                corner_radius=0.1,
                stroke_width=2,
                fill_opacity=0.05
            )
            
            card = VGroup(card_bg, card_group)
            card.move_to(UP * (3.5 - i * 2))
            
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            
            cards.add(card)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.wait(0.4)
        
        # 卡片依次滑入
        for card in cards:
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.4
            )
            self.wait(0.1)
        
        # 整体闪烁强调
        for card in cards:
            self.play(
                card[0].animate.set_stroke(width=4),
                run_time=0.15
            )
        
        self.wait(0.6)
        
        # 清除卡片
        self.play(
            FadeOut(title),
            FadeOut(cards),
            run_time=0.6
        )
        
        # 作者信息放大
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
        
        # 对称符号装饰
        symmetric_symbols = VGroup(
            MathTex(r"f", font_size=32, color=COLOR_PRIMARY),
            MathTex(r"\leftrightarrow", font_size=32, color=COLOR_HIGHLIGHT),
            MathTex(r"f^{-1}", font_size=32, color=COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(symbol, scale=0.5) for symbol in symmetric_symbols],
            run_time=0.6
        )
        
        # 旋转动画
        self.play(
            Rotate(symmetric_symbols, angle=PI/6),
            run_time=1.5,
            rate_func=there_and_back
        )
        
        self.wait(0.5)
        
        # 总结文字
        summary = Text(
            "掌握反函数，函数更通透！",
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
            FadeOut(symmetric_symbols),
            FadeOut(summary),
            run_time=1.0
        )


# ===== 运行说明 =====
"""
渲染命令:

快速预览（低质量）:
manim -pql inverse_functions.py InverseFunctions

中等质量:
manim -qm inverse_functions.py InverseFunctions

高质量（1080p）:
manim -qh inverse_functions.py InverseFunctions

4K质量:
manim -qk inverse_functions.py InverseFunctions

透明背景:
manim -qh -t inverse_functions.py InverseFunctions

GIF格式:
manim -qm --format gif inverse_functions.py InverseFunctions
"""