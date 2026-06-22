# Alligation Basics

## Overview
This pattern is used when you need to find the ratio in which two ingredients (with different known prices) must be mixed to achieve a specific target "mean" price. The central idea is to calculate the difference between each ingredient's price and the mean price, then cross-assign these differences to find the ratio.

---

## Recognition Clues
* **Keywords:** "In what ratio must...", "mixed with...", "worth...", "mixture".
* **Given:** Two individual prices (e.g., ₹ 15/kg and ₹ 20/kg) and one mean price (e.g., ₹ 16.50/kg).
* **Asked:** The ratio of the two ingredients.
* **Scan:** Look for three price values; the mean price will always be between the two individual prices.

---

## Key Formulas

### Alligation Ratio Formula
$$
\text{Ratio} = (\text{Price}_{\text{Dearer}} - \text{Mean}) : (\text{Mean} - \text{Price}_{\text{Cheaper}})
$$

**Variables:**
- $\text{Price}_{\text{Dearer}}$ = The higher unit price
- $\text{Price}_{\text{Cheaper}}$ = The lower unit price
- $\text{Mean}$ = The target price of the mixture

**When to use:** Whenever you are asked for the ratio of two components to form a mixture of a given price.

**Worked example:** Rice at ₹ 9.30 (Cheaper) and ₹ 10.80 (Dearer) mixed to cost ₹ 10.00 (Mean).
Ratio = $(10.80 - 10.00) : (10.00 - 9.30) = 0.80 : 0.70 = 8 : 7$.

---

## Solution Framework

**Step 1: Standardize units** — Convert all values to the same unit (e.g., all to paise) to eliminate decimals.
**Step 2: Set up the cross** — Place the two prices at the top left and top right, and the mean price in the center.
**Step 3: Calculate differences** — Subtract the mean from the higher price (place result under the cheaper price) and subtract the lower price from the mean (place result under the dearer price).
**Step 4: Simplify** — Reduce the resulting ratio to its simplest form.

---

## Shortcut Tricks

* **Trick:** Work in paise or multiply by 10/100 immediately to remove decimals.
* **Why it works:** It prevents arithmetic errors caused by decimal subtraction under pressure.
* **When to use:** Whenever prices are given in decimals (e.g., ₹ 9.30, ₹ 16.50).
* **Example:** Instead of $16.50 - 15 = 1.50$, use $1650 - 1500 = 150$.

---

## Common Mistakes

* **Mistake:** Subtracting the mean from the wrong side.
    * **Why it happens:** Confusing the "Cheaper" and "Dearer" positions.
    * **Fix:** Always ensure the result under the "Cheaper" price is the difference between the "Dearer" price and the "Mean".
* **Mistake:** Forgetting to simplify the final ratio.
    * **Why it happens:** Rushing to the final answer.
    * **Fix:** Always check if the ratio can be divided by a common factor.

---

## Worked Example (Step-by-Step)

**Question:** In what ratio must tea at ₹ 62 per kg be mixed with tea at ₹ 72 per kg so that the mixture must be worth ₹ 64.50 per kg?

**Solution:**
1. **Standardize:** Prices are 6200p, 7200p, and 6450p.
2. **Set up:** 
   - Left: 6200 (Cheaper)
   - Right: 7200 (Dearer)
   - Center: 6450 (Mean)
3. **Calculate Differences:**
   - Under Cheaper: $7200 - 6450 = 750$
   - Under Dearer: $6450 - 6200 = 250$
4. **Simplify:** $750 : 250 = 3 : 1$.

**Answer:** 3 : 1

---

## Similar Patterns
**Weighted Averages:** This is mathematically identical to alligation; use alligation when you need the *ratio* of quantities, and weighted averages when you need the *resultant mean* given the ratio.

---

## Revision Summary
* **Key formula:** $(\text{Dearer} - \text{Mean}) : (\text{Mean} - \text{Cheaper})$.
* **Spot it by:** Three price values given, ratio asked.
* **First move:** Convert all values to the same unit (e.g., paise).
* **Fastest method:** Cross-subtraction method.
* **Biggest trap:** Inverting the ratio or failing to simplify.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Ratios** — Expressing the relationship between two quantities as $a:b$.
* **Decimal Arithmetic** — Basic subtraction of numbers like $10.80 - 10.00$.

### Formulas You Must Know First
* No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Mean Price** — The target cost price of the final mixture.
* **Alligation** — A shortcut method to solve mixture problems involving two components.