# Capital Changes

## Overview

These questions involve partners who change their investment amounts (withdrawals or additional deposits) at specific intervals during the business term. The central idea is to calculate the "equivalent capital" for each partner by summing the products of each distinct capital amount and the time duration it was invested.

---

## Recognition Clues

* **Keywords:** "withdrew", "invests more", "additional amount", "increases his share", "after X months/years".
* **Given:** Initial investment ratios or amounts, specific time-based changes in capital, and total profit.
* **Asked:** Individual share of profit or the ratio of profit distribution.
* **Timeframe:** The total duration of the business is always specified (e.g., "at the end of the year" or "at the end of 3 years").

---

## Important Formulas

### [Equivalent Capital Ratio]

$$
\text{Profit Ratio} = (C_1 \times t_1 + C_2 \times t_2 + \dots) : (D_1 \times t_1 + D_2 \times t_2 + \dots)
$$

*Meaning:* $C, D$ are capital amounts; $t$ is the time duration (in months or years) each amount was held.

*Use when:* A partner changes their investment amount one or more times during the total business period.

---

## Solution Framework

1. **Standardize Time:** Convert all time periods to the same unit (e.g., all in months).
2. **Calculate Segments:** For each partner, multiply each capital amount by the number of months it remained in the business.
3. **Sum Products:** Add these products together to get the total "equivalent capital" for each partner.
4. **Simplify Ratio:** Reduce the resulting large numbers to their simplest integer ratio.
5. **Distribute Profit:** Divide the total profit using the simplified ratio parts.

---

## Shortcut Tricks

* **Cancel Common Factors Early:** Divide all initial capital amounts by a common factor (e.g., 1000 or 10000) before multiplying by time to keep numbers manageable.
* **Ratio Scaling:** If investments are given as fractions (e.g., $\frac{1}{3} : \frac{1}{4}$), multiply by the LCM of denominators immediately to work with integers.
* **Validity:** These are valid because the profit ratio is proportional to the total equivalent capital; scaling the inputs does not change the final ratio.

---

## Common Mistakes

* **Time Mismatch:** Using the "time elapsed" instead of "time remaining" for the second investment period.
    * *Reason:* Forgetting that the total time is fixed (e.g., if a change happens at 4 months in a 12-month year, the second period is 8 months, not 4).
    * *Fix:* Always verify: $\sum (\text{time segments}) = \text{Total duration}$.
* **Ignoring Initial Capital:** Treating an "additional investment" as the *new* total capital instead of adding it to the existing amount.
    * *Reason:* Misreading "invests ₹ 5000 more" as "invests ₹ 5000".
    * *Fix:* Explicitly write: $\text{New Capital} = \text{Old Capital} \pm \text{Change}$.
* **Ratio Inversion:** Calculating the ratio of time instead of the ratio of (Capital $\times$ Time).
    * *Reason:* Habit from simple partnership problems.
    * *Fix:* Always write out the product $C \times t$ before forming the ratio.

---

## Similar Patterns

This pattern is distinct from "Simple Partnership" because capital is dynamic. It is most often confused with "Time-based Partnership" (where capital is constant but partners join at different times); the difference is that here, the *amount* changes, not just the *start date*.

---

## Revision Summary

**Key formula:** $\text{Profit Ratio} = \sum (\text{Capital} \times \text{Time})$.

**Spot it by:** Look for "withdrew" or "additional investment" mid-term.

**Fastest method:** Simplify capital values by common factors before multiplying by time.

**Biggest trap:** Using the wrong time duration for the second investment segment.