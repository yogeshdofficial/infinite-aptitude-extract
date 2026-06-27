# True Discount — Chapter Overview

## What This Chapter Is About

This chapter deals with the financial mathematics of settling debts before they are officially due. The central relationship revolves around the difference between the "face value" of a debt (the amount due in the future) and its "present value" (the amount that, if invested today at a specific interest rate, would grow to equal that future debt). You will learn to calculate how much a creditor should accept today to settle a future obligation, and how this differs from standard simple interest calculations.

---

## Core Concepts

**[The Time Value of Money]** — Money available today is worth more than the same amount in the future because today's money can be invested to earn interest. For example, if you have ₹100 today and the interest rate is 10%, you will have ₹110 in a year; therefore, ₹100 is the "present" value of ₹110 due one year from now.

**[Present Worth (P.W.)]** — This is the principal amount that, when invested at a given rate of interest for a specific time, accumulates to the total sum due. It represents the "true" value of a future payment if you were to pay it off right now.

**[True Discount (T.D.)]** — This is the interest earned on the Present Worth over the given time period. It is the difference between the total amount due in the future and the amount you would need to pay today to settle that debt.

**[Sum Due (Amount)]** — This is the total value of the debt at the time of maturity. It is the sum of the Present Worth and the True Discount.

**[Interest vs. Discount]** — Simple Interest (S.I.) is calculated on the principal (the money you start with), whereas True Discount is calculated on the Present Worth (the money that *becomes* the final amount). Because of this, the True Discount is always slightly less than the Simple Interest on the same sum for the same time and rate.

---

## Key Terms Glossary

**Sum Due (Amount)** — The total value to be paid at a future date.

**Present Worth (P.W.)** — The current value of a future sum; the amount that would grow to the "Sum Due" if invested today.

**True Discount (T.D.)** — The difference between the Sum Due and the Present Worth.

**Rate (R)** — The annual percentage rate of interest used to calculate the growth of money over time.

**Time (T)** — The duration in years until the debt becomes due.

---

## Pattern Map

**[Present Worth]** (5 questions) — The foundational pattern where you are given the Amount, Rate, and Time and must calculate the P.W.

**[Discount Proportionality]** (3 questions) — Focuses on the relationship where T.D. is directly proportional to the P.W. and time.

**[Rate Calculation]** (3 questions) — Requires rearranging the standard formulas to solve for the interest rate when the T.D. and other variables are known.

**[Interest Comparison]** (5 questions) — Involves comparing Simple Interest (S.I.) and True Discount (T.D.) to find the sum or rate.

**[Equivalent Offers]** (8 questions) — The most complex pattern; involves balancing two different payment scenarios (e.g., paying half now vs. later) to find the total bill amount.

**[Missing Variables]** (2 questions) — General algebraic problems where one of the primary variables (P.W., T.D., Rate, or Time) is missing and must be derived from the others.

---

## Core Formulas

### Present Worth (P.W.)
$$
P.W. = \frac{100 \times \text{Amount}}{100 + (R \times T)}
$$
**Variables:** $R$ = Rate %, $T$ = Time in years.
**When to use:** When you need to find the current value of a future debt.
**Key insight:** The denominator $100 + (R \times T)$ accounts for the interest that would have been earned on the P.W.
**Worked example:** If Amount = ₹156, R = 14%, T = 4 years, $P.W. = \frac{100 \times 156}{100 + (14 \times 4)} = \frac{15600}{156} = ₹100$.

### True Discount (T.D.)
$$
T.D. = \frac{\text{Amount} \times R \times T}{100 + (R \times T)}
$$
**Variables:** $R$ = Rate %, $T$ = Time in years.
**When to use:** When you need to find the discount amount directly from the future sum.
**Key insight:** This is essentially the interest on the P.W., but expressed in terms of the final Amount.
**Worked example:** If Amount = ₹156, R = 14%, T = 4 years, $T.D. = \frac{156 \times 14 \times 4}{100 + 56} = \frac{8736}{156} = ₹56$.

### Relationship between S.I. and T.D.
$$
\text{Sum} = \frac{S.I. \times T.D.}{S.I. - T.D.}
$$
**Variables:** $S.I.$ = Simple Interest, $T.D.$ = True Discount.
**When to use:** When you are given both the S.I. and T.D. for the same sum and time.
**Key insight:** The difference between S.I. and T.D. is equal to the interest on the T.D. itself.

---

## Suggested Study Order

1. **Present Worth** — Start here to master the basic relationship between future and present value.
2. **Discount Proportionality** — Study next to understand how changes in time or rate affect the discount.
3. **Rate Calculation** — Move here to practice algebraic manipulation of the core formulas.
4. **Missing Variables** — Use this to solidify your ability to solve for any unknown in the P.W. equation.
5. **Interest Comparison** — Study this to understand the conceptual difference between S.I. and T.D.
6. **Equivalent Offers** — Tackle this last as it requires applying all previous concepts to multi-step scenarios.

---

## Chapter-Wide Traps

**Time Unit Mismatch:** Students often forget to convert months into years (e.g., 6 months = 0.5 years) before plugging into the formula → Always check that $T$ is in years.

**Confusing S.I. with T.D.:** Using the Simple Interest formula ($P \times R \times T / 100$) when the question asks for True Discount → Remember that T.D. is calculated on the P.W., not the final Amount.

**Ignoring the Denominator:** Forgetting the $(100 + RT)$ part of the formula and using only $100$ → Always remember that the base for True Discount is the Present Worth, which is smaller than the final Amount.