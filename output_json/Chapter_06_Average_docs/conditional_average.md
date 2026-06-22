# Conditional Average

## Overview
This pattern involves finding an average when the data is constrained by inequalities (e.g., "greater than X but less than Y") or logical conditions. The central idea is to identify the specific set of values that satisfy all given constraints and then calculate their arithmetic mean.

---

## Recognition Clues
* **Keywords:** "at most," "between," "greater than," "less than," "cannot be greater than."
* **Given:** Multiple overlapping ranges or constraints on a single variable.
* **Asked:** The average of the "probable" or "possible" values that satisfy all conditions.
* **Constraint Check:** Look for phrases like "If all of them are correct" or "at the most."

---

## Key Formulas

### [Arithmetic Mean]
$$
\text{Average} = \frac{\text{Sum of observations}}{\text{Number of observations}}
$$

**Variables:**
- $\text{Sum}$ = Total of all valid values identified.
- $\text{Number}$ = Count of those valid values.

**When to use:** To find the final average once the set of valid numbers is determined.

**Worked example:** For weights 66, 67, 68: $\text{Average} = \frac{66+67+68}{3} = \frac{201}{3} = 67$.

---

## Solution Framework

1. **List Constraints:** Write down every inequality provided for the variable (e.g., $W > 65$, $W < 72$).
2. **Find Intersection:** Combine all inequalities to find the narrowest range that satisfies every condition simultaneously.
3. **Identify Values:** List all integers (or specific values) that fall within this final range.
4. **Calculate Mean:** Sum these values and divide by the count of values identified.

---

## Shortcut Tricks

* **Trick:** For a range of consecutive integers, the average is simply the middle value.
* **Why it works:** In an Arithmetic Progression (AP), the mean is equal to the median.
* **When to use:** When the valid values form a sequence with a constant difference (like 66, 67, 68).
* **Example:** For 66, 67, 68, the middle value is 67. No need to sum and divide.

---

## Common Mistakes

* **Mistake:** Ignoring one of the constraints (e.g., forgetting the "mother's condition").
    * **Fix:** Always re-read the question to ensure every condition is applied to the range.
* **Mistake:** Including values outside the intersection of all ranges.
    * **Fix:** Draw a number line if the inequalities are complex to visualize the overlap.
* **Mistake:** Assuming the average of 20 numbers being zero means all numbers are zero.
    * **Fix:** Remember that positive and negative values can cancel each other out to sum to zero.

---

## Worked Example (Step-by-Step)

**Question:** Arun’s weight is $> 65$ but $< 72$. His brother says $> 60$ but $< 70$. His mother says $\leq 68$. If all are correct, what is the average of probable weights?

**Solution:**
1. **List Constraints:** $65 < W < 72$; $60 < W < 70$; $W \leq 68$.
2. **Find Intersection:** 
   - $65 < W < 70$ (from Arun and Brother).
   - $W \leq 68$ (from Mother).
   - Combined: $65 < W \leq 68$.
3. **Identify Values:** The integers satisfying this are $66, 67, 68$.
4. **Calculate Mean:** $\frac{66+67+68}{3} = 67$.

**Answer:** 67 kg.

---

## Similar Patterns

**Weighted Average:** Distinguished by having different groups (e.g., boys and girls) with different averages; use this when you have counts and group averages, not range constraints.

---

## Revision Summary

* **Key formula:** $\text{Average} = \frac{\text{Sum}}{\text{Count}}$.
* **Spot it by:** Overlapping inequalities or "at most" conditions.
* **First move:** Intersect all inequalities to find the valid range.
* **Fastest method:** Use the middle value if the valid numbers are consecutive.
* **Biggest trap:** Forgetting to include all constraints or miscounting the valid set.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Inequalities** — Understanding that $x > a$ and $x < b$ defines a range $(a, b)$.
* **Arithmetic Mean** — The central value of a set of numbers.

### Formulas You Must Know First
$$
\text{Sum} = \text{Average} \times \text{Count}
$$
**What it means:** If you know the average and the number of items, you can find the total sum.
**Example:** If 20 numbers have an average of 0, their sum is $20 \times 0 = 0$.

### Terms Used In This Pattern
* **Probable weights** — The set of values that satisfy the given conditions.
* **Mean** — The arithmetic average.