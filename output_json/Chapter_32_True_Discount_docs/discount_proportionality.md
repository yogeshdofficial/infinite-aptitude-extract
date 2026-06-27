# Discount Proportionality

## Overview
This pattern involves finding the True Discount (T.D.) on a sum when the time period changes, while the rate and sum remain constant. The central idea is that the True Discount is equivalent to the Simple Interest (S.I.) on the Present Worth (P.W.), and both are directly proportional to the time period.

---

## Recognition Clues
* **Keywords:** "True discount," "due after a certain time," "double the time," "half the time."
* **Given:** A specific T.D. on a specific Amount for a specific Time.
* **Asked:** The new T.D. on the same Amount for a different Time (e.g., double or half).
* **Constraint:** The rate of interest ($R$) remains constant.

---

## Key Formulas

### [True Discount Relationship]
$$
\text{T.D.} = \frac{\text{Amount} \times R \times T}{100 + RT}
$$

**Variables:**
- $\text{T.D.}$ = True Discount
- $\text{Amount}$ = The sum due at the end of the period
- $R$ = Rate of interest per annum
- $T$ = Time in years

**When to use:** When you need to calculate the T.D. directly or verify the relationship between variables.

**Worked example:** For Q8, Amount = 110, T.D. = 10. $10 = \frac{110 \times RT}{100 + RT} \implies 1000 + 10RT = 110RT \implies 100RT = 1000 \implies RT = 10$.

---

## Solution Framework

1. **Find Present Worth (P.W.):** Calculate $\text{P.W.} = \text{Amount} - \text{T.D.}$ because T.D. is the interest on the P.W.
2. **Identify Interest:** Recognize that the given T.D. is the S.I. on the P.W. for the original time.
3. **Adjust for Time:** Calculate the new S.I. by multiplying the original T.D. by the ratio of the new time to the old time.
4. **Find New T.D.:** Use the proportionality of T.D. to Amount to find the final answer: $\text{New T.D.} = \frac{\text{New S.I.}}{\text{P.W.} + \text{New S.I.}} \times \text{Amount}$.

---

## Shortcut Tricks

* **Trick:** If the time changes by factor $k$, the new T.D. is not simply $k \times \text{T.D.}$, but rather the S.I. on the P.W. adjusted for the new time, then re-calculated as a discount on the original Amount.
* **Why it works:** T.D. is calculated on the Amount, while S.I. is calculated on the P.W.; the denominator $(100+RT)$ changes as $T$ changes.
* **When to use it:** Always use this when the time is scaled (doubled/halved).

---

## Common Mistakes

* **Mistake:** Assuming the discount simply doubles when time doubles.
    * **Why it happens:** Confusing T.D. with Simple Interest.
    * **Fix:** Always calculate the P.W. first and adjust the interest on that P.W.
* **Mistake:** Calculating interest on the Amount instead of the P.W.
    * **Why it happens:** Forgetting that T.D. is interest on the P.W.
    * **Fix:** Always subtract T.D. from Amount to get P.W. before applying time changes.

---

## Worked Example (Step-by-Step)

**Question:** ₹ 20 is the true discount on ₹ 260 due after a certain time. What will be the true discount on the same sum due after half of the former time?

**Solution:**
1. **Find P.W.:** $\text{P.W.} = 260 - 20 = 240$.
2. **Identify Interest:** The T.D. of ₹ 20 is the S.I. on ₹ 240 for time $T$.
3. **Adjust for Time:** For time $\frac{T}{2}$, the new S.I. is $\frac{20}{2} = 10$.
4. **Find New T.D.:** The new T.D. on the new P.W. (240) is 10. The new Amount is $240 + 10 = 250$.
5. **Proportionality:** We need the T.D. on the original amount of 260. $\text{T.D.} = \frac{10}{250} \times 260 = 10.40$.

**Answer:** ₹ 10.40

---

## Similar Patterns

**Simple Interest:** Distinguished by the fact that S.I. is calculated on the Principal (P), whereas T.D. is calculated on the Amount (A).

---

## Revision Summary

* **Key formula:** $\text{T.D.} = \frac{\text{Amount} \times R \times T}{100 + RT}$
* **Spot it by:** "True discount" and "time changes" for the same sum.
* **First move:** Calculate $\text{P.W.} = \text{Amount} - \text{T.D.}$
* **Fastest method:** Adjust the S.I. on the P.W. for the new time, then convert back to T.D.
* **Biggest trap:** Assuming T.D. is directly proportional to time (it is not).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Present Worth (P.W.)** — The original sum that, when interest is added, becomes the final amount due.
* **True Discount (T.D.)** — The difference between the Amount due and the Present Worth.

### Formulas You Must Know First
$$
\text{Amount} = \text{P.W.} + \text{T.D.}
$$
**What it means:** The total sum due is the sum of the principal and the interest earned on it.

### Terms Used In This Pattern
* **Bill:** The document representing the debt or sum due.
* **Due:** The future date when the payment must be made.