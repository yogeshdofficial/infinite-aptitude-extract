# Missing Component Price

## Overview
This pattern involves finding the unknown price of one ingredient when the prices of other ingredients and the final mixture ratio are known. The central idea is the **Rule of Alligation**, which balances the differences between individual prices and the mean price against the given ratio.

---

## Recognition Clues
* **Keywords:** "mixed in the ratio," "mixture is worth," "price per kg of the mixed variety," "what is the rate per kg."
* **Given:** Prices of components (or a way to calculate them) and the ratio of the mixture.
* **Asked:** The price of one of the components (or the mean price).
* **Visual:** Look for two or more prices and a ratio; you are solving for the "missing" price variable.

---

## Key Formulas

### Rule of Alligation
$$
\frac{\text{Price}_2 - \text{Mean Price}}{\text{Mean Price} - \text{Price}_1} = \frac{\text{Quantity}_1}{\text{Quantity}_2}
$$

**Variables:**
- $\text{Price}_1, \text{Price}_2$ = Cost per unit of the two ingredients.
- $\text{Mean Price}$ = Cost per unit of the final mixture.
- $\text{Quantity}_1, \text{Quantity}_2$ = The ratio in which they are mixed.

**When to use:** Whenever you have two ingredients and need to find one of the three price variables (Price 1, Price 2, or Mean Price).

**Worked example:** Using Q5: Price 1 = 15, Price 2 = 20, Ratio = 2:3.
$\frac{20 - x}{x - 15} = \frac{2}{3} \implies 60 - 3x = 2x - 30 \implies 5x = 90 \implies x = 18$.

---

## Solution Framework

1. **Step 1: Identify the variables** — Assign $x$ to the unknown price and list the known prices and the ratio.
2. **Step 2: Set up the Alligation cross** — Place the two prices at the top and the mean price in the center.
3. **Step 3: Calculate differences** — Subtract the mean price from the larger price and the smaller price from the mean price.
4. **Step 4: Equate to the ratio** — Set the ratio of these differences equal to the given mixture ratio.
5. **Step 5: Solve for $x$** — Use cross-multiplication to isolate $x$ and find the missing price.

---

## Shortcut Tricks

* **Trick:** If the ratio is $1:1$, the mean price is simply the arithmetic average of the two component prices.
* **Why it works:** When quantities are equal, the weighted average formula $\frac{P_1+P_2}{2}$ applies.
* **When to use:** Only when the question states the ratio is $1:1$ or "equal proportions."
* **Example:** In Q14, the first two teas are $1:1$. Average = $(126+135)/2 = 130.50$.

---

## Common Mistakes

* **Mistake:** Calculating a simple average when the ratio is not $1:1$.
    * **Why it happens:** Assuming the mean is always the midpoint.
    * **Fix:** Always use the Alligation cross for ratios other than $1:1$.
* **Mistake:** Swapping the ratio values in the fraction.
    * **Why it happens:** Misaligning the "cheaper" and "dearer" quantities.
    * **Fix:** Ensure the difference involving the "dearer" price is paired with the "cheaper" quantity.
* **Mistake:** Arithmetic errors with decimals.
    * **Why it happens:** Rushing the cross-multiplication.
    * **Fix:** Convert all values to the same unit (e.g., paise) if decimals are confusing.

---

## Worked Example (Step-by-Step)

**Question (Q13):** One quality of wheat at ₹ 9.30 per kg is mixed with another quality at a certain rate in the ratio 8 : 7. If the mixture so formed be worth ₹ 10 per kg, what is the rate per kg of the second quality of wheat?

**Solution:**
1. **Identify:** Price 1 = 9.30, Mean = 10.00, Ratio = 8:7. Let Price 2 = $x$.
2. **Alligation:** 
   - Difference 1 (between $x$ and 10) = $x - 10$
   - Difference 2 (between 10 and 9.30) = $0.70$
3. **Equate:** $\frac{x - 10}{0.70} = \frac{8}{7}$
4. **Solve:** $7(x - 10) = 8 \times 0.70 \implies 7x - 70 = 5.60 \implies 7x = 75.60 \implies x = 10.80$.

**Answer:** ₹ 10.80 per kg.

---

## Similar Patterns
**Weighted Average Problems:** These are mathematically identical to Alligation but often presented as "find the average of a group." Use Alligation when you have a ratio and need a component price; use Weighted Average when you have all components and need the mean.

---

## Revision Summary
* **Key formula:** $\frac{\text{Price}_2 - \text{Mean}}{\text{Mean} - \text{Price}_1} = \frac{\text{Qty}_1}{\text{Qty}_2}$.
* **Spot it by:** Mixture ratio given, one price missing.
* **First move:** Set unknown price as $x$.
* **Fastest method:** Alligation cross-subtraction.
* **Biggest trap:** Using simple average instead of weighted average.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio** — A comparison of two quantities expressed as $a:b$ or $\frac{a}{b}$.
* **Weighted Average** — The mean of a set of numbers where some values contribute more than others.

### Formulas You Must Know First
$$
\text{Mean Price} = \frac{\sum (\text{Price} \times \text{Quantity})}{\sum \text{Quantity}}
$$
**What it means:** The total cost of the mixture divided by the total quantity.

### Terms Used In This Pattern
* **Mean Price** — The cost price of the final mixture.
* **Alligation** — A method to solve problems involving the mixing of two or more ingredients.