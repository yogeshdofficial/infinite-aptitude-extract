# Complex Distribution

## Overview
This pattern involves distributing a total value (profit or rent) using multiple, non-uniform rules simultaneously. The central idea is to partition the total into distinct "buckets" (e.g., time-based periods or fixed vs. proportional shares) and calculate the distribution for each bucket separately before summing them up.

---

## Recognition Clues
* **Keywords:** "One-half... divided equally," "remainder divided equally," "remained together for X months," "after X months... left."
* **Given:** A total amount and a set of changing conditions (people leaving/joining or different rules for different portions of the profit).
* **Asked:** The final total share of an individual partner.
* **Time-Pressure Tip:** If the question mentions "after X months" or "part equally, part by capital," immediately stop and draw a timeline or a table of segments.

---

## Key Formulas

### [Segmented Distribution]
$$
\text{Total Share} = \sum (\text{Share in Segment}_n)
$$

**Variables:**
- $\text{Share in Segment}_n$ = The amount received by a person during a specific time period or specific distribution rule.

**When to use:** When the distribution rules change over time or the profit is split into different categories (e.g., fixed vs. proportional).

**Worked example:** From Q9, A's share = (Rent for 4 months/3) + (Rent for 5 months/2) + (Rent for 3 months/1) = $1536 + 2880 + 3456 = 7872$.

---

## Solution Framework

**Step 1: Segment the total.** Divide the total amount into the specific portions defined by the problem (e.g., time periods or profit-split categories).
**Step 2: Calculate per-segment shares.** For each segment, apply the specific rule (equal split or ratio split) to find the amount per person.
**Step 3: Aggregate.** Sum the individual shares calculated across all segments to find the total for each person.
**Step 4: Verify.** Ensure the sum of all individual totals equals the original total amount.

---

## Shortcut Tricks

* **Trick:** Use the "Monthly Rent" unit.
* **Why it works:** It converts a variable time problem into a constant rate problem, preventing errors in calculating total rent per period.
* **When to use:** When rent or profit is given for a total duration (e.g., 1 year) and partners leave at different times.
* **Example:** In Q9, total rent 13824/12 months = 1152/month. Then simply multiply 1152 by the number of months each person stayed.

---

## Common Mistakes

* **Mistake:** Calculating the ratio of the *entire* period instead of segmenting.
    * **Why it happens:** Habit from simple partnership problems.
    * **Fix:** Always draw a timeline to see who is present in which segment.
* **Mistake:** Forgetting to add the "equal share" to the "proportional share."
    * **Why it happens:** Treating the two parts as mutually exclusive.
    * **Fix:** Explicitly write "Total = Part A + Part B" before calculating.

---

## Worked Example (Step-by-Step)

**Question (Q7):** Two friends invested ₹ 1500 and ₹ 2500. Profit is ₹ 800. One-half is divided equally, the other half in proportion to capital. Find each share.

**Solution:**
1. **Segment:** Total profit = 800. Segment 1 (Equal) = 400. Segment 2 (Proportional) = 400.
2. **Calculate Segment 1:** 400 / 2 = 200 each.
3. **Calculate Segment 2:** Ratio = 1500:2500 = 3:5. Total parts = 8.
   - Friend 1: $\frac{3}{8} \times 400 = 150$.
   - Friend 2: $\frac{5}{8} \times 400 = 250$.
4. **Aggregate:**
   - Friend 1: $200 + 150 = 350$.
   - Friend 2: $200 + 250 = 450$.

**Answer:** ₹ 350 and ₹ 450.

---

## Similar Patterns

**Simple Partnership:** Distinguished by a single, constant ratio applied to the entire profit; no segments or changing rules.

---

## Revision Summary

* **Key formula:** $\text{Total Share} = \sum (\text{Share in Segment}_n)$.
* **Spot it by:** Phrases like "one-half divided equally" or "after X months."
* **First move:** Break the total into distinct segments (time or rule-based).
* **Fastest method:** Calculate the value per segment first, then sum.
* **Biggest trap:** Forgetting to add the different segments together for each person.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio Simplification** — Reducing $1500:2500$ to $3:5$ by dividing by the HCF.
* **Proportional Division** — Dividing a value $V$ in ratio $a:b$ as $\frac{a}{a+b} \times V$.

### Formulas You Must Know First
$$
\text{Share} = \frac{\text{Individual Ratio}}{\text{Sum of Ratios}} \times \text{Total Amount}
$$
**What it means:** How to distribute a total based on a specific ratio.

### Terms Used In This Pattern
* **Capital** — The amount of money invested by a partner.
* **Proportion** — The relative share of profit based on the ratio of capital invested.