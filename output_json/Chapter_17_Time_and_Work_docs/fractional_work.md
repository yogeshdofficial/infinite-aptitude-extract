# Fractional Work

## Overview
This pattern involves tasks where you are given the time taken to complete only a *fraction* of a total job. The central idea is to convert these fractional rates into the time required for the *whole* work (1 unit) before performing any further calculations.

---

## Recognition Clues
* Keywords: "$\frac{1}{x}$ of a work", "percentage of work", "completes in $y$ days".
* Given: Time taken to complete a specific fraction or percentage of a task.
* Asked: Total time to complete the whole work, or combined time for multiple people.
* Look for: Multiple people with different fractional work rates.

---

## Key Formulas

### [Total Time Calculation]
$$
\text{Total Time} = \text{Time taken} \times \frac{1}{\text{Fraction of work}}
$$

**Variables:**
- $\text{Time taken}$ = days/minutes given in the problem.
- $\text{Fraction of work}$ = the portion of the job completed (e.g., $\frac{1}{4}$).

**When to use:** To find the time required for one person to finish the entire job.

**Worked example:** If X does $\frac{1}{4}$ of work in 10 days, Total Time = $10 \times \frac{1}{1/4} = 10 \times 4 = 40$ days.

### [Combined Rate]
$$
\text{Combined Rate} = \text{Rate}_A + \text{Rate}_B + \dots
$$

**Variables:**
- $\text{Rate}$ = $\frac{1}{\text{Total Time}}$ (work done per unit of time).

**When to use:** To find how long it takes for multiple people to finish a job together.

**Worked example:** If A takes 15 days ($\text{Rate} = \frac{1}{15}$) and B takes 25 days ($\text{Rate} = \frac{1}{25}$), Combined Rate = $\frac{1}{15} + \frac{1}{25} = \frac{8}{75}$.

---

## Solution Framework

1. **Normalize:** Convert all given fractional/percentage work times into the time taken for the *whole* work (1 unit).
2. **Rate Conversion:** Convert each person's total time into a daily/minute rate by taking the reciprocal ($\frac{1}{\text{Total Time}}$).
3. **Combine:** Add the individual rates together to find the collective work rate.
4. **Finalize:** Take the reciprocal of the combined rate to find the total time taken for the whole work.

---

## Shortcut Tricks

* **Trick:** For two people, if A takes $a$ days and B takes $b$ days, combined time is $\frac{a \times b}{a + b}$.
* **Why it works:** This is a simplified algebraic form of $\frac{1}{a} + \frac{1}{b} = \frac{a+b}{ab}$.
* **When to use:** When you have exactly two people and their total times are known.
* **Example:** A takes 15 days, B takes 25 days. Combined = $\frac{15 \times 25}{15 + 25} = \frac{375}{40} = 9\frac{3}{8}$ days.

---

## Common Mistakes

* **Mistake:** Adding the given days directly (e.g., $15+25$) instead of adding rates.
* **Why it happens:** Intuitive but mathematically incorrect; time is inversely proportional to work rate.
* **Fix:** Always convert to rates ($\frac{1}{T}$) before adding.
* **Mistake:** Forgetting to invert the final combined rate.
* **Why it happens:** Stopping at the "work per day" value instead of "days per work."
* **Fix:** Always take the reciprocal of the final sum.

---

## Worked Example (Step-by-Step)

**Question:** A can complete $\frac{1}{3}$ of a work in 5 days and B, $\frac{2}{5}$ of the work in 10 days. In how many days both A and B together can complete the work?

**Solution:**
1. **Normalize:** A's total time = $5 \times 3 = 15$ days. B's total time = $10 \times \frac{5}{2} = 25$ days.
2. **Rate Conversion:** A's rate = $\frac{1}{15}$. B's rate = $\frac{1}{25}$.
3. **Combine:** Combined rate = $\frac{1}{15} + \frac{1}{25} = \frac{5+3}{75} = \frac{8}{75}$.
4. **Finalize:** Total time = $\frac{75}{8} = 9\frac{3}{8}$ days.

**Answer:** $9\frac{3}{8}$ days.

---

## Similar Patterns

**Work-Efficiency Patterns:** Distinguished by "A is twice as fast as B" instead of fractional work; use ratios instead of reciprocals.

---

## Revision Summary

* **Key formula:** $\text{Total Time} = \text{Time} \times \text{Reciprocal of Fraction}$.
* **Spot it by:** Given time for a fraction of work.
* **First move:** Calculate time for the *whole* work for each person.
* **Fastest method:** Use $\frac{ab}{a+b}$ for two people.
* **Biggest trap:** Adding days instead of rates.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Reciprocals** — The value $\frac{1}{x}$ is the reciprocal of $x$.
* **Fractions** — Ability to add fractions with different denominators using LCM.
* **Percentages** — Convert percentage to fraction (e.g., $40\% = \frac{40}{100} = \frac{2}{5}$).

### Formulas You Must Know First
$$
\text{Rate} = \frac{\text{Work}}{\text{Time}}
$$
**What it means:** Work rate is the amount of work done per unit of time.
**Example:** If 1 work is done in 5 days, rate is $\frac{1}{5}$ work/day.

### Terms Used In This Pattern
* **Work Rate** — The portion of a task completed in one unit of time.
* **Whole Work** — Represented as 1 (the complete task).