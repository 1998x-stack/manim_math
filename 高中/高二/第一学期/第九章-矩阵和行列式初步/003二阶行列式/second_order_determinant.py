"""
二阶行列式 - Second Order Determinant
使用 Manim 创建的高中数学教学视频

内容: 二阶行列式的定义、对角线法则、计算示例、性质
目标观众: 高二学生
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


class SecondOrderDeterminant(Scene):
    """
    二阶行列式教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 行列式定义
    3. 主对角线
    4. 副对角线
    5. 完整公式
    6. 计算示例
    7. 应用场景
    8. 重要性质
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 行列式
        self.COLOR_MAIN_DIAG = "#e74c3c"    # 红色 - 主对角线
        self.COLOR_ANTI_DIAG = "#2ecc71"    # 绿色 - 副对角线
        self.COLOR_RESULT = "#f39c12"       # 橙色 - 结果
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化全局元素
        self.setup_globals()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_main_diagonal()
        self.show_anti_diagonal()
        self.show_complete_formula()
        self.show_example()
        self.show_applications()
        self.show_properties()
    
    def setup_globals(self):
        """初始化全局配置和常驻元素"""
        # 作者信息 (持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.add(self.author_info)
        
        # 标准位置
        self.DET_CENTER = UP * 2.5
        self.TITLE_POS = UP * 6
        self.EXPLAIN_POS = DOWN * 4.5
    
    def create_determinant_visual(self, entries_list, font_size=32):
        """
        创建带竖线的行列式视觉表示
        entries_list: [[a, b], [c, d]]
        """
        # 创建矩阵内容
        matrix = Matrix(
            entries_list,
            element_to_mobject_config={"font_size": font_size},
            h_buff=1.0,
            v_buff=0.8
        )
        
        # 创建竖线（行列式符号）
        left_bar = Line(
            matrix.get_corner(UL) + LEFT * 0.15,
            matrix.get_corner(DL) + LEFT * 0.15,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        right_bar = Line(
            matrix.get_corner(UR) + RIGHT * 0.15,
            matrix.get_corner(DR) + RIGHT * 0.15,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        determinant = VGroup(left_bar, matrix, right_bar)
        return determinant
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 钩子问题
        hook = Text(
            "四个数能算出一个数?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.3)
        
        # 2×2 数表
        matrix_only = Matrix(
            [["a", "b"], ["c", "d"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
            h_buff=1.0,
            v_buff=0.8
        ).move_to(UP * 2)
        
        matrix_only.set_color(WHITE)
        
        self.play(Create(matrix_only), run_time=1.0)
        self.wait(0.5)
        
        # 变换为行列式
        determinant = self.create_determinant_visual([["a", "b"], ["c", "d"]])
        determinant.move_to(UP * 2)
        
        self.play(Transform(matrix_only, determinant), run_time=0.8)
        self.wait(0.3)
        
        # 过渡文字
        transition = Text(
            "行列式来揭秘!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(matrix_only),
            FadeOut(transition),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 行列式定义"""
        # 标题
        title = Text(
            "二阶行列式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 行列式
        determinant = self.create_determinant_visual([["a", "b"], ["c", "d"]])
        determinant.move_to(self.DET_CENTER)
        
        self.play(Create(determinant), run_time=1.2)
        
        # 定义说明
        definition = Text(
            "2×2数表按规则计算的数值",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(definition), run_time=0.6)
        self.wait(0.5)
        
        # 符号说明
        symbol_note = Text(
            "竖线 | | 表示行列式",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(symbol_note), run_time=0.5)
        self.wait(1.5)  # 延长等待
        
        # 保存行列式用于后续场景
        self.determinant = determinant
        
        # 清理说明文字，保留行列式
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(symbol_note),
            run_time=0.5
        )
    
    def show_main_diagonal(self):
        """场景3: 主对角线"""
        # 标题
        title = Text(
            "主对角线 \\",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_MAIN_DIAG
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.6)
        
        # 获取矩阵元素
        matrix = self.determinant[1]  # 中间的 Matrix 对象
        entries = matrix.get_entries()
        
        a = entries[0]  # 左上
        d = entries[3]  # 右下
        
        # 绘制主对角线
        main_diag = Line(
            start=a.get_center(),
            end=d.get_center(),
            color=self.COLOR_MAIN_DIAG,
            stroke_width=6
        )
        
        self.play(Create(main_diag), run_time=1.0)
        
        # 高亮元素
        self.play(
            Indicate(a, color=self.COLOR_MAIN_DIAG, scale_factor=1.3),
            Indicate(d, color=self.COLOR_MAIN_DIAG, scale_factor=1.3),
            run_time=0.8
        )
        
        # 显示乘积
        product_main = MathTex(
            "a \\times d",
            font_size=28,
            color=self.COLOR_MAIN_DIAG
        ).move_to(DOWN * 1)
        
        self.play(Write(product_main), run_time=0.8)
        
        # 简化显示
        product_main_simple = MathTex(
            "ad",
            font_size=32,
            color=self.COLOR_MAIN_DIAG
        ).move_to(DOWN * 1)
        
        self.play(Transform(product_main, product_main_simple), run_time=0.6)
        self.wait(1.5)  # 延长等待
        
        # 保存用于后续
        self.main_diag = main_diag
        self.product_main = product_main
        
        # 清理
        self.play(FadeOut(title), run_time=0.3)
    
    def show_anti_diagonal(self):
        """场景4: 副对角线"""
        # 标题
        title = Text(
            "副对角线 /",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ANTI_DIAG
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.6)
        
        # 获取矩阵元素
        matrix = self.determinant[1]
        entries = matrix.get_entries()
        
        b = entries[1]  # 右上
        c = entries[2]  # 左下
        
        # 绘制副对角线
        anti_diag = Line(
            start=b.get_center(),
            end=c.get_center(),
            color=self.COLOR_ANTI_DIAG,
            stroke_width=6
        )
        
        self.play(Create(anti_diag), run_time=1.0)
        
        # 高亮元素
        self.play(
            Indicate(b, color=self.COLOR_ANTI_DIAG, scale_factor=1.3),
            Indicate(c, color=self.COLOR_ANTI_DIAG, scale_factor=1.3),
            run_time=0.8
        )
        
        # 显示乘积
        product_anti = MathTex(
            "b \\times c",
            font_size=28,
            color=self.COLOR_ANTI_DIAG
        ).move_to(DOWN * 2)
        
        self.play(Write(product_anti), run_time=0.8)
        
        # 简化显示
        product_anti_simple = MathTex(
            "bc",
            font_size=32,
            color=self.COLOR_ANTI_DIAG
        ).move_to(DOWN * 2)
        
        self.play(Transform(product_anti, product_anti_simple), run_time=0.6)
        self.wait(1.5)  # 延长等待
        
        # 保存用于后续
        self.anti_diag = anti_diag
        self.product_anti = product_anti
        
        # 清理
        self.play(FadeOut(title), run_time=0.3)
    
    def show_complete_formula(self):
        """场景5: 完整公式"""
        # 标题
        title = Text(
            "对角线法则",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 移动两个乘积到一起
        self.play(
            self.product_main.animate.move_to(DOWN * 1 + LEFT * 1.5),
            self.product_anti.animate.move_to(DOWN * 1 + RIGHT * 1.5),
            run_time=0.8
        )
        
        # 减号
        minus = MathTex("-", font_size=40, color=WHITE).move_to(DOWN * 1)
        self.play(Write(minus), run_time=0.4)
        
        # 完整公式
        formula = MathTex(
            r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}",
            "=",
            "ad",
            "-",
            "bc",
            font_size=32
        ).move_to(DOWN * 3)
        
        formula[0].set_color(self.COLOR_PRIMARY)
        formula[2].set_color(self.COLOR_MAIN_DIAG)
        formula[4].set_color(self.COLOR_ANTI_DIAG)
        
        self.play(Write(formula), run_time=1.5)
        self.wait(0.8)
        
        # 记忆提示
        hint = Text(
            "记忆口诀: 主减副",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, scale=1.1), run_time=0.6)
        self.wait(2.0)  # 延长等待，强调记忆口诀
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.determinant),
            FadeOut(self.main_diag),
            FadeOut(self.anti_diag),
            FadeOut(self.product_main),
            FadeOut(self.product_anti),
            FadeOut(minus),
            FadeOut(formula),
            FadeOut(hint),
            run_time=0.6
        )
    
    def show_example(self):
        """场景6: 计算示例"""
        # 标题
        title = Text(
            "计算示例",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.6)
        
        # 数值行列式
        det_example = self.create_determinant_visual([["3", "2"], ["1", "4"]], font_size=36)
        det_example.move_to(UP * 3.5)
        
        self.play(Create(det_example), run_time=1.0)
        
        # 获取元素位置
        matrix = det_example[1]
        entries = matrix.get_entries()
        
        # 主对角线计算
        main_calc = MathTex(
            "3 \\times 4 = 12",
            font_size=28,
            color=self.COLOR_MAIN_DIAG
        ).move_to(UP * 1.5)
        
        # 绘制主对角线
        main_line = Line(
            entries[0].get_center(),
            entries[3].get_center(),
            color=self.COLOR_MAIN_DIAG,
            stroke_width=5
        )
        
        self.play(Create(main_line), run_time=0.6)
        self.play(Write(main_calc), run_time=0.8)
        self.wait(0.5)
        
        # 副对角线计算
        anti_calc = MathTex(
            "2 \\times 1 = 2",
            font_size=28,
            color=self.COLOR_ANTI_DIAG
        ).move_to(UP * 0.5)
        
        # 绘制副对角线
        anti_line = Line(
            entries[1].get_center(),
            entries[2].get_center(),
            color=self.COLOR_ANTI_DIAG,
            stroke_width=5
        )
        
        self.play(Create(anti_line), run_time=0.6)
        self.play(Write(anti_calc), run_time=0.8)
        self.wait(0.5)
        
        # 减法
        subtraction = MathTex(
            "12 - 2",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(subtraction), run_time=0.7)
        self.wait(0.5)
        
        # 结果
        result = MathTex(
            "= 10",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 1.5)
        
        self.play(Write(result), run_time=0.8)
        
        # 完整等式
        complete = MathTex(
            r"\begin{vmatrix} 3 & 2 \\ 1 & 4 \end{vmatrix} = 10",
            font_size=32,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 3)
        
        self.play(Write(complete), run_time=1.0)
        self.wait(2.0)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(det_example),
            FadeOut(main_line),
            FadeOut(anti_line),
            FadeOut(main_calc),
            FadeOut(anti_calc),
            FadeOut(subtraction),
            FadeOut(result),
            FadeOut(complete),
            run_time=0.6
        )
    
    def show_applications(self):
        """场景7: 应用场景"""
        # 标题
        title = Text(
            "行列式的应用",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 三个应用
        app1 = VGroup(
            Text("① 解方程组", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("(克拉默法则)", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.2).move_to(UP * 2.5)
        
        app2 = VGroup(
            Text("② 判断向量平行", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            MathTex(r"\begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} = 0", font_size=22)
        ).arrange(DOWN, buff=0.2).move_to(UP * 0.5)
        
        app3 = VGroup(
            Text("③ 计算面积", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("(平行四边形)", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.5)
        
        applications = VGroup(app1, app2, app3)
        
        for app in applications:
            self.play(FadeIn(app, shift=RIGHT * 0.3), run_time=0.8)
            self.wait(0.6)
        
        # 提示
        hint = Text(
            "后续课程详细讲解",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1.8)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(applications),
            FadeOut(hint),
            run_time=0.6
        )
    
    def show_properties(self):
        """场景8: 重要性质"""
        # 标题
        title = Text(
            "重要性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 性质1: 转置
        prop1_title = Text(
            "性质1: 转置值不变",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.5)
        
        prop1_formula = MathTex(
            r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}",
            "=",
            r"\begin{vmatrix} a & c \\ b & d \end{vmatrix}",
            font_size=26
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(prop1_title, shift=UP * 0.2), run_time=0.6)
        self.play(Write(prop1_formula), run_time=1.0)
        self.wait(0.8)
        
        # 性质2: 交换行变号
        prop2_title = Text(
            "性质2: 交换行变号",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 1)
        
        prop2_formula = MathTex(
            r"\begin{vmatrix} c & d \\ a & b \end{vmatrix}",
            "= -",
            r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}",
            font_size=26
        ).move_to(ORIGIN)
        
        self.play(FadeIn(prop2_title, shift=UP * 0.2), run_time=0.6)
        self.play(Write(prop2_formula), run_time=1.0)
        self.wait(0.8)
        
        # 性质3: 数乘提取
        prop3_title = Text(
            "性质3: 数乘可提取",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        prop3_formula = MathTex(
            r"\begin{vmatrix} ka & kb \\ c & d \end{vmatrix}",
            "= k",
            r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}",
            font_size=26
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(prop3_title, shift=UP * 0.2), run_time=0.6)
        self.play(Write(prop3_formula), run_time=1.0)
        self.wait(1.0)
        
        # 总结
        summary = Text(
            "掌握这些性质, 计算更轻松!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary, scale=1.1), run_time=0.6)
        self.wait(0.8)
        
        # 清理部分内容，准备片尾
        self.play(
            FadeOut(title),
            FadeOut(prop1_title),
            FadeOut(prop1_formula),
            FadeOut(prop2_title),
            FadeOut(prop2_formula),
            FadeOut(prop3_title),
            FadeOut(prop3_formula),
            FadeOut(summary),
            run_time=0.6
        )
        
        # 片尾关注
        outro = Text(
            "关注我, 学更多行列式知识!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_RESULT
        ).move_to(UP * 1)
        
        self.play(FadeIn(outro, shift=UP * 0.3), run_time=0.6)
        
        # 装饰元素
        decorations = VGroup(*[
            Line(ORIGIN, RIGHT * 0.3, color=GOLD, stroke_width=3)
            .rotate(i * PI / 4)
            .move_to(outro.get_center() + 1.8 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
            for i in range(8)
        ])
        
        self.play(
            *[Create(deco) for deco in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI / 2, run_time=1.0))
        
        self.wait(2.0)  # 延长片尾等待
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql second_order_determinant.py SecondOrderDeterminant  # 快速预览
# manim -qh second_order_determinant.py SecondOrderDeterminant   # 高质量 1080p
# manim -qk second_order_determinant.py SecondOrderDeterminant   # 4K质量