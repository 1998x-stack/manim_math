import os
import json
import shutil
from pathlib import Path

# 原始JSON数据

with open("docs/chuzhong.json", 'r') as f:
    data = json.load(f)

with open("docs/manim.md", 'r') as f:
    template = ''.join(f.readlines())

def create_directory_structure(data):
    """
    根据JSON数据创建嵌套文件夹结构
    """
    # 统计每个章节下的知识点数量，用于生成序号
    chapter_counter = {}
    
    for item in data:
        # 提取数据
        grade = item["年级"]
        semester = item["学期"]
        chapter = item["章节"]
        content = item["内容"]
        knowledge_point = item["知识点"]
        
        # 创建章节标识符
        chapter_key = f"{grade}-{semester}-{chapter}-{content}"
        
        # 为该章节的知识点计数
        if chapter_key not in chapter_counter:
            chapter_counter[chapter_key] = 1
        else:
            chapter_counter[chapter_key] += 1
        
        # 生成序号（3位数）
        sequence_num = str(chapter_counter[chapter_key]).zfill(3)
        
        # 构建路径
        base_path = Path("初中")
        grade_path = base_path / grade
        semester_path = grade_path / semester
        chapter_content_name = f"{chapter}-{content}"
        chapter_path = semester_path / chapter_content_name
        knowledge_folder_name = f"{sequence_num}{knowledge_point}"
        final_path = chapter_path / knowledge_folder_name
        
        # 创建文件夹（如果不存在）
        final_path.mkdir(parents=True, exist_ok=True)
        print(f"创建文件夹: {final_path}")
        
        # 创建文件（如果不存在）
        create_files(final_path, item, sequence_num)
    
    print("\n所有文件夹和文件创建完成！")

def create_files(folder_path, item, sequence_num):
    """
    在指定文件夹中创建文件
    """
    # 1. 创建description.json
    desc_file = folder_path / "description.json"
    if not desc_file.exists():
        with open(desc_file, 'w', encoding='utf-8') as f:
            # 只保存当前知识点的JSON
            json.dump(item, f, ensure_ascii=False, indent=2)
        print(f"  创建文件: {desc_file}")
        
    
    # 2. 创建prompt.md
    prompt_file = folder_path / "prompt.md"
    if not prompt_file.exists():
        with open(prompt_file, 'w', encoding='utf-8') as f:
            prompt_content = template.replace("$problem$", json.dumps(item, ensure_ascii=False, indent=2))
            f.write(prompt_content)
        print(f"  创建文件: {prompt_file}")
    
    # 2. 创建storybook.md
    story_file = folder_path / "storybook.md"
    if not story_file.exists():
        with open(story_file, 'w', encoding='utf-8') as f:
            # 创建基本的Markdown内容
            story_content = f"""# {item['知识点']}

## 概述
{item['知识点内容详细描述']}

## 数学公式
"""
            # 添加公式
            for formula in item['数学公式']:
                story_content += f"- {formula}\n"
            
            story_content += "\n## 相关知识点\n"
            # 添加相关知识点
            for related in item['相关知识点']:
                story_content += f"- {related}\n"
            
            f.write(story_content)
        print(f"  创建文件: {story_file}")
    
    # 3. 创建Python文件（使用知识点名称作为文件名）
    python_filename = f"{sequence_num}_{item['知识点'].replace(' ', '_')}.py"
    python_file = folder_path / python_filename
    if not python_file.exists():
        with open(python_file, 'w', encoding='utf-8') as f:
            # 创建基本的Manim动画模板
            python_content = f'''from manim import *

class {item['知识点'].replace(' ', '')}Animation(Scene):
    """{item['知识点']}的Manim动画演示"""
    
    def construct(self):
        # 标题
        title = Text("{item['知识点']}", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建基本图形
        circle = Circle(radius=2, color=BLUE)
        circle.shift(LEFT * 3)
        
        # 添加标签
        formula = MathTex("{item['数学公式'][0] if item['数学公式'] else ''}")
        formula.next_to(circle, RIGHT, buff=1)
        
        # 动画序列
        self.play(Create(circle))
        self.play(Write(formula))
        self.wait(2)
        
        # 更多动画元素可以根据需要添加
        # 使用到的Manim元素: {', '.join(item['manim动画涉及元素'])}
        
        self.wait(1)
        
if __name__ == "__main__":
    # 运行命令: manim -pql {python_filename} {item['知识点'].replace(' ', '')}Animation
    pass
'''
            f.write(python_content)
        print(f"  创建文件: {python_file}")

def check_and_clean():
    """
    检查是否已存在结构，并提供清理选项
    """
    base_path = Path("初中")
    if base_path.exists():
        print("检测到已存在的'初中'文件夹。")
        # response = input("是否要清理并重新生成？(y/n): ").lower()
        response = 'n'
        if response == 'y':
            shutil.rmtree(base_path)
            print("已清理旧文件夹。")
        else:
            print("将在现有基础上继续创建（不会覆盖已存在的文件）。")

def main():
    """
    主函数
    """
    print("开始创建文件夹结构...")
    print("=" * 50)
    
    # 检查并清理
    check_and_clean()
    
    # 创建文件夹结构
    create_directory_structure(data)
    
    # 显示最终结构
    print("\n" + "=" * 50)
    print("创建的文件夹结构:")
    print("=" * 50)
    
    def print_tree(path, prefix=""):
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}├── {item.name}/")
                print_tree(item, prefix + "│   ")
            else:
                print(f"{prefix}├── {item.name}")
    
    if Path("初中").exists():
        print_tree(Path("初中"))

if __name__ == "__main__":
    main()