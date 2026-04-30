"""
百分比应用 - Percentage Applications in Life
使用 Manim 创建的小学数学教学视频

内容: 折扣、利率、浓度的实际应用
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


class PercentageApplications(Scene):
    """
    百分比应用教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 应用概览
    3. 折扣应用（购物打折）
    4. 利率应用（银行存款）
    5. 浓度应用（溶液配置）
    6. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_DISCOUNT = "#e74c3c"      # 红色 - 折扣
        self.COLOR_INTEREST = "#3498db"      # 蓝色 - 利率
        self.COLOR_CONCENTRATION = "#2ecc71" # 绿色 - 浓度
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_FORMULA = "#f39c12"       # 橙色 - 公式
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 执行动画序列
        self.show_opening()
        self.show_overview()
        self.show_discount_application()
        self.show_interest_application()
        self.show_concentration_application()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "百分比在生活中\n有哪些应用？",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 四个应用图标
        icons = VGroup(
            # 折扣图标 - 标签
            VGroup(
                Polygon(
                    [-0.3, 0.3, 0], [0.3, 0.3, 0], [0.3, -0.3, 0], 
                    [-0.3, -0.3, 0], [-0.2, 0, 0],
                    color=self.COLOR_DISCOUNT,
                    fill_opacity=0.5,
                    stroke_width=3
                ),
                MathTex(r"\%", font_size=40, color=self.COLOR_DISCOUNT)
            ).arrange(ORIGIN),
            
            # 利率图标 - 钱币
            Circle(
                radius=0.35,
                color=self.COLOR_INTEREST,
                fill_opacity=0.5,
                stroke_width=3
            ),
            
            # 浓度图标 - 烧杯
            Polygon(
                [-0.25, -0.3, 0], [-0.25, 0.2, 0], [-0.2, 0.3, 0],
                [0.2, 0.3, 0], [0.25, 0.2, 0], [0.25, -0.3, 0],
                color=self.COLOR_CONCENTRATION,
                fill_opacity=0.3,
                stroke_width=3
            ),
            
            # 税率图标 - 文档
            Rectangle(
                width=0.5,
                height=0.6,
                color=self.COLOR_FORMULA,
                fill_opacity=0.3,
                stroke_width=3
            )
        )
        
        icons.arrange(RIGHT, buff=0.8).move_to(UP * 2)
        
        for icon in icons:
            self.play(FadeIn(icon, scale=0.5), run_time=0.3)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(icons),
            run_time=0.5
        )
    
    def show_overview(self):
        """场景2: 应用概览"""
        # 标题
        title = Text(
            "生活中的百分比",
            font="PingFang SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个应用卡片
        card1 = self.create_app_card(
            "折扣",
            "购物打折",
            "折扣价 = 原价 × 折扣率",
            self.COLOR_DISCOUNT,
            UP * 2.5
        )
        
        card2 = self.create_app_card(
            "利率",
            "银行存款",
            "利息 = 本金 × 利率 × 时间",
            self.COLOR_INTEREST,
            UP * 0.5
        )
        
        card3 = self.create_app_card(
            "浓度",
            "溶液配置",
            "浓度 = 溶质 / 溶液 × 100%",
            self.COLOR_CONCENTRATION,
            DOWN * 1.5
        )
        
        # 卡片依次滑入
        for card in [card1, card2, card3]:
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            run_time=0.5
        )
    
    def create_app_card(self, app_name, scenario, formula, color, position):
        """创建应用卡片"""
        # 背景矩形
        bg_rect = RoundedRectangle(
            width=7.5,
            height=1.3,
            corner_radius=0.15,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=3
        )
        
        # 应用名称
        name_text = Text(
            app_name,
            font="PingFang SC",
            font_size=32,
            color=color,
            weight=BOLD
        )
        
        # 场景说明
        scenario_text = Text(
            scenario,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 公式
        formula_text = Text(
            formula,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        content = VGroup(
            name_text,
            scenario_text,
            formula_text
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        card = VGroup(bg_rect, content)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_discount_application(self):
        """场景3: 折扣应用"""
        # 标题
        title = Text(
            "应用一: 折扣",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_DISCOUNT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "一件外套原价500元\n打8折，实际多少钱？",
            font="PingFang SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 原价标签
        price_tag = VGroup(
            RoundedRectangle(
                width=2,
                height=1,
                corner_radius=0.1,
                fill_color=self.COLOR_DISCOUNT,
                fill_opacity=0.3,
                stroke_color=self.COLOR_DISCOUNT,
                stroke_width=3
            ),
            Text("原价", font="PingFang SC", font_size=22, color=WHITE),
            Text("500元", font="PingFang SC", font_size=36, color=WHITE, weight=BOLD)
        )
        price_tag[1].move_to(price_tag[0].get_center() + UP * 0.25)
        price_tag[2].move_to(price_tag[0].get_center() + DOWN * 0.15)
        price_tag.move_to(UP * 3 + LEFT * 2.5)
        
        self.play(FadeIn(price_tag, scale=1.1), run_time=0.8)
        
        # 原价矩形
        price_rect = Rectangle(
            width=6,
            height=0.8,
            color=self.COLOR_DISCOUNT,
            stroke_width=3
        ).move_to(UP * 1.5)
        
        price_label = Text(
            "500元",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(price_rect.get_center())
        
        self.play(
            Create(price_rect),
            FadeIn(price_label),
            run_time=1.0
        )
        
        # 折扣标签
        discount_tag = VGroup(
            Circle(
                radius=0.6,
                fill_color=self.COLOR_FORMULA,
                fill_opacity=0.8,
                stroke_color=self.COLOR_FORMULA,
                stroke_width=3
            ),
            Text("8折", font="PingFang SC", font_size=32, color=WHITE, weight=BOLD)
        )
        discount_tag[1].move_to(discount_tag[0].get_center())
        discount_tag.move_to(UP * 3 + RIGHT * 2.5)
        
        self.play(FadeIn(discount_tag, scale=0.8), run_time=0.6)
        
        # 折扣部分矩形 (80%)
        discount_rect = Rectangle(
            width=6 * 0.8,
            height=0.8,
            color=self.COLOR_FORMULA,
            fill_opacity=0.5,
            stroke_width=3
        )
        discount_rect.align_to(price_rect, LEFT)
        discount_rect.align_to(price_rect, DOWN)
        
        discount_label = MathTex(
            r"80\%",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(discount_rect.get_center())
        
        self.play(
            Create(discount_rect),
            FadeIn(discount_label),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 公式说明
        formula_parts = [
            Text("折扣价", font="PingFang SC", font_size=28, color=WHITE),
            MathTex(r"=", font_size=36, color=WHITE),
            Text("原价", font="PingFang SC", font_size=28, color=WHITE),
            MathTex(r"\times", font_size=36, color=WHITE),
            Text("折扣率", font="PingFang SC", font_size=28, color=WHITE)
        ]
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(Write(formula), run_time=1.5)
        
        # 具体计算
        calculation = MathTex(
            r"500 \times 80\% = 400",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 答案框
        answer_box = RoundedRectangle(
            width=4.5,
            height=1.2,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 4)
        
        answer = Text(
            "实付: 400元",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(answer_box.get_center())
        
        savings = Text(
            "省了100元!",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(answer_box, DOWN, buff=0.3)
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.4)
        self.play(FadeIn(savings), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(price_tag),
            FadeOut(price_rect),
            FadeOut(price_label),
            FadeOut(discount_tag),
            FadeOut(discount_rect),
            FadeOut(discount_label),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(answer_box),
            FadeOut(answer),
            FadeOut(savings),
            run_time=0.6
        )
    
    def show_interest_application(self):
        """场景4: 利率应用"""
        # 标题
        title = Text(
            "应用二: 利率",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_INTEREST
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "存入10000元，年利率3%\n存3年，利息多少？",
            font="PingFang SC",
            font_size=30,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 本金可视化 - 钱袋
        principal_circle = Circle(
            radius=0.9,
            fill_color=self.COLOR_INTEREST,
            fill_opacity=0.3,
            stroke_color=self.COLOR_INTEREST,
            stroke_width=3
        ).move_to(UP * 2.8)
        
        principal_label = Text(
            "10000元",
            font="PingFang SC",
            font_size=28,
            color=WHITE,
            weight=BOLD
        ).move_to(principal_circle.get_center())
        
        principal_text = Text(
            "本金",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(principal_circle, DOWN, buff=0.2)
        
        self.play(
            FadeIn(principal_circle, scale=0.8),
            FadeIn(principal_label),
            FadeIn(principal_text),
            run_time=1.0
        )
        
        # 时间轴
        timeline = Line(LEFT * 3, RIGHT * 3, color=self.COLOR_AUXILIARY, stroke_width=3).move_to(UP * 0.8)
        
        year_marks = VGroup(*[
            VGroup(
                Dot(timeline.point_from_proportion(i/3), radius=0.08, color=self.COLOR_INTEREST),
                Text(f"第{i}年", font="PingFang SC", font_size=18, color=GRAY_A)
                .next_to(timeline.point_from_proportion(i/3), DOWN, buff=0.2)
            )
            for i in range(4)
        ])
        
        self.play(Create(timeline), run_time=0.8)
        self.play(FadeIn(year_marks, lag_ratio=0.3), run_time=1.0)
        
        # 利率标签
        rate_label = VGroup(
            RoundedRectangle(
                width=2,
                height=0.7,
                corner_radius=0.1,
                fill_color=self.COLOR_FORMULA,
                fill_opacity=0.3,
                stroke_color=self.COLOR_FORMULA,
                stroke_width=2
            ),
            Text("年利率 3%", font="PingFang SC", font_size=22, color=WHITE)
        )
        rate_label[1].move_to(rate_label[0].get_center())
        rate_label.next_to(timeline, UP, buff=0.5)
        
        self.play(FadeIn(rate_label), run_time=0.6)
        
        # 每年利息可视化
        interest_bars = VGroup()
        interest_per_year = 300  # 10000 * 3% = 300
        
        for i in range(3):
            bar = Rectangle(
                width=0.6,
                height=1.2,
                fill_color=self.COLOR_FORMULA,
                fill_opacity=0.6,
                stroke_color=self.COLOR_FORMULA,
                stroke_width=2
            ).next_to(year_marks[i+1], DOWN, buff=0.8)
            
            bar_label = Text(
                f"+{interest_per_year}元",
                font="PingFang SC",
                font_size=18,
                color=self.COLOR_FORMULA
            ).next_to(bar, DOWN, buff=0.1)
            
            interest_bars.add(VGroup(bar, bar_label))
        
        for i, bar_group in enumerate(interest_bars):
            self.play(
                GrowFromEdge(bar_group[0], DOWN),
                FadeIn(bar_group[1]),
                run_time=0.6
            )
            self.wait(0.3)
        
        # 公式
        formula_parts = [
            Text("利息", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"=", font_size=32, color=WHITE),
            Text("本金", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"\times", font_size=32, color=WHITE),
            Text("利率", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"\times", font_size=32, color=WHITE),
            Text("时间", font="PingFang SC", font_size=26, color=WHITE)
        ]
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.25).move_to(DOWN * 3)
        
        self.play(Write(formula), run_time=1.5)
        
        # 计算步骤
        step1 = MathTex(
            r"10000 \times 3\% \times 3",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        step2 = MathTex(
            r"= 300 \times 3 = 900",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.8)
        self.play(TransformMatchingTex(step1, step2), run_time=1.0)
        
        # 答案
        answer_box = RoundedRectangle(
            width=4.5,
            height=1,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 6.2)
        
        answer = Text(
            "利息: 900元",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(answer_box.get_center())
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, question, principal_circle, principal_label, principal_text,
                timeline, year_marks, rate_label, interest_bars,
                formula, step2, answer_box, answer
            )),
            run_time=0.6
        )
    
    def show_concentration_application(self):
        """场景5: 浓度应用"""
        # 标题
        title = Text(
            "应用三: 浓度",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_CONCENTRATION
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "20克盐溶解在100克水中\n浓度是多少？",
            font="PingFang SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 烧杯
        beaker = Polygon(
            [-1, -1.5, 0], [-1, 1.2, 0], [-0.8, 1.4, 0],
            [0.8, 1.4, 0], [1, 1.2, 0], [1, -1.5, 0],
            color=self.COLOR_CONCENTRATION,
            stroke_width=3
        ).move_to(UP * 1.5)
        
        self.play(Create(beaker), run_time=1.0)
        
        # 水（蓝色）
        water = Rectangle(
            width=1.8,
            height=2.0,
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )
        water.move_to(beaker.get_center() + DOWN * 0.35)
        
        water_label = Text(
            "水 100克",
            font="PingFang SC",
            font_size=22,
            color=BLUE_B
        ).next_to(beaker, LEFT, buff=0.8).shift(DOWN * 0.3)
        
        self.play(
            FadeIn(water, shift=DOWN * 0.5),
            FadeIn(water_label),
            run_time=1.0
        )
        
        # 盐（小方块）
        salt_cubes = VGroup(*[
            Square(0.15, fill_color=WHITE, fill_opacity=0.8, stroke_width=1)
            for _ in range(6)
        ]).arrange_in_grid(rows=2, cols=3, buff=0.1)
        salt_cubes.next_to(beaker, RIGHT, buff=0.8).shift(UP * 0.5)
        
        salt_label = Text(
            "盐 20克",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(salt_cubes, UP, buff=0.2)
        
        self.play(
            FadeIn(salt_cubes, lag_ratio=0.2),
            FadeIn(salt_label),
            run_time=0.8
        )
        
        # 盐倒入水中
        salt_copy = salt_cubes.copy()
        self.play(
            salt_copy.animate.move_to(water.get_center()).scale(0.3),
            FadeOut(salt_cubes),
            FadeOut(salt_label),
            run_time=1.0
        )
        
        # 溶解动画 - 溶液变色
        solution = Rectangle(
            width=1.8,
            height=2.4,
            fill_color=BLUE_E,
            fill_opacity=0.4,
            stroke_width=0
        )
        solution.move_to(beaker.get_center() + DOWN * 0.23)
        
        solution_label = Text(
            "盐水 120克",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_CONCENTRATION
        ).move_to(water_label.get_center())
        
        self.play(
            Transform(water, solution),
            FadeOut(salt_copy),
            Transform(water_label, solution_label),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 浓度说明
        conc_parts = [
            Text("浓度", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"=", font_size=32, color=WHITE),
            Text("溶质", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"\div", font_size=32, color=WHITE),
            Text("溶液", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"\times 100\%", font_size=32, color=WHITE)
        ]
        
        formula = VGroup(*conc_parts).arrange(RIGHT, buff=0.25).move_to(DOWN * 2)
        
        self.play(Write(formula), run_time=1.5)
        
        # 计算步骤
        step1 = MathTex(
            r"20 \div 120 \times 100\%",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        step2 = MathTex(
            r"\approx 16.7\%",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.8)
        self.play(TransformMatchingTex(step1, step2), run_time=1.0)
        
        # 答案
        answer_box = RoundedRectangle(
            width=5,
            height=1,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 5.2)
        
        answer = MathTex(
            r"16.7\%",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(answer_box.get_center())
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, question, beaker, water, water_label,
                formula, step2, answer_box, answer
            )),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 总结与关注"""
        # 总结标题
        title = Text(
            "百分比，生活好帮手!",
            font="PingFang SC",
            font_size=42,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三个应用总结卡片
        card1 = self.create_summary_card(
            "折扣",
            "折扣价 = 原价 × 折扣率",
            self.COLOR_DISCOUNT,
            UP * 3.5
        )
        
        card2 = self.create_summary_card(
            "利率",
            "利息 = 本金 × 利率 × 时间",
            self.COLOR_INTEREST,
            UP * 2
        )
        
        card3 = self.create_summary_card(
            "浓度",
            "浓度 = 溶质 / 溶液 × 100%",
            self.COLOR_CONCENTRATION,
            UP * 0.5
        )
        
        cards = VGroup(card1, card2, card3)
        
        self.play(FadeIn(cards, shift=UP * 0.3, lag_ratio=0.3), run_time=1.2)
        
        # 关键提示
        key_point = Text(
            "掌握公式，轻松应用!",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(key_point, scale=1.2), run_time=0.8)
        self.play(
            Flash(key_point, color=self.COLOR_HIGHLIGHT, flash_radius=0.8, num_lines=12),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeOut(self.author_info),
            FadeIn(author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰元素 - 百分号旋转
        decorations = VGroup(*[
            MathTex(r"\%", font_size=40, color=color)
            .move_to(2 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i, color in enumerate([
                self.COLOR_DISCOUNT, self.COLOR_INTEREST, self.COLOR_CONCENTRATION,
                self.COLOR_DISCOUNT, self.COLOR_INTEREST, self.COLOR_CONCENTRATION
            ])
        ]).move_to(follow_text.get_center() + DOWN * 1.5)
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI, run_time=2))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(
                title, cards, key_point,
                author_large, author_id, follow_text, decorations
            )),
            run_time=1.0
        )
    
    def create_summary_card(self, name, formula, color, position):
        """创建总结卡片"""
        # 背景
        bg = RoundedRectangle(
            width=7.5,
            height=0.9,
            corner_radius=0.12,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=2
        )
        
        # 名称
        name_text = Text(
            name,
            font="PingFang SC",
            font_size=28,
            color=color,
            weight=BOLD
        )
        
        # 公式
        formula_text = Text(
            formula,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 组合
        content = VGroup(name_text, formula_text).arrange(RIGHT, buff=0.5)
        card = VGroup(bg, content)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql percentage_applications.py PercentageApplications  # 快速预览
# manim -qh percentage_applications.py PercentageApplications   # 高质量渲染