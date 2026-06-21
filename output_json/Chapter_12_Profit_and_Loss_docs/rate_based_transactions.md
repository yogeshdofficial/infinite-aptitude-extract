# Rate-Based Transactions

## Overview

These questions involve buying and selling items at specific rates (e.g., "x items for ₹ y") where the quantity and price vary. The central idea is to normalize the quantity by finding the Least Common Multiple (LCM) of the item counts or by calculating the unit price to compare Cost Price (C.P.) and Selling Price (S.P.).

---

## Recognition Clues

* **Keywords:** "at the rate of", "x for ₹ y", "how many for a rupee".
* **Given:** Two different rates for buying and selling, or one rate plus a profit/loss percentage.
* **Asked:** Profit/loss percentage, or the quantity to be sold to achieve a specific profit/loss.
* **Visual cue:** The question provides two distinct ratios of (Quantity : Price).

---

## Important Formulas

### [Profit/Loss Percentage]

$$
\text{Profit/Loss \%} = \left( \frac{\text{S.P.} - \text{C.P.}}{\text{C.P.}} \right) \times 100
$$

*Meaning:* S.P. and C.P. are calculated for the same quantity of items.
*Use when:* You need to find the gain or loss percentage after comparing two rates.

### [Quantity Adjustment]

$$
\text{New Quantity} = \text{Original Quantity} \times \left( \frac{\text{Old Price}}{\text{New Price}} \right) \times \left( \frac{100 \pm \text{Old \%}}{100 \pm \text{New \%}} \right)
$$

*Meaning:* Adjusts the quantity based on price changes and target profit/loss margins.
*Use when:* You are given a rate and a profit/loss, and asked for a new quantity for a different price.

---

## Solution Framework

1. **Normalize Quantity:** Find the LCM of the item counts given in the two rates.
2. **Calculate C.P.:** Determine the total cost for the LCM quantity.
3. **Calculate S.P.:** Determine the total selling price for the same LCM quantity.
4. **Compare:** Find the difference (Profit/Loss) and divide by C.P.
5. **Scale:** If asked for a specific quantity or price, use the unitary method on the calculated C.P./S.P.

---

## Shortcut Tricks

* **Cross-Multiplication:** For rates "a items for ₹ b" (C.P.) and "c items for ₹ d" (S.P.), the profit/loss is determined by comparing $(b \times c)$ and $(a \times d)$.
* **Why:** This effectively calculates the S.P. and C.P. for a common quantity of $(a \times c)$ without explicitly writing out the LCM.

---

## Common Mistakes

* **Mixing Units:** Calculating profit on different quantities (e.g., comparing 6 items' C.P. to 4 items' S.P.).
    * *Reason:* Profit/Loss must be calculated on the same base quantity.
    * *Fix:* Always equate the number of items using LCM before subtracting.
* **Inverting the Ratio:** Flipping the price/quantity fraction (e.g., using $\frac{6}{10}$ instead of $\frac{10}{6}$).
    * *Reason:* Confusing "Price per item" with "Items per price".
    * *Fix:* Always write the units clearly: $\frac{\text{Price}}{\text{Quantity}}$.
* **Ignoring the Base:** Calculating profit percentage on S.P. instead of C.P.
    * *Reason:* Habitual error in percentage calculations.
    * *Fix:* Always divide by C.P. as per the fundamental definition.

---

## Similar Patterns

This pattern is distinct from "False Weight" problems because it deals with variable rates of goods rather than physical weight manipulation.

---

## Revision Summary

**Key formula:** $\text{Profit/Loss \%} = \frac{\text{S.P.} - \text{C.P.}}{\text{C.P.}} \times 100$.

**Spot it by:** Rates given as "x items for ₹ y".

**Fastest method:** Cross-multiply the rates to compare total C.P. and S.P.

**Biggest trap:** Comparing prices of different quantities without normalizing to LCM.