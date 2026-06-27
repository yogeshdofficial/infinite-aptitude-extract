# Division Problems

## Overview
These problems involve finding a number that satisfies specific divisibility conditions (e.g., "smallest number to add/subtract" or "nearest multiple"). The central idea is to use the division algorithm to find the remainder and then adjust the dividend to reach the next or previous exact multiple.

---

## Recognition Clues
* **Keywords:** "Smallest number to be added," "least number to be subtracted," "exactly divisible," "nearest to," "smallest/greatest number of N digits."
* **Given:** A dividend (or a range like "5-digit number") and a divisor.
* **Asked:** The adjustment required to make the dividend perfectly divisible or the resulting number itself.

---

## Key Formulas

### The Division Algorithm
$$
\text{Dividend} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}
$$

**Variables:**
- Dividend: The number being divided.
- Divisor: The number dividing the dividend.
- Quotient: The result of the division.
- Remainder: The amount left over.

**When to use:** To find the remainder when the division is not exact.

**Worked example:** $1000 \div 45 = 22$ remainder $10$. Here, $1000 = (45 \times 22) + 10$.

### Adjustment Formulas
- **To Add:** $\text{Adjustment} = \text{Divisor} - \text{Remainder}$
- **To Subtract:** $\text{Adjustment} = \text{Remainder}$

**When to use:** When asked for the smallest number to add or subtract to make a number divisible.

**Worked example:** For $1000 \div 45$, remainder is $10$. To add: $45 - 10 = 35$. To subtract: $10$.

---

## Solution Framework
1. **Divide:** Perform long division of the given number by the divisor to find the remainder.
2. **Identify Goal:** Determine if the question asks for addition (next multiple) or subtraction (previous multiple).
3. **Calculate Adjustment:** 
   - If adding: Use $(\text{Divisor} - \text{Remainder})$.
   - If subtracting: Use the $\text{Remainder}$ itself.
4. **Finalize:** Add or subtract the adjustment from the original number to get the final answer.

---

## Shortcut Tricks
* **Trick:** For "nearest number," calculate both the next multiple ($+ (\text{Divisor} - \text{Remainder})$) and the previous multiple ($- \text{Remainder}$), then pick the one with the smaller distance.
* **Why it works:** The nearest multiple is either the one just above or just below the current number.
* **When to use:** When the question asks for the "nearest" number rather than just "smallest to add."

---

## Common Mistakes
* **Mistake:** Adding the remainder instead of the difference when asked to add.
* **Why it happens:** Confusing the "remainder" with the "distance to the next multiple."
* **Fix:** Always subtract the remainder from the divisor first to find the "gap."
* **Mistake:** Forgetting to check the sum of digits rule for divisibility by 9.
* **Why it happens:** Overlooking properties of numbers in multiplication-based problems.

---

## Worked Example (Step-by-Step)

**Question:** Find the smallest number to be added to 1000 so that 45 divides the sum exactly.

**Solution:**
1. **Divide:** $1000 \div 45 = 22$ with a remainder of $10$.
2. **Identify Goal:** We need to add a number to reach the *next* multiple.
3. **Calculate Adjustment:** The gap to the next multiple is $\text{Divisor} - \text{Remainder} = 45 - 10 = 35$.
4. **Finalize:** $1000 + 35 = 1035$.

**Answer:** 35

---

## Similar Patterns
* **HCF/LCM Problems:** These involve finding a number that divides *multiple* numbers, whereas these division problems focus on a single dividend and divisor relationship.

---

## Revision Summary
* **Key formula:** $\text{Dividend} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}$.
* **Spot it by:** Looking for "exactly divisible" and "add/subtract" keywords.
* **First move:** Divide the number to find the remainder.
* **Fastest method:** Use $(\text{Divisor} - \text{Remainder})$ for addition; use $\text{Remainder}$ for subtraction.
* **Biggest trap:** Adding the remainder instead of the difference.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Long Division** — The process of finding the quotient and remainder.
* **Divisibility Rule for 9** — A number is divisible by 9 if the sum of its digits is divisible by 9.

### Terms Used In This Pattern
* **Dividend** — The number being divided.
* **Divisor** — The number by which the dividend is divided.
* **Remainder** — The amount remaining after division.