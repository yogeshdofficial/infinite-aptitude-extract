# enrichment_utils.py
from pathlib import Path
from cache_utils import cache_batch
import json
import re
from gemini_utils import call_gemini_text
from enrichment_prompts import ENRICHMENT_PROMPT
from enrichment_schema import AI_ENRICHMENT_PROPS

from gemini_utils import call_gemini

# Batch size for enrichment. Kept small so a single hard question
# cannot burn the token budget for the entire batch.
BATCH_SIZE = 5


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


def _fix_currency_inside_math_boundary(text: str) -> tuple[str, int]:
    """
    Safety net: \\right) immediately followed by '= ₹ <number>' BEFORE
    the closing $, pulling currency inside KaTeX math mode.
    """
    if not text or "₹" not in text or "\\right" not in text:
        return text, 0

    pattern = re.compile(r"(\\right[\)\]])(\\s*=\\s*)(₹\\s*[\\d,]+(?:\\.\\d+)?)(\\$)")
    fix_count = 0

    def _fix(m):
        nonlocal fix_count
        fix_count += 1
        right_paren, eq, currency_part, dollar = m.groups()
        return f"{right_paren}{dollar}{eq}{currency_part}"

    fixed = pattern.sub(_fix, text)
    return fixed, fix_count


def _fix_bare_fractions(text: str) -> tuple[str, int]:
    """
    Safety net: digit/digit fractions sitting outside $...$ blocks.
    """
    if not text or "/" not in text:
        return text, 0

    parts = re.split(r"(\$[^$]*\$)", text)
    fix_count = 0
    bare_fraction = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")

    for i, part in enumerate(parts):
        if part.startswith("$") and part.endswith("$"):
            continue

        def _wrap(m):
            nonlocal fix_count
            fix_count += 1
            return f"$\\frac{{{m.group(1)}}}{{{m.group(2)}}}$"

        parts[i] = bare_fraction.sub(_wrap, part)

    return "".join(parts), fix_count


def fix_latex_in_ai_enrichment(ai_enrichment: dict) -> dict:
    """
    Run LaTeX safety-net fixes over human-readable text fields.
    Mutates and returns ai_enrichment.
    """
    text_fields = [
        "paraphrased_question",
        "traditional_solution",
        "shortcut_solution",
    ]
    total_fixes = 0
    for field in text_fields:
        value = ai_enrichment.get(field)
        if isinstance(value, str) and value:
            value, frac_fixes = _fix_bare_fractions(value)
            value, currency_fixes = _fix_currency_inside_math_boundary(value)
            count = frac_fixes + currency_fixes
            if count:
                ai_enrichment[field] = value
                total_fixes += count

    if total_fixes:
        qn = ai_enrichment.get("question_number", "?")
        print(
            f"[latex-fix] auto-wrapped {total_fixes} bare fraction(s)"
            f" (question {qn})"
        )

    return ai_enrichment


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

    ai = fix_latex_in_ai_enrichment(ai)

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


def _is_enriched(q: dict) -> bool:
    """
    A question is considered already enriched only when its ai_enrichment
    dict is non-empty AND contains at least a paraphrased_question value.
    An empty dict {} (written on previous failure) is treated as not enriched
    so it gets retried on the next run.
    """
    ae = q.get("ai_enrichment")
    return (
        isinstance(ae, dict)
        and bool(ae)
        and bool(ae.get("paraphrased_question", "").strip())
    )


def _build_prompt(chapter_name: str, questions: list[dict]) -> str:
    payload = [
        {
            "question_number": q["question_number"],
            "question_text": q.get("question_text", ""),
            "option_a": q.get("option_a", ""),
            "option_b": q.get("option_b", ""),
            "option_c": q.get("option_c", ""),
            "option_d": q.get("option_d", ""),
            "option_e": q.get("option_e", ""),
            "correct_option": q.get("correct_option", ""),
            "solution": q.get("solution", ""),
        }
        for q in questions
    ]
    return (
        ENRICHMENT_PROMPT
        + "\n\n"
        + f"Chapter: {chapter_name}\n\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
    )


def _schema_for_batch(expected_count: int) -> dict:
    return {
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
                    "required": ["question_number", "ai_enrichment"],
                },
            }
        },
        "required": ["items"],
    }


def _call_batch(
    *,
    client,
    model,
    rate_limiter,
    chapter_name: str,
    questions: list[dict],
    label: str,
) -> list[dict] | None:
    """
    Call Gemini for a batch. Returns a list of enrichment dicts on success,
    or None on total failure. Partial results (fewer items than requested)
    are returned as-is so the caller can salvage them.
    """
    expected_count = len(questions)
    prompt = _build_prompt(chapter_name, questions)
    schema = _schema_for_batch(expected_count)

    # We do NOT use the strict validate= count check here — instead we accept
    # partial results and let the caller decide what to do with them.
    # This avoids burning all 5 retries just because 1 of 5 questions is hard.
    result = call_gemini_text(
        client=client,
        model=model,
        prompt=prompt,
        response_schema=schema,
        rate_limiter=rate_limiter,
        # validate=None  intentionally — we salvage partials below
    )

    if result is None:
        return None

    items = result.get("items") if isinstance(result, dict) else None
    if not isinstance(items, list):
        return None

    got = len(items)
    if got == 0:
        print(f"  [{label}] model returned 0 items — skipping batch")
        return None

    if got < expected_count:
        print(
            f"  [{label}] partial result: got {got}/{expected_count} — "
            "salvaging returned items, missing ones will be retried individually"
        )

    return items


def enrich_question_batch(
    *,
    client,
    model,
    chapter_name,
    questions,
    rate_limiter,
) -> list[dict] | None:
    """
    Enrich a batch of questions with automatic fallback to per-question
    enrichment when the batch call returns fewer items than expected.

    Strategy:
    1. Try the whole batch once.
    2. Collect whichever items came back successfully.
    3. For any question not covered by step 2, retry it individually
       (batch-of-1), which virtually eliminates token-budget blowout.
    4. Return the combined list (same length as input, or None if everything
       failed).
    """
    n = len(questions)
    label = (
        f"batch[{questions[0]['question_number']}–{questions[-1]['question_number']}]"
    )

    # ── Step 1: attempt the full batch ──────────────────────────────────────
    items = _call_batch(
        client=client,
        model=model,
        rate_limiter=rate_limiter,
        chapter_name=chapter_name,
        questions=questions,
        label=label,
    )

    enrichment_map: dict[str, dict] = {}

    if items:
        for item in items:
            qnum = item.get("question_number")
            ae = item.get("ai_enrichment")
            if qnum and isinstance(ae, dict):
                enrichment_map[qnum] = ae

    # ── Step 2: individually retry any questions not covered ─────────────────
    missing = [q for q in questions if q["question_number"] not in enrichment_map]

    if missing:
        print(f"  [{label}] retrying {len(missing)} question(s) individually…")

    for q in missing:
        qnum = q["question_number"]
        solo_label = f"solo[{qnum}]"

        solo_items = _call_batch(
            client=client,
            model=model,
            rate_limiter=rate_limiter,
            chapter_name=chapter_name,
            questions=[q],
            label=solo_label,
        )

        if solo_items:
            for item in solo_items:
                ae = item.get("ai_enrichment")
                if isinstance(ae, dict):
                    enrichment_map[qnum] = ae
                    break
        else:
            print(f"  [{solo_label}] failed even as solo — leaving blank for retry")

    if not enrichment_map:
        return None

    # ── Step 3: assemble results in original order ───────────────────────────
    return [
        {
            "question_number": q["question_number"],
            "ai_enrichment": enrichment_map.get(q["question_number"], {}),
        }
        for q in questions
    ]


def enrich_questions(
    *,
    client,
    model,
    chapter_name,
    questions,
    rate_limiter,
    output_path: Path | None = None,
):
    total = len(questions)
    enriched_count = 0

    for start in range(0, total, BATCH_SIZE):
        end = min(start + BATCH_SIZE, total)
        batch = questions[start:end]

        # Only send questions that have not been successfully enriched yet.
        # An empty dict {} from a prior failed run is NOT considered enriched.
        unenriched = [q for q in batch if not _is_enriched(q)]

        print(f"[pass3] questions {start+1}-{end}", end="")
        if not unenriched:
            print(" (already enriched)")
            continue
        print(f" ({len(unenriched)} to enrich)")

        try:
            enrichments = enrich_question_batch(
                client=client,
                model=model,
                chapter_name=chapter_name,
                questions=unenriched,
                rate_limiter=rate_limiter,
            )

            if enrichments is None:
                print(
                    f"[pass3] batch {start+1}-{end}: all attempts failed, will retry on next run"
                )
                # Do NOT write empty dicts — leave ai_enrichment absent so
                # the next run will retry these questions.
                continue

            enrichment_map = {
                x["question_number"]: x["ai_enrichment"]
                for x in enrichments
                if x.get("ai_enrichment")  # only store non-empty results
            }

            for q in unenriched:
                qnum = q["question_number"]
                ae = enrichment_map.get(qnum)
                if ae:
                    q["ai_enrichment"] = ae
                    enriched_count += 1
                # If ae is None/empty, leave q["ai_enrichment"] absent so
                # it will be retried on the next run.

            normalize_questions_ai_enrichment(questions, chapter_name)

            if output_path is not None:
                cache_batch(
                    chapter_title=chapter_name,
                    questions=questions,
                    output_path=output_path,
                )

        except Exception as ex:
            print(f"[pass3] batch {start+1}-{end} exception: {ex}")
            # Do NOT write empty dicts — leave absent for retry

    print(f"[pass3] {enriched_count} questions enriched.")
    return questions
