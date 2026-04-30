from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class ContinuousSubtraction(Scene):
    """
    二年级下册三位数减法（连续退位）教学动画
    
    场景顺序:
    1. 开场钩子
    2. 竖式对齐
    3. 个位不够减，向十位借
    4. 十位向百位借
    5. 计算结果
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_AUXILIARY = "#95a5a6"
        self.COLOR_NEGATIVE = "#e74c3c"
        self.COLOR_POSITIVE = "#2ecc71"
        self.COLOR_WHITE = WHITE
        
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        # 执行动画序列
        self.show_opening()
        self.show_vertical_form()
        self.show_ones_problem()
        self.show_tens_borrow()
        self.show_calculation()
        self.show_summary()
    
    def create_digit(self, digit_str, font_size=48, color=WHITE):
        """创建单个数字对象"""
        return Text(digit_str, font_size=font_size, color=color)
    
    def show_opening(self):
        """场景1: 开场钩子"""
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "个位不够减，十位是0怎么办？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        # 题目
        problem_eq = MathTex(r"500 - 123 = ?", font_size=48)
        problem_desc = Text("连续退位减法", font="PingFang SC", font_size=28, color=self.COLOR_AUXILIARY)
        problem = VGroup(problem_eq, problem_desc).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        self.play(Write(problem), run_time=2.0)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(hook_text), FadeOut(problem), run_time=0.5)
    
    def show_vertical_form(self):
        """场景2: 竖式对齐"""
        # 创建被减数500的各个数字
        self.m_hundreds = self.create_digit("5")
        self.m_tens = self.create_digit("0")
        self.m_ones = self.create_digit("0")
        
        # 被减数组
        self.minuend = VGroup(self.m_hundreds, self.m_tens, self.m_ones)
        self.minuend.arrange(RIGHT, buff=1.5).move_to(UP * 2)
        
        # 减号
        self.minus_sign = self.create_digit("-")
        self.minus_sign.move_to(LEFT * 3.5 + UP * 1)
        
        # 创建减数123的各个数字
        self.s_hundreds = self.create_digit("1")
        self.s_tens = self.create_digit("2")
        self.s_ones = self.create_digit("3")
        
        # 减数组
        self.subtrahend = VGroup(self.s_hundreds, self.s_tens, self.s_ones)
        self.subtrahend.arrange(RIGHT, buff=1.5).move_to(UP * 1)
        
        # 横线
        self.hr = Line(LEFT * 3, RIGHT * 3, color=self.COLOR_WHITE, stroke_width=3).move_to(ORIGIN)
        
        # 数位标签
        place_labels = VGroup(
            Text("百位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.m_hundreds, UP, buff=0.8),
            Text("十位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.m_tens, UP, buff=0.8),
            Text("个位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.m_ones, UP, buff=0.8)
        )
        
        self.play(Write(self.minuend), run_time=1.0)
        self.play(Write(self.minus_sign), Write(self.subtrahend), run_time=1.0)
        self.play(Create(self.hr), run_time=0.5)
        self.play(FadeIn(place_labels), run_time=0.5)
        
        # 高亮数位对齐
        digits = VGroup(
            self.m_hundreds, self.m_tens, self.m_ones,
            self.s_hundreds, self.s_tens, self.s_ones
        )
        self.play(Indicate(digits, color=self.COLOR_HIGHLIGHT), run_time=1.5)
        self.wait(2.0)
        
        # 保存竖式元素
        self.vertical_form = VGroup(self.minuend, self.minus_sign, self.subtrahend, self.hr, place_labels)
    
    def show_ones_problem(self):
        """场景3: 个位不够减，向十位借"""
        # 高亮个位0和3
        ones_digits = VGroup(self.m_ones, self.s_ones)
        self.play(Indicate(ones_digits, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        
        # 个位问题文字
        ones_problem = Text(
            "个位：0 不够减 3",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_WHITE
        ).move_to(DOWN * 3)
        self.play(Write(ones_problem), run_time=1.0)
        
        # 画借位箭头到十位
        self.arrow_to_tens = Arrow(
            start=self.m_ones.get_center() + DOWN * 0.5,
            end=self.m_tens.get_center() + DOWN * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(GrowArrow(self.arrow_to_tens), run_time=1.0)
        
        # 高亮十位0
        self.play(Indicate(self.m_tens, color=self.COLOR_NEGATIVE), run_time=1.0)
        
        # 十位问题文字
        tens_problem = Text(
            "十位：是 0，借不到！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 4)
        self.play(Write(tens_problem), run_time=1.0)
        self.wait(4.0)
        
        # 清理
        self.play(FadeOut(ones_problem), FadeOut(tens_problem), run_time=0.5)
    
    def show_tens_borrow(self):
        """场景4: 十位向百位借"""
        # 画借位箭头到百位
        self.arrow_to_hundreds = Arrow(
            start=self.m_tens.get_center() + DOWN * 0.5,
            end=self.m_hundreds.get_center() + DOWN * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(GrowArrow(self.arrow_to_hundreds), run_time=1.0)
        
        # 百位5变4：划掉5，写4
        cross_five = Cross(self.m_hundreds, color=self.COLOR_NEGATIVE, stroke_width=3)
        four = self.create_digit("4", color=self.COLOR_HIGHLIGHT)
        four.move_to(self.m_hundreds.get_center() + UP * 0.6)
        
        self.play(Create(cross_five), run_time=0.5)
        self.play(Write(four), run_time=0.5)
        
        # 十位0变10：在十位上方写10
        ten_on_tens = Text("10", font_size=36, color=self.COLOR_HIGHLIGHT)
        ten_on_tens.move_to(self.m_tens.get_center() + UP * 0.6)
        self.play(Write(ten_on_tens), run_time=0.5)
        
        # 十位借给个位1的文字
        tens_lend = Text(
            "十位有10了，借给个位1",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_WHITE
        ).move_to(DOWN * 3)
        self.play(Write(tens_lend), run_time=1.0)
        
        # 十位10变9：划掉10，写9
        cross_ten = Cross(ten_on_tens, color=self.COLOR_NEGATIVE, stroke_width=3)
        nine_on_tens = Text("9", font_size=36, color=self.COLOR_HIGHLIGHT)
        nine_on_tens.move_to(ten_on_tens.get_center())
        self.play(Create(cross_ten), run_time=0.5)
        self.play(Write(nine_on_tens), run_time=0.5)
        
        # 个位0变10：在个位上方写10
        ten_on_ones = Text("10", font_size=36, color=self.COLOR_HIGHLIGHT)
        ten_on_ones.move_to(self.m_ones.get_center() + UP * 0.6)
        self.play(Write(ten_on_ones), run_time=0.5)
        
        self.wait(3.5)
        
        # 清理
        self.play(FadeOut(tens_lend), run_time=0.5)
        
        # 保存借位标记
        self.borrow_marks = VGroup(
            self.arrow_to_tens, self.arrow_to_hundreds,
            cross_five, four, ten_on_tens, cross_ten, nine_on_tens, ten_on_ones
        )
    
    def show_calculation(self):
        """场景5: 计算结果"""
        # 个位计算：10-3=7
        ones_result = self.create_digit("7", color=self.COLOR_POSITIVE)
        ones_result.move_to(self.m_ones.get_center() + DOWN * 1.5)
        self.play(Write(ones_result), run_time=1.0)
        self.wait(0.5)
        
        # 十位计算：9-2=7
        tens_result = self.create_digit("7", color=self.COLOR_POSITIVE)
        tens_result.move_to(self.m_tens.get_center() + DOWN * 1.5)
        self.play(Write(tens_result), run_time=1.0)
        self.wait(0.5)
        
        # 百位计算：4-1=3
        hundreds_result = self.create_digit("3", color=self.COLOR_POSITIVE)
        hundreds_result.move_to(self.m_hundreds.get_center() + DOWN * 1.5)
        self.play(Write(hundreds_result), run_time=1.0)
        self.wait(0.5)
        
        # 组合最终答案377
        final_answer = VGroup(hundreds_result, tens_result, ones_result)
        self.play(Indicate(final_answer, color=self.COLOR_POSITIVE), run_time=1.5)
        
        # 显示完整等式
        full_eq = MathTex(r"500 - 123 = 377", font_size=48, color=self.COLOR_POSITIVE)
        full_eq.move_to(DOWN * 4)
        self.play(Write(full_eq), run_time=1.0)
        self.wait(2.0)
        
        # 保存答案
        self.final_answer = VGroup(final_answer, full_eq)
    
    def show_summary(self):
        """场景6: 总结与片尾"""
        # 竖式和答案淡出
        self.play(
            FadeOut(self.vertical_form),
            FadeOut(self.borrow_marks),
            FadeOut(self.final_answer),
            run_time=0.5
        )
        
        # 步骤总结
        summary = VGroup(
            Text("连续退位减法步骤：", font="PingFang SC", font_size=32, color=self.COLOR_HIGHLIGHT),
            Text("1. 相同数位对齐", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("2. 从个位减起", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("3. 哪一位不够减，向前一位借1", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("4. 中间是0，继续向前借", font="PingFang SC", font_size=24, color=self.COLOR_WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 2)
        
        self.play(FadeIn(summary, shift=DOWN * 0.3), run_time=2.0)
        self.wait(2.0)
        
        # 作者信息放大
        author_large = VGroup(
            Text("上海初高中数学直通车", font="PingFang SC", font_size=40, color=self.COLOR_WHITE),
            Text("@emptyandcalm", font="PingFang SC", font_size=32, color=self.COLOR_AUXILIARY)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2)
        
        self.play(Transform(self.author_info, author_large), run_time=1.0)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary),
            FadeOut(self.author_info),
            FadeOut(follow_text),
            run_time=1.0
        )

# 运行命令:
# manim -pql continuous_subtraction.py ContinuousSubtraction  # 快速预览
# manim -qh continuous_subtraction.py ContinuousSubtraction   # 高质量