"""
用样本估计总体教学动画 - Sample Estimation
使用 Manim 创建的中学统计学教学视频

内容: 用样本统计量估计总体参数
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
import random


# ========== 全局配置 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SampleEstimation(Scene):
    """
    用样本估计总体教学动画
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 总体与样本概念 - 基本概念
    3. 抽样过程 - 动画展示
    4. 样本平均数估计 - 核心方法
    5. 样本容量的影响 - 准确性分析
    6. 代表性的重要性 - 避免偏差
    7. 总结和片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_POPULATION = "#3498db"    # 蓝色 - 总体
        self.COLOR_SAMPLE = "#e74c3c"        # 红色 - 样本
        self.COLOR_ESTIMATE = "#2ecc71"      # 绿色 - 估计值
        self.COLOR_TRUE_VALUE = "#9b59b6"    # 紫色 - 真实值
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 设置随机种子（保证可重复性）
        random.seed(42)
        np.random.seed(42)
        
        # 总体数据（100个数据点）
        self.population_size = 100
        self.population_mean = 75  # 总体平均数（真实值）
        self.population_std = 10
        
        # 生成总体数据
        self.population_data = np.random.normal(
            self.population_mean, 
            self.population_std, 
            self.population_size
        )
        self.population_data = np.clip(self.population_data, 50, 100)
        
        # 实际总体平均数
        self.actual_population_mean = np.mean(self.population_data)
        
        # 执行动画序列
        self.show_opening()
        self.show_population_concept()
        self.show_sampling_process()
        self.show_sample_mean_estimation()
        self.show_sample_size_effect()
        self.show_representativeness()
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
            "1000万人口城市",
            font=self.FONT_CHINESE,
            font_size=42,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 问题情境
        scenario = Text(
            "如何调查平均收入?",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(FadeIn(scenario, shift=UP * 0.3), run_time=0.8)
        
        # 问题
        question = VGroup(
            Text("全部调查？", font=self.FONT_CHINESE, font_size=30, color=GRAY_A),
            Text("→ 时间长、成本高", font=self.FONT_CHINESE, font_size=26, color=GRAY_B)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.5)
        
        self.play(FadeIn(question), run_time=0.8)
        
        # 解决方案
        solution = Text(
            "用样本估计总体！",
            font=self.FONT_CHINESE,
            font_size=38,
            color=self.COLOR_ESTIMATE,
            weight=BOLD
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(solution, shift=UP * 0.5, scale=1.2), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(scenario),
            FadeOut(question),
            FadeOut(solution),
            run_time=0.5
        )
    
    def show_population_concept(self):
        """场景2: 总体与样本概念 (5-12秒)"""
        # 标题
        title = Text(
            "总体 vs 样本",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建总体点阵（10×10网格，共100个点）
        self.population_dots = VGroup()
        for i in range(10):
            for j in range(10):
                dot = Dot(
                    radius=0.08,
                    color=self.COLOR_POPULATION,
                    fill_opacity=0.8
                )
                # 定位到网格位置
                x = (j - 4.5) * 0.5
                y = (i - 4.5) * 0.5 + 2
                dot.move_to([x, y, 0])
                self.population_dots.add(dot)
        
        # 逐渐显示总体点
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in self.population_dots], 
                       lag_ratio=0.02),
            run_time=2.0
        )
        
        # 总体标签
        population_label = Text(
            "总体：所有研究对象",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_POPULATION
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(population_label), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "100个数据点代表总体",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理说明，保留标题和总体
        self.play(FadeOut(explanation), FadeOut(population_label), run_time=0.3)
        
        # 保存标题
        self.current_title = title
    
    def show_sampling_process(self):
        """场景3: 抽样过程 (12-20秒)"""
        # 新标题
        new_title = Text(
            "抽样过程",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 说明文字
        sampling_text = Text(
            "从总体中随机抽取样本",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(sampling_text), run_time=0.5)
        
        # 样本区域标签
        sample_area_label = Text(
            "样本",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_SAMPLE
        ).move_to(DOWN * 1.2)
        
        self.play(FadeIn(sample_area_label), run_time=0.4)
        
        # 样本区域框
        sample_box = Rectangle(
            width=4.5,
            height=1.8,
            stroke_color=self.COLOR_SAMPLE,
            stroke_width=2,
            fill_opacity=0
        ).move_to(DOWN * 2.5)
        
        self.play(Create(sample_box), run_time=0.5)
        
        # 随机抽取10个点
        sample_size = 10
        sample_indices = random.sample(range(self.population_size), sample_size)
        
        self.sample_dots = VGroup()
        
        # 抽样动画
        for idx_count, idx in enumerate(sample_indices):
            dot = self.population_dots[idx]
            
            # 创建样本点位置
            row = idx_count // 5
            col = idx_count % 5
            sample_x = (col - 2) * 0.8
            sample_y = -2.5 + (0.5 - row * 0.6)
            sample_pos = np.array([sample_x, sample_y, 0])
            
            # 创建箭头
            arrow = Arrow(
                dot.get_center(),
                sample_pos,
                color=self.COLOR_SAMPLE,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15
            )
            
            # 动画：高亮→箭头→移动→变色
            self.play(
                Indicate(dot, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
                run_time=0.2
            )
            
            self.play(Create(arrow), run_time=0.3)
            
            # 创建样本点的副本
            sample_dot = dot.copy()
            
            self.play(
                sample_dot.animate.move_to(sample_pos).set_color(self.COLOR_SAMPLE).scale(1.2),
                FadeOut(arrow),
                run_time=0.4
            )
            
            self.sample_dots.add(sample_dot)
        
        # 说明样本
        sample_label = Text(
            f"n = {sample_size}（样本容量）",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_SAMPLE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(sample_label), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(sampling_text),
            FadeOut(sample_area_label),
            FadeOut(sample_box),
            FadeOut(sample_label),
            run_time=0.4
        )
        
        # 保存样本索引
        self.current_sample_indices = sample_indices
    
    def show_sample_mean_estimation(self):
        """场景4: 样本平均数估计 (20-32秒)"""
        # 新标题
        new_title = Text(
            "用样本平均数估计总体",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 计算样本平均数
        sample_data = self.population_data[self.current_sample_indices]
        sample_mean = np.mean(sample_data)
        
        # 样本平均数计算
        calc_title = Text(
            "计算样本平均数：",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(calc_title), run_time=0.5)
        
        formula_group = VGroup()
        
        left_side = MathTex(r"\bar{x}_{sample}", font_size=32)
        
        equals_sign = MathTex("=", font_size=32).next_to(left_side, RIGHT, buff=0.3)
        
        right_side = MathTex(r"\frac{\sum x_i}{n}", font_size=32).next_to(equals_sign, RIGHT, buff=0.3)
        
        formula = VGroup(left_side, equals_sign, right_side).move_to(UP * 3.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 结果
        sample_result = MathTex(
            f"\\bar{{x}}_{{sample}} = {sample_mean:.1f}",
            font_size=32,
            color=self.COLOR_SAMPLE
        ).move_to(UP * 2.5)
        
        self.play(Write(sample_result), run_time=0.8)
        
        # 估计关系
        estimate_text = Text(
            "used to estimate",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        estimate_arrow = Arrow(
            UP * 2.2,
            UP * 0.8,
            color=self.COLOR_ESTIMATE,
            stroke_width=4
        )
        
        self.play(
            FadeIn(estimate_text),
            Create(estimate_arrow),
            run_time=0.8
        )
        
        # 总体平均数
        population_result = VGroup(
            MathTex(
                f"\\mu_{{population}} \\approx {sample_mean:.1f}",
                font_size=32,
                color=self.COLOR_TRUE_VALUE
            ),
            Text(
                f"(True value: {self.actual_population_mean:.1f})",
                font=self.FONT_CHINESE,
                font_size=20,
                color=GRAY_A
            )
        ).arrange(DOWN, buff=0.3).move_to(UP * 0)
        
        self.play(Write(population_result), run_time=1.2)
        
        # 对比
        error = abs(sample_mean - self.actual_population_mean)
        comparison = Text(
            f"Estimation error: {error:.1f}",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT if error < 3 else self.COLOR_AUXILIARY
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(comparison), run_time=0.5)
        
        # 强调接近
        if error < 3:
            emphasis = Text(
                "Accurate estimation!",
                font=self.FONT_CHINESE,
                font_size=26,
                color=self.COLOR_ESTIMATE,
                weight=BOLD
            ).move_to(DOWN * 2.5)
            
            self.play(FadeIn(emphasis, shift=UP * 0.3), run_time=0.6)
            self.wait(1.2)
            self.play(FadeOut(emphasis), run_time=0.3)
        else:
            self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(calc_title),
            FadeOut(formula),
            FadeOut(sample_result),
            FadeOut(estimate_text),
            FadeOut(estimate_arrow),
            FadeOut(population_result),
            FadeOut(comparison),
            run_time=0.5
        )
    
    def show_sample_size_effect(self):
        """场景5: 样本容量的影响 (32-45秒)"""
        # 新标题
        new_title = Text(
            "样本容量的影响",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 清空旧样本
        self.play(FadeOut(self.sample_dots), run_time=0.4)
        
        # 三种样本容量
        sample_sizes = [5, 10, 30]
        estimates = []
        
        # 说明文字
        explanation = Text(
            "对比不同样本容量的估计效果",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 创建对比表格
        table_title = Text(
            "样本容量    估计值    误差",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(table_title), run_time=0.5)
        
        table_rows = VGroup()
        
        for i, size in enumerate(sample_sizes):
            # 随机抽样
            indices = random.sample(range(self.population_size), size)
            sample_data = self.population_data[indices]
            sample_mean = np.mean(sample_data)
            error = abs(sample_mean - self.actual_population_mean)
            estimates.append((size, sample_mean, error))
            
            # 创建行
            row = Text(
                f"n = {size:2d}        {sample_mean:5.1f}      {error:4.1f}",
                font=self.FONT_CHINESE,
                font_size=24,
                color=self.COLOR_SAMPLE if i < 2 else self.COLOR_ESTIMATE
            ).move_to(UP * (2.5 - i * 0.8))
            
            table_rows.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.6)
        
        # 结论
        conclusion = VGroup(
            Text("样本容量越大", font=self.FONT_CHINESE, font_size=28, color=WHITE),
            Text("→", font=self.FONT_CHINESE, font_size=28, color=self.COLOR_HIGHLIGHT),
            Text("估计越准确", font=self.FONT_CHINESE, font_size=28, color=self.COLOR_ESTIMATE, weight=BOLD)
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=1.0)
        
        # 视觉强调：n=30的行
        self.play(
            table_rows[2].animate.scale(1.1).set_color(self.COLOR_ESTIMATE),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(table_title),
            FadeOut(table_rows),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_representativeness(self):
        """场景6: 代表性的重要性 (45-55秒)"""
        # 新标题
        new_title = Text(
            "样本的代表性很重要",
            font=self.FONT_CHINESE,
            font_size=30,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Transform(self.current_title, new_title), run_time=0.5)
        
        # 有偏样本示例（只从左上角抽取）
        biased_label = Text(
            "❌ 有偏样本（集中某区域）",
            font=self.FONT_CHINESE,
            font_size=24,
            color=RED
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(biased_label), run_time=0.5)
        
        # 高亮左上角区域
        biased_indices = list(range(0, 10))  # 前10个
        biased_box = SurroundingRectangle(
            VGroup(*[self.population_dots[i] for i in biased_indices]),
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(Create(biased_box), run_time=0.8)
        
        # 有偏样本的估计
        biased_data = self.population_data[biased_indices]
        biased_mean = np.mean(biased_data)
        biased_error = abs(biased_mean - self.actual_population_mean)
        
        biased_result = Text(
            f"估计值: {biased_mean:.1f}  误差: {biased_error:.1f}",
            font=self.FONT_CHINESE,
            font_size=22,
            color=RED
        ).move_to(UP * 4)
        
        self.play(FadeIn(biased_result), run_time=0.6)
        self.wait(1.0)
        
        # 代表性样本（随机分布）
        self.play(
            FadeOut(biased_box),
            FadeOut(biased_result),
            FadeOut(biased_label),
            run_time=0.4
        )
        
        representative_label = Text(
            "✓ 代表性样本（随机分布）",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_ESTIMATE
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(representative_label), run_time=0.5)
        
        # 高亮分散的点
        representative_indices = random.sample(range(self.population_size), 10)
        representative_circles = VGroup()
        
        for idx in representative_indices:
            circle = Circle(
                radius=0.15,
                color=self.COLOR_ESTIMATE,
                stroke_width=3
            ).move_to(self.population_dots[idx].get_center())
            representative_circles.add(circle)
        
        self.play(
            LaggedStart(*[Create(c) for c in representative_circles], lag_ratio=0.1),
            run_time=1.0
        )
        
        # 代表性样本的估计
        representative_data = self.population_data[representative_indices]
        representative_mean = np.mean(representative_data)
        representative_error = abs(representative_mean - self.actual_population_mean)
        
        representative_result = Text(
            f"估计值: {representative_mean:.1f}  误差: {representative_error:.1f}",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_ESTIMATE
        ).move_to(UP * 4)
        
        self.play(FadeIn(representative_result), run_time=0.6)
        
        # 关键要点
        key_point = Text(
            "随机抽样保证代表性！",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 3)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(representative_label),
            FadeOut(representative_circles),
            FadeOut(representative_result),
            FadeOut(key_point),
            run_time=0.5
        )
    
    def show_summary_and_outro(self):
        """场景7: 总结和片尾 (55-70秒)"""
        # 清空画面
        self.play(
            FadeOut(self.current_title),
            FadeOut(self.population_dots),
            run_time=0.5
        )
        
        # 总结标题
        summary_title = Text(
            "用样本估计总体 - 要点",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 三大要点
        points = VGroup(
            Text("1. 样本统计量可估计总体参数", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("2. 样本容量越大，估计越准确", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("3. 样本必须有代表性（随机抽样）", font=self.FONT_CHINESE, font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(UP * 3)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT * 0.3), run_time=0.8)
        
        # 关键公式
        formulas = VGroup(
            MathTex(r"\bar{x}_{sample} \approx \mu_{population}", font_size=28),
            MathTex(r"s^2_{sample} \approx \sigma^2_{population}", font_size=28)
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 0.5)
        
        self.play(Write(formulas), run_time=1.5)
        
        self.wait(2.0)
        
        # 清空准备片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(points),
            FadeOut(formulas),
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
            "关注我，学更多统计方法！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标（统计图标）
        icons = VGroup()
        for i in range(8):
            angle = i * PI / 4
            pos = follow.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 小点阵图标
            icon_dots = VGroup()
            for j in range(3):
                for k in range(3):
                    dot = Dot(
                        radius=0.03,
                        color=self.COLOR_POPULATION if (j+k) % 2 == 0 else self.COLOR_SAMPLE,
                        fill_opacity=0.8
                    )
                    dot.shift(RIGHT * (k-1) * 0.08 + UP * (j-1) * 0.08)
                    icon_dots.add(dot)
            
            icon_dots.move_to(pos)
            icons.add(icon_dots)
        
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
# manim -pql sample_estimation.py SampleEstimation    # 快速预览
# manim -qm sample_estimation.py SampleEstimation     # 中等质量
# manim -qh sample_estimation.py SampleEstimation     # 高质量 1080p