"""
sqlite.py  –  InfiniteAptitude database builder

Schema
──────
  chapters          one row per chapter
  patterns          one row per sub-pattern,        FK → chapters
  pattern_docs      markdown revision note,         FK → chapters, patterns
  questions         one row per question,           FK → chapters, patterns
  question_hints    one row per hint,               FK → questions
  question_formulas one row per formula,            FK → questions
  question_mistakes one row per common mistake,     FK → questions
  chapter_resources cheatsheet / overview markdown, FK → chapters

Usage
─────
  python sqlite.py <path_to_output_folder>

Globs for:
  *_categorized_ai_enriched_flattened.json  → questions + patterns
  *_CHEATSHEET.md                           → chapter_resources (type=cheatsheet)
  *_PATTERNS_OVERVIEW.md                    → chapter_resources (type=overview)
  *_docs/*.md                               → pattern_docs
"""

import json
import re
import sqlite3
import sys
from pathlib import Path

DB_FILE = Path("infinite_aptitude.db")

# ─────────────────────────────────────────────────────────────────────────────
# helpers
# ─────────────────────────────────────────────────────────────────────────────


def slugify(text: str) -> str:
    """'Profit Loss Percent' → 'profit_loss_percent'"""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_") or "unknown"


def parse_chapter_title(chapter_title: str) -> tuple[str, str, int | None]:
    """
    'Chapter_12_Profit_and_Loss' → (id='profit_and_loss',
                                    display_name='Profit and Loss',
                                    number=12)
    """
    cleaned = re.sub(r"^Chapter_\d+_", "", chapter_title, flags=re.IGNORECASE)
    display_name = cleaned.replace("_", " ")
    chapter_id = slugify(display_name)
    m = re.match(r"^Chapter_(\d+)_", chapter_title, flags=re.IGNORECASE)
    number = int(m.group(1)) if m else None
    return chapter_id, display_name, number


def parse_json_array(value) -> list[str]:
    """
    Pipeline stores hints/formulas/mistakes as a JSON-encoded string.
    Handles both already-decoded lists and raw strings robustly.
    """
    if isinstance(value, list):
        return [str(v) for v in value if v]
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return []
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return [str(v) for v in parsed if v]
        except json.JSONDecodeError:
            pass
        return [value]  # single-item fallback
    return []


# ─────────────────────────────────────────────────────────────────────────────
# schema
# ─────────────────────────────────────────────────────────────────────────────

DDL = """
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE chapters (
    id           TEXT PRIMARY KEY,  -- slug: 'profit_and_loss'
    display_name TEXT NOT NULL,     -- 'Profit and Loss'
    number       INTEGER            -- 12
);

CREATE TABLE patterns (
    id         TEXT PRIMARY KEY,    -- '{chapter_id}__{pattern_slug}'
    chapter_id TEXT NOT NULL REFERENCES chapters(id),
    name       TEXT NOT NULL        -- 'Profit Loss Percent'
);

CREATE TABLE pattern_docs (
    id         TEXT PRIMARY KEY,    -- '{chapter_id}__{doc_slug}'
    chapter_id TEXT NOT NULL REFERENCES chapters(id),
    pattern_id TEXT      REFERENCES patterns(id),  -- NULL if no matching pattern
    markdown   TEXT NOT NULL
);

CREATE TABLE questions (
    id                   TEXT    PRIMARY KEY,
    chapter_id           TEXT    NOT NULL REFERENCES chapters(id),
    pattern_id           TEXT             REFERENCES patterns(id),
    question_number      TEXT    NOT NULL,
    difficulty           TEXT    CHECK(difficulty IN ('easy', 'medium', 'hard')),
    question_text        TEXT,
    option_a             TEXT,
    option_b             TEXT,
    option_c             TEXT,
    option_d             TEXT,
    correct_option       TEXT,
    final_answer         TEXT,
    traditional_solution TEXT,
    shortcut_solution    TEXT
);

CREATE TABLE question_hints (
    id          INTEGER PRIMARY KEY,
    question_id TEXT    NOT NULL REFERENCES questions(id),
    hint        TEXT    NOT NULL
);

CREATE TABLE question_formulas (
    id          INTEGER PRIMARY KEY,
    question_id TEXT    NOT NULL REFERENCES questions(id),
    formula     TEXT    NOT NULL
);

CREATE TABLE question_mistakes (
    id          INTEGER PRIMARY KEY,
    question_id TEXT    NOT NULL REFERENCES questions(id),
    mistake     TEXT    NOT NULL
);

CREATE TABLE chapter_resources (
    id            INTEGER PRIMARY KEY,
    chapter_id    TEXT    NOT NULL REFERENCES chapters(id),
    resource_type TEXT    NOT NULL CHECK(resource_type IN ('cheatsheet', 'overview')),
    markdown      TEXT    NOT NULL,
    UNIQUE(chapter_id, resource_type)
);

-- indexes on every FK column that isn't already a PK
CREATE INDEX idx_patterns_chapter          ON patterns(chapter_id);
CREATE INDEX idx_pattern_docs_chapter      ON pattern_docs(chapter_id);
CREATE INDEX idx_pattern_docs_pattern      ON pattern_docs(pattern_id);
CREATE INDEX idx_questions_chapter         ON questions(chapter_id);
CREATE INDEX idx_questions_pattern         ON questions(pattern_id);
CREATE INDEX idx_question_hints_question   ON question_hints(question_id);
CREATE INDEX idx_question_formulas_question ON question_formulas(question_id);
CREATE INDEX idx_question_mistakes_question ON question_mistakes(question_id);
CREATE INDEX idx_chapter_resources_chapter  ON chapter_resources(chapter_id);
"""


# ─────────────────────────────────────────────────────────────────────────────
# setup
# ─────────────────────────────────────────────────────────────────────────────


def open_db() -> sqlite3.Connection:
    if DB_FILE.exists():
        DB_FILE.unlink()
        print(f"Removed existing: {DB_FILE}")
    con = sqlite3.connect(DB_FILE)
    con.executescript(DDL)
    con.commit()
    print(f"Created schema:   {DB_FILE}")
    return con


# ─────────────────────────────────────────────────────────────────────────────
# upsert helpers
# ─────────────────────────────────────────────────────────────────────────────


def upsert_chapter(con: sqlite3.Connection, chapter_title: str) -> str:
    chapter_id, display_name, number = parse_chapter_title(chapter_title)
    con.execute(
        """
        INSERT INTO chapters(id, display_name, number) VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            display_name = excluded.display_name,
            number       = excluded.number
        """,
        (chapter_id, display_name, number),
    )
    return chapter_id


def upsert_pattern(con: sqlite3.Connection, chapter_id: str, name: str) -> str:
    pattern_id = f"{chapter_id}__{slugify(name)}"
    con.execute(
        "INSERT INTO patterns(id, chapter_id, name) VALUES (?,?,?) ON CONFLICT(id) DO NOTHING",
        (pattern_id, chapter_id, name),
    )
    return pattern_id


# ─────────────────────────────────────────────────────────────────────────────
# ingestion
# ─────────────────────────────────────────────────────────────────────────────


def process_questions(con: sqlite3.Connection, root_dir: Path) -> None:
    json_files = sorted(root_dir.rglob("*categorized_ai_enriched_flattened.json"))
    if not json_files:
        print("No *_categorized_ai_enriched_flattened.json files found.")
        return

    for json_file in json_files:
        print(f"Questions: {json_file.name}")
        data = json.loads(json_file.read_text(encoding="utf-8"))
        chapter_title = data.get("chapter_title", "")
        items = data.get("items", [])

        if not chapter_title:
            print(f"  WARNING: missing chapter_title, skipping.")
            continue

        chapter_id = upsert_chapter(con, chapter_title)

        for idx, item in enumerate(items, start=1):
            pattern_id = upsert_pattern(
                con, chapter_id, item.get("sub_pattern") or "Uncategorized"
            )
            # chapter_id__qnum__position — position breaks the se/ex tie
            # (both sections restart numbering at 1)
            question_id = f"{chapter_id}__{item.get('question_number', '')}_{idx}"

            con.execute(
                """
                INSERT INTO questions(
                    id, chapter_id, pattern_id, question_number, difficulty,
                    question_text, option_a, option_b, option_c, option_d,
                    correct_option, final_answer,
                    traditional_solution, shortcut_solution
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET
                    pattern_id           = excluded.pattern_id,
                    difficulty           = excluded.difficulty,
                    question_text        = excluded.question_text,
                    option_a             = excluded.option_a,
                    option_b             = excluded.option_b,
                    option_c             = excluded.option_c,
                    option_d             = excluded.option_d,
                    correct_option       = excluded.correct_option,
                    final_answer         = excluded.final_answer,
                    traditional_solution = excluded.traditional_solution,
                    shortcut_solution    = excluded.shortcut_solution
                """,
                (
                    question_id,
                    chapter_id,
                    pattern_id,
                    str(item.get("question_number", "")),
                    item.get("difficulty"),
                    item.get("paraphrased_question"),
                    item.get("paraphrased_option_a"),
                    item.get("paraphrased_option_b"),
                    item.get("paraphrased_option_c"),
                    item.get("paraphrased_option_d"),
                    item.get("paraphrased_correct_option"),
                    item.get("paraphrased_final_answer"),
                    item.get("traditional_solution"),
                    item.get("shortcut_solution"),
                ),
            )

            # child rows: delete-then-insert so replays stay clean
            con.execute(
                "DELETE FROM question_hints    WHERE question_id=?", (question_id,)
            )
            con.execute(
                "DELETE FROM question_formulas WHERE question_id=?", (question_id,)
            )
            con.execute(
                "DELETE FROM question_mistakes WHERE question_id=?", (question_id,)
            )

            con.executemany(
                "INSERT INTO question_hints(question_id, hint) VALUES (?,?)",
                [(question_id, h) for h in parse_json_array(item.get("hints"))],
            )
            con.executemany(
                "INSERT INTO question_formulas(question_id, formula) VALUES (?,?)",
                [(question_id, f) for f in parse_json_array(item.get("formulas_used"))],
            )
            con.executemany(
                "INSERT INTO question_mistakes(question_id, mistake) VALUES (?,?)",
                [
                    (question_id, m)
                    for m in parse_json_array(item.get("common_mistakes"))
                ],
            )

        con.commit()
        print(f"  → {len(items)} questions  (chapter: {chapter_id})")


def process_markdown_files(con: sqlite3.Connection, root_dir: Path) -> None:
    for md_file in sorted(root_dir.rglob("*.md")):
        name = md_file.name

        # ── cheatsheet ───────────────────────────────────────────────────────
        if name.endswith("_CHEATSHEET.md"):
            chapter_id = upsert_chapter(con, md_file.stem.removesuffix("_CHEATSHEET"))
            con.execute(
                """
                INSERT INTO chapter_resources(chapter_id, resource_type, markdown)
                VALUES (?,?,?)
                ON CONFLICT(chapter_id, resource_type) DO UPDATE SET markdown = excluded.markdown
                """,
                (chapter_id, "cheatsheet", md_file.read_text(encoding="utf-8")),
            )
            print(f"  cheatsheet  → {chapter_id}")
            continue

        # ── patterns overview ────────────────────────────────────────────────
        if name.endswith("_PATTERNS_OVERVIEW.md"):
            chapter_id = upsert_chapter(
                con, md_file.stem.removesuffix("_PATTERNS_OVERVIEW")
            )
            con.execute(
                """
                INSERT INTO chapter_resources(chapter_id, resource_type, markdown)
                VALUES (?,?,?)
                ON CONFLICT(chapter_id, resource_type) DO UPDATE SET markdown = excluded.markdown
                """,
                (chapter_id, "overview", md_file.read_text(encoding="utf-8")),
            )
            print(f"  overview    → {chapter_id}")
            continue

        # ── pattern doc  (<chapter_title>_docs/<pattern_slug>.md) ───────────
        if md_file.parent.name.endswith("_docs"):
            chapter_id = upsert_chapter(con, md_file.parent.name.removesuffix("_docs"))
            doc_id = f"{chapter_id}__{md_file.stem}"

            # resolve pattern FK if the pattern row already exists
            row = con.execute(
                "SELECT id FROM patterns WHERE id=?", (doc_id,)
            ).fetchone()
            pattern_id = doc_id if row else None

            con.execute(
                """
                INSERT INTO pattern_docs(id, chapter_id, pattern_id, markdown)
                VALUES (?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET
                    pattern_id = excluded.pattern_id,
                    markdown   = excluded.markdown
                """,
                (doc_id, chapter_id, pattern_id, md_file.read_text(encoding="utf-8")),
            )
            print(f"  pattern_doc → {doc_id}")

    con.commit()


def backfill_pattern_doc_links(con: sqlite3.Connection) -> None:
    """Wire any pattern_docs.pattern_id that is still NULL but resolvable."""
    con.execute("""
        UPDATE pattern_docs SET pattern_id = id
        WHERE pattern_id IS NULL
          AND EXISTS (SELECT 1 FROM patterns WHERE patterns.id = pattern_docs.id)
        """)
    con.commit()


# ─────────────────────────────────────────────────────────────────────────────
# summary
# ─────────────────────────────────────────────────────────────────────────────


def print_summary(con: sqlite3.Connection) -> None:
    tables = [
        "chapters",
        "patterns",
        "pattern_docs",
        "questions",
        "question_hints",
        "question_formulas",
        "question_mistakes",
        "chapter_resources",
    ]
    print()
    print("─" * 38)
    print("Database summary")
    print("─" * 38)
    for t in tables:
        (n,) = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()
        print(f"  {t:<26} {n:>5} rows")
    print("─" * 38)

    issues = []
    if con.execute(
        "SELECT COUNT(*) FROM questions WHERE pattern_id IS NULL"
    ).fetchone()[0]:
        issues.append("questions with no pattern")
    unlinked = con.execute(
        "SELECT COUNT(*) FROM pattern_docs WHERE pattern_id IS NULL"
    ).fetchone()[0]
    if unlinked:
        issues.append(
            f"{unlinked} pattern_docs unlinked (docs ahead of questions JSON)"
        )

    for msg in issues:
        print(f"  NOTE: {msg}")


# ─────────────────────────────────────────────────────────────────────────────
# entry point
# ─────────────────────────────────────────────────────────────────────────────


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python sqlite.py <path_to_output_folder>")
        sys.exit(1)

    root_dir = Path(sys.argv[1]).resolve()
    if not root_dir.exists():
        print(f"Error: folder does not exist: {root_dir}")
        sys.exit(1)

    con = open_db()
    print(f"\nIngesting: {root_dir}\n")

    process_questions(con, root_dir)
    process_markdown_files(con, root_dir)
    backfill_pattern_doc_links(con)
    print_summary(con)
    con.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
