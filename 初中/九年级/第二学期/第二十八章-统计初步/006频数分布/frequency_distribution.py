"""
频数分布教学动画 - Frequency Distribution
使用 Manim 创建的中学统计学教学视频

内容: 频数分布的整理过程和直方图绘制
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FrequencyDistribution(Scene):
    """
    频数分布教学动画
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 原始数据展示 - 杂乱数据
    3. 计算极差 - 数据范围
    4. 确定组距和组数 - 数据分组
    5. 频数分布表 - 整理数据
    6. 频数直方图 - 可视化
    7. 频率直方图 - 标准化
    8. 总结和片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"    # 红色
        self.COLOR_HISTOGRAM = "#9b59b6"    # 紫色
        self.COLOR_TABLE = "#2ecc71"        # 绿色
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色
        self.COLOR_AUXILIARY = GRAY_B       # 灰色
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 原始数据（30个学生成绩）
        self.raw_data = np.array([
            85, 72, 68, 90, 55, 78, 82, 95, 61, 77,
            88, 70, 92, 66, 81, 74, 87, 59, 79, 84,
            91, 73, 86, 63, 75, 89, 67, 80, 94, 71
        ])
        
        # 统计数据
        self.max_val = 95
        self.min_val = 55
        self.range_val = 40
        self.group_width = 10
        
        # 频数分布（验证后的正确值）
        self.groups = [
            ("50-60", 2, 0.067),
            ("60-70", 5, 0.167),
            ("70-80", 9, 0.300),
            ("80-90", 9, 0.300),
            ("90-100", 5, 0.167)
        ]
        
        self.total = 30
        
        # 执行动画序列
        self.show_opening()
        self.show_raw_data()
        self.show_range_calculation()
        self.show_grouping()
        self.show_frequency_table()
        self.show_histogram()
        self.show_frequency_histogram()
        self.show_summary_and_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "30个学生的成绩",
            font=self.FONT_CHINESE,
            font_size=42,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 杂乱数据预览（部分）
        data_preview = VGroup(
            *[Text(str(val), font=self.FONT_CHINESE, font_size=24, color=self.COLOR_PRIMARY)
              for val in self.raw_data[:12]]
        ).arrange_in_grid(rows=3, cols=4, buff=0.5).move_to(UP * 2)
        
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.8) for d in data_preview], lag_ratio=0.1),
            run_time=1.2
        )
        
        # 问题
        question = Text(
            "如何整理这些数据?",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(Write(question), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(data_preview),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_raw_data(self):
        """场景2: 原始数据展示 (5-12秒)"""
        # 标题
        title = Text(
            "原始数据：30个学生成绩",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 数据网格（6行5列）
        self.data_grid = VGroup()
        for i, val in enumerate(self.raw_data):
            row = i // 5
            col = i % 5
            cell = Text(
                str(val),
                font=self.FONT_CHINESE,
                font_size=22,
                color=self.COLOR_PRIMARY
            )
            cell.move_to(np.array([col * 0.8 - 1.6, 3.5 - row * 0.6, 0]))
            self.data_grid.add(cell)
        
        # 逐个显示
        self.play(
            LaggedStart(*[FadeIn(cell, scale=0.7) for cell in self.data_grid], lag_ratio=0.05),
            run_time=2.5
        )
        
        # 说明
        explanation = Text(
            "数据杂乱，难以看出规律",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.0)
        
        # 清理说明，保留数据用于标记
        self.play(FadeOut(explanation), run_time=0.3)
        
        # 保存标题
        self.current_title = title
    
    def show_range_calculation(self):
        """场景3: 计算极差 (12-20秒)"""
        # 新标题
        new_title = Text(
            "步骤1：计算极差",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 找出最大值和最小值
        max_index = np.where(self.raw_data == self.max_val)[0][0]
        min_index = np.where(self.raw_data == self.min_val)[0][0]
        
        max_cell = self.data_grid[max_index]
        min_cell = self.data_grid[min_index]
        
        # 高亮最大值
        self.play(
            max_cell.animate.set_color(self.COLOR_SECONDARY).scale(1.3),
            run_time=0.8
        )
        
        max_label = Text(
            "最大值",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_SECONDARY
        ).next_to(max_cell, UP, buff=0.1)
        
        self.play(FadeIn(max_label), run_time=0.4)
        
        # 高亮最小值
        self.play(
            min_cell.animate.set_color(self.COLOR_SECONDARY).scale(1.3),
            run_time=0.8
        )
        
        min_label = Text(
            "最小值",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_SECONDARY
        ).next_to(min_cell, DOWN, buff=0.1)
        
        self.play(FadeIn(min_label), run_time=0.4)
        
        # 公式 (使用英文避免LaTeX编译错误)
        formula = MathTex(
            r"\text{Range} = \text{Max} - \text{Min}",
            font_size=28
        ).move_to(DOWN * 1.5)
        
        # 中文解释 (作为普通文本对象)
        chinese_explanation = Text(
            "极差 = 最大值 - 最小值",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        self.play(Write(formula), run_time=1.0)
        self.play(Write(chinese_explanation), run_time=1.0)
        
        # 计算
        calculation = MathTex(
            r"= 95 - 55 = 40",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, DOWN, buff=0.4)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 说明
        meaning = Text(
            "极差表示数据的分布范围",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(meaning), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(self.data_grid),
            FadeOut(max_label),
            FadeOut(min_label),
            FadeOut(formula),
            FadeOut(meaning),
            run_time=0.5
        )
        
        # 保留计算结果
        self.range_result = calculation
    
    def show_grouping(self):
        """场景4: 确定组距和组数 (20-28秒)"""
        # 新标题
        new_title = Text(
            "步骤2：确定组距和组数",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(
            Transform(self.current_title, new_title),
            self.range_result.animate.move_to(UP * 5),
            run_time=0.6
        )
        
        # 组距说明
        width_text = Text(
            "选择合适的组距（如10分）",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(width_text), run_time=0.6)
        
        # 组数公式
        formula_groups = MathTex(
            r"\text{Groups} \approx \frac{\text{Range}}{\text{Width}}",
            font_size=28
        ).move_to(UP * 1.5)
        
        # 中文解释
        chinese_explanation_2 = Text(
            "组数 ≈ 极差÷组距",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Write(formula_groups), run_time=1.0)
        self.play(Write(chinese_explanation_2), run_time=1.0)
        
        # 计算
        calc_groups = MathTex(
            r"= \frac{40}{10} = 4",
            font_size=28
        ).next_to(formula_groups, DOWN, buff=0.3)
        
        self.play(Write(calc_groups), run_time=1.0)
        
        # 确定分组
        final_groups = Text(
            "确定5组：50-60, 60-70, ..., 90-100",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(final_groups, shift=UP * 0.3), run_time=0.8)
        
        # 分组示意（数轴）
        number_line = Line(LEFT * 3, RIGHT * 3, color=self.COLOR_AUXILIARY).move_to(DOWN * 1.5)
        
        # 标记点
        marks = VGroup()
        labels_group = VGroup()
        
        for i, val in enumerate([50, 60, 70, 80, 90, 100]):
            pos = number_line.point_from_proportion((val - 50) / 50)
            mark = Line(pos + UP * 0.15, pos + DOWN * 0.15, color=self.COLOR_AUXILIARY)
            marks.add(mark)
            
            label = Text(str(val), font=self.FONT_CHINESE, font_size=18, color=GRAY_A)
            label.next_to(mark, DOWN, buff=0.2)
            labels_group.add(label)
        
        self.play(
            Create(number_line),
            Create(marks),
            FadeIn(labels_group),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(self.range_result),
            FadeOut(width_text),
            FadeOut(formula_groups),
            FadeOut(calc_groups),
            FadeOut(final_groups),
            FadeOut(number_line),
            FadeOut(marks),
            FadeOut(labels_group),
            run_time=0.5
        )
    
    def show_frequency_table(self):
        """场景5: 频数分布表 (28-40秒)"""
        # 新标题
        new_title = Text(
            "步骤3：列频数分布表",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 创建表格数据
        table_data = [
            ["分组", "频数", "频率"]
        ]
        
        for group, freq, freq_rate in self.groups:
            table_data.append([group, str(freq), f"{freq_rate:.2f}"])
        
        table_data.append(["合计", str(self.total), "1.00"])
        
        # 使用 MobjectTable
        from manim import Table
        
        self.freq_table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": self.COLOR_TABLE},
            element_to_mobject_config={"font_size": 24}
        ).scale(0.7).move_to(UP * 2)
        
        # 逐行显示
        self.play(Create(self.freq_table), run_time=2.0)
        
        # 说明频率计算
        freq_explain = Text(
            "频率 = 频数 ÷ 总数",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(freq_explain), run_time=0.5)
        
        # 示例 (英文版)
        example = MathTex(
            r"\text{e.g., } \frac{9}{30} = 0.30",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(freq_explain, DOWN, buff=0.3)
        
        # 中文示例说明
        example_chinese = Text(
            "例如：9÷30=0.30",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(freq_explain, DOWN, buff=0.3)
        
        self.play(Write(example), run_time=0.6)
        self.play(Write(example_chinese), run_time=0.6)
        
        self.wait(2.0)
        
        # 缩小表格移至左侧
        self.play(
            self.freq_table.animate.scale(0.6).move_to(LEFT * 3 + UP * 2),
            FadeOut(freq_explain),
            FadeOut(example),
            FadeOut(example_chinese),
            run_time=0.6
        )
    
    def show_histogram(self):
        """场景6: 频数直方图 (40-52秒)"""
        # 新标题
        new_title = Text(
            "步骤4：画频数分布直方图",
            font=self.FONT_CHINESE,
            font_size=30,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=[50, 100, 10],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "color": GRAY_B
            },
            tips=False
        ).move_to(RIGHT * 1 + UP * 1)
        
        # 轴标签
        x_label = Text("分数", font=self.FONT_CHINESE, font_size=20, color=GRAY_A)
        x_label.next_to(self.axes.x_axis, DOWN, buff=0.2)
        
        y_label = Text("频数", font=self.FONT_CHINESE, font_size=20, color=GRAY_A)
        y_label.next_to(self.axes.y_axis, LEFT, buff=0.2)
        
        self.play(
            Create(self.axes),
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=1.5
        )
        
        # 创建直方图柱子
        self.bars = VGroup()
        bar_labels = VGroup()
        
        x_positions = [55, 65, 75, 85, 95]  # 每组的中心
        frequencies = [2, 5, 9, 9, 5]
        
        for i, (x_center, freq) in enumerate(zip(x_positions, frequencies)):
            # 计算柱子位置
            x_start = x_center - 5
            x_end = x_center + 5
            
            # 创建矩形
            bar = Rectangle(
                width=self.axes.x_axis.unit_size * 10,
                height=self.axes.y_axis.unit_size * freq,
                fill_color=self.COLOR_HISTOGRAM,
                fill_opacity=0.7,
                stroke_color=WHITE,
                stroke_width=2
            )
            
            # 定位
            bar.move_to(self.axes.c2p(x_center, freq / 2))
            self.bars.add(bar)
            
            # 频数标签
            label = Text(
                str(freq),
                font=self.FONT_CHINESE,
                font_size=18,
                color=WHITE
            )
            label.next_to(bar, UP, buff=0.1)
            bar_labels.add(label)
        
        # 逐个绘制柱子
        for bar, label in zip(self.bars, bar_labels):
            self.play(
                GrowFromEdge(bar, DOWN),
                FadeIn(label, shift=DOWN * 0.3),
                run_time=0.8
            )
        
        # 说明
        explanation = Text(
            "直方图直观展示数据分布",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(explanation), run_time=0.3)
        
        # 保存标签
        self.bar_labels = bar_labels
        self.x_label = x_label
        self.y_label = y_label
    
    def show_frequency_histogram(self):
        """场景7: 频率直方图 (52-62秒)"""
        # 新标题
        new_title = Text(
            "频率直方图：面积之和=1",
            font=self.FONT_CHINESE,
            font_size=30,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 说明变换
        transform_text = Text(
            "纵轴改为：频率/组距",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(transform_text), run_time=0.8)
        
        # 纵轴标签变换
        new_y_label = Text("频率/组距", font=self.FONT_CHINESE, font_size=18, color=GRAY_A)
        new_y_label.next_to(self.axes.y_axis, LEFT, buff=0.2)
        
        self.play(Transform(self.y_label, new_y_label), run_time=0.8)
        
        # 计算新高度（频率/组距）
        frequencies = [2, 5, 9, 9, 5]
        freq_densities = [f / self.total / self.group_width for f in frequencies]
        
        # 调整柱子高度（但保持视觉效果，按比例缩放）
        # 实际上频率/组距的值很小，我们需要放大显示
        scale_factor = 100  # 放大100倍便于显示
        
        new_bars = VGroup()
        new_labels = VGroup()
        
        for i, (bar, density) in enumerate(zip(self.bars, freq_densities)):
            x_center = [55, 65, 75, 85, 95][i]
            
            # 新柱子（视觉上保持相似高度，实际代表频率/组距）
            new_bar = Rectangle(
                width=self.axes.x_axis.unit_size * 10,
                height=self.axes.y_axis.unit_size * density * scale_factor,
                fill_color=self.COLOR_HISTOGRAM,
                fill_opacity=0.7,
                stroke_color=WHITE,
                stroke_width=2
            )
            new_bar.move_to(self.axes.c2p(x_center, density * scale_factor / 2))
            new_bars.add(new_bar)
            
            # 新标签
            new_label = Text(
                f"{density:.3f}",
                font=self.FONT_CHINESE,
                font_size=16,
                color=WHITE
            )
            new_label.next_to(new_bar, UP, buff=0.1)
            new_labels.add(new_label)
        
        # 变换动画
        self.play(
            *[Transform(old, new) for old, new in zip(self.bars, new_bars)],
            *[Transform(old, new) for old, new in zip(self.bar_labels, new_labels)],
            run_time=2.0
        )
        
        # 公式说明 (英文版)
        formula = MathTex(
            r"\text{Area} = \frac{\text{Freq}}{\text{Width}} \times \text{Width} = \text{Freq}",
            font_size=20
        ).move_to(DOWN * 2.5)
        
        # 中文公式说明
        formula_chinese = Text(
            "面积 = (频率÷组距)×组距 = 频率",
            font=self.FONT_CHINESE,
            font_size=18,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(Write(formula), run_time=1.0)
        self.play(Write(formula_chinese), run_time=1.0)
        
        # 面积之和
        area_sum = Text(
            "所有矩形面积之和 = 1",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(area_sum, shift=UP * 0.3), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(transform_text),
            FadeOut(formula),
            FadeOut(area_sum),
            run_time=0.5
        )
    
    def show_summary_and_outro(self):
        """场景8: 总结和片尾 (62-75秒)"""
        # 清空画面
        self.play(
            FadeOut(self.current_title),
            FadeOut(self.freq_table),
            FadeOut(self.axes),
            FadeOut(self.bars),
            FadeOut(self.bar_labels),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.5
        )
        
        # 总结标题
        summary_title = Text(
            "频数分布四步骤",
            font=self.FONT_CHINESE,
            font_size=38,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 四个步骤
        steps = VGroup(
            Text("1. 计算极差（最大值-最小值）", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("2. 确定组距和组数", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("3. 列频数分布表", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("4. 画频数分布直方图", font=self.FONT_CHINESE, font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 2)
        
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.8)
        
        # 关键要点
        key_points = VGroup(
            Text("● 直方图能直观展示数据分布", font=self.FONT_CHINESE, font_size=22, color=GRAY_A),
            Text("● 频率直方图面积之和=1", font=self.FONT_CHINESE, font_size=22, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 1.5)
        
        self.play(FadeIn(key_points, shift=UP * 0.3), run_time=1.5)
        
        self.wait(2.0)
        
        # 清空准备片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(steps),
            FadeOut(key_points),
            run_time=0.6
        )
        
        # 片尾
        author_large = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多统计技巧！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标
        icons = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = follow.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 小直方图图标
            icon_bars = VGroup(
                Rectangle(width=0.15, height=0.2, fill_color=self.COLOR_HISTOGRAM, fill_opacity=0.8, stroke_width=0),
                Rectangle(width=0.15, height=0.35, fill_color=self.COLOR_HISTOGRAM, fill_opacity=0.8, stroke_width=0),
                Rectangle(width=0.15, height=0.25, fill_color=self.COLOR_HISTOGRAM, fill_opacity=0.8, stroke_width=0)
            ).arrange(RIGHT, buff=0.05)
            icon_bars.move_to(pos)
            icons.add(icon_bars)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.play(Rotate(icons, angle=PI/2, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql frequency_distribution.py FrequencyDistribution    # 快速预览
# manim -qm frequency_distribution.py FrequencyDistribution     # 中等质量
# manim -qh frequency_distribution.py FrequencyDistribution     # 高质量 1080p