# Interest Comparison

## Overview
This pattern involves problems where both the True Discount (T.D.) and Simple Interest (S.I.) are provided for the same sum, time, and rate. The central idea is to use the specific relationship between these two values to isolate the principal sum before solving for the rate or time.

---

## Recognition Clues
* **Keywords:** "True discount," "Simple interest," "Same sum," "Same time," "Same rate."
* **Given:** Both T.D. and S.I. values are provided (or their difference).
* **Asked:** The principal sum, the rate percent, or the time.

---

## Key Formulas

### [Sum Calculation]
$$
\text{Sum} = \frac{\text{S.I.} \times \text{T.D.}}{\text{S.I.} - \text{T.D.}}
$$

**Variables:**
- $\text{S.I.}$ = Simple Interest
- $\text{T.D.}$ = True Discount

**When to use:** When you are given both the S.I. and T.D. and need to find the principal sum.

**Worked example:** Given S.I. = 375, T.D. = 250. 
$\text{Sum} = \frac{375 \times 250}{375 - 250} = \frac{93750}{125} = 750$.

### [Rate Calculation]
$$
R = \frac{\text{S.I.} \times 100}{P \times T}
$$

**Variables:**
- $R$ = Rate percent per annum
- $P$ = Present Worth (Sum - T.D.)
- $T$ = Time in years

**When to use:** After finding the Sum and Present Worth, use this to find the rate.

**Worked example:** Sum = 750, T.D. = 250, $T = 3$. $P = 750 - 250 = 500$.
$R = \frac{250 \times 100}{500 \times 3} = 16\frac{2}{3}\%$.

---

## Solution Framework

1. **Identify Values:** Extract S.I., T.D., and Time from the question.
2. **Calculate Sum:** Use the formula $\text{Sum} = \frac{\text{S.I.} \times \text{T.D.}}{\text{S.I.} - \text{T.D.}}$ to find the total amount due.
3. **Find Present Worth ($P$):** Subtract the T.D. from the Sum ($P = \text{Sum} - \text{T.D.}$).
4. **Solve for Unknown:** Use the standard S.I. formula ($\text{T.D.} = \frac{P \times R \times T}{100}$) to find the missing Rate or Time.

---

## Shortcut Tricks
* **Trick:** If given the difference between S.I. and T.D. ($D$), use $\text{Sum} = \frac{\text{S.I.} \times \text{T.D.}}{D}$.
* **Why it works:** Since $D = \text{S.I.} - \text{T.D.}$, this is just a rearrangement of the primary formula.
* **When to use:** When the question explicitly states "The difference between S.I. and T.D. is X."

---

## Common Mistakes
* **Mistake:** Using the "Sum" as the principal in the interest formula.
    * **Why it happens:** Confusing the amount due with the present worth.
    * **Fix:** Always use $P = \text{Sum} - \text{T.D.}$ for interest calculations.
* **Mistake:** Incorrectly converting time (e.g., months to years).
    * **Why it happens:** Forgetting that $T$ must be in years.
    * **Fix:** Always divide months by 12.

---

## Worked Example (Step-by-Step)

**Question:** The true discount on a certain sum of money due 3 years hence is ₹ 250 and the simple interest on the same sum for the same time and at the same rate is ₹ 375. Find the sum and the rate percent.

**Solution:**
1. **Identify:** S.I. = 375, T.D. = 250, $T = 3$.
2. **Calculate Sum:** $\text{Sum} = \frac{375 \times 250}{375 - 250} = \frac{93750}{125} = 750$.
3. **Find $P$:** $P = 750 - 250 = 500$.
4. **Solve for $R$:** $250 = \frac{500 \times R \times 3}{100} \Rightarrow 250 = 15R \Rightarrow R = \frac{250}{15} = 16\frac{2}{3}\%$.

**Answer:** Sum = ₹ 750, Rate = $16\frac{2}{3}\%$.

---

## Similar Patterns
* **Simple Interest/Compound Interest:** Distinguish by checking if the question mentions "True Discount" or "Present Worth"; if not, it is a standard interest problem.

---

## Revision Summary
* **Key formula:** $\text{Sum} = \frac{\text{S.I.} \times \text{T.D.}}{\text{S.I.} - \text{T.D.}}$
* **Spot it by:** Presence of both "True Discount" and "Simple Interest."
* **First move:** Calculate the Sum using the given S.I. and T.D.
* **Fastest method:** Use the difference formula if the difference is provided.
* **Biggest trap:** Using the Sum instead of Present Worth for interest calculations.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the principal amount: $\text{S.I.} = \frac{P \times R \times T}{100}$.
* **True Discount** — The interest on the Present Worth: $\text{T.D.} = \frac{P \times R \times T}{100}$.

### Formulas You Must Know First
* $\text{Amount} = P + \text{T.D.}$
* $\text{Present Worth} = \text{Amount} - \text{T.D.}$

### Terms Used In This Pattern
* **Sum Due:** The total amount to be paid at a future date.
* **Present Worth ($P$):** The amount that, if invested today, would grow to the Sum Due.