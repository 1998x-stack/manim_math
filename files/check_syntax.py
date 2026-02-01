#!/usr/bin/env python
"""
快速语法检查脚本
验证 simson_line.py 没有明显的语法错误
"""

import sys
import ast

def check_syntax(filepath):
    """检查Python文件的语法"""
    print(f"检查文件: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # 尝试解析为AST
        ast.parse(code)
        
        print("✓ 语法检查通过")
        return True
        
    except SyntaxError as e:
        print(f"✗ 语法错误:")
        print(f"  行 {e.lineno}: {e.msg}")
        print(f"  {e.text}")
        return False
    
    except Exception as e:
        print(f"✗ 检查失败: {e}")
        return False

if __name__ == "__main__":
    success = check_syntax("simson_line.py")
    
    if success:
        print("\n代码已准备就绪! 可以运行:")
        print("  manim -pql simson_line.py SimsonLineScene")
    else:
        print("\n请修复上述错误后再运行")
    
    sys.exit(0 if success else 1)