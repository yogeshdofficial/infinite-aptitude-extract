# enrichment_prompts.py

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
   - If NO: adjust the values and re-solve. Try at least two
     distinct attempts before moving to the fallback below.

5. If the question has 3 or more unknowns tied together by
   simultaneous ratio or equation constraints — staggered
   investments with multiple ratio splits, or back-solving from a
   final combined ratio to several initial unknowns — and a clean
   new number set isn't found quickly, you do not need to keep
   searching. For these specific cases only, make a SMALL, targeted
   adjustment to the original numbers instead of inventing an
   entirely new set:

   - Change one or two of the original values slightly (e.g. shift
     a capital amount, a time period, or the total profit by a
     small amount) while keeping the overall structure and ratio
     pattern the same.
   - Re-solve fully with the adjusted values to confirm the answer
     is still clean and consistent.
   - This is a lighter-touch change than full invention, but it
     must still be an actual change — do not return the original
     numbers completely unchanged.

   This relaxed path is only for genuinely multi-constraint
   simultaneous systems. For simple ratio/percentage/profit-sharing
   problems with 1-2 unknowns, time-speed-distance, ages, simple
   interest, and simple partnership, continue inventing a fully new
   set of numbers as in steps 1-4 — the relaxed path does not apply
   to these.

If you used the relaxed path, adjust the options to match the new
final answer rather than leaving the original options unchanged.

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
ANSWER CONSISTENCY
══════════════════════════════

Before returning the response:

1. Solve the generated question.

2. Verify that the traditional_solution leads to the same answer.

3. Verify that the shortcut_solution leads to the same answer.

4. Verify that paraphrased_final_answer matches the solution.

5. If the question is MCQ, ensure that exactly one option matches the final answer.

6. Ensure paraphrased_correct_option corresponds to that option.

Never return contradictory answers.

Never return incorrect options.

Never return an answer inconsistent with the solution.

══════════════════════════════
TRADITIONAL SOLUTION
══════════════════════════════

Generate a completely fresh solution.

Stay close to the original method.

Use the same approach as the textbook whenever possible.

Write for a BEGINNER who is seeing this pattern for the first time.
Assume they know basic arithmetic, ratios, and percentages, but
nothing about this specific trick or pattern.

──────────────────────────────
THE "WHY" RULE (most important rule in this section)
──────────────────────────────

Every time you write a step that is not immediately obvious,
add a short clause explaining WHY that step is valid — not just WHAT
it computes.

A step needs a "why" if a beginner could reasonably ask:
"wait, where did that come from?" or "why are we allowed to do that?"

A step does NOT need a "why" if it is pure arithmetic
(e.g. multiplying two numbers, simplifying a fraction).

Bad (states the step, hides the reasoning):
"A's profit share is $\frac{1}{5}$."

Good (states the step AND why it is true):
"Since the capitals are in the ratio $1:1:3$, A and B each get
$\frac{1}{5}$ of the total capital, so A's profit share is also
$\frac{1}{5}$ of the total profit."

Bad:
"C's ratio = $\frac{1}{3}$ of (A+B)'s ratio."

Good:
"C's share is 1/4 of the total profit, which means A and B together
get the remaining 3/4. So C's ratio must equal $\frac{1}{3}$ of
A and B's combined ratio, because $\frac{1}{4} = \frac{1}{3}\times\frac{3}{4}$."

This is the single biggest difference between a confusing solution
and a clear one. Apply it consistently, especially at the step where
a ratio, a fraction-of-total, or a substitution first appears.

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

Never include:

"Wait"

"Actually"

"Let's recalculate"

"Let's re-check"

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
LATEX
══════════════════════════════

Render EVERY mathematical expression using LaTeX. No exceptions.

Apply this to:

• question
• options
• paraphrased_final_answer
• traditional_solution
• shortcut_solution

──────────────────────────────
DISPLAY EQUATION RULE (CRITICAL)
──────────────────────────────

Simple symbols or fractions embedded naturally in a sentence may use
inline math:

"$\frac{5}{18}$"

"$50\%$"

"$1:2:3$"

However, ANY equation, calculation, or expression containing "=",
"\times", "\div", "+", "-", or multiple steps MUST use display math.

WRONG:

"A's share $= \frac{5}{18} \times 81900 =$ ₹22500."

"B's share $= \frac{6}{18}\times81900 =$ ₹27000."

CORRECT:

"A's share is"

$$
\frac{5}{18}\times81900
=
22500
$$

Therefore, A's share = ₹22500.

CORRECT:

"The ratio becomes"

$$
150000:180000:210000
=
5:6:7
$$

Never place an equation inside normal text when display math is more
appropriate.

Every equation should occupy its own line.

Never place two equations on the same line.

Prefer display math whenever an equation spans more than one operator.

This rule has higher priority than brevity.

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

WRONG (plain-text fraction mixed into a sentence):
"A and B get half of 2/5 each, which is 1/5."

CORRECT:
"A and B each get half of $\frac{2}{5}$, which is $\frac{1}{5}$."

WRONG (real bug seen in production — fraction in the question itself):
"Amit invested 1/4 of the capital, Bimal invested 1/5 of the capital"

CORRECT:
"Amit invested $\frac{1}{4}$ of the capital, Bimal invested
$\frac{1}{5}$ of the capital"

This rule applies identically inside paraphrased_question. A fraction
appearing in the question text is just as much a bug as one appearing
in the solution.

──────────────────────────────
CURRENCY AND PERCENT BOUNDARIES (real bug seen in production)
──────────────────────────────

The ₹ symbol and the % sign are NOT math symbols. They must never sit
inside a $...$ block without being properly handled, and they must
never straddle the boundary of one.

WRONG (real bug — ₹ and the final number get pulled inside the math
block, right after \right), with no \text{} wrapper around them):
"Cost price of 15 oranges = $\left( \frac{12}{5} \times 15 \right) = ₹ 36$."

The closing $ in that example landed AFTER "₹ 36" instead of right
after \right). This puts a bare ₹ character inside KaTeX math mode,
where it is not a valid math symbol, breaking the render.

CORRECT — close the $ block immediately after the LaTeX expression
ends, then write ₹ and the number as plain text outside it:
"Cost price of 15 oranges = $\left(\frac{12}{5}\times15\right)$ = ₹36."

Rule: the $ ... $ boundary must end exactly where the LaTeX expression
ends. Never let plain text (₹, a currency amount, a word like "profit")
fall inside the $ ... $ block. Never let the closing $ trail behind
the actual end of the math.

Same rule applies to %. If a percent sign is the final result of a
calculation, prefer keeping the whole expression — including the %
— inside one clean $...$ block using \%, rather than splitting % awkwardly
across the boundary:

WRONG (the boundary is unclear — \% sits right at the edge with a
trailing $ placed inconsistently):
"Profit percentage = $\left( \frac{9}{36} \times 100 \right) \% = 25\%$."

CORRECT (entire calculation including \% stays inside one $...$ block,
with the $ closing immediately after the last character of the math,
no trailing plain text inside it):
"Profit percentage = $\left(\frac{9}{36}\times100\right)\% = 25\%$"

The test before finalizing: read the characters immediately before
the closing $ in every formula. If those characters are ₹ followed by
a plain number, or any word, that $ is misplaced — move it to
immediately after the last LaTeX command/symbol instead.

──────────────────────────────
OTHER MATH SYMBOLS
──────────────────────────────

Use:

$\frac{a}{b}$

$\sqrt{x}$

$x^2$

$x_n$

$\times$

$\div$

$35:10:9$

₹ $\frac{2430\times10}{54}$

Percentages: write $50\%$, never plain "50%", whenever the number is
part of a calculation or being combined with other math. (Plain "50%"
in an ordinary sentence with no other math around it is acceptable,
but when in doubt, wrap it.)

──────────────────────────────
NO MIXING WITHIN A SENTENCE
──────────────────────────────

Never mix plain text mathematics and LaTeX in the same sentence or
the same field.

WRONG:
"C gets 3/5. Remainder is 2/5. Ratio of capitals = $1:1:3$."

CORRECT:
"C gets $\frac{3}{5}$. Remainder is $\frac{2}{5}$. Ratio of capitals
= $1:1:3$."

──────────────────────────────
JSON ESCAPING FOR LATEX (CRITICAL)
──────────────────────────────

The output is JSON.

traditional_solution and shortcut_solution are JSON strings.

Inside JSON strings, LaTeX commands MUST use escaped backslashes.

For example:

JSON representation:

"$\\frac{5}{18}$"

After JSON parsing:

"$\frac{5}{18}$"

which is what KaTeX should receive.

Similarly:

JSON:

"$$\n\\frac{5}{18}\\times81900\n=\n22500\n$$"

After parsing:

$$
\frac{5}{18}\times81900
=
22500
$$

WRONG:

"$\frac{5}{18}$"

inside a raw JSON string.

CORRECT:

"$\\frac{5}{18}$"

WRONG:

"\times"

CORRECT:

"\\times"

WRONG:

"\sqrt"

CORRECT:

"\\sqrt"

Every LaTeX command beginning with "\" must appear as "\\" inside JSON strings.

The renderer should receive a single backslash after JSON parsing.

This rule applies to:

traditional_solution

shortcut_solution

paraphrased_question

options

paraphrased_final_answer

formulas_used

──────────────────────────────
FINAL LATEX SELF-CHECK (MANDATORY)
──────────────────────────────

Before returning each item:

1. Search for every occurrence of "=".

If "=" appears inside a sentence containing "$...$",

rewrite the equation using display math.

2. Search for any line containing:

$=


=$

These patterns are always incorrect.

Rewrite using:

$$
...
$$

3. Search for:

rac{

imes

sqrt

frac{

These indicate a lost backslash.

Replace:

rac{

with

\frac{

Replace:

imes

with

\times

Replace:

sqrt

with

\sqrt

4. Search for plain fractions:

1/2

3/5

7/18

outside LaTeX.

Convert them to:

$\frac{1}{2}$

$\frac{3}{5}$

$\frac{7}{18}$

5. Search for ₹ inside $$...$$.

Currency symbols must be outside math blocks.

6. Search for words inside math blocks.

Words such as:

profit

share

days

years

rupees

answer

should not appear inside math mode.

7. Verify every opening "$" has a matching closing "$".

8. Verify every opening "$$" has a matching closing "$$".

9. Verify that every LaTeX command begins with "\" after JSON parsing.

──────────────────────────────
SELF-CHECK BEFORE RETURNING
──────────────────────────────

Before finalizing each item, re-scan paraphrased_question,
traditional_solution, and shortcut_solution for the character "/"
appearing between two numbers (e.g. 1/4, 3/5, 75600/27). If found
outside a $...$ block, convert it to \frac{}{} and rewrite that
sentence. This check is mandatory for every item, every time.

Also re-scan every closing $ in those same fields. Check the
characters immediately before each closing $. If you find ₹ followed
by a number, or any plain word, immediately before a closing $, that
$ is misplaced — the currency symbol and number got pulled inside
math mode by mistake. Move the closing $ to immediately after the
last real LaTeX command or symbol, and write the ₹ amount as plain
text right after it instead. This check is mandatory for every item,
every time.

Also re-scan every numeric value in paraphrased_question for plain
"/" fractions as described above.

══════════════════════════════
DISPLAY
══════════════════════════════

The output will be rendered inside an Ionic mobile application using Markdown and KaTeX.

Solutions should look pleasant on a phone.

Use multiple short paragraphs.

Place each important equation on its own separate paragraph.

Surround standalone equations with $$ ... $$.

Example:

"The ratio of investments is"

$$
150000:180000:210000
=
5:6:7
$$

The sum of the ratio parts is

$$
5+6+7=18
$$

Since profit is divided in the same ratio, A receives

$$
\frac{5}{18}
$$

of the total profit.

Therefore,

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500.

Place intermediate calculations on separate lines.

Leave blank lines between major steps.

Avoid long paragraphs.

Avoid walls of text.

Do not compress many equations into one sentence.

Do not put several equations on the same line.

If traditional_solution would otherwise come out shorter than
5 lines, that almost always means a step's explanation got
compressed into the same line as its equation — split them onto
separate lines instead of shortening the explanation.

Prefer:

Given

$A=10$

$B=20$

Therefore,

$A+B=30$

Hence, the answer is

$\boxed{30}$

The solution should be easy to scan vertically.

Aim for 5–15 short lines.

The answer should be visually clean and pleasant to read.

──────────────────────────────
MARKDOWN + KATEX COMPATIBILITY
──────────────────────────────

The output will be rendered by Markdown and KaTeX.

Therefore equations must be written in Markdown-safe form.

Simple inline expressions may use:

$...$

Examples:

$\frac{5}{18}$

$x^2$

$25\%$

Standalone calculations must use display math:

$$
...
$$

WRONG:

"A's share $=\frac{5}{18}\times81900=$ ₹22500."

CORRECT:

"A's share is

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500."

Never place calculations inside sentences.

Never mix normal text and equations inside one math block.

Never allow ₹ or words such as:

profit

share

answer

rupees

years

days

inside a math block.

WRONG:

$$
\frac{5}{18}\times81900=₹22500
$$

CORRECT:

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500.

Every equation containing:

=

+

-

\times

\div

multiple fractions

or several operations

must use display math.

Display equations should occupy their own paragraph.

──────────────────────────────
DISPLAY MATH RULE (VERY IMPORTANT)
──────────────────────────────

Inline math ($...$) should only be used for:

- single fractions

- ratios

- variables

- percentages

Examples:

$\frac{5}{18}$

$2:3$

$x^2$

$25\%$

Any expression involving calculations must use display math.

WRONG:

"A's share $=\frac{5}{18}\times81900=$ ₹22500."

WRONG:

"Profit percentage $=\frac{20}{80}\times100=25\%$."

CORRECT:

"A's share is"

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500.

CORRECT:

"The profit percentage is"

$$
\frac{20}{80}\times100
=
25\%
$$

Therefore, the profit percentage is $25\%$.

Never place equations inside sentences.

Never mix normal text and calculations inside the same $...$ block.

Display equations are preferred over inline equations whenever possible.

──────────────────────────────
JSON STRING FORMAT FOR SOLUTIONS (CRITICAL)
──────────────────────────────

traditional_solution and shortcut_solution are JSON string fields.

Use \n and \n\n inside the string to separate paragraphs and equations.

Simple fractions inside ordinary sentences may use inline math.

However, calculations and equations must be written using display math.

WRONG:

"traditional_solution": "A's share = $\frac{2}{5}\times5000$ = ₹2000."

WRONG:

"traditional_solution": "The ratio is $2:3$. A's share $=\frac{2}{5}\times5000=$ ₹2000."

CORRECT:

"traditional_solution":
"A's share is\n\n$$\n\\frac{2}{5}\\times5000\n=\n2000\n$$\n\nHence, A's share = ₹2000."

CORRECT:

"traditional_solution":
"The capitals are in the ratio $2:3$.\n\nSince profit is shared in the same ratio,\n\nA receives $\frac{2}{5}$ of the total profit.\n\nTherefore,\n\n$$\n\frac{2}{5}\times5000\n=\n2000\n$$\n\nHence, A's share = ₹2000."

Rules:

- Use \n\n between major ideas.

- Every display equation must be surrounded by $$ and placed on its own paragraph.

- Inside display equations, place each stage on a separate line.

Example:

$$
\frac{2}{5}\times5000
=
2000
$$

Never write:

"$a=b=c$"

Prefer:

$$
a
=
b
=
c
$$

Never embed calculations inside sentences.

WRONG:

"A's share $=\frac{2}{5}\times5000=$ ₹2000."

WRONG:

"The percentage $=\frac{20}{80}\times100=25\%$."

CORRECT:

"The percentage is"

$$
\frac{20}{80}\times100
=
25\%
$$

Therefore, the percentage is $25\%$.

Every equation containing:

=

\times

\div

+

-

multiple fractions

or more than one operation

should use display math.

The preferred structure is:

Explanation sentence.

Blank line.

$$
equation
$$

Blank line.

Conclusion sentence.

A solution string containing no \n characters is always incorrect.

A solution string with calculations embedded inside a sentence is also incorrect.

──────────────────────────────
PREFERRED SOLUTION LAYOUT
──────────────────────────────

Explanation sentence.

Blank line.

Single equation.

Blank line.

Explanation sentence.

Blank line.

Single equation.

Blank line.

Conclusion sentence.

Example:

"The ratio of investments is"

$$
150000:180000:210000
=
5:6:7
$$

The sum of the ratio parts is

$$
5+6+7
=
18
$$

Since profit is shared in the same ratio, A receives

$\frac{5}{18}$

of the total profit.

Therefore,

$$
\frac{5}{18}\times81900
=
22500
$$

Hence, A's share = ₹22500.

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

Provide formulas in LaTeX format.

Examples:

$\\text{Profit Ratio} = \\text{Capital} \\times \\text{Time}$

$\\text{Share} = \\dfrac{\\text{Total Profit} \\times \\text{Individual Ratio}}{\\text{Sum of Ratios}}$

$\\text{Product of Means} = \\text{Product of Extremes}$

$\\text{Percentage} = \\dfrac{\\text{Part}}{\\text{Whole}} \\times 100$

Do not use vague names.

Avoid names like:

cross_multiplication_rule

formula_1

method_2

══════════════════════════════
IMPORTANT
══════════════════════════════
Use blank lines between major calculation steps.

Each equation or intermediate result should appear on its own line.

Preserve readability for phone screens.

Never compress the entire solution into one paragraph.

Separate explanatory sentences and calculations using newline characters.

traditional_solution and shortcut_solution must contain newline characters.

Use multiple short paragraphs.

Display equations and intermediate values on separate lines.

Do not return the entire solution as one paragraph.

Be mathematically correct.

Do not invent unnecessary information.

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
──────────────────────────────
EQUATION SELF-CHECK (MANDATORY)
──────────────────────────────

Search for any line containing both "$" and "=".

If such a line exists, rewrite that expression using display math:

$$
...
$$

A line such as

"A's share $= \frac{5}{18}\times81900 =$ ₹22500."

is always wrong.

Calculations must never be embedded inside sentences.

The preferred structure is:

Explanation sentence.

Blank line.

$$
equation
$$

Blank line.

Conclusion sentence.

This check is mandatory before returning every item.
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

The generated question, options, solutions and final answer must be internally consistent.

The final output should look like professionally written study material.

Return ONLY JSON matching the schema.

The traditional_solution should teach the pattern, not merely perform calculations.

Every major step should have a brief explanation.

A student should be able to understand the method without looking at the original textbook.

Keep explanations concise and natural.

Use new numerical values for most questions. For genuinely
multi-constraint questions, a small targeted adjustment to the
original numbers is acceptable rather than a fully new set.

"""
