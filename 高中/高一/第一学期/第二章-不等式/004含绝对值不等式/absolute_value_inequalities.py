from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class AbsoluteValueInequalitiesAnimation(Scene):
    """
    含绝对值不等式教学动画场景
    
    场景顺序:
    1. 开场介绍绝对值不等式
    2. 绝对值几何意义回顾
    3. |x| < a 型不等式解法
    4. |x| > a 型不等式解法
    5. |x-a| < b 型不等式解法
    6. 三角不等式简介
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ABSOLUTE_VALUE = BLUE
        self.COLOR_NUMBER_LINE = WHITE
        self.COLOR_POINTS = YELLOW
        self.COLOR_SOLUTION_REGION = GREEN
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.review_absolute_value_meaning()
        self.show_less_than_inequality()
        self.show_greater_than_inequality()
        self.show_shifted_inequality()
        self.show_triangle_inequality()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化数轴和其他几何元素"""
        # 创建数轴 - 使用适合竖屏的布局
        self.number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=8,
            include_numbers=True,
            label_direction=UP,
            stroke_width=4
        ).shift(DOWN * 1)  # 移到下方给标题和解释留空间
        
        # 设置参数
        self.a_val = 3  # 示例参数 a > 0
        self.b_val = 2  # 示例参数 b > 0
        
        # 计算关键位置
        self.origin_pos = self.number_line.n2p(0)
        self.pos_a = self.number_line.n2p(self.a_val)
        self.neg_a = self.number_line.n2p(-self.a_val)
        self.pos_b = self.number_line.n2p(self.b_val)
        self.neg_b = self.number_line.n2p(-self.b_val)
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证数轴上的点位置
        zero_pos = self.number_line.n2p(0)
        three_pos = self.number_line.n2p(3)
        minus_three_pos = self.number_line.n2p(-3)
        
        # 验证距离关系
        dist_0_to_3 = np.linalg.norm(three_pos - zero_pos)
        dist_0_to_minus_3 = np.linalg.norm(minus_three_pos - zero_pos)
        
        if abs(dist_0_to_3 - dist_0_to_minus_3) > epsilon:
            print(f"⚠️  警告: 数轴上距离不对称")
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
            "含绝对值不等式",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)
        
        # 钩子问题
        hook_question = Text(
            "你知道|x| < 3的解是什么吗？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(hook_question), run_time=0.4)
        self.wait(1)
        
        # 清理钩子问题
        self.play(FadeOut(hook_question), run_time=0.5)
    
    def review_absolute_value_meaning(self):
        """场景2: 绝对值几何意义回顾"""
        # 显示数轴
        self.play(Create(self.number_line), run_time=1.5)
        
        # 原点标记
        origin_dot = Dot(self.origin_pos, color=RED, radius=0.1)
        origin_label = MathTex("0", color=RED).next_to(origin_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(origin_dot),
            Write(origin_label)
        )
        
        # 示例点x=2和x=-2
        x_pos = 2
        x_neg = -2
        
        x_pos_dot = Dot(self.number_line.n2p(x_pos), color=self.COLOR_POINTS, radius=0.1)
        x_neg_dot = Dot(self.number_line.n2p(x_neg), color=self.COLOR_POINTS, radius=0.1)
        
        x_pos_label = MathTex(f"{x_pos}", color=self.COLOR_POINTS).next_to(x_pos_dot, UP, buff=0.2)
        x_neg_label = MathTex(f"{x_neg}", color=self.COLOR_POINTS).next_to(x_neg_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(x_pos_dot),
            Write(x_pos_label),
            FadeIn(x_neg_dot),
            Write(x_neg_label)
        )
        
        # 显示距离线段
        dist_to_pos = Line(self.origin_pos, self.number_line.n2p(x_pos), color=self.COLOR_HIGHLIGHT, stroke_width=3)
        dist_to_neg = Line(self.origin_pos, self.number_line.n2p(x_neg), color=self.COLOR_HIGHLIGHT, stroke_width=3)
        
        dist_pos_brace = Brace(dist_to_pos, UP, color=self.COLOR_HIGHLIGHT)
        dist_neg_brace = Brace(dist_to_neg, DOWN, color=self.COLOR_HIGHLIGHT)
        
        dist_pos_label = MathTex(f"|{x_pos}| = {x_pos}", color=self.COLOR_HIGHLIGHT).next_to(dist_pos_brace, UP)
        dist_neg_label = MathTex(f"|{x_neg}| = {-x_neg}", color=self.COLOR_HIGHLIGHT).next_to(dist_neg_brace, DOWN)
        
        self.play(
            Create(dist_to_pos),
            GrowFromCenter(dist_pos_brace),
            Write(dist_pos_label)
        )
        
        self.play(
            Create(dist_to_neg),
            GrowFromCenter(dist_neg_brace),
            Write(dist_neg_label)
        )
        
        # 解释绝对值的几何意义
        geometric_meaning = Text(
            "绝对值|a|表示数a到原点的距离",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5)
        
        self.play(Write(geometric_meaning), run_time=1)
        self.wait(1)
        
        # 清理部分元素，保留数轴和原点
        self.play(
            FadeOut(dist_to_pos),
            FadeOut(dist_to_neg),
            FadeOut(dist_pos_brace),
            FadeOut(dist_neg_brace),
            FadeOut(dist_pos_label),
            FadeOut(dist_neg_label),
            FadeOut(geometric_meaning),
            FadeOut(x_pos_dot),
            FadeOut(x_pos_label),
            FadeOut(x_neg_dot),
            FadeOut(x_neg_label),
            run_time=0.5
        )
    
    def show_less_than_inequality(self):
        """场景3: |x| < a 型不等式"""
        # 标题
        title = Text(
            "|x| < a 型不等式 (a > 0)",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ABSOLUTE_VALUE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记-a和a点
        neg_a_dot = Dot(self.neg_a, color=RED, radius=0.1)
        pos_a_dot = Dot(self.pos_a, color=RED, radius=0.1)
        
        neg_a_label = MathTex(f"-{self.a_val}", color=RED).next_to(neg_a_dot, DOWN, buff=0.2)
        pos_a_label = MathTex(f"{self.a_val}", color=RED).next_to(pos_a_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(neg_a_dot),
            FadeIn(pos_a_dot),
            Write(neg_a_label),
            Write(pos_a_label)
        )
        
        # 高亮区间(-a, a)
        solution_line = Line(self.neg_a, self.pos_a, color=self.COLOR_SOLUTION_REGION, stroke_width=8)
        
        self.play(Create(solution_line), run_time=1)
        
        # 显示等价形式
        equivalence = MathTex(
            f"|x| < {self.a_val}", 
            "\\iff", 
            f"-{self.a_val} < x < {self.a_val}",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(DOWN * 3)
        
        self.play(Write(equivalence), run_time=1)
        
        # 解释几何意义
        geometric_interpretation = Text(
            f"在数轴上，到原点距离小于{self.a_val}的点的集合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(Write(geometric_interpretation), run_time=1)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(neg_a_dot),
            FadeOut(pos_a_dot),
            FadeOut(neg_a_label),
            FadeOut(pos_a_label),
            FadeOut(solution_line),
            FadeOut(equivalence),
            FadeOut(geometric_interpretation),
            FadeOut(title),
            run_time=0.5
        )
    
    def show_greater_than_inequality(self):
        """场景4: |x| > a 型不等式"""
        # 标题
        title = Text(
            "|x| > a 型不等式 (a > 0)",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ABSOLUTE_VALUE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记-a和a点
        neg_a_dot = Dot(self.neg_a, color=RED, radius=0.1)
        pos_a_dot = Dot(self.pos_a, color=RED, radius=0.1)
        
        neg_a_label = MathTex(f"-{self.a_val}", color=RED).next_to(neg_a_dot, DOWN, buff=0.2)
        pos_a_label = MathTex(f"{self.a_val}", color=RED).next_to(pos_a_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(neg_a_dot),
            FadeIn(pos_a_dot),
            Write(neg_a_label),
            Write(pos_a_label)
        )
        
        # 高亮解集：(-∞, -a) ∪ (a, +∞)
        left_ray = Line(
            self.number_line.n2p(-5), 
            self.neg_a, 
            color=self.COLOR_SOLUTION_REGION, 
            stroke_width=8
        )
        right_ray = Line(
            self.pos_a, 
            self.number_line.n2p(5), 
            color=self.COLOR_SOLUTION_REGION, 
            stroke_width=8
        )
        
        self.play(
            Create(left_ray),
            Create(right_ray),
            run_time=1.5
        )
        
        # 显示等价形式
        equivalence = MathTex(
            f"|x| > {self.a_val}", 
            "\\iff", 
            f"x < -{self.a_val}", 
            "\\text{ 或 }", 
            f"x > {self.a_val}",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(DOWN * 3)
        
        self.play(Write(equivalence), run_time=1)
        
        # 解释几何意义
        geometric_interpretation = Text(
            f"在数轴上，到原点距离大于{self.a_val}的点的集合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(Write(geometric_interpretation), run_time=1)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(neg_a_dot),
            FadeOut(pos_a_dot),
            FadeOut(neg_a_label),
            FadeOut(pos_a_label),
            FadeOut(left_ray),
            FadeOut(right_ray),
            FadeOut(equivalence),
            FadeOut(geometric_interpretation),
            FadeOut(title),
            run_time=0.5
        )
    
    def show_shifted_inequality(self):
        """场景5: |x-a| < b 型不等式"""
        # 标题
        title = Text(
            "|x-a| < b 型不等式 (b > 0)",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ABSOLUTE_VALUE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 使用具体数值 a=2, b=1 来演示 |x-2| < 1
        center_val = 2
        radius_val = 1
        
        # 标记中心点a和边界点
        center_dot = Dot(self.number_line.n2p(center_val), color=RED, radius=0.1)
        left_boundary = Dot(self.number_line.n2p(center_val - radius_val), color=RED, radius=0.1)
        right_boundary = Dot(self.number_line.n2p(center_val + radius_val), color=RED, radius=0.1)
        
        center_label = MathTex(f"{center_val}", color=RED).next_to(center_dot, UP, buff=0.2)
        left_label = MathTex(f"{center_val - radius_val}", color=RED).next_to(left_boundary, DOWN, buff=0.2)
        right_label = MathTex(f"{center_val + radius_val}", color=RED).next_to(right_boundary, DOWN, buff=0.2)
        
        self.play(
            FadeIn(center_dot),
            FadeIn(left_boundary),
            FadeIn(right_boundary),
            Write(center_label),
            Write(left_label),
            Write(right_label)
        )
        
        # 高亮区间[a-b, a+b]
        interval_line = Line(
            self.number_line.n2p(center_val - radius_val), 
            self.number_line.n2p(center_val + radius_val), 
            color=self.COLOR_SOLUTION_REGION, 
            stroke_width=8
        )
        
        self.play(Create(interval_line), run_time=1)
        
        # 显示等价形式
        equivalence = MathTex(
            f"|x-{center_val}| < {radius_val}", 
            "\\iff", 
            f"{center_val - radius_val} < x < {center_val + radius_val}",
            color=self.COLOR_HIGHLIGHT,
            font_size=28
        ).move_to(DOWN * 3)
        
        self.play(Write(equivalence), run_time=1)
        
        # 解释几何意义
        geometric_interpretation = Text(
            f"在数轴上，到点{center_val}距离小于{radius_val}的点的集合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(Write(geometric_interpretation), run_time=1)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(center_dot),
            FadeOut(left_boundary),
            FadeOut(right_boundary),
            FadeOut(center_label),
            FadeOut(left_label),
            FadeOut(right_label),
            FadeOut(interval_line),
            FadeOut(equivalence),
            FadeOut(geometric_interpretation),
            FadeOut(title),
            run_time=0.5
        )
    
    def show_triangle_inequality(self):
        """场景6: 三角不等式"""
        # 标题
        title = Text(
            "三角不等式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ABSOLUTE_VALUE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 主要公式
        main_inequality = MathTex(
            "|a + b| \\leq |a| + |b|",
            color=self.COLOR_HIGHLIGHT,
            font_size=36
        ).move_to(UP * 4)
        
        self.play(Write(main_inequality), run_time=0.8)
        
        # 补充公式
        extended_inequality = MathTex(
            "||a| - |b|| \\leq |a \\pm b| \\leq |a| + |b|",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(UP * 2.5)
        
        self.play(Write(extended_inequality), run_time=0.8)
        
        # 举例说明
        example = MathTex(
            "\\text{例如: } a=3, b=-2 ", 
            "\\Rightarrow |3+(-2)| = |1| = 1", 
            "\\leq |3| + |-2| = 5",
            font_size=28
        ).move_to(DOWN * 1)
        
        self.play(Write(example), run_time=1.5)
        
        self.wait(2)
        
        # 清理部分元素，保留标题和主要不等式
        self.play(
            FadeOut(extended_inequality),
            FadeOut(example),
            run_time=0.5
        )
    
    def show_outro(self):
        """片尾"""
        # 总结文字
        summary = Text(
            "总结:\n1. |x| < a ⟺ -a < x < a\n2. |x| > a ⟺ x < -a 或 x > a\n3. |x-a| < b ⟺ a-b < x < a+b",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1)
        
        self.play(Write(summary), run_time=1.5)
        
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
    # 运行命令: manim -pql absolute_value_inequalities.py AbsoluteValueInequalitiesAnimation
    pass