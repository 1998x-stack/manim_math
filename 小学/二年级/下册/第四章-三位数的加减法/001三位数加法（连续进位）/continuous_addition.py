from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class ContinuousAddition(Scene):
    """
    二年级下册三位数加法（连续进位）教学动画
    
    场景顺序:
    1. 开场钩子
    2. 竖式对齐
    3. 个位相加满十进一
    4. 十位相加满十进一
    5. 百位相加得出结果
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_AUXILIARY = "#95a5a6"
        self.COLOR_CARRY = "#e74c3c"
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
        self.show_ones_addition()
        self.show_tens_addition()
        self.show_hundreds_addition()
        self.show_summary()
    
    def create_digit(self, digit_str, font_size=48, color=WHITE):
        """创建单个数字对象"""
        return Text(digit_str, font_size=font_size, color=color)
    
    def show_opening(self):
        """场景1: 开场钩子"""
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "个位十位都满十，怎么办？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        # 题目
        problem_eq = MathTex(r"199 + 103 = ?", font_size=48)
        problem_desc = Text("连续进位加法", font="PingFang SC", font_size=28, color=self.COLOR_AUXILIARY)
        problem = VGroup(problem_eq, problem_desc).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        self.play(Write(problem), run_time=2.0)
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(hook_text), FadeOut(problem), run_time=0.5)
    
    def show_vertical_form(self):
        """场景2: 竖式对齐"""
        # 创建被加数199的各个数字
        self.a1_hundreds = self.create_digit("1")
        self.a1_tens = self.create_digit("9")
        self.a1_ones = self.create_digit("9")
        
        # 被加数组
        self.addend1 = VGroup(self.a1_hundreds, self.a1_tens, self.a1_ones)
        self.addend1.arrange(RIGHT, buff=1.5).move_to(UP * 2)
        
        # 加号
        self.plus_sign = self.create_digit("+")
        self.plus_sign.move_to(LEFT * 3.5 + UP * 1)
        
        # 创建加数103的各个数字
        self.a2_hundreds = self.create_digit("1")
        self.a2_tens = self.create_digit("0")
        self.a2_ones = self.create_digit("3")
        
        # 加数组
        self.addend2 = VGroup(self.a2_hundreds, self.a2_tens, self.a2_ones)
        self.addend2.arrange(RIGHT, buff=1.5).move_to(UP * 1)
        
        # 横线
        self.hr = Line(LEFT * 3, RIGHT * 3, color=self.COLOR_WHITE, stroke_width=3).move_to(ORIGIN)
        
        # 数位标签
        place_labels = VGroup(
            Text("百位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.a1_hundreds, UP, buff=0.8),
            Text("十位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.a1_tens, UP, buff=0.8),
            Text("个位", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(self.a1_ones, UP, buff=0.8)
        )
        
        self.play(Write(self.addend1), run_time=1.0)
        self.play(Write(self.plus_sign), Write(self.addend2), run_time=1.0)
        self.play(Create(self.hr), run_time=0.5)
        self.play(FadeIn(place_labels), run_time=0.5)
        
        # 高亮数位对齐
        digits = VGroup(
            self.a1_hundreds, self.a1_tens, self.a1_ones,
            self.a2_hundreds, self.a2_tens, self.a2_ones
        )
        self.play(Indicate(digits, color=self.COLOR_HIGHLIGHT), run_time=1.5)
        self.wait(2.0)
        
        # 保存竖式元素
        self.vertical_form = VGroup(self.addend1, self.plus_sign, self.addend2, self.hr, place_labels)
    
    def show_ones_addition(self):
        """场景3: 个位相加满十进一"""
        # 高亮个位9和3
        ones_digits = VGroup(self.a1_ones, self.a2_ones)
        self.play(Indicate(ones_digits, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        
        # 个位计算文字
        ones_calc = VGroup(
            MathTex(r"9 + 3 = 12", font_size=36),
            Text("满十进一", font="PingFang SC", font_size=24, color=self.COLOR_CARRY)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3)
        self.play(Write(ones_calc), run_time=1.5)
        
        # 画进位箭头到十位
        self.arrow_to_tens = Arrow(
            start=self.a1_ones.get_center() + UP * 0.8,
            end=self.a1_tens.get_center() + UP * 0.8,
            color=self.COLOR_CARRY,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(GrowArrow(self.arrow_to_tens), run_time=1.0)
        
        # 写进位小1
        self.carry_one_tens = Text("1", font_size=24, color=self.COLOR_CARRY)
        self.carry_one_tens.next_to(self.a1_tens, UP, buff=0.3)
        self.play(Write(self.carry_one_tens), run_time=0.5)
        
        # 写个位结果2
        self.ones_result = self.create_digit("2", color=self.COLOR_POSITIVE)
        self.ones_result.move_to(self.a1_ones.get_center() + DOWN * 1.5)
        self.play(Write(self.ones_result), run_time=0.5)
        
        self.wait(4.0)
        
        # 清理
        self.play(FadeOut(ones_calc), run_time=0.5)
    
    def show_tens_addition(self):
        """场景4: 十位相加满十进一"""
        # 高亮十位9、0和进位1
        tens_digits = VGroup(self.a1_tens, self.a2_tens, self.carry_one_tens)
        self.play(Indicate(tens_digits, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        
        # 十位计算文字
        tens_calc = VGroup(
            MathTex(r"9 + 0 + 1 = 10", font_size=36),
            Text("又满十了，再进一！", font="PingFang SC", font_size=24, color=self.COLOR_CARRY)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3)
        self.play(Write(tens_calc), run_time=2.0)
        
        # 画进位箭头到百位
        self.arrow_to_hundreds = Arrow(
            start=self.a1_tens.get_center() + UP * 0.8,
            end=self.a1_hundreds.get_center() + UP * 0.8,
            color=self.COLOR_CARRY,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(GrowArrow(self.arrow_to_hundreds), run_time=1.0)
        
        # 写进位小1
        self.carry_one_hundreds = Text("1", font_size=24, color=self.COLOR_CARRY)
        self.carry_one_hundreds.next_to(self.a1_hundreds, UP, buff=0.3)
        self.play(Write(self.carry_one_hundreds), run_time=0.5)
        
        # 写十位结果0
        self.tens_result = self.create_digit("0", color=self.COLOR_POSITIVE)
        self.tens_result.move_to(self.a1_tens.get_center() + DOWN * 1.5)
        self.play(Write(self.tens_result), run_time=0.5)
        
        self.wait(5.5)
        
        # 清理
        self.play(FadeOut(tens_calc), run_time=0.5)
    
    def show_hundreds_addition(self):
        """场景5: 百位相加得出结果"""
        # 高亮百位1、1和进位1
        hundreds_digits = VGroup(self.a1_hundreds, self.a2_hundreds, self.carry_one_hundreds)
        self.play(Indicate(hundreds_digits, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        
        # 百位计算文字
        hundreds_calc = MathTex(r"1 + 1 + 1 = 3", font_size=36).move_to(DOWN * 3)
        self.play(Write(hundreds_calc), run_time=2.0)
        
        # 写百位结果3
        self.hundreds_result = self.create_digit("3", color=self.COLOR_POSITIVE)
        self.hundreds_result.move_to(self.a1_hundreds.get_center() + DOWN * 1.5)
        self.play(Write(self.hundreds_result), run_time=0.5)
        
        # 组合最终答案302
        final_answer = VGroup(self.hundreds_result, self.tens_result, self.ones_result)
        self.play(Indicate(final_answer, color=self.COLOR_POSITIVE), run_time=1.5)
        
        # 显示完整等式
        full_eq = MathTex(r"199 + 103 = 302", font_size=48, color=self.COLOR_POSITIVE)
        full_eq.move_to(DOWN * 4.5)
        self.play(Write(full_eq), run_time=1.0)
        self.wait(2.0)
        
        # 保存答案
        self.final_answer = VGroup(final_answer, full_eq)
    
    def show_summary(self):
        """场景6: 总结与片尾"""
        # 竖式和答案淡出
        self.play(
            FadeOut(self.vertical_form),
            FadeOut(self.arrow_to_tens),
            FadeOut(self.carry_one_tens),
            FadeOut(self.ones_result),
            FadeOut(self.arrow_to_hundreds),
            FadeOut(self.carry_one_hundreds),
            FadeOut(self.tens_result),
            FadeOut(self.hundreds_result),
            FadeOut(self.final_answer),
            run_time=0.5
        )
        
        # 步骤总结
        summary = VGroup(
            Text("连续进位加法步骤：", font="PingFang SC", font_size=32, color=self.COLOR_HIGHLIGHT),
            Text("1. 相同数位对齐", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("2. 从个位加起", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("3. 哪一位满十，向前一位进1", font="PingFang SC", font_size=24, color=self.COLOR_WHITE),
            Text("4. 连续满十，连续进位", font="PingFang SC", font_size=24, color=self.COLOR_WHITE)
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
# manim -pql continuous_addition.py ContinuousAddition  # 快速预览
# manim -qh continuous_addition.py ContinuousAddition   # 高质量