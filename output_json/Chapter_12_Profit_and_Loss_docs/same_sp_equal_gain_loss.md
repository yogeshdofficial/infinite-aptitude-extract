# Same SP, Equal % Gain/Loss

## Overview
This pattern involves selling two items at the same Selling Price (SP), where one is sold at a profit of $x\%$ and the other at a loss of $x\%$. The transaction always results in a net loss, and the specific SP values are irrelevant to calculating the percentage.

---

## Recognition Clues
* **Keywords:** "Sold two [items] for [same price] each", "gains x% on one", "loses x% on the other".
* **Given:** Two items, identical SP, identical percentage values for profit and loss.
* **Asked:** Net gain or loss percent for the entire transaction.
* **Scan Tip:** If you see the same percentage value for both profit and loss, ignore the actual currency values (e.g., ₹ 6,75,958) immediately.

---

## Important Formulas

### [Net Loss Percentage]

$$
\text{Loss\%} = \left( \frac{x}{10} \right)^2
$$

*Meaning:* $x$ is the common profit/loss percentage value.
*Use when:* You need the net percentage change in the total transaction.

---

## Solution Framework
1. Identify the common percentage value ($x$).
2. Divide $x$ by 10.
3. Square the result.
4. Express the final value as a percentage (always a loss).

---

## Shortcut Tricks
* **The "Square and Divide" Trick:** Simply square the first digit of the percentage (if $x$ is a multiple of 10) or calculate $(x/10)^2$.
* **Why it works:** It is a simplified derivation of the net effect formula $\frac{x^2}{100}$, which is mathematically equivalent to $(\frac{x}{10})^2$.

---

## Common Mistakes
* **Mistake:** Assuming there is "No Profit, No Loss" because the percentages are equal.
    * **Reason:** The base (CP) for the profit and loss are different, so the absolute values do not cancel out.
    * **Fix:** Always apply the $\left(\frac{x}{10}\right)^2$ formula; the result is always a loss.
* **Mistake:** Trying to calculate the actual Cost Price of each item.
    * **Reason:** The question asks for percentage, making the actual SP values redundant.
    * **Fix:** Ignore the currency figures entirely to save time.

---

## Similar Patterns
This is distinct from "False Weight" problems (where weights are manipulated) or "Successive Percentage" problems (where the base changes sequentially). If the SP is not identical, this shortcut does not apply.

---

## Revision Summary
**Key formula:** $\text{Loss\%} = (\frac{x}{10})^2$.
**Spot it by:** Identical SP and identical profit/loss percentages.
**Fastest method:** Square the percentage value divided by 10.
**Biggest trap:** Assuming the net result is zero profit/loss.