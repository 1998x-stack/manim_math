#!/bin/bash
count=0
for dir in $(find 初中/ 高中/ -name "prompt.md" -exec dirname {} \; | sort); do
  if [ ! "$(ls "$dir"/*.mp4 2>/dev/null)" ]; then
    total_lines=0
    for py_file in "$dir"/*.py; do
      if [ -f "$py_file" ]; then
        lines=$(wc -l < "$py_file")
        total_lines=$((total_lines + lines))
      fi
    done
    if [ $total_lines -le 200 ]; then
      if [ $total_lines -eq 0 ]; then
        echo "$dir (no Python files)"
      else
        echo "$dir (total $total_lines lines)"
      fi
      ((count++))
    fi
  fi
done
echo "Total directories with Python files <= 200 lines or no Python files: $count"