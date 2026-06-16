import re
from collections import Counter

from stitch import normalize_question_number


def find_duplicate_questions(questions):

    keys = []

    for q in questions:

        key = (q["section"], normalize_question_number(q["question_number"]))

        keys.append(key)

    counts = Counter(keys)

    duplicates = []

    for key, count in counts.items():

        if count > 1:
            duplicates.append(key)

    return duplicates


def find_missing_solutions(questions):

    missing = []

    for q in questions:

        if q["section"] != "exercise":
            continue

        if q["solution"].strip():
            continue

        missing.append(q["question_number"])

    return missing


def validate_page_numbers(
    questions,
    total_pages,
):

    errors = []

    for q in questions:

        pages = q.get("page_numbers", [])

        for p in pages:

            try:

                page = int(p)

            except Exception:

                errors.append((q["question_number"], p))

                continue

            if page < 1 or page > total_pages:

                errors.append((q["question_number"], p))

    return errors


def validate_answer_page_numbers(
    questions,
    total_pages,
):

    errors = []

    for q in questions:

        pages = q.get("answer_page_numbers", [])

        for p in pages:

            try:

                page = int(p)

            except Exception:

                errors.append((q["question_number"], p))

                continue

            if page < 1 or page > total_pages:

                errors.append((q["question_number"], p))

    return errors


def natural_key(text):

    return tuple(
        int(x) if x.isdigit() else x for x in re.split(r"(\d+)", text.lower()) if x
    )


def validate_order(questions):

    errors = []

    previous = None

    for q in questions:

        key = (q["section"], natural_key(q["question_number"]))

        if previous is not None:

            if key < previous:

                errors.append(q["question_number"])

        previous = key

    return errors


def suspicious_solutions(
    questions,
    min_chars=5,
):

    suspicious = []

    for q in questions:

        if q["section"] != "exercise":
            continue

        solution = q["solution"].strip()

        if solution and len(solution) < min_chars:

            suspicious.append(q["question_number"])

    return suspicious


def validate_all(
    questions,
    total_pages,
):

    report = {
        "duplicate_questions": find_duplicate_questions(questions),
        "missing_solutions": find_missing_solutions(questions),
        "bad_question_pages": validate_page_numbers(questions, total_pages),
        "bad_answer_pages": validate_answer_page_numbers(questions, total_pages),
        "order_errors": validate_order(questions),
        "suspicious_solutions": suspicious_solutions(questions),
    }

    return report
