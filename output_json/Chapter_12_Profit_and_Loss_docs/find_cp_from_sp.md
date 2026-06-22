# Find CP from SP

## Overview
This pattern involves calculating the original Cost Price (CP) when you are given the Selling Price (SP) and a profit or loss percentage. The central idea is that the SP is always a percentage of the CP, so you must divide the SP by that percentage to "reverse" the transaction back to the base cost.

---

## Recognition Clues
* **Keywords:** "sold for", "paid", "charges", "gain of", "loss of", "what was the cost price".
* **Given:** Selling Price (SP) and a percentage (Profit % or Loss %).
* **Asked:** Original Cost Price (CP).
* **Context:** A transaction where the final price is known, but the starting price is missing.

---

## Key Formulas

### [Cost Price from Profit]
$$
\text{C.P.} = \text{S.P.} \times \left( \frac{100}{100 + \text{Profit } \%} \right)
$$

**Variables:**
- $\text{S.P.}$ = Final price paid by the customer
- $\text{Profit } \%$ = The percentage gain over the cost price

**When to use:** When the item is sold at a profit (e.g., "charges 23% more").

**Worked example:** If $\text{S.P.} = 7011$ and $\text{Profit} = 23\%$:
$\text{C.P.} = 7011 \times \left( \frac{100}{123} \right) = 5700$.

### [Cost Price from Loss]
$$
\text{C.P.} = \text{S.P.} \times \left( \frac{100}{100 - \text{Loss } \%} \right)
$$

**Variables:**
- $\text{S.P.}$ = Final price received
- $\text{Loss } \%$ = The percentage decrease from the cost price

**When to use:** When the item is sold at a loss (e.g., "sold at a loss of 20%").

**Worked example:** If $\text{S.P.} = 14500$ and $\text{Loss} = 20\%$:
$\text{C.P.} = 14500 \times \left( \frac{100}{80} \right) = 18125$.

---

## Solution Framework
1. **Identify the base:** Determine if the percentage is a profit (add to 100) or a loss (subtract from 100).
2. **Set up the ratio:** Express the SP as a percentage of the CP (e.g., $123\%$ of $\text{CP} = \text{SP}$).
3. **Isolate CP:** Multiply the SP by the reciprocal of the percentage fraction ($\frac{100}{\text{percentage value}}$).
4. **Calculate:** Perform the division and multiplication to find the final value.

---

## Shortcut Tricks
* **Trick:** Use the "Fractional Multiplier" method.
* **Why it works:** It avoids complex decimals by converting percentages to simple fractions (e.g., $20\% \text{ loss} = \frac{4}{5}$ of CP, so $\text{CP} = \text{SP} \times \frac{5}{4}$).
* **When to use it:** When the percentage is a clean number like 20%, 25%, or 50%.
* **Example:** For $20\%$ loss, $\text{CP} = \text{SP} \times \frac{100}{80} = \text{SP} \times \frac{5}{4}$.

---

## Common Mistakes
* **Mistake:** Calculating the percentage of the SP and adding/subtracting it.
    * **Why it happens:** Confusing the base (Profit/Loss is always on CP, not SP).
    * **Fix:** Always divide the SP by the percentage factor (e.g., $1.23$ or $0.80$).
* **Mistake:** Using the wrong sign in the denominator.
    * **Why it happens:** Rushing through the sign (Profit = $+$, Loss = $-$).
    * **Fix:** Double-check the question for "gain" or "loss" before setting up the fraction.

---

## Worked Example (Step-by-Step)

**Question:** The owner of a cell phone charges his customer 23% more than the cost price. If a customer paid ₹ 7011 for a cell phone, then what was the cost price?

**Solution:**
1. **Identify:** Profit is 23%. The SP is $100\% + 23\% = 123\%$ of CP.
2. **Equation:** $1.23 \times \text{CP} = 7011$.
3. **Isolate:** $\text{CP} = \frac{7011}{1.23}$.
4. **Calculate:** $\frac{701100}{123} = 5700$.

**Answer:** ₹ 5,700.

---

## Similar Patterns
**Find SP from CP:** Distinguished by the question asking for the final price given the cost price; here you multiply by the percentage instead of dividing.

---

## Revision Summary
* **Key formula:** $\text{CP} = \text{SP} \times \frac{100}{100 \pm \%}$.
* **Spot it by:** Given SP and Profit/Loss %, asked for CP.
* **First move:** Determine if it is a profit (+) or loss (-).
* **Fastest method:** Use the reciprocal fraction of the percentage.
* **Biggest trap:** Calculating the percentage of the SP instead of the CP.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage as a decimal:** Understanding that $123\% = 1.23$ and $80\% = 0.80$.
* **Algebraic Isolation:** Moving a multiplier from one side of an equation to the other by dividing.

### Formulas You Must Know First
* **Profit/Loss Percentage:** $\text{Profit} \% = \frac{\text{Profit}}{\text{CP}} \times 100$.

### Terms Used In This Pattern
* **Cost Price (CP):** The original price paid for an item.
* **Selling Price (SP):** The price at which the item is sold to the customer.