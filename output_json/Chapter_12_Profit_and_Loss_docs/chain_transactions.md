# Chain Transactions

## Overview

These questions involve an item passing through multiple hands (manufacturer, dealer, retailer) where each party adds a profit or incurs a loss. The central idea is to treat the final price as a product of successive percentage changes applied to the initial cost price.

---

## Recognition Clues

* **Keywords:** "Passing through hands," "successive," "A sells to B, B sells to C," "manufacturer/wholesale/retailer."
* **Given:** A sequence of profit/loss percentages and either the initial cost or the final selling price.
* **Asked:** Either the initial cost price or the final selling price after the chain is complete.
* **Visual cue:** A chain of transactions where the Selling Price (S.P.) of one person becomes the Cost Price (C.P.) of the next.

---

## Important Formulas

### Successive Transaction Formula

$$
\text{Final Price} = \text{Initial Price} \times \left(1 \pm \frac{r_1}{100}\right) \times \left(1 \pm \frac{r_2}{100}\right) \times \dots \times \left(1 \pm \frac{r_n}{100}\right)
$$

*Meaning:* $r_n$ is the profit (+) or loss (-) percentage at each stage.
*Use when:* You need to find the final price given the initial cost, or vice versa.

---

## Solution Framework

1. Assign a variable (e.g., $x$) to the unknown initial cost price.
2. Represent each profit as $(100 + \text{gain})\%$ and each loss as $(100 - \text{loss})\%$.
3. Multiply the initial price by these percentage factors in sequence.
4. Equate the resulting expression to the final given value.
5. Solve for $x$ using basic algebraic isolation.

---

## Shortcut Tricks

* **Fractional Multipliers:** Convert percentages to fractions (e.g., $20\% = \frac{6}{5}$, $25\% = \frac{5}{4}$) before multiplying.
* **Why:** Multiplying fractions is significantly faster and less prone to decimal errors than multiplying large percentages.
* **Example:** $125\% \times 120\% \times x \rightarrow \frac{5}{4} \times \frac{6}{5} \times x = \frac{3}{2}x$.

---

## Common Mistakes

* **Adding Percentages:** Adding profit percentages (e.g., $20\% + 10\% = 30\%$) instead of multiplying them.
    * *Reason:* Profit is calculated on the *new* cost price, not the original.
    * *Fix:* Always multiply the factors: $(1.20 \times 1.10)$.
* **Ignoring Intermediate Costs:** Forgetting to subtract repair/transport costs from the initial price before starting the chain.
    * *Reason:* The chain starts from the *actual* investment.
    * *Fix:* Calculate the "true" initial cost ($C.P. + \text{repairs}$) first.
* **Directional Error:** Dividing by the percentage factor when you should multiply (or vice versa).
    * *Reason:* Confusing "Initial to Final" with "Final to Initial."
    * *Fix:* Always write the equation: $\text{Initial} \times \text{Factors} = \text{Final}$.

---

## Similar Patterns

This pattern is distinct from "False Weight" problems because it involves a sequence of independent transactions rather than a single transaction with a deceptive measurement.

---

## Revision Summary

**Key formula:** $\text{Final} = \text{Initial} \times \prod (1 \pm \frac{r}{100})$.

**Spot it by:** Multiple parties buying and selling the same item sequentially.

**Fastest method:** Convert all percentages to fractions and multiply them.

**Biggest trap:** Adding profit percentages instead of multiplying the factors.