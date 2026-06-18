# Successive Discounts

## Overview

These questions involve multiple percentage reductions applied sequentially to a marked price (M.P.) or list price. The central idea is that each subsequent discount is calculated on the *remaining* value after the previous discount, not on the original price.

---

## Recognition Clues

* **Keywords:** "Successive discounts," "additional discount," "discount on the reduced price," "series discount."
* **Given:** Marked price (M.P.), list price, or a series of percentage rates.
* **Asked:** Final selling price (S.P.), the single equivalent discount, or the original list price.
* **Visual Cue:** Look for phrases like "10% and 20% successive" or "extra discount on the reduced price."

---

## Important Formulas

### [Net Selling Price]
$$
\text{S.P.} = \text{M.P.} \times \left(1 - \frac{d_1}{100}\right) \times \left(1 - \frac{d_2}{100}\right) \times \dots
$$
*Meaning:* $d_1, d_2$ are successive discount percentages.
*Use when:* You need the final price after multiple discounts.

### [Equivalent Single Discount]
$$
\text{Single Discount} = 100 - \left[ 100 \times \left(1 - \frac{d_1}{100}\right) \times \left(1 - \frac{d_2}{100}\right) \dots \right]
$$
*Meaning:* The single percentage that replaces a series of discounts.
*Use when:* The question asks for a "single discount equivalent" to a series.

---

## Solution Framework

1. Assume the Marked Price (M.P.) is 100 (if not given).
2. Apply the first discount to the M.P. to get the intermediate price.
3. Apply the next discount to the *intermediate* price, not the original M.P.
4. Repeat until all discounts are applied.
5. If finding the original price, set the final S.P. equal to the product of the multipliers and solve for M.P.

---

## Shortcut Tricks

* **Free Item Trick:** If you get $n$ items free on a purchase of $m$ items, the discount % is $\frac{n}{m+n} \times 100$.
    * *Why:* You are effectively receiving $(m+n)$ items while paying for only $m$.
* **Successive Change (2 discounts):** For two discounts $a\%$ and $b\%$, the equivalent discount is $(a + b - \frac{ab}{100})\%$.
    * *Why:* This is derived from the expansion of $(1 - \frac{a}{100})(1 - \frac{b}{100})$.

---

## Common Mistakes

* **Adding Percentages:** Adding discounts (e.g., 10% + 20% = 30%).
    * *Reason:* Discounts are multiplicative, not additive.
    * *Fix:* Always use the multiplier $(1 - \frac{d}{100})$.
* **Applying to M.P. repeatedly:** Calculating all discounts on the original M.P.
    * *Reason:* Successive discounts are applied to the *diminishing* balance.
    * *Fix:* Multiply the M.P. by each discount factor sequentially.
* **Confusing S.P. and M.P.:** Using S.P. as the base for the first discount.
    * *Reason:* Discounts are always calculated on the Marked Price (List Price).
    * *Fix:* Clearly label M.P. and S.P. before starting calculations.

---

## Similar Patterns

* **Successive Percentage Increases:** These are solved similarly but using $(1 + \frac{r}{100})$ instead of $(1 - \frac{d}{100})$.
* **Profit/Loss:** Often confused because both involve percentages; remember that discounts apply to M.P., while profit/loss applies to C.P.

---

## Revision Summary

**Key formula:** $\text{S.P.} = \text{M.P.} \times \prod (1 - \frac{d_i}{100})$.

**Spot it by:** Phrases like "successive," "additional," or "discount on reduced price."

**Fastest method:** Use multipliers (e.g., 20% discount = 0.8 multiplier) for rapid calculation.

**Biggest trap:** Adding discount percentages together instead of multiplying their factors.