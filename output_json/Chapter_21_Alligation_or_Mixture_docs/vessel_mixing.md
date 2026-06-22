# Vessel Mixing

## Overview
This pattern involves mixing two different mixtures (e.g., milk and water) to achieve a specific target concentration. The central idea is to convert all ratios into a single component's fraction (e.g., only milk) and use the **Rule of Alligation** to find the required mixing ratio.

---

## Recognition Clues
* **Keywords:** "In what ratio," "mixed to obtain," "new mixture," "vessels A and B."
* **Given:** Two vessels with different ratios of two liquids (e.g., 4:3 and 2:3).
* **Asked:** The ratio in which these two vessels must be mixed to get a target ratio in a third vessel.
* **Target:** A final ratio or percentage (e.g., "half milk and half water" or "69 3/13% milk").

---

## Key Formulas

### Rule of Alligation
$$
\text{Ratio} = |C_2 - C_{mean}| : |C_{mean} - C_1|
$$

**Variables:**
- $C_1$ = Concentration of the chosen liquid in Vessel A (as a fraction)
- $C_2$ = Concentration of the chosen liquid in Vessel B (as a fraction)
- $C_{mean}$ = Concentration of the chosen liquid in the final mixture (as a fraction)

**When to use:** Whenever you need to find the ratio of two mixtures to reach a target concentration.

**Worked example:** Vessel A (4:3 milk/water) $\rightarrow C_1 = \frac{4}{7}$. Vessel B (2:3) $\rightarrow C_2 = \frac{2}{5}$. Target (1:1) $\rightarrow C_{mean} = \frac{1}{2}$.
Ratio $= |\frac{1}{2} - \frac{2}{5}| : |\frac{4}{7} - \frac{1}{2}| = \frac{1}{10} : \frac{1}{14} = 7:5$.

---

## Solution Framework

**Step 1: Pick one liquid** — Choose either milk or spirit and stick to it for all calculations.
**Step 2: Convert to fractions** — Express the amount of that liquid as a fraction of the total parts (e.g., 4:3 becomes $\frac{4}{7}$).
**Step 3: Identify the mean** — Convert the target mixture ratio or percentage into a fraction of the same liquid.
**Step 4: Apply Alligation** — Subtract the mean from the individual concentrations and cross-subtract to find the ratio.
**Step 5: Simplify** — Multiply by the LCM of the denominators to get the final integer ratio.

---

## Shortcut Tricks
* **Trick:** If the target is "equal parts" (1:1), the ratio is simply $| \frac{1}{2} - C_2 | : | C_1 - \frac{1}{2} |$.
* **Why it works:** It is a specific case of the alligation formula where $C_{mean} = 0.5$.
* **Example:** For 4:7 and 2:5, ratio is $|\frac{1}{2} - \frac{2}{5}| : |\frac{4}{7} - \frac{1}{2}| = \frac{1}{10} : \frac{1}{14} = 7:5$.

---

## Common Mistakes
* **Mistake:** Using the ratio of the *other* liquid for one vessel and the *chosen* liquid for another. **Fix:** Always calculate the fraction for the same liquid across all three values.
* **Mistake:** Forgetting to convert percentages to fractions. **Fix:** Always convert $X\%$ to $\frac{X}{100}$ before starting alligation.
* **Mistake:** Inverting the final ratio. **Fix:** Remember the ratio is (Difference from $C_2$) : (Difference from $C_1$).

---

## Worked Example (Step-by-Step)

**Question:** Two vessels A and B contain spirit and water in the ratio 5:2 and 7:6. Find the ratio to obtain a mixture in C with spirit and water in the ratio 8:5.

**Solution:**
1. **Pick Liquid:** Spirit.
2. **Fractions:** Vessel A = $\frac{5}{7}$, Vessel B = $\frac{7}{13}$, Target = $\frac{8}{13}$.
3. **Alligation:**
   - Difference 1: $|\frac{8}{13} - \frac{7}{13}| = \frac{1}{13}$
   - Difference 2: $|\frac{5}{7} - \frac{8}{13}| = \frac{65-56}{91} = \frac{9}{91}$
4. **Ratio:** $\frac{1}{13} : \frac{9}{91}$.
5. **Simplify:** Multiply by 91 $\rightarrow (\frac{1}{13} \times 91) : (\frac{9}{91} \times 91) = 7 : 9$.

**Answer:** 7:9

---

## Similar Patterns
**Replacement/Removal:** If the question involves taking out a quantity and replacing it with water, use the formula $1 - (\frac{y}{x})^n$ instead of alligation.

---

## Revision Summary
* **Key formula:** $|C_2 - C_{mean}| : |C_{mean} - C_1|$.
* **Spot it by:** Two ratios given, one target ratio asked.
* **First move:** Convert all ratios to fractions of the *same* liquid.
* **Fastest method:** Alligation cross-subtraction.
* **Biggest trap:** Mixing up the order of subtraction or using different liquids.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractional Concentration** — The part of the whole, calculated as $\frac{\text{Part}}{\text{Total Parts}}$.
* **LCM (Least Common Multiple)** — Used to clear denominators when simplifying ratios.

### Formulas You Must Know First
* **Percentage to Fraction:** $X\% = \frac{X}{100}$.

### Terms Used In This Pattern
* **Alligation** — A method to find the ratio of two ingredients to reach a mean value.
* **Mean Price/Concentration** — The target value of the final mixture.