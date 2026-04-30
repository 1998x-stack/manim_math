"""
数据的收集与整理教学动画 - Data Collection and Organization Animation
使用 Manim 创建的九年级统计教学视频

内容: 数据收集方式、频数分布表、频率计算
目标观众: 九年级学生
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


class DataCollectionOrganization(Scene):
    """
    数据的收集与整理教学动画场景
    
    场景顺序:
    1. 开场钩子（班级统计身高）
    2. 统计步骤介绍
    3. 数据收集方式（普查vs抽样）
    4. 原始数据展示
    5. 数据分组
    6. 频数分布表
    7. 频率概念
    8. 柱状图展示
    9. 结尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主色调
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调色
        self.COLOR_SUCCESS = "#2ecc71"        # 绿色 - 成功
        self.COLOR_WARNING = "#f39c12"        # 橙色 - 警告
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_TABLE = WHITE              # 白色 - 表格
        
        # 数据设置
        self.setup_data()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_statistics_steps()
        self.scene_3_data_collection_methods()
        self.scene_4_raw_data()
        self.scene_5_data_grouping()
        self.scene_6_frequency_table()
        self.scene_7_rate_concept()
        self.scene_8_bar_chart()
        self.scene_9_outro()
    
    def setup_data(self):
        """设置示例数据"""
        # 原始数据：20个学生的身高（cm）
        # 按分组调整数据，确保频数匹配
        self.raw_data = [
            # 155-159组: 4个
            155, 157, 158, 159,
            # 160-164组: 6个
            160, 161, 162, 162, 163, 164,
            # 165-169组: 5个
            165, 166, 167, 168, 169,
            # 170-174组: 5个
            170, 171, 172, 173, 174
        ]
        
        # 分组
        self.groups = ["155-159", "160-164", "165-169", "170-174"]
        
        # 频数
        self.frequencies = [4, 6, 5, 5]
        
        # 频率
        self.rates = [0.20, 0.30, 0.25, 0.25]
        
        # 数据总数
        self.total = len(self.raw_data)
        
        # 验证数据
        assert sum(self.frequencies) == self.total, "频数和不等于总数"
        assert abs(sum(self.rates) - 1.0) < 1e-6, "频率和不等于1"
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "班级要统计身高",
            font="PingFang SC",
            font_size=50,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 数据图标（一堆数字）
        data_icons = VGroup(*[
            Text(str(d), font_size=28, color=WHITE)
            for d in self.raw_data[:10]
        ]).arrange_in_grid(rows=2, cols=5, buff=0.3).move_to(UP * 2)
        
        self.play(
            LaggedStart(
                *[FadeIn(icon, scale=0.5) for icon in data_icons],
                lag_ratio=0.1
            ),
            run_time=1.0
        )
        
        # 问题文字
        question = Text(
            "这么多数据怎么整理？",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            FadeOut(data_icons),
            run_time=0.6
        )
    
    def scene_2_statistics_steps(self):
        """场景2: 统计步骤介绍"""
        # 标题
        title = Text(
            "统计的步骤",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 四个步骤卡片
        steps = [
            ("1", "收集数据", self.COLOR_PRIMARY),
            ("2", "整理数据", self.COLOR_SECONDARY),
            ("3", "描述数据", self.COLOR_SUCCESS),
            ("4", "分析数据", self.COLOR_WARNING)
        ]
        
        step_mobjects = []
        for i, (num, text, color) in enumerate(steps):
            # 数字圆
            circle = Circle(radius=0.4, color=color, fill_opacity=0.8)
            number = Text(num, font_size=36, color=WHITE, weight=BOLD)
            circle_group = VGroup(circle, number)
            
            # 文字
            step_text = Text(text, font="PingFang SC", font_size=28, color=color)
            
            # 组合
            step_card = VGroup(circle_group, step_text).arrange(RIGHT, buff=0.4)
            step_card.move_to(UP * (2 - i * 1.2))
            
            step_mobjects.append(step_card)
        
        # 逐个显示
        for step in step_mobjects:
            self.play(FadeIn(step, shift=LEFT * 0.5), run_time=0.5)
        
        # 连接箭头
        arrows = VGroup()
        for i in range(len(step_mobjects) - 1):
            arrow = Arrow(
                step_mobjects[i].get_bottom() + DOWN * 0.1,
                step_mobjects[i+1].get_top() + UP * 0.1,
                color=GRAY_B,
                buff=0,
                stroke_width=3
            )
            arrows.add(arrow)
        
        self.play(Create(arrows), run_time=0.6)
        
        # 高亮前两步（重点）
        self.play(
            Indicate(step_mobjects[0], scale_factor=1.1),
            Indicate(step_mobjects[1], scale_factor=1.1),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(*step_mobjects)),
            FadeOut(arrows),
            FadeOut(title),
            run_time=0.6
        )
    
    def scene_3_data_collection_methods(self):
        """场景3: 数据收集方式"""
        # 标题
        title = Text(
            "数据收集方式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 普查卡片
        census_title = Text(
            "普查（全面调查）",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 3.5)
        
        census_desc = Text(
            "调查全部对象",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(census_title, DOWN, buff=0.3)
        
        # 普查视觉（10个实心圆）
        census_visual = VGroup(*[
            Dot(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=1)
            for _ in range(10)
        ]).arrange(RIGHT, buff=0.3).move_to(UP * 2.2)
        
        self.play(FadeIn(census_title), run_time=0.6)
        self.play(Write(census_desc), run_time=0.8)
        self.play(
            LaggedStart(
                *[GrowFromCenter(dot) for dot in census_visual],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        
        # 抽样调查卡片
        sample_title = Text(
            "抽样调查",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 0.8)
        
        sample_desc = Text(
            "调查部分对象",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(sample_title, DOWN, buff=0.3)
        
        # 抽样视觉（部分实心，部分空心）
        sample_visual = VGroup()
        for i in range(10):
            if i % 3 == 0:  # 每3个抽1个
                dot = Dot(radius=0.15, color=self.COLOR_SECONDARY, fill_opacity=1)
            else:
                dot = Circle(radius=0.15, color=GRAY_B, fill_opacity=0, stroke_width=2)
            sample_visual.add(dot)
        sample_visual.arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(FadeIn(sample_title), run_time=0.6)
        self.play(Write(sample_desc), run_time=0.8)
        self.play(
            LaggedStart(
                *[GrowFromCenter(dot) for dot in sample_visual],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        
        # 对比表
        comparison_data = [
            ["全部", "高", "高"],
            ["部分", "较高", "低"]
        ]
        
        comparison_table = Table(
            comparison_data,
            row_labels=[
                Text("普查", font="PingFang SC", font_size=20),
                Text("抽样", font="PingFang SC", font_size=20)
            ],
            col_labels=[
                Text("范围", font="PingFang SC", font_size=20),
                Text("准确", font="PingFang SC", font_size=20),
                Text("成本", font="PingFang SC", font_size=20)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1}
        ).scale(0.5).move_to(DOWN * 3)
        
        self.play(Create(comparison_table), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in [
                title, census_title, census_desc, census_visual,
                sample_title, sample_desc, sample_visual, comparison_table
            ]],
            run_time=0.6
        )
    
    def scene_4_raw_data(self):
        """场景4: 原始数据展示"""
        # 标题
        title = Text(
            "原始数据",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 数据说明
        data_desc = Text(
            "学生身高（cm）：",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(data_desc), run_time=0.5)
        
        # 原始数据（分两行显示）
        data_row1 = VGroup(*[
            Text(str(d), font_size=24, color=WHITE)
            for d in self.raw_data[:10]
        ]).arrange(RIGHT, buff=0.3).move_to(UP * 2.8)
        
        data_row2 = VGroup(*[
            Text(str(d), font_size=24, color=WHITE)
            for d in self.raw_data[10:]
        ]).arrange(RIGHT, buff=0.3).move_to(UP * 2)
        
        data_numbers = VGroup(data_row1, data_row2)
        
        self.play(
            LaggedStart(
                *[Write(num) for num in data_row1],
                lag_ratio=0.1
            ),
            run_time=1.0
        )
        self.play(
            LaggedStart(
                *[Write(num) for num in data_row2],
                lag_ratio=0.1
            ),
            run_time=1.0
        )
        
        # 混乱强调
        self.play(
            Wiggle(data_numbers, scale_value=1.1),
            run_time=0.6
        )
        
        # 问题文字
        problem_text = Text(
            "数据太乱了，怎么办？",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_WARNING
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(problem_text, scale=1.1), run_time=0.5)
        self.wait(1.0)
        
        # 保存数据用于下一场景
        self.data_numbers = data_numbers
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem_text),
            run_time=0.6
        )
    
    def scene_5_data_grouping(self):
        """场景5: 数据分组"""
        # 标题
        title = Text(
            "数据分组",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 分组说明
        group_desc = Text(
            "按身高分成4组：",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(group_desc), run_time=0.5)
        
        # 创建4个分组框
        colors = [self.COLOR_PRIMARY, "#9b59b6", "#1abc9c", self.COLOR_WARNING]
        group_boxes = VGroup()
        
        for i, (group_name, freq, color) in enumerate(zip(self.groups, self.frequencies, colors)):
            # 组名
            label = Text(
                group_name,
                font="PingFang SC",
                font_size=24,
                color=color
            )
            
            # 框
            box = Rectangle(
                width=3.5,
                height=0.8,
                color=color,
                stroke_width=3,
                fill_opacity=0.1
            )
            
            VGroup(label, box).arrange(DOWN, buff=0.1)
            group_boxes.add(VGroup(label, box))
        
        group_boxes.arrange(DOWN, buff=0.4).move_to(UP * 0.5)
        
        self.play(
            LaggedStart(
                *[Create(box[1]) for box in group_boxes],
                lag_ratio=0.2
            ),
            run_time=0.8
        )
        self.play(
            *[Write(box[0]) for box in group_boxes],
            run_time=0.6
        )
        
        # 数据归类动画（简化版）
        # 让数据快速淡出然后频数显示
        self.play(FadeOut(self.data_numbers), run_time=0.5)
        
        # 显示各组频数
        freq_labels = VGroup()
        for i, (box, freq) in enumerate(zip(group_boxes, self.frequencies)):
            freq_text = Text(
                f"频数: {freq}",
                font="PingFang SC",
                font_size=22,
                color=WHITE
            ).move_to(box[1].get_center())
            freq_labels.add(freq_text)
        
        self.play(
            LaggedStart(
                *[Write(label) for label in freq_labels],
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        
        # 高亮结果
        self.play(
            LaggedStart(
                *[Indicate(label, scale_factor=1.2) for label in freq_labels],
                lag_ratio=0.1
            ),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(group_desc),
            FadeOut(group_boxes),
            FadeOut(freq_labels),
            run_time=0.6
        )
    
    def scene_6_frequency_table(self):
        """场景6: 频数分布表"""
        # 标题
        title = Text(
            "频数分布表",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 创建表格数据
        table_data = [
            [self.groups[0], str(self.frequencies[0])],
            [self.groups[1], str(self.frequencies[1])],
            [self.groups[2], str(self.frequencies[2])],
            [self.groups[3], str(self.frequencies[3])],
        ]
        
        # 创建表格
        freq_table = Table(
            table_data,
            row_labels=[
                Text(g, font="PingFang SC", font_size=24) 
                for g in ["分组1", "分组2", "分组3", "分组4"]
            ],
            col_labels=[
                Text("身高分组(cm)", font="PingFang SC", font_size=24),
                Text("频数", font="PingFang SC", font_size=24)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            element_to_mobject_config={"font_size": 28}
        ).scale(0.65).move_to(UP * 1.5)
        
        # 逐步创建表格
        # 先创建框架
        self.play(Create(freq_table.get_horizontal_lines()), run_time=0.4)
        self.play(Create(freq_table.get_vertical_lines()), run_time=0.4)
        
        # 表头
        self.play(
            *[Write(label) for label in freq_table.get_col_labels()],
            run_time=0.6
        )
        
        # 逐行数据
        entries = freq_table.get_entries()
        for i in range(0, len(entries), 2):  # 每行2个单元格
            self.play(
                Write(entries[i]),
                Write(entries[i+1]),
                run_time=0.5
            )
        
        # 合计行
        total_text = Text(
            f"合计: {self.total}",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).next_to(freq_table, DOWN, buff=0.3)
        
        self.play(Write(total_text), run_time=0.6)
        
        # 表格高亮
        self.play(
            Indicate(freq_table, scale_factor=1.05),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 保存表格供后续使用
        self.freq_table = freq_table
        self.total_text = total_text
        
        # 缩小并移到左侧
        self.play(
            VGroup(freq_table, total_text).animate.scale(0.7).move_to(LEFT * 3 + UP * 2),
            FadeOut(title),
            run_time=0.6
        )
    
    def scene_7_rate_concept(self):
        """场景7: 频率概念"""
        # 标题
        title = Text(
            "频率",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 频率定义
        definition = Text(
            "频率表示各组数据占总数的比例",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.6)
        
        # 频率公式
        formula = MathTex(
            r"\text{Rate} = \frac{\text{Frequency}}{\text{Total}}",
            font_size=36
        ).move_to(UP * 3.5)
        
        formula_cn = Text(
            "频率 = 频数 / 总数",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_PRIMARY
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(Write(formula), run_time=0.8)
        self.play(FadeIn(formula_cn), run_time=0.5)
        
        # 示例计算
        calc_title = Text(
            "计算示例：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 1.8)
        
        self.play(Write(calc_title), run_time=0.5)
        
        # 第1组计算
        calc1 = MathTex(
            r"155\text{-}159: \quad",
            r"\frac{4}{20} = 0.20",
            font_size=28
        ).move_to(UP * 1)
        calc1[1].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(calc1), run_time=1.0)
        
        # 第2组计算
        calc2 = MathTex(
            r"160\text{-}164: \quad",
            r"\frac{6}{20} = 0.30",
            font_size=28
        ).move_to(UP * 0.2)
        calc2[1].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(calc2), run_time=1.0)
        
        # 添加频率列（完整表格）
        complete_table_data = [
            [self.groups[0], str(self.frequencies[0]), f"{self.rates[0]:.2f}"],
            [self.groups[1], str(self.frequencies[1]), f"{self.rates[1]:.2f}"],
            [self.groups[2], str(self.frequencies[2]), f"{self.rates[2]:.2f}"],
            [self.groups[3], str(self.frequencies[3]), f"{self.rates[3]:.2f}"],
        ]
        
        complete_table = Table(
            complete_table_data,
            col_labels=[
                Text("身高(cm)", font="PingFang SC", font_size=20),
                Text("频数", font="PingFang SC", font_size=20),
                Text("频率", font="PingFang SC", font_size=20)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 2},
            element_to_mobject_config={"font_size": 22}
        ).scale(0.5).move_to(DOWN * 2)
        
        self.play(Create(complete_table), run_time=1.0)
        
        # 频率和性质
        sum_property = Text(
            "各组频率之和 = 1",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_WARNING,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        sum_check = MathTex(
            r"0.20 + 0.30 + 0.25 + 0.25 = 1.00 \quad \checkmark",
            font_size=24,
            color=self.COLOR_SUCCESS
        ).next_to(sum_property, DOWN, buff=0.3)
        
        self.play(FadeIn(sum_property), run_time=0.8)
        self.play(Write(sum_check), run_time=0.8)
        self.play(Indicate(sum_check, scale_factor=1.15), run_time=0.6)
        
        self.wait(2.0)
        
        # 保存完整表格
        self.complete_table = complete_table
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(formula),
            FadeOut(formula_cn),
            FadeOut(calc_title),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(sum_property),
            FadeOut(sum_check),
            FadeOut(self.freq_table),
            FadeOut(self.total_text),
            run_time=0.6
        )
        
        # 表格移到右上角
        self.play(
            complete_table.animate.scale(0.8).move_to(RIGHT * 2.5 + UP * 5),
            run_time=0.5
        )
    
    def scene_8_bar_chart(self):
        """场景8: 柱状图展示"""
        # 标题
        title = Text(
            "柱状图",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5 + LEFT * 2)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 创建柱状图
        chart = BarChart(
            values=self.frequencies,
            bar_names=self.groups,
            y_range=[0, 8, 2],
            y_length=5,
            x_length=7,
            x_axis_config={"font_size": 20},
            bar_colors=[self.COLOR_PRIMARY, "#9b59b6", "#1abc9c", self.COLOR_WARNING],
            bar_fill_opacity=0.8
        ).move_to(DOWN * 0.5)
        
        # 坐标轴
        self.play(Create(chart.get_axes()), run_time=0.8)
        
        # 柱子逐个生长
        bars = chart.get_bars()
        for bar in bars:
            self.play(GrowFromEdge(bar, DOWN), run_time=0.6)
        
        # 数值标注
        bar_labels = VGroup()
        for i, (bar, freq) in enumerate(zip(bars, self.frequencies)):
            label = Text(
                str(freq),
                font_size=24,
                color=WHITE,
                weight=BOLD
            ).next_to(bar, UP, buff=0.1)
            bar_labels.add(label)
        
        self.play(
            *[Write(label) for label in bar_labels],
            run_time=0.8
        )
        
        # 横坐标标签
        x_labels = chart.get_bar_labels(font_size=18)
        self.play(Write(x_labels), run_time=0.6)
        
        # 纵坐标标签
        y_label = Text(
            "频数",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(chart.get_axes()[1], LEFT, buff=0.3)
        
        self.play(Write(y_label), run_time=0.4)
        
        # 图表标题
        chart_title = Text(
            "学生身高频数分布",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(chart, DOWN, buff=0.5)
        
        self.play(Write(chart_title), run_time=0.5)
        
        # 高亮最高柱
        max_bar = bars[self.frequencies.index(max(self.frequencies))]
        self.play(
            Indicate(max_bar, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in [
                title, chart, bar_labels, x_labels, y_label, chart_title
            ]],
            run_time=0.6
        )
    
    def scene_9_outro(self):
        """场景9: 结尾总结"""
        # 总结标题
        summary_title = Text(
            "知识总结",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 关键点
        points = [
            "① 数据分组，计算频数",
            "② 频率 = 频数 / 总数",
            "③ 各组频率之和 = 1"
        ]
        
        point_mobjects = VGroup()
        for i, point in enumerate(points):
            point_text = Text(
                point,
                font="PingFang SC",
                font_size=28,
                color=WHITE
            ).move_to(UP * (2.5 - i * 0.8))
            point_mobjects.add(point_text)
        
        for point in point_mobjects:
            self.play(FadeIn(point, shift=UP * 0.2), run_time=0.5)
        
        # 公式框
        formulas = VGroup(
            Text("频数 = 该组出现次数", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("频率 = 频数/总数", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("频率和 = 1", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 0.5)
        
        formula_box = SurroundingRectangle(
            formulas,
            color=self.COLOR_PRIMARY,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(
            Create(formula_box),
            *[FadeIn(f, shift=RIGHT * 0.2) for f in formulas],
            run_time=0.8
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            self.author_info.animate.become(author_large),
            FadeIn(author_id, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多统计技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        self.play(
            Write(follow_text),
            follow_text.animate.scale(1.1),
            run_time=0.8
        )
        
        # 装饰（柱状图图标）
        deco_bars = VGroup(*[
            Rectangle(
                width=0.3,
                height=0.5 + i * 0.2,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.8
            )
            for i in range(4)
        ]).arrange(RIGHT, buff=0.2).scale(0.8).move_to(DOWN * 6.8)
        
        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, DOWN) for bar in deco_bars],
                lag_ratio=0.2
            ),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in [
                summary_title, point_mobjects, formulas, formula_box,
                self.author_info, author_id, follow_text, deco_bars,
                self.complete_table
            ]],
            run_time=1.0
        )


# 运行命令:
# manim -pql data_collection_organization.py DataCollectionOrganization  # 快速预览
# manim -qh data_collection_organization.py DataCollectionOrganization   # 高质量 1080p
# manim -qk data_collection_organization.py DataCollectionOrganization   # 4K质量