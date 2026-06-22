# Instalment Debt

## Overview
This pattern involves clearing a debt through a series of periodic payments (instalments) where interest is calculated on the remaining balance or the time remaining for each instalment. The central idea is that the total debt equals the sum of all instalments plus the interest accrued on each instalment from the time it is paid until the end of the term.

---

## Recognition Clues
* **Keywords:** "Annual instalment," "discharge a debt," "payable in X months," "equal instalments."
* **Given:** Total debt amount, time period, and interest rate.
* **Asked:** The value of each equal instalment or the rate of interest.
* **Clue:** Look for a fixed total amount being paid off in multiple parts over time.

---

## Key Formulas

### [Instalment Calculation]
$$
\text{Total Debt} = \sum (\text{Instalment} + \text{Interest on that instalment})
$$

**Variables:**
- $x$ = value of each equal instalment
- $R$ = rate of interest
- $T$ = time remaining for a specific instalment until the end of the term

**When to use:** When you need to find the value of an equal instalment to clear a debt.

**Worked example:** For a debt of ₹ 848 in 4 years at 4% interest:
$x + (x + \frac{x \cdot 4 \cdot 1}{100}) + (x + \frac{x \cdot 4 \cdot 2}{100}) + (x + \frac{x \cdot 4 \cdot 3}{100}) = 848$.

---

## Solution Framework

**Step 1: Define the instalment as $x$.** This creates a single variable to solve for.
**Step 2: Calculate the time remaining for each instalment.** Determine how long each payment "sits" before the final debt due date.
**Step 3: Express each instalment as $(x + \text{Interest})$.** Interest is calculated as $\frac{x \cdot R \cdot T}{100}$ for each specific $T$.
**Step 4: Sum all expressions and equate to the total debt.** This forms a linear equation.
**Step 5: Solve for $x$.** Isolate the variable to find the instalment value.

---

## Shortcut Tricks

* **Trick:** For equal annual instalments, use the sum of the series: $\text{Debt} = nx + \frac{xR}{100} \times \frac{n(n-1)}{2}$.
* **Why it works:** It simplifies the sum of interest calculations into an arithmetic progression.
* **When to use:** When the number of instalments ($n$) is large.
* **Example:** For $n=3, R=12, \text{Debt}=1092$: $1092 = 3x + \frac{x \cdot 12}{100} \cdot \frac{3(2)}{2} \Rightarrow 1092 = 3x + 0.36x \Rightarrow 3.36x = 1092 \Rightarrow x = 325$.

---

## Common Mistakes

* **Mistake:** Calculating interest on the full debt for the entire duration.
    * **Fix:** Interest is only calculated on the instalment amount for the time it remains unpaid.
* **Mistake:** Forgetting the last instalment earns zero interest.
    * **Fix:** The final payment is made at the end of the term; it earns no interest.
* **Mistake:** Mixing up months and years in the rate formula.
    * **Fix:** Always ensure $T$ is in years (e.g., 10 months = $\frac{10}{12}$ years).

---

## Worked Example (Step-by-Step)

**Question:** What annual instalment will discharge a debt of ₹ 1092 due in 3 years at 12% simple interest?

**Solution:**
1. **Define $x$:** Let each instalment be $x$.
2. **Time remaining:** 1st instalment (2 years), 2nd (1 year), 3rd (0 years).
3. **Express:** 
   - 1st: $x + \frac{x \cdot 12 \cdot 2}{100} = 1.24x$
   - 2nd: $x + \frac{x \cdot 12 \cdot 1}{100} = 1.12x$
   - 3rd: $x$
4. **Sum:** $1.24x + 1.12x + x = 3.36x$.
5. **Solve:** $3.36x = 1092 \Rightarrow x = \frac{1092}{3.36} = 325$.

**Answer:** ₹ 325.

---

## Similar Patterns
**Simple Interest (General):** Distinguished by a single lump sum repayment at the end of the term, whereas Instalment Debt involves multiple partial payments.

---

## Revision Summary
* **Key formula:** $\text{Total Debt} = \sum (\text{Instalment} + \text{Interest})$.
* **Spot it by:** "Equal instalments" and "discharge a debt."
* **First move:** Assign $x$ to the instalment and calculate interest for each payment's duration.
* **Fastest method:** Use the AP sum formula: $\text{Debt} = nx + \frac{xR}{100} \cdot \frac{n(n-1)}{2}$.
* **Biggest trap:** Assuming the last instalment earns interest.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the principal amount: $SI = \frac{P \cdot R \cdot T}{100}$.
* **Arithmetic Progression (AP)** — A sequence of numbers where the difference between consecutive terms is constant.

### Formulas You Must Know First
* **Amount** = $P + SI$.
* **Time Conversion** — If time is in months, divide by 12 to get years.

### Terms Used In This Pattern
* **Instalment** — A fixed portion of a debt paid at regular intervals.
* **Discharge a debt** — To pay off the total amount owed completely.