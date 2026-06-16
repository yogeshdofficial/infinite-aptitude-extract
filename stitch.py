# stitch.py

import re


def normalize_question_number(qnum: str) -> str:
    """
    Normalize question numbers for matching.

    Examples:
        "1."      -> "1"
        "1"       -> "1"
        "Q.1"     -> "q.1"
        "Ex. 4."  -> "ex.4"
    """

    if qnum is None:
        return ""

    qnum = str(qnum).lower().strip()

    # remove spaces
    qnum = re.sub(r"\s+", "", qnum)

    # remove trailing periods
    qnum = qnum.rstrip(".")

    return qnum


def build_answer_map(answer_entries):
    """
    Build:

        normalized_qnum -> answer_dict

    If duplicate answers exist, keep the longest solution.
    """

    answer_map = {}

    for answer in answer_entries:

        key = normalize_question_number(answer["question_number"])

        if key not in answer_map:

            answer_map[key] = answer

        else:

            old_len = len(answer_map[key].get("solution", ""))

            new_len = len(answer.get("solution", ""))

            if new_len > old_len:
                answer_map[key] = answer

    return answer_map


def stitch_answers(questions, answers):
    """
    Inject answer data into exercise questions.

    Returns:
        number of questions updated
    """

    answer_map = build_answer_map(answers)

    stitched = 0

    for question in questions:

        if question["section"] != "exercise":
            continue

        if question["solution"].strip():
            continue

        key = normalize_question_number(question["question_number"])

        if key not in answer_map:
            continue

        answer = answer_map[key]

        question["solution"] = answer.get(
            "solution",
            "",
        )

        if answer.get(
            "correct_option",
            "",
        ):
            question["correct_option"] = answer["correct_option"]

        question["answer_page_numbers"] = answer.get(
            "answer_page_numbers",
            [],
        )

        stitched += 1

    return stitched


def find_duplicate_answers(answer_entries):
    """
    Return duplicate answer numbers.
    """

    counts = {}

    for answer in answer_entries:

        key = normalize_question_number(answer["question_number"])

        counts[key] = (
            counts.get(
                key,
                0,
            )
            + 1
        )

    duplicates = []

    for key, count in counts.items():

        if count > 1:
            duplicates.append(key)

    return duplicates


def find_missing_exercise_questions(questions):
    """
    Return exercise questions whose solutions are empty.
    """

    missing = []

    for question in questions:

        if question["section"] != "exercise":
            continue

        if question["solution"].strip():
            continue

        missing.append(question)

    return missing


def chunk_questions(
    questions,
    batch_size=20,
):
    """
    Split question list into chunks.

    Example:

        83 questions

    →

        20
        20
        20
        20
        3
    """

    for i in range(
        0,
        len(questions),
        batch_size,
    ):

        yield questions[i : i + batch_size]


def dedup_questions(all_questions):
    """
    Remove duplicates caused by overlapping page batches.

    Keeps first occurrence to preserve PDF order.
    """

    seen = set()

    deduped = []

    for q in all_questions:

        key = (
            q["section"],
            normalize_question_number(q["question_number"]),
        )

        if key in seen:
            continue

        seen.add(key)

        deduped.append(q)

    return deduped
