# Same SP Different %

## Overview
This pattern involves selling two distinct items at the **same selling price**, where one item is sold at a profit percentage ($x\%$) and the other at an identical loss percentage ($x\%$). The central concept is that such a transaction **always results in a net loss**, regardless of the specific selling price values.

---

## Recognition Clues
* **Keywords:** "Sold two [items] for [same price] each", "gains $x\%$ on one and loses $x\%$ on the other".
* **Given:** Selling price (SP) of both items is identical; profit % and loss % are numerically equal.
* **Asked:** Overall gain or loss percentage, or the absolute value of the gain/loss in currency.

---

## Important Formulas

### Net Loss Percentage
$$
\text{Loss}\% = \left( \frac{x}{10} \right)^2
$$
*Meaning:* $x$ is the common profit/loss percentage.
*Use when:* The question asks for the overall percentage change in the transaction.

### Net Loss in Currency
$$
\text{Loss} = (\text{Total CP}) - (\text{Total SP})
$$
*Meaning:* Total CP is the sum of individual CPs calculated as $\frac{100}{100 \pm x} \times \text{SP}$.
*Use when:* The question asks for the actual monetary value of the loss.

---

## Solution Framework

1. **Identify the common percentage ($x$):** Extract the numerical value of the profit/loss.
2. **Apply the shortcut:** Calculate $\left(\frac{x}{10}\right)^2$ to get the percentage loss immediately.
3. **Calculate individual CPs (if needed):** Use $CP = \frac{100}{100+x} \times SP$ (for profit) and $CP = \frac{100}{100-x} \times SP$ (for loss).
4. **Sum the CPs:** Add the two calculated CPs to find the total investment.
5. **Find absolute loss:** Subtract the total SP ($2 \times \text{SP}$) from the total CP.

---

## Shortcut Tricks

* **The "Always Loss" Rule:** Never calculate gain; the result is always a loss.
* **Mental Math:** If $x=10$, loss is $1\%$; if $x=20$, loss is $4\%$; if $x=5$, loss is $0.25\%$.
* **Why it works:** The loss on the item sold at a discount is always greater than the profit on the item sold at a premium because the base (CP) for the loss item is higher.

---

## Common Mistakes

* **Assuming "No Profit, No Loss":** Students often think $+x\%$ and $-x\%$ cancel out.
    * *Reason:* Percentages are calculated on different base CPs.
    * *Fix:* Always apply the $\left(\frac{x}{10}\right)^2$ formula.
* **Using SP as the base for %:** Calculating the loss percentage on the total SP.
    * *Reason:* Profit/Loss is always calculated on CP.
    * *Fix:* Use the standard formula; ignore the SP value when only the percentage is asked.
* **Mixing up CP formulas:** Using the wrong denominator for the profit/loss item.
    * *Reason:* Rushing the calculation of individual CPs.
    * *Fix:* Remember: Profit item CP = $\frac{100}{100+x} \times SP$; Loss item CP = $\frac{100}{100-x} \times SP$.

---

## Similar Patterns
This is distinct from "False Weight" problems. If the question mentions weights or grams, use the False Weight formulas; if it only mentions prices and percentages, use this pattern.

---

## Revision Summary

**Key formula:** $\text{Loss}\% = (\frac{x}{10})^2$.

**Spot it by:** Same SP for two items with equal profit/loss percentages.

**Fastest method:** Square the first digit of the percentage (if $x$ is a multiple of 10).

**Biggest trap:** Assuming the net result is zero profit/loss.