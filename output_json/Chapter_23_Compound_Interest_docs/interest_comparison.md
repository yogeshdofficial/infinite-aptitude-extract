# Interest Comparison

## Overview
This pattern involves comparing Simple Interest (S.I.) and Compound Interest (C.I.) for the same principal, rate, and time. The central idea is to use the S.I. formula to extract missing variables (usually Principal or Rate) and then apply the C.I. formula to find the required value.

---

## Recognition Clues
* **Keywords:** "Simple interest accrued," "compound interest accrued," "same amount," "same rate," "same period."
* **Given:** S.I. value, time, and rate (or principal).
* **Asked:** C.I. value, or the difference between C.I. and S.I.
* **Scan for:** Questions that provide S.I. data to force you to calculate the Principal or Rate before you can solve for C.I.

---

## Key Formulas

### Simple Interest
$$
S.I. = \frac{P \times R \times T}{100}
$$
**Variables:** $P$ = Principal, $R$ = Rate %, $T$ = Time in years.
**When to use:** To find $P$ or $R$ when $S.I.$ is given.

### Compound Interest
$$
C.I. = P \left[ \left(1 + \frac{R}{100}\right)^T - 1 \right]
$$
**Variables:** $P$ = Principal, $R$ = Rate %, $T$ = Time in years.
**When to use:** To calculate the interest earned over a period with compounding.

---

## Solution Framework

1. **Step 1: Extract Variables:** Identify $P, R, T,$ and $S.I.$ from the question.
2. **Step 2: Solve for Missing Variable:** Use the $S.I.$ formula to find the unknown $P$ or $R$.
3. **Step 3: Apply C.I. Formula:** Use the found $P$ and $R$ in the $C.I.$ formula for the specified time.
4. **Step 4: Final Calculation:** Compute the result and ensure the units (currency) match the question.

---

## Shortcut Tricks
**Trick:** For 2 years, $C.I. - S.I. = P \times (\frac{R}{100})^2$.
**Why it works:** It isolates the interest earned on the interest of the first year.
**When to use:** Only when the time period is exactly 2 years.
**Example:** If $P=1000, R=10\%$, $C.I. - S.I. = 1000 \times (0.1)^2 = 10$.

---

## Common Mistakes
* **Mistake:** Assuming $R$ for $S.I.$ is different from $R$ for $C.I.$
    * **Fix:** The question usually states "same rate," so use the same value.
* **Mistake:** Using the $S.I.$ formula for $C.I.$ calculations.
    * **Fix:** Always use the exponential formula $A = P(1+R/100)^T$ for $C.I.$
* **Mistake:** Forgetting to subtract $P$ from the Amount to get $C.I.$
    * **Fix:** Remember $C.I. = Amount - Principal$.

---

## Worked Example (Step-by-Step)

**Question:** The simple interest accrued on an amount of ₹ 40000 at the end of four years is ₹ 24000. What would be the compound interest accrued on the same amount at the same rate in the same period?

**Solution:**
1. **Extract:** $P = 40000, T = 4, S.I. = 24000$.
2. **Find Rate:** $24000 = \frac{40000 \times R \times 4}{100} \implies 24000 = 1600R \implies R = 15\%$.
3. **Calculate C.I.:** $C.I. = 40000 \times [(1 + \frac{15}{100})^4 - 1]$.
4. **Compute:** $40000 \times [(\frac{23}{20})^4 - 1] = 40000 \times [\frac{279841}{160000} - 1] = 40000 \times \frac{119841}{160000} = 29960.25$.

**Answer:** ₹ 29960.25

---

## Similar Patterns
**Difference Problems:** If the question asks for the *difference* between C.I. and S.I., use the specific difference formula (e.g., $P(R/100)^2$ for 2 years) rather than calculating both separately to save time.

---

## Revision Summary
* **Key formula:** $S.I. = \frac{PRT}{100}$ and $C.I. = P(1+\frac{R}{100})^T - P$.
* **Spot it by:** "Same amount," "same rate," and "same period" keywords.
* **First move:** Calculate the missing $P$ or $R$ using the $S.I.$ data.
* **Fastest method:** Use the $S.I.$ formula to find the rate, then apply the $C.I.$ formula.
* **Biggest trap:** Forgetting to subtract the principal from the final amount.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentage:** Understanding $R\%$ as $\frac{R}{100}$.
* **Algebraic Rearrangement:** Ability to solve $S.I. = \frac{PRT}{100}$ for any single variable.

### Formulas You Must Know First
* **Amount:** $A = P + I$ (where $I$ is interest).

### Terms Used In This Pattern
* **Principal ($P$):** The initial sum of money invested.
* **Rate ($R$):** The percentage of interest charged per year.
* **Time ($T$):** The duration of the investment in years.