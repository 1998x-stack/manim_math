from manim import *
import numpy as np

# manim -qh BasicInequalityAnimation.py BasicInequalityAnimation

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class BasicInequalityAnimation(Scene):
    """
    基本不等式（均值不等式）教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 算术平均数与几何平均数比较
    3. 几何解释 - 矩形与正方形
    4. 代数证明
    5. 应用条件
    6. 平均数链式不等式
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ARITHMETIC_MEAN = BLUE
        self.COLOR_GEOMETRIC_MEAN = GREEN
        self.COLOR_HARMONIC_MEAN = PURPLE
        self.COLOR_QUADRATIC_MEAN = ORANGE
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_arithmetic_vs_geometric_means()
        self.show_geometric_interpretation()
        self.show_algebraic_proof()
        self.show_application_conditions()
        self.show_means_chain_inequality()
    
    def setup_geometry(self):
        """初始化几何数据和参数"""
        # 设定测试值
        self.a = 4.0  # 可以根据需要调整
        self.b = 1.0
        
        # 计算各种平均数
        self.arithmetic_mean = (self.a + self.b) / 2
        self.geometric_mean = np.sqrt(self.a * self.b)
        self.harmonic_mean = 2 / (1/self.a + 1/self.b)
        self.quadratic_mean = np.sqrt((self.a**2 + self.b**2) / 2)
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证基本不等式 H ≤ G ≤ A ≤ Q
        means = [self.harmonic_mean, self.geometric_mean, self.arithmetic_mean, self.quadratic_mean]
        names = ["调和平均数", "几何平均数", "算术平均数", "平方平均数"]
        
        valid_chain = True
        for i in range(len(means) - 1):
            if means[i] > means[i+1] + epsilon:
                print(f"警告: {names[i]} > {names[i+1]} 不符合链式不等式")
                valid_chain = False
        
        if valid_chain:
            print("✓ 链式不等式验证通过")
        else:
            print("❌ 链式不等式验证失败")
    
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
            "基本不等式（均值不等式）",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        # 钩子问题
        hook_question = Text(
            "为什么算术平均数总是大于等于几何平均数？",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(hook_question), run_time=0.4)
        self.wait(1)
        
        # 清理
        self.play(FadeOut(hook_question), run_time=0.5)
    
    def show_arithmetic_vs_geometric_means(self):
        """场景2: 算术平均数与几何平均数比较"""
        # 标题
        title = Text(
            "算术平均数 vs 几何平均数",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ARITHMETIC_MEAN
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建数轴
        number_line = NumberLine(
            x_range=[-1, max(self.a, self.b) + 1, 1],
            length=6,
            include_numbers=True,
            label_direction=UP
        ).shift(UP * 3)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 标记a和b点
        point_a = Dot(number_line.n2p(self.a), color=RED, radius=0.1)
        point_b = Dot(number_line.n2p(self.b), color=RED, radius=0.1)
        
        label_a = MathTex(f"a={self.a}", color=RED).next_to(point_a, DOWN, buff=0.2)
        label_b = MathTex(f"b={self.b}", color=RED).next_to(point_b, DOWN, buff=0.2)
        
        self.play(
            FadeIn(point_a),
            FadeIn(point_b),
            Write(label_a),
            Write(label_b)
        )
        
        # 计算并标记算术平均数
        arithmetic_pos = number_line.n2p(self.arithmetic_mean)
        arithmetic_dot = Dot(arithmetic_pos, color=self.COLOR_ARITHMETIC_MEAN, radius=0.1)
        arithmetic_label = MathTex(
            f"A = \\frac{{a+b}}{{2}} = \\frac{{{self.a}+{self.b}}}{{2}} = {self.arithmetic_mean}", 
            color=self.COLOR_ARITHMETIC_MEAN
        ).next_to(arithmetic_dot, UP, buff=0.2)
        
        self.play(FadeIn(arithmetic_dot), Write(arithmetic_label), run_time=0.8)
        
        # 计算并标记几何平均数
        geometric_pos = number_line.n2p(self.geometric_mean)
        geometric_dot = Dot(geometric_pos, color=self.COLOR_GEOMETRIC_MEAN, radius=0.1)
        geometric_label = MathTex(
            f"G = \\sqrt{{ab}} = \\sqrt{{{self.a}\\cdot {self.b}}} = \\sqrt{{{self.a * self.b}}} = {self.geometric_mean:.3f}", 
            color=self.COLOR_GEOMETRIC_MEAN
        ).next_to(geometric_dot, DOWN, buff=0.2)
        
        self.play(FadeIn(geometric_dot), Write(geometric_label), run_time=0.8)
        
        # 用线段比较两者大小
        comparison_line = Line(
            geometric_pos, arithmetic_pos,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        comparison_text = MathTex(
            f"A \\geq G", 
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison_line, UP, buff=0.1)
        
        self.play(Create(comparison_line), Write(comparison_text), run_time=1.0)
        
        # 显示基本不等式
        main_inequality = MathTex(
            f"\\frac{{a+b}}{{2}} \\geq \\sqrt{{ab}} \\quad (a,b > 0)",
            color=self.COLOR_HIGHLIGHT,
            font_size=36
        ).move_to(DOWN * 2)
        
        self.play(Write(main_inequality), run_time=1.0)
        
        self.wait(2)
        
        # 清理部分元素，保留数轴和关键点
        self.play(
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(comparison_line),
            FadeOut(comparison_text),
            FadeOut(main_inequality),
            run_time=0.5
        )
    
    def show_geometric_interpretation(self):
        """场景3: 几何解释 - 矩形与正方形"""
        # 标题
        title = Text(
            "几何解释",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(ReplacementTransform(self.mobjects[self.index_of_last_object("Text")], title), run_time=0.8)
        
        # 创建矩形 (边长a和b)
        rect_width = self.a
        rect_height = self.b
        rectangle = Rectangle(
            width=rect_width, 
            height=rect_height, 
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3
        ).move_to(UP * 1.5)

        rect_label = Text(
            f"矩形: 长={self.a}, 宽={self.b}, 面积={self.a*self.b}",
            font="Noto Sans CJK SC", font_size=22, color=WHITE
        ).next_to(rectangle, UP, buff=0.2)

        self.play(Create(rectangle), Write(rect_label), run_time=1.0)
        
        # 创建面积相等的正方形 (边长为√(ab))
        square_side = np.sqrt(self.a * self.b)
        square = Square(
            side_length=square_side,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.3
        ).next_to(rectangle, DOWN, buff=1.5)
        
        sq_text = Text(f"正方形: 边长=", font="Noto Sans CJK SC", font_size=20, color=GREEN)
        sq_math = MathTex(f"\\sqrt{{ab}}={square_side:.3f}", font_size=20, color=GREEN)
        sq_area = Text(f", 面积={self.a*self.b}", font="Noto Sans CJK SC", font_size=20, color=GREEN)
        square_label = VGroup(sq_text, sq_math, sq_area).arrange(RIGHT, buff=0.1).next_to(square, DOWN, buff=0.2)
        
        self.play(Create(square), Write(square_label), run_time=1.0)
        
        # 创建周长相等的正方形 (边长为(a+b)/2)
        perimeter_square_side = (self.a + self.b) / 2
        perimeter_square = Square(
            side_length=perimeter_square_side,
            color=RED,
            fill_color=RED,
            fill_opacity=0.3
        ).next_to(rectangle, LEFT, buff=2.5)
        
        ps_text = Text(f"周长相同正方形: 边长=", font="Noto Sans CJK SC", font_size=18, color=RED)
        ps_math = MathTex(f"\\frac{{a+b}}{{2}}={perimeter_square_side}", font_size=18, color=RED)
        perimeter_square_label = VGroup(ps_text, ps_math).arrange(RIGHT, buff=0.1).next_to(perimeter_square, LEFT, buff=0.2)
        
        self.play(Create(perimeter_square), Write(perimeter_square_label), run_time=1.0)
        
        # 添加比较说明
        comparison_text = Text(
            "相同周长下，正方形面积 > 矩形面积\n相同面积下，正方形周长 < 矩形周长",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(Write(comparison_text), run_time=1.0)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(rectangle),
            FadeOut(rect_label),
            FadeOut(square),
            FadeOut(square_label),
            FadeOut(perimeter_square),
            FadeOut(perimeter_square_label),
            FadeOut(comparison_text),
            run_time=0.5
        )
    
    def show_algebraic_proof(self):
        """场景4: 代数证明"""
        # 标题
        title = Text(
            "代数证明",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        # 清理前一场景，显示标题
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title and type(mob) != Text and not isinstance(mob, NumberLine)],
            run_time=0.5
        )
        
        # 证明步骤
        step1 = MathTex("(a-b)^2 \\geq 0", font_size=36, color=WHITE).move_to(UP * 3)
        step2 = MathTex("a^2 - 2ab + b^2 \\geq 0", font_size=36, color=WHITE).move_to(UP * 1.5)
        step3 = MathTex("a^2 + 2ab + b^2 \\geq 4ab", font_size=36, color=WHITE).move_to(ORIGIN)
        step4 = MathTex("(a+b)^2 \\geq 4ab", font_size=36, color=WHITE).move_to(DOWN * 1.5)
        step5 = MathTex("\\frac{(a+b)^2}{4} \\geq ab", font_size=36, color=WHITE).move_to(DOWN * 3)
        step6 = MathTex("\\frac{a+b}{2} \\geq \\sqrt{ab}", font_size=36, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        
        # 逐步展示证明过程
        self.play(Write(step1), run_time=1.0)
        self.wait(1)
        
        self.play(Write(step2), run_time=1.0)
        self.wait(1)
        
        self.play(Write(step3), run_time=1.0)
        self.wait(1)
        
        self.play(Write(step4), run_time=1.0)
        self.wait(1)
        
        self.play(Write(step5), run_time=1.0)
        self.wait(1)
        
        self.play(Write(step6), run_time=1.0)
        self.wait(2)
        
        # 显示等号成立条件
        cond_text = Text("等号成立当且仅当 ", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_HIGHLIGHT)
        cond_math = MathTex("a = b", font_size=28, color=self.COLOR_HIGHLIGHT)
        condition = VGroup(cond_text, cond_math).arrange(RIGHT, buff=0.15).move_to(DOWN * 6)
        self.play(Write(condition), run_time=0.8)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(step5),
            FadeOut(condition),
            run_time=0.5
        )
    
    def show_application_conditions(self):
        """场景5: 应用条件"""
        # 标题
        title = Text(
            "应用条件「一正二定三相等」",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        # 清理前一场景，显示标题
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title and str(type(mob).__name__) != "NumberLine"],
            run_time=0.5
        )
        
        # 显示三个条件
        condition1 = Text(
            "一正：各项为正 (a, b > 0)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=BLUE
        ).move_to(UP * 3)
        
        condition2 = Text(
            "二定：和或积为定值",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).move_to(UP * 1.5)
        
        condition3 = Text(
            "三相等：能取到等号 (a = b)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=PURPLE
        ).move_to(ORIGIN)
        
        # 举例说明
        example = Text(
            "例：若 x > 0，求 x + 1/x 的最小值",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        solution = MathTex(
            "x + \\frac{1}{x} \\geq 2\\sqrt{x \\cdot \\frac{1}{x}} = 2",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 3)
        
        min_value = Text(
            "当 x = 1/x 即 x = 1 时，取得最小值 2",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        # 动画展示
        self.play(Write(condition1), run_time=0.8)
        self.play(Write(condition2), run_time=0.8)
        self.play(Write(condition3), run_time=0.8)
        
        self.wait(1)
        
        self.play(Write(example), run_time=0.8)
        self.play(Write(solution), run_time=0.8)
        self.play(Write(min_value), run_time=0.8)
        
        self.wait(2)
    
    def show_means_chain_inequality(self):
        """场景6: 平均数链式不等式"""
        # 标题
        title = Text(
            "平均数链式不等式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        # 清理前一场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if str(type(mob).__name__) != "Text"],
            ReplacementTransform(self.mobjects[self.index_of_last_object("Text")], title),
            run_time=0.5
        )
        
        # 链式不等式
        chain_inequality = MathTex(
            "\\underbrace{\\frac{2}{\\frac{1}{a} + \\frac{1}{b}}}_{H} \\leq "
            "\\underbrace{\\sqrt{ab}}_{G} \\leq "
            "\\underbrace{\\frac{a+b}{2}}_{A} \\leq "
            "\\underbrace{\\sqrt{\\frac{a^2+b^2}{2}}}_{Q}",
            font_size=32
        ).move_to(UP * 4.5)
        
        # 各义说明
        def mean_label(letter, name, color, pos):
            math = MathTex(f"{letter} =", color=color, font_size=28)
            txt = Text(name, font="Noto Sans CJK SC", font_size=24, color=color)
            return VGroup(math, txt).arrange(RIGHT, buff=0.15).move_to(pos)

        means_explanation = VGroup(
            mean_label("H", "调和平均数", PURPLE,  UP * 3),
            mean_label("G", "几何平均数", GREEN,   UP * 2),
            mean_label("A", "算术平均数", BLUE,    UP * 1),
            mean_label("Q", "平方平均数", ORANGE,  ORIGIN),
        )
        
        self.play(Write(chain_inequality), run_time=1.0)
        self.wait(1)
        
        for exp in means_explanation:
            self.play(Write(exp), run_time=0.5)
        
        self.wait(2)
        
        # 用具体数值验证
        verification_text = Text(
            f"验证 (a={self.a}, b={self.b}):",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2)
        
        values_text = MathTex(
            f"H={self.harmonic_mean:.3f} \\leq "
            f"G={self.geometric_mean:.3f} \\leq "
            f"A={self.arithmetic_mean:.3f} \\leq "
            f"Q={self.quadratic_mean:.3f}",
            font_size=28
        ).move_to(DOWN * 3.5)
        
        self.play(Write(verification_text), run_time=0.8)
        self.play(Write(values_text), run_time=0.8)
        
        self.wait(2)
        
        # 作者信息
        final_author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(final_author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 关注提示
        follow_hint = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(Write(follow_hint), run_time=0.8)
        
        self.wait(2)
    
    def index_of_last_object(self, class_name):
        """查找指定类型对象的索引"""
        for i in range(len(self.mobjects)-1, -1, -1):
            if class_name in str(type(self.mobjects[i]).__name__):
                return i
        return len(self.mobjects)-1


if __name__ == "__main__":
    # 运行命令: manim -pql 005_基本不等式（均值不等式）.py BasicInequalityAnimation
    pass
