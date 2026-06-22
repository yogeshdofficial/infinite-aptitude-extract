# Quantity Adjustment

## Overview
This pattern involves mixtures where you either add/remove an ingredient or combine two different mixtures to reach a target concentration or ratio. The central idea is to use the **Rule of Alligation** for concentration problems or **Algebraic Balancing** for quantity addition/removal problems.

---

## Recognition Clues
* **Keywords:** "replaced by," "added to," "mixture contains," "profit on the whole," "ratio of."
* **Given:** Initial ratio/concentration, amount added/removed, or final target ratio/concentration.
* **Asked:** Quantity of a specific ingredient, amount to be added, or fraction replaced.

---

## Key Formulas

### Rule of Alligation
$$
\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{\text{Price}_D - \text{Mean}}{\text{Mean} - \text{Price}_C}
$$
**Variables:** $Price_D$ = higher concentration/price, $Price_C$ = lower concentration/price, $Mean$ = target concentration/price.
**When to use:** When mixing two substances with different concentrations/prices to get a specific mean.
**Worked example:** Q16: $40\%$ and $19\%$ mixed to get $26\%$. Ratio = $(26-19) : (40-26) = 7:14 = 1:2$.

### Component Quantity
$$
\text{Quantity of Component} = \frac{\text{Ratio Part}}{\text{Total Ratio Parts}} \times \text{Total Quantity}
$$
**Variables:** Ratio Part = specific share, Total Ratio Parts = sum of all parts, Total Quantity = volume of mixture.
**When to use:** To find the actual amount of an ingredient before adding or removing.
**Worked example:** Q22: 20L mixture, ratio 3:1. Milk = $\frac{3}{4} \times 20 = 15$L.

---

## Solution Framework

1. **Identify the type:** If given two concentrations and a mean, use **Alligation**. If given a ratio and an addition/removal, use **Algebraic Balancing**.
2. **Find initial amounts:** Use the total quantity and ratio to find the exact volume of each ingredient.
3. **Apply changes:** Add or subtract the specified amounts to the individual components (e.g., $15+x$ for milk).
4. **Set up the equation:** Equate the new ratio to the target ratio provided in the question.
5. **Solve for $x$:** Perform basic algebraic cross-multiplication to find the unknown quantity.

---

## Shortcut Tricks

* **Trick:** In Alligation, the ratio is always the *difference* between the values.
* **Why it works:** It balances the "excess" of one ingredient against the "deficit" of the other relative to the mean.
* **When to use:** Whenever you see two distinct concentrations/prices and a target mean.
* **Example:** Q15: Profit 8% and 18%, Mean 14%. Differences are $(18-14)=4$ and $(14-8)=6$. Ratio $4:6 = 2:3$.

---

## Common Mistakes

* **Mistake:** Adding the new quantity to the *total* mixture instead of the *specific* component.
    * **Fix:** Only add/subtract from the specific ingredient's variable.
* **Mistake:** Forgetting to subtract the removed portion in multi-part mixtures (Q23).
    * **Fix:** Calculate the removed amount using the initial ratio before adding new quantities.
* **Mistake:** Mixing up the order of subtraction in Alligation.
    * **Fix:** Always subtract the smaller value from the larger value to keep the ratio positive.

---

## Worked Example (Step-by-Step)

**Question (Q22):** 20 litres of a mixture contains milk and water in the ratio 3 : 1. Then the amount of milk to be added to the mixture so as to have milk and water in ratio 4 : 1 is?

**Solution:**
1. **Find initial amounts:** Total parts = $3+1=4$. Milk = $\frac{3}{4} \times 20 = 15$L. Water = $\frac{1}{4} \times 20 = 5$L.
2. **Apply changes:** Let $x$ be milk added. New milk = $15+x$. Water remains $5$L.
3. **Set up equation:** $\frac{15+x}{5} = \frac{4}{1}$.
4. **Solve:** $15+x = 20 \Rightarrow x = 5$.

**Answer:** 5 litres.

---

## Similar Patterns
* **Partnership Problems:** These involve investment and time ratios; distinguish by looking for "money/time" keywords vs "mixture/concentration" keywords.

---

## Revision Summary
* **Key formula:** $\frac{\text{Part}}{\text{Total}} \times \text{Total Quantity}$ or Alligation ratio.
* **Spot it by:** "Added to," "Replaced by," or "Ratio of concentrations."
* **First move:** Calculate the initial quantity of each ingredient using the ratio.
* **Fastest method:** Use Alligation for concentration/price; use Algebra for adding/removing.
* **Biggest trap:** Adding the new quantity to the total volume instead of the specific ingredient.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratios:** Expressing parts of a whole ($a:b$ means $\frac{a}{a+b}$ of the total).
* **Algebraic Equations:** Solving $ax + b = c$ for $x$.

### Formulas You Must Know First
* **Fractional Part:** $\text{Value} = \text{Ratio} \times \text{Total}$.

### Terms Used In This Pattern
* **Alligation:** A method to find the ratio of two ingredients to reach a mean value.
* **Mean:** The weighted average concentration or price of the final mixture.