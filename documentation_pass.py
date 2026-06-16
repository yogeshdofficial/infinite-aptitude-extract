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
You are an expert mathematics educator creating comprehensive learning material.

Create detailed markdown documentation for this sub-pattern:

**Pattern Name:** {pattern_name}
**Type:** {pattern_description}
**Related Problems:** {question_count}
**Reference:** Pages {page_range}

**Available Context:**
{pdf_content}

---

GENERATE MARKDOWN WITH THESE SECTIONS:

## 1. Pattern Overview
- One clear sentence defining what this pattern solves
- Why this pattern matters

## 2. Key Formulas
- Display ALL relevant formulas using $$formula$$
- Label each formula clearly
- Use proper mathematical notation
- Example: $$\\text{{Profit %}} = \\frac{{Profit}}{{Cost Price}} \\times 100$$

## 3. When to Use This Pattern
- List specific keywords/phrases that signal this pattern
- Recognition clues from problem statements
- What's typically GIVEN and what's to be FOUND

## 3. Core Concept & Theory
- Explain the fundamental idea
- Why the approach works

## 5. Step-by-Step Solution Method
- Number each step with explanation of WHAT and WHY
- Show which formula to use at each step
- Include decision branches

## 6. Worked Examples (2-3 complete)
- Show full working with all steps
- Explain reasoning at each step
- Format:
  **Example 1: [Description]**
  Given: ...
  Solution: [Full working]

## 7. Recognition Clues & Keywords
- Phrases that signal this pattern
- When to apply this pattern
- What NOT to confuse with

## 8. Common Mistakes (3-4)
- Frequent errors students make
- Why they're wrong
- How to avoid them

## 9. Practice Tips
- How to master this pattern
- Related patterns to study

---

RULES:
- Use # ## ### for headers
- Use $math$ for inline, $$math$$ for display
- Make formulas CLEAR and COMPLETE
- Use **bold** for key terms
- Be pedagogical - explain reasoning
- Suitable for first-time learners
- Include ALL relevant formulas

Return ONLY valid markdown (no code fences or extra text).
"""


CHAPTER_OVERVIEW_PROMPT = """
You are an expert mathematics educator creating an introduction page for a chapter.

Write a clear chapter introduction in markdown for:

**Chapter Title:** {chapter_title}
**Reference Pages:** {page_range}

Use the source text below as the only reference material:
{pdf_content}

The document must feel like a useful study guide, not a file index.

Include these sections:

## 1. Chapter Introduction
- What this chapter is about
- Why the topic matters

## 2. Core Ideas
- Explain the main ideas in simple language
- Mention the typical situations covered in the chapter

## 3. Important Formulas
- List the key formulas clearly
- Use display math for formulas
- Add a short note on when each formula is used

## 4. Important Facts and Shortcuts
- Summarize rules, patterns, and quick observations from the chapter
- Keep them practical for revision

## 5. How to Recognize the Problem Type
- Mention keywords or clues from questions
- Relate them to the chapter patterns

## 6. Common Mistakes
- List 3-5 common mistakes students make

## 7. Chapter Pattern Map
- Briefly mention the major sub-patterns discovered in this chapter
- Keep this short, as supporting context only

Rules:
- Use markdown headings
- Keep the language crisp and student-friendly
- Do not mention that the text was extracted from a PDF
- Do not produce a table of contents or a generic outline
- Include only content supported by the provided source text
- Return only valid markdown
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
        pdf_content=(
            f"{pdf_content[:5000]}\n\nChapter pattern summary:\n{pattern_summary}"
        ),
    )

    overview = call_gemini(prompt)

    if not overview or len(overview.strip()) < 100:
        overview = "# Chapter Introduction\n\n*Failed to generate chapter introduction. Please retry.*"

    # Save
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(overview)

    print(f"  ✓ Overview: {output_file}")
