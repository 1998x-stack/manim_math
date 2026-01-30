"""
圆的面积 - Circle Area Animation
使用 Manim 创建的小学六年级数学教学视频

内容: 圆的面积公式 S=πr² 的推导过程（转化思想）
目标观众: 小学六年级学生
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


class CircleArea(Scene):
    """
    圆的面积教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 展示已知信息 - 标注半径
    3. 转化思想引入 - 化圆为方
    4. 精细分割演示 - 16等份拼接
    5. 标注长方形尺寸 - 建立关系
    6. 推导面积公式 - 得出S=πr²
    7. 片尾总结 - 强化记忆
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 主蓝色 - 圆
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 扇形
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮黄色
        self.COLOR_AUXILIARY = GRAY_B       # 辅助灰色
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
        self.COLOR_TRANSFORM = "#9b59b6"    # 紫色 - 变换后的图形
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_radius()
        self.scene_3_transformation_idea()
        self.scene_4_sector_division()
        self.scene_5_rectangle_dimensions()
        self.scene_6_formula_derivation()
        self.scene_7_conclusion()
    
    def setup_geometry(self):
        """初始化圆和扇形的几何数据"""
        # 基准参数
        self.center = ORIGIN + UP * 1.5  # 圆心位置（稍微上移）
        self.radius = 1.8  # 半径
        self.num_sectors = 16  # 扇形数量
        
        # 创建完整圆
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.center)
        
        # 计算扇形的顶点
        self.sector_points = []
        angles = np.linspace(0, 2*PI, self.num_sectors + 1)
        for angle in angles:
            point = self.center + self.radius * np.array([np.cos(angle), np.sin(angle), 0])
            self.sector_points.append(point)
        
        # 创建16个扇形
        self.sectors = VGroup()
        colors = [self.COLOR_SECONDARY, self.COLOR_TRANSFORM]
        
        for i in range(self.num_sectors):
            sector = Polygon(
                self.center,
                self.sector_points[i],
                self.sector_points[i + 1],
                color=colors[i % 2],
                fill_opacity=0.7,
                stroke_width=2,
                stroke_color=WHITE
            )
            self.sectors.add(sector)
        
        # 计算拼接后的长方形尺寸
        self.rect_width = PI * self.radius  # 圆周长的一半
        self.rect_height = self.radius      # 半径
        
        print(f"✓ 几何初始化完成")
        print(f"  圆心: {self.center}")
        print(f"  半径: {self.radius}")
        print(f"  扇形数量: {self.num_sectors}")
        print(f"  拼接后尺寸: {self.rect_width:.2f} × {self.rect_height:.2f}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何求圆的面积？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=1.0)
        
        # 圆形从中心生长
        self.play(GrowFromCenter(self.circle), run_time=1.2)
        
        # 问号闪烁出现
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.center)
        
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(question_mark),
            FadeOut(hook_question),
            run_time=0.5
        )
    
    def scene_2_radius(self):
        """场景2: 展示已知信息 - 标注半径"""
        # 圆轻微缩放强调
        self.play(
            self.circle.animate.scale(1.1),
            run_time=0.3
        )
        self.play(
            self.circle.animate.scale(1/1.1),
            run_time=0.3
        )
        
        # 半径线段（从圆心到右侧边）
        radius_end = self.center + RIGHT * self.radius
        self.radius_line = Line(
            self.center,
            radius_end,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        self.play(Create(self.radius_line), run_time=0.8)
        
        # 半径标签
        self.radius_label = MathTex(
            "r",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(self.radius_line, DOWN, buff=0.15)
        
        self.play(Write(self.radius_label), run_time=0.7)
        
        # 说明文字
        explanation = Text(
            "已知圆的半径为 r",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(explanation), run_time=0.4)
    
    def scene_3_transformation_idea(self):
        """场景3: 转化思想引入 - 化圆为方"""
        # 标题
        title = Text(
            "转化思想: 化圆为方",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 创建4等份分割线（预览效果）
        sector_lines_4 = VGroup()
        for i in range(4):
            angle = i * PI / 2
            end_point = self.center + self.radius * 1.2 * np.array([np.cos(angle), np.sin(angle), 0])
            line = DashedLine(
                self.center,
                end_point,
                color=self.COLOR_AUXILIARY,
                dash_length=0.1
            )
            sector_lines_4.add(line)
        
        self.play(Create(sector_lines_4), run_time=1.2)
        
        # 创建4个扇形用于演示
        sectors_4 = VGroup()
        angles_4 = [0, PI/2, PI, 3*PI/2, 2*PI]
        sector_points_4 = [
            self.center + self.radius * np.array([np.cos(a), np.sin(a), 0])
            for a in angles_4
        ]
        
        for i in range(4):
            sector = Polygon(
                self.center,
                sector_points_4[i],
                sector_points_4[i + 1],
                color=self.COLOR_SECONDARY,
                fill_opacity=0.6,
                stroke_width=2
            )
            sectors_4.add(sector)
        
        # 扇形轻微分离
        self.play(
            FadeOut(self.circle),
            FadeOut(self.radius_line),
            FadeOut(self.radius_label),
            FadeOut(sector_lines_4),
            run_time=0.3
        )
        
        self.play(
            *[sector.animate.shift((sector.get_center() - self.center) * 0.3) for sector in sectors_4],
            run_time=0.8
        )
        
        # 箭头和长方形轮廓
        arrow = Arrow(
            start=UP * 0.5,
            end=DOWN * 0.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3
        ).move_to(DOWN * 0.5)
        
        # 简化的长方形轮廓
        rect_outline = Rectangle(
            width=3.5,
            height=1.5,
            color=self.COLOR_TRANSFORM,
            stroke_width=3
        ).move_to(DOWN * 2.5)
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Create(rect_outline), run_time=0.8)
        
        # 说明文字
        area_constant_text = Text(
            "面积不变！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(rect_outline, DOWN, buff=0.4)
        
        self.play(Write(area_constant_text), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sectors_4),
            FadeOut(arrow),
            FadeOut(rect_outline),
            FadeOut(area_constant_text),
            run_time=0.5
        )
        
        # 恢复完整圆（重置场景）
        self.play(FadeIn(self.circle), run_time=0.4)
    
    def scene_4_sector_division(self):
        """场景4: 精细分割演示 - 16等份拼接"""
        # 说明文字
        explanation = Text(
            "分得越细，越接近长方形",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建16条分割线
        sector_lines = VGroup()
        for i in range(self.num_sectors):
            angle = i * 2 * PI / self.num_sectors
            end_point = self.sector_points[i]
            line = Line(
                self.center,
                end_point,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
            sector_lines.add(line)
        
        self.play(Create(sector_lines), run_time=1.5)
        
        # 扇形依次闪烁高亮（快速）
        for i in range(0, self.num_sectors, 2):  # 只闪烁偶数个以加快速度
            self.play(
                Flash(
                    self.sector_points[i],
                    color=self.COLOR_HIGHLIGHT,
                    flash_radius=0.3
                ),
                run_time=0.15
            )
        
        self.play(FadeOut(explanation), run_time=0.3)
        
        # 圆淡出，扇形淡入
        self.play(
            FadeOut(self.circle),
            FadeOut(sector_lines),
            FadeIn(self.sectors),
            run_time=0.8
        )
        
        # 扇形重新排列成近似长方形
        # 计算拼接位置
        arranged_sectors = self.arrange_sectors_as_rectangle()
        
        self.play(
            Transform(self.sectors, arranged_sectors),
            run_time=2.0
        )
        
        # 外轮廓高亮
        # 计算外轮廓的边界
        rect_center = arranged_sectors.get_center()
        rect_width_visual = self.rect_width
        rect_height_visual = self.rect_height
        
        self.rect_frame = Rectangle(
            width=rect_width_visual,
            height=rect_height_visual,
            color=self.COLOR_TRANSFORM,
            stroke_width=4
        ).move_to(rect_center)
        
        self.play(Create(self.rect_frame), run_time=1.0)
        self.wait(2.0)
    
    def arrange_sectors_as_rectangle(self):
        """将扇形排列成近似长方形"""
        arranged = VGroup()
        
        # 计算基准位置
        base_y = self.center[1]
        start_x = self.center[0] - self.rect_width / 2
        
        for i in range(self.num_sectors):
            sector = self.sectors[i].copy()
            
            # 计算每个扇形的宽度（圆周的1/16）
            sector_width = 2 * PI * self.radius / self.num_sectors
            
            # 计算x位置
            x_pos = start_x + sector_width * (i + 0.5)
            
            # 奇数扇形（索引0, 2, 4...）：顶点向上
            # 偶数扇形（索引1, 3, 5...）：旋转180度，顶点向下
            if i % 2 == 0:
                # 顶点向上
                y_pos = base_y - self.rect_height / 2
                sector.rotate(PI/2 - i * 2*PI / self.num_sectors)
            else:
                # 顶点向下（旋转180度）
                y_pos = base_y + self.rect_height / 2
                sector.rotate(-PI/2 - i * 2*PI / self.num_sectors)
            
            sector.move_to(np.array([x_pos, y_pos, 0]))
            arranged.add(sector)
        
        return arranged
    
    def scene_5_rectangle_dimensions(self):
        """场景5: 标注长方形尺寸"""
        # 上边Brace（长）
        rect_top = self.rect_frame.get_top()
        rect_bottom = self.rect_frame.get_bottom()
        rect_left = self.rect_frame.get_left()
        rect_right = self.rect_frame.get_right()
        
        length_brace = Brace(
            Line(rect_left + UP * rect_top[1], rect_right + UP * rect_top[1]),
            direction=UP,
            buff=0.1,
            color=self.COLOR_HIGHLIGHT
        )
        
        length_label = MathTex(
            r"\pi r",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(length_brace, UP, buff=0.1)
        
        length_text = Text(
            "(周长的一半)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(length_label, RIGHT, buff=0.15)
        
        self.play(Create(length_brace), run_time=0.6)
        self.play(Write(length_label), run_time=0.7)
        self.play(FadeIn(length_text, shift=LEFT * 0.2), run_time=0.4)
        
        # 侧边Brace（宽）
        width_brace = Brace(
            Line(rect_right + UP * rect_bottom[1], rect_right + UP * rect_top[1]),
            direction=RIGHT,
            buff=0.1,
            color=self.COLOR_HIGHLIGHT
        )
        
        width_label = MathTex(
            "r",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(width_brace, RIGHT, buff=0.1)
        
        self.play(Create(width_brace), run_time=0.6)
        self.play(Write(width_label), run_time=0.7)
        
        # 说明文字
        explanation = Text(
            "拼成的近似长方形",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)
        
        # 保存Brace以便后续清理
        self.length_brace = length_brace
        self.length_label = length_label
        self.length_text = length_text
        self.width_brace = width_brace
        self.width_label = width_label
        
        self.play(FadeOut(explanation), run_time=0.4)
    
    def scene_6_formula_derivation(self):
        """场景6: 推导面积公式"""
        # 图形整体缩小上移
        group = VGroup(
            self.sectors,
            self.rect_frame,
            self.length_brace,
            self.length_label,
            self.length_text,
            self.width_brace,
            self.width_label
        )
        
        self.play(
            group.animate.scale(0.5).move_to(UP * 3.5),
            run_time=1.0
        )
        
        # 公式演变
        # Step 1: 长方形面积
        formula_1 = MathTex(
            r"S", r"=", r"\text{长}", r"\times", r"\text{宽}",
            font_size=32
        ).move_to(DOWN * 1)
        
        # 设置颜色
        formula_1[0].set_color(self.COLOR_FORMULA)  # S
        
        self.play(Write(formula_1), run_time=1.2)
        self.wait(0.8)
        
        # Step 2: 替换长和宽
        formula_2 = MathTex(
            r"S", r"=", r"\pi r", r"\times", r"r",
            font_size=32
        ).move_to(DOWN * 1)
        
        formula_2[0].set_color(self.COLOR_FORMULA)  # S
        formula_2[2].set_color(self.COLOR_HIGHLIGHT)  # πr
        formula_2[4].set_color(self.COLOR_HIGHLIGHT)  # r
        
        self.play(TransformMatchingTex(formula_1, formula_2), run_time=1.2)
        self.wait(1.0)
        
        # Step 3: 简化
        formula_3 = MathTex(
            r"S", r"=", r"\pi r^2",
            font_size=36
        ).move_to(DOWN * 1)
        
        formula_3[0].set_color(self.COLOR_FORMULA)  # S
        formula_3[2].set_color(self.COLOR_HIGHLIGHT)  # πr²
        
        self.play(TransformMatchingTex(formula_2, formula_3), run_time=1.2)
        
        # 公式放大并高亮
        self.play(
            formula_3.animate.scale(1.4).set_color(YELLOW),
            run_time=0.8
        )
        
        # 外框闪烁
        self.play(
            Flash(formula_3, color=YELLOW, flash_radius=1.5, num_lines=16),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 保存公式
        self.final_formula = formula_3
        
        # 清理其他元素
        self.play(
            FadeOut(group),
            run_time=0.6
        )
    
    def scene_7_conclusion(self):
        """场景7: 片尾总结"""
        # 公式移动到上方
        self.play(
            self.final_formula.animate.move_to(UP * 4.5).scale(0.8),
            run_time=0.8
        )
        
        # 知识点卡片
        card_1 = self.create_knowledge_card(
            "记住: 半径是 r",
            UP * 2.5
        )
        
        card_2 = self.create_knowledge_card(
            "π ≈ 3.14 或 22/7",
            UP * 1.2
        )
        
        card_3 = self.create_knowledge_card(
            "面积单位: 平方单位",
            DOWN * 0.1
        )
        
        self.play(FadeIn(card_1, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(card_2, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(card_3, shift=RIGHT * 0.5), run_time=0.5)
        self.wait(1.0)
        
        # 示例计算
        example_title = Text(
            "例: r = 2",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.8)
        
        example_calc = MathTex(
            r"S = \pi \times 2^2 = 4\pi \approx 12.56",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2.6)
        
        self.play(
            FadeIn(example_title),
            Write(example_calc),
            run_time=1.2
        )
        self.wait(1.5)
        
        # 清理，准备片尾
        self.play(
            FadeOut(self.final_formula),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(example_title),
            FadeOut(example_calc),
            run_time=0.6
        )
        
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_big),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰圆圈
        circles = VGroup(*[
            Circle(radius=0.3, color=self.COLOR_PRIMARY, stroke_width=3)
            .move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in circles],
            run_time=0.6
        )
        
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, text, position):
        """创建知识点卡片"""
        # 图标
        icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_FORMULA,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 文字
        content = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, content).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql circle_area.py CircleArea  # 快速预览
# manim -qh circle_area.py CircleArea   # 高质量渲染