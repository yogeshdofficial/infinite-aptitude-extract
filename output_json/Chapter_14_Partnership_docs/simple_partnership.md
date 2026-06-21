# Simple Partnership

## Overview

This pattern involves multiple partners investing capital for the **same duration** of time. The central idea is that the profit distribution ratio is identical to the ratio of the capital invested by each partner.

---

## Recognition Clues

* **Keywords:** "Started a business," "invested," "share of profit," "total profit."
* **Given:** Individual investment amounts and the total profit (or one partner's specific share).
* **Asked:** Individual share of profit, total profit, or the ratio of profit distribution.
* **Timeframe:** Explicitly stated as the same for all (e.g., "annual profit," "at the end of 2 years").

---

## Important Formulas

### Profit Distribution Ratio
$$
\text{Share}_A : \text{Share}_B : \text{Share}_C = \text{Investment}_A : \text{Investment}_B : \text{Investment}_C
$$
*Meaning:* Profit is divided in direct proportion to the capital invested.
*Use when:* All partners invest for the same time period.

### Individual Share Calculation
$$
\text{Partner's Share} = \text{Total Profit} \times \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* The specific share is the total profit multiplied by the partner's fractional part of the total investment.
*Use when:* You need to find the monetary value of a partner's profit.

---

## Solution Framework

1. Write down the investment amounts for all partners.
2. Simplify the investments into the smallest possible integer ratio.
3. Calculate the sum of the ratio parts.
4. Divide the total profit by the sum of parts to find the value of "one part."
5. Multiply the value of "one part" by each partner's ratio to find their individual shares.

---

## Shortcut Tricks

* **Zero Cancellation:** Immediately strike out common zeros from all investment amounts before calculating the ratio.
    * *Why:* Ratios are scale-invariant; dividing all terms by 1000 or 10000 does not change the proportion.
* **Fractional Investment:** If investments are given as fractions of total capital, convert them to a common denominator to find the ratio.
    * *Why:* Comparing numerators of fractions with a common denominator gives the exact ratio of investments.

---

## Common Mistakes

* **Ignoring Time:** Applying the simple ratio when partners join at different times.
    * *Reason:* This pattern only applies when time is constant; otherwise, use "Capital × Time."
    * *Fix:* Always check if the time period is identical for all partners before using the simple ratio.
* **Miscalculating the "Rest":** Incorrectly calculating the remaining share when one partner's investment is defined as "the rest."
    * *Reason:* Forgetting to subtract the sum of known fractions from 1.
    * *Fix:* Always ensure the sum of all fractional parts equals 1.
* **Ratio Inversion:** Assigning the wrong ratio part to the wrong partner.
    * *Reason:* Rushing the mapping of names to their respective investment values.
    * *Fix:* Write the names and their corresponding investments in a vertical list before simplifying.

---

## Similar Patterns

* **Compound Partnership:** Confused with this when time periods differ.
    * *Distinction:* If the question mentions "after X months" or "joined later," you must multiply each investment by the time it was active before finding the ratio.

---

## Revision Summary

**Key formula:** $\text{Profit Ratio} = \text{Investment Ratio}$.

**Spot it by:** Identical time periods for all partners in the business.

**Fastest method:** Simplify investment amounts by removing common zeros first.

**Biggest trap:** Assuming the ratio is simple when partners join at different times.