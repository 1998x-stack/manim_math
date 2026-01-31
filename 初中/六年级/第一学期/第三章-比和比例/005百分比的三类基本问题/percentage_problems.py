"""
百分比的三类基本问题 - Percentage Three Basic Problems
使用 Manim 创建的小学数学教学视频

内容: 求部分、求百分比、求整体
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PercentageProblems(Scene):
    """
    百分比三类基本问题教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 问题类型概览
    3. 类型一: 求部分 (整体 × 百分比)
    4. 类型二: 求百分比 (部分 ÷ 整体 × 100%)
    5. 类型三: 求整体 (部分 ÷ 百分比)
    6. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TYPE1 = "#3498db"      # 蓝色 - 类型一
        self.COLOR_TYPE2 = "#e74c3c"      # 红色 - 类型二
        self.COLOR_TYPE3 = "#f39c12"      # 橙色 - 类型三
        self.COLOR_HIGHLIGHT = YELLOW     # 黄色 - 高亮
        self.COLOR_FORMULA = "#2ecc71"    # 绿色 - 公式
        self.COLOR_AUXILIARY = GRAY_B     # 灰色 - 辅助
        
        # 执行动画序列
        self.show_opening()
        self.show_overview()
        self.show_type1_find_part()
        self.show_type2_find_percentage()
        self.show_type3_find_whole()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "百分比的三类问题\n你都会做吗？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 三个问号图标
        question_marks = VGroup(*[
            Text("?", font_size=60, color=self.COLOR_HIGHLIGHT)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.8).move_to(UP * 2.5)
        
        for qm in question_marks:
            self.play(FadeIn(qm, scale=0.5), run_time=0.3)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_marks),
            run_time=0.5
        )
    
    def show_overview(self):
        """场景2: 问题类型概览"""
        # 标题
        title = Text(
            "三类基本问题",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个类型卡片
        card1 = self.create_type_card(
            "类型一",
            "求部分",
            "整体 × 百分比",
            self.COLOR_TYPE1,
            UP * 2.5
        )
        
        card2 = self.create_type_card(
            "类型二",
            "求百分比",
            "部分 ÷ 整体 × 100%",
            self.COLOR_TYPE2,
            UP * 0.5
        )
        
        card3 = self.create_type_card(
            "类型三",
            "求整体",
            "部分 ÷ 百分比",
            self.COLOR_TYPE3,
            DOWN * 1.5
        )
        
        # 卡片依次滑入
        for card in [card1, card2, card3]:
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            run_time=0.5
        )
    
    def create_type_card(self, type_num, type_name, formula, color, position):
        """创建类型卡片"""
        # 背景矩形
        bg_rect = RoundedRectangle(
            width=7,
            height=1.2,
            corner_radius=0.15,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=3
        )
        
        # 类型编号
        num_text = Text(
            type_num,
            font="Noto Sans CJK SC",
            font_size=28,
            color=color,
            weight=BOLD
        )
        
        # 类型名称
        name_text = Text(
            type_name,
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        )
        
        # 公式
        formula_text = Text(
            formula,
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        
        # 组合
        content = VGroup(num_text, name_text, formula_text).arrange(RIGHT, buff=0.4)
        card = VGroup(bg_rect, content)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_type1_find_part(self):
        """场景3: 类型一 - 求部分"""
        # 标题
        title = Text(
            "类型一: 求部分",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TYPE1
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "一件衣服200元\n打8折，是多少钱？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 整体矩形 (200元)
        whole_rect = Rectangle(
            width=6,
            height=0.8,
            color=self.COLOR_TYPE1,
            stroke_width=3
        ).move_to(UP * 2.5)
        
        whole_label = Text(
            "200元 (整体)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(whole_rect, UP, buff=0.2)
        
        self.play(Create(whole_rect), run_time=1.0)
        self.play(FadeIn(whole_label), run_time=0.5)
        
        # 部分矩形 (80% = 0.8)
        part_rect = Rectangle(
            width=6 * 0.8,
            height=0.8,
            color=self.COLOR_FORMULA,
            fill_opacity=0.5,
            stroke_width=3
        )
        part_rect.align_to(whole_rect, LEFT)
        part_rect.align_to(whole_rect, DOWN)
        
        part_label = Text(
            "80%",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(part_rect.get_center())
        
        self.play(
            Create(part_rect),
            FadeIn(part_label),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 公式
        formula_parts = [
            Text("整体", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"\times", font_size=36, color=WHITE),
            Text("百分比", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"=", font_size=36, color=WHITE),
            Text("部分", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        ]
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        
        self.play(Write(formula), run_time=1.5)
        self.wait(0.5)
        
        # 具体计算
        calculation = MathTex(
            r"200 \times 80\% = 160",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 答案
        answer_box = RoundedRectangle(
            width=4,
            height=1,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 3.5)
        
        answer = Text(
            "160元",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(answer_box.get_center())
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(whole_rect),
            FadeOut(whole_label),
            FadeOut(part_rect),
            FadeOut(part_label),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(answer_box),
            FadeOut(answer),
            run_time=0.6
        )
    
    def show_type2_find_percentage(self):
        """场景4: 类型二 - 求百分比"""
        # 标题
        title = Text(
            "类型二: 求百分比",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TYPE2
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "班级50人，女生30人\n女生占百分之几？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 整体矩形 (50人)
        whole_rect = Rectangle(
            width=6,
            height=0.8,
            color=self.COLOR_TYPE2,
            stroke_width=3
        ).move_to(UP * 3)
        
        whole_label = Text(
            "50人 (整体)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(whole_rect, UP, buff=0.2)
        
        self.play(Create(whole_rect), FadeIn(whole_label), run_time=1.0)
        
        # 部分矩形 (30人 = 60%)
        part_rect = Rectangle(
            width=6 * 0.6,
            height=0.8,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.5,
            stroke_width=3
        )
        part_rect.align_to(whole_rect, LEFT)
        part_rect.align_to(whole_rect, DOWN)
        
        part_label = Text(
            "30人",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(part_rect.get_center())
        
        self.play(
            Create(part_rect),
            FadeIn(part_label),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 公式
        formula_parts = [
            Text("部分", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"\div", font_size=36, color=WHITE),
            Text("整体", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"\times 100\%", font_size=36, color=WHITE)
        ]
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.3).move_to(UP * 0.8)
        
        self.play(Write(formula), run_time=1.5)
        
        # 计算步骤
        step1 = MathTex(
            r"30 \div 50 \times 100\%",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        step2 = MathTex(
            r"0.6 \times 100\% = 60\%",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.8)
        self.play(TransformMatchingTex(step1, step2), run_time=1.0)
        
        # 答案
        answer_box = RoundedRectangle(
            width=4,
            height=1,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 2.5)
        
        answer = MathTex(
            r"60\%",
            font_size=56,
            color=self.COLOR_HIGHLIGHT
        ).move_to(answer_box.get_center())
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(whole_rect),
            FadeOut(whole_label),
            FadeOut(part_rect),
            FadeOut(part_label),
            FadeOut(formula),
            FadeOut(step2),
            FadeOut(answer_box),
            FadeOut(answer),
            run_time=0.6
        )
    
    def show_type3_find_whole(self):
        """场景5: 类型三 - 求整体"""
        # 标题
        title = Text(
            "类型三: 求整体",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TYPE3
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题
        question = Text(
            "一本书，已读40页\n占全书的25%\n全书多少页？",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.8)
        
        # 部分矩形 (40页, 25%)
        part_rect = Rectangle(
            width=6 * 0.25,
            height=0.8,
            color=self.COLOR_TYPE3,
            fill_opacity=0.5,
            stroke_width=3
        ).move_to(UP * 2.5)
        
        part_label_1 = Text(
            "40页",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(part_rect.get_center())
        
        part_label_2 = MathTex(
            r"25\%",
            font_size=28,
            color=self.COLOR_TYPE3
        ).next_to(part_rect, DOWN, buff=0.2)
        
        self.play(
            Create(part_rect),
            FadeIn(part_label_1),
            run_time=1.0
        )
        self.play(FadeIn(part_label_2), run_time=0.5)
        
        self.wait(0.5)
        
        # 公式
        formula_parts = [
            Text("部分", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"\div", font_size=36, color=WHITE),
            Text("百分比", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"=", font_size=36, color=WHITE),
            Text("整体", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        ]
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.3).move_to(UP * 0.8)
        
        self.play(Write(formula), run_time=1.5)
        
        # 计算
        calculation = MathTex(
            r"40 \div 25\% = 160",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 扩展到整体矩形
        whole_rect = Rectangle(
            width=6,
            height=0.8,
            color=self.COLOR_FORMULA,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(UP * 2.5)
        
        whole_label = Text(
            "160页 (整体)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_FORMULA
        ).next_to(whole_rect, UP, buff=0.2)
        
        self.play(
            ReplacementTransform(part_rect.copy(), whole_rect),
            FadeOut(part_label_1),
            FadeOut(part_label_2),
            run_time=1.2
        )
        self.play(FadeIn(whole_label), run_time=0.5)
        
        # 答案
        answer_box = RoundedRectangle(
            width=4,
            height=1,
            corner_radius=0.2,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.3,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(DOWN * 2.5)
        
        answer = Text(
            "160页",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(answer_box.get_center())
        
        self.play(
            FadeIn(answer_box),
            FadeIn(answer, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(part_rect),
            FadeOut(whole_rect),
            FadeOut(whole_label),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(answer_box),
            FadeOut(answer),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 总结与关注"""
        # 总结标题
        title = Text(
            "掌握三类问题",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三个公式卡片
        card1 = self.create_summary_card(
            "求部分",
            "整体 × 百分比",
            self.COLOR_TYPE1,
            UP * 3.5
        )
        
        card2 = self.create_summary_card(
            "求百分比",
            "部分 ÷ 整体 × 100%",
            self.COLOR_TYPE2,
            UP * 2
        )
        
        card3 = self.create_summary_card(
            "求整体",
            "部分 ÷ 百分比",
            self.COLOR_TYPE3,
            UP * 0.5
        )
        
        cards = VGroup(card1, card2, card3)
        
        self.play(FadeIn(cards, shift=UP * 0.3), run_time=1.0)
        
        # 关键提示
        key_point = Text(
            "关键: 找准'单位1'!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(key_point, scale=1.2), run_time=0.8)
        self.play(
            Flash(key_point, color=self.COLOR_HIGHLIGHT, flash_radius=0.8, num_lines=12),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeOut(self.author_info),
            FadeIn(author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰元素 - 百分号旋转
        decorations = VGroup(*[
            MathTex(r"\%", font_size=40, color=color)
            .move_to(2 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i, color in enumerate([
                self.COLOR_TYPE1, self.COLOR_TYPE2, self.COLOR_TYPE3,
                self.COLOR_TYPE1, self.COLOR_TYPE2, self.COLOR_TYPE3
            ])
        ]).move_to(follow_text.get_center() + DOWN * 1.5)
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI, run_time=2))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(
                title, cards, key_point,
                author_large, author_id, follow_text, decorations
            )),
            run_time=1.0
        )
    
    def create_summary_card(self, name, formula, color, position):
        """创建总结卡片"""
        # 背景
        bg = RoundedRectangle(
            width=7.5,
            height=0.9,
            corner_radius=0.12,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=2
        )
        
        # 名称
        name_text = Text(
            name,
            font="Noto Sans CJK SC",
            font_size=28,
            color=color,
            weight=BOLD
        )
        
        # 公式
        formula_text = Text(
            formula,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 组合
        content = VGroup(name_text, formula_text).arrange(RIGHT, buff=0.5)
        card = VGroup(bg, content)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql percentage_problems.py PercentageProblems  # 快速预览
# manim -qh percentage_problems.py PercentageProblems   # 高质量渲染