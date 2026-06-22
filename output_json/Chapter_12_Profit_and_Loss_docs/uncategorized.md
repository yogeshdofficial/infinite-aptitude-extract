# Profit and Loss: Quantity-Based Adjustments

## Overview
This pattern involves calculating profit or loss when the quantity of goods changes (due to breakage, waste, or multiple item types) or when overhead costs are added. The central idea is to calculate the **Total Investment (C.P.)** and **Total Revenue (S.P.)** separately before finding the percentage gain or loss.

---

## Recognition Clues
* **Keywords:** "broken," "not working," "transportation," "octroi," "coolie," "average selling price," "remaining items."
* **Given:** Purchase price per unit, quantity, overhead costs (transport/labor), and number of damaged/unsellable units.
* **Asked:** Profit/Loss percentage or the required Selling Price per unit to achieve a target profit.

---

## Key Formulas

### Total Cost Price (C.P.)
$$
\text{Total C.P.} = (\text{Quantity} \times \text{Rate}) + \text{Overheads}
$$
**Variables:** Quantity = number of items; Rate = cost per item; Overheads = extra expenses (transport, labor).
**When to use:** When there are additional costs beyond the purchase price.
**Example:** 120 reams at ₹80 + ₹280 transport = $(120 \times 80) + 280 = 9880$.

### Required Selling Price (S.P.)
$$
\text{Total S.P.} = \text{Total C.P.} \times \left(1 + \frac{\text{Profit } \%}{100}\right)
$$
**Variables:** Profit % = desired gain percentage.
**When to use:** To find the total revenue needed to hit a specific profit target.
**Example:** If C.P. is ₹10,000 and profit is 8%, Total S.P. = $10,000 \times 1.08 = 10,800$.

---

## Solution Framework
1. **Calculate Total C.P.:** Multiply quantity by unit price and add all overheads (transport, labor, etc.).
2. **Adjust Quantity:** Subtract any broken or unusable units from the total quantity to get "sellable units."
3. **Calculate Target Total S.P.:** Apply the profit percentage to the Total C.P. to find the required revenue.
4. **Find Unit S.P.:** Divide the Target Total S.P. by the number of sellable units.

---

## Shortcut Tricks
* **Trick:** Use the "Total Value" approach rather than calculating per-unit costs early.
* **Why it works:** It prevents rounding errors and keeps the focus on the total money invested vs. total money earned.
* **When to use:** Always, especially when overheads are involved.
* **Example:** In Q29, calculating total investment (10,000) first is faster than adding overheads to each individual ream.

---

## Common Mistakes
* **Broken Items:** Forgetting to subtract broken units from the denominator when calculating S.P. per unit.
* **Overheads:** Calculating profit percentage on the purchase price only, ignoring transportation/labor costs.
* **Units:** Mixing up paise and rupees (e.g., 40 paise = ₹0.40).
* **Average:** Taking the simple average of two prices instead of the weighted average (Total S.P. / Total Quantity).

---

## Worked Example (Step-by-Step)

**Question:** A shopkeeper buys 144 eggs at 90 paise each. 20 eggs were broken. He sold the remaining at ₹1.20 each. Find the gain %.

**Solution:**
1. **Total C.P.:** $144 \times 0.90 = 129.60$.
2. **Adjust Quantity:** $144 - 20 = 124$ sellable eggs.
3. **Total S.P.:** $124 \times 1.20 = 148.80$.
4. **Gain %:** $\frac{148.80 - 129.60}{129.60} \times 100 = \frac{19.20}{129.60} \times 100 \approx 14.81\%$.

**Answer:** 14.81%

---

## Similar Patterns
**False Weight Patterns:** Distinguished by the mention of "false weights" or "cheating" rather than "broken" or "damaged" goods.

---

## Revision Summary
* **Key formula:** $\text{Total S.P.} = \text{Total C.P.} \times (1 + \frac{\text{Profit } \%}{100})$.
* **Spot it by:** Look for "broken," "damaged," or "overhead costs" in the text.
* **First move:** Calculate the total investment (C.P.) including all overheads.
* **Fastest method:** Work with total values, not per-unit values, until the final step.
* **Biggest trap:** Dividing total revenue by the *original* quantity instead of the *remaining* quantity.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Weighted Average** — The mean of a set of numbers where some values contribute more than others.
* **Percentage Calculation** — Finding a percentage of a value: `(Value / Total) * 100`.

### Formulas You Must Know First
$$
\text{Profit} = \text{S.P.} - \text{C.P.}
$$
**What it means:** Profit is the surplus money after covering costs.
**Example:** If you buy for 100 and sell for 120, profit is 20.

### Terms Used In This Pattern
* **C.P. (Cost Price)** — The total amount spent to acquire and prepare goods for sale.
* **S.P. (Selling Price)** — The amount received from selling the goods.
* **Overhead** — Additional costs like transport, labor, or taxes.
* **Ream** — A unit of quantity (specifically for paper).