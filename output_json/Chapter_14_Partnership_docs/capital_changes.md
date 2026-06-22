# Capital Changes

## Overview
This pattern involves partners who change their investment amounts (withdrawals or additions) mid-way through the business term. The central idea is to calculate the **Effective Capital** for each partner by summing the products of each capital amount and the time period it was held.

---

## Recognition Clues
* **Keywords:** "withdrew," "invests more," "increases his share," "at the end of the first year."
* **Given:** Initial investment, specific time intervals, and change amounts.
* **Asked:** Profit share of each partner or the initial investment amount.
* **Timeframe:** Business duration is usually 12, 24, or 36 months.

---

## Key Formulas

### Effective Capital Ratio
$$
\text{Profit Ratio} = \sum (\text{Capital}_i \times \text{Time}_i) : \sum (\text{Capital}_j \times \text{Time}_j) : \dots
$$

**Variables:**
- $\text{Capital}_n$ = Amount invested during a specific phase.
- $\text{Time}_n$ = Duration (in months) that specific amount was held.

**When to use:** Whenever a partner's investment amount changes during the business term.

**Worked example:** A invests ₹20,000 for 5 months, then ₹15,000 for 7 months.
Effective Capital = $(20,000 \times 5) + (15,000 \times 7) = 100,000 + 105,000 = 205,000$.

---

## Solution Framework

1. **Define Time Phases:** Identify the exact months each capital amount was held (e.g., if total is 12 months and change happens at month 5, phases are 5 and 7).
2. **Calculate Effective Capital:** Multiply each capital amount by its respective duration and sum them for each partner.
3. **Form the Ratio:** Simplify the resulting sums into the smallest integer ratio.
4. **Distribute Profit:** Divide the total profit by the sum of ratio parts and multiply by each partner's ratio share.

---

## Shortcut Tricks
* **Trick:** Cancel common zeros and common factors across all partners' effective capital sums *before* calculating the final ratio.
* **Why it works:** Ratios are scale-invariant; dividing all terms by a common factor does not change the proportion.
* **When to use:** When dealing with large investment figures (e.g., thousands).
* **Example:** Instead of $205,000 : 212,000$, use $205 : 212$ immediately.

---

## Common Mistakes
* **Mistake:** Using only the initial capital for the entire duration.
* **Why it happens:** Ignoring the "mid-term" change clause.
* **Fix:** Always split the investment into segments based on the time of change.
* **Mistake:** Miscalculating remaining time (e.g., using 5 instead of 7 for the second phase).
* **Fix:** Ensure the sum of time phases equals the total business duration.

---

## Worked Example (Step-by-Step)

**Question:** A, B and C start a business each investing ₹20,000. After 5 months A withdrew ₹5,000, B withdrew ₹4,000 and C invests ₹6,000 more. At the end of the year, total profit is ₹69,900. Find the share of each.

**Solution:**
1. **Time Phases:** Total 12 months. Change at 5 months. Phases are 5 months and 7 months ($12-5=7$).
2. **Effective Capital:**
   - A: $(20,000 \times 5) + (15,000 \times 7) = 100,000 + 105,000 = 205,000$
   - B: $(20,000 \times 5) + (16,000 \times 7) = 100,000 + 112,000 = 212,000$
   - C: $(20,000 \times 5) + (26,000 \times 7) = 100,000 + 182,000 = 282,000$
3. **Ratio:** $205,000 : 212,000 : 282,000 \Rightarrow 205 : 212 : 282$.
4. **Distribute:** Total parts = $205+212+282 = 699$.
   - A's share: $\frac{205}{699} \times 69,900 = 20,500$.
   - B's share: $\frac{212}{699} \times 69,900 = 21,200$.
   - C's share: $\frac{282}{699} \times 69,900 = 28,200$.

**Answer:** A: ₹20,500; B: ₹21,200; C: ₹28,200.

---

## Similar Patterns
**Simple Partnership:** Distinguishable because capital amounts remain constant throughout the entire duration; no "after X months" clauses exist.

---

## Revision Summary
* **Key formula:** $\text{Profit Ratio} = \sum (\text{Capital} \times \text{Time})$.
* **Spot it by:** Phrases like "withdrew" or "invests more" mid-term.
* **First move:** Split the total time into segments based on when the capital changed.
* **Fastest method:** Simplify capital figures by removing common zeros early.
* **Biggest trap:** Forgetting to multiply the *new* capital amount by the *remaining* time.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio Simplification** — Dividing all terms in a ratio by their Greatest Common Divisor (GCD).
* **Proportional Distribution** — Dividing a total value $T$ into parts $a:b:c$ using $\frac{a}{a+b+c} \times T$.

### Formulas You Must Know First
* **Profit Sharing:** $\text{Share} = \frac{\text{Partner's Ratio}}{\text{Total Ratio}} \times \text{Total Profit}$.

### Terms Used In This Pattern
* **Effective Capital** — The total investment value adjusted for the time it was held.
* **Withdrawal** — A reduction in the capital invested.