# Greatest Common Measure (HCF)

## Overview
This pattern involves finding the largest number that can divide a set of values or measure them exactly. The central idea is to calculate the **Highest Common Factor (HCF)**, adjusting the input numbers first if remainders or unit differences are involved.

---

## Recognition Clues
* **Keywords:** "Greatest possible," "largest number," "measure exactly," "lowest terms."
* **Given:** A set of numbers, lengths with different units, or numbers that leave specific remainders.
* **Asked:** The largest divisor, the maximum length of a measuring tool, or the simplified form of a fraction.

---

## Key Formulas

### [HCF of Numbers with Remainders]
$$
\text{Required Number} = \text{HCF of } (N_1 - R_1), (N_2 - R_2), \dots
$$
**Variables:** $N$ = original numbers, $R$ = respective remainders.
**When to use:** When the question asks for the greatest number that divides $N_1, N_2$ leaving remainders $R_1, R_2$.
**Example:** For 1657 and 2037 with remainders 6 and 5: HCF of $(1657-6)=1651$ and $(2037-5)=2032$ is 127.

### [HCF of Numbers with Same Remainder]
$$
\text{Required Number} = \text{HCF of } (b-a), (c-b), (c-a)
$$
**Variables:** $a, b, c$ = given numbers (sorted $a < b < c$).
**When to use:** When the question asks for the largest number that divides $a, b, c$ leaving the *same* remainder.
**Example:** For 62, 132, 237: HCF of $(132-62)=70, (237-132)=105, (237-62)=175$ is 35.

---

## Solution Framework
**Step 1: Standardize** — Convert all units to the smallest unit (e.g., m to cm) or subtract remainders if provided.
**Step 2: Difference/Reduction** — If finding a common divisor for "same remainder" cases, calculate the differences between numbers.
**Step 3: Apply Euclidean Algorithm** — Divide the larger number by the smaller, then the divisor by the remainder until the remainder is 0.
**Step 4: Identify HCF** — The last non-zero divisor is your HCF.
**Step 5: Final Operation** — If simplifying a fraction, divide both numerator and denominator by the HCF.

---

## Shortcut Tricks
* **Trick:** For two numbers, the HCF must be a factor of their difference.
* **Why it works:** If $d$ divides $A$ and $B$, it must divide $(A-B)$.
* **When to use:** When numbers are close together or large.
* **Example:** For 391 and 667, difference is 276. Factors of 276 include 23. $391/23 = 17$.

---

## Common Mistakes
* **Mistake:** Calculating LCM instead of HCF. **Fix:** Remember "Greatest" = HCF, "Least" = LCM.
* **Mistake:** Forgetting to subtract remainders. **Fix:** Always subtract $R$ from $N$ before finding HCF.
* **Mistake:** Using only one difference for "same remainder" problems. **Fix:** Calculate all pairwise differences $(b-a), (c-b), (c-a)$.

---

## Worked Example (Step-by-Step)

**Question:** Find the greatest number which on dividing 1657 and 2037 leaves remainders 6 and 5 respectively.

**Solution:**
1. **Standardize:** Subtract remainders: $1657 - 6 = 1651$ and $2037 - 5 = 2032$.
2. **Apply Euclidean Algorithm:**
   - $2032 \div 1651 = 1$ remainder $381$.
   - $1651 \div 381 = 4$ remainder $127$.
   - $381 \div 127 = 3$ remainder $0$.
3. **Identify HCF:** The last divisor is 127.

**Answer:** 127

---

## Similar Patterns
**LCM Patterns:** Distinguished by keywords like "least," "smallest," "when will they meet again," or "divisible by." If the question asks for a number *larger* than the given values, it is an LCM problem.

---

## Revision Summary
* **Key formula:** HCF of $(N_1-R_1, N_2-R_2)$.
* **Spot it by:** "Greatest number" or "measure exactly."
* **First move:** Subtract remainders or convert units.
* **Fastest method:** Euclidean division (successive division).
* **Biggest trap:** Forgetting to subtract remainders before finding HCF.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Factors** — Numbers that divide another number exactly.
* **Euclidean Algorithm** — The process of repeated division to find the HCF.
* **Prime Factorization** — Breaking a number into its prime components (e.g., $12 = 2^2 \times 3$).

### Terms Used In This Pattern
* **HCF (Highest Common Factor)** — The largest number that divides all given numbers without a remainder.
* **Remainder** — The amount left over after division.