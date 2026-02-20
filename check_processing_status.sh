#!/bin/bash

# Script to check all prompt.md files and determine which ones need processing
PROMPT_FILES=$(find /Users/mx/Desktop/manim_math -name "prompt.md" | sort)
TOTAL_COUNT=0
SKIPPED_COUNT=0
TO_PROCESS_COUNT=0

# Create a temporary file to store the results
RESULTS_FILE="/tmp/prompt_processing_check.txt"
echo "# Prompt.md Processing Status Report" > $RESULTS_FILE
echo "Generated on: $(date)" >> $RESULTS_FILE
echo "" >> $RESULTS_FILE
echo "| Status | File Path | Details |" >> $RESULTS_FILE
echo "|--------|-----------|---------|" >> $RESULTS_FILE

for prompt_file in $PROMPT_FILES; do
    TOTAL_COUNT=$((TOTAL_COUNT + 1))
    
    # Get directory of the prompt file
    dir_path=$(dirname "$prompt_file")
    
    # Check if .mp4 file exists in the same directory
    mp4_exists=false
    for file in "$dir_path"/*.mp4; do
        if [ -e "$file" ]; then
            mp4_exists=true
            break
        fi
    done
    
    # Check if media folder exists in the same directory
    media_folder_exists=false
    if [ -d "$dir_path/media" ]; then
        media_folder_exists=true
    fi
    
    if [ "$mp4_exists" = true ] || [ "$media_folder_exists" = true ]; then
        # Skip this file
        SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        
        if [ "$mp4_exists" = true ] && [ "$media_folder_exists" = true ]; then
            details="Has both .mp4 and media/ folder"
        elif [ "$mp4_exists" = true ]; then
            details="Has .mp4 file"
        else
            details="Has media/ folder"
        fi
        
        echo "| SKIPPED | $prompt_file | $details |" >> $RESULTS_FILE
    else
        # Need to process this file
        TO_PROCESS_COUNT=$((TO_PROCESS_COUNT + 1))
        echo "| TO PROCESS | $prompt_file | No .mp4 or media/ folder found |" >> $RESULTS_FILE
    fi
done

echo "" >> $RESULTS_FILE
echo "## Summary" >> $RESULTS_FILE
echo "- Total prompt.md files found: $TOTAL_COUNT" >> $RESULTS_FILE
echo "- Files already processed (skipped): $SKIPPED_COUNT" >> $RESULTS_FILE
echo "- Files to process: $TO_PROCESS_COUNT" >> $RESULTS_FILE

echo $RESULTS_FILE