# enrichment_schema.py
#
# Schema for Pass 3 ("enrichment"). Pass 3 no longer invents a new
# question with new numbers. It takes the ORIGINAL question and
# ORIGINAL solution extracted from the textbook (Pass 1/2) and:
#
#   1. reproduces them exactly, cleanly formatted in LaTeX/Markdown
#      (paraphrased_question / traditional_solution carry the ORIGINAL
#       numbers — field names kept for backward compatibility with
#       sqlite.py, documentation_pass.py, the Android app, etc.)
#   2. adds a fully detailed, no-assumptions explanation of the
#      official/book method (still traditional_solution)
#   3. adds a separate shortcut/trick method (shortcut_solution)
#   4. adds classification + study metadata (concepts, formulas,
#      prerequisites, hints, common mistakes, related patterns)
#
# Field names are intentionally unchanged from the old paraphrasing
# pipeline so every downstream consumer (sqlite.py, documentation_pass.py,
# cache_utils.py, the Android app's SQLite repository) keeps working
# without modification.

AI_ENRICHMENT_PROPS = {
    #
    # Human-readable content — ORIGINAL question/answer, reformatted
    #
    "paraphrased_question": {
        # Despite the legacy name, this is the ORIGINAL question text,
        # cleanly reformatted with proper LaTeX/Markdown. Numbers,
        # context, and wording must match the source PDF exactly.
        "type": "STRING",
    },
    "paraphrased_option_a": {
        "type": "STRING",
    },
    "paraphrased_option_b": {
        "type": "STRING",
    },
    "paraphrased_option_c": {
        "type": "STRING",
    },
    "paraphrased_option_d": {
        "type": "STRING",
    },
    "paraphrased_correct_option": {
        "type": "STRING",
    },
    "paraphrased_final_answer": {
        # The ORIGINAL book answer, in clean LaTeX.
        "type": "STRING",
    },
    "traditional_solution": {
        # The book's method, fully detailed, no assumptions, original
        # numbers, with a plain-English WHY for every non-arithmetic step.
        "type": "STRING",
    },
    "shortcut_solution": {
        # A genuine shortcut / trick method, same original numbers,
        # same final answer, formatted the same way as traditional_solution.
        "type": "STRING",
    },
    #
    # Classification
    #
    "chapter": {
        "type": "STRING",
    },
    "difficulty": {
        "type": "STRING",
        "enum": [
            "easy",
            "medium",
            "hard",
        ],
    },
    #
    # Knowledge graph
    #
    "concepts": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    "prerequisites": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    "formulas_used": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    #
    # Learning aids
    #
    "hints": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    "common_mistakes": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    "related_patterns": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
    "confusing_patterns": {
        "type": "ARRAY",
        "items": {
            "type": "STRING",
        },
    },
}


ENRICHMENT_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "ai_enrichment": {
            "type": "OBJECT",
            "properties": AI_ENRICHMENT_PROPS,
            "required": list(AI_ENRICHMENT_PROPS.keys()),
        },
    },
    "required": [
        "ai_enrichment",
    ],
}
