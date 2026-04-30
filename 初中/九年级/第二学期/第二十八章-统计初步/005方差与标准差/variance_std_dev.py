"""
方差与标准差教学动画 - Variance and Standard Deviation
使用 Manim 创建的中学统计学教学视频

内容: 方差与标准差的概念、计算和意义
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


class VarianceAndStdDev(Scene):
    """
    方差与标准差教学动画
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 建立坐标系 - 展示数据
    3. 平均数线 - 数据中心
    4. 偏差可视化 - 波动对比
    5. 方差公式 - 计算过程
    6. 标准差 - 单位恢复
    7. 总结对比 - 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 数据集A（稳定）
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 数据集B（波动）
        self.COLOR_MEAN = "#2ecc71"         # 绿色 - 平均数
        self.COLOR_DEVIATION = "#f39c12"    # 橙色 - 偏差
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 数据集
        self.data_a = np.array([5, 5, 5, 5, 5], dtype=float)
        self.data_b = np.array([1, 3, 5, 7, 9], dtype=float)
        self.mean_val = 5.0
        self.variance_a = 0.0
        self.variance_b = 8.0
        self.std_b = np.sqrt(8.0)
        
        # 执行动画序列
        self.show_opening()
        self.show_axes_and_data()
        self.show_mean_line()
        self.show_deviations()
        self.show_variance_formula()
        self.show_standard_deviation()
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
            "两组数据，平均分都是5分",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 快速展示两组数据
        preview_a = Text(
            "A组: 5, 5, 5, 5, 5",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.5)
        
        preview_b = Text(
            "B组: 1, 3, 5, 7, 9",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2.5)
        
        self.play(
            FadeIn(preview_a, shift=RIGHT * 0.3),
            FadeIn(preview_b, shift=LEFT * 0.3),
            run_time=0.6
        )
        
        # 问题
        question = Text(
            "哪组成绩更稳定?",
            font=self.FONT_CHINESE,
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(Write(question), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(preview_a),
            FadeOut(preview_b),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_axes_and_data(self):
        """场景2: 建立坐标系 (5-10秒)"""
        # 标题
        title = Text(
            "方差：衡量数据的波动程度",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=5,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "color": GRAY_B
            },
            tips=False
        ).move_to(UP * 1.5)
        
        # 轴标签
        x_label = Text("数据序号", font=self.FONT_CHINESE, font_size=20, color=GRAY_A)
        x_label.next_to(self.axes.x_axis, DOWN, buff=0.3)
        
        y_label = Text("数值", font=self.FONT_CHINESE, font_size=20, color=GRAY_A)
        y_label.next_to(self.axes.y_axis, LEFT, buff=0.3)
        
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 数据集A的点（稳定）
        self.dots_a = VGroup()
        for i, val in enumerate(self.data_a):
            dot = Dot(
                self.axes.c2p(i + 1, val),
                radius=0.12,
                color=self.COLOR_PRIMARY,
                fill_opacity=1
            )
            self.dots_a.add(dot)
        
        # 逐个显示
        for dot in self.dots_a:
            self.play(FadeIn(dot, scale=0.5), run_time=0.3)
        
        # 标注
        label_a = Text(
            "A组（稳定数据）",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(label_a), run_time=0.5)
        self.wait(1.0)
        
        # 保存标题和标签
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.label_a = label_a
    
    def show_mean_line(self):
        """场景3: 平均数线 (10-15秒)"""
        # 平均数虚线
        self.mean_line = DashedLine(
            self.axes.c2p(0, self.mean_val),
            self.axes.c2p(6, self.mean_val),
            color=self.COLOR_MEAN,
            stroke_width=3,
            dash_length=0.15
        )
        
        self.play(Create(self.mean_line), run_time=1.0)
        
        # 标签
        mean_label = MathTex(
            r"\bar{x} = 5",
            color=self.COLOR_MEAN,
            font_size=32
        ).next_to(self.mean_line, RIGHT, buff=0.2)
        
        self.play(FadeIn(mean_label), run_time=0.4)
        
        # 公式
        formula_mean = MathTex(
            r"\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}",
            font_size=28
        ).move_to(UP * 5)
        
        self.play(Write(formula_mean), run_time=1.0)
        
        # 强调
        explain = Text(
            "平均数是数据的中心",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.play(Indicate(self.mean_line, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(formula_mean), FadeOut(explain), run_time=0.4)
        self.mean_label = mean_label
    
    def show_deviations(self):
        """场景4: 偏差可视化 (15-25秒)"""
        # 说明文字
        explain_dev = Text(
            "偏差 = 数据值 - 平均数",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_dev), run_time=0.5)
        
        # 数据集A的偏差线（全部为0）
        dev_lines_a = VGroup()
        for i, val in enumerate(self.data_a):
            # 偏差为0，画一个小标记
            point = self.axes.c2p(i + 1, val)
            marker = Cross(scale_factor=0.1, color=self.COLOR_DEVIATION, stroke_width=2)
            marker.move_to(point)
            dev_lines_a.add(marker)
        
        self.play(FadeIn(dev_lines_a), run_time=0.5)
        
        # 强调：所有偏差为0
        highlight_a = Text(
            "A组：所有偏差 = 0",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(highlight_a), run_time=0.5)
        self.wait(1.0)
        
        # 清理并引入数据集B
        transition = Text(
            "对比 B 组数据...",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(
            FadeOut(dev_lines_a),
            FadeOut(highlight_a),
            FadeOut(explain_dev),
            FadeIn(transition),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 变换到数据集B
        self.dots_b = VGroup()
        for i, val in enumerate(self.data_b):
            dot = Dot(
                self.axes.c2p(i + 1, val),
                radius=0.12,
                color=self.COLOR_SECONDARY,
                fill_opacity=1
            )
            self.dots_b.add(dot)
        
        # 更新标签
        label_b = Text(
            "B组（波动数据）",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 2)
        
        self.play(
            *[Transform(self.dots_a[i], self.dots_b[i]) for i in range(5)],
            Transform(self.label_a, label_b),
            FadeOut(transition),
            run_time=2.0
        )
        
        # 绘制数据集B的偏差线
        self.dev_lines_b = VGroup()
        dev_labels = VGroup()
        
        for i, val in enumerate(self.data_b):
            line = Line(
                self.axes.c2p(i + 1, val),
                self.axes.c2p(i + 1, self.mean_val),
                color=self.COLOR_DEVIATION,
                stroke_width=4
            )
            self.dev_lines_b.add(line)
            
            # 偏差值标签（部分显示）
            if i in [0, 4]:  # 只显示两端
                dev_val = val - self.mean_val
                label = MathTex(
                    f"{dev_val:+.0f}",
                    font_size=20,
                    color=self.COLOR_DEVIATION
                ).next_to(line, RIGHT if i == 4 else LEFT, buff=0.1)
                dev_labels.add(label)
        
        self.play(
            LaggedStart(*[Create(line) for line in self.dev_lines_b], lag_ratio=0.2),
            run_time=1.5
        )
        self.play(FadeIn(dev_labels), run_time=0.5)
        
        # 强调波动
        comparison = Text(
            "B组波动更大！",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(comparison, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(FadeOut(comparison), FadeOut(dev_labels), run_time=0.4)
        
        # 更新保存的元素
        self.current_dots = self.dots_a  # 实际上已经变换为B了
    
    def show_variance_formula(self):
        """场景5: 方差公式 (25-40秒)"""
        # 公式
        formula_var = MathTex(
            r"s^2 = \frac{(x_1-\bar{x})^2 + (x_2-\bar{x})^2 + \cdots + (x_n-\bar{x})^2}{n}",
            font_size=26
        ).move_to(UP * 5.5)
        
        self.play(
            Transform(self.title, formula_var),
            run_time=1.5
        )
        
        # 为什么要平方？
        why_square = Text(
            "为什么要平方？",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(why_square), run_time=0.5)
        
        # 解释
        explain_square = VGroup(
            Text("1. 消除正负号", font=self.FONT_CHINESE, font_size=22, color=GRAY_A),
            Text("2. 放大差异", font=self.FONT_CHINESE, font_size=22, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 3.5)
        
        self.play(FadeIn(explain_square, shift=RIGHT * 0.3), run_time=1.0)
        self.wait(1.5)
        
        self.play(FadeOut(why_square), FadeOut(explain_square), run_time=0.4)
        
        # 计算过程（数据集B）
        calc_title = Text(
            "计算 B 组方差:",
            font=self.FONT_CHINESE,
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(calc_title), run_time=0.4)
        
        # 分步计算
        steps = VGroup()
        deviations_b = self.data_b - self.mean_val
        
        for i, (val, dev) in enumerate(zip(self.data_b, deviations_b)):
            step = MathTex(
                f"({val:.0f} - 5)^2 = {dev**2:.0f}",
                font_size=22,
                color=GRAY_A
            )
            steps.add(step)
        
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(calc_title, DOWN, buff=0.3)
        
        # 逐步显示
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.5)
        
        # 求和
        sum_step = MathTex(
            r"\text{Sum} = 16 + 4 + 0 + 4 + 16 = 40",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(steps, DOWN, buff=0.3)
        
        self.play(Write(sum_step), run_time=1.0)
        
        # 除以n
        final_step = MathTex(
            r"s^2 = \frac{40}{5} = 8",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(sum_step, DOWN, buff=0.3)
        
        self.play(Write(final_step), run_time=1.0)
        self.play(Indicate(final_step, color=GOLD), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(calc_title),
            FadeOut(steps),
            FadeOut(sum_step),
            FadeOut(final_step),
            run_time=0.5
        )
        
        # 保存结果
        self.variance_result = final_step.copy()
    
    def show_standard_deviation(self):
        """场景6: 标准差 (40-50秒)"""
        # 标准差公式
        formula_std = MathTex(
            r"s = \sqrt{s^2}",
            font_size=32
        ).move_to(UP * 5)
        
        self.play(Transform(self.title, formula_std), run_time=1.0)
        
        # 计算
        calc_std = MathTex(
            r"s = \sqrt{8} \approx 2.83",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        self.play(Write(calc_std), run_time=1.0)
        
        # 说明
        explain_std = Text(
            "标准差恢复到原数据单位",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3)
        
        self.play(FadeIn(explain_std), run_time=0.5)
        
        # 在图上标注 ±s 范围
        std_val = self.std_b
        lower_line = DashedLine(
            self.axes.c2p(0, self.mean_val - std_val),
            self.axes.c2p(6, self.mean_val - std_val),
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            dash_length=0.1
        )
        
        upper_line = DashedLine(
            self.axes.c2p(0, self.mean_val + std_val),
            self.axes.c2p(6, self.mean_val + std_val),
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            dash_length=0.1
        )
        
        # 范围标注
        range_label = MathTex(
            r"\bar{x} \pm s",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).next_to(upper_line, RIGHT, buff=0.2)
        
        self.play(
            Create(lower_line),
            Create(upper_line),
            FadeIn(range_label),
            run_time=1.5
        )
        
        # 说明范围
        range_text = Text(
            f"数据大多在 [{self.mean_val-std_val:.1f}, {self.mean_val+std_val:.1f}] 范围",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(range_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(calc_std),
            FadeOut(explain_std),
            FadeOut(lower_line),
            FadeOut(upper_line),
            FadeOut(range_label),
            FadeOut(range_text),
            run_time=0.5
        )
    
    def show_summary_and_outro(self):
        """场景7: 总结对比 + 片尾 (50-70秒)"""
        # 清空画面
        self.play(
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.current_dots),
            FadeOut(self.mean_line),
            FadeOut(self.mean_label),
            FadeOut(self.dev_lines_b),
            FadeOut(self.label_a),
            FadeOut(self.title),
            run_time=0.5
        )
        
        # 对比表
        comparison_title = Text(
            "两组数据对比",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(comparison_title), run_time=0.5)
        
        # 表格
        table_data = [
            ["", "A组", "B组"],
            ["平均数", "5", "5"],
            ["方差", "0", "8"],
            ["标准差", "0", "2.83"]
        ]
        
        table = VGroup()
        for i, row in enumerate(table_data):
            row_group = VGroup()
            for j, cell in enumerate(row):
                if i == 0:  # 表头
                    color = GRAY_A
                    size = 26
                elif j == 0:  # 第一列
                    color = WHITE
                    size = 24
                elif j == 1:  # A组
                    color = self.COLOR_PRIMARY
                    size = 26
                else:  # B组
                    color = self.COLOR_SECONDARY
                    size = 26
                
                cell_text = Text(cell, font=self.FONT_CHINESE, font_size=size, color=color)
                row_group.add(cell_text)
            
            row_group.arrange(RIGHT, buff=0.8)
            table.add(row_group)
        
        table.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 2.5)
        
        self.play(FadeIn(table, shift=DOWN * 0.5), run_time=1.5)
        
        # 核心要点
        key_points = VGroup(
            Text("● 方差越大 → 波动越大", font=self.FONT_CHINESE, font_size=26, color=GRAY_A),
            Text("● 方差越小 → 数据越稳定", font=self.FONT_CHINESE, font_size=26, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(FadeIn(key_points, shift=UP * 0.3), run_time=2.0)
        self.wait(2.0)
        
        # 简化公式（彩蛋）
        bonus = Text(
            "计算技巧：",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        simplified = MathTex(
            r"s^2 = \frac{x_1^2 + x_2^2 + \cdots + x_n^2}{n} - \bar{x}^2",
            font_size=24
        ).next_to(bonus, DOWN, buff=0.3)
        
        self.play(FadeIn(bonus), Write(simplified), run_time=2.0)
        self.wait(2.0)
        
        # 清空准备片尾
        self.play(
            FadeOut(comparison_title),
            FadeOut(table),
            FadeOut(key_points),
            FadeOut(bonus),
            FadeOut(simplified),
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
        
        # 装饰元素
        icons = VGroup()
        for i in range(8):
            angle = i * PI / 4
            pos = follow.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            icon = Square(side_length=0.25, color=GOLD, fill_opacity=0.7)
            icon.rotate(PI / 4)
            icon.move_to(pos)
            icons.add(icon)
        
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
# manim -pql variance_std_dev.py VarianceAndStdDev    # 快速预览（低质量）
# manim -qm variance_std_dev.py VarianceAndStdDev     # 中等质量
# manim -qh variance_std_dev.py VarianceAndStdDev     # 高质量 1080p