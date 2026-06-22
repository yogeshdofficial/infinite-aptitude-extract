# Property Transformation

## Overview
This pattern involves sets of numbers where you must find a missing value, a total, or a new average after applying algebraic operations or constraints. The central idea is to always convert "Average" information into "Sum" information immediately: $\text{Sum} = \text{Average} \times \text{Count}$.

---

## Recognition Clues
* **Keywords:** "Arithmetic mean," "average of," "sum of," "consecutive," "reciprocals," "greatest possible."
* **Given:** A set of numbers, their average, or a relationship between variables (e.g., $ab+bc+ca=0$).
* **Asked:** The sum of the set, a missing value, the average of transformed values (e.g., squares), or the maximum/minimum possible value of one element.

---

## Key Formulas

### [Sum of Observations]
$$
\text{Sum} = \text{Average} \times \text{Count}
$$
**Variables:**
- $\text{Average}$ = the mean value provided
- $\text{Count}$ = total number of items in the set

**When to use:** Whenever you need to manipulate the total value of a set.

**Worked example:** If 15 numbers have a mean of 41.4, $\text{Sum} = 41.4 \times 15 = 621$.

### [Algebraic Identity for Squares]
$$
a^2 + b^2 + c^2 = (a+b+c)^2 - 2(ab+bc+ca)
$$
**Variables:**
- $a, b, c$ = the numbers in the set
- $ab+bc+ca$ = the sum of pairwise products

**When to use:** When asked for the mean of squares given the mean of the numbers and a relationship between products.

**Worked example:** If mean of $a, b, c$ is $M$, then $a+b+c = 3M$. Sum of squares $= (3M)^2 - 2(0) = 9M^2$. Mean of squares $= \frac{9M^2}{3} = 3M^2$.

---

## Solution Framework

1. **Convert to Sum:** Immediately multiply the average by the count to get the total sum.
2. **Isolate Unknowns:** If a variable is missing, set up an equation: $\text{Total} = \text{Sum of knowns} + \text{Unknowns}$.
3. **Apply Constraints:** If asked for "greatest/least" values, assign the minimum possible values to all other items to maximize the remaining one.
4. **Simplify Expressions:** Use algebraic identities (like $(a+b+c)^2$) if the numbers are variables.
5. **Final Division:** Divide the final sum by the count to return to the average if required.

---

## Shortcut Tricks

* **Trick:** For "greatest possible" value questions, minimize all other variables.
* **Why it works:** Since $\text{Total} = \text{Sum of others} + \text{Target}$, minimizing the "Sum of others" maximizes the "Target."
* **When to use:** When given an average and a range/constraint for individual items.
* **Example:** Q31: Total = 30,000. To maximize one, set 10 items to 420 and 14 items to 1000. $30,000 - (4200 + 14000) = 11,800$.

---

## Common Mistakes

* **Mistake:** Dividing the mean by the count. **Fix:** Always multiply to get the sum.
* **Mistake:** Forgetting to square the multiplier in $(a+b+c)^2$. **Fix:** Remember $(3M)^2 = 9M^2$, not $3M^2$.
* **Mistake:** Miscounting the number of elements (e.g., including/excluding zero). **Fix:** List the elements explicitly if the set is small.

---

## Worked Example (Step-by-Step)

**Question:** The arithmetic mean of 15 numbers is 41.4. Then the sum of these numbers is?

**Solution:**
1. **Identify:** Mean = 41.4, Count = 15.
2. **Apply Formula:** $\text{Sum} = \text{Mean} \times \text{Count}$.
3. **Calculate:** $41.4 \times 15 = 621$.

**Answer:** 621.

---

## Similar Patterns
**Weighted Average:** Distinguished by having different "weights" or frequencies for different values (e.g., "5 shirts at 450, 4 trousers at 750"). Use $\frac{\sum (value \times weight)}{\sum weights}$.

---

## Revision Summary
* **Key formula:** $\text{Sum} = \text{Average} \times \text{Count}$.
* **Spot it by:** Looking for "average of" or "mean of" a set.
* **First move:** Convert the average to a total sum immediately.
* **Fastest method:** Use algebraic identities for squared terms; minimize others for "greatest" value.
* **Biggest trap:** Forgetting to multiply the mean by the count.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Arithmetic Mean** — The sum of all values divided by the number of values.
* **Reciprocal** — The value $\frac{1}{x}$ for any number $x$.
* **Algebraic Identity** — $(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)$.

### Formulas You Must Know First
$$
\text{Average} = \frac{\text{Sum of terms}}{\text{Number of terms}}
$$
**What it means:** The central value of a set.
**Example:** Average of 2, 4, 6 is $\frac{12}{3} = 4$.

### Terms Used In This Pattern
* **Arithmetic Mean:** Synonymous with "Average."
* **Consecutive:** Numbers following each other in order (e.g., $x, x+2, x+4$).