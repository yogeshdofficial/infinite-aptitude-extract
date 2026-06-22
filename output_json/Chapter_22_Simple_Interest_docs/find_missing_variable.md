# Find Missing Variable

## Overview
This pattern involves solving for an unknown variable (Principal, Rate, or Time) when the Simple Interest (S.I.) or Amount is provided. The central idea is to rearrange the standard S.I. formula to isolate the missing variable.

---

## Recognition Clues
* **Keywords:** "Find the sum," "At what rate," "In how many years," "amounts to."
* **Given:** Usually two of the three variables ($P, R, T$) and either the S.I. or the final Amount.
* **Asked:** The one variable not provided in the problem statement.
* **Variation:** Questions involving "doubling" or "fraction of the sum" imply $S.I. = P$ or $S.I. = \text{fraction} \times P$.

---

## Key Formulas

### [Rearranged S.I. Formula]
$$
P = \frac{100 \times S.I.}{R \times T}, \quad R = \frac{100 \times S.I.}{P \times T}, \quad T = \frac{100 \times S.I.}{P \times R}
$$
**Variables:** $P$ = Principal, $R$ = Rate, $T$ = Time, $S.I.$ = Simple Interest.
**When to use:** When $S.I.$ is explicitly given or can be derived from the Amount.
**Example:** If $S.I. = 208, P = 800, T = 2$, then $R = \frac{100 \times 208}{800 \times 2} = 13\%$.

### [Amount-Principal Relationship]
$$
\text{Amount} = P + S.I. = P \left(1 + \frac{RT}{100}\right)
$$
**When to use:** When the final Amount is given instead of the interest.
**Example:** Amount = 2502.50, $R = 13.5\%, T = 4$. $2502.50 = P(1 + \frac{13.5 \times 4}{100}) \implies P = \frac{2502.50}{1.54} = 1625$.

---

## Solution Framework
1. **Identify Variables:** List all given values ($P, R, T, S.I., \text{Amount}$) and mark the missing one.
2. **Derive S.I.:** If Amount is given, calculate $S.I. = \text{Amount} - P$. If "doubling" is mentioned, set $S.I. = P$.
3. **Handle Time/Rate:** Convert mixed fractions (e.g., $13\frac{1}{2}\%$) to improper fractions or decimals.
4. **Substitute:** Plug known values into the appropriate rearranged formula.
5. **Solve:** Isolate the variable and calculate the final value.

---

## Shortcut Tricks
* **Trick:** If $S.I.$ is a fraction of $P$ (e.g., $S.I. = \frac{3}{4}P$), ignore $P$ entirely.
* **Why it works:** $P$ cancels out on both sides of the equation $\frac{3}{4}P = \frac{P \times R \times T}{100}$.
* **Example:** $S.I. = \frac{3}{4}P, T = 12.5$. $\frac{3}{4} = \frac{R \times 12.5}{100} \implies R = 6\%$.

---

## Common Mistakes
* **Mistake:** Calculating interest on the Amount instead of the Principal.
* **Fix:** Always use $S.I. = \text{Amount} - P$ first.
* **Mistake:** Forgetting to convert time in months to years (divide by 12).
* **Fix:** Ensure $T$ is always in years before plugging into the formula.

---

## Worked Example (Step-by-Step)

**Question:** A sum of money amounts to ₹ 1008 in 2 years and to ₹ 1164 in $3\frac{1}{2}$ years. Find the sum.

**Solution:**
1. **Identify:** $A_1 = 1008 (T=2)$, $A_2 = 1164 (T=3.5)$.
2. **Difference:** $S.I.$ for $(3.5 - 2) = 1.5$ years is $1164 - 1008 = 156$.
3. **Unitary Method:** $S.I.$ for 2 years = $\frac{156}{1.5} \times 2 = 208$.
4. **Find P:** $P = \text{Amount} - S.I. = 1008 - 208 = 800$.

**Answer:** ₹ 800.

---

## Similar Patterns
* **Compound Interest:** Distinguish by the keyword "compounded annually/half-yearly"; if not mentioned, assume Simple Interest.

---

## Revision Summary
* **Key formula:** $S.I. = \frac{P \times R \times T}{100}$.
* **Spot it by:** Missing $P, R,$ or $T$ with $S.I.$ or Amount given.
* **First move:** Calculate $S.I.$ if only Amount is provided.
* **Fastest method:** Cancel $P$ if $S.I.$ is given as a fraction of $P$.
* **Biggest trap:** Using Amount instead of Principal in the denominator.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Fractions/Decimals:** Converting $13\frac{1}{2}$ to $13.5$ or $\frac{27}{2}$.
* **Algebraic Isolation:** Moving terms across the equals sign to solve for $x$.

### Formulas You Must Know First
$$
S.I. = \frac{P \times R \times T}{100}
$$
**What it means:** The basic definition of Simple Interest.

### Terms Used In This Pattern
* **Principal ($P$):** The original sum of money.
* **Amount ($A$):** The total sum after interest is added ($P + S.I.$).