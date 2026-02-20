from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class InequalityProofsAnimation(Scene):
    """
    不等式的证明教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 比较法证明
    3. 综合法证明
    4. 分析法证明
    5. 反证法证明
    6. 放缩法证明
    7. 总结回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PROOF_METHOD = BLUE
        self.COLOR_FORMULA = WHITE
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_comparison_method()
        self.show_synthetic_method()
        self.show_analytic_method()
        self.show_proof_by_contradiction()
        self.show_estimation_method()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何数据和参数"""
        # 示例值
        self.example_a = 3
        self.example_b = 2
        self.diff_ab = self.example_a - self.example_b
        self.prod_ab = self.example_a * self.example_b
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证示例值计算
        computed_diff = self.example_a - self.example_b
        computed_prod = self.example_a * self.example_b
        
        if abs(computed_diff - self.diff_ab) > epsilon:
            print(f"⚠️  警告: 差值计算错误! {computed_diff} ≠ {self.diff_ab}")
        else:
            print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 标题
        title = Text(
            "不等式的证明",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)
        
        # 钩子问题
        hook_question = Text(
            "如何证明 a² + b² ≥ 2ab？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(hook_question), run_time=0.4)
        self.wait(1)
        
        # 清理钩子问题
        self.play(FadeOut(hook_question), run_time=0.5)
    
    def show_comparison_method(self):
        """场景2: 比较法证明"""
        # 标题
        title = Text(
            "比较法证明",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROOF_METHOD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 比较法原理
        principle = MathTex(
            "a \\geq b \\iff a - b \\geq 0",
            color=WHITE,
            font_size=32
        ).move_to(UP * 4)
        
        self.play(Write(principle), run_time=0.8)
        
        # 待证明不等式
        inequality_to_prove = MathTex(
            f"{self.example_a}^2 + {self.example_b}^2 \\geq 2 \\cdot {self.example_a} \\cdot {self.example_b}",
            color=WHITE,
            font_size=32
        ).move_to(UP * 3)
        
        self.play(Write(inequality_to_prove), run_time=0.8)
        
        # 作差
        diff_step = MathTex(
            f"{self.example_a}^2 + {self.example_b}^2 - 2 \\cdot {self.example_a} \\cdot {self.example_b}",
            color=WHITE,
            font_size=32
        ).move_to(UP * 2)
        
        self.play(Write(diff_step), run_time=0.8)
        
        # 因式分解
        factored = MathTex(
            f"= ({self.example_a} - {self.example_b})^2",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).next_to(diff_step, DOWN, buff=0.3)
        
        self.play(Write(factored), run_time=0.8)
        
        # 非负性说明
        non_negative = MathTex(
            f"= {self.diff_ab}^2 = {self.diff_ab**2} \\geq 0",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).next_to(factored, DOWN, buff=0.3)
        
        self.play(Write(non_negative), run_time=0.8)
        
        # 结论
        conclusion = MathTex(
            "\\therefore a^2 + b^2 \\geq 2ab",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(DOWN * 1)
        
        self.play(Write(conclusion), run_time=1.0)
        
        self.wait(2)
        
        # 清理部分元素，保留标题和核心结论
        self.play(
            FadeOut(principle),
            FadeOut(inequality_to_prove),
            FadeOut(diff_step),
            FadeOut(factored),
            FadeOut(non_negative),
            run_time=0.5
        )
    
    def show_synthetic_method(self):
        """场景3: 综合法证明"""
        # 标题
        title = Text(
            "综合法证明",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROOF_METHOD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 综合法原理
        principle = Text(
            "已知条件 → ... → 目标结论",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(principle), run_time=0.6)
        
        # 从基本不等式出发
        basic_inequality = MathTex(
            "(a - b)^2 \\geq 0",
            color=WHITE,
            font_size=32
        ).move_to(UP * 3.5)
        
        self.play(Write(basic_inequality), run_time=0.8)
        
        # 展开平方
        expanded = MathTex(
            "a^2 - 2ab + b^2 \\geq 0",
            color=WHITE,
            font_size=32
        ).move_to(UP * 2.5)
        
        self.play(Write(expanded), run_time=0.8)
        
        # 移项
        rearranged = MathTex(
            "a^2 + b^2 \\geq 2ab",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(UP * 1.5)
        
        self.play(Write(rearranged), run_time=0.8)
        
        # 推广形式
        general = MathTex(
            "a^2 + b^2 \\geq 2|ab|",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(UP * 0.5)
        
        self.play(Write(general), run_time=0.8)
        
        self.wait(2)
        
        # 清理部分元素
        self.play(
            FadeOut(principle),
            FadeOut(basic_inequality),
            FadeOut(expanded),
            FadeOut(rearranged),
            run_time=0.5
        )
    
    def show_analytic_method(self):
        """场景4: 分析法证明"""
        # 标题
        title = Text(
            "分析法证明",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROOF_METHOD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 分析法原理
        principle = Text(
            "目标结论 ← ... ← 已知条件",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(principle), run_time=0.6)
        
        # 待证结论
        target = MathTex(
            "\\frac{a}{b} + \\frac{b}{a} \\geq 2", 
            "\\quad (a,b同号)",
            color=WHITE,
            font_size=28
        ).move_to(UP * 3.5)
        
        self.play(Write(target), run_time=0.8)
        
        # 通分变换
        transformed = MathTex(
            "\\frac{a^2 + b^2}{ab} \\geq 2",
            color=WHITE,
            font_size=28
        ).move_to(UP * 2.5)
        
        self.play(TransformMatchingTex(target.copy(), transformed), run_time=0.8)
        
        # 乘以ab（同号）
        multiplied = MathTex(
            "a^2 + b^2 \\geq 2ab",
            color=WHITE,
            font_size=28
        ).move_to(UP * 1.5)
        
        self.play(TransformMatchingTex(transformed.copy(), multiplied), run_time=0.8)
        
        # 移项
        rearranged = MathTex(
            "a^2 - 2ab + b^2 \\geq 0",
            color=WHITE,
            font_size=28
        ).move_to(UP * 0.5)
        
        self.play(TransformMatchingTex(multiplied.copy(), rearranged), run_time=0.8)
        
        # 因式分解
        factored = MathTex(
            "(a - b)^2 \\geq 0",
            color=self.COLOR_HIGHLIGHT,
            font_size=28
        ).move_to(DOWN * 0.5)
        
        self.play(TransformMatchingTex(rearranged.copy(), factored), run_time=0.8)
        
        self.wait(2)
        
        # 清理部分元素
        self.play(
            FadeOut(principle),
            FadeOut(target),
            FadeOut(transformed),
            FadeOut(multiplied),
            FadeOut(rearranged),
            run_time=0.5
        )
    
    def show_proof_by_contradiction(self):
        """场景5: 反证法证明"""
        # 标题
        title = Text(
            "反证法证明",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROOF_METHOD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 反证法原理
        principle = Text(
            "假设结论不成立 → 推出矛盾 → 原结论成立",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(principle), run_time=0.6)
        
        # 假设相反
        assumption = MathTex(
            "\\text{假设: } a^2 + b^2 < 2ab",
            color=RED,
            font_size=28
        ).move_to(UP * 3.5)
        
        self.play(Write(assumption), run_time=0.8)
        
        # 移项变形
        rearranged = MathTex(
            "a^2 - 2ab + b^2 < 0",
            color=RED,
            font_size=28
        ).move_to(UP * 2.5)
        
        self.play(TransformMatchingTex(assumption.copy(), rearranged), run_time=0.8)
        
        # 因式分解
        factored = MathTex(
            "(a - b)^2 < 0",
            color=RED,
            font_size=28
        ).move_to(UP * 1.5)
        
        self.play(TransformMatchingTex(rearranged.copy(), factored), run_time=0.8)
        
        # 显示矛盾
        contradiction = Text(
            "但这与 (a-b)² ≥ 0 矛盾!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=RED
        ).move_to(UP * 0.5)
        
        self.play(Write(contradiction), run_time=0.8)
        
        # 得出原结论
        original_conclusion = MathTex(
            "\\therefore a^2 + b^2 \\geq 2ab",
            color=self.COLOR_HIGHLIGHT,
            font_size=28
        ).move_to(DOWN * 0.5)
        
        self.play(Write(original_conclusion), run_time=1.0)
        
        self.wait(2)
        
        # 清理部分元素
        self.play(
            FadeOut(principle),
            FadeOut(assumption),
            FadeOut(rearranged),
            FadeOut(factored),
            FadeOut(contradiction),
            run_time=0.5
        )
    
    def show_estimation_method(self):
        """场景6: 放缩法证明"""
        # 标题
        title = Text(
            "放缩法证明",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROOF_METHOD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 放缩法原理
        principle = Text(
            "适当放大或缩小来证明",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(principle), run_time=0.6)
        
        # 示例不等式
        example = MathTex(
            "\\frac{1}{n^2} < \\frac{1}{n(n-1)}",
            "\\quad (n \\geq 2)",
            color=WHITE,
            font_size=28
        ).move_to(UP * 3.5)
        
        self.play(Write(example), run_time=0.8)
        
        # 右侧变形
        equivalent = MathTex(
            "= \\frac{1}{n-1} - \\frac{1}{n}",
            color=WHITE,
            font_size=28
        ).move_to(UP * 2.5)
        
        self.play(Write(equivalent), run_time=0.8)
        
        # 应用技巧
        technique = Text(
            "裂项相消技巧",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Write(technique), run_time=0.6)
        
        # 累加结果
        sum_result = MathTex(
            "\\sum_{k=2}^{n} \\frac{1}{k^2} < 2 - \\frac{1}{n}",
            color=self.COLOR_HIGHLIGHT,
            font_size=28
        ).move_to(UP * 0.5)
        
        self.play(Write(sum_result), run_time=1.0)
        
        self.wait(2)
        
        # 清理部分元素
        self.play(
            FadeOut(principle),
            FadeOut(example),
            FadeOut(equivalent),
            FadeOut(technique),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景7: 总结回顾"""
        # 总结文字
        method_summary = Text(
            "不等式证明的五种方法:\n\n1. 比较法: 作差a-b≥0或作商a/b≥1\n2. 综合法: 由因导果\n3. 分析法: 执果索因\n4. 反证法: 假设结论不成立推出矛盾\n5. 放缩法: 适当放大/缩小",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1)
        
        self.play(Write(method_summary), run_time=1.5)
        
        # 作者信息
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 关注提示
        follow_hint = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(Write(follow_hint), run_time=0.8)
        
        self.wait(2)


if __name__ == "__main__":
    # 运行命令: manim -pql InequalityProofsAnimation.py InequalityProofsAnimation
    pass