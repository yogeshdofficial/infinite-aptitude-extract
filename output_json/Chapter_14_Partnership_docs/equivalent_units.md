# Equivalent Units (Heterogeneous Partnership)

## Overview
This pattern involves partners contributing different types of resources (e.g., horses, cows, sheep) for varying durations. The central idea is to convert all heterogeneous units into a single "base unit" (e.g., all into sheep) to calculate the total effective investment ratio.

---

## Recognition Clues
* **Keywords:** "A puts X [units] for Y months", "B puts P [units] for Q months", "X [units] eat as much as Y [units]".
* **Given:** Conversion rates between different resource types and their respective time durations.
* **Asked:** The share of profit or rent for a specific person.
* **Visual cue:** Multiple resource types (horses, cows, sheep) mixed with time periods.

---

## Important Formulas

### [Conversion Ratio]
$$
1 \text{ Unit}_A = \left( \frac{\text{Value}_B}{\text{Value}_A} \right) \text{ Unit}_B
$$
*Meaning:* Expressing one resource type in terms of another using the given consumption/value equivalence.
*Use when:* You need to normalize all inputs to a single common unit.

### [Effective Investment]
$$
\text{Effective Investment} = (\text{Quantity} \times \text{Conversion Factor} \times \text{Time})
$$
*Meaning:* The total "work" or "consumption" done by a resource over a specific duration.
*Use when:* Calculating the ratio of shares for partners with mixed resources.

---

## Solution Framework
1. Pick one resource type as the "Base Unit" (e.g., convert everything to sheep).
2. Convert all other resource quantities into this Base Unit using the given equivalence ratios.
3. Calculate the "Effective Investment" for each partner by summing $(\text{Quantity}_{\text{base}} \times \text{Time})$ for all their assets.
4. Simplify the ratio of the total Effective Investments of all partners.
5. Calculate the required share using the simplified ratio.

---

## Shortcut Tricks
* **Common Denominator Elimination:** If all conversion factors result in fractions with the same denominator, ignore the denominator during the ratio calculation.
* **Why:** Ratios are scale-invariant; multiplying both sides of a ratio by the same constant does not change the final proportion.

---

## Common Mistakes
* **Time Neglect:** Forgetting to multiply the converted quantity by the time duration.
    * *Reason:* Focusing only on the conversion and ignoring the "partnership" aspect.
    * *Fix:* Always write $(\text{Quantity} \times \text{Conversion} \times \text{Time})$ as a single block before adding.
* **Incorrect Conversion Direction:** Dividing instead of multiplying when converting units.
    * *Reason:* Confusing the ratio of "value" with the ratio of "quantity".
    * *Fix:* Use the unitary method: if $3 \text{ horses} = 5 \text{ cows}$, then $1 \text{ horse} = \frac{5}{3} \text{ cows}$.

---

## Similar Patterns
This is a specialized version of "Compound Partnership." Distinguish it by the presence of **multiple resource types** (horses/cows) rather than just different capital amounts (money).

---

## Revision Summary
**Key formula:** $\text{Total Effective Units} = \sum (\text{Quantity} \times \text{Conversion} \times \text{Time})$.
**Spot it by:** Multiple resource types with specific consumption/value equivalence rates.
**Fastest method:** Convert all to the smallest unit first, then multiply by time.
**Biggest trap:** Forgetting to multiply by the time duration for every individual resource entry.