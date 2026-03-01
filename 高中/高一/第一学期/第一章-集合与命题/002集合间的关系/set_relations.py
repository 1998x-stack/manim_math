"""
集合间的关系 - Set Relations Animation
使用 Manim 创建的高一数学教学视频

内容: 子集、真子集、集合相等、空集、子集个数公式
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


class SetRelationsAnimation(Scene):
    """
    集合间的关系教学动画
    
    场景顺序:
    1. 开场钩子
    2. 子集定义 (A⊆B)
    3. 真子集 (A⊊B)
    4. 集合相等 (A=B)
    5. 空集性质 (∅⊆A)
    6. 子集个数公式 (2^n)
    7. 真子集个数 (2^n-1)
    8. 片尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_SET_A = "#3498db"      # 蓝色 - 集合A
        self.COLOR_SET_B = "#e74c3c"      # 红色 - 集合B
        self.COLOR_SUBSET = "#2ecc71"     # 绿色 - 子集强调
        self.COLOR_HIGHLIGHT = YELLOW     # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B     # 灰色 - 辅助
        self.COLOR_EMPTY = "#95a5a6"      # 灰色 - 空集
        
        # 初始化几何布局
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_subset()
        self.scene_3_proper_subset()
        self.scene_4_set_equality()
        self.scene_5_empty_set()
        self.scene_6_subset_count()
        self.scene_7_proper_subset_count()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """初始化所有几何布局和位置"""
        # 关键Y坐标
        self.TITLE_Y = 5.5
        self.MAIN_Y = 2.0
        self.FORMULA_Y = -2.5
        self.EXPLANATION_Y = -4.5
        self.AUTHOR_Y = 7.0
        
        # 场景1：独立两圆
        self.CIRCLE_A_CENTER_INIT = np.array([-1.5, self.MAIN_Y, 0])
        self.CIRCLE_B_CENTER_INIT = np.array([1.5, self.MAIN_Y, 0])
        self.CIRCLE_RADIUS_INIT = 1.3
        
        # 场景2-5：子集布局（A在B内）
        self.CIRCLE_B_CENTER_SUBSET = np.array([0, self.MAIN_Y, 0])
        self.CIRCLE_A_CENTER_SUBSET = np.array([-0.5, self.MAIN_Y, 0])
        self.CIRCLE_B_RADIUS_SUBSET = 2.0
        self.CIRCLE_A_RADIUS_SUBSET = 1.2
        
        # 元素点位置（圆内均匀分布）
        self._calculate_element_positions()
        
        # 验证位置
        self._verify_positions()
    
    def _calculate_element_positions(self):
        """计算元素点在圆内的位置"""
        # A集合元素（3个点）
        self.element_count_A = 3
        self.element_positions_A = []
        
        for i in range(self.element_count_A):
            angle = i * 2 * PI / self.element_count_A + PI/2
            x = 0.6 * np.cos(angle)
            y = 0.6 * np.sin(angle)
            self.element_positions_A.append(np.array([x, y, 0]))
        
        # B集合额外元素（2个点，在A外B内）
        self.element_positions_B_extra = [
            np.array([1.2, 0.5, 0]),
            np.array([1.2, -0.5, 0])
        ]
    
    def _verify_positions(self):
        """验证所有位置在安全边界内"""
        SAFE_X = 4.0
        SAFE_Y_TOP = 7.0
        SAFE_Y_BOTTOM = -7.0
        
        # 检查圆是否在边界内
        circle_configs = [
            ("初始A", self.CIRCLE_A_CENTER_INIT, self.CIRCLE_RADIUS_INIT),
            ("初始B", self.CIRCLE_B_CENTER_INIT, self.CIRCLE_RADIUS_INIT),
            ("子集A", self.CIRCLE_A_CENTER_SUBSET, self.CIRCLE_A_RADIUS_SUBSET),
            ("子集B", self.CIRCLE_B_CENTER_SUBSET, self.CIRCLE_B_RADIUS_SUBSET),
        ]
        
        for name, center, radius in circle_configs:
            assert abs(center[0]) + radius < SAFE_X, f"{name}圆X方向溢出"
            assert center[1] - radius > SAFE_Y_BOTTOM, f"{name}圆底部溢出"
            assert center[1] + radius < SAFE_Y_TOP, f"{name}圆顶部溢出"
        
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
        hook = Text(
            "集合A和B\n谁包含谁?",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(UP * self.TITLE_Y)
        
        self.play(Write(hook), run_time=1.2)
        
        # 两个独立的圆
        circle_A_init = Circle(
            radius=self.CIRCLE_RADIUS_INIT,
            color=self.COLOR_SET_A,
            stroke_width=4
        ).move_to(self.CIRCLE_A_CENTER_INIT)
        
        circle_B_init = Circle(
            radius=self.CIRCLE_RADIUS_INIT,
            color=self.COLOR_SET_B,
            stroke_width=4
        ).move_to(self.CIRCLE_B_CENTER_INIT)
        
        label_A = MathTex("A", font_size=40, color=self.COLOR_SET_A).next_to(
            circle_A_init, UP, buff=0.2
        )
        label_B = MathTex("B", font_size=40, color=self.COLOR_SET_B).next_to(
            circle_B_init, UP, buff=0.2
        )
        
        self.play(
            FadeIn(circle_A_init),
            FadeIn(circle_B_init),
            run_time=1.0
        )
        self.play(Write(label_A), Write(label_B), run_time=0.5)
        
        # 问号
        question = Text("?", font="Noto Sans CJK SC", font_size=80, color=YELLOW).move_to(
            UP * self.MAIN_Y
        )
        self.play(FadeIn(question, scale=0.5), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(question),
            FadeOut(circle_A_init),
            FadeOut(circle_B_init),
            FadeOut(label_A),
            FadeOut(label_B),
            run_time=0.5
        )
    
    def scene_2_subset(self):
        """场景2: 子集定义"""
        # 标题
        title = Text(
            "子集 Subset",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_SUBSET
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 绘制大圆B
        self.circle_B = Circle(
            radius=self.CIRCLE_B_RADIUS_SUBSET,
            color=self.COLOR_SET_B,
            stroke_width=4
        ).move_to(self.CIRCLE_B_CENTER_SUBSET)
        
        self.label_B = MathTex("B", font_size=40, color=self.COLOR_SET_B).move_to(
            self.CIRCLE_B_CENTER_SUBSET + UP * (self.CIRCLE_B_RADIUS_SUBSET + 0.3)
        )
        
        self.play(Create(self.circle_B), run_time=1.0)
        self.play(Write(self.label_B), run_time=0.4)
        
        # 绘制小圆A（在B内）
        self.CIRCLE_A = Circle(
            radius=self.CIRCLE_A_RADIUS_SUBSET,
            color=self.COLOR_SET_A,
            stroke_width=4,
            fill_opacity=0.1,
            fill_color=self.COLOR_SET_A
        ).move_to(self.CIRCLE_A_CENTER_SUBSET)
        
        self.label_A = MathTex("A", font_size=40, color=self.COLOR_SET_A).move_to(
            self.CIRCLE_A_CENTER_SUBSET + UP * (self.CIRCLE_A_RADIUS_SUBSET + 0.3)
        )
        
        self.play(Create(self.CIRCLE_A), run_time=1.0)
        self.play(Write(self.label_A), run_time=0.4)
        
        # 添加元素点
        self.dots_A = VGroup()
        for i, rel_pos in enumerate(self.element_positions_A):
            dot = Dot(
                point=self.CIRCLE_A_CENTER_SUBSET + rel_pos,
                radius=0.08,
                color=WHITE
            )
            self.dots_A.add(dot)
        
        # B的额外元素
        self.dots_B_extra = VGroup()
        for pos in self.element_positions_B_extra:
            dot = Dot(
                point=self.CIRCLE_B_CENTER_SUBSET + pos,
                radius=0.08,
                color=GRAY_A
            )
            self.dots_B_extra.add(dot)
        
        self.play(FadeIn(self.dots_A), FadeIn(self.dots_B_extra), run_time=0.8)
        
        # 高亮A的元素
        self.play(Indicate(self.dots_A, color=YELLOW, scale_factor=1.5), run_time=0.8)
        
        # 箭头和说明
        arrow = Arrow(
            start=self.CIRCLE_A.get_right() + RIGHT * 0.3,
            end=self.CIRCLE_A.get_right() + RIGHT * 0.3 + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        arrow_text = Text(
            "都在B中",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(arrow, RIGHT, buff=0.1)
        
        self.play(GrowArrow(arrow), FadeIn(arrow_text), run_time=0.7)
        
        # 公式
        formula = MathTex(
            "A", r"\subseteq", "B",
            font_size=48
        ).move_to(DOWN * self.FORMULA_Y)
        formula[0].set_color(self.COLOR_SET_A)
        formula[2].set_color(self.COLOR_SET_B)
        
        self.play(Write(formula), run_time=1.0)
        
        # 朗读
        reading = Text(
            "A是B的子集",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * (self.FORMULA_Y + 1.0))
        
        self.play(FadeIn(reading), run_time=0.5)
        
        # 定义
        definition = Text(
            "A的所有元素都是B的元素",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(arrow_text),
            FadeOut(formula),
            FadeOut(reading),
            FadeOut(definition),
            run_time=0.6
        )
    
    def scene_3_proper_subset(self):
        """场景3: 真子集"""
        # 标题
        title = Text(
            "真子集 Proper Subset",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 高亮B中不在A的元素
        self.play(
            Indicate(self.dots_B_extra, color=RED, scale_factor=1.5),
            run_time=1.0
        )
        
        # 不等号
        inequality = MathTex(
            "A", r"\neq", "B",
            font_size=44
        ).move_to(DOWN * self.FORMULA_Y + LEFT * 2)
        inequality[0].set_color(self.COLOR_SET_A)
        inequality[2].set_color(self.COLOR_SET_B)
        
        self.play(Write(inequality), run_time=1.0)
        
        # 真子集符号
        formula = MathTex(
            "A", r"\subsetneq", "B",
            font_size=48
        ).move_to(DOWN * self.FORMULA_Y + RIGHT * 1.5)
        formula[0].set_color(self.COLOR_SET_A)
        formula[2].set_color(self.COLOR_SET_B)
        
        self.play(Write(formula), run_time=1.0)
        
        # 说明
        explanation = Text(
            "A⊆B 且 A≠B",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * (self.FORMULA_Y + 1.2))
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 对比动画：⊆ → ⊊
        subset_symbol = MathTex(r"\subseteq", font_size=60, color=BLUE).move_to(
            DOWN * self.EXPLANATION_Y + LEFT * 1.5
        )
        arrow_transform = Arrow(
            start=DOWN * self.EXPLANATION_Y + LEFT * 0.5,
            end=DOWN * self.EXPLANATION_Y + RIGHT * 0.5,
            color=YELLOW
        )
        proper_symbol = MathTex(r"\subsetneq", font_size=60, color=RED).move_to(
            DOWN * self.EXPLANATION_Y + RIGHT * 1.5
        )
        
        self.play(
            FadeIn(subset_symbol),
            GrowArrow(arrow_transform),
            FadeIn(proper_symbol),
            run_time=1.2
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(inequality),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(subset_symbol),
            FadeOut(arrow_transform),
            FadeOut(proper_symbol),
            run_time=0.6
        )
    
    def scene_4_set_equality(self):
        """场景4: 集合相等"""
        # 标题
        title = Text(
            "集合相等",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 移除B的额外元素
        self.play(FadeOut(self.dots_B_extra), run_time=0.5)
        
        # 圆A移动到与B重合
        self.play(
            self.CIRCLE_A.animate.move_to(self.CIRCLE_B_CENTER_SUBSET).set_fill(opacity=0),
            self.label_A.animate.move_to(
                self.CIRCLE_B_CENTER_SUBSET + UP * (self.CIRCLE_A_RADIUS_SUBSET + 0.3) + LEFT * 0.5
            ),
            self.dots_A.animate.shift(
                self.CIRCLE_B_CENTER_SUBSET - self.CIRCLE_A_CENTER_SUBSET
            ),
            run_time=1.5
        )
        
        # 两圆变同色
        self.play(
            self.CIRCLE_A.animate.set_color(PURPLE),
            self.circle_B.animate.set_color(PURPLE),
            run_time=0.5
        )
        
        # 双向包含箭头
        arrow_AB = Arrow(
            start=UP * (self.MAIN_Y - 2.8) + LEFT * 1.5,
            end=UP * (self.MAIN_Y - 2.8) + RIGHT * 1.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        label_AB = MathTex(r"A \subseteq B", font_size=24, color=GRAY_A).next_to(
            arrow_AB, UP, buff=0.1
        )
        
        arrow_BA = Arrow(
            start=UP * (self.MAIN_Y - 3.5) + RIGHT * 1.5,
            end=UP * (self.MAIN_Y - 3.5) + LEFT * 1.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        label_BA = MathTex(r"B \subseteq A", font_size=24, color=GRAY_A).next_to(
            arrow_BA, DOWN, buff=0.1
        )
        
        self.play(
            GrowArrow(arrow_AB),
            Write(label_AB),
            run_time=0.8
        )
        self.play(
            GrowArrow(arrow_BA),
            Write(label_BA),
            run_time=0.8
        )
        
        # 等号公式
        formula = MathTex(
            "A", "=", "B",
            font_size=52
        ).move_to(DOWN * self.FORMULA_Y)
        formula[0].set_color(PURPLE)
        formula[2].set_color(PURPLE)
        
        self.play(Write(formula), run_time=1.0)
        
        # 条件
        condition = Text(
            "双向包含则相等",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(FadeIn(condition), run_time=0.5)
        self.wait(1.5)
        
        # 清理并恢复
        self.play(
            FadeOut(title),
            FadeOut(arrow_AB),
            FadeOut(label_AB),
            FadeOut(arrow_BA),
            FadeOut(label_BA),
            FadeOut(formula),
            FadeOut(condition),
            run_time=0.6
        )
        
        # 恢复原状
        self.play(
            self.CIRCLE_A.animate.move_to(self.CIRCLE_A_CENTER_SUBSET).set_color(
                self.COLOR_SET_A
            ).set_fill(opacity=0.1),
            self.circle_B.animate.set_color(self.COLOR_SET_B),
            self.label_A.animate.move_to(
                self.CIRCLE_A_CENTER_SUBSET + UP * (self.CIRCLE_A_RADIUS_SUBSET + 0.3)
            ),
            self.dots_A.animate.shift(
                self.CIRCLE_A_CENTER_SUBSET - self.CIRCLE_B_CENTER_SUBSET
            ),
            FadeIn(self.dots_B_extra),
            run_time=1.0
        )
    
    def scene_5_empty_set(self):
        """场景5: 空集性质"""
        # 标题
        title = Text(
            "空集 Empty Set",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_EMPTY
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 清空圆A
        self.play(
            FadeOut(self.dots_A),
            self.CIRCLE_A.animate.set_fill(opacity=0),
            run_time=0.8
        )
        
        # 空集符号
        empty_symbol = MathTex(
            r"\emptyset",
            font_size=60,
            color=self.COLOR_EMPTY
        ).move_to(self.CIRCLE_A_CENTER_SUBSET)
        
        self.play(Write(empty_symbol), run_time=0.8)
        
        # 移入圆B（表示空集在任何集合内）
        self.wait(0.5)
        
        # 公式1
        formula_1 = MathTex(
            r"\emptyset", r"\subseteq", "A",
            font_size=44
        ).move_to(DOWN * self.FORMULA_Y)
        formula_1[0].set_color(self.COLOR_EMPTY)
        formula_1[2].set_color(self.COLOR_SET_A)
        
        self.play(Write(formula_1), run_time=1.0)
        
        # 说明
        text = Text(
            "空集是任何集合的子集",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * (self.FORMULA_Y + 1.0))
        
        self.play(FadeIn(text), run_time=0.5)
        self.wait(1.5)
        
        # 公式2（真子集）
        formula_2 = MathTex(
            r"\emptyset", r"\subsetneq", "A",
            font_size=44,
            color=GRAY_A
        ).move_to(DOWN * self.EXPLANATION_Y)
        formula_2[0].set_color(self.COLOR_EMPTY)
        
        note = Text(
            "(若A非空)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).next_to(formula_2, RIGHT, buff=0.2)
        
        self.play(Write(formula_2), FadeIn(note), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(empty_symbol),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(text),
            FadeOut(note),
            run_time=0.6
        )
        
        # 恢复A的元素
        self.play(FadeIn(self.dots_A), run_time=0.5)
    
    def scene_6_subset_count(self):
        """场景6: 子集个数公式"""
        # 清空Venn图
        self.play(
            FadeOut(self.CIRCLE_A),
            FadeOut(self.circle_B),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.dots_A),
            FadeOut(self.dots_B_extra),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "子集个数",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 展示集合A
        set_A = MathTex(
            "A", "=", r"\{", "1", ",", "2", ",", "3", r"\}",
            font_size=36
        ).move_to(UP * 4.5)
        set_A[0].set_color(self.COLOR_SET_A)
        
        self.play(Write(set_A), run_time=0.8)
        
        # n=3
        n_value = MathTex("n", "=", "3", font_size=32, color=GRAY_A).move_to(UP * 3.8)
        self.play(Write(n_value), run_time=0.5)
        
        # 8个子集
        subsets_data = [
            (r"\emptyset", 0),
            (r"\{1\}", 1),
            (r"\{2\}", 2),
            (r"\{3\}", 3),
            (r"\{1,2\}", 4),
            (r"\{1,3\}", 5),
            (r"\{2,3\}", 6),
            (r"\{1,2,3\}", 7),
        ]
        
        self.subset_boxes = VGroup()
        positions = [
            UP * 2.5 + LEFT * 3,
            UP * 2.5 + LEFT * 1,
            UP * 2.5 + RIGHT * 1,
            UP * 2.5 + RIGHT * 3,
            UP * 1.0 + LEFT * 3,
            UP * 1.0 + LEFT * 1,
            UP * 1.0 + RIGHT * 1,
            UP * 1.0 + RIGHT * 3,
        ]
        
        for (subset_tex, idx), pos in zip(subsets_data, positions):
            subset_label = MathTex(subset_tex, font_size=24, color=WHITE)
            box = SurroundingRectangle(
                subset_label,
                color=self.COLOR_SUBSET,
                buff=0.15,
                corner_radius=0.1
            )
            subset_group = VGroup(box, subset_label).move_to(pos)
            self.subset_boxes.add(subset_group)
        
        # 逐个出现
        for i, subset_box in enumerate(self.subset_boxes):
            self.play(FadeIn(subset_box, scale=0.8), run_time=0.4)
        
        # 计数高亮
        self.play(
            *[Indicate(box, color=YELLOW) for box in self.subset_boxes],
            run_time=1.0
        )
        
        # 公式
        formula = MathTex("2^3 = 8", font_size=44).move_to(DOWN * self.FORMULA_Y)
        
        self.play(Write(formula), run_time=1.0)
        
        # 一般公式
        general_formula = MathTex(
            r"\text{Subsets: }", "2", "^", "n",
            font_size=40,
            color=self.COLOR_SUBSET
        ).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(TransformMatchingTex(formula.copy(), general_formula), run_time=1.0)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(set_A),
            FadeOut(n_value),
            FadeOut(self.subset_boxes),
            FadeOut(formula),
            FadeOut(general_formula),
            run_time=0.6
        )
    
    def scene_7_proper_subset_count(self):
        """场景7: 真子集个数"""
        # 标题
        title = Text(
            "真子集个数",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 重新展示8个子集（快速）
        subsets_data = [
            (r"\emptyset", 0),
            (r"\{1\}", 1),
            (r"\{2\}", 2),
            (r"\{3\}", 3),
            (r"\{1,2\}", 4),
            (r"\{1,3\}", 5),
            (r"\{2,3\}", 6),
            (r"\{1,2,3\}", 7),
        ]
        
        subset_boxes = VGroup()
        positions = [
            UP * 3.0 + LEFT * 3,
            UP * 3.0 + LEFT * 1,
            UP * 3.0 + RIGHT * 1,
            UP * 3.0 + RIGHT * 3,
            UP * 1.5 + LEFT * 3,
            UP * 1.5 + LEFT * 1,
            UP * 1.5 + RIGHT * 1,
            UP * 1.5 + RIGHT * 3,
        ]
        
        for (subset_tex, idx), pos in zip(subsets_data, positions):
            subset_label = MathTex(subset_tex, font_size=22, color=WHITE)
            box = SurroundingRectangle(
                subset_label,
                color=self.COLOR_SUBSET,
                buff=0.12,
                corner_radius=0.1
            )
            subset_group = VGroup(box, subset_label).move_to(pos)
            subset_boxes.add(subset_group)
        
        self.play(FadeIn(subset_boxes), run_time=0.8)
        
        # 划掉 {1,2,3}
        cross = Cross(subset_boxes[7], color=RED, stroke_width=4)
        self.play(Create(cross), run_time=0.8)
        
        # 说明
        text = Text(
            "排除自身",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(text), run_time=0.5)
        
        # 剩余7个高亮
        remaining = VGroup(*[subset_boxes[i] for i in range(7)])
        self.play(Indicate(remaining, color=YELLOW, scale_factor=1.1), run_time=1.0)
        
        # 公式
        formula = MathTex("2^3 - 1 = 7", font_size=44).move_to(DOWN * self.FORMULA_Y)
        
        self.play(Write(formula), run_time=1.0)
        
        # 一般公式
        general_formula = MathTex(r"\text{Proper Subsets: }2^n - 1", font_size=36).move_to(DOWN * self.EXPLANATION_Y)
        
        self.play(TransformMatchingTex(formula.copy(), general_formula), run_time=1.0)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subset_boxes),
            FadeOut(cross),
            FadeOut(text),
            FadeOut(formula),
            FadeOut(general_formula),
            run_time=0.6
        )
    
    def scene_8_outro(self):
        """场景8: 片尾总结"""
        # 标题
        summary_title = Text(
            "集合关系要点",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 创建总结卡片
        cards = VGroup()
        
        # 卡片1: 子集
        card_1 = self._create_summary_card(
            "子集",
            "A⊆B: A的元素都在B中",
            self.COLOR_SET_A,
            UP * 3
        )
        cards.add(card_1)
        
        # 卡片2: 真子集
        card_2 = self._create_summary_card(
            "真子集",
            "A⊊B: A⊆B 且 A≠B",
            self.COLOR_SUBSET,
            UP * 1.5
        )
        cards.add(card_2)
        
        # 卡片3: 空集
        card_3 = self._create_summary_card(
            "空集",
            "∅⊆任何集合",
            self.COLOR_EMPTY,
            ORIGIN
        )
        cards.add(card_3)
        
        # 卡片4: 公式
        card_4 = self._create_summary_card(
            "个数",
            "子集: 2ⁿ, 真子集: 2ⁿ-1",
            self.COLOR_HIGHLIGHT,
            DOWN * 1.5
        )
        cards.add(card_4)
        
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
        symbols_list = [r"\subseteq", r"\subsetneq", r"\in", r"\emptyset"]
        for i in range(6):
            angle = i * PI / 3
            symbol_tex = symbols_list[i % len(symbols_list)]
            symbol = MathTex(
                symbol_tex,
                font_size=36,
                color=self.COLOR_SUBSET
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
# manim -pql set_relations.py SetRelationsAnimation  # 快速预览
# manim -qh set_relations.py SetRelationsAnimation   # 高质量 1080p
# manim -qk set_relations.py SetRelationsAnimation   # 4K质量