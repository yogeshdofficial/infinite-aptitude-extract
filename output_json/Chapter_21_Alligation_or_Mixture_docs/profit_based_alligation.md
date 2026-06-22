# Profit-Based Alligation

## Overview
This pattern involves mixing two ingredients of known prices to achieve a target mixture price that yields a specific profit percentage. The central idea is to convert the "Selling Price" of the mixture into its "Cost Price" before applying the rule of alligation.

---

## Recognition Clues
* **Keywords:** "gain %", "selling the mixture at", "in what ratio must be mixed".
* **Given:** Selling Price (SP) of the mixture, Profit %, and the individual Cost Prices (CP) of the two ingredients.
* **Asked:** The ratio in which the ingredients must be mixed, or the quantity of one ingredient required.

---

## Key Formulas

### Cost Price of Mixture
$$
\text{CP}_{\text{mixture}} = \frac{100}{100 + \text{Gain}\%} \times \text{SP}_{\text{mixture}}
$$

**Variables:**
- $\text{CP}_{\text{mixture}}$ = The cost price per unit of the final mixture.
- $\text{Gain}\%$ = The profit percentage earned on the mixture.
- $\text{SP}_{\text{mixture}}$ = The price at which the mixture is sold.

**When to use:** Always use this first when the question provides a selling price and a profit percentage.

**Worked example:** If SP = ₹ 7.20 and Gain = 20%:
$\text{CP} = \frac{100}{120} \times 7.20 = 6$.

---

## Solution Framework

**Step 1: Calculate CP of the mixture** — Use the formula above to find the true cost price, as alligation only works with cost prices.
**Step 2: Set up the Alligation cross** — Place the CP of the cheaper ingredient on the left and the dearer on the right.
**Step 3: Place the Mean Price** — Put the calculated $\text{CP}_{\text{mixture}}$ in the center.
**Step 4: Subtract diagonally** — Subtract the center value from the ingredient prices to find the ratio of quantities.
**Step 5: Scale the ratio** — If a specific quantity is given for one ingredient, use the ratio to find the missing quantity.

---

## Shortcut Tricks

**Trick:** If the gain is 20%, the CP is $\frac{5}{6}$ of the SP. If the gain is 10%, the CP is $\frac{10}{11}$ of the SP.
**Why it works:** It simplifies the fraction $\frac{100}{100+P}$ instantly.
**When to use:** When the gain percentage is a standard value like 10%, 20%, or 25%.
**Example:** For 20% gain, $\text{CP} = \text{SP} \times \frac{100}{120} = \text{SP} \times \frac{5}{6}$.

---

## Common Mistakes

* **Mistake:** Using SP directly in the alligation cross.
    * **Why it happens:** Forgetting that alligation requires cost prices.
    * **Fix:** Always convert SP to CP first.
* **Mistake:** Inverting the ratio.
    * **Why it happens:** Mixing up the "cheaper" and "dearer" positions.
    * **Fix:** Always keep the cheaper price on the left and dearer on the right.
* **Mistake:** Calculation errors with decimals.
    * **Why it happens:** Rushing the subtraction of mean prices.
    * **Fix:** Convert all prices to the same unit (e.g., paise) if decimals are confusing.

---

## Worked Example (Step-by-Step)

**Question:** How many kgs. of wheat costing ₹ 8 per kg must be mixed with 36 kg of rice costing ₹ 5.40 per kg so that 20% gain may be obtained by selling the mixture at ₹ 7.20 per kg?

**Solution:**
1. **Find CP of mixture:** $\text{CP} = \frac{100}{120} \times 7.20 = 6$.
2. **Alligation setup:**
   - Cheaper (Rice): 5.40
   - Dearer (Wheat): 8.00
   - Mean: 6.00
3. **Subtract:**
   - $(8.00 - 6.00) = 2.00$ (Rice part)
   - $(6.00 - 5.40) = 0.60$ (Wheat part)
4. **Ratio:** Wheat : Rice = $0.60 : 2.00 = 6 : 20 = 3 : 10$.
5. **Calculate quantity:** $\frac{\text{Wheat}}{36} = \frac{3}{10} \implies \text{Wheat} = \frac{3 \times 36}{10} = 10.8$ kg.

**Answer:** 10.8 kg.

---

## Similar Patterns

**Simple Alligation:** If the question gives the "Mean Price" directly without a profit percentage, skip the CP calculation step and go straight to the alligation cross.

---

## Revision Summary

* **Key formula:** $\text{CP} = \frac{100}{100 + \text{Gain}\%} \times \text{SP}$.
* **Spot it by:** Looking for "gain %" and "selling price" in mixture problems.
* **First move:** Convert SP to CP immediately.
* **Fastest method:** Use the alligation cross after finding the mean CP.
* **Biggest trap:** Using the selling price as the mean price in the alligation cross.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratio** — A comparison of two quantities expressed as $a:b$.
* **Cost Price (CP)** — The amount paid to acquire an item.
* **Selling Price (SP)** — The amount received after selling an item.

### Formulas You Must Know First
$$
\text{Profit} = \text{SP} - \text{CP}
$$
**What it means:** Profit is the difference between selling price and cost price.

### Terms Used In This Pattern
* **Mean Price** — The cost price of the final mixture.
* **Alligation** — A method to find the ratio of two ingredients when the mean price is known.