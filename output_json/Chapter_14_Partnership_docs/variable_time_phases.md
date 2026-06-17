# Variable Time Phases

## Overview
* **What it is:** A partnership scenario where partners invest different amounts of capital for different durations.
* **The Core Logic:** Profit is not just proportional to money invested, but to the **"Effective Capital"** (Money $\times$ Time).
* **Goal:** Distribute total profit based on the ratio of these effective capitals.

---

## Recognition Clues
* **Keywords:** "Joined after $x$ months," "Withdrew after $y$ months," "At the end of the year."
* **Structure:** Multiple partners, varying entry/exit times, total annual profit given.
* **Given:** Individual investments ($C$) and individual time periods ($T$).
* **To Find:** Individual profit shares or total profit.

---

## Important Formulas

### Effective Capital (EC)
$$EC = C \times T$$
* **Meaning:** The weight of an investment over time.
* **Use:** Calculate this for every partner before finding the ratio.

### Profit Ratio
$$\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}$$
* **Meaning:** Profit is directly proportional to the product of capital and time.
* **Use:** To split the total profit ($P_{total}$) into parts.

### Individual Share
$$Share_A = \left( \frac{EC_A}{\sum EC} \right) \times P_{total}$$
* **Meaning:** The fraction of the total profit belonging to partner A.

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (usually months).
2. **Calculate EC:** Multiply each partner's capital by their respective time duration.
3. **Simplify Ratio:** Reduce the $EC$ values to their simplest integer ratio ($EC_1 : EC_2 : EC_3 \dots$).
4. **Sum Parts:** Add the ratio terms to get the "Total Parts."
5. **Distribute:** Divide the total profit by "Total Parts" and multiply by each partner's ratio share.

---

## Shortcut Tricks
* **Zero Cancellation:** Before multiplying, cancel common zeros in all capital amounts (e.g., $120,000 : 135,000 \rightarrow 120 : 135$).
* **Ratio Simplification:** Divide the $EC$ values by the greatest common divisor (GCD) immediately to keep numbers small.
* **The "12-Month" Rule:** If the business runs for a year, use $T$ as the number of months the money was actually in the business (e.g., "Joined after 3 months" means $T = 12 - 3 = 9$).

---

## Common Mistakes
* **Time Confusion:** Using the "time joined" instead of "time invested" (e.g., using 3 instead of 9).
* **Ignoring Units:** Mixing years and months. Always convert to months.
* **Ratio Inversion:** Calculating $T/C$ instead of $C \times T$.
* **Arithmetic Errors:** Multiplying large numbers instead of simplifying ratios first.
* **Partial Sums:** Forgetting to include all partners in the "Total Parts" sum.

---

## Similar Patterns
* **Simple Partnership:** All $T$ are equal. $P_1 : P_2 = C_1 : C_2$. (Distinguish by checking if time is constant).
* **Working Partner Salary:** A portion of profit is set aside as salary before distributing the remainder. (Distinguish by looking for "Managerial/Working allowance" clauses).

---

## Revision Summary

### Key Formula
$$Ratio = (C_1T_1) : (C_2T_2) : (C_3T_3)$$

### Recognition Signal
"Joined/Left after $X$ months" + "Total Profit".

### Main Trick
Cancel zeros in capitals *before* multiplying by time.

### Common Trap
Using the "time elapsed" instead of "time invested" (e.g., using 3 months instead of 9 months).