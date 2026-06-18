# cache_utils.py

import json
from pathlib import Path


def ensure_output_dir(output_dir):
    """
    Create output directory if needed.
    """

    output_dir = Path(output_dir)

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    return output_dir


def save_json(data, output_path):

    output_path = Path(output_path)

    tmp_path = output_path.with_suffix(".tmp")

    with open(
        tmp_path,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2,
        )

    tmp_path.replace(output_path)


def load_json(path):
    """
    Load JSON file.
    """

    path = Path(path)

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:

        return json.load(f)


def cache_batch(
    chapter_title,
    questions,
    output_path,
):
    """
    Save intermediate state.
    """

    data = {
        "chapter_title": chapter_title,
        "question_count": len(questions),
        "questions": questions,
    }

    save_json(
        data,
        output_path,
    )


def cache_final(
    chapter_title,
    source_file,
    total_pages,
    questions,
    output_path,
):

    data = {
        "source_file": source_file,
        "chapter_title": chapter_title,
        "total_pages": total_pages,
        "question_count": len(questions),
        "questions": questions,
    }

    save_json(
        data,
        output_path,
    )


def load_existing_questions(
    output_path,
):
    """
    Return previously saved questions.

    Empty list if file doesn't exist.
    """

    output_path = Path(output_path)

    if not output_path.exists():
        return []

    data = load_json(output_path)

    return data.get(
        "questions",
        [],
    )


def save_batch_progress(
    progress_path,
    completed_batches,
):
    progress = {
        "completed_batches": completed_batches,
        "last_batch": completed_batches[-1] if completed_batches else 0,
    }

    save_json(
        progress,
        progress_path,
    )


def load_batch_progress(
    progress_path,
):

    progress_path = Path(progress_path)

    if not progress_path.exists():

        return {
            "completed_batches": [],
            "last_batch": 0,
        }

    return load_json(
        progress_path,
    )


def export_flattened_ai_enrichment(source_path):
    """Write a flattened ai_enrichment export next to the source chapter JSON."""
    source_path = Path(source_path)
    if not source_path.exists():
        return

    data = load_json(source_path)
    chapter_title = data.get("chapter_title", "") if isinstance(data, dict) else ""
    questions = data.get("questions", []) if isinstance(data, dict) else []

    items = []
    for question in questions:
        ai_enrichment = question.get("ai_enrichment", {})
        if not isinstance(ai_enrichment, dict):
            ai_enrichment = {}

        row = {
            "chapter_title": chapter_title,
            "question_number": question.get("question_number", ""),
            "sub_pattern": question.get("sub_pattern", ""),
            "pattern_doc": question.get("pattern_doc", ""),
        }
        row.update(ai_enrichment)
        items.append(row)

    flattened = {
        "chapter_title": chapter_title,
        "question_count": len(items),
        "items": items,
    }

    output_path = source_path.with_name(
        f"{source_path.stem}_ai_enriched_flattened.json"
    )
    save_json(flattened, output_path)
