import json
import subprocess
import sys
from pathlib import Path

DB_FILE = Path("infinite_aptitude.db")

FIELDS_TO_DELETE = [
    "pattern",
    "subpattern",
    "canonical_method",
    "concepts",
    "prerequisites",
    "related_patterns",
    "confusing_patterns",
]


def run_command(cmd):
    print("Executing:", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True)


def recreate_database():
    if DB_FILE.exists():
        DB_FILE.unlink()
        print(f"Removed existing database: {DB_FILE}")


def insert_json_rows(table_name, rows):
    if not rows:
        return

    temp_file = Path(f"temp_{table_name}.json")
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False)

    try:
        run_command(
            [
                "sqlite-utils",
                "insert",
                str(DB_FILE),
                table_name,
                str(temp_file),
                "--pk=id",
                "--replace",
            ]
        )
    finally:
        if temp_file.exists():
            temp_file.unlink()


def process_questions(root_dir):
    json_files = list(root_dir.rglob("*categorized_ai_enriched_flattened.json"))

    if not json_files:
        print("No categorized_ai_enriched_flattened.json files found.")
        return

    for json_file in json_files:
        print(f"Processing questions: {json_file.name}")

        del_fields = ", ".join(f".{field}" for field in FIELDS_TO_DELETE)
        jq_filter = f"""
        .items
        | map(del({del_fields}))
        | to_entries
        | map(.value + {{
            id: (
                .value.chapter_title
                + "_" + (.value.question_number | tostring)
                + "_" + ((.key + 1) | tostring)
            )
        }})
        """

        temp_file = Path("temp_processed_questions.json")

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                subprocess.run(
                    ["jq", jq_filter, str(json_file)],
                    stdout=f,
                    check=True,
                )

            run_command(
                [
                    "sqlite-utils",
                    "insert",
                    str(DB_FILE),
                    "questions",
                    str(temp_file),
                    "--pk=id",
                    "--replace",
                ]
            )
        finally:
            if temp_file.exists():
                temp_file.unlink()


def process_markdown_files(root_dir):
    cheatsheets = []
    overviews = []
    docs = []

    for md_file in root_dir.rglob("*.md"):
        name = md_file.name

        if name.endswith("_CHEATSHEET.md"):
            cheatsheets.append(
                {
                    "id": md_file.stem.removesuffix("_CHEATSHEET"),
                    "markdown": md_file.read_text(encoding="utf-8"),
                }
            )
            continue

        if name.endswith("_PATTERNS_OVERVIEW.md"):
            overviews.append(
                {
                    "id": md_file.stem.removesuffix("_PATTERNS_OVERVIEW"),
                    "markdown": md_file.read_text(encoding="utf-8"),
                }
            )
            continue

        if md_file.parent.name.endswith("_docs"):
            chapter_name = md_file.parent.name.removesuffix("_docs")
            docs.append(
                {
                    "id": f"{chapter_name}_{md_file.stem}",
                    "chapter": chapter_name,
                    "doc_name": md_file.stem,
                    "markdown": md_file.read_text(encoding="utf-8"),
                }
            )

    insert_json_rows("chapter_cheatsheets", cheatsheets)
    insert_json_rows("chapter_overviews", overviews)
    insert_json_rows("chapter_docs", docs)


def main():
    if len(sys.argv) < 2:
        print("Usage: python sqlite.py <path_to_output_json_folder>")
        sys.exit(1)

    root_dir = Path(sys.argv[1]).resolve()

    if not root_dir.exists():
        print(f"Error: folder does not exist: {root_dir}")
        sys.exit(1)

    recreate_database()
    print(f"Starting ingestion from: {root_dir}")
    print(f"Target database: {DB_FILE}")

    process_questions(root_dir)
    process_markdown_files(root_dir)

    print("Processing complete successfully.")


if __name__ == "__main__":
    main()
