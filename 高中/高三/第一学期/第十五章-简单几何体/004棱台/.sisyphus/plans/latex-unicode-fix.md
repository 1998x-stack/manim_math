# Fix LaTeX Unicode Character Error in Frustum Lesson

## TL;DR

> **Quick Summary**: Replace Chinese characters in MathTeX expressions that cause LaTeX compilation errors
> 
> **Deliverables**: Fixed frustum_lesson.py with English equivalents in MathTeX
> - Line 501: V_{大} → V_{big}
> - Line 509: V_{小} → V_{small} 
> - Line 525: V_{大} - V_{小} → V_{big} - V_{small}
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: NO - sequential
> **Critical Path**: Single file edit

---

## Context

### Original Request
Fix the LaTeX compilation error caused by Unicode characters (Chinese characters) in MathTeX expressions in the frustum lesson.

### Issue Analysis
The error occurs because LaTeX doesn't natively support Unicode characters like Chinese characters. The problematic lines are in the `scene_5_volume()` method where Chinese characters "大" (meaning "big") and "小" (meaning "small") are used in MathTeX expressions.

### Research Findings
- Found 6 total occurrences of Chinese characters in the file
- Only 3 of these occur in MathTeX expressions (lines 501, 509, 525) and need to be fixed
- The other 3 occurrences are in regular text strings and are fine

---

## Work Objectives

### Core Objective
Replace Unicode characters in MathTeX expressions with English equivalents to fix LaTeX compilation error.

### Concrete Deliverables
- Fixed `frustum_lesson.py` file with English replacements for MathTeX expressions

### Definition of Done
- [ ] LaTeX compiles successfully without Unicode errors
- [ ] MathTeX expressions use English equivalents instead of Chinese characters
- [ ] Visual meaning remains unchanged

### Must Have
- All MathTeX expressions with Chinese characters converted to English
- LaTeX compilation succeeds

### Must NOT Have (Guardrails)
- No remaining Unicode characters in MathTeX expressions
- No change to non-MathTeX text strings

---

## Verification Strategy (MANDATORY)

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: None
- **Framework**: None

### QA Policy
Every task MUST include agent-executed QA scenarios (see TODO template below).
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Backend/Code**: Use Bash (python syntax check, basic import test)

---

## Execution Strategy

### Parallel Execution Waves

Sequential execution required - single file edit across specific lines.

```
Wave 1 (Start Immediately — single task):
├── Task 1: Replace Unicode characters in MathTeX expressions [quick]

Critical Path: Task 1
Parallel Speedup: N/A
Max Concurrent: 1
```

### Dependency Matrix
- **1**: — — (no dependencies)

### Agent Dispatch Summary
- **1**: **1** — T1 → `quick`

---

## TODOs

> Implementation + Test = ONE Task. Never separate.
> EVERY task MUST have: Recommended Agent Profile + Parallelization info + QA Scenarios.
> **A task WITHOUT QA Scenarios is INCOMPLETE. No exceptions.**

- [ ] 1. Replace Unicode Characters in MathTeX Expressions

  **What to do**:
  - Replace "V_{大}" with "V_{big}" in line 501
  - Replace "V_{小}" with "V_{small}" in line 509
  - Replace "V_{大} - V_{小}" with "V_{big} - V_{small}" in line 525
  - Keep all other functionality identical

  **Must NOT do**:
  - Change text strings containing Chinese characters (lines 299, 310, 463) - these are OK in regular text
  - Modify any other parts of the code unnecessarily

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: Simple text replacement in specific lines
  - **Skills**: []
    - No special skills needed for this task
  - **Skills Evaluated but Omitted**:
    - `playwright`: Not a browser automation task
    - `git-master`: Not a git operation task

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential
  - **Blocks**: None
  - **Blocked By**: None (can start immediately)

  **References** (CRITICAL - Be Exhaustive):

  **Pattern References** (existing code to follow):
  - `frustum_lesson.py:500-530` - Current MathTex expressions with Chinese characters

  **API/Type References** (contracts to implement against):
  - Manim MathTex class - requires valid LaTeX syntax

  **Test References** (testing patterns to follow):
  - None - manual verification of LaTeX compilation

  **External References** (libraries and frameworks):
  - Official docs: `https://docs.manim.community/` - Manim MathTex usage

  **WHY Each Reference Matters** (explain the relevance):
  - Lines 500-530 show the current problematic code that needs to be modified
  
  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY — task is INCOMPLETE without these):**

  ```
  Scenario: LaTeX compilation succeeds after replacement
    Tool: Bash (python)
    Preconditions: Modified frustum_lesson.py file exists
    Steps:
      1. Try to import the modified file to check for Python syntax errors
      2. Verify MathTex expressions are valid LaTeX after character replacement
    Expected Result: Python import succeeds without syntax errors
    Failure Indicators: Python syntax errors or import failures
    Evidence: .sisyphus/evidence/task-1-latex-compilation-success.txt

  Scenario: MathTex expressions use English equivalents
    Tool: Bash (grep)
    Preconditions: Modified frustum_lesson.py file exists
    Steps:
      1. Search for "V_{大}" in the file
      2. Search for "V_{小}" in the file
      3. Verify these have been replaced with "V_{big}" and "V_{small}"
    Expected Result: No occurrences of "V_{大}" or "V_{小}" remain in MathTex expressions
    Evidence: .sisyphus/evidence/task-1-unicode-check.txt
  ```

  **Evidence to Capture**:
  - [ ] Each evidence file named: task-{N}-{scenario-slug}.{ext}
  - [ ] Python import test result
  - [ ] Verification that Chinese characters are removed from MathTeX

  **Commit**: YES
  - Message: `fix(latex): replace Unicode characters in MathTeX expressions`
  - Files: `frustum_lesson.py`
  - Pre-commit: `python -m py_compile frustum_lesson.py`

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 1 review agent runs. Must approve. Rejection → fix → re-run.

- [ ] F1. **Code Quality Review** — `quick`
  Check the modified file for: valid Python syntax, proper LaTeX in MathTex expressions, no remaining Unicode characters in MathTeX. Verify the changes maintain mathematical meaning.
  Output: `Python syntax [PASS/FAIL] | LaTeX validity [PASS/FAIL] | Unicode check [PASS/FAIL] | VERDICT`

---

## Commit Strategy

- **1**: `fix(latex): replace Unicode characters in MathTeX expressions` — frustum_lesson.py, python -m py_compile frustum_lesson.py

---

## Success Criteria

### Verification Commands
```bash
python -m py_compile frustum_lesson.py  # Expected: no errors
grep -n "V_{大}\|V_{小}" frustum_lesson.py  # Expected: no matches in MathTeX
```

### Final Checklist
- [ ] All MathTeX expressions use English equivalents instead of Chinese characters
- [ ] LaTeX compilation succeeds
- [ ] Code maintains original meaning and functionality