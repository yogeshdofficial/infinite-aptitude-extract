# Capital/Time Calculation (Partnership)

## Overview
* This pattern deals with the distribution of profits among partners based on their financial contributions and the duration of those contributions.
* It covers scenarios ranging from simple investments (same time) to complex ones (varying capitals and varying time periods).
* **Central Idea:** Profit is always proportional to the **Effective Capital** (Capital $\times$ Time).

---

## Recognition Clues
* **Keywords:** "Invested," "Joined after X months," "Withdrew," "Annual profit," "Ratio of shares."
* **Structure:** Multiple entities, different amounts, different time durations.
* **GIVEN:** Individual capitals, time periods, and total profit.
* **FOUND:** Individual profit shares or the ratio of investment.

---

## Important Formulas

### Effective Capital
$$E = C \times T$$
* $E$: Effective Capital, $C$: Capital, $T$: Time.
* Use this to normalize investments before calculating profit ratios.

### Profit Ratio
$$\frac{P_1}{P_2} = \frac{C_1 \times T_1}{C_2 \times T_2}$$
* $P$: Profit, $C$: Capital, $T$: Time.
* Use to find the ratio in which total profit is divided.

### Individual Share
$$\text{Share}_A = \left( \frac{E_A}{\sum E} \right) \times \text{Total Profit}$$
* $\sum E$: Sum of all partners' effective capitals.

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (e.g., months).
2. **Calculate Effective Capital:** Multiply each partner's capital by the time it remained in the business.
3. **Simplify Ratio:** Reduce the effective capitals to their simplest integer ratio.
4. **Distribute Profit:** Divide the total profit according to the ratio obtained in Step 3.

---

## Shortcut Tricks
* **Ratio Simplification:** Cancel common zeros and common factors in capitals *before* multiplying by time.
* **Time-Saving:** If all partners invest for the same time, ignore time and distribute profit directly in the ratio of capitals.
* **Mental Math:** If the ratio is $2:3:5$, the total parts are $10$. Each part is $\frac{\text{Total Profit}}{10}$. Multiply by $2, 3,$ and $5$ respectively.

---

## Common Mistakes
1. **Ignoring Time:** Assuming profit is shared only by capital ratio when time differs.
2. **Wrong Time Units:** Mixing years and months (always convert to months).
3. **"After X months":** Forgetting to subtract the "after" time from the total duration (e.g., if total is 12 months and joined after 3, time = 9).
4. **Calculation Errors:** Failing to simplify the ratio before multiplying by profit.
5. **Total Profit Confusion:** Using the capital amount instead of the profit amount for the final distribution.

---

## Similar Patterns
* **Mixture & Alligation:** Distinguish by looking for "mixing" of substances vs. "investing" of money.
* **Work & Wages:** Similar logic (Work = Efficiency $\times$ Time), but uses efficiency instead of capital.

---

## Revision Summary

### Key Formula
$$\text{Profit Ratio} = (C_1T_1) : (C_2T_2) : (C_3T_3)$$

### Recognition Signal
"Partnership" + "Different time periods" + "Total profit".

### Main Trick
Simplify the ratio of $(C \times T)$ as much as possible before calculating shares.

### Common Trap
Miscalculating the "active" time (e.g., using 3 months instead of $12-3=9$ months).