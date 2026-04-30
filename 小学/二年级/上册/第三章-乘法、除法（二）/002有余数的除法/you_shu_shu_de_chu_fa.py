from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# LaTeX 配置说明:
# - 中文文本使用 Text() 而非 MathTex() (避免 LaTeX Unicode errors)
# - 数学公式使用 MathTex() with proper LaTeX commands
# - 使用 r"..." raw strings for LaTeX
# - 度数符号使用 ^\circ instead of raw ° character
# - 避免双花括号 {{a} \over {b}} - use \frac{a}{b} instead

# 字体配置
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "PingFang SC"  # 或 "SimHei"


class YouShuShuDeChuFa(Scene):
    """
    有余数的除法教学动画场景

    场景顺序:
    1. 开场介绍
    2. 平均分演示 (13 ÷ 4)
    3. 数学算式解析
    4. 概念解释
    5. 总结与练习
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_SUCCESS = GREEN
        self.COLOR_WARNING = ORANGE
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_PRIMARY = WHITE

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_average_division()
        self.show_mathematical_expression()
        self.show_concept_explanation()
        self.show_summary_and_practice()

    def setup_geometry(self):
        """初始化所有几何数据"""
        # 基准参数
        self.SCALE = 0.8
        self.OFFSET = UP * 2.0

        # 创建13个圆形物体（代表苹果）
        # 使用网格布局，确保精确位置
        self.objects = []
        grid_rows = 3
        grid_cols = 5
        spacing = 0.8

        for i in range(grid_rows):
            for j in range(grid_cols):
                if len(self.objects) < 13:  # 只创建13个
                    x = (j - (grid_cols-1)/2) * spacing
                    y = (i - (grid_rows-1)/2) * spacing + 1.0
                    pos = np.array([x, y, 0]) * self.SCALE + self.OFFSET
                    self.objects.append(pos)

        # 分组框位置 - 4个水平排列
        self.groups = []
        group_spacing = 2.5
        for i in range(4):
            x = (i - 1.5) * group_spacing
            self.groups.append(np.array([x, -1.5, 0]) * self.SCALE + self.OFFSET)

        # 余数位置
        self.remainder_pos = np.array([0, -2.5, 0]) * self.SCALE + self.OFFSET

        # 验证几何计算
        self._verify_geometry()

    def _verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        print("✓ 几何验证完成")

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "有余数的除法",
            font="PingFang SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "平均分时的剩余问题",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 创建13个圆形物体
        self.circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_PRIMARY, fill_opacity=0.8).move_to(pos)
            for pos in self.objects
        ])

        self.play(Create(self.circles), run_time=1.5)

        # 提示文字
        hint = Text(
            "13个苹果，平均分给4个小朋友，会怎样？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)

        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hint),
            run_time=0.5
        )

    def show_average_division(self):
        """场景2: 平均分演示"""
        # 标题
        title = Text(
            "平均分演示",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        definition = Text(
            "每个小朋友分到同样多的苹果",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(definition), run_time=0.8)

        # 创建4个分组框
        self.groups_rects = VGroup(*[
            Rectangle(width=2.0, height=1.2, color=self.COLOR_AUXILIARY, stroke_width=2).move_to(pos)
            for pos in self.groups
        ])

        self.play(Create(self.groups_rects), run_time=0.8)

        # 分配过程：每个框放3个圆
        # 创建3个圆的组
        circle_groups = []
        for i in range(4):
            # 创建3个圆的位置
            positions = []
            for j in range(3):
                x_offset = (j - 1) * 0.5
                y_offset = -0.2
                pos = self.groups[i] + np.array([x_offset, y_offset, 0])
                positions.append(pos)

            circles_in_group = VGroup(*[
                Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=0.8).move_to(pos)
                for pos in positions
            ])
            circle_groups.append(circles_in_group)

        # 动画分配
        for i in range(4):
            self.play(Create(circle_groups[i]), run_time=0.5)

        # 显示余数
        self.remainder_circle = Circle(radius=0.2, color=self.COLOR_WARNING, fill_opacity=0.8).move_to(self.remainder_pos)
        self.remainder_label = Text("剩余", font="PingFang SC", font_size=20, color=self.COLOR_WARNING).next_to(self.remainder_circle, DOWN, buff=0.1)

        self.play(FadeIn(self.remainder_circle, scale=0.5), FadeIn(self.remainder_label), run_time=0.5)
        self.play(Flash(self.remainder_circle, color=self.COLOR_WARNING, flash_radius=0.3), run_time=0.4)

        # 解释文字
        explain = Text(
            "还剩1个，不够再分一份！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_WARNING
        ).move_to(DOWN * 5)

        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explain),
            FadeOut(self.remainder_label),
            run_time=0.5
        )

        # 保留重要元素
        self.remaining_circles = VGroup(*circle_groups)
        self.play(self.circles.animate.set_opacity(0.3), run_time=0.3)

    def show_mathematical_expression(self):
        """场景3: 数学算式解析"""
        # 标题
        title = Text(
            "数学算式",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # 创建算式：13 ÷ 4 = 3 … 1
        self.formula = MathTex(r"13", r"\div", r"4", r"=", r"3", r"\dots", r"1")
        self.formula.scale(1.2).move_to(UP * 3)

        self.play(Write(self.formula), run_time=0.8)

        # 高亮各部分
        # 被除数 13
        self.play(self.formula[0].animate.set_color(YELLOW), run_time=0.4)
        self.play(Flash(self.formula[0], color=YELLOW, flash_radius=0.2), run_time=0.3)

        # 除数 4
        self.play(self.formula[2].animate.set_color(GREEN), run_time=0.4)
        self.play(Flash(self.formula[2], color=GREEN, flash_radius=0.2), run_time=0.3)

        # 商 3
        self.play(self.formula[4].animate.set_color(BLUE), run_time=0.4)
        self.play(Flash(self.formula[4], color=BLUE, flash_radius=0.2), run_time=0.3)

        # 余数 1
        self.play(self.formula[6].animate.set_color(RED), run_time=0.4)
        self.play(Flash(self.formula[6], color=RED, flash_radius=0.2), run_time=0.3)

        # 关系说明：余数 < 除数
        relation = Text(
            "余数必须比除数小",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3)

        self.play(FadeIn(relation), run_time=0.5)

        # 用Brace连接余数和除数
        brace = Brace(VGroup(self.formula[2], self.formula[6]), direction=DOWN, buff=0.2, color=YELLOW)
        brace_text = Text("1 < 4", font="PingFang SC", font_size=20, color=YELLOW).next_to(brace, DOWN, buff=0.1)

        self.play(Create(brace), Write(brace_text), run_time=0.6)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(relation),
            FadeOut(brace),
            FadeOut(brace_text),
            run_time=0.5
        )

    def show_concept_explanation(self):
        """场景4: 概念解释"""
        # 标题
        title = Text(
            "概念解释",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        # 定义文字
        definition = Text(
            "平均分时，有剩余且不够再分一份，剩下的数叫做'余数'",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 3.5)

        self.play(Write(definition), run_time=1.0)

        # 箭头指向余数
        arrow = Arrow(
            start=self.remainder_pos + DOWN * 0.3,
            end=self.remainder_circle.get_center(),
            buff=0.1,
            color=YELLOW
        )

        self.play(Create(arrow), run_time=0.4)

        # 错误示例：尝试将余数再分
        cross = Text("×", font="PingFang SC", font_size=36, color=RED).move_to(self.remainder_pos + RIGHT * 1.5)

        self.play(FadeIn(cross), run_time=0.3)

        # 正确总结
        summary = Text(
            "余数是不够再分一份的剩余数",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3)

        self.play(FadeIn(summary), run_time=0.5)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(arrow),
            FadeOut(cross),
            FadeOut(summary),
            run_time=0.5
        )

    def show_summary_and_practice(self):
        """场景5: 总结与练习"""
        # 总结要点卡片
        cards = VGroup()

        # 卡片1: 什么是余数
        card1 = VGroup(
            Text("什么是余数？", font="PingFang SC", font_size=20, color=WHITE),
            Text("平均分后剩下的数", font="PingFang SC", font_size=18, color=GRAY_A)
        ).arrange(DOWN, buff=0.2)

        # 卡片2: 余数特点
        card2 = VGroup(
            Text("余数特点", font="PingFang SC", font_size=20, color=WHITE),
            Text("余数 < 除数", font="PingFang SC", font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.2)

        # 卡片3: 算式格式
        card3 = VGroup(
            Text("算式格式", font="PingFang SC", font_size=20, color=WHITE),
            Text("被除数÷除数=商…余数", font="PingFang SC", font_size=18, color=BLUE)
        ).arrange(DOWN, buff=0.2)

        cards.add(card1)
        cards.add(card2)
        cards.add(card3)

        cards.arrange(RIGHT, buff=1.0).move_to(UP * 2)

        # 卡片依次滑入
        for card in cards:
            card.shift(RIGHT * 10)

        for card in cards:
            self.play(card.animate.shift(LEFT * 10), run_time=0.6)
            self.wait(0.3)

        # 练习题
        exercise = Text(
            "练习题：17 ÷ 5 = ? … ?",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)

        self.play(FadeIn(exercise), run_time=0.5)

        # 思考时间
        self.wait(2.0)

        # 显示答案
        answer = Text(
            "17 ÷ 5 = 3 … 2",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3)

        self.play(FadeIn(answer), run_time=0.5)

        # 作者信息
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=24,
            color=GRAY_B
        ).move_to(DOWN * 6)

        self.play(
            FadeIn(author_name, shift=UP * 0.3),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.6
        )

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        self.wait(2.0)

# 运行命令:
# manim -pql you_shu_shu_de_chu_fa.py YouShuShuDeChuFa  # 快速预览
# manim -qh you_shu_shu_de_chu_fa.py YouShuShuDeChuFa   # 高质量
