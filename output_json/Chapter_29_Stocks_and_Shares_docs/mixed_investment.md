# Mixed Investment

## Overview
This pattern involves splitting a total sum of money into two or more parts, each invested in different stocks with varying dividend rates and market prices. The goal is to find the individual investment amounts by equating their incomes or by adjusting for a change in total income.

---

## Recognition Clues
* **Keywords:** "partly in... and partly in...", "total sum", "income from both is equal", "increases his income by".
* **Given:** Total investment amount, dividend rates, market prices of stocks, and either the relationship between incomes (equal) or the change in total income.
* **Asked:** The specific amount invested in each individual stock.

---

## Key Formulas

### [Income from Investment]
$$
\text{Income} = \text{Investment} \times \frac{\text{Dividend Rate}}{\text{Market Price}}
$$

**Variables:**
- $\text{Investment}$ = The amount of money put into a specific stock.
- $\text{Dividend Rate}$ = The percentage return on the face value.
- $\text{Market Price}$ = The price at which the stock is currently traded.

**When to use:** To calculate the annual return from a specific portion of your investment.

**Worked example:** Investing ₹ 485 in 4% stock at ₹ 97:
$\text{Income} = 485 \times \frac{4}{97} = 5 \times 4 = ₹ 20$.

---

## Solution Framework

1. **Assign Variables:** Let the investment in the first stock be $x$ and the second be $(\text{Total} - x)$.
2. **Express Incomes:** Write the income for each part using the formula: $\text{Income} = \text{Investment} \times \frac{\text{Rate}}{\text{Price}}$.
3. **Set Equation:** Equate the sum of incomes to the target total income (or equate them to each other if the problem states they are equal).
4. **Solve for $x$:** Use algebraic simplification to isolate $x$.
5. **Find Second Part:** Subtract $x$ from the total to find the second investment amount.

---

## Shortcut Tricks
**No shortcut faster than the standard framework — apply the steps above directly.** The algebraic setup is the most reliable way to handle the varying denominators (market prices) and rates.

---

## Common Mistakes
* **Face Value Trap:** Calculating income as a percentage of the *Market Price* instead of the *Face Value*. Always use the dividend rate on the face value, then adjust for the market price.
* **Income Confusion:** Forgetting to add or subtract the "increase/decrease" in income when comparing two different investment scenarios.
* **Denominator Error:** Using the wrong market price for the wrong stock; always map the dividend rate to its specific market price.

---

## Worked Example (Step-by-Step)

**Question:** Ravi invested ₹ 913 partly in 4% stock at ₹ 97 and partly in 5% stock at ₹ 107. If his income from both is equal, find the amount invested in each stock.

**Solution:**
1. **Assign Variables:** Let investment in 4% stock be $x$. Then investment in 5% stock is $(913 - x)$.
2. **Express Incomes:** 
   - Income from 4% stock = $x \times \frac{4}{97}$
   - Income from 5% stock = $(913 - x) \times \frac{5}{107}$
3. **Set Equation:** $\frac{4x}{97} = \frac{5(913 - x)}{107}$
4. **Solve for $x$:** 
   - $4x \times 107 = 5(913 - x) \times 97$
   - $428x = 442805 - 485x$
   - $913x = 442805 \Rightarrow x = 485$.
5. **Find Second Part:** $913 - 485 = 428$.

**Answer:** ₹ 485 in 4% stock and ₹ 428 in 5% stock.

---

## Similar Patterns
* **Simple Interest/Mixture Problems:** These are distinct because they use simple interest rates on the principal, whereas this pattern uses dividend rates on market prices.

---

## Revision Summary
* **Key formula:** $\text{Income} = \text{Investment} \times \frac{\text{Rate}}{\text{Market Price}}$.
* **Spot it by:** "Partly in X and partly in Y" with different rates/prices.
* **First move:** Assign $x$ and $(\text{Total} - x)$ to the two investments.
* **Fastest method:** Direct algebraic equation of the two income expressions.
* **Biggest trap:** Calculating dividend as a percentage of market price instead of face value.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Algebraic Equations** — Solving for a single variable $x$ in a linear equation.
* **Fractions** — Adding and equating fractions with different denominators.

### Formulas You Must Know First
$$
\text{Income} = \text{Face Value} \times \text{Dividend Rate}
$$
**What it means:** The actual cash earned from a stock is based on its printed face value, not what you paid for it.
**Example:** A ₹ 100 stock at 12% pays ₹ 12 annually.

### Terms Used In This Pattern
* **Face Value (N.V.)** — The value printed on the share certificate.
* **Market Value (M.V.)** — The actual price you pay to buy the share in the market.
* **Dividend** — The annual profit payout per share.