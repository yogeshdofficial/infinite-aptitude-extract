# Compound Interest Calculation

## Overview
These questions ask you to calculate the final amount or the interest earned on a principal sum over a specific period. The central idea is that interest is added to the principal at the end of each compounding period, making the principal grow over time.

---

## Recognition Clues
* **Keywords:** "Compound interest," "compounded annually/half-yearly/quarterly," "accrued."
* **Given:** Principal ($P$), Rate ($R$), Time ($T$), and compounding frequency.
* **Asked:** Compound Interest (C.I.) or Total Amount ($A$).
* **Time format:** Look for years, months, or fractions of years (e.g., "2 years 4 months").

---

## Key Formulas

### [Standard Compound Amount]
$$
A = P \times \left(1 + \frac{R}{100}\right)^n
$$
**Variables:** $P$ = Principal, $R$ = Annual Rate, $n$ = Number of years.
**When to use:** Compounding annually for a whole number of years.
**Example:** $P=7800, R=5, n=3 \implies A = 7800 \times (1.05)^3 = 9029.475$.

### [Compounding Frequency Adjustment]
$$
A = P \times \left(1 + \frac{R/k}{100}\right)^{n \times k}
$$
**Variables:** $k$ = frequency per year (2 for half-yearly, 4 for quarterly).
**When to use:** When interest is compounded more than once a year.
**Example:** $P=10000, R=4, T=2, k=2 \implies A = 10000 \times (1 + \frac{2}{100})^4 = 10824.32$.

### [Fractional Time]
$$
A = P \times \left(1 + \frac{R}{100}\right)^n \times \left(1 + \frac{f \times R}{100}\right)
$$
**Variables:** $n$ = full years, $f$ = fractional part of the year.
**When to use:** Time is given as "X years Y months."
**Example:** $P=8000, R=15, n=2, f=1/3 \implies A = 8000 \times (1.15)^2 \times (1 + \frac{1/3 \times 15}{100}) = 11109$.

---

## Solution Framework
1. **Identify $P, R, T$:** Extract values and convert time to years (e.g., 4 months = $1/3$ year).
2. **Adjust for Frequency:** If half-yearly, divide $R$ by 2 and multiply $T$ by 2. If quarterly, divide $R$ by 4 and multiply $T$ by 4.
3. **Calculate Amount ($A$):** Apply the appropriate formula to find the total accumulated value.
4. **Find Interest (C.I.):** Subtract the original principal from the amount ($C.I. = A - P$).

---

## Shortcut Tricks
* **Trick:** For 2 years, $C.I. = P \times (\frac{2R}{100} + \frac{R^2}{10000})$.
* **Why it works:** This is the expansion of $(1 + R/100)^2 - 1$.
* **When to use:** Only for 2-year problems to avoid long multiplication.
* **Example:** $P=1000, R=10\% \implies C.I. = 1000 \times (0.20 + 0.01) = 210$.

---

## Common Mistakes
* **Mistake:** Using Simple Interest formula ($P \times R \times T / 100$). **Fix:** Always use the exponential formula for compound interest.
* **Mistake:** Treating 4 months as 0.4 years. **Fix:** Always convert months to years as a fraction ($months/12$).
* **Mistake:** Forgetting to subtract $P$ at the end. **Fix:** Remember $A$ is the total, $C.I.$ is only the interest.

---

## Worked Example (Step-by-Step)

**Question:** Find the compound interest on ₹ 8000 at 15% per annum for 2 years 4 months, compounded annually.

**Solution:**
1. **Identify:** $P=8000, R=15, T=2$ years 4 months.
2. **Convert Time:** $T = 2 + 4/12 = 2 + 1/3$ years.
3. **Calculate Amount:** $A = 8000 \times (1 + 15/100)^2 \times (1 + (1/3 \times 15)/100)$.
   $A = 8000 \times (23/20)^2 \times (1 + 5/100) = 8000 \times (529/400) \times (21/20) = 11109$.
4. **Find C.I.:** $C.I. = 11109 - 8000 = 3109$.

**Answer:** ₹ 3109.

---

## Similar Patterns
**Simple Interest:** Distinguish by the keyword "Simple Interest" vs "Compound Interest"; Simple Interest does not add interest to the principal.

---

## Revision Summary
* **Key formula:** $A = P(1 + R/100)^n$.
* **Spot it by:** "Compounded" keyword and time duration.
* **First move:** Convert time to years and adjust $R$ for frequency.
* **Fastest method:** Use the fractional multiplier method for manual calculation.
* **Biggest trap:** Confusing months with decimals (e.g., 4 months $\neq$ 0.4 years).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Percentages** — Expressing rates as fractions (e.g., $5\% = 1/20$).
* **Exponents** — Calculating powers like $(21/20)^3$.

### Formulas You Must Know First
* **Fractional conversion:** $Time (years) = \frac{Months}{12}$.

### Terms Used In This Pattern
* **Principal ($P$):** The initial amount borrowed or invested.
* **Rate ($R$):** The percentage of interest charged per year.
* **Amount ($A$):** The total sum of principal plus interest.