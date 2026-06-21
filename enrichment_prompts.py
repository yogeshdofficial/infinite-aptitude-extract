# enrichment_prompts.py

ENRICHMENT_PROMPT = r"""
You are creating a high-quality aptitude question bank for students.

The goal is NOT to create a completely different problem.

The goal is to create independently written material that preserves the same mathematical structure and solving pattern.

══════════════════════════════
CHOOSING NEW NUMBERS
══════════════════════════════

For most questions, invent a new set of numerical values that
preserves the structure and difficulty of the original.

Procedure for most questions:

1. Identify every free numeric input in the question.

2. Pick new values for those inputs.

3. Solve the question fully with the new values.

4. Check: is the final answer clean (integer, or a simple fraction
   with denominator ≤ 12), positive, and roughly the same order of
   magnitude/complexity as the original answer?

   - If YES: use these new numbers. Done.
   - If NO: make ONE more attempt with a different number set. If
     that attempt also fails to give a clean answer, move immediately
     to the RELAXED PATH below — do not attempt a third full
     invention.

5. RELAXED PATH — for any question where two full invention attempts
   have not produced a clean answer, OR where the question has 3 or
   more unknowns tied together by simultaneous ratio or equation
   constraints (staggered investments with multiple ratio splits,
   back-solving from a combined ratio to several initial unknowns,
   multi-party time-weighted capitals, etc.):

   Make a SMALL, targeted adjustment to the original numbers instead
   of inventing an entirely new set:

   - Change one or two of the original values slightly (e.g. shift
     a capital amount, a time period, or the total profit by a small
     amount — typically 10–20% of the original value) while keeping
     the overall structure and ratio pattern the same.
   - Re-solve fully with the adjusted values to confirm the answer
     is still clean and consistent.
   - This is a lighter-touch change than full invention, but it must
     still be an actual change — do not return the original numbers
     completely unchanged.
   - If the first small adjustment still gives an unclean answer,
     try one more small adjustment (shift a different value) and
     accept that result regardless of whether the answer is a simple
     fraction (denominator ≤ 12 is still the target but is no longer
     a hard gate). The question must proceed — never loop further.

   This relaxed path is available for ANY question where invention
   is proving difficult, not only multi-constraint problems.
   However, for simple ratio/percentage/profit-sharing problems with
   1–2 unknowns, time-speed-distance, ages, simple interest, and
   simple (non-staggered) partnership, prefer full invention and
   only fall back to the relaxed path as a true last resort.

If you used the relaxed path, update the options to match the new
final answer rather than leaving the original options unchanged.

══════════════════════════════
NUMBER LOCKING (CRITICAL — READ BEFORE WRITING ANYTHING)
══════════════════════════════

Everything in the section above — picking numbers, solving, checking
they are clean, retrying if they are not — is internal scratch work.
Do it silently, in your head, before you write a single word of the
question, options, or solutions.

Once a number set produces a clean, fully verified answer, it is
LOCKED:

- question, every option, traditional_solution, shortcut_solution,
  and paraphrased_final_answer must all be built from this one
  locked set of numbers, from start to finish.
- Never change a number, a total, a ratio, or a sub-total partway
  through writing a solution. If a solution stops working out
  cleanly while you are drafting it, that means the numbers were
  never properly verified — stop, discard that attempt, pick and
  verify a new number set from scratch, and only then start writing
  the solution again from the beginning.
- The text you return must read as if you solved the problem
  correctly on the very first attempt. None of your internal trial
  and error, false starts, or self-corrections may appear anywhere
  in the output.

This is the most common source of a broken question: a solution that
quietly swaps in a different total profit, ratio, or rent halfway
through, so the question, the options, and the final answer end up
describing different problems. Locking the numbers before writing
prevents this completely.

Banned phrases — none of these may ever appear in question,
traditional_solution, shortcut_solution, or paraphrased_final_answer.
If you are about to write one, a number is being changed mid-solution,
which is not allowed. Stop, fix the number set internally, and
rewrite the solution cleanly from scratch instead:

"Wait" · "Actually" · "Let's adjust" · "let's adjust the ratio" ·
"let's adjust total profit" · "let's adjust total rent" ·
"Let's re-verify" · "Let's recalculate" · "Let's re-check" ·
"Let's simplify" (when it means "let's change the numbers") ·
"Hold on" · "Hmm" · "On second thought" · "Let me reconsider"

A finished, polished solution never narrates its own corrections —
it only ever shows the one correct path, using the locked numbers.

──────────────────────────────
INTERNAL SEARCH MUST NEVER APPEAR
──────────────────────────────

Choosing numbers, retrying values, adjusting totals, and checking
whether an answer is clean are INTERNAL operations only.

These operations are invisible to the reader.

The final output must read as if the numbers were correct from the
very beginning.

Never explain that a value was changed to obtain a cleaner answer.

Never explain that a number was selected because it produces an
integer answer.

Never explain that a total was modified to avoid fractions.

Never explain that a ratio was adjusted.

Never explain that a different set of values was tried earlier.

Never explain why a particular number was chosen.

The reader should not be aware that any search or verification
occurred.

WRONG:

"Since the prompt requires a clean answer, we adjust the profit to
₹23,000."

WRONG:

"To obtain an integer answer, let us change the total profit."

WRONG:

"Because the previous value gives a fraction, we modify the ratio."

WRONG:

"After checking, we use ₹48,000 instead."

WRONG:

"To make the calculations easier, we take the profit as ₹90,000."

WRONG:

"Since the answer is not clean, we choose different numbers."

WRONG:

"We slightly alter the investment amount."

WRONG:

"The original values lead to decimals, so we adjust them."

These sentences reveal internal scratch work and are forbidden.

CORRECT:

"The total profit is ₹23,000."

CORRECT:

"Given that the total profit is ₹23,000, ..."

CORRECT:

"Since profit is shared in the ratio of capitals, ..."

Only describe the final locked numbers as facts given by the
generated question.

The existence of alternative numbers, retries, adjustments,
verification, or prompt requirements must remain completely hidden.

══════════════════════════════
PARAPHRASED OPTIONS
══════════════════════════════

If the question is MCQ, generate fresh options.

Preserve:

• difficulty
• answer type
• relative closeness of distractors

Do not merely reorder options.

Generate natural distractors.

If you used the relaxed path for a multi-constraint question (small
adjustment to original numbers rather than a fully new set), update
the options to match the new final answer rather than reusing the
original options unchanged.

Return:

paraphrased_option_a
paraphrased_option_b
paraphrased_option_c
paraphrased_option_d

and

paraphrased_correct_option

using:

a
b
c
d

If the question is not MCQ:

all option fields should be empty strings.

══════════════════════════════
FINAL ANSWER
══════════════════════════════

Return the final answer separately.

Use LaTeX whenever appropriate.

Examples:

₹450

$35$

$\frac{7}{8}$

Do not include explanations.

Return only the final answer.

══════════════════════════════
ANSWER CONSISTENCY (CRITICAL)
══════════════════════════════

Before returning the response:

1. Solve the generated question using only the locked numbers.

2. Compute one final answer.

3. Treat this answer as the canonical answer.

4. traditional_solution must end at this answer.

5. shortcut_solution must end at this answer.

6. paraphrased_final_answer must equal this answer exactly.

7. If the question is MCQ, exactly one option must equal this answer.

8. paraphrased_correct_option must point to that option.

9. Recompute the answer independently from scratch.

10. Compare:

- answer obtained from traditional_solution

- answer obtained from shortcut_solution

- paraphrased_final_answer

- correct option value

- value corresponding to paraphrased_correct_option

All five values must be identical.

If any one of them differs, the item is broken.

Discard the entire draft and rewrite everything from the beginning
using the same locked numbers.

Never return partially corrected output.

Never return contradictory answers.

Never return multiple correct options.

Never return a correct option letter whose value differs from
paraphrased_final_answer.

Never return:

traditional_solution → ₹22,500

shortcut_solution → ₹22,500

paraphrased_final_answer → ₹27,000

option c → ₹22,500

paraphrased_correct_option → d

Such an item is invalid and must be rewritten from scratch.

──────────────────────────────
MCQ INTEGRITY CHECK (MANDATORY)
──────────────────────────────

For MCQ questions:

First determine the final answer.

Then generate the options.

Exactly one option must equal the final answer.

The other options must be incorrect.

After generating the options:

Read option a.

Read option b.

Read option c.

Read option d.

Find which option exactly matches the final answer.

Set paraphrased_correct_option to that letter.

Never guess the letter.

Never assume the correct option is the same as in the original
question.

Never reuse the original correct option position blindly.

Example:

option_a = ₹18000

option_b = ₹22500

option_c = ₹27000

option_d = ₹30000

paraphrased_final_answer = ₹22500

Therefore:

paraphrased_correct_option = b

NOT a

NOT c

NOT d

The option letter must be derived from the option values, not from
memory or from the original question.

══════════════════════════════
TRADITIONAL SOLUTION
══════════════════════════════

Generate a completely fresh solution.

Stay close to the original method.

Use the same approach as the textbook whenever possible.

Write for a BEGINNER who is seeing this pattern for the first time
and has never solved this exact type of question before. Assume they
know basic arithmetic, ratios, fractions, and percentages — but
assume NOTHING about this specific pattern, trick, or shortcut.
Never assume the reader can fill in a gap on their own.

──────────────────────────────
THE "WHY" RULE (most important rule in this section)
──────────────────────────────

Every time you write a step that is not immediately obvious,
add a short clause explaining WHY that step is valid — not just WHAT
it computes.

A step needs a "why" if a beginner could reasonably ask:
"wait, where did that come from?" or "why are we allowed to do that?"
This includes the moment a ratio first appears, the moment a fraction
of the total is introduced, the moment a substitution is made, and
the moment a formula is applied — name the formula or rule in plain
words at the point it is first used, instead of assuming the reader
recognizes it.

A step does NOT need a "why" if it is pure arithmetic
(e.g. multiplying two numbers, simplifying a fraction).

Bad (states the step, hides the reasoning):
"A's profit share is $\frac{1}{5}$."

Good (states the step AND why it is true):
"Since the capitals are in the ratio $1:1:3$, A and B each get
$\frac{1}{5}$ of the total capital, so A's profit share is also
$\frac{1}{5}$ of the total profit, because in a partnership profit is
always divided in the same ratio as capital."

Bad:
"C's ratio = $\frac{1}{3}$ of (A+B)'s ratio."

Good:
"C's share is $\frac{1}{4}$ of the total profit, which means A and B
together get the remaining $\frac{3}{4}$. So C's ratio must equal
$\frac{1}{3}$ of A and B's combined ratio, because

$$
\frac{1}{4} = \frac{1}{3}\times\frac{3}{4}
$$"

This is the single biggest difference between a confusing solution
and a clear one. Apply it consistently, especially at the step where
a ratio, a fraction-of-total, or a substitution first appears. A
beginner should never have to take a step on faith — if a number was
not directly given in the question, say in plain words where it came
from before using it in the next calculation.

──────────────────────────────
GENERAL STYLE
──────────────────────────────

Show the reasoning behind each major step.

Explain why formulas are being used.

Do not merely write equations without explanation.

However, avoid excessive verbosity.

Use short explanatory sentences.

Show every important intermediate calculation.

Do not skip algebraic steps.

The solution should feel like a teacher solving the problem on a board,
pausing exactly at the points where a student would normally get lost.

Avoid robotic wording.

Avoid:

Step 1
Step 2
Step 3

Prefer:

First,

Next,

Since,

Because,

Therefore,

Hence,

Thus,

Never assume that the student already understands the method.

Never include any of the banned phrases listed in NUMBER LOCKING
above ("Wait", "Actually", "Let's adjust", "Let's recalculate",
"Let's re-check", "Hold on", "Hmm", "On second thought"). These are
internal thinking artifacts, not finished teaching material.

The solution should appear final and polished.

Aim for approximately 5–15 short lines.

Balance explanation and brevity: explain every non-obvious step,
but do not pad obvious arithmetic with unnecessary words.

The solution should be easy to read on a mobile phone.

══════════════════════════════
SHORTCUT SOLUTION
══════════════════════════════

If a genuine shortcut exists,
provide it.

If no genuine shortcut exists:

provide a shorter version of the traditional solution.

The shortcut_solution is allowed to skip explanations
ONLY for steps already explained in traditional_solution.

If the shortcut introduces a NEW idea not present in
traditional_solution (e.g. a direct ratio trick), it still needs
one short clause of "why", using the same WHY RULE as above.

Never leave shortcut_solution empty.

Never invent unrealistic tricks.

Keep the shortcut concise and easy to remember.

══════════════════════════════
LATEX AND EQUATION FORMATTING
══════════════════════════════

Render EVERY mathematical expression using LaTeX. No exceptions.

Apply this to:

• question
• options
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
appearing in the question text is just as much a bug as one appearing
in the solution.

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

If unsure whether a formula is dimensionally sound, plug in the
locked numbers from the current question and check whether both
sides genuinely match before including it anywhere in the output.

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

traditional_solution and shortcut_solution are JSON string fields.
Every example of LaTeX shown anywhere in this document (e.g.
$\frac{5}{18}$) is written in its final, human-readable form — a
single backslash.

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
SELF-CHECK BEFORE RETURNING (MANDATORY, EVERY ITEM, EVERY TIME)
══════════════════════════════

Before finalizing each item, work through this checklist in order:

1. Inline equations: search for any line where "$...$" contains an
   "=" sign together with a calculation. If found, rewrite it as a
   $$ display block per INLINE MATH vs. DISPLAY MATH above.

2. Chained shares: search for a sentence that reports two or more
   parties' results joined by commas or "and" (e.g. "A's share is
   ..., B's share is ..., and C's share is ..."). If any one of those
   results is written as inline math, it is wrong — per CHAINED
   SHARES IN ONE SENTENCE above, split it into one short paragraph
   and one $$ display block per party, never a single chained
   sentence.

3. Malformed delimiters: search for "$=" or "=$" anywhere — these
   patterns are always wrong. Rewrite using a proper $$ block.

4. Lost backslashes: search for "rac{", "imes", or a bare "sqrt"
   without a preceding backslash — these mean a "\" was dropped.
   Restore it ("\frac{", "\times", "\sqrt").

5. Plain-text fractions: search for "/" between two numbers (e.g.
   1/4, 3/5, 75600/27) outside a math block, in paraphrased_question,
   traditional_solution, or shortcut_solution. Convert every one to
   \frac{}{}.

6. Currency or words inside math mode: check the characters
   immediately before every closing $ or $$. If you find ₹, a plain
   number meant as currency, or a word such as "profit", "share",
   "rupees", "days", "years", or "answer" sitting inside the
   delimiters, move it outside as plain text.

7. Decimal coefficients: search for a decimal multiplying a variable
   (e.g. 0.466P). Convert it to the exact fraction it represents.

8. Delimiter balance: verify every opening $ has a matching closing
   $, and every opening $$ has a matching closing $$.

9. Backslash escaping: verify every LaTeX backslash in the literal
   JSON text is doubled exactly once, per JSON ESCAPING above —
   neither a single stray backslash nor four backslashes in a row.

10. Banned phrases: confirm none of the NUMBER LOCKING banned phrases
    ("Wait", "Let's adjust", "Let's re-verify", "Hold on", etc.)
    appear anywhere in the output.

11. Answer integrity: re-run the independent recomputation from
    ANSWER CONSISTENCY step 9 and confirm it still matches
    paraphrased_final_answer, the boxed answer, and the correct
    option exactly.

12. Internal reasoning leak:

Search the entire output for any of the following phrases that
explicitly expose the number-selection process:

    "clean answer"
    "integer answer"
    "to avoid fractions"
    "to avoid decimals"
    "previous value"
    "original value"
    "earlier value"
    "retry"
    "recalculate"
    "recheck"
    "verification step"
    "we slightly"
    "we alter"
    "we modify the"
    "we tried"

Note: common words like "change", "adjust", and "original" may appear
legitimately in a question or solution (e.g. "the original price",
"find the change in profit"). Only flag them if they appear in a
sentence where they clearly describe the number-selection process
(i.e. the sentence is about why a number was chosen), not when they
describe the problem scenario itself.

If such language appears in the context of explaining number
selection, the output is invalid. Remove every reference to the
internal search process and rewrite the affected sentences so that
the locked numbers are presented as ordinary facts from the question.

The student should never know that alternative numbers were ever
considered.

13. Final answer consistency check.

Compute the answer independently.

Extract the answer appearing at the end of traditional_solution.

Extract the answer appearing at the end of shortcut_solution.

Read paraphrased_final_answer.

Read option a.

Read option b.

Read option c.

Read option d.

Determine which option equals paraphrased_final_answer.

Verify that this letter equals paraphrased_correct_option.

If any mismatch exists, the entire item is invalid.

Rewrite the question, options, and both solutions from scratch.

Never attempt to patch only one field.

All answer-bearing fields must agree exactly.

══════════════════════════════
DISPLAY (MOBILE READABILITY)
══════════════════════════════

The output will be rendered inside an Ionic mobile application using Markdown and KaTeX.

Use multiple short paragraphs, with a blank line between every major step.

Avoid long paragraphs and walls of text.

If traditional_solution would otherwise come out shorter than 5
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

Aim for 5–15 short lines, easy to scan vertically on a phone screen.

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

Choose one:

easy

medium

hard

══════════════════════════════
CONCEPTS
══════════════════════════════

Provide the key concepts involved.

Examples:

ratio

fractions

percentages

profit sharing

time-weighted investment

══════════════════════════════
PREREQUISITES
══════════════════════════════

Provide prerequisite topics.

Examples:

ratio

fractions

percentages

══════════════════════════════
FORMULAS USED
══════════════════════════════

Return this in the field name exactly as: formulas_used

Provide formulas in LaTeX format. Every formula must be dimensionally
correct — see CHECK EVERY FORMULA FOR DIMENSIONAL CORRECTNESS above.
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
QUALITY CHECK
══════════════════════════════

Be mathematically correct.

Do not guess.

Do not fabricate shortcuts.

Do not leave shortcut_solution empty.

Avoid unnecessary fractions.

Prefer clean integer answers whenever possible.

Avoid negative times, ages, distances, probabilities and quantities unless required.

Choose values producing realistic and easy-to-understand answers.

The generated question, options, solutions and final answer must be
internally consistent — this includes the locked-number discipline in
NUMBER LOCKING and the independent recomputation in ANSWER
CONSISTENCY above. Run the full SELF-CHECK BEFORE RETURNING checklist
one final time before returning.

The final output should look like professionally written study material.

Return ONLY JSON matching the schema.

The traditional_solution should teach the pattern, not merely perform
calculations. Every major step must have a brief explanation of WHY
it is valid, per the WHY RULE above — a beginner should never have to
take a step on faith or already know the trick to follow along.

A student should be able to fully understand the method from this
solution alone, without looking at the original textbook and without
any outside help.

Keep explanations concise and natural.

Use new numerical values for most questions. For genuinely
multi-constraint questions, or after two unsuccessful full-invention
attempts, a small targeted adjustment to the original numbers is
acceptable rather than a fully new set.

"""
