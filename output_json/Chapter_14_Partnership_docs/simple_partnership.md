# Simple Partnership

## Overview
This pattern covers business scenarios where partners invest capital for the **same duration** (usually one year). The central idea is that profit is distributed in the exact same ratio as the capital invested.

---

## Recognition Clues
* **Keywords:** "Started a business," "invested," "annual profit," "at the end of the year."
* **Given:** Individual investment amounts and total profit.
* **Time:** The time period is either identical for all (e.g., "at the end of the year") or not mentioned at all.
* **Asked:** The specific share of one or more partners.

---

## Key Formulas

### [Profit Distribution Formula]
$$
\text{Share of Partner}_i = \frac{\text{Investment}_i}{\text{Total Investment}} \times \text{Total Profit}
$$

**Variables:**
- $\text{Investment}_i$ = Capital invested by the specific partner.
- $\text{Total Investment}$ = Sum of all partners' capitals.
- $\text{Total Profit}$ = The total amount to be divided.

**When to use:** When you need to find the monetary value of a partner's profit share.

**Worked example:** A invests ₹ 120,000, B invests ₹ 135,000. Total profit is ₹ 56,700.
Ratio = $120:135 = 8:9$. Total parts = $8+9=17$.
A's share = $\frac{8}{17} \times 56700 = 26682$ (Note: Use the simplified ratio $8:9$ to calculate).

---

## Solution Framework

1. **Extract Capitals:** Write down the investment amount for each partner.
2. **Simplify Ratio:** Divide all investment amounts by their Greatest Common Divisor (GCD) to get the simplest integer ratio.
3. **Sum the Parts:** Add the terms of the simplified ratio together.
4. **Calculate Share:** Multiply the total profit by the fraction $\frac{\text{Partner's Ratio Part}}{\text{Total Parts}}$.

---

## Shortcut Tricks

* **Trick:** Use the simplified ratio directly.
* **Why it works:** The ratio of profits is identical to the ratio of investments; large numbers only increase the risk of calculation errors.
* **When to use:** Always, before performing any multiplication.
* **Example:** Instead of calculating $\frac{120000}{405000} \times 56700$, use $\frac{8}{27} \times 56700$.

---

## Common Mistakes

* **Mistake:** Forgetting to simplify the ratio. **Fix:** Always divide by the common factor (e.g., 1000 or 5000) first.
* **Mistake:** Using the wrong denominator. **Fix:** Ensure the denominator is the sum of the *simplified* ratio parts, not the sum of the original investments.
* **Mistake:** Assuming equal shares. **Fix:** Always calculate based on the ratio of capital, even if the question doesn't explicitly state "proportional."

---

## Worked Example (Step-by-Step)

**Question:** A, B and C started a business by investing ₹ 120,000, ₹ 135,000 and ₹ 150,000 respectively. Find the share of each, out of an annual profit of ₹ 56,700.

**Solution:**
1. **Extract:** A=120,000, B=135,000, C=150,000.
2. **Simplify:** Divide by 15,000 $\rightarrow$ $8 : 9 : 10$.
3. **Sum:** $8 + 9 + 10 = 27$.
4. **Calculate:** 
   - A: $\frac{8}{27} \times 56700 = 8 \times 2100 = 16,800$.
   - B: $\frac{9}{27} \times 56700 = 9 \times 2100 = 18,900$.
   - C: $\frac{10}{27} \times 56700 = 10 \times 2100 = 21,000$.

**Answer:** A: ₹ 16,800; B: ₹ 18,900; C: ₹ 21,000.

---

## Similar Patterns

**Compound Partnership:** Distinguished by partners joining/leaving at different times or changing capital mid-term; look for "after X months" or "withdrew/invested more."

---

## Revision Summary

* **Key formula:** $\text{Share} = (\text{Ratio Part} / \text{Total Parts}) \times \text{Total Profit}$.
* **Spot it by:** Same time duration for all partners.
* **First move:** Simplify the investment ratio to the smallest integers.
* **Fastest method:** Work with the simplified ratio parts, not the raw capital amounts.
* **Biggest trap:** Using raw capital amounts instead of the simplified ratio.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio Simplification** — Reducing a ratio $a:b:c$ by dividing all terms by their GCD.
* **Fractional Parts** — Understanding that a share is a portion of the whole: $\frac{\text{Part}}{\text{Whole}}$.

### Formulas You Must Know First
* **Sum of Ratio Parts:** $S = a + b + c$.
* **Individual Share:** $\text{Value} = \frac{\text{Part}}{S} \times \text{Total}$.

### Terms Used In This Pattern
* **Capital:** The money invested by a partner.
* **Partnership:** A business arrangement where profits are shared based on investment.