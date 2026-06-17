"""
Documentation Generation Pass: Create markdown files for each sub-pattern
"""

import json
import re
from pathlib import Path
from typing import Optional
from gemini_utils import call_gemini
import PyPDF2

PATTERN_DOC_PROMPT = """
You are an expert mathematics educator and aptitude trainer.

Create a concise but high-quality markdown revision note for this pattern.

The goal is to help students quickly understand and solve most questions belonging to this pattern.

Do NOT write like a textbook.

Prefer formulas, frameworks, tricks, and recognition clues over lengthy explanations.

Pattern Name: {pattern_name}

Pattern Description:
{pattern_description}

Reference Pages:
{page_range}

Source Material:
{pdf_content}

────────────────────────

Generate markdown with the following sections.

# {{pattern_name}}

## Overview

Explain briefly:

* What this pattern represents.
* What kind of questions belong here.
* The central idea used to solve them.

Maximum 3 short paragraphs.

---

## Recognition Clues

List:

* keywords,
* phrases,
* common problem structures,
* what is usually GIVEN,
* what is usually FOUND.

Use bullets.

---

## Important Formulas

List ALL important formulas relevant to this pattern.

Include all useful variations and derived formulas whenever appropriate.

Use proper LaTeX.

For each formula:

* formula,
* meaning,
* when to use it.

Example:

### Effective Capital

$$
\text{{Effective Capital}}
=
\text{{Capital}}
\times
\text{{Time}}
$$

### Profit Share

$$
\frac{{P_1}}{{P_2}}
=

\frac{{C_1T_1}}{{C_2T_2}}
$$

Mention alternate forms and rearrangements whenever useful.

More formulas are acceptable if they are genuinely useful.

---

## Solution Framework

Give the standard solving approach.

Use numbered steps.

Keep it concise.

Students should be able to memorize this framework.

---

## Shortcut Tricks

Include practical competitive exam tricks.

Focus on:

* ratio tricks,
* symmetry,
* simplifications,
* elimination,
* common observations,
* mental math.

Include only genuinely useful tricks.

---

## Common Mistakes

List 5-10 common mistakes.

Mention:

* mistake,
* why it happens,
* how to avoid it.

Keep each point short.

---

## Similar Patterns

Mention nearby patterns and how to distinguish them.

Focus on recognition clues.

Keep this section brief.

---

## Revision Summary

Provide a cheat sheet.

### Key Formula

...

### Recognition Signal

...

### Main Trick

...

### Common Trap

...

────────────────────────

Rules:

* Use concise markdown.
* Use bullets heavily.
* Use proper LaTeX for formulas.
* Prefer formulas over long explanations.
* Include useful formula variations.
* Avoid unnecessary theory.
* Avoid historical discussion.
* Optimize for revision and problem solving.
* Keep the document compact but information-dense.

Return only valid markdown.
"""

CHAPTER_OVERVIEW_PROMPT = """
You are an expert mathematics educator and aptitude trainer.

Create a concise and high-quality chapter overview in markdown.

The document should act as a roadmap and revision sheet for the chapter.

Do NOT write like a textbook.

Prefer formulas, tricks, and pattern recognition over lengthy explanations.

Chapter Title:
{chapter_title}

Reference Pages:
{page_range}

Source Material:
{pdf_content}

Pattern Summary:
{pattern_summary}

────────────────────────

Generate markdown with the following sections.

# {{chapter_title}}

## Chapter Overview

Explain briefly:

* What this chapter is about.
* The central idea behind the chapter.
* Why the chapter matters.

Maximum 3 short paragraphs.

---

## Core Concepts

Explain the major ideas of the chapter.

Use bullets.

Keep explanations short.

---

## Important Formulas

List ALL important formulas of the chapter.

Use proper LaTeX.

Include useful variations and derived formulas whenever appropriate.

For each formula mention:

* formula,
* meaning,
* when to use it.

More formulas are acceptable if they are genuinely useful.

---

## Shortcut Tricks

Include useful competitive exam tricks.

Focus on:

* ratio tricks,
* symmetry,
* simplifications,
* observations,
* elimination tricks,
* mental math shortcuts.

Include only genuinely useful tricks.

---

## Pattern Map

Briefly list the major patterns discovered in this chapter.

For each pattern mention:

* what kind of questions belong to it,
* one recognition clue.

Keep this section concise.

---

## Problem Recognition Guide

Mention:

* common keywords,
* common question structures,
* what is usually GIVEN,
* what is usually FOUND.

Use bullets.

---

## Common Mistakes

List 5-10 common mistakes students make in this chapter.

For each:

* mistake,
* why it happens,
* how to avoid it.

Keep each point short.

---

## Revision Sheet

Provide a very compact cheat sheet.

### Most Important Formula

...

### Main Idea

...

### Fast Trick

...

### Biggest Trap

...

────────────────────────

Rules:

* Use concise markdown.
* Use bullets heavily.
* Use proper LaTeX for formulas.
* Include useful formula variations.
* Avoid unnecessary theory.
* Avoid historical discussion.
* Avoid textbook style.
* Keep the document compact but information-dense.
* Optimize for revision and problem solving.
* Make the notes genuinely useful for competitive exams.

Return only valid markdown.
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


def generate_pattern_documentation(
    pattern_name: str,
    pattern_description: str,
    question_count: int,
    pdf_content: str,
    page_range: tuple,
) -> str:
    """Generate markdown documentation for a pattern using Gemini."""

    prompt = PATTERN_DOC_PROMPT.format(
        pattern_name=pattern_name,
        pattern_description=pattern_description,
        question_count=question_count,
        page_range=f"{page_range[0]}-{page_range[1]}",
        pdf_content=pdf_content[:2000],  # Include more PDF context
    )

    try:
        documentation = call_gemini(prompt)

        # Validate that documentation has content
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

    # Load categorized data
    with open(categorized_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data.get("questions", []) if isinstance(data, dict) else data

    # Extract PDF content
    pdf_content = extract_pdf_pages(pdf_path, pdf_pages[0], pdf_pages[1])

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Identify unique patterns
    patterns_map = {}
    for item in questions:
        pattern = item.get("sub_pattern", "Uncategorized")
        if pattern not in patterns_map:
            patterns_map[pattern] = []
        patterns_map[pattern].append(item["question_number"])

    # Generate markdown for each pattern
    for idx, (pattern_name, question_numbers) in enumerate(patterns_map.items(), 1):
        print(f"  [{idx}/{len(patterns_map)}] {pattern_name}...")

        # Create filename early so resume mode can skip the Gemini call entirely.
        filename = safe_filename_stem(pattern_name) + ".md"
        filepath = output_path / filename

        if skip_existing and filepath.exists():
            print(f"    → Skipping existing file: {filepath.name}")
            continue

        # Generate documentation
        documentation = generate_pattern_documentation(
            pattern_name=pattern_name,
            pattern_description=f"Pattern covering {len(question_numbers)} problem types",
            question_count=len(question_numbers),
            pdf_content=pdf_content,
            page_range=pdf_pages,
        )

        # Save markdown
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(documentation)


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
        pattern = item.get("sub_pattern", "Uncategorized")
        if pattern not in patterns_map:
            patterns_map[pattern] = []
        patterns_map[pattern].append(item["question_number"])

    pattern_summary = "\n".join(
        f"- {pattern}: {len(questions)} questions"
        for pattern, questions in sorted(patterns_map.items())
    )

    prompt = CHAPTER_OVERVIEW_PROMPT.format(
        chapter_title=Path(categorized_file).stem.replace("_categorized", ""),
        page_range=f"{pdf_pages[0]}-{pdf_pages[1]}",
        pdf_content=pdf_content[:5000],
        pattern_summary=pattern_summary,
    )

    overview = call_gemini(prompt)

    if not overview or len(overview.strip()) < 100:
        overview = "# Chapter Introduction\n\n*Failed to generate chapter introduction. Please retry.*"

    # Save
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(overview)

    print(f"  ✓ Overview: {output_file}")
