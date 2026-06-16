# enrichment_utils.py
from pathlib import Path
from cache_utils import cache_batch
import json
import re
from gemini_utils import call_gemini_text
from enrichment_prompts import ENRICHMENT_PROMPT
from enrichment_schema import AI_ENRICHMENT_PROPS

from gemini_utils import call_gemini

BATCH_SIZE = 10


def chapter_slug(chapter_name: str) -> str:
    """Normalize chapter name to a stable snake_case slug."""
    slug = (chapter_name or "").strip().lower()
    slug = re.sub(r"^chapter_\d+_", "", slug)
    slug = re.sub(r"[^a-z0-9]+", "_", slug).strip("_")
    return slug


def _latex_formula(formula: str) -> str:
    """Wrap formula expressions in LaTeX delimiters when needed."""
    text = (formula or "").strip()
    if not text:
        return ""

    if "$" in text:
        return text

    if ":" in text:
        label, expr = text.split(":", 1)
        label = label.strip()
        expr = expr.strip()
        if expr:
            return f"{label}: ${expr}$"

    return f"${text}$"


def normalize_ai_enrichment(ai_enrichment: dict, chapter_name: str) -> dict:
    """Normalize AI enrichment structure and content for stable downstream usage."""
    ai = dict(ai_enrichment or {})

    chapter = ai.get("chapter") or chapter_slug(chapter_name)
    ai["chapter"] = chapter_slug(chapter)

    formulas = ai.get("formulas_used")
    if formulas is None:
        formulas = ai.get("formulae_used", [])

    if isinstance(formulas, str):
        formulas = [formulas]
    elif not isinstance(formulas, list):
        formulas = []

    ai["formulas_used"] = [_latex_formula(str(item)) for item in formulas if item]
    ai.pop("formulae_used", None)

    return ai


def normalize_questions_ai_enrichment(questions: list[dict], chapter_name: str) -> None:
    """In-place normalization for all question ai_enrichment blocks."""
    for question in questions:
        ai_enrichment = question.get("ai_enrichment")
        if isinstance(ai_enrichment, dict) and ai_enrichment:
            question["ai_enrichment"] = normalize_ai_enrichment(
                ai_enrichment,
                chapter_name,
            )


def enrich_question_batch(
    *,
    client,
    model,
    chapter_name,
    questions,
    rate_limiter,
):
    """
    Enrich a batch of questions.
    """

    payload = []

    for q in questions:

        payload.append(
            {
                "question_number": q["question_number"],
                "question_text": q.get(
                    "question_text",
                    "",
                ),
                "option_a": q.get(
                    "option_a",
                    "",
                ),
                "option_b": q.get(
                    "option_b",
                    "",
                ),
                "option_c": q.get(
                    "option_c",
                    "",
                ),
                "option_d": q.get(
                    "option_d",
                    "",
                ),
                "option_e": q.get(
                    "option_e",
                    "",
                ),
                "correct_option": q.get(
                    "correct_option",
                    "",
                ),
                "solution": q.get(
                    "solution",
                    "",
                ),
            }
        )

    prompt = (
        ENRICHMENT_PROMPT
        + "\n\n"
        + f"Chapter: {chapter_name}\n\n"
        + json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        )
    )

    schema = {
        "type": "OBJECT",
        "properties": {
            "items": {
                "type": "ARRAY",
                "items": {
                    "type": "OBJECT",
                    "properties": {
                        "question_number": {"type": "STRING"},
                        "ai_enrichment": {
                            "type": "OBJECT",
                            "properties": AI_ENRICHMENT_PROPS,
                            "required": list(AI_ENRICHMENT_PROPS.keys()),
                        },
                    },
                    "required": [
                        "question_number",
                        "ai_enrichment",
                    ],
                },
            }
        },
        "required": ["items"],
    }

    result = call_gemini_text(
        client=client,
        model=model,
        prompt=prompt,
        response_schema=schema,
        rate_limiter=rate_limiter,
    )

    return result["items"]


def enrich_questions(
    *,
    client,
    model,
    chapter_name,
    questions,
    rate_limiter,
):
    total = len(questions)

    enriched_count = 0

    for start in range(
        0,
        total,
        BATCH_SIZE,
    ):

        end = min(
            start + BATCH_SIZE,
            total,
        )

        batch = questions[start:end]
        batch = [q for q in batch if not q.get("ai_enrichment")]
        print(f"[pass3] " f"questions " f"{start+1}-{end}")
        if not batch:

            print("[pass3] already enriched")

            continue
        try:

            enrichments = enrich_question_batch(
                client=client,
                model=model,
                chapter_name=chapter_name,
                questions=batch,
                rate_limiter=rate_limiter,
            )
            if enrichments is None:

                raise ValueError("Gemini returned None")

            print(
                "returned", len(enrichments), "enrichments for", len(batch), "questions"
            )

            if len(enrichments) != len(batch):

                raise ValueError(
                    f"Expected {len(batch)} enrichments, got {len(enrichments)}"
                )
            enrichment_map = {
                x["question_number"]: x["ai_enrichment"] for x in enrichments
            }

            for q in batch:

                qnum = q["question_number"]

                if qnum in enrichment_map:

                    q["ai_enrichment"] = enrichment_map[qnum]

                    enriched_count += 1

                else:

                    q["ai_enrichment"] = {}

            normalize_questions_ai_enrichment(
                questions,
                chapter_name,
            )
            cache_batch(
                chapter_title=chapter_name,
                questions=questions,
                output_path=Path("output_json") / f"{chapter_name}.json",
            )
        except Exception as ex:

            print(
                "[pass3] failed:",
                ex,
            )

            for q in batch:
                q["ai_enrichment"] = {}

    print("[pass3]", enriched_count, "questions enriched.")

    return questions
