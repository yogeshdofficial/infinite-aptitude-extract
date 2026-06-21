# Depreciation/VAT

## Overview
These questions involve adjusting a base value by a percentage rate (VAT/Tax) or applying successive percentage decreases (Depreciation). The central idea is to treat the "Base Value" as 100% and adjust it by the given rate to reach the "Final Value."

---

## Recognition Clues
* **Keywords:** "VAT of X%", "Sales tax of X%", "Depreciates every year", "Worth X years ago".
* **Given:** Final value (including tax or after depreciation) and the rate (%).
* **Asked:** Original list price, cost price, or value at a past time.
* **Visual cue:** Look for a total amount that includes an "extra" percentage (tax) or a "reduced" percentage (depreciation).

---

## Important Formulas

### [VAT/Tax Adjustment]
$$
\text{List Price} = \frac{\text{Price including VAT}}{100 + \text{VAT}\%} \times 100
$$
*Meaning:* Reverses the addition of tax to find the original base price.
*Use when:* You are given a final price that includes a tax percentage.

### [Depreciation/Past Value]
$$
\text{Past Value} = \frac{\text{Present Value}}{(1 - r)^n}
$$
*Meaning:* $r$ is the depreciation rate (as a decimal) and $n$ is the number of years.
*Use when:* You need to find the value of an asset at a time *before* the present.

---

## Solution Framework
1. Identify the base (100%) and the rate (R%).
2. If VAT/Tax: Divide the given total by $(100 + R)$ and multiply by 100.
3. If Depreciation: Divide the present value by $(1 - R)^n$.
4. If multiple conditions (e.g., Profit + Tax): Calculate the base cost price first, then apply the tax/profit multipliers sequentially.

---

## Shortcut Tricks
* **Ratio Method:** Convert the percentage rate to a fraction (e.g., 10% = $1/10$). If depreciating, the value changes from $10 \to 9$. For $n$ years, use $(10/9)^n$.
* **Why it works:** It avoids large decimal calculations and allows for quick cancellation of terms.

---

## Common Mistakes
* **Adding Tax to the Total:** Calculating tax on the final price instead of the base price. Always divide by $(100 + \text{rate})$ to "strip" the tax.
* **Confusing Depreciation with Appreciation:** Subtracting the rate from 100 for depreciation but adding it for tax. Remember: Tax increases the price; Depreciation decreases it.
* **Incorrect Time Period:** Using $n=1$ when the question specifies multiple years. Always check the time duration.

---

## Similar Patterns
This is distinct from standard Profit/Loss because it involves "external" additions (taxes) or "compounded" reductions (depreciation) rather than a simple markup on cost.

---

## Revision Summary
**Key formula:** $\text{Base} = \frac{\text{Final}}{1 \pm \text{Rate}}$.
**Spot it by:** Keywords like "including tax" or "depreciates".
**Fastest method:** Use the fraction ratio method for depreciation.
**Biggest trap:** Calculating tax on the final price instead of the base price.