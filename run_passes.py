"""
Main runner for categorization and documentation passes
Orchestrates the complete workflow
"""

import sys
import argparse
from pathlib import Path
from categorization_pass import run_categorization_pass
from documentation_pass import run_documentation_pass


def main():
    parser = argparse.ArgumentParser(
        description="Run categorization and documentation passes for Profit & Loss problems"
    )

    parser.add_argument(
        "--step",
        choices=["both", "categorize", "document"],
        default="both",
        help="Which step(s) to run",
    )

    parser.add_argument(
        "--input",
        default="ai_studio_input.json",
        help="Input JSON file with questions and solutions",
    )

    parser.add_argument(
        "--output",
        default="ai_studio_categorized.json",
        help="Output JSON file with sub_patterns added",
    )

    parser.add_argument(
        "--pdf", required=False, help="Path to PDF file for documentation"
    )

    parser.add_argument(
        "--pdf-start", type=int, required=False, help="PDF starting page number"
    )

    parser.add_argument(
        "--pdf-end", type=int, required=False, help="PDF ending page number"
    )

    parser.add_argument(
        "--docs-dir",
        default="pattern_docs",
        help="Output directory for pattern documentation",
    )

    args = parser.parse_args()

    # Step 1: Categorization
    if args.step in ["both", "categorize"]:
        print("\n" + "=" * 80)
        print("STEP 1: CATEGORIZATION")
        print("=" * 80)

        if not Path(args.input).exists():
            print(f"ERROR: Input file not found: {args.input}")
            sys.exit(1)

        run_categorization_pass(input_file=args.input, output_file=args.output)

    # Step 2: Documentation
    if args.step in ["both", "document"]:
        print("\n" + "=" * 80)
        print("STEP 2: DOCUMENTATION GENERATION")
        print("=" * 80)

        if not Path(args.output).exists():
            print(f"ERROR: Categorized file not found: {args.output}")
            print("Run with --step categorize first")
            sys.exit(1)

        if not args.pdf or args.pdf_start is None or args.pdf_end is None:
            print("ERROR: PDF documentation requires:")
            print("  --pdf <path>       Path to PDF file")
            print("  --pdf-start <page> Starting page")
            print("  --pdf-end <page>   Ending page")
            sys.exit(1)

        if not Path(args.pdf).exists():
            print(f"ERROR: PDF file not found: {args.pdf}")
            sys.exit(1)

        run_documentation_pass(
            categorized_file=args.output,
            pdf_path=args.pdf,
            pdf_start_page=args.pdf_start,
            pdf_end_page=args.pdf_end,
        )

    print("\n" + "=" * 80)
    print("WORKFLOW COMPLETE")
    print("=" * 80)
    if args.step in ["both", "categorize"]:
        print(f"✓ Categorized JSON: {args.output}")
    if args.step in ["both", "document"]:
        print(f"✓ Pattern docs: {args.docs_dir}/")
        print(f"✓ Overview: PATTERNS_OVERVIEW.md")


if __name__ == "__main__":
    main()
