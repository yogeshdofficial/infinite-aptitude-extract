# Compound Interest — Chapter Overview

## What This Chapter Is About

Compound Interest deals with the growth of money where interest is earned not just on the original principal, but also on the accumulated interest from previous periods. The central relationship is the "compounding effect," where the total amount grows exponentially over time rather than linearly. This chapter covers calculating final amounts, determining interest earned, finding missing variables like time or rate, and handling variations in compounding frequency and installment payments.

---

## Core Concepts

**[The Compounding Cycle]** — This is the fundamental mechanism where interest is calculated at the end of a fixed period (e.g., annually, half-yearly) and added to the principal. For the next period, this new total becomes the base for calculating interest, meaning your money "earns interest on interest." For example, if you invest ₹100 at 10% for two years, you earn ₹10 in the first year, but in the second year, you earn 10% on ₹110, not just the original ₹100.

**[Compounding Frequency]** — Interest is not always calculated once a year; it can be calculated more frequently, such as every six months (half-yearly) or every three months (quarterly). When the frequency increases, the interest is calculated more often, which increases the total amount earned, even if the annual rate remains the same.

**[Principal vs. Amount]** — The Principal ($P$) is the initial sum of money borrowed or invested, while the Amount ($A$) is the final sum after the interest has been added. The Compound Interest ($C.I.$) is simply the difference between the two: $C.I. = A - P$.

**[Time Sensitivity]** — Because interest is calculated based on the duration the money is held, time must always be expressed in the same units as the compounding frequency. If a problem specifies a rate "per annum" but asks for "half-yearly" compounding, you must adjust both the rate (divide by 2) and the time (multiply by 2) to match the compounding period.

---

## Key Terms Glossary

**Principal ($P$)** — The original sum of money lent or invested at the start of the period.

**Amount ($A$)** — The total value of the investment or loan after interest has been added to the principal at the end of the term.

**Rate ($R$)** — The percentage of the principal charged or earned as interest per unit of time, usually expressed as "per annum" (per year).

**Time ($n$)** — The duration for which the money is invested or borrowed, typically measured in years.

**Compounding** — The process of adding earned interest back into the principal so that it earns interest in the next period.

**Present Worth** — The current value of a future sum of money, calculated by discounting the future amount back to the present using the interest rate.

---

## Pattern Map

**Compound Interest Calculation** (11 questions) — The baseline pattern where all variables ($P, R, n$) are provided to find the final amount or interest.

**Missing Variable** (15 questions) — The inverse of the baseline; you are given the interest or amount and must solve for the unknown $P, R,$ or $n$.

**Growth and Multiples** (6 questions) — Focuses on the ratio-based growth of money over specific time intervals (e.g., "money doubles in 5 years").

**Interest Comparison** (28 questions) — Requires calculating and comparing interest across different scenarios, such as Simple Interest vs. Compound Interest or different rates/times.

**Complex Scenarios** (19 questions) — Involves non-standard time frames (fractions of years) or varying interest rates for different years.

**Installment Payments** (8 questions) — Deals with paying off a debt in equal periodic installments where each payment includes both principal and interest.

**Uncategorized** (1 questions) — Miscellaneous problems that do not fit the standard structural categories.

---

## Core Formulas

### Annual Compounding
$$
A = P \left(1 + \frac{R}{100}\right)^n
$$
**Variables:** $A$ = Amount, $P$ = Principal, $R$ = Rate, $n$ = Time in years.
**When to use:** When interest is calculated once per year.
**Key insight:** The exponent $n$ represents the number of times interest is applied.
**Worked example:** $P=100, R=10\%, n=2 \implies A = 100(1.1)^2 = 121$.

### Periodic Compounding (Half-Yearly/Quarterly)
$$
A = P \left(1 + \frac{R/k}{100}\right)^{nk}
$$
**Variables:** $k$ = number of times interest is compounded per year ($k=2$ for half-yearly, $k=4$ for quarterly).
**When to use:** When the compounding frequency is more than once a year.
**Key insight:** Always divide the rate by $k$ and multiply the time by $k$ before calculating.
**Worked example:** $R=20\%$ p.a., half-yearly $\implies$ use $10\%$ rate and $2n$ periods.

### Varying Rates
$$
A = P \left(1 + \frac{R_1}{100}\right) \left(1 + \frac{R_2}{100}\right) \left(1 + \frac{R_3}{100}\right)
$$
**Variables:** $R_1, R_2, R_3$ = different interest rates for consecutive years.
**When to use:** When the interest rate changes year-over-year.
**Key insight:** Each bracket represents the growth factor for that specific year.
**Worked example:** $10\%$ then $20\% \implies A = P(1.1)(1.2) = 1.32P$.

### Present Worth
$$
P = \frac{A}{(1 + R/100)^n}
$$
**Variables:** $P$ = Present Worth, $A$ = Future Amount, $R$ = Rate, $n$ = Time.
**When to use:** When you need to find the initial investment required to reach a specific future goal.
**Key insight:** This is simply the Compound Interest formula rearranged to solve for $P$.
**Worked example:** To get $121$ in 2 years at $10\%$, $P = 121 / (1.1)^2 = 100$.

---

## Suggested Study Order

1. **Compound Interest Calculation** — Start here to master the basic formula and the mechanics of compounding.
2. **Missing Variable** — Study next to learn how to manipulate the formula algebraically when $P, R,$ or $n$ is unknown.
3. **Complex Scenarios** — Move here to handle fractional time and varying rates, which are just extensions of the base formula.
4. **Interest Comparison** — Tackle this to apply your calculation skills to logical comparisons between different financial products.
5. **Growth and Multiples** — Study this for shortcut methods involving ratios and powers.
6. **Installment Payments** — Save for last as it requires a solid grasp of how interest accumulates over multiple payment stages.

---

## Chapter-Wide Traps

**Rate-Time Mismatch:** Using the annual rate for a half-yearly or quarterly calculation without adjusting the rate and time variables → Always divide the rate by the frequency and multiply the time by the frequency.

**Simple vs. Compound Confusion:** Applying the simple interest formula ($SI = \frac{PRT}{100}$) to compound interest problems → Remember that compound interest requires exponential growth, not linear.

**Rounding Errors:** Rounding off intermediate steps in multi-year calculations → Keep fractions or decimals as precise as possible until the final step to avoid significant errors.