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

Your task is to divide the questions into well-defined groups of similar problems.

══════════════════════════════
GOAL
══════════════════════════════

The purpose of grouping is student learning.

A student should be able to select one group and practice all questions in that group together.

Each group should correspond to ONE lesson or ONE markdown note.

Questions in the same group should:

* use similar ideas,
* use similar formulas,
* follow similar reasoning,
* share common shortcuts,
* share common mistakes,
* share common recognition clues.

Overly broad groups are unacceptable.

If a group contains many different problem setups, split it into smaller groups.

Groups should represent recognizable question families rather than broad chapter themes.

══════════════════════════════
IMPORTANT REQUIREMENTS
══════════════════════════════

* Every question MUST belong to exactly one group.
* No question may remain uncategorized.
* Similar questions MUST always receive exactly the same group name.
* Use stable and consistent names.
* Avoid duplicate names.
* Use concise names (prefer 1-4 words).
* Balance specificity and generality.
* Questions in the same group should be teachable with a single markdown note.
* Avoid overly broad groups.
* Avoid unnecessary tiny groups.
* More groups are acceptable if they represent genuinely different problem types.
* The number of groups should emerge naturally.

══════════════════════════════
GROUPS SHOULD DIFFER BY
══════════════════════════════

1. Typical problem setup.
2. Information given.
3. Quantity to be found.
4. Keywords appearing in the question.
5. The reasoning process.
6. Shortcuts used.
7. Common mistakes.
8. Special cases.
9. Whether a student would benefit from a separate explanation.

══════════════════════════════
IMPORTANT
══════════════════════════════

Avoid creating groups that simply correspond to the chapter itself.

For example, in a Partnership chapter:

BAD:

* Partnership Problems
* Basic Partnership

GOOD:

* Equal Investment
* Different Durations
* Missing Investment
* Missing Time
* Joining Later
* Leaving Early
* Working Partner
* Salary + Share
* Admission of Partner
* Retirement of Partner
* Mixed Cases

Similarly, in Profit and Loss:

BAD:

* Profit Problems

GOOD:

* Find SP
* Find CP
* Profit %
* Loss %
* Marked Price
* Successive Change
* False Weight
* Alligation

The groups should be useful for revision and practice.

══════════════════════════════
GROUP NAMES
══════════════════════════════

Group names should be:

* concise,
* memorable,
* easy for students to recognize,
* suitable as markdown filenames.

Prefer names with 1-4 words.

GOOD EXAMPLES

* Find SP
* Find CP
* Profit %
* Loss %
* Successive Change
* False Weight
* Marked Price
* Alligation
* Mixture
* Relative Speed
* Replacement
* Partial Work
* Pipes With Leak

BAD EXAMPLES

* Finding Selling Price Given Cost Price and Profit Percentage
* Miscellaneous
* Type 1
* Easy Questions
* Formula Based Problems

══════════════════════════════
QUALITY CHECK
══════════════════════════════

Before returning the answer, verify:

* Every question is assigned to exactly one group.
* Similar questions share the same group name.
* No group is excessively broad.
* No group contains unrelated question families.
* Each group could realistically be explained by one markdown note.
* A student could select a group and study that topic independently.

══════════════════════════════
RETURN FORMAT
══════════════════════════════

Return ONLY valid JSON.

{{
"groups": [
{{
"name": "",
"description": "",
"question_numbers": []
}}
],
"question_to_group": {{
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
        categorization.get("sub_patterns") or categorization.get("groups") or []
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
                    pattern.get("subpattern_name")
                    or pattern.get("pattern_name")
                    or f"Subpattern {index}"
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
