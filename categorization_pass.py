"""
Categorization Pass: Extract Q&S and use Gemini to classify into sub-patterns
"""

import json
import re
from typing import Optional
from gemini_utils import call_gemini

CATEGORIZATION_PROMPT = """
You are an expert mathematics educator. Analyze the following questions and solutions.

Your task: Identify and categorize these into DISTINCT SUB-PATTERNS based on:
1. The specific mathematical technique or formula required
2. The problem setup and type of information given
3. The solution approach and steps involved
4. The conceptual understanding needed

IMPORTANT GUIDELINES:
- 3-8 patterns maximum (not too fragmented)
- Pattern names should be DESCRIPTIVE and ACTIONABLE (e.g., "Finding Cost Price from Given Loss" not just "Loss Problems")
- Each pattern must have a UNIQUE solution approach
- Group problems only if they use the SAME technique

Pattern criteria:
- Should differ in HOW problems are solved
- Should differ in what's GIVEN vs what's to be FOUND
- Can be recognized by KEYWORDS and PROBLEM STRUCTURE

Example good patterns:
- "Finding Profit/Loss Percentage from CP and SP"
- "Finding Selling Price Given Cost Price and Profit Percentage"  
- "Finding Cost Price from Loss Percentage and Selling Price"

For EACH question, determine the simplest, most specific pattern that fits.

Return valid JSON ONLY (no explanations):
{{
  "sub_patterns": [
    {{
      "pattern_name": "Descriptive pattern name",
      "description": "Brief description of technique/approach",
      "question_numbers": ["1", "2", "3"]
    }}
  ],
  "question_to_pattern": {{
    "1": "Pattern Name",
    "2": "Pattern Name"
  }}
}}

Questions and Solutions:
{questions_solutions}
"""


def format_for_gemini(questions_solutions: list[dict]) -> str:
    """Format Q&S pairs for Gemini API."""
    formatted = []
    for item in questions_solutions:
        formatted.append(f"""
Q{item['question_number']}: {item.get('question_text', item.get('question', ''))}

Solution: {item['solution'][:500]}...
""")
    return "\n---\n".join(formatted[:20])  # Limit to first 20 to avoid token overflow


def normalize_categorization_response(categorization: dict) -> dict:
    """Coerce Gemini output into the canonical categorization shape."""
    if not isinstance(categorization, dict):
        return {}

    sub_patterns = categorization.get("sub_patterns", [])
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
                    "pattern_name": str(pattern_name),
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

                normalized_patterns.append(
                    {
                        "pattern_name": str(
                            pattern.get("pattern_name", f"Pattern {index}")
                        ),
                        "description": str(pattern.get("description", "")),
                        "question_numbers": [str(q) for q in question_numbers],
                    }
                )
            elif isinstance(pattern, str):
                normalized_patterns.append(
                    {
                        "pattern_name": pattern,
                        "description": "",
                        "question_numbers": [],
                    }
                )

    question_to_pattern = categorization.get("question_to_pattern", {})
    if not isinstance(question_to_pattern, dict):
        question_to_pattern = {}

    derived_question_to_pattern = {}
    for pattern in normalized_patterns:
        for qnum in pattern.get("question_numbers", []):
            derived_question_to_pattern[str(qnum)] = pattern["pattern_name"]

    for qnum, pattern_name in derived_question_to_pattern.items():
        question_to_pattern.setdefault(qnum, pattern_name)

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
