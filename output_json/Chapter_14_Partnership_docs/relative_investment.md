# Relative Investment

## Overview
These questions involve partners whose investments are defined by relationships (multiples, fractions, or differences) rather than absolute values. The core idea is to express all investments in terms of a single variable ($x$) to derive a fixed ratio, then distribute the total profit based on that ratio.

---

## Recognition Clues
* **Keywords:** "3 times as much as," "two-thirds of," "less than," "contributes one-third," "twice A = thrice B."
* **Given:** A total profit amount and a set of comparative constraints between partners.
* **Asked:** The specific share of one partner (e.g., "What is B's share?").
* **Structure:** Look for a chain of dependencies (A depends on B, B depends on C).

---

## Important Formulas

### [Profit Distribution]
$$
\text{Partner's Share} = \text{Total Profit} \times \left( \frac{\text{Partner's Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* The profit is divided proportionally based on the investment ratio.
*Use when:* You have the final ratio of investments and the total profit amount.

---

## Solution Framework
1. **Assign Variable:** Let the last person in the dependency chain be $x$.
2. **Express Others:** Write every partner's investment as a function of $x$ based on the given constraints.
3. **Form Ratio:** Write the ratio $A : B : C$ and simplify by canceling $x$.
4. **Sum Ratios:** Add the parts of the ratio to get the denominator.
5. **Calculate Share:** Multiply the total profit by the fraction $\frac{\text{Partner's Part}}{\text{Total Parts}}$.

---

## Shortcut Tricks
* **The "Inverse" Trick:** If $aA = bB = cC$, the ratio $A:B:C$ is $\frac{1}{a} : \frac{1}{b} : \frac{1}{c}$.
    * *Why:* This converts the equality into a ratio by finding a common multiple for the coefficients.
* **Total Capital Shortcut:** If given "B contributes as much as A and C together," then $B = \frac{1}{2} \times (\text{Total Capital})$.
    * *Why:* Since $A+B+C = \text{Total}$ and $A+C = B$, then $B+B = \text{Total}$.

---

## Common Mistakes
* **Misinterpreting "Less Than":** Writing $B = x - 600$ but then writing $C = x - 300$ instead of $(x - 600) - 300$.
    * *Reason:* Failing to realize the dependency is sequential.
    * *Fix:* Always read the dependency chain carefully; draw arrows if needed.
* **Ignoring Time:** Assuming all investments are for the same duration.
    * *Reason:* Habitually using only capital ratios.
    * *Fix:* Check if the problem mentions different time periods (e.g., Q46); if so, use $\text{Capital} \times \text{Time}$.
* **Ratio Inversion:** Writing the ratio as $a:b:c$ instead of $\frac{1}{a}:\frac{1}{b}:\frac{1}{c}$ when given $aA=bB=cC$.
    * *Reason:* Confusing coefficients with the actual shares.
    * *Fix:* Always test with a dummy value (e.g., let $aA=bB=cC=12$).

---

## Similar Patterns
* **Absolute Investment:** Where values are given directly (e.g., ₹ 120000).
* **Distinction:** Relative investment requires algebraic setup ($x$); absolute investment allows direct ratio calculation.

---

## Revision Summary
**Key formula:** $\text{Share} = \text{Total Profit} \times \frac{\text{Ratio Part}}{\text{Sum of Ratios}}$.
**Spot it by:** Comparative phrases like "thrice," "two-thirds," or "equal to."
**Fastest method:** Assign $x$ to the last person in the chain and work backward.
**Biggest trap:** Forgetting to subtract sequentially in "less than" problems.