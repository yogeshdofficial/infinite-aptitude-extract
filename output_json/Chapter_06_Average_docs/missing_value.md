# Missing Value

## Overview
This pattern involves finding one or more unknown values within a set when the average of that set is provided. The central idea is to convert the average into a total sum, allowing you to isolate the unknown variable using basic algebra.

---

## Recognition Clues
* **Keywords:** "average of... is [number]", "x is unknown", "find the [missing] number".
* **Given:** A set of numbers (some known, some variables) and their average.
* **Asked:** The value of the unknown variable or a specific term in a sequence.
* **Variations:** Single missing number, consecutive numbers, or overlapping groups (e.g., "first 7" and "last 7").

---

## Key Formulas

### [Sum of Observations]
$$
\text{Sum} = \text{Average} \times \text{Count}
$$

**Variables:**
- $\text{Sum}$ = Total of all values in the set
- $\text{Average}$ = The given mean value
- $\text{Count}$ = Total number of items in the set

**When to use:** Every time you are given an average and need to find a missing value.

**Worked example:** For Q3, Average = 60, Count = 6. $\text{Sum} = 60 \times 6 = 360$.

---

## Solution Framework

1. **Step 1: Calculate Total Sum** — Multiply the given average by the total count of numbers to get the target sum.
2. **Step 2: Sum Knowns** — Add all the provided numerical values together.
3. **Step 3: Set up Equation** — Write the equation: $(\text{Sum of knowns}) + (\text{Unknowns}) = \text{Target Sum}$.
4. **Step 4: Solve for Variable** — Subtract the sum of knowns from the target sum to isolate the missing value.

---

## Shortcut Tricks

* **Trick:** Use the "Deviation Method" for large sets.
* **Why it works:** Instead of summing large numbers, calculate how much each number deviates from the average. The sum of deviations must be zero.
* **When to use:** When numbers are close to the average, making mental subtraction easier than adding large totals.
* **Example:** In Q3 (Avg 60): 30 (-30), 72 (+12), 53 (-7), 68 (+8), 87 (+27). Sum of deviations = $-30+12-7+8+27 = +10$. To balance to 0, $x$ must be $60 - 10 = 50$.

---

## Common Mistakes

* **Mistake:** Forgetting to multiply the average by the count.
    * **Why it happens:** Rushing to add the numbers without converting the average to a total.
    * **Fix:** Always write $\text{Sum} = \text{Avg} \times \text{Count}$ at the top of your scratchpad.
* **Mistake:** Double-counting the overlap in overlapping groups (e.g., Q15).
    * **Why it happens:** Assuming the sum of two groups equals the total sum, ignoring that the middle term is counted twice.
    * **Fix:** Subtract the total sum from the sum of the two groups to find the overlap.

---

## Worked Example (Step-by-Step)

**Question:** The average of marks of 13 papers is 40. The average of marks of the first 7 papers is 42 and that of the last 7 papers is 35. What are the marks of the seventh paper?

**Solution:**
1. **Total Sum:** $13 \times 40 = 520$.
2. **Sum of first 7:** $7 \times 42 = 294$.
3. **Sum of last 7:** $7 \times 35 = 245$.
4. **Identify Overlap:** The 7th paper is in both groups. Sum of 14 papers = $294 + 245 = 539$.
5. **Isolate 7th paper:** $539 - 520 = 19$.

**Answer:** 19

---

## Similar Patterns
* **Weighted Average:** Distinguish by checking if the groups have different counts or weights; if they do, use the weighted average formula instead of simple sum subtraction.

---

## Revision Summary
* **Key formula:** $\text{Sum} = \text{Average} \times \text{Count}$.
* **Spot it by:** Average given, one or more values missing.
* **First move:** Calculate the total sum immediately.
* **Fastest method:** Use deviations from the average to avoid large additions.
* **Biggest trap:** Forgetting to account for overlapping terms in group problems.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Algebraic Equation** — Balancing both sides of an equation to solve for $x$.
* **Consecutive Numbers** — Numbers following each other, e.g., $x, x+1, x+2$.

### Formulas You Must Know First
$$
\text{Average} = \frac{\text{Sum of observations}}{\text{Number of observations}}
$$
**What it means:** The central value of a data set.
**Example:** Avg of 10 and 20 is $(10+20)/2 = 15$.

### Terms Used In This Pattern
* **Observations** — The individual numerical values in a set.
* **Variable ($x$)** — The unknown value we are solving for.