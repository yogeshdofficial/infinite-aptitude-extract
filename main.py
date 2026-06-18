import json
import argparse
from pathlib import Path
from enrichment_utils import enrich_questions
from enrichment_utils import normalize_questions_ai_enrichment
from pypdf import PdfReader

from cache_utils import (
    ensure_output_dir,
    cache_batch,
    cache_final,
    load_existing_questions,
    load_batch_progress,
    save_batch_progress,
    export_flattened_ai_enrichment,
)

from gemini_utils import (
    create_client,
    RateLimiter,
    extract_questions,
    extract_answers,
)

from pdf_utils import (
    get_total_pages,
    parse_page_range,
    extract_page_range,
    build_batches,
)

from stitch import (
    dedup_questions,
    stitch_answers,
    find_missing_exercise_questions,
    chunk_questions,
)

from validator import validate_all
from categorization_pass import categorize_with_gemini, add_subpatterns_to_json
from documentation_pass import (
    create_pattern_markdown_files,
    create_main_pattern_overview,
    create_chapter_cheatsheet_v2,
)


def parse_args():

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--input-file")

    group.add_argument("--input-dir")

    parser.add_argument(
        "--output-dir",
        default="output_json",
    )

    parser.add_argument(
        "--question-pages",
        default="1-",
    )

    parser.add_argument(
        "--answer-pages",
        default=None,
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
    )

    parser.add_argument(
        "--overlap",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--answer-batch-size",
        type=int,
        default=20,
    )

    parser.add_argument(
        "--rpm",
        type=int,
        default=10,
    )

    parser.add_argument(
        "--model",
        default="gemini-3.1-flash-lite",
    )
    parser.add_argument(
        "--enrich-only",
        type=Path,
    )
    parser.add_argument(
        "--categorize",
        action="store_true",
        help="Run categorization pass (PASS 4)",
    )
    parser.add_argument(
        "--generate-docs",
        action="store_true",
        help="Generate documentation (PASS 5)",
    )
    parser.add_argument(
        "--pdf-pages",
        default=None,
        help="PDF pages for documentation (format: 1-10)",
    )
    return parser.parse_args()


def get_input_files(args):

    if args.input_file:

        return [Path(args.input_file)]

    return sorted(Path(args.input_dir).glob("*.pdf"))


def process_file(
    input_path,
    args,
    client,
    rate_limiter,
):

    print()
    print("=" * 60)
    print(input_path.name)
    print("=" * 60)

    output_dir = ensure_output_dir(args.output_dir)

    output_path = output_dir / f"{input_path.stem}.json"

    progress_path = output_dir / f"{input_path.stem}.progress.json"

    reader = PdfReader(str(input_path))

    total_pages = get_total_pages(reader)

    q_start, q_end = parse_page_range(
        args.question_pages,
        total_pages,
    )

    all_questions = load_existing_questions(output_path)

    progress = load_batch_progress(progress_path)

    completed_batches = set(progress["completed_batches"])

    if args.enrich_only:

        with open(
            args.enrich_only,
            encoding="utf-8",
        ) as f:

            all_questions = json.load(f)

        for q in all_questions:

            q["ai_enrichment"] = {}

        print("\nPASS 3: AI enrichment")

        all_questions = enrich_questions(
            client=client,
            model=args.model,
            chapter_name=args.enrich_only.stem,
            questions=all_questions,
            rate_limiter=rate_limiter,
        )

        normalize_questions_ai_enrichment(
            all_questions,
            args.enrich_only.stem,
        )

        cache_batch(
            chapter_title=args.enrich_only.stem,
            questions=all_questions,
            output_path=args.enrich_only,
        )
        export_flattened_ai_enrichment(args.enrich_only)

        print(
            "\nSaved to",
            args.enrich_only,
        )

        return

    # PASS 1
    print()
    print("PASS 1: extracting questions")

    batch_iterator = list(
        build_batches(
            q_start,
            q_end,
            args.batch_size,
            args.overlap,
        )
    )

    for batch_num, (start_page, end_page) in enumerate(
        batch_iterator,
        start=1,
    ):

        if batch_num in completed_batches:

            print(f"Skipping batch {batch_num}")

            continue

        print(f"Batch {batch_num}: pages {start_page}-{end_page}")

        pdf_bytes = extract_page_range(
            reader,
            start_page,
            end_page,
        )

        questions = extract_questions(
            client=client,
            model=args.model,
            pdf_bytes=pdf_bytes,
            start_page=start_page,
            end_page=end_page,
            rate_limiter=rate_limiter,
        )

        print(f"  -> {len(questions)} questions")

        if questions:

            all_questions.extend(questions)

            all_questions = dedup_questions(all_questions)

            cache_batch(
                chapter_title=input_path.stem,
                questions=all_questions,
                output_path=output_path,
            )

        completed_batches.add(batch_num)

        save_batch_progress(
            progress_path,
            sorted(completed_batches),
        )

    all_questions = dedup_questions(all_questions)

    print()
    print(f"Pass 1 complete: {len(all_questions)} questions")

    # PASS 2
    if args.answer_pages:

        print()
        print("PASS 2: answer stitching")

        a_start, a_end = parse_page_range(
            args.answer_pages,
            total_pages,
        )

        answer_pdf = extract_page_range(
            reader,
            a_start,
            a_end,
        )

        previous_missing = None

        round_num = 1

        while True:

            missing_questions = find_missing_exercise_questions(all_questions)

            missing_count = len(missing_questions)

            print()
            print(f"Round {round_num}: {missing_count} missing")

            if missing_count == 0:
                break

            if previous_missing == missing_count:

                print("No further progress.")

                break

            previous_missing = missing_count

            total_stitched_this_round = 0

            for chunk in chunk_questions(
                missing_questions,
                args.answer_batch_size,
            ):

                qnums = [q["question_number"] for q in chunk]

                answers = extract_answers(
                    client=client,
                    model=args.model,
                    pdf_bytes=answer_pdf,
                    missing_question_numbers=qnums,
                    rate_limiter=rate_limiter,
                )

                stitched = stitch_answers(
                    all_questions,
                    answers,
                )

                total_stitched_this_round += stitched

                print(f"  chunk stitched {stitched}")

            print(f"Round {round_num} stitched " f"{total_stitched_this_round}")

            cache_batch(
                chapter_title=input_path.stem,
                questions=all_questions,
                output_path=output_path,
            )

            round_num += 1
    # PASS 3
    print()
    print("PASS 3: AI enrichment")

    all_questions = enrich_questions(
        client=client,
        model=args.model,
        chapter_name=input_path.stem,
        questions=all_questions,
        rate_limiter=rate_limiter,
    )

    normalize_questions_ai_enrichment(
        all_questions,
        input_path.stem,
    )
    # VALIDATION
    print()
    print("VALIDATION")

    report = validate_all(
        all_questions,
        total_pages,
    )

    for key, value in report.items():

        print(f"{key}: {len(value)}")

        if value:

            print(value[:10])

        # FINAL SAVE
    cache_final(
        chapter_title=input_path.stem,
        source_file=input_path.name,
        total_pages=total_pages,
        questions=all_questions,
        output_path=output_path,
    )
    export_flattened_ai_enrichment(output_path)

    print()
    print(f"Saved to {output_path}")

    # PASS 4: CATEGORIZATION
    if args.categorize:
        print()
        print("PASS 4: Categorization into sub-patterns")

        categorized_path = output_dir / f"{input_path.stem}_categorized.json"

        if categorized_path.exists():
            print(f"  → Resuming from existing categorized file: {categorized_path}")
            export_flattened_ai_enrichment(categorized_path)
            output_path = categorized_path
        else:
            # Extract Q&S pairs
            qs_pairs = [
                {
                    "section": q["section"],
                    "question_number": q["question_number"],
                    "question_text": q.get("question_text", q.get("question", "")),
                    "solution": q.get("solution", ""),
                }
                for q in all_questions
            ]

            # Get categorization from Gemini
            categorization = categorize_with_gemini(qs_pairs)

            if categorization:
                print(
                    f"  → {len(categorization['sub_patterns'])} sub-patterns identified:"
                )
                for pattern in categorization["sub_patterns"]:
                    print(
                        f"     - {pattern['pattern_name']}: {len(pattern['question_numbers'])} questions"
                    )

                # Add sub_pattern field
                add_subpatterns_to_json(
                    input_file=output_path,
                    output_file=categorized_path,
                    categorization=categorization,
                )

                print(f"  → Categorized JSON: {categorized_path}")
                export_flattened_ai_enrichment(categorized_path)
                output_path = categorized_path  # Update for next pass
            else:
                raise RuntimeError(
                    "Categorization (Pass 4) failed to produce any patterns. "
                    "Refusing to continue with --generate-docs, since Pass 5 "
                    "groups documentation strictly by sub_pattern, and every "
                    "question would otherwise be silently written as "
                    "'Uncategorized'. Re-run with --categorize once the "
                    "underlying API/parsing issue is fixed."
                )

    # PASS 5: DOCUMENTATION GENERATION
    if args.generate_docs:
        if not args.pdf_pages:
            print()
            print("WARNING: --generate-docs requires --pdf-pages (format: 1-10)")
        else:
            print()
            print("PASS 5: Generating pattern documentation")

            # Parse page range
            pages = args.pdf_pages.split("-")
            pdf_start = int(pages[0])
            pdf_end = int(pages[1]) if len(pages) > 1 else pdf_start

            docs_dir = output_dir / f"{input_path.stem}_docs"

            print(f"  → Creating markdown docs from pages {pdf_start}-{pdf_end}")
            print(f"  → Output directory: {docs_dir}")

            create_pattern_markdown_files(
                categorized_file=str(output_path),
                pdf_path=str(input_path),
                pdf_pages=(pdf_start, pdf_end),
                output_dir=str(docs_dir),
                skip_existing=True,
            )

            create_main_pattern_overview(
                categorized_file=str(output_path),
                pdf_path=str(input_path),
                pdf_pages=(pdf_start, pdf_end),
                output_file=str(output_dir / f"{input_path.stem}_PATTERNS_OVERVIEW.md"),
                overwrite=False,
            )

            create_chapter_cheatsheet_v2(
                categorized_file=str(output_path),
                output_file=str(output_dir / f"{input_path.stem}_CHEATSHEET.md"),
                overwrite=False,
            )


def main():

    args = parse_args()

    input_files = get_input_files(args)

    client = create_client()

    rate_limiter = RateLimiter(args.rpm)

    print(f"Found {len(input_files)} PDF(s)")

    for input_path in input_files:

        try:

            process_file(
                input_path,
                args,
                client,
                rate_limiter,
            )

        except Exception as e:

            print()
            print(f"FAILED: {input_path.name}")

            print(e)


if __name__ == "__main__":
    main()
