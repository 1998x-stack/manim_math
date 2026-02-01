"""
相反数 (Opposite Numbers) - Manim 教学动画
使用 Manim 创建的中学数学教学视频

内容: 相反数的定义、性质和应用
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


class OppositeNumbers(Scene):
    """
    相反数教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 数轴引入 - 建立坐标系
    3. 相反数定义 - 核心概念
    4. 更多例子 - 巩固理解
    5. 特殊情况 - 0的相反数
    6. 总结与关注 - 知识回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 正数
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 负数
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_ORIGIN = "#2ecc71"       # 绿色 - 原点
        self.COLOR_NUMBERLINE = WHITE       # 白色 - 数轴
        
        # 字体大小规范
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 24
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        self.FONT_FORMULA = 28
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_number_line()
        self.scene_3_definition()
        self.scene_4_more_examples()
        self.scene_5_special_case()
        self.scene_6_summary()
    
    def setup_geometry(self):
        """初始化数轴和所有几何元素"""
        # 数轴参数
        self.NUMBER_LINE_LENGTH = 7.0  # 数轴总长度
        self.NUMBER_LINE_Y = 0.5       # 数轴垂直位置
        self.NUMBER_LINE_RANGE = [-5, 5]  # 数轴范围
        
        # 计算单位长度
        total_range = self.NUMBER_LINE_RANGE[1] - self.NUMBER_LINE_RANGE[0]
        self.UNIT_LENGTH = self.NUMBER_LINE_LENGTH / total_range
        
        # 原点位置
        self.ORIGIN_POS = np.array([0, self.NUMBER_LINE_Y, 0])
        
        print(f"✓ 几何初始化完成: 单位长度 = {self.UNIT_LENGTH:.3f}")
    
    def get_number_position(self, n):
        """计算数字 n 在数轴上的位置"""
        return self.ORIGIN_POS + RIGHT * n * self.UNIT_LENGTH
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "3 和 -3 有什么关系?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE + 4,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 两个神秘数字
        num_3 = MathTex(
            "3",
            font_size=self.FONT_TITLE * 2,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 2 + UP * 3)
        
        num_neg3 = MathTex(
            "-3",
            font_size=self.FONT_TITLE * 2,
            color=self.COLOR_SECONDARY
        ).move_to(RIGHT * 2 + UP * 3)
        
        self.play(
            FadeIn(num_3, scale=1.2),
            run_time=0.5
        )
        self.wait(0.3)
        
        self.play(
            FadeIn(num_neg3, scale=1.2),
            run_time=0.5
        )
        
        # 闪烁效果
        self.play(
            Flash(num_3, color=self.COLOR_PRIMARY, flash_radius=0.5),
            Flash(num_neg3, color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.5
        )
        
        # 提示文字
        hint = Text(
            "它们是相反数!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(num_3),
            FadeOut(num_neg3),
            FadeOut(hint),
            run_time=0.5
        )
    
    def scene_2_number_line(self):
        """场景2: 数轴引入"""
        # 创建数轴
        number_line = NumberLine(
            x_range=self.NUMBER_LINE_RANGE + [1],  # [min, max, step]
            length=self.NUMBER_LINE_LENGTH,
            include_numbers=False,
            include_ticks=True,
            tick_size=0.1,
            numbers_to_exclude=[],
            color=self.COLOR_NUMBERLINE,
            stroke_width=3
        ).move_to(self.ORIGIN_POS)
        
        # 保存数轴对象供后续使用
        self.number_line = number_line
        
        # 数轴生长
        self.play(Create(number_line), run_time=1.0)
        
        # 添加数字标签
        labels = VGroup()
        for n in range(self.NUMBER_LINE_RANGE[0], self.NUMBER_LINE_RANGE[1] + 1):
            if n == 0:
                continue  # 原点单独处理
            
            label = MathTex(
                str(n),
                font_size=self.FONT_LABEL,
                color=self.COLOR_PRIMARY if n > 0 else self.COLOR_SECONDARY
            ).move_to(self.get_number_position(n) + DOWN * 0.4)
            labels.add(label)
        
        self.labels = labels
        self.play(FadeIn(labels, lag_ratio=0.05), run_time=1.5)
        
        # 原点特殊标记
        origin_dot = Dot(
            self.ORIGIN_POS,
            radius=0.12,
            color=self.COLOR_ORIGIN
        )
        
        origin_label = MathTex(
            "0",
            font_size=self.FONT_LABEL + 4,
            color=self.COLOR_ORIGIN
        ).move_to(self.ORIGIN_POS + DOWN * 0.5)
        
        self.origin_dot = origin_dot
        self.origin_label = origin_label
        
        self.play(
            FadeIn(origin_dot, scale=1.5),
            run_time=0.5
        )
        self.play(
            Indicate(origin_dot, color=self.COLOR_ORIGIN),
            run_time=0.5
        )
        self.play(
            FadeIn(origin_label),
            run_time=0.4
        )
        
        # 方向说明
        chinese_pos = Text(
            "正数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIMARY
        ).move_to(self.get_number_position(4.5) + UP * 0.5)
        
        arrow_pos = Arrow(
            start=self.get_number_position(3.5) + UP * 0.3,
            end=self.get_number_position(4.3) + UP * 0.3,
            color=self.COLOR_PRIMARY,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        
        chinese_neg = Text(
            "负数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(self.get_number_position(-4.5) + UP * 0.5)
        
        arrow_neg = Arrow(
            start=self.get_number_position(-3.5) + UP * 0.3,
            end=self.get_number_position(-4.3) + UP * 0.3,
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(
            GrowArrow(arrow_pos),
            GrowArrow(arrow_neg),
            run_time=0.6
        )
        self.play(
            FadeIn(chinese_pos),
            FadeIn(chinese_neg),
            run_time=0.4
        )
        
        # 说明文字
        explanation = Text(
            "数轴上,原点左边是负数,右边是正数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理方向说明
        self.play(
            FadeOut(explanation),
            FadeOut(arrow_pos),
            FadeOut(arrow_neg),
            FadeOut(chinese_pos),
            FadeOut(chinese_neg),
            run_time=0.5
        )
    
    def scene_3_definition(self):
        """场景3: 相反数定义"""
        # 标题
        title_chinese = Text(
            "相反数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        )
        
        title_english = Text(
            "Opposite Numbers",
            font_size=self.FONT_SMALL + 2,
            color=GRAY_A
        )
        
        title_group = VGroup(title_chinese, title_english).arrange(DOWN, buff=0.2)
        title_group.move_to(UP * 5.5)
        
        self.play(Write(title_chinese), run_time=0.6)
        self.play(FadeIn(title_english), run_time=0.3)
        
        # 在数轴上标记 3 和 -3
        dot_3 = Dot(
            self.get_number_position(3),
            radius=0.15,
            color=self.COLOR_PRIMARY
        )
        
        label_3 = MathTex(
            "3",
            font_size=self.FONT_LABEL + 4,
            color=self.COLOR_PRIMARY
        ).next_to(dot_3, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_3, scale=1.5),
            run_time=0.5
        )
        self.play(FadeIn(label_3), run_time=0.3)
        
        # 标记 -3
        dot_neg3 = Dot(
            self.get_number_position(-3),
            radius=0.15,
            color=self.COLOR_SECONDARY
        )
        
        label_neg3 = MathTex(
            "-3",
            font_size=self.FONT_LABEL + 4,
            color=self.COLOR_SECONDARY
        ).next_to(dot_neg3, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_neg3, scale=1.5),
            run_time=0.5
        )
        self.play(FadeIn(label_neg3), run_time=0.3)
        
        self.wait(0.5)
        
        # 到原点的虚线
        dash_3 = DashedLine(
            self.get_number_position(3),
            self.ORIGIN_POS,
            color=self.COLOR_PRIMARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        dash_neg3 = DashedLine(
            self.get_number_position(-3),
            self.ORIGIN_POS,
            color=self.COLOR_SECONDARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(dash_3), run_time=0.5)
        self.play(Create(dash_neg3), run_time=0.5)
        
        # 距离标注
        dist_3 = MathTex(
            "3",
            font_size=self.FONT_SMALL + 2,
            color=self.COLOR_PRIMARY
        ).move_to(self.get_number_position(1.5) + DOWN * 0.3)
        
        dist_neg3 = MathTex(
            "3",
            font_size=self.FONT_SMALL + 2,
            color=self.COLOR_SECONDARY
        ).move_to(self.get_number_position(-1.5) + DOWN * 0.3)
        
        self.play(
            FadeIn(dist_3),
            FadeIn(dist_neg3),
            run_time=0.5
        )
        
        # 高亮距离相等
        self.play(
            Indicate(dist_3, color=self.COLOR_HIGHLIGHT),
            Indicate(dist_neg3, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # 定义文字
        def_1 = Text(
            "只有符号不同的两个数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        def_2 = Text(
            "叫做互为相反数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(def_1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(def_2, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title_group),
            FadeOut(dash_3),
            FadeOut(dash_neg3),
            FadeOut(dist_3),
            FadeOut(dist_neg3),
            FadeOut(def_1),
            FadeOut(def_2),
            FadeOut(dot_3),
            FadeOut(dot_neg3),
            FadeOut(label_3),
            FadeOut(label_neg3),
            run_time=0.6
        )
    
    def scene_4_more_examples(self):
        """场景4: 更多例子"""
        # 例子标题
        example_title = Text(
            "更多例子",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(example_title), run_time=0.4)
        
        # 例子 1: 5 和 -5
        dot_5 = Dot(self.get_number_position(5), radius=0.12, color=self.COLOR_PRIMARY)
        label_5 = MathTex("5", font_size=self.FONT_LABEL, color=self.COLOR_PRIMARY).next_to(dot_5, UP, buff=0.15)
        
        self.play(FadeIn(dot_5, scale=1.3), run_time=0.5)
        self.play(FadeIn(label_5), run_time=0.3)
        
        # 对称生成 -5
        dot_neg5 = Dot(self.get_number_position(-5), radius=0.12, color=self.COLOR_SECONDARY)
        label_neg5 = MathTex("-5", font_size=self.FONT_LABEL, color=self.COLOR_SECONDARY).next_to(dot_neg5, UP, buff=0.15)
        
        self.play(
            TransformFromCopy(dot_5, dot_neg5),
            run_time=0.5
        )
        self.play(FadeIn(label_neg5), run_time=0.3)
        
        self.wait(0.8)
        
        # 例子 2: 1.5 和 -1.5
        dot_1_5 = Dot(self.get_number_position(1.5), radius=0.12, color=self.COLOR_PRIMARY)
        label_1_5 = MathTex("1.5", font_size=self.FONT_LABEL - 2, color=self.COLOR_PRIMARY).next_to(dot_1_5, UP, buff=0.15)
        
        self.play(FadeIn(dot_1_5, scale=1.3), run_time=0.5)
        self.play(FadeIn(label_1_5), run_time=0.3)
        
        dot_neg1_5 = Dot(self.get_number_position(-1.5), radius=0.12, color=self.COLOR_SECONDARY)
        label_neg1_5 = MathTex("-1.5", font_size=self.FONT_LABEL - 2, color=self.COLOR_SECONDARY).next_to(dot_neg1_5, UP, buff=0.15)
        
        self.play(
            TransformFromCopy(dot_1_5, dot_neg1_5),
            run_time=0.5
        )
        self.play(FadeIn(label_neg1_5), run_time=0.3)
        
        self.wait(0.8)
        
        # 公式卡片
        formula_1_chinese = Text(
            "的相反数是",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA - 4,
            color=WHITE
        )
        formula_1_a = MathTex("a", font_size=self.FONT_FORMULA, color=self.COLOR_PRIMARY)
        formula_1_neg_a = MathTex("-a", font_size=self.FONT_FORMULA, color=self.COLOR_SECONDARY)
        
        formula_1 = VGroup(formula_1_a, formula_1_chinese, formula_1_neg_a).arrange(RIGHT, buff=0.2)
        formula_1.move_to(UP * 3.5)
        
        self.play(FadeIn(formula_1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 公式 2
        formula_2 = MathTex(
            r"-(-a) = a",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(formula_2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 公式 3
        formula_3 = MathTex(
            r"a + (-a) = 0",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(formula_3, shift=UP * 0.2, scale=1.1), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(dot_5),
            FadeOut(label_5),
            FadeOut(dot_neg5),
            FadeOut(label_neg5),
            FadeOut(dot_1_5),
            FadeOut(label_1_5),
            FadeOut(dot_neg1_5),
            FadeOut(label_neg1_5),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(formula_3),
            run_time=0.6
        )
    
    def scene_5_special_case(self):
        """场景5: 特殊情况 - 0的相反数"""
        # 原点放大
        self.play(
            self.origin_dot.animate.scale(1.8),
            self.origin_label.animate.scale(1.3),
            run_time=0.5
        )
        
        # 原点闪烁
        self.play(
            Flash(self.origin_dot, color=self.COLOR_ORIGIN, flash_radius=0.5),
            run_time=0.5
        )
        
        # 特殊标题
        special_title = Text(
            "特殊情况",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(special_title), run_time=0.6)
        
        # 说明 1
        special_1 = Text(
            "0 的相反数是 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_ORIGIN
        ).move_to(UP * 4)
        
        self.play(FadeIn(special_1, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 说明 2
        special_2 = Text(
            "因为 0 到原点的距离是 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 3)
        
        self.play(FadeIn(special_2, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 公式
        special_formula = MathTex(
            r"0 + 0 = 0",
            font_size=self.FONT_FORMULA + 8,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(special_formula, scale=1.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(special_title),
            FadeOut(special_1),
            FadeOut(special_2),
            FadeOut(special_formula),
            run_time=0.5
        )
        
        # 原点恢复
        self.play(
            self.origin_dot.animate.scale(1/1.8),
            self.origin_label.animate.scale(1/1.3),
            run_time=0.4
        )
    
    def scene_6_summary(self):
        """场景6: 总结与关注"""
        # 数轴淡出
        self.play(
            FadeOut(self.number_line),
            FadeOut(self.labels),
            FadeOut(self.origin_dot),
            FadeOut(self.origin_label),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "相反数知识点总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点列表
        point_1 = Text(
            "① 符号不同, 绝对值相等",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4.5)
        
        point_2 = Text(
            "② 在数轴上关于原点对称",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 3.5)
        
        point_3_chinese = Text(
            "③ ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        point_3_math = MathTex(
            r"a + (-a) = 0",
            font_size=self.FONT_BODY + 2,
            color=self.COLOR_HIGHLIGHT
        )
        point_3 = VGroup(point_3_chinese, point_3_math).arrange(RIGHT, buff=0.1)
        point_3.move_to(UP * 2.5)
        
        point_4 = Text(
            "④ 0 的相反数是 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.5)
        
        # 依次显示要点
        self.play(FadeIn(point_1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(point_2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(point_3, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(point_4, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE + 4,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_B
        ).move_to(DOWN * 1.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        # 装饰圆点
        decorations = VGroup(*[
            Dot(
                follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                radius=0.08,
                color=self.COLOR_HIGHLIGHT
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in decorations],
            run_time=0.5
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql opposite_numbers.py OppositeNumbers  # 快速预览
# manim -qh opposite_numbers.py OppositeNumbers   # 高质量渲染