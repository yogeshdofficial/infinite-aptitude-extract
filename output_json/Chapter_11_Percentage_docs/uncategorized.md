# Percentage-Based Distribution and Difference Analysis

## Overview
This pattern involves calculating changes in tax/cost based on rate differences or determining missing values in a multi-part distribution (like test scores or investment returns). The central idea is to treat the "Total" as a base and apply percentages to specific segments or differences to find the required result.

---

## Recognition Clues
* **Keywords:** "reduced from... to...", "what difference does it make", "what percent of", "average rate of return", "how many more questions".
* **Given:** A total value (e.g., marked price, total capital, total questions) and multiple percentage rates or segments.
* **Asked:** The difference in final amounts, the average percentage, or the "gap" needed to reach a target.

---

## Key Formulas

### [Difference in Amount]
$$
\text{Difference} = (\text{Rate}_1 - \text{Rate}_2) \times \text{Total Value}
$$
**Variables:** $\text{Rate}_1, \text{Rate}_2$ = percentage rates; $\text{Total Value}$ = the base amount.
**When to use:** When asked for the change in cost/tax due to a change in percentage rate.
**Worked example:** Tax reduced from $11\frac{1}{3}\%$ to $3\frac{1}{3}\%$ on ₹ 8400. Difference = $(11\frac{1}{3} - 3\frac{1}{3})\% \text{ of } 8400 = 8\% \text{ of } 8400 = 672$.

### [Weighted Average Percentage]
$$
\text{Average Rate} = \frac{\sum (\text{Rate}_i \times \text{Part}_i)}{\text{Total}}
$$
**Variables:** $\text{Rate}_i$ = percentage for segment $i$; $\text{Part}_i$ = value of segment $i$.
**When to use:** When calculating the overall return or average performance across different segments.
**Worked example:** 3% on $\frac{1}{4}$ capital, 5% on $\frac{2}{3}$ capital, 11% on remainder ($\frac{1}{12}$). Total = $(3\% \times 0.25) + (5\% \times 0.66) + (11\% \times 0.083) = 5\%$.

---

## Solution Framework

**Step 1: Identify the Base** — Assign a variable (e.g., $x$) or use the given total to define the "whole."
**Step 2: Segment the Data** — Break the total into the specific parts mentioned (e.g., arithmetic/algebra/geometry or capital portions).
**Step 3: Calculate Individual Parts** — Apply the specific percentage to each segment to find the actual value.
**Step 4: Aggregate or Compare** — Sum the parts to find the total achieved or subtract to find the difference.
**Step 5: Final Adjustment** — If a target is missing, subtract the achieved total from the target total.

---

## Shortcut Tricks

* **Trick:** For tax/price differences, subtract the rates *first* before multiplying by the total.
* **Why it works:** Distributive property: $P \times R_1 - P \times R_2 = P \times (R_1 - R_2)$.
* **When to use:** When the base (Total) remains constant for both rates.
* **Example:** $8\% \text{ of } 8400$ is much faster than calculating $11\frac{1}{3}\% \text{ of } 8400$ and $3\frac{1}{3}\% \text{ of } 8400$ separately.

---

## Common Mistakes

* **Mistake:** Calculating percentages on the wrong base (e.g., using the remaining part as the total).
* **Fix:** Always verify the "of" phrase (e.g., "of the total" vs "of the remainder").
* **Mistake:** Forgetting to divide by the total when asked for an "average rate."
* **Fix:** Ensure the final step is $\frac{\text{Total Return}}{\text{Total Capital}} \times 100$.

---

## Worked Example (Step-by-Step)

**Question:** Shobha’s test had 75 problems: 10 arithmetic, 30 algebra, 35 geometry. She got 70% of arithmetic, 40% of algebra, 60% of geometry. How many more questions needed for 60% total?

**Solution:**
1. **Calculate correct answers:**
   - Arithmetic: $70\% \text{ of } 10 = 7$
   - Algebra: $40\% \text{ of } 30 = 12$
   - Geometry: $60\% \text{ of } 35 = 21$
2. **Sum achieved:** $7 + 12 + 21 = 40$.
3. **Calculate target:** $60\% \text{ of } 75 = 45$.
4. **Find gap:** $45 - 40 = 5$.

**Answer:** 5 questions.

---

## Similar Patterns
**Weighted Average Problems:** Distinguished by the request for a single "average" rate rather than a specific count or difference.

---

## Revision Summary
* **Key formula:** $\text{Difference} = (\Delta \text{Rate}) \times \text{Base}$.
* **Spot it by:** Multiple segments with different percentage rates.
* **First move:** Calculate the value of each segment individually.
* **Fastest method:** Subtract rates first if the base is constant.
* **Biggest trap:** Confusing "of the total" with "of the remainder."

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage** — A fraction with 100 as the denominator; $x\% = \frac{x}{100}$.
* **Weighted Sum** — The total value obtained by summing individual parts: $\sum (\text{Value}_i \times \text{Weight}_i)$.

### Formulas You Must Know First
* **Part Calculation:** $\text{Part} = \text{Percentage} \times \text{Total}$.

### Terms Used In This Pattern
* **Marked Price** — The base value of an article before tax or discount.
* **Remainder** — The portion left after subtracting other segments from the total.