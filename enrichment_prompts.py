# enrichment_prompts.py


ENRICHMENT_PROMPT = r"""
You are creating a high-quality aptitude question bank for students.

The goal is NOT to create a completely different problem.

The goal is to create independently written material that preserves the same mathematical structure and solving pattern.

══════════════════════════════
PARAPHRASED QUESTION
══════════════════════════════

Rewrite the question slightly.

Preserve:

• mathematical structure
• difficulty
• solving pattern
• answer type

You may change:

• names
• objects
• wording
• numerical values

Choose new numbers carefully so that:

• answers remain clean
• answers remain positive
• ugly fractions are avoided
• the resulting answer is similar in complexity to the original answer

Do not make unnecessary changes.

Students familiar with the original problem should immediately recognize the pattern.

Do not mechanically substitute synonyms.

Write naturally.
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

Explain like an experienced teacher.

The solution should teach the student how to think.

Show the reasoning behind each major step.

Explain why formulas are being used.

Do not merely write equations without explanation.

However, avoid excessive verbosity.

Use short explanatory sentences.

Show every important intermediate calculation.

Do not skip algebraic steps.

The solution should feel like a teacher solving the problem on a board.

Avoid robotic wording.

Avoid:

Step 1
Step 2
Step 3

Prefer:

First,

Next,

Therefore,

Hence,

Because,

Since,

Thus,

The explanation should be concise but sufficiently detailed for a student seeing the pattern for the first time.

Never assume that the student already understands the method.

Never include:

"Wait"

"Actually"

"Let's recalculate"

"Let's re-check"

The solution should appear final and polished.

Aim for approximately 5–15 short lines.

Balance explanation and brevity.

The solution should be easy to read on a mobile phone.

══════════════════════════════
SHORTCUT SOLUTION
══════════════════════════════

If a genuine shortcut exists,
provide it.

If no genuine shortcut exists:

provide a shorter version of the traditional solution.

Never leave shortcut_solution empty.

Never invent unrealistic tricks.

Keep the shortcut concise and easy to remember.

══════════════════════════════
LATEX
══════════════════════════════

Render EVERY mathematical expression using LaTeX.

Apply this to:

• question
• options
• paraphrased_final_answer
• traditional_solution
• shortcut_solution

Examples:

$\frac{a}{b}$

$\sqrt{x}$

$x^2$

$x_n$

$\times$

$\div$

$35:10:9$

₹ $\frac{2430\times10}{54}$

Never mix plain text mathematics and LaTeX.

Never output escaped LaTeX such as:

\\frac

\\sqrt

Output proper LaTeX:

\frac

\sqrt

══════════════════════════════
DISPLAY
══════════════════════════════

The output will be rendered inside an Ionic mobile application using Markdown and KaTeX.

Solutions should look pleasant on a phone.

Use multiple short paragraphs.

Place each important equation on a separate line.

Place intermediate calculations on separate lines.

Leave blank lines between major steps.

Avoid long paragraphs.

Avoid walls of text.

Do not compress many equations into one sentence.

Do not put several equations on the same line.

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

══════════════════════════════
CLASSIFICATION
══════════════════════════════

Provide:

chapter

pattern

subpattern

canonical_method

Use snake_case.

Examples:

profit_sharing

time_weighted_capital_ratio

combined_work

unit_digit_cycle

alligation

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



"""
