# Complex Profit Sharing

## Overview
* **What it is:** A scenario where multiple partners invest varying amounts of capital for different durations.
* **The Core Logic:** Profit is not just based on money invested, but on "Effective Capital" (Money $\times$ Time).
* **Goal:** Distribute total profit based on the ratio of the partners' effective capitals.

---

## Recognition Clues
* **Keywords:** "Joined after $x$ months," "Withdrew capital," "At the end of the year."
* **Structure:** Multiple investors, varying time periods, total profit given.
* **GIVEN:** Individual investments ($C$) and individual time periods ($T$).
* **FOUND:** Individual profit shares or total profit.

---

## Important Formulas

### Effective Capital (EC)
$$EC = \text{Capital} \times \text{Time}$$
*Use to normalize investments to a common time unit.*

### Profit Ratio
$$\frac{P_A}{P_B} = \frac{C_A \times T_A}{C_B \times T_B}$$
*Use to find the distribution ratio of profits.*

### Individual Share
$$\text{Share}_A = \left( \frac{EC_A}{\sum EC} \right) \times \text{Total Profit}$$
*Use to calculate the final monetary value for a partner.*

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (e.g., months).
2. **Calculate EC:** Multiply each partner's capital by their respective time duration.
3. **Simplify Ratio:** Reduce the $EC$ values to their simplest integer ratio.
4. **Sum Parts:** Add the ratio components to get the "Total Parts."
5. **Distribute:** Multiply the total profit by the fraction of each partner's ratio.

---

## Shortcut Tricks
* **Zero Cancellation:** Cancel common zeros in capital amounts *before* multiplying by time.
* **Time Simplification:** If all time periods are in months, divide by a common factor (e.g., if times are 12, 9, 3, use 4, 3, 1).
* **Ratio Check:** If the ratio is $2:2:1$, the total parts are $5$. Always check if the sum of parts divides the total profit evenly.
* **Mental Math:** If one partner invests double the capital for double the time, their share is $4\times$ the base unit.

---

## Common Mistakes
1. **Ignoring Time:** Treating it as a simple partnership (only capital).
2. **Wrong Time Units:** Mixing years and months (convert everything to months).
3. **Miscalculating Duration:** "After 3 months" means the partner was in for $(12 - 3) = 9$ months.
4. **Ratio Inversion:** Putting time in the denominator instead of multiplying.
5. **Calculation Errors:** Failing to simplify the ratio before distributing the profit.

---

## Similar Patterns
* **Simple Partnership:** All $T$ are equal. $P_1:P_2 = C_1:C_2$.
* **Work-Wage Problems:** Similar logic; replace "Capital" with "Efficiency" and "Time" with "Days worked."

---

## Revision Summary

### Key Formula
$$P \propto C \times T$$

### Recognition Signal
"Joined after $X$ months" or "Withdrew after $Y$ months."

### Main Trick
Simplify the ratio of $(C \times T)$ as early as possible to avoid large numbers.

### Common Trap
Confusing "After $X$ months" (time spent = $12-X$) with "For $X$ months" (time spent = $X$).