# Time Equivalence

## Overview
This pattern involves finding the time period when the Banker's Discount (B.D.) on one sum is equal to the True Discount (T.D.) on a different sum at the same rate. The central idea is that if B.D. on $P_1$ equals T.D. on $P_2$, then $P_1$ is the Present Worth (P.W.) of $P_2$.

---

## Recognition Clues
* **Keywords:** "Banker's discount on [Amount A]... is equal to the true discount on [Amount B]".
* **Given:** Two different amounts, a common rate of interest, and a common time period.
* **Asked:** The time period ($T$).
* **Scan for:** Two distinct monetary values and a percentage rate.

---

## Key Formulas

### [Time Calculation]
$$
T = \frac{100 \times (A_2 - A_1)}{R \times A_1}
$$

**Variables:**
- $T$ = Time in years
- $A_1$ = The amount on which B.D. is calculated (the smaller amount)
- $A_2$ = The amount on which T.D. is calculated (the larger amount)
- $R$ = Rate percent per annum

**When to use:** Whenever you are asked for the time given the equality of B.D. and T.D. on two different sums.

**Worked example:** Given B.D. on ₹ 1800 ($A_1$) and T.D. on ₹ 1872 ($A_2$) at 12% ($R$):
$T = \frac{100 \times (1872 - 1800)}{12 \times 1800} = \frac{100 \times 72}{21600} = \frac{7200}{21600} = \frac{1}{3}$ year.

---

## Solution Framework

**Step 1: Identify the Present Worth.** Recognize that the smaller amount is the Present Worth ($P.W.$) and the larger amount is the Amount ($A$).
**Step 2: Find the Interest.** Calculate the difference between the two amounts ($A - P.W.$); this difference is the Simple Interest ($S.I.$) on the $P.W.$
**Step 3: Apply S.I. Formula.** Use $S.I. = \frac{P \times R \times T}{100}$ where $P$ is the smaller amount.
**Step 4: Solve for T.** Isolate $T$ and convert the resulting fraction of a year into months by multiplying by 12.

---

## Shortcut Tricks

**Trick:** $T = \frac{\text{Difference in Amounts} \times 100}{\text{Smaller Amount} \times \text{Rate}}$
**Why it works:** It is a direct algebraic rearrangement of the Simple Interest formula where the interest is the difference between the two sums.
**When to use:** Always, as it bypasses the need to write out the full S.I. equation.
**Example:** For Q9: $\frac{(1680 - 1600) \times 100}{1600 \times 15} = \frac{8000}{24000} = \frac{1}{3}$ year (4 months).

---

## Common Mistakes

* **Mistake:** Calculating interest on the larger sum.
    * **Why it happens:** Confusing the "Amount" with the "Principal" in the S.I. formula.
    * **Fix:** Always use the smaller sum (the Present Worth) as the Principal.
* **Mistake:** Forgetting to convert years to months.
    * **Why it happens:** Stopping at the fraction (e.g., $1/3$) without checking the required units.
    * **Fix:** Always multiply the final fraction by 12 to get the answer in months.

---

## Worked Example (Step-by-Step)

**Question:** The banker’s discount on ₹ 1600 at 15% per annum is the same as true discount on ₹ 1680 for the same time and at the same rate. The time is?

**Solution:**
1. **Identify:** $P.W. = 1600$, $Amount = 1680$, $Rate = 15\%$.
2. **Find Interest:** $1680 - 1600 = 80$.
3. **Apply Formula:** $80 = \frac{1600 \times 15 \times T}{100}$.
4. **Solve:** $80 = 16 \times 15 \times T \Rightarrow 80 = 240 \times T$.
5. **Calculate:** $T = \frac{80}{240} = \frac{1}{3}$ year.
6. **Convert:** $\frac{1}{3} \times 12 = 4$ months.

**Answer:** 4 months.

---

## Similar Patterns
**Banker's Gain Problems:** These involve finding the difference between B.D. and T.D. on the *same* sum; distinguish by checking if the question provides one sum or two.

---

## Revision Summary
* **Key formula:** $T = \frac{100 \times (A_2 - A_1)}{R \times A_1}$
* **Spot it by:** Two different amounts given with a single rate.
* **First move:** Subtract the smaller amount from the larger to find the interest.
* **Fastest method:** Use the shortcut formula directly.
* **Biggest trap:** Using the larger amount as the Principal in the S.I. formula.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest ($S.I.$):** Interest calculated only on the principal amount `(P * R * T) / 100`.
* **Present Worth ($P.W.$):** The original sum of money that would grow to a specific amount at a given rate and time.

### Formulas You Must Know First
$$
S.I. = \frac{P \times R \times T}{100}
$$
**What it means:** The standard formula for calculating interest over time.
**Example:** $S.I. = \frac{1000 \times 10 \times 1}{100} = 100$.

### Terms Used In This Pattern
* **Banker's Discount (B.D.):** Simple interest on the face value of a bill.
* **True Discount (T.D.):** Simple interest on the present worth of a bill.