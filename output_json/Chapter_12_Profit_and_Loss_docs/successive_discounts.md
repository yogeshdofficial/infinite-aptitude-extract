# Successive Discounts

## Overview
These questions involve applying multiple percentage reductions sequentially to a single Marked Price (M.P.). The central idea is that each subsequent discount is calculated on the *remaining* balance, not the original M.P.

---

## Recognition Clues
* **Keywords:** "Successive discounts," "rebate on the reduced price," "series discount," or "further discount."
* **Given:** A series of percentage values (e.g., 10%, 20%) and either the M.P. or the final Selling Price (S.P.).
* **Asked:** Either the "single equivalent discount" or the final price after all discounts are applied.

---

## Important Formulas

### [Equivalent Single Discount]
$$
\text{Single Discount \%} = \left( p + q - \frac{pq}{100} \right) \%
$$
*Meaning:* $p$ and $q$ are two successive discount percentages.
*Use when:* You need to find the single discount equivalent to two successive discounts quickly.

### [Successive Multiplier Method]
$$
\text{S.P.} = \text{M.P.} \times \left( 1 - \frac{d_1}{100} \right) \times \left( 1 - \frac{d_2}{100} \right) \times \dots
$$
*Meaning:* $d_1, d_2$ are successive discount percentages; S.P. is the final price.
*Use when:* Calculating the final price after three or more discounts or solving for M.P.

---

## Solution Framework
1. Assume the Marked Price (M.P.) is $100$ (or use the given value if provided).
2. Convert each discount $d\%$ into its remaining value factor: $(100 - d)\%$.
3. Multiply the M.P. by all the remaining value factors sequentially.
4. If finding a single discount, subtract the final result from $100$.
5. If solving for M.P. given S.P., equate the product to the given S.P. and solve for $x$.

---

## Shortcut Tricks
* **Ratio Method:** Convert discounts to fractions (e.g., $20\% = \frac{1}{5}$, so price becomes $\frac{4}{5}$). Multiply the fractions of the remaining values to get the final ratio of S.P. to M.P.
* **Symmetry:** For two discounts of $x\%$ and $y\%$, the order does not matter; the final S.P. remains the same.

---

## Common Mistakes
* **Adding percentages:** Adding $10\% + 20\% = 30\%$. This ignores that the second discount is on a smaller base. Always use the multiplicative approach.
* **Discounting the discount:** Calculating the second discount on the *original* M.P. instead of the *reduced* price.
* **Mixing up M.P. and S.P.:** Applying discounts to the Cost Price (C.P.) instead of the Marked Price.

---

## Similar Patterns
This is distinct from "Profit and Loss" percentage changes because discounts always reduce the price from the M.P., whereas profit/loss is calculated on the C.P.

---

## Revision Summary
**Key formula:** $\text{S.P.} = \text{M.P.} \times \prod (1 - \frac{d_i}{100})$.
**Spot it by:** Multiple percentage "rebates" or "successive" discounts mentioned.
**Fastest method:** Use the multiplier method (e.g., $0.9 \times 0.8 \times \text{M.P.}$).
**Biggest trap:** Simply adding the discount percentages together.