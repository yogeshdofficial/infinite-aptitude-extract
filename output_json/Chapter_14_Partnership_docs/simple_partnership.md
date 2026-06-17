# Simple & Compound Partnership

## Overview
Partnership problems involve distributing total profit (or loss) among partners based on their financial contribution and the duration of their investment.

* **Simple Partnership:** All partners invest for the *same* time. Profit is shared in the ratio of capital.
* **Compound Partnership:** Partners invest for *different* time periods. Profit is shared in the ratio of "Effective Capital" (Capital × Time).

---

## Recognition Clues
* **Keywords:** "Invested," "Joined after X months," "Withdrew," "Annual profit," "Ratio of shares."
* **Given:** Individual capital amounts, time durations (or start/end dates), and total profit.
* **To Find:** Individual profit shares, total investment, or the time a partner stayed in the business.
* **Structure:** Look for "A invested X, B joined after Y months with Z."

---

## Important Formulas

### Effective Capital (EC)
$$EC = \text{Capital} \times \text{Time}$$
*Use this for every partner to normalize investments across different time periods.*

### Profit Ratio
$$\frac{P_A}{P_B} = \frac{C_A \times T_A}{C_B \times T_B}$$
*Where $P$ = Profit, $C$ = Capital, $T$ = Time.*

### Individual Share
$$\text{Partner's Share} = \left( \frac{\text{Partner's Ratio}}{\text{Sum of Ratios}} \right) \times \text{Total Profit}$$

---

## Solution Framework
1. **Standardize Time:** Convert all time periods into the same unit (e.g., months).
2. **Calculate Effective Capital:** Multiply each partner's capital by the time it was invested.
3. **Simplify Ratio:** Reduce the resulting values to the simplest integer ratio.
4. **Sum the Parts:** Add the ratio components to get the "Total Parts."
5. **Distribute:** Multiply the total profit by the fraction of each partner's ratio.

---

## Shortcut Tricks
* **Zero Cancellation:** Cancel common zeros in capital amounts *before* multiplying by time.
* **Ratio Scaling:** If all investments are multiples of a number, divide them first to keep numbers small.
* **Time Symmetry:** If the total time is 12 months and someone joins after 3 months, their time is $(12 - 3) = 9$ months.
* **Fractional Profit:** If you know the total profit and the ratio, use the "Sum of Parts" as your denominator immediately.

---

## Common Mistakes
1. **Ignoring Time:** Treating all investments as equal time (only valid if stated).
2. **Wrong Time Calculation:** Using the "time joined" instead of "time invested" (e.g., using 3 months instead of 9).
3. **Calculation Errors:** Forgetting to simplify the ratio before distributing profit.
4. **Unit Mismatch:** Mixing years and months (always convert to months).
5. **Partial Withdrawals:** Failing to split a partner's investment into two periods if they change their capital mid-year.

---

## Similar Patterns
* **Mixture & Alligation:** Partnership is essentially a weighted average problem.
* **Time & Work:** Partnership is "Profit = Capital × Time," similar to "Work = Efficiency × Time."
* **Ratio & Proportion:** Partnership is a direct application of dividing a quantity in a given ratio.

---

## Revision Summary

### Key Formula
$$\text{Profit Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)$$

### Recognition Signal
"Different capital amounts" + "Different time durations" = Compound Partnership.

### Main Trick
Simplify the ratio of $(C \times T)$ as early as possible to avoid large multiplication.

### Common Trap
Using the time *elapsed* instead of the time *invested* (e.g., "Joined after 4 months" means $T = 12 - 4 = 8$).