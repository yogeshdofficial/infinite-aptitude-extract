def build_question_prompt(
    chapter_start_page: int,
    chapter_end_page: int,
) -> str:

    return rf"""
You are digitizing a competitive-exam textbook into structured JSON.

This PDF contains chapter pages {chapter_start_page} to {chapter_end_page}.

══════════════════════════════
TASK
══════════════════════════════

Extract EVERY question appearing on these pages.

Return questions in EXACT PDF order.

Never reorder questions.

Never summarize.

Never stop early.

Completeness is more important than brevity.

══════════════════════════════
SECTION RULES
══════════════════════════════

The chapter structure is:

IMPORTANT FACTS
→ SOLVED EXAMPLES
→ EXERCISE
→ ANSWERS
→ SOLUTIONS
→ DATA SUFFICIENCY
→ DATA SUFFICIENCY ANSWERS

Extract ONLY:

1. Solved Examples
2. Exercise Questions

Ignore completely:

• IMPORTANT FACTS
• ANSWERS
• SOLUTIONS
• DATA SUFFICIENCY
• DATA SUFFICIENCY ANSWERS

Solved examples exist ONLY between:

SOLVED EXAMPLES
and
EXERCISE

Exercise questions exist ONLY between:

EXERCISE
and
ANSWERS

Everything after ANSWERS must be ignored.

Never create questions from:

• answer keys
• solution paragraphs
• isolated calculations
• continuation text

A question must contain an explicit problem statement.

A question must ask something — it must contain a question mark, or
an explicit instruction like "Find...", "What is...", "Calculate...".
A block that only states a fact, a conclusion, or a final computed
value is NOT a question, even if it looks like one at first glance.

Reject any block that is a continuation of a calculation or
conclusion rather than a new problem statement. This commonly looks
like a block beginning with a connective or a "result =" pattern, such
as (these are illustrative examples from one chapter — apply the same
logic to whatever connective/result pattern appears in THIS chapter):

Hence,
Therefore,
Thus,
Balance =,
Ratio of,
A : B : C =,
B's share =,
C's share =,
Required answer =,

The underlying rule, not the specific words above, is what matters:
if a block is restating or concluding a calculation that was already
in progress — rather than posing a fresh, self-contained problem for
the reader to solve — reject it, regardless of which chapter or which
specific connective word it starts with.

══════════════════════════════
BOUNDARY RULES
══════════════════════════════

If the first page begins in the middle of a question whose number is absent,
skip that fragment.

If a question starts on these pages and continues beyond the last page,
extract everything visible.

══════════════════════════════
PASSAGES
══════════════════════════════

For ordinary questions:

passage_text = ""

Put the COMPLETE problem statement into question_text.

Do not split a question into passage_text and question_text.

Use passage_text ONLY when multiple questions share the same:

• paragraph
• table
• chart
• graph
• caselet

passage_text should be empty for more than 95% of questions.

══════════════════════════════
QUESTION STRUCTURE
══════════════════════════════

Question numbers belong ONLY in question_number.

Never include question numbers inside:

• passage_text
• question_text

Example:

Input:

8. Three persons started a placement business with a capital of ₹3000.
B invests ₹600 less than A and C invests ₹300 less than B.
What is B's share in a profit of ₹886?

Correct output:

question_number = "8"

passage_text = ""

question_text =
"Three persons started a placement business with a capital of ₹3000. B invests ₹600 less than A and C invests ₹300 less than B. What is B's share in a profit of ₹886?"

Incorrect:

passage_text =
"Three persons started a placement business..."

question_text =
"What is B's share in a profit of ₹886?"

══════════════════════════════
MATHEMATICS
══════════════════════════════

Render ALL mathematical expressions using LaTeX.

Apply this to:

• question_text
• solution
• option_a
• option_b
• option_c
• option_d
• option_e

Use:

$x+y$

$\frac{{a}}{{b}}$

$\sqrt{{x}}$

$x^2$

$x_n$

$\times$

$\div$

══════════════════════════════
MULTI-LINE CALCULATIONS
══════════════════════════════

For calculations involving multiple steps, preserve each step on a separate line.

Example:

Input:

Ratio of capitals = (7/2 × 30) : (4/3 × 30) : (6/5 × 30)
= 105 : 40 : 36

A's share = ₹ (2430 × 35/54)
= ₹1575

Output:

Ratio of capitals

$\left(\frac{{7}}{{2}}\times30\right):
\left(\frac{{4}}{{3}}\times30\right):
\left(\frac{{6}}{{5}}\times30\right)$

$=105:40:36$

A's share

₹ $\left(\frac{{2430\times35}}{{54}}\right)$

$=₹1575$

══════════════════════════════
CONSISTENCY
══════════════════════════════

Never mix plain text mathematics and LaTeX.

Incorrect:

2 × 7 and $7^2$

Correct:

$2\times7$ and $7^2$

══════════════════════════════
DISPLAY EQUATIONS
══════════════════════════════

Preserve displayed equations exactly as printed.

Keep intermediate steps.

Do not collapse multiple lines into one paragraph.

══════════════════════════════
FRACTIONS
══════════════════════════════

Convert

7/2

into

$\frac{{7}}{{2}}$

Convert

2430 × 35/54

into

$\frac{{2430\times35}}{{54}}$

Never leave fractions as plain text.

This applies EVERYWHERE a fraction appears, including inside an
ordinary sentence in question_text or solution, not only inside a
standalone displayed equation.

Example:

Input:

A invested 1/4 of the capital and B invested 1/5 of the capital.

Output:

A invested $\frac{{1}}{{4}}$ of the capital and B invested
$\frac{{1}}{{5}}$ of the capital.

══════════════════════════════
CURRENCY AND PERCENT SYMBOL BOUNDARIES
══════════════════════════════

₹ and % are plain text, not LaTeX. They must never be left sitting
inside a $...$ block by accident, and the closing $ must always sit
immediately after the LaTeX expression ends — never after a trailing
₹ amount or word.

Wrong (the closing $ trails behind \right), pulling ₹ and 36 inside
math mode where ₹ is not a valid symbol):

$\left(\frac{{12}}{{5}}\times15\right) = ₹ 36$

Correct (the $ closes immediately after \right), then ₹ 36 sits
outside it as plain text):

$\left(\frac{{12}}{{5}}\times15\right)$ = ₹ 36

If a percent sign is the final result of a calculation, keep \% and
the final number inside one clean $...$ block with the $ closing
immediately after the last character of the math — do not let the
boundary land in the middle of the percent sign or split it from its
number.

Before finalizing, check the character immediately before every
closing $. If it is ₹ followed by a number, or any plain word, that
$ is misplaced.

══════════════════════════════
OPTIONS
══════════════════════════════

Apply the same LaTeX rules to MCQ options.

Example:

option_a = "$7^2$"

option_b = "$\frac{{3}}{{5}}$"

option_c = "$\sqrt{{17}}$"

option_d = "$2\times5$"

══════════════════════════════
SOLVED EXAMPLES
══════════════════════════════

For solved examples:

Transcribe the COMPLETE solution exactly as printed.

Preserve:

• line order
• paragraph breaks
• displayed equations
• intermediate steps

Separate lines using \n.

Do not summarize.

Do not simplify.

══════════════════════════════
EXERCISE QUESTIONS
══════════════════════════════

If a solution appears immediately below the question on these pages,
extract it.

Otherwise:

solution = ""

Pass 2 will fill missing solutions.

Do not invent answers.

══════════════════════════════
MCQ OPTIONS
══════════════════════════════

If MCQ:

fill option_a to option_e.

Unused options = ""

If answer is marked:

correct_option = "a"
or
"b"
or
"c"
or
"d"
or
"e"

Else:

correct_option = ""

Render mathematical expressions inside options using LaTeX.

Example:

option_a = "$7^2$"

option_b = "$\frac{{3}}{{5}}$"

option_c = "$\sqrt{{17}}$"

option_d = "$2\times5$"

══════════════════════════════
DATA SUFFICIENCY
══════════════════════════════

Never extract Data Sufficiency questions.

Set:

is_data_sufficiency = false

for all extracted questions.

══════════════════════════════
PAGE NUMBERS
══════════════════════════════

page_numbers = []

answer_page_numbers = []

for every question.

Do not infer page numbers.

══════════════════════════════
CRITICAL
══════════════════════════════

Never skip questions.

Never merge questions.

Never rewrite wording.

Never simplify.

Never explain.

Return ONLY JSON matching the schema.
"""


def build_answer_prompt(
    missing_question_numbers: list[str],
) -> str:

    qlist = ", ".join(f'"{q}"' for q in missing_question_numbers)

    return rf"""
You are given pages containing the solution section.

The following question numbers need answers:

[{qlist}]

══════════════════════════════
TASK
══════════════════════════════

Locate each requested question number.

Return one answer object per question.

question_number must exactly match the requested number.

Do not invent answers.

If a question number is absent, omit it.

══════════════════════════════
SOLUTION
══════════════════════════════

Transcribe the COMPLETE solution exactly as printed.

Preserve:

• line order
• paragraph breaks
• displayed equations
• intermediate steps

Separate lines using \n.

Do not summarize.

Do not simplify.

══════════════════════════════
MATHEMATICS
══════════════════════════════

Render ALL mathematical expressions using LaTeX.

Apply this to:

• question_text
• solution
• option_a
• option_b
• option_c
• option_d
• option_e

Use:

$x+y$

$\frac{{a}}{{b}}$

$\sqrt{{x}}$

$x^2$

$x_n$

$\times$

$\div$

══════════════════════════════
MULTI-LINE CALCULATIONS
══════════════════════════════

For calculations involving multiple steps, preserve each step on a separate line.

Example:

Input:

Ratio of capitals = (7/2 × 30) : (4/3 × 30) : (6/5 × 30)
= 105 : 40 : 36

A's share = ₹ (2430 × 35/54)
= ₹1575

Output:

Ratio of capitals

$\left(\frac{{7}}{{2}}\times30\right):
\left(\frac{{4}}{{3}}\times30\right):
\left(\frac{{6}}{{5}}\times30\right)$

$=105:40:36$

A's share

₹ $\left(\frac{{2430\times35}}{{54}}\right)$

$=₹1575$

══════════════════════════════
CONSISTENCY
══════════════════════════════

Never mix plain text mathematics and LaTeX.

Incorrect:

2 × 7 and $7^2$

Correct:

$2\times7$ and $7^2$

══════════════════════════════
DISPLAY EQUATIONS
══════════════════════════════

Preserve displayed equations exactly as printed.

Keep intermediate steps.

Do not collapse multiple lines into one paragraph.

══════════════════════════════
FRACTIONS
══════════════════════════════

Convert

7/2

into

$\frac{{7}}{{2}}$

Convert

2430 × 35/54

into

$\frac{{2430\times35}}{{54}}$

Never leave fractions as plain text.

This applies EVERYWHERE a fraction appears, including inside an
ordinary sentence in question_text or solution, not only inside a
standalone displayed equation.

Example:

Input:

A invested 1/4 of the capital and B invested 1/5 of the capital.

Output:

A invested $\frac{{1}}{{4}}$ of the capital and B invested
$\frac{{1}}{{5}}$ of the capital.

══════════════════════════════
CURRENCY AND PERCENT SYMBOL BOUNDARIES
══════════════════════════════

₹ and % are plain text, not LaTeX. They must never be left sitting
inside a $...$ block by accident, and the closing $ must always sit
immediately after the LaTeX expression ends — never after a trailing
₹ amount or word.

Wrong (the closing $ trails behind \right), pulling ₹ and 36 inside
math mode where ₹ is not a valid symbol):

$\left(\frac{{12}}{{5}}\times15\right) = ₹ 36$

Correct (the $ closes immediately after \right), then ₹ 36 sits
outside it as plain text):

$\left(\frac{{12}}{{5}}\times15\right)$ = ₹ 36

If a percent sign is the final result of a calculation, keep \% and
the final number inside one clean $...$ block with the $ closing
immediately after the last character of the math — do not let the
boundary land in the middle of the percent sign or split it from its
number.

Before finalizing, check the character immediately before every
closing $. If it is ₹ followed by a number, or any plain word, that
$ is misplaced.

══════════════════════════════
OPTIONS
══════════════════════════════

Apply the same LaTeX rules to MCQ options.

Example:

option_a = "$7^2$"

option_b = "$\frac{{3}}{{5}}$"

option_c = "$\sqrt{{17}}$"

option_d = "$2\times5$"

══════════════════════════════
BARE ANSWERS
══════════════════════════════

If the book gives only:

(a)

or

12

or

₹150

store exactly that.

Do not expand.

══════════════════════════════
CORRECT OPTION
══════════════════════════════

If answer choices are given:

correct_option =
"a"
"b"
"c"
"d"
or
"e"

Otherwise:

correct_option = ""

══════════════════════════════
PAGE NUMBERS
══════════════════════════════

answer_page_numbers = []

for every answer.

══════════════════════════════
IMPORTANT
══════════════════════════════

Never invent answers.

Never return blank entries.

Return ONLY JSON matching the schema.
"""
