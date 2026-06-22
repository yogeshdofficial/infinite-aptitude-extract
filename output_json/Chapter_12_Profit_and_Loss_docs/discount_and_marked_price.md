# Discount and Marked Price

## Overview
This pattern involves calculating the final selling price after one or more discounts are applied to a marked price (MP). The central idea is that each successive discount is applied to the *remaining* balance, not the original price.

---

## Recognition Clues
* **Keywords:** "Marked price," "List price," "Successive discounts," "Trade discount," "Cash discount."
* **Given:** Usually the MP, a series of discount percentages, or the final SP.
* **Asked:** The single equivalent discount, the missing discount percentage, or the required markup to achieve a specific profit.

---

## Key Formulas

### Successive Discount Formula
$$
\text{Net SP} = \text{MP} \times \left(1 - \frac{d_1}{100}\right) \times \left(1 - \frac{d_2}{100}\right) \times \dots
$$
**Variables:** $d_1, d_2$ = discount percentages.
**When to use:** When multiple discounts are applied to the same item.
**Worked example:** For 10% and 20% discounts on ₹100: $100 \times 0.9 \times 0.8 = ₹72$.

### Profit/Markup Relationship
$$
\text{SP} = \text{CP} \times \left(1 + \frac{\text{Profit}\%}{100}\right) = \text{MP} \times \left(1 - \frac{\text{Discount}\%}{100}\right)
$$
**Variables:** CP = Cost Price, MP = Marked Price.
**When to use:** When the question links cost price, profit, and discount.
**Worked example:** If CP=100, Profit=20%, Discount=20%: $100 \times 1.2 = \text{MP} \times 0.8 \Rightarrow \text{MP} = 150$.

---

## Solution Framework
**Step 1: Assume MP = 100** (or CP = 100 if profit is involved) to simplify percentage calculations.
**Step 2: Apply discounts successively** by multiplying the current value by $(1 - \frac{d}{100})$ for each discount.
**Step 3: Equate to the target value** (either the given SP or the required profit-based SP).
**Step 4: Solve for the unknown variable** using basic algebraic isolation.

---

## Shortcut Tricks
* **Trick:** For two successive discounts $a\%$ and $b\%$, the single equivalent discount is $(a + b - \frac{ab}{100})\%$.
* **Why it works:** It represents the net percentage change of two successive reductions.
* **When to use:** Only when there are exactly two discounts.
* **Example:** 10% and 20% discount: $10 + 20 - \frac{10 \times 20}{100} = 30 - 2 = 28\%$.

---

## Common Mistakes
* **Adding discounts:** Adding 10% + 20% = 30% is wrong; it ignores the base reduction. Always apply successively.
* **Discount on CP:** Discounts are *always* applied to the Marked Price, never the Cost Price.
* **Miscalculating fractions:** Confusing $6\frac{1}{4}\%$ as $0.625$ instead of $0.0625$ (or $\frac{1}{16}$).

---

## Worked Example (Step-by-Step)

**Question:** By how much above the cost should goods be marked so that after a 20% and $6\frac{1}{4}\%$ discount, a 20% profit is made?

**Solution:**
1. **Assume CP = 100.** Since we want 20% profit, **SP = 120**.
2. **Convert discounts:** 20% discount means paying 80% ($\frac{4}{5}$). $6\frac{1}{4}\%$ is $\frac{25}{4}\% = \frac{1}{16}$, so paying $1 - \frac{1}{16} = \frac{15}{16}$.
3. **Set equation:** $\text{MP} \times \frac{4}{5} \times \frac{15}{16} = 120$.
4. **Solve:** $\text{MP} \times \frac{60}{80} = 120 \Rightarrow \text{MP} \times \frac{3}{4} = 120 \Rightarrow \text{MP} = 160$.
5. **Markup:** $160 - 100 = 60$ above CP.

**Answer:** 60% above cost price.

---

## Similar Patterns
**Profit and Loss (Basic):** Distinguish by checking if "Marked Price" or "Discount" is mentioned; if only CP and SP are involved, use standard Profit/Loss formulas.

---

## Revision Summary
* **Key formula:** $\text{Net SP} = \text{MP} \times (1-d_1) \times (1-d_2)$.
* **Spot it by:** Looking for "Marked Price" and "Discount" keywords.
* **First move:** Assume MP = 100.
* **Fastest method:** Use the net percentage change formula for two discounts.
* **Biggest trap:** Adding discount percentages instead of applying them successively.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentages** — Expressing parts of 100.
* **Successive Change** — Applying a percentage change to a result of a previous change.

### Formulas You Must Know First
$$
\text{Profit}\% = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100
$$
**What it means:** Profit relative to the initial investment.

### Terms Used In This Pattern
* **Marked Price (MP)** — The price tag on an item.
* **Discount** — A reduction from the Marked Price.
* **Successive Discount** — A discount applied to the price after a previous discount.