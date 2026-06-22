# Split Investment

## Overview
This pattern involves a single total sum or capital divided into two or more parts, each invested at different interest rates or for different terms. The central idea is to express each part in terms of a single variable (e.g., $x$ and $Total-x$) and equate the sum of the individual interests to the given total interest.

---

## Recognition Clues
* **Keywords:** "divided into two parts," "lent out at," "invested in two different schemes," "remainder at."
* **Given:** Total principal, different interest rates for each part, and the total annual income (interest).
* **Asked:** The specific amount invested in each part or the total capital.
* **Time Pressure Tip:** If you see a total amount split into two rates, immediately set up the equation: $Interest_1 + Interest_2 = Total Interest$.

---

## Key Formulas

### Simple Interest (S.I.)
$$
\text{S.I.} = \frac{P \times R \times T}{100}
$$

**Variables:**
- $P$ = Principal (the amount invested)
- $R$ = Rate of interest per annum
- $T$ = Time in years

**When to use:** To calculate the interest earned on any individual part of the split investment.

**Worked example:** For ₹ 650 at 8% for 1 year: $\frac{650 \times 8 \times 1}{100} = 52$.

---

## Solution Framework

1. **Assign Variables:** Assign $x$ to the first part and $(Total - x)$ to the second part.
2. **Set up Equation:** Write the sum of interests for all parts equal to the total interest given.
3. **Clear Denominators:** Multiply the entire equation by 100 to eliminate fractions.
4. **Solve for $x$:** Isolate $x$ to find the first principal.
5. **Find Remaining Parts:** Subtract $x$ from the total to find the second principal.

---

## Shortcut Tricks

* **Trick:** Use the "Alligation" method if you know the overall average rate of interest.
* **Why it works:** It balances the deviation of individual rates from the mean rate to find the ratio of the two principals.
* **When to use:** When the total interest and total principal are given, allowing you to calculate an overall percentage rate.
* **Example:** If ₹ 1550 earns ₹ 106, the average rate is $\frac{106}{1550} \times 100 \approx 6.84\%$. Use the difference between 8%, 6%, and 6.84% to find the ratio of parts.

---

## Common Mistakes

* **Mistake:** Forgetting to subtract the first part from the total to find the second part.
    * **Fix:** Always write $P_2 = Total - P_1$ before starting the calculation.
* **Mistake:** Miscalculating the remainder fraction (e.g., in Q19).
    * **Fix:** Always sum the known fractions first and subtract from 1: $1 - (\frac{1}{3} + \frac{1}{4}) = \frac{5}{12}$.
* **Mistake:** Arithmetic errors when clearing the denominator.
    * **Fix:** Multiply every single term in the equation by 100 before simplifying.

---

## Worked Example (Step-by-Step)

**Question:** A sum of ₹ 1550 is lent out into two parts, one at 8% and another one at 6%. If the total annual income is ₹ 106, find the money lent at each rate.

**Solution:**
1. **Assign Variables:** Let the sum at 8% be $x$. Then the sum at 6% is $(1550 - x)$.
2. **Set up Equation:** $\frac{x \times 8 \times 1}{100} + \frac{(1550 - x) \times 6 \times 1}{100} = 106$.
3. **Clear Denominators:** $8x + 6(1550 - x) = 10600$.
4. **Solve for $x$:** $8x + 9300 - 6x = 10600 \Rightarrow 2x = 1300 \Rightarrow x = 650$.
5. **Find Remaining:** Part 1 = ₹ 650; Part 2 = $1550 - 650 = 900$.

**Answer:** ₹ 650 at 8% and ₹ 900 at 6%.

---

## Similar Patterns
**Weighted Average/Mixture Problems:** Distinguish by checking if the question asks for a "final concentration" or "final rate" (Mixture) versus finding the "individual principal amounts" (Split Investment).

---

## Revision Summary
* **Key formula:** $S.I. = \frac{P \times R \times T}{100}$.
* **Spot it by:** Total sum split into parts with different rates.
* **First move:** Assign $x$ and $(Total - x)$ to the parts.
* **Fastest method:** Algebraic equation or Alligation if average rate is known.
* **Biggest trap:** Forgetting to subtract the first part from the total.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Linear Equations** — Solving equations with one variable $x$.
* **Fractions** — Adding and subtracting fractions with different denominators.

### Formulas You Must Know First
$$
\text{S.I.} = \frac{P \times R \times T}{100}
$$
**What it means:** The standard formula for calculating interest on a principal.

### Terms Used In This Pattern
* **Principal ($P$):** The original sum of money invested or lent.
* **Rate ($R$):** The percentage of the principal paid as interest per year.
* **Annual Income:** The total interest earned in one year ($T=1$).