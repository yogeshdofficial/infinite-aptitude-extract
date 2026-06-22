# Mixture Replacement

## Overview
This pattern involves two distinct scenarios: mixing two ingredients to achieve a target price (Alligation) and repeatedly replacing a portion of a mixture with another liquid. The central idea is to use the weighted average of costs for mixing or the exponential decay formula for repeated replacements.

---

## Recognition Clues
* **Alligation:** Keywords like "in what ratio," "mixed," "worth," or "price per litre."
* **Replacement:** Keywords like "drawn out," "replaced by," "repeated," or "n times."
* **Given:** Cost prices of individual items, mean price of the mixture, or total volume and amount removed.
* **Asked:** The ratio of ingredients or the final quantity of the original liquid remaining.

---

## Key Formulas

### [Alligation Ratio]
$$
\text{Ratio} = (\text{Price}_{\text{Dearer}} - \text{Mean}) : (\text{Mean} - \text{Price}_{\text{Cheaper}})
$$
**Variables:**
- $\text{Price}_{\text{Dearer}}$ = Higher cost per unit
- $\text{Price}_{\text{Cheaper}}$ = Lower cost per unit (Water = 0)
- $\text{Mean}$ = Target price of the mixture

**When to use:** When asked for the ratio to mix two items to get a specific price.

**Worked example:** Milk (₹12) and Water (₹0) mixed to get ₹8. Ratio = $(12-8) : (8-0) = 4:8 = 1:2$.

### [Repeated Replacement]
$$
\text{Final Quantity} = \text{Initial} \times \left( 1 - \frac{\text{Removed}}{\text{Total}} \right)^n
$$
**Variables:**
- $\text{Initial}$ = Starting volume
- $\text{Removed}$ = Amount taken out per operation
- $\text{Total}$ = Total capacity of the container
- $n$ = Number of operations

**When to use:** When a liquid is removed and replaced by another multiple times.

**Worked example:** 40L milk, 4L removed, 3 times total. Final = $40 \times (1 - \frac{4}{40})^3 = 40 \times (0.9)^3 = 29.16$L.

---

## Solution Framework

**Step 1: Identify the type.** Determine if it is a simple mixture (Alligation) or a repeated replacement.
**Step 2: Standardize units.** Ensure all prices are per unit (e.g., calculate cost per litre if given for $1.5$ litres).
**Step 3: Apply formula.** Use the Alligation ratio formula or the Replacement decay formula.
**Step 4: Adjust for ratios.** If given a final ratio (e.g., $16:65$), convert it to a fraction of the total (e.g., $\frac{16}{16+65} = \frac{16}{81}$) before solving for the unknown.

---

## Shortcut Tricks

* **Trick:** For repeated replacement, the ratio of "Remaining Liquid : Total Volume" is always $(1 - \frac{x}{V})^n$.
* **Why it works:** It bypasses calculating the water volume separately.
* **When to use:** When the question asks for the final concentration or the original volume.
* **Example:** If $1 - \frac{8}{x} = \frac{2}{3}$, then $\frac{8}{x} = \frac{1}{3}$, so $x = 24$.

---

## Common Mistakes

* **Mistake:** Treating water as having a cost. **Fix:** Always use 0 for the cost of water.
* **Mistake:** Miscounting $n$. **Fix:** If a process is done "3 more times" after the first, $n=4$.
* **Mistake:** Using the ratio of water to milk instead of milk to total. **Fix:** Always use the ratio of the *remaining* substance to the *total* volume in the decay formula.

---

## Worked Example (Step-by-Step)

**Question:** A container contains 40 litres of milk. 4 litres are taken out and replaced by water. This is repeated two more times. How much milk is left?

**Solution:**
1. **Identify:** Repeated replacement. Initial = 40, Removed = 4, $n = 1 + 2 = 3$.
2. **Formula:** $\text{Final} = 40 \times (1 - \frac{4}{40})^3$.
3. **Calculate:** $40 \times (1 - 0.1)^3 = 40 \times (0.9)^3 = 40 \times 0.729 = 29.16$.
**Answer:** 29.16 litres.

---

## Similar Patterns
* **Weighted Averages:** Similar to Alligation but involves finding the mean price rather than the ratio.

---

## Revision Summary
* **Key formula:** $\text{Final} = \text{Initial} \times (1 - \frac{x}{V})^n$.
* **Spot it by:** "Replaced by," "repeated," or "in what ratio."
* **First move:** Calculate unit cost or identify $n$.
* **Fastest method:** Use the ratio of remaining liquid to total volume.
* **Biggest trap:** Forgetting that water cost is 0 or miscounting $n$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Weighted Average** — The average value of a mixture based on the quantity and price of each component.
* **Exponents** — Understanding $(a/b)^n$ for repeated operations.

### Formulas You Must Know First
* **Cost Price per Unit** = $\frac{\text{Total Cost}}{\text{Total Quantity}}$.

### Terms Used In This Pattern
* **Alligation** — A method to find the ratio of two ingredients to reach a mean price.
* **Mean Price** — The target price of the final mixture.