# Present Worth

## Overview
These questions involve calculating the value of a future debt if paid today, accounting for interest. The central idea is that the "Amount" due is the sum of the "Present Worth" (the principal) and the "True Discount" (the interest earned on that principal).

---

## Recognition Clues
* **Keywords:** "Present worth," "due X years hence," "true discount," "bill due."
* **Given:** Future amount, time period, and rate of interest.
* **Asked:** Present worth (P.W.), True Discount (T.D.), or the time/rate.
* **Timeframe:** Always check if time is in months (convert to years by dividing by 12).

---

## Key Formulas

### Present Worth
$$
\text{P.W.} = \frac{100 \times \text{Amount}}{100 + (R \times T)}
$$
**Variables:** $R$ = Rate %, $T$ = Time in years.
**When to use:** When you have the future amount and need the current value.
**Example:** Amount = 930, R = 8%, T = 3. $\text{P.W.} = \frac{100 \times 930}{100 + (8 \times 3)} = \frac{93000}{124} = 750$.

### True Discount
$$
\text{T.D.} = \text{Amount} - \text{P.W.} \quad \text{OR} \quad \text{T.D.} = \frac{\text{P.W.} \times R \times T}{100}
$$
**When to use:** When you need the interest component of the future sum.
**Example:** Amount = 930, P.W. = 750. $\text{T.D.} = 930 - 750 = 180$.

---

## Solution Framework
1. **Convert Time:** Ensure time $T$ is in years (e.g., 9 months = $9/12 = 3/4$ years).
2. **Identify Knowns:** List Amount, Rate, and Time.
3. **Calculate P.W.:** Use the formula $\text{P.W.} = \frac{100 \times \text{Amount}}{100 + RT}$.
4. **Calculate T.D.:** Subtract P.W. from the Amount if needed.
5. **Solve for Unknowns:** If $T$ or $R$ is missing, substitute knowns into the T.D. formula and solve the algebraic equation.

---

## Shortcut Tricks
* **Trick:** $\text{T.D.} = \frac{\text{Amount} \times R \times T}{100 + (R \times T)}$.
* **Why it works:** It combines the P.W. formula and the T.D. definition into one step.
* **When to use:** When you are given the Amount and asked for the True Discount directly.
* **Example:** Amount = 930, R = 8%, T = 3. $\text{T.D.} = \frac{930 \times 8 \times 3}{100 + 24} = \frac{22320}{124} = 180$.

---

## Common Mistakes
* **Mistake:** Calculating Simple Interest (S.I.) on the Amount instead of the P.W.
* **Why it happens:** Confusing "True Discount" with "Banker's Discount" or standard S.I.
* **Fix:** Always remember T.D. is interest on P.W., not on the total Amount.
* **Mistake:** Forgetting to convert months to years.
* **Fix:** Always divide months by 12 before plugging into the formula.

---

## Worked Example (Step-by-Step)

**Question:** The true discount on a bill due 9 months hence at 16% per annum is ₹ 189. The amount of the bill is?

**Solution:**
1. **Convert Time:** $T = 9/12 = 3/4$ years.
2. **Set up Equation:** Let P.W. be $x$. $\text{T.D.} = \frac{x \times R \times T}{100} \Rightarrow 189 = \frac{x \times 16 \times (3/4)}{100}$.
3. **Solve for P.W.:** $189 = \frac{x \times 12}{100} \Rightarrow x = \frac{189 \times 100}{12} = 1575$.
4. **Find Amount:** $\text{Amount} = \text{P.W.} + \text{T.D.} = 1575 + 189 = 1764$.

**Answer:** ₹ 1764.

---

## Similar Patterns
**Simple Interest:** Distinguish by the fact that S.I. is calculated on the *Principal* (present value), whereas True Discount is calculated on the *Present Worth* to reach a *Future Amount*.

---

## Revision Summary
* **Key formula:** $\text{P.W.} = \frac{100 \times \text{Amount}}{100 + RT}$.
* **Spot it by:** Keywords "True Discount" or "Due X years hence."
* **First move:** Convert time to years.
* **Fastest method:** Use the combined T.D. formula if Amount is given.
* **Biggest trap:** Calculating interest on the future amount instead of the P.W.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the principal amount: $S.I. = \frac{P \times R \times T}{100}$.
* **Algebraic Manipulation** — Ability to solve for $x$ in equations like $A = \frac{B}{C+Dx}$.

### Formulas You Must Know First
* $S.I. = \frac{P \times R \times T}{100}$ (Standard interest formula).

### Terms Used In This Pattern
* **Present Worth (P.W.)** — The value of a future sum if paid today.
* **True Discount (T.D.)** — The difference between the future amount and the present worth.
* **Sum Due (Amount)** — The total value to be paid at the future date.