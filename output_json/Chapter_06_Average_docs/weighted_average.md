# Weighted Average

## Overview
This pattern involves finding the average of a combined group where subgroups have different sizes and different averages. The central idea is to calculate the **Total Sum** of all components first, then divide by the **Total Count** of items.

---

## Recognition Clues
* **Keywords:** "Average expenditure per article," "Average monthly income," "Average salary of workers," "Average score of boys/girls."
* **Given:** Multiple groups with distinct counts (or ratios) and their respective averages.
* **Asked:** The combined average of the entire set, or a missing subgroup value/count.

---

## Key Formulas

### [Weighted Average]
$$
\text{Average} = \frac{\sum (\text{Value} \times \text{Frequency})}{\sum \text{Frequency}}
$$

**Variables:**
- $\text{Value}$ = The average of a specific subgroup.
- $\text{Frequency}$ = The number of items in that subgroup.

**When to use:** When you need the overall average of multiple groups with different sizes.

**Worked example:** 5 shirts at ₹450, 4 trousers at ₹750.
$\text{Avg} = \frac{(5 \times 450) + (4 \times 750)}{5 + 4} = \frac{2250 + 3000}{9} = \frac{5250}{9} \approx 583.33$.

---

## Solution Framework

**Step 1: Calculate Total Sums** — Multiply each subgroup's average by its count to find the total value for that group.
**Step 2: Sum the Totals** — Add all the subgroup totals together to get the grand total.
**Step 3: Sum the Counts** — Add all the individual counts together to get the total number of items.
**Step 4: Divide** — Divide the grand total (Step 2) by the total count (Step 3) to get the final average.

---

## Shortcut Tricks

**Trick:** Use the **Alligation Method** for two-group problems.
**Why it works:** It directly calculates the ratio of the two groups based on their deviation from the mean.
**When to use:** When you have two groups and the overall average (e.g., Q26: Boys and Girls scores).
**Example:** Boys (71), Girls (73), Class (71.8).
Difference: $|73 - 71.8| = 1.2$ (Boys ratio), $|71 - 71.8| = 0.8$ (Girls ratio). Ratio $1.2 : 0.8 = 3:2$.

---

## Common Mistakes

* **Mistake:** Calculating the "Average of Averages."
    * **Why it happens:** Taking $(Avg_1 + Avg_2) / 2$ instead of weighting by count.
    * **Fix:** Always multiply by the count first.
* **Mistake:** Forgetting to include all items in the total count.
    * **Why it happens:** Missing a subgroup or miscounting the total.
    * **Fix:** List all counts explicitly before summing.
* **Mistake:** Subtracting the average instead of the total.
    * **Why it happens:** Confusing "Total Cost" with "Average Cost."
    * **Fix:** Always convert averages to totals ($Total = Avg \times Count$) before adding/subtracting.

---

## Worked Example (Step-by-Step)

**Question:** A man bought 5 shirts at ₹450 each, 4 trousers at ₹750 each, and 12 pairs of shoes at ₹750 each. What is the average expenditure per article?

**Solution:**
1. **Calculate Total Sums:** $(5 \times 450) = 2250$; $(4 \times 750) = 3000$; $(12 \times 750) = 9000$.
2. **Sum the Totals:** $2250 + 3000 + 9000 = 14250$.
3. **Sum the Counts:** $5 + 4 + 12 = 21$.
4. **Divide:** $\frac{14250}{21} = 678.57$.

**Answer:** ₹678.57

---

## Similar Patterns

**Mixture and Alligation:** Use this when you are given two groups and need to find the ratio of their quantities to reach a target average.

---

## Revision Summary

* **Key formula:** $\text{Total} = \sum (\text{Avg} \times \text{Count}) / \sum \text{Count}$.
* **Spot it by:** Multiple groups with different counts and averages.
* **First move:** Convert all averages to totals by multiplying by their counts.
* **Fastest method:** Use Alligation for two-group ratio problems.
* **Biggest trap:** Averaging the averages without weighting by count.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Arithmetic Mean** — The sum of values divided by the number of values.
* **Algebraic Substitution** — Solving for $x$ in linear equations (e.g., $6000x = 12000(150) + 3750(x-150)$).

### Formulas You Must Know First
$$
\text{Total} = \text{Average} \times \text{Count}
$$
**What it means:** To find the sum of a group, multiply the average by the number of items.
**Example:** If 5 items have an average of 10, the total is $5 \times 10 = 50$.

### Terms Used In This Pattern
* **Expenditure** — The total amount of money spent.
* **Savings** — Income minus Expenditure.
* **Technician/Non-technician** — Subgroups of a total population.