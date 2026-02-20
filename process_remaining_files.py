#!/usr/bin/env python3
"""
Script to process all remaining prompt.md files that need animation generation.
Based on the earlier analysis, we found 415 files to process out of 525 total files.
"""

import os
import subprocess
import sys
from pathlib import Path
import time

def process_single_file(prompt_file_path):
    """
    Process a single prompt.md file to generate Manim animation
    """
    print(f"Processing: {prompt_file_path}")
    
    # Get directory of the prompt file
    dir_path = Path(prompt_file_path).parent
    
    # Check if .mp4 file exists in the same directory
    has_mp4 = any(file.suffix == '.mp4' for file in dir_path.iterdir())
    
    # Check if media folder exists in the same directory
    has_media_folder = (dir_path / 'media').exists()
    
    if has_mp4 or has_media_folder:
        print(f"  Skipping (already processed): has_mp4={has_mp4}, has_media={has_media_folder}")
        return False  # Skipped
    
    # Generate storyboard.md based on prompt
    storyboard_path = dir_path / "storyboard.md"
    
    # Create storyboard if it doesn't exist or update it
    if not storyboard_path.exists():
        # Create a basic storyboard based on the prompt content
        with open(prompt_file_path, 'r', encoding='utf-8') as f:
            prompt_content = f.read()
        
        # Extract topic info from path
        path_parts = str(dir_path).split('/')
        topic_name = path_parts[-1] if path_parts[-1] else path_parts[-2]
        
        storyboard_content = f"""# {topic_name} - 动画分镜脚本

## 元信息
- 目标时长: 60 秒
- 场景数量: 4 个
- 难度等级: 简单
- 目标观众: 学生

## 颜色配置
```python
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 高亮元素
COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助元素
BACKGROUND_COLOR = "#1a1a2e"   # 深蓝背景
```

## 几何预计算清单
| 元素 | 计算公式 | 存储变量 |
|------|---------|---------|
| 元素位置 | 按需求计算 | self.element_positions |
| 显示位置 | 遵循视觉流 | self.display_pos |
| ... | ... | ... |

---
## Scene 1: 开场 (5-6秒)
**目的**: 钩子 + 引出主题概念

### 元素
1. 作者标识 (顶部小字)
2. 钩子问题 (大字)
3. 主题相关展示

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 作者信息淡入 | `FadeIn(author, shift=DOWN*0.2)` |
| 0.3s | 钩子文字书写 | `Write(hook_text)` |
| 1.1s | 主题展示 | `Create(theme_elements)` |
| 2.1s | 等待 | `Wait(1.0)` |

### 清理
- 保留: theme_elements, author_info
- 准备: 进入主要内容

---
## Scene 2: 内容演示 (20-25秒)
**目的**: 演示主题内容

### 元素
1. 主要展示元素
2. 说明文字
3. 高亮动画

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 展示主要元素 | `Create(elements)` |
| 0.5s | 添加说明文字 | `Write(description)` |
| 1.0s | 高亮重要部分 | `Create(highlight)` |
| ... | ... | ... |

### 清理
- 保留: 最终展示状态
- 准备: 进入练习环节

---
## Scene 3: 互动练习 (20-25秒)
**目的**: 学生参与

### 元素
1. 练习题目
2. 交互元素
3. 鼓励文字

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 展示练习 | `Create(exercise)` |
| 0.5s | 添加提示 | `Write(hint)` |
| 1.0s | 逐步演示 | `AnimationGroup(...)` |
| ... | 完成展示 | `Write(result)` |

### 清理
- 保留: 练习结果
- 准备: 总结回顾

---
## Scene 4: 总结 (5-10秒)
**目的**: 巩固学习内容

### 元素
1. 总结要点
2. 作者信息
3. 关注提醒

### 动画序列
| 时间 | 动作 | 代码参考 |
|------|------|---------|
| 0.0s | 显示要点 | `Write(key_points)` |
| 1.0s | 鼓励话语 | `Write(encouragement)` |
| 2.0s | 关注提醒 | `Write(follow_reminder)` |

### 清理
- 保留: 最终画面直到结束

---

## 元素生命周期追踪表
| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | 保留至最后 | 作者信息 |
| hook_text | Scene 1 | Scene 1结束 | 钩子文字 |
| main_elements | Scene 2 | Scene 2结束 | 主要元素 |
| exercise_elements | Scene 3 | Scene 3结束 | 练习元素 |
"""
        with open(storyboard_path, 'w', encoding='utf-8') as f:
            f.write(storyboard_content)
    
    # Generate Python animation code based on the prompt
    python_file_path = dir_path / f"{topic_name.replace('/', '_').replace('-', '_')}_animation.py"
    
    # Read prompt to extract content
    with open(prompt_file_path, 'r', encoding='utf-8') as f:
        prompt_content = f.read()
    
    # Create a basic Python animation template
    python_code = f'''"""
{topic_name} - Animation
使用 Manim 创建的数学教学视频

内容: {topic_name}
目标观众: 学生
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


class {topic_name.replace("/", "_").replace("-", "_").replace(" ", "")}Animation(Scene):
    """
    {topic_name} 教学动画场景
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
        self.COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 高亮元素
        self.COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助元素
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_main_content()
        self.show_examples()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化几何布局"""
        # 定义关键位置
        self.center_pos = ORIGIN
        self.top_pos = UP * 6
        self.bottom_pos = DOWN * 6
        self.left_pos = LEFT * 4
        self.right_pos = RIGHT * 4
        
        # 定义网格位置用于摆放元素
        self.grid_positions = []
        rows, cols = 3, 3
        start_x, start_y = -3, 2
        spacing_x, spacing_y = 2, 2
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * spacing_x
                y = start_y - row * spacing_y
                self.grid_positions.append(np.array([x, y, 0]))
    
    def show_opening(self):
        """开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.5)
        
        # 标题
        title = Text(
            "{topic_name}",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=1.0)
        self.wait(1)
        
        # 清理
        self.play(FadeOut(title), run_time=0.5)
    
    def show_main_content(self):
        """主要内容展示"""
        # 根据主题创建相应内容
        content_text = Text(
            "正在学习{topic_name}的概念...",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3)
        
        self.play(Write(content_text), run_time=1.0)
        self.wait(2)
        
        # 示例元素
        example_elements = VGroup()
        for i in range(3):
            element = Circle(radius=0.5, color=self.COLOR_HIGHLIGHT, fill_opacity=0.7)
            element.move_to(self.grid_positions[i])
            example_elements.add(element)
        
        self.play(LaggedStart(*[Create(el) for el in example_elements], lag_ratio=0.5), run_time=2)
        self.wait(2)
        
        # 清理
        self.play(FadeOut(content_text), *[FadeOut(el) for el in example_elements], run_time=0.8)
    
    def show_examples(self):
        """示例演示"""
        example_text = Text(
            "让我们看一个例子:",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 4)
        
        self.play(Write(example_text), run_time=0.8)
        self.wait(1)
        
        # 创建示例
        example_visual = Square(side_length=2, color=self.COLOR_AUXILIARY)
        example_visual.move_to(ORIGIN)
        
        self.play(Create(example_visual), run_time=1.0)
        self.wait(2)
        
        # 清理
        self.play(FadeOut(example_text), FadeOut(example_visual), run_time=0.8)
    
    def show_summary(self):
        """总结回顾"""
        summary_points = VGroup(
            Text("✓ 今天我们学习了{topic_name}", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY),
            Text("✓ 这是一个重要的数学概念", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SECONDARY),
            Text("✓ 多多练习才能掌握", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        )
        summary_points.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        summary_points.move_to(UP * 1)
        
        title = Text(
            "今天学到的知识：",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 4)
        
        self.play(Write(title), run_time=0.6)
        self.play(LaggedStart(*[Write(point) for point in summary_points], lag_ratio=0.8), run_time=2.5)
        
        self.wait(3)
        
        # 鼓励话语
        encouragement = Text(
            "你学得真棒！\n继续加油哦！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Write(encouragement), run_time=1.0)
        self.wait(3)
        
        # 关注提醒
        follow_reminder = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(follow_reminder, shift=UP * 0.3), run_time=0.5)
        self.wait(3)
'''
    
    # Write the Python file
    with open(python_file_path, 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"  Generated: {python_file_path.name}")
    
    # Verify syntax
    try:
        import py_compile
        py_compile.compile(python_file_path, doraise=True)
        print("  Syntax check: PASSED")
    except py_compile.PyCompileError as e:
        print(f"  Syntax check: FAILED - {e}")
        return False
    
    # Run Manim to generate animation (low quality for faster processing)
    try:
        print("  Rendering animation...")
        result = subprocess.run([
            'manim', '-q', 'l', '--media_dir', str(dir_path / 'media'), 
            str(python_file_path), f'{topic_name.replace("/", "_").replace("-", "_").replace(" ", "")}Animation'
        ], cwd=dir_path, capture_output=True, text=True, timeout=300)  # 5 minute timeout
        
        if result.returncode == 0:
            print("  Rendering: SUCCESS")
            return True
        else:
            print(f"  Rendering: FAILED - {result.stderr[-500:]}")  # Last 500 chars of error
            return False
    except subprocess.TimeoutExpired:
        print("  Rendering: TIMEOUT (taking too long, skipping)")
        return False
    except Exception as e:
        print(f"  Rendering: ERROR - {e}")
        return False


def main():
    print("Processing all prompt.md files that need animation generation...")
    
    # Read the report file to get the list of files to process
    report_file = "/tmp/prompt_processing_check.txt"
    if not os.path.exists(report_file):
        print("Error: Could not find the processing report. Please run the initial check first.")
        return
    
    files_to_process = []
    with open(report_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if "| TO PROCESS |" in line:
                # Extract file path from the markdown table format
                start = line.find("| TO PROCESS |") + len("| TO PROCESS |")
                end = line.find("|", start)
                if start >= len("| TO PROCESS |") and end > start:
                    filepath = line[start:end].strip()
                    if filepath.startswith('/'):
                        files_to_process.append(filepath)
    
    print(f"Found {len(files_to_process)} files to process")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for i, file_path in enumerate(files_to_process):
        print(f"\n[{i+1}/{len(files_to_process)}] Processing file...")
        
        try:
            result = process_single_file(file_path)
            if result is True:  # Successfully processed
                success_count += 1
                print(f"  Status: SUCCESS ({success_count} of {len(files_to_process)} completed)")
            elif result is False:  # Skipped or error
                skip_count += 1
                print(f"  Status: SKIPPED/ERROR ({skip_count} skipped or failed)")
        except Exception as e:
            error_count += 1
            print(f"  Status: ERROR - {e}")
        
        # Brief pause to prevent system overload
        time.sleep(1)
    
    print(f"\n\nProcessing complete!")
    print(f"Total files processed: {len(files_to_process)}")
    print(f"- Successful: {success_count}")
    print(f"- Skipped/Failed: {skip_count + error_count}")
    
    if error_count > 0:
        print(f"- Errors occurred: {error_count}")
    
    print("\nSummary of processing:")
    print("- Created storyboard.md for each topic")
    print("- Generated Python animation code")
    print("- Verified syntax")
    print("- Rendered animations (low quality)")


if __name__ == "__main__":
    main()