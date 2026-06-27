# Sum and Rate Calculation

## Overview
This pattern involves finding the face value (Sum) of a bill and the interest rate when given Banker's Discount (B.D.) and True Discount (T.D.). The central idea is that B.D. is simple interest on the Sum, while T.D. is simple interest on the Present Worth (P.W.).

---

## Recognition Clues
* **Keywords:** "Banker's discount," "True discount," "Due hence," "Rate percent," "Sum of money."
* **Given:** B.D. and T.D. values for a specific time, or B.D. and rate/time.
* **Asked:** The original sum (face value) or the rate percent.
* **Time:** Always look for a time period (months or years) provided in the question.

---

## Key Formulas

### [Sum Calculation]
$$
\text{Sum} = \frac{\text{B.D.} \times \text{T.D.}}{\text{B.D.} - \text{T.D.}}
$$
**Variables:** B.D. = Banker's Discount, T.D. = True Discount.
**When to use:** When both B.D. and T.D. are provided for the same sum and time.
**Worked example:** Given B.D. = 120, T.D. = 110. Sum = $(120 \times 110) / (120 - 110) = 13200 / 10 = 1320$.

### [Rate Calculation]
$$
\text{Rate} = \frac{100 \times \text{B.D.}}{\text{Sum} \times \text{Time}}
$$
**Variables:** B.D. = Banker's Discount, Sum = Face value, Time = Years.
**When to use:** To find the annual interest rate after finding the Sum.
**Worked example:** B.D. = 120, Sum = 1320, Time = 8 months ($2/3$ year). Rate = $(100 \times 120) / (1320 \times 2/3) = 13\frac{7}{11}\%$.

---

## Solution Framework
1. **Normalize Time:** Convert all time periods into years (e.g., 8 months = $8/12 = 2/3$ year).
2. **Find Sum:** Use the formula $\text{Sum} = (\text{B.D.} \times \text{T.D.}) / (\text{B.D.} - \text{T.D.})$ if both discounts are given.
3. **Adjust B.D. (if needed):** If B.D. is given for a different time than T.D., scale the B.D. proportionally to match the time period.
4. **Calculate Rate:** Use the Simple Interest formula $\text{B.D.} = (\text{Sum} \times \text{Rate} \times \text{Time}) / 100$ to solve for Rate.

---

## Shortcut Tricks
* **Trick:** If a man deducts $x\%$ of the bill amount, the money he receives is $(100-x)\%$.
* **Why it works:** The deduction is effectively the interest earned on the money actually lent.
* **When to use:** When the question states a percentage of the bill is deducted as discount.
* **Example:** Bill = 100, Deduction = 10%. Money received = 90. Interest = 10 on 90 for the given time.

---

## Common Mistakes
* **Mistake:** Using months directly in the formula. **Fix:** Always convert months to years by dividing by 12.
* **Mistake:** Confusing B.D. with T.D. **Fix:** Remember B.D. is always larger than T.D. for the same sum and time.
* **Mistake:** Calculating interest on the discounted value instead of the face value for B.D. **Fix:** B.D. is always calculated on the face value (Sum).

---

## Worked Example (Step-by-Step)

**Question:** The banker’s discount and the true discount on a sum of money due 8 months hence are ₹ 120 and ₹ 110 respectively. Find the sum and the rate percent.

**Solution:**
1. **Find Sum:** Using the formula $\text{Sum} = (120 \times 110) / (120 - 110) = 13200 / 10 = 1320$.
2. **Convert Time:** 8 months = $8/12 = 2/3$ year.
3. **Calculate Rate:** $120 = (1320 \times \text{Rate} \times 2/3) / 100$.
4. **Solve:** $120 = (880 \times \text{Rate}) / 100 \Rightarrow 120 = 8.8 \times \text{Rate} \Rightarrow \text{Rate} = 120 / 8.8 = 13\frac{7}{11}\%$.

**Answer:** Sum = ₹ 1320, Rate = $13\frac{7}{11}\%$.

---

## Similar Patterns
* **Simple Interest:** Distinguish by the presence of "Banker's Discount" or "True Discount" terminology; standard S.I. problems do not involve these terms.

---

## Revision Summary
* **Key formula:** $\text{Sum} = (\text{B.D.} \times \text{T.D.}) / (\text{B.D.} - \text{T.D.})$
* **Spot it by:** Presence of "Banker's Discount" and "True Discount" in the same problem.
* **First move:** Convert all time units into years.
* **Fastest method:** Use the Sum formula first, then the S.I. formula for the rate.
* **Biggest trap:** Forgetting to convert months to years.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest (S.I.)** — Interest calculated only on the principal amount: $\text{S.I.} = (P \times R \times T) / 100$.
* **Banker's Discount (B.D.)** — Simple interest on the face value of the bill for the unexpired time.
* **True Discount (T.D.)** — Simple interest on the Present Worth (P.W.) for the unexpired time.

### Formulas You Must Know First
$$
\text{S.I.} = \frac{P \times R \times T}{100}
$$
**What it means:** The standard formula for calculating interest over time.

### Terms Used In This Pattern
* **Face Value (Sum)** — The total amount written on the bill.
* **Present Worth (P.W.)** — The amount that, if invested at the given rate, would equal the face value at the due date.