# Missing Initial Capital

## Overview
These problems involve partners who change their investment amounts mid-way through a business term. The central idea is to calculate the **total equivalent capital** for each partner by summing the products of (capital $\times$ time) for every distinct period of their investment.

---

## Recognition Clues
* **Keywords:** "invests another," "invests more," "after [X] months," "at the end of [Y] years."
* **Given:** Initial investment ratio, specific amounts added later, time intervals, and final profit ratio.
* **Asked:** The initial investment amount (usually represented as $x$).
* **Visual Scan:** Look for a multi-stage investment timeline for at least two partners.

---

## Important Formulas

### Equivalent Capital
$$
\text{Total Investment} = \sum (\text{Capital}_i \times \text{Time}_i)
$$
*Meaning:* The sum of products of each capital amount held and the duration it remained in the business.
*Use when:* A partner changes their capital contribution at different points in time.

### Profit Distribution Ratio
$$
\frac{P_A}{P_B} = \frac{C_A \times T_A}{C_B \times T_B}
$$
*Meaning:* $P$ is profit, $C$ is total equivalent capital, and $T$ is total time.
*Use when:* Comparing the final profit shares of two partners to solve for an unknown variable $x$.

---

## Solution Framework
1. Assign initial investments as variables (e.g., $3x, 2x, 4x$).
2. Break each partner's timeline into segments based on when they added capital.
3. Calculate the total equivalent capital for each partner by summing (capital $\times$ months).
4. Set the ratio of these sums equal to the given profit ratio.
5. Solve the resulting linear equation for $x$.
6. Multiply $x$ by the initial ratio coefficients to find the specific initial investments.

---

## Shortcut Tricks
* **Ratio Scaling:** If the profit ratio and time periods are simple, simplify the equivalent capital expressions by dividing by common factors before equating.
* **No universal shortcut:** Because these problems involve solving for an unknown $x$ embedded in a sum, the algebraic framework is the most reliable method.

---

## Common Mistakes
* **Time Mismatch:** Using the "added amount" as the total capital instead of adding it to the initial capital.
    * *Reason:* Forgetting that the initial capital continues to earn alongside the new addition.
    * *Fix:* Always use $(Initial + Added)$ for the subsequent time period.
* **Partial Time Calculation:** Calculating the second investment period as the total time instead of (Total Time - Time elapsed).
    * *Reason:* Misreading "after X months" as the duration of the second investment.
    * *Fix:* Explicitly write down the duration for each segment (e.g., "first 4 months" and "remaining 8 months").
* **Ratio Inversion:** Equating the profit ratio to the inverse of the capital ratio.
    * *Reason:* Confusion between profit-sharing and time-sharing.
    * *Fix:* Always write $\frac{\text{Profit A}}{\text{Profit B}} = \frac{\text{Capital A}}{\text{Capital B}}$.

---

## Similar Patterns
This is distinct from "Simple Partnership" (where capital is constant) and "Joining/Leaving" (where capital is zero for part of the time). Distinguish this by the presence of **additional capital injections** rather than just a change in the number of partners.

---

## Revision Summary
**Key formula:** $\text{Total Investment} = \sum (\text{Capital} \times \text{Time})$.
**Spot it by:** Multiple investment stages for the same partner within one business term.
**Fastest method:** Set up the ratio of total equivalent capitals and solve for $x$.
**Biggest trap:** Forgetting to add the new investment to the existing capital for the remaining time.