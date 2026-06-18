# Weighted Average Selling Price

## Overview
* This pattern involves calculating the required selling price for a mixed batch of items to achieve a specific overall profit percentage.
* The central idea is to calculate the total Cost Price (CP) of all items combined, apply the profit percentage to that total, and divide by the total quantity of items.

---

## Recognition Clues
* Multiple quantities of different items (e.g., shirts and trousers) are given with their individual unit costs.
* The question asks for the "overall average selling price" to achieve a target profit percentage.
* Keywords: "purchased [x] of A and [y] of B", "overall average selling price", "profit is earned".

---

## Important Formulas

### Total Cost Price
$$
\text{Total CP} = (Q_1 \times P_1) + (Q_2 \times P_2)
$$
*Meaning:* $Q$ = Quantity, $P$ = Price per unit.
*Use when:* You need the base value to calculate the total required revenue.

### Target Selling Price
$$
\text{Total SP} = \text{Total CP} \times \left(1 + \frac{\text{Profit \%}}{100}\right)
$$
*Meaning:* Total SP is the revenue needed to cover costs plus the desired profit.
*Use when:* You have the total investment and the target profit margin.

---

## Solution Framework
1. Calculate the total CP by summing the products of quantities and their respective unit prices.
2. Calculate the total SP by multiplying the total CP by $(1 + \text{Profit \%})$.
3. Sum the total number of items (total quantity).
4. Divide the total SP by the total quantity to find the average selling price.
5. Round off the result to the nearest integer as specified.

---

## Shortcut Tricks
* **Weighted Average Shortcut:** Instead of calculating total SP, calculate the weighted average CP first: $\text{Avg CP} = \frac{\sum (Q_i \times P_i)}{\sum Q_i}$.
* **Why it works:** Multiplying the average CP by $(1 + \text{Profit \%})$ yields the same result as dividing the total SP by total quantity, saving you from handling large numbers in the final division.

---

## Common Mistakes
* **Calculating average of prices first:** Averaging the unit prices (e.g., $\frac{450+550}{2}$) and then applying profit; this is wrong because it ignores the different quantities of each item.
* **Forgetting to sum quantities:** Dividing the total SP by only one of the item quantities instead of the total count.
* **Rounding too early:** Rounding intermediate steps instead of the final result, which leads to precision errors.

---

## Similar Patterns
* This is distinct from simple profit/loss on a single item; it is a **Weighted Average** problem disguised as a Profit and Loss question. Always treat it as a "Total Value / Total Quantity" problem.

---

## Revision Summary
**Key formula:** $\text{Avg SP} = \frac{\text{Total CP} \times (1 + \text{Profit \%})}{\text{Total Quantity}}$.
**Spot it by:** Multiple items with different quantities and unit costs.
**Fastest method:** Find weighted average CP first, then apply the profit percentage.
**Biggest trap:** Calculating the simple average of unit prices instead of the weighted average.