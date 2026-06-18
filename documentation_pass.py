"""
Documentation Generation Pass: Create markdown files for each sub-pattern
"""

import json
import re
from pathlib import Path
from typing import Optional
from gemini_utils import call_gemini
import PyPDF2

# ─────────────────────────────────────────────────────────────────
# PATTERN DOC PROMPT  (unchanged — per-pattern revision note)
# ─────────────────────────────────────────────────────────────────
PATTERN_DOC_PROMPT = r"""
You are an expert mathematics educator and aptitude trainer, writing a
revision note for a student preparing for Indian competitive exams
(SSC, Banking, CAT, placement tests).

Create a concise but high-quality markdown revision note for ONE pattern.

The reader has already studied the chapter once. This note is for
REVISION and PATTERN RECOGNITION, not first-time learning. Assume they
know basic arithmetic, ratios, and percentages.

The goal: a student should be able to read this note in 3-4 minutes
and immediately recognize and solve any question of this type in an
exam.

──────────────────────────────
GROUNDING RULE (most important)
──────────────────────────────

Base Recognition Clues, Important Formulas, and Common Mistakes on
the ACTUAL questions listed below under "Questions In This Chapter
Belonging To This Pattern". Do not write generic, chapter-level
content that could apply to any partnership/profit-loss/work problem.
If a formula or trick doesn't actually appear in these specific
questions, leave it out — do not pad the note with material that
isn't grounded in what's given.

Use the Source Material only for terminology, notation, and to
double-check a formula. Never copy long passages from it.

Do NOT write like a textbook. Prefer formulas, frameworks, tricks,
and recognition clues over lengthy explanations.

Pattern Name: {pattern_name}

Pattern Description:
{pattern_description}

Reference Pages:
{page_range}

Questions In This Chapter Belonging To This Pattern:
{pattern_questions}

Source Material (full chapter, for terminology and notation context):
{pdf_content}

────────────────────────

Generate markdown with the following sections.

# {{pattern_name}}

## Overview

In 2-3 short sentences (not paragraphs), explain:

* What kind of question this is — describe it the way a student
  would recognize it on sight, not in abstract terms.
* The one central idea used to solve it.

Skip this section's intro fluff. Get straight to the idea.

---

## Recognition Clues

How to spot this pattern in under 10 seconds while skimming an exam.

List, as short bullets:

* exact keywords/phrases that appear in these specific questions,
* what is usually GIVEN,
* what is usually ASKED.

3-6 bullets. Every bullet must be something a student can literally
scan for in a question — not a vague description.

---

## Important Formulas

List the formulas actually used to solve the questions above. Each
formula needs:

* the formula itself, in display LaTeX using `$$ ... $$`,
* one line on what each symbol means,
* one line on when to reach for it.

Use this exact format for each formula:

### [Formula Name]

$$
\text{{...}}
$$

*Meaning:* ...

*Use when:* ...

Only include formulas that genuinely appear in the questions above.
2-4 formulas is normal. More is fine only if they are all genuinely
distinct and used.

---

## Solution Framework

The standard step-by-step approach for this pattern, as a numbered
list. Each step should be one short line — this is a checklist to
follow under exam time pressure, not an explanation.

Aim for 3-6 steps. A student should be able to memorize this list.

---

## Shortcut Tricks

Practical exam-time shortcuts that genuinely apply to THESE questions
— ratio shortcuts, symmetry, elimination of options, mental math.

Each trick: one line stating the trick, one line on why it's valid
(so it doesn't feel like an unexplained rule to memorize blindly).

Only include a trick if it is genuinely faster than the standard
framework above. If no real shortcut exists for this pattern, say so
in one line instead of inventing one.

---

## Common Mistakes

3-6 mistakes students actually make on THIS pattern (not generic
arithmetic slips). For each:

* the mistake, stated concretely,
* the one-line reason it happens,
* the one-line fix.

---

## Similar Patterns

1-2 lines on the pattern(s) most likely to be confused with this one,
and the single clearest way to tell them apart. If this pattern is
fairly distinct from everything else in the chapter, say that
briefly instead of forcing a comparison.

---

## Revision Summary

A 4-line cheat sheet, each line a single short sentence:

**Key formula:** ...

**Spot it by:** ...

**Fastest method:** ...

**Biggest trap:** ...

────────────────────────

FORMATTING RULES (for mobile/KaTeX rendering):

* Use `$$ ... $$` for standalone formulas, `$...$` for inline math.
* Never leave a fraction as plain text like 1/2 — always `\frac{{1}}{{2}}`.
* Never mix LaTeX and plain-text math in the same line.
* Keep bullets short — one idea per bullet, not multi-clause sentences.
* No long paragraphs anywhere in this document.
* Use concise markdown, bullets heavily, proper LaTeX for all formulas.
* Avoid unnecessary theory or historical discussion.
* Keep the document compact and information-dense — this is a
  revision note, not a lesson.

Return only valid markdown. No preamble, no explanation of what you did.
"""

# ─────────────────────────────────────────────────────────────────
# CHAPTER OVERVIEW PROMPT  (rewritten — intro + core formulas + terms)
# ─────────────────────────────────────────────────────────────────
CHAPTER_OVERVIEW_PROMPT = r"""
You are an expert mathematics educator writing a chapter introduction
for a student preparing for Indian competitive exams (SSC, Banking,
CAT, placement tests).

This document is read FIRST, before any pattern notes. Its job is to
teach the chapter's core concepts, key terminology, and foundational
formulas so the student has the right mental model before drilling
individual patterns.

Think of it as "the one page you'd read if you had 10 minutes to
understand what this chapter is about".

Chapter Title:
{chapter_title}

Reference Pages:
{page_range}

Patterns Discovered In This Chapter (name: question count):
{pattern_summary}

Source Material:
{pdf_content}

────────────────────────

Generate markdown with the following sections.

# {{chapter_title}}

## What This Chapter Is About

2-3 sentences. State clearly:
- What real-world situation or mathematical domain this chapter deals with.
- The central quantity or relationship that ALL problems in this chapter
  revolve around.

No history, no motivation, no "in this chapter we will learn". Just
orient the student factually.

---

## Key Terms

A compact glossary of the 4-8 terms a student MUST know to read any
question in this chapter. Format:

**Term** — one-line definition, in plain English. If the term has a
standard formula attached to it, include it inline as `$...$`.

Only include terms that genuinely appear in questions of this chapter.
Do not add generic math terms (ratio, fraction, percentage) unless
they have a chapter-specific meaning here.

---

## Core Formulas

The 3-6 formulas that appear most frequently across ALL patterns in
this chapter. These are the chapter's building blocks — pattern-specific
formulas belong in each pattern's own note.

Use this format for each:

### [Formula Name]

$$
\text{{...}}
$$

*When to use:* one line — describe the scenario, not the math.

*Variables:* brief key for each symbol used.

Only include formulas genuinely needed across multiple question types.
If a formula is used by only one pattern, leave it for that pattern's note.

---

## How Patterns Connect

For each pattern listed under "Patterns Discovered In This Chapter",
write exactly ONE line:

**[Pattern Name]** — what kind of question this pattern covers,
written so a student can immediately tell it apart from the others.

List every pattern given to you, in the order given. Do not skip,
merge, or invent patterns. This is a navigation aid, not a description.

---

## Common Traps (Chapter-Wide)

2-4 mistakes that cut across ALL patterns in this chapter — things
students get wrong regardless of which pattern they're solving.
One bullet per trap, max 2 lines each. Do not repeat pattern-specific
traps that belong in the individual pattern notes.

If fewer than 2 genuine chapter-wide traps exist, skip this section.

────────────────────────

FORMATTING RULES:

* Use proper LaTeX for any formula (`$$...$$` for display, `$...$` inline).
* Never write a fraction as plain text — always `\frac{{a}}{{b}}`.
* Use concise markdown with bullets where listed above.
* No long paragraphs. Every section should be scannable in under a minute.
* Avoid textbook-style explanations or restating content that belongs
  in individual pattern notes.

Return only valid markdown. No preamble.
"""

# ─────────────────────────────────────────────────────────────────
# CHAPTER CHEATSHEET PROMPT  (improved density + structure)
# ─────────────────────────────────────────────────────────────────
CHAPTER_CHEATSHEET_PROMPT = r"""
You are an expert aptitude trainer writing a ONE-PAGE cheat sheet for
a student doing last-minute revision before an exam — they have
5-10 minutes for this entire chapter.

This is the densest, most compressed document in the set. Zero
explanations, zero teaching — pure lookup reference. If the student
has time to read only one document before the exam, this is it.

Chapter Title:
{chapter_title}

Patterns In This Chapter (name: question count):
{pattern_summary}

Extracted Data Per Pattern (formulas, mistakes, shortcuts — sourced directly from solved questions):
{enriched_context}

────────────────────────

Generate markdown with the following sections.

# {chapter_title} — Cheat Sheet

## Formula Bank

For EVERY pattern listed above, list its key formulas in display LaTeX.
Group by pattern with a bold label. Format:

**[Pattern Name]**
$$\text{{formula}}$$
*→ [4-word label for what this computes]*

List every pattern. Do not skip, merge, or invent patterns.
If a pattern has more than one essential formula, list all of them —
one formula per block.

---

## Recognition Table

A markdown table: 3 columns — Pattern | Trigger Keywords | What's Asked.

One row per pattern. Keep each cell to ≤6 words. This is the student's
first-pass scan when reading an exam question.

---

## Fastest Tricks

One bullet per trick. Format: **[Pattern or scenario]:** trick in ≤12 words.
Only include tricks that are genuinely faster than the standard method.
5-8 bullets max. No explanations.

---

## Trap Watch

One bullet per standout mistake. Format: **[Pattern]:** trap in ≤8 words.
Skip patterns where there's no memorable trap. Do not force one.

────────────────────────

FORMATTING RULES:

* Maximum density. No paragraphs, no intros, no summaries-of-summaries.
* Every formula in proper LaTeX (`$$...$$` display, `$...$` inline).
* Never write a plain-text fraction like 1/2 — always `\frac{{a}}{{b}}`.
* The table must be a real markdown table (pipe-delimited).
* This document must fit comfortably on one phone screen of scrolling
  per section. Cut content rather than cramming.

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
    Strips a leading 'Chapter_<number>_' prefix if present and
    replaces underscores with spaces.
    """
    cleaned = re.sub(r"^chapter_\d+_", "", stem, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned.title() if cleaned else stem


def format_pattern_questions(questions: list[dict], max_chars: int = 6000) -> str:
    """
    Format the actual questions belonging to one pattern for grounding
    the documentation prompt. Truncates by whole-question boundaries
    (never mid-question) once max_chars is reached.
    """
    blocks = []
    total_len = 0
    for q in questions:
        qnum = q.get("question_number", "?")
        qtext = q.get("question_text", q.get("question", ""))
        solution = q.get("solution", "") or q.get("traditional_solution", "")
        block = f"Q{qnum}: {qtext}\nSolution: {solution}"
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
        pdf_content=pdf_content[:2000],
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

    # Build pattern_name -> filename map up front so we can backfill
    # pattern_doc on every question regardless of skip_existing.
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
            documentation = generate_pattern_documentation(
                pattern_name=pattern_name,
                pattern_description=f"Pattern covering {len(pattern_questions)} problem types",
                question_count=len(pattern_questions),
                pdf_content=pdf_content,
                page_range=pdf_pages,
                pattern_questions=format_pattern_questions(pattern_questions),
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(documentation)

    # Backfill pattern_doc on every question in the categorized JSON,
    # then save — this is what lets the app link a question to its doc.
    for item in questions:
        pattern = item.get("sub_pattern") or "Uncategorized"
        item["pattern_doc"] = pattern_filenames.get(pattern, "")

    with open(categorized_file, "w", encoding="utf-8") as f:
        json.dump(data if isinstance(data, dict) else questions, f, indent=2, ensure_ascii=False)

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

    pattern_summary = "\n".join(
        f"- {pattern_name}: {len(qnums)} questions"
        for pattern_name, qnums in sorted(patterns_map.items())
    )

    prompt = CHAPTER_OVERVIEW_PROMPT.format(
        chapter_title=humanize_chapter_title(
            Path(categorized_file).stem.replace("_categorized", "")
        ),
        page_range=f"{pdf_pages[0]}-{pdf_pages[1]}",
        pdf_content=pdf_content[:5000],
        pattern_summary=pattern_summary,
    )

    overview = call_gemini(prompt)

    if not overview or len(overview.strip()) < 100:
        overview = "# Chapter Introduction\n\n*Failed to generate chapter introduction. Please retry.*"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(overview)

    print(f"  ✓ Overview: {output_file}")


def create_chapter_cheatsheet(
    categorized_file: str,
    pdf_path: str,
    pdf_pages: tuple,
    output_file: str = "CHAPTER_CHEATSHEET.md",
    overwrite: bool = True,
) -> None:
    """Create a chapter cheat sheet for the current chapter."""

    output_path = Path(output_file)
    if not overwrite and output_path.exists():
        print(f"  ✓ Cheat sheet already exists: {output_file}")
        return

    with open(categorized_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", []) if isinstance(data, dict) else data

    pdf_content = extract_pdf_pages(pdf_path, pdf_pages[0], pdf_pages[1])

    patterns_map = {}
    for item in questions:
        pattern = item.get("sub_pattern") or "Uncategorized"
        patterns_map.setdefault(pattern, []).append(item["question_number"])

    pattern_summary = "\n".join(
        f"- {pattern}: {len(qs)} questions"
        for pattern, qs in sorted(patterns_map.items())
    )

    prompt = CHAPTER_CHEATSHEET_PROMPT.format(
        chapter_title=humanize_chapter_title(
            Path(categorized_file).stem.replace("_categorized", "")
        ),
        pattern_summary=pattern_summary,
        pdf_content=pdf_content[:5000],
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


def build_cheatsheet_context(questions: list[dict]) -> dict[str, dict]:
    """
    Aggregate per-pattern data from the already-enriched JSON.
    Returns dict keyed by pattern name with formulas, mistakes, shortcuts.
    """
    patterns: dict[str, dict] = {}

    for q in questions:
        pattern = q.get("sub_pattern") or "Uncategorized"
        enrichment = q.get("ai_enrichment") or {}

        entry = patterns.setdefault(
            pattern,
            {"question_count": 0, "formulas": [], "common_mistakes": [], "shortcuts": []},
        )

        entry["question_count"] += 1

        for f in enrichment.get("formulas_used", []):
            if f and f not in entry["formulas"]:
                entry["formulas"].append(f)

        for m in enrichment.get("common_mistakes", []):
            if m and m not in entry["common_mistakes"]:
                entry["common_mistakes"].append(m)

        shortcut = (enrichment.get("shortcut_solution") or "").strip()
        if shortcut:
            first_sentence = re.split(r"(?<=[.!?])\s", shortcut)[0]
            if first_sentence and first_sentence not in entry["shortcuts"]:
                entry["shortcuts"].append(first_sentence)

    return patterns


def format_cheatsheet_context(patterns: dict[str, dict]) -> str:
    """Serialize aggregated pattern data into a compact text block for the prompt."""
    lines = []
    for pattern_name, data in sorted(patterns.items()):
        lines.append(f"### {pattern_name} ({data['question_count']} questions)")
        if data["formulas"]:
            lines.append("Formulas used:")
            for f in data["formulas"][:6]:
                lines.append(f"  - {f}")
        if data["common_mistakes"]:
            lines.append("Common mistakes:")
            for m in data["common_mistakes"][:3]:
                lines.append(f"  - {m}")
        if data["shortcuts"]:
            lines.append("Shortcuts:")
            for s in data["shortcuts"][:3]:
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
