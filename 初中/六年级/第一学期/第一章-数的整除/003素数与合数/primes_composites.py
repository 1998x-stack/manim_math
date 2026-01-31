"""
素数与合数 教学动画
Prime and Composite Numbers Teaching Animation

使用 Manim 创建的小学数学教学视频
内容: 素数与合数的定义、识别和分类
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

运行命令:
manim -pql primes_composites.py PrimesComposites  # 快速预览
manim -qh primes_composites.py PrimesComposites   # 高质量渲染
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PrimesComposites(Scene):
    """
    素数与合数教学动画场景
    
    场景顺序:
    1. 开场钩子 - 神秘数字分类
    2. 因数回顾 - 复习因数概念
    3. 素数定义 - 素数的定义和例子
    4. 合数定义 - 合数的定义和例子
    5. 特殊情况 - 1和2的特殊性
    6. 分类展示 - 1-20数字分类
    7. 总结关注 - 关键要点+关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIME = "#2ecc71"          # 绿色 - 素数
        self.COLOR_COMPOSITE = "#e74c3c"      # 红色 - 合数
        self.COLOR_SPECIAL = "#f39c12"        # 橙色 - 特殊数字（1）
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮强调
        self.COLOR_FACTOR = "#9b59b6"         # 紫色 - 因数
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要概念
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
        
        # 字体大小
        self.FONT_TITLE = 40
        self.FONT_SUBTITLE = 32
        self.FONT_BODY = 26
        self.FONT_SMALL = 22
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_factors_review()
        self.show_prime_definition()
        self.show_composite_definition()
        self.show_special_cases()
        self.show_classification()
        self.show_outro()
    
    def is_prime(self, n):
        """判断是否为素数"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_factors(self, n):
        """获取一个数的所有因数"""
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    def create_number_circle(self, number, color, radius=0.4, font_size=28):
        """创建带数字的圆圈"""
        circle = Circle(
            radius=radius,
            fill_color=color,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        text = Text(
            str(number),
            font="Noto Sans CJK SC",
            font_size=font_size,
            color=WHITE
        )
        
        return VGroup(circle, text)
    
    def create_factor_display(self, number, factors, center_pos, center_color):
        """创建中心数字和周围因数的展示"""
        # 中心大圆
        center = self.create_number_circle(
            number,
            center_color,
            radius=0.6,
            font_size=32
        ).move_to(center_pos)
        
        # 周围因数小圆
        factor_circles = VGroup()
        n = len(factors)
        for i, factor in enumerate(factors):
            angle = 2 * PI * i / n + PI / 2  # 从上方开始
            x = center_pos[0] + 1.2 * np.cos(angle)
            y = center_pos[1] + 1.2 * np.sin(angle)
            
            fc = self.create_number_circle(
                factor,
                self.COLOR_FACTOR,
                radius=0.3,
                font_size=20
            ).move_to(np.array([x, y, 0]))
            
            factor_circles.add(fc)
        
        # 连线
        lines = VGroup()
        for fc in factor_circles:
            line = Line(
                center.get_center(),
                fc.get_center(),
                color=self.COLOR_AUXILIARY,
                stroke_width=1.5
            )
            lines.add(line)
        
        return VGroup(lines, center, factor_circles)
    
    def show_opening(self):
        """场景1: 开场钩子 (5秒)"""
        # 作者信息（顶部，始终保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这些数字有什么秘密?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.3)
        
        # 第一组数字（素数）
        group1_numbers = [2, 3, 5, 7, 11]
        group1 = VGroup()
        for i, num in enumerate(group1_numbers):
            circle = self.create_number_circle(
                num,
                self.COLOR_PRIME,
                radius=0.35
            ).move_to(np.array([i * 0.9 - 1.8, 3.5, 0]))
            group1.add(circle)
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in group1],
            run_time=1.0,
            lag_ratio=0.2
        )
        
        # 第二组数字（合数）
        group2_numbers = [4, 6, 8, 9, 10]
        group2 = VGroup()
        for i, num in enumerate(group2_numbers):
            circle = self.create_number_circle(
                num,
                self.COLOR_COMPOSITE,
                radius=0.35
            ).move_to(np.array([i * 0.9 - 1.8, 2, 0]))
            group2.add(circle)
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in group2],
            run_time=1.0,
            lag_ratio=0.2
        )
        
        # 问题
        question = Text(
            "它们有什么不同?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(group1),
            FadeOut(group2),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_factors_review(self):
        """场景2: 因数回顾 (10秒)"""
        # 标题
        title = Text(
            "因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "能整除一个数的整数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)
        
        # 例子标题
        example_title = Text(
            "例如：6 的因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(example_title), run_time=0.6)
        self.wait(0.4)
        
        # 创建6和它的因数展示
        factors_6 = self.get_factors(6)
        display = self.create_factor_display(
            6,
            factors_6,
            np.array([0, 0.5, 0]),
            self.COLOR_PRIMARY
        )
        
        # 先显示中心数字
        self.play(FadeIn(display[1], scale=0.8), run_time=0.6)
        
        # 显示连线和因数
        self.play(Create(display[0]), run_time=0.8)
        self.play(
            *[FadeIn(fc, scale=0.5) for fc in display[2]],
            run_time=1.2,
            lag_ratio=0.3
        )
        
        # 总结
        summary = Text(
            "6 有 4 个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.6)
        
        # 高亮因数
        self.play(
            *[Flash(fc, color=YELLOW, flash_radius=0.2) for fc in display[2]],
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example_title),
            FadeOut(display),
            FadeOut(summary),
            run_time=0.6
        )
    
    def show_prime_definition(self):
        """场景3: 素数定义 (12秒)"""
        # 标题
        title = Text(
            "素数（质数）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIME
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义1
        definition_1 = Text(
            "只有 1 和本身两个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(definition_1, shift=UP * 0.3), run_time=1.0)
        
        # 定义2
        definition_2 = Text(
            "大于 1 的正整数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 3.3)
        
        self.play(FadeIn(definition_2), run_time=0.7)
        self.wait(0.5)
        
        # 例子标题
        example_title = Text(
            "例如：7 是素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(FadeIn(example_title), run_time=0.6)
        self.wait(0.4)
        
        # 创建7和它的因数展示
        factors_7 = self.get_factors(7)
        display = self.create_factor_display(
            7,
            factors_7,
            np.array([0, 0.5, 0]),
            self.COLOR_PRIME
        )
        
        # 显示
        self.play(FadeIn(display[1], scale=0.8), run_time=0.6)
        self.play(Create(display[0]), run_time=0.6)
        self.play(
            *[FadeIn(fc, scale=0.5) for fc in display[2]],
            run_time=0.8,
            lag_ratio=0.5
        )
        
        # 计数
        count = Text(
            "只有 2 个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(count, shift=UP * 0.3), run_time=0.6)
        
        # 判定
        checkmark = Text(
            "✓",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIME
        )
        
        judgment_text = Text(
            "7 是素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIME
        )
        
        judgment = VGroup(judgment_text, checkmark).arrange(
            RIGHT, buff=0.3
        ).move_to(DOWN * 2.5)
        
        self.play(
            FadeIn(judgment, shift=UP * 0.3, scale=1.1),
            Flash(display[1], color=GREEN, flash_radius=0.4),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 更多例子
        more = Text(
            "更多素数: 2, 3, 5, 7, 11, 13, 17, 19...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(more), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_1),
            FadeOut(definition_2),
            FadeOut(example_title),
            FadeOut(display),
            FadeOut(count),
            FadeOut(judgment),
            FadeOut(more),
            run_time=0.6
        )
    
    def show_composite_definition(self):
        """场景4: 合数定义 (12秒)"""
        # 标题
        title = Text(
            "合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_COMPOSITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "除了 1 和本身还有其他因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)
        
        # 例子标题
        example_title = Text(
            "例如：6 是合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(FadeIn(example_title), run_time=0.6)
        self.wait(0.4)
        
        # 创建6和它的因数展示
        factors_6 = self.get_factors(6)
        display = self.create_factor_display(
            6,
            factors_6,
            np.array([0, 0.5, 0]),
            self.COLOR_COMPOSITE
        )
        
        # 显示
        self.play(FadeIn(display[1], scale=0.8), run_time=0.6)
        self.play(Create(display[0]), run_time=0.6)
        
        # 逐个显示因数，高亮2和3（其他因数）
        for i, fc in enumerate(display[2]):
            if i == 1 or i == 2:  # 2和3的位置
                self.play(
                    FadeIn(fc, scale=0.5),
                    fc.animate.set_color(self.COLOR_HIGHLIGHT),
                    run_time=0.5
                )
            else:
                self.play(FadeIn(fc, scale=0.5), run_time=0.4)
        
        # 计数
        count = Text(
            "有 4 个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(count, shift=UP * 0.3), run_time=0.6)
        
        # 说明
        note = Text(
            "除了1和6，还有2和3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(note), run_time=0.6)
        
        # 判定
        checkmark = Text(
            "✓",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_COMPOSITE
        )
        
        judgment_text = Text(
            "6 是合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_COMPOSITE
        )
        
        judgment = VGroup(judgment_text, checkmark).arrange(
            RIGHT, buff=0.3
        ).move_to(DOWN * 3.5)
        
        self.play(
            FadeIn(judgment, shift=UP * 0.3),
            Flash(display[1], color=RED, flash_radius=0.4),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 更多例子
        more = Text(
            "更多合数: 4, 6, 8, 9, 10, 12, 14, 15...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(more), run_time=0.6)
        self.wait(0.7)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example_title),
            FadeOut(display),
            FadeOut(count),
            FadeOut(note),
            FadeOut(judgment),
            FadeOut(more),
            run_time=0.6
        )
    
    def show_special_cases(self):
        """场景5: 特殊情况 (14秒)"""
        # 标题
        title = Text(
            "特殊情况",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # === 左边：数字1 ===
        # 1的展示
        factors_1 = self.get_factors(1)
        display_1 = self.create_factor_display(
            1,
            factors_1,
            LEFT * 2 + UP * 2.5,
            self.COLOR_SPECIAL
        )
        
        self.play(FadeIn(display_1[1], scale=0.8), run_time=0.6)
        self.wait(0.4)
        self.play(Create(display_1[0]), run_time=0.4)
        self.play(FadeIn(display_1[2], scale=0.5), run_time=0.6)
        
        # 说明1
        note_1 = Text(
            "只有 1 个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=WHITE
        ).move_to(LEFT * 2 + UP * 0.8)
        
        self.play(FadeIn(note_1, shift=UP * 0.2), run_time=0.6)
        
        # 结论1
        conclusion_1_line1 = Text(
            "1 既不是素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SPECIAL
        ).move_to(LEFT * 2 + UP * 0.1)
        
        conclusion_1_line2 = Text(
            "也不是合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SPECIAL
        ).move_to(LEFT * 2 + DOWN * 0.5)
        
        self.play(FadeIn(conclusion_1_line1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(conclusion_1_line2, shift=UP * 0.2), run_time=0.6)
        
        # 高亮1
        self.play(
            Flash(display_1[1], color=self.COLOR_SPECIAL, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(0.4)
        
        # === 右边：数字2 ===
        # 2的展示
        factors_2 = self.get_factors(2)
        display_2 = self.create_factor_display(
            2,
            factors_2,
            RIGHT * 2 + UP * 2.5,
            self.COLOR_PRIME
        )
        
        self.play(FadeIn(display_2[1], scale=0.8), run_time=0.6)
        self.wait(0.4)
        self.play(Create(display_2[0]), run_time=0.4)
        self.play(
            *[FadeIn(fc, scale=0.5) for fc in display_2[2]],
            run_time=0.8,
            lag_ratio=0.5
        )
        
        # 说明2a
        note_2a = Text(
            "最小的素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIME
        ).move_to(RIGHT * 2 + UP * 0.8)
        
        self.play(FadeIn(note_2a, shift=UP * 0.2), run_time=0.6)
        
        # 说明2b
        note_2b = Text(
            "唯一的偶素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIME
        ).move_to(RIGHT * 2 + UP * 0.1)
        
        self.play(FadeIn(note_2b, shift=UP * 0.2), run_time=0.6)
        
        # 高亮2
        self.play(
            Flash(display_2[1], color=GREEN, flash_radius=0.4),
            run_time=0.6
        )
        
        # 强调说明
        star = Text(
            "★",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).next_to(note_2b, LEFT, buff=0.2)
        
        self.play(FadeIn(star, scale=1.5), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(display_1),
            FadeOut(note_1),
            FadeOut(conclusion_1_line1),
            FadeOut(conclusion_1_line2),
            FadeOut(display_2),
            FadeOut(note_2a),
            FadeOut(note_2b),
            FadeOut(star),
            run_time=0.6
        )
    
    def show_classification(self):
        """场景6: 分类展示 (18秒)"""
        # 标题
        title = Text(
            "1-20 的分类",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建1-20的网格
        numbers = list(range(1, 21))
        rows = 4
        cols = 5
        cell_width = 0.8
        cell_height = 0.7
        start_x = -1.6
        start_y = 3.5
        
        number_circles = VGroup()
        for i, num in enumerate(numbers):
            row = i // cols
            col = i % cols
            x = start_x + col * cell_width
            y = start_y - row * cell_height
            
            # 初始都用灰色
            circle = self.create_number_circle(
                num,
                GRAY,
                radius=0.3,
                font_size=22
            ).move_to(np.array([x, y, 0]))
            
            number_circles.add(circle)
        
        # 逐个出现
        self.play(
            *[FadeIn(c, scale=0.5) for c in number_circles],
            run_time=3.0,
            lag_ratio=0.08
        )
        self.wait(0.5)
        
        # 提示
        prompt = Text(
            "让我们分类吧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(prompt, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(prompt), run_time=0.3)
        
        # 分类：1变橙色
        self.play(
            number_circles[0].animate.set_color(self.COLOR_SPECIAL),
            run_time=0.5
        )
        
        # 素数变绿色
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        prime_indices = [num - 1 for num in primes]
        
        self.play(
            *[number_circles[i].animate.set_color(self.COLOR_PRIME) 
              for i in prime_indices],
            run_time=2.0
        )
        
        # 合数变红色
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        composite_indices = [num - 1 for num in composites]
        
        self.play(
            *[number_circles[i].animate.set_color(self.COLOR_COMPOSITE) 
              for i in composite_indices],
            run_time=2.0
        )
        
        # 统计
        count_primes = Text(
            f"素数: {len(primes)} 个",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIME
        ).move_to(DOWN * 2.5 + LEFT * 1.5)
        
        count_composites = Text(
            f"合数: {len(composites)} 个",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_COMPOSITE
        ).move_to(DOWN * 2.5 + RIGHT * 1.5)
        
        count_special = Text(
            "特殊: 1 个",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SPECIAL
        ).move_to(DOWN * 3.5)
        
        self.play(
            FadeIn(count_primes, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.2)
        self.play(
            FadeIn(count_composites, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.2)
        self.play(
            FadeIn(count_special, shift=UP * 0.2),
            run_time=0.6
        )
        
        # 整体闪烁
        self.play(
            *[Flash(number_circles[i], color=GREEN, flash_radius=0.15) 
              for i in prime_indices],
            run_time=0.8
        )
        self.play(
            *[Flash(number_circles[i], color=RED, flash_radius=0.15) 
              for i in composite_indices],
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(number_circles),
            FadeOut(count_primes),
            FadeOut(count_composites),
            FadeOut(count_special),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 总结关注 (14秒)"""
        # 总结标题
        summary_title = Text(
            "记住这些!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点1
        point_1 = Text(
            "素数 = 只有 2 个因数 (1和本身)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIME
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(point_1, shift=UP * 0.3), run_time=0.6)
        self.wait(0.2)
        
        # 要点2
        point_2 = Text(
            "合数 = 有 3 个或更多因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_COMPOSITE
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(point_2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.2)
        
        # 要点3
        point_3 = Text(
            "1 既不是素数也不是合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SPECIAL
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(point_3, shift=UP * 0.3), run_time=0.6)
        self.wait(0.2)
        
        # 要点4
        point_4 = Text(
            "2 是最小且唯一的偶素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIME
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(point_4, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 要点闪烁
        self.play(
            Flash(point_1, color=GREEN, flash_radius=0.4),
            run_time=0.4
        )
        self.play(
            Flash(point_2, color=RED, flash_radius=0.4),
            run_time=0.4
        )
        self.play(
            Flash(point_3, color=self.COLOR_SPECIAL, flash_radius=0.4),
            run_time=0.4
        )
        self.play(
            Flash(point_4, color=GREEN, flash_radius=0.4),
            run_time=0.4
        )
        
        # 清理要点
        self.play(
            FadeOut(summary_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            FadeOut(point_4),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Transform(self.author_info, author_large), run_time=0.8)
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰：素数圆圈
        primes_deco = [2, 3, 5, 7, 11]
        decorations = VGroup()
        for i, prime in enumerate(primes_deco):
            circle = self.create_number_circle(
                prime,
                self.COLOR_PRIME,
                radius=0.25,
                font_size=18
            ).move_to(np.array([i * 0.9 - 1.8, -2.5, 0]))
            decorations.add(circle)
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        
        self.play(
            Rotate(decorations, angle=PI, run_time=1.5)
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 测试场景
class TestPrimesComposites(Scene):
    """测试单个场景"""
    
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        # 这里可以复制粘贴单个场景的代码进行测试
        pass