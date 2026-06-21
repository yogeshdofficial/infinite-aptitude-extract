# Rent Sharing: Equivalent Units

## Overview
This pattern involves sharing rent or expenses based on the "consumption" of resources by different entities over varying time periods. The central idea is to convert all heterogeneous units (horses, cows, sheep) into a single common unit to calculate the total "equivalent consumption" for each person.

---

## Recognition Clues
* **Keywords:** "Rent", "Field", "Put on it", "Eat as much as".
* **Given:** Multiple types of entities (e.g., horses, cows, sheep), their quantities, time durations, and consumption equivalence ratios.
* **Asked:** The fractional share of rent or total cost to be paid by one party.

---

## Important Formulas

### [Equivalent Consumption Ratio]
$$
\text{Total Consumption} = \sum (\text{Quantity} \times \text{Equivalence Factor} \times \text{Time})
$$

*Meaning:* The total resource usage of a person is the sum of their individual holdings converted to a base unit and multiplied by the duration.

*Use when:* Calculating the ratio of shares between two or more parties.

---

## Solution Framework
1. **Select a Base Unit:** Choose one entity type (e.g., sheep) as the common denominator.
2. **Convert All Entities:** Use the given equivalence ratios to express all other entities in terms of the base unit.
3. **Calculate Weighted Totals:** Multiply the converted quantity by the time duration for every item.
4. **Sum for Each Person:** Add the weighted totals for each individual to get their total "equivalent units."
5. **Find the Ratio:** Simplify the ratio of the total equivalent units of the parties.
6. **Determine Share:** Convert the ratio into a fraction of the total rent.

---

## Shortcut Tricks
* **Simplify Ratios Early:** Convert all entities to the base unit immediately before multiplying by time to keep numbers small.
* **Avoid Large Multiplications:** If all terms share a common factor, cancel it out across the entire ratio before summing.

---

## Common Mistakes
* **Time Mismatch:** Forgetting to multiply by the duration for *every* group of animals.
    * *Reason:* Treating it like a simple ratio problem rather than a compound partnership.
    * *Fix:* Always write out `(Quantity × Factor × Time)` for every entry.
* **Incorrect Conversion:** Using the reciprocal of the equivalence ratio.
    * *Reason:* Confusing "3 horses = 5 cows" with "1 horse = 3/5 cows."
    * *Fix:* Always write the conversion as an equation (e.g., $1 \text{ horse} = \frac{5}{3} \text{ cows}$) before substituting.

---

## Similar Patterns
This is a variation of the **Compound Partnership** pattern. While standard partnerships use money as the unit, this pattern uses "consumption units" as the investment.

---

## Revision Summary
**Key formula:** $\text{Total} = \sum (\text{Quantity} \times \text{Factor} \times \text{Time})$.
**Spot it by:** Multiple animal/resource types with different consumption rates and time periods.
**Fastest method:** Convert all to a single base unit before calculating the weighted sum.
**Biggest trap:** Forgetting to multiply by the time duration for each specific group.