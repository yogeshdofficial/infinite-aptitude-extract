# Different Time Periods (Compound Partnership)

## Overview
* This pattern deals with partnerships where partners invest different amounts of capital for **varying durations**.
* It applies to business scenarios where partners join or leave at different points in time.
* The central idea is the **"Effective Capital"** concept: Profit is distributed based on the product of capital and the time it remained invested.

---

## Recognition Clues
* **Keywords:** "Joined after X months," "Left after Y months," "At the end of the year."
* **Structure:** Multiple partners, different investment amounts, different time durations.
* **Given:** Individual investments and the specific time each person stayed in the business.
* **To Find:** Individual profit shares based on total profit.

---

## Important Formulas

### Effective Capital (Investment Unit)
$$E = C \times T$$
* **Meaning:** The weight of an investment.
* **Use:** Calculate this for every partner before finding the ratio.

### Profit Ratio
$$\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}$$
* **Meaning:** Profit is directly proportional to the product of Capital ($C$) and Time ($T$).
* **Use:** To distribute total profit among $n$ partners.

### Individual Share
$$\text{Share}_A = \left( \frac{E_A}{\sum E} \right) \times \text{Total Profit}$$
* **Meaning:** Partner's portion of the total gain.

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (usually months).
2. **Calculate Effective Capital:** Multiply each partner's investment by their respective time duration ($C \times T$).
3. **Simplify Ratio:** Reduce the resulting values to their simplest integer ratio.
4. **Distribute Profit:** Divide the total profit according to the simplified ratio.

---

## Shortcut Tricks
* **Zero Cancellation:** Cancel common zeros in investments *before* multiplying by time.
* **Time Simplification:** If all time periods are in months, divide by a common factor (e.g., if times are 12, 9, 6, use 4, 3, 2).
* **Ratio Scaling:** If the ratio is $2:3:5$, the total parts are $2+3+5=10$. Simply multiply the total profit by $0.2, 0.3,$ and $0.5$ respectively.

---

## Common Mistakes
1. **Ignoring Time:** Treating it as a simple partnership (only using capital).
2. **Wrong Time Units:** Mixing years and months (always convert to months).
3. **Miscalculating "After":** If someone joins "after 3 months," their time is $(12 - 3) = 9$ months, not 3.
4. **Calculation Errors:** Multiplying large numbers instead of simplifying ratios first.
5. **Total Profit Confusion:** Applying the ratio to the *capital* instead of the *profit*.

---

## Similar Patterns
* **Simple Partnership:** All $T$ are equal. $P_1:P_2 = C_1:C_2$.
* **Working Partner Salary:** Deduct fixed salary from total profit *before* distributing the remainder by the investment ratio.

---

## Revision Summary

### Key Formula
$$\text{Profit Ratio} = (C_1T_1) : (C_2T_2) : (C_3T_3)$$

### Recognition Signal
"Joined/Left after X months" or "Different time periods."

### Main Trick
Simplify the ratio of $(C \times T)$ by dividing by common factors before calculating shares.

### Common Trap
Using the "joined after" time as the "active" time (Always use $12 - \text{joined\_time}$).