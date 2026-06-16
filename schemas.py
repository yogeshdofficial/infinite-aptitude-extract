# schemas.py

QUESTION_PROPS = {
    "section": {
        "type": "STRING",
        "enum": ["solved_example", "exercise"],
    },
    "question_number": {"type": "STRING"},
    "exam_reference": {"type": "STRING"},
    "passage_text": {"type": "STRING"},
    "question_text": {"type": "STRING"},
    "is_mcq": {"type": "BOOLEAN"},
    "is_data_sufficiency": {"type": "BOOLEAN"},
    "option_a": {"type": "STRING"},
    "option_b": {"type": "STRING"},
    "option_c": {"type": "STRING"},
    "option_d": {"type": "STRING"},
    "option_e": {"type": "STRING"},
    "correct_option": {"type": "STRING"},
    "solution": {"type": "STRING"},
    "page_numbers": {"type": "ARRAY", "items": {"type": "STRING"}},
    # page(s) where answer came from
    "answer_page_numbers": {"type": "ARRAY", "items": {"type": "STRING"}},
}

RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "chapter_title": {"type": "STRING"},
        "questions": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": QUESTION_PROPS,
                "required": list(QUESTION_PROPS.keys()),
            },
        },
    },
    "required": ["chapter_title", "questions"],
}


ANSWER_PROPS = {
    "question_number": {"type": "STRING"},
    "correct_option": {"type": "STRING"},
    "solution": {"type": "STRING"},
    "answer_page_numbers": {"type": "ARRAY", "items": {"type": "STRING"}},
}

ANSWER_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "answers": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": ANSWER_PROPS,
                "required": list(ANSWER_PROPS.keys()),
            },
        }
    },
    "required": ["answers"],
}
