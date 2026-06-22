# Multi-Stage Transactions

## Overview
This pattern involves an item passing through multiple hands (e.g., manufacturer to wholesaler to retailer), where each person adds a profit or incurs a loss. The central idea is to treat each transaction as a successive percentage change applied to the previous price.

---

## Recognition Clues
* **Keywords:** "passing through three hands," "sold to B," "sold to C," "manufacturer to wholesaler to retailer."
* **Given:** A sequence of profit/loss percentages and either the initial cost or the final selling price.
* **Asked:** Either the initial cost of production or the final price paid by the last person in the chain.

---

## Key Formulas

### Successive Transaction Formula
$$
\text{Final Price} = \text{Initial Price} \times \left(1 \pm \frac{r_1}{100}\right) \times \left(1 \pm \frac{r_2}{100}\right) \times \dots
$$

**Variables:**
- $r_n$ = profit percentage (use $+$) or loss percentage (use $-$) at stage $n$.

**When to use:** When an item changes hands multiple times and you need to find the final price or the starting cost.

**Worked example:** Manufacturer gains 10%, wholesaler 15%, retailer 25%. Final price = $x \times 1.10 \times 1.15 \times 1.25$.

---

## Solution Framework

**Step 1: Assign a variable** — Let the unknown initial cost be $x$ (or $P$).
**Step 2: Convert percentages to multipliers** — Write each gain $r\%$ as $(1 + \frac{r}{100})$ and each loss $r\%$ as $(1 - \frac{r}{100})$.
**Step 3: Chain the equation** — Multiply the initial cost by all successive multipliers to equal the final known price.
**Step 4: Solve for the variable** — Isolate $x$ by dividing the final price by the product of the multipliers.

---

## Shortcut Tricks

**Trick:** Use the "Multiplier Chain" method instead of calculating each step individually.
**Why it works:** It avoids rounding errors and keeps the equation in one line, allowing for easy cancellation of terms.
**When to use:** When you have more than two transactions.
**Example:** For Q21, instead of calculating intermediate prices, write $x \times \frac{110}{100} \times \frac{115}{100} \times \frac{125}{100} = 1265$.

---

## Common Mistakes

* **Mistake:** Adding percentages (e.g., $10\% + 15\% + 25\% = 50\%$).
* **Why it happens:** Confusing simple addition with successive compounding.
* **Fix:** Always multiply the growth factors $(1 + \frac{r}{100})$.
* **Mistake:** Applying all percentages to the original cost price.
* **Why it happens:** Forgetting that each person calculates profit on the price *they* paid.
* **Fix:** Apply each percentage to the result of the previous transaction.

---

## Worked Example (Step-by-Step)

**Question:** A sells an article which costs him ₹ 400 to B at a profit of 20%. B then sells it to C, making a profit of 10% on the price he paid to A. How much does C pay B?

**Solution:**
1. **Assign:** Initial cost = ₹ 400.
2. **Multipliers:** A's profit 20% $\rightarrow 1.20$; B's profit 10% $\rightarrow 1.10$.
3. **Chain:** Final Price = $400 \times 1.20 \times 1.10$.
4. **Solve:** $400 \times 1.2 = 480$; $480 \times 1.1 = 528$.

**Answer:** C pays ₹ 528.

---

## Similar Patterns

**Single-Stage Profit/Loss:** Distinguish by checking if the item changes hands; if there is only one C.P. and one S.P., use basic profit/loss formulas instead of the chain.

---

## Revision Summary

* **Key formula:** $\text{Final} = \text{Initial} \times (1 \pm \frac{r_1}{100}) \times (1 \pm \frac{r_2}{100}) \dots$
* **Spot it by:** Multiple sellers/buyers in a single transaction chain.
* **First move:** Define the initial cost as $x$.
* **Fastest method:** Chain all multipliers into one equation.
* **Biggest trap:** Adding percentages instead of multiplying them.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage Multiplier** — A profit of $r\%$ is represented as $(1 + \frac{r}{100})$ and a loss of $r\%$ as $(1 - \frac{r}{100})$.
* **Successive Change** — The principle that a change applied to a value is then applied to the *new* value.

### Formulas You Must Know First
$$
\text{S.P.} = \text{C.P.} \times \left(1 + \frac{\text{Profit}\%}{100}\right)
$$
**What it means:** The selling price is the cost price plus the profit percentage of that cost.

### Terms Used In This Pattern
* **C.P. (Cost Price)** — The price at which an article is purchased.
* **S.P. (Selling Price)** — The price at which an article is sold.