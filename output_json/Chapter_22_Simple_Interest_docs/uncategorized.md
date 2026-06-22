# Simple Interest: Variations and Relationships

## Overview
This pattern covers Simple Interest (S.I.) problems where the principal is often unknown or the relationship between interest, time, and rate is tested through ratios or compounding-like logic. The central idea is that $S.I. = \frac{P \times R \times T}{100}$ and that $S.I.$ is directly proportional to $T$ and $R$ when $P$ is constant.

---

## Recognition Clues
* **"Becomes n times of itself":** Look for phrases like "becomes three times" or "becomes double."
* **"Ratio of interest":** Look for questions asking for the ratio of interest over different time periods.
* **"Effective rate":** Look for "interest calculated every six months" or "includes interest in principal."
* **"Data Inadequate":** If the principal ($P$) is missing and cannot be canceled out, the answer is often "Data Inadequate."
* **"Geometric Mean":** Look for a chain of interest: $y$ is interest on $x$, $z$ is interest on $y$.

---

## Key Formulas

### [Simple Interest Relationship]
$$
\frac{S.I._1}{S.I._2} = \frac{T_1}{T_2} \quad (\text{if } P, R \text{ are constant})
$$
**Variables:** $S.I.$ = Simple Interest, $T$ = Time.
**When to use:** Comparing interest earned over different time periods for the same principal and rate.
**Worked example:** For $T_1=6$ and $T_2=9$, ratio is $\frac{6}{9} = 2:3$.

### [Geometric Mean Property]
$$
y^2 = xz
$$
**Variables:** $x$ = Principal, $y$ = S.I. on $x$, $z$ = S.I. on $y$ (for same $T, R$).
**When to use:** When interest is calculated on the previous interest.
**Worked example:** If $x=100, y=10$, then $z = \frac{10^2}{100} = 1$.

---

## Solution Framework

1. **Define Variables:** Assign $P$ for principal, $R$ for rate, and $T$ for time.
2. **Express Interest:** Write $S.I.$ in terms of $P$ (e.g., if amount is $3P$, $S.I. = 2P$).
3. **Set up Equation:** Use $S.I. = \frac{P \times R \times T}{100}$ to isolate the unknown.
4. **Check for Cancellation:** If $P$ appears on both sides, cancel it; if it remains, check if the question provides enough data.
5. **Solve for Target:** Calculate the final required value (Time, Rate, or Ratio).

---

## Shortcut Tricks

* **Trick:** For "becomes $n$ times in $T$ years," the interest is $(n-1)P$.
* **Why it works:** Amount = $P + S.I. = nP \implies S.I. = (n-1)P$.
* **When to use:** Any question asking for time to reach a certain multiple of the principal.
* **Example:** Becomes 3 times in 20 years $\implies 2P$ interest in 20 years. To become double ($P$ interest), it takes $20 \times \frac{1}{2} = 10$ years.

---

## Common Mistakes

* **Mistake:** Using Amount instead of Interest in the $S.I.$ formula.
* **Fix:** Always subtract $P$ from the Amount to get $S.I.$ ($S.I. = A - P$).
* **Mistake:** Assuming $P$ can be found when it cancels out.
* **Fix:** If $P$ cancels out, the answer is independent of $P$; if it doesn't, check if $P$ is provided.
* **Mistake:** Calculating 10% annual rate as 10% for 6 months.
* **Fix:** Divide the annual rate by the number of periods (e.g., $10\% / 2 = 5\%$ for 6 months).

---

## Worked Example (Step-by-Step)

**Question:** A certain sum becomes three times of itself in 20 years at simple interest. In how many years does it become double of itself?

**Solution:**
1. **Define:** Let $P$ be the principal.
2. **Express Interest:** For 3 times, $A = 3P$, so $S.I. = 3P - P = 2P$.
3. **Find Rate:** $2P = \frac{P \times R \times 20}{100} \implies 2 = \frac{R}{5} \implies R = 10\%$.
4. **Solve for Target:** For double, $A = 2P$, so $S.I. = P$.
5. **Calculate Time:** $P = \frac{P \times 10 \times T}{100} \implies 1 = \frac{T}{10} \implies T = 10$ years.

**Answer:** 10 years.

---

## Similar Patterns
**Compound Interest:** Distinguished by the phrase "compounded annually/half-yearly" vs "simple interest." In S.I., interest is only on the original principal; in C.I., interest is on the accumulated amount.

---

## Revision Summary
* **Key formula:** $S.I. = \frac{P \times R \times T}{100}$.
* **Spot it by:** "Becomes $n$ times" or "Ratio of interest."
* **First move:** Convert "Amount" to "Interest" by subtracting $P$.
* **Fastest method:** Use proportionality ($S.I. \propto T$) for ratio questions.
* **Biggest trap:** Forgetting to subtract $P$ from the total amount.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Simple Interest** — Interest calculated only on the original principal.
* **Proportionality** — If $A = k \times B$, then $A$ is directly proportional to $B$.

### Formulas You Must Know First
$$
A = P + S.I.
$$
**What it means:** The total amount is the sum of the principal and the interest earned.

### Terms Used In This Pattern
* **Principal ($P$)** — The initial sum of money.
* **Rate ($R$)** — The percentage of principal paid as interest per year.
* **Time ($T$)** — The duration the money is invested.