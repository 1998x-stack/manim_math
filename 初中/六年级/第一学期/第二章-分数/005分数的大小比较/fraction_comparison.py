"""
分数大小比较动画 - Fraction Comparison Animation
使用 Manim 创建的六年级数学教学视频

内容: 分数大小比较的三种方法
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


class FractionComparison(Scene):
    """
    分数大小比较教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 方法一: 同分母比分子
    3. 方法二: 同分子比分母
    4. 方法三: 通分法 - 引入
    5. 通分过程详解
    6. 数轴可视化
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要分数
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比分数
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_CORRECT = "#2ecc71"      # 绿色 - 正确
        self.COLOR_FILL = "#3498db"         # 填充色
        
        # 字体配置
        self.FONT = "PingFang SC"
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "fraction": 36,
            "label": 20,
            "small": 18,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_same_denominator()
        self.show_same_numerator()
        self.show_common_denominator_intro()
        self.show_common_denominator_process()
        self.show_number_line()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何元素的位置参数"""
        # 圆形参数 (场景2)
        self.circle_radius = 1.0
        self.circle1_center = LEFT * 2 + UP * 1.5
        self.circle2_center = RIGHT * 2 + UP * 1.5
        
        # 条形参数 (场景3)
        self.bar_width = 1.2
        self.bar_max_height = 3.5
        self.bar1_center = LEFT * 2 + UP * 0.5
        self.bar2_center = RIGHT * 2 + UP * 0.5
        
        # 数轴参数 (场景6)
        self.numberline_length = 7.0
        self.numberline_y = 0
    
    def create_fraction(self, numerator, denominator, color=WHITE, font_size=36):
        """创建分数显示"""
        num_text = MathTex(str(numerator), font_size=font_size, color=color)
        line = Line(LEFT * 0.3, RIGHT * 0.3, stroke_width=2, color=color)
        den_text = MathTex(str(denominator), font_size=font_size, color=color)
        
        fraction = VGroup(num_text, line, den_text).arrange(DOWN, buff=0.15)
        return fraction, num_text, den_text
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "哪个分数更大?",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"] + 8,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 显示两个分数对比
        frac1, _, _ = self.create_fraction(3, 5, self.COLOR_PRIMARY, 48)
        frac2, _, _ = self.create_fraction(4, 7, self.COLOR_SECONDARY, 48)
        
        frac1.move_to(LEFT * 2 + UP * 2.5)
        frac2.move_to(RIGHT * 2 + UP * 2.5)
        
        vs_text = Text("VS", font=self.FONT, font_size=32, color=GRAY_A).move_to(UP * 2.5)
        
        self.play(
            FadeIn(frac1, shift=RIGHT * 0.5),
            FadeIn(frac2, shift=LEFT * 0.5),
            run_time=0.8
        )
        self.play(Write(vs_text), run_time=0.3)
        
        # 闪烁强调
        self.play(
            Flash(frac1, color=self.COLOR_PRIMARY, flash_radius=0.8),
            Flash(frac2, color=self.COLOR_SECONDARY, flash_radius=0.8),
            run_time=0.5
        )
        
        # 提示文字
        hint = Text(
            "掌握三种比较方法!",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(frac1),
            FadeOut(frac2),
            FadeOut(vs_text),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_same_denominator(self):
        """场景2: 同分母比分子"""
        # 标题
        title = Text(
            "方法一: 同分母比分子",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_CORRECT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 显示分数 3/7 和 5/7
        frac1, num1, den1 = self.create_fraction(3, 7, self.COLOR_PRIMARY, 36)
        frac2, num2, den2 = self.create_fraction(5, 7, self.COLOR_SECONDARY, 36)
        
        frac1.move_to(LEFT * 2 + UP * 4.5)
        frac2.move_to(RIGHT * 2 + UP * 4.5)
        
        self.play(Write(frac1), Write(frac2), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "分母相同, 比较分子",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 3.3)
        
        self.play(FadeIn(explain), run_time=0.5)
        
        # 绘制两个圆形并分成7份
        circle1 = Circle(
            radius=self.circle_radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.circle1_center)
        
        circle2 = Circle(
            radius=self.circle_radius,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(self.circle2_center)
        
        self.play(Create(circle1), Create(circle2), run_time=1.0)
        
        # 创建扇形分割线 (7份)
        num_sectors = 7
        sectors1 = VGroup()
        sectors2 = VGroup()
        
        for i in range(num_sectors):
            angle = i * TAU / num_sectors
            end_point1 = self.circle1_center + self.circle_radius * np.array([np.cos(angle), np.sin(angle), 0])
            end_point2 = self.circle2_center + self.circle_radius * np.array([np.cos(angle), np.sin(angle), 0])
            
            line1 = Line(self.circle1_center, end_point1, color=self.COLOR_PRIMARY, stroke_width=1.5)
            line2 = Line(self.circle2_center, end_point2, color=self.COLOR_SECONDARY, stroke_width=1.5)
            
            sectors1.add(line1)
            sectors2.add(line2)
        
        self.play(Create(sectors1), Create(sectors2), run_time=0.8)
        
        # 填充扇形 (3份和5份)
        filled_sectors1 = VGroup()
        for i in range(3):
            angle_start = i * TAU / num_sectors
            angle_end = (i + 1) * TAU / num_sectors
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=self.circle_radius,
                angle=TAU / num_sectors,
                start_angle=angle_start,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6,
                stroke_width=0
            ).move_arc_center_to(self.circle1_center)
            filled_sectors1.add(sector)
        
        filled_sectors2 = VGroup()
        for i in range(5):
            angle_start = i * TAU / num_sectors
            angle_end = (i + 1) * TAU / num_sectors
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=self.circle_radius,
                angle=TAU / num_sectors,
                start_angle=angle_start,
                color=self.COLOR_SECONDARY,
                fill_opacity=0.6,
                stroke_width=0
            ).move_arc_center_to(self.circle2_center)
            filled_sectors2.add(sector)
        
        self.play(FadeIn(filled_sectors1), run_time=0.6)
        self.play(FadeIn(filled_sectors2), run_time=0.6)
        
        # 高亮分子
        self.play(
            Indicate(num1, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            Indicate(num2, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 显示比较结果
        comparison = MathTex(
            r"3 < 5",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN + DOWN * 0.3)
        
        # 修复：这里用Write代替GrowArrow
        arrow_symbol = MathTex(
            r"\Downarrow",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison, DOWN, buff=0.2)
        
        conclusion = MathTex(
            r"\frac{3}{7} < \frac{5}{7}",
            font_size=36,
            color=self.COLOR_CORRECT
        ).next_to(arrow_symbol, DOWN, buff=0.3)
        
        self.play(Write(comparison), run_time=0.5)
        self.play(Write(arrow_symbol), run_time=0.3)  # 改为Write
        self.play(Write(conclusion), run_time=0.8)
        
        # 底部说明
        rule = Text(
            "同分母分数: 分子大的分数大",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(frac1),
            FadeOut(frac2),
            FadeOut(explain),
            FadeOut(circle1),
            FadeOut(circle2),
            FadeOut(sectors1),
            FadeOut(sectors2),
            FadeOut(filled_sectors1),
            FadeOut(filled_sectors2),
            FadeOut(comparison),
            FadeOut(arrow_symbol),
            FadeOut(conclusion),
            FadeOut(rule),
            run_time=0.6
        )
    
    def show_same_numerator(self):
        """场景3: 同分子比分母"""
        # 标题
        title = Text(
            "方法二: 同分子比分母",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_CORRECT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 显示分数 2/5 和 2/7
        frac1, num1, den1 = self.create_fraction(2, 5, self.COLOR_PRIMARY, 36)
        frac2, num2, den2 = self.create_fraction(2, 7, self.COLOR_SECONDARY, 36)
        
        frac1.move_to(LEFT * 2 + UP * 4.5)
        frac2.move_to(RIGHT * 2 + UP * 4.5)
        
        self.play(Write(frac1), Write(frac2), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "分子相同, 比较分母",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 3.3)
        
        self.play(FadeIn(explain), run_time=0.5)
        
        # 绘制两个矩形条形图
        bar1_outline = Rectangle(
            width=self.bar_width,
            height=self.bar_max_height,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.bar1_center)
        
        bar2_outline = Rectangle(
            width=self.bar_width,
            height=self.bar_max_height,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(self.bar2_center)
        
        self.play(Create(bar1_outline), Create(bar2_outline), run_time=1.0)
        
        # 分割条形图 (5份和7份)
        divisions1 = VGroup()
        for i in range(1, 5):
            y_pos = self.bar1_center[1] - self.bar_max_height/2 + i * (self.bar_max_height / 5)
            line = Line(
                self.bar1_center + LEFT * self.bar_width/2 + UP * (y_pos - self.bar1_center[1]),
                self.bar1_center + RIGHT * self.bar_width/2 + UP * (y_pos - self.bar1_center[1]),
                color=self.COLOR_PRIMARY,
                stroke_width=1.5
            )
            divisions1.add(line)
        
        divisions2 = VGroup()
        for i in range(1, 7):
            y_pos = self.bar2_center[1] - self.bar_max_height/2 + i * (self.bar_max_height / 7)
            line = Line(
                self.bar2_center + LEFT * self.bar_width/2 + UP * (y_pos - self.bar2_center[1]),
                self.bar2_center + RIGHT * self.bar_width/2 + UP * (y_pos - self.bar2_center[1]),
                color=self.COLOR_SECONDARY,
                stroke_width=1.5
            )
            divisions2.add(line)
        
        self.play(Create(divisions1), Create(divisions2), run_time=0.8)
        
        # 填充2份
        unit_height1 = self.bar_max_height / 5
        fill_height1 = 2 * unit_height1
        
        filled1 = Rectangle(
            width=self.bar_width - 0.05,
            height=fill_height1,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(
            self.bar1_center + DOWN * (self.bar_max_height/2 - fill_height1/2)
        )
        
        unit_height2 = self.bar_max_height / 7
        fill_height2 = 2 * unit_height2
        
        filled2 = Rectangle(
            width=self.bar_width - 0.05,
            height=fill_height2,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(
            self.bar2_center + DOWN * (self.bar_max_height/2 - fill_height2/2)
        )
        
        self.play(GrowFromEdge(filled1, DOWN), run_time=0.6)
        self.play(GrowFromEdge(filled2, DOWN), run_time=0.6)
        
        # 高亮分母
        self.play(
            Indicate(den1, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            Indicate(den2, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 显示比较结果
        comparison = MathTex(
            r"5 < 7",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN + DOWN * 1.8)
        
        # 修复：这里用Write代替GrowArrow
        arrow_symbol = MathTex(
            r"\Downarrow",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison, DOWN, buff=0.2)
        
        conclusion = MathTex(
            r"\frac{2}{5} > \frac{2}{7}",
            font_size=36,
            color=self.COLOR_CORRECT
        ).next_to(arrow_symbol, DOWN, buff=0.3)
        
        self.play(Write(comparison), run_time=0.5)
        self.play(Write(arrow_symbol), run_time=0.3)  # 改为Write
        self.play(Write(conclusion), run_time=0.8)
        
        # 底部说明
        rule = Text(
            "同分子分数: 分母小的分数大",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(frac1),
            FadeOut(frac2),
            FadeOut(explain),
            FadeOut(bar1_outline),
            FadeOut(bar2_outline),
            FadeOut(divisions1),
            FadeOut(divisions2),
            FadeOut(filled1),
            FadeOut(filled2),
            FadeOut(comparison),
            FadeOut(arrow_symbol),
            FadeOut(conclusion),
            FadeOut(rule),
            run_time=0.6
        )
    
    def show_common_denominator_intro(self):
        """场景4: 通分法引入"""
        # 标题
        title = Text(
            "方法三: 通分后比较",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_CORRECT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 显示分数 2/3 和 3/4
        frac1, num1, den1 = self.create_fraction(2, 3, self.COLOR_PRIMARY, 40)
        frac2, num2, den2 = self.create_fraction(3, 4, self.COLOR_SECONDARY, 40)
        
        frac1.move_to(LEFT * 2 + UP * 3)
        frac2.move_to(RIGHT * 2 + UP * 3)
        
        self.play(Write(frac1), Write(frac2), run_time=0.8)
        
        # 问号
        question = Text(
            "?",
            font=self.FONT,
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(question, scale=0.5), run_time=0.5)
        self.play(Flash(question, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.4)
        
        # 提示文字
        hint = Text(
            "分子分母都不同, 怎么比较?",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        answer = Text(
            "答案: 先通分!",
            font=self.FONT,
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(hint), run_time=0.6)
        self.wait(1.0)
        self.play(Write(answer), run_time=0.8)
        self.wait(1.5)
        
        # 清理问号和提示, 保留标题和分数
        self.play(
            FadeOut(question),
            FadeOut(hint),
            FadeOut(answer),
            run_time=0.5
        )
        
        # 保存这些对象供下一场景使用
        self.method3_title = title
        self.method3_frac1 = frac1
        self.method3_frac2 = frac2
    
    def show_common_denominator_process(self):
        """场景5: 通分过程详解"""
        # 移动分数到上方
        self.play(
            self.method3_frac1.animate.move_to(LEFT * 2.5 + UP * 4.5),
            self.method3_frac2.animate.move_to(RIGHT * 2.5 + UP * 4.5),
            run_time=0.8
        )
        
        # 显示"找最小公倍数"
        lcm_text = Text(
            "找最小公倍数",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(lcm_text), run_time=0.6)
        
        # 显示 LCM(3,4) = 12
        lcm_calc = MathTex(
            r"\text{LCM}(3, 4) = 12",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)
        
        self.play(Write(lcm_calc), run_time=0.8)
        
        # 箭头向下
        arrow1 = Arrow(
            self.method3_frac1.get_bottom() + DOWN * 0.2,
            self.method3_frac1.get_bottom() + DOWN * 1.5,
            color=self.COLOR_PRIMARY,
            buff=0
        )
        
        arrow2 = Arrow(
            self.method3_frac2.get_bottom() + DOWN * 0.2,
            self.method3_frac2.get_bottom() + DOWN * 1.5,
            color=self.COLOR_SECONDARY,
            buff=0
        )
        
        self.play(Create(arrow1), Create(arrow2), run_time=0.6)  # 改为Create
        
        # 显示转换过程
        conv1_text = Text(
            "×4",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_PRIMARY
        ).next_to(arrow1, RIGHT, buff=0.3)
        
        conv2_text = Text(
            "×3",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SECONDARY
        ).next_to(arrow2, LEFT, buff=0.3)
        
        self.play(Write(conv1_text), Write(conv2_text), run_time=0.6)
        
        # 显示结果分数
        result1, res_num1, res_den1 = self.create_fraction(8, 12, self.COLOR_PRIMARY, 36)
        result2, res_num2, res_den2 = self.create_fraction(9, 12, self.COLOR_SECONDARY, 36)
        
        result1.move_to(LEFT * 2.5 + UP * 0.3)
        result2.move_to(RIGHT * 2.5 + UP * 0.3)
        
        self.play(FadeIn(result1), FadeIn(result2), run_time=0.8)
        
        # 高亮分子比较
        self.play(
            Indicate(res_num1, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            Indicate(res_num2, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 显示比较
        comparison = MathTex(
            r"8 < 9",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        # 修复：这里用Write代替GrowArrow
        arrow_symbol = MathTex(
            r"\Downarrow",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison, DOWN, buff=0.2)
        
        conclusion = MathTex(
            r"\frac{2}{3} < \frac{3}{4}",
            font_size=36,
            color=self.COLOR_CORRECT
        ).next_to(arrow_symbol, DOWN, buff=0.3)
        
        self.play(Write(comparison), run_time=0.5)
        self.play(Write(arrow_symbol), run_time=0.3)  # 改为Write
        self.play(Write(conclusion), run_time=0.8)
        
        # 底部说明
        rule = Text(
            "异分母分数: 先通分, 再比较",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(self.method3_title),
            FadeOut(self.method3_frac1),
            FadeOut(self.method3_frac2),
            FadeOut(lcm_text),
            FadeOut(lcm_calc),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(conv1_text),
            FadeOut(conv2_text),
            FadeOut(result1),
            FadeOut(result2),
            FadeOut(comparison),
            FadeOut(arrow_symbol),
            FadeOut(conclusion),
            FadeOut(rule),
            run_time=0.6
        )
    
    def show_number_line(self):
        """场景6: 数轴可视化"""
        # 标题
        title = Text(
            "数轴上直观比较",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_CORRECT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 绘制数轴
        numberline = NumberLine(
            x_range=[0, 1, 0.1],
            length=self.numberline_length,
            include_numbers=False,
            include_ticks=True,
            tick_size=0.1,
            color=WHITE
        ).move_to(self.numberline_y * UP)
        
        self.play(Create(numberline), run_time=1.0)
        
        # 标注0和1
        label_0 = MathTex("0", font_size=24).next_to(numberline.n2p(0), DOWN, buff=0.3)
        label_1 = MathTex("1", font_size=24).next_to(numberline.n2p(1), DOWN, buff=0.3)
        
        self.play(FadeIn(label_0), FadeIn(label_1), run_time=0.5)
        
        # 标记 2/3 的位置
        pos_2_3 = 2/3
        dot1 = Dot(
            numberline.n2p(pos_2_3),
            color=self.COLOR_PRIMARY,
            radius=0.1
        )
        
        frac1_label = MathTex(
            r"\frac{2}{3}",
            font_size=28,
            color=self.COLOR_PRIMARY
        ).next_to(dot1, UP, buff=0.5)
        
        line1 = DashedLine(
            dot1.get_center(),
            frac1_label.get_bottom() + DOWN * 0.1,
            color=self.COLOR_PRIMARY,
            dash_length=0.1
        )
        
        self.play(FadeIn(dot1, scale=0.5), run_time=0.5)
        self.play(Create(line1), Write(frac1_label), run_time=0.6)
        
        # 标记 3/4 的位置
        pos_3_4 = 3/4
        dot2 = Dot(
            numberline.n2p(pos_3_4),
            color=self.COLOR_SECONDARY,
            radius=0.1
        )
        
        frac2_label = MathTex(
            r"\frac{3}{4}",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).next_to(dot2, UP, buff=0.5)
        
        line2 = DashedLine(
            dot2.get_center(),
            frac2_label.get_bottom() + DOWN * 0.1,
            color=self.COLOR_SECONDARY,
            dash_length=0.1
        )
        
        self.play(FadeIn(dot2, scale=0.5), run_time=0.5)
        self.play(Create(line2), Write(frac2_label), run_time=0.6)
        
        # 绘制比较箭头
        comparison_arrow = Arrow(
            numberline.n2p(pos_2_3) + DOWN * 0.8,
            numberline.n2p(pos_3_4) + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4
        )
        
        arrow_label = Text(
            "更大",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison_arrow, DOWN, buff=0.2)
        
        self.play(Create(comparison_arrow), run_time=0.6)  # 改为Create
        self.play(FadeIn(arrow_label), run_time=0.4)
        
        # 显示结论
        conclusion = MathTex(
            r"\frac{2}{3} < \frac{3}{4}",
            font_size=36,
            color=self.COLOR_CORRECT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(conclusion), run_time=0.8)
        
        # 说明
        explain = Text(
            "数轴上, 右边的数更大",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(numberline),
            FadeOut(label_0),
            FadeOut(label_1),
            FadeOut(dot1),
            FadeOut(dot2),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(frac1_label),
            FadeOut(frac2_label),
            FadeOut(comparison_arrow),
            FadeOut(arrow_label),
            FadeOut(conclusion),
            FadeOut(explain),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        summary_title = Text(
            "三种比较方法",
            font=self.FONT,
            font_size=self.FONT_SIZES["title"] + 4,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 创建三个方法卡片
        card1 = self.create_method_card(
            "方法一",
            "同分母比分子",
            "分子大的分数大",
            self.COLOR_PRIMARY,
            UP * 3
        )
        
        card2 = self.create_method_card(
            "方法二",
            "同分子比分母",
            "分母小的分数大",
            self.COLOR_SECONDARY,
            UP * 1
        )
        
        card3 = self.create_method_card(
            "方法三",
            "通分后比较",
            "化为同分母再比较",
            self.COLOR_CORRECT,
            DOWN * 1
        )
        
        # 卡片依次滑入
        cards = VGroup(card1, card2, card3)
        for card in cards:
            card.shift(LEFT * 10)
        
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 所有卡片闪烁
        self.play(
            Flash(card1, color=self.COLOR_PRIMARY),
            Flash(card2, color=self.COLOR_SECONDARY),
            Flash(card3, color=self.COLOR_CORRECT),
            run_time=0.6
        )
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font=self.FONT,
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=self.FONT_SIZES["body"],
            color=GRAY_B
        ).move_to(DOWN * 6.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(follow_text),
            FadeOut(self.author_info),
            FadeOut(author_id),
            run_time=1.0
        )
    
    def create_method_card(self, number, title, description, color, position):
        """创建方法卡片"""
        # 图标
        icon = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 序号
        num_text = Text(
            number,
            font=self.FONT,
            font_size=self.FONT_SIZES["label"],
            color=WHITE
        ).move_to(icon.get_center())
        
        icon_group = VGroup(icon, num_text)
        
        # 标题
        title_text = Text(
            title,
            font=self.FONT,
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE
        )
        
        # 描述
        desc_text = Text(
            description,
            font=self.FONT,
            font_size=self.FONT_SIZES["label"],
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon_group, title_text, desc_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql fraction_comparison.py FractionComparison  # 快速预览
# manim -qh fraction_comparison.py FractionComparison   # 高质量渲染