# Successive Sales

## Overview
These questions involve an item changing hands multiple times, with each transaction involving a profit or loss percentage. The central idea is to treat the final selling price as a product of the initial cost price and the successive multipliers $(1 \pm \frac{r}{100})$.

---

## Recognition Clues
* **Keywords:** "Passing through hands," "A sells to B, B sells to C," "Successive," "Manufacturer to wholesaler to retailer."
* **Given:** Initial cost price OR final selling price, and a series of profit/loss percentages.
* **Asked:** The original cost price (if final is given) or the final selling price (if original is given).
* **Scan for:** A chain of percentage changes applied to a single base value.

---

## Important Formulas

### Successive Multiplier Chain
$$
\text{Final Price} = \text{Initial Price} \times \left(1 \pm \frac{r_1}{100}\right) \times \left(1 \pm \frac{r_2}{100}\right) \times \dots \times \left(1 \pm \frac{r_n}{100}\right)
$$
*Meaning:* Each term represents the multiplier for profit ($+$) or loss ($-$).
*Use when:* You need to find the final price or the starting price in a chain of transactions.

---

## Solution Framework
1. Assign a variable (e.g., $x$) to the unknown price (usually the first cost price).
2. Convert each profit/loss percentage into a multiplier (e.g., 20% profit = $1.20$, 5% loss = $0.95$).
3. Set up the equation: $x \times (\text{multiplier}_1) \times (\text{multiplier}_2) \dots = \text{Final Value}$.
4. Solve for $x$ using basic division.
5. If there are additional costs (like repairs), subtract them from the calculated $x$ at the very end.

---

## Shortcut Tricks
* **Fractional Multipliers:** Convert percentages to fractions (e.g., 25% = $\frac{5}{4}$, 20% = $\frac{6}{5}$) to simplify calculations.
* **Why:** Multiplying fractions often allows for cross-cancellation with the final price, avoiding large decimal multiplications.
* **Symmetry:** If the total percentage change is given, use $(100+x)\%$ of the product of known multipliers to find the unknown percentage.

---

## Common Mistakes
* **Adding Percentages:** Adding profit percentages (e.g., 20% + 10% = 30%) instead of multiplying them.
    * *Reason:* Profit is calculated on the *new* cost price, not the original.
    * *Fix:* Always multiply the multipliers.
* **Ignoring "Additional Costs":** Forgetting to subtract repair/transport costs from the final calculated $x$.
    * *Reason:* The question asks for the *original* purchase price, not the cost after repairs.
    * *Fix:* Read the last sentence carefully to see if the variable $x$ includes extra expenses.
* **Directional Error:** Applying the multiplier to the wrong end of the chain.
    * *Reason:* Confusing the starting price with the final price.
    * *Fix:* Always write the equation as: $\text{Start} \times \text{Multipliers} = \text{End}$.

---

## Similar Patterns
This is distinct from "False Weight" problems because it involves a chain of ownership rather than a single transaction with a dishonest scale.

---

## Revision Summary
**Key formula:** $\text{Final} = \text{Initial} \times \prod (1 \pm \frac{r}{100})$.
**Spot it by:** Multiple traders or "passing through hands" in the question.
**Fastest method:** Convert percentages to fractions and cancel terms.
**Biggest trap:** Adding percentages instead of multiplying them.