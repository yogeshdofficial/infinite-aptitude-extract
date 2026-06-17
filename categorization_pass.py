"""
Categorization Pass: Extract Q&S and use Gemini to classify into sub-patterns
"""

import json
import re
from typing import Optional
from gemini_utils import call_gemini

CATEGORIZATION_PROMPT = """
You are an expert mathematics educator, curriculum designer, and competitive exam trainer.

You are given ALL questions and solutions from ONE chapter.

Your task is to discover PATTERNS that are genuinely useful for students.

══════════════════════════════
GOAL
══════════════════════════════

The purpose of these patterns is student learning.

Students should be able to select one pattern and study all questions belonging to that pattern together.

Each pattern should correspond to ONE lesson or ONE markdown note.

A pattern represents:

* one recognition process,
* one mental model,
* one solving framework,
* one set of shortcuts,
* one family of common mistakes.

Patterns should reflect how students naturally organize problems in their minds.

══════════════════════════════
MOST IMPORTANT RULE
══════════════════════════════

Imagine you are writing a textbook or preparing coaching lectures.

If two sets of questions would normally be taught in different lectures, they MUST belong to different patterns.

Even if they use the same formula, separate them if they have different recognition clues or different solving frameworks.

Do not optimize for the minimum number of patterns.

Optimize for how a human teacher would divide the chapter into lessons.

══════════════════════════════
DO NOT GROUP ONLY BY FORMULAS
══════════════════════════════

Many questions may use the same underlying formula.

This does NOT mean they belong to the same pattern.

For example, in Partnership, many questions use:

Profit ∝ Capital × Time

However, students study these separately:

* Simple Partnership
* Different Time Periods
* Capital Changes
* Additional Investment
* Withdrawal Cases
* Working Partner
* Salary + Share
* Mixed Distribution
* Find Capital
* Find Time
* Rent Sharing
* Equivalent Units
* Multiple Time Phases

Using the same formula alone is NOT sufficient reason to merge patterns.

══════════════════════════════
WHAT DEFINES A PATTERN
══════════════════════════════

Patterns should differ by:

1. Recognition clues.
2. Keywords appearing in the question.
3. Information given.
4. Quantity to be found.
5. Typical question structure.
6. Solving framework.
7. Intermediate variables introduced.
8. Shortcuts used.
9. Common mistakes.
10. Whether students would benefit from a separate lesson.

══════════════════════════════
IMPORTANT REQUIREMENTS
══════════════════════════════

* Every question MUST belong to exactly one pattern.
* No question may remain uncategorized.
* Similar questions MUST always receive exactly the same pattern name.
* Use stable and consistent names.
* Avoid duplicate names.
* Prefer creating too many patterns rather than too few.
* More patterns are acceptable if they represent genuinely different solving frameworks.
* Overly broad patterns are unacceptable.
* Catch-all patterns are unacceptable.

══════════════════════════════
AVOID CATCH-ALL PATTERNS
══════════════════════════════

The following are unacceptable:

* Complex Problems
* Advanced Problems
* Miscellaneous
* Mixed Problems
* Formula Problems
* Difficult Problems
* Type 1
* Type 2
* Chapter Name

These names do not explain WHY the questions belong together.

Pattern names should describe the underlying idea or solving framework.

══════════════════════════════
GOOD PATTERN NAMES
══════════════════════════════

Examples:

Simple Partnership
Different Time Periods
Capital Changes
Additional Investment
Withdrawal Cases
Working Partner
Salary + Share
Mixed Distribution
Find Capital
Find Time
Rent Sharing
Equivalent Units
Multiple Time Phases

Find SP
Find CP
Profit Percentage
Loss Percentage
Marked Price
Successive Change
False Weight

Combined Work
Efficiency Ratio
Pipes With Leak
Men-Women-Children
Work And Wages

══════════════════════════════
BAD PATTERN NAMES
══════════════════════════════

* Partnership Problems
* Profit Problems
* Complex Profit Sharing
* Basic Problems
* Easy Questions
* Formula Based Problems
* Miscellaneous

══════════════════════════════
INTERNAL REASONING PROCESS
══════════════════════════════

Think deeply and perform the following steps internally before producing the final JSON.

STEP 1

For each question, identify:

* recognition clues,
* keywords,
* information given,
* quantity to be found,
* formulas involved,
* mental model,
* solving framework,
* shortcuts,
* common mistakes.

STEP 2

Discover candidate question families.

Questions belong to the same family if they share:

* recognition process,
* mental model,
* solving framework,
* shortcuts,
* common mistakes.

Imagine that one teacher could explain all questions in that family in one lecture.

STEP 3

Split overly broad families.

If a family contains multiple recognition processes or multiple solving frameworks, split it.

Prefer too many patterns rather than too few.

STEP 4

Merge overly narrow families.

Merge only if:

* recognition clues are similar,
* solving framework is the same,
* shortcuts are the same,
* and students would naturally revise them together.

STEP 5

Simulate a student.

Ask:

"If I were revising this chapter, would I naturally want to practice these questions together?"

If yes, group them together.

If no, separate them.

STEP 6

Simulate a teacher.

Ask:

"Would I teach these questions in one lecture or separate lectures?"

Questions taught in separate lectures should belong to different patterns.

STEP 7

Perform a final quality check.

══════════════════════════════
QUALITY CHECK
══════════════════════════════

Verify:

* every question belongs to exactly one pattern,
* no question remains uncategorized,
* similar questions receive identical pattern names,
* no pattern is based on difficulty,
* no pattern is a catch-all bucket,
* no pattern is excessively broad,
* each pattern has one recognition process,
* each pattern has one solving framework,
* each pattern could realistically be explained by one markdown note,
* students would naturally revise the questions in that pattern together.

Only after completing these steps should you return the final JSON.

══════════════════════════════
GROUP NAME RULES
══════════════════════════════

Use concise names.

Prefer 2-5 words.

Names should be:

* memorable,
* descriptive,
* suitable as markdown filenames,
* useful for revision.

══════════════════════════════
RETURN FORMAT
══════════════════════════════

Return ONLY valid JSON.

{{
"patterns": [
{{
"pattern_name": "",
"description": "",
"question_numbers": []
}}
],
"question_to_pattern": {{
"1": "",
"2": ""
}}
}}

Questions and solutions:

{questions_solutions}
"""


def format_for_gemini(questions_solutions: list[dict]) -> str:
    """Format Q&S pairs for Gemini API."""
    formatted = []
    for item in questions_solutions:
        formatted.append(f"""
Q{item['question_number']}: {item.get('question_text', item.get('question', ''))}

Solution: {item['solution']}...
""")
    return "\n---\n".join(formatted)  # Limit to first 20 to avoid token overflow


def normalize_categorization_response(categorization: dict) -> dict:
    """Coerce Gemini output into the canonical categorization shape."""
    if not isinstance(categorization, dict):
        return {}

    # sub_patterns = categorization.get("sub_patterns", [])
    sub_patterns = (
        categorization.get("patterns")
        or categorization.get("sub_patterns")
        or categorization.get("groups")
        or []
    )
    normalized_patterns = []

    if isinstance(sub_patterns, dict):
        for pattern_name, question_numbers in sub_patterns.items():
            if isinstance(question_numbers, list):
                normalized_question_numbers = [str(q) for q in question_numbers]
            elif question_numbers is None:
                normalized_question_numbers = []
            else:
                normalized_question_numbers = [str(question_numbers)]

            normalized_patterns.append(
                {
                    "subpattern_name": str(pattern_name),
                    "description": "",
                    "question_numbers": normalized_question_numbers,
                }
            )
    elif isinstance(sub_patterns, list):
        for index, pattern in enumerate(sub_patterns, 1):
            if isinstance(pattern, dict):
                question_numbers = pattern.get("question_numbers", [])
                if isinstance(question_numbers, str):
                    question_numbers = [question_numbers]
                elif not isinstance(question_numbers, list):
                    question_numbers = []

                name = (
                    pattern.get("pattern_name")
                    or pattern.get("name")
                    or pattern.get("subpattern_name")
                    or f"Pattern {index}"
                )

                normalized_patterns.append(
                    {
                        "subpattern_name": str(name),
                        "description": str(pattern.get("description", "")),
                        "question_numbers": [str(q) for q in question_numbers],
                    }
                )
            elif isinstance(pattern, str):
                normalized_patterns.append(
                    {
                        "subpattern_name": pattern,
                        "description": "",
                        "question_numbers": [],
                    }
                )

    # question_to_pattern = categorization.get("question_to_pattern", {})
    question_to_pattern = (
        categorization.get("question_to_pattern")
        or categorization.get("question_to_group")
        or {}
    )
    if not isinstance(question_to_pattern, dict):
        question_to_pattern = {}

    derived_question_to_pattern = {}

    for pattern in normalized_patterns:
        for qnum in pattern.get("question_numbers", []):
            derived_question_to_pattern[str(qnum)] = pattern["subpattern_name"]
    for qnum, pattern_name in derived_question_to_pattern.items():
        question_to_pattern.setdefault(qnum, pattern_name)
    for pattern in normalized_patterns:
        pattern["pattern_name"] = pattern["subpattern_name"]
    categorization["sub_patterns"] = normalized_patterns
    categorization["question_to_pattern"] = {
        str(question_number): str(pattern_name)
        for question_number, pattern_name in question_to_pattern.items()
    }

    return categorization


def categorize_with_gemini(questions_solutions: list[dict]) -> Optional[dict]:
    """Send Q&S to Gemini for categorization."""
    formatted = format_for_gemini(questions_solutions)
    prompt = CATEGORIZATION_PROMPT.format(questions_solutions=formatted)

    response = call_gemini(prompt)

    # Parse JSON from response
    try:
        json_match = re.search(r"\{.*\}", response, re.DOTALL)
        if json_match:
            categorization = json.loads(json_match.group())
            print(json.dumps(categorization, indent=2))
            return normalize_categorization_response(categorization)
    except json.JSONDecodeError as e:
        print(f"Failed to parse Gemini response: {e}")
        print(f"Response: {response}")

    return None


def add_subpatterns_to_json(
    input_file: str, output_file: str, categorization: dict
) -> None:
    """Add sub_pattern field to original JSON file."""
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    question_to_pattern = categorization.get("question_to_pattern", {})

    questions = data.get("questions", []) if isinstance(data, dict) else data

    for item in questions:
        q_num = str(item["question_number"])
        pattern = question_to_pattern.get(q_num, "Uncategorized")
        item["sub_pattern"] = pattern

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
