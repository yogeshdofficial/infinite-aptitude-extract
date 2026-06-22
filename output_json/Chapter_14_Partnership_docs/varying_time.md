# Varying Time Partnership

## Overview
This pattern involves partners who join, leave, or change their investment amounts at different times during a business cycle. The central idea is that profit is distributed based on the **effective capital**, which is the product of the investment amount and the time it was held.

---

## Recognition Clues
* **Keywords:** "After X months", "joined", "withdrew", "at the end of the year", "for a period of".
* **Given:** Individual investment amounts and specific time durations for each partner.
* **Asked:** The share of profit for a specific partner or the total profit of the business.
* **Visual cue:** Look for multiple time durations (e.g., "3 months", "6 months") associated with different people.

---

## Key Formulas

### [Effective Capital Ratio]
$$
\text{Ratio} = (C_1 \times T_1) : (C_2 \times T_2) : (C_3 \times T_3)
$$

**Variables:**
- $C_n$ = Capital invested by partner $n$
- $T_n$ = Time duration for which $C_n$ was invested

**When to use:** To find the ratio in which total profit must be divided among partners.

**Worked example:** Alfred (45k for 12m) and Peter (60k for 9m). Ratio = $(45000 \times 12) : (60000 \times 9) = 540000 : 540000 = 1:1$.

---

## Solution Framework

1. **Standardize Time:** Convert all time periods into the same unit (usually months) based on the total duration (e.g., 12 months for a year).
2. **Calculate Effective Capital:** Multiply each partner's investment by the time they kept it in the business.
3. **Simplify Ratio:** Divide the effective capital values by their greatest common divisor to get the simplest ratio.
4. **Calculate Shares:** Divide the total profit by the sum of the ratio parts and multiply by each partner's specific ratio part.

---

## Shortcut Tricks

* **Trick:** Cancel common zeros and common factors in the investment amounts *before* multiplying by time.
* **Why it works:** Ratios are scale-invariant; dividing all terms by a constant does not change the final distribution.
* **When to use:** Whenever investment amounts have large trailing zeros (e.g., 45000, 60000).
* **Example:** Instead of $45000 \times 12$, use $45 \times 12 = 540$.

---

## Common Mistakes

* **Mistake:** Using only the investment amount without multiplying by time.
    * **Why it happens:** Forgetting that money "earning" profit depends on how long it stays in the business.
    * **Fix:** Always write down the time duration for each person before calculating.
* **Mistake:** Miscalculating the time for late joiners.
    * **Why it happens:** Confusing "after 3 months" with "for 3 months".
    * **Fix:** If the total time is 12 months and someone joins after 3, their time is $12 - 3 = 9$ months.

---

## Worked Example (Step-by-Step)

**Question:** Alfred invested ₹ 45000. After 3 months, Peter joined with ₹ 60000. After another 6 months, Ronald joined with ₹ 90000. Total profit at year-end is ₹ 16500. Find each share.

**Solution:**
1. **Standardize Time:** Total time = 12 months. Alfred = 12m. Peter = $12 - 3 = 9$m. Ronald = $12 - (3+6) = 3$m.
2. **Effective Capital:** 
   - Alfred: $45000 \times 12 = 540000$
   - Peter: $60000 \times 9 = 540000$
   - Ronald: $90000 \times 3 = 270000$
3. **Simplify Ratio:** $540000 : 540000 : 270000 \rightarrow 2 : 2 : 1$.
4. **Calculate Shares:** Total parts = $2+2+1 = 5$.
   - Alfred: $\frac{2}{5} \times 16500 = 6600$
   - Peter: $\frac{2}{5} \times 16500 = 6600$
   - Ronald: $\frac{1}{5} \times 16500 = 3300$

**Answer:** Alfred: ₹ 6600, Peter: ₹ 6600, Ronald: ₹ 3300.

---

## Similar Patterns
**Simple Partnership:** All partners invest for the same duration; you can ignore time and divide profit directly by the ratio of investments.

---

## Revision Summary
* **Key formula:** $\text{Profit Ratio} = \text{Capital} \times \text{Time}$.
* **Spot it by:** Different time durations mentioned for different partners.
* **First move:** Calculate the time each person's money was actually in the business.
* **Fastest method:** Simplify investment amounts by removing common zeros first.
* **Biggest trap:** Confusing "joined after X months" with "invested for X months".

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio Simplification** — Reducing a ratio to its smallest integer form by dividing by the HCF.
* **Proportional Division** — Dividing a total amount $T$ into parts $a:b:c$ using $\frac{a}{a+b+c} \times T$.

### Formulas You Must Know First
* **Part Calculation:** $\text{Share} = \frac{\text{Individual Ratio}}{\text{Sum of Ratios}} \times \text{Total Profit}$.

### Terms Used In This Pattern
* **Capital:** The amount of money invested in the business.
* **Effective Capital:** The product of capital and time, representing the "weight" of an investment.