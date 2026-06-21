# Working Partner

## Overview

These questions involve a business where one partner receives a fixed percentage of the total profit as a "salary" for management before the remaining profit is distributed. The core idea is to split the total profit into two distinct pools: the management fee and the residual profit shared by ratio of investment.

---

## Recognition Clues

* **Keywords:** "Working partner," "managing the business," "gets X% of the profit for managing."
* **Given:** Total profit amount, individual capital investments, time periods (if applicable), and the management percentage.
* **Asked:** Total profit, or the specific share of a partner (including their management fee).

---

## Important Formulas

### [Management Fee Calculation]
$$
\text{Fee} = \text{Total Profit} \times \left( \frac{\text{Percentage}}{100} \right)
$$
*Meaning:* The fixed portion of profit allocated to the working partner before any ratio-based distribution.
*Use when:* You need to isolate the "residual profit" to be shared among all partners.

### [Residual Profit Distribution]
$$
\text{Partner's Share} = \text{Residual Profit} \times \left( \frac{\text{Partner's Investment Ratio}}{\text{Sum of all Ratios}} \right)
$$
*Meaning:* The remaining profit after the management fee is deducted, distributed based on capital contribution.
*Use when:* Calculating the final payout for each partner after the working partner's fee is removed.

---

## Solution Framework

1. Calculate the management fee as a percentage of the total profit.
2. Subtract the management fee from the total profit to find the "Residual Profit."
3. Determine the investment ratio for all partners (Capital $\times$ Time).
4. Divide the Residual Profit among partners according to their investment ratio.
5. Add the management fee back to the working partner's share from Step 4.

---

## Shortcut Tricks

* **Proportional Scaling:** If the total profit is unknown, assume it is $100$ or $x$, solve for the ratio, and equate to the given difference in shares.
* **Validity:** This avoids complex algebraic fractions by working with a variable that cancels out during the final comparison.

---

## Common Mistakes

* **Forgetting the Fee:** Adding the management fee to the total profit instead of subtracting it.
    * *Reason:* Misreading "balance profit" as "total profit."
    * *Fix:* Always calculate the "Residual Profit" first.
* **Double Counting:** Giving the working partner their share of the residual profit *without* adding the management fee back.
    * *Reason:* Treating the working partner like a sleeping partner.
    * *Fix:* Ensure the final share = (Management Fee) + (Share of Residual Profit).
* **Ratio Error:** Applying the investment ratio to the *total* profit instead of the *residual* profit.
    * *Reason:* Habitual application of standard partnership rules.
    * *Fix:* Explicitly write "Residual Profit = Total - Fee" at the top of your scratchpad.

---

## Similar Patterns

This is distinct from standard partnership problems because the profit is not distributed in a single ratio. Always check if a "working partner" clause exists before calculating ratios.

---

## Revision Summary

**Key formula:** $\text{Residual Profit} = \text{Total Profit} - \text{Management Fee}$.

**Spot it by:** Looking for "working partner" or "managing the business" in the problem statement.

**Fastest method:** Calculate the fee first, then distribute the remainder using the investment ratio.

**Biggest trap:** Forgetting to add the management fee back to the working partner's final share.