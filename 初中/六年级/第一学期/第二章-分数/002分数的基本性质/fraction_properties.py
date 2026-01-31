"""
分数的基本性质 - Fraction Basic Properties Animation
使用 Manim 创建的小学数学教学视频

内容: 分数的分子和分母同时乘以或除以同一个不为零的数,分数的值不变
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql fraction_properties.py FractionProperties  # 快速预览
  manim -qh fraction_properties.py FractionProperties   # 高质量渲染
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FractionProperties(Scene):
    """
    分数的基本性质教学动画场景
    
    场景顺序:
    1. 开场钩子 - 三个分数相等吗?
    2. 视觉验证 - 分数条展示
    3. 核心概念 - 分数基本性质说明
    4. 乘法性质 - 分子分母同时乘
    5. 除法性质 - 分子分母同时除(约分)
    6. 应用示例 - 通分与约分
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_FRACTION_BASE = "#3498db"     # 蓝色 - 基础分数
        self.COLOR_MULTIPLY = "#e74c3c"          # 红色 - 乘法操作
        self.COLOR_DIVIDE = "#2ecc71"            # 绿色 - 除法操作
        self.COLOR_HIGHLIGHT = YELLOW            # 黄色 - 高亮强调
        self.COLOR_AUXILIARY = GRAY_B            # 灰色 - 辅助线/说明
        self.COLOR_EQUAL = "#f39c12"             # 橙色 - 等号/等值
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_visual_proof()
        self.show_core_concept()
        self.show_multiply_property()
        self.show_divide_property()
        self.show_applications()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化分数条和位置参数"""
        # 分数条参数
        self.BAR_WIDTH = 6.0
        self.BAR_HEIGHT = 0.8
        self.BAR_CENTER = UP * 2
        
        # 公式区域
        self.FORMULA_CENTER = DOWN * 2
        
        print("✓ 几何参数初始化完成")
    
    def create_fraction_bar(self, parts, filled, position, color=None):
        """
        创建可视化分数条
        
        参数:
        - parts: 总份数
        - filled: 填充份数
        - position: 中心位置
        - color: 填充颜色
        """
        if color is None:
            color = self.COLOR_FRACTION_BASE
        
        # 外框
        outline = Rectangle(
            width=self.BAR_WIDTH, 
            height=self.BAR_HEIGHT,
            color=WHITE,
            stroke_width=3
        )
        outline.move_to(position)
        
        # 分割线
        lines = VGroup()
        part_width = self.BAR_WIDTH / parts
        for i in range(1, parts):
            x_offset = -self.BAR_WIDTH/2 + i * part_width
            line = Line(
                position + UP*self.BAR_HEIGHT/2 + RIGHT*x_offset,
                position + DOWN*self.BAR_HEIGHT/2 + RIGHT*x_offset,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
            lines.add(line)
        
        # 填充部分
        filled_rects = VGroup()
        for i in range(filled):
            x_start = -self.BAR_WIDTH/2 + i * part_width
            rect = Rectangle(
                width=part_width - 0.02,  # 留小间隙
                height=self.BAR_HEIGHT - 0.02,
                fill_color=color,
                fill_opacity=0.7,
                stroke_width=0
            )
            rect.move_to(position + RIGHT*(x_start + part_width/2))
            filled_rects.add(rect)
        
        return VGroup(outline, lines, filled_rects)
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这三个分数相等吗?",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三个分数依次出现
        frac_1 = MathTex(r"\frac{1}{2}", font_size=60, color=WHITE).move_to(UP * 3.5 + LEFT * 2.5)
        frac_2 = MathTex(r"\frac{2}{4}", font_size=60, color=WHITE).move_to(UP * 3.5)
        frac_3 = MathTex(r"\frac{3}{6}", font_size=60, color=WHITE).move_to(UP * 3.5 + RIGHT * 2.5)
        
        self.play(FadeIn(frac_1, scale=0.8), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(frac_2, scale=0.8), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(frac_3, scale=0.8), run_time=0.5)
        
        # 问号闪烁
        question_mark = Text("?", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(UP * 2)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.3)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.4
        )
        
        # 保存分数以便后续使用
        self.frac_group = VGroup(frac_1, frac_2, frac_3)
    
    def show_visual_proof(self):
        """场景2: 视觉验证 - 分数条展示"""
        # 将分数移到顶部
        self.play(
            self.frac_group.animate.arrange(RIGHT, buff=1.2).move_to(UP * 6).scale(0.7),
            run_time=0.8
        )
        
        # 第一个分数条 (1/2)
        bar_1 = self.create_fraction_bar(2, 1, UP * 3.5)
        label_1 = Text("1/2", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(bar_1, LEFT, buff=0.3)
        
        self.play(
            Create(bar_1[0]),  # 外框
            FadeIn(label_1),
            run_time=0.6
        )
        self.play(Create(bar_1[1]), run_time=0.5)  # 分割线
        self.play(FadeIn(bar_1[2]), run_time=0.6)   # 填充
        
        self.wait(0.3)
        
        # 第二个分数条 (2/4)
        bar_2 = self.create_fraction_bar(4, 2, UP * 2)
        label_2 = Text("2/4", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(bar_2, LEFT, buff=0.3)
        
        self.play(
            Create(bar_2[0]),
            FadeIn(label_2),
            run_time=0.6
        )
        self.play(Create(bar_2[1]), run_time=0.5)
        self.play(FadeIn(bar_2[2]), run_time=0.6)
        
        self.wait(0.3)
        
        # 第三个分数条 (3/6)
        bar_3 = self.create_fraction_bar(6, 3, UP * 0.5)
        label_3 = Text("3/6", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(bar_3, LEFT, buff=0.3)
        
        self.play(
            Create(bar_3[0]),
            FadeIn(label_3),
            run_time=0.6
        )
        self.play(Create(bar_3[1]), run_time=0.5)
        self.play(FadeIn(bar_3[2]), run_time=0.6)
        
        self.wait(0.5)
        
        # 等号连接
        equal_1 = MathTex("=", font_size=50, color=self.COLOR_EQUAL).move_to(UP * 2.75 + LEFT * 3.5)
        equal_2 = MathTex("=", font_size=50, color=self.COLOR_EQUAL).move_to(UP * 1.25 + LEFT * 3.5)
        
        self.play(Write(equal_1), Write(equal_2), run_time=0.5)
        
        # 结论
        conclusion = Text(
            "它们确实相等!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(bar_1, bar_2, bar_3, label_1, label_2, label_3)),
            FadeOut(equal_1),
            FadeOut(equal_2),
            FadeOut(conclusion),
            FadeOut(self.frac_group),
            run_time=0.6
        )
    
    def show_core_concept(self):
        """场景3: 核心概念引入"""
        # 标题
        title = Text(
            "分数的基本性质",
            font="Noto Sans CJK SC",
            font_size=44,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 性质描述 (分两行)
        property_line1 = Text(
            "分数的分子和分母",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4)
        
        property_line2 = Text(
            "同时乘以或除以同一个不为零的数",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 3.2)
        
        property_line3 = Text(
            "分数的值不变",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.4)
        
        self.play(FadeIn(property_line1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(property_line2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(property_line3), run_time=0.6)
        
        # 高亮框
        highlight_box = SurroundingRectangle(
            VGroup(property_line2, property_line3),
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(highlight_box), run_time=0.8)
        self.wait(0.5)
        
        # 公式预告
        formula_preview = Text(
            "用公式表达:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(formula_preview), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property_line1),
            FadeOut(property_line2),
            FadeOut(property_line3),
            FadeOut(highlight_box),
            FadeOut(formula_preview),
            run_time=0.5
        )
    
    def show_multiply_property(self):
        """场景4: 乘法性质演示"""
        # 标题
        title = Text(
            "乘法性质",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_MULTIPLY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 基础分数
        base_frac = MathTex(
            r"\frac{1}{2}",
            font_size=70,
            color=WHITE
        ).move_to(LEFT * 3 + UP * 3)
        
        self.play(FadeIn(base_frac, scale=0.8), run_time=0.6)
        
        # 说明文字
        explain_1 = Text(
            "分子分母同时乘以 2",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        
        # 乘号和数字 (分别作用于分子分母)
        multiply_top = MathTex(r"\times 2", font_size=40, color=self.COLOR_MULTIPLY).next_to(base_frac[0][0], RIGHT, buff=0.3)
        multiply_bottom = MathTex(r"\times 2", font_size=40, color=self.COLOR_MULTIPLY).next_to(base_frac[0][2], RIGHT, buff=0.3)
        
        self.play(
            Write(multiply_top),
            Write(multiply_bottom),
            run_time=0.8
        )
        
        # 高亮分子分母 (强调"同时")
        self.play(
            Indicate(base_frac[0][0], color=self.COLOR_MULTIPLY),
            Indicate(base_frac[0][2], color=self.COLOR_MULTIPLY),
            run_time=0.8
        )
        
        # 箭头
        arrow_1 = Arrow(
            LEFT * 0.5 + UP * 3,
            RIGHT * 0.5 + UP * 3,
            color=self.COLOR_EQUAL,
            buff=0.3,
            stroke_width=6
        )
        
        self.play(GrowArrow(arrow_1), run_time=0.6)
        
        # 结果分数
        result_frac_1 = MathTex(
            r"\frac{2}{4}",
            font_size=70,
            color=WHITE
        ).move_to(RIGHT * 3 + UP * 3)
        
        self.play(FadeIn(result_frac_1, scale=0.8), run_time=0.6)
        
        # 等号
        equal_sign_1 = MathTex("=", font_size=60, color=self.COLOR_EQUAL).move_to(UP * 3)
        self.play(Write(equal_sign_1), run_time=0.4)
        
        self.wait(0.8)
        
        # 再次变换 (1/2 → 3/6)
        self.play(
            FadeOut(multiply_top),
            FadeOut(multiply_bottom),
            FadeOut(explain_1),
            run_time=0.3
        )
        
        explain_2 = Text(
            "再同时乘以 3",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5)
        
        self.play(FadeIn(explain_2), run_time=0.4)
        
        # 新的乘法
        multiply_top_2 = MathTex(r"\times 3", font_size=40, color=self.COLOR_MULTIPLY).next_to(base_frac[0][0], RIGHT, buff=0.3)
        multiply_bottom_2 = MathTex(r"\times 3", font_size=40, color=self.COLOR_MULTIPLY).next_to(base_frac[0][2], RIGHT, buff=0.3)
        
        self.play(
            Write(multiply_top_2),
            Write(multiply_bottom_2),
            run_time=0.6
        )
        
        # 第二个结果
        result_frac_2 = MathTex(
            r"\frac{3}{6}",
            font_size=70,
            color=WHITE
        ).move_to(RIGHT * 3 + UP * 1.5)
        
        arrow_2 = Arrow(
            LEFT * 0.5 + UP * 1.5,
            RIGHT * 0.5 + UP * 1.5,
            color=self.COLOR_EQUAL,
            buff=0.3,
            stroke_width=6
        )
        
        equal_sign_2 = MathTex("=", font_size=60, color=self.COLOR_EQUAL).move_to(UP * 1.5)
        
        # 基础分数复制到新位置
        base_frac_2 = base_frac.copy().move_to(LEFT * 3 + UP * 1.5)
        
        self.play(
            FadeIn(base_frac_2),
            run_time=0.4
        )
        
        self.play(
            GrowArrow(arrow_2),
            FadeIn(result_frac_2, scale=0.8),
            run_time=0.6
        )
        
        self.play(Write(equal_sign_2), run_time=0.4)
        
        self.wait(0.5)
        
        # 清理上面的内容,准备显示公式
        self.play(
            FadeOut(VGroup(
                base_frac, result_frac_1, arrow_1, equal_sign_1,
                base_frac_2, result_frac_2, arrow_2, equal_sign_2,
                multiply_top_2, multiply_bottom_2, explain_2
            )),
            run_time=0.5
        )
        
        # 公式总结
        formula_box = Rectangle(
            width=7,
            height=1.5,
            color=self.COLOR_MULTIPLY,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=self.COLOR_MULTIPLY
        ).move_to(UP * 2.5)
        
        formula = MathTex(
            r"\frac{a}{b} = \frac{a \times k}{b \times k}",
            font_size=50,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Create(formula_box), run_time=0.5)
        self.play(Write(formula), run_time=1.0)
        
        # k≠0 条件
        condition = MathTex(
            r"(k \neq 0)",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, RIGHT, buff=0.3)
        
        self.play(FadeIn(condition), run_time=0.5)
        self.play(Indicate(condition, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        self.wait(1.2)
        
        # 将公式移到顶部保存
        formula_group = VGroup(formula_box, formula, condition)
        self.play(
            formula_group.animate.scale(0.6).move_to(UP * 5.5),
            FadeOut(title),
            run_time=0.6
        )
        
        self.multiply_formula = formula_group
    
    def show_divide_property(self):
        """场景5: 除法性质演示 (约分)"""
        # 标题
        title = Text(
            "除法性质 (约分)",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_DIVIDE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 大分数
        large_frac = MathTex(
            r"\frac{6}{12}",
            font_size=70,
            color=WHITE
        ).move_to(LEFT * 3 + UP * 3)
        
        self.play(FadeIn(large_frac, scale=0.8), run_time=0.6)
        
        # 说明文字
        explain_3 = Text(
            "分子分母同时除以 2",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(explain_3), run_time=0.5)
        
        # 除号和数字
        divide_top = MathTex(r"\div 2", font_size=40, color=self.COLOR_DIVIDE).next_to(large_frac[0][0], RIGHT, buff=0.3)
        divide_bottom = MathTex(r"\div 2", font_size=40, color=self.COLOR_DIVIDE).next_to(large_frac[0][2], RIGHT, buff=0.3)
        
        self.play(
            Write(divide_top),
            Write(divide_bottom),
            run_time=0.8
        )
        
        # 高亮
        self.play(
            Indicate(large_frac[0][0], color=self.COLOR_DIVIDE),
            Indicate(large_frac[0][2], color=self.COLOR_DIVIDE),
            run_time=0.8
        )
        
        # 除法动画 (数字缩小/划线效果)
        cross_top = Line(
            large_frac[0][0].get_corner(UL),
            large_frac[0][0].get_corner(DR),
            color=self.COLOR_DIVIDE,
            stroke_width=4
        )
        cross_bottom = Line(
            large_frac[0][2].get_corner(UL),
            large_frac[0][2].get_corner(DR),
            color=self.COLOR_DIVIDE,
            stroke_width=4
        )
        
        self.play(
            Create(cross_top),
            Create(cross_bottom),
            run_time=0.6
        )
        
        # 箭头
        arrow_3 = Arrow(
            LEFT * 0.5 + UP * 3,
            RIGHT * 0.5 + UP * 3,
            color=self.COLOR_EQUAL,
            buff=0.3,
            stroke_width=6
        )
        
        self.play(GrowArrow(arrow_3), run_time=0.6)
        
        # 简化后的分数
        simplified_frac_1 = MathTex(
            r"\frac{3}{6}",
            font_size=70,
            color=WHITE
        ).move_to(RIGHT * 3 + UP * 3)
        
        self.play(FadeIn(simplified_frac_1, scale=0.8), run_time=0.6)
        
        # 等号
        equal_sign_3 = MathTex("=", font_size=60, color=self.COLOR_EQUAL).move_to(UP * 3)
        self.play(Write(equal_sign_3), run_time=0.4)
        
        self.wait(0.8)
        
        # 再次约分 (3/6 → 1/2)
        self.play(
            FadeOut(divide_top),
            FadeOut(divide_bottom),
            FadeOut(cross_top),
            FadeOut(cross_bottom),
            FadeOut(explain_3),
            run_time=0.3
        )
        
        explain_4 = Text(
            "再同时除以 3",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(explain_4), run_time=0.4)
        
        # 标注3/6
        frac_36 = MathTex(
            r"\frac{3}{6}",
            font_size=70,
            color=WHITE
        ).move_to(LEFT * 3 + UP * 1.5)
        
        divide_top_2 = MathTex(r"\div 3", font_size=40, color=self.COLOR_DIVIDE).next_to(frac_36[0][0], RIGHT, buff=0.3)
        divide_bottom_2 = MathTex(r"\div 3", font_size=40, color=self.COLOR_DIVIDE).next_to(frac_36[0][2], RIGHT, buff=0.3)
        
        self.play(
            FadeIn(frac_36),
            Write(divide_top_2),
            Write(divide_bottom_2),
            run_time=0.6
        )
        
        # 第二次约分结果
        arrow_4 = Arrow(
            LEFT * 0.5 + UP * 1.5,
            RIGHT * 0.5 + UP * 1.5,
            color=self.COLOR_EQUAL,
            buff=0.3,
            stroke_width=6
        )
        
        final_frac = MathTex(
            r"\frac{1}{2}",
            font_size=70,
            color=WHITE
        ).move_to(RIGHT * 3 + UP * 1.5)
        
        equal_sign_4 = MathTex("=", font_size=60, color=self.COLOR_EQUAL).move_to(UP * 1.5)
        
        self.play(
            GrowArrow(arrow_4),
            FadeIn(final_frac, scale=0.8),
            run_time=0.6
        )
        
        self.play(Write(equal_sign_4), run_time=0.4)
        
        # "最简分数"标注
        simplest_label = Text(
            "最简分数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(final_frac, DOWN, buff=0.3)
        
        self.play(FadeIn(simplest_label), run_time=0.5)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                large_frac, simplified_frac_1, arrow_3, equal_sign_3,
                frac_36, final_frac, arrow_4, equal_sign_4,
                divide_top_2, divide_bottom_2, explain_4, simplest_label
            )),
            run_time=0.5
        )
        
        # 公式总结
        formula_box_2 = Rectangle(
            width=7,
            height=1.5,
            color=self.COLOR_DIVIDE,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=self.COLOR_DIVIDE
        ).move_to(UP * 2.5)
        
        formula_2 = MathTex(
            r"\frac{a}{b} = \frac{a \div k}{b \div k}",
            font_size=50,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Create(formula_box_2), run_time=0.5)
        self.play(Write(formula_2), run_time=1.0)
        
        # k≠0 且能整除
        condition_2 = MathTex(
            r"(k \neq 0)",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula_2, DOWN, buff=0.3)
        
        self.play(FadeIn(condition_2), run_time=0.5)
        self.play(Indicate(condition_2, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        self.wait(1.0)
        
        # 两个公式并排显示
        divide_formula_group = VGroup(formula_box_2, formula_2, condition_2)
        
        self.play(
            self.multiply_formula.animate.move_to(UP * 4.5 + LEFT * 0),
            divide_formula_group.animate.scale(0.6).move_to(UP * 3.2 + LEFT * 0),
            FadeOut(title),
            run_time=0.8
        )
        
        self.divide_formula = divide_formula_group
    
    def show_applications(self):
        """场景6: 应用示例 - 通分与约分"""
        # 标题
        title = Text(
            "实际应用",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 应用1: 通分 (比较大小)
        question = Text(
            "比较大小: 哪个更大?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(question), run_time=0.6)
        
        frac_a = MathTex(r"\frac{1}{3}", font_size=60, color=WHITE).move_to(LEFT * 2 + UP * 0.5)
        frac_b = MathTex(r"\frac{1}{4}", font_size=60, color=WHITE).move_to(RIGHT * 2 + UP * 0.5)
        vs_text = Text("VS", font="Noto Sans CJK SC", font_size=32, color=GRAY_A).move_to(UP * 0.5)
        
        self.play(
            FadeIn(frac_a),
            FadeIn(vs_text),
            FadeIn(frac_b),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 说明通分
        explain_5 = Text(
            "通分: 找公分母 12",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explain_5), run_time=0.5)
        
        # 变换过程
        arrow_a = MathTex(r"\times 4", font_size=30, color=self.COLOR_MULTIPLY).next_to(frac_a, UP, buff=0.2)
        arrow_b = MathTex(r"\times 3", font_size=30, color=self.COLOR_MULTIPLY).next_to(frac_b, UP, buff=0.2)
        
        self.play(
            Write(arrow_a),
            Write(arrow_b),
            run_time=0.6
        )
        
        # 结果
        result_a = MathTex(r"\frac{4}{12}", font_size=60, color=WHITE).move_to(LEFT * 2 + DOWN * 1.8)
        result_b = MathTex(r"\frac{3}{12}", font_size=60, color=WHITE).move_to(RIGHT * 2 + DOWN * 1.8)
        
        self.play(
            FadeIn(result_a, shift=DOWN * 0.3),
            FadeIn(result_b, shift=DOWN * 0.3),
            run_time=0.8
        )
        
        # 比较符号
        comparison = MathTex(r">", font_size=70, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 1.8)
        self.play(Write(comparison), run_time=0.5)
        
        # 结论
        conclusion_compare = Text(
            "所以 1/3 > 1/4",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.2)
        
        self.play(FadeIn(conclusion_compare), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理应用1
        self.play(
            FadeOut(VGroup(
                question, frac_a, frac_b, vs_text, explain_5,
                arrow_a, arrow_b, result_a, result_b, comparison, conclusion_compare
            )),
            run_time=0.5
        )
        
        # 应用2: 约分
        simplify_title = Text(
            "约分: 化简分数",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(simplify_title), run_time=0.5)
        
        example_frac = MathTex(r"\frac{8}{12}", font_size=70, color=WHITE).move_to(LEFT * 3 + UP * 0)
        
        self.play(FadeIn(example_frac, scale=0.8), run_time=0.6)
        
        # 找最大公约数
        gcd_hint = Text(
            "最大公约数: 4",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(gcd_hint), run_time=0.5)
        
        # 除以4
        divide_4 = MathTex(r"\div 4", font_size=35, color=self.COLOR_DIVIDE).next_to(example_frac, RIGHT, buff=0.4)
        self.play(Write(divide_4), run_time=0.5)
        
        # 箭头
        arrow_simplify = Arrow(
            LEFT * 0.8 + UP * 0,
            RIGHT * 0.2 + UP * 0,
            color=self.COLOR_EQUAL,
            buff=0.2,
            stroke_width=6
        )
        
        self.play(GrowArrow(arrow_simplify), run_time=0.5)
        
        # 最简形式
        simplified_final = MathTex(r"\frac{2}{3}", font_size=70, color=WHITE).move_to(RIGHT * 2.5 + UP * 0)
        
        self.play(FadeIn(simplified_final, scale=0.8), run_time=0.6)
        
        # 标注
        final_label = Text(
            "最简分数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(simplified_final, DOWN, buff=0.3)
        
        checkmark = Text("✓", font_size=40, color=GREEN).next_to(final_label, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(final_label),
            FadeIn(checkmark, scale=1.5),
            run_time=0.6
        )
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, simplify_title, example_frac, gcd_hint,
                divide_4, arrow_simplify, simplified_final, final_label, checkmark
            )),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与关注"""
        # 清理公式
        self.play(
            FadeOut(self.multiply_formula),
            FadeOut(self.divide_formula),
            run_time=0.4
        )
        
        # 总结标题
        summary_title = Text(
            "记住这三点!",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 三个要点
        point_1 = Text(
            "1. 分子分母同时乘或除",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 3.8)
        
        point_2 = Text(
            "2. 这个数不能为 0",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 2.8)
        
        point_3 = Text(
            "3. 应用: 通分和约分",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 1.8)
        
        # 依次淡入
        self.play(FadeIn(point_1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(point_2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(point_3, shift=RIGHT * 0.3), run_time=0.6)
        
        self.wait(0.5)
        
        # 公式回顾 (小字)
        formula_recap = VGroup(
            MathTex(r"\frac{a}{b} = \frac{a \times k}{b \times k}", font_size=32, color=GRAY_A),
            MathTex(r"\frac{a}{b} = \frac{a \div k}{b \div k}", font_size=32, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.3)
        
        self.play(FadeIn(formula_recap), run_time=0.8)
        
        self.wait(0.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(DOWN * 3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)
        
        # 小装饰 - 分数符号旋转
        decorations = VGroup(*[
            MathTex(r"\frac{1}{2}", font_size=30, color=GOLD).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(
                summary_title, point_1, point_2, point_3,
                formula_recap, self.author_info, author_id,
                follow_text, decorations
            )),
            run_time=1.0
        )


# 如果直接运行此脚本
if __name__ == "__main__":
    print("\n" + "="*60)
    print("分数的基本性质 - Manim动画")
    print("="*60)
    print("\n渲染命令:")
    print("  快速预览: manim -pql fraction_properties.py FractionProperties")
    print("  高质量:    manim -qh fraction_properties.py FractionProperties")
    print("\n预计时长: 70-75秒")
    print("="*60 + "\n")