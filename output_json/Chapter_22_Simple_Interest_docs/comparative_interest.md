# Comparative Interest

## Overview
This pattern involves comparing two different Simple Interest (S.I.) scenarios for the same principal or comparing two different loans. The central idea is to set up an equation where the difference or equality between two interest expressions allows you to solve for the unknown variable (Principal, Time, or Rate).

---

## Recognition Clues
* **Keywords:** "is ₹ X less/more than", "is equal to", "in each case he had to pay".
* **Given:** Two sets of $(P, R, T)$ where one or more variables are shared or linked.
* **Asked:** Usually the Principal ($P$), Time ($T$), or Rate ($R$).
* **Structure:** Look for two distinct scenarios described in a single problem statement.

---

## Key Formulas

### Simple Interest Comparison
$$
\frac{P \times R_1 \times T_1}{100} \pm \text{Difference} = \frac{P \times R_2 \times T_2}{100}
$$

**Variables:**
- $P$ = Principal sum
- $R_1, R_2$ = Rates for scenario 1 and 2
- $T_1, T_2$ = Time periods for scenario 1 and 2

**When to use:** When the problem states one interest is a specific amount more or less than the other.

**Worked example:** Q13: $P$ is unknown, $R_1=12, T_1=2.5$; $R_2=10, T_2=3.5$. Difference = 40.
$\frac{P \times 10 \times 3.5}{100} - \frac{P \times 12 \times 2.5}{100} = 40 \Rightarrow \frac{35P - 30P}{100} = 40 \Rightarrow 5P = 4000 \Rightarrow P = 800$.

---

## Solution Framework

1. **Define Variables:** Assign $P$ to the principal and $T$ to the time if unknown.
2. **Express Interests:** Write the S.I. formula for both scenarios separately.
3. **Set Equation:** Use the relationship provided (e.g., $SI_2 - SI_1 = \text{Difference}$ or $SI_1 = SI_2$).
4. **Simplify:** Cancel common factors (like 100 in the denominator) to isolate the unknown.
5. **Solve:** Perform the final algebraic calculation to find the value.

---

## Shortcut Tricks

* **Trick:** If $P$ is the same, use $P \times \frac{|R_1T_1 - R_2T_2|}{100} = \text{Difference}$.
* **Why it works:** It factors out $P$ from the standard S.I. formula, reducing the number of operations.
* **When to use:** When the principal is identical in both scenarios.
* **Example:** Q63: $P \times \frac{|11 \times 3 - 11 \times 2.5|}{100} = 412.50 \Rightarrow P \times \frac{5.5}{100} = 412.50 \Rightarrow P = 7500$.

---

## Common Mistakes

* **Mistake:** Forgetting to convert months to years (e.g., 6 months = 0.5 years).
* **Why it happens:** Rushing the setup without checking units.
* **Fix:** Always ensure $T$ is in years before plugging into the formula.
* **Mistake:** Confusing "Amount" ($P + SI$) with "Interest" ($SI$).
* **Why it happens:** Misreading the question text.
* **Fix:** If the question mentions "repaid" or "cleared," it usually refers to the Amount.

---

## Worked Example (Step-by-Step)

**Question:** Simple interest on ₹ 500 for 4 years at 6.25% p.a. is equal to the simple interest on ₹ 400 at 5% p.a. for a certain period of time. Find the time.

**Solution:**
1. **Define:** $P_1=500, R_1=6.25, T_1=4$; $P_2=400, R_2=5, T_2=T$.
2. **Express:** $SI_1 = \frac{500 \times 6.25 \times 4}{100} = 125$.
3. **Set Equation:** $SI_2 = \frac{400 \times 5 \times T}{100} = 20T$. Since $SI_1 = SI_2$, then $125 = 20T$.
4. **Solve:** $T = \frac{125}{20} = 6.25$ years.

**Answer:** $6\frac{1}{4}$ years.

---

## Similar Patterns
**Installment/Amount Problems:** Distinguish by checking if the question mentions "Amount" (Principal + Interest) or just "Interest." If it says "Amount," you must add $P$ to your interest expression.

---

## Revision Summary
* **Key formula:** $SI = \frac{PRT}{100}$.
* **Spot it by:** Two scenarios with shared variables and a comparison (difference/equality).
* **First move:** Write the S.I. expression for both scenarios.
* **Fastest method:** Factor out $P$ and use the difference in $(R \times T)$ products.
* **Biggest trap:** Forgetting to convert months to years or confusing Interest with Amount.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the principal amount: $SI = \frac{PRT}{100}$.
* **Algebraic Manipulation** — Ability to solve linear equations with one variable.

### Formulas You Must Know First
* **Amount** — The total money returned: $A = P + SI = P(1 + \frac{RT}{100})$.

### Terms Used In This Pattern
* **Principal ($P$)** — The original sum of money borrowed or lent.
* **Rate ($R$)** — The percentage of the principal paid as interest per year.
* **Time ($T$)** — The duration for which the money is borrowed, in years.