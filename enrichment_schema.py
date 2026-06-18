# enrichment_schema.py

AI_ENRICHMENT_PROPS = {
    #
    # Human-readable content
    #
    "paraphrased_question": {
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
        "type": "STRING",
    },
    "traditional_solution": {
        "type": "STRING",
    },
    "shortcut_solution": {
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
