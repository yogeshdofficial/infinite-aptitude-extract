# Mixed Distribution

## Overview

These problems involve splitting total profit into two or more distinct "pots" (e.g., charity, fixed salary, interest, or equal shares) before distributing the remainder based on capital ratios. The central idea is to calculate the value of each "pot" separately and then aggregate the shares for each partner.

---

## Recognition Clues

* **Keywords:** "One-half... divided equally," "60%... distributed equally," "5%... goes to charity," "remaining... in proportion to capitals."
* **Given:** Total profit, investment amounts (or ratios), and specific rules for splitting the profit pool.
* **Asked:** Total profit or the specific share of an individual partner.

---

## Important Formulas

### [Proportional Share]
$$
\text{Partner's Share} = \text{Total Pool} \times \left( \frac{\text{Partner's Capital}}{\text{Total Capital}} \right)
$$
*Meaning:* Distributes a specific portion of profit based on the investment ratio.
*Use when:* Calculating the portion of profit allocated to capital-based distribution.

### [Total Profit Reconstruction]
$$
\text{Total Profit} = \frac{\text{Known Share}}{\text{Fractional Share of Total}}
$$
*Meaning:* Back-calculates the whole from a known part after accounting for deductions like charity.
*Use when:* A specific partner's share is given, and you need the total profit.

---

## Solution Framework

1. Identify the "fixed" or "equal" portion of the profit and divide it by the number of partners.
2. Calculate the "remaining" portion of the profit after subtracting fixed deductions (charity/salary).
3. Determine the capital ratio of the partners.
4. Distribute the "remaining" portion using the capital ratio.
5. Add the fixed share and the proportional share for each partner to find their total.

---

## Shortcut Tricks

* **The 100-Unit Assumption:** Assume total profit is 100 units, subtract charity/fixed costs, then distribute the remainder by ratio to find the value of 1 unit.
* **Why it works:** It avoids messy fractions and allows you to work with integers until the final step.
* **Difference Shortcut:** If given the difference between two partners' shares, equate the difference in their ratio-based shares to the given value to solve for the total profit variable $x$.

---

## Common Mistakes

* **Forgetting the "Equal" Part:** Applying the capital ratio to the *entire* profit instead of just the "remaining" portion.
    * *Reason:* Misreading the instruction that only a part of the profit is capital-dependent.
    * *Fix:* Always underline the specific distribution rule for each segment of the profit.
* **Charity Deduction Error:** Calculating charity on the *remaining* profit instead of the *total* profit.
    * *Reason:* Assuming deductions happen sequentially rather than from the gross amount.
    * *Fix:* Always calculate charity/fixed deductions from the total profit first.

---

## Similar Patterns

* **Simple Partnership:** Only involves one distribution rule (capital ratio).
* **Compound Partnership:** Involves time-weighted capital.
* **Distinction:** If the problem mentions "equally," "charity," or "interest," it is a **Mixed Distribution** problem; if it only mentions "invested for X months," it is a **Compound Partnership** problem.

---

## Revision Summary

**Key formula:** $\text{Total} = \text{Fixed Share} + (\text{Remaining} \times \text{Ratio Share})$.

**Spot it by:** Phrases like "partly equal" or "partly proportional" or "charity deduction."

**Fastest method:** Assume total profit is 100 and solve for the value of 1 unit.

**Biggest trap:** Applying the capital ratio to the entire profit instead of the remainder.