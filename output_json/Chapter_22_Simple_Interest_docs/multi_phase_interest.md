# Multi-Phase Interest

## Overview
This pattern involves calculating Simple Interest (S.I.) when the interest rate changes over different time intervals for the same principal. The central idea is to calculate the interest for each phase separately and sum them up to equal the total interest given.

---

## Recognition Clues
* **Keywords:** "first X years", "next Y years", "period beyond Z years", "rate increased by".
* **Given:** Total interest earned over a long period, and a breakdown of different rates for different time segments.
* **Asked:** The original principal (sum) borrowed or lent.
* **Time Check:** If the total time is 9 years and the phases are 2 and 3 years, the final phase is $9 - (2+3) = 4$ years.

---

## Key Formulas

### Total Simple Interest
$$
\text{Total S.I.} = \frac{P \times R_1 \times T_1}{100} + \frac{P \times R_2 \times T_2}{100} + \dots
$$

**Variables:**
- $P$ = Principal (the unknown sum)
- $R_n$ = Interest rate for phase $n$
- $T_n$ = Time duration for phase $n$

**When to use:** Whenever the interest rate changes at specific time intervals.

**Worked example:** For Q6, $P$ is unknown, $R_1=6, T_1=2$; $R_2=9, T_2=3$; $R_3=14, T_3=4$.
Total S.I. $= \frac{P}{100} \times [(6 \times 2) + (9 \times 3) + (14 \times 4)] = \frac{P}{100} \times [12 + 27 + 56] = \frac{95P}{100} = 11400$.

---

## Solution Framework

**Step 1: Identify the time segments** — Break the total time into the specific phases mentioned in the question.
**Step 2: Calculate the remaining time** — Subtract the sum of known phase durations from the total time to find the duration of the final phase.
**Step 3: Set up the equation** — Express total interest as the sum of $(P \times R \times T)/100$ for each phase.
**Step 4: Factor out P** — Simplify the equation by taking $P/100$ as a common factor to solve for $P$ quickly.

---

## Shortcut Tricks

* **Trick:** Use the "Effective Rate" method: $P \times (\frac{R_1T_1 + R_2T_2 + \dots}{100}) = \text{Total Interest}$.
* **Why it works:** It avoids writing the fraction $100$ repeatedly and simplifies the arithmetic.
* **When to use:** When the principal $P$ is constant across all phases.
* **Example:** In Q35, $P \times (\frac{8 \times 4 + 10 \times 6 + 12 \times 5}{100}) = 12160 \Rightarrow P \times (\frac{32+60+60}{100}) = 12160 \Rightarrow P \times 1.52 = 12160$.

---

## Common Mistakes

* **Mistake:** Miscalculating the final time phase.
    * **Why it happens:** Forgetting to subtract previous years from the total time.
    * **Fix:** Always verify: $\sum T_n = \text{Total Time}$.
* **Mistake:** Adding interest rates instead of calculating interest for each phase.
    * **Why it happens:** Confusing "rate" with "interest".
    * **Fix:** Always multiply $R \times T$ for each phase before adding.
* **Mistake:** Assuming the principal changes when it doesn't.
    * **Why it happens:** Misreading questions like Q38 where the principal *does* change.
    * **Fix:** Check if the question mentions "principal is trebled/doubled" mid-term.

---

## Worked Example (Step-by-Step)

**Question:** Adam borrowed money at 6% p.a. for the first 2 years, 9% p.a. for the next 3 years, and 14% p.a. for the period beyond 5 years. Total interest at the end of 9 years is ₹11400. Find the sum.

**Solution:**
1. **Identify segments:** Phase 1: 2 yrs @ 6%; Phase 2: 3 yrs @ 9%.
2. **Remaining time:** Total 9 yrs. Remaining = $9 - (2+3) = 4$ yrs @ 14%.
3. **Equation:** $P \times (\frac{6 \times 2 + 9 \times 3 + 14 \times 4}{100}) = 11400$.
4. **Solve:** $P \times (\frac{12 + 27 + 56}{100}) = 11400 \Rightarrow P \times \frac{95}{100} = 11400$.
5. **Result:** $P = \frac{11400 \times 100}{95} = 12000$.

**Answer:** ₹12,000.

---

## Similar Patterns

**Variable Principal Pattern:** Distinguish by checking if the principal changes (e.g., "principal is trebled after 5 years"). If it changes, calculate interest for each block of time using the *new* principal value.

---

## Revision Summary

* **Key formula:** $\text{Total S.I.} = \sum \frac{P \times R_i \times T_i}{100}$.
* **Spot it by:** Different interest rates for different time periods.
* **First move:** Calculate the duration of each time phase.
* **Fastest method:** Sum the $(R \times T)$ products first, then divide by 100.
* **Biggest trap:** Forgetting to subtract previous years from the total time for the final phase.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the original principal: $S.I. = \frac{P \times R \times T}{100}$.
* **Algebraic Equation Solving** — Isolating a variable $P$ in a linear equation.

### Formulas You Must Know First
$$
S.I. = \frac{P \times R \times T}{100}
$$
**What it means:** The standard formula for interest over a single period.

### Terms Used In This Pattern
* **p.c.p.a.** — Per cent per annum (annual interest rate).
* **Principal** — The original sum of money borrowed.