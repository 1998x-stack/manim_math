"""
集合的概念与表示 - Sets Concept and Representation Animation
使用 Manim 创建的高一数学教学视频

内容: 集合的定义、三大特性、元素关系、表示方法
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


class SetsConceptAnimation(Scene):
    """
    集合概念与表示教学动画
    
    场景顺序:
    1. 开场钩子
    2. 集合的定义
    3. 三大特性（确定性、互异性、无序性）
    4. 元素与集合关系（∈ 和 ∉）
    5. 表示方法1：列举法
    6. 表示方法2：描述法
    7. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主集合
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 元素/强调
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 正确
        self.COLOR_ERROR = "#e67e22"        # 橙色 - 错误
        
        # 初始化视觉元素位置
        self.setup_visual_elements()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_properties()
        self.scene_4_membership()
        self.scene_5_roster_notation()
        self.scene_6_set_builder_notation()
        self.scene_7_outro()
    
    def setup_visual_elements(self):
        """初始化所有视觉元素的位置和参数"""
        # 关键位置
        self.TITLE_Y = 5.5
        self.MAIN_Y = 2.0
        self.FORMULA_Y = -2.0
        self.EXPLANATION_Y = -4.5
        self.AUTHOR_Y = 7.0
        
        # 集合圆参数
        self.SET_CIRCLE_RADIUS = 1.8
        self.SET_CIRCLE_CENTER = np.array([0, self.MAIN_Y, 0])
        
        # 元素点分布（圆内五边形均匀分布）
        self.ELEMENT_COUNT = 5
        self.ELEMENT_RADIUS = 1.0  # 距圆心距离
        self.element_positions = []
        
        for i in range(self.ELEMENT_COUNT):
            angle = i * 2 * PI / self.ELEMENT_COUNT - PI/2  # 从顶部开始
            x = self.ELEMENT_RADIUS * np.cos(angle)
            y = self.ELEMENT_RADIUS * np.sin(angle) + self.MAIN_Y
            self.element_positions.append(np.array([x, y, 0]))
        
        # 验证位置是否在边界内
        self._verify_positions()
    
    def _verify_positions(self):
        """验证所有关键位置是否在安全边界内"""
        SAFE_X = 4.0
        SAFE_Y_TOP = 7.0
        SAFE_Y_BOTTOM = -7.0
        
        # 检查集合圆是否在边界内
        circle_top = self.SET_CIRCLE_CENTER[1] + self.SET_CIRCLE_RADIUS
        circle_bottom = self.SET_CIRCLE_CENTER[1] - self.SET_CIRCLE_RADIUS
        
        assert circle_top < SAFE_Y_TOP, f"集合圆顶部溢出: {circle_top}"
        assert circle_bottom > SAFE_Y_BOTTOM, f"集合圆底部溢出: {circle_bottom}"
        
        # 检查元素点位置
        for i, pos in enumerate(self.element_positions):
            assert abs(pos[0]) < SAFE_X, f"元素{i+1} X坐标溢出: {pos[0]}"
            assert SAFE_Y_BOTTOM < pos[1] < SAFE_Y_TOP, f"元素{i+1} Y坐标溢出: {pos[1]}"
        
        print("✓ 位置验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部常驻）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * self.AUTHOR_Y)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "1, 2, 3, 🍎, 🐱...\n如何整理这些对象?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * self.TITLE_Y)
        
        self.play(Write(hook_question), run_time=1.2)
        
        # 创建随机散落的对象（数字和符号）
        random_objects = VGroup()
        
        # 数字
        for num in [1, 2, 3, 4, 5]:
            obj = Text(
                str(num),
                font="Noto Sans CJK SC",
                font_size=36,
                color=self.COLOR_PRIMARY
            )
            random_objects.add(obj)
        
        # 符号/图标（用文字代替emoji以避免兼容性问题）
        for symbol in ["★", "♠", "♥"]:
            obj = Text(
                symbol,
                font="Noto Sans CJK SC",
                font_size=36,
                color=self.COLOR_SECONDARY
            )
            random_objects.add(obj)
        
        # 随机分布
        for obj in random_objects:
            random_pos = np.array([
                np.random.uniform(-3, 3),
                np.random.uniform(0, 4),
                0
            ])
            obj.move_to(random_pos)
        
        # 对象飞入
        self.play(
            LaggedStart(*[
                FadeIn(obj, shift=DOWN * 0.5, scale=0.5)
                for obj in random_objects
            ], lag_ratio=0.15),
            run_time=1.5
        )
        
        # 稍等
        self.wait(0.5)
        
        # 聚拢到网格
        random_objects.generate_target()
        random_objects.target.arrange_in_grid(rows=2, buff=0.5).move_to(UP * 1.5)
        
        self.play(MoveToTarget(random_objects), run_time=0.8)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(random_objects),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 集合的定义"""
        # 标题
        title = Text(
            "什么是集合?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 绘制集合圆
        self.set_circle = Circle(
            radius=self.SET_CIRCLE_RADIUS,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.SET_CIRCLE_CENTER)
        
        self.play(Create(self.set_circle), run_time=1.0)
        
        # 集合标签 A
        self.set_label = MathTex(
            "A",
            font_size=48,
            color=self.COLOR_PRIMARY
        ).next_to(self.set_circle, UP, buff=0.3)
        
        self.play(Write(self.set_label), run_time=0.5)
        
        # 定义文字
        definition = Text(
            "由确定对象组成的整体",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)
        
        # 创建元素点
        self.element_dots = VGroup()
        self.element_labels = VGroup()
        
        for i in range(self.ELEMENT_COUNT):
            # 点
            dot = Dot(
                point=self.element_positions[i],
                radius=0.12,
                color=self.COLOR_SECONDARY
            )
            self.element_dots.add(dot)
            
            # 标签
            label = MathTex(
                str(i + 1),
                font_size=32,
                color=WHITE
            ).move_to(self.element_positions[i])
            self.element_labels.add(label)
        
        # 元素依次出现
        self.play(
            Succession(*[
                FadeIn(dot, scale=0.5)
                for dot in self.element_dots
            ]),
            run_time=2.0
        )
        
        # 标签出现
        self.play(Write(self.element_labels), run_time=1.5)
        
        # 强调"整体"
        self.play(
            Indicate(self.set_circle, color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(title), FadeOut(definition), run_time=0.5)
    
    def scene_3_properties(self):
        """场景3: 三大特性"""
        # 3.1 确定性
        self._show_property_determinacy()
        
        # 3.2 互异性
        self._show_property_distinctness()
        
        # 3.3 无序性
        self._show_property_unordered()
    
    def _show_property_determinacy(self):
        """确定性"""
        title = Text(
            "特性1: 确定性",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 不确定的对象 "?"
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.COLOR_ERROR
        ).move_to(LEFT * 3.5)
        
        self.play(FadeIn(question_mark, shift=RIGHT), run_time=0.5)
        
        # 尝试靠近集合
        self.play(
            question_mark.animate.move_to(LEFT * 2.5 + UP * self.MAIN_Y),
            run_time=1.0
        )
        
        # 被弹开
        self.play(
            question_mark.animate.shift(DOWN * 3).set_opacity(0),
            run_time=0.8
        )
        self.remove(question_mark)
        
        # 确定的对象 "√"
        check_mark = Text(
            "√",
            font="Noto Sans CJK SC",
            font_size=50,
            color=self.COLOR_SUCCESS
        ).move_to(RIGHT * 3.5)
        
        self.play(FadeIn(check_mark, shift=LEFT), run_time=0.5)
        
        # 靠近并进入集合
        self.play(
            check_mark.animate.move_to(RIGHT * 2.3 + UP * self.MAIN_Y),
            run_time=0.8
        )
        
        # 变成新元素
        new_dot = Dot(
            point=RIGHT * 0.8 + UP * (self.MAIN_Y - 0.3),
            radius=0.12,
            color=self.COLOR_SUCCESS
        )
        
        self.play(
            Transform(check_mark, new_dot),
            run_time=0.5
        )
        self.remove(check_mark)
        self.add(new_dot)
        
        # 说明文字
        explanation = Text(
            "要么属于，要么不属于",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(new_dot),
            run_time=0.5
        )
    
    def _show_property_distinctness(self):
        """互异性"""
        title = Text(
            "特性2: 互异性",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 复制一个 "3"
        duplicate = self.element_labels[2].copy()
        duplicate.set_color(self.COLOR_ERROR)
        duplicate.move_to(RIGHT * 3.5 + UP * self.MAIN_Y)
        
        self.play(FadeIn(duplicate, shift=LEFT), run_time=0.5)
        
        # 尝试靠近集合
        target_pos = self.element_positions[2] + RIGHT * 0.5
        self.play(duplicate.animate.move_to(target_pos), run_time=0.8)
        
        # 红色警告
        warning_x = Text(
            "✗",
            font="Noto Sans CJK SC",
            font_size=80,
            color=RED
        ).move_to(target_pos)
        
        self.play(
            Flash(duplicate, color=RED, flash_radius=0.5),
            FadeIn(warning_x, scale=0.5),
            run_time=0.5
        )
        
        # 重复元素消失
        self.play(
            FadeOut(duplicate),
            FadeOut(warning_x),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "元素互不相同",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(FadeOut(title), FadeOut(explanation), run_time=0.5)
    
    def _show_property_unordered(self):
        """无序性"""
        title = Text(
            "特性3: 无序性",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 记录原始位置
        original_positions = [label.get_center() for label in self.element_labels]
        
        # 第一次重排 - 顺时针旋转
        new_positions_1 = [
            self.element_positions[(i + 1) % self.ELEMENT_COUNT]
            for i in range(self.ELEMENT_COUNT)
        ]
        
        self.play(
            *[
                self.element_labels[i].animate.move_to(new_positions_1[i])
                for i in range(self.ELEMENT_COUNT)
            ],
            run_time=1.2
        )
        self.wait(0.3)
        
        # 第二次重排 - 再次旋转
        new_positions_2 = [
            self.element_positions[(i + 2) % self.ELEMENT_COUNT]
            for i in range(self.ELEMENT_COUNT)
        ]
        
        self.play(
            *[
                self.element_labels[i].animate.move_to(new_positions_2[i])
                for i in range(self.ELEMENT_COUNT)
            ],
            run_time=1.2
        )
        
        # 等号出现
        equals = MathTex(
            "=",
            font_size=80,
            color=self.COLOR_SUCCESS
        ).move_to(RIGHT * 3 + UP * self.MAIN_Y)
        
        self.play(FadeIn(equals, scale=0.5), run_time=0.5)
        self.wait(0.5)
        
        # 说明文字
        explanation = Text(
            "顺序不影响集合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 恢复原始位置
        self.play(
            *[
                self.element_labels[i].animate.move_to(original_positions[i])
                for i in range(self.ELEMENT_COUNT)
            ],
            FadeOut(equals),
            FadeOut(title),
            FadeOut(explanation),
            run_time=0.8
        )
    
    def scene_4_membership(self):
        """场景4: 元素与集合关系"""
        # 标题
        title = Text(
            "元素与集合",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 高亮元素 3
        self.play(
            Indicate(self.element_dots[2], color=YELLOW, scale_factor=1.5),
            Indicate(self.element_labels[2], color=YELLOW, scale_factor=1.3),
            run_time=0.8
        )
        
        # 公式: 3 ∈ A
        formula_1 = MathTex(
            "3", r"\in", "A",
            font_size=48
        ).move_to(DOWN * self.FORMULA_Y)
        formula_1[0].set_color(self.COLOR_SECONDARY)
        formula_1[2].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula_1), run_time=1.0)
        
        # 朗读
        reading_1 = Text(
            "3 属于 A",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * (self.FORMULA_Y + 1.0))
        
        self.play(FadeIn(reading_1), run_time=0.5)
        self.wait(1.2)
        
        # 清除第一个公式
        self.play(FadeOut(formula_1), FadeOut(reading_1), run_time=0.5)
        
        # 数字 6 出现在圆外
        six_dot = Dot(
            point=RIGHT * 3.5 + UP * self.MAIN_Y,
            radius=0.12,
            color=self.COLOR_ERROR
        )
        six_label = MathTex(
            "6",
            font_size=32,
            color=self.COLOR_ERROR
        ).move_to(RIGHT * 3.5 + UP * self.MAIN_Y)
        
        self.play(
            FadeIn(six_dot, shift=LEFT * 0.5),
            FadeIn(six_label, shift=LEFT * 0.5),
            run_time=0.5
        )
        
        # 公式: 6 ∉ A
        formula_2 = MathTex(
            "6", r"\notin", "A",
            font_size=48
        ).move_to(DOWN * self.FORMULA_Y)
        formula_2[0].set_color(self.COLOR_ERROR)
        formula_2[2].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula_2), run_time=1.0)
        
        # 朗读
        reading_2 = Text(
            "6 不属于 A",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * (self.FORMULA_Y + 1.0))
        
        self.play(FadeIn(reading_2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_2),
            FadeOut(reading_2),
            FadeOut(six_dot),
            FadeOut(six_label),
            run_time=0.6
        )
    
    def scene_5_roster_notation(self):
        """场景5: 列举法"""
        # 标题
        title = Text(
            "表示方法 1: 列举法",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 公式框架: A = { }
        formula_shell = MathTex(
            "A", "=", r"\{", r"\}",
            font_size=44
        ).move_to(DOWN * self.FORMULA_Y)
        formula_shell[0].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula_shell), run_time=0.8)
        
        # 元素依次加入公式
        formula_elements = VGroup()
        
        for i in range(self.ELEMENT_COUNT):
            # 高亮圆内元素
            self.play(
                Indicate(self.element_dots[i], color=YELLOW, scale_factor=1.3),
                run_time=0.3
            )
            
            # 创建公式中的元素
            if i == 0:
                elem = MathTex(str(i + 1), font_size=40, color=WHITE)
            else:
                elem = MathTex(",", str(i + 1), font_size=40, color=WHITE)
            
            formula_elements.add(elem)
        
        # 重新排列公式元素
        formula_content = VGroup(*formula_elements).arrange(RIGHT, buff=0.1)
        
        # 计算位置（在花括号之间）
        left_brace_x = formula_shell[2].get_center()[0]
        right_brace_x = formula_shell[3].get_center()[0]
        formula_y = formula_shell.get_center()[1]
        
        formula_content.move_to([
            (left_brace_x + right_brace_x) / 2,
            formula_y,
            0
        ])
        
        # 逐个添加元素到公式
        for i, elem in enumerate(formula_elements):
            # 从圆内元素复制
            elem_copy = self.element_labels[i].copy()
            
            if i == 0:
                target_elem = formula_content[i]
            else:
                target_elem = formula_content[i][1]  # 跳过逗号
            
            self.play(
                Transform(elem_copy, target_elem),
                run_time=0.4
            )
            self.remove(elem_copy)
            self.add(target_elem)
        
        self.wait(0.8)
        
        # 最终完整公式
        final_formula = MathTex(
            "A", "=", r"\{", "1", ",", "2", ",", "3", ",", "4", ",", "5", r"\}",
            font_size=40
        ).move_to(DOWN * self.FORMULA_Y)
        final_formula[0].set_color(self.COLOR_PRIMARY)
        
        self.play(
            FadeOut(formula_shell),
            FadeOut(formula_content),
            FadeIn(final_formula),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "一一列举元素",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(final_formula),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def scene_6_set_builder_notation(self):
        """场景6: 描述法"""
        # 标题
        title = Text(
            "表示方法 2: 描述法",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 公式框架: A = {x | ... }
        formula_framework = MathTex(
            "A", "=", r"\{", "x", r"\mid", r"\ldots", r"\}",
            font_size=38
        ).move_to(DOWN * self.FORMULA_Y)
        formula_framework[0].set_color(self.COLOR_PRIMARY)
        formula_framework[3].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(formula_framework), run_time=1.0)
        self.wait(0.5)
        
        # 条件1: x ∈ ℕ
        condition_1 = MathTex(
            "x", r"\in", r"\mathbb{N}",
            font_size=36
        ).move_to(DOWN * (self.FORMULA_Y - 1.2))
        condition_1[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(condition_1), run_time=0.8)
        self.wait(0.5)
        
        # 条件2: 1 ≤ x ≤ 5
        condition_2 = MathTex(
            "1", r"\leq", "x", r"\leq", "5",
            font_size=36
        ).move_to(DOWN * (self.FORMULA_Y - 2.0))
        condition_2[2].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(condition_2), run_time=0.8)
        self.wait(0.8)
        
        # 完整公式
        complete_formula = MathTex(
            "A", "=", r"\{", "x", r"\mid", "x", r"\in", r"\mathbb{N}", ",", 
            "1", r"\leq", "x", r"\leq", "5", r"\}",
            font_size=32
        ).move_to(DOWN * self.FORMULA_Y)
        complete_formula[0].set_color(self.COLOR_PRIMARY)
        complete_formula[3].set_color(self.COLOR_SECONDARY)
        complete_formula[5].set_color(self.COLOR_SECONDARY)
        complete_formula[11].set_color(self.COLOR_SECONDARY)
        
        self.play(
            FadeOut(formula_framework),
            FadeOut(condition_1),
            FadeOut(condition_2),
            FadeIn(complete_formula),
            run_time=1.0
        )
        
        # 说明文字
        explanation = Text(
            "用共同特征描述",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.0)
        
        # 高亮 x
        x_positions = [3, 5, 11]
        self.play(
            *[Indicate(complete_formula[i], color=YELLOW, scale_factor=1.3) for i in x_positions],
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(complete_formula),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 集合圆淡出
        self.play(
            self.set_circle.animate.set_opacity(0.2),
            self.element_dots.animate.set_opacity(0.2),
            self.element_labels.animate.set_opacity(0.2),
            self.set_label.animate.set_opacity(0.2),
            run_time=0.5
        )
    
    def scene_7_outro(self):
        """场景7: 片尾总结"""
        # 清空场景
        self.play(
            FadeOut(self.set_circle),
            FadeOut(self.element_dots),
            FadeOut(self.element_labels),
            FadeOut(self.set_label),
            run_time=0.5
        )
        
        # 标题
        summary_title = Text(
            "集合要点",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 创建总结卡片
        cards = VGroup()
        
        # 卡片1: 三大特性
        card_1 = self._create_summary_card(
            "三大特性",
            "确定性 · 互异性 · 无序性",
            self.COLOR_PRIMARY,
            UP * 3
        )
        cards.add(card_1)
        
        # 卡片2: 元素关系
        card_2 = self._create_summary_card(
            "元素关系",
            "∈ (属于)  ∉ (不属于)",
            self.COLOR_SECONDARY,
            UP * 1.5
        )
        cards.add(card_2)
        
        # 卡片3: 表示方法
        card_3 = self._create_summary_card(
            "表示方法",
            "列举法 · 描述法",
            self.COLOR_SUCCESS,
            ORIGIN
        )
        cards.add(card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(2.0)
        
        # 清除卡片和标题
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.6
        )
        
        # 作者信息放大
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
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 集合符号装饰
        set_symbols = VGroup()
        for i in range(6):
            angle = i * PI / 3
            symbol = MathTex(
                r"\in",
                font_size=40,
                color=self.COLOR_PRIMARY
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            )
            set_symbols.add(symbol)
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in set_symbols],
            run_time=0.6
        )
        
        # 旋转动画
        self.play(
            Rotate(set_symbols, angle=PI, run_time=1.5)
        )
        
        self.wait(3.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(set_symbols),
            run_time=1.0
        )
    
    def _create_summary_card(self, title_text, content_text, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title = Text(
            title_text,
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        )
        
        # 内容
        content = Text(
            content_text,
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title, content).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql sets_concept.py SetsConceptAnimation  # 快速预览
# manim -qh sets_concept.py SetsConceptAnimation   # 高质量 1080p
# manim -qk sets_concept.py SetsConceptAnimation   # 4K质量