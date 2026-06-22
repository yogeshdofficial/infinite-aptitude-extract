# enrichment_prompts.py

ENRICHMENT_PROMPT = r"""
You are creating high-quality study material for students, based on
REAL questions and REAL official solutions extracted from a textbook.

══════════════════════════════
ABSOLUTE RULE — DO NOT CHANGE THE QUESTION OR THE ANSWER
══════════════════════════════

You are given the ORIGINAL question text and the ORIGINAL solution/
answer exactly as they appear in the book (extracted from the PDF in
an earlier pass). Your job is NOT to invent a new question, NOT to
change any number, NOT to paraphrase the scenario, and NOT to alter
the options or the final answer in any way.

Specifically, you must NEVER:

- change any number, quantity, price, ratio, percentage, date, name,
  or unit that appears in the original question
- invent a different scenario or storyline
- generate new MCQ options or a new correct option
- compute a different final answer than the one given/implied by the
  book's original solution
- "improve" or "simplify" the question's wording in a way that changes
  its meaning

You MUST:

- reproduce the original question text exactly, only fixing OCR/PDF
  extraction artifacts (broken spacing, stray characters, garbled
  symbols) and reformatting numbers/symbols into clean LaTeX
- reproduce the original options exactly (if MCQ), same wording/values,
  only cleaned up for formatting
- reproduce the original correct option / final answer exactly as
  given in the source solution
- write the explanation (traditional_solution) using the SAME method
  the book uses, arriving at the SAME final answer, just explained far
  more thoroughly than the book's own (often terse) solution
- write a shortcut method (shortcut_solution) that also uses the exact
  same numbers and arrives at the exact same final answer

If the original solution provided to you is incomplete, terse, or
skips steps (which is common in textbooks), that is expected and is
exactly what you are here to fix: you fill in the missing reasoning
and steps, using the original numbers, until a beginner can follow it
end to end. You are not allowed to "fill the gap" by changing what the
question is asking or what the answer is — only by adding explanation.

If the original solution text contains an obvious arithmetic slip
that does not match the given options/answer, trust the OPTIONS and
the marked correct answer (if present) as the ground truth, and show
the correct working that leads there. If there is no way to determine
the book's intended correct answer (no options, no marked answer, and
the working is genuinely ambiguous), solve the question correctly
yourself from the given data and clearly use that as the final answer
— do not fabricate uncertainty or hedge in the output.

══════════════════════════════
PARAPHRASED_QUESTION FIELD (= the original question, cleaned up)
══════════════════════════════

Despite the field name "paraphrased_question" (kept for compatibility
with the rest of the pipeline), this field must contain the ORIGINAL
question, NOT a paraphrase of it. Reproduce it faithfully:

- Same numbers, same names, same units, same scenario.
- Clean up only formatting: proper LaTeX for every fraction, ratio,
  percentage, exponent, and equation; proper line breaks; remove PDF
  extraction noise (stray page numbers, broken hyphenation, doubled
  spaces, mis-OCR'd symbols like "Rs" vs "₹" — normalize currency
  symbols consistently, prefer ₹ for Indian Rupees if that is what the
  source uses).
- If the original question text you were given already looks clean,
  copy it through with only LaTeX-ification of any bare numbers/
  fractions — do not rewrite sentences unnecessarily.

══════════════════════════════
PARAPHRASED OPTIONS AND FINAL ANSWER (= the original ones)
══════════════════════════════

If the question is MCQ, reproduce the original four options exactly
(same values), only cleaning up LaTeX formatting. Set
paraphrased_correct_option to the letter (a/b/c/d) of whichever option
equals the original correct answer — derived from the option VALUES,
not assumed from the source's stated letter if there is any mismatch
(the source's labeling could differ in lettering convention; the value
must match).

If the question is not MCQ, all four paraphrased_option_* fields must
be empty strings, and paraphrased_correct_option must be an empty
string.

paraphrased_final_answer is the original book's final numeric/algebraic
answer, in clean LaTeX. Examples:

₹450

$35$

$\frac{7}{8}$

Do not include explanations in this field. Return only the final
answer.

══════════════════════════════
ANSWER CONSISTENCY (CRITICAL)
══════════════════════════════

Before returning the response:

1. Identify the original final answer from the source solution/options
   provided to you. This is the canonical answer — it must never
   change.

2. traditional_solution must end at this exact answer.

3. shortcut_solution must end at this exact answer.

4. paraphrased_final_answer must equal this answer exactly.

5. If the question is MCQ, exactly one option (using the ORIGINAL
   option values) must equal this answer, and
   paraphrased_correct_option must point to that letter.

6. Re-derive the answer yourself from the locked original numbers,
   independently, using the book's method. Compare:

- answer obtained from traditional_solution
- answer obtained from shortcut_solution
- paraphrased_final_answer
- correct option value (if MCQ)
- value corresponding to paraphrased_correct_option (if MCQ)

All of these must be identical. If any one of them differs, you have
made an error — find it and fix it before returning. Never return
contradictory answers, multiple correct options, or a correct option
letter whose value differs from paraphrased_final_answer.

──────────────────────────────
MCQ INTEGRITY CHECK (MANDATORY)
──────────────────────────────

For MCQ questions, after copying the original options through:

Read option a. Read option b. Read option c. Read option d.

Find which option's VALUE exactly matches the original final answer.

Set paraphrased_correct_option to that letter — derived from the
option values, never guessed, never assumed from memory.

══════════════════════════════
TRADITIONAL SOLUTION — DETAILED, NO-ASSUMPTIONS EXPLANATION
══════════════════════════════

This is the most important deliverable. The original textbook solution
you were given is often terse — it may jump straight from the question
to a formula to an answer in two lines, with no explanation. Your job
is to expand it into a complete teaching solution that uses the exact
SAME numbers and the exact SAME method/approach as the book, but
explains every step in full.

Write for a BEGINNER who is seeing this exact question for the first
time and has never solved this type of question before.

The student knows:
- basic arithmetic (add, subtract, multiply, divide)
- what a ratio means
- what a fraction means
- what a percentage means

The student does NOT know:
- which formula applies here
- why a particular formula applies here
- what to do first
- what any intermediate result means in context

Never assume the reader can fill in a gap on their own. If a step
would make sense only to someone who already knows how to solve this
type of question, it needs an explanation. Make NO unstated
assumptions — if the book's solution skips a step, you must supply it
explicitly, still using the book's original numbers.

──────────────────────────────
THE "WHY" RULE (most important rule in this section)
──────────────────────────────

For every non-arithmetic step, write one plain-English sentence
explaining WHY that step is valid, before or immediately after the
equation. The WHY sentence answers the question a beginner would ask
at that exact moment.

A step needs a WHY sentence if it involves any of the following:

• Introducing a formula for the first time
  — name the rule and say why it applies here.

• A ratio appearing that was not directly stated in the question
  — explain where it came from.

• A fraction of the total being taken
  — say why that fraction and not some other.

• One quantity being substituted or replaced by another
  — say what justifies the substitution.

• A simplification that uses a mathematical property
  — name the property in plain words.

• Any step where a beginner would reasonably ask:
  "where did that come from?" or "why are we allowed to do that?"

A step does NOT need a WHY sentence if it is pure arithmetic:
multiplying, dividing, adding, subtracting, or simplifying a fraction
that was already fully set up in the previous step.

──────────────────────────────
WORKED EXAMPLES OF THE WHY RULE
──────────────────────────────

These show the exact level of explanation required (illustrative —
your actual numbers come from the real original question given to you).

— Example 1: profit sharing ratio —

Bad (no explanation, beginner is lost):
"A's profit share is $\frac{1}{5}$."

Good (explains the rule AND connects it to this question):
"In a partnership, profit is always shared in the same ratio as the
partners' capitals. Since the capitals are in the ratio $1:1:3$,
the total ratio has $1+1+3=5$ parts. A's capital is 1 part out of 5,
so A's share of the profit is also $\frac{1}{5}$ of the total."

— Example 2: deriving one partner's ratio from another —

Bad (equation with no context):
"C's ratio = $\frac{1}{3}$ of (A+B)'s ratio."

Good (builds the logic step by step):
"We are told C gets $\frac{1}{4}$ of the total profit. That means
A and B together get the remaining $\frac{3}{4}$. We can verify
C's share is $\frac{1}{3}$ of A and B's combined share, because

$$
\frac{1}{3}\times\frac{3}{4}
=
\frac{1}{4}
$$

which matches what was given."

— Example 3: setting up an equation from a word condition —

Bad (equation appears with no justification):
"$x + 10 = 2(y + 10)$"

Good (translates the word condition into math explicitly):
"The problem says that after 10 years, A's age will be twice B's age.
A's age in 10 years is $x+10$. B's age in 10 years is $y+10$.
'Twice' means we multiply B's future age by 2 and set it equal to A's:

$$
x+10=2(y+10)
$$"

— Example 4: time-weighted investment —

Bad (ratio stated without justification):
"Effective capital ratio = $12000\times8 : 16000\times6$"

Good (explains why time is multiplied in):
"When partners invest for different time periods, the profit-sharing
ratio is not just based on the amount invested but on
capital × time — because a larger capital invested for a shorter
period contributes the same as a smaller capital invested for longer.
So the effective capital for each partner is:

$$
12000\times8 : 16000\times6
$$"

──────────────────────────────
GENERAL STYLE
──────────────────────────────

Show the reasoning behind each major step.

Do not merely write equations without explanation.

Use short, natural sentences — one idea per sentence.

Show every important intermediate calculation.

Do not skip algebraic steps.

The solution should feel like a teacher solving the problem on a
whiteboard, narrating every decision out loud, pausing at exactly the
moments where a student would normally get stuck.

Avoid robotic numbering:

Step 1 / Step 2 / Step 3

Use natural connective words instead:

First, · Next, · Since, · Because, · Notice that, ·
This means, · Therefore, · Hence, · Thus,

Never assume that the student already understands the method.

Never narrate your own internal process (e.g. "let me check", "wait",
"actually", "on second thought"). The solution should read as a
final, polished explanation — never reveal that you double-checked or
reconsidered anything while writing it.

──────────────────────────────
BALANCE RULE (explanation vs. brevity)
──────────────────────────────

The goal is a solution that is complete without being padded.

Explain every non-arithmetic step (per the WHY RULE above).
Do not explain pure arithmetic — a student who knows basic arithmetic
does not need "we multiply 5 by 18 to get 90" spelled out.

The right length is determined by the question's complexity:
- A simple one-step ratio question may need only 6–8 lines.
- A multi-party time-weighted partnership may need 15–25 lines.
This is a DETAILED, no-assumptions explanation — when in doubt, favor
explaining more rather than less. Do not compress a complex question
to hit an artificial maximum, but also do not pad a trivial question
with filler sentences that say nothing new.

A good test: read the solution imagining you are seeing this type of
question for the first time. If any step would leave you confused
about where the next line came from, add a WHY sentence there. If any
sentence is pure restatement that adds zero new information, cut it.

The solution should be easy to read on a mobile phone.

══════════════════════════════
SHORTCUT SOLUTION — TRICK / FAST METHOD
══════════════════════════════

Provide a genuine shortcut method — the kind an experienced student
or coaching-class trainer would use to solve this exact question much
faster than the full textbook method above. Use the exact same
original numbers and arrive at the exact same final answer as
traditional_solution.

Format it the same way as the original solution style: clean LaTeX,
short lines, blank lines between steps — but compressed to only the
essential moves, written as a fast, trick-based path rather than a
full derivation.

Genuine shortcuts include things like: direct ratio/proportion
shortcuts that skip setting up full equations, percentage-to-fraction
conversion tricks, recognizing a special-case formula that bypasses
several algebra steps, working backward from the options (when MCQ),
unit-cancellation tricks, alligation/mixture shortcuts, and similar
exam-speed techniques genuinely used for this pattern of question.

If a genuine shortcut exists, provide it, and include one brief clause
explaining WHY it works (using the same WHY RULE as above, but kept
short — this field optimizes for speed, not full teaching).

If no genuine shortcut faster than the full method exists for this
particular question, provide a tightly compressed version of the
traditional method instead — skip explanations for steps already
explained in traditional_solution, keep only the equations and minimal
connective text, while still ending at the exact same final answer.

Never leave shortcut_solution empty. Never invent an unrealistic or
fake "trick" that doesn't actually save time — a compressed version of
the standard method is always an acceptable fallback.

══════════════════════════════
LATEX AND EQUATION FORMATTING
══════════════════════════════

Render EVERY mathematical expression using LaTeX. No exceptions.

Apply this to:

• paraphrased_question (the original question text)
• paraphrased_option_a / b / c / d
• paraphrased_final_answer
• traditional_solution
• shortcut_solution

──────────────────────────────
INLINE MATH vs. DISPLAY MATH (CRITICAL)
──────────────────────────────

Inline math, $...$, is ONLY for something simple sitting inside a
sentence: a single fraction, a ratio, a variable, or a percentage —
never a calculation.

Allowed inline: $\frac{5}{18}$ · $2:3$ · $x^2$ · $25\%$

Display math, on its own paragraph between $$ and $$, is REQUIRED for
any expression containing "=", "+", "-", "\times", "\div", or more
than one operation — i.e. any actual calculation, not just a bare
value.

WRONG (a calculation embedded in a sentence):
"A's share $= \frac{5}{18} \times 81900 =$ ₹22500."

CORRECT:
"A's share is

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500."

WRONG:
"Profit percentage $=\left(\frac{9}{36}\times100\right)\%=25\%$."

CORRECT:
"The profit percentage is

$$
\frac{9}{36}\times100
$$

which equals $25\%$."

Rules:

- Every display equation occupies its own paragraph, with a blank
  line before and after it.
- Never put two equations on the same line, inside or outside a
  display block.
- Inside a display block, if the calculation has multiple stages,
  put each stage on its own line (expression, then "=", then result),
  rather than chaining "a = b = c" on one line.
- Never write "$a=b=c$" inline; use a $$ block with each value on its
  own line instead.
- This rule has higher priority than brevity — splitting a step
  across more lines is always preferred over compressing a
  calculation into a sentence.

──────────────────────────────
ABSOLUTE FRACTION RULE
──────────────────────────────

ANY number written as a fraction — including inside a normal English
sentence, including "1/4 of the capital", including ratio-derived
fractions like "1/5 of the profit" — MUST be wrapped as
$\frac{a}{b}$.

There is no such thing as a "casual" fraction that can stay as plain
text. If you write a "/" between two numbers anywhere in the output,
that is a bug.

WRONG: "A and B get half of 2/5 each, which is 1/5."
CORRECT: "A and B each get half of $\frac{2}{5}$, which is $\frac{1}{5}$."

WRONG (real bug seen in production — fraction in the question itself):
"Amit invested 1/4 of the capital, Bimal invested 1/5 of the capital"
CORRECT:
"Amit invested $\frac{1}{4}$ of the capital, Bimal invested
$\frac{1}{5}$ of the capital"

This rule applies identically inside paraphrased_question. A fraction
appearing in the original question text must still be wrapped in
LaTeX — fixing formatting is allowed and required, even though
changing the underlying numbers is not.

──────────────────────────────
NO DECIMAL APPROXIMATIONS OF EXACT VALUES
──────────────────────────────

Never represent an exact fraction as a rounded decimal, especially
when it is multiplying a variable.

WRONG: "0.466P" · "0.533P"
CORRECT (the exact fraction, never rounded): $\frac{7P}{15}$, or
before simplifying, $\frac{14P}{30}$.

Decimals lose precision and hide where the number came from.
Fractions are exact and make the next algebraic step obvious. The
only acceptable decimal is one that was genuinely a decimal in the
original question (e.g. a price of ₹19.50) — never a decimal that
results from dividing two numbers in your own working.

──────────────────────────────
CURRENCY AND PERCENT BOUNDARIES (real bug seen in production)
──────────────────────────────

The ₹ symbol and the % sign are NOT math symbols. They must never sit
inside a $...$ or $$...$$ block, and they must never straddle the
boundary of one.

WRONG (₹ and the number get pulled inside the math block):
"Cost price of 15 oranges = $\left( \frac{12}{5} \times 15 \right) = ₹ 36$."

CORRECT — close the math block immediately after the LaTeX
expression ends, then write ₹ and the number as plain text outside it:
"Cost price of 15 oranges is

$$
\frac{12}{5}\times15
=
36
$$

So the cost price is ₹36."

Rule: the math block boundary must end exactly where the LaTeX
expression ends. Never let plain text — ₹, a currency amount, or a
word like "profit" — fall inside a $...$ or $$...$$ block. The test
before finalizing: read the characters immediately before every
closing $ or $$. If those characters are ₹ followed by a number, or
any plain word, that delimiter is misplaced.

The same applies to %: keep the whole calculation, including \%,
inside one clean math block, then state the result in plain text
right after — never split a % awkwardly across the boundary.

──────────────────────────────
CHAINED SHARES IN ONE SENTENCE (real bug — multiple parties)
──────────────────────────────

This is the single most common way the two rules above get broken at
once, and it happens specifically in partnership and ratio-sharing
questions with three or more parties. When summarizing every party's
share in one closing sentence, it is tempting to write each share as
its own little inline equation, chained together with commas — but
every one of those mini-equations contains a "=" AND ends with a ₹
amount pulled inside the delimiter, breaking both rules at the same
time, for every party, in a single sentence.

WRONG (real bug — three inline equations chained in one sentence,
each one mixing "=" inside $...$ with ₹ pulled inside the closing
delimiter):
"Therefore, A's share is $8 \times 2000 = ₹16,000$, B's share is
$9 \times 2000 = ₹18,000$, and C's share is $10 \times 2000 = ₹20,000$."

This is wrong twice over for every single share: it embeds a
calculation containing "=" inside inline math instead of using a
display block (see INLINE MATH vs. DISPLAY MATH), and it pulls ₹ and
the comma-formatted result inside the math delimiter (see CURRENCY
AND PERCENT BOUNDARIES). Three parties means three repetitions of
the same double violation.

CORRECT — give each party's share its own display block, with the ₹
amount stated as plain text immediately after, never chained together
with commas in one sentence:

"Therefore, A's share is

$$
8\times2000
=
16000
$$

which is ₹16,000.

B's share is

$$
9\times2000
=
18000
$$

which is ₹18,000.

And C's share is

$$
10\times2000
=
20000
$$

which is ₹20,000."

This pattern applies to any question with three or more parties,
items, or people whose individual results are summarized at the end
— partnership shares, mixture quantities, age comparisons, and so
on. Never summarize multiple computed values in a single sentence
using inline math. Give each one its own short paragraph and its own
display block, exactly as if it were the only value being reported.

──────────────────────────────
LARGE NUMBERS AND THOUSANDS SEPARATORS
──────────────────────────────

Prefer keeping standalone currency amounts as plain text outside math
mode entirely, with an ordinary comma: "= ₹20,000".

If a number must stay inside a math block because it is genuinely
part of a larger equation, use brace-grouped commas so KaTeX does not
misparse the comma as a list separator, e.g. $20{,}000$ rather than
$20,000$.

──────────────────────────────
RATIOS ARE PROPORTIONAL, NOT EQUAL
──────────────────────────────

A profit-sharing ratio formula describes a proportionality between
quantities of different kinds (money, compared to money×time), not a
literal equality. Use $\propto$ for this relationship, not $=$:

$$
\text{Profit ratio} \propto \text{Capital} \times \text{Time}
$$

Reserve $=$ for the actual share formula, where both sides really are
the same kind of quantity (money):

$$
\text{Share of } i = \frac{C_iT_i}{\sum_j C_jT_j} \times \text{Total Profit}
$$

──────────────────────────────
CHECK EVERY FORMULA FOR DIMENSIONAL CORRECTNESS
──────────────────────────────

Before writing any formula — in formulas_used or anywhere in a
solution — check what kind of quantity sits on each side of "=".
Money must equal money, a ratio must equal a ratio, a time must equal
a time. If the two sides are different kinds of quantities, the
formula is wrong.

WRONG (dividing money by money cannot produce a time):
$$
\text{Time} = \frac{\text{Profit}}{\text{Capital}}
$$

CORRECT (profit ratio is built from capital and time together, as a
proportionality, never as a quotient that changes the kind of
quantity you end up with):
$$
\text{Profit ratio} \propto \text{Capital} \times \text{Time}
$$

If unsure whether a formula is dimensionally sound, plug in the actual
numbers from the current question and check whether both sides
genuinely match before including it anywhere in the output.

──────────────────────────────
OTHER MATH SYMBOLS
──────────────────────────────

Use: $\frac{a}{b}$ · $\sqrt{x}$ · $x^2$ · $x_n$ · $\times$ · $\div$ ·
$35:10:9$

For a currency amount that is the result of a LaTeX calculation,
close the math block first and write ₹ outside:
"which gives ₹$\frac{2430\times10}{54}$" is WRONG —
instead write "which gives

$$
\frac{2430\times10}{54}
=
450
$$

so the amount is ₹450."

Percentages: write $50\%$, never plain "50%", whenever the number is
part of a calculation or combined with other math. Plain "50%" in an
ordinary sentence with no other math around it is acceptable, but
when in doubt, wrap it.

──────────────────────────────
NO MIXING WITHIN A SENTENCE
──────────────────────────────

Never mix plain text mathematics and LaTeX in the same sentence or
field.

WRONG: "C gets 3/5. Remainder is 2/5. Ratio of capitals = $1:1:3$."
CORRECT: "C gets $\frac{3}{5}$. Remainder is $\frac{2}{5}$. Ratio of
capitals = $1:1:3$."

Never output an un-escaped LaTeX command in the final JSON text, and
never output a doubly-escaped one either — see JSON ESCAPING below
for the exact rule.

──────────────────────────────
JSON ESCAPING FOR LATEX (CRITICAL)
──────────────────────────────

paraphrased_question, traditional_solution, and shortcut_solution are
JSON string fields. Every example of LaTeX shown anywhere in this
document (e.g. $\frac{5}{18}$) is written in its final, human-readable
form — a single backslash.

When you actually emit the JSON output, that single backslash must be
written as a literal double backslash inside the JSON string, because
a lone backslash is not valid inside a JSON string. This is standard
JSON string escaping, not a special transformation — apply it to
every backslash, every time, with no exceptions:

A human-readable LaTeX command       →  What you write in the JSON string
$\frac{5}{18}$                        →  $\\frac{5}{18}$
\times                                →  \\times
\sqrt                                 →  \\sqrt

After the JSON is parsed back into a string by the consuming
application, the double backslash becomes a single backslash again,
which is what the KaTeX renderer expects. Do this exactly once per
backslash — never leave a backslash unescaped, and never escape it
twice (e.g. \\\\frac is as wrong as \frac).

══════════════════════════════
DISPLAY (MOBILE READABILITY)
══════════════════════════════

The output will be rendered inside an Ionic mobile application using Markdown and KaTeX.

Use multiple short paragraphs, with a blank line between every major step.

Avoid long paragraphs and walls of text.

If traditional_solution would otherwise come out shorter than 6
lines, that almost always means a step's explanation got compressed
into the same line as its equation — split them onto separate lines
instead of shortening the explanation.

Prefer:

Given

$A=10$

$B=20$

Therefore,

$$
A+B=10+20=30
$$

Hence, the answer is $\boxed{30}$.

Aim for 6–20 short lines depending on question complexity, easy to
scan vertically on a phone screen.

──────────────────────────────
JSON STRING FORMAT FOR SOLUTIONS (CRITICAL)
──────────────────────────────

Use \n inside the string to separate lines, and \n\n between major
steps. A solution string with zero \n characters is always wrong, and
a solution with a calculation embedded inside a sentence is always
wrong.

WRONG (collapsed into one line, calculation embedded in a sentence):
"traditional_solution": "The ratio of investments is 150000:180000:210000 = 5:6:7. A's share = 5/18 x 81900 = ₹22500."

CORRECT (each idea on its own line, equations in their own display
blocks, fractions properly wrapped):
"traditional_solution": "The ratio of investments is\n\n$$\n150000:180000:210000\n=\n5:6:7\n$$\n\nSince profit is shared in the same ratio, A receives $\\frac{5}{18}$ of the total profit, because A's part of the ratio is 5 out of the total 18 parts.\n\nTherefore,\n\n$$\n\\frac{5}{18}\\times81900\n=\n22500\n$$\n\nHence, A's share = ₹22500."

(Note the doubled backslashes above — \\frac, \\times — exactly as
required by JSON ESCAPING.)

══════════════════════════════
CHAPTER
══════════════════════════════

Provide:

chapter

Use snake_case.

Example:

partnership

This is just the chapter identifier. Pattern and sub-pattern
classification are handled by a separate pass and are NOT part of
this task — do not invent pattern, subpattern, or canonical_method
values here.

══════════════════════════════
DIFFICULTY
══════════════════════════════

Choose one, based on the genuine difficulty of the ORIGINAL question
(number of steps, number of unknowns, conceptual subtlety) — not on
how long your explanation turned out to be:

easy

medium

hard

══════════════════════════════
CONCEPTS
══════════════════════════════

Provide the key concepts genuinely involved in solving THIS question.

Examples:

ratio

fractions

percentages

profit sharing

time-weighted investment

══════════════════════════════
PREREQUISITES
══════════════════════════════

Provide prerequisite topics a student must already know before
attempting this question.

Examples:

ratio

fractions

percentages

══════════════════════════════
FORMULAS USED
══════════════════════════════

Return this in the field name exactly as: formulas_used

Provide the formula(s) actually used to solve this specific question,
in LaTeX format. Every formula must be dimensionally correct — see
CHECK EVERY FORMULA FOR DIMENSIONAL CORRECTNESS above.
Use $\propto$ for proportional relationships and $=$ only when both
sides are genuinely the same kind of quantity.

Examples:

$\text{Profit ratio} \propto \text{Capital} \times \text{Time}$

$\text{Share} = \dfrac{\text{Total Profit} \times \text{Individual Ratio}}{\text{Sum of Ratios}}$

$\text{Product of Means} = \text{Product of Extremes}$

$\text{Percentage} = \dfrac{\text{Part}}{\text{Whole}} \times 100$

Do not use vague names.

Avoid names like:

cross_multiplication_rule

formula_1

method_2

══════════════════════════════
HINTS, COMMON MISTAKES, RELATED/CONFUSING PATTERNS
══════════════════════════════

hints: 2-4 short hints a student could use to get unstuck on THIS
specific question if they were solving it independently — not generic
advice, but specific to what this question requires (e.g. "Start by
converting the time periods to the same unit before forming the
ratio").

common_mistakes: 2-4 mistakes students realistically make on THIS
exact type of question (e.g. forgetting to weight capital by time,
mixing up which partner's ratio corresponds to which letter).

related_patterns: 1-3 other question types that use a similar method
or formula to this one.

confusing_patterns: 1-3 other question types that LOOK similar to this
one on the surface but actually require a different method — the kind
of question a student might wrongly assume uses the same approach.

══════════════════════════════
MULTIPLE QUESTION REQUIREMENT
══════════════════════════════

The input contains multiple questions.

You MUST process EVERY question.

Return EXACTLY one output object for each input question.

Never skip a question.

Never merge questions.

Preserve question_number exactly.

For example:

If there are 2 input questions,

then items must contain exactly 2 objects.

Returning fewer objects is incorrect.

Before returning the response, count the number of objects inside items and verify that it equals the number of input questions.

══════════════════════════════
SELF-CHECK BEFORE RETURNING (MANDATORY, EVERY ITEM, EVERY TIME)
══════════════════════════════

Before finalizing each item, work through this checklist in order:

1. Fidelity check: compare paraphrased_question against the original
   question text you were given. Every number, name, and unit must
   match exactly. If anything differs, fix it — you are not allowed to
   change the question.

2. Answer fidelity: compare paraphrased_final_answer, the end of
   traditional_solution, and the end of shortcut_solution against the
   original solution/answer you were given. They must all agree with
   the book's answer and with each other. If anything differs, find
   the error in your own working and fix it — never change the
   target answer to match a wrong derivation.

3. Inline equations: search for any line where "$...$" contains an
   "=" sign together with a calculation. If found, rewrite it as a
   $$ display block per INLINE MATH vs. DISPLAY MATH above.

4. Chained shares: search for a sentence that reports two or more
   parties' results joined by commas or "and" (e.g. "A's share is
   ..., B's share is ..., and C's share is ..."). If any one of those
   results is written as inline math, it is wrong — per CHAINED
   SHARES IN ONE SENTENCE above, split it into one short paragraph
   and one $$ display block per party, never a single chained
   sentence.

5. Malformed delimiters: search for "$=" or "=$" anywhere — these
   patterns are always wrong. Rewrite using a proper $$ block.

6. Lost backslashes: search for "rac{", "imes", or a bare "sqrt"
   without a preceding backslash — these mean a "\" was dropped.
   Restore it ("\frac{", "\times", "\sqrt").

7. Plain-text fractions: search for "/" between two numbers (e.g.
   1/4, 3/5, 75600/27) outside a math block, in paraphrased_question,
   traditional_solution, or shortcut_solution. Convert every one to
   \frac{}{}.

8. Currency or words inside math mode: check the characters
   immediately before every closing $ or $$. If you find ₹, a plain
   number meant as currency, or a word such as "profit", "share",
   "rupees", "days", "years", or "answer" sitting inside the
   delimiters, move it outside as plain text.

9. Decimal coefficients: search for a decimal multiplying a variable
   (e.g. 0.466P). Convert it to the exact fraction it represents.

10. Delimiter balance: verify every opening $ has a matching closing
    $, and every opening $$ has a matching closing $$.

11. Backslash escaping: verify every LaTeX backslash in the literal
    JSON text is doubled exactly once, per JSON ESCAPING above —
    neither a single stray backslash nor four backslashes in a row.

12. WHY-rule coverage: scan traditional_solution for any formula,
    ratio, or substitution that appears without a preceding or
    following plain-English WHY sentence. If found, add it.

══════════════════════════════
QUALITY CHECK
══════════════════════════════

Be mathematically correct.

Do not guess.

Do not fabricate shortcuts.

Do not leave shortcut_solution empty.

Never alter the original question's numbers, scenario, options, or
final answer.

The generated explanation must be internally consistent with, and
faithful to, the original question and original answer — this
includes the FIDELITY rules above and the independent recomputation in
ANSWER CONSISTENCY above. Run the full SELF-CHECK BEFORE RETURNING
checklist one final time before returning.

The final output should look like professionally written study
material built directly on top of the real textbook question.

Return ONLY JSON matching the schema.

The traditional_solution should teach the pattern, not merely perform
calculations. Every non-arithmetic step must have a plain-English WHY
sentence, per the WHY RULE above. A beginner should be able to follow
every line without already knowing the trick — if a number or formula
appears without explanation, that is a bug.

A student should be able to fully understand the method from this
solution alone, without the original textbook and without any outside
help, while the question and answer remain identical to the book's.

Keep explanations natural and proportionate to the question's
complexity — do not pad simple questions, do not compress complex ones.

"""
