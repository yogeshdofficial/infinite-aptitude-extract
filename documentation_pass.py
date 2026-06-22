import json
import re
from pathlib import Path
from typing import Optional
from gemini_utils import call_gemini
import PyPDF2

# ─────────────────────────────────────────────────────────────────
# PATTERN DOCUMENTATION PROMPT
# ─────────────────────────────────────────────────────────────────
PATTERN_DOC_PROMPT = r"""
You are an expert mathematics educator and aptitude trainer, writing a
pattern note for a student preparing for Indian competitive exams
(SSC, Banking, CAT, placement tests).

This note covers ONE pattern. Its single goal is: after reading it, the
student can correctly solve EVERY question in "Questions In This Pattern"
below, and any new question of the same type in the exam.

This is read under exam time pressure. The student needs to recognize
the pattern, recall the formula, and execute the steps — FAST. Lead with
that. Background theory (prerequisites, definitions) is useful but
secondary, so it goes at the END as a reference appendix, not the start.
A student should never have to scroll past a wall of definitions to
reach the formula they came here for.

──────────────────────────────
GROUNDING RULE (most important)
──────────────────────────────

Base EVERY section on the ACTUAL questions listed below under
"Questions In This Pattern". Do not write generic, chapter-level
content that could apply to any partnership/profit-loss/work problem.

Before writing, scan all the listed questions and identify every
distinct variation in what's given and what's asked (e.g. "find share
from investment+time" vs "find investment from share" vs "partner
joins/leaves mid-term"). Key Formulas and Solution Framework together
must cover EVERY variation present — if you only handle the most common
case, a student will be stuck on the others. This is the actual test of
whether this note succeeds: could a student who has only read it solve
every single question listed below? If not, the note is incomplete.

If a formula, trick, or mistake doesn't actually appear in these
specific questions, leave it out. If the supplied questions don't
clearly support a section, say so briefly instead of inventing generic
content to fill space. A short, honest section beats a padded, generic one.

Use the Source Material only for terminology, notation, and formula
verification. Never copy long passages from it.

Pattern Name: {pattern_name}

Pattern Description:
{pattern_description}

Reference Pages:
{page_range}

Questions In This Pattern:
{pattern_questions}

Source Material (for terminology and notation context):
{pdf_content}

────────────────────────

Generate markdown with the following sections, in this exact order.

# {{pattern_name}}

## Overview

2-3 short sentences only. Explain:
* What kind of question this is — describe it the way a student would
  recognize it on sight, not in abstract terms.
* The one central idea used to solve it.

Get straight to the point. No fluff.

---

## Recognition Clues

How to spot this pattern in under 10 seconds while skimming an exam.

List as short bullets:
* exact keywords/phrases that appear in these specific questions,
* what is usually GIVEN,
* what is usually ASKED.

3-6 bullets. Every bullet must be something a student can literally
scan for in a question — not a vague description.

---

## Key Formulas

List the formulas actually used to solve the questions in this pattern.
This is NOT the same as the prerequisite formulas above — these are
the formulas specific to this pattern.

For each formula use this exact format:

### [Formula Name]

$$
\text{{formula}}
$$

**Variables:**
- $X$ = what X represents
- $Y$ = what Y represents
(list every symbol used in the formula)

**When to use:** one line describing the specific scenario.

**Worked example:** a short, concrete numerical walkthrough using
actual numbers from the questions listed above — state the given
values, substitute into the formula, and show the resulting answer.
This should be enough on its own for a student to see exactly how the
formula is applied, not just what it looks like.

Only include formulas that genuinely appear in the questions above.
2-4 formulas is normal. If no formula is specific to this pattern
beyond what was listed in Prerequisites, say so.

---

## Solution Framework

The standard step-by-step approach for this pattern, as a numbered
list. Each step is one short line — this is a checklist to follow
under exam time pressure.

For each step, write:
**Step N: [what to do]** — one-line explanation of WHY this step is
done (so students understand the logic, not just the mechanics).

Aim for 3-6 steps. A student should be able to memorize this list
and apply it mechanically to any question in this pattern.

---

## Shortcut Tricks

Practical exam-time shortcuts that genuinely apply to THESE questions.

Each trick:
* **Trick:** one line stating the trick.
* **Why it works:** one line explaining the underlying reason.
* **When to use it:** one line on the specific condition that makes
  the trick applicable.
* **Example:** a quick numerical demonstration using values from the
  questions above, showing the trick actually saving a step compared
  to the full Solution Framework.

Only include tricks that are genuinely faster than the Solution
Framework above. If no real shortcut exists, say: "No shortcut
faster than the standard framework — apply the steps above directly."

---

## Common Mistakes

3-5 mistakes students actually make on THIS pattern (not generic
arithmetic slips). For each:

* **Mistake:** state it concretely.
* **Why it happens:** one-line root cause.
* **Fix:** one-line correction.

---

## Worked Example (Step-by-Step)

Pick ONE representative question from the pattern questions above and
show the full solution using the Solution Framework steps. This must be
a COMPLETE, beginner-friendly walkthrough — every step explained, no gaps.

Format:
**Question:** [quote the question]

**Solution:**
[walk through each step of the Solution Framework applied to this question]

**Answer:** [state the final answer clearly]

If the questions in this pattern vary meaningfully (e.g. some give the
answer-back-from-share instead of share-from-investment, or involve a
twist like a partner joining/leaving mid-term), pick a SECOND worked
example that covers that variation, so a student who only reads this
section can still handle every question type listed above — not just
the simplest one. Otherwise, one example is enough.

This section exists so a student who is confused by the abstract
framework can see it applied concretely. Make it count — after reading
this, the student should be able to solve every question listed above
on their own.

---

## Similar Patterns

1-2 lines on the pattern(s) most likely to be confused with this one,
and the single clearest way to tell them apart.

Format:
**[Similar Pattern Name]:** [how to distinguish it from this pattern
in one line — what specific clue in the question tells you which one
it is].

If this pattern is fairly distinct, say so briefly instead of forcing
a comparison.

---

## Revision Summary

A 5-line cheat sheet, each line a single short sentence:

**Key formula:** ...

**Spot it by:** ...

**First move:** ...

**Fastest method:** ...

**Biggest trap:** ...

---

## Appendix: Prerequisites

This section is for a student who has never studied this pattern before
and needs background before the sections above make sense. A student
who already knows the basics can skip this entirely — everything they
need to solve questions is already above.

List everything a student must already know before they can understand
this pattern. Be specific and concrete — this is not a vague "you should
know ratios" section. It is a precise checklist.

Organize into three sub-sections:

### Concepts You Must Know
Bullet list of mathematical concepts. For each, write:
**Concept name** — one-line plain-English definition. If the concept
has a formula attached, include it inline as `$...$`.

Only include concepts that are genuinely needed for this specific
pattern's questions. Do not list generic concepts (like "addition")
that every student obviously knows.

### Formulas You Must Know First
For each formula that is used as a building block in this pattern
(i.e. a formula the student must already know, not the pattern's own
formula), use this format:

$$
\text{{formula}}
$$

**What it means:** one sentence.
**Example:** one concrete numerical example showing the formula in use.

If this pattern's questions don't rely on any prerequisite formulas
(e.g. it only uses direct given information), write: "No prerequisite
formulas — all formulas needed are introduced below."

### Terms Used In This Pattern
A compact glossary of terms that appear in the questions for this
pattern. Format:

**Term** — one-line definition. If the term has a standard abbreviation
or notation, include it.

Only include terms that literally appear in the question text or
solution steps shown below.

────────────────────────

FORMATTING RULES (for mobile/KaTeX rendering):

* Use `$$ ... $$` for standalone formulas, `$...$` for inline math.
* Never write a fraction as plain text — always `\frac{{a}}{{b}}`.
* Never mix LaTeX and plain-text math in the same line.
* Keep bullets short — one idea per bullet.
* No long paragraphs anywhere.
* Use concise markdown with bullets and headers.
* Avoid unnecessary theory or historical discussion.

Return only valid markdown. No preamble, no explanation of what you did.
"""

# ─────────────────────────────────────────────────────────────────
# CHAPTER OVERVIEW PROMPT
# ─────────────────────────────────────────────────────────────────
CHAPTER_OVERVIEW_PROMPT = r"""
You are an expert mathematics educator writing a chapter introduction
for a student preparing for Indian competitive exams (SSC, Banking,
CAT, placement tests).

This document is read FIRST, before any pattern notes — it's the
student's introduction to the chapter. Its job is to actually teach:
1. Give the student a clear mental model of what this chapter is about,
   in plain language, with real terminology explained properly.
2. Build up the core concepts and formulas the student needs, so when
   they reach the pattern notes, nothing feels unfamiliar.
3. Then orient them — show how the patterns connect and differ, and
   suggest a sensible study order.

Write it the way a good teacher would explain a new chapter on day
one: start from what the student already knows, introduce new ideas
properly with definitions and small examples, and only then get into
navigation. Don't write it like a dense exam cheat-sheet — that's what
the pattern notes and cheat sheet are for. This document can take its
time to actually explain things.

Chapter Title:
{chapter_title}

Reference Pages:
{page_range}

Patterns Discovered In This Chapter (name: question count):
{pattern_summary}

Source Material:
{pdf_content}

────────────────────────

Generate markdown with the following sections, in this exact order.

# {chapter_title} — Chapter Overview

## What This Chapter Is About

3-4 sentences. State clearly:
- What real-world situation or mathematical domain this chapter deals with.
- The central quantity or relationship that ALL problems in this chapter
  revolve around.
- What types of questions appear (briefly — patterns are detailed below).

No history, no motivation, no "in this chapter we will learn." Orient
the student factually.

---

## Core Concepts

The 4-8 fundamental ideas a student must understand to work any
question in this chapter. These are concepts, not formulas — the
mental models that underpin everything that follows.

For each:
**[Concept Name]** — plain-English definition, written so a student
seeing this chapter for the first time actually understands it. Include
a concrete, one-sentence example that shows the concept in a realistic
setting.

Only include concepts that are genuinely needed across this chapter —
but don't shortchange this section. If a student needs to understand
something to follow the pattern notes later, it belongs here, explained
properly.

---

## Key Terms Glossary

A glossary of terms that appear repeatedly in this chapter's questions.
A student who has never seen this chapter's vocabulary should be able
to read this and follow everything afterward without confusion. Format:

**Term** — clear definition. Include the standard notation or
abbreviation if one exists, and a short example if the term benefits
from one.

Only include terms that literally appear in question text or solutions
in this chapter. Do not add generic math terms everyone already knows.

---

## Pattern Map

For every pattern listed under "Patterns Discovered In This Chapter",
write exactly ONE line answering the question:
"What makes this pattern distinct from all the others?"

Format:
**[Pattern Name]** (N questions) — what distinguishes this pattern
from the others: the specific clue in the question, the specific
quantity being found, or the specific setup move that is unique to it.

List EVERY pattern given to you, in a logical study order (simpler
patterns first, more complex ones that build on them later).
Do not skip, merge, or invent patterns.

This section is a navigation aid — a student should be able to read
it, recognize which pattern matches their current exam question, and
jump to the right pattern note.

---

## Core Formulas

Every formula that a student needs to solve questions across this
chapter's patterns — this is the chapter's formula reference, so do
not artificially cap the count. Include every distinct formula that
genuinely appears across the patterns, even if some look similar
(e.g. a base case and a special case deserve separate entries if
they're applied differently).

For each use this format:

### [Formula Name]

$$
\text{{formula}}
$$

**Variables:**
- $X$ = what X represents
(list every symbol)

**When to use:** one line — describe the scenario, not the math.

**Key insight:** one line — the non-obvious thing about this formula
that students typically get wrong or forget.

**Worked example:** one concrete numerical example.

Only include formulas genuinely needed across multiple patterns.
Pattern-specific formulas belong in each pattern's own note.

---

## Suggested Study Order

A numbered list giving the recommended sequence for studying the
patterns, with a one-line reason for each ordering decision.

1. [Pattern Name] — start here because ...
2. [Pattern Name] — study next because it builds on ...
...

Only include genuine ordering reasons. If two patterns are independent,
say so rather than forcing a sequence.

---

## Chapter-Wide Traps

3-5 mistakes that apply across ALL patterns in this chapter — things
students get wrong regardless of which pattern they're solving.

Format:
**[Trap name]:** what the trap is (one line) → how to avoid it (one line).

Do not repeat pattern-specific traps. Only include traps that genuinely
cut across the whole chapter.

If fewer than 2 genuine chapter-wide traps exist, skip this section.

────────────────────────

FORMATTING RULES:

* Use proper LaTeX (`$$...$$` for display, `$...$` inline).
* Never write a fraction as plain text — always `\frac{{a}}{{b}}`.
* Use markdown with headers and bullets for structure, but write
  Core Concepts and Key Terms Glossary as proper explanatory prose —
  this document is meant to teach, not just list facts. A sentence or
  two of real explanation is good; this is not the cheat sheet.
* Keep Pattern Map, Study Order, and Chapter-Wide Traps tight and
  scannable, since those are navigation aids, not teaching content.
* Avoid content that belongs in individual pattern notes (pattern-
  specific formulas, tricks, mistakes) — keep this chapter-level.

Return only valid markdown. No preamble.
"""

# ─────────────────────────────────────────────────────────────────
# CHAPTER CHEATSHEET PROMPT
# ─────────────────────────────────────────────────────────────────
CHAPTER_CHEATSHEET_PROMPT = r"""
You are an expert aptitude trainer writing the single most useful
reference document for this chapter — dense enough for a 5-10 minute
last-minute revision pass, but complete enough that a student who has
ALREADY studied the pattern notes could use ONLY this document to
solve any question of any type in this chapter, with every formula
they would need right there.

Every line must earn its place. Minimal prose, maximum usable
density — but do not sacrifice completeness for brevity: missing a
formula or a pattern's trigger condition makes this document useless
for that pattern. If the student has time to read only one document
before the exam, this is it, so it must genuinely cover everything.

Chapter Title:
{chapter_title}

Patterns In This Chapter (name: question count):
{pattern_summary}

Extracted Data Per Pattern (formulas, mistakes, shortcuts, question
samples — sourced directly from solved questions):
{enriched_context}

────────────────────────

Generate markdown with the following sections, in this exact order.

# {chapter_title} — Exam Cheat Sheet

## How To Solve Any Question In This Chapter

A short decision flow (numbered steps, 4-7 steps) a student can follow
on ANY question from this chapter, even one they haven't seen before:
1. What to read/identify first in the question (the discriminating
   clue that tells you which pattern applies).
2. How to map from that clue to one of the patterns listed below.
3. The general move once the pattern is identified (set up ratio /
   apply formula / form equation — at a high level).
4. A reminder to sanity-check the final answer (sign, realistic
   magnitude, matches a given option if MCQ).

This section is the master key — write it so a student who is unsure
which pattern a brand-new question belongs to can use this to figure
it out, then jump to the right row in the Quick-Recognition Table.

---

## Quick-Recognition Table

A markdown table with 4 columns:
Pattern | Trigger Words | Given | Find

One row per pattern. Rules:
- **Trigger Words:** 2-4 actual keywords from question text that
  signal this pattern (e.g. "salary + share", "withdrew after X months").
- **Given:** what information the question provides (≤5 words).
- **Find:** what the question asks for (≤4 words).

Every pattern must have its own row. Do not skip any.

---

## Formula Bank

For EVERY pattern, list ALL of its key formulas — this is the part of
the document students rely on most, so do not omit a formula just to
save space. Group by pattern.

Format:
**[Pattern Name]**

$$
\text{{formula}}
$$

→ *produces: [what the formula gives you, in 4-6 words]*
→ *use when: [the specific situation that calls for this formula, in 4-8 words]*

One formula block per formula. If a pattern has multiple essential
formulas (e.g. a base formula and a special-case variant), list them
all — one block each, in the order a student would reach for them.
Do not merge multiple formulas into one block, and do not skip a
formula because it seems minor — a student in an exam can't tell which
formula is "minor" until they need exactly that one.

---

## Step Sequences

For each pattern, the solution steps compressed to a one-line checklist.

Format:
**[Pattern Name]:** Step 1 → Step 2 → Step 3 → Answer

Keep each step to 2-4 words. This is a memory aid, not an explanation.
Cover every pattern listed in Quick-Recognition Table — do not skip
any pattern here even if its steps feel obvious.

---

## Fastest Tricks

One bullet per trick. Tricks only — no steps, no explanations.
Format: **[Pattern]:** trick in ≤12 words.

Only include tricks that are genuinely faster than the standard method.
Cover as many patterns as genuinely have a real shortcut — do not cap
this artificially; skip a pattern entirely only if it has no real
shortcut beyond the standard method.

---

## Trap Watch

The most dangerous mistake per pattern. One bullet per pattern that
has a real trap worth flagging.

Format: **[Pattern]:** trap in ≤8 words → fix in ≤6 words.

Skip patterns with no memorable trap. Do not force one.

---

## Last-Minute Reminders

3-5 short sentences covering the most commonly forgotten facts or
rules for this chapter — things that are easy to know in isolation
but get confused under exam pressure.

Keep each reminder to one sentence. No bullets inside bullets.

────────────────────────

FORMATTING RULES:

* Maximum density. No paragraphs, no intros, no summaries-of-summaries
  outside the "How To Solve Any Question" section, which is allowed to
  be a tight numbered list.
* Every formula in proper LaTeX (`$$...$$` display, `$...$` inline).
* Never write a plain-text fraction like 1/2 — always `\frac{{a}}{{b}}`.
* The table must be a real markdown table (pipe-delimited, with header
  separator row).
* Completeness of formulas and patterns takes priority over length —
  cut filler words, not coverage.

Return markdown only. No preamble.
"""


def extract_pdf_pages(pdf_path: str, start_page: int, end_page: int) -> str:
    """Extract text from PDF pages."""
    text = []
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(start_page - 1, min(end_page, len(reader.pages))):
                page = reader.pages[page_num]
                text.append(page.extract_text())
        return "\n".join(text)
    except Exception as e:
        print(f"  WARNING: Error reading PDF: {e}")
        return ""


def safe_filename_stem(text: str) -> str:
    """Convert arbitrary text into a safe lowercase filename stem."""
    stem = re.sub(r"[^A-Za-z0-9]+", "_", text.lower()).strip("_")
    return stem or "document"


def humanize_chapter_title(stem: str) -> str:
    """
    Turn a raw filename stem like 'Chapter_14_Partnership' into a
    readable title like 'Partnership' for use in markdown headings.
    """
    cleaned = re.sub(r"^chapter_\d+_", "", stem, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned.title() if cleaned else stem


def format_pattern_questions(questions: list[dict], max_chars: int = 8000) -> str:
    """
    Format the actual questions belonging to one pattern for grounding
    the documentation prompt. Includes question text, solution, AND the
    paraphrased solution from ai_enrichment when available (richer context
    for the model to draw formulas and mistakes from).
    Truncates by whole-question boundaries once max_chars is reached.
    """
    blocks = []
    total_len = 0
    for q in questions:
        qnum = q.get("question_number", "?")
        qtext = q.get("question_text", q.get("question", ""))
        solution = q.get("solution", "") or q.get("traditional_solution", "")

        # Also pull paraphrased solution from ai_enrichment — it's often
        # more formula-rich and better structured than the raw solution.
        ae = q.get("ai_enrichment") or {}
        paraphrased = ae.get("traditional_solution", "").strip()
        formulas = ae.get("formulas_used", [])
        mistakes = ae.get("common_mistakes", [])

        block_parts = [f"Q{qnum}: {qtext}", f"Solution: {solution}"]
        if paraphrased:
            block_parts.append(f"Structured solution: {paraphrased}")
        if formulas:
            block_parts.append(f"Formulas used: {', '.join(formulas)}")
        if mistakes:
            block_parts.append(f"Common mistakes: {', '.join(mistakes)}")

        block = "\n".join(block_parts)

        if total_len + len(block) > max_chars and blocks:
            blocks.append(
                f"... ({len(questions) - len(blocks)} more questions omitted for length)"
            )
            break
        blocks.append(block)
        total_len += len(block)
    return "\n---\n".join(blocks) if blocks else "(no questions found for this pattern)"


def generate_pattern_documentation(
    pattern_name: str,
    pattern_description: str,
    question_count: int,
    pdf_content: str,
    page_range: tuple,
    pattern_questions: str = "",
) -> str:
    """Generate markdown documentation for a pattern using Gemini."""

    prompt = PATTERN_DOC_PROMPT.format(
        pattern_name=pattern_name,
        pattern_description=pattern_description,
        question_count=question_count,
        page_range=f"{page_range[0]}-{page_range[1]}",
        pattern_questions=pattern_questions,
        pdf_content=pdf_content[:5000],  # increased from 2000 for better grounding
    )

    try:
        documentation = call_gemini(prompt)

        if not documentation or len(documentation.strip()) < 100:
            print(f"  WARNING: Generated documentation too short for {pattern_name}")

        return documentation
    except Exception as e:
        print(f"  ERROR generating docs for {pattern_name}: {e}")
        return f"# {pattern_name}\n\n*Documentation generation failed. Please retry.*"


def create_pattern_markdown_files(
    categorized_file: str,
    pdf_path: str,
    pdf_pages: tuple,
    output_dir: str = "pattern_docs",
    skip_existing: bool = True,
) -> None:
    """Create markdown files for each sub-pattern."""

    with open(categorized_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data.get("questions", []) if isinstance(data, dict) else data

    pdf_content = extract_pdf_pages(pdf_path, pdf_pages[0], pdf_pages[1])

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    patterns_map: dict[str, list[dict]] = {}
    for item in questions:
        pattern = item.get("sub_pattern") or "Uncategorized"
        patterns_map.setdefault(pattern, []).append(item)

    if list(patterns_map.keys()) == ["Uncategorized"]:
        print(
            "  WARNING: every question is 'Uncategorized'. This usually means "
            "Pass 4 (--categorize) was not run, or it failed. Pattern "
            "documentation will not be meaningful until categorization "
            "succeeds. Re-run with --categorize first."
        )

    pattern_filenames: dict[str, str] = {
        pattern_name: safe_filename_stem(pattern_name) + ".md"
        for pattern_name in patterns_map
    }

    for idx, (pattern_name, pattern_questions) in enumerate(patterns_map.items(), 1):
        print(f"  [{idx}/{len(patterns_map)}] {pattern_name}...")

        filename = pattern_filenames[pattern_name]
        filepath = output_path / filename

        if skip_existing and filepath.exists():
            print(f"    → Skipping existing file: {filepath.name}")
        else:
            # Build pattern description from categorization data if available
            pattern_desc = f"Pattern covering {len(pattern_questions)} questions"
            cat_data = data.get("categorization", {}) if isinstance(data, dict) else {}
            for sp in cat_data.get("sub_patterns", []):
                if sp.get("pattern_name") == pattern_name:
                    pattern_desc = sp.get("description", pattern_desc)
                    break

            documentation = generate_pattern_documentation(
                pattern_name=pattern_name,
                pattern_description=pattern_desc,
                question_count=len(pattern_questions),
                pdf_content=pdf_content,
                page_range=pdf_pages,
                pattern_questions=format_pattern_questions(pattern_questions),
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(documentation)

    # Backfill pattern_doc on every question in the categorized JSON
    for item in questions:
        pattern = item.get("sub_pattern") or "Uncategorized"
        item["pattern_doc"] = pattern_filenames.get(pattern, "")

    with open(categorized_file, "w", encoding="utf-8") as f:
        json.dump(
            data if isinstance(data, dict) else questions,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"  ✓ pattern_doc field written to {Path(categorized_file).name}")


def create_main_pattern_overview(
    categorized_file: str,
    pdf_path: str,
    pdf_pages: tuple,
    output_file: str = "PATTERNS_OVERVIEW.md",
    overwrite: bool = True,
) -> None:
    """Create a chapter introduction document for the current chapter."""

    output_path = Path(output_file)
    if not overwrite and output_path.exists():
        print(f"  ✓ Overview already exists: {output_file}")
        return

    with open(categorized_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data.get("questions", []) if isinstance(data, dict) else data

    pdf_content = extract_pdf_pages(pdf_path, pdf_pages[0], pdf_pages[1])

    patterns_map = {}
    for item in questions:
        pattern = item.get("sub_pattern") or "Uncategorized"
        if pattern not in patterns_map:
            patterns_map[pattern] = []
        patterns_map[pattern].append(item["question_number"])

    if list(patterns_map.keys()) == ["Uncategorized"]:
        print(
            "  WARNING: every question is 'Uncategorized' in the chapter "
            "overview. Run --categorize first for a meaningful Pattern Map."
        )

    # Include prerequisite_patterns in pattern_summary for the overview
    # so the model can suggest a study order grounded in real dependencies.
    cat_data = data.get("categorization", {}) if isinstance(data, dict) else {}
    prereq_map: dict[str, list[str]] = {}
    for sp in cat_data.get("sub_patterns", []):
        prereq_map[sp["pattern_name"]] = sp.get("prerequisite_patterns", [])

    pattern_summary_lines = []
    for pattern_name, qnums in sorted(patterns_map.items()):
        prereqs = prereq_map.get(pattern_name, [])
        prereq_str = f" [requires: {', '.join(prereqs)}]" if prereqs else ""
        pattern_summary_lines.append(
            f"- {pattern_name}: {len(qnums)} questions{prereq_str}"
        )
    pattern_summary = "\n".join(pattern_summary_lines)

    prompt = CHAPTER_OVERVIEW_PROMPT.format(
        chapter_title=humanize_chapter_title(
            Path(categorized_file).stem.replace("_categorized", "")
        ),
        page_range=f"{pdf_pages[0]}-{pdf_pages[1]}",
        pdf_content=pdf_content[:6000],
        pattern_summary=pattern_summary,
    )

    overview = call_gemini(prompt)

    if not overview or len(overview.strip()) < 100:
        overview = "# Chapter Introduction\n\n*Failed to generate chapter introduction. Please retry.*"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(overview)

    print(f"  ✓ Overview: {output_file}")


def build_cheatsheet_context(questions: list[dict]) -> dict[str, dict]:
    """
    Aggregate per-pattern data from the already-enriched JSON.
    Returns dict keyed by pattern name with formulas, mistakes, shortcuts,
    and representative question samples for richer prompt grounding.
    """
    patterns: dict[str, dict] = {}

    for q in questions:
        pattern = q.get("sub_pattern") or "Uncategorized"
        enrichment = q.get("ai_enrichment") or {}

        entry = patterns.setdefault(
            pattern,
            {
                "question_count": 0,
                "formulas": [],
                "common_mistakes": [],
                "shortcuts": [],
                "question_samples": [],
            },
        )

        entry["question_count"] += 1

        for f in enrichment.get("formulas_used", []):
            if f and f not in entry["formulas"]:
                entry["formulas"].append(f)

        for m in enrichment.get("common_mistakes", []):
            if m and m not in entry["common_mistakes"]:
                entry["common_mistakes"].append(m)

        # Grab the shortcut solution's first one or two meaningful sentences
        shortcut = (enrichment.get("shortcut_solution") or "").strip()
        if shortcut:
            sentences = re.split(r"(?<=[.!?])\s", shortcut)
            snippet = " ".join(sentences[:2]).strip()
            if snippet and snippet not in entry["shortcuts"]:
                entry["shortcuts"].append(snippet)

        # Add representative question samples (question text only, brief)
        qtext = (q.get("question_text") or q.get("question") or "").strip()
        if qtext and len(entry["question_samples"]) < 4:
            entry["question_samples"].append(
                f"Q{q.get('question_number', '?')}: {qtext[:220]}"
            )

    return patterns


def format_cheatsheet_context(patterns: dict[str, dict]) -> str:
    """Serialize aggregated pattern data into a compact text block for the prompt."""
    lines = []
    for pattern_name, data in sorted(patterns.items()):
        lines.append(f"### {pattern_name} ({data['question_count']} questions)")
        if data["question_samples"]:
            lines.append("Example questions:")
            for s in data["question_samples"]:
                lines.append(f"  {s}")
        if data["formulas"]:
            lines.append("Formulas used (cover ALL of these in the Formula Bank):")
            for f in data["formulas"][:12]:
                lines.append(f"  - {f}")
        if data["common_mistakes"]:
            lines.append("Common mistakes:")
            for m in data["common_mistakes"][:8]:
                lines.append(f"  - {m}")
        if data["shortcuts"]:
            lines.append("Shortcuts:")
            for s in data["shortcuts"][:6]:
                lines.append(f"  - {s}")
        lines.append("")
    return "\n".join(lines)


def create_chapter_cheatsheet_v2(
    categorized_file: str,
    output_file: str = "CHAPTER_CHEATSHEET.md",
    overwrite: bool = True,
    # kept for call-site compatibility — not used
    pdf_path: Optional[str] = None,
    pdf_pages: Optional[tuple] = None,
) -> None:
    """
    Create a chapter cheat sheet built entirely from the enriched JSON.
    No PDF read — all data comes from ai_enrichment fields (Pass 3).
    """
    output_path = Path(output_file)
    if not overwrite and output_path.exists():
        print(f"  ✓ Cheat sheet already exists: {output_file}")
        return

    with open(categorized_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", []) if isinstance(data, dict) else data
    patterns = build_cheatsheet_context(questions)

    pattern_summary = "\n".join(
        f"- {name}: {d['question_count']} questions"
        for name, d in sorted(patterns.items())
    )
    enriched_context = format_cheatsheet_context(patterns)

    prompt = CHAPTER_CHEATSHEET_PROMPT.format(
        chapter_title=humanize_chapter_title(
            Path(categorized_file).stem.replace("_categorized", "")
        ),
        pattern_summary=pattern_summary,
        enriched_context=enriched_context,
    )

    cheatsheet = call_gemini(prompt)

    if not cheatsheet or len(cheatsheet.strip()) < 100:
        cheatsheet = (
            "# Chapter Cheat Sheet\n\n"
            "*Failed to generate chapter cheat sheet. Please retry.*"
        )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cheatsheet)

    print(f"  ✓ Cheat sheet: {output_file}")


# ── kept for backwards compatibility ──────────────────────────────
def create_chapter_cheatsheet(
    categorized_file: str,
    pdf_path: str,
    pdf_pages: tuple,
    output_file: str = "CHAPTER_CHEATSHEET.md",
    overwrite: bool = True,
) -> None:
    """Backwards-compatible wrapper — delegates to create_chapter_cheatsheet_v2."""
    create_chapter_cheatsheet_v2(
        categorized_file=categorized_file,
        output_file=output_file,
        overwrite=overwrite,
    )
