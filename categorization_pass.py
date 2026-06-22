import json
import re
from typing import Optional
from gemini_utils import call_gemini, call_gemini_text, create_client, RateLimiter

_SECTION_PREFIX = {
    "solved_example": "se",
    "exercise": "ex",
}


def make_composite_key(section: str, question_number) -> str:
    """
    Build a stable identifier that disambiguates the same question_number
    appearing in both 'solved_example' and 'exercise' sections.
    """
    prefix = _SECTION_PREFIX.get(section, str(section)[:2].lower() or "unk")
    return f"{prefix}:{question_number}"


def parse_composite_key(key: str) -> tuple[str, str]:
    """Inverse of make_composite_key. Returns (section_prefix, question_number)."""
    prefix, _, qnum = str(key).partition(":")
    return prefix, qnum


CATEGORIZATION_PATTERN_PROPS = {
    "pattern_name": {"type": "STRING"},
    "description": {"type": "STRING"},
    "prerequisite_patterns": {"type": "ARRAY", "items": {"type": "STRING"}},
    "question_numbers": {"type": "ARRAY", "items": {"type": "STRING"}},
}

CATEGORIZATION_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "patterns": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": CATEGORIZATION_PATTERN_PROPS,
                "required": list(CATEGORIZATION_PATTERN_PROPS.keys()),
            },
        },
    },
    "required": ["patterns"],
}

CATEGORIZATION_PROMPT = """
You are an expert mathematics educator, curriculum designer, and competitive exam trainer.

You are given ALL questions and solutions from ONE chapter.

Your task is to discover PATTERNS that are genuinely useful for students.

══════════════════════════════
GOAL
══════════════════════════════

The purpose of these patterns is student learning.

Students should be able to select one pattern and study all questions belonging to that pattern together.

Each pattern should correspond to ONE lesson or ONE markdown note.

A pattern represents:

* one recognition process,
* one mental model,
* one solving framework,
* one set of shortcuts,
* one family of common mistakes.

Patterns should reflect how students naturally organize problems in their minds.

══════════════════════════════
MOST IMPORTANT RULE
══════════════════════════════

Imagine you are writing a textbook or preparing coaching lectures.

If two sets of questions would normally be taught in DIFFERENT lectures because they need a different solving framework, they MUST belong to different patterns.

If two sets of questions would normally be taught in the SAME lecture — even if one has an extra step, an extra given fact, or a different cover story — they MUST belong to the SAME pattern.

Same formula is not sufficient reason to merge. But also: a minor variation is not sufficient reason to split. Both mistakes are equally bad.

Optimize for how a human teacher would divide the chapter into lessons — not for the number of patterns in either direction.

══════════════════════════════
DO NOT GROUP ONLY BY FORMULAS
══════════════════════════════

Many questions may use the same underlying formula.

This does NOT mean they belong to the same pattern.

For example, in Partnership, many questions use:

Profit ∝ Capital × Time

However, students study these separately:

* Simple Partnership
* Different Time Periods
* Capital Changes
* Additional Investment
* Withdrawal Cases
* Working Partner
* Salary + Share
* Mixed Distribution
* Find Capital
* Find Time
* Rent Sharing
* Equivalent Units
* Multiple Time Phases

Using the same formula alone is NOT sufficient reason to merge patterns.

══════════════════════════════
WHAT DEFINES A PATTERN
══════════════════════════════

Patterns should differ by:

1. Recognition clues.
2. Keywords appearing in the question.
3. Information given.
4. Quantity to be found.
5. Typical question structure.
6. Solving framework.
7. Intermediate variables introduced.
8. Shortcuts used.
9. Common mistakes.
10. Whether students would benefit from a separate lesson.

══════════════════════════════
IMPORTANT REQUIREMENTS
══════════════════════════════

* Every question MUST belong to exactly one pattern.
* No question may remain uncategorized.
* Similar questions MUST always receive exactly the same pattern name.
* Use stable and consistent names.
* Avoid duplicate names.
* Use the FEWEST patterns that are still genuinely correct — do not
  create a new pattern just because a question has one extra detail;
  only create a new pattern when the recognition process or solving
  framework is actually different.
* A pattern with only 1-2 questions is almost always a sign that you
  fragmented a larger pattern rather than found a genuine standalone
  lesson. Before keeping any pattern that small, you must be able to
  name a DIFFERENT solving framework it uses compared to every other
  pattern — if you cannot, merge it into the closest matching pattern
  instead.
* Overly broad patterns are unacceptable.
* Catch-all patterns are unacceptable.

══════════════════════════════
AVOID CATCH-ALL PATTERNS
══════════════════════════════

The following are unacceptable:

* Complex Problems
* Advanced Problems
* Miscellaneous
* Mixed Problems
* Formula Problems
* Difficult Problems
* Type 1
* Type 2
* Chapter Name

These names do not explain WHY the questions belong together.

Pattern names should describe the underlying idea or solving framework.

══════════════════════════════
GOOD PATTERN NAMES
══════════════════════════════

Examples:

Simple Partnership
Different Time Periods
Capital Changes
Additional Investment
Withdrawal Cases
Working Partner
Salary + Share
Mixed Distribution
Find Capital
Find Time
Rent Sharing
Equivalent Units
Multiple Time Phases

Find SP
Find CP
Profit Percentage
Loss Percentage
Marked Price
Successive Change
False Weight

Combined Work
Efficiency Ratio
Pipes With Leak
Men-Women-Children
Work And Wages

══════════════════════════════
BAD PATTERN NAMES
══════════════════════════════

* Partnership Problems
* Profit Problems
* Complex Profit Sharing
* Basic Problems
* Easy Questions
* Formula Based Problems
* Miscellaneous

══════════════════════════════
INTERNAL REASONING PROCESS
══════════════════════════════

Think deeply and perform the following steps internally before producing the final JSON.

STEP 1

For each question, identify:

* recognition clues,
* keywords,
* information given,
* quantity to be found,
* formulas involved,
* mental model,
* solving framework,
* shortcuts,
* common mistakes.

STEP 2

Discover candidate question families.

Questions belong to the same family if they share:

* recognition process,
* mental model,
* solving framework,
* shortcuts,
* common mistakes.

Imagine that one teacher could explain all questions in that family in one lecture.

STEP 3

Split overly broad families if — and only if — they genuinely
contain multiple recognition processes or multiple solving
frameworks. Do not split based on cover story, extra given facts, or
different numbers alone.

When genuinely unsure whether two sub-families are really the same
lesson, lean toward keeping them together for now. STEP 4 and the
SCALE CHECK in STEP 7B exist specifically to catch real
under-splitting later, so an early bias toward splitting is not
protective — it only creates more fragmentation to undo afterward.

STEP 4

Merge overly narrow families.

Merge only if:

* recognition clues are similar,
* solving framework is the same,
* shortcuts are the same,
* and students would naturally revise them together.

STEP 5

Apply the SETUP TEST to every candidate pair of questions in a family.
This is the single most important test for learning ease, because the
real difficulty in these chapters is rarely the formula — it is
knowing which setup move to reach for the moment you read the
question.

Ask, for every pair of questions you are considering grouping together:

"If a student has just solved question A, can they solve question B
using the identical first move — the same thing they would write
down first on paper — changing only the numbers and names?"

If YES for every pair in the family: keep them as one pattern.

If NO — i.e. question B requires the student to first notice
something new (a withdrawal happened, a time period is unknown, a
working partner takes a salary, a capital value is missing, an
extra phase was added) before they can even begin setting up the
problem — then B requires a different first move. It must be a
separate pattern, even if the formula used afterward, or the final
arithmetic, is identical to question A's.

A pattern should let a student build ONE repeatable first-move
reflex through repetition. If practicing the "same" pattern secretly
requires switching setup frameworks partway through, the grouping
has failed at its actual job, regardless of how similar the formulas
look on paper.

STEP 6

Simulate a teacher.

Ask:

"Would I teach these questions in one lecture or separate lectures?"

Questions taught in separate lectures should belong to different patterns.

Use this as a sanity check alongside the SETUP TEST in STEP 5 — the
two should agree. If they disagree, trust the SETUP TEST: it is the
more concrete, repeatable signal of whether a single lesson is
genuinely possible.

STEP 7

Final naming pass. This step exists because the most common failure
mode in this task is producing two patterns that are actually the
same idea under different names — e.g. "Capital Withdrawal" and
"Withdrawal Cases", or "Missing Time" and "Find Time", or
"Profit Sharing Ratio" and "Profit Distribution". These look
different as strings but describe the same recognition process and
solving framework.

A second, equally common failure mode: taking one real pattern and
splitting it into "Base Pattern" plus "Base Pattern + minor variant"
— e.g. "Rent Sharing" vs "Rent Sharing With Early Leaving Partner",
or "Equivalent Units" vs "Rent Sharing Equivalence". If the core
recognition process and solving framework are the same and the
"variant" is really just one extra step or one extra piece of given
information layered on top of the same base method, this is ONE
pattern, not two. A genuinely separate pattern needs its OWN
recognition process or solving framework — a qualifier suffix OR a
"Base Name: Variant" colon-prefixed name (e.g. "Rent Sharing: Usage-
Based Distribution", "Rent Sharing: Equivalent Units", "Rent Sharing:
Phased Usage" — all three are fragments of ONE "Rent Sharing"
pattern) on an existing pattern's name is a strong signal you have
fragmented one pattern into pieces rather than discovered two distinct ones. When in doubt, default to the
shorter, base name and fold the variation in as a sub-case covered by
the same pattern, rather than inventing a longer compound name.

Before finalizing, list all your candidate pattern names side by
side and ask, for every pair:

"Would a student studying one of these also need the other, or are
they really the same lesson with two different names? Or is one of
them just the other plus one extra step?"

If they are the same lesson, merge them into a single pattern with
one name and combine their question_numbers. Do this even if it
means fewer patterns than you discovered in STEP 2-4 — a single
clean pattern beats two fragments of the same idea.

STEP 7B

Count your current candidate patterns.

If the count exceeds roughly 12-15 for a chapter of this size, treat
that as a strong signal of fragmentation, not a signal that the
chapter is unusually rich. Most chapters — even formula-heavy ones
like Profit & Loss — genuinely resolve into 6-12 distinct setup
moves. A count meaningfully above that almost always means several
"patterns" are actually the same lesson taught under different
cover stories, slightly different given-information, or one extra
step layered on a base method.

If your count is high, re-run this check before finalizing:

For every pattern, write one sentence: "A student who has mastered
[Pattern X] would still get stuck on [Pattern Y] because ___."

If you cannot fill in that blank with a genuine NEW recognition step
or solving move (not just "the numbers/cover-story are different,"
not just "this has one extra given fact"), merge Y into X.

Do this for every pair of patterns that are even loosely similar in
topic (e.g. all "discount" patterns, all "successive change"
patterns, all "find CP/SP" patterns) — not just patterns with
similar names. Topic-adjacent patterns are exactly where silent
duplication hides, because the names can look different while the
solving move is identical.

A high pattern count is not inherently wrong — but every single one
of them must survive this test. If you finish this check and still
have 20+ patterns, that is only acceptable if you can point to 20+
genuinely distinct first moves a student would need. This is rare.

STEP 8

Assign prerequisite_patterns for each pattern.

For each pattern, decide whether a student should be comfortable
with another pattern from this SAME chapter BEFORE attempting this
one. Only record a genuine dependency — e.g. "Capital Changes"
naturally builds on "Simple Partnership," so "Simple Partnership"
is a prerequisite.

Rules for prerequisite_patterns:
* Only reference pattern_names from THIS SAME response.
* Only list a prerequisite if studying it first genuinely makes the
  current pattern easier to understand — not just because it is
  "simpler."
* Most patterns will have zero prerequisites — leave the list empty
  rather than forcing a sequence that doesn't really exist.
* Never create circular dependencies (if A lists B as a prerequisite,
  B must not list A).
* prerequisite_patterns is purely a study-order aid. It does not
  imply one pattern is more important than another.

STEP 9

Perform a final quality check.

══════════════════════════════
QUALITY CHECK
══════════════════════════════

Verify:

* every question belongs to exactly one pattern,
* no question remains uncategorized,
* similar questions receive identical pattern names,
* no two pattern names describe the same recognition process and
  solving framework (re-run STEP 7's merge check if unsure),
* no pattern name is just another pattern's name plus a qualifier
  suffix for a minor variant,
* no pattern is based on difficulty,
* no pattern is a catch-all bucket,
* no pattern is excessively broad,
* each pattern has one recognition process,
* each pattern has one solving framework,
* every question pair within a pattern passes the SETUP TEST from
  STEP 5 (same first move, only numbers/names differ),
* the total pattern count has survived the SCALE CHECK in STEP 7B,
* each pattern could realistically be explained by one markdown note,
* students would naturally revise the questions in that pattern together,
* prerequisite_patterns only lists genuine dependencies from this
  same response, is left empty where no real ordering exists, and
  contains no circular references.

Only after completing these steps should you return the final JSON.

══════════════════════════════
GROUP NAME RULES
══════════════════════════════

HARD LIMIT: 2-3 words. Never more than 3.

Names must be:

* a noun phrase — no verbs ("Find Capital" not "Finding Capital"),
* no filler: "based on", "with", "using", "from", "for",
* no redundant chapter word (never prefix every name with the chapter title),
* memorable, suitable as a short markdown filename.

Bad → Good (enforce these):
  "Simple Partnership: Profit Distribution"           → "Simple Partnership"
  "Partnership with Varying Time Periods"             → "Varying Time"
  "Partnership with Capital Changes"                  → "Capital Changes"
  "Partnership with Relative Investments"             → "Relative Investment"
  "Partnership with Mixed Profit Distribution"        → "Mixed Distribution"
  "Rent Sharing based on Usage"                       → "Rent Sharing"
  "Finding Missing Time in Partnership"               → "Missing Time"
  "Finding Missing Capital in Partnership"            → "Missing Capital"
  "Deriving Investment/Time Ratios from Profit Ratios" → "Profit Ratio"

══════════════════════════════
DESCRIPTION FIELD SPEC
══════════════════════════════

The description must answer, in 1-2 sentences:

1. How do you RECOGNIZE this pattern from the question text alone —
   the specific clue, keyword, or combination of given information
   that signals "this is that kind of problem"?
2. What is the FIRST MOVE a student makes once they recognize it —
   the first thing they write down or set up on paper?

Do not describe the formula in isolation, and do not just restate
the pattern name. Recognition is the part students actually forget
under exam pressure — the formula itself is rarely the hard part.

Example (good):
"Recognize this when a partner joins or leaves partway through the
year, or capital changes mid-year — the question will mention a
specific month or 'after X months.' First move: convert each
partner's capital into capital-months by multiplying capital by the
number of months it was actually invested, then form the ratio."

Example (bad — restates the name, no recognition or first move):
"This pattern covers partnership problems where capital changes
during the year."

══════════════════════════════
COMPLETENESS CHECK (do this before returning)
══════════════════════════════

Each question below is labeled with an identifier in the form
Q[se:1] or Q[ex:1] — "se" means solved example, "ex" means exercise.
These identifiers are NOT the printed question numbers; they exist
because solved examples and exercises restart numbering separately,
so "1" alone is ambiguous. Always copy the FULL identifier inside the
brackets (e.g. "se:1", "ex:1") into question_numbers — never strip the
prefix and never reuse the bare number.

You are given a list of question identifiers below. Before returning your
answer, count them. Then count how many identifiers appear across
all of your "patterns" entries combined. These two counts MUST match
exactly.

Every identifier given to you must appear in the question_numbers
list of EXACTLY ONE pattern. Not zero patterns. Not two patterns.

If you are unsure which pattern a question belongs to, choose the
single closest match rather than omitting it or duplicating it.

══════════════════════════════
RETURN FORMAT
══════════════════════════════

Return ONLY valid JSON, matching this shape:

{{
"patterns": [
{{
"pattern_name": "",
"description": "",
"prerequisite_patterns": [],
"question_numbers": []
}}
]
}}

question_numbers must contain the full Q[se:1] / Q[ex:1] style
identifiers (without the "Q[" and "]", i.e. just "se:1" or "ex:1"),
exactly as shown for each question below — not the bare printed number.

prerequisite_patterns must contain pattern_name strings (from this
same response) that a student should ideally study before this
pattern. Leave empty if there is no genuine prerequisite.

Do not include a separate question-to-pattern mapping. The
question_numbers array inside each pattern is the only place
question assignment is recorded.

Questions and solutions:

{questions_solutions}
"""


def format_for_gemini(questions_solutions: list[dict]) -> str:
    """Format Q&S pairs for Gemini API using composite section:number identifiers."""
    formatted = []
    for item in questions_solutions:
        key = make_composite_key(item.get("section", ""), item["question_number"])
        formatted.append(f"""
Q[{key}]: {item.get('question_text', item.get('question', ''))}

Solution: {item['solution']}
""")
    return "\n---\n".join(formatted)


def _closest_pattern_by_word_overlap(
    name: str, candidate_names: list[str]
) -> Optional[str]:
    """Return the candidate name with the highest word overlap with `name`."""
    words = _name_word_set(name)
    if not words:
        return candidate_names[0] if candidate_names else None

    best_name, best_overlap = None, -1
    for candidate in candidate_names:
        candidate_words = _name_word_set(candidate)
        overlap = len(words & candidate_words)
        if overlap > best_overlap:
            best_name, best_overlap = candidate, overlap

    return best_name


def fold_tiny_patterns(patterns: list[dict], min_questions: int = 1) -> list[dict]:
    """
    Code-level safety net for the "pattern with 1-2 questions" rule in the
    prompt: the model is instructed to avoid leaving fragments this small,
    but LLM output isn't guaranteed to follow every instruction. This only
    auto-folds patterns at `min_questions` or fewer (default: singletons) —
    a single-question "pattern" is essentially never a genuine standalone
    lesson, so folding it is safe. Two-question patterns are left alone:
    they're a real borderline case the prompt already asks the model to
    judge, and auto-folding them risks erasing a genuinely distinct but
    rare pattern. Any pattern with `min_questions` or fewer questions gets
    folded into its closest-matching sibling by pattern-name word overlap.
    """
    if len(patterns) <= 1:
        return patterns

    by_name = {p["pattern_name"]: p for p in patterns}
    tiny = [p for p in patterns if len(p.get("question_numbers", [])) <= min_questions]

    for tiny_pattern in tiny:
        name = tiny_pattern["pattern_name"]
        if name not in by_name:
            continue  # already folded into something else this pass

        other_names = [n for n in by_name if n != name]
        if not other_names:
            continue  # this is the only pattern left; nothing to fold into

        target_name = _closest_pattern_by_word_overlap(name, other_names)
        if target_name is None:
            continue

        target = by_name[target_name]
        print(
            f"  INFO: folding tiny pattern '{name}' "
            f"({len(tiny_pattern.get('question_numbers', []))} question(s)) "
            f"into '{target_name}'"
        )

        target["question_numbers"] = list(
            dict.fromkeys(
                target.get("question_numbers", [])
                + tiny_pattern.get("question_numbers", [])
            )
        )
        del by_name[name]

    return list(by_name.values())


def merge_near_duplicate_patterns(
    patterns: list[dict], min_ratio: float = 0.85
) -> list[dict]:
    """
    Code-level safety net for STEP 7 in the prompt: the model is instructed
    to merge pattern names that describe the same idea, but this isn't
    guaranteed, so high-confidence near-duplicates (word overlap >= min_ratio,
    stricter than the 0.66 used for warnings) are auto-merged here. Lower-
    confidence overlaps are left as warnings only, since merging those
    automatically risks collapsing genuinely distinct patterns.
    """
    if len(patterns) <= 1:
        return patterns

    by_name = {p["pattern_name"]: p for p in patterns}
    pattern_names = list(by_name.keys())
    duplicates = find_near_duplicate_pattern_names(pattern_names)

    for name_a, name_b, ratio in duplicates:
        if ratio < min_ratio:
            continue
        if name_a not in by_name or name_b not in by_name:
            continue  # one side already merged away this pass

        # Keep the shorter name (prompt's stated preference: shorter base
        # name over a longer compound/variant name).
        keep, drop = (
            (name_a, name_b) if len(name_a) <= len(name_b) else (name_b, name_a)
        )

        print(
            f"  INFO: auto-merging near-duplicate pattern '{drop}' into "
            f"'{keep}' (word overlap: {ratio})"
        )

        by_name[keep]["question_numbers"] = list(
            dict.fromkeys(
                by_name[keep].get("question_numbers", [])
                + by_name[drop].get("question_numbers", [])
            )
        )
        del by_name[drop]

    return list(by_name.values())


def _name_word_set(name: str) -> set:
    """Normalize a pattern name into a set of significant words."""
    filler = {"the", "a", "an", "of", "in", "with", "and", "case", "cases"}
    words = re.findall(r"[a-z0-9]+", name.lower())
    return {w for w in words if w not in filler}


def find_near_duplicate_pattern_names(pattern_names: list[str]) -> list[tuple]:
    """
    Detect pattern name pairs that likely describe the same idea.
    Returns list of (name_a, name_b, overlap_ratio).
    """
    candidates = []
    word_sets = [(name, _name_word_set(name)) for name in pattern_names]

    for i in range(len(word_sets)):
        name_a, words_a = word_sets[i]
        if not words_a:
            continue
        for j in range(i + 1, len(word_sets)):
            name_b, words_b = word_sets[j]
            if not words_b:
                continue
            overlap = words_a & words_b
            smaller = min(len(words_a), len(words_b))
            if smaller == 0:
                continue
            ratio = len(overlap) / smaller
            if ratio >= 0.66:
                candidates.append((name_a, name_b, round(ratio, 2)))

    return candidates


def _detect_circular_prereqs(patterns: list[dict]) -> list[tuple[str, str]]:
    """
    Detect direct circular prerequisite pairs (A requires B, B requires A).
    Returns list of (name_a, name_b) pairs that form a cycle.
    """
    prereq_map = {
        p["pattern_name"]: set(p.get("prerequisite_patterns", [])) for p in patterns
    }
    cycles = []
    names = list(prereq_map.keys())
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            if b in prereq_map[a] and a in prereq_map.get(b, set()):
                cycles.append((a, b))
    return cycles


def normalize_categorization_response(
    categorization: dict,
    expected_question_numbers: Optional[list[str]] = None,
) -> dict:
    """
    Coerce Gemini's structured output into the canonical categorization shape.
    Preserves prerequisite_patterns and validates them.
    """
    if not isinstance(categorization, dict):
        return {"sub_patterns": [], "question_to_pattern": {}}

    raw_patterns = categorization.get("patterns") or []
    if not isinstance(raw_patterns, list):
        raw_patterns = []

    normalized_patterns = []

    # First pass: collect all pattern names for prerequisite validation
    all_pattern_names = {
        str(p.get("pattern_name", "")).strip()
        for p in raw_patterns
        if isinstance(p, dict)
    }

    for index, pattern in enumerate(raw_patterns, 1):
        if not isinstance(pattern, dict):
            continue

        name = str(pattern.get("pattern_name") or f"Pattern {index}").strip()
        description = str(pattern.get("description", ""))

        # Normalize prerequisite_patterns — validate each one references a
        # real pattern name from this same response
        raw_prereqs = pattern.get("prerequisite_patterns", [])
        if isinstance(raw_prereqs, str):
            raw_prereqs = [raw_prereqs]
        elif not isinstance(raw_prereqs, list):
            raw_prereqs = []

        prereqs = []
        for p in raw_prereqs:
            p = str(p).strip()
            if p and p != name:  # never self-reference
                if p in all_pattern_names:
                    prereqs.append(p)
                else:
                    print(
                        f"  WARNING: pattern '{name}' lists prerequisite "
                        f"'{p}' which is not a known pattern name — dropped."
                    )

        question_numbers = pattern.get("question_numbers", [])
        if isinstance(question_numbers, str):
            question_numbers = [question_numbers]
        elif not isinstance(question_numbers, list):
            question_numbers = []
        question_numbers = [str(q) for q in question_numbers]

        normalized_patterns.append(
            {
                "pattern_name": name,
                "subpattern_name": name,
                "description": description,
                "prerequisite_patterns": prereqs,
                "question_numbers": question_numbers,
            }
        )

    # Apply code-level safety nets the model is asked for in the prompt but
    # isn't guaranteed to follow: fold near-empty fragments into their
    # closest sibling, then auto-merge high-confidence near-duplicate names.
    # Both can change which patterns survive, so question_to_pattern and
    # prerequisite_patterns are rebuilt from the result afterward.
    normalized_patterns = fold_tiny_patterns(normalized_patterns)
    normalized_patterns = merge_near_duplicate_patterns(normalized_patterns)

    surviving_names = {p["pattern_name"] for p in normalized_patterns}
    for p in normalized_patterns:
        dropped_prereqs = [
            prereq
            for prereq in p["prerequisite_patterns"]
            if prereq not in surviving_names
        ]
        if dropped_prereqs:
            print(
                f"  INFO: pattern '{p['pattern_name']}' had prerequisite(s) "
                f"{dropped_prereqs} removed during merge/fold cleanup."
            )
        p["prerequisite_patterns"] = [
            prereq for prereq in p["prerequisite_patterns"] if prereq in surviving_names
        ]

    question_to_pattern = {}
    duplicate_assignments = []
    for p in normalized_patterns:
        for qnum in p["question_numbers"]:
            if qnum in question_to_pattern:
                duplicate_assignments.append(
                    (qnum, question_to_pattern[qnum], p["pattern_name"])
                )
            question_to_pattern[qnum] = p["pattern_name"]

    if duplicate_assignments:
        print(
            f"  WARNING: {len(duplicate_assignments)} question(s) assigned to "
            f"more than one pattern; keeping the last assignment seen:"
        )
        for qnum, first_pattern, second_pattern in duplicate_assignments:
            print(
                f"    Q{qnum}: '{first_pattern}' -> overwritten by '{second_pattern}'"
            )

    if expected_question_numbers is not None:
        expected_set = {str(q) for q in expected_question_numbers}
        missing = sorted(expected_set - question_to_pattern.keys(), key=str)
        if missing:
            print(
                f"  WARNING: {len(missing)} question(s) not assigned to any "
                f"pattern and will be marked 'Uncategorized': {missing}"
            )

    # Detect near-duplicate pattern names
    pattern_names = [p["pattern_name"] for p in normalized_patterns]
    near_duplicates = find_near_duplicate_pattern_names(pattern_names)
    if near_duplicates:
        print(
            f"  WARNING: {len(near_duplicates)} pattern name pair(s) look like "
            f"the same idea under different names:"
        )
        for name_a, name_b, ratio in near_duplicates:
            print(f"    '{name_a}' <-> '{name_b}' (word overlap: {ratio})")

    # Detect circular prerequisite dependencies
    circular = _detect_circular_prereqs(normalized_patterns)
    if circular:
        print(f"  WARNING: {len(circular)} circular prerequisite pair(s) detected:")
        for a, b in circular:
            print(
                f"    '{a}' <-> '{b}' (mutual prerequisite — breaking cycle by removing from '{b}')"
            )
            # Break the cycle by removing the back-edge from the later pattern
            for p in normalized_patterns:
                if p["pattern_name"] == b and a in p["prerequisite_patterns"]:
                    p["prerequisite_patterns"].remove(a)

    return {
        "sub_patterns": normalized_patterns,
        "question_to_pattern": question_to_pattern,
    }


def categorize_with_gemini(questions_solutions: list[dict]) -> Optional[dict]:
    """Send Q&S to Gemini for whole-chapter pattern categorization."""
    formatted = format_for_gemini(questions_solutions)
    prompt = CATEGORIZATION_PROMPT.format(questions_solutions=formatted)

    client = create_client()
    rate_limiter = RateLimiter(max_per_minute=10)
    model = "gemini-3.1-flash-lite"

    result = call_gemini_text(
        client=client,
        model=model,
        prompt=prompt,
        response_schema=CATEGORIZATION_SCHEMA,
        rate_limiter=rate_limiter,
    )

    if result is None:
        print(
            "  ERROR: categorization call failed after retries; "
            "no patterns were generated."
        )
        return None

    expected_question_numbers = [
        make_composite_key(item.get("section", ""), item["question_number"])
        for item in questions_solutions
    ]

    normalized = normalize_categorization_response(
        result,
        expected_question_numbers=expected_question_numbers,
    )

    print(json.dumps(normalized, indent=2, ensure_ascii=False))

    return normalized


def add_subpatterns_to_json(
    input_file: str, output_file: str, categorization: dict
) -> None:
    """Add sub_pattern and prerequisite_patterns fields to the JSON file."""
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    question_to_pattern = categorization.get("question_to_pattern", {})

    # Build a pattern_name -> prerequisite_patterns lookup
    prereq_map: dict[str, list[str]] = {
        sp["pattern_name"]: sp.get("prerequisite_patterns", [])
        for sp in categorization.get("sub_patterns", [])
    }

    questions = data.get("questions", []) if isinstance(data, dict) else data

    uncategorized = []
    for item in questions:
        key = make_composite_key(item.get("section", ""), item["question_number"])
        pattern = question_to_pattern.get(key, "Uncategorized")
        if pattern == "Uncategorized":
            uncategorized.append(key)
        item["sub_pattern"] = pattern
        # Carry prerequisite_patterns through to each question so the app
        # can surface "study these first" guidance per question.
        item["prerequisite_patterns"] = prereq_map.get(pattern, [])

    if uncategorized:
        print(
            f"  WARNING: {len(uncategorized)}/{len(questions)} question(s) "
            f"written as 'Uncategorized': {uncategorized}"
        )

    # Store the full categorization metadata in the JSON for downstream use
    # (overview and cheatsheet generators read prerequisite_patterns from here)
    if isinstance(data, dict):
        data["categorization"] = {
            "sub_patterns": categorization.get("sub_patterns", [])
        }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
