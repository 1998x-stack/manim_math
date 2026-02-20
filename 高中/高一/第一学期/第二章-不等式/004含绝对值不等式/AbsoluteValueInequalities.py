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
        self.show_absolute_value_geometric_meaning()
        self.show_inequality_less_than()
        self.show_inequality_greater_than()
        self.show_translated_inequality()
        self.show_triangle_inequality()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何数据和参数"""
        # 创建数轴
        self.number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=8,
            include_numbers=True,
            label_direction=UP,
            stroke_width=4
        ).shift(DOWN * 1)
        
        # 设置参数值
        self.a_val = 3  # 示例参数 a > 0
        self.b_val = 2  # 示例参数 b > 0
        
        # 计算关键点位置
        self.origin_pos = self.number_line.n2p(0)
        self.pos_a = self.number_line.n2p(self.a_val)
        self.neg_a = self.number_line.n2p(-self.a_val)
        self.pos_b = self.number_line.n2p(self.b_val)
        self.neg_b = self.number_line.n2p(-self.b_val)
        
        # 用于|x-a|<b的中心点 (设置为2)
        self.center_a = 2
        self.center_a_pos = self.number_line.n2p(self.center_a)
        self.center_a_minus_b = self.number_line.n2p(self.center_a - self.b_val)
        self.center_a_plus_b = self.number_line.n2p(self.center_a + self.b_val)
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证数轴上关键点的位置
        zero_pos = self.number_line.n2p(0)
        three_pos = self.number_line.n2p(3)
        minus_three_pos = self.number_line.n2p(-3)
        
        # 验证距离关系
        dist_0_to_3 = np.linalg.norm(three_pos - zero_pos)
        dist_0_to_minus_3 = np.linalg.norm(minus_three_pos - zero_pos)
        
        if abs(dist_0_to_3 - dist_0_to_minus_3) > epsilon:
            print("⚠️  警告: 数轴上距离不对称")
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
    
    def show_absolute_value_geometric_meaning(self):
        """场景2: 绝对值几何意义"""
        # 显示数轴
        self.play(Create(self.number_line), run_time=1.5)
        
        # 原点标记
        origin_dot = Dot(self.origin_pos, color=RED, radius=0.1)
        origin_label = MathTex("0", color=RED).next_to(origin_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(origin_dot),
            Write(origin_label)
        )
        
        # 示例点x=2
        x_val = 2
        x_pos = self.number_line.n2p(x_val)
        x_dot = Dot(x_pos, color=self.COLOR_POINTS, radius=0.1)
        x_label = MathTex(f"{x_val}", color=self.COLOR_POINTS).next_to(x_dot, UP, buff=0.2)
        
        self.play(
            FadeIn(x_dot),
            Write(x_label)
        )
        
        # 显示距离线段
        distance_line = Line(self.origin_pos, x_pos, color=self.COLOR_HIGHLIGHT, stroke_width=3)
        distance_brace = Brace(distance_line, UP, color=self.COLOR_HIGHLIGHT)
        distance_label = MathTex(f"|{x_val}| = {abs(x_val)}", color=self.COLOR_HIGHLIGHT).next_to(distance_brace, UP)
        
        self.play(
            Create(distance_line),
            GrowFromCenter(distance_brace),
            Write(distance_label)
        )
        
        # 添加反向点x=-2
        x_neg = -2
        x_neg_pos = self.number_line.n2p(x_neg)
        x_neg_dot = Dot(x_neg_pos, color=self.COLOR_POINTS, radius=0.1)
        x_neg_label = MathTex(f"{x_neg}", color=self.COLOR_POINTS).next_to(x_neg_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(x_neg_dot),
            Write(x_neg_label)
        )
        
        # 反向距离线段
        distance_neg_line = Line(self.origin_pos, x_neg_pos, color=self.COLOR_HIGHLIGHT, stroke_width=3)
        distance_neg_brace = Brace(distance_neg_line, DOWN, color=self.COLOR_HIGHLIGHT)
        distance_neg_label = MathTex(f"|{x_neg}| = {-x_neg}", color=self.COLOR_HIGHLIGHT).next_to(distance_neg_brace, DOWN)
        
        self.play(
            Create(distance_neg_line),
            GrowFromCenter(distance_neg_brace),
            Write(distance_neg_label)
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
            FadeOut(x_dot),
            FadeOut(x_label),
            FadeOut(x_neg_dot),
            FadeOut(x_neg_label),
            FadeOut(distance_line),
            FadeOut(distance_brace),
            FadeOut(distance_label),
            FadeOut(distance_neg_line),
            FadeOut(distance_neg_brace),
            FadeOut(distance_neg_label),
            FadeOut(geometric_meaning),
            run_time=0.5
        )
    
    def show_inequality_less_than(self):
        """场景3: |x| < a 型不等式"""
        # 标题
        title = Text(
            "|x| < a 型不等式",
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
        solution_interval = Line(self.neg_a, self.pos_a, color=self.COLOR_SOLUTION_REGION, stroke_width=8)
        
        self.play(Create(solution_interval), run_time=1)
        
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
            FadeOut(solution_interval),
            FadeOut(equivalence),
            FadeOut(geometric_interpretation),
            FadeOut(title),
            run_time=0.5
        )
    
    def show_inequality_greater_than(self):
        """场景4: |x| > a 型不等式"""
        # 标题
        title = Text(
            "|x| > a 型不等式",
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
        left_ray = DashedLine(
            self.number_line.n2p(-5), 
            self.neg_a, 
            color=self.COLOR_SOLUTION_REGION, 
            dash_length=0.1,
            stroke_width=8
        )
        right_ray = DashedLine(
            self.pos_a, 
            self.number_line.n2p(5), 
            color=self.COLOR_SOLUTION_REGION, 
            dash_length=0.1,
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
    
    def show_translated_inequality(self):
        """场景5: |x-a| < b 型不等式"""
        # 标题
        title = Text(
            "|x-a| < b 型不等式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ABSOLUTE_VALUE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记中心点a和边界点
        center_a_dot = Dot(self.center_a_pos, color=RED, radius=0.1)
        left_boundary = Dot(self.center_a_minus_b, color=RED, radius=0.1)
        right_boundary = Dot(self.center_a_plus_b, color=RED, radius=0.1)
        
        center_a_label = MathTex(f"{self.center_a}", color=RED).next_to(center_a_dot, UP, buff=0.2)
        left_label = MathTex(f"{self.center_a - self.b_val}", color=RED).next_to(left_boundary, DOWN, buff=0.2)
        right_label = MathTex(f"{self.center_a + self.b_val}", color=RED).next_to(right_boundary, DOWN, buff=0.2)
        
        self.play(
            FadeIn(center_a_dot),
            FadeIn(left_boundary),
            FadeIn(right_boundary),
            Write(center_a_label),
            Write(left_label),
            Write(right_label)
        )
        
        # 高亮区间[a-b, a+b]
        interval_line = Line(self.center_a_minus_b, self.center_a_plus_b, color=self.COLOR_SOLUTION_REGION, stroke_width=8)
        
        self.play(Create(interval_line), run_time=1)
        
        # 显示等价形式
        equivalence = MathTex(
            f"|x-{self.center_a}| < {self.b_val}", 
            "\\iff", 
            f"{self.center_a - self.b_val} < x < {self.center_a + self.b_val}",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(DOWN * 3)
        
        self.play(Write(equivalence), run_time=1)
        
        # 解释几何意义
        geometric_interpretation = Text(
            f"在数轴上，到点{self.center_a}距离小于{self.b_val}的点的集合",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(Write(geometric_interpretation), run_time=1)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(center_a_dot),
            FadeOut(left_boundary),
            FadeOut(right_boundary),
            FadeOut(center_a_label),
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
        
        # 扩展公式
        extended_inequality = MathTex(
            "||a| - |b|| \\leq |a \\pm b| \\leq |a| + |b|",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(UP * 2.5)
        
        self.play(Write(extended_inequality), run_time=0.8)
        
        # 举例验证
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
    
    def show_summary(self):
        """场景7: 总结"""
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
    # 运行命令: manim -pql AbsoluteValueInequalitiesAnimation.py AbsoluteValueInequalitiesAnimation
    pass