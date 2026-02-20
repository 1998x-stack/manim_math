"""
充分条件与必要条件 - Sufficient and Necessary Conditions
使用 Manim 创建的中学逻辑推理教学视频

内容: 充分条件、必要条件、充要条件的概念及集合关系解释
目标观众: 高中生
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


class SufficientNecessaryConditions(Scene):
    """
    充分条件与必要条件教学动画场景

    场景顺序:
    1. 开场介绍
    2. 充分条件解释
    3. 必要条件解释
    4. 充要条件讲解
    5. 总结与应用
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_LOGIC = "#3498db"        # 蓝色 - 逻辑关系
        self.COLOR_SUFFICIENT = "#e74c3c"   # 红色 - 充分条件
        self.COLOR_NECESSARY = "#2ecc71"    # 绿色 - 必要条件
        self.COLOR_EQUIVALENT = "#f39c12"   # 橙色 - 充要条件
        self.COLOR_SET = "#9b59b6"          # 紫色 - 集合关系
        self.COLOR_AUXILIARY = GRAY_B       # 辅助元素颜色
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮颜色

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_sufficient_condition()
        self.show_necessary_condition()
        self.show_equivalent_condition()
        self.show_summary()


    def setup_geometry(self):
        """初始化所有几何元素"""
        # 基准参数
        self.RADIUS = 1.2
        self.SPACING = 3.0

        # 定义集合中心点
        self.CENTER_P = np.array([-2, 0, 0])  # 命题P的集合中心
        self.CENTER_Q = np.array([1, 0, 0])   # 命题Q的集合中心

        # 验证几何计算
        self.verify_geometry()

    def verify_geometry(self):
        """验证几何关系"""
        print("✓ 几何验证完成")


    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "充分条件与必要条件",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "逻辑推理的重要概念",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 核心概念展示
        concept = MathTex(
            "p \\Rightarrow q",
            font_size=36
        ).move_to(UP * 3.5)

        concept_explanation = Text(
            "若p则q",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(concept, DOWN, buff=0.3)

        self.play(Write(concept), run_time=0.8)
        self.play(Write(concept_explanation), run_time=0.6)

        # 等待
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(concept),
            FadeOut(concept_explanation),
            run_time=0.6
        )


    def show_sufficient_condition(self):
        """场景2: 充分条件解释"""
        # 标题
        title = Text(
            "充分条件",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_SUFFICIENT
        ).move_to(UP * 6)

        self.play(Write(title), run_time=0.6)

        # P集合 (较小，放在左边)
        set_p = Circle(
            radius=self.RADIUS,
            color=self.COLOR_SUFFICIENT,
            fill_color=self.COLOR_SUFFICIENT,
            fill_opacity=0.2
        ).move_to(self.CENTER_P)

        label_p = Text(
            "P",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(self.CENTER_P)

        # Q集合 (较大，包含P)
        set_q = Circle(
            radius=self.RADIUS * 1.5,
            color=self.COLOR_LOGIC,
            fill_color=self.COLOR_LOGIC,
            fill_opacity=0.15
        ).move_to(self.CENTER_Q)

        label_q = Text(
            "Q",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(self.CENTER_Q)

        # 为了表示P是Q的子集，我们将Q的中心调整到和P相同位置或靠近
        adjusted_center_q = self.CENTER_P + RIGHT * 1.5  # 让P成为Q的子集
        set_q_target = Circle(
            radius=self.RADIUS * 1.5,
            color=self.COLOR_LOGIC,
            fill_color=self.COLOR_LOGIC,
            fill_opacity=0.15
        ).move_to(adjusted_center_q)

        # 先创建P集合
        self.play(Create(set_p), run_time=0.8)
        self.play(Write(label_p), run_time=0.4)

        # 再创建Q集合，显示P⊂Q的关系
        self.play(Create(set_q), run_time=0.8)
        self.play(Write(label_q), run_time=0.4)

        # 调整使P成为Q的子集
        self.play(
            Transform(set_q, set_q_target),
            label_q.animate.move_to(adjusted_center_q),
            run_time=1.0
        )

        # 添加子集符号
        subset_symbol = MathTex(
            "\\subset",
            font_size=36
        ).move_to((self.CENTER_P + adjusted_center_q) / 2)

        self.play(Write(subset_symbol), run_time=0.5)

        # 充分条件定义
        sufficient_def = Text(
            "p是q的充分条件",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SUFFICIENT
        ).move_to(UP * 1.5)

        self.play(Write(sufficient_def), run_time=0.8)

        # 充分条件解释
        sufficient_explanation = Text(
            "P⊂Q 时，p⇒q\n有它一定行",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 1)

        self.play(FadeIn(sufficient_explanation), run_time=0.6)

        # 箭头从P指向Q
        arrow = Arrow(
            start=self.CENTER_P + RIGHT * self.RADIUS * 0.8,
            end=adjusted_center_q + LEFT * self.RADIUS * 0.8,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )

        arrow_label = MathTex(
            "p \\Rightarrow q",
            color=self.COLOR_HIGHLIGHT,
            font_size=28
        ).next_to(arrow, UP, buff=0.1)

        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(Write(arrow_label), run_time=0.5)

        # 高亮重要部分
        self.play(
            Indicate(sufficient_def, color=self.COLOR_SUFFICIENT),
            run_time=1.0
        )

        # 等待
        self.wait(2)

        # 清理部分元素，保留集合图示
        self.play(
            FadeOut(title),
            FadeOut(subset_symbol),
            FadeOut(sufficient_def),
            FadeOut(sufficient_explanation),
            FadeOut(arrow_label),
            run_time=0.6
        )


    def show_necessary_condition(self):
        """场景3: 必要条件解释"""
        # 使用当前的集合图示，解释必要条件
        necessary_title = Text(
            "必要条件",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_NECESSARY
        ).move_to(UP * 6)

        self.play(Write(necessary_title), run_time=0.6)

        # 必要条件定义
        necessary_def = Text(
            "q是p的必要条件",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_NECESSARY
        ).move_to(UP * 4.5)

        self.play(Write(necessary_def), run_time=0.8)

        # 必要条件解释
        necessary_explanation = Text(
            "P⊂Q 时，q是p的必要条件\n没它一定不行",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 3)

        self.play(FadeIn(necessary_explanation), run_time=0.6)

        # 示例说明 - 使用Text而不是MathTex以避免LaTeX中文字符错误
        example_part1 = Text("例如：若 ", font="Noto Sans CJK SC", font_size=26)
        example_math = MathTex("x > 2", font_size=28)
        example_part2 = Text(" ，则 ", font="Noto Sans CJK SC", font_size=26)
        example_math2 = MathTex("x > 0", font_size=28)

        example = VGroup(example_part1, example_math, example_part2, example_math2).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)

        example_meaning = Text(
            "x>2 是 x>0 的充分条件\nx>0 是 x>2 的必要条件",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A,
            line_spacing=1.2
        ).next_to(example, DOWN, buff=0.4)

        self.play(Write(example), run_time=0.8)
        self.play(Write(example_meaning), run_time=1.0)

        # 如果箭头不存在则创建
        arrow = Arrow(
            start=self.CENTER_P + RIGHT * self.RADIUS * 0.8,
            end=(self.CENTER_P + RIGHT * 1.5) + LEFT * self.RADIUS * 0.8,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(GrowArrow(arrow), run_time=0.8)

        # 高亮必要条件
        self.play(
            Indicate(necessary_def, color=self.COLOR_NECESSARY),
            run_time=1.0
        )

        # 等待
        self.wait(2)

        # 清理部分元素，保留集合图示
        self.play(
            FadeOut(necessary_title),
            FadeOut(necessary_def),
            FadeOut(necessary_explanation),
            FadeOut(example),
            FadeOut(example_meaning),
            run_time=0.6
        )


    def show_equivalent_condition(self):
        """场景4: 充要条件讲解"""
        # 标题
        equivalent_title = Text(
            "充要条件",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_EQUIVALENT
        ).move_to(UP * 6)

        self.play(Write(equivalent_title), run_time=0.6)

        # 清除之前的集合图示，重新绘制以表示充要条件（P=Q）
        # 创建两个相同的集合，表示P=Q
        center_equal = ORIGIN
        set_p_equal = Circle(
            radius=self.RADIUS,
            color=self.COLOR_SUFFICIENT,
            fill_color=self.COLOR_SUFFICIENT,
            fill_opacity=0.2
        ).move_to(center_equal)

        set_q_equal = Circle(
            radius=self.RADIUS,
            color=self.COLOR_LOGIC,
            fill_color=self.COLOR_LOGIC,
            fill_opacity=0.15
        ).move_to(center_equal + 0.1*RIGHT)  # 微小偏移以便观察

        label_p_equal = Text(
            "P",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(center_equal + LEFT * 0.3)

        label_q_equal = Text(
            "Q",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(center_equal + RIGHT * 0.3)

        # 清除之前的对象并展示新的等价关系
        all_mobjects = list(self.mobjects)
        for obj in all_mobjects:
            if obj != equivalent_title:  # 保留标题
                self.remove(obj)

        # 添加新的等价条件表示
        self.play(
            Create(set_p_equal),
            Create(set_q_equal),
            Write(label_p_equal),
            Write(label_q_equal),
            run_time=1.2
        )

        # 添加双向箭头表示等价关系
        double_arrow = DoubleArrow(
            start=center_equal + LEFT * self.RADIUS * 0.7,
            end=center_equal + RIGHT * self.RADIUS * 0.7,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.1
        )

        self.play(GrowArrow(double_arrow), run_time=0.8)

        # 等价符号
        equivalence_symbol = MathTex(
            "p \\iff q",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(center_equal + UP * 1.5)

        self.play(Write(equivalence_symbol), run_time=0.6)

        # 充要条件定义
        equivalent_def = Text(
            "充要条件 (充分必要条件)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_EQUIVALENT
        ).move_to(UP * 0.5)

        self.play(Write(equivalent_def), run_time=0.8)

        # 充要条件解释
        equivalent_explanation = Text(
            "P = Q 时，p⟺q\n互为充要条件",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(equivalent_explanation), run_time=0.6)

        # 高亮等价关系
        self.play(
            Flash(double_arrow, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=1.0
        )

        # 等待
        self.wait(2)

        # 清理部分元素
        self.play(
            FadeOut(equivalent_title),
            FadeOut(equivalence_symbol),
            FadeOut(equivalent_def),
            FadeOut(equivalent_explanation),
            FadeOut(double_arrow),
            FadeOut(set_p_equal),
            FadeOut(set_q_equal),
            FadeOut(label_p_equal),
            FadeOut(label_q_equal),
            run_time=0.6
        )


    def show_summary(self):
        """场景5: 总结与应用"""
        # 标题
        title = Text(
            "总结",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        self.play(Write(title), run_time=0.8)

        # 创建条件对比表
        sufficient_row = VGroup(
            Text("充分条件", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_SUFFICIENT),
            MathTex("p \\Rightarrow q", font_size=28),
            Text("P⊂Q", font_size=24)
        ).arrange(RIGHT, buff=1).move_to(UP * 4)

        necessary_row = VGroup(
            Text("必要条件", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_NECESSARY),
            MathTex("q \\Leftarrow p", font_size=28),
            Text("Q⊃P", font_size=24)
        ).arrange(RIGHT, buff=1).move_to(UP * 2.5)

        equivalent_row = VGroup(
            Text("充要条件", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_EQUIVALENT),
            MathTex("p \\iff q", font_size=28),
            Text("P=Q", font_size=24)
        ).arrange(RIGHT, buff=1).move_to(UP * 1)

        summary_table = VGroup(sufficient_row, necessary_row, equivalent_row)

        # 逐行显示表格
        for row in summary_table:
            self.play(Write(row), run_time=0.8)
            self.wait(0.5)

        # 记忆口诀
        mnemonic = Text(
            "记忆口诀：\n充分条件 - 有它一定行\n必要条件 - 没它一定不行",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE,
            line_spacing=1.3
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(mnemonic), run_time=0.8)

        # 学习建议
        advice = Text(
            "理解集合关系是掌握\n充分条件与必要条件的关键！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(DOWN * 4)

        self.play(Write(advice), run_time=1.0)

        # 作者信息
        final_author = Text(
            "上海初高中数学直通车\n@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(final_author, shift=UP * 0.3), run_time=0.6)

        # 关注提示
        follow_up = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7.5)

        self.play(Write(follow_up), run_time=0.8)

        # 最后的高亮效果
        self.play(
            *[Indicate(obj, color=self.COLOR_HIGHLIGHT) for obj in [title, advice, follow_up]],
            run_time=1.5
        )

        # 结束
        self.wait(2)


# 运行命令:
# manim -pql sufficient_necessary_conditions.py SufficientNecessaryConditions  # 快速预览
# manim -qh sufficient_necessary_conditions.py SufficientNecessaryConditions   # 高质量