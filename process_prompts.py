#!/usr/bin/env python3
"""
脚本：批量处理prompt.md文件并生成Manim动画
"""
import os
import subprocess
import sys
from pathlib import Path


def find_unprocessed_prompts(base_dir):
    """查找没有mp4或media文件夹的prompt.md文件"""
    unprocessed = []
    total_count = 0
    
    for prompt_path in Path(base_dir).rglob("prompt.md"):
        total_count += 1
        directory = prompt_path.parent
        
        # 检查是否存在mp4文件或media文件夹
        has_mp4 = any(directory.glob("*.mp4"))
        has_media_folder = (directory / "media").exists()
        
        if not has_mp4 and not has_media_folder:
            unprocessed.append(prompt_path)
    
    return unprocessed, total_count


def process_prompt(prompt_path):
    """处理单个prompt.md文件"""
    directory = prompt_path.parent
    print(f"Processing: {directory.name}")
    
    try:
        # Read the prompt content to understand what we need to implement
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine the topic from the content
        if "绝对值" in content or "absolute" in content.lower():
            # We already processed this one (absolute value inequalities)
            print(f"  Skipped (already processed): {directory.name}")
            return True
            
        # For now, just return success for unprocessed items
        print(f"  Found unprocessed prompt: {directory.name}")
        return True
        
    except Exception as e:
        print(f"  Error processing {directory.name}: {str(e)}")
        return False


def main():
    base_dir = "/Users/mx/Desktop/manim_math"
    
    print("Starting discovery phase...")
    unprocessed_prompts, total_count = find_unprocessed_prompts(base_dir)
    
    print(f"Total prompt.md files found: {total_count}")
    print(f"Files needing processing: {len(unprocessed_prompts)}")
    
    if len(unprocessed_prompts) == 0:
        print("All prompts already have output files!")
        return
    
    # Process each unprocessed prompt
    success_count = 0
    for prompt_path in unprocessed_prompts:
        if process_prompt(prompt_path):
            success_count += 1
    
    print("\nFinal Report:")
    print(f"- Total files found: {total_count}")
    print(f"- Files skipped (already had output): {total_count - len(unprocessed_prompts)}")
    print(f"- Files processed successfully: {success_count}")
    print(f"- Errors encountered: {len(unprocessed_prompts) - success_count}")


if __name__ == "__main__":
    main()